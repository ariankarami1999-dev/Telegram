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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-27 01:20:28</div>
<hr>

<div class="tg-post" id="msg-6748">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67af3237af.mp4?token=B6sBOdloDVnhFoNbX2_BINbCqZQN3ujpyPB77xVLFnOStA572M3EyvsvfnjU7yxjVoIT4BZyqgZb2ZJnB9zALHyxboDe46S94zHEXk4_BHYdgCEDJa9KZ3kQHXEpHmFKhc1FGd6EWq8xHA1KQHcnOxaixVENkjkYV-xBlVyEwkJMUztMq3r6K__Cp0KOCUzJtH30bYa6_-WjIwpAWs6euV7wh3oRPJmfF1GypwXUrtlFIMBpnIC-rSeGo64eQkR5zzZPdkmLi6s0WLlP7ewkBOHEIRuc-7Ec7NLKkpS-6beavq_3uiHMrNoogKtXW5ml9WXjoMyVSF5i2d2Y-iDu_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67af3237af.mp4?token=B6sBOdloDVnhFoNbX2_BINbCqZQN3ujpyPB77xVLFnOStA572M3EyvsvfnjU7yxjVoIT4BZyqgZb2ZJnB9zALHyxboDe46S94zHEXk4_BHYdgCEDJa9KZ3kQHXEpHmFKhc1FGd6EWq8xHA1KQHcnOxaixVENkjkYV-xBlVyEwkJMUztMq3r6K__Cp0KOCUzJtH30bYa6_-WjIwpAWs6euV7wh3oRPJmfF1GypwXUrtlFIMBpnIC-rSeGo64eQkR5zzZPdkmLi6s0WLlP7ewkBOHEIRuc-7Ec7NLKkpS-6beavq_3uiHMrNoogKtXW5ml9WXjoMyVSF5i2d2Y-iDu_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فیلم تعرض به کودک در کلانتری
نیروی انتظامی جمهوری اسلامی آینه تمام قد نظامشه، وحشی و عقب افتاده و‌ خشن.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAxG7YVglpKQtz_qUrBsKIJd3nODp0ZJiY-DznNOM3kH6HbcPosYUQpEUNWUP1QcyCw0MgckB8YKn_v01wLTZA5SAB9zJNln0ZctPhRlY0Jj2M4A_Dd7SmRJ76ARYFVXN9X-_-BepEixR_2QfctgljAusRixVTWbuq0BhwpbV84wm_F_jQtUrOcPXkD2Bbgp5XDA_Ivf4jyL6bXppRviVhMsGO6NP59UVcBdqvIeraJlZhaTTrxD_hOXLrigsbnOr44RHmCZoH9stUZSxxYwEd76xN_63NqFpqbXXdwAyDjGBy9_zY_2D8W7MT29xP0DDH1TdVvxnNZmXTP5CKR1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6746">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GpTI1WWKVwYi7f1p3CfOJkneJhCqt1DHZIvfIhxInyi_ET7VkhYvNT-Tkm7TtUTXlfEkHtZlcwuPDbuq34sK0_A9whkOO81YC1eCq8y6Vq3aOfY-ABEpa5jOB7w1yxO1JV1WS7Nw-FNQ2R-bh4RE8djqfEmWy3HQa6sMikLaYfGgX9ZEw3_vJtvcM0SP5F1kTj_Kn52Xpv77AEALxTqfmeGOUYTs19Vmv03XxVYNSPaNfMNh5cTh0hBqhWoHkSmqtbFbDPrkzSliB3tKzsRyPAtJHJmVbLuJYEGTzI6yEKYc1auBz8RPkbo3VciEVuAAexCWFktj8uwu59RjTEXO4h13Lnr0hFlpIbZEBJ5pkrysRq-eH9xNRxnuH8PB9KsJav4oVLMGjf_8vH0toVtfQtyh0UZDowEHkrWUGypTSZvnh4hxIGwkfBfGkiV4Fhjv3yAi0dQ7z9l2I9bfGP6mq4FRbxvPmA__Whsm9kqKbWCOkYTzvbZibmccJytBwsT8xi8zhE7njkP2BredYWn6iZEBzEUdXbqZGxbroCN9-zV7sgLE5VT7EZXpYEne9PVl0HWZDnltMfSalSjcwNg5E6jrH-FG7pDvW22EQtKgfHlXy3smIQ99ZzabVVsKl0PfdS3UPafUDSfqVfOR_-v_CARrwaYn_WDlYolbXvRLUXE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8baed34198.mp4?token=GpTI1WWKVwYi7f1p3CfOJkneJhCqt1DHZIvfIhxInyi_ET7VkhYvNT-Tkm7TtUTXlfEkHtZlcwuPDbuq34sK0_A9whkOO81YC1eCq8y6Vq3aOfY-ABEpa5jOB7w1yxO1JV1WS7Nw-FNQ2R-bh4RE8djqfEmWy3HQa6sMikLaYfGgX9ZEw3_vJtvcM0SP5F1kTj_Kn52Xpv77AEALxTqfmeGOUYTs19Vmv03XxVYNSPaNfMNh5cTh0hBqhWoHkSmqtbFbDPrkzSliB3tKzsRyPAtJHJmVbLuJYEGTzI6yEKYc1auBz8RPkbo3VciEVuAAexCWFktj8uwu59RjTEXO4h13Lnr0hFlpIbZEBJ5pkrysRq-eH9xNRxnuH8PB9KsJav4oVLMGjf_8vH0toVtfQtyh0UZDowEHkrWUGypTSZvnh4hxIGwkfBfGkiV4Fhjv3yAi0dQ7z9l2I9bfGP6mq4FRbxvPmA__Whsm9kqKbWCOkYTzvbZibmccJytBwsT8xi8zhE7njkP2BredYWn6iZEBzEUdXbqZGxbroCN9-zV7sgLE5VT7EZXpYEne9PVl0HWZDnltMfSalSjcwNg5E6jrH-FG7pDvW22EQtKgfHlXy3smIQ99ZzabVVsKl0PfdS3UPafUDSfqVfOR_-v_CARrwaYn_WDlYolbXvRLUXE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6745">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKvxAnrIRfvmwKPBm07HqUGE7UT5g9k2MCfljWLWqFWY4JfXrvgKdld0nrY_haRUhGT2wwmu-iDMo5mLkPapwXAVTEBUSiAT1jxFeV42XLVIWy8zeAek6IRW4gv0vHTukvjr716BTuLHi0iW8zJkkWOsAwxjaqq4eL5J2bwxgiWx9gJZEqdJhl50-6KDIZ-k2AY-5US6wapN4IFIvuTnXCulb2vcfQWaoMI53f1ZJHhogtdP7vh-PUfxld1INwES9F6kGb4tQBfcLMyo2CtbC11-sH1QlzA1KwhkJwus7j0rlz7UA2SspthbD5pDWfiYXAejROTlK2PyE1B5zCHIhA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6744">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c8bbbad4c.mp4?token=OLWgET2pZzz_aYZhoxG0UzZaqfw-5V5wc3rtd3P65l3PaaSr9_UIaS7qtvCT9OQT3M3T5dKeg2VcjadQHaGTbXtvQe_k7HprRWxVaOFgtlGZ4u4UoVhtbMlqx5Tg-pawkY9xQday4pwAPkKURwF3ecqhGgVP89-_R4wrU6_WAWl4sWcuzH-qAacVAheiJgfPiNwJSfMvpEySVUDL9Lyby9uihJn4rHL5bmVxOSq0tE-0k1DeSmU72RAC0FBfPAZpa0yKcUqquXL_h2JN0vkWONZCjmfcMLN5_3_jvsz8XplghnmVW5bjA4BlxwNsLOAk9gdBUcO5M9f-hlAMz4L9ow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به همون خدایی که اینها به اسمش اینهمه جنایت و ظلم میکنن،  قوم بنی‌اسرائیل، ۳ هزار سال پیش،  در اون روزهایی که یک «گوساله» رو می‌پرستیدند،  شرف دارند به قومی که بر ایران امروزه حاکمه. اون گوساله قتل عام نمیکرد!  جنایت نمیکرد!  اموال اون مردم رو غارت نمیکرد!…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7_Iuhz4_0xcOrTUmDdDwxOY7thmSJX-6XcyY4-cDjXB5QUuf0jxh2I6hDyZmwLq565APgy4lh6mcQIf3yEyj8zQVvCmSTCxKwP3DD1AGfbdExQez8Uhepwap2xkERjzd-Bojxb9v7kz-_0JhIyjIDiaRvvTdOaPQvAXszzN_5Urs70ijOjPbjmtmvFGiEfctHzv1bvML-zLoTc7jwA5o-MiJu7lsPFNwNsJZwPAOCxEDPymx1DsHdqvDVZ-4xby7sHpjXYdycjuh8RzeM8ot1KFFRtRsE9BwEuSEWq3M7GrErXVkF0vGnCqwa5ns9w-yajNohrO8Hz_khZJYCZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP7x72Hy0Fa2XziovhkvqBKFUX2B4L5g1gbWJCIfiauaqmcRDdDcYgY7ppGPRC-fjxmAOABxurOqgEiS6F7sLGo5fyyVlUmmgaeN1kpEnTm6CnTlH3kysJQhftj6Dr7cXv2h5fdZQtdoO4kvSHkwKl_QKOdIYVRH99Pena8aEfvi7bO2b5G6yWrbsfkiOEVSyVbjptD5mLXjGfAlq2htAgHIbaCt-oKXZaPxTn6yR5Si3c_0AmUy0vbSRUllQez61xTJ0RBUJE4bZ1yVXXzkFr5Bp10JbWL4UHmwrtusz-gKLlk_M2jOOdQPy1Pyf2a93V7L5jiTR4v-NetzaUmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL5JuPtHA0SSfs6Y3rPmUOWQY9p4ntNG9RrSDYhYqTIWlswKD-2RL20jPTRYWsGFmcnXoZdHysxJ9thRkhfTmYtgCKA5iNhOWhEoHTe2BhGke_hEqGqdrYqtB6JKOzMLsF9fwI0t_8Cf9T33QWTIGScm4GFVaOgACex0fs40-J4LuXlHzjOXsvbr2OX7mVcnFjWgzydBEXdspB6AL2wUCY6VrcmQ9cUXY5qRJKA7RjKVT05HcE2ZdWYY4gJwVB2qgH290tHm72pIZYaflGHACwPokyDQCmccS-AnPDhPB-k_h-GDimmwICSKT-LZDGC9_Yx9u8VsHzV0oJ6IuCQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6740">
<div class="tg-post-header">📌 پیام #92</div>
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
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8KGfBKiFw_3fGy66Azn7-r-N4gZT8-nFls5nnHyPxpytFJ7jHecFsRzibmrOGI3a749vUuFvrdo7zx3GzktcTjsUA9IwjcoqL18lq7F1esTvuVgi8wDP8vyv94scTwJCIVsX1I-NYpgeGRfZgPiEtFyMqCARzWlzzjL4AwIIRKSB0mA8-uZ95AaIh1DIqL1egLkFCizKOq3XhVdiQYT8aHsRcEGUoUpoQnz8rqHcIacc9k3MwYCDGZy57NIfaZYZ_naiZdMh8IMzJvLkXyLVOe2gspDtwIGBKAUkppAk36BXlibN3HpJwxLjl05qsGUsB6bW4h71AYtEDk4Fga8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6738">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCaVVDxVmHS1FUmtJkJZ6to9MHN7K_b9rbR34Mq3lteMy2JJPLWyFJcFLQGAonURz0Qd21Ina666xXKk3DSMoI8XzgN_mecQ0N5jJU1kLoVgtHt1OtOmYF_1UQobeLEIN53FpMSNU3KmOrmqhkenxymRtJWo4ry5z7Wz6cRrCIKCd3Q1ysKlkyQQp1rCNUbdXfqVpkAr4bffNlPDHW7Vp8sMNJzooAHyQWu0v8jSvVAg5Ulv93lwfwrcPhtRjmNm7WkxKmtXuHLFJwLsl9UKI0ctiQu3F_XtpNt48UKLPu-XgNdLltmCOf9Va7Oq2t5krFR9rdJenKTxeMpNTd5zXDc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef1762e4.mp4?token=lnnAWgSVv-mfQZiAmpJi6zFNLr_yJrSwEbJ2z6_cX2dbw6nplsbZwjnTSh_3CXiC_kIM_FQeDlSREYZiTnrJ3jhqMUNBoYJrunSCAfZs9P-kD21c8NSjqK95t60Qm2smKQkWi4IQPdS_TPtEtwFFI9F51yarrrh0csVC3k7_06PZ0amT1gr620rUK9qlQu9daa-d75VpiZ0sZ1VM1OapcNXnMEqgNL7h62SeCWCKiOpxq70uIeDQXFxkbf9JWOCf8NkOY3s5Ji3OHZ77Ssi2OjFVjex-G4hIFTDXAsINJXsOPDkDRvWGSOvMhdgoGbUbc8AUGCTkYdjaFXWvbTBfFCaVVDxVmHS1FUmtJkJZ6to9MHN7K_b9rbR34Mq3lteMy2JJPLWyFJcFLQGAonURz0Qd21Ina666xXKk3DSMoI8XzgN_mecQ0N5jJU1kLoVgtHt1OtOmYF_1UQobeLEIN53FpMSNU3KmOrmqhkenxymRtJWo4ry5z7Wz6cRrCIKCd3Q1ysKlkyQQp1rCNUbdXfqVpkAr4bffNlPDHW7Vp8sMNJzooAHyQWu0v8jSvVAg5Ulv93lwfwrcPhtRjmNm7WkxKmtXuHLFJwLsl9UKI0ctiQu3F_XtpNt48UKLPu-XgNdLltmCOf9Va7Oq2t5krFR9rdJenKTxeMpNTd5zXDc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏بعد از سقوط جنگنده آمریکایی خلبان مجبور شده ایجکت کنه، موقع برخورد با زمین چترش باز نشده‌‌ و کمر، دست و شونه هاش شکست توی دره‌ای بین صخره‌ها گیر افتاده بود، و برای اینکه دستگیر نشه، با وجود این وضعیت خودش رو رسونده به راس یک ارتفاع ۲۱۰۰ متری در کوه‌های زاگرس
- نمی‌خواستم در صدا و سیمای ایران دیده شوم!</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6737">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DZHeuYSAL2XdoWTHZ6gBa3x7SMFv_E_pqir4AC0n3ICbUyxrayxvZpwWCwFxlV0CBbwDZJRlF6yrY1MCThzykIymM-oV8DMq5iP-66OnCu9sbmxrbwlwUMHbTgA7g2JUDJPe2m0fjv2cxSnF5T2KukTbqhtj7qD-51UVumuZX5jKh5J8GoXB4-PveY9epC2PXzNZbFQs-UIUG5f5b5CMa5AjZ64VI2kwPsIM_SGbJH0kdO_hCkHicCQlZoZVdYLI1Bv0Ij77Fw68D_E7LUzqCejxfcs_x_gD7lUx8t1xTLc1dZuBG3ng6SkNSut2J2ShJy9peV77BcY-yF-ZgkPcdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d865a7fd.mp4?token=DZHeuYSAL2XdoWTHZ6gBa3x7SMFv_E_pqir4AC0n3ICbUyxrayxvZpwWCwFxlV0CBbwDZJRlF6yrY1MCThzykIymM-oV8DMq5iP-66OnCu9sbmxrbwlwUMHbTgA7g2JUDJPe2m0fjv2cxSnF5T2KukTbqhtj7qD-51UVumuZX5jKh5J8GoXB4-PveY9epC2PXzNZbFQs-UIUG5f5b5CMa5AjZ64VI2kwPsIM_SGbJH0kdO_hCkHicCQlZoZVdYLI1Bv0Ij77Fw68D_E7LUzqCejxfcs_x_gD7lUx8t1xTLc1dZuBG3ng6SkNSut2J2ShJy9peV77BcY-yF-ZgkPcdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش آمریکا برای فراهم کردن شرایط عملیات نجات خلبان خود، به یک مرکز متعلق به سپاه که در اطراف محل سقوط خلبان بود، حمله کرد.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6736">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=f-5HyfA0RoQAUHfgpEjYrVfYKoj7fy85dDHLfcQvGy0Sh1VEXzeNoKU1lcxf33-LWbNj0pIzkqoU4IlQigQmSEaguRi6QvAK6I68jKVCM1MqklLdAn-jnYEgKGyb-IIsVQjYKHRBG5i2eLdbDwo49V4MsOXlHYMBczhb0ZncKHKe0KF3uvolLDkrPzUku486dWwMH2aLSb03XgRUjUJL1YP6Qz3kC_i5LGX9jEfpqyC3ceIB6ICqLJ600QGfjEKdReg6IwyJkg_X7gePOutAT7LsVKOtIKh5QUHs1BYY_tsIgHkwafwiyO68unQQJE7ThhR9d-uYlo87360-d8xksnYpbxMzKEH6BLdoFdq6n1jHQQpg0aWcvHrGAkrIf5LaBZCqCV72RiriEy7-r8kZyFRgXTiYBY9wB4WqzGAcUT-21bDJI2E2yW8a4yFDjvAug1vJRWXLWZNteLmKjQsBi5Bm2SpvQHP4MhEv5Izsbz2w3v6CjgMQTMkIBCVVcadZjcxmEVtPcGOJFnMNZkUqxqgd8NZmxYixpD1-2SOsZHdC3mewGqLiM4UfS_IJhEvnx7JyCskdyukz2gKCpy-NKrADL2ZuTCWT_GL_ywSuWESbUFbRFo0aB1zPUUnEMwjpB1c3l6u8y9acTJ5m6sOYJyKL-PQjqCPW95ICmn0AjqM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca9eeeae8b.mp4?token=f-5HyfA0RoQAUHfgpEjYrVfYKoj7fy85dDHLfcQvGy0Sh1VEXzeNoKU1lcxf33-LWbNj0pIzkqoU4IlQigQmSEaguRi6QvAK6I68jKVCM1MqklLdAn-jnYEgKGyb-IIsVQjYKHRBG5i2eLdbDwo49V4MsOXlHYMBczhb0ZncKHKe0KF3uvolLDkrPzUku486dWwMH2aLSb03XgRUjUJL1YP6Qz3kC_i5LGX9jEfpqyC3ceIB6ICqLJ600QGfjEKdReg6IwyJkg_X7gePOutAT7LsVKOtIKh5QUHs1BYY_tsIgHkwafwiyO68unQQJE7ThhR9d-uYlo87360-d8xksnYpbxMzKEH6BLdoFdq6n1jHQQpg0aWcvHrGAkrIf5LaBZCqCV72RiriEy7-r8kZyFRgXTiYBY9wB4WqzGAcUT-21bDJI2E2yW8a4yFDjvAug1vJRWXLWZNteLmKjQsBi5Bm2SpvQHP4MhEv5Izsbz2w3v6CjgMQTMkIBCVVcadZjcxmEVtPcGOJFnMNZkUqxqgd8NZmxYixpD1-2SOsZHdC3mewGqLiM4UfS_IJhEvnx7JyCskdyukz2gKCpy-NKrADL2ZuTCWT_GL_ywSuWESbUFbRFo0aB1zPUUnEMwjpB1c3l6u8y9acTJ5m6sOYJyKL-PQjqCPW95ICmn0AjqM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی نجات خلبان آمریکایی در عمق ۵۰۰ کیلومتری خاک ایران، دو روز پس از سقوط و با وجود زخمی شدن شدید خلبان.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bi2fymb0A8mmxN0siU7BOj_XCpRZOdz0RB_JtHULWQlqzre6nlhydYBWxkXHti0bD8FVLPAuU4nICoJX6kzHgkS8yEeZ5dpBqVIU-c9sJt2elJyyXJ0MwW-O3OwbQwfqon4m5-J6PsJAtIgK_SJV8YUDW3tzdpKgNkQSbq4eBym-opMgMyo8ARQy9TgftjKC1dPVJEKZoab5Io6NOhJy68n72GG19WvW-thm5pfr2jzNIi43IcM92OYdJzoMjQy-jbYsAyqOBJkQQxRjcrdWzZ0rzXaiwXFAQGP5x-f4xGzUoxy6nq86sKct7v4EeokvVC_VrSuhZba5MuqEvX3H9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d8244747.mp4?token=bi2fymb0A8mmxN0siU7BOj_XCpRZOdz0RB_JtHULWQlqzre6nlhydYBWxkXHti0bD8FVLPAuU4nICoJX6kzHgkS8yEeZ5dpBqVIU-c9sJt2elJyyXJ0MwW-O3OwbQwfqon4m5-J6PsJAtIgK_SJV8YUDW3tzdpKgNkQSbq4eBym-opMgMyo8ARQy9TgftjKC1dPVJEKZoab5Io6NOhJy68n72GG19WvW-thm5pfr2jzNIi43IcM92OYdJzoMjQy-jbYsAyqOBJkQQxRjcrdWzZ0rzXaiwXFAQGP5x-f4xGzUoxy6nq86sKct7v4EeokvVC_VrSuhZba5MuqEvX3H9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محبوبیت حکومت امام علی بسیار کم بود
برای حفظ حکومت تا انتها با شمشیر
مبارزه کردند، حفظ حکومت اسلامی
از حفظ جان امام زمان هم مهمتره.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGLhFLCPOImDauGioh1et70A0ThVVqcZY_a_TTcy1Jf43VDK-SorLsGFVk_HflowJMjOBvSzMEBQDeARPRJ1jjODgziHmuPajWCsSGq_0QIxhXXYT2Syr-Y3SCylaaW1PGER1fOfCwq1C8aWii8fXNpGRoCSBu8pvWEHrwpRsWdQQOMsdPTBFk3zofMuBKl6GZRInX6-VBpP4ZYyeCRxVOAid9HhLIuiirCGrEtqPzSByKPuY5BG0R03-LlftKJkdy7Bollad8tYwmzwsQfierblpJmyGEJTMpYrVCXaMGBaoKA5uw7phwMiF1xqne6hd_Vk10jSY-kQol_9Aby1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6731">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6730">
<div class="tg-post-header">📌 پیام #84</div>
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
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrizzU9zmbICrqet4MvVKfIpUHVUt7IIXPpUEAvNEue2zSPqFDKGVbphH2plJS9byQtPHBtdrHP5u7AIlbrHvO2LorWrabXdorpfrDx5AvUzXI7dHH8JDKrkxFil3R1YIzKFfobiCarj7RsO4vqw3A8qvzyoQd-3rJm2bsXjkJLvnHe0AvpYnTJYBGjioZpfrZOJkcTyAZPbluGnLizhGK8RaNNd4BX6JiAKWHaBM53ok5NbT_GZKgXLK_mJJkDPwuuzL68H0-a46jlFK0YrxP5UNtAHdZZiqxyMIKD63nlli8Vdrz105kWtnyITiOCL13dfKxprBlWLcL4jcufhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6728">
<div class="tg-post-header">📌 پیام #82</div>
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
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6727">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kLF05tmGCi1TCIczn3UddWaJ6wrp4cQUgFh17GGFW2xPIeY8J0UL8IYx0jgH7anUmCr4x0GyuyrhBJz109qb4X7yW_EFGMVovO297Gc1ybCRrZIP_k-9rFZRazM9ycaApzY71MVrvv0gr3BMUb6IhXbJO-95JEGr3BZ_kQ7kWCE9nR2_unU0vjECnkDaBW-hMP4kgHKZiiZlx--adlphUarHQTvPBm60WvO6u3DQDe5d8z2Tf6A9nsKb2xCqATuHgRvFGk4fDvB0cf1yWayN8HtS8TR2H1S6H9LAb9vmz7yglAWxwBeq6veSV-AIaz7XK3TsflSlQNtEUh1Cvcv6zkH2-ryjQiYwpMrW23GA_UkipIJixR4UDKeTz-51KNEUWwIBmrkPaxzJcGiLL12JxxPlDdVlW5fLsypdSUPydNhEHWRnYy_LxgUIGgyAcQkvxxK8wYnffitTyo4gYH9Ky2dI24jqcB6Mc6v6Pa9SZugaQJg2POWv3N7YTaku3pmcMsBoARdClgmuINhCxPoBYgvzoPo9-0VX3pUEEdW8kaZfp2CM-qskHtCy6xSXF9oeFF_RLREg6tSVlj3gwJwChd58mqSf4zPc0tmWr7e62gxSEGW8ChimTVj1Xc2B8NCQSB70o89MDb_QRrTGfANiv73Pft-rncJreDxB8DZTla4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9327ed6ed.mp4?token=kLF05tmGCi1TCIczn3UddWaJ6wrp4cQUgFh17GGFW2xPIeY8J0UL8IYx0jgH7anUmCr4x0GyuyrhBJz109qb4X7yW_EFGMVovO297Gc1ybCRrZIP_k-9rFZRazM9ycaApzY71MVrvv0gr3BMUb6IhXbJO-95JEGr3BZ_kQ7kWCE9nR2_unU0vjECnkDaBW-hMP4kgHKZiiZlx--adlphUarHQTvPBm60WvO6u3DQDe5d8z2Tf6A9nsKb2xCqATuHgRvFGk4fDvB0cf1yWayN8HtS8TR2H1S6H9LAb9vmz7yglAWxwBeq6veSV-AIaz7XK3TsflSlQNtEUh1Cvcv6zkH2-ryjQiYwpMrW23GA_UkipIJixR4UDKeTz-51KNEUWwIBmrkPaxzJcGiLL12JxxPlDdVlW5fLsypdSUPydNhEHWRnYy_LxgUIGgyAcQkvxxK8wYnffitTyo4gYH9Ky2dI24jqcB6Mc6v6Pa9SZugaQJg2POWv3N7YTaku3pmcMsBoARdClgmuINhCxPoBYgvzoPo9-0VX3pUEEdW8kaZfp2CM-qskHtCy6xSXF9oeFF_RLREg6tSVlj3gwJwChd58mqSf4zPc0tmWr7e62gxSEGW8ChimTVj1Xc2B8NCQSB70o89MDb_QRrTGfANiv73Pft-rncJreDxB8DZTla4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از محور مقاومت
بخش «دمپایی» و «قات» مونده.</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dqdypgzo2P4DiVHIAgFP9rXLeYXHWPXdse2HqQro1OL3lH0eV2Sq8K4x_0oSUlnlqty8wiq_w_AYoAmsiOICQNgYs2kcoAsekznqsRz1e76jxijqUQ1D2deqs9c8WA6MI-C7oxh1tTN3m34h6Y-65VyiDSKUQ5SdrTWWAkZXgH1JXZMcWUfqr22DG2AznSpepqU2ZnSBdpJ4YsqAAfEtXcjDC7_K4rA_pottBpw2jYzEOZmjw1P4oLv-l_mLk78YQENzX0iOLdqI-ZvHLwL29TG6huCi-Ct6xjh83kcW52Qw8h8cM_PR6DgqdQ4n0xMOhUjb_ytEIRB-B5u7wf3dKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=dqdypgzo2P4DiVHIAgFP9rXLeYXHWPXdse2HqQro1OL3lH0eV2Sq8K4x_0oSUlnlqty8wiq_w_AYoAmsiOICQNgYs2kcoAsekznqsRz1e76jxijqUQ1D2deqs9c8WA6MI-C7oxh1tTN3m34h6Y-65VyiDSKUQ5SdrTWWAkZXgH1JXZMcWUfqr22DG2AznSpepqU2ZnSBdpJ4YsqAAfEtXcjDC7_K4rA_pottBpw2jYzEOZmjw1P4oLv-l_mLk78YQENzX0iOLdqI-ZvHLwL29TG6huCi-Ct6xjh83kcW52Qw8h8cM_PR6DgqdQ4n0xMOhUjb_ytEIRB-B5u7wf3dKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=s0ouIW_bO9kSFzoHsgPVOFkcBUkgz2nRmE-8NrksaAJZjIeTy9Rw1Rn6FGM-Zrjrj8A0gR6yisiwco08dU77_zl35r3bSvt2f67tGnIihiFQUfvdKAAol8EUcPQmVxfNJa50h8P8BE2WiALOV-F8wenSyMpzlvcjUBtJG1Ymds_fmNuGNsFG-vsxpEwpx8o7dqsVOHY3AgeRk-ZwDEYFW9vaeB9N4LxMofB3gxkty2qg3UJuMdoNHKlsaz3NYs9G2Ymgsg0WxbqlF5t7WY-vCx2tdZ7iViibFAvsshe7eXMhs3wzdgjmTIcf8DdsVR6giDgMGatFrb1YvFlqJ1G9Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=s0ouIW_bO9kSFzoHsgPVOFkcBUkgz2nRmE-8NrksaAJZjIeTy9Rw1Rn6FGM-Zrjrj8A0gR6yisiwco08dU77_zl35r3bSvt2f67tGnIihiFQUfvdKAAol8EUcPQmVxfNJa50h8P8BE2WiALOV-F8wenSyMpzlvcjUBtJG1Ymds_fmNuGNsFG-vsxpEwpx8o7dqsVOHY3AgeRk-ZwDEYFW9vaeB9N4LxMofB3gxkty2qg3UJuMdoNHKlsaz3NYs9G2Ymgsg0WxbqlF5t7WY-vCx2tdZ7iViibFAvsshe7eXMhs3wzdgjmTIcf8DdsVR6giDgMGatFrb1YvFlqJ1G9Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=twXFwJAh0V6L9w7WlaMDIbRDXK5ExQ6B4_5-gkSCKpnNS7rO67aMRqIXnhsQu-2Y86KyG4wz8fdQkkWYPbAk6_mVp5WLquzWyZ8Ye2XG_g7jyz8Mx2KfmCqjlZgaMSrULENVIyqczy4Sfm8nkOXmUvodwJ9vBi6HT_EjBJUf0UtS4uE7JQroWuuymcnPnV3LAj6uACaH_BuMVDdcYWTWgIpWTMij4FB2A9IlsiqYijjQBihS8DOx-26QM3KyewjLoXxVzqppm8N2X45Mw2X3kOXiPI8HiEK4SZafK1DTSqLQBsNuSD7PnzuNEo6PeiwwJdO9iaQf0AXe7FTnU57emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=twXFwJAh0V6L9w7WlaMDIbRDXK5ExQ6B4_5-gkSCKpnNS7rO67aMRqIXnhsQu-2Y86KyG4wz8fdQkkWYPbAk6_mVp5WLquzWyZ8Ye2XG_g7jyz8Mx2KfmCqjlZgaMSrULENVIyqczy4Sfm8nkOXmUvodwJ9vBi6HT_EjBJUf0UtS4uE7JQroWuuymcnPnV3LAj6uACaH_BuMVDdcYWTWgIpWTMij4FB2A9IlsiqYijjQBihS8DOx-26QM3KyewjLoXxVzqppm8N2X45Mw2X3kOXiPI8HiEK4SZafK1DTSqLQBsNuSD7PnzuNEo6PeiwwJdO9iaQf0AXe7FTnU57emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gRh7rZJIP4tCgvvHJl1I5J00LuQl5sqvH2jH9TwTxaVGvnZWkZgh4KvcANd-b3vHog2ReylUQFdXwQDXQVXSr4sLoLSACe-apRMgzV99yg1yN8_xwWS-VLFGF8mqyz26siP9p8tCW2AlwWfbbE0uZM1V5N320JehnUk1RLj2QSzGLsGEOZKvYFs1CIpBo1pj6s4Iok5ptVcIkpb9TGvNZarj-zSZZK1ecKWEilIWmECXVf733yfpBVDlG2mT_HCvfd42dV_UdmTsDKzKD4wExAhhapAdgI8J1eo14qvY81zWongq-mgjzYExI0z7bsv1IvxpTHaa9BMMyPCObKnB4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gRh7rZJIP4tCgvvHJl1I5J00LuQl5sqvH2jH9TwTxaVGvnZWkZgh4KvcANd-b3vHog2ReylUQFdXwQDXQVXSr4sLoLSACe-apRMgzV99yg1yN8_xwWS-VLFGF8mqyz26siP9p8tCW2AlwWfbbE0uZM1V5N320JehnUk1RLj2QSzGLsGEOZKvYFs1CIpBo1pj6s4Iok5ptVcIkpb9TGvNZarj-zSZZK1ecKWEilIWmECXVf733yfpBVDlG2mT_HCvfd42dV_UdmTsDKzKD4wExAhhapAdgI8J1eo14qvY81zWongq-mgjzYExI0z7bsv1IvxpTHaa9BMMyPCObKnB4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gfHTquBrhDR1VsHk-RN7Qwj6O9EivmZVsKz_YeK_2vLu_-c6vxbm-GnK9nX73X_x0atag-FDTczpfRVbEpuAcJ47bPsNGnVr4T0akeSvIrzUmFKcEsSM2K0PhwPumz5nXsF2F4IuyePENbeAy2Zxz75v6jeqt8B3AZ5qoEIQcOEoIl50-zQzcyOwrObYEmpKSa_IeYgEeZm9XBfHvY27qWLtROF7EAfX8Io8WHgCv-vebe6LoiruCHJuXUTScq2WFBjwrRN0gvGWQgGaQgwqJZE9sZAScDdbeBQRM7aYIctDnqwP9mxFibKf-nn7WDLUTxGEd99e0kx1Hsb2fbORJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=gfHTquBrhDR1VsHk-RN7Qwj6O9EivmZVsKz_YeK_2vLu_-c6vxbm-GnK9nX73X_x0atag-FDTczpfRVbEpuAcJ47bPsNGnVr4T0akeSvIrzUmFKcEsSM2K0PhwPumz5nXsF2F4IuyePENbeAy2Zxz75v6jeqt8B3AZ5qoEIQcOEoIl50-zQzcyOwrObYEmpKSa_IeYgEeZm9XBfHvY27qWLtROF7EAfX8Io8WHgCv-vebe6LoiruCHJuXUTScq2WFBjwrRN0gvGWQgGaQgwqJZE9sZAScDdbeBQRM7aYIctDnqwP9mxFibKf-nn7WDLUTxGEd99e0kx1Hsb2fbORJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Wk5FUsSjWhHfMb6PSwLA2IuDSKp_-E7UTFDQU4V56Evp7E_my5bz1NzhqWWb9SaAbfLmHYtYsne7FL1XHGWw9-dd7QVA-OiByTOVtpAbQCikqlcV_SJXWT_uaBSvEO17-1YN7X88aNk8OYLs6G_eID5Z0zdbPwiBLhYznvHeNjZGqrD-55D3rkVXyxfB2CJGSovm_GxeLouafieqI6AxUObsbeYY3jlBTymHB_W2ZYFTokeJ0Fbf5zlsjiobQAOiVjUUGWQY-KwPqBBcMw8xqf4dIrfMHroIX67hSxqabg108OPpP8ivKTvL6joFdVSwxZyVwcZbuavxAgqONJr-Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=Wk5FUsSjWhHfMb6PSwLA2IuDSKp_-E7UTFDQU4V56Evp7E_my5bz1NzhqWWb9SaAbfLmHYtYsne7FL1XHGWw9-dd7QVA-OiByTOVtpAbQCikqlcV_SJXWT_uaBSvEO17-1YN7X88aNk8OYLs6G_eID5Z0zdbPwiBLhYznvHeNjZGqrD-55D3rkVXyxfB2CJGSovm_GxeLouafieqI6AxUObsbeYY3jlBTymHB_W2ZYFTokeJ0Fbf5zlsjiobQAOiVjUUGWQY-KwPqBBcMw8xqf4dIrfMHroIX67hSxqabg108OPpP8ivKTvL6joFdVSwxZyVwcZbuavxAgqONJr-Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rjbA_wxp-0gM2Ivpfot0hX6JigTnxUjUtMOCG9NnTnRnywGemNgE-NG4aiwBWSpmM6AW8srYAwzwHVBWbMNc1Hykbm6YRHLmHr8V0gJS9ChlbXLSKL1uQ-rPbzh_80FBi-SBH_MRga7rXO2ZFw7Cu6axjr1e3VvrhoW0ub19lN8ppOhXzS9cBIukfWQmci5FaLeb1GlMp9vi1YokmvMKcqTzUf55ffZmx3coLxfG-5AMjd8skN3RLSczkND6aUPbXdP0IG5Jl9nVaq6MpetwuQ5LGl8FlWUd5xY2f1-dwv9yxxV9ONOkd5RUHSUxBurNKz5VH7nYhTvQmRI6Ke6Flg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=rjbA_wxp-0gM2Ivpfot0hX6JigTnxUjUtMOCG9NnTnRnywGemNgE-NG4aiwBWSpmM6AW8srYAwzwHVBWbMNc1Hykbm6YRHLmHr8V0gJS9ChlbXLSKL1uQ-rPbzh_80FBi-SBH_MRga7rXO2ZFw7Cu6axjr1e3VvrhoW0ub19lN8ppOhXzS9cBIukfWQmci5FaLeb1GlMp9vi1YokmvMKcqTzUf55ffZmx3coLxfG-5AMjd8skN3RLSczkND6aUPbXdP0IG5Jl9nVaq6MpetwuQ5LGl8FlWUd5xY2f1-dwv9yxxV9ONOkd5RUHSUxBurNKz5VH7nYhTvQmRI6Ke6Flg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QH2YqexLX-oAqt0Frdbx4A3rwtD2kHu6pUDJPF3NIH9IAki6-1PRMSE2TRSG0rZbW19__Vo7mttXHeOj0BhREBJgloUfGZmQrgpTvEA9GE0Lj8DlJ9R6cWA7_Z5YEyn85MwReyrr6d1aWkBEoENliLR4ZMHlthjg6GwWW23ydHGjOtTUZiUBkq10YDwkBEHGd--2U6a-l-2hO61rSV1kSnM2lWq2Xn57CdaNmbcx5HhDFs8KL0CiktaaTFfYM4VKxSJIQAFfq9tx5jucqY6utDz5ROzhLh6YwBTfcQfFSuxXOAdB6uTGGsPi5XJDznY4GmofQTm8kOJizA4-pG1uiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l8sYmO_TSAEmptOzEkutUZdjIKe2lZtRut9BXHuo8Vr8rZlwOR9T2Xj4Y-AbONJd1FFcrxiiaXupR6ZDdXtt3I06PgkP5ppLrXZK7sNYPqwU2YLqqgLif_ZOgM7Pswli1WA-NE_jWoiM4yCE5Dj4ETZQFfExi990lGHnM3eJh-qApHEEaeIDreSCNJnANx83Huk4IlLJZJLlh3-nepfPekcmGndTC-ADi2h9X3-gORQUfMrzMcU2fjM_gEMr_zjjWSXhsem61z8gwGEA7HrnUBVGVgAKmgLXuuvlMbiM9qh611O1P7fq2L0QPcn9RdGbruKB-AmXz9VWWQYXRbVuFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=l8sYmO_TSAEmptOzEkutUZdjIKe2lZtRut9BXHuo8Vr8rZlwOR9T2Xj4Y-AbONJd1FFcrxiiaXupR6ZDdXtt3I06PgkP5ppLrXZK7sNYPqwU2YLqqgLif_ZOgM7Pswli1WA-NE_jWoiM4yCE5Dj4ETZQFfExi990lGHnM3eJh-qApHEEaeIDreSCNJnANx83Huk4IlLJZJLlh3-nepfPekcmGndTC-ADi2h9X3-gORQUfMrzMcU2fjM_gEMr_zjjWSXhsem61z8gwGEA7HrnUBVGVgAKmgLXuuvlMbiM9qh611O1P7fq2L0QPcn9RdGbruKB-AmXz9VWWQYXRbVuFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Ix1458aikME36T8N0iocdAhhaRw4JbWsu4P2DLC9uzibX3Vdg2cY1COfhFpI1EH0QA1aGdq9c76lUKe_5yg0X1vkCTjhUBdX7YZWJbjEsaRf7r6YTX-rUjPjK3lOrt0NNdBPw0Hog3xhLYZ5Qe3puEKOV-mJTY45GVS04cwf1r9SqQ_-knmMPjSjWbL9JfxOptCLEksCTaEj0IeuBxoiu4cnvS4CAIIlrOvBVPPQ9xqVDACihFHgKDsNqV_DW0gO3NqSZRKdii86z_qJ7uI3el2jlZPt0F07Uy-21QrBLz5jFDtfWRJ71U4mtcdn90SlBgLS9WgmUt9VZbXmtn3VHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=Ix1458aikME36T8N0iocdAhhaRw4JbWsu4P2DLC9uzibX3Vdg2cY1COfhFpI1EH0QA1aGdq9c76lUKe_5yg0X1vkCTjhUBdX7YZWJbjEsaRf7r6YTX-rUjPjK3lOrt0NNdBPw0Hog3xhLYZ5Qe3puEKOV-mJTY45GVS04cwf1r9SqQ_-knmMPjSjWbL9JfxOptCLEksCTaEj0IeuBxoiu4cnvS4CAIIlrOvBVPPQ9xqVDACihFHgKDsNqV_DW0gO3NqSZRKdii86z_qJ7uI3el2jlZPt0F07Uy-21QrBLz5jFDtfWRJ71U4mtcdn90SlBgLS9WgmUt9VZbXmtn3VHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vpUgAdEzX0lTlTgo6pOT5-c6zIFyhO0Tt7N8R-xQJwt3aJY0m6OLcbHvSaCg4TY8h7QoUPJ1NtUrPl5zXkEtTs0yte1MNWouZUYScxglcSRBzi5oaHfxLqWvcC-s9AjZaeMV7SvcvmeFrI4PxmdCtQGjM_RgKB98ox-APTwK53BUZ4ar_Moji9gW-mDQajUa6KtMPNNkrKkes4k_2WBZSgYvxVNqE85loWjx3UL9VvnEx9t5E-E271FkzGfX-mvvu20m7Sui64n079subiEP8pEuOhSY1MMKLzFB0joYeVEnQUVt_0Bmm4E6UeBdF7o52MqETP39fRh817Lc87xG3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=vpUgAdEzX0lTlTgo6pOT5-c6zIFyhO0Tt7N8R-xQJwt3aJY0m6OLcbHvSaCg4TY8h7QoUPJ1NtUrPl5zXkEtTs0yte1MNWouZUYScxglcSRBzi5oaHfxLqWvcC-s9AjZaeMV7SvcvmeFrI4PxmdCtQGjM_RgKB98ox-APTwK53BUZ4ar_Moji9gW-mDQajUa6KtMPNNkrKkes4k_2WBZSgYvxVNqE85loWjx3UL9VvnEx9t5E-E271FkzGfX-mvvu20m7Sui64n079subiEP8pEuOhSY1MMKLzFB0joYeVEnQUVt_0Bmm4E6UeBdF7o52MqETP39fRh817Lc87xG3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oUjUR5TL3tcFktHs9Jlyi0iPNIsyKdjPB-6IDPtgc7stu758egwZyMaXOxF2nJVAwI6bk9cBY2cLUEp3nVsbHUuLGuEIAPou17lL5uWZjkSYefWLe338RjB_3_RczJtL7bceIo-WAgbVqn7oz4bhFxf8rpx_f1b0l3nV4uUttYvavBWZ4_SheCpowPsSn4DEGRAM4aFMCLyKJG1GKdPLO3iqkbLk0OUNHYl1V45RkHIyYsE_LBei8l-i-vdSTZOOGAUMr_c3z_2hTGAJHTQzWxMjnvPNu_RnsXIO3Qm2cHDspCYC4zWKMBqh_xxbWtSEKx47R5ma7zKTZzGZ0fkVng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=oUjUR5TL3tcFktHs9Jlyi0iPNIsyKdjPB-6IDPtgc7stu758egwZyMaXOxF2nJVAwI6bk9cBY2cLUEp3nVsbHUuLGuEIAPou17lL5uWZjkSYefWLe338RjB_3_RczJtL7bceIo-WAgbVqn7oz4bhFxf8rpx_f1b0l3nV4uUttYvavBWZ4_SheCpowPsSn4DEGRAM4aFMCLyKJG1GKdPLO3iqkbLk0OUNHYl1V45RkHIyYsE_LBei8l-i-vdSTZOOGAUMr_c3z_2hTGAJHTQzWxMjnvPNu_RnsXIO3Qm2cHDspCYC4zWKMBqh_xxbWtSEKx47R5ma7zKTZzGZ0fkVng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cw0dugzcnZQPs431UUcgyfdP5KwCS2ojn8MEEI07LTfSftd7Hy5rwU7zcCyBhc18bYk7UITWQWF4Mx_EM2x-gPdrVw54qzi23tOoVVjxy6v1Cb3Mkh4k4LXTkGG8D-Q8cO0RXBNhXItdxjpc9u5auvrBTkFmkvZVhynYHN7L7y2bVIqCR7MUvF_vEO3a-_vRYFYe4UvFY-XkGM96jMoaMLa69qi6RsdgLftuV8hgEiNtbAGLVt6PnBe4ONkr-agif8ZkUQ3xTtSHMFPXCstbMF-3JIImDQV9lb6Si265kkgGaTrUPDHVJGSJefGtjCSZ4qXy3L7sKndrOqb_XRJpUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TXIwgT9m8DbWKvPqxuKPyJY9-_vZSHaJmYkBe-GeA3zDJIdwBtBVhaKDtp5QzwTZo8xtoddu5R6ULjoadqTOeorW_1Oz7_g5MnfQ4qZ39bm1qYfVZnsTn1yfaJHxW4impu44AarSkm9F2qxDH3K-yQDjq7J9DF7ZMjB4ketvNQkVJk25xWwcLnEA7FM-JyPmq_JWSEFMZB3887tgv77W_3P-opkyE920irK-2wuv-aKA5u5sPNNL9kaFDliC1fomudiH3a9bgnj4Z6fRabr6hQ8SmB4F15C7kqRtlaUIGgoY-DnUKdcz3-ebI8f_xxVTYE485BSdtgpQBPY5-kG7eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=TXIwgT9m8DbWKvPqxuKPyJY9-_vZSHaJmYkBe-GeA3zDJIdwBtBVhaKDtp5QzwTZo8xtoddu5R6ULjoadqTOeorW_1Oz7_g5MnfQ4qZ39bm1qYfVZnsTn1yfaJHxW4impu44AarSkm9F2qxDH3K-yQDjq7J9DF7ZMjB4ketvNQkVJk25xWwcLnEA7FM-JyPmq_JWSEFMZB3887tgv77W_3P-opkyE920irK-2wuv-aKA5u5sPNNL9kaFDliC1fomudiH3a9bgnj4Z6fRabr6hQ8SmB4F15C7kqRtlaUIGgoY-DnUKdcz3-ebI8f_xxVTYE485BSdtgpQBPY5-kG7eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hKjWJyDENR5rDeFhU9GRz0ZAy02Dp0JbHeP7TozlrlPSJBWUixSeclF7MrNEg0P8wmt54ZZWI6V0ay4gkbayNzBXb41G5aCY5Tq70vPPsMul5hsiXxQ68_VJZ2NmnB3CZmzqgaQJ-ufPrl03hssnqvQeMUEp6vDMs4Bt1JCnWQP2oQlJ0_9_RLVlBSHFb-TnCI8eHB3Lgz7OCVoZCFokT4QEJ72lI7MT1ENx6Cpyg9ZqdQUyesep5tkoZcDAhJ-kkuIDCKIBJZa3muSsXoJO3LcCZ-CEB05hXbVibeavpu4y7bBwIwaJtc0ABCiyaRHtmFkcnWLL-ToIoxlQueT-ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=hKjWJyDENR5rDeFhU9GRz0ZAy02Dp0JbHeP7TozlrlPSJBWUixSeclF7MrNEg0P8wmt54ZZWI6V0ay4gkbayNzBXb41G5aCY5Tq70vPPsMul5hsiXxQ68_VJZ2NmnB3CZmzqgaQJ-ufPrl03hssnqvQeMUEp6vDMs4Bt1JCnWQP2oQlJ0_9_RLVlBSHFb-TnCI8eHB3Lgz7OCVoZCFokT4QEJ72lI7MT1ENx6Cpyg9ZqdQUyesep5tkoZcDAhJ-kkuIDCKIBJZa3muSsXoJO3LcCZ-CEB05hXbVibeavpu4y7bBwIwaJtc0ABCiyaRHtmFkcnWLL-ToIoxlQueT-ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q4EgTcwdqw77XzbPr4m59bVyZXVBr60oEHxSKIOZbY4qupjZEMa05OJT0Ef_Q6ufpCgEj-YA7gw2aE02i1wohzeKOFK-xG5VdQ1GEvDk1q1C4ZMKsdBPmYwtFRKj-DKGXyVhD5sxBbepImDa2E3B8WzOciaDYYhzXp_frNfWT_q-3PjaqV5NfjLdYFhdci2CbcspgcLpn5ZTck4IZa2ImEh19WAjP9Qv23rrImwYYnfxlucjy1WjxxXiNsBFnZ3tXUSWOO_LIsOzNOgDVHuaoyjAoNq7gG3RQtRrR75l_DcmC7kqRKcOfSgM4RfcSrHlhOXIincfniRH4x8cIFHJQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QDXJqrQmDmbJFuD4gFF208O87FrxzdKxlfF61t7w6LrRZ31PobRJDwiY2fVzeseGneDBOQGlxtfcIPuVgKewLHOTWVvm8vG6Lt-hU7LTYctgXOLssGcRgb-d_Rfl6LDmL3AruB7vfB2goaT6_KrNdFJSD8o3lx9NAehFZC_CZe_hyEFdse76Ce2vsGhBuVjUqxLhyZmAwRLZZ6kh8jde7Y8vUKRJMQ4TXgiQO3JDgPKRP_z_utJXr3D3BzoR8JULzepcOzbOKevIi5T_xeGy5yjO6aPJOMd0grmeGcuHRq9PH-jlDWYFz5trS9RWVlrkCd4HrvFV0Y0N-OhASJ-XVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 38.3K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qRgoB04BcDYqtdnFQjVA0NPd1nu3ZWdRmXKtuj8WFzhBXFjLj2fctXO9gsftVOJDtoLTxu66NSP3gMBtmMuBkDrjdIQ_LVJygvf6CbaTsFVTtypJb3cjw5Saj0Ua4MRBtPtFV-bDy8x2bSOy2Sw7zNuxN1WeldQSvKW0g6HLAm0_7RzmaifYpm1cbpwwYEGe-84b_42r_CUL24FX1XId8Xz_ZxNj1pPay1tjmoOOxHZ_w5tIg1ZmACT7H6kwyOetPu616YceBJYrATZ3wmh-eY3NJPDrlbE1tAf0uOTrLOzWJ3YO5U5IYPMM-KfYLTNTeoE_6TOpRiHBIiqjsjJTPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=qRgoB04BcDYqtdnFQjVA0NPd1nu3ZWdRmXKtuj8WFzhBXFjLj2fctXO9gsftVOJDtoLTxu66NSP3gMBtmMuBkDrjdIQ_LVJygvf6CbaTsFVTtypJb3cjw5Saj0Ua4MRBtPtFV-bDy8x2bSOy2Sw7zNuxN1WeldQSvKW0g6HLAm0_7RzmaifYpm1cbpwwYEGe-84b_42r_CUL24FX1XId8Xz_ZxNj1pPay1tjmoOOxHZ_w5tIg1ZmACT7H6kwyOetPu616YceBJYrATZ3wmh-eY3NJPDrlbE1tAf0uOTrLOzWJ3YO5U5IYPMM-KfYLTNTeoE_6TOpRiHBIiqjsjJTPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVmIj_4lvud4K1eOV2n6noqyRtShTxiqBA6T_5lV5Gl0WJ7KlhRQQ5YSJYYRgc7tRiWHygedkBeKs4tPoHc6_Dp4v-Xy8y5tUk_jx0e68TF5HJKCy9XBR997gzjG0rFcl_3Pxnf1SJdzIM_-RZZvkXYTtUFZ6ReYiBohhw5kfIi46eJoBRk908QNrW8NWzB6eIjxb9hfFnsuR2IkIiXrxApO8wpUyJkrBZ0AOcuhEs16FrC-QcLswhciZrcbAChJ3OHfb29O50aAyFjMn8h-Kp6m6_oS_BxGjfO4B_FsVCrXzD63U2RZqHge-S52PNBnG4kYMaNWfSxmJ0FehCkmIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bM2eaOjXQoEHGcYKF8Oi8EsHv8BBPaTPuqhlS6jHU9G1eyMY7ros8oFq6x2ATruUt3dAfElzqMT4zvqPjb-2_JWCD2X46IZCnqa1IfEHPWS1MKSfSUmP1qceAbaUcX6m53WmIqCGodOcR1J3H1O_S3vl4QOYxhKaq6PWdvgqxcoDEbYifLv3ZkH8r6i-McpvjRxoavdMuku3uPLE-Go5V2K1A6CTWAV0Jerm2NfM09-_oBVilzxrf0H_H3PEZYq_hlFYHKug0c4FjFjOd_SHbdF8ZKzzfhMHx6Mb9g0e0pzeTjrUiF-p_SuL70F5H2y29pAP_mMe3fB_jq8vBaknWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEZddNGjNq2rNjxqozNxa3hd4v43SX26b44ZVOxYnDDs7NfxqwZ96wzz6i9Zx7Vf_8eNHdeW07jag5krka7J_gDrCCVEY5Jh8iRzdGL6VOpyUfqoURKQQs3qazTWLBOWkiuK-yF5KMR2xij3aUq73bPYAmHM8o71OtYZkEvRa7EeL2qUOFpqZNNrHG-3s5uslxeqcf0joQ9nJ-J8vIhiX93OH-Ok9lup1GXlkagimbcXYVwRJlQr95qIe_H7RgMOBD_JBlTulbP-JKSF9iqBr9OoeAa6xoqNlwSJWCZ96UDlj9TST0hRiyw8Uy7b9CnbQ5w3SukmTcsSlW5JxKnmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=r9_SWCf1zfg_E-lS9ubLcczD0g91il4-HHKY9WXtS6WUwfTvnhw1gx_mkOec_uOSFswT3evdJwjrCIEgQuJjY2bsCmO-Ux45A4lmhE_rNsghJBgKmOekTfanbPuQ8xA7GhSKyX-Rpz-RcLKWBMXuVkAqls5-0PT2pNso9fbd-9lfWRjy8vODi-8c8e942MU5LO-tPeNMivog01hD71eNGhJG1N3cgGy-Lz5fXKEUoB7pBwl6EgK4mHqqX04nRHwZU7FPdCTwPxXIYhR2twD5XRwGFmRVpLjkWj7f_0yfprhwQGGdheL2WYmap2031hy7O4O7Yr865hyqlJqE_Rw_GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=r9_SWCf1zfg_E-lS9ubLcczD0g91il4-HHKY9WXtS6WUwfTvnhw1gx_mkOec_uOSFswT3evdJwjrCIEgQuJjY2bsCmO-Ux45A4lmhE_rNsghJBgKmOekTfanbPuQ8xA7GhSKyX-Rpz-RcLKWBMXuVkAqls5-0PT2pNso9fbd-9lfWRjy8vODi-8c8e942MU5LO-tPeNMivog01hD71eNGhJG1N3cgGy-Lz5fXKEUoB7pBwl6EgK4mHqqX04nRHwZU7FPdCTwPxXIYhR2twD5XRwGFmRVpLjkWj7f_0yfprhwQGGdheL2WYmap2031hy7O4O7Yr865hyqlJqE_Rw_GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UvE4o_M1rVBkp8gNtpfGKD3LuSlOlhOuWk4zw49U1TED9VKYfBIQhDgtQKueXJ__udu1JkcY3wguuusGe0aAC1i1ZdkTD1CzYS-L9E3-Gd_0CaX-4s4tbgdHHqI6qWVcAAft-_l2uF0JZUfYZIVVFtdUFRLdJFvOUleE4o2sP9waiAyohlfGY6z1ZfcWIudiC_tHQ_ZuCz5rk-6_OtgfvTn6o43WvlWmfHUm_u8wEuNt4ITMT7Js5KkyZ6k3FGHM42L-r_b2tmP76SaEjGM_ZpgnGQbCJA4i1MGJVo89oV4pEDcPfnrul44mwvsrAPUlzfqUhN-qd3qWoq13kN1GCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=UvE4o_M1rVBkp8gNtpfGKD3LuSlOlhOuWk4zw49U1TED9VKYfBIQhDgtQKueXJ__udu1JkcY3wguuusGe0aAC1i1ZdkTD1CzYS-L9E3-Gd_0CaX-4s4tbgdHHqI6qWVcAAft-_l2uF0JZUfYZIVVFtdUFRLdJFvOUleE4o2sP9waiAyohlfGY6z1ZfcWIudiC_tHQ_ZuCz5rk-6_OtgfvTn6o43WvlWmfHUm_u8wEuNt4ITMT7Js5KkyZ6k3FGHM42L-r_b2tmP76SaEjGM_ZpgnGQbCJA4i1MGJVo89oV4pEDcPfnrul44mwvsrAPUlzfqUhN-qd3qWoq13kN1GCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oS3uXlswkr_v9pkHGdKe30m6OqVW33OYArMRx-1DruOeY70quPYB3LewiHqfLtjJUJy_0DAPZqM10xeuBNBGXLV8SncOsq_HmsG8ZcT8O9YWtT6-FBV16ejOt7IJ5zodPL6isW-FopXLVxRi3TG1f4aYJMA0V-gEVM1Ny2GrmfnZPJInLApbOb6oTv6LAI9T7rJosaOrqCQ6s2RMlt6iL3qqmxQMtQMg82Vnxcwsc2G4QQ32viP6-wnUvk7DyMUwwDnXch3Y5irBdC5N9rar6PiAy4CJ_MLioj5KU_q7FYP7-GOETa2DDhl2qJpa2OUzPBHY_hZSS7v5rUVnLVP-r34TrDiV_yRa4YC3Y76vC5y64LYYQKJO6O8NN-eOocTit35iYChuToHvtXdvtatOuY3y4EqZPcGTA8S6EzoTBZA-VoL0HNG5oSD0JUO983ZDkcu1J3CuEuuDknSTA7P_lh4_5VvgCuJX29OnhXea5MkMCwufhb6gv4M3NKf6tEPH-HBZAuIxIg0ApHtFMvIxvJ-I0tsWQ_eZyBkVaur9NZe5yXJ1iSxFQhzDaaM776h3ww3oSRFhteDW5ZyjgZKmS0C89tVa_FECzyHlplcxLtyQ9TQclySPkwxpmGgqvfVqMjwv5lPgyHq3vNdlen7yOUJOGjX1L9sEEqA1zl68MOI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=oS3uXlswkr_v9pkHGdKe30m6OqVW33OYArMRx-1DruOeY70quPYB3LewiHqfLtjJUJy_0DAPZqM10xeuBNBGXLV8SncOsq_HmsG8ZcT8O9YWtT6-FBV16ejOt7IJ5zodPL6isW-FopXLVxRi3TG1f4aYJMA0V-gEVM1Ny2GrmfnZPJInLApbOb6oTv6LAI9T7rJosaOrqCQ6s2RMlt6iL3qqmxQMtQMg82Vnxcwsc2G4QQ32viP6-wnUvk7DyMUwwDnXch3Y5irBdC5N9rar6PiAy4CJ_MLioj5KU_q7FYP7-GOETa2DDhl2qJpa2OUzPBHY_hZSS7v5rUVnLVP-r34TrDiV_yRa4YC3Y76vC5y64LYYQKJO6O8NN-eOocTit35iYChuToHvtXdvtatOuY3y4EqZPcGTA8S6EzoTBZA-VoL0HNG5oSD0JUO983ZDkcu1J3CuEuuDknSTA7P_lh4_5VvgCuJX29OnhXea5MkMCwufhb6gv4M3NKf6tEPH-HBZAuIxIg0ApHtFMvIxvJ-I0tsWQ_eZyBkVaur9NZe5yXJ1iSxFQhzDaaM776h3ww3oSRFhteDW5ZyjgZKmS0C89tVa_FECzyHlplcxLtyQ9TQclySPkwxpmGgqvfVqMjwv5lPgyHq3vNdlen7yOUJOGjX1L9sEEqA1zl68MOI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=pYTirBzNnkDomFVPrUwEWRoOVWHfEBJ6m5KUw7Yc1D_8_cUwzmAtXREXXwFr9_UZcLsrlFaTENRef5bSo7sJTilYFSAWwiWmHMBahsNxREddwNNgH0nJxrDBsEXE0ybDYHXaVq9hC8avGvgIOCOyWxuO4H8WB3atJLltRIOqu1T0pg3oPQDP6WGYRpVBc2jAKuh9EDPS332vve0NcKFlYrqMyvPIzVOFPSkmpneLm8LDJQAHEl4vzFWCO8Tz3thYR_rsSNoxrODewgZpxeuNMaZKDjWfQUmQ55fmD0_oGj2nXhgeuBtx-NjmFKSld7e0o8Ef4iI9tZO9gu6AUH8KDUSR22_cmmev2U7lwQabi1tHjU9x3Q8cegn8IakQPH_d-r3bxQv1YeGRw-fh3nroltw_ItONTJrvzBekzHAYO0yP-4rz21EAUHTbD6WsqJDGRNTr7WZys4r2aN2BLzvHUy0rLy7Zabd9_m9OtRsoVzucNusXCID3AlRcT46UvsByjI1D1gsumDTfMZUJxpFhrwO7zUz9Ky5wFuYWx4FnMCWAlrm86CQEpYzxkeWkQkQwEsCCKlj9KDTOvnjM9i5CO4zIhSgjbMtKSkvg5vfFCBmvjmmGTOqm50PrDmRHx89cMm-y-Wmk091N98Kba-KkwLR8X5hZBD7GG6O7hwlcFHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=pYTirBzNnkDomFVPrUwEWRoOVWHfEBJ6m5KUw7Yc1D_8_cUwzmAtXREXXwFr9_UZcLsrlFaTENRef5bSo7sJTilYFSAWwiWmHMBahsNxREddwNNgH0nJxrDBsEXE0ybDYHXaVq9hC8avGvgIOCOyWxuO4H8WB3atJLltRIOqu1T0pg3oPQDP6WGYRpVBc2jAKuh9EDPS332vve0NcKFlYrqMyvPIzVOFPSkmpneLm8LDJQAHEl4vzFWCO8Tz3thYR_rsSNoxrODewgZpxeuNMaZKDjWfQUmQ55fmD0_oGj2nXhgeuBtx-NjmFKSld7e0o8Ef4iI9tZO9gu6AUH8KDUSR22_cmmev2U7lwQabi1tHjU9x3Q8cegn8IakQPH_d-r3bxQv1YeGRw-fh3nroltw_ItONTJrvzBekzHAYO0yP-4rz21EAUHTbD6WsqJDGRNTr7WZys4r2aN2BLzvHUy0rLy7Zabd9_m9OtRsoVzucNusXCID3AlRcT46UvsByjI1D1gsumDTfMZUJxpFhrwO7zUz9Ky5wFuYWx4FnMCWAlrm86CQEpYzxkeWkQkQwEsCCKlj9KDTOvnjM9i5CO4zIhSgjbMtKSkvg5vfFCBmvjmmGTOqm50PrDmRHx89cMm-y-Wmk091N98Kba-KkwLR8X5hZBD7GG6O7hwlcFHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Lv4EOl4gEGLGD0waRhNTL7dKBMwRLkg4ukEwWQ0FPAtRK6htMuPssNL4ocZwnOP4jk-PfWGfuqCAlLsPa9_UdBHPwujNxuoGYpLmGdvvclIDgz2cB7Sp5sNNB8VUY1BcMlU3CXEPgnEGXC5lxIISs_omrL2B4CEURNzEV5R1b-4npQSakgwdzN9XPpBHCT_m5Iokfn1WzXwcsHWtdDvEqWSQbHHX12AUeUzPFfLyB4V7stqpfaCf_bU8ytSCwkNxn0QKYW5cdTklvdPsPFxCZ-Lb8gI8BaHRIKOdq9mpaWCd5CQm_5UNOEvhv-SPUr8eCvsAUWQVRPLqgR4BCS3ieg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=Lv4EOl4gEGLGD0waRhNTL7dKBMwRLkg4ukEwWQ0FPAtRK6htMuPssNL4ocZwnOP4jk-PfWGfuqCAlLsPa9_UdBHPwujNxuoGYpLmGdvvclIDgz2cB7Sp5sNNB8VUY1BcMlU3CXEPgnEGXC5lxIISs_omrL2B4CEURNzEV5R1b-4npQSakgwdzN9XPpBHCT_m5Iokfn1WzXwcsHWtdDvEqWSQbHHX12AUeUzPFfLyB4V7stqpfaCf_bU8ytSCwkNxn0QKYW5cdTklvdPsPFxCZ-Lb8gI8BaHRIKOdq9mpaWCd5CQm_5UNOEvhv-SPUr8eCvsAUWQVRPLqgR4BCS3ieg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HIsa6ROKNM2RdrJe3jSey7RABS6SSHuehPG7BEWoKhgaRSHlGiytazN9-EiVEGGy1GTckC-U4xPj63SQLvHeXFwVlRmuC6LzgbPSQp8Vn757-u9zSh3akq9VO_3uBlkFRsg6ruVFVsTjYkiHvthHTq0_GoHelKavcZrKMVUMf6bYt1Gk8r8qj7dOH2rMV1ENzzEeGF0nZgWGbohKjLKzpDhXaJ3cX1Eaow9qvu28e7hbgMawwgatNYAK2to5vukmjwdpNIN5KbU_GndbOYXfHa1qbFKMK2uYs1lsaageW_3sDFWOCu9r04Y2zfGOpO80lXO2bRsjOfdaArDX_pXS9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=CT_oXyH2rZ_qAuuauudv8y79hXsaq05t5eBafqP8LsjWLTpIOA8wx-YCAIi8ZYzgD2BJgQVCoTuUPPhmbA7ciDXXXQSA8r9cDWlxAoIwIwi8sPQyKD__W5kYh4qIPafVAFaPPuQ-3JtsvBDsR5SiFbVb1OJWNyhP9XZgKmPO-mLCf6OasFv-EbCzyuubm9COYlvTXVF-irtW3wcOMsrznxsurSjhXTJFFUfUKz-xaqeKtYndaGwxIGAU19_7VF1QQe7UXsUVy80EmckHo8bamfVZuaxNdW8uk8TbYR-rSlMDh_jF7e31A-Mybr6KuTf8M0PGwkmdLz88W7Pf79d6Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=CT_oXyH2rZ_qAuuauudv8y79hXsaq05t5eBafqP8LsjWLTpIOA8wx-YCAIi8ZYzgD2BJgQVCoTuUPPhmbA7ciDXXXQSA8r9cDWlxAoIwIwi8sPQyKD__W5kYh4qIPafVAFaPPuQ-3JtsvBDsR5SiFbVb1OJWNyhP9XZgKmPO-mLCf6OasFv-EbCzyuubm9COYlvTXVF-irtW3wcOMsrznxsurSjhXTJFFUfUKz-xaqeKtYndaGwxIGAU19_7VF1QQe7UXsUVy80EmckHo8bamfVZuaxNdW8uk8TbYR-rSlMDh_jF7e31A-Mybr6KuTf8M0PGwkmdLz88W7Pf79d6Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L2hlu-UZdVIf27R-8ly-IsuWeIeiXDZKG9wl_PP0TZZHHmwW6LyQ8oI9ca4zsvhUwc7CVxTyl01Kzf8m1IZAcTCeer5lu-kzN3KPWyLD9COfqnxzOVQPTxmqzN9RLUgJv9JLmTX9iUYhtp6G8Payrq7cHMvjWNnrQ7VJg5187kTTjGDKLNzNCm-yAsf4kJAzgbViDOvZXkFzdxDNmanBRkvPRm43G-4-H9S20dj8rcEJZvqmQiAVqb2tAC_5XKEKRkXPNzktFQA_RL5qCD3_SZ_ecT-LaUtZTUV0EOJvH6u9vjnfaX_sqIAsHBeyBYHoW9sgA_2ns86LEL6a5vvaVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=L2hlu-UZdVIf27R-8ly-IsuWeIeiXDZKG9wl_PP0TZZHHmwW6LyQ8oI9ca4zsvhUwc7CVxTyl01Kzf8m1IZAcTCeer5lu-kzN3KPWyLD9COfqnxzOVQPTxmqzN9RLUgJv9JLmTX9iUYhtp6G8Payrq7cHMvjWNnrQ7VJg5187kTTjGDKLNzNCm-yAsf4kJAzgbViDOvZXkFzdxDNmanBRkvPRm43G-4-H9S20dj8rcEJZvqmQiAVqb2tAC_5XKEKRkXPNzktFQA_RL5qCD3_SZ_ecT-LaUtZTUV0EOJvH6u9vjnfaX_sqIAsHBeyBYHoW9sgA_2ns86LEL6a5vvaVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFOS1AdozVqqijvpTJOMQDn-rtXSSSHyiB58QAn4QsNiJoOUCACIlpCmTHgGkRCO4sON1OV1wpDTKD-QyW26D6KGrG55w_6RG6-dvuqaSXUUzmfEYjHt_oFyrF7B72YyfdzBtiYZh4rlHu58GQv2jVIq5wmLoTun-jOuG2-7iHiAURViFosTrR6eq0MC4cIQqXBmuTXiU3LEEiypdCa_f42eC9kghadZ5c5E1mTn2EzmqMWfZmfSq37YNXnldZCmC3f2jjNrVG5RVxUu5M1kjZcaFrmye2foTCTW023GBOSxLEH2CV0wUJXWHC2ePs7kfY0mXBthDt1U4Tp2CFCvBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Inh48Gf2uF4L-Of5cCdkCO6uN-mx5T4d9PK3oAOcRfMUED-0dC2Zkv4KNGQ6Z3vJ-5pMGoPqZpMf29cJ3SJzCzbkaQCyDKvl2bcL2R4OlNFI1D9d394BDjKumnsXlxo2FMIi0Bb7rlbDWiGtBxI-nnEX_C_yMmnY7TwSgop41FvTnTcgIRBoquOo3cZLrqZlmyCgRhdAdI8krOXVqYsY3grqKiRgCn1WbQYTdiYcf2dRjMi3_5HaLdN2bvQL8fCX-ZruKIpebz6r3RPqVHCRsu-2OUF0aADiQ_ulzuSndup7rVujBSUFlgVtdMvpSyTk_In0vB-lDCB8idH5NnV3VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aM9LrdI1Fq8MCUOys91jcIHquPCW7l3UK5m_hmRPte4dxOGmO_FPeOeEy88YFMs1oqHcjt3kVCEPwx6GNVNxHo7INQqPkXWZYZvhf6br8VWeDFbVAA96C6nRfbQf6Wd6bylyyta6rXE3McLmvxcYcc8BgPdR4zCENO5oB3Bf9_MLzxLKRjbZXo3NqFkr7SpX-NNPpa87vQpK5SJBYis52dYziMO2mzsDUlztx_QWoCpexjm1uMQymlqAVIRZdJl0jbSEPSAMBLhYl6pSidIzdHjKgDtQa5v5ohD6gyybdwRQh5oWowcBd6y49aKaIngttCf1fWdVSgeaIi0ylvwo3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZYpgTrQBLXpUsqNeCHQFEwgi2pxJW4tCIKYxXYbPRnSIys64dZklK1Wp8SkkjLdSfmX7ituLXt60Wl33qwta69NdlgGb9H7LGJQ5sWPD_6_l2s-E_t-gKmVWK9j9hvVg2vVwK52RpvaXgRBVyebbsi0sv2S4ByrM4U8NHMSS2b4bwifigPhuIqryjCNquiDhk3gkiNLkXNBhmQpEQ4GHLObkxZK5oSzXzrGX7yUgAptTz7xwKhakE8CioT9I86JH3vyfZpbLc3Xyf-1PZYgXDpj5XXB-ThWcB_uqRjjqSf2Co6RDIH27PCl8QND-mQUQ6i4bjdNfUFHtjQYOqXNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izcci30u7jpEa3awqHU0cKhfcJb3Gehjv2knoXw91v-BjCwMp3NqVPW3e8jn67HR62EuCOdmaUHBMTUiuVJnhYGuOzZJATRjLJrEvBhVdD_PEl6F_c8AUffZ78vkA44MuQa1t651LEnjIRNPzwpz2SxcAfrBtHq4GXOLfaU6MqNCabjCQ8eW6NqeV_7HqYdyLXWZR2-Gllpbr0MuBtxqCkuoCsLN1-PCtKk2a2Ckv6s2huVI5hJBQNqUaFN5nYD-O7VjUkE5vjD3PU8X3kmj_zudERRcNioXO0fNdPpA3GhIffx86PtMG5jjCaoIT_Qnp_Sn7hAR2fgm4oWjLWKegQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ofezz8bjnbSR5DAgMqLbM8waybmkq8_V3uVZApXXStKL8iLC7FijpBS0R1Tr3pXJPWhvSPq95og0gmy_SueT09_-UnA56WQbfsLDQfcUmWAFbb2kWLGhqIAYd0eyiZOvJtkaSwewp9RoS_FeY9dzWKDWA8WsuqheObScQLVrUYT3hU-ykaCzOAiyHhpu-8-Y-0o9ZL2nozAbFhEHP3uHDFBqtFtkbdxbY35bExUSX26FUCE0ImuEPWS7uJbIpORXu3nTJeJWPI-POnaKqQDgZ15FodLYsrzTOAP7HE5S0q7H3G90XXXAg8auVNZ1mNtgKy73_eIAeBsRq3SSVKriUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Heus9HbPNu-cXkVGlJnnifjHwkZnljqD4QbvzJ3cAgMF6EfqMdnJ21f-W1hVL4udLiKwuBg6lTAmkU1VU-wxg4PCaCRHOhxnKQyZzT9RPMwwHgyNwLv2tJTrB5tOpjlUJ5G50OFPs_4q-9MKda82KBhpdNfysIqzxoQR60TOl6KP5YIX1NCc1WfPRleql5ZwRbEKA0QSPXqt4iiBO4uFDfP80gpTRD98dcX9dNdeT3Mi315vnIapdTL629A25HP046GmINf7mCB7UZTZ0m_SFUesabBLCP0riJXN4hQcyXHuMuvMGA2xr_Q57jdY0SwygG9VS2tsDq1TC3tLe29paQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UrNs_hr5n_KKSJ4G1dS6yxqbAGsiWgxwjUuAHXFhhpshN7r5btNpegtl1UDAAkzZty3rl2lZt4aG_WmgEAt6Y_j9KC-T_6ZJDcgxdnjGOnFxPL3wvl15JDSXkBAAn16YV-WmRlK3FSdhuQiFvn42Gj1iRvnNwYXi3mtRM6ip9eiIBIIZJF24bzPI3BDn9_Ykd4gt3iCjP53-HuUGGUvJU0_h1qI-dmDBublH_vtYiZoCsZLailVXdc4PjJCmSiq88ha_oc97iN6_97CIcy_opwYc-K5ROLzgbyfZBiwB-P1Grui2ohLhiqx_eI__9QcDFivdNhEaDIM2RhRCuOAOzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F8jYPNPrp83XogJhLTKBgEwW8vmO-cRz1Zce5MFFLgBWMlx3wj5eqktHJSEuGPQeHujck8wX2QzsuhhgnhEqCfvB6GllwuerD9Q-PKXUC6hMRUzgOKNpo8_UBk4ImdRKVbnKLi3Btdwxr7PIlFJQoV2A5tPxyhL-ZhJTu6nanUpOYUfhiSEr5fWTRfOBH1miBbOObsPcPmffjEbWiJQiJXWNo9sjkJkMIvywA6mCxc_hB_lgh1z9rEbokjQMzFNzXfwDfGXkRGTxklINEvnTg8rU8mF0ynZhQyVvHO3K13AfvY_kG8z1Xds6PaiGHKo3t3wv-YMqf_RuzUphG2_IcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CNxtB-Rj_BdE32fBnsRWuK5OStK7srhYAcWf2dt_zilqcvWgJVdXi96zImLD7ArQpHOVE1vqmtwvo3vBF4W_qEksECLJWFlBoksnqk91IhY-lgWOKN9r_k8VzVRCz2UGWV78i_HTX6bOSD67owKHajyKCUH-TbUM31RYajlQ30jRUPngtSo_lsh3p_dIbRZvCmaungDkpBxNsjDvX7HUqEkeIbabfKAqL4_YA8Z4vlkYkK-FMc0muo4r0nDBqf6k-sKS05b_VY7nIieq9ZdWLQ_iUiKx4tjMM2goedCFIvTG4Am9MPig1DuqyAGqmgkSb6tsnrwNP6PZ2wwfNI5qgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #27</div>
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
<div class="tg-post-header">📌 پیام #26</div>
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
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Bbzn8AaQeH-6kspcpkI_-O2YHa7-T60wDZEMXQeRESje71geGSL8qMAeldaEn3PKGYIYibwmCn3DJ3274MbYMDH9SRP9nYfEo6o9h-nGVORYQVbnMp67L-s2EY0uBRMIVZukObexPSLdiyEC2GFYGKLc3Hy9Q8bF041JcqFNfYE-jfWO-nzySVWmdPAYJsYY4wdG1RpBzoSNfCbp3r8ugg2qNMLKMkc6YG0pcXlcA52D4iq7t9QLME3yoopvQDP5zmtL7dzPIBaO7lIno6pbjNIfnR6qpFFDK7z2TRc10sNHelBBpuoX8Dpr2SlgHrwooUf2gjlsWiNAcHR4Cw-bpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=Bbzn8AaQeH-6kspcpkI_-O2YHa7-T60wDZEMXQeRESje71geGSL8qMAeldaEn3PKGYIYibwmCn3DJ3274MbYMDH9SRP9nYfEo6o9h-nGVORYQVbnMp67L-s2EY0uBRMIVZukObexPSLdiyEC2GFYGKLc3Hy9Q8bF041JcqFNfYE-jfWO-nzySVWmdPAYJsYY4wdG1RpBzoSNfCbp3r8ugg2qNMLKMkc6YG0pcXlcA52D4iq7t9QLME3yoopvQDP5zmtL7dzPIBaO7lIno6pbjNIfnR6qpFFDK7z2TRc10sNHelBBpuoX8Dpr2SlgHrwooUf2gjlsWiNAcHR4Cw-bpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBqZ8VkbSxFR3FbN2uWvjhnTkgq6-y8EGONTFP-7g0hMddatXuF-Q8SWW_2i6J_SFX9wKMefuLwLPhPXe4R36L61EeFwGwg5ywqkPmLCtMQZX1Ca9tlW3boZin9f8CxN0VmgSCiZBw4CeEU7nSMKyvoIunXoGKCB2FmbGSjcD1DHMi_mMEXazaJ2S1b6Sbj4CqT1HGlxFTvMCqQczBGwIKIEC_DEW1VoFRCAjjuyrXbGVfLOufXpL2xbNHH2RSdqAuwHmMTYnbxunWfZuXbpEY1ZomltmVDq2yijKtNKHBeuuDySFcIafK09tWZaxhLh3cJwiRqEzFqzJQUjaA2NIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTUuBXgVz_35bZwC1EWGWaK45jrCfQuzeoZpJVxB0RsH0_gWl8mCNBg_6T2BYA_PZwJWZgNZ7iDMYpERt8CnlDHMJJtkFYB6JqVbFZ6ElW4I0eNVMJF2D-1SBEXWAJOrNezjviDaAxr_zkpdjztF_eyNBfHHlMyhuI7Pp2YUhS8lWAumQBKJkSZ0xg1RDWrD2BYz9kbXEnASXiandM2J5tTQUPV0TDdSRT0iPn6B2aYPPeOtTIXiFs7oCX7WDPJjuYi530T3PaMsQVa9fRb5LM4g4irlyseklS51xr9Lh6QuDLPe-BHah1lmm6mD5T374rF8I68ReW8GS_HS_TzvNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=E-8OC0c-aC7-ckTKlSbJuwLpDgsHdwgxt5-DSZvlEZT7z82lvTKu7aHldikpqRFsU3JaGE6G8Y1OQJUYRlDjvKYrlYrjqfsUnUUgNNxUhZqt3TR6kOHqHpd8357B-JeIdK8DsJ2udRD3z2_X9PJtHY1q_4BrIBbfjRbes9CeNRfGy0ibJbCDJ6HL53qgpRHHTAIAqOfGt5QAWZZlFzzXv7fMoEqt8glpLWR7duXAv70lCKeA-jxcA7lpfjyGSYURtSfGGIPjQncZOezd-0jJBb_o172zcaBs4x-saig48ul13Q35AfIqVNAcA0LzOBUGW9BLjUzv6VY5pNFPpAVAUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=E-8OC0c-aC7-ckTKlSbJuwLpDgsHdwgxt5-DSZvlEZT7z82lvTKu7aHldikpqRFsU3JaGE6G8Y1OQJUYRlDjvKYrlYrjqfsUnUUgNNxUhZqt3TR6kOHqHpd8357B-JeIdK8DsJ2udRD3z2_X9PJtHY1q_4BrIBbfjRbes9CeNRfGy0ibJbCDJ6HL53qgpRHHTAIAqOfGt5QAWZZlFzzXv7fMoEqt8glpLWR7duXAv70lCKeA-jxcA7lpfjyGSYURtSfGGIPjQncZOezd-0jJBb_o172zcaBs4x-saig48ul13Q35AfIqVNAcA0LzOBUGW9BLjUzv6VY5pNFPpAVAUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=tkGvFsYeMwiAyoXJ3s3qUcC2zk282eiZ0IyMrghD_3RcAq5JZHIugZRjFsz7cFIyzhHwKEZUZ2ym7n45JUF5nUl3L_R5qamvYtRF6sbtzs-UNexHR0RPeHOaKdFxaP7ny3Du3UYB37BjbIBNxkFLCdJbyQ_r5_D3pCnRsJizGPR4_oohYlSHmT30jU711uSJA8UjTZf9sX-MBpnUCkEq3Dj_yMX12uFhqLFUflFFDCRhpDuRHwkUqzOcHYULiPYvV5nDyReQ87WvARjfozL2Sz11pquxBT7Jpuc7MYONR64JuWH5aWDVuJut9depm7Xzv4ys7yfGKvUdCWIQucs1Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=tkGvFsYeMwiAyoXJ3s3qUcC2zk282eiZ0IyMrghD_3RcAq5JZHIugZRjFsz7cFIyzhHwKEZUZ2ym7n45JUF5nUl3L_R5qamvYtRF6sbtzs-UNexHR0RPeHOaKdFxaP7ny3Du3UYB37BjbIBNxkFLCdJbyQ_r5_D3pCnRsJizGPR4_oohYlSHmT30jU711uSJA8UjTZf9sX-MBpnUCkEq3Dj_yMX12uFhqLFUflFFDCRhpDuRHwkUqzOcHYULiPYvV5nDyReQ87WvARjfozL2Sz11pquxBT7Jpuc7MYONR64JuWH5aWDVuJut9depm7Xzv4ys7yfGKvUdCWIQucs1Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i8RiWR3a_VRVnIP6yXUcnVuoTz8ePLYRiMKghxXGFOW4YljjO6qgumZyECmE-tIArZIcqbJofs_qhAQnx9aF_thvxnupcaWZIyEzcoBGnWusPM28UViroGC6Rj8rnCFzjPb5IXgphB9MxgxuHPghSHpgw52Q6SSVgxHkNlBJiEuh1HmxBLlph-Tc7EBqAa9vIDf0cWnYXOvKXKqG1s9mZKT2WzO-UzqGU4FxZ4zCB55AOYELCmIt_T4ft8aIsp6qoPzTLg1COC2jqoQlTyvzh5xC09rm19e87rBL1Bj6JTl8Iu18r1aSMIawpq2X-sFxABW-W9ShXypZD4VhuPzcgQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnCAJekwwlN9teD8rRM1Ywyg7wBNWUSkirYaTCWPbR6FAae4MFDKjrvgfIcCOD6el2Cyk-GMQXF5XsqsvCcAI2epmrQ7XqG9RVpAdqX5WEImHwqkP5OMK--KBQVKUxhfXUtx15OOEr56i9i37_kgup36ONUMTgM0-3ESe4KgBUWuDr26ZvlY5B1Byw8JecqI7c8JHjyZ4zbqhQwDcY9_tbdeaUwh7JfLvb8w3P365AD3CCrVCMZZADUbXR4MZZ535p2YbiwDPJmfXYq93xqDK9qm41iSL1R0p3g5GhLOM7JB0PCXI_w5h_gPSjParAGPZw_C7b16ZwnV1bhL2504mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzMPNuXAs0Om6G7HHMRFj7dOUT6B7ylKLYyVQMhvpP0SvmIzB9J44vlJtQSaV3JB_xBRYVEHzx7PPlNKl-PcE6l4X2Luv6Jhg5Fbny1eUC8f4wVJUybylO6PEWXGUoiQOzHCq7ZzsvmmtBml9QoP0fdpyNoX3w0wjaatW3oZuQ0IchoAHwf0uYTV2PFX2KWrB6zRG-mx27HFLKx2PtYyJMrenAwJpY1nkk2jssrnPYCZrhVSHgj_I2XukQU1AWKF6BwdIoCFi2mSWTWGdGUlUCEBQWPsAYWF_a7umY1YA0ve_7bH2kvH7JwRI_nctMDbpRj9k9LbIBO0FqjZ8d0ODQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHlkETyMh_vdEj3ra3ix62Cub74fMaQwxWkH7ZPmxmYeXKj8FO3ZaEg41s-orzdtBXjvVt1-uBOlK-fIDThjYVPBKUrKoVBnTBEroa1cM742J0dt83V7Fyytr8PgjMuJMLkbmNs24skeA9VAmE1qYGkZLaxtMFpagykkRZzO5U1hEEMDaqnSyL6d4GLHZENPojj868JH0UINw7DKNP5YrJ5W26OP2SL522HqgFPeZpeh06qTcV4-zktIOT0_oGQmLxbYKcc21vBnOy8kLDHTZCiUS7IfLlg_XWcmjszZdd9VOpaYXWwxFqrXmTAie4PU6uLJhChmONeJ3J8uBtKDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfjOqMAGyHY2C_XebGp34LWHi0v5Y3RSpID87wcPVUFtWXC3RX_0HiVW1TVs8Skwa7GG1qErnk6Gy-0mX4PMkPhwYFa9wHRaLmjpQzLY0tFATInKQzQ8hFvwsHkwHbZ6KHLpSBXHw774OFis_dq-iBk8BRyGQUcSgkjreZb3B8hRHHbnIq6FrqijidB56P-cLIXKfnLfG5K85ytFcvQyrguBdz962T_0FdRW46QFXIKyEjmmu08Fc0qu74PMyncgFuG-CY0zha2iCIyk2utL8L1vbhQXtF39JQRZh7l6wnhm5FNVKS37nIZJTC2XMXEI28iCUNo5su-LcBn80Fs_ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1MjpyTczToHJLvygvCk6kKH276TPT2C9rtWrBjk9NnzNY3e8CJqOPYZzDCwFoKvlPIAuqB1P4liOJGiIasmKuQGpMd1kzLlidJcXurWNiyvikBhYN8OrWbHcJu-AhPeZhDEtrrdiGhem869JxqiQzvAcG1yqsPdtG7MZcPE15C7utiyVCpNdO2v2HBVtb4xJeNNORqc5Qebmjx2r5IOxjSh_S2FyQS24tslRlRuVOQsds6A8Mw0yIOVY_nfHx-8oA7r4xoG79ZYfBhJJM5OZSM3VLZC3Nol3idiePdG5wFpcus5ccqEftbc4-4e2NslmzXmY7LuNGiOiTamA8Wz-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nevQjT-6xLpehctQKbLdqexuK1C6tYOKfri5aqrI7nYTkflUYFDfmtWYW9_N0LbPh5RpAyyzcW1y--NkevwSDi7qeU9YE8RogmWs8SP_35Ma3YMuLNSrk7VIBDw0TaAfjXvySwkMLmndzJtYS587RvM-PF0J9UCSFlz2-7f-5Y3jxbUBAwfiL8l1O-gHhvt4pKnpRsSrONxsjAzPfuLiAJYJbDelouOQTnw0Y1TNv2QvK-naIN1MrTkFW9wE8lkBZDcG9-To5OhnVBCw0mKyfE7Xl4oBX-gbXV-V0sKpRX3QguJwrCiZUvSglRLC-fKnC8zSPs7bv5zSlGCOOjxFiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpGBujJ7Hrk0y09XVrEJvZgBjWUPc0Hwz0r0wm8o_YCke5sqgI6dhQokTaUOhCK7Of3riCmkwhb7gVWpr_NqpBOZc2vlFJoKcKDca98jgJyPjGELu02JQrFN9LemvHGaBeaiummjxET05vyIaZbydzJMWrvR2tpPDCkEPp9SjdMjjtC15rZmZWYP4SK5I1oqd-jYnVy5ee6sxf411sHlKbV4rfiTSUZUGkeU7KIhftHqbY_7SU1M2ZDeqgl4ggHe7IM7Md_yaANgcDDk1qjUPLV1J7iUqYMVzFK3OaORES4_68Ne0Sd8Ucd-ESYnMtXkwM4m1ci0KNXtL3QgPr_z6w.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=J8DA5IPfvXT3jT5UHHPiqmiQ3Ym9vtaoDdDkaOamqKuSgMnjT6xtK6_jaP5MiEpBqkRR-DU95StobkjygZ2cp3nBkhYXi5lXR6Iwh17FGlj-Fo7kPLB2R5YwnqM5bMjD9IN5NRMxd_CvJ_z9yVX-NEnAKCbjj8sIknCmNQ0Bs0n15HqM8e8DsSZ2wvaTjg0_Te6Q-54eDYP2XEqJXD7S4M38trD3Cofk2mmxrUh3Aejb8MdIR6qL6C5yuUUFlfClXnLrpntjGYOTZMZG69hSdFUrPd4rsR17UsUTeWRhSvlJ3kkLSL_ZjTbXgm55zq4GfNJr_S7ypYqpY2sElfV3DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=J8DA5IPfvXT3jT5UHHPiqmiQ3Ym9vtaoDdDkaOamqKuSgMnjT6xtK6_jaP5MiEpBqkRR-DU95StobkjygZ2cp3nBkhYXi5lXR6Iwh17FGlj-Fo7kPLB2R5YwnqM5bMjD9IN5NRMxd_CvJ_z9yVX-NEnAKCbjj8sIknCmNQ0Bs0n15HqM8e8DsSZ2wvaTjg0_Te6Q-54eDYP2XEqJXD7S4M38trD3Cofk2mmxrUh3Aejb8MdIR6qL6C5yuUUFlfClXnLrpntjGYOTZMZG69hSdFUrPd4rsR17UsUTeWRhSvlJ3kkLSL_ZjTbXgm55zq4GfNJr_S7ypYqpY2sElfV3DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDNsJaVthPnkww4pk14LGPL8TuDmQlBANK1Ql16nWOi8Zuz3dv_WXluqz0o3Yh55_F9CKLne3lsDW07iZC4vYJwtMiLI33hPkD997_HfPhmW8pae3syggOAyfqvKbgFVLMeJgRum1MJ3xyKPrMTl67rrhwlXMiOyb4xMbHqeciw7EwVfYjWsOau6IgDi467YVbgd0ZNLPHhCgl02XuYwyEpem3x0C-gOMcg9ZxGasnvaIbLSKlNwpLah-vD-Nu5gdb6dkqAgvLdcCmQgtNxw0aWpZFHV4iRImYcpjJkvAW2Cy2cIcuw88K3uLV2s1_uR60G6phLOagWVIkUV5TwRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=MGDjkLviOjsR510_H6grv3OoQ6x1qB2TCRkrxzkMsaYeQVH4s6N66LN9USk0gSbO-k8gY80XmWbRNQ1Yfm8gT6t6bH6aFoobtCdn_y551hojdzA-Y9fF7JiYE3SecSpDlbmQY8afKpsT5u3mAu_QdOyLUIgimTe6xkaYY0ai6KXs88M66GZsdULTKyogINzd31v_jRmO0RWDKaNmJEDvCJZxjS7y0iNhJySz7r8bbCVgkSyQvSKWHms1J1QAiVAlmfs0o_j7c5qer8ZzeJ-g0eICZsshBoCQ6uFBx_SBoCv_JHhu9Fhsx_8Ndf---bcncBeG50MZmF60dm3qKUhhIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=MGDjkLviOjsR510_H6grv3OoQ6x1qB2TCRkrxzkMsaYeQVH4s6N66LN9USk0gSbO-k8gY80XmWbRNQ1Yfm8gT6t6bH6aFoobtCdn_y551hojdzA-Y9fF7JiYE3SecSpDlbmQY8afKpsT5u3mAu_QdOyLUIgimTe6xkaYY0ai6KXs88M66GZsdULTKyogINzd31v_jRmO0RWDKaNmJEDvCJZxjS7y0iNhJySz7r8bbCVgkSyQvSKWHms1J1QAiVAlmfs0o_j7c5qer8ZzeJ-g0eICZsshBoCQ6uFBx_SBoCv_JHhu9Fhsx_8Ndf---bcncBeG50MZmF60dm3qKUhhIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=DN4AhRx_iPTOP7QAM3TI4nVVIAsGJ6S2EVdtl9ZNGeoOrIaog-ti89Lf2vpsq31LX-lJRzskthEPmGiY9BLoV-GEKzUGsEK8582z1AubTQKCDyuiyJOzm6p55TbHb4vGDZwkwL2N4mApWycdrAfAzxsM5kZZO18pGvi4ryAm5xhWE3KgJz8LsuDHOPC5mou3v2qr5fzJH9BkBrNBSG3HA25B2r3yRLHDZZuXTU8fiFuMTOaxMp2teIlBTJiaVLo0U-Ltpan7WHuj3eIVUbrZmrhBsIcfgbjIIcC8icwkc-BNAjJkw57uRNEYV27LoTJCJbuu70ueNkY9G3G_AY91KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=DN4AhRx_iPTOP7QAM3TI4nVVIAsGJ6S2EVdtl9ZNGeoOrIaog-ti89Lf2vpsq31LX-lJRzskthEPmGiY9BLoV-GEKzUGsEK8582z1AubTQKCDyuiyJOzm6p55TbHb4vGDZwkwL2N4mApWycdrAfAzxsM5kZZO18pGvi4ryAm5xhWE3KgJz8LsuDHOPC5mou3v2qr5fzJH9BkBrNBSG3HA25B2r3yRLHDZZuXTU8fiFuMTOaxMp2teIlBTJiaVLo0U-Ltpan7WHuj3eIVUbrZmrhBsIcfgbjIIcC8icwkc-BNAjJkw57uRNEYV27LoTJCJbuu70ueNkY9G3G_AY91KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgqog5CUqM1zZ3BlqMmkCeIbtqdQtZbo3-gBSNxI3q9miTgjqzSLYnC1dBYIasDdeDHxQNYpTzK7fRyodjEP9J339MduZx2bEriFhQUqn-T7HRtU3lTmquKf6uuHU0xHLtUEJrnTwO3kM4va6dF4nL2N1qMOMzGpS-c0GY2ZcXQEdnBGZWALQCCvfCEc9N-CLTEblqM6NbGWClqhAXvaBh4yy4UZQ7KyqbyNmwOIeZL9NOpSkclOFxEEiFHYL5NL_dVQhxN1Vh6w6yX3rDmSl63FGc5Uzt8BbiSLy4G2Z_VXC2sqgafb_GPbM1_KHwxcqB-uK2cCwUCDu4Z9qaJhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
