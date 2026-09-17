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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-26 22:11:46</div>
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
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6748" target="_blank">📅 14:56 · 26 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6747">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAxG7YVglpKQtz_qUrBsKIJd3nODp0ZJiY-DznNOM3kH6HbcPosYUQpEUNWUP1QcyCw0MgckB8YKn_v01wLTZA5SAB9zJNln0ZctPhRlY0Jj2M4A_Dd7SmRJ76ARYFVXN9X-_-BepEixR_2QfctgljAusRixVTWbuq0BhwpbV84wm_F_jQtUrOcPXkD2Bbgp5XDA_Ivf4jyL6bXppRviVhMsGO6NP59UVcBdqvIeraJlZhaTTrxD_hOXLrigsbnOr44RHmCZoH9stUZSxxYwEd76xN_63NqFpqbXXdwAyDjGBy9_zY_2D8W7MT29xP0DDH1TdVvxnNZmXTP5CKR1Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اکسیوس: ترامپ هفته آینده در نیویورک با رهبران هیئت‌های کشورهای خلیج فارس دیدار و گفت‌وگو خواهد کرد تا آن‌ها را در جریان ایده‌های واشنگتن برای استراتژی پس از جنگ با جمهوری اسلامی قرار دهد.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/farahmand_alipour/6747" target="_blank">📅 11:12 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6746" target="_blank">📅 11:11 · 26 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/6745" target="_blank">📅 13:24 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6744" target="_blank">📅 12:10 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6743">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ie7_Iuhz4_0xcOrTUmDdDwxOY7thmSJX-6XcyY4-cDjXB5QUuf0jxh2I6hDyZmwLq565APgy4lh6mcQIf3yEyj8zQVvCmSTCxKwP3DD1AGfbdExQez8Uhepwap2xkERjzd-Bojxb9v7kz-_0JhIyjIDiaRvvTdOaPQvAXszzN_5Urs70ijOjPbjmtmvFGiEfctHzv1bvML-zLoTc7jwA5o-MiJu7lsPFNwNsJZwPAOCxEDPymx1DsHdqvDVZ-4xby7sHpjXYdycjuh8RzeM8ot1KFFRtRsE9BwEuSEWq3M7GrErXVkF0vGnCqwa5ns9w-yajNohrO8Hz_khZJYCZKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبری که برای خمینی ساختن رو فرعون‌ها نساختند!  جلوی چشم همه مردم از بدی فرعون میگن و خودشون ساختن و بدتر ساختند و بدتر کردند!  حقیقتا فرعون در برابر اینها، فرشته است!  می‌دونید فرعون «موسی» رو به عنوان پسرخوانده پذیرفت! یک بچه سر راهی رو!  و بعد به ارشدترین…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6743" target="_blank">📅 11:40 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6742">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hP7x72Hy0Fa2XziovhkvqBKFUX2B4L5g1gbWJCIfiauaqmcRDdDcYgY7ppGPRC-fjxmAOABxurOqgEiS6F7sLGo5fyyVlUmmgaeN1kpEnTm6CnTlH3kysJQhftj6Dr7cXv2h5fdZQtdoO4kvSHkwKl_QKOdIYVRH99Pena8aEfvi7bO2b5G6yWrbsfkiOEVSyVbjptD5mLXjGfAlq2htAgHIbaCt-oKXZaPxTn6yR5Si3c_0AmUy0vbSRUllQez61xTJ0RBUJE4bZ1yVXXzkFr5Bp10JbWL4UHmwrtusz-gKLlk_M2jOOdQPy1Pyf2a93V7L5jiTR4v-NetzaUmJgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رو برای مردم عادی میگن که «رزق و روزی» دست خداست!  ولی حتی رئیس امر به معروف و نهی از منکرشون، که هر هفته روی منبر اینها رو ارشاد میکنه،   بهترین و ارزشمندترین زمین‌های شمال تهران رو دستچین و گلچین میکنن!  در خرج طلا برای گنبدها هم نمیگن حالا آجری باشه…</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6742" target="_blank">📅 11:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6741">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sL5JuPtHA0SSfs6Y3rPmUOWQY9p4ntNG9RrSDYhYqTIWlswKD-2RL20jPTRYWsGFmcnXoZdHysxJ9thRkhfTmYtgCKA5iNhOWhEoHTe2BhGke_hEqGqdrYqtB6JKOzMLsF9fwI0t_8Cf9T33QWTIGScm4GFVaOgACex0fs40-J4LuXlHzjOXsvbr2OX7mVcnFjWgzydBEXdspB6AL2wUCY6VrcmQ9cUXY5qRJKA7RjKVT05HcE2ZdWYY4gJwVB2qgH290tHm72pIZYaflGHACwPokyDQCmccS-AnPDhPB-k_h-GDimmwICSKT-LZDGC9_Yx9u8VsHzV0oJ6IuCQKAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی سوئیس باشی یا غزه فرقی نمیکنه  مهم اینه دلت با خدا باشه!  علی علی!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6741" target="_blank">📅 11:30 · 25 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/6740" target="_blank">📅 11:25 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6739">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S8KGfBKiFw_3fGy66Azn7-r-N4gZT8-nFls5nnHyPxpytFJ7jHecFsRzibmrOGI3a749vUuFvrdo7zx3GzktcTjsUA9IwjcoqL18lq7F1esTvuVgi8wDP8vyv94scTwJCIVsX1I-NYpgeGRfZgPiEtFyMqCARzWlzzjL4AwIIRKSB0mA8-uZ95AaIh1DIqL1egLkFCizKOq3XhVdiQYT8aHsRcEGUoUpoQnz8rqHcIacc9k3MwYCDGZy57NIfaZYZ_naiZdMh8IMzJvLkXyLVOe2gspDtwIGBKAUkppAk36BXlibN3HpJwxLjl05qsGUsB6bW4h71AYtEDk4Fga8yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیلبوردی در مرکز تهران
و دعوت به آموزش کار با اسلحه و «یگان‌های مردمی»
حکومتی تحقیر شده در جهان و طرد و لعن شده از طرف مردم ایران که فقط به زور اسلحه و دار اعدام مونده.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/6739" target="_blank">📅 20:16 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6738" target="_blank">📅 09:15 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6737" target="_blank">📅 09:07 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6736" target="_blank">📅 09:06 · 23 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6733" target="_blank">📅 20:19 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6732">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGLhFLCPOImDauGioh1et70A0ThVVqcZY_a_TTcy1Jf43VDK-SorLsGFVk_HflowJMjOBvSzMEBQDeARPRJ1jjODgziHmuPajWCsSGq_0QIxhXXYT2Syr-Y3SCylaaW1PGER1fOfCwq1C8aWii8fXNpGRoCSBu8pvWEHrwpRsWdQQOMsdPTBFk3zofMuBKl6GZRInX6-VBpP4ZYyeCRxVOAid9HhLIuiirCGrEtqPzSByKPuY5BG0R03-LlftKJkdy7Bollad8tYwmzwsQfierblpJmyGEJTMpYrVCXaMGBaoKA5uw7phwMiF1xqne6hd_Vk10jSY-kQol_9Aby1qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اون برنامه «نفت در برابر غذا»
بود که علیه عراقِ صدام حسین اعمال شده بود و تحقیری بود برای صدام،
عملا سالهاست چین با جمهوری اسلامی همین رفتار رو داره حالا بقیه هم به همین رویه پیوستن.</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6732" target="_blank">📅 15:23 · 22 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6731" target="_blank">📅 10:44 · 21 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6730" target="_blank">📅 10:24 · 21 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6729">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VrizzU9zmbICrqet4MvVKfIpUHVUt7IIXPpUEAvNEue2zSPqFDKGVbphH2plJS9byQtPHBtdrHP5u7AIlbrHvO2LorWrabXdorpfrDx5AvUzXI7dHH8JDKrkxFil3R1YIzKFfobiCarj7RsO4vqw3A8qvzyoQd-3rJm2bsXjkJLvnHe0AvpYnTJYBGjioZpfrZOJkcTyAZPbluGnLizhGK8RaNNd4BX6JiAKWHaBM53ok5NbT_GZKgXLK_mJJkDPwuuzL68H0-a46jlFK0YrxP5UNtAHdZZiqxyMIKD63nlli8Vdrz105kWtnyITiOCL13dfKxprBlWLcL4jcufhhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولایتی - مشاور خامنه‌ای که در یک کاخ مصادره‌ای زندگی میکنه به مردم ایران میگفت :  «مقاومت رو از یمنی‌ها یاد بگیرید، لنگ می‌پوشند و نان خشک میخورند و مقاومت میکنن»  و البته نگفته بود همه‌شون قات میزنن و کلا توی هپروت به سر می‌برن.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6729" target="_blank">📅 12:09 · 20 Shahrivar 1405</a></div>
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
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6728" target="_blank">📅 11:20 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=K6v9mA5rC-WOdpjVFQ9e_k2VgjZiQnVE-EaKu5M67Gzr6ME66IUEn9ERP4XBtgE40wmsiZXxhy4CyvHPKhuyWmdnL33AkyKsN6wH__hHCGW1UPNVLQ2NCRCAXYz0mrVawgw7k1noSGis_YOAS1ER8cCevGR68MXNqHI03jMQ7XzVskVbrXTmK_0xdmYAiqV5M7GI951xiCUCcFLxmJGawgTKOxQe6FpgBaZoUcNnK1BiaCZitRCYNWcC_AWNthuzNtgsIjdB_vzb40UdTIfD_LnLg42sUJEQuqTCWD4f_dQhNuKpBeVCLmaDaFGE5s0B2IZp5Iu5kCGGXa7XhlbV-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8dc5dd7f89.mp4?token=K6v9mA5rC-WOdpjVFQ9e_k2VgjZiQnVE-EaKu5M67Gzr6ME66IUEn9ERP4XBtgE40wmsiZXxhy4CyvHPKhuyWmdnL33AkyKsN6wH__hHCGW1UPNVLQ2NCRCAXYz0mrVawgw7k1noSGis_YOAS1ER8cCevGR68MXNqHI03jMQ7XzVskVbrXTmK_0xdmYAiqV5M7GI951xiCUCcFLxmJGawgTKOxQe6FpgBaZoUcNnK1BiaCZitRCYNWcC_AWNthuzNtgsIjdB_vzb40UdTIfD_LnLg42sUJEQuqTCWD4f_dQhNuKpBeVCLmaDaFGE5s0B2IZp5Iu5kCGGXa7XhlbV-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شدت انفجارها رو ببینید
بخشی اش موشک‌ها و سلاح‌هایی است
که درون تونل‌های این تپه بودند.
این دژی که تصور می‌کردند شکست ناپذیره از درون نابود شد.
پول‌ها و سرمایه‌های ملت ایرانه
که دود میشن و به هوا میرن</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6726" target="_blank">📅 09:48 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6725">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AzUM3GQoS5AZDXCsTXuTY6uP3W9eKLCNsPBHGBV51Bm4g6FJFa0tTyzfcPdgLKZ33POW5qwSAYsedEoOCkGEuZ2LuA9l2AMFBWaJsw63qYaIqjD7URnjEqZAyOMHoHTQ8jQepFw4NEb8jhpP9OGRsYYrklbHeb5Y7KjMCazjQIyy6bBDI-zudaIB9tomByHEU1BDeWZwmafeg4SA4JS9G9oOHsgFuPHRH_46N1XC_JFK9nlmuveCu-_A3H5i4SPT86v1RFQsfvWmwiJ4uNkoB6TlLUt7jopdeWFzq35be2x3qvZAo5CgEE5CQsaaUHkeubMyZfAWTH4kQvMZhj1KfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0ebd8f25.mp4?token=AzUM3GQoS5AZDXCsTXuTY6uP3W9eKLCNsPBHGBV51Bm4g6FJFa0tTyzfcPdgLKZ33POW5qwSAYsedEoOCkGEuZ2LuA9l2AMFBWaJsw63qYaIqjD7URnjEqZAyOMHoHTQ8jQepFw4NEb8jhpP9OGRsYYrklbHeb5Y7KjMCazjQIyy6bBDI-zudaIB9tomByHEU1BDeWZwmafeg4SA4JS9G9oOHsgFuPHRH_46N1XC_JFK9nlmuveCu-_A3H5i4SPT86v1RFQsfvWmwiJ4uNkoB6TlLUt7jopdeWFzq35be2x3qvZAo5CgEE5CQsaaUHkeubMyZfAWTH4kQvMZhj1KfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=kCXLTebeetl_zkVugtWqUbeCBkSx4ZzC36RLc59fYT8i7AweqUoFxAlkVBEQV8Teo5OotHkXJtQwcr8b3x7flHkTiibpNVedcpPOhvWm1nMQurOCB_gjcupQ0iX7nOCedwcJ59u-yx2fb5dCwLbgY0gtsdKX_xn-7XoltmUf_QBq_2iugyjYxwHEQKk4vITnMhAX36k7txGNRWdSw3XwtdrJKBLQvzwDHdrhGW_qT-3lABqBzdnEVVO1t9yWRTnm9ebkREq9El2hCUDTOmI2BDPwy0XCLOs__vqzcjRD7a0YuW65meEL4g5QdAGQaaDRc9CHtzBafM1PCdjlGUc-Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7939ba4ba.mp4?token=kCXLTebeetl_zkVugtWqUbeCBkSx4ZzC36RLc59fYT8i7AweqUoFxAlkVBEQV8Teo5OotHkXJtQwcr8b3x7flHkTiibpNVedcpPOhvWm1nMQurOCB_gjcupQ0iX7nOCedwcJ59u-yx2fb5dCwLbgY0gtsdKX_xn-7XoltmUf_QBq_2iugyjYxwHEQKk4vITnMhAX36k7txGNRWdSw3XwtdrJKBLQvzwDHdrhGW_qT-3lABqBzdnEVVO1t9yWRTnm9ebkREq9El2hCUDTOmI2BDPwy0XCLOs__vqzcjRD7a0YuW65meEL4g5QdAGQaaDRc9CHtzBafM1PCdjlGUc-Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در ویدیویی از نخستین توزیع قند و شکر کوپنی در دهه ۶۰، عبدالناصر همتی، خبرنگار وقت صداوسیما و در میانه گفتگو با مردم به مصاحبه شونده می‌گوید: «اگر قند و شکر کوپنی کافی نیست، باید کمتر بخوری» مصاحبه شونده هم می‌گوید: «اصلا ترک می‌کنیم، ضرر هم داره ...»
همتی در این کشور خبرنگار ساده بوده و شده وزیر و رییس بانک مرکزی و کاندید ریاست جمهوری‌ ...</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/farahmand_alipour/6724" target="_blank">📅 09:23 · 20 Shahrivar 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gypqkCu9aGZBiTrw78fuJvG4pBlxUTA3hTE367Tx1j053Ggnn-nh-5j1hZxYqZlr-wbeQr7t5rkVpABFucrwpd6Um52Zq5qQTPvXqloljRP2QpwDdnUt2-EJ_YMwDsRTz3HinL-geabEm7RhwGmJ5Zz33IWwSpOK56HO7o4rmO3_DD7JtCqdNSI-2fr64XqvBiaOTmKOB2YQQ3I1RmX8gj12MS1df276ZDy7kSsUBmJJbKzy8rjutcxIg-QLdrRoWCR9mNJhK5GXEHb_yThkJde-71prb0d8jBcwBIKQSU1xfHs00cGTQWZeIydjcx9rdQ6H7YAQpWc197dd7zI7Rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=gypqkCu9aGZBiTrw78fuJvG4pBlxUTA3hTE367Tx1j053Ggnn-nh-5j1hZxYqZlr-wbeQr7t5rkVpABFucrwpd6Um52Zq5qQTPvXqloljRP2QpwDdnUt2-EJ_YMwDsRTz3HinL-geabEm7RhwGmJ5Zz33IWwSpOK56HO7o4rmO3_DD7JtCqdNSI-2fr64XqvBiaOTmKOB2YQQ3I1RmX8gj12MS1df276ZDy7kSsUBmJJbKzy8rjutcxIg-QLdrRoWCR9mNJhK5GXEHb_yThkJde-71prb0d8jBcwBIKQSU1xfHs00cGTQWZeIydjcx9rdQ6H7YAQpWc197dd7zI7Rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=lHOEinXOrTC_LCjnJEnmVUCtMIzme4CHEMvij9CaqcIIE36DKL_Xox0_csuphJNTKiaWlHxtkAUmXfvf1MP4hP4nydJxAOVqomj-syYcgTApn-eoJZt8G16ZiOYGvU9RzVLK9PcM1N_pS9ms5reKw5UzYll2FlWsRmHqtpM9cErVvAVIZaISrLj8aH0xx-pVhUgTq2tMK75tTsRSoYbwV5xhttTUJZTrgfFOtw2FlWctJvjAejUpU_EbQW-zqIc7sf-KucgRBoIBaI98uIQSm0xnQ2qhNrgEXc68pSwbQZjm9L5BRMczp1Ub_xSqVhE2N5QYnydA9KUZTzBjfADlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=lHOEinXOrTC_LCjnJEnmVUCtMIzme4CHEMvij9CaqcIIE36DKL_Xox0_csuphJNTKiaWlHxtkAUmXfvf1MP4hP4nydJxAOVqomj-syYcgTApn-eoJZt8G16ZiOYGvU9RzVLK9PcM1N_pS9ms5reKw5UzYll2FlWsRmHqtpM9cErVvAVIZaISrLj8aH0xx-pVhUgTq2tMK75tTsRSoYbwV5xhttTUJZTrgfFOtw2FlWctJvjAejUpU_EbQW-zqIc7sf-KucgRBoIBaI98uIQSm0xnQ2qhNrgEXc68pSwbQZjm9L5BRMczp1Ub_xSqVhE2N5QYnydA9KUZTzBjfADlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MXZ04j2DT9EJOUhCbBpNd-gDXwHXO8oBAWvm0FKvfBDNL0I0y9EyZLlQEyoEkFhYq54ANxh84l6mLbkwHTtGUk0dKTHsIH2hw1NL-_oQRkphFlnKICdNONBSNBSPtoUoOn8C6wYN3jnp5xA8C_00SZHIN-BoB1u_eoa7TKkdD6bYN20MSkaLjOLCVwiYyyRCnTaKD66_a0gTZ9gFzpmLV7J43y8LwEEnx1PN4Q83HWCETFqD9flmrngErIvXRHN54eRVSApgwz-Rcea-Vh90BjJrVuoypF6i-g-ShWGPO4ODT7k51SkR6386u0QcokOMKdNjepdRIb-gHcDDLDUfsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=MXZ04j2DT9EJOUhCbBpNd-gDXwHXO8oBAWvm0FKvfBDNL0I0y9EyZLlQEyoEkFhYq54ANxh84l6mLbkwHTtGUk0dKTHsIH2hw1NL-_oQRkphFlnKICdNONBSNBSPtoUoOn8C6wYN3jnp5xA8C_00SZHIN-BoB1u_eoa7TKkdD6bYN20MSkaLjOLCVwiYyyRCnTaKD66_a0gTZ9gFzpmLV7J43y8LwEEnx1PN4Q83HWCETFqD9flmrngErIvXRHN54eRVSApgwz-Rcea-Vh90BjJrVuoypF6i-g-ShWGPO4ODT7k51SkR6386u0QcokOMKdNjepdRIb-gHcDDLDUfsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=kiIZ9ZgSKXgr2NbnWWaOZbtueRkU8sLLywFCCoKO3B5KxT_RRqu_W0m7ddGJZKyaUzUkP4vitguMQnmUsRAL41IO3iVrwbqPvQmUjOuZiYUtGuv8oFAlq_WfbraEr-qWpltHolNCLFK0aKHRgeKutt_2ec_dUNBRUrfiI-jwbEeBLosv0XEwJ3ov0PrSLnVq6KgcVLr46DQzrrCs4M2HBxkAcn-5Dkmfu9DPrPvlKq40pu-7IRiXX6G0dj6jUu6y0v8RaU3xrJ7meVPP5QexdUeIU-TaZtkcDGywXQcezKe1Wx3nzRd6srLuimR9-RVBDdXouL_SLpFlH98Q5HDaHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=kiIZ9ZgSKXgr2NbnWWaOZbtueRkU8sLLywFCCoKO3B5KxT_RRqu_W0m7ddGJZKyaUzUkP4vitguMQnmUsRAL41IO3iVrwbqPvQmUjOuZiYUtGuv8oFAlq_WfbraEr-qWpltHolNCLFK0aKHRgeKutt_2ec_dUNBRUrfiI-jwbEeBLosv0XEwJ3ov0PrSLnVq6KgcVLr46DQzrrCs4M2HBxkAcn-5Dkmfu9DPrPvlKq40pu-7IRiXX6G0dj6jUu6y0v8RaU3xrJ7meVPP5QexdUeIU-TaZtkcDGywXQcezKe1Wx3nzRd6srLuimR9-RVBDdXouL_SLpFlH98Q5HDaHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYZS_5XRJJUx37FNu3dScsehSVYKw2A7UKLxfJea9McphAoBD48w96yWF3tQXzGUFJ1mXx1fXPk_Dhon7qdl4jlSHCHQ7uQEPmgEWzxV4Y5BPERD-SXNBXgSPbcjdbyXiaVxKADIqF536qy2vbKx1WdH0848e4gtjcP97eDlHfc1E65nEJtnx-I5fcZfiMgBZo4JATFMZSUEDHYIom31Fq23S02rH7_bdm6Efue_J6bC2N3roh8xDYlkDBFrp1yauctl1nA3A18BiF1kucIU1I-LXSKuhoaS1C1GeUGVg1pnlHT0rb2swubBlTy-jdWsy2IH1h7zPr3Tf7rjJRUMUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=tZcfNhrddU7mmBF-mx2dOaJipdl5gFCh9_1hScxbP6tYx1iu-7AsitbLSRDYmYWnA0lwUdkDKb01KOUPWv2L9EkfF_wH8USDvFIoSefjt8b17rbGjFMtFDaWgGqDXaJJYwy0ALd2Kwlyex9grIqyb_b0-Yime-gXtaePuNRzjX6ZyuFOIvJI_XvRFMSloj6_E7p0iN_FgcHeenoOPaZgsWwmi-RjT-_iQzsHomNReZzKyHNBR_LWyfmqs4USWoACw9pVixDIjMOF9m6LvmywtY--7REaWtUEyg6WwIEOidGh6m1tygVwt-Ab0Eh6ZhawImmUrjQ7036KlzIgB9HzNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=tZcfNhrddU7mmBF-mx2dOaJipdl5gFCh9_1hScxbP6tYx1iu-7AsitbLSRDYmYWnA0lwUdkDKb01KOUPWv2L9EkfF_wH8USDvFIoSefjt8b17rbGjFMtFDaWgGqDXaJJYwy0ALd2Kwlyex9grIqyb_b0-Yime-gXtaePuNRzjX6ZyuFOIvJI_XvRFMSloj6_E7p0iN_FgcHeenoOPaZgsWwmi-RjT-_iQzsHomNReZzKyHNBR_LWyfmqs4USWoACw9pVixDIjMOF9m6LvmywtY--7REaWtUEyg6WwIEOidGh6m1tygVwt-Ab0Eh6ZhawImmUrjQ7036KlzIgB9HzNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RwwaeLIa9r9P0vNVUci-ZU4dCRvD8MiM3uqN9XJi2s1sC5bGsHTK-BHpFs-rle44B1G7M4AzL7Us31f1VOdeVHm2RfFPW1nCS5L_maG6acdu2v4955oIo_pCuxVNurtvgIAqV2-1ZBkummGg4zRi8NUd7Ny9KmppMbh1GlYsp_ioaYSbknqx6D9hcZlYYbyT3bLC9lTEftRLXvasLPk8F2ta6nxOxNCtyNIBBLCkUwZgSAdDjqHGeZ92jjtOvJzWr6Hh2eFGLW9aYLv9BO9ZuB-GtOZrQKom0xXjVteJkfdE7dfVF89m1KNOtskVbpr4EWhI-cX4fFStUlvORg8LCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=RwwaeLIa9r9P0vNVUci-ZU4dCRvD8MiM3uqN9XJi2s1sC5bGsHTK-BHpFs-rle44B1G7M4AzL7Us31f1VOdeVHm2RfFPW1nCS5L_maG6acdu2v4955oIo_pCuxVNurtvgIAqV2-1ZBkummGg4zRi8NUd7Ny9KmppMbh1GlYsp_ioaYSbknqx6D9hcZlYYbyT3bLC9lTEftRLXvasLPk8F2ta6nxOxNCtyNIBBLCkUwZgSAdDjqHGeZ92jjtOvJzWr6Hh2eFGLW9aYLv9BO9ZuB-GtOZrQKom0xXjVteJkfdE7dfVF89m1KNOtskVbpr4EWhI-cX4fFStUlvORg8LCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=CaQYrqalrTc5VprOmiFb4j6DpWBmdPXjPda217LPgJ6sXAXakL00odCCO4SVB2DURRFLlHwFexV7WRJ6YJSiy6R2YKNr6STTKVDmzQ5nomPdYPm8bMEXR13YugNT2LXOtMUh5Yns2ljmHS0JawJMYPolEplPTb89kK5Eb1gMMTbcAGw9nlDyP82rG2ziwnzHsggw63xM9GAUTrpHaIiS_uOBnWUeOid02ZMkoC0Yq8wLME2veEVjGmbmeZu3ezsafzA9A2UtlnM5JztxDwhEpqJ24B611-wPaYd3iUMzHh_M2zc3K9c49ngbc_VmisWoWDuAhI8j5xDtJ7ckB8V3mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=CaQYrqalrTc5VprOmiFb4j6DpWBmdPXjPda217LPgJ6sXAXakL00odCCO4SVB2DURRFLlHwFexV7WRJ6YJSiy6R2YKNr6STTKVDmzQ5nomPdYPm8bMEXR13YugNT2LXOtMUh5Yns2ljmHS0JawJMYPolEplPTb89kK5Eb1gMMTbcAGw9nlDyP82rG2ziwnzHsggw63xM9GAUTrpHaIiS_uOBnWUeOid02ZMkoC0Yq8wLME2veEVjGmbmeZu3ezsafzA9A2UtlnM5JztxDwhEpqJ24B611-wPaYd3iUMzHh_M2zc3K9c49ngbc_VmisWoWDuAhI8j5xDtJ7ckB8V3mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L8pmQe6EanQ-u5uXsSUOlnwr_CJ_FDOM2tHxdFE6WNbDd8t63Gy1WcKvtmIMoV9TJGGLbli4oHih_4aXDxYi2noZPhYiFI2IyBYnKvu817dtb1Aqhp2mNPo_Pazrsom20baSZOkPjx8aaFE0aEXvsqCZYKUvk4b2DAccFkxLXTTIy2xrsdu1J2wvB2l8Ix_uZneYtViEHh31ae1iGKG6uakNT7_TXQ2AcnUdd343Zw8a_ysLU8QHNm_-G4rx7i6dsmij48Rtu1oXOBCISCPF3pnoEsdE-pC_vGrqLNAc_EMpgvGxtLXCQ5MubNM8eI6IvwrJNeHWKaB_WBkyFw7Y3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=L8pmQe6EanQ-u5uXsSUOlnwr_CJ_FDOM2tHxdFE6WNbDd8t63Gy1WcKvtmIMoV9TJGGLbli4oHih_4aXDxYi2noZPhYiFI2IyBYnKvu817dtb1Aqhp2mNPo_Pazrsom20baSZOkPjx8aaFE0aEXvsqCZYKUvk4b2DAccFkxLXTTIy2xrsdu1J2wvB2l8Ix_uZneYtViEHh31ae1iGKG6uakNT7_TXQ2AcnUdd343Zw8a_ysLU8QHNm_-G4rx7i6dsmij48Rtu1oXOBCISCPF3pnoEsdE-pC_vGrqLNAc_EMpgvGxtLXCQ5MubNM8eI6IvwrJNeHWKaB_WBkyFw7Y3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EhKXRsyQIjGS2BsGGhcF0NK3gIgtgGjlSWJH9LGuGVhx3LZkvqxLv6OhndZwnwJx_IgNw-J_yef_7gNf4_YajZSyWiLn8IC6Rr8VYWjLjxP9CFuf3UnqBudsVz0sJLpakMpCsNHVtucKBOQd32Vfi_YGVKrpkP6n7V6Y_heDhG_vJL6VkMwxhxhd6ZvVNFx3PSFF50Ukar0dFl-WuQ77xkVYiD_cs0INx2cajmrzdWR_-uWarxKY3VKNHUTM7L2I5ke_ru89pcrJb7irLPYXcPgkb3aZmUzS2CCi69XQhnB0kXCmbJUq0ssyKgm0yo2rYsDxFEp2K1_BGk7syeSWcQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NfiKitRhPYswlB9CDBUreao_GEU_6BUVBaBrSyyZrenfjWjdk_a8eLRK5wx6B6dcxvxNgf3uZDLJkuYq6_Ra9WUKVAkRDxP5UTl8FKj9TugM2hdMSdQLlkSm30bwb6ZpL7bDSAKaL7MU46ssQMtZjtyXFqHIbeLhbuIe7Q0LDE-q_Gnf47tLcJrZoWBShG7pflDqjbidGSlPDRX_DRMgg4iO5h4TUzV3Ev5s62ZbStOyM86G6P3EA8mhtj8GCbgSwMsNqs4Oy-stF6FaV7iF1qTjLC-CwcI0VDkjUJ7UApFaL1jTfQpdfloB0_JRHbPBuGUC322u42Um_ZgTtI4eKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=NfiKitRhPYswlB9CDBUreao_GEU_6BUVBaBrSyyZrenfjWjdk_a8eLRK5wx6B6dcxvxNgf3uZDLJkuYq6_Ra9WUKVAkRDxP5UTl8FKj9TugM2hdMSdQLlkSm30bwb6ZpL7bDSAKaL7MU46ssQMtZjtyXFqHIbeLhbuIe7Q0LDE-q_Gnf47tLcJrZoWBShG7pflDqjbidGSlPDRX_DRMgg4iO5h4TUzV3Ev5s62ZbStOyM86G6P3EA8mhtj8GCbgSwMsNqs4Oy-stF6FaV7iF1qTjLC-CwcI0VDkjUJ7UApFaL1jTfQpdfloB0_JRHbPBuGUC322u42Um_ZgTtI4eKjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=V5o2oU6fSeDTmcnLpNA3CvERnDDPMcUX6LvS4jqFbvx7UYsTUbWrK6L0G9yI4JGZ7Hbm08vA_sqf0cHYPU3hddejISZen7u_qfwXRl7TwfUcwlFBW0gc5Qcx4COdlorA70KCyiWFBp7LEkiYao5quvGaIN16NM_rvyH592xCAYTn4YOXL_azlcKptoYqeEFXw5Du-6ewqgk25kgVgDKsmMg4RXkUhBohtQNz-hIAOxIn_4RSDOpznqjDEcEwdd8MnzJMd-ht3n2GPbHchRkeX0-2j3eAg_S6WRtBC29fQNxkNTpvxtIhSwyYXEKmnF6oL_MZgT8pmkySDAfyM7Ry2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=V5o2oU6fSeDTmcnLpNA3CvERnDDPMcUX6LvS4jqFbvx7UYsTUbWrK6L0G9yI4JGZ7Hbm08vA_sqf0cHYPU3hddejISZen7u_qfwXRl7TwfUcwlFBW0gc5Qcx4COdlorA70KCyiWFBp7LEkiYao5quvGaIN16NM_rvyH592xCAYTn4YOXL_azlcKptoYqeEFXw5Du-6ewqgk25kgVgDKsmMg4RXkUhBohtQNz-hIAOxIn_4RSDOpznqjDEcEwdd8MnzJMd-ht3n2GPbHchRkeX0-2j3eAg_S6WRtBC29fQNxkNTpvxtIhSwyYXEKmnF6oL_MZgT8pmkySDAfyM7Ry2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MbUzKvZ-L-2M-_kiHTHAN_8rlBKseN1fD7M0t8IKId8sm5Ykwrnm3Cd4REwmkMlIvkAAjehaxnbgOrwKgyY5yigBJKBlArDDxTUsYitOC0aR6CoRm-o4LbQgmpF994wHpOy5BxZ3dWpWtQJgWEVka1QaBQpHmQFivdPFNTfiMs77wOBwFQrIklW4rd7ZBwahIbrUFVc7u3WJb3P0sv2Qn0D3DGvAqtqmDarqZeKZ_Ml9MwjNDCFxPAtCM4ROz62qY2HOhnAVm27ldji0MLLrulOmfP293eNZalQSdeDwt630KB--MONADD9gOGmHCysWHLMf9kHsyDB8_FrpMYpQBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o0OSnpY7i4I9pLYBfgLuW03N4ItUqiuDPLCpWs-kWA_gN7H-Rh_r_nZdxF7tVdduUexukicWfRfCaGAsHH0X0-AIBxCGcYe2BTZtddBj7D17EYPHOr90kDZx0ocrZsgFDka32pl4bDVEVism-bFxxaA-0Ah4PoDliqrmvsOuHu5dDAmelkT9iyPzSvu0MFV4bYQ90AlRxN-3isM0nYxS3qIOCzijMqomtMZ6c6YBYweW8i-ggZ1j8fG0Xu4NXtLu5qQ-RReCtRKqZc2H1AGbT7fjp_7cyXJ_MaZc9Dtli_8d70XXtF2A0JtbvCOv-SE-zxflWDP-M8DiBfzbuugEyQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dopUu8CYiE47WQuQCIFTivaVicU3a5_7mzrvzG37ycw01eHDl2piGvblZaGAXQW3d4N-6FCVk0KqpfvpfuPEBDhLSb8mMnI9WnhQ0hE2Bu6zb_Nmzj83QPRNjTiy4Wsk1kD9HW5XRqKhjOufczvDEmAhSCgv2qeQMfB_cy3_WCHwK7DrC70K4Si021AmwM4CQpLclNP4dlgXLRYS3tq1f_dxw9BXWXrGybCiwZpPl-Gy6h5Ij2kWECPP5nJlqamVhIHv5zLSXL4ry_xz2y6sJ7m6UZnKZ3ASW2m59OO9hGFKfmppVCb3yxwCy4iDXCNPqZxieDtyqVs66ahNVPfYBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=dopUu8CYiE47WQuQCIFTivaVicU3a5_7mzrvzG37ycw01eHDl2piGvblZaGAXQW3d4N-6FCVk0KqpfvpfuPEBDhLSb8mMnI9WnhQ0hE2Bu6zb_Nmzj83QPRNjTiy4Wsk1kD9HW5XRqKhjOufczvDEmAhSCgv2qeQMfB_cy3_WCHwK7DrC70K4Si021AmwM4CQpLclNP4dlgXLRYS3tq1f_dxw9BXWXrGybCiwZpPl-Gy6h5Ij2kWECPP5nJlqamVhIHv5zLSXL4ry_xz2y6sJ7m6UZnKZ3ASW2m59OO9hGFKfmppVCb3yxwCy4iDXCNPqZxieDtyqVs66ahNVPfYBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jwBbhNxzBqmpOwhlilpzgsRsbawqV0GRIYegvTtY_vfOwWxkEXvY5d9wv5Mn8LUDL1sPyF3SDIWAN2vgNxonSDW_PRkPCJABi6BP6J2lVNNXVCD1GLrOQ6pWPs9-zYi-c80pUJ9b65DUHmM_FxkX4d6HCj-kK8j20h-MMMqa2uhD9Aj1iuVY5opDr_iHRYJr4vMXb_B3OBC3JiBdr9qJsbz10QlV06CEmMDYDFm6x0gWIfq90F0xwNtU6PWzPbk7ktJH8uPEdIPgjvh23rwdcia_JaNSVapYXnFR7w_NmeTweuOyT5nxwZlYpJ2iOzdK6GTOsr-MoOwSYsv5jKTlOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2nWwqZDSIR0Jn-S3y38t2AF-EVPt5R0ywDb0iiJaTZIDue5U34lsma3XgtDEGTQ8DvjceAfX4IQGlOFiYIx90hIPT0f-wRFQF2ESiBRihc-Nrg-N_nVm3k02qx7rNo1Ekk6tbjs35efgBEvXWcj_dHD-SSr5vgbVhQjY4C8U4fM4AtzQxH09B2l746kYEnrHh4AlykKQlQGYVfe8UctqAUaNtATuueBdnM33k-MlX5qY1e2WNyH53jt5QbnqgZsnl5C_TAQf28Cr4NDSjV001uDtXAtDlH8BJyexwwyQ1vdZFpj3tWOtNLMhoWCfzlFRnSTMVzsEqaL9EgfNHgRAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EYvLgxFJJAF8ynxCjtRjpYcKT5BkqeuXoTki2ree91sEZW8k1TbWXC-r6GzGXIl32U4mmlyzDLEGf1NLJI90HbSRHdvTn8jJsDXcsGYQmQGZzQxTtxUblzZPxvF24_dcDJmhRe5ngWKHrnv-DzCtdspwr8OKptdnRYbzY36JhrqKF1s6da2ses3NrqbEsw7sLQmxB12FlBHiGKL8p_zl0-pjcwyV56L_bOqQCSHIE0ragIjL90yNy5zixx4mH0ec34i-8TOsTZMtch-n6tlBND7eac6Dj20O99W34gX8zl-1iR-fmwkWA_xFPdqI73OqWS9DBGCTz1Zc37SnM9X9mA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=RYJ6IsJMHjDNsKE6yeZ1iUklm1s4VpGJRa9AyvsEU7kwXrx2TybIjyvHNWGoAOjVu1d-F9bbAT0LBBdNeebfRODlcy77_Z9hPdQPUzJDCR9JGR6EFr1q-F2buDepA2lbq3nKkOPVy3swMH1VE_7FwolIoI8ANesMbH22U5qBwcBy5HzTmffdqMbI8AfQc9qT2HTtmLjWIQFAkuErRS8otcjODI1-8OuCbCvTE0SlQOKU_hMCt_5KSakz_yHa1s5UXK8ZtRab9DYgliRniHZcm5fTwmjBb81aG-n7JQliZQtjNFW9mQ3QaHo8A_Y6mGSkCU26YNKEOCIG4Zxlk1VFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=RYJ6IsJMHjDNsKE6yeZ1iUklm1s4VpGJRa9AyvsEU7kwXrx2TybIjyvHNWGoAOjVu1d-F9bbAT0LBBdNeebfRODlcy77_Z9hPdQPUzJDCR9JGR6EFr1q-F2buDepA2lbq3nKkOPVy3swMH1VE_7FwolIoI8ANesMbH22U5qBwcBy5HzTmffdqMbI8AfQc9qT2HTtmLjWIQFAkuErRS8otcjODI1-8OuCbCvTE0SlQOKU_hMCt_5KSakz_yHa1s5UXK8ZtRab9DYgliRniHZcm5fTwmjBb81aG-n7JQliZQtjNFW9mQ3QaHo8A_Y6mGSkCU26YNKEOCIG4Zxlk1VFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pruT-bOvRuSCWTRUAsp8YNqzqZjtuhwAJw2Fptxtqt_Gf_Iyjdax2BSN5Px7ILFTH2QGf-A0UTpsOnw5wAmaz0Ys0saGfAvFxy-2Kx_hxFo9uJbBQVzfCrUjGIKVibzVkg7AKAfKVTgjZGvMUKSKCMaO0ZkDs1gDjxitlsGWlqsWJ0Dghi2jAZnqr27jD5M_vhYq-9phX9riUQ_Y1RYWhUgl2vS0PDabEjUdKEcj2ML2DTvc3CQmPdLYrGi3SQqKy-hAs0w6q3Jr3xJVDMFxnrs-bD1lrgsZE_yr0DKrtIB8PAdL4VinX9uvreH1VdyirCc5wbHS3Q2p-U3zs-zCdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=pruT-bOvRuSCWTRUAsp8YNqzqZjtuhwAJw2Fptxtqt_Gf_Iyjdax2BSN5Px7ILFTH2QGf-A0UTpsOnw5wAmaz0Ys0saGfAvFxy-2Kx_hxFo9uJbBQVzfCrUjGIKVibzVkg7AKAfKVTgjZGvMUKSKCMaO0ZkDs1gDjxitlsGWlqsWJ0Dghi2jAZnqr27jD5M_vhYq-9phX9riUQ_Y1RYWhUgl2vS0PDabEjUdKEcj2ML2DTvc3CQmPdLYrGi3SQqKy-hAs0w6q3Jr3xJVDMFxnrs-bD1lrgsZE_yr0DKrtIB8PAdL4VinX9uvreH1VdyirCc5wbHS3Q2p-U3zs-zCdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cjsUXYQN4JqLCwLtpPLKLGHzOnXAqi7NIizwiFe1vmOxEE6eoNIZ8FiIAqzOkeeM8nIr3ESrz6Niye0fsphSpoLL7_ZOhGj12RXNJbVuTzCBdiYNOAHRIjdOgvTIl-ngSKwnqGggSMvQpnkpkpK0j3mcY9QzInbvx6BUWlnOGBW0NP81LTXTPEXF9kzT1KXVcQ1FrSfZYPFe9Yqgk1wzHE4Lydlm5pK2hzBPFzH6BtFw9krvmqGYKI9wNsf6GyM3r1CCSImTwkVx6N-LTJfnSHNuz5Uney0SVgLsrkY1tpEDX4eMUADtmFWsnVK8JjN009bfaD805vhKRlbcLkWirw-V5QpS6SDc2KbIXg5515LBcXSOVlD6ONEcDmagqD3GK7eL0i2qvIDCSPhegy4DTb24EwyDCHP8xtoPCKNtLsaOCMS7YUwFQuVJktawJ9SGjpp8YDZhavuePo5HlzU-CQmEIERLytBpwaxlVVUq0G5XCCFxkmUvBxSyOKsOyqO0zQwtBuP7oDE4X7rzvE_iYjnDOSXpdsfqbTW1rU84OoDAjfXMzuYq9OssEvSbzsFVK7FrjzNhYjvtdWE5xBMU4QQJGAf8WxY9xew-8ahsa3wqZu2TKXYcFUNUF_CsoY26_vDYJFh6MUpYL8T_h42lkh6CkZXi6JN94zyhrYN6jak" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=cjsUXYQN4JqLCwLtpPLKLGHzOnXAqi7NIizwiFe1vmOxEE6eoNIZ8FiIAqzOkeeM8nIr3ESrz6Niye0fsphSpoLL7_ZOhGj12RXNJbVuTzCBdiYNOAHRIjdOgvTIl-ngSKwnqGggSMvQpnkpkpK0j3mcY9QzInbvx6BUWlnOGBW0NP81LTXTPEXF9kzT1KXVcQ1FrSfZYPFe9Yqgk1wzHE4Lydlm5pK2hzBPFzH6BtFw9krvmqGYKI9wNsf6GyM3r1CCSImTwkVx6N-LTJfnSHNuz5Uney0SVgLsrkY1tpEDX4eMUADtmFWsnVK8JjN009bfaD805vhKRlbcLkWirw-V5QpS6SDc2KbIXg5515LBcXSOVlD6ONEcDmagqD3GK7eL0i2qvIDCSPhegy4DTb24EwyDCHP8xtoPCKNtLsaOCMS7YUwFQuVJktawJ9SGjpp8YDZhavuePo5HlzU-CQmEIERLytBpwaxlVVUq0G5XCCFxkmUvBxSyOKsOyqO0zQwtBuP7oDE4X7rzvE_iYjnDOSXpdsfqbTW1rU84OoDAjfXMzuYq9OssEvSbzsFVK7FrjzNhYjvtdWE5xBMU4QQJGAf8WxY9xew-8ahsa3wqZu2TKXYcFUNUF_CsoY26_vDYJFh6MUpYL8T_h42lkh6CkZXi6JN94zyhrYN6jak" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=A_zfYbX0RbKXtS68L9wubereVlkMCUMxEHvJhqBlY_RGEJvQKiDiA7hxvfjY6UM9sg8XpT_n1ycXdBFZMxJy7BdTOq5su-WVYSNnHFEzPjc1YFL1K9FaCrjeSwNxgUG5lTm82Y5bxCOsR-qpjx4j6ywRAZSoZeeazYUQmq7j_JodlS8eDEmz8utiEpnxBLCbl6GSUwE77RS1xtZKxAYSLZJQyUiDjc32QQazEYwpxU-sZShrNzpbzLZ301LENu3Irm5ukI7NUs0JVyTWFxancXYk_k1xZMrBX_eZq0eYXZiz5fbh_q_3fCYcuXJY0qLpP0kynoWiuO8o6DVvOj-pWw86zwr6JMc4WNsL55mSliQMkUya400sDfY8iVu8NraxPoYvMkMOT5aOeOHR3x0R11CLxHQjmN37oHyw99LSf98NlwO1Ag6lu9fg7ajN5FK69wyJK0TzDH4pG5vXI5oKJv9xCw6PDi7zijRtweXqDKX3fldsn1L2P5x3L3XjyMgUrsZUorQhbrudGPLaSCDJIODp4HNzTIGmK4hSGvAOrnqPC54kgsNwSbHdE7VjkwPNTjh1UF_5iSmU2lRyADEvdZeK9it8AsG55gXhw9MppMmmmsbjgQI7a8ncbaOniR1-MqSGxFtQ38hxG1yAtLjp56Fj3i1h89T0_QA6STI43rQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=A_zfYbX0RbKXtS68L9wubereVlkMCUMxEHvJhqBlY_RGEJvQKiDiA7hxvfjY6UM9sg8XpT_n1ycXdBFZMxJy7BdTOq5su-WVYSNnHFEzPjc1YFL1K9FaCrjeSwNxgUG5lTm82Y5bxCOsR-qpjx4j6ywRAZSoZeeazYUQmq7j_JodlS8eDEmz8utiEpnxBLCbl6GSUwE77RS1xtZKxAYSLZJQyUiDjc32QQazEYwpxU-sZShrNzpbzLZ301LENu3Irm5ukI7NUs0JVyTWFxancXYk_k1xZMrBX_eZq0eYXZiz5fbh_q_3fCYcuXJY0qLpP0kynoWiuO8o6DVvOj-pWw86zwr6JMc4WNsL55mSliQMkUya400sDfY8iVu8NraxPoYvMkMOT5aOeOHR3x0R11CLxHQjmN37oHyw99LSf98NlwO1Ag6lu9fg7ajN5FK69wyJK0TzDH4pG5vXI5oKJv9xCw6PDi7zijRtweXqDKX3fldsn1L2P5x3L3XjyMgUrsZUorQhbrudGPLaSCDJIODp4HNzTIGmK4hSGvAOrnqPC54kgsNwSbHdE7VjkwPNTjh1UF_5iSmU2lRyADEvdZeK9it8AsG55gXhw9MppMmmmsbjgQI7a8ncbaOniR1-MqSGxFtQ38hxG1yAtLjp56Fj3i1h89T0_QA6STI43rQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=atQK27jMsvGzDdrWPP4Dc-j5NLh948h1B_zhQGUXdoI88JLFMXeIK6jfQgGS9n9rs4hcideNG31kMw4zqh8Tjq9wK_Dx4jZ19t3G3moOVvCFu_zkF3is559L14C03pmMBYKJh3r9SK02A7fZ0NcLaDDyKvu4pnKWL-LnB75O9mMRR86Sid9rjgMnSmE2F2p-r-DbnCFouQUqdmJz3QVxkHHXXUX5SplEYKNOsd8dvAVaAIwbfFrPX0PDs7Vwt299WDK7GdU4bfiiJzMfX4sojVDlJ_Kvr2EPSWv8_R4OE27Q8U-wTtkAYKMK6iKPYEBwqyIbp8ChdzfaZAJtEL1uQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=atQK27jMsvGzDdrWPP4Dc-j5NLh948h1B_zhQGUXdoI88JLFMXeIK6jfQgGS9n9rs4hcideNG31kMw4zqh8Tjq9wK_Dx4jZ19t3G3moOVvCFu_zkF3is559L14C03pmMBYKJh3r9SK02A7fZ0NcLaDDyKvu4pnKWL-LnB75O9mMRR86Sid9rjgMnSmE2F2p-r-DbnCFouQUqdmJz3QVxkHHXXUX5SplEYKNOsd8dvAVaAIwbfFrPX0PDs7Vwt299WDK7GdU4bfiiJzMfX4sojVDlJ_Kvr2EPSWv8_R4OE27Q8U-wTtkAYKMK6iKPYEBwqyIbp8ChdzfaZAJtEL1uQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FDvqnqLyddcfCMOWPFaOuktqfSNYAqABmtxX71lXOkCnfM73A_ru6i1wDFaxMA1ouAVTCMfNpbLaNmlZ7HuGnXuT0uA4_B8lMqyb192xYcJQ_sKSJnjA5WLvaiotC5i1U_Y-5WfamZHaooxlLrtZGUVs5DdO-OBCFZxAUA0LAE-m55VHwOhJcyR9eeQ7RYE63UxVtWchVofwurjx7BhxYqH3y4a24H6yur3bZg6jCiQ3itFgHL22yYPW8XCz2sJpP7TGgGDDSnCVvnEXaQAzhNg-Zus4n1mlBZaaWtFaJ2mTP2078y-o2ujGEv6hsE4-DvqTH2xlWgL0B0aS-BF4Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=S1rI5wIj57WpjbMxaXJX8dQSEJpWDI824kaPxz_ow4DM7BAxAHLrLCWBTufDiy0u08fqZWQJv-rOTjQA_V5IE813aC-RdeBuJBkd77DUFeJrbo0sE_dTuKxl1LB1FV0xIe0lCE5IoA8hYnkE-TqkCxLXMdm_4t3urXQSNIaHGeOwDO1mUlD-WN4vdt4FdcQRISj-RQPhBalIfLi1bxhafp2ETnDiqyDdelLo5HVNw1394lqY_DFtUWy-nRI88I2pHJAgD8kyhaXhjg8cz5gvCSPrZuA8nnU98-WdUtd4GgdFtjJ71_gSG7ZG3SXKp-tRni8iOXI064Vo7ZJ5W4PQiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=S1rI5wIj57WpjbMxaXJX8dQSEJpWDI824kaPxz_ow4DM7BAxAHLrLCWBTufDiy0u08fqZWQJv-rOTjQA_V5IE813aC-RdeBuJBkd77DUFeJrbo0sE_dTuKxl1LB1FV0xIe0lCE5IoA8hYnkE-TqkCxLXMdm_4t3urXQSNIaHGeOwDO1mUlD-WN4vdt4FdcQRISj-RQPhBalIfLi1bxhafp2ETnDiqyDdelLo5HVNw1394lqY_DFtUWy-nRI88I2pHJAgD8kyhaXhjg8cz5gvCSPrZuA8nnU98-WdUtd4GgdFtjJ71_gSG7ZG3SXKp-tRni8iOXI064Vo7ZJ5W4PQiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=OFc_gFRj1zrIFTnqWOTpj_Klw5C8wMBIV2ZXH6Qtk1LNu6C9CmaYndzo2IICxnKia6KTrtMdDPFPwbobZ-tdkfeq0XrsqxGwQb8iIzbRhTLxpxGo2Ysv9CNvwkWGkFAvT4W-gjpSfk4AbiDHBHqtkHTvZn9M8_4mCkuXaAk0B3lmLLMB7a6A1Ox4pDh8YgEuXogB8_2GZoml82rKNJduD5I9anH7KI_OZEJ_JeL2noFen99ipJse3FFTLBLVqtjv81R-8RyKR2VUjYvV04XY2MXcQChyguS9hQdxBlOcoyiL0Ki3sf702ZG7fS26Gc7bDho8HUt1zK7GkYzpKCXGoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=OFc_gFRj1zrIFTnqWOTpj_Klw5C8wMBIV2ZXH6Qtk1LNu6C9CmaYndzo2IICxnKia6KTrtMdDPFPwbobZ-tdkfeq0XrsqxGwQb8iIzbRhTLxpxGo2Ysv9CNvwkWGkFAvT4W-gjpSfk4AbiDHBHqtkHTvZn9M8_4mCkuXaAk0B3lmLLMB7a6A1Ox4pDh8YgEuXogB8_2GZoml82rKNJduD5I9anH7KI_OZEJ_JeL2noFen99ipJse3FFTLBLVqtjv81R-8RyKR2VUjYvV04XY2MXcQChyguS9hQdxBlOcoyiL0Ki3sf702ZG7fS26Gc7bDho8HUt1zK7GkYzpKCXGoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdbUADzwFIeaEDaaltk3LvaFjBytQqrGparNPJB2KBxBjTlcqRY0w3UH8zfftMAT-zfFNLLaKdd3ONj6iOYRsM6yLKxqhjIthqqN76Bq6RTIPNIBUpypgTm4qRNt_EAol3lF1Lj7EyI599hhmdlPulz70SPitIeeHUW0uzLk7WCHzSjfrYfveD7386gVDZRejDyMS0MQPW1CH_hsDv2pn47VwlJvWD7MxyshM8dSX6zWP79c8yO-FV64KaVQX-86SaGnOXPeYhCG72z4M_w5yrSexgYmF9uy0KeCvvmJOPMoHScOu3sjpSenoaHsD1HNakytm5wH2V2Q0vipIHLbuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nbPeCxph8GEv8Px6EBYiw4frhHqUL9f1oOoi_86uJqG_Qj_LWx0covJSHja2g-HtT7bW2cTovdR_booZh8Zw2sQkbupTyqApeNPEcU5_0N0eyiGK75HO13qudMbqHnBi6oOKCTeTMItfpfthKsLYNe-lxk_bBh_dPEUtKHqXyv_FDIF7DhIAVf9wz7yAQkrMPD4UL64W2bG7NbSmPYI8Y4LlSfQBpsiKVhmjigbMvvfJCETCihVT-csKWBWPqVjMyrSdBvgJtyP-VZJmwgbden6j69lZJGMmZZVjLdsupRAxo2SxAM17_w5jUeU7U8DKmhNuYwdzDpR4Ad0cxbzJcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CD3ON6s2jaSHOsaUcuR7uSVpriopCX6vW3YDJ7RaU3k6VE5bp9rpUuN2RHeJ3ebjNwyk8KbILbdioRDRwTWqGTWwviXs0n43TI-T-Tnpbhvzbd65EkRK8I6wuyFdJPlfCGJydFLbR16x52JMgyk0uVDvXHO0eywA7OkFfUvvUuyDGCNiH38pdi0RwJMm88q2OE65RNhKCakPy47RjiVy-uXA3JdXAvdvjebhNEdRStbsCHAc6swaklcBDyl3QbRJBSQBCsiv0eUue0jD_euSMnetPPfPn6rLP4ZL6EznuroTfzaJ-EyQvWhotbDAM7_sd__PePGuAvLOGSYycLeoOQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eq_-334zod9uL10HfjIylX7KtAxuN1Q8HAJ-p03Vp9jij04k7OF4Qg0nQCxWKXah18wJlTTVmZqo5X0fA1kZcOOld12arvDVjYHHvgL0oCYcknt6GSWoSIOtCdkQxWlP48-4-ylko8N8EnBOvMG9DkdTdAifO_LWSQrKf53DExcRE_TRk-jkY-7DudTyjPMAD2_Uls6bBOYMcux11JBv03EIIIAdgprjfXgi4i24HJrhaUhopIj1H8fY9HtnFjQOT_CxeacJcFeC38BtDNv5l2_hi6K0ilNcR7cjToQRMRI5GlzTP6f0pEUp-Dz81klxAux87QIV2jOwL-F6LkQctg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_VdsJR7123SSQRuCY12gqxj6iASyjd-oVUJusM0I78WwHhcR7K8s2QkgXBxqC1D2KKIJJkKX_nWzRdsXOEGCOiVoQySP_k2XWo9Z94KKjzwxrTVId1nTxyaisHNYGjzd6XwkF0nE57iVzKrcy_30zEn3pM7Dzbx6GmEHLrFOCS5w6XarKDiNtP-Y-x8iq5-O0jHol5xecPz6h_p1liFprSffEK2QjeFRrcPhyzJeahGjnHVRREzFrHwV2vaGxyGXcNBmLH1z2vBOl21q_lYda54bQitXR7QSL8lcnCiDYQQC4wAo7N7dRfoSsLz0hTN5pnyj348-i4lAgE_I5oKmg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XAvZuiDCdNmn1Y5dR8MjAensLQcSiW8XndYDQXE7azMQ1zm2ujneRnhXJf-w4eyQ9yn33qDuPdbeeyCwdp5_VtvlhBFLEkJ0mvteegclYy6mLxneMgqCaQvuqRa4Yvo9eT18AZSSWECCIRJ_wQBiZLh4lFJ0OcI3qJ0SlGIyd7ohd11ecUTICYgWDMhqQ_Gk8DNbUO1AUDTBZ1IR6SFcf0jX1yDXtgiFy8pzuevbkhwI9tmC21zNkh9g6nyZjcPsWdLnR8j-hR4QAfaA0kks8n6xTThGLuPvOqKzOKV6fR5pn7wOScLWWixu80w2cE5BLaDU-qIFysZl3CjGnYEsUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pUEJHb2ZYuM9UAua9F2U8HmKYC31bumMhDd1Uu6Q0oqvB3lcmUiay2790OinCpxCty9_6gQ0BPAn54yNeD9KTZICAhQj-LIRzVAVrIcYp9Fh9ujOcuitdD94ylIXU7t5DlHzTiNA9Ay2Fa26zC-jDJxNprG5s1UNpTPIxgFelTBdg52kzY8WLDt9ADR3ErpqaXK_NIQnWpEga7qewHiJVcFRcfnyq_EWOEJOOuyxTI7pDavA0NayCz5lUlcFtUHnKDHPE5Yc6XxrE-8yMJibnf9_yk7FmDF5KrQev3z_e3lXU211EcxlQzJvlmI2oov91WQZyK3FrmTRyiFVVQasuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iX6x5g736Vl-gHy9moLNvAvoX4dJaUI3v0293W2AHFto-gy2bSZbgF3xyIa_MyMiBXAObMNijOBtj1Wxu6AIYgCfdEME6IptGGsg3yLPVKA-A9Pz0plYDS98BLAqccWdPZKERcZBp-i4NVoQvFM6H5ZdyRkdx65ddD7qxSyJiPvNsaa-5lysRVwZPzsX1LWQljHFFztKOOaK7FJ9XhEflsu8Y2O4v94T5tas2c-mAQSJsu_Su9u1D7okk4flNYRbBwIKittNvzxbA-QG0SlIR6qXPaZcmxEIcYlSovK4nRbbur63sFZdPRWTzvx_vB7edKT1fYdxD5PFV5DhYiPcoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VV9rm8yX2RJ3_kFYnBVK_oe4hd-ANa4UpSjq6NyuxLGzTb4JnP4-zjvS__4nl7JXpsFAWym3h11LZN2sbKvHNQT2xey_D0E3qGGT51eohGnnPmV1oGO6QbZ6acFIwCbVdbvx7eqXAM5DLot5uUuPKKptRKyWalTTATkgFr71F3u16XUW5qwsWuEEXXxuwmq8KYF9sWz_9QouYlHcJIuY4c8dI1l7NX4MgvOgT7uokEVWRU5JJ4ZE9vvWKVxzNadWutJZtWv6yUPyKrQv4bV7WOLTsP-qF_1NRZFAw2prjBTPrERnR2D4NRLAcfklllizBtNyiTUWz1NYV2xDp2LtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mdIGr0W-mEqLs6Afr6srtNOXgkZImj_TN-qdVQwbGDT4E3bOaQDKHRXfzRzMR-ohKrCrMWkWDIduMbxljkld2XCmxkhAmeCRYb7pQAJ_bhAGGIAbpAWdxrszvI0T3SVR6wmdi2tjvyQBozeJ5r4vh_8SJE7pCsZcfKYcAWjGJsFUN-7U-MKUVYedIaC89-jkwZhaowzp70toLgObyxdn3y8YV1WV6WPyxc7qMsidRWwLS9op-lbYgPI13jrX_qWyGKY688jmHBI64i2tFfO5NZkvHFM65oE1A17yygz4kZxkpZE3upBNTf1X2wxdisyyGxyPt-kZafeuog0rtZUgdg.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=q3Y-mgtvSI5CzgNzg7m9cM-BThtEYkN_9QC1FAnnr0xZhzeiUTuV5yD6Wekk8kJ6LnIzhRSKl9gyTSAZal-vfBf-VYu09Pv8n7dRmEE-LtMxSQ358yK_XBbRtWKkzeXvWgKcYjhNFvtpD5kLm1W6mGL2pbSZtIl7ziUpcR26jOd2XeumNQD6c185PDJniHiE3MqXrgqRsrehKIekzOJVDsYsz4C5bbwVvW9-4gTv3LvaUgVwbyC-676musgEB6j989s3jD9IgWGuFT6AhwiZV4Jv8vBGQ5d1Tv2s08JGGduuL46XxxQAfonbUJ1Pqcjc_gCZODYpRYnMU6y0HbDFyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=q3Y-mgtvSI5CzgNzg7m9cM-BThtEYkN_9QC1FAnnr0xZhzeiUTuV5yD6Wekk8kJ6LnIzhRSKl9gyTSAZal-vfBf-VYu09Pv8n7dRmEE-LtMxSQ358yK_XBbRtWKkzeXvWgKcYjhNFvtpD5kLm1W6mGL2pbSZtIl7ziUpcR26jOd2XeumNQD6c185PDJniHiE3MqXrgqRsrehKIekzOJVDsYsz4C5bbwVvW9-4gTv3LvaUgVwbyC-676musgEB6j989s3jD9IgWGuFT6AhwiZV4Jv8vBGQ5d1Tv2s08JGGduuL46XxxQAfonbUJ1Pqcjc_gCZODYpRYnMU6y0HbDFyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT5K3giPd6n7KuF62TjPyKXs1MgnkXAas1Rlao2fueoGh9iI_FyOCg_OCbndJyZIhb2CyKC5hWfZcmKPFoYRz2PKpbr9mf-7qMa6pYi1LWugDbpvwx2iqlh7DYwVADWzjj2N2rHCwWCLK4Cmam5at2IFdZfnCeySL0hc2yCNSU3z5QibE4Q6mUjx8xsrxFtbDwSuFyvib4xBA40Gj6nm_d4c5bEra2pwX2uwkEWv077fJoekkJNzrpCDZDmLgA6nGKivgktO8hWksrV3kztDljKOKHO44CR_aPHFZ7D7u_4jVMXMZog8qsr2WDEhxqTpg5pDXslFoRWe7jC2Y_Ydbw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3sBkumoZAFPTxXrML7PMX6AEdiPeTxYKTUuBSA-pwdqQj7kn6sslmrp_fAnUW94mrbxUOtuAQkbJ_A8V6Q2e0CoOu93drvUwuPlhFYn_dY-EW15yMCMobGmlb8126r4jznOoNxBwyI0d9caARZqvTT0aaPdS6TV1hR7Mf6Ikl3U2WMkwXbNhVvG7SY4z6xhogm4yvb1T8WtfvtqOYGw_gloN0zv2WT3nrRAIW7R8GFob90_dSZOC3YgD91ibVN_akmStZzBfvJpD2Rc6x_Vp38bY8T7gx519_MQJv7FXWWfRxShYXqzrNmY6oEaW2lxe1V8nyKrp2dHgDtAMd8IUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=TLwFQBn2sVp18m8VSCITr7p9b3jskopCo5q-j6_FQxX9GGznsOycK3OcZkkvivTZw1jurwMDhnlKsvc6QAeyYIincAa-iei-dmRhYFoiDNYWUnawUmKO5wbTi6V9F9VYXumbPxnn2rT1m_L-Ff4rn-BxkuAO0ssJKhluvbjGxH6MxGvbZ9iFt89mSs54jTzoZGO08SArY9tkXpj7pA137sjn4_xivngCZ0P2rvjw_Udwg2_mfeLhvpV1xw9eJ4mYhyC0Q4tiwmr_mIbLXSz4EAM-AXgVMjmZciQEO5uDhIpt-Jh-1AIZQSMkWEFlwPbPe6k12eRZDQUopDb5PHlQzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=TLwFQBn2sVp18m8VSCITr7p9b3jskopCo5q-j6_FQxX9GGznsOycK3OcZkkvivTZw1jurwMDhnlKsvc6QAeyYIincAa-iei-dmRhYFoiDNYWUnawUmKO5wbTi6V9F9VYXumbPxnn2rT1m_L-Ff4rn-BxkuAO0ssJKhluvbjGxH6MxGvbZ9iFt89mSs54jTzoZGO08SArY9tkXpj7pA137sjn4_xivngCZ0P2rvjw_Udwg2_mfeLhvpV1xw9eJ4mYhyC0Q4tiwmr_mIbLXSz4EAM-AXgVMjmZciQEO5uDhIpt-Jh-1AIZQSMkWEFlwPbPe6k12eRZDQUopDb5PHlQzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=GB8c9tVBqTgzkneEqmUN6URg07ivmKShx-RzaMVHGCpZhyhlGwTUGxByvUz9LQ0B14qXXPSfyG_cIdAxLwYr8ycLc1Ca9AMiMYbTfW4rn3z8H6ha_rjGlG8MxtpLRdlbUErKbOtXxLlV2nbdYazYqXwlw1TgZr9zt0kfBqD8vFXJmnVD98Yl2Ocyn-6mLxvesgIrdFY8jcwu-clyp54RSzLafDGUfwoUr28m5zfzx9Ds6er9FCjttHXzI42xUGU0MDRf3BfCKaQY2XNIehg_AgnuGB-UZOkln0T3nMCbBfBnUDkef9yfvO0IcxrOnXjuKw_wXnCvFlOjMUPaYS96VA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=GB8c9tVBqTgzkneEqmUN6URg07ivmKShx-RzaMVHGCpZhyhlGwTUGxByvUz9LQ0B14qXXPSfyG_cIdAxLwYr8ycLc1Ca9AMiMYbTfW4rn3z8H6ha_rjGlG8MxtpLRdlbUErKbOtXxLlV2nbdYazYqXwlw1TgZr9zt0kfBqD8vFXJmnVD98Yl2Ocyn-6mLxvesgIrdFY8jcwu-clyp54RSzLafDGUfwoUr28m5zfzx9Ds6er9FCjttHXzI42xUGU0MDRf3BfCKaQY2XNIehg_AgnuGB-UZOkln0T3nMCbBfBnUDkef9yfvO0IcxrOnXjuKw_wXnCvFlOjMUPaYS96VA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rN0HBn7o1zK7guUe1OJ9MpxobNJTvSA2uoUXyrkorLYG5LEn_FRm5EhiFX8BKz8QsL3cBDgAaMbHmLGf1cnww4JIw0CBptRervUdiKWI70NFfZR_0DukWgBbbwGv-4hqjCx1_1EN7FECRYr3yaF6uanbMecWsLnBdIj9GgS9jeCPZ33-vr0jiOgw4rZ6Mgb8eP6Px9BzLNa5wiAOyH5eo2QtNAtKgqrVQs-7caLR2mjzu2e4Fh2cB50Bb2VT2e5WjUzb-0_MxsNrcVnkcgg1JZVJQNDg85qti8GO3kjqjDc-tkozzRpUyRWB2Zx048KAY7C6b_IUAJVHWLLOetnkLA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7PVUeWX4fp-vloheGaydXAsEPot8zwADZXWnUJcEKGr_ae4zegGpGubOgFJddUpg7zV6gmctk2Y0zZzf7RJEI4_b99ObKt-LeFcK6UzGU842KJ-2bfaHHbs2Mmo8IpRvJlsZ5iYub-4SDz2okHG-KJ17tenCdeQJ3SIRg9FzQuGhERhqtVyIaJ6DRgkBSz7J1mtprWGrUFw4NeJ3vzdIbqjWDa4o4HvosyMEU9zR5T1wWI9_ON3YaD0y4GnwsoC7xcU55y9jktNCzeRnw1t8ht-AW7vcc5lqi5vROd9FYeLB2sUfFgLJoOiTHXTG-vSVTQ8D4Zlye41JjDoafdP1g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BmTI_lc3Er2C9iCozf8ME7NZSmJNiTrGTbQ42rdegZuN7Vb69KZTVj0za5l8XS_ooMLLCmG-rbMOAZsq1TwPYIhtTurV1nQBzeduS6esoH9Td0RaP8LpjLzdQTon4wn0nVdXZ_9cpO4eXOH4XP7r4jcwhOa8bopi_TPtx3rPF7HXOqSkKuktpvTLbeYBVmwAVkv-MT_CgzZOIaW3WGo3HIvps50kkzdK3jDWK2R7M11y9-VBIq6NtVnomWtXbJXKMbIZMTU2E3QKeARYYAxvgSUl50A-Y9zxmOVGLeuyfuzQKzq2ytxfG9HSlrvyZq6wsUpJj0PpmYI2NONNJ_G5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZ5HDja0Qyl5h-cC9mPXR84y1RNq3xkRymw_OQr7LwWR4_AhkPvF72XD9QYI6Pb8jcgnw-IGFikrwSnZV-WC3Kz6p9X4ibKE7jf8GaEOzar83iXh2YimQQ30LKj3QgaVzhT83EM9EjLzINnsHyBBr5ym2hGo1vhw7xEt67rHxo6eCiNs8cIQN9x9cAlILLoetAptYx_n2koEAoZ9ddD2JuJ1o3vDlizldez-hdk0GNd9hJDfWi45XcRi8wqCodHmcsMx2Fid6S8TyFE5L-L1Woe8551ixi747pq-1gi21EBlfnO6uUDKDII_rUV-vSuwf3dgS9rGY8_G3GQIr6hkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf8J7hZoJFYtxe5MU8dgpALxXkAk0ZrC1t_b90IfUjcQVcF7mWfpfqxQK3NXla-NCVuqnWr3BzjJ1JHK_gyXS6DiEwqBX1OI91QnxWjbXAPLkWhAxPoTq80wglpQlwc1YtFC3h_6j4nwEkgqqZNTcVoamq7LIR_VkfMr2MUjlHDs2jERnTnurEDq2cVPDdQnnMiWvHMx2bUI_Xz7SFfEqMmBIenOhlvlP7SbxF_F23H101ftYcIpv-A7NTRhKygOcLAA_mJg0V9-L-ckS-DX1nCkDkOird22hVN2CcqntzfeGdXvrWpR0vESGow3HlaJ_f8ZjLLmaLHHALx9rKEOeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s0m0tyZQlYxShI6h0TpfGq9vAVG3DvGHN1GUKZHYILfW-iYjQECnXsChmgAJLytN-OmVVtUZCZDVtgELnqKDrq-uyJEL7kdpC4rEfu_U2m3-wvaUe_llP3YmB5HhOZThncsjni2A0i4G5nTdqNEKdMpX9mGivQRKbDFg_2Ye6_cbXrcIWu2Nt89VhmB4TGOuwt3OmH8REP9k-dRm6k_blzmp1fj3V-Vyj9vHj1piz4GI1_0iHb8VcoiTKT0WExBjLyEeSx3fJict7gDuIqa998Fyrv27U7Iz9y5G5FwgFBAzwg7uAzlSWIUYnQyg04N5J9t8P2R4yfb1cz1XFmO-mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yfam2osdwLmr9uxLbJ2amHs8kc12TT5GP-jgWkbPkBIVaGur9H6MaPZsxWH1qDnV4TF16kccYXRt64fAs_JjS-k6VdAWAuMJlh60LMc0teNu52-adBqyinJyVkr3dG03KlL1-TRA81bqXTN7qXWdN_7ojx2FmP3uRH2s9C4ZVSuSrXDsvYSn5lIxKRvOb23dLi5D7_Kbi6gr6MTc78PVepz0f3xZrL0hFr-94aqS7mgI5sU6KzA0eSkhHM0h1Mwm1LIqfyl-RYiU6btzPUZ6rc-SV21SJ6sq8m52jpi1ibtsOPaEfq9P2vLRxzMwYHmle_x95j7MkAH1N2m4-5io-Q.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YrKqbiknlrw_iV2PBf5ikjaZMAeWHhtOPdcIGhi4lFG_OQ9vfbsXfM4VD7kSafkeajbquFhA12g_XLuKisXkza75RVkXO1Yb6i_o8gmz3cjQccnFIyNkiR7gIuqClOdn4HQDdT4CWfj8Au49iJjauB3Qtit07MqKFdgLee2X1msjbHcdASzydSjyOK2mFMHFHV3sPo-gzNgF2DC4fnxkBU8yHB0vA0mVACv4FdRRRtAJwnaeNUTd2W4r_WbjwGUPy52g38WeiOgK3RrEYXsA8zzj2lP068Q0x7K0lWXR7sRpOt_0-l6Hh_SdS9meF21qMMrVSPgk0VKQjpQtAB3UtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=YrKqbiknlrw_iV2PBf5ikjaZMAeWHhtOPdcIGhi4lFG_OQ9vfbsXfM4VD7kSafkeajbquFhA12g_XLuKisXkza75RVkXO1Yb6i_o8gmz3cjQccnFIyNkiR7gIuqClOdn4HQDdT4CWfj8Au49iJjauB3Qtit07MqKFdgLee2X1msjbHcdASzydSjyOK2mFMHFHV3sPo-gzNgF2DC4fnxkBU8yHB0vA0mVACv4FdRRRtAJwnaeNUTd2W4r_WbjwGUPy52g38WeiOgK3RrEYXsA8zzj2lP068Q0x7K0lWXR7sRpOt_0-l6Hh_SdS9meF21qMMrVSPgk0VKQjpQtAB3UtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vi06bdmN0mwglhU2lUQvd-2tokoyTUoSbTBlC7lkCe0d7Ni4Q_Iz1MlKEjz2KxPi0Jtt8khsnaNSdl4qCxIUA2otwFBzNfp6ACKuzJX8Oud_RxJt32KzIzftwH2j43Q7lepOw_utayL8ecB9nL-A0o7pK-ybHY5R0gJm_dtbbfiVXXQoeZ0x4TtvOhfFQgFrxgj6kiUjTtmHpecZoLr6RqEgFkbHTdvYU0FH7usuY0xjw1eqLHkx_DJmph8Q7AKNbG3u976Ys38qbDRbpViDzHQxpApYZXHnimjTUr9XncmTeMZkCa-f9NdqpXVaiNrpUHmVSFbNZFW9e-1WNyvPGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=gFtaa6fT9slKJMKf8hbGBXjOvV_wV-6SOcRtIwcD961cmfNGdGalU8hqAvwuMD3VzDiy8STKDOtm47dYB8XVf_D3bstPiSzgVQmm_aTLTrfsTo3VBd7X8vJSWHxjPjgjkFSrZSUp1W47yIwBqQzQGPxBu7iUUCDHTOxZlWPY97gcXGS3xTaru61ywo_G5CazR7FWAG0sm0phns9FKPgPC1ETex0s0I-SXnbywFn3wjxL_SyCrlSrB5j0HFiLU0WrW8mTqqqQTTxdderkjIFC4ts2G5EGSuG7kpT_2XnymVLg4Cx0mcbCZ6tWr_AyVaCiWQw5IU2GIkpnCaQkH-qoRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=gFtaa6fT9slKJMKf8hbGBXjOvV_wV-6SOcRtIwcD961cmfNGdGalU8hqAvwuMD3VzDiy8STKDOtm47dYB8XVf_D3bstPiSzgVQmm_aTLTrfsTo3VBd7X8vJSWHxjPjgjkFSrZSUp1W47yIwBqQzQGPxBu7iUUCDHTOxZlWPY97gcXGS3xTaru61ywo_G5CazR7FWAG0sm0phns9FKPgPC1ETex0s0I-SXnbywFn3wjxL_SyCrlSrB5j0HFiLU0WrW8mTqqqQTTxdderkjIFC4ts2G5EGSuG7kpT_2XnymVLg4Cx0mcbCZ6tWr_AyVaCiWQw5IU2GIkpnCaQkH-qoRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=ibV2N6hlt68APyqusVwg8Barzbzu823XNty9-sBTFvLnbw9YUc1ulxEYgvvT3cl5f76Zs4f0ci705ZEexQ5tPrsQ6D8ydcDKqgOdHku0xkcIzecp8NxwtR3iHPNzE071Gdjy199QF3TyUZlFIX4MNa0JSGnj9bpVFGitYZX4CEyqOyc6-xnVkDtiQ5Dt7JQl1NJkahph5n4V8beFp6D_EaF8Xme3SeVD1BUBswmYajuNcIVyd08RkyxMdjOIz2Ms3gRkBnuxrj_JaozNsDVyryXJEOec59W-bVWnGH7JvCkwqYNNbm2a_4FuNY8FiuvLYDtVLBFAzrkomaYrtEYsAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=ibV2N6hlt68APyqusVwg8Barzbzu823XNty9-sBTFvLnbw9YUc1ulxEYgvvT3cl5f76Zs4f0ci705ZEexQ5tPrsQ6D8ydcDKqgOdHku0xkcIzecp8NxwtR3iHPNzE071Gdjy199QF3TyUZlFIX4MNa0JSGnj9bpVFGitYZX4CEyqOyc6-xnVkDtiQ5Dt7JQl1NJkahph5n4V8beFp6D_EaF8Xme3SeVD1BUBswmYajuNcIVyd08RkyxMdjOIz2Ms3gRkBnuxrj_JaozNsDVyryXJEOec59W-bVWnGH7JvCkwqYNNbm2a_4FuNY8FiuvLYDtVLBFAzrkomaYrtEYsAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ucbi_l4xLwH5DDwo8oqV9CPLCQRGLCCz0qZlUhpG4Ip_qnqacJvUTOybe3LbzZS05Ayp1dGT1plgsRm_PaMi4J4KTPmQSy1lF7-Qyx2FMp2x8CGA6jo6cxe4w0l_z4Fx52KJVAmk6KeJeLxc4LkwcH2qsVXpcXOqVwSa6q6_hAe5fYP9xtClZ1AfyttlL-6hghJj6SC4yEzZ5TbowczJS-zQ7U9E3H1wsTSC_a-sHUIUnuLpmwpms7sR2MeZVSNOLSlAZ8YeuizHoK7EoEDGWyHI-bTAg2Qmfg17f6MY-JkBB09rTc7auaJkYgzyo1le50Aej2hQdKokYiTbHUAdNg.jpg" alt="photo" loading="lazy"/></div>
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
