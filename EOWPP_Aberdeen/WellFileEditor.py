# This program goes through the abr_ref.wel file
# and generates a new file with the Stress Periods annotated

AnnotatedLine = 6   # Variable initialized with the first line to be annotated. Zero-Indexed
Line = 0			# Current line within the read file
SP = 1				# Current Stress Period

# Open abr_ref.wel file
with open('abr_ref.wel', 'r') as read_f:
    # Prepare a new file to write to
    with open('Revised_abr.wel', 'w') as write_f:

        # Read the first line into a string variable
        StringRead = read_f.readline()

        # Loop through the entire file till an empty line is reached
        while len(StringRead) > 0:
            # Check if it's a line of interest
            if Line == AnnotatedLine:
                # Parse out the number of entries for this stress period
                # print(Line, ' ', StringRead, end='')
                ListRead = StringRead.split()
                # print(ListRead)
                SPNum = int(ListRead[0])
                # print(SPNum)

                # Append stress period annotation to string
                StringWrite = StringRead[:(len(StringRead)-1)] + 'SP' + str(SP) + StringRead[(len(StringRead)-1)]
                print(StringWrite, end='')
                SP += 1

                # Write new string to file
                write_f.write(StringWrite)

                # Update AnnotatedLine with the next stress period entry
                AnnotatedLine = AnnotatedLine + SPNum + 1
            else:
                write_f.write(StringRead)

            # Grab the next line
            StringRead = read_f.readline()
            Line += 1
