<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/mwvGVOnoseSXg8sQOA5ijapw2tOaDl9s5OkLi8nzKfLcOQWH3uFISEOLmqyX4PBZqBhaLczbfrv6DmlzG6f1xBx13apif5WxiMahsUwTP-ekGGJFbOLWPGHkVEMWvnaJgtcW5Mja96elrZl3pq4y-X870gHF3f0V4Jz9rPTCd2y9Y2mfcuwZ3xNTUmw55NYLc9BYEoQCYx1qz8RnuPuuG3aL7AM2POfl-0H4RMSQO4dZbUXxheXZWzQrNB-kwC31NpVfkboSU8aFt8kMZrEOWZe-5omCmO-xPQg0EXgGjHmAqi8gFTb2hlBedIy_9qulHHcRsdD7E5JWlmWt1pZhXw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.2K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 13:03:18</div>
<hr>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAxG7YVglpKQtz_qUrBsKIJd3nODp0ZJiY-DznNOM3kH6HbcPosYUQpEUNWUP1QcyCw0MgckB8YKn_v01wLTZA5SAB9zJNln0ZctPhRlY0Jj2M4A_Dd7SmRJ76ARYFVXN9X-_-BepEixR_2QfctgljAusRixVTWbuq0BhwpbV84wm_F_jQtUrOcPXkD2Bbgp5XDA_Ivf4jyL6bXppRviVhMsGO6NP59UVcBdqvIeraJlZhaTTrxD_hOXLrigsbnOr44RHmCZoH9stUZSxxYwEd76xN_63NqFpqbXXdwAyDjGBy9_zY_2D8W7MT29xP0DDH1TdVvxnNZmXTP5CKR1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GpTI1WWKVwYi7f1p3CfOJkneJhCqt1DHZIvfIhxInyi_ET7VkhYvNT-Tkm7TtUTXlfEkHtZlcwuPDbuq34sK0_A9whkOO81YC1eCq8y6Vq3aOfY-ABEpa5jOB7w1yxO1JV1WS7Nw-FNQ2R-bh4RE8djqfEmWy3HQa6sMikLaYfGgX9ZEw3_vJtvcM0SP5F1kTj_Kn52Xpv77AEALxTqfmeGOUYTs19Vmv03XxVYNSPaNfMNh5cTh0hBqhWoHkSmqtbFbDPrkzSliB3tKzsRyPAtJHJmVbLuJYEGTzI6yEKYc1auBz8RPkbo3VciEVuAAexCWFktj8uwu59RjTEXO4h13Lnr0hFlpIbZEBJ5pkrysRq-eH9xNRxnuH8PB9KsJav4oVLMGjf_8vH0toVtfQtyh0UZDowEHkrWUGypTSZvnh4hxIGwkfBfGkiV4Fhjv3yAi0dQ7z9l2I9bfGP6mq4FRbxvPmA__Whsm9kqKbWCOkYTzvbZibmccJytBwsT8xi8zhE7njkP2BredYWn6iZEBzEUdXbqZGxbroCN9-zV7sgLE5VT7EZXpYEne9PVl0HWZDnltMfSalSjcwNg5E6jrH-FG7pDvW22EQtKgfHlXy3smIQ99ZzabVVsKl0PfdS3UPafUDSfqVfOR_-v_CARrwaYn_WDlYolbXvRLUXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GpTI1WWKVwYi7f1p3CfOJkneJhCqt1DHZIvfIhxInyi_ET7VkhYvNT-Tkm7TtUTXlfEkHtZlcwuPDbuq34sK0_A9whkOO81YC1eCq8y6Vq3aOfY-ABEpa5jOB7w1yxO1JV1WS7Nw-FNQ2R-bh4RE8djqfEmWy3HQa6sMikLaYfGgX9ZEw3_vJtvcM0SP5F1kTj_Kn52Xpv77AEALxTqfmeGOUYTs19Vmv03XxVYNSPaNfMNh5cTh0hBqhWoHkSmqtbFbDPrkzSliB3tKzsRyPAtJHJmVbLuJYEGTzI6yEKYc1auBz8RPkbo3VciEVuAAexCWFktj8uwu59RjTEXO4h13Lnr0hFlpIbZEBJ5pkrysRq-eH9xNRxnuH8PB9KsJav4oVLMGjf_8vH0toVtfQtyh0UZDowEHkrWUGypTSZvnh4hxIGwkfBfGkiV4Fhjv3yAi0dQ7z9l2I9bfGP6mq4FRbxvPmA__Whsm9kqKbWCOkYTzvbZibmccJytBwsT8xi8zhE7njkP2BredYWn6iZEBzEUdXbqZGxbroCN9-zV7sgLE5VT7EZXpYEne9PVl0HWZDnltMfSalSjcwNg5E6jrH-FG7pDvW22EQtKgfHlXy3smIQ99ZzabVVsKl0PfdS3UPafUDSfqVfOR_-v_CARrwaYn_WDlYolbXvRLUXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRSN09u_Ej5XVX3CKul8QeIlXERflG7x6xPGrALRQwzdRTiT0Nb-uwg9FI-xKl8Dz2bY0wHnstXfIu64gdrxwKqHr3tagyduv72FarkYSTFbAovjjrZ8lpRG38O1id9NMLPIhcho25KcCxHeHpYyTcQE4i7C7nMMrpoGnQlfa_1GDhjrF4zL0BTxpB6ws0cR06-1t-Z5RYcBu6wivDhkD7DMxb2rlMs1Q90zDUKjZGRJumFxg8TE0DfpEcAvKPc3Whni5NLXxjN5k4xBrgbeFMZkuZbysKM95aLHHrxTh15aycmEQRJK4EfxNPrryk-Htp70lsztEfgF-zM1G28bsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان جمهوری اسلامی این روزها
برای عروسی در یمن شیرینی میدن،
۳ سال پیش برای عروسی
در غزه شیرینی میدادن،
پارسال برای جنوب لبنان!
عروسی‌هاتون و پیروزی‌هاتون پی در پی
✌🏼
۲ میلیون اهالی غزه سه ساله زیر چادر هستن
۶۰۰ هزار شیعه لبنانی ۵ ماهه
توی توالت‌ها و گاراژهای محله‌های مسیحی و سنی پناه گرفتن!  پیروزی‌هاتون پر تکرار!</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7_Iuhz4_0xcOrTUmDdDwxOY7thmSJX-6XcyY4-cDjXB5QUuf0jxh2I6hDyZmwLq565APgy4lh6mcQIf3yEyj8zQVvCmSTCxKwP3DD1AGfbdExQez8Uhepwap2xkERjzd-Bojxb9v7kz-_0JhIyjIDiaRvvTdOaPQvAXszzN_5Urs70ijOjPbjmtmvFGiEfctHzv1bvML-zLoTc7jwA5o-MiJu7lsPFNwNsJZwPAOCxEDPymx1DsHdqvDVZ-4xby7sHpjXYdycjuh8RzeM8ot1KFFRtRsE9BwEuSEWq3M7GrErXVkF0vGnCqwa5ns9w-yajNohrO8Hz_khZJYCZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP7x72Hy0Fa2XziovhkvqBKFUX2B4L5g1gbWJCIfiauaqmcRDdDcYgY7ppGPRC-fjxmAOABxurOqgEiS6F7sLGo5fyyVlUmmgaeN1kpEnTm6CnTlH3kysJQhftj6Dr7cXv2h5fdZQtdoO4kvSHkwKl_QKOdIYVRH99Pena8aEfvi7bO2b5G6yWrbsfkiOEVSyVbjptD5mLXjGfAlq2htAgHIbaCt-oKXZaPxTn6yR5Si3c_0AmUy0vbSRUllQez61xTJ0RBUJE4bZ1yVXXzkFr5Bp10JbWL4UHmwrtusz-gKLlk_M2jOOdQPy1Pyf2a93V7L5jiTR4v-NetzaUmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL5JuPtHA0SSfs6Y3rPmUOWQY9p4ntNG9RrSDYhYqTIWlswKD-2RL20jPTRYWsGFmcnXoZdHysxJ9thRkhfTmYtgCKA5iNhOWhEoHTe2BhGke_hEqGqdrYqtB6JKOzMLsF9fwI0t_8Cf9T33QWTIGScm4GFVaOgACex0fs40-J4LuXlHzjOXsvbr2OX7mVcnFjWgzydBEXdspB6AL2wUCY6VrcmQ9cUXY5qRJKA7RjKVT05HcE2ZdWYY4gJwVB2qgH290tHm72pIZYaflGHACwPokyDQCmccS-AnPDhPB-k_h-GDimmwICSKT-LZDGC9_Yx9u8VsHzV0oJ6IuCQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=v60g7xZEE0XZUxubpHqhzpVAtckGXigGGW7l2UJRxUL0rrRM2XpiyVOocur-WHBnyo1CLC84vWsJPxie6EVvVdtgkbCgADKSQORdLNDwmlaAHPag2HO__sv5KRrHAozTqvZDKCTFom0x00D8cVTv0rXbqN6tIAdbTbGXgqSDOGwmt9JC6B-17Kw2piiiC7AMtKitmd5VYJFyWH22ptJmg55ooPDsYyCHS07LUDnzX92pV05fbHaWWwBTjizUNN9ASug43Ih-WgrKXgXQDHoMZVGibutFVgfGyYfyEkrgkf-6PO01aEsp16DklxatyjU4wBUHfJl-7_Ou3uilzH8Aiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d6eaeb7a7.mp4?token=v60g7xZEE0XZUxubpHqhzpVAtckGXigGGW7l2UJRxUL0rrRM2XpiyVOocur-WHBnyo1CLC84vWsJPxie6EVvVdtgkbCgADKSQORdLNDwmlaAHPag2HO__sv5KRrHAozTqvZDKCTFom0x00D8cVTv0rXbqN6tIAdbTbGXgqSDOGwmt9JC6B-17Kw2piiiC7AMtKitmd5VYJFyWH22ptJmg55ooPDsYyCHS07LUDnzX92pV05fbHaWWwBTjizUNN9ASug43Ih-WgrKXgXQDHoMZVGibutFVgfGyYfyEkrgkf-6PO01aEsp16DklxatyjU4wBUHfJl-7_Ou3uilzH8Aiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه
مهم اینه دلت با خدا باشه!
علی علی!</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHx64jqVOQsibxvmxecEi9EBgNJbrBJc0iOFpUN1JTlqUrm9JAt2_l8JOLz-MbB5eSm_2s8JwdhETbilzNE8LY5OzDsbPqnKvgr7pbSHJBuHAdMeBt0u2pMLLLKfAlUPQJrVm6OlqlWq6y5QZunHRotrfTBiKbS5LZeWeLf2-j3GH6P0Dy_YhfVdbzQ1EWYWX8ovVXpuoODnN_y_DMOxDA7qXqnZYQ2K62QGK6VTOO1l-xTNVrAIYuH4uyUXcFLrtFZVtc3c5KJyxV8hzXQJciH1uZPtjtpIR_3UXEm60S3sklLvXHLvyoZl0gbvmAmiJhEHqSBZ1AhYZVv3C5--5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCaVVDxVmHS1FUmtJkJZ6to9MHN7K_b9rbR34Mq3lteMy2JJPLWyFJcFLQGAonURz0Qd21Ina666xXKk3DSMoI8XzgN_mecQ0N5jJU1kLoVgtHt1OtOmYF_1UQobeLEIN53FpMSNU3KmOrmqhkenxymRtJWo4ry5z7Wz6cRrCIKCd3Q1ysKlkyQQp1rCNUbdXfqVpkAr4bffNlPDHW7Vp8sMNJzooAHyQWu0v8jSvVAg5Ulv93lwfwrcPhtRjmNm7WkxKmtXuHLFJwLsl9UKI0ctiQu3F_XtpNt48UKLPu-XgNdLltmCOf9Va7Oq2t5krFR9rdJenKTxeMpNTd5zXDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCaVVDxVmHS1FUmtJkJZ6to9MHN7K_b9rbR34Mq3lteMy2JJPLWyFJcFLQGAonURz0Qd21Ina666xXKk3DSMoI8XzgN_mecQ0N5jJU1kLoVgtHt1OtOmYF_1UQobeLEIN53FpMSNU3KmOrmqhkenxymRtJWo4ry5z7Wz6cRrCIKCd3Q1ysKlkyQQp1rCNUbdXfqVpkAr4bffNlPDHW7Vp8sMNJzooAHyQWu0v8jSvVAg5Ulv93lwfwrcPhtRjmNm7WkxKmtXuHLFJwLsl9UKI0ctiQu3F_XtpNt48UKLPu-XgNdLltmCOf9Va7Oq2t5krFR9rdJenKTxeMpNTd5zXDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DZHeuYSAL2XdoWTHZ6gBa3x7SMFv_E_pqir4AC0n3ICbUyxrayxvZpwWCwFxlV0CBbwDZJRlF6yrY1MCThzykIymM-oV8DMq5iP-66OnCu9sbmxrbwlwUMHbTgA7g2JUDJPe2m0fjv2cxSnF5T2KukTbqhtj7qD-51UVumuZX5jKh5J8GoXB4-PveY9epC2PXzNZbFQs-UIUG5f5b5CMa5AjZ64VI2kwPsIM_SGbJH0kdO_hCkHicCQlZoZVdYLI1Bv0Ij77Fw68D_E7LUzqCejxfcs_x_gD7lUx8t1xTLc1dZuBG3ng6SkNSut2J2ShJy9peV77BcY-yF-ZgkPcdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DZHeuYSAL2XdoWTHZ6gBa3x7SMFv_E_pqir4AC0n3ICbUyxrayxvZpwWCwFxlV0CBbwDZJRlF6yrY1MCThzykIymM-oV8DMq5iP-66OnCu9sbmxrbwlwUMHbTgA7g2JUDJPe2m0fjv2cxSnF5T2KukTbqhtj7qD-51UVumuZX5jKh5J8GoXB4-PveY9epC2PXzNZbFQs-UIUG5f5b5CMa5AjZ64VI2kwPsIM_SGbJH0kdO_hCkHicCQlZoZVdYLI1Bv0Ij77Fw68D_E7LUzqCejxfcs_x_gD7lUx8t1xTLc1dZuBG3ng6SkNSut2J2ShJy9peV77BcY-yF-ZgkPcdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=f-5HyfA0RoQAUHfgpEjYrVfYKoj7fy85dDHLfcQvGy0Sh1VEXzeNoKU1lcxf33-LWbNj0pIzkqoU4IlQigQmSEaguRi6QvAK6I68jKVCM1MqklLdAn-jnYEgKGyb-IIsVQjYKHRBG5i2eLdbDwo49V4MsOXlHYMBczhb0ZncKHKe0KF3uvolLDkrPzUku486dWwMH2aLSb03XgRUjUJL1YP6Qz3kC_i5LGX9jEfpqyC3ceIB6ICqLJ600QGfjEKdReg6IwyJkg_X7gePOutAT7LsVKOtIKh5QUHs1BYY_tsIgHkwafwiyO68unQQJE7ThhR9d-uYlo87360-d8xksnYpbxMzKEH6BLdoFdq6n1jHQQpg0aWcvHrGAkrIf5LaBZCqCV72RiriEy7-r8kZyFRgXTiYBY9wB4WqzGAcUT-21bDJI2E2yW8a4yFDjvAug1vJRWXLWZNteLmKjQsBi5Bm2SpvQHP4MhEv5Izsbz2w3v6CjgMQTMkIBCVVcadZjcxmEVtPcGOJFnMNZkUqxqgd8NZmxYixpD1-2SOsZHdC3mewGqLiM4UfS_IJhEvnx7JyCskdyukz2gKCpy-NKrADL2ZuTCWT_GL_ywSuWESbUFbRFo0aB1zPUUnEMwjpB1c3l6u8y9acTJ5m6sOYJyKL-PQjqCPW95ICmn0AjqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=f-5HyfA0RoQAUHfgpEjYrVfYKoj7fy85dDHLfcQvGy0Sh1VEXzeNoKU1lcxf33-LWbNj0pIzkqoU4IlQigQmSEaguRi6QvAK6I68jKVCM1MqklLdAn-jnYEgKGyb-IIsVQjYKHRBG5i2eLdbDwo49V4MsOXlHYMBczhb0ZncKHKe0KF3uvolLDkrPzUku486dWwMH2aLSb03XgRUjUJL1YP6Qz3kC_i5LGX9jEfpqyC3ceIB6ICqLJ600QGfjEKdReg6IwyJkg_X7gePOutAT7LsVKOtIKh5QUHs1BYY_tsIgHkwafwiyO68unQQJE7ThhR9d-uYlo87360-d8xksnYpbxMzKEH6BLdoFdq6n1jHQQpg0aWcvHrGAkrIf5LaBZCqCV72RiriEy7-r8kZyFRgXTiYBY9wB4WqzGAcUT-21bDJI2E2yW8a4yFDjvAug1vJRWXLWZNteLmKjQsBi5Bm2SpvQHP4MhEv5Izsbz2w3v6CjgMQTMkIBCVVcadZjcxmEVtPcGOJFnMNZkUqxqgd8NZmxYixpD1-2SOsZHdC3mewGqLiM4UfS_IJhEvnx7JyCskdyukz2gKCpy-NKrADL2ZuTCWT_GL_ywSuWESbUFbRFo0aB1zPUUnEMwjpB1c3l6u8y9acTJ5m6sOYJyKL-PQjqCPW95ICmn0AjqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SkbtflSpXcwYtKCIKyh4aAHlCJrQttaGaPWzVKr78S6gjero7aZ4rKy-EjjIDAV9D4Qdd5ep4LEmxmQjxQGjxR2rr4r2S5oQBU-8uTgeO9HMAsFbtPqxJNu_KD2dPthXVJkGMA4F2iIRgA0D1gcEydzDZrhTgbba4jEV2N07Q0h72gXSbLq5iORgrtXgCiGTTqf2HcKoI2d7XFX7RNppurZbYk6igJaUyK1LOiYxcXFyKiyghSUHDzB9Pp8ei3HRJgP3SzGuR_PLGOMgatiNPcrF7ftlAxlr-2-A9ccbFUFdjxuqNCwRBzv5M4HMcKXo4DgXvtbfRz_C6ahcO2U6Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=SkbtflSpXcwYtKCIKyh4aAHlCJrQttaGaPWzVKr78S6gjero7aZ4rKy-EjjIDAV9D4Qdd5ep4LEmxmQjxQGjxR2rr4r2S5oQBU-8uTgeO9HMAsFbtPqxJNu_KD2dPthXVJkGMA4F2iIRgA0D1gcEydzDZrhTgbba4jEV2N07Q0h72gXSbLq5iORgrtXgCiGTTqf2HcKoI2d7XFX7RNppurZbYk6igJaUyK1LOiYxcXFyKiyghSUHDzB9Pp8ei3HRJgP3SzGuR_PLGOMgatiNPcrF7ftlAxlr-2-A9ccbFUFdjxuqNCwRBzv5M4HMcKXo4DgXvtbfRz_C6ahcO2U6Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rnOkKG4KBZ01e-18LYRzIZD5W21iLzodyQ9iNGCVxCy-_sYzatc-1t488Nj7n6WPsQByZuLDgdTpYwUZYvNlze3xjwVL0fQxBJWZfeqHPg9J-1jsvs80zPmaLdqSewjRCawMTjzwithO0CAiy28ullZ5IauCGOGRjVDTU_NJt2E0rcaGMPlcWWMtXzSXpf6zgG7bqCvkfPmcfB3nPnB7WExDfVsaTo2OCiHpI2iT1g7iWpmY7aA4PvHj4MInzlKX_ZnS8vcI5RBxJt-OgO8yBHd2J1Iz3lVr2EywqnV-qMzcDggjXjZazPn76D8bNce-zQ0wW871TleyLsQdUUq3sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=OWHDpjcJy7Xs7T0R7JT-vE5-FhYj48wmrc1LJAmn4QowFRCn-7y81y_khOp2qQ-etLH4e6IuOECnxy1EVX8gM7oE4Mq9fteIShvhMw5qFzwOw-hBi7eUxNtyFGQ7z6-g4t4K2NZl0h6dL3Pb2ek6I0Il8tLF2vaPrc7WO1P5Cg-JGVMnpmJMT_s5mHmDKTnljC0VersYsUBuIMxuHKN6RK83hL720A1iGpogRjQGQhpWBVKmTHRTfMqlcIQb6mr5VZ7Z5P4qsly-vU9-sixYxMVK2x4R4WmDm-BycizuWxGHH1T7d5MCwlr8Kos5R3jSuAwHzqQ5rXXQXWWULC8jaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57d085c21a.mp4?token=OWHDpjcJy7Xs7T0R7JT-vE5-FhYj48wmrc1LJAmn4QowFRCn-7y81y_khOp2qQ-etLH4e6IuOECnxy1EVX8gM7oE4Mq9fteIShvhMw5qFzwOw-hBi7eUxNtyFGQ7z6-g4t4K2NZl0h6dL3Pb2ek6I0Il8tLF2vaPrc7WO1P5Cg-JGVMnpmJMT_s5mHmDKTnljC0VersYsUBuIMxuHKN6RK83hL720A1iGpogRjQGQhpWBVKmTHRTfMqlcIQb6mr5VZ7Z5P4qsly-vU9-sixYxMVK2x4R4WmDm-BycizuWxGHH1T7d5MCwlr8Kos5R3jSuAwHzqQ5rXXQXWWULC8jaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زهران ممدانی
به مناسبت ۱۱ سپتامبر که هزاران آمریکایی به دست مسلمانان افراطی کشته شدند،
با صدایی بغض کرده
از عمه‌اش یاد کرد که بعد از ۱۱ سپتامبر
از مترو استفاده نکرد، به خاطر اینکه حجاب داشت و در مترو احساس امنیت نمی‌کرد!</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=nwmXtr_1gXqG_7SYLSlTXRfHCdCUB9tOpfeOy-W27rm0e-isCG6N4npCNsPRRdIR6Pel-r-j0hTdcAG3pkwFZP-bn9PuQgGJZJsOeIXGVXGMFLpXqCpci5zhgNhwjLfFjLgjty0urcMKpgVhQ52kJIRXvFH3tXDdt-SHeF4CYREke796fLBvjpIdcHJuq2ksw2qvd06II0-2DYqFZGTsIgwCj2GZiRH-VEINd8bZxHXowPSwlqRM4rpW8O_ZBR1hKXIunK-hrMgRNkjW3jU-nGWESSM59AYhDoK5oDk4dJPXh-voi5JgTobxAihVq6lYeFHwM-MpJKwUFT67-NENgD6Ua_-8ioeI68EYrKSSfqPycOEWhWxZ_Y8O6Dlj4Z4Kzue6CVCe1Ys51sRVBRIJnQ0_tVeI26xgskVL_zU57YvUPMrqJTfLsYUzgzB81mGbm8Xq3JOFKhHdD3PHFlsKA41bfh1zV_T4A34SUM2I2LcUodrH5svKq64NR84Lmw5LjYEJMm9ug9lfVviE_iK_3jc2lX3fIddNo-2pYgu8c_r1jF3gRIWwhP_1rXdhXIWba7xlrUt4Xw56HIfkdvS3MzBgrsIq4T_BCqEHEu0EZk9w8ANn3JJCZSAlvBLsbCLL7_TVCyQmTJmihSYeh_X4Zk8mXxDo1oSq22ZfV_EdGuM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec3fad6c0b.mp4?token=nwmXtr_1gXqG_7SYLSlTXRfHCdCUB9tOpfeOy-W27rm0e-isCG6N4npCNsPRRdIR6Pel-r-j0hTdcAG3pkwFZP-bn9PuQgGJZJsOeIXGVXGMFLpXqCpci5zhgNhwjLfFjLgjty0urcMKpgVhQ52kJIRXvFH3tXDdt-SHeF4CYREke796fLBvjpIdcHJuq2ksw2qvd06II0-2DYqFZGTsIgwCj2GZiRH-VEINd8bZxHXowPSwlqRM4rpW8O_ZBR1hKXIunK-hrMgRNkjW3jU-nGWESSM59AYhDoK5oDk4dJPXh-voi5JgTobxAihVq6lYeFHwM-MpJKwUFT67-NENgD6Ua_-8ioeI68EYrKSSfqPycOEWhWxZ_Y8O6Dlj4Z4Kzue6CVCe1Ys51sRVBRIJnQ0_tVeI26xgskVL_zU57YvUPMrqJTfLsYUzgzB81mGbm8Xq3JOFKhHdD3PHFlsKA41bfh1zV_T4A34SUM2I2LcUodrH5svKq64NR84Lmw5LjYEJMm9ug9lfVviE_iK_3jc2lX3fIddNo-2pYgu8c_r1jF3gRIWwhP_1rXdhXIWba7xlrUt4Xw56HIfkdvS3MzBgrsIq4T_BCqEHEu0EZk9w8ANn3JJCZSAlvBLsbCLL7_TVCyQmTJmihSYeh_X4Zk8mXxDo1oSq22ZfV_EdGuM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از حمله گروه‌های وابسته به ج‌ا در عراق به عربستان :
عراق مرزهای شلمچه و چذابه را بست.
اینهم وضع مرز بازرگان
این چند روز ویدئوهای زیادی از وضعیت مرز پاکستان و کامیون‌دارها نیز منتشر شد.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrizzU9zmbICrqet4MvVKfIpUHVUt7IIXPpUEAvNEue2zSPqFDKGVbphH2plJS9byQtPHBtdrHP5u7AIlbrHvO2LorWrabXdorpfrDx5AvUzXI7dHH8JDKrkxFil3R1YIzKFfobiCarj7RsO4vqw3A8qvzyoQd-3rJm2bsXjkJLvnHe0AvpYnTJYBGjioZpfrZOJkcTyAZPbluGnLizhGK8RaNNd4BX6JiAKWHaBM53ok5NbT_GZKgXLK_mJJkDPwuuzL68H0-a46jlFK0YrxP5UNtAHdZZiqxyMIKD63nlli8Vdrz105kWtnyITiOCL13dfKxprBlWLcL4jcufhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=aqBPcuBuNvBMMd4ZRXwEdWhESy53dIEjM4rDP75naCin2CjD4BmRQWWYY2FKQvWWf1dAr2n1-hydXz-dzOvCk0SOJ8QzskxEr7--JoZPw6BTLCVKYeSyssiPM5-hBoGVd_RV58BlT8lxSbO9CDDINyeUtRVaXB7RB2DX_qzL_nMIXMMQ4PtV-6t9t4CaZQQaxLnWtNoNFTt4qBYFrfDtae-Od6v2Fpaj4ma-t9-3YGcyDyzBEqtPaDp6VaiHX6Pt4XZN7_6ycERp4f6YvOKe5VQS1MAIbjeEJ1XGFOu8E6G_rFAx-B_pQuZ9QaWTwypgVgFjLHNfFTriDWt56BFR359crMBaFk8EfKHqi-oNF_3vAdgVSSLiT_aPHMUQXl4NjH393pjl9-ZmJXrhaqYHkmUwXLgebHw6DGTXVS9XyA8PqjNTDWLhLyRgjdlKPsND75t294I5SY3TCBTqOHJg7ccIMOonZZl3_amOsERSGRL8Ck8EjRp-3sv64Rqd62tTJfbKN5pic05FMNyUq2ebNKVF3JjiC5chHP5Yze_RqjYzzzmTLZ-vudv99wHKCH-Qm3nQFuRqeQhKWfCli7JuvhBXmU5SzJ4hcGN4w6Z9bjngXZLRwr7rx7KELB2Do_y6590IoaHQPfv8z5kJgrdcdAfY0C4WAUVZG7Kb_q2OoOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fab4b9913d.mp4?token=aqBPcuBuNvBMMd4ZRXwEdWhESy53dIEjM4rDP75naCin2CjD4BmRQWWYY2FKQvWWf1dAr2n1-hydXz-dzOvCk0SOJ8QzskxEr7--JoZPw6BTLCVKYeSyssiPM5-hBoGVd_RV58BlT8lxSbO9CDDINyeUtRVaXB7RB2DX_qzL_nMIXMMQ4PtV-6t9t4CaZQQaxLnWtNoNFTt4qBYFrfDtae-Od6v2Fpaj4ma-t9-3YGcyDyzBEqtPaDp6VaiHX6Pt4XZN7_6ycERp4f6YvOKe5VQS1MAIbjeEJ1XGFOu8E6G_rFAx-B_pQuZ9QaWTwypgVgFjLHNfFTriDWt56BFR359crMBaFk8EfKHqi-oNF_3vAdgVSSLiT_aPHMUQXl4NjH393pjl9-ZmJXrhaqYHkmUwXLgebHw6DGTXVS9XyA8PqjNTDWLhLyRgjdlKPsND75t294I5SY3TCBTqOHJg7ccIMOonZZl3_amOsERSGRL8Ck8EjRp-3sv64Rqd62tTJfbKN5pic05FMNyUq2ebNKVF3JjiC5chHP5Yze_RqjYzzzmTLZ-vudv99wHKCH-Qm3nQFuRqeQhKWfCli7JuvhBXmU5SzJ4hcGN4w6Z9bjngXZLRwr7rx7KELB2Do_y6590IoaHQPfv8z5kJgrdcdAfY0C4WAUVZG7Kb_q2OoOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :
«مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»
و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kLF05tmGCi1TCIczn3UddWaJ6wrp4cQUgFh17GGFW2xPIeY8J0UL8IYx0jgH7anUmCr4x0GyuyrhBJz109qb4X7yW_EFGMVovO297Gc1ybCRrZIP_k-9rFZRazM9ycaApzY71MVrvv0gr3BMUb6IhXbJO-95JEGr3BZ_kQ7kWCE9nR2_unU0vjECnkDaBW-hMP4kgHKZiiZlx--adlphUarHQTvPBm60WvO6u3DQDe5d8z2Tf6A9nsKb2xCqATuHgRvFGk4fDvB0cf1yWayN8HtS8TR2H1S6H9LAb9vmz7yglAWxwBeq6veSV-AIaz7XK3TsflSlQNtEUh1Cvcv6zkH2-ryjQiYwpMrW23GA_UkipIJixR4UDKeTz-51KNEUWwIBmrkPaxzJcGiLL12JxxPlDdVlW5fLsypdSUPydNhEHWRnYy_LxgUIGgyAcQkvxxK8wYnffitTyo4gYH9Ky2dI24jqcB6Mc6v6Pa9SZugaQJg2POWv3N7YTaku3pmcMsBoARdClgmuINhCxPoBYgvzoPo9-0VX3pUEEdW8kaZfp2CM-qskHtCy6xSXF9oeFF_RLREg6tSVlj3gwJwChd58mqSf4zPc0tmWr7e62gxSEGW8ChimTVj1Xc2B8NCQSB70o89MDb_QRrTGfANiv73Pft-rncJreDxB8DZTla4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kLF05tmGCi1TCIczn3UddWaJ6wrp4cQUgFh17GGFW2xPIeY8J0UL8IYx0jgH7anUmCr4x0GyuyrhBJz109qb4X7yW_EFGMVovO297Gc1ybCRrZIP_k-9rFZRazM9ycaApzY71MVrvv0gr3BMUb6IhXbJO-95JEGr3BZ_kQ7kWCE9nR2_unU0vjECnkDaBW-hMP4kgHKZiiZlx--adlphUarHQTvPBm60WvO6u3DQDe5d8z2Tf6A9nsKb2xCqATuHgRvFGk4fDvB0cf1yWayN8HtS8TR2H1S6H9LAb9vmz7yglAWxwBeq6veSV-AIaz7XK3TsflSlQNtEUh1Cvcv6zkH2-ryjQiYwpMrW23GA_UkipIJixR4UDKeTz-51KNEUWwIBmrkPaxzJcGiLL12JxxPlDdVlW5fLsypdSUPydNhEHWRnYy_LxgUIGgyAcQkvxxK8wYnffitTyo4gYH9Ky2dI24jqcB6Mc6v6Pa9SZugaQJg2POWv3N7YTaku3pmcMsBoARdClgmuINhCxPoBYgvzoPo9-0VX3pUEEdW8kaZfp2CM-qskHtCy6xSXF9oeFF_RLREg6tSVlj3gwJwChd58mqSf4zPc0tmWr7e62gxSEGW8ChimTVj1Xc2B8NCQSB70o89MDb_QRrTGfANiv73Pft-rncJreDxB8DZTla4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ULmsZOmvu9HKfTMOzEkdLgAxHOKCeQy0638jOZJ8pzxGR0uevECw59jmdpH7YCshLVcyvup7jxR9CX27s0e32W2QufvSKev2EOgDwlcVSp3FdhbAomkk54_tQPxLEIdg9rNqclhs6ATZ0oSNcmrk3tVlKVCow8CLuLOaVs7WCPpen5oXntQCf-dSw8mFwZB0yNYakkPwJvtdhq5-wwjHEk6nEkYgRrLYcVHgk2AfJkDJ-lO8Wch8TzDBJg6jql4dPJXiNTN8JdFP-Sew3s_3eqHw5EgUcK1du5sfjG8Q3nd6NjIMqZudQ_JR31FEaWN9QcOag6SBHKg3fzGnaRKy4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=ULmsZOmvu9HKfTMOzEkdLgAxHOKCeQy0638jOZJ8pzxGR0uevECw59jmdpH7YCshLVcyvup7jxR9CX27s0e32W2QufvSKev2EOgDwlcVSp3FdhbAomkk54_tQPxLEIdg9rNqclhs6ATZ0oSNcmrk3tVlKVCow8CLuLOaVs7WCPpen5oXntQCf-dSw8mFwZB0yNYakkPwJvtdhq5-wwjHEk6nEkYgRrLYcVHgk2AfJkDJ-lO8Wch8TzDBJg6jql4dPJXiNTN8JdFP-Sew3s_3eqHw5EgUcK1du5sfjG8Q3nd6NjIMqZudQ_JR31FEaWN9QcOag6SBHKg3fzGnaRKy4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QINSx-ADpH08FSDSg_QwPAyH-ibX0auJrsVZi8E2Wvy1bu5BTTMwl3J0V6aAJdCaNWUBVMSAlZUHFzU66JpfYvK8s2v_jJjg6ZtULncBS5o3-EMISXrXXXK-RPPSrvQkszCO1p1RQMazSTrDMOq2tKyHPaAt0UiXEuw247ONmfp_VKPONBRKwkoi0Vk1OSYRLmEaQmXDcLfWQK48O0D_B8SmrtSQNLhKr4UWkcGXq523eklXtLiKRkMVcIDdymOQKaJeQ5a4q2FFn8KrjlKll1TRqzyhobWI9GK-H8Feb9W85n98DC3zv9G84r1o7UuTv4lAlcfzcM-LjmFEhvkgCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=QINSx-ADpH08FSDSg_QwPAyH-ibX0auJrsVZi8E2Wvy1bu5BTTMwl3J0V6aAJdCaNWUBVMSAlZUHFzU66JpfYvK8s2v_jJjg6ZtULncBS5o3-EMISXrXXXK-RPPSrvQkszCO1p1RQMazSTrDMOq2tKyHPaAt0UiXEuw247ONmfp_VKPONBRKwkoi0Vk1OSYRLmEaQmXDcLfWQK48O0D_B8SmrtSQNLhKr4UWkcGXq523eklXtLiKRkMVcIDdymOQKaJeQ5a4q2FFn8KrjlKll1TRqzyhobWI9GK-H8Feb9W85n98DC3zv9G84r1o7UuTv4lAlcfzcM-LjmFEhvkgCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=pu_hzOSdYJ4RC1Luae6Hu1btEPx-j9dRhq4BEoVXRBXEjJgvARvDF5F2vcZ_Zgb5pjEB_lsR2mKa5YxdVl2slHK_b1a8Gz5satvOBuFwSmPEB0VJGWZV7PFoRc_1TQ0O34u-rXxhdYuZe2YtMRl05tBA3ui9xiIIqpRDq7h7WOsHE7OVxU4a4ci6iybI4piXEvaooiVvcI0XXyq-RRG309lvkukMRufR3sPOzAPZzIy05GJvqrM50_d1x2WqI8tI6IhUT8GNoXnQ5oogxoVUE3C24kOdNDRKD9M-CS06Fuo7X-LfS3aB1-O3Ca8DKQIEw7piAyg1zR7r9njYegJyZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=pu_hzOSdYJ4RC1Luae6Hu1btEPx-j9dRhq4BEoVXRBXEjJgvARvDF5F2vcZ_Zgb5pjEB_lsR2mKa5YxdVl2slHK_b1a8Gz5satvOBuFwSmPEB0VJGWZV7PFoRc_1TQ0O34u-rXxhdYuZe2YtMRl05tBA3ui9xiIIqpRDq7h7WOsHE7OVxU4a4ci6iybI4piXEvaooiVvcI0XXyq-RRG309lvkukMRufR3sPOzAPZzIy05GJvqrM50_d1x2WqI8tI6IhUT8GNoXnQ5oogxoVUE3C24kOdNDRKD9M-CS06Fuo7X-LfS3aB1-O3Ca8DKQIEw7piAyg1zR7r9njYegJyZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=c45HTjLVdyVGc4DFF0tmPACRRCJQjfv8DnVZwVWcfvpOm6Xbc8Pe6yiW4Feq1lCTenGL8V25O6Mswba2ewtplqykgAFY6xHE9uF3rQbXGWnxHu_nX-dRXoHWeVTu5sgq65FrX_EU8xEKjxi_gQdIGtUI_mIp8LHLHHB1Tc1AynUvyQyF_lg8wR_YbsupQ2-m3NOSzCcGCnHboM65aGfyI8Mj7XuolVVUweQdog8GeadjoXAL4cuAqtMdHdx2cRj6A05VU20I-sOaDZJILhk7i8fNcV7cXMC0OT5q8K_fs0hM-roJHQx1Y0BWi9oS59m8ruWRMNoIdjS8N7nLhgcVmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=c45HTjLVdyVGc4DFF0tmPACRRCJQjfv8DnVZwVWcfvpOm6Xbc8Pe6yiW4Feq1lCTenGL8V25O6Mswba2ewtplqykgAFY6xHE9uF3rQbXGWnxHu_nX-dRXoHWeVTu5sgq65FrX_EU8xEKjxi_gQdIGtUI_mIp8LHLHHB1Tc1AynUvyQyF_lg8wR_YbsupQ2-m3NOSzCcGCnHboM65aGfyI8Mj7XuolVVUweQdog8GeadjoXAL4cuAqtMdHdx2cRj6A05VU20I-sOaDZJILhk7i8fNcV7cXMC0OT5q8K_fs0hM-roJHQx1Y0BWi9oS59m8ruWRMNoIdjS8N7nLhgcVmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IV7ywaF6CwVgMbdcUwx1HbRqV0iDn-ot6CEXZeHkQrbMEnFdmBJF8npO_ApLRtdP0lC6TQ7AxX9GeJNpbIk0MBKk1XQ5rIi2imttoQ69sN_WQk9pbD9CK0wr3U1AKfasA4NOpKwUMNk07st3Ne0Nh8aKOLyrWSqGsghJxfINWKi8d6UrtHNtS2Re0u80LE2fNGo5AnCA2N3IYARmWl63Yvd6MUOrttfhPfsJyGxVhnhhpkje583wZwDixrCMLfmziFp2VvnNmazLbDhyMRfDxGVaMAe8iWt0O_v7_kcAXjdsX-7l3sor_PUO0mwfeLsMll2e2Kah00hJ9VZC48oihg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=IV7ywaF6CwVgMbdcUwx1HbRqV0iDn-ot6CEXZeHkQrbMEnFdmBJF8npO_ApLRtdP0lC6TQ7AxX9GeJNpbIk0MBKk1XQ5rIi2imttoQ69sN_WQk9pbD9CK0wr3U1AKfasA4NOpKwUMNk07st3Ne0Nh8aKOLyrWSqGsghJxfINWKi8d6UrtHNtS2Re0u80LE2fNGo5AnCA2N3IYARmWl63Yvd6MUOrttfhPfsJyGxVhnhhpkje583wZwDixrCMLfmziFp2VvnNmazLbDhyMRfDxGVaMAe8iWt0O_v7_kcAXjdsX-7l3sor_PUO0mwfeLsMll2e2Kah00hJ9VZC48oihg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DK-KPjrFQrfIS1PstsGOSKnAdDadbUlzVUZIGzXQZMNvl1lX8QCIq0W0xI8LUKyixPhSk_MmfD5NszBwAVRc0zfGhT_7DrQULtmYImqo3hUHxLX4lsTZAN-rnIeKLjT822Avdbkqx8e8GHRneLIpd5N_0PTIKIjPT5KsvtifiDu5JF65TteDlCQEwaWndXAMN-otenKfMT0Z0F8mT4p5JGw4oCNMRsw1lsM3zoFPbmCBoHFpA1I4raaT0DqF-MUNNYbd1UJWJE3v7_w75io5D5lvqZWrHsitcUM8EhOIuI_gWKYV4YpV-86VacJ9U58xLaegoBWSlUQc3KZRZz8sKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=DK-KPjrFQrfIS1PstsGOSKnAdDadbUlzVUZIGzXQZMNvl1lX8QCIq0W0xI8LUKyixPhSk_MmfD5NszBwAVRc0zfGhT_7DrQULtmYImqo3hUHxLX4lsTZAN-rnIeKLjT822Avdbkqx8e8GHRneLIpd5N_0PTIKIjPT5KsvtifiDu5JF65TteDlCQEwaWndXAMN-otenKfMT0Z0F8mT4p5JGw4oCNMRsw1lsM3zoFPbmCBoHFpA1I4raaT0DqF-MUNNYbd1UJWJE3v7_w75io5D5lvqZWrHsitcUM8EhOIuI_gWKYV4YpV-86VacJ9U58xLaegoBWSlUQc3KZRZz8sKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OgwtUizCsy8MSYrDo3T_LjANRVL73yQwwC6zRJKr-tmOciKHa8rBTXTyorFVv2mzYk47TRajXdXVZy185VqAxVJh00rXfg2K9yT7jOkLXPPkwaJVCdcrwnn5gVJrG82G-0mIMx845TB9kvJOxoNqvq3ci09ZjXh02D_kBvliNDdurGiSeWRL4WuZ16-MC9l-pO7t_SABMFDcEJNYwQVcoDozDJGIiguuKJeHlvCLl4xN0V-QQtvqt_OGpSzpbRpS-s1vK2nOMOaYYjUbw0V62aiLVpEk_sOS4pO9CRFdCjMex6vxR7DonamVIRLIL86mv50btJO25uYOq8S75Nusdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=OgwtUizCsy8MSYrDo3T_LjANRVL73yQwwC6zRJKr-tmOciKHa8rBTXTyorFVv2mzYk47TRajXdXVZy185VqAxVJh00rXfg2K9yT7jOkLXPPkwaJVCdcrwnn5gVJrG82G-0mIMx845TB9kvJOxoNqvq3ci09ZjXh02D_kBvliNDdurGiSeWRL4WuZ16-MC9l-pO7t_SABMFDcEJNYwQVcoDozDJGIiguuKJeHlvCLl4xN0V-QQtvqt_OGpSzpbRpS-s1vK2nOMOaYYjUbw0V62aiLVpEk_sOS4pO9CRFdCjMex6vxR7DonamVIRLIL86mv50btJO25uYOq8S75Nusdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/da5u87NqRu6g-RoyueZgbuOV8dja78RxL4DJrRM8-79FYK3JHdg3lySAUDy9Cbqbo9_MVk4xZaq6ow1xPTWTkmdkt0gJUB4-R93ripzHqlVTB_HoXnbCs51pOK4bgLp7h5tvvhi5FtxOLP6xRW5Nyp94_zfzl-BpC-BbQQrn9lou4wQx0UHM6qenRc7vv2n6uc7TfQJn_dJtLvj7IQRr829sbk4nkAaKKCfJdrC11rkfdh0Y9yZE7pCiWTcsJUWR163r0-4-4x3amSq83bagqf8w1ZsgeXiWvpurmfq75l70pRcVq02T1dZ0TzbIuuP9wQZAruch8oqDtzTWQMhOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BJzeLi6ftfqK_ZIsR_EqsuQfUM8-yel96tBuo8NvjVWiwKr1SFLoh3mwsN7GFHzvkXxTHSZa7aoTko4we6EPe8kEtIqqF9niwPPS_f9R7pSltNWw3BAiikUVSntxM2QWviCvMYZyWHEYafCMWuC7xIfswpg_dc0A4vL-IH52NuToX0vaO0dnhUZwEeyllzb4vJlzsLNQnWAAytw3-kWg5luRaza2w9IvZS2EFb_pF0zxrLJZk5079Q_yn32KkVRFNDtbCiQZ9UDrdYKpLHe0vwmMqe6nnjZdvjit1UmCAobLeuyMgKeIstWIxBYENtZfzkfpIuAAdP3ZJAyZPuvezQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=BJzeLi6ftfqK_ZIsR_EqsuQfUM8-yel96tBuo8NvjVWiwKr1SFLoh3mwsN7GFHzvkXxTHSZa7aoTko4we6EPe8kEtIqqF9niwPPS_f9R7pSltNWw3BAiikUVSntxM2QWviCvMYZyWHEYafCMWuC7xIfswpg_dc0A4vL-IH52NuToX0vaO0dnhUZwEeyllzb4vJlzsLNQnWAAytw3-kWg5luRaza2w9IvZS2EFb_pF0zxrLJZk5079Q_yn32KkVRFNDtbCiQZ9UDrdYKpLHe0vwmMqe6nnjZdvjit1UmCAobLeuyMgKeIstWIxBYENtZfzkfpIuAAdP3ZJAyZPuvezQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=r3XY-filP8wu7V_9lvkcE6tOkz71uVDCLFAdEALu7XIpdaOinqJ0NpBgPe6q3KM3ULkqbhzCrwVYSVpx37eKVLw4NOHaAuI4pmFXjkQNVepxE8UmCr2oLJ5RMS41htRjf8jJO3POnzbdy8045tGVXOM-KRILtJ2rk48DIcVMqdX19JDi9y41b7ruSH3cpRuifP1F-mgFSu-PSV5oPJvVq9xCS28DUSPFthOtsappgPZzcmnTX4XIQPvFtmqvylR0HbXcYOuLdBJqKK7CVfUKuqJolZooV956_9bWgcxVuN6Zi3SDL6dUJkcNmDLfcO6XB74KmX3QjzPqrGaJcQYJgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=r3XY-filP8wu7V_9lvkcE6tOkz71uVDCLFAdEALu7XIpdaOinqJ0NpBgPe6q3KM3ULkqbhzCrwVYSVpx37eKVLw4NOHaAuI4pmFXjkQNVepxE8UmCr2oLJ5RMS41htRjf8jJO3POnzbdy8045tGVXOM-KRILtJ2rk48DIcVMqdX19JDi9y41b7ruSH3cpRuifP1F-mgFSu-PSV5oPJvVq9xCS28DUSPFthOtsappgPZzcmnTX4XIQPvFtmqvylR0HbXcYOuLdBJqKK7CVfUKuqJolZooV956_9bWgcxVuN6Zi3SDL6dUJkcNmDLfcO6XB74KmX3QjzPqrGaJcQYJgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Cv5XUIPVj1ZRmjs5Gh3JiD08hRTYfNIyTPvLHWgwZgOQgANOHc7Rli7iv-IROqyFmzVmDl6QEzpOhoA-0c51cWSZV2mMmqfn5t3EFkayqeM5i2NvmDUBwDksCwYzJJgjUOA19lwrfGKv0JtBlPyo_NhszkgCLEMvqZd627BsG-grvO8SSa4F2K0I95sYjekucBUtEG_iPuBJ6PKr7pZb8C1n9lS8P8lH2yVhVio8dcUa7vLQ56Jq0EWSoLmB-0qY4Y85czwJlB0GNeKIA6OOlTmSZLkLbGeCQlBU6tCihqAQZZyPkY7xEN72bxpox_AutgF4JLnVQeYj0_ACOhIrGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=Cv5XUIPVj1ZRmjs5Gh3JiD08hRTYfNIyTPvLHWgwZgOQgANOHc7Rli7iv-IROqyFmzVmDl6QEzpOhoA-0c51cWSZV2mMmqfn5t3EFkayqeM5i2NvmDUBwDksCwYzJJgjUOA19lwrfGKv0JtBlPyo_NhszkgCLEMvqZd627BsG-grvO8SSa4F2K0I95sYjekucBUtEG_iPuBJ6PKr7pZb8C1n9lS8P8lH2yVhVio8dcUa7vLQ56Jq0EWSoLmB-0qY4Y85czwJlB0GNeKIA6OOlTmSZLkLbGeCQlBU6tCihqAQZZyPkY7xEN72bxpox_AutgF4JLnVQeYj0_ACOhIrGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=G36EAHr_Qcev5KGjSXpVc6QNpMZ0hcfQmCp2HRBOzKTvqv8HbLFdchhzYmH2fzskHTjAlJJ6C2Gib568GdxjhkiF_MU_Y6I-EOUClcdlPg7exZw4sdTc-Na4XAK2YccECEbYQfZodnokEuaVLjKrOXCwYf4VN4t49BDhe5JPkaSNxt4cIiWldAtaiidEnzyyiyX3l_oi25mvz653XXvfHAvaSyqZZKDn9PX3tEa30lZT3nuG0GIUxpatyn-DjDCho_zTIVlgO_MpcO5Njzu7nTYy4DKsqCDWV3QwflfG_xekNc9a08a2RIpkSz68u06nm7FLHz73qteCE1Jb52TFng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=G36EAHr_Qcev5KGjSXpVc6QNpMZ0hcfQmCp2HRBOzKTvqv8HbLFdchhzYmH2fzskHTjAlJJ6C2Gib568GdxjhkiF_MU_Y6I-EOUClcdlPg7exZw4sdTc-Na4XAK2YccECEbYQfZodnokEuaVLjKrOXCwYf4VN4t49BDhe5JPkaSNxt4cIiWldAtaiidEnzyyiyX3l_oi25mvz653XXvfHAvaSyqZZKDn9PX3tEa30lZT3nuG0GIUxpatyn-DjDCho_zTIVlgO_MpcO5Njzu7nTYy4DKsqCDWV3QwflfG_xekNc9a08a2RIpkSz68u06nm7FLHz73qteCE1Jb52TFng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Llng_PFAMq9PeNQTXaju2Iqq1uddns6NBXRIp4uDJbtZcNJVa_LWy17ZNZuKRBG1IUWkuy9CG8V_YDPLR2HvFVC_RhY2p1A4pXNsYJtjRUgdoLe7FjPerDPxtVwr5ZMvaeTgB3SwAvYvUFn3IvVfw5RbRYl0ylOiosOBUW2m6Nxx3Q06l05rtNu95plk_FgqeEtJ5EpoAIlsb1qH0hp0GEU6JJcxZMSJN03YPOhIY-86P-Euj6bhn7InYH2UKNd9rmdbq10Nu0cDIXWk94jHim1Adq6UEdVYF-K-Bcv1yiGFf7ndinvWSvXx_RgDh16tKdlsoVYnMcIoACOGUrMeqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=pjuaxNIExwC2tUhShJzB8G0a2WISvneoyLAcrq9jukvg-b8qOxVHKpIW8UUTzkMu8hQvWLoWk0cy3XafbsalrHEzFMJF7pmI7RSn8Adj-9Qz37S1pM2DDDl3gOJ92krlrUTqRAzhRjJ3Mitxa7Sys1tnYe8r44DglNzdKxW369pgNvxt6V-cwgU8a_hT6ym2vXc319oAupcWVYt01krPwfeu-pVHWezz1C-Mw4x7c5bELDgaHQoxMz5Mh2Lnbu2t2fILGAKJhbb-fY5_5wRzw-R2nLzP9FMeRPcVg-ADOb47O8j-rk3SxhqSIARSniL0HxN0PwHtXM6x0N3wBJ_mLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=pjuaxNIExwC2tUhShJzB8G0a2WISvneoyLAcrq9jukvg-b8qOxVHKpIW8UUTzkMu8hQvWLoWk0cy3XafbsalrHEzFMJF7pmI7RSn8Adj-9Qz37S1pM2DDDl3gOJ92krlrUTqRAzhRjJ3Mitxa7Sys1tnYe8r44DglNzdKxW369pgNvxt6V-cwgU8a_hT6ym2vXc319oAupcWVYt01krPwfeu-pVHWezz1C-Mw4x7c5bELDgaHQoxMz5Mh2Lnbu2t2fILGAKJhbb-fY5_5wRzw-R2nLzP9FMeRPcVg-ADOb47O8j-rk3SxhqSIARSniL0HxN0PwHtXM6x0N3wBJ_mLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Pkm-7foC22L3keiBj1ajSj3OAz3lBBAv9sP5V8ZNU0DLlqF_b6qnZbbPBdEEuFFB3lyPOHBupH_chLviybWqaTyn64B7JFdPZ0dPSZ88vsvD36OizVRcFG4xF1DWur7ZEYnP3qi3859-cQAeoWDyBnG4SPvR-B8v5w5P_9MCtD6OzLVegbeLZeyT3RdQEKMSlWaeFDncb21cFDGvxyei5VDIRtBXFxOb1Hus2h6aASBIkbopD6pLhKI64ntx3ScX0hWNOsXqVcDagUoIMenlrBE1qGy_DOHiTOUhFRAvwVBso1mbEoMkDTBVzB7O_DSg2kz0ciBy7Pv7UlLiWfxiZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Pkm-7foC22L3keiBj1ajSj3OAz3lBBAv9sP5V8ZNU0DLlqF_b6qnZbbPBdEEuFFB3lyPOHBupH_chLviybWqaTyn64B7JFdPZ0dPSZ88vsvD36OizVRcFG4xF1DWur7ZEYnP3qi3859-cQAeoWDyBnG4SPvR-B8v5w5P_9MCtD6OzLVegbeLZeyT3RdQEKMSlWaeFDncb21cFDGvxyei5VDIRtBXFxOb1Hus2h6aASBIkbopD6pLhKI64ntx3ScX0hWNOsXqVcDagUoIMenlrBE1qGy_DOHiTOUhFRAvwVBso1mbEoMkDTBVzB7O_DSg2kz0ciBy7Pv7UlLiWfxiZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vv2JUn3a-ToPpNUIqEry2Hrevv6aYDsWOjwF69KuFMeaAsNw9EaDHtfgSH8bwGAvQoX5HvU-2mIr_Ys3PsGSnGlDn6qi_B_D5Tl9HIfNWsL3m4AefaPZyuE_IWypYRjKkTKEG5LxUM0f6wLY0OSxJxOi5KYhb43uf-5D96x9qycLxW-P3g54yeqhlw6dZpY5PpvFJNlZY-tKBmqocrxfZxMWsXK50vDt4u6opKv3D94JtgWS65HMCLclen7mgSRo1XAUaXEmSjw26qTqOlPBzmPjfScz0sIfKEfzZIgY8CMlP7tTUztpiEc_Wd6pAVEfjs0vE9gWLyksd7gRbqMVTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8oiK_fLE0aNsV0t7OG9qdtke64wyKrI9xUcUfp4cBD1AtHMOsEd-ugn3CpuGpQz8MOGPHQlxzBv9cgebVPh0scUN_zSpjm0QnfrROKarDsfe71pN4g8H3csz-yHy1UwV9lzcNh_mwbqBgamLBwWRoXt-uTxWpNEwZ_Hi9tUIGGvJemlm15BdoA5-aCsXSv9gb5FZmfjym8HHIgWBzETvFGe1UA6NQYkOoBq1bJPwv5mkZy2CmjjO8yNfRO1jJIVMh4MkNG3W74VKcxwPWYwvlV2cOo8EAJsG6i-T6AtMDdXIJSFhsfkpMnoeNFB6nRiW1FHvnPSnEzDHQEOzzQf_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sWHuWFAIlT0Fn1uFDSrYLM6X6qAiEuK4DptDktL5rh2ZX-5b2kaTiTjB-XkHPM0YqfZZkSMVUuYONdPE5KXYOmMVLYQKvYiXnhqQ-xOKEogCVQhgJ3BL2CNWcQ6zsWZfIyU8SMYBNxNTz8IWNHdHIn5tdsD3fD1yflt09CwXmlZRTQVJnNQHjg3ASnStIuA3T3SeoT9pKz8BBuf-mOo1yrd_mmmJ9th_1nDBTm_umaj9HTPCA4n_AfDkwon8aOGYM4Lz9hFpz8lsG2VAiym_I8YkSncppl35vkg6Q1pt5T5m74tK9JRxi3ZC86omQpaI0VKvcwcJC_I6wA33oDGZ1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=sWHuWFAIlT0Fn1uFDSrYLM6X6qAiEuK4DptDktL5rh2ZX-5b2kaTiTjB-XkHPM0YqfZZkSMVUuYONdPE5KXYOmMVLYQKvYiXnhqQ-xOKEogCVQhgJ3BL2CNWcQ6zsWZfIyU8SMYBNxNTz8IWNHdHIn5tdsD3fD1yflt09CwXmlZRTQVJnNQHjg3ASnStIuA3T3SeoT9pKz8BBuf-mOo1yrd_mmmJ9th_1nDBTm_umaj9HTPCA4n_AfDkwon8aOGYM4Lz9hFpz8lsG2VAiym_I8YkSncppl35vkg6Q1pt5T5m74tK9JRxi3ZC86omQpaI0VKvcwcJC_I6wA33oDGZ1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xk48r8G1Z_ZLaSmUxKQyiwtMVFW_2MjzSbLVhj1sLw5DIChWM9dxoYNKC2gW4msFJLbhIeeCDH3MYlmt2J550tVYBD6Bv5XXaR9NDd2UUzYYE5V-pH3lIVwG_2j_cvb0AqhENpQQYV3g8Nvj_1KhFGhuNwxnrVh6OjDCf1qB0Kv4rnJA0yfV6qUR1XHT4kC80Jy_Im-ydSojCc_Fnuv60aO9VE8Y7RcEy-kP-XkXrwmC_RLpg41PbGHo7WUlzq4ci0CNZauoloum-BSpROi8kwW1mD2UvOSO2WNnqVJ6LigFduKiwjeu-gjX5YFsssXxCmmmjnsW-q_Tb0WX9Wy7Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PwhhPxIgktzOrEpVtQSTXMkNZ-_HPXlgOzVaz2ReN49mnRimgn2FFrD1DZiku6DyJ1XxnfcdJfLf68g_Z3W6V6NLdOhN6WnXyh7wis5LM7YzKzSft8vRX0UKzLjHTtNgoo-0VoMrk5CB1M1z8eABDhlJTO4Z4HTMMjtGwaMmDP14YESvfYdQEGN_EtN2BeAfo2AZJO0xjal8Atf4Hso9-66P4RgdDmGQYa761kHmhAJIR9M6f2cWcRNioESKTbBAJjidUAyMdZUsNGPSy0Cc3qIJySfKDc6fIZYgAxjznzqQUQbqfUw6lk0nxTQEEdHYHoKcURwB1V-Lo2vM0QMdlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dx68jRLTpo8kWWGdd_CLrDxYmucvqaXRkkrUdrOXdqons8MGvwoMytTvjiixRF9l3ng1RMC-uiIjJl_jqDkypx99x8X9FAEGrXGahkrwfJ4x-7_OpIK2uldmYNtRgNX9qBwWTM1FIfzrlUc1Aw5l1uWKUuNHmlytL3W2dIvTBN-JbLpkTV-j2ac__IVXwFXmfAZeaBUC83ScHcXk6iyhkxf2_sFApgfX0bI7_rQD1ubabOdM7Ru5wAushomLbDuYXG8rV8DTsZlLMHSurM2ETOhQeQxfetPd3ZhvGw1FbwHLZlpgKrK-lJswSsZ-5SYFGGfhXlSUR1Qw8GkDOvYzgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=G7NqbYcdw_AEKndl-sNLH3kNbjrLp8ZOW8RnJrIr4wqFiGWpELB_HPYnkyVv3ipRslXguI0UFphDHVORhLEGfIHsip1chImcs1qElQvYauc2kGZVkWjczWRCUzgF60yzL-D_L39zAiwUBaYijyYVVwRipoYetGNgAuiZTFdOXtqmMaXmtlIYrmcjudycKMYjvad6X3sMB6sJvDIZQooiIv7qANIndVO_MR8mcrBZPyMSASRC5_plt29lLZxs6J8UtQnMizBx1Ik6dJjaDqELUOAaQeBDaEtS2q2VklR25Kuz61gmX8L1cDh4EJx1bRd9_DuURJszuefKRUjB0HCE7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=G7NqbYcdw_AEKndl-sNLH3kNbjrLp8ZOW8RnJrIr4wqFiGWpELB_HPYnkyVv3ipRslXguI0UFphDHVORhLEGfIHsip1chImcs1qElQvYauc2kGZVkWjczWRCUzgF60yzL-D_L39zAiwUBaYijyYVVwRipoYetGNgAuiZTFdOXtqmMaXmtlIYrmcjudycKMYjvad6X3sMB6sJvDIZQooiIv7qANIndVO_MR8mcrBZPyMSASRC5_plt29lLZxs6J8UtQnMizBx1Ik6dJjaDqELUOAaQeBDaEtS2q2VklR25Kuz61gmX8L1cDh4EJx1bRd9_DuURJszuefKRUjB0HCE7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=fW1FIApHkew19hR6USqKnaf2Rg0Kg1KG43Tx1BeY_He2v3MyKLrHjDLTVnXDp_gsnIdxIKkEVLXUli_qQdlop39QJOx0izD_X1brmeXenKwzjluGM33ImpdYedE6ylLXWxK14-5Qyih3jqFMbMb_R9lnNbUmu1-v32kC_ZUN7H8FnCJWx__AqabdnK78YIqdUIKm8WqBzV2RdCsTUAUF1ghfmc9esISv23mJpb2R4iybcb52__FY2LFQlLqh8rFxUHUZz7knZIhlMDKDg5SEC7WshJJvTQa7OW5TB9vJnrbxPAWmaMfa8jkcYY5vrVmMYqGoOIX9tNCsp9Jtz7Y64w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=fW1FIApHkew19hR6USqKnaf2Rg0Kg1KG43Tx1BeY_He2v3MyKLrHjDLTVnXDp_gsnIdxIKkEVLXUli_qQdlop39QJOx0izD_X1brmeXenKwzjluGM33ImpdYedE6ylLXWxK14-5Qyih3jqFMbMb_R9lnNbUmu1-v32kC_ZUN7H8FnCJWx__AqabdnK78YIqdUIKm8WqBzV2RdCsTUAUF1ghfmc9esISv23mJpb2R4iybcb52__FY2LFQlLqh8rFxUHUZz7knZIhlMDKDg5SEC7WshJJvTQa7OW5TB9vJnrbxPAWmaMfa8jkcYY5vrVmMYqGoOIX9tNCsp9Jtz7Y64w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=C6wRr7cm9SXDEc7s5QgFuaRlFRxCxo33HtX29zML663a-VLt4JURKzW84LipXdzEZYLH_7_zPTESczHhZsANHT81Vwt52Pvc0X6v9MZXv3GfpGHmkqSnXW-oQBDpJnsIICpCZAjn4Boh6PD3UNrKymJf0vPN385UEoJJaDKD0lzST23sHnyuFIj1ToLtGZZWwBzcfQTdHZaI1S5MuqfpZFF9PPHZ6463fFeqf7ajZSudadj_yh7KeKes_1AvB-t_1HmUKNyedKWAldUVMYmQA92UhkVkdl9TI0-OKxmBnDuwHN3BLZyFkDKsJm4syXZT3o-S1PF7EtQqRb3twRT0EQZ8_7jWPjlKbgqPbMQQ2ey9oWMcw2TRozoipbcCt8VGNHwoq6iYwPChIaAHXrtAeXEghMgeALxXFbZYB3J7sYbkcgrbYrExdq6sUBWOfYd_TvXvVtuK_7Q2s1hN2QAe1Eg2_ZW1-nWEha-Rr9AvtHqSSWuMl1RWTBWY0Dc4kqzJTW4wlbBkilVGNs4seiw-xqJADFcUrDqyIiLHCsNqrprlB2kGdnq7i8mZRwgefNdl9U6AqbXyijfzlzo0rIpHXqyWJjB_sjgtQ5lK7EmFUkFmxQOikrkZPfVYinJesb8x2YUsgXgZgRDTdlP7mEmkxefa7sRCQv4MVCEd-vUYALA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=C6wRr7cm9SXDEc7s5QgFuaRlFRxCxo33HtX29zML663a-VLt4JURKzW84LipXdzEZYLH_7_zPTESczHhZsANHT81Vwt52Pvc0X6v9MZXv3GfpGHmkqSnXW-oQBDpJnsIICpCZAjn4Boh6PD3UNrKymJf0vPN385UEoJJaDKD0lzST23sHnyuFIj1ToLtGZZWwBzcfQTdHZaI1S5MuqfpZFF9PPHZ6463fFeqf7ajZSudadj_yh7KeKes_1AvB-t_1HmUKNyedKWAldUVMYmQA92UhkVkdl9TI0-OKxmBnDuwHN3BLZyFkDKsJm4syXZT3o-S1PF7EtQqRb3twRT0EQZ8_7jWPjlKbgqPbMQQ2ey9oWMcw2TRozoipbcCt8VGNHwoq6iYwPChIaAHXrtAeXEghMgeALxXFbZYB3J7sYbkcgrbYrExdq6sUBWOfYd_TvXvVtuK_7Q2s1hN2QAe1Eg2_ZW1-nWEha-Rr9AvtHqSSWuMl1RWTBWY0Dc4kqzJTW4wlbBkilVGNs4seiw-xqJADFcUrDqyIiLHCsNqrprlB2kGdnq7i8mZRwgefNdl9U6AqbXyijfzlzo0rIpHXqyWJjB_sjgtQ5lK7EmFUkFmxQOikrkZPfVYinJesb8x2YUsgXgZgRDTdlP7mEmkxefa7sRCQv4MVCEd-vUYALA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Pa-PPMeGKJlJZ1fUyadbmJbA45oFMSBVu9qinq7-GbdyX1p41BjVftA0IVMPPQ8ogZNsqzbaINBusfsT4wABliYJYMPxVjj_jd_7aeYwYZS1sQIzorijFiB0Xgw7wkNIEEr7xDTrZ9wNat_WhOqABIU7ciqTv4d3b5XOHvHsoDlEuPqcGD9G8J3c8HPrN_BENb6oG7jOQM4jaMmvdNTKKH1LNiPQ1PIwGPpOKq9KMweeOrHrk6Jvrbj4CR9m04DG1vLg-k0h9_KGOPAfUfY3qBXlG55g4C8pOSSO3VJjatSdf1ACsD46w1a1nz4donJdmVvnC0U3SHIHXZqMJYjjm5Q7LCk5nJ_eHHsqolVEa-ONmIFA5KDzHQlPfTOvYIEAGnxgtzHlPHC0HS3SEZKbOh99X0LwMCqM8YikTWO3RlOgZs69XGsQetE8YiHdgwBMMjEtyDVGCJ9hU1tYu1RObaJAHeUc0fM8gCv7o4eOPt98zELGOMrzund5U861VXWNdKJr7-8JWMSJCPlhd1x7RnMKTX_BPRR-5V6cf2RWnq3NBnFKjkHOgbX41272VtAENnOd97CcWScsmlGwqA17Kxz7rCPoDCG-ynu0oSnW3bTvmk4RBkzfaRMukgHcHS9ozRwoYDQnQV7WyQTdk23d7FinA_ozt85uecrUpzGNB9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=Pa-PPMeGKJlJZ1fUyadbmJbA45oFMSBVu9qinq7-GbdyX1p41BjVftA0IVMPPQ8ogZNsqzbaINBusfsT4wABliYJYMPxVjj_jd_7aeYwYZS1sQIzorijFiB0Xgw7wkNIEEr7xDTrZ9wNat_WhOqABIU7ciqTv4d3b5XOHvHsoDlEuPqcGD9G8J3c8HPrN_BENb6oG7jOQM4jaMmvdNTKKH1LNiPQ1PIwGPpOKq9KMweeOrHrk6Jvrbj4CR9m04DG1vLg-k0h9_KGOPAfUfY3qBXlG55g4C8pOSSO3VJjatSdf1ACsD46w1a1nz4donJdmVvnC0U3SHIHXZqMJYjjm5Q7LCk5nJ_eHHsqolVEa-ONmIFA5KDzHQlPfTOvYIEAGnxgtzHlPHC0HS3SEZKbOh99X0LwMCqM8YikTWO3RlOgZs69XGsQetE8YiHdgwBMMjEtyDVGCJ9hU1tYu1RObaJAHeUc0fM8gCv7o4eOPt98zELGOMrzund5U861VXWNdKJr7-8JWMSJCPlhd1x7RnMKTX_BPRR-5V6cf2RWnq3NBnFKjkHOgbX41272VtAENnOd97CcWScsmlGwqA17Kxz7rCPoDCG-ynu0oSnW3bTvmk4RBkzfaRMukgHcHS9ozRwoYDQnQV7WyQTdk23d7FinA_ozt85uecrUpzGNB9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HLMoJ5HipIAoVZkK2121yq9uCQI28raKDbVDoG8luZRQ3vssTzJN3WoX2u8p-jp1vpTlGCLsxvAWE30_kLkzWlCsehdYvMnhF3Z5alB3llyxY3V11t_EGnmBRZPYdGjbgexo1uKdYeRT0Atc8-ZA9Vidj3DMFeTBBWBk5XLtf84A-NZyVSRhDS4PKknB1i-ETDB244t3H86PwogL6MrdQFqDSm3Z2wkhMqNbB1RKUMHpROlnuul0hEq2QPSaKFvitafmSKgrUZ9Zigsbbz0-2PI04dVMhp5NWyGoMY4JMqCMZ7g3kNYFyDMJZhAhT9orZo5NfFLsUYQQfpYhJB4q6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HLMoJ5HipIAoVZkK2121yq9uCQI28raKDbVDoG8luZRQ3vssTzJN3WoX2u8p-jp1vpTlGCLsxvAWE30_kLkzWlCsehdYvMnhF3Z5alB3llyxY3V11t_EGnmBRZPYdGjbgexo1uKdYeRT0Atc8-ZA9Vidj3DMFeTBBWBk5XLtf84A-NZyVSRhDS4PKknB1i-ETDB244t3H86PwogL6MrdQFqDSm3Z2wkhMqNbB1RKUMHpROlnuul0hEq2QPSaKFvitafmSKgrUZ9Zigsbbz0-2PI04dVMhp5NWyGoMY4JMqCMZ7g3kNYFyDMJZhAhT9orZo5NfFLsUYQQfpYhJB4q6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJkQuDJjttRDdd7pDCQSuqkl1Qi6OZGJFvs7L4wgfA1icsUyxaUJ3zitNc9tUPrUnCYz5QQHYNgO-IRpnBdTnAhOKIM3lC4Gyu1auuCrdnE9v7sdpQjyWMH9N6KSaWHJSOprA4pGDoRpNdeEwCRGwX06LXHaD_Y_8b2GVFm3NJ-1p4x3ACOg4kYppAiUW8rSidnm9R-pVis9CbYvreS1i0rkzoCh3H9RYacc3obHRXi3dos64TKg9mMn87ykHa3Ek9v23K8dPBe4NeJEyM49jvFaFwkDg5LGE8qmJdXPuH4RWxtdYpSCZrgcJa2Yg2pbiaW6lGFNubqy-GNJMR1LMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VEpGdz2ZDhJ790JAHRipQrPWmMluyktM96MJlHZ7VjXeb6PtSJ296PdaOYWsIOrEWz4LBKA1ZKcLHcuz8LlvZDK6V2I-HS5QzggmzkT5UnGkik11B54sjMnwu2mBLQe6daShpVvp_h6lUDDrOmJGMsC9oUsJ9F2l5FuS0j4im98FWtcOhWY-hZXO0p5JEAqUgwTQn-h4NRkq6DoeHRLlr_v01qYGT1GDMfj5lYBv_j7_BKfKmqGq5MZwwSDkeCTTMH4pwFaopD3uiZm4s59bAHMgTw5ppQ4XeI6ECwTDX5NvljxxSQOVu-9KZAI9dNE5LaVKvogjL9jeQDoQI5aj3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=VEpGdz2ZDhJ790JAHRipQrPWmMluyktM96MJlHZ7VjXeb6PtSJ296PdaOYWsIOrEWz4LBKA1ZKcLHcuz8LlvZDK6V2I-HS5QzggmzkT5UnGkik11B54sjMnwu2mBLQe6daShpVvp_h6lUDDrOmJGMsC9oUsJ9F2l5FuS0j4im98FWtcOhWY-hZXO0p5JEAqUgwTQn-h4NRkq6DoeHRLlr_v01qYGT1GDMfj5lYBv_j7_BKfKmqGq5MZwwSDkeCTTMH4pwFaopD3uiZm4s59bAHMgTw5ppQ4XeI6ECwTDX5NvljxxSQOVu-9KZAI9dNE5LaVKvogjL9jeQDoQI5aj3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=WW9XSsk6Df8GHcynqfrpBUKTCWue1WRm1bfe3KrO15Nh8Yc4WqQhymCLd9P9YXzEUDlmTF_TiI9Q3nleJxD3ecUgNjkPNTirzL3wA67BLPFL3pAjLMJQ9IRpKU2a0GlmK-qnG7Jy3fYXHePvYNFmu5Hmx0ZDOd4kvODK0BHR2tnsMUrtSN4HkBdSp7HwjkFi80iSBvLKMCam70JbGy6h-FrDJrx2vhSWP2X6aeLEJtbDjyVKavAZSh1pNSjZGIloS-q8xeE-HWlSU9j-38tRSlEHWWhtztDwI9B9TF1261-OYRDrS5th1rXzVFGDH6PLcu5m9tTmwmkou6VPgBk53Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=WW9XSsk6Df8GHcynqfrpBUKTCWue1WRm1bfe3KrO15Nh8Yc4WqQhymCLd9P9YXzEUDlmTF_TiI9Q3nleJxD3ecUgNjkPNTirzL3wA67BLPFL3pAjLMJQ9IRpKU2a0GlmK-qnG7Jy3fYXHePvYNFmu5Hmx0ZDOd4kvODK0BHR2tnsMUrtSN4HkBdSp7HwjkFi80iSBvLKMCam70JbGy6h-FrDJrx2vhSWP2X6aeLEJtbDjyVKavAZSh1pNSjZGIloS-q8xeE-HWlSU9j-38tRSlEHWWhtztDwI9B9TF1261-OYRDrS5th1rXzVFGDH6PLcu5m9tTmwmkou6VPgBk53Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYXZ4424YV5RHyT_zlJ_sns5O5BBJhQMolSjLHPQQv9kDANLs6Ar0lm9uwd1D2XwKWBCuBwlBIItarIfc4vo--Yvjmznv5mbmQTRVZNUp0FvlpQbNoFlPzY9Qy8gmJNsEOu46BN5IGORlLxkVu-wC0-D9wKJuRu7tPy0FNaLzYt36thU0rdTDp8XYbCd_8xmdHSNhZRQ5KYurZbOoCJEwccGD6eHZjWHnUbEtZGQ0b93rRCMWPUqrtMI08U_DKOx-StwFUJhG5wXHNuF1o3h-lpIFMotPlQc2tJVV8RtHnzsYfj75_0R7yFbcJWuDtKEhy5YvbK1dwq1o9rVo7Cs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWpGyUcD7-8Yrod8dUA1-GVLshXqKyaR-d-lk0EQJUH60HA9r7oVf0VYkJZpxEtiZfSohM-LKUNq5Ll6FN-JcYrNS2sMXGb2_mxtH7kxDjQpM_f7dkjBgIT17AzmJguUzlt4p0II1183nud5A5t5LpZITgOxuRqYgwd3Hg-jko3FLN-XUz9mTWfu0e8c8sSi4HSP-TvYkfP9Orkg5fqlC2NkScmGZ-ibIaH3BEWDxi0sPH5GJvfZC0pBKtaaiec0RnAD4SAwyRqsBXTwBvnAtXarMv57MZTnZf9CzXQtTzfpNh3S35HwLUULmIDdteyu1m5MzlJs90SPBzcw_1aHbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFnjRnyvZCgJEOmn-m7y3byF2ScE2CQnOsCF43-IBUVPYIX2fqGcL3iDGtgSL7ED4N5Xy8T6jNuA8JffPWrPFxJaPtmPwdOV-oUg2tDGB_HUvopwk7Nx2fBFosvs1aL1Kb4pMtBk9AoGZHC2CR6Cqs_91lr_a_0FehTRtL6EpBF24Psg520E66HvUKD7v_0MGWlXIFwp8OWkWB3MkXAKsI2IIL05oruh8zgZ0yzppjG863PL15CjAKjhb00YfpfbnIB11Lm30L9VTxGNOrbNwNOOFDlVEcWNpLOvSA_wAeV2WELp1fZbbzDYm6ui5rEmZ-jweSF3mcT_ONU_6oZN8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hbj1FfAfzm7tjrPWJVKqruym0ocVBeY04xY7SKSdz4KfLY7Kfsqme1YGzdblyGcLGLX9ODQ-v1ttQY8wuHjliMnyRKVRz7s5Z6omnP8OpycLWh0-AN5mmI4dmRKktv3ZIS0J4D56HeZaMhlKvq9TTdCK0vLKSLIu8RR0MegslWwnN8cTho5JIRdKjzsABIqnsrUnTMh9I5jM-13h1bW3Rl2O1t_0YDZzOVplsBt-k8lmnOlCG_j-YgeLuAlyVRKaEaWNiK8akYjUKRdZCmOd6GPp3n_hXFvuYauLBl7Xm-8_0ZHyCn2uVkMk2N6AR1r1CZr8AidZvqxny9vfcx06Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IKiNMJc2_M3SY200LQfCcqjOgsEoYABWgO0qyTYfRhGWB2SVuRRZMm-dZ_QaVZ4AeoUVFFw9jwuIuEykrv5lLB_7jQWgjZxA8mQt0i6YrmNvpO5zFqnxpNzxKMAGzZ-NgA_fDW2rBHQQbwJAmc9HXB3sVWA7NDxiZe0BB4x2ADg3vK7RC1P5Oj9G6_QTokVuSdnRcMlv8fXO1Bv3hXSzJvwbfvVu9sHrsolPjGGF6sQGoI8n8FhnyWCx_9d8V7Fde93VxKIqWPLhzeTxFhlrvVAsYFQjls7pDhE3HFhqCxzShVANdMRhuy7j_icrxRPqsjh3Ol_vC9Ji2MXXCaidYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3ESFw01ht7UaS42dO_XUoZl9dfcoRcksJ0ufzZg7IiSIrKMvpNYPJgcqfaS6PtBzPFpF8URhnddszvOnI-mJlbYRWPrEsfFdjxxJL1MbmweiWv5XiktDpNKJ46UZw4fxsscEU1CdzMg-QYKWYzf1Er1NQEMXdU7YAw15ZXIuj6GcrlDL7nbJW63SgxbRJdxFqFudW8csdBsA-LUElXMp-9-JuAufkvZO3lWC3o3lmi0uFGcnYUUTU83y8Vvf2Skx-V-dq5QKMCCKiJnDayIXas8lSID0_sBtWVGo6O4-JZRKw_0ao0s6_b1fAE78HBEoVtb2KQgHW3VrcpzUo4qJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4c-1U1KE1QkdIWaNztnjS8a0xJDSvyVgRKv4-8fS4xrhXulh0-ZO-sl0pSALjw-u5lrDXjr7QYDcQ2qAJRvTTyTPC3z1BVJkEunlIKfEMDNBWAc3V2-RSFh2doNUzr8C4bIRf9fpk9-0nw71cwpEyLoRoubSUGyKZZwkWVzr7-uN3rF7GxcqHUHXJOGfHWlh3gF_XdH3pPatHw89L8OEFFaT7yg21ObTTvswjtKck2siWCJNoKyt1bALEvTIRlpRn2nt0TcHjNdoe1o3p37J45xzsNZF5vZuLzXgpMqIAfx8EwD3TyfU7p1qUppVYw8TQwYjLG09qhHjweQFkODbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i0DkN_QOPZzvtxLyO43Q7ikdSg5Xn0ULwogboYCl9A6Zu-ZstwuHm8tJiDg7ZBBZs5ML8xNX9fTDZbRvk9rDBB_CL848LOrPun5KZGSMT2SS8xmrhCMxZmgFIGu3vnWUzb2y1ryu_uKiAVv1LiHw1BdFIUCMA1sqPXhGl02dObl4jYkz0w_A4Y8aT3lG31qZpCQ8igSDXu5Aeejay45CfgT-lhGr41zi7cMO9vg59GrmknMPyLCgRcp0H9ajGssiW5qUbniONrcB5GeshimWp2YsCysDsbIF1MjT1Ngi6hTrXTqMLpV-CEkZSmlEZeMTInXQIspLQq3iSi_MYU5FuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NkCleuf-_PcLBES1zY5AwJPKSN4kXC4XAMlY3PBPfcM_0pG5YKOksmA9W989xnXavjlypPADwyF2bN3jP-NijFDeUYVNcSDq-vLmblt6G2UDSUwOT7vw93WP9RVO6FcOX7x_0IE8TTp4WU-S6TaDrfzwYt-kVhPb8N24dyTpVt6iqFQo_ppi_QSrsC66m1xiT-2g3WwTqZp_DYyDAbX8BDRsuz3pq1Q1qP3NgsyJT1vT3atvEit5WTznScrTrI2yhIEaElmAz9g0MudoIirRypRD5VJOZYokG3SMdzrC33T92oDvTQZUchf9ULfmWTJlIyIKN57CdTWJ9hB3M8yPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bDPFS5DpLghS-aTz-Oyk9f2mPYURFNCQB6rPuikizhzt9WYW69vAPHPLa4Jsrvv2-qu9LZ7azxx7gmQNARkzVRQEq0rTQcmhasv8-HuTzq8xG045fyHV6AbiEqjj0teN8uYtBmtDhogfrZz3yZU8DMICWyxEzE0y3R2SdN4PFhY6LieVLbp-B9XtSNOYqlG8Ga17sUxXUtRiumcdxmO2e4eEo_-1e-_wH8ZeKDIfiaWbcyRSZ59fbpSzND8brSQ69kCQ3vhqVjvkkcGAbkziVuDvjvbLphDoEIK4RNGmd_mVvGlfyRPJ7LGQsPmvi8JtAM5AiEFmZqEQTwlepo78Ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=fukrGXP8ujaZ3uMh__cU824ZCAldVpS598Glvz0bPS0lg4A8KVGOsqph-sjcPW-0Z7NT_jfeAr9-qS8MUo1EeuSefSMby818AJNwCLkZIriwobimeDsMNFSRWWcFcucP8NvdMLtLj-2aN8k8GqSPLNLS05U5DMx2CQY0U2i-7XMz9orklwxZFzJsyMfDrdLiuXP99ukyAd_NlTPZwRYf92T82sgALkulo-W8GuwfsfycNnNkqPkiuCmCiRdD5xAmn5okLA1Hg-xW_EVUkdPi_ibceIVd4ePe9O5Fne0heLLu7X-VEA-43zFFm_YvuI5a5IbaEIjC17TUdl0nN-yR-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=fukrGXP8ujaZ3uMh__cU824ZCAldVpS598Glvz0bPS0lg4A8KVGOsqph-sjcPW-0Z7NT_jfeAr9-qS8MUo1EeuSefSMby818AJNwCLkZIriwobimeDsMNFSRWWcFcucP8NvdMLtLj-2aN8k8GqSPLNLS05U5DMx2CQY0U2i-7XMz9orklwxZFzJsyMfDrdLiuXP99ukyAd_NlTPZwRYf92T82sgALkulo-W8GuwfsfycNnNkqPkiuCmCiRdD5xAmn5okLA1Hg-xW_EVUkdPi_ibceIVd4ePe9O5Fne0heLLu7X-VEA-43zFFm_YvuI5a5IbaEIjC17TUdl0nN-yR-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQdm5SGtpouQOjUJS1DnvCpXWXHNzIcwLi4xLuFNlKQHKdYpvH4fxzlW41_zhpWFQV6CsI_lo3y5zzlkItt9j8suV0wm2YJOC07D2IbgDEXsoVEcOQFON0l8tBYZToMomwMWHNFUPyY_3IdWiI8qbM55Ezbyj_BK6c-ccU2exlcofLwvt5loSHbywQ82VjIUWiDp0xwNGCm_bHiwHc-9X4WsH7hXg2V6XnYq06LvrzEkng0J8VmqJh7MavwBJ-om27Wy20DonjFeHB_lAh10rQ_fHbtnDRn5-TLrx8Q6jIV5VSo-Q-YQGmgwX23E6XC4P_yll0GTb1MWBTMxleasjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrWhUBFYgYa8WBZD5CLcLPjmO3t8oX0LsjK8dE-AAuN6EAgr8N_cEbCraPcAzei3qATBq4RFeF9EyoKce5_DgECF4nMH_DflnByX1hemHrpO7q44wLds9ODE-MeLS7VGM8UDg2p7ABdVxnkPpUHn5dlyu75Jnqfyu92w1Jj9X_NGD55LNt5RgEnnIq27dAkTIVuhMie-gpuuZnd9bDZJNoLCsq9Q_RCF9K-FffH-J6g4GMrovGUwNCQK8D_1eE37ow_k0p_dW34gdx9D1Xwx52cupk8HSZJdPCs9nHw94hB2BZVNzWi8dyEbCvoO304aVyScqQRKxdkK9f7frZVbtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=loaosdSgOoQgNOMsZISXeIr5Mm1x8g4fZD_o4cTznA3xYOHBNCh6wcYrBp8L9-u8vlmdX0OjHjzEngWQrKMKpMtX1bdW_Uc4gDyxGTH2XSS2NAl2bLasP4CDEIAebwYgG7kMNRpaneOPNq_RcHUFr_ohfzug8NvhJloHnQpLYNnxXVa1udfQeiua3W6bPd-Pjt7YOpWWcAJN6_c_40GOZ5R_NdLzRNCXgk0bFdfQjWoUaUYfVk5Ej4AeLdt7O63UyOtJSHx2ysXlWrr0PDcwo1T40mRjGTlcQms399LnnxSYpKGPCmNP9CklAags7nWVS4Y-AOpEN3BDUXd9EPQ29Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=loaosdSgOoQgNOMsZISXeIr5Mm1x8g4fZD_o4cTznA3xYOHBNCh6wcYrBp8L9-u8vlmdX0OjHjzEngWQrKMKpMtX1bdW_Uc4gDyxGTH2XSS2NAl2bLasP4CDEIAebwYgG7kMNRpaneOPNq_RcHUFr_ohfzug8NvhJloHnQpLYNnxXVa1udfQeiua3W6bPd-Pjt7YOpWWcAJN6_c_40GOZ5R_NdLzRNCXgk0bFdfQjWoUaUYfVk5Ej4AeLdt7O63UyOtJSHx2ysXlWrr0PDcwo1T40mRjGTlcQms399LnnxSYpKGPCmNP9CklAags7nWVS4Y-AOpEN3BDUXd9EPQ29Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=f1DKYaRBDd5xqPEhwqhcemiMEDpsHUGgeiPPpV2uCl-eEdaLvzD9Vd7NV_CJque44o2W2NH5Vivc7BiZhzrQ1cvJT44NbxjFyf0gpvREbNXnHoDCR6IdsQByxfV6-8jYun8vvK1Auz65dRSDRbJTMgqL1FA6SA_IILiSNPkvSSslVMmg8CdFZoFGc4bBpS0gjGbl32Ic27SVQ3Q6XM0hp_GRmhUhEqtwce-EVad1Ezvc2dZRijWXr7TWgk3csgScrgG6-v4oWwhRet-D1gPyZykldpL8rS99C1NsPuAYeJrO0_9eTtLRnAx-ngqAZayn906kwcPKVPdAHeMDiVj0XA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=f1DKYaRBDd5xqPEhwqhcemiMEDpsHUGgeiPPpV2uCl-eEdaLvzD9Vd7NV_CJque44o2W2NH5Vivc7BiZhzrQ1cvJT44NbxjFyf0gpvREbNXnHoDCR6IdsQByxfV6-8jYun8vvK1Auz65dRSDRbJTMgqL1FA6SA_IILiSNPkvSSslVMmg8CdFZoFGc4bBpS0gjGbl32Ic27SVQ3Q6XM0hp_GRmhUhEqtwce-EVad1Ezvc2dZRijWXr7TWgk3csgScrgG6-v4oWwhRet-D1gPyZykldpL8rS99C1NsPuAYeJrO0_9eTtLRnAx-ngqAZayn906kwcPKVPdAHeMDiVj0XA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gTlnxp1H_cqrvk8eltyn44LAQl3-18jzD-mc71g_6IFm2rcMnONA2egqOFgyUfILgf2pzIu1yZqG3kMuEijen8wvTFFOmPLnbiP8hjFxOTi6_hVGPGO5EW53seokT-C38IGDLLGbAE4Jukzk_r3CXqKDFmPPk7HyjvBE7DMcnTCt9q5-a9suZfMBQghffRlwmfkWpbPOHartu3f1rnqk4u41CenXwcjsFpRo4noAd72sxWqOeNOxKHSV0wmXNHt-3zoltBgcJzt73iICn-2prRm6zmofMpkV9qUMNeTbEjp-hYmW744iqxeyu_J2ARbcpUN_SdN_FBSdMnNkp2AD7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSmJYcB0_2d_KMJ8p35-JOvhrFu2WorwoB4jGrRabdLUmeoHkpCka781-wARyWXqVi8kijJRFuyIGsJ8zeLVxPs-se_liRiBg3EhgHNeP-HS_vc9W8Fvs3VTkmeVXHVKEjRJDnye0BvNcZVcTwk-vIjw6w47R0ZsFjgwvJpS4x9CvSksES2042-_CTVRYBq7ws2RBkNd48NV-nzaVFa9p9-CfLjq0bCUr1ao7U7qwhMeMD8xo1IQiHA_hHXQkaL--G_DgkGVPBwb0KprRtgvy9bzbszPQAw0Nn9D-z6jNGQbvWSzQsdx87CIbfCAoPne-SL7ltR29aOJwfUcltrTJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9zBOL_4aVlqWE2q4_CLrFmuW0Pu0Xi9O1CXSrQqwEtwASG74wvvnNn7uWqZEAcKGLD6-D_8akdcLMy88iG8FUIiAKZZPb9C1E2R_QiocmOg6Xh5D4TWuvBfqQsl7J6qIUBPdYGg3APgYxobQxCVohyYRWmLlgAdM8Yt6pW6XgsRQ2A_exF8sXFh8UnKwSrbpMdrO08CHLV2oC4hhDaIwaO2W0C2OanX4TKfdddEHjNVw7xNAvpvmzvKE1C_Vv2k6GgE50gqYc8dKW_f4mrcNiES_QfCcSiO3-bkaK-rXNwMUfNZ4Dhs1IoIwX-3gUKSgdPJcGkTPA96EKCh2LYGJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CSIep_N4a3r3xVpyDfAdrFijr2AMNUF_nRjkYxREJ_wgNWvAgRTUjKzYf-szePX1WOoaedmJU0JAWoG6dOdPOvCvuFQkNlLtYIbNj8arER9SjLQfW8sMhHLP_VE2iWibXsxNEdxuXPXLHH3gBDht_AJt_HmV7NJnJok7ZNBmo062e8ThHLXknJo_HGlReBSIg4XjH2iMOQ7loTlCTIoJ1Kmng3OHlL-26X2vD18E6eMtdcJc2NA3XvwQNwE1wxALWGy_GE8v3ip4GoXaKLaztBiAs6i3a6hDYjnsdH0fXnK9tbZyku1nETeRepPaYuLfQniA-c92zZ3qtpMXb9JFiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NWx_Cy4SR0-W-3W131VL82HoaQsWKdo0jO63_tAn-8WUhXxYtC3rgH7onbm5bUvOqiqGH0fdgv3DNWM4R8OcY7hQXC0Sb-BWMDkwzmMOiccQlrzjxeGelZ7fIiZLXcbQyCoSAQdgqclM7tjcgMPkI2LKnqutDKSamRrEdaQNnocCla9CbbzBsOKmVgwlSZlr1ZiMa3ORJ3W3jHiRp8leEgLaibLNF0tPOKZzPIjDKmX8O-NyNVajbWe33N9-A-Asps5HDHfCaizjNcTZb3y5whN9dZQrFLesuTlSlkJ4AvFZvi5Vj2yxxwO4lkAFs8qMSfFyWeDFpOU8mlYNVEbsDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mttr-yM2uNZnSvi-8HdhFWFqA8A7t3t9uF6tgT19PPIMqtFsUUSapflQAzM-egeH1XUuuALFrMF6A1b8EaT0YT00fjX8qvM9RKpeqyf3gOmmR5kVanlJkQB8gkSbLtutq9Mwqjm74_ZgDCGIwmBP5i2iMsdmaiGYm0KZ3iEWFHGSWKRFagILuJrGXFVscNBw3xmwinBBiY4SqDm2bZCQ1EJU6st_tIuKJin_e2wuZznSG-0MF7e7rgTh78G7_xYYw_1qtEJ7AEe8Dp4rF9Rf39-aBcd2jRnjhANUkxz7pMc64o9sdbcfi6eQEm0xd0tfHK2Vjltr5n8nel_T1m1umA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRLv0aRiAElVobnREXf-hh0WGodwrUyySjHQnn_JNjeVKBwvNUyiC6ovq-2PMLXDhBUF9mPLvfJmZBvrykgD7Rhct-ddgxddbp0IocS8a941ynpT94ytZjX2uwVwioiqQxhKp47a9CvNo6fxeVM5NJDl2vrfeVBRt9l6M-0NxeK_CkIg-SBz-IMu3RRx-376qJi7aZsCyK-OqOwNNZYx6JDNd2sA_m4eJje3jjyyO_4uMJDPGSDP-36ECS1N1UT1jqnHenNBBRdQ4uYwAct_Q4481wEu2ghbpQH1OQqCpzxM3Butk0KE5lNYdcK4cDwIwKpyEimjVy9bB6DZr_cXFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b7j-szBwbOXL3BhFby5pc0InMoUs3O3vtmB0fpQb_faxFEqjXyY81Vb9uGjCczWSuUz9EeBo2_wfE9TVy9cDVuLsfULNG6Zh5hjGPTDT1J0SGXXGMth0CfvPgTzojE1NYGcfMrMMs_nBV9ilh6mmDx-Y9R-Vac4NCJ1m0yXioOXfvKHoA8bPc7IMBwJ7-TfqWzNLEd506dWzOTAsaSlmRc2CNYUw5fz0q_gUAaii2uSIJb0TMFO1LGFyS-LphbE-m88hFYOmoDawTbrQ6QibF6jcHZG38HOQK1QzHRLstkeQXl0DuEdGIATgX5qMZXo4UQPx80WZVYGJtUBgwU5BSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=q2TRdl-W2L5PQQNN13PIhKkM_qVVQT3j9v8169k9GBGjwRD__hCsMHenSRVbf1RavDbCJXrefoypl-rXKJ5v1VHFw7vn3HkCbc71piX3kaaCsQgI_XL5QAkqgVHE8HnKaKXaRYLLpp6hYpHOylM74STaDufFsMu74fknb_iDSIvkX2dxc2XLqR-kr349EHnGLMM414gwWJcdIIMadB0uGhkna_RVjCewVMX6Tz1Wr64r4kM6On_t0ff9WIgUXSXrbWGXzXDaxm_MdBh7sDS-aUPsPcKyvab0uy--BiXJGest3jwNAxJxvZuN2INYuUoO5EMyZ8CIsCJrsyiS2A2vMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=q2TRdl-W2L5PQQNN13PIhKkM_qVVQT3j9v8169k9GBGjwRD__hCsMHenSRVbf1RavDbCJXrefoypl-rXKJ5v1VHFw7vn3HkCbc71piX3kaaCsQgI_XL5QAkqgVHE8HnKaKXaRYLLpp6hYpHOylM74STaDufFsMu74fknb_iDSIvkX2dxc2XLqR-kr349EHnGLMM414gwWJcdIIMadB0uGhkna_RVjCewVMX6Tz1Wr64r4kM6On_t0ff9WIgUXSXrbWGXzXDaxm_MdBh7sDS-aUPsPcKyvab0uy--BiXJGest3jwNAxJxvZuN2INYuUoO5EMyZ8CIsCJrsyiS2A2vMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HSmuCg4MyUtSdhz-UKM-fQekzVqFljsnALVbu-ICwXNJ37YgqmcZCZM08zfvtBto7TsSSWE0Rjqp5JDFUFzDPyayEzDwbT4ksOBO9woVjwLaAvIu03393BDUigCf8APwLUHBRaxbHsPw3Hhjkp9ekMQ_h8i1TDSgi4Pt5jNHVRIb9a7Mr6hhkpWEV_0DKVR2Q8FvV-Laz9pd42Hhs2iK-cpMqka1nQY49CwZz6KHqAdS9RfC-Xp1z7a47xSJNhirwQfz6abzqWDkwI8cbQWUf2nkHoyVohk-18atsLJB1JIur2LWhQhn4z76naLZew55Rcxs-ZCOEtleGjdErGao-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=dO08t_xDGoTYoKI3hkoe_BMpdPl2LS9w_mAqvUM9D1zXIHJuV8ff37ZkpZWFc4Fw-Y5K6We9nH58B0Yqz3LBjOmT4VO8t6nbrcr3BE_4CV9CgaX5UQXcKAmdFwFGcDwQcQD2PO8L4BQnADA8vee0mVtQXQ9ELOlk3dTlfm_88EEGzwGxuzdiab25ZiV2gmpjild0AhliFYwfpzxkr3Zq0K491w55mzbMyw4vdCtQwKoXEsqdvewvEKaAK-oMASWtvR4ATVuli1wTZ8RAc_p_cTBRSRym0hSRzhMYO35JOcqjpfni0LAoTKBqInKzpYex5bKoBOG3U_ClF4NnPJzSWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=dO08t_xDGoTYoKI3hkoe_BMpdPl2LS9w_mAqvUM9D1zXIHJuV8ff37ZkpZWFc4Fw-Y5K6We9nH58B0Yqz3LBjOmT4VO8t6nbrcr3BE_4CV9CgaX5UQXcKAmdFwFGcDwQcQD2PO8L4BQnADA8vee0mVtQXQ9ELOlk3dTlfm_88EEGzwGxuzdiab25ZiV2gmpjild0AhliFYwfpzxkr3Zq0K491w55mzbMyw4vdCtQwKoXEsqdvewvEKaAK-oMASWtvR4ATVuli1wTZ8RAc_p_cTBRSRym0hSRzhMYO35JOcqjpfni0LAoTKBqInKzpYex5bKoBOG3U_ClF4NnPJzSWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ZFtYzFNVFGQP-5xlvbuev8qNKz_7F4FlpOnIruYK9S0CvWkr0QW8L3B3eAq3cyykBzmCJqTG_Us_thHmHlBH3PrGUuqbQRUG043Wyj6ARbtIjv_rvBNxdJOpNXcyg0K2j5uyxAeWbdTD0RgjFC-TOKJdBsSaxumNUugQPf9POQhKf6_epEdfyOdIsW3nsZ43KDku6O5B35_0uyIWH3GnPPOlBNYap-vcp_FOQEunmHjKpS6Um0DerXpHFBich163oXusCWXH6T-qHpHy9yAyd_9QQNXx12IMzpq0o1BJ7g8hOaza-Rv8mGiZp9WxyBWzgqFMFj17mufc8lmOHxtkgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ZFtYzFNVFGQP-5xlvbuev8qNKz_7F4FlpOnIruYK9S0CvWkr0QW8L3B3eAq3cyykBzmCJqTG_Us_thHmHlBH3PrGUuqbQRUG043Wyj6ARbtIjv_rvBNxdJOpNXcyg0K2j5uyxAeWbdTD0RgjFC-TOKJdBsSaxumNUugQPf9POQhKf6_epEdfyOdIsW3nsZ43KDku6O5B35_0uyIWH3GnPPOlBNYap-vcp_FOQEunmHjKpS6Um0DerXpHFBich163oXusCWXH6T-qHpHy9yAyd_9QQNXx12IMzpq0o1BJ7g8hOaza-Rv8mGiZp9WxyBWzgqFMFj17mufc8lmOHxtkgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0iXuQZ7LBYRPFBwn76o2Uicjn2RI6AgSjwvi31MVNsOa0A8qQRseO3mf-8_3fgmm2s_vUsj1UHHo5_7TiEjZ2NN2LVi592wcAJwbjutvCFvtmtnlY-ICVwQHx1jYrRwCsLYx6iqulhY1z7YWOM5rceTAJnugp_bdJjKod4l3Yoyp_OpnPkmXXhbijJ8WUyHJc17hfmhLpINxqv5JAQe8mfOPMVEdhox_7QnpS-KgFu5kEs0qXWJgTSUlLzCeuKZUYwcJdUEUnXMoQIDXOx630ymSQwPS3ik8EurwkS1wI_sSEfU7nWcwVkAXc4eG-ihxHflUN5--Fw2rpTgOXVC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6lrU1KximmuF4quQXnvpmud6i9kFTvzv25n9uAe90qdmuN1l_qLQhRgJcLLqh3rW5sbDIs4GlJdYxvt_UxGY7_lviyjh1dv6GTFVrpgICugXj8zexM_dWY3NQ4jmstIuay8E_s7BlEDv_EHriX4IrGznhMN3Bke6i8gq0BtgNud0cZi1dgaoCoEJf2XFHSP_jhciuyqVe0cIEWReq6EIsbY5-lU66iJSpRrjUjpxyLB8p_TkGojWBci8MTwdTXNEEFM2sBSjkYTDhAUt_aqB9MKIuAk6v0-stzNTCZj3P9Y5sD59-eqs1WiprJEcX4z8CVqJedBO_K7olxAXTGKKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
