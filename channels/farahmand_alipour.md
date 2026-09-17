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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 18:02:50</div>
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
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAxG7YVglpKQtz_qUrBsKIJd3nODp0ZJiY-DznNOM3kH6HbcPosYUQpEUNWUP1QcyCw0MgckB8YKn_v01wLTZA5SAB9zJNln0ZctPhRlY0Jj2M4A_Dd7SmRJ76ARYFVXN9X-_-BepEixR_2QfctgljAusRixVTWbuq0BhwpbV84wm_F_jQtUrOcPXkD2Bbgp5XDA_Ivf4jyL6bXppRviVhMsGO6NP59UVcBdqvIeraJlZhaTTrxD_hOXLrigsbnOr44RHmCZoH9stUZSxxYwEd76xN_63NqFpqbXXdwAyDjGBy9_zY_2D8W7MT29xP0DDH1TdVvxnNZmXTP5CKR1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7_Iuhz4_0xcOrTUmDdDwxOY7thmSJX-6XcyY4-cDjXB5QUuf0jxh2I6hDyZmwLq565APgy4lh6mcQIf3yEyj8zQVvCmSTCxKwP3DD1AGfbdExQez8Uhepwap2xkERjzd-Bojxb9v7kz-_0JhIyjIDiaRvvTdOaPQvAXszzN_5Urs70ijOjPbjmtmvFGiEfctHzv1bvML-zLoTc7jwA5o-MiJu7lsPFNwNsJZwPAOCxEDPymx1DsHdqvDVZ-4xby7sHpjXYdycjuh8RzeM8ot1KFFRtRsE9BwEuSEWq3M7GrErXVkF0vGnCqwa5ns9w-yajNohrO8Hz_khZJYCZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP7x72Hy0Fa2XziovhkvqBKFUX2B4L5g1gbWJCIfiauaqmcRDdDcYgY7ppGPRC-fjxmAOABxurOqgEiS6F7sLGo5fyyVlUmmgaeN1kpEnTm6CnTlH3kysJQhftj6Dr7cXv2h5fdZQtdoO4kvSHkwKl_QKOdIYVRH99Pena8aEfvi7bO2b5G6yWrbsfkiOEVSyVbjptD5mLXjGfAlq2htAgHIbaCt-oKXZaPxTn6yR5Si3c_0AmUy0vbSRUllQez61xTJ0RBUJE4bZ1yVXXzkFr5Bp10JbWL4UHmwrtusz-gKLlk_M2jOOdQPy1Pyf2a93V7L5jiTR4v-NetzaUmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL5JuPtHA0SSfs6Y3rPmUOWQY9p4ntNG9RrSDYhYqTIWlswKD-2RL20jPTRYWsGFmcnXoZdHysxJ9thRkhfTmYtgCKA5iNhOWhEoHTe2BhGke_hEqGqdrYqtB6JKOzMLsF9fwI0t_8Cf9T33QWTIGScm4GFVaOgACex0fs40-J4LuXlHzjOXsvbr2OX7mVcnFjWgzydBEXdspB6AL2wUCY6VrcmQ9cUXY5qRJKA7RjKVT05HcE2ZdWYY4gJwVB2qgH290tHm72pIZYaflGHACwPokyDQCmccS-AnPDhPB-k_h-GDimmwICSKT-LZDGC9_Yx9u8VsHzV0oJ6IuCQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHx64jqVOQsibxvmxecEi9EBgNJbrBJc0iOFpUN1JTlqUrm9JAt2_l8JOLz-MbB5eSm_2s8JwdhETbilzNE8LY5OzDsbPqnKvgr7pbSHJBuHAdMeBt0u2pMLLLKfAlUPQJrVm6OlqlWq6y5QZunHRotrfTBiKbS5LZeWeLf2-j3GH6P0Dy_YhfVdbzQ1EWYWX8ovVXpuoODnN_y_DMOxDA7qXqnZYQ2K62QGK6VTOO1l-xTNVrAIYuH4uyUXcFLrtFZVtc3c5KJyxV8hzXQJciH1uZPtjtpIR_3UXEm60S3sklLvXHLvyoZl0gbvmAmiJhEHqSBZ1AhYZVv3C5--5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6733">
<div class="tg-post-header">📌 پیام #87</div>
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
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGLhFLCPOImDauGioh1et70A0ThVVqcZY_a_TTcy1Jf43VDK-SorLsGFVk_HflowJMjOBvSzMEBQDeARPRJ1jjODgziHmuPajWCsSGq_0QIxhXXYT2Syr-Y3SCylaaW1PGER1fOfCwq1C8aWii8fXNpGRoCSBu8pvWEHrwpRsWdQQOMsdPTBFk3zofMuBKl6GZRInX6-VBpP4ZYyeCRxVOAid9HhLIuiirCGrEtqPzSByKPuY5BG0R03-LlftKJkdy7Bollad8tYwmzwsQfierblpJmyGEJTMpYrVCXaMGBaoKA5uw7phwMiF1xqne6hd_Vk10jSY-kQol_9Aby1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrizzU9zmbICrqet4MvVKfIpUHVUt7IIXPpUEAvNEue2zSPqFDKGVbphH2plJS9byQtPHBtdrHP5u7AIlbrHvO2LorWrabXdorpfrDx5AvUzXI7dHH8JDKrkxFil3R1YIzKFfobiCarj7RsO4vqw3A8qvzyoQd-3rJm2bsXjkJLvnHe0AvpYnTJYBGjioZpfrZOJkcTyAZPbluGnLizhGK8RaNNd4BX6JiAKWHaBM53ok5NbT_GZKgXLK_mJJkDPwuuzL68H0-a46jlFK0YrxP5UNtAHdZZiqxyMIKD63nlli8Vdrz105kWtnyITiOCL13dfKxprBlWLcL4jcufhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6727" target="_blank">📅 11:06 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6726">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hIQ3Y6g2Knx5dmTwrCOgnaJa3yvQeChCXBxurTa1YOo9PDfU8_DNq9wy9mfsLiBDEQQ0a_oNDd1XKz18nHZ1F3Xm9H-W5XhkMJhBM2lL8omO3q9HQXqu8Ov9KhK2Zj8-CSPtWL429FNlpy32zIFUhs-YgfnXhPgp17C8MrXEZuHebGhyHMZgGCY6NdsOs1AtooBtH0mUGqrhT-OfwIMz6Ec5ZU0Jr1gORxXKQEqgPFyt9Y2BBu-KEt7mU_jtAMRLQjI8YSpKCMfhAmAaC77aKmT-D_kb-aGW4_doLU75F5O3QeOkk4JCHB50o_bB3BvW8UljCdVMynKxQ_0ktOHCTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=hIQ3Y6g2Knx5dmTwrCOgnaJa3yvQeChCXBxurTa1YOo9PDfU8_DNq9wy9mfsLiBDEQQ0a_oNDd1XKz18nHZ1F3Xm9H-W5XhkMJhBM2lL8omO3q9HQXqu8Ov9KhK2Zj8-CSPtWL429FNlpy32zIFUhs-YgfnXhPgp17C8MrXEZuHebGhyHMZgGCY6NdsOs1AtooBtH0mUGqrhT-OfwIMz6Ec5ZU0Jr1gORxXKQEqgPFyt9Y2BBu-KEt7mU_jtAMRLQjI8YSpKCMfhAmAaC77aKmT-D_kb-aGW4_doLU75F5O3QeOkk4JCHB50o_bB3BvW8UljCdVMynKxQ_0ktOHCTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GSosWfdahBYPJ6xBleQEJZCJwNP5G8Moo6RPw19iNLkfzRPoRq4KnoEKnJHIrSKeSWWKmwTmsniKeGSLiJ28r9BvKetM82M6dJF8dh3bGaAmzJ8QDNL2RZZQmD1UxVRkssx4ogkGixLbeKGd2FHnalMBCJnA84A2VnWEfy7SiwgrV-FZbgU0VVkC0LCZGw9xTTCfE8eYeX5RzImutwCL8SfAKUhVvJalxtEutyIpvt5c6jsZWRLNpCvfIMNL9u6231kpM0HsQ4pcTfSDaUE6cCz--3HEbdMrLuyHBF3ZjJ8I-99hPB8zcDia9Bi7rQ_6uvZt9u9MDAitO9OPfCsCug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=GSosWfdahBYPJ6xBleQEJZCJwNP5G8Moo6RPw19iNLkfzRPoRq4KnoEKnJHIrSKeSWWKmwTmsniKeGSLiJ28r9BvKetM82M6dJF8dh3bGaAmzJ8QDNL2RZZQmD1UxVRkssx4ogkGixLbeKGd2FHnalMBCJnA84A2VnWEfy7SiwgrV-FZbgU0VVkC0LCZGw9xTTCfE8eYeX5RzImutwCL8SfAKUhVvJalxtEutyIpvt5c6jsZWRLNpCvfIMNL9u6231kpM0HsQ4pcTfSDaUE6cCz--3HEbdMrLuyHBF3ZjJ8I-99hPB8zcDia9Bi7rQ_6uvZt9u9MDAitO9OPfCsCug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جمهوری اسلامی به «علی الطاهر» میگفت «مینی پنتاگون» پنتاگون کوچک. با هزینه میلیارد  دلاری، با صرف ۱۸ سال زمان، شبکه‌ای از تونل‌ها در درون این تپه ساخته بود،  مرکز فرماندهی، انبار تسلیحاتی، محلی برای حمله به اسرائیل و…..
اسرائیل دو سه ماه محاصره‌اش کرد و اجازه نداد آب و غذا به اونجا برسه،
سه هفته پیش جمهوری اسلامی
به آمریکا پیام داده بود که اگر دست
به علی طاهر بزنید، جنگ برپا میشه و…..
اسرائیل در یک شب، پس از شناسایی ورودی تونل‌ها، ورودی تونل‌ها رو نابود کرد و تبدیلش کرد به یک «تله» برای سازندگانش.
جمهوری اسلامی تنگه رو هم بست و خودش در داخل تله اش افتاد!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6725" target="_blank">📅 09:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6724">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IgfiFIwZTfm9MxS-_Mske-p9IqNQgKqmxNQbQI9iVr6KvG82Os0KH8yVcGsSIPGGhPRaufDGXN4-w7ZAMWzkEE8QhadILgvPmakBscqXwTfS4C4I34s2oNMFxH8bUcOfnNcXacyslwycszAjXiXg_tpmlv_wDBp8ceD742Qnq8VRbHilPjyF9nUjApPgsMV9x2bLDoa8gf_M2Kpt59EFhYq4o0-hTwiq-G6fPC94p3yZi4gQITo7d65TseJS-fPWI7tLFhlHS9CKVm_xfdw9OxnJyDWq5QhX6KwliYMmkWfjBkjifbnVhSGixLCMFIWUo1eyt48_eISTgcqPSNIAyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=IgfiFIwZTfm9MxS-_Mske-p9IqNQgKqmxNQbQI9iVr6KvG82Os0KH8yVcGsSIPGGhPRaufDGXN4-w7ZAMWzkEE8QhadILgvPmakBscqXwTfS4C4I34s2oNMFxH8bUcOfnNcXacyslwycszAjXiXg_tpmlv_wDBp8ceD742Qnq8VRbHilPjyF9nUjApPgsMV9x2bLDoa8gf_M2Kpt59EFhYq4o0-hTwiq-G6fPC94p3yZi4gQITo7d65TseJS-fPWI7tLFhlHS9CKVm_xfdw9OxnJyDWq5QhX6KwliYMmkWfjBkjifbnVhSGixLCMFIWUo1eyt48_eISTgcqPSNIAyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WHT2y7IADS_FDHy-aUfyPX-QsTInwtAEh5OWUVvDYJfr8FnvgFUVUOCkZQgAQRg78Pl-qszVazQJM4s7t648HV7aY7cQhR9GI43_e2gTKb14_jCg1srKBGQ5hCuLm5a_Ontg4VVYp4aE6ho-Pp8DP_66i4VABTsf-bCdHGO5cwLDKvCWhgAmF0u_durhaHHkIU3CnZNXmC69gCvpTnHVG_fSKfHfh1qr8iTqjt0wg2Dmiqw8rQXzf1xyurmIBNGlHLEbBfw5alcgUW4Sd_5ghWDkor5KiEnVAu6TMPYH5oEaILeiakuX-lyqdKgv6_Y-vspnu1b79fsjyiKKoWAn9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=WHT2y7IADS_FDHy-aUfyPX-QsTInwtAEh5OWUVvDYJfr8FnvgFUVUOCkZQgAQRg78Pl-qszVazQJM4s7t648HV7aY7cQhR9GI43_e2gTKb14_jCg1srKBGQ5hCuLm5a_Ontg4VVYp4aE6ho-Pp8DP_66i4VABTsf-bCdHGO5cwLDKvCWhgAmF0u_durhaHHkIU3CnZNXmC69gCvpTnHVG_fSKfHfh1qr8iTqjt0wg2Dmiqw8rQXzf1xyurmIBNGlHLEbBfw5alcgUW4Sd_5ghWDkor5KiEnVAu6TMPYH5oEaILeiakuX-lyqdKgv6_Y-vspnu1b79fsjyiKKoWAn9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=jzV_Jpw56_45l9AKy31c1lzpAtQSKMzxLPr590PRg_FPzZ7_ffVrJTAEbuCMQyeVqQbE0loHNn1OAx5zxmFkmFWmB9BU8xd2ei6FNGmvcQyFTbNtyGgpFSsimIrGatW57bzQaU3Ki-SjMqh96StHkfWdTFkfp2enTOIUe9IgIWCnJQHOTQXmztOM5RFnls_r08ynpGngr8CMA_vUN97SLBSoFJuOJrORsFyVdEETTZZebn6FmLD0b9QWYfRzr__UbWx5vsoDuk8z5G3N_h-XfwEqbqk1F7VAHsY1qlDeTkBPI-QIzjTEGRYG_UeI3i-wkb0uF6S74-q6hP0ZE0Ikzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=jzV_Jpw56_45l9AKy31c1lzpAtQSKMzxLPr590PRg_FPzZ7_ffVrJTAEbuCMQyeVqQbE0loHNn1OAx5zxmFkmFWmB9BU8xd2ei6FNGmvcQyFTbNtyGgpFSsimIrGatW57bzQaU3Ki-SjMqh96StHkfWdTFkfp2enTOIUe9IgIWCnJQHOTQXmztOM5RFnls_r08ynpGngr8CMA_vUN97SLBSoFJuOJrORsFyVdEETTZZebn6FmLD0b9QWYfRzr__UbWx5vsoDuk8z5G3N_h-XfwEqbqk1F7VAHsY1qlDeTkBPI-QIzjTEGRYG_UeI3i-wkb0uF6S74-q6hP0ZE0Ikzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=rpaIUoamCFtBczTHjXM8Sz3ziKXax44ykOZmVOwD9jbur9flHwSWRwkmalNrIp4zi0n5FhNSaErvjbU6DbFitML0v-ypx98mJQUvBzfaDLAKvy19PSUSu8_vhHX2bUX_jxZNlpxxfB0RVy3zwMdsH7vhfSR8dwVBpHOHLLXxOy7VsKYxt4Vy1R5WZJMOOqjb2YB5zEb97Q9BOF-MlTxpWt_4Cru1Q30kdpG55W4B_mLf44cTOws5oQah5dHQKt1USdDlfhmkpKqzjSS68tNLUJ1aHBsLCgszHil6IqKLOLzkIdCEl6KtG83KvngLwD7SuxqPtajwK6ocK0mNl8GewA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=rpaIUoamCFtBczTHjXM8Sz3ziKXax44ykOZmVOwD9jbur9flHwSWRwkmalNrIp4zi0n5FhNSaErvjbU6DbFitML0v-ypx98mJQUvBzfaDLAKvy19PSUSu8_vhHX2bUX_jxZNlpxxfB0RVy3zwMdsH7vhfSR8dwVBpHOHLLXxOy7VsKYxt4Vy1R5WZJMOOqjb2YB5zEb97Q9BOF-MlTxpWt_4Cru1Q30kdpG55W4B_mLf44cTOws5oQah5dHQKt1USdDlfhmkpKqzjSS68tNLUJ1aHBsLCgszHil6IqKLOLzkIdCEl6KtG83KvngLwD7SuxqPtajwK6ocK0mNl8GewA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=quO9uWeutHkjBx6axAwUgHhSj223sLRRF4KlxTJP7VwVtSTVHV9dWGf0aI1LCun-IUZd7w0z01-yb0caho1OL5uGDuZXBgFsSYA3BlmeGAnZ0JHrUMf98wkeMU68AQPxC9CwAzTl8azdnMTNQW3YigHZyo40xEyL_AJ-YCuTuZp4GWMKzWIG_d3nhJn4bHHEdXcDS4qBejekDyzsRt_fyYPbAcceRwsj0o0xxUPiFp9WLGwXaPRWYTTrGovxHIjp1wyhp5ERrUfUMqQWw5L9mdTrZINl9GliPc94Kgu1dnNsW6o5D1jC1HmQHbaFByrfKNPYsEsjAdtz7kfVNJxpPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=quO9uWeutHkjBx6axAwUgHhSj223sLRRF4KlxTJP7VwVtSTVHV9dWGf0aI1LCun-IUZd7w0z01-yb0caho1OL5uGDuZXBgFsSYA3BlmeGAnZ0JHrUMf98wkeMU68AQPxC9CwAzTl8azdnMTNQW3YigHZyo40xEyL_AJ-YCuTuZp4GWMKzWIG_d3nhJn4bHHEdXcDS4qBejekDyzsRt_fyYPbAcceRwsj0o0xxUPiFp9WLGwXaPRWYTTrGovxHIjp1wyhp5ERrUfUMqQWw5L9mdTrZINl9GliPc94Kgu1dnNsW6o5D1jC1HmQHbaFByrfKNPYsEsjAdtz7kfVNJxpPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DL_WHkdogWw0MOIupfi8RoQcZKZqBfaVWKQoij4BR-u8D0OitrwkPsV9fg5ZN471vy0iaGWcMlNeXho36Jtfwhz6upxvylUJDyp6SpKyuxweMuzvLk0joNXX5aTyvS7FkkducHtkx5woBWa1ZOYj5wTf54Ur-Z4fMFvmPXg-fdpvyc4BdJga-dGvAzu7wC5H0ftGFJoIpOdTY97VM6aJSkExQryOJxBEaO4L8mdPmT8pETCzy7WueURMZlB71TvLQjzf-74PDk8iImZ-5qmeFROzVsjhVq3eDVGzeDRtwYhN7x5qk-Sn-TV8Ci8vKjPdnkYaJwcS4dmWsw-RXZEHPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=NdDLKhu1eTIYJRJsV3A4ami0LouSr5SxBi_Wpd0nXYrDV9ksAIz2OXOvLOsjwFCgOhI73nzpanxVGYhnIU5CDliNcbb09VHbV3zoIPbYNHO3vwvq7sqrlJrgQp-Os5RZoehBfX4X5xObgHikbLpKsZlqI18kZ-DDkdxHJWjlwzzjRyc5P-n44uylhTNIqbYeFEH1a9ET1hG8djDca9H-QoNQnv5qblz0x3RN6GYUpX5OABL2gilkQRY0PE5kqDkBSyxhSW_eBa8Q9QmaqTb49-eG5W0eyZfehVgAh4kmtl-IhttNC_pw_87QYsp0guBVR-fo_Xa0kS5lIkMww3epMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=NdDLKhu1eTIYJRJsV3A4ami0LouSr5SxBi_Wpd0nXYrDV9ksAIz2OXOvLOsjwFCgOhI73nzpanxVGYhnIU5CDliNcbb09VHbV3zoIPbYNHO3vwvq7sqrlJrgQp-Os5RZoehBfX4X5xObgHikbLpKsZlqI18kZ-DDkdxHJWjlwzzjRyc5P-n44uylhTNIqbYeFEH1a9ET1hG8djDca9H-QoNQnv5qblz0x3RN6GYUpX5OABL2gilkQRY0PE5kqDkBSyxhSW_eBa8Q9QmaqTb49-eG5W0eyZfehVgAh4kmtl-IhttNC_pw_87QYsp0guBVR-fo_Xa0kS5lIkMww3epMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=iwFSpTh31ud0c0_hGMivNEp-Ra_Q0if3tefwMK-zriR21Po2hA6_mRVn3YLNwhRscsS6lxVJ2dTIng31sTpHEgOnG_l0jkOv_AQagUnOKSTY50aMlUvSd7hgl6FT_ZUXPLKg6J6pJj4SQw0_PRIj7eq687Cwl0BtrU_KiX09bt3A1wGwIc4pqXLpMkmSNmQ3D8Zu8TNpalzXpS7b566nHLZ8oQnN5tLyYuT6IiTqxxQ3cWVspc48Rn8O8rY5h44JugBVCq-QuA20OEvD6JqN_AAB_31N7qvpgE-a8uBcviRh_IkOitZRV5Z9fpdHPTQDo-x5zG3ekUDjOXHhjLpJEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=iwFSpTh31ud0c0_hGMivNEp-Ra_Q0if3tefwMK-zriR21Po2hA6_mRVn3YLNwhRscsS6lxVJ2dTIng31sTpHEgOnG_l0jkOv_AQagUnOKSTY50aMlUvSd7hgl6FT_ZUXPLKg6J6pJj4SQw0_PRIj7eq687Cwl0BtrU_KiX09bt3A1wGwIc4pqXLpMkmSNmQ3D8Zu8TNpalzXpS7b566nHLZ8oQnN5tLyYuT6IiTqxxQ3cWVspc48Rn8O8rY5h44JugBVCq-QuA20OEvD6JqN_AAB_31N7qvpgE-a8uBcviRh_IkOitZRV5Z9fpdHPTQDo-x5zG3ekUDjOXHhjLpJEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fwRE8wS945FfdZ0VFTVy7LyIqgRez6XQAdSmJl2EeRGbVV2XWGaZUCj1zD8RkeVSI41em5l65BjfSrH2hj00cSeX9wU30nFB9kaoznpIiEXFO8vMkHBkdWlAekuBaqxtEh28VtB7zrWeED8kVrHDJlqIThtc5gKJD2OcddbLBRzlTek9Jn1TrQVM1P7oUbbuti0cRHbVOeX8yIC1OIfK4hZpHHYf50UNhIhS7kZGc4-PotnGdzS40MR6V9lppim2f8SF51fa9ZRV2rWeYfI9AGKwy1eb66si0QsWKns-x2UNnoh0Mkax6HFsuZJRO06fzjoUQ6DHHyltmA6zJCgjUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=fwRE8wS945FfdZ0VFTVy7LyIqgRez6XQAdSmJl2EeRGbVV2XWGaZUCj1zD8RkeVSI41em5l65BjfSrH2hj00cSeX9wU30nFB9kaoznpIiEXFO8vMkHBkdWlAekuBaqxtEh28VtB7zrWeED8kVrHDJlqIThtc5gKJD2OcddbLBRzlTek9Jn1TrQVM1P7oUbbuti0cRHbVOeX8yIC1OIfK4hZpHHYf50UNhIhS7kZGc4-PotnGdzS40MR6V9lppim2f8SF51fa9ZRV2rWeYfI9AGKwy1eb66si0QsWKns-x2UNnoh0Mkax6HFsuZJRO06fzjoUQ6DHHyltmA6zJCgjUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=obbxqvJUrV2zqh_LMCuoa4i0eGBt5JfTmo1SnZGpX8dP-Bv4g2jvIWQ2nOFeBisZQvFeliEp2L9P782QXEYgtc6H8Jqikpf0IVRhKk93JTEdKjxyPKayHZHnVIsHn7LRsN9JyE18YNolA6BrvGB8ETL12z_TDdksNkg5_BA5PHUC8FdFc8dKeOFVRr3GW1ozNA319KzHYwOrD2xhOKAx696SSS9hQwTEGDncNGh-DGO2Aks1EKrPsl6wCiBe6O5GZmSA8UTCH_TEizJq0WbK2-EaKG78wYrrwTN3nMltLy2HVBM7OR7PkvqkJ8V1QPDNCe2F9YHdSu_M0O8Ua0f3pA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=obbxqvJUrV2zqh_LMCuoa4i0eGBt5JfTmo1SnZGpX8dP-Bv4g2jvIWQ2nOFeBisZQvFeliEp2L9P782QXEYgtc6H8Jqikpf0IVRhKk93JTEdKjxyPKayHZHnVIsHn7LRsN9JyE18YNolA6BrvGB8ETL12z_TDdksNkg5_BA5PHUC8FdFc8dKeOFVRr3GW1ozNA319KzHYwOrD2xhOKAx696SSS9hQwTEGDncNGh-DGO2Aks1EKrPsl6wCiBe6O5GZmSA8UTCH_TEizJq0WbK2-EaKG78wYrrwTN3nMltLy2HVBM7OR7PkvqkJ8V1QPDNCe2F9YHdSu_M0O8Ua0f3pA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2W7MV-TKWZzHpduNuaT5buwEVp-uMqX8W2B39GkoQfbLzwju9r0jIsyX5YtdkkmgyS5GRFB-t2FWkApu_1jFlDJ7EAoAw0gTamVatdCzez60Pf_OkHmeuA42_2hf6_JGJDK8clUUHcJISnp3V_FlKkrs7hV79uIJSP96ucX2sCcjs0F3rv5JCrTteJ6WtG9xYsRY_LnvHm65xwmfY3XkvK2J0p4b0DGfX2jq-9KSyB1BwElA-kh_w0HtwwPHQK2OQ2Mc0_D0Qpt5DPlwD-80akpMQWin4f7g5GvOtmVfliZzxue9J12ljEXkxOr-VMo8OJX0Q9mXYeNqTfDOHhLMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=iPtcth2_utwJe_pXzhGDXkwp7rtAkOQpoOCWneZ1TlEDVbCtY-InUtZ2fkYBnHVIm8I7Bi2VDOh5C2UcMV4CRyKlDU376TVDbOQSpIvJtCxejQNWBQ1dxPpL_juoTVjmX_-qVCEb8yZ7TBWtMD30SMmnQPe_KvOaS2s2mtciUnz1vzX5gNRNqA24g1apZKqxv-g9QND_6d4FHhO-gSdkLMcMxb-k94XTAo-jZRKyFAC5mBZGYXenRrWErVOLcROwTHEh_wBNyg9evSUpBC710eHAynND_FZ0jRMNsEZtPjOLiJ4HS8RTJaavzGBWrcidgEpUIjbNDzKN_m9XlJuxoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=iPtcth2_utwJe_pXzhGDXkwp7rtAkOQpoOCWneZ1TlEDVbCtY-InUtZ2fkYBnHVIm8I7Bi2VDOh5C2UcMV4CRyKlDU376TVDbOQSpIvJtCxejQNWBQ1dxPpL_juoTVjmX_-qVCEb8yZ7TBWtMD30SMmnQPe_KvOaS2s2mtciUnz1vzX5gNRNqA24g1apZKqxv-g9QND_6d4FHhO-gSdkLMcMxb-k94XTAo-jZRKyFAC5mBZGYXenRrWErVOLcROwTHEh_wBNyg9evSUpBC710eHAynND_FZ0jRMNsEZtPjOLiJ4HS8RTJaavzGBWrcidgEpUIjbNDzKN_m9XlJuxoTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ZbEGQg9vBmGkmKfYuormOPX-FYqY_c8vpp47-81xPILiOMVTFZ9YGefrUJFQvRI8UgKE6SF1f7DwhASdXtKQrwAHAHQwWZ6JJr8-KFYCbP1JaFmC_OmYmz3E44Gjd2mFgrKAZTGV2AoykJm5UbKdRv9Lql89eLomqixG_AkH3Y8gfToFnQVQvk9uo-hTHR1J2ONXgGm9Q4aP_xuCGfwL9sK0qyR1Nie6jdtzMUFzjCrsOKXEda2b4wcJkPmeWKRqE5skHr1mAxDXDH4T6uWK-0-dbWK1a-AczcdBuv4qook5K2Z3W8cMgAlBhDMZmG8iakXh_ieL35UwzEBfxMx3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=ZbEGQg9vBmGkmKfYuormOPX-FYqY_c8vpp47-81xPILiOMVTFZ9YGefrUJFQvRI8UgKE6SF1f7DwhASdXtKQrwAHAHQwWZ6JJr8-KFYCbP1JaFmC_OmYmz3E44Gjd2mFgrKAZTGV2AoykJm5UbKdRv9Lql89eLomqixG_AkH3Y8gfToFnQVQvk9uo-hTHR1J2ONXgGm9Q4aP_xuCGfwL9sK0qyR1Nie6jdtzMUFzjCrsOKXEda2b4wcJkPmeWKRqE5skHr1mAxDXDH4T6uWK-0-dbWK1a-AczcdBuv4qook5K2Z3W8cMgAlBhDMZmG8iakXh_ieL35UwzEBfxMx3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSvs9hOje62T9W9ihPqgIUvhpCSpq-5QydJn5K4_wAY3f6StNdOTCzP_GBiue5Qytv7JFQMMEZ1kVRX11kjHGFWZAHnThsgjUrIHtJXXed5QrPNQTtmNPPJhSWA7Uzk93VRHw_h8tEW1fevGNjUyETPPSoqavnly0sEm7fePXNODLoE7Vt_LVYj6Vhb3auu2HGUkG7Rtqn0QMlpJOKpcRsIZwo4QdWRxn7slr6oQsg6FleXEGLeAzVzQwQ-eiWxFnfu6ha_iTCITM9ea1NuU778oysedhcpYxHSfshL4U_tu-NVrzc3kX-7JRQd9DUcGMAL4ygChFDBZPKTBDonwrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gxix0Bk3BI35qMpXYyo7mJybI1pVImc-7jOP6hlDwYimfMnbmMq4YlaSK5ErSppWxh_8Ah9FhMzEy57y3hoMkFqCLJGg50v6KpDJekVFkjp9gTHhAN5AaTQxRcQCHcGhcpB2VSYCYVaGnSFBPRq0CsMN5PLPUgR9GzL98KEFDYDmvX08Cfm_LLbtQHpZJHgAK8PbAZL4aGX4vi_oP1Aa1RQdyB8IcgFATLKLp-jAQRaZdu3PzTiht-5GLhqyRFH_D5cBcvwnkwjnvAt4QI-AyXNKvzVB9gqTK1hpW-IFNn-Yck9C9XjxMi0SD3K6zKKqxngmIKQS-b6pv4Ewe4AYBA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Z6VNpdfUiFCny2N4DJ5krJgWmHxQhXHwMsIuhvz2Mhk3_xlOVJVsFkw9AUiZblVVSB6qudKEqStw6-59Ub3i8-rp0CRxwR_josaIHfacfxcO-UCZ3UbuCzJb5pktrI61LatVFJhxAhkkI70YOm1BK1xH5oHTJFz2xjo0Gh9IYmBDYX1WErU-soOdR98R7t1TBdkCwwY4YMj2KjOSCLq_SdQVnQTGecPeOXdr3WiNltxrPn1TLXaUR9dGOd_7I9WId3IhAkDZ76tzZSFYmxhkkl9VcDrXZ1aVBUE2oIEB8n23sWMfbWUqiDAgTvOMP9pEFIs-oQNUUozQWkhoM9p-cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=Z6VNpdfUiFCny2N4DJ5krJgWmHxQhXHwMsIuhvz2Mhk3_xlOVJVsFkw9AUiZblVVSB6qudKEqStw6-59Ub3i8-rp0CRxwR_josaIHfacfxcO-UCZ3UbuCzJb5pktrI61LatVFJhxAhkkI70YOm1BK1xH5oHTJFz2xjo0Gh9IYmBDYX1WErU-soOdR98R7t1TBdkCwwY4YMj2KjOSCLq_SdQVnQTGecPeOXdr3WiNltxrPn1TLXaUR9dGOd_7I9WId3IhAkDZ76tzZSFYmxhkkl9VcDrXZ1aVBUE2oIEB8n23sWMfbWUqiDAgTvOMP9pEFIs-oQNUUozQWkhoM9p-cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/edlo4ioW0aBRiBvWXKO3DJNY7LuR9o9Lk-Mh89-eJLcUeXSiaIBjSasCmfs1TqT80L-QFQRfPWBV5RHfCN6BOsgmoyHIPfrscItPcygBd5LQd2VKvKXx5OmczMSlxaTmH62b_59fvKSPktfU-Isg5ZFh1wld1od5Ks0BTcRAQO_9-orkNJqOsTNoucATTP9IpOTT6MAZwXXS-w_w-76IAAJljhbi5UaTvlqbXXnVaiCcJAZvjETk199gR2mDh67wMf9ry0JO7i_mAib2bkChGq5Z6aNU9AhnCcGKmMyzp4JTLXOpRS8DCunjbOePSsZMzlr0GmWV_xJKIr-HCF7-tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lezy0yNSwaMKcQUkW7ed64HkfQyexmVWJTHMftYbdYmfBgZVJO-W0__3P1LwwmfzlBWtJgJ0754rvoP5vKk2qoUDISeTfaai71ena19Ni5T9V3hd1Kd4Pa1k5_k13sShPdqs9tLF7kXtYdxASlXNbtPDYqsPcO46OcVwAegLnXnCXLNJJI48lU3CRz8u71j66IRJ7f5oKfgkm1FgJWpvQsjx-OZc1smdhpZVJCrhMh-D6ftUq0fGia8M4dyCXwex_e2qDpWCR23MqdyUrx6hBJFIXm0Jzw6o6sHjtbq859Z8i9yVne7-d5ULRZlkgiI7vg8aB8Wjf0X01Az8s4vDgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRjMX2IL68L5ewLcfMJMs4DebnHtPik_ENfUSKmJWm2dYIv4IS7pVbRl3huJ129JoSJhG_IRL7i78PE1jXwyrTAionkj0pdgh0EvKAqTy7mqvNbmO-JnBDPM94D4ugyxb23r-IsmzP7zH_y74WYNVrViW5QwRKZJ4C19i-Siam5Bfh8LCXDxec3YehmJvR-Z2uK_G9hNlPheU76KRVBKjgcjRuHX8Qw4vblLtsTNzN55mp5il9kvB445ARRbRm-8M2gGbFfeGtAsJQsjbHy1Pdm-X9q4kB_Vnx8z2Lh-g8xzmjUL3wkO56AxYdglSk5tM7PYt5oFWI6aGcSQfx38Zg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=uu3Y7uIg6G49Y2KizWdLYaYXFrqb4vzDLiapCvnioqKFEiYdNa1iRtU7QCYE-gc-vJSMeLWxuJkyVP00VUrYpPr0C-6Kwre6OhnxCnVK_H8Py8sY5fbNNBWkRs8eWtGPggmBjBnTfpmhznE-sjrZXCn02vsM2ewgtm61Jx_ARb9t9nXtKPiOOA2Y0UIxjbdQtsmnj_MOcZqd0YS3bvF1oKBKo1p9gHkIJ2A_2rT9Rfcbj0-AE9qlNHbC5DLfhoh4y__47l46PwLNYo2vQ28OnAiU0mJEDZqGDh2s6QlTcyiA-gUx0BlMISI6kI1MsVUKsDZkk9GKS9H0sLny-bkF1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=uu3Y7uIg6G49Y2KizWdLYaYXFrqb4vzDLiapCvnioqKFEiYdNa1iRtU7QCYE-gc-vJSMeLWxuJkyVP00VUrYpPr0C-6Kwre6OhnxCnVK_H8Py8sY5fbNNBWkRs8eWtGPggmBjBnTfpmhznE-sjrZXCn02vsM2ewgtm61Jx_ARb9t9nXtKPiOOA2Y0UIxjbdQtsmnj_MOcZqd0YS3bvF1oKBKo1p9gHkIJ2A_2rT9Rfcbj0-AE9qlNHbC5DLfhoh4y__47l46PwLNYo2vQ28OnAiU0mJEDZqGDh2s6QlTcyiA-gUx0BlMISI6kI1MsVUKsDZkk9GKS9H0sLny-bkF1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=e1FrO86xXb9c85JO51TmBBrouf2-yge4C3ByI4NA1924z7kJLe6LCW2rTbJ1rrV0Pn_dN_-VdM8RH2fcoLj7Un2-Ur4TQY1RbCArExFOR_hnI8ltA-D6mHwRA8I93clCRqJMUD908q8p1RJZz9iZJWVVSrPaPap3qbwFUMBqoaY7EnJpChgFBtgW6LbwbBLwDojB2RSCTImDsFT4R5u48V4ZSDGisPdtXxmWFdx0kFo5yZDtlK387yhTGx1qg_lL7sJZmZqIw-VCB-Hi8HALSEj12RYaAwZs8yG5K7qVxGsy4izmpfaZVEhUiFExZmPWKTYpjerqZccZKtqlEH5hEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=e1FrO86xXb9c85JO51TmBBrouf2-yge4C3ByI4NA1924z7kJLe6LCW2rTbJ1rrV0Pn_dN_-VdM8RH2fcoLj7Un2-Ur4TQY1RbCArExFOR_hnI8ltA-D6mHwRA8I93clCRqJMUD908q8p1RJZz9iZJWVVSrPaPap3qbwFUMBqoaY7EnJpChgFBtgW6LbwbBLwDojB2RSCTImDsFT4R5u48V4ZSDGisPdtXxmWFdx0kFo5yZDtlK387yhTGx1qg_lL7sJZmZqIw-VCB-Hi8HALSEj12RYaAwZs8yG5K7qVxGsy4izmpfaZVEhUiFExZmPWKTYpjerqZccZKtqlEH5hEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=UBF1XfXCW0qhfqafAgpd5HtwpSZZnAAV9uMRAXC4kjfoifIhqBCN-CUafUNOi-tEVJ6c3kNRu7ANg6GHfuO5IFbDJaLf0cEOs0vVhFtDHPCGtRfySALcjRDA7n1U4zTr2c6mjmt_--Bda0cznOUBtc_pVt7f1AHuIxMIMk0kbI0tLn8-qwIOEZ5FmROfkXnrgs37KOc5je5pjhItngcsXHJolpTeJopWAyrL5ZtK2v98K8ej6tlnA0MlQLyeuNlAe32fbqDF_XrljHTRmCbY576m_NWUZyDE1GdyYSwuh4mJdftq18bGVI09G4YKtXfXxdVJZ_AiJ_0F5_ElkhxvgKXPhHIBjY9Hze1IVHDtAvyhlAYTr7dIz2sP7hRvc0-kJKMT7JFBWtqUsNBvSiMrbOyaHnjVl9GEE7GddBKtpG_DkYHQUGwJV03mrJLBqemW0VXs69IMpMFZ11onLUik6bSZkqueUczVepc9sG6xzth6oyp0Z9aGaZjhlPJzp4BfkFrp_-CH2AloLlIK74xN6SgWUJVe1r1Wu7Fl3WLShl8biRvrXAsBY4abJKhw2oapSbG8VnAVGSQgtP4R-h03dMXxGnmUNF2XH-Ked1jpg_kuRhGZZdPz3aW_jRUyhsKcR1A--qdwBqY1-uLk8xHfUtqTpesbrjqC7YEba3RX0Yc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=UBF1XfXCW0qhfqafAgpd5HtwpSZZnAAV9uMRAXC4kjfoifIhqBCN-CUafUNOi-tEVJ6c3kNRu7ANg6GHfuO5IFbDJaLf0cEOs0vVhFtDHPCGtRfySALcjRDA7n1U4zTr2c6mjmt_--Bda0cznOUBtc_pVt7f1AHuIxMIMk0kbI0tLn8-qwIOEZ5FmROfkXnrgs37KOc5je5pjhItngcsXHJolpTeJopWAyrL5ZtK2v98K8ej6tlnA0MlQLyeuNlAe32fbqDF_XrljHTRmCbY576m_NWUZyDE1GdyYSwuh4mJdftq18bGVI09G4YKtXfXxdVJZ_AiJ_0F5_ElkhxvgKXPhHIBjY9Hze1IVHDtAvyhlAYTr7dIz2sP7hRvc0-kJKMT7JFBWtqUsNBvSiMrbOyaHnjVl9GEE7GddBKtpG_DkYHQUGwJV03mrJLBqemW0VXs69IMpMFZ11onLUik6bSZkqueUczVepc9sG6xzth6oyp0Z9aGaZjhlPJzp4BfkFrp_-CH2AloLlIK74xN6SgWUJVe1r1Wu7Fl3WLShl8biRvrXAsBY4abJKhw2oapSbG8VnAVGSQgtP4R-h03dMXxGnmUNF2XH-Ked1jpg_kuRhGZZdPz3aW_jRUyhsKcR1A--qdwBqY1-uLk8xHfUtqTpesbrjqC7YEba3RX0Yc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=anJ9mAojPYtE3S2a0dlJ5PGdX8jydX54FHXQ4zFkrt7zRvX8Eularv12e3es9-YJ8ooG6npE8NQxPxLokeJXJ2713QxnASI9nuGSlvFiui2inJMizBJnvdQX-SeeRRtDvKy8LDKy67wEKNruDkBfBibsDpgrdctOabLREeLbHEguiTJjjPFYiXgx95Z9DZiRUupVKIU8v5gwiBxba30No97a6EuYEa6U1VZZ5FmJuFifLLXK0esOOd5KKwS2eaczcp5fCtdcC5TmyAadf585W0AHUAkURWPy2m3QUe9164kFjhEdxA2uPosAv9EdUI2dWV6KUlKBAGifwt6Ak8YkpHE_SLdk3FbK31HFWYVs-Fq6QHCC16px4oEPFyo939ZA2CsnPUQBiaH5CpDTCCVFGvs5zdPlnrzMM-318fxjABnJf1yCzbY33OdlN_aBecYgqEfMGqLRqIeYagVrn8TLzliCYV_lPHuQigjRl2D2Fh-qQhh_47ieVc0P-nZsRtK_kaBA77P3hLiukrEeOR2TxherFw-EYVRAUmvEr2S9mTKywO5DiaayOCWiuhBWjpjMAl-osf38czFmQpg-fwGAVh24mlSVBe42K9OgxBRdy_aIHi5j0L3BbFdKesW9jqIrodNJ57KsO6CkcyY72bFx1aSXJ3TSXcboH_obJZvPK3Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=anJ9mAojPYtE3S2a0dlJ5PGdX8jydX54FHXQ4zFkrt7zRvX8Eularv12e3es9-YJ8ooG6npE8NQxPxLokeJXJ2713QxnASI9nuGSlvFiui2inJMizBJnvdQX-SeeRRtDvKy8LDKy67wEKNruDkBfBibsDpgrdctOabLREeLbHEguiTJjjPFYiXgx95Z9DZiRUupVKIU8v5gwiBxba30No97a6EuYEa6U1VZZ5FmJuFifLLXK0esOOd5KKwS2eaczcp5fCtdcC5TmyAadf585W0AHUAkURWPy2m3QUe9164kFjhEdxA2uPosAv9EdUI2dWV6KUlKBAGifwt6Ak8YkpHE_SLdk3FbK31HFWYVs-Fq6QHCC16px4oEPFyo939ZA2CsnPUQBiaH5CpDTCCVFGvs5zdPlnrzMM-318fxjABnJf1yCzbY33OdlN_aBecYgqEfMGqLRqIeYagVrn8TLzliCYV_lPHuQigjRl2D2Fh-qQhh_47ieVc0P-nZsRtK_kaBA77P3hLiukrEeOR2TxherFw-EYVRAUmvEr2S9mTKywO5DiaayOCWiuhBWjpjMAl-osf38czFmQpg-fwGAVh24mlSVBe42K9OgxBRdy_aIHi5j0L3BbFdKesW9jqIrodNJ57KsO6CkcyY72bFx1aSXJ3TSXcboH_obJZvPK3Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tHLxughOUCIZupMIPw5mOO9Vh5mgV1d1GpHAuXPaF2JtkLUxe-vn76YidX-3mUGUeaqN8qy_dsDT0NSd3g09Y5QS6WTPQ8pH--9Pk9ZDv7hHZQ_pQkflitcvrwz5heNjLAQkVqzh0ziWljBhTRyRwmzfi9l_SRIqqunBYlJ_l4zPE8tsaG96fLA3ZNEuZuPbbejToPRF81v_XD_HcUPR9SvtoiYrC-6M5TI7kYNcuPwYsp2qdrNaoK2QOC2sQYDrA8cdHi3_QsqRbhZD2z1yiWU6Q_rnBkMl6jTpHnWoJyhtmFgrDiXWBtq83Xz5CXBfPeTOBXryKvCuPxC7i8s_Bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=tHLxughOUCIZupMIPw5mOO9Vh5mgV1d1GpHAuXPaF2JtkLUxe-vn76YidX-3mUGUeaqN8qy_dsDT0NSd3g09Y5QS6WTPQ8pH--9Pk9ZDv7hHZQ_pQkflitcvrwz5heNjLAQkVqzh0ziWljBhTRyRwmzfi9l_SRIqqunBYlJ_l4zPE8tsaG96fLA3ZNEuZuPbbejToPRF81v_XD_HcUPR9SvtoiYrC-6M5TI7kYNcuPwYsp2qdrNaoK2QOC2sQYDrA8cdHi3_QsqRbhZD2z1yiWU6Q_rnBkMl6jTpHnWoJyhtmFgrDiXWBtq83Xz5CXBfPeTOBXryKvCuPxC7i8s_Bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B998og8vp4KKPWmOdgKosImdO-O77cWTo_rY76afbdU77vdKuRDByN5pulFgQauoAOYSiB-ZkxGjVl7Q2JkuSm-WLIbsSXve7ryfFLn5t1PNBX6zfN7HdUjoZDI2xtw4m-z37R6hso6gVblmNlH_C7ITvaYbrBUYLph8_mSpzYBCDyzbY5n2LuK5kGi0NnaajZPvyq6STVxBsc8_7XXgErHwBV-Ob1j3JvHaKUZSLU1nFtC2InTNbXRk_GnTtluMJSasQOWgmUXgwwFfD8LhnStzzdjGbGfwqFd5j51nG1vD3gdqDRWUGCRgy9bm8j7vqHdyxQJLvI7xieaAnYyivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=hJZrSBpQyjcAg5J97YdObetIF3Zadmp8Q9EW2moY6y7hdJZkWnXYUekGJXa7AJ1ssEbNpGGC09DdxM-o3Nj_bS_XrVlVMkWyfEDWvV6pXoLova_OK8BJCRbMIRaJxYib7Jt1tDZfEFtCu51LeicMjzMnZ0MSHau3bYrhrMj5LieSXrDkhyVe7XYGO_5_o3nrBNZ-Xatq0UZxtYLgQ7djwI3zY4Zo06DtVQf4r1dMBu-fw0j9Iur9YYpDBkDqtWisPWVFnylVYYmxW4TN2-Guevi3Ju4bEztdwg0PYPMDqBPbKyg70C0HD-tZMctdMMXoEHY99HSoDd9pjiXPer5ZUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=hJZrSBpQyjcAg5J97YdObetIF3Zadmp8Q9EW2moY6y7hdJZkWnXYUekGJXa7AJ1ssEbNpGGC09DdxM-o3Nj_bS_XrVlVMkWyfEDWvV6pXoLova_OK8BJCRbMIRaJxYib7Jt1tDZfEFtCu51LeicMjzMnZ0MSHau3bYrhrMj5LieSXrDkhyVe7XYGO_5_o3nrBNZ-Xatq0UZxtYLgQ7djwI3zY4Zo06DtVQf4r1dMBu-fw0j9Iur9YYpDBkDqtWisPWVFnylVYYmxW4TN2-Guevi3Ju4bEztdwg0PYPMDqBPbKyg70C0HD-tZMctdMMXoEHY99HSoDd9pjiXPer5ZUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=v2XMxefln5FKu-nO1ILrxNUC1zA8qs1w5PQZAcy2VJit67rxu1TkdYUZctRKHRVOT9iUVI2B_NA4GHCV3_NvahtZCJi6I1aY84c3zTwdFIljY_sWvEGRDFlbMHq8kJwt4xS5iMd_L6l_dqKEtFd6g2uUpVaxaylvNd-_qlIbAyLSO1wGj_ZlFBYqTkxYKe4CJ6FOb4fBSAdecRtUU3TxaqdmM0nDevbaX8bn80uGLFkuQoTsAgPlmB1nvWAk1H2Vp5bMIqCK48dB67GGSsaV-5BGomdSh3tZ4gFpIMdHpqYF8lWkx4zmL1W9YwsbImOQtLtuM1I9_I6sssP493ekIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=v2XMxefln5FKu-nO1ILrxNUC1zA8qs1w5PQZAcy2VJit67rxu1TkdYUZctRKHRVOT9iUVI2B_NA4GHCV3_NvahtZCJi6I1aY84c3zTwdFIljY_sWvEGRDFlbMHq8kJwt4xS5iMd_L6l_dqKEtFd6g2uUpVaxaylvNd-_qlIbAyLSO1wGj_ZlFBYqTkxYKe4CJ6FOb4fBSAdecRtUU3TxaqdmM0nDevbaX8bn80uGLFkuQoTsAgPlmB1nvWAk1H2Vp5bMIqCK48dB67GGSsaV-5BGomdSh3tZ4gFpIMdHpqYF8lWkx4zmL1W9YwsbImOQtLtuM1I9_I6sssP493ekIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dqfmDyNw_g2JuUpVs_ByuAwy8uVl32utcrJsC4QbPvCldoKjbsVcFzVze8mV5hGTqkvn76s8gk30uHe1f94IP90I4M-JppcA6nXBt9kpU7tpnMI9NWVPxP_WP05CyMkqoVpUC4RCXhuDszpAvnUKOk2LJOovDLIEcNVBHFQuK729A4RA9PgskeLEo7dOPpgiubj7n62n8UXK1qeRaq-iwklY-Ah0DpGAafNTo_U7OlZjyS03nQTVoLXw-TcG0jWny5KPr4uDYEikE6d3Qvq8Tg4jwYmh3nf4jziRV7pnUTvTthYOSduSm7I384pDOXg6XVLZAJgNYd7NtRAvSbTnpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LRQcXxzL_GRC2L5fUabs9dfuO84rvgqc5ZZfp8_FExxV6CDZVia6QsiHmY12wKUbF-WuCfk84_yVwuA3ZfC5Ssw4wP1eEF8Gpe1tWKPj3FqTqQQE6tfRTVwUEGsldcLDAKUQ2OZeE5Y0O-87CIKI3QfjqvIhDnZ-nfTv0scH72lMjwuZkUmPoonBJ7no5qHBm1cpdLMwpqugLRkv0-m70w67fy_t1COrlsokLwcNrjRqUhtq3SJEYgoj0Y7_MgSLBazjd-GhL1z2zrdfxTqOnh6Du9dAdVvj2YAr-8bmSe2mP6jC1rk5_uS_3ovK_EBPG94oSHCbBdWXwDOlZkKywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D4ZnRvMnbNmfn2atVyhe0uFzxZcisYnihcEqa3s3EEOjvIkVy4hlKnG1IEK6RqVvI4BoLa4hxSmKeq8yOSFvCE1iphUMtcwQeWjPq5EUBepsB1nbeO_PJOqylgJCTYVUt0qQdJ-uJWNAQSrIJDh_MXKGNkOcop51L5987G9cD48KfE2w3Lw0IrxO7i2wMG8ItNTVBWWJiq-dqeMJliDr_Ug-asnKIa-1JZXn09uO9GuPpfstggzVc8mNGxI6Hv1pezG3iQWCN4iU5avb4siRornvYUAwyL2kPGzjEaPMjJjWvrgUGXYqvRN_5-ee1kTLJ8rLHsN4ip5hUKPY8u6eTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jm-E0_eolxPIX80UqZ9_Nte4JdVfWWmj7Y5VrP5Y4Zcv7b-6KajDccKBBrXkMRuKfy2l-2sJcD9Qc6B-qxzLFFHmC3Pzav7Bjf6mo3fcCVGPBEiCY60HLJhxEleTOwq0gklBvA_dbS2bc7mqOKHJuF3o4qxblrh3PZ-DLdFQoEYJF621sAH3m65i8QYPlQMGB6FWo4K88NqT2w3W3wILxKKbG68xp1M8ix3ww-FMgMZHH8eP2zl9GXv9VIE-nlrmMnA3vANYPnuzX0cWMHUU4Iy4lv5AsCo10Kt5o8YvYI-LG8SUrcCOcpXIEFx99rkNCDCBAJDx3sMaK2jv1Xr2vQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/axvOEPtFx7lcIq5yyzimC0JHgEFIbHsFSwmbTHKx8I72_ZqnWlPB6vAUbuUxgnv3tbXkNLsg9I501dc-s-o1lX1V1oXbldMAYFJTmhuKTFzzBr2_156-YvI3vteauXS-i0vIZK1TIzoxZv4tpZwuckjPsZ1zeBRtaKNPgzVX9_PYeK-WsHTwutB6q7PotL6Jxnz3H9pxxTC-NPFO6f9IWdeoQ_s0WS1u2iArIFA89wYgN_keb_D8b1TduUCUf6OcXTG0XNN3mCliElKyBWqlzGGMX5dRRYc81U3yinwjrUexyIpnk-W9vlLT8db9sshVAPmnwDW78TIvoH27B65Q6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0fxX2vT5fcz7zO4lGSyubNNa2YNM4hFy6Ld_QAYSr-Oj42uAXUcC--J69zgFteHnk3ZtlZUTnNzYiqb_CjzgdQolvq6ESwpVsd1KcVNIfaIP8Dwv7KRVUlhYZCxoJDuKm9th10cf8V-yCeyDdXK-6VtSIrApU7PXqeaFVcU_8PkAzgsMphcGo9hs-bMnWf6ilpbChO-XWwqbUEL7kuP583hwMbtVMbTaT_50XF_gOfLAvFdAExI97bsIOVkH2gXgvn_LZFPgFeM9nFo-LLnkbGHh5H7F-aeLttUJ5PdmQlWDghC_EYgH6dDSEJkQNLGNiA97rtNbg0sV167-nO33Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rx5dr6g2ke8EINR2gFu2Ura9D90t2mJ6bAYCOnIf5riSsgLg8MnGEbi0TrBYfkZefBIiW_tuTtTPhoWW-MIr9BQ6uN43ddccqYrlRRa6dqvH3VC7WGjVTy9gE8ToFYRYTnUHMUFA18CRzaih8GWHFsN4BU-VmQmOxoi5WvXx94pj2PQu8MiUV4kXT0u6SRHsvBa9ftuRdR8dT-NFc8MsERhNIql7z2uIX_DfgZDPkD8muGgMAVyqlT62UOdMJgLxw6vlDxb4aw88sF9MNwBEheEGkPmn4nDbH0rktvIEDqgcQz9fZiBwo6-acafPWML5p6RFzXK0kaYL8sk6vZ0sVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ug3hpqRUo20WvDaB5hMQwmrRO9rIUcF8NMNH_U4M0I2NEFM_jfST4U1sAG7fNK_sn63fJm9o3XDAdjyI3cg8oSpYZL4yvgX5PkWvr2LJ1FDKkzYkwwxY3cdIPUq5mTz0vaJCXbHGLWCU8Lvjhb3O83wfzkOZbDFijO_eAjqfD9Ikx5FSshSq46txEIzMby0JmL5yZBgfLlfwdOWaOU1wr310ufyAtrNrMENjOtO1vmy7YFGTW-uQ33ZBYgSWmswxqZ-9u--k7-5swYvXMV5BYXxkk7yGi8lrfZiRwQbLeTsGhFoH1YQY7Ni_2k_a8J-h1QxazVVabO8NFfSp66de5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFhOLW2On7V9ClL7BZrg7QHeBBNOzzCUPa6ZJUO99fWhC5u1ClaFCJ-bH6yxOkPGyR-bbQy0pRiaspUYchFVgOjqKQzhCoAj9YPUVEW_0oVppDSpHkxEJrySkXoiUmhRfV2uvTBeOJSjb6gX_Tengsra4_HwvtWH-EUOMjMHnNSRP8IqSvVLAs5mWMCnWd4Z0dMYbwzdPHUXdrzMbyF-rB_o9C2tdbEUeOcpybYfUXh1KP44jgN5uZYKAsZAQyLxhYTbefJnqIg1epmb_WpMWWH6tzWXlcGDfDiQEFlGL2PsBzxN_vctIAGyKX2_U01Ack-0d8x0vi-6CADWpu4HmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NY_tKhBGSr0qsbmzpLMTjYrgNngvUbN1d__J8eWg4px9sjuiMgkuKIeXdUca5iKnAlWmSVkABfW_MPXLRMmIG-PUNtrStD_-FbjU27bThreoChfsOdbOQJqVq4dgl4zjDSSGQ8414MCc5DvC7zDtNRaopRWtIYw5kSy8BpFGZpItDutLnfWLr-BI0QekZDtX6bQ6UI_ujCQt7dWpvoASYRMCyHpQ_wq5ao-z-MBcGDoyIheeLFyiB6GV4zdWc0F564lmjNY_d1tVvSdl66qYHGYBG5O3l7075G_FDDublN7wP4q37iq7LRuqKcGDu8OfE9DIAKjkVd7gmONRNujA4w.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XBOs8a3RsEv6ITtKf9UtwqUsEiTcG93KvOpIWIBQvYg79-z9T-6uhkCiMlyKHLYFagbVd5d8s0dEidlf52TqPmWq9AbPJYQgwCFJmhKr6Xk9w1JomeFxKFpfVLKsIzhpXK_XJARD7Tcq-WwqwAy2Y1fybyEj1Yot-VTlRLScx_yJWb0fuGApD577BYPSI49XKaziXY_bnfdkoRt7AL1p_25CTwBlEkQ7Ea9M6Z6kECS7GQLbC0LKu7sJDMis__84L2BXj6rxxHpqeH8hrs-dATRDs0AW5FV8r5O2gL4RccefnAIzCxUQ1M5RrUphzkfC4lg3Y2FRqRdC1lhDpHJmLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=XBOs8a3RsEv6ITtKf9UtwqUsEiTcG93KvOpIWIBQvYg79-z9T-6uhkCiMlyKHLYFagbVd5d8s0dEidlf52TqPmWq9AbPJYQgwCFJmhKr6Xk9w1JomeFxKFpfVLKsIzhpXK_XJARD7Tcq-WwqwAy2Y1fybyEj1Yot-VTlRLScx_yJWb0fuGApD577BYPSI49XKaziXY_bnfdkoRt7AL1p_25CTwBlEkQ7Ea9M6Z6kECS7GQLbC0LKu7sJDMis__84L2BXj6rxxHpqeH8hrs-dATRDs0AW5FV8r5O2gL4RccefnAIzCxUQ1M5RrUphzkfC4lg3Y2FRqRdC1lhDpHJmLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2JgRZTaqRCyUkz_N8c6QneGYNy9bHYrF3PDnO2Tp5eX7VrQu3LRwkafuTpcKy1Vn567qp-YFvRZURPm_WCj0yfQLXsycsYgc8Ekth9wz2as5nVh8zn5-LTH-_FpXSlhtRFuqe62gWXK9d3Fd2EfXHzu4X_D57-ofTSCoEmKMV2UuEJUxWLsq3xjm99_AfRYpAV5MbRftfrUM97Tgaip3QLee8PnmWxjl1uTuowZaMUTFA31jZsBGW8RSS-5zvcXb5PG5pgr3C-0IB-Y-aJUqeWo4dNqgs6maa6wDG2V0qqA9y89gMMiG5h0ADudj0W9nuROSFL-W6so-INOVmXvxg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNgEhH1cSlELuuer5IMxphkennoEy6BUHBzjvGyycnAh8U9_4tq8k3cQRT-T-sDS5bBTL9hvvJpXsUEp8x0RdRSYnDt-GlTHxLPs5ALxVqr2IxhP_i2Y5zaGRZ0mY2hFdQ50HIlT7UvZdZV-ZYCw4E8vxPI-itdrvOPpcCgQ4sHLsvGneiawGl7zgpFH4kIOqfB21WVdgxi-ZfYYQHQDGruYOtEJmWD-EAgKSjMKhABzx5fBXFmgBbz44_4iH0AfIfXSOQsH719Ny6IU08Pa5F-bnl7ktVGdS4clfDOdc7lBjIPxutz1aewVBC5iLSY0bzs7vduvFK_zieaMFeq0LQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=r-fKLNSTCMm8yryTg-BXm90cHo78OUpVl6TR_VcKvruh2g8U5ctZKOqJ34aLwDCe8XHSegsBwVGKp7Nch8AxYgZiMmLP3wu5jeLKI19ipRSnLB1Ew_gF-0FkDAsh1ELEG-mYc6ZYgKrRmlASDCJMDBaXfaGYHnBGyp0zbIZnu_a1FD4L_D5Mi9eE7q_A8xF6-GyQS1ZO6n0lqrTEzDN9kzwD68041AtGcuEPAucd4blreP9HRsiuYFVWoie2d0JiLYqU0oth5OQ770VmRVC3Sw456zohE1WaF3BxbJyiPuanr8ikZPCWO8t5BxHEuTHOqRYEfdsTN7qaduHxGjPfWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=r-fKLNSTCMm8yryTg-BXm90cHo78OUpVl6TR_VcKvruh2g8U5ctZKOqJ34aLwDCe8XHSegsBwVGKp7Nch8AxYgZiMmLP3wu5jeLKI19ipRSnLB1Ew_gF-0FkDAsh1ELEG-mYc6ZYgKrRmlASDCJMDBaXfaGYHnBGyp0zbIZnu_a1FD4L_D5Mi9eE7q_A8xF6-GyQS1ZO6n0lqrTEzDN9kzwD68041AtGcuEPAucd4blreP9HRsiuYFVWoie2d0JiLYqU0oth5OQ770VmRVC3Sw456zohE1WaF3BxbJyiPuanr8ikZPCWO8t5BxHEuTHOqRYEfdsTN7qaduHxGjPfWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jpzo-f3a3R5WS596mPqfsIuK732U6MoTETf7N3sXlZ6C1gOtn0IBB2Pj6av5oNZZBpRkrqyOSfVy2XPHX6af3qwVt2In1aRrRkDqAnxLb6ThIw26vEW197vv0B8DgTD2xhANEZxzC_MNh2zgkhXXGc6pZkcZ-QFNMpH62rhjxD-FeraYdIe_4CLeN5oU3qSLLvx6ycKyz120_EuGVm4AV_tjDwImxQ_noANHjOGTpVMiF2stnJjx-I_e9jm7wVNM0DKqXid0dk7qwPkj-1z8Rx7YG7Xv4Xn3o28puVdHpuVmuZavCblfZHx39mEOrpZPI8sSegBo-jONs5sBjGGcDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=jpzo-f3a3R5WS596mPqfsIuK732U6MoTETf7N3sXlZ6C1gOtn0IBB2Pj6av5oNZZBpRkrqyOSfVy2XPHX6af3qwVt2In1aRrRkDqAnxLb6ThIw26vEW197vv0B8DgTD2xhANEZxzC_MNh2zgkhXXGc6pZkcZ-QFNMpH62rhjxD-FeraYdIe_4CLeN5oU3qSLLvx6ycKyz120_EuGVm4AV_tjDwImxQ_noANHjOGTpVMiF2stnJjx-I_e9jm7wVNM0DKqXid0dk7qwPkj-1z8Rx7YG7Xv4Xn3o28puVdHpuVmuZavCblfZHx39mEOrpZPI8sSegBo-jONs5sBjGGcDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2QVRymIB55xYPHcuH5anUP-kyxkDkNjc3YVxLicYALaC83xPzsGMfMMjVmrvkP9W4hqXOo1T69yt3XTY_n0Qp_7_LvcQOP1gIMPJb779vXVU1etIHjdrPtwsX25-HiTgbKc1DqVSMU4V5UnMzgQe8yW4lNbNyMDivHcOB9y748Ixs5SW889odl602iXaZLa1F4uzLQdr4h90TBfYaAJIVyxXR1WfxAZL99w3jJwHBfZxdOaJCGgTmAufQdoXOmbYsrfg1v7v60XsQYvPEVKRsJYkA_FTWYu7hvTaovLhtaFB35sM-zFKdPju9ygtuBFwsj_vhneyfLUwcbYICKm1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSmJYcB0_2d_KMJ8p35-JOvhrFu2WorwoB4jGrRabdLUmeoHkpCka781-wARyWXqVi8kijJRFuyIGsJ8zeLVxPs-se_liRiBg3EhgHNeP-HS_vc9W8Fvs3VTkmeVXHVKEjRJDnye0BvNcZVcTwk-vIjw6w47R0ZsFjgwvJpS4x9CvSksES2042-_CTVRYBq7ws2RBkNd48NV-nzaVFa9p9-CfLjq0bCUr1ao7U7qwhMeMD8xo1IQiHA_hHXQkaL--G_DgkGVPBwb0KprRtgvy9bzbszPQAw0Nn9D-z6jNGQbvWSzQsdx87CIbfCAoPne-SL7ltR29aOJwfUcltrTJQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WTheLCIXTqxI6_WwBlIDPLJ9W7kpHSLnmFpZnAt9GiVqijTfVvl3pzJa_y8kHlpqyRYv_Tjwys3aJsetmf-08QM1OwJWFPZvyaVwFPvJMJpxck7Xg_ZqwP-zHyxLemijGb6QuZWpniWfvHaa-usSqo9FDbtBmAFppOzBfWXcvkeATSFFv2AlKpWvRJjr9JtBIzb5o7eb8NsTn1x5Cg2qb9wA3o1S_EIY7wvTC0_cpYD9nMBizSHZupCwp4W1Kzzse6abvn6V_XtDrGiZG3j8MDlEG_ADXh6h9lTu_eIWzUwvbSGobACE_PIeCdKd46usqzhN5EHT2lvi6z-ZnCaUFQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GkJzY9xBmJTrStVCWl_p6Uj-HIejMDWxBkfqbiVut4Wlj_Qfz47QthOMQ23Ch4fomubd-wT_PhCKTM5rNYVji3qj-ifeq8rpxbwxE6oz51hdBCh2na9XVMbQY-akY21LXbDLeSbbspOmfLx3u0rQragHB7L8m6tBXByiDEeWEULNo7zOk2_tF1M0qffO9l_WLikH3sDWyRrFcnZbCTHt_QUtJTJXVONecGvfWQnG0qYkjOFfqI_janEjRm8brm2OLilXGPZuaGC5hJa8uSfSsDhvK2xGXdTUMApYLfnPNJAFhtiZ5g00-rrofo8J8kyTT_DNg0amcWzhyodCrfgoGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GdAzL3z8ToNuCAnzs38380ndTs1BThaxGj12MgA77MVRXYY6G0eh1SAbHp1tY7zrPETxj1eADs1EXdEs41PIMOGQKyGx0WpGWoC6GgKwWzVQLYVhCWhxeKrwp6Ghh0MoM0CJP1EBWPns8yhicaIe8H6vtXJaTceUPkeG7kOUVMmDzMBcV243dKydBI2v_e1LSopuyPcUU6WhQWLk2D3ZKc0l6Go9eyO5mhTe9WnKP6vFpmi723UpjwrOYzPn-xgMlThRWfaskg2my2BWJVSXYHZDeOG0BUF1s9-j67sNLHs5jfNEXPVShVPFdP-aLIKPhTmzntKzfjbPBDTLfGUk9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eu3ZFvP_sC1fwhZP5Kw87SSdNKB-UtO_w4QSVyKiZAt9WEy9lwHTQ6q6_qYkLGiv8uXTAPndhpSw_jPqQV3BA69_9jC58C9F1PXZSPH8qvLwMO3Ay56gCH6JnMa5nAqUSdxTQjfESwr1_B7-Sf6Y_gCSQrVzu76f5IrMtn05KZsudKj1DsPlwROm-bkfBTtnSm_rDavzRqFPjsNFYj0h8-4BfxBhXEH_Sld6C7CmX2nV8K563L04lRh6vSnj9eqUPza-RJMOxscZf37N4kaFUtmRRYdHa4UsoqNAsIhMl6vh0Ca017BhHTJOTB6nhWqDa0dU3h-5BxYrssAC_YvCYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZDCHUeBaJcF_itoub16cS8WKDtmU2_ABjBGydS1r7sj0FYxvQc7n2mGqnlLSnWGVB1mTnAFfM0hRKSUL9ucniA0hT0mORvYW2OOlqPI1SB81SzKh7LNT1s8JpoHCMyOfXUTIjzMed_sCrwHt14hlDM6mxN2aSRhQqpK8eOig5At81j9My3QhUWuLW0X1fUnvCfZIjB6Qu_lCEg7jq1ld8syzH8s3lmlIekl5_BkAQrPVHwYjqT_EAoUd6Dw-1wr2qiUEiwewkKFHCE2U4seqpNJ9DQfpF0NsPam-b5LXhquhnQ5C-LeGlzWbX9wW6YLnEtZCdWc4KWYoYVP1s_JSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btTx0FtGUhl3A9uec58GFT4M38YvckBQV3Z3ILBosXesMJ1yWHVhc0QhwTr754l9kyS03dUwCkdr4B3hoFeMypwhbNr8YTWxZXHi63uPVpzF_sU4QgyNVmCr8GaoqXw5-bZkZdLkb3UYzEik9Hjk_mDzdFZbv8_dSMNRxyV4ylV13e4RtfKkZAfEAZmyTHg8uu65k5-7fRHSdkXVA2gm3RYcAGDTqmRyhsR0vtLGxwgWipfaf-NCOWrBa-YueO6u9u-ZlO5C4GgO39W8vlZTEbw6iIRnuwE6UMMRpnNvsp85yJ9x39h9MLze_dfBEHx7VWoZX2ttnCYRsU3JtFShNQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=EvLlsS9H8ZboR939zNSs2lPjs668HTwdZ8hnpwYKM_fJm43uI4Y4Zagymc7to4aDyzk8Gyxgxpb_cgO-l0ETqWoWI6rQOeL5T_kvl75dVKJWhHiVJNKF6f047nkyrZycWPIZ0mEzbOB34fFUDw0CXJgraawDQGQOC9GmRJfxVZsB0VgtVt4Obk-1oCnTyNRcEgCuINKEEb0lONhfP5QiQ0jbRwXesCsVdRlKFK8KYFD5B0TcBIi2a6T28Mn-nSwZHCHmrsFlSk6fybkwUzxwPPoxoZrP_3ieocXHn0xNb0nwjcL7dhCdUS41UflJWfjH9_FLSW5pYb1Pp_j2SMzF2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=EvLlsS9H8ZboR939zNSs2lPjs668HTwdZ8hnpwYKM_fJm43uI4Y4Zagymc7to4aDyzk8Gyxgxpb_cgO-l0ETqWoWI6rQOeL5T_kvl75dVKJWhHiVJNKF6f047nkyrZycWPIZ0mEzbOB34fFUDw0CXJgraawDQGQOC9GmRJfxVZsB0VgtVt4Obk-1oCnTyNRcEgCuINKEEb0lONhfP5QiQ0jbRwXesCsVdRlKFK8KYFD5B0TcBIi2a6T28Mn-nSwZHCHmrsFlSk6fybkwUzxwPPoxoZrP_3ieocXHn0xNb0nwjcL7dhCdUS41UflJWfjH9_FLSW5pYb1Pp_j2SMzF2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJlByO7RVH3hhJFW5v-tHYNqTXjEA_cFfgyzsuyPAmQL3OwGYAJndqjfbXzTS5Q1fy0YDlIyoDq1GlSX_L-QY_vKrQ0Rd4uKCdgjxebWZMaAIGqileB6OIocMKg-NjDrqiVYSYEHhfaVdAkn4DT0_fulckc5Fww8Uc60pzbH7DCUG5Kf_i6G_l-mCq-RE0uSXw67Qoas0g2dxRiZkRJJo8PqRmMcudBNNDAcZ8Z-Ls-sdBPmbjKivgI8WrXt0lWyI0GUQ6eTvMYD9gMrgPdgtMZUVIx216XKOkwN583SL7fPBDa3NcLEndIxcJswC4HnOiYhzRGPzqtrdb4lN5_z1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=tD80KLyBaCaVTrMAaU7LMWUeLut8U-C2pem79wahvd9oCxkow9oh5XAyImclQxDTya-zXUkOetC1JICKZlAX6QjZA3c8EFEifuJUr4KBPlSEQRcy6-aYrWfv7ccOFHyh9u2Vf0iKFQhaJZ3SMN461Re-AgBDlHC0282ueI2kPsRQoV_rySzb9gWIWZAbVqlqhBUfMOdtsysZpLlpOkIQgPHQxv9p2r3bkYhCiRf2qjl4wX5KK9vao_qp6BBgm6fx5kW-EL8-btaewzUSUZaTpkCOrVCCSf9losu0cSGHPGINDtnk56b7x44VLa58MxjaQ3OguKm-6hGfiwB4ioxdFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=tD80KLyBaCaVTrMAaU7LMWUeLut8U-C2pem79wahvd9oCxkow9oh5XAyImclQxDTya-zXUkOetC1JICKZlAX6QjZA3c8EFEifuJUr4KBPlSEQRcy6-aYrWfv7ccOFHyh9u2Vf0iKFQhaJZ3SMN461Re-AgBDlHC0282ueI2kPsRQoV_rySzb9gWIWZAbVqlqhBUfMOdtsysZpLlpOkIQgPHQxv9p2r3bkYhCiRf2qjl4wX5KK9vao_qp6BBgm6fx5kW-EL8-btaewzUSUZaTpkCOrVCCSf9losu0cSGHPGINDtnk56b7x44VLa58MxjaQ3OguKm-6hGfiwB4ioxdFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=haaM_6ctcFdHXv5ePS7jLX6uQUpAjOTgQnMqiNjXAzlbqxJMC_V4dofT3AVzLz61HyWY1cOQYstV3sEC6eY9-8W4DlG63o6HXophbVSOWbZan1nX0i-7-Oa6nJsuL8FCsqb-xD7nsOGAZu4SBjr7mikuwJvjCX1eJdD1bNn_X04BWela7Ps3zvPjI_RKpHTExXk9pBftKjP2uVOiocaxwqY2QRrUbUQFqQcCnzRVoEMvfOmfb6QwlOF2Hwg80g1azisE9qsNGyi8AOYVY3BSFJGDYtOTQ1McWvtlQrQgHP3sYgMyETTMfjDsPsYL0FUZ5H8MB1SjWv_pdLpdukgwYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=haaM_6ctcFdHXv5ePS7jLX6uQUpAjOTgQnMqiNjXAzlbqxJMC_V4dofT3AVzLz61HyWY1cOQYstV3sEC6eY9-8W4DlG63o6HXophbVSOWbZan1nX0i-7-Oa6nJsuL8FCsqb-xD7nsOGAZu4SBjr7mikuwJvjCX1eJdD1bNn_X04BWela7Ps3zvPjI_RKpHTExXk9pBftKjP2uVOiocaxwqY2QRrUbUQFqQcCnzRVoEMvfOmfb6QwlOF2Hwg80g1azisE9qsNGyi8AOYVY3BSFJGDYtOTQ1McWvtlQrQgHP3sYgMyETTMfjDsPsYL0FUZ5H8MB1SjWv_pdLpdukgwYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XUb2PWiK5x3wVapouATOhgY5EkF3x3hnziytsrRIT7U6L2VsradLgRkh9soI5uRDD4h73lx0DYCqEHcVSZjGGODyylOXitX_cFjAT4kKecAptiguLPoTtdk1bqx32LcOriM78C4JOQuPM-0AUDUu9sLjiDXZi0_29PDEltjjXNOrcGMPjWdNlWfqA-HP_lrY5Mcf16TbixNHBHSlDPp1K2t6JOar5WMV71T7pa8lqoby36Eqfpm7fYu_2rm54jF3YSH36o8FaEtf3ljWVT2XlvScDPx0wD0H7yWbC5PSZ99MDtxKlTEUxQKy-cFuLhemyqN0MHzWGZ4PVa0eZyJSwA.jpg" alt="photo" loading="lazy"/></div>
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
