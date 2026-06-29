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
<img src="https://cdn4.telesco.pe/file/KQYllhrq5fquFtHCl-q3zQgK6mHyFRITxhPfTjZAVFfEZxjL5smCcAsz8EuTtYbMnZoqBTW9beNEJdLakE6fiB2sox75YXmlda737VXHmtfPUH1khrPvscjX6W5fIxMnXHtaszLHO_QSeMSxyPpnaA7ThK6IdDznx9KKY3E87D3kIbWk2dhgeDXuo1Dd6qWtUjqfXa_Fj9O2vHHdraHj7EKGhZRLgCKNQLvMAJNJDK1g8YOIrVCjTXVph6WRw0BVEoA4CHwCvtKlT6F-UQwbJe2BG1Bg18qrPDNY3gGYWeWmiNT9Sje-6VnaYHNd2t7tZBzDg6iTNDj8aEN2Lh3-Kg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 345K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 22:51:11</div>
<hr>

<div class="tg-post" id="msg-24633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3KfqEW3b0AQvdNjZ7uQH3g4lfek0rqHM9H-ZqHod1J0R9eAmziyaUQlmzMg4EB8HDBJ5r6PDFfnryeR8bFBuyzMGnRqdebNhiKPIRXCtlUN2VkPv7O86I-sWnZkgrFJ7e4S3oiNUFxOs3CQgaUVzhmoCVX4sW38s62diZOArINdmbaHmqvez8FuNeiT28a5fy3mN2N3JJRnQL77086G45PUIHvnnBr-jK49Bum_Bm5aCNrj22zeKYI9vGKXRghqfHiCDzaPbElfZer0z6Ir61IR42-fFzwzB4oJn8YSewbf22WAU27iSew-0sV0FsX7SQgwb0KA37YXraZtmiwa4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/persiana_Soccer/24633" target="_blank">📅 22:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbGpqMY_LQwwcLH5WmlJXHAkBTORebXz-R93-RlM_7O0OEBLZrN6nHzCy_efHeUQzurilg9igh8_v6kNri842rKs5kz3S7mKZn92ULRMHlse0FQjEIku7Hvn5bjuCnPJzymTUgfUZ1bF4cR-Q3_E2BuSn0O2sFNSwMU48FSM03mF5nPQda1Gk7K_6bnbmg_TYBnykUw9CXwbaAVX7GEDeG532q64qQYC4iV19JxTwC8UeVVjml3ygMvvf3NeuOshJqXxHrncgQiULn0zU8z6zDF5IgOF_WgzBZJ9bZwjZLX75OrBGnBxa6VzyjiDaz64aeVyoCSEIpM0gzmqxqXGXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
کاسمیرو ستاره سابق رئال مادرید به این شکل گل مساوی رو وارد دروازه سامورایی‌ها کرد. سانتر دیدنی گابریل رو ببینید. قشنگ گذاشت رو سر کاسمیرو‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/persiana_Soccer/24632" target="_blank">📅 22:36 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a71ed73a.mp4?token=HN3aZjjgIKa-M0zLrgtQK1ImjxUTuOKW4A8tpskhRlbajo7oeIPjy_yMH2o0uKpG5HHytD6cTJRP4oSTv1GuUsKII89eNT9gregXNEWuuM68HElpqdtWouEu6D5fZf21pQkvfgeUDeKq9DmaTXzf_EfAxO76g2shXFDdUnvAWS-tlS0E3DwOydpAyEX1sNBZLAqZ3-FAVW2mNBsiDbuO45ufR9J83srUHzLMZMz0egTrm4RBU5C0a3BfZdzOb_VHyQPSQ5MbBwgpBl7u3d7ERKs1JB4enuuKhcLDPqPqGrMUBnvpUUredgK3t-Jq6hSklilHmjVfbAhGfAT2Df-PfFZjlKETJGWknj2Up8yIGNC5gW3my7015BVoqAM8IOlch9wxhZg1qO6uj35lGQckxCxs8jXvc204woJc8XdbniI1d2OOG5EVVAC4UWSSYyX_ZDLQS4d92DXkcc315rTqQ3GVr3WCw7vAiyajqz-LjHvph5gg0ho184OAWGWYG8XOqBpJNHIY1ZmyON_bQBP_1P8diFChJ_spLh54CHmBoPzVJGKfnTMDTQj9RJlUsLaicBIBfDDBwZtBLX7V-3VjF59ocFP1TZJ1J6nWtTKJHiOztRnbq-Bfd8C13RV0wY0UqXiQXCbD6t7Dc0K8M7-WwgifwQA9IT_08bSk1kdIIgs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
جالبه بدونید که؛ گل حساس کایشو سانو مقابل برزیل اولین گل دوران حرفه‌ای او برای ژاپن بود. تو ایران هم‌بازیکن‌داریم تو بازی دوستانه هتریک میکنه تویه بازی خیلی مهم مثل مصر پنالتی خراب میکنه. فوتبال ژاپن 100 سال از کل آسیا جلو تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/24631" target="_blank">📅 22:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔵
تیم چادرملو بعدتساوی بدون‌گل دروقت‌های عادی و اضافه توانست بعداز زدن ۲۲ پنالتی در مجموع ۷ بر ۶ گل‌گهر را شکست دهد و به سطح دوم آسیا برسد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24630" target="_blank">📅 22:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TZdohz2TApj49LC5iZPm72kpMdzwWCQl0X7TEqq5J-4AaOerzczm2ZGzT3jquEoUd9EboDoAi0mu7iknISglPiKgzK80Y20HBzb94tAfHnvwJPHpOsmEh6co7BS3CFfEwa47M-J9NManNuqRJ2Yoc4GJ4NbYVtGBeiifIvokamy9dgaWfCMwQS9IeX16IMnIuJtV7hkCIUqhxBy60ROer2BW7yuRFATLr30wdDnUvUMZ7JQv1rJ77NkFCJxEkiz-BpvNY2VmvpuD2UPtMwXQvmBN5fXsH62RvMkdp1Xg9lwT5q-V28BOAHG5M-5znF83QSvWWf_iVL4NEgL09vyBFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🔴
باشگاه گل‌گهر سیرجان: مدیران باشگاه پرسپولیس مدعی‌شده‌بودند که این تیم یک ماه کامل برای تورنمنت آسیایی‌تمرین کرده و این تورنمنت باید حتما برگزارشود امادیدید که تیم چادرملو در تنها دو جلسه تمرین این‌تیم رو تهران باتمام ستاره هاش برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/persiana_Soccer/24629" target="_blank">📅 22:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b41af009b6.mp4?token=STtO8qA9kJ7GI8F7T-uBEx204hVTHAwyAoX03DmB0HqtsETPPgHpEM5-lFobHfClA5hR_40L3F5KH5SGkrITOqhes7AINEeBj-AblXAmS0Mre_PFLJ3ENz0HYwjb3btoaX2SK1HDmfvdtP5ISgHkKJ9Re1JEJVj9kSYKAcf80voQqtB9GgYF1mss_A81m4AU7lSYWdm6K55Lb5lRK_36tIJT6az7RnnEJh5f3kpRehBLIwfUOMnHYK4Xoj--HMJVWG-5WoDnWWRmQqbeKS1HyOvU6xGGgCtQek5w9BTk0cjSP9SWh5ludmoCebiREoENWNp2C_gfAprM5pg-91Kq1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت های ابوطالب حسینی درباره خوشحالی بعد از گل شجاع خلیل زاده در بازی برابر مصر‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/persiana_Soccer/24628" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سورپرایز پامپ با جایزه یک کیلویی والگلد
بعد از پامپ ۱ و ۲ با قیاسی، برنامه جیمی جام با ابوطالب ترکونده
اگه میخوای از یک کیلوطلا سهم ببری کافیه تو پامپ ثبت نام کنی و هر چقدر بیشتر بازی کنی سهمت بیشتر میشه
فرصت رو از دست نده
اینم لینک :
👇
👇
👇
ثبت نام رایگان و دریافت طلا
کانال تلگرام پامپ:
@pump_vod</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/24627" target="_blank">📅 22:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/863d336b56.mp4?token=bq3K7mGH6cMCvZ3hyaJqciyy2qwBB2fsSN-VUexWrHxUw5WmPPlw4wFrjJiP2evdwT-5DNNlhoIWDl3ZfuWfp9gYAht0Po_RXbNZji16uB-W9dV8JJPR7_Tgo8VnPzeiRQCgKbKAk_X27Ms0ZlXkHsY9N3o28er9ZmKujffnik9xonX5pZ24boTbfsf0dLuF83kgxUSh8X4KM0PMVWLZAQdtn-cJbmrBkQupkSom3Rc6egZdaXbA41Ra4FP9_CwMOgUjb51RCumjoFoeyWgPe-kpb2T9lCX_zV-Ek_nZpGIYStUCBXZS1pT7sr3YWWrEh7lD5hK7CWGYeqNi9_dTe0oBBofg7ZLAO0lVpVVyO5j7iQhsGq79sG7eK0i6mSAQSsBQep1EmFJjRQevAweq0-U2gQ94mnsrBiTR_Omrw7XjaMoEGp9bGhwit2sFgz9P9dePgMn-VKrpc78DNdYnZZg0p-deO5LiK9fgZ7-5T9CoJxKGBqP0Tn5XUvgVgaj3-4HSN-kREksvPz_IedIRCjS3vhVoelJ4SLoh8CQe615oREjHOL7iK8QJrGdOdLbgRV1GZb_NH_Vrq6C8x7SWjU3hjjSsSUTZTCREtixTTGvEiJ987cj4oAksjo7xLxSfD28GGGMnddfVG7OMGkZvhtNjsk7VAiF3NbI_EXPLpVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خطای شدید روی وینیسیوس در بازی امشب با ژاپن؛کارت‌قرمزنداشت؟ داور به کارت زرد اکتفا کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/persiana_Soccer/24626" target="_blank">📅 21:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8A5E75KdTy_NAA5GPYx4mo7IlcPz-9PvboPem23rXXiRIvEpgFx7Op3hjmgDbhaE38otYoIFDjIEAr3mIIUfFP0fuq57ZtdkbOLheDi4PumrsHb4UNjRcEipCM7YnE4QtegIBQfJZ8lmcax3WiTEEP_xyym_hlH_HUmmnDTb9ii208wP7AkANy-UqJr-kcRpFHHTlOaERzg8SHikRJDao5f7C1HDVNVY8JNaRwmbiutWAT9hN1C7_56eTXeIlLv_C6aMBOHFGWmqhyY35mEpywUtIGMz4jvA3f1UoxKhzg4YbNf7ZhGbFEKe8k-Hq47zs-yvD-0vWb9K5XchRktGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک شانزدهم نهایی جام جهانی؛ شماتیک ترکیب دو تیم برزیل
🆚
ژاپن؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24625" target="_blank">📅 21:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7056183539.mp4?token=XJrXqclN13soqQT_0fo0ApG9TO_VPwjcO_Ky4A0Uf_8psrIMhsuzxuJRV_uDY5vSgHsIFSm7wXMU9-HQLtl_d9Qa6_f3p6867eSJ7RgPe_hNZ-KyN5VAIkXM_yYhT0gE-rgoPrYSKWKLxxJgL3bK48BzcpxJaSLjGwi6y6m40GvOBkwu60U8GMzQmYo5eC53HFIAITAsaT00Hu51GXMk8DZQPxAS3jEK_a262jj0-wrn5lWYlgeYVMy8dv-qX-4vxCfnSbT2PcV7N43WJQHnh9ycUJILvSRmD4W21BE1n-Mut3trKupiSyjG_FKcRBrFi8nyL1fyTcPPLpC5a8VD5avR-OXLirvxz8ndwv75k0ZBqxMjS87A651YlMM-UCKbOu70zLpF2lWoYhysQhVLwnLjJcZviJke7yjYO6R-HO0vlpOBAS-DDWKPhejZUjuEK6nZi6PFT7MKWlRMlQEO0Q41D5hrozWLAU1kcO-wWpriyeC2BM0BP9GEjCOFwpldHx6JNfth4FsJCZ6w9ao7Zq0Ep_TnOVir-YBDJ5dDS2U0CLVoY2H_IfZp5BNN8okd66E0hm0hs3TARmt1qhTH0t_TEoCivLttJpDlWh-NjidSCWsSNkLfIHEhVfUqfK4-d4hCi5PjpUGgRDL_rtXLj9AE0LTIr7g0IFaatv36-54" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب حمیدمحمدی درباره شبه علم، خرافه و فوتبال در ویژه برنامه جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/persiana_Soccer/24624" target="_blank">📅 20:14 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufmRqLNLDeJlqFYpsADBdn0_RezOR3lGimo9wXNDPgTvIvbamzXAlVb20lR0wEEcXRhhpLBgSj_H1NdJKhcW78qfZLOPIVsPhfqGU6GKaHUafNichqXhF2V-wvUkuQC1n-wLsyxNYTDUAB2kIhMszaOdsEnyW3WPPmEDimz9k4pIcdwybLN-IQ6wO2N9Izt6L99Ej-MUq1sD1fRfEDqaDGnD6jVzNqAgzIlRSK0mLYEzSCIzyOwp_-jBmk_f4V8Bi9Iatg8Mbd276u3_TR4rm6p_FEP5kqd-6y88IHgjx0Cq1Xkn1u8puf4mTM4hvnJJmtchcHo_02Ehp4KZXUr8BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
طبق‌شنیده‌های‌پرشیانا؛
جواد نکونام در جلسه با مدیران‌ایرانخودرو برای‌پذیرفتن‌سکان هدایت باشگاه پیکان برای یک فصل حضور در این تیم خواستار 55 میلیارد تومان شده. درصورتی که پیکانی‌ ها موافقت کنند نکونام قرارداد خود را با این تیم امضا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/24623" target="_blank">📅 20:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmSRFaKSRNz3TsWZ2HEO3qH6ZDhrCrdLFTVilXHYSCWDy9mARSSsY9_4QRLUrTy_UHVWdKSvC8ETOFYZ_2Ey8hdGYIfr9MG5CSz53EBJHo62sMHuNzPD8GKKoa_lCP2j_UuO2ze2yeX9xQrIGwBTJBnT2t9gUD2c9__NPQ5BO8AA8UH6JCWtgZt-9gHzI6GEfIeyfpLcFVLLgKZRcrw5YJ58wMsRCgFrwXG7sp4z2oZdKHcLYi01xgMykx_MKnpgvxlE89Co8_EhFnHiq7co1MwSzg9Rqd3PnyoPMiiAETS6wUggGBS5uMgdyGtqAZdzAoiXXj-rnUoLvzY8QJjR-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌رسانه‌پرشیانا
؛ سیدمهدی رحمتی بعد از عدم توافق با مدیران ذوب آهن؛ با صنعت نفت آبادان مذاکرات مثبتی داشته و احتمال اینکه به‌زودی هدایت این‌باشگاه رو برعهده بگیره زیاده. تیم صنعت نفت در آستانه بازگشت به لیگ برتر ایران قرار داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24622" target="_blank">📅 19:35 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24620">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZFn6PvIKjH6YZQ6HLPS01OmOjxx0vr56v16UFNp9F2wpVauMqh9ekAZ3fN1yUWCxiLqrH2gvmlrsbi6bfKe-Ukyjm98hOrNT90GDcI9DgOUcW1i8zymZwYGQwvyKn3VX5ea4o_uscI5T2t0xSgsPkwTLuBmq907FNbQ0Bd4eAeYJ8AmxKGNPRCACVCZkyc44YU9TaTb6-7vvnfFvHrzuD8YjflW2lg6lZlFxQYanzbbFpc-hjpy9lOzcNG8ZVRoPhfeNFNgeX9z8RKCevtg4QiZtTeKPXXE6JPCrsnux0loXrHd7zlhieaUhogqkjTxie_m0ZfBmnOVpUQoKiMy9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/givv9g2lmwSCgvhOJveNTQeS8tsFKkGcmWj6BBsqnCYZsDIv_sfw7AiY1knUrW5ZyDgUAHrIP6bEK9p2uoBsEGqSOxOvinJlqpvXpFBc0jopYou2MaKm072UKgDIBRNrojBtycFuMVb_iJqxQbbqv4pzPqg_31fe8SrTEs3B3h0dGQjlc9pKkSUtpIylM9Uja6HIZYuiNGCNasm-GUPkAi9AhaPJPNFjowVSbSJtbA8qvPDRZNVIa-UOpSWjwzpsvMJP7STjjxb4iTCMS0PDWLMoq4o7Jaom0Jp_526jaV1ElXE4JEwkRabyyIroexDAqlbjJDlDH2TzYgUi70JYGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
از تلویزیون تا زمین فوتبال؛ بالاخره اتفاق افتاد؛ تقابل جذاب ژاپن
🆚
برزیل؛ امشب ساعت 20:30
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24620" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24619">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQ6sgMqG4FCjjw0QEtylPseHHICwGhLs5sTnFYJ_70iNqy5dTbHdQaD3eWXowIjFMpCBXS72KLV0PBM74EHT1gphC9nk1cCdFjx4aJi6iQRlDGKPdsHevyA3GsEYUTkZ0JKC1Ok36NBEUQEJSce7vPEyPYZ5zRejyMUeQilIlfB8VmSoklveKWTht7BgfKmZ5UJQY7C2uy3k0ye0jd6t9f57e8VEwK0kT-tL9ehP16JX6-tfU9HM1188BSVqnsbcpNFHLD9yym4zlaeD0LQycZRFWzm248ZZ0IIeyM5_xLYwxIE28M5mApU0KOnSTp2yJ6gsqXfrR0zDo51CQ1JP5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شانس قهرمانی تیم‌ها درجام جهانی ۲۰۲۶ از نگاه بازار پیش‌بینی؛ فرانسه با شانس ۲۳ درصدی در صدر قرار دارد. پس از آن آرژانتین با ۲۰ درصد و اسپانیا با ۱۱ درصد در رتبه‌های بعدی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/24619" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24618">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnFl49s9FRRHJJeiQtrFsm4shTqSbzlqHMxTzQGIDjyrBoXCiIOVd16m69os9EMqzT1peEJ96UWyIBJxZ8GynQAWt_kHeE7at10keOM4LUL2s3vZ_Cy02xMBDO_U6pRvIPmio2HVYu_Vp3K8QmL1_qPk3zt6uMthV3h7h8qgGQfGZ50V4nyTgF4JSkPA_03rCQ27F0kWjCc7wXt3bX6eRHDldwsYtApx656cJrZTbChfeo7ndClBpn_S8z7--ZOImehpQEmLsiEKU49aizyXh4wYy2pW9p7dNZDKFf5ZSrn2ZLGXQtxkCmvfvAi-DjN_wa4M2lXUetfsLeAQrwvTtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
تورنومنت ۲.۵ میلیارد تومانی رومابت آغاز شد!
مسابقات جام جهانی 2026 را در رومابت پیش‌بینی کنید، امتیازجمع‌کنید و برای سهمی از جایزه بزرگ ۲.۵
#میلیارد
تومانی رقابت کنید
😍
🏆
هر پیش‌بینی شما را یک قدم به صدر جدول و جوایز ویژه نزدیک‌تر می‌کند
🚀
⏳
فرصت را از دست ندهید ؛ هیجان واقعی جام جهانی را با رومابت تجربه کنید!
🆔
@RomaBet_official
┅━━━━━━━━━━━┅
🔰
لینک سایت جهت ورود 8:
🌐
RomaBet.tournament</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24618" target="_blank">📅 19:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24617">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FEypeBVWv_eM_wYHJ1pIoOMD1nnn_iXzJF5Cqmv1OlTmRjt-XdohIJLGNh-dipd13N8gKHDFgscrR6StDYKFl8HyvlV5P33BK-RZxZ5bjE5VPEhmdFZOPodnasWpNuMWIVkJcV7Uvw0C52yOxq3gp390gc_NToEHPVSEDCtRowYVm5erbckkCSZKMnQSENwhtj_Gz8f9NCn1gZInPz7UqRbMP4Psti7FOiNJeTKe5SNtqeRh17D2Dx_v1vZaIyJCcJAFGzDEyXHg-LJRqLq3viVYmlF1MxFyo1Y_XkHPZNi0MMMNKvn_qZvyK0AHBGpMebN-Q1wFWJNWzU5k19VJrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/persiana_Soccer/24617" target="_blank">📅 19:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24616">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGdcYmPQsNnby908Iyt0A7oXkDldiBsuOMN7_T2pQ7pMSoCHxts7ybxKAYN3ar3vEGZz0gjLhKa19HyAmdyaamWnWO_7LvV9UMsQWMACsv6ozTdLjWPK1S8VfthHZW9GIG26pz91Dux-8pZOwjwztD7PlhOqcjOvw1_x2ObiRmpv-1AT-VPGGIO6uJ1095VGKwQo7eJMj0tPnzG3OhvTcdJava6LkDxRwVqaFowsAKV02fpcjY24vqP3AZp9_6J3aSOkHyBsa6YzMkhBc-LYXgyLkocRl03FAAxegX5giDS62GVcJLI0YR-kfmW_yaVIpnFF2nOg16xs7HIOsgY6AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/24616" target="_blank">📅 18:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24615">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aq9I0Qo7DWHnzRX35-60ucdvG5pe2M9GboVTNBhhlk_Df6HNKTNjo95VLwcL9tXN_3kWFPhnpC46tVduZl4aOECGYUdrdJFM-jyLNlkfxNPbog-YsEQnOpf_rfJuUyZlk_qcPEFOdi-G2ZCNuXJJIBJFBnPMi6QwU15rE4rmXCBbrRuCrmYLtfG1P_Yv9i7V-kN1VDm_E7fOX7aGz1ImVazu264nckzZekSDKdp57XK6uP0PKUNyI6wRVLhdZSHioX80Zhz7j6TOWuduPjdD4AAB8u8yKSWXgiWGwuINUJnmp5hpjI_EtISRHRdGtXPqiEQWv5O0i20ZAFhp48W3hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باشگاه‌هایی که در جام‌جهانی رکورددار بیشترین دریافت جایزه انتخاب بهترین بازبکن زمین‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24615" target="_blank">📅 18:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24614">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R1ecOWSbOcQ6kXIjndACDuuOifidFZtagJNBmb_6scZflJRy5o9uYTqxWA5KXBIZ0vMz4pVTqHHm2FDlKJmIDWd7ArFvYRKIH5Bn0-e-zvpGJaUNlU-nLfETpHQMywK1nm0mq0yi_mGnyetLuG3kfBx6K3XeOsXZuCcBp5aJTd02w8LrryK4SaLX9dO_OleX3QOn6DhhRH-t5z7kX8xjefZjK_t2E0gctL1p0sPI0icVIwR2XnocZkwNyquNmevRvmVkJqDd3xDHaPPMUUPBG_GfD5Us0FbvDHT9FXSpKUEbX30KTiKSw0AB9dpCgqaVHdxXnC_Ckq_8HHfaDgkjJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ نشریه مارکا: مایکل اولیسه بله ضمنی رو برای پیوستن به رئال مادرید به مدیران این باشگاه گفته و اعلام‌کرده‌درصورت کردن رضایت سران بایرن مونیخ اماده عقد قرارداد با کهکشانی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/persiana_Soccer/24614" target="_blank">📅 18:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24612">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6nj-C6R4jjJZGce3j5955l7ZJeeMBKpy9QQFVPJpUd4CKRVZFswQL07tz8qKXkN-rFF3ebfeGNmZjTLCONVBuIHV8Q_mXX2MP5UHREFg30SI3eWdykhKcPlulMdphR8sp3KPeEUHasVKCHlFKpQ3EOkfJLdn9ONbO7HDDrSuTGcBD4vmpeGFCxwQEt2bPaW3fwJx40Nfs7ja0RGY4zXlNOvDeZOl1V5K2RWw4UAUliLyA-t2WcC2AIBxYQZZftdxvMgrMml3bPs1yAQp1P4fAoxzye25mLGWmq5NlA5XtHtnrkC5uV2k5r95wx56cjWDSqdfPTMeBaUI2EfzvooRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
محمدمحبی امروز به‌ایجنت‌ خود گفته تا دو هفته‌آینده‌افری دریافت نکرده به استقلال برمیگرده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/24612" target="_blank">📅 16:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24611">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9BcLJDYjDEieQCSTxXMquzIDqkYtckUrxar7W173a42EykiWxHARE_qrATRyE0abowfh7Z4XINWJRi-V8KoLDBp5RH8ynjrOLmZ9BNbeHqMweMXZNV3ge02rXlG4NoO3MrRtzeailSAgyF_9OnFsYFYp-kSvJ6k8I4SwuaAIqk4QSlJq81EhKSCDDnKqSDdIYAibtiW8Z6-zWaMVvQvtlFB4-WtTKsqMo0pAr4Y1GMiBQO9S3UOb1OluoOUKmJOVTJ3OVn7ixcdywynBOPGooQAJa9CuGI6zXQvQWdqqPSwzRCjMwFF6QHct0GVW0suAAFbjazh8Wq6MW07ESZEdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریتزیو رومانو: انزو مارسکا با قراردادی 3 ساله به عنوان سرمربی جدید منچستر سیتی انتخاب شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24611" target="_blank">📅 16:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24610">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jUX0tRd4MCovODNxLfXHE_8Ktea0SKPvS8PFQPMQj_Q0OOEx1yFVG74OVaQs0r9gO-PjeI1itlgfISsiIHDZw6Gvse4ilSvkLyQkiH1-9tXb6EVf7emrby2iAW3T8YN4CHcTOuQI6up6AZNjRdxIncKfn9tHA5d5HUXLm97Ygzydgu1Uea50g7bXQzwaAyhK6jepTT7KiEWas6-tXYHkOI9xJRv_VGq-kd1xnc2D3ntPItAI1XCl35o-LsvfDXW2blTZ0c7b8EN2O1zXJl34Cup3Soz0UaSp8AiXHMitF4B-7Re-ZwfcbvhG_QnmT0gwXW_f9WnqxKYt7qCyYEC6PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
باشگاه رئال مادرید رقم فروش ادر کاماوینگا هافبک فرانسوی خود را اعلام کرد: 60 میلیون یورو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24610" target="_blank">📅 16:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24609">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c7c83867.mp4?token=bW6r6TG5Bn2aj1ky498wzlmM6p354JAnOTx1UfYPFyjgnLbkuZydwjaPLo7KoAKpBP3HDmZ0QUKYjEXp4KskpDLlgX_hm8Vi_vlUh74PVu6Wj9gbRgTZ84TNr7Xrmu0S0GlAdJHCRLSwJ1tGQEmPgdRPPj-6N9UDsK6D0mB4PrJqqQsoY9sKRPUrTRdnGR7a_KDCcZs2eRw_RvruZt7oyIgFQg7zm0cxHaJ3rjV0BCs3iHVhsO8mXCQwvKDfhcnQlRJUZfXHljkXodug04ligfOEMhJ9aCkzKpTZrQlUeb-V6V1ozuvjDOUdZ2zSrN6dR0vwLn8e69CrEcVxutC4jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آهنگی‌که وقتی شاگردان قلعه نویی بعد حذف از جام‌جهانی به ایران برگشتن باید براشون بخونند:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24609" target="_blank">📅 15:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24608">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQzgWv_TEX2nqwbU8no8sadVq6oPMf_sDKC2tBH1FTypVpAsaqBQkAZ_XX9sA6neUkcPTbciAlk_18-Th8_NWn4FSVXdOinx3AfNK2ft1lqgYn85lnTXDNXkimbckU6_emv9PcSnoahoG5gpQkuc6XchCrwU1klwQQdG4BIoQbS-Jd5FXaeKA-yV3AqXdCGRXmjnzL5bPf-34P0eOhQVfgJSSEgkZJXYHccyTLbOArUWA8JiZWWhbVz8KMF0TXnnjJ0iuwnNZToLSTrbD3zoiNSVxhEV-_JJ_CnCp1LWNQfVCrlgxXFr6O8ycIfJThuUKeRHNiZL21wHDEiBT99Kzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24608" target="_blank">📅 15:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rd0gdzoX7N9CRdmfhq8E9Ee_W6UlDIjNcZrnv4yA3BwuVWFBGEgKFnylQkXWLateR30cnDkm-tCM7L3E_55rducv6XCZ86l_uf2y_AG3nvb2cGtiJxMuQx3h-FQQYEDeqUazAgdzRKMC7onuHCeTp9sHTLPn9EuLnx0TYea5ebA2Eokk4RBb-TjT9gImEOrB8SHEAtfZKOq8oxvwaF_VeesKBpYyyTZa3tF0eIAHq1LFQzAYRHYkGj__22lDjyJZ1yLM-6O1bNVgPxO6Xs1UsEeArccSdctlmqgtLguzVsUwmri9f2vefrYM7iL1kn9wpTe4fKZS72hkz4dszMrFZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j_3AnMh198Igvs-6lPiBLhQHfSzsaojKLg9sk09iMqwCVZF1_KK6pSsPR-UEQt7viXfFwcWRtCnksRhGP3BS6SCyyF4-KF1EyEtx9N7pvQjfvYUpnq18cKcJyIntnQydJvueNfiJaQyWzoqXQj_YGJibNRY9izNWFm-xSaIj0tTE41qr9rkUx88AbJ6nTI1JjvZ-w6wlAan7OsMBRy95GpnowyBLpgHuz5aBueipW5XjcmKukh60CjKn9Exx7a6Wlw2umi6UNSRvQkfahER1vnuMRQYUktGTgPmonn1Nx6w6TbwhU5NjHzQx1jKIA8YbSKbmnep6-XmWNd7EH7sVSQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور کاپیتان دوم تیم ملی برزیل: وینیسیوس فوق‌ستاره جام جهانیه و مطمئن هستم که میتونه ما رو به قهرمانی این رقابت‌ها برسونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24606" target="_blank">📅 14:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dYrjefui9H_2rPofJmBKEY67zVfP-v042WKvEP_kjk0iZ6Fi9gl9X7gSROP8dlIjWNG9bTeiRTA7X-SKQLxhmU-iYScMxiXg3wmFB10mGBvHhs9I6tgcTZrZE39SkyZF7BYz0fhxDANsrhBiPRzjn9jWBg-PDuzZVZwYjG2Ngny3LPnVnq8nWypMlWZSGy5RsRJgwXIvuI0Hw3mWXs5m_2Hk-Qjf4X29e5n6LUUdY-Mti4CvOPkn01Ajfnzj8FxYi23k46Pl7cQMWQGL26fMXciop1CE-O7NdlSWDDpoIQ-uqg9A4hMgDQkIlNAA7y60R3i76M01GqmUWtlMLsvpKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این بلاگر و هوادار تیم ملی اردن در پیجش افشا کرده یکی از بازیکنان متاهل تیم ملی آرژانتین بهش پیشنهاد دوستی و رابطه داده که او رو بلاک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24605" target="_blank">📅 14:38 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vz4kXQNYdw3XTptJXiFkDikukCSV6XSfe3XP58-qncnZcUtRETK2vZvltl3ldbmmj3HPiiYgBKXYo7xflvGqWwujcwZfh-yHQvnsxvzjAyW9pP14URKWuRdMpoER8wRAb--DwryQTree384KMtnzM34XiGwvbpFJ9aMykLhvEoLuu0rCqPZMLzpt5_frlxFiw9gtF0RHE9uIt6UKjDTGflpoUEKspAs0wUYb6fHTr85QNotzZzTauF8I_buNm6P8-s8-JoIJx2_ydjQ22flb_WqHpTXy9Nnmu6qmwVMCL_ob48X_YGDd207g8tngqJ1DLfmuGfxawQqmApBDh5fCeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
مسی باگلش‌‌به اردن حالا ۷۲ گل با کاشته به ثبت رسونده، همون‌تعدادی‌که جونینیو افسانه‌ای داره. لئو به۷ کاشته دیگه نیاز داره تا این رکورد رو هم بشکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24604" target="_blank">📅 14:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTCi8AzIM_iD98uKoX0q7aqbsaKwOB6FwUsPA5YnyY69CMVIHBuyOFQCKvjY3eZsJrrZwCTehXHcKgtREWVfsH39KW3ovo7VSy6MTT-8-mIqfxfCyD8_4rFRZO_EkzyZkdojbt5Eala0RSV6NQj5P66cINk3ndMsCJqhgWj-YDzvGyLian8bTBLVghm3JOiVlbtSAWo0yTEjiCRZF-ylXGepdPSZhQT_DnEeQCKw9cTAZjq15_IvPAqQ-gxloyPhqpopcgy89Tm6R0Al51J0H-bxpOtMxVbZEdTq-jfnFcBhTIiTNfJK2gMCAoExFXbxm7nUKJQairoi3BNDyUesTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24603" target="_blank">📅 13:46 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24602">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=T7pyYgYfnhCWIYAWuLoYrXMqoR5oRcMtsiBzd3XzMNAopIeTZTiJYePTDamLGWCyM1v0gHWhZV4qB_BR1Qgox0zP8r0KwTfgHa1SjDiGE1i-mASIW07l5a4XdjHEOcBcUW9hxTCn7eB3Bm53e6tLemzbHhPgkC3PTTe9AtP7mqR85pTCeYRsJjbPoPXBw9reIyy2rctRiBKnRxaDIpuLY0CnzcnKHRwRNMfkMNoYccBrBR5Tmlja7GhZ04NjX-9n9ud0We1bWI6XR6rxelfrSMHRPui6f7tPxQGrLORQr1Y16M1InrrDQotmMXpFStZqLy4uF0-5m8z90OPNrVDLy0okDoIVDcSlszNZlHMrtpw6rI5cg-IxJbcHVggN6P2C3S31N8LpsXeCFAFR7QR2eoy8h_Z5vKOyoI63TDnXTEwl1uohcjRQ8wAqeHJaiZoNCqha08y0xdS7rhVpV_Q6WmKPBe-3TdIK9w6ZQ1j2VsjgeVip6vCGhG_CUknM-5BNSXVAdaREH2F9WQ0EhWNAChXt4EgWPyjXZlwQgXt1OrT1ouE8vsjulpqUjNLBqtAkhHjlBOPEiv-oxwY1cW3i4v5cQFPE_lGldZC-T6sw1MpyHP07DV6nGZrUyBVlew7vy-VoAO-UsRbLgxobtvSZ9vBdo_nVssoJhAgknoYGVGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2df383dff2.mp4?token=T7pyYgYfnhCWIYAWuLoYrXMqoR5oRcMtsiBzd3XzMNAopIeTZTiJYePTDamLGWCyM1v0gHWhZV4qB_BR1Qgox0zP8r0KwTfgHa1SjDiGE1i-mASIW07l5a4XdjHEOcBcUW9hxTCn7eB3Bm53e6tLemzbHhPgkC3PTTe9AtP7mqR85pTCeYRsJjbPoPXBw9reIyy2rctRiBKnRxaDIpuLY0CnzcnKHRwRNMfkMNoYccBrBR5Tmlja7GhZ04NjX-9n9ud0We1bWI6XR6rxelfrSMHRPui6f7tPxQGrLORQr1Y16M1InrrDQotmMXpFStZqLy4uF0-5m8z90OPNrVDLy0okDoIVDcSlszNZlHMrtpw6rI5cg-IxJbcHVggN6P2C3S31N8LpsXeCFAFR7QR2eoy8h_Z5vKOyoI63TDnXTEwl1uohcjRQ8wAqeHJaiZoNCqha08y0xdS7rhVpV_Q6WmKPBe-3TdIK9w6ZQ1j2VsjgeVip6vCGhG_CUknM-5BNSXVAdaREH2F9WQ0EhWNAChXt4EgWPyjXZlwQgXt1OrT1ouE8vsjulpqUjNLBqtAkhHjlBOPEiv-oxwY1cW3i4v5cQFPE_lGldZC-T6sw1MpyHP07DV6nGZrUyBVlew7vy-VoAO-UsRbLgxobtvSZ9vBdo_nVssoJhAgknoYGVGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24602" target="_blank">📅 13:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24601">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/frgwFgQPS-R347xA3G_iLeNpXgrzo9HzJckjN0ZlknJsoevnZBbzRfRoW-xT6bGZ90B-uWtHlVhL1avgNkVL53z3YZ5sqczdGFA1ms_KZ8lP8yhyzWWG_ql3tnqx5q3J-ANy_pb7pC03p8aKqqt-mbEXM61099JbCHLj86DJjmjh3sd-Akp6gU5VMHPYZi02NPnf5t46deS8fg5Y-uB6eNBw5FXm_O95I05Nw6kQ5I6i8ZAY3VDlLN43bRHuIRXlpBgVp3QiEsjkOGY3vfKv-v6ohjSt0zRd8kZQLnWGC40kvW4MKRmigbpQ-3B2XDE_iy9rc4C7tH_Fs2ZP052Z5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24601" target="_blank">📅 13:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24600">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=lMEcpoi3GbaAfNjmXHB2czP9uWxMqBafxMvNqYGyhfsGiaymhktpvXU-AXDVF2afoIv6IB_82T-wqQZCxgIkD1hLsTtg3X41ixTQ56JzvQZqlS4Ala41kJ6abVMhWvNWNov5r-B9DInHImsIXeKlzksNo7n0dMvVtpOVPLWqGAIrSKyFTbcALXuWPCuj_pjs-ndYr_KA3LCaZ7aMGTeZy4oXe1qw6ZYvrzq2YSTORrXKtQptrCrelSB3agc2ZretiaDMwf34jSIA6CATWZB8DdJwslO2-d23xqYc45Hq_t3o2HBYygD8x133okKODGtYPk80TMDKbFLRir3CG_27SQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/268dcda4c9.mp4?token=lMEcpoi3GbaAfNjmXHB2czP9uWxMqBafxMvNqYGyhfsGiaymhktpvXU-AXDVF2afoIv6IB_82T-wqQZCxgIkD1hLsTtg3X41ixTQ56JzvQZqlS4Ala41kJ6abVMhWvNWNov5r-B9DInHImsIXeKlzksNo7n0dMvVtpOVPLWqGAIrSKyFTbcALXuWPCuj_pjs-ndYr_KA3LCaZ7aMGTeZy4oXe1qw6ZYvrzq2YSTORrXKtQptrCrelSB3agc2ZretiaDMwf34jSIA6CATWZB8DdJwslO2-d23xqYc45Hq_t3o2HBYygD8x133okKODGtYPk80TMDKbFLRir3CG_27SQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌مناسبت‌دیدارحساس امشب؛
24 سال پیش، فوتبالیست‌ها رؤیایی را به‌تصویرکشید که میلیون‌ها نفر باآن‌بزرگ‌شدند؛ نبرد دو تیم ژاپن و برزیل، جایی که هیچ چیزی غیرممکن نبود. «رویای ژاپنی» فقط یک مسابقه نبود؛ یادآوری این بود که با باور، حتی بزرگ‌ترین غول‌های فوتبال هم شکست‌دادنی‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24600" target="_blank">📅 12:37 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24599">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s1vHCSbkKH7ex9WTrod9izafbcgQHqeQ45im1l4PvB3x2L6vvp6_kFyWrnlPTZaxucpom7_M08iDHV36335Bd081igmGNx1WqdOjf82M5Ig4HfkkeXQhSDV0-35BXoxMWMg7rw8aOWyGlnqUHU_bQoBe4BRgDbzaNEp-A8cizFoqEmC1vJzhirdzXIA2m10nkyzf0m0vKJ8Cy0r9tHnIa1OxmYyAk4vT-L4DisHpm5AvvmINcnsx1Fxq_OZ9ELElJZ9uyirn5remEJiA4l9sRsiIetlpl8z4H3QL3aX60doA24gphoCqN_FmgTguzJfpc-U7MvQ3ZWvMqA70pmowGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
خوزه‌فلیکس‌دیاز:فلورنتینو پرز رئیس باشگاه رئال مادرید بعداز فروش نیکو پاز به کومو با رقم 60 میلیون یورو به‌اوقول‌داده در تابستان‌سال‌بعداو رو به رئال مادرید برگردونه تا برای کهکشانی ها بازی کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24599" target="_blank">📅 12:23 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24598">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PlPRd1-njEQJNYwYULsIO-GFJL-xZI9Mioi_EsntMYc7JCnCQ1MQ5_q0p6uRR6jJcApoBRgKl-WyH_CpiQQJhwhHJwaJx_gPO1tOxSeRqZ8HDLmf29H_0buPSg9ZnebpOkWU8ywW5v99J8gzfOfZWUJdda34KVXfSifKHdfa0_ixaexjtb3GBPKqLJHfv3EueFZrPSeo7v3tSHEatPQ316Bx4ga3LASwXfbDOFiVsLcVYOkCamDX6tdAbGxeksbmF1nrOWvAuucLVVLilpgc5q41Q-BxRl-3sbfZaHczNe02GopbjrExp21Muz5UInEjNBtU18GOgvH5fEm8pkAgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛
پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24598" target="_blank">📅 12:06 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24597">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GK9A6kqSIw_XOCy642rfdVxHYZQwAMkmFtEKilf-K7TmRk3P68Rs0UgIenQpSgw0Q-7uYYg1uAntkwLgX_0SUqjpd9XSgurCAKAEhzdl0izoW4P5M3tmZPu8XCCpLZ_-SG9KB9A9_9ET-gbRc7_5Ma13-4_beAuuIR6JWXbkCNilClpdBzOJmDVYWFyCdICDPRvu9YQHBIsAGR-x577ABDuD227OhoqXjwHarJjJH16VaagOlOLtoa-VhPrK1QThGjjU-CvdXVwMlHT5lC4_w3Qg6qXKZwU-XyAv2Y_YbKEUj6ZydQDAGiGaS0OU00tZ8uBS_9IPLbOGw-cLLkskTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا
#فوری
؛
طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24597" target="_blank">📅 11:51 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24595">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1UnNdStfMHmWlaH0wyorUqmQE2A1LVJygZWU7qJA9Xpz-ii6DGkiVVabKzq_iPNH9KD3Ny58cuSxbflo3u1M2WiYeCPpzO0QlnBWta3QpGeiBos-oWk5UeShECrHNej8SLbtUnRIDEcEoUXv84-6zW9UBnvv9Nu1GvTzQbC68AmKHWjnngk3C6xeNTpp7TpQKlw6mUMTgdB87LZPb0egCk7fpyzDSdoXKar_qH0AqJLkLWEIsa-FhJ6T2ZhxLcvPWTfohM63QgzsFO_jt7BGkbwK5ta81Liglf6uzwIDG9vePPHxNPQ7X8x53FlHtTb7_Qsna7GqLrMr43tfej7cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛ تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24595" target="_blank">📅 11:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24594">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/na_K03kG9D0q6FoJLD5boFvpv6tegOLf4X5wEWHuTG2ri9csGdm7P6IWm2NG-zvznyBB0I24-LUbVnU5WkWOfiSPgas9SFqoV6mHisp9cYooXduiYXExkkvTi_RyNRSIleMSaXM7xYu9MpTmNvt9FIIEa9wfotgG46APgsf10n6Vc_otDN_NDYJsl5l_K8AbL29IJ9DG9zmLZHdAzUKTWSGJYTAdJHlr7rfFh4la2mVvGVJYpj-3_O0KsbZ_9XDBlryaMVI_poIeDaIoCreEYxjLAWDovfeGA8YqjBwi5ixDi1ix_Ndx0bu_JpMIGStb7UBBWbPhB3F0ISMmPVxIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ باشگاه شباب‌الاهلی پاسخ نامه باشگاه استقلال رو در ایمیلی داد: 2 میلیون دلار نقدی پرداخت پرداخت کنید تا ما رضایت نامه رضا غندی پور رو براتون صادر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24594" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24593">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/maxbcQixQrU6BuLe1MRIXxMRLdP6jq6XX04MJgDlmGPJdk0O6GBzaI_fP7YWCwJAis13YrMewpULdhOO38qDITJGXlMTz03pnDu-kfw7jldqm72rbuqSrkf1aRPkF7WgIx8Kd9I0Pbhl_ildqf2HcHwKbR33Dvhze8AJinTBTgOjiclZolHPH19RCNAd2EQNjso7gUXxL5PjbKNgqdBJQ5CF9GUiKgufhR788T_RZHnaKPWBawSesKERx0rj4LvtEbZ50Zw4kdaAucd2QZ3x6GoRceJ3B4ugNQxsvqRHMwGOjgEMxJKLJpeLuJcrwLyZnm33dE_m03M27G-XDb2C-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟠
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال در تماس با مدیریت فولاد خوزستان آمادگی‌ خود را برای‌پرداخت‌رضایت نامه یوسف مزرعه وینگر چپ تکنیکی‌این‌تیم اعلام کرده و این بازیکن بزودی با عقد قراردادی چهار ساله به استقلال خواهد پیوست.
🔵
باشگاه‌استقلال پیش‌تر باخود…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24593" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24592">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=O2rnsbsHgTXtR0w-UILTQ7ZPukY7FycM_GnpYrXG1csd_bz36ZZ8DZBhuQtuOnrUQaFPehMffVOiLz-VYs1tATCgd3Dige3IjKVYypALOhMdnK5XvV3JqbTQPiDWAIs5iK4tsgQJVevQJp2xoyQhjMlRfiPgGpjXZ_iVKpGoiIeGATfW6l1fuol8mRL-2RjUkJ3h908wYzHQ7hzdYtS0906YwRsQb4-jvRxigKoDqAom32yksd_rKAxrTU5ZxQCkBFnvQWSyVTofZqVHUMlbJYukfRL6a1ND0rbVYLy11u93gUYhYJhsYmYYwHX4h5duoHVqWRgHIGpn-fYfqpjvVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99ad96741e.mp4?token=O2rnsbsHgTXtR0w-UILTQ7ZPukY7FycM_GnpYrXG1csd_bz36ZZ8DZBhuQtuOnrUQaFPehMffVOiLz-VYs1tATCgd3Dige3IjKVYypALOhMdnK5XvV3JqbTQPiDWAIs5iK4tsgQJVevQJp2xoyQhjMlRfiPgGpjXZ_iVKpGoiIeGATfW6l1fuol8mRL-2RjUkJ3h908wYzHQ7hzdYtS0906YwRsQb4-jvRxigKoDqAom32yksd_rKAxrTU5ZxQCkBFnvQWSyVTofZqVHUMlbJYukfRL6a1ND0rbVYLy11u93gUYhYJhsYmYYwHX4h5duoHVqWRgHIGpn-fYfqpjvVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شمامصاحبه امیر قلعه‌نویی درپایان بازی امروز با مصر رو ببینید؛ از اول‌تاآخر این مصاحبه سم خالصه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24592" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24591">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xx9Ra6kKiBwkaWzvnHivRHbyIZTioI2w9bdUszqw4NTMvJwSEQH17Wt7r3t2BihYaOrx3dOe8dMBC9WnDlmU6942mn6ze3RyQ2_Smpf7BBZfIDawWc1LNjkE4jmto46jT00GyqCeQ8oTKMGKMaQLA5ELPNkphRkPU8T_6wE8DtWPB7S-q6L2aBC9Gl48iboOsv5zuoFSxifwXAieSfMiEeo_tzBLCg8XTFbHusqdV6mGvy6LA9I2fMaTUSSF9McBf2rAzZ8C7bj-vDZCCmkTmyvgAtcNBS7WQggQvRMnaPoaYF2XvpeJlUlrLv9Ntt57pZtrtnwi3mghy8lYNtgZ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تجربه پیشبینی مطمئن با
🅰️
🅰️
🅰️
شارژ اضافی و ریسک خیلی پایین در
#بت_اینجا
رو از دست نده
❌
🛍
ازاین‌لحظه‌به‌ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان شارژ میده
💰
🤩
🤩
درصد برگشت وجه در  صورت باخت
⌛
همه بونوس ها بی قیدوشرطن:
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r8
@betinjabet</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24591" target="_blank">📅 10:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24590">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v3Vg2qFuYEcCkCjT_SMMHaQHO0WaKt_k8_GVEveRIDST8djTJabC9UYXEBT1fIKCtyFeo52KzaM9OBn8NagEDqKXpZxvrTywu_sjEto4yYH3w0zpXrMGPhTWVdis3fnRTe3vCdp0u5aQFVJx9inVrdu2QVXZf8J0YLMhlPu6uRgdJ876vvg5THZaQ7cerU_Qr1UafQFEKe2tN7t7Xuu9MX5xbK05R9D5GXry_QcyvCYwOdKOj5M46xjdSFiAHHZvPbR0ggVgQSqUo7Q2hubFFBetNTVyBpF1bKsLGINdP4YSHTyzUYWF1q08fCaEl6CCzdKWlO2Tjk-weqUCrQE91Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رسانه‌های‌اسپانیایی: هدف اول و اصلی مدیران بارسا برای تقویت‌خط‌حمله این تیم خولیان آلوارزه و درصورت‌پرداخت 150 میلیون یورو به اتلتیکو قطعا این انتقال انجام میشه. حالا اگه یه درصد این انتقال انجام نشه گزینه دوم بارسا هری کین 33 ساله است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24590" target="_blank">📅 10:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24589">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2RPbz87fjKGrCQGPVO1bRHhUOMCo8dMAoydxba39tjomewR0XGtyKj4N0b0zLRhq2U1mQEEeVv9f9jqzKKG8pMtqLqHzSC90m37mxqkLQ7bx4eqSO8SkLNDRQMpgd4xF4wYGl_iWKXZhl6KCOKFg4VWA9T2sKGIoGkdNPE1K4-mn2mNRhpYBDlW3hfirHchFEUbUShoUWE0sSYRi-dtZOp5rSdvdARksUyOxR7PLtkH_ZPr8Ey8QQZw8H9CWvsxi0lOsE-8Bs-5pmrlukiDn0Gv-_RRXw9taZ3kIxeqOod9LWXiySP_ewHDLt-WWCgh2nvn1B2lNZpjW6gbwz6TDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
پارتنر آقای گابریل مارتینلی وینگر آرسنال و تیم ملی برزیل که دیشب فرصت بازی بهش نرسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24589" target="_blank">📅 10:22 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24588">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Trfb9a6u-V109RTNNhZtPGIHQMj14Empm2dvzaNKjDo65YFWr7hWiinEnBTCDA43j3FI9Td-w8qFzFEuDUTBhtMGfvEfjUJEuV-H9tWG6MooM5hHuN6Xg5SrZC-UxHsdJT6oqIWhQjFZ_tCssGatkYSVhL1BKR1pv3C_JHNZaXYCJsnH-CpyHwVsi4kgFYjLa-5AXZwzjfOjDWeVxaaXrO_Z0rlolvtchr6bpqtDMVVNveuz1vGvVwQVCnGFV0m_jNNJ2LNxk5qyPCtBKme_uhcHSGzTZhAku6oqyN5SgaLhOJUPbjTVJmKVwiyUmVPu1PTmJ7vZVNaA0bx8QdY4yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/26bb073d91.mp4?token=Trfb9a6u-V109RTNNhZtPGIHQMj14Empm2dvzaNKjDo65YFWr7hWiinEnBTCDA43j3FI9Td-w8qFzFEuDUTBhtMGfvEfjUJEuV-H9tWG6MooM5hHuN6Xg5SrZC-UxHsdJT6oqIWhQjFZ_tCssGatkYSVhL1BKR1pv3C_JHNZaXYCJsnH-CpyHwVsi4kgFYjLa-5AXZwzjfOjDWeVxaaXrO_Z0rlolvtchr6bpqtDMVVNveuz1vGvVwQVCnGFV0m_jNNJ2LNxk5qyPCtBKme_uhcHSGzTZhAku6oqyN5SgaLhOJUPbjTVJmKVwiyUmVPu1PTmJ7vZVNaA0bx8QdY4yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
👤
صحبت‌های‌رامین‌رضاییان ستاره استقلال در دوره از رقابت‌های جام ملت‌های آسیا و جام جهانی‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24588" target="_blank">📅 10:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24587">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=qy2yVeqOXotJ0SggUR-o5_R_HQadw_z46PZqoSPITMCPxw1HsjSucNu80kMyLpqph4D3Zcl_a5mM7dMgjntOuNf-teZqjRJRXKIKgJKELdZv1kLN3alhpMn1DORY8Ot9AVLcoHcvjCxdv7gaWK05_KF6oloe2wpaZu-0TZKGWDI6qPb6obRiPvTIiWEMAAeDTjWokHOpRF0nB1NNFS4e9Q1qCqC38AugMOiXPXODl0sz0nZXl9Lpo1ob9a3oz8ZD53ngDc246WmIxRIcyZV2Tx8w2ryoULwPWpVfi628W1F2wPSKv-2RG7h0VIYwBpKY99rToNnjaji8XveT_Yc6qIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b1c18abd6.mp4?token=qy2yVeqOXotJ0SggUR-o5_R_HQadw_z46PZqoSPITMCPxw1HsjSucNu80kMyLpqph4D3Zcl_a5mM7dMgjntOuNf-teZqjRJRXKIKgJKELdZv1kLN3alhpMn1DORY8Ot9AVLcoHcvjCxdv7gaWK05_KF6oloe2wpaZu-0TZKGWDI6qPb6obRiPvTIiWEMAAeDTjWokHOpRF0nB1NNFS4e9Q1qCqC38AugMOiXPXODl0sz0nZXl9Lpo1ob9a3oz8ZD53ngDc246WmIxRIcyZV2Tx8w2ryoULwPWpVfi628W1F2wPSKv-2RG7h0VIYwBpKY99rToNnjaji8XveT_Yc6qIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ابوطالب‌حسینی درباره بیانیه اخیر جواد خیابانی با زبان عربی برای الجرایری  ها؛ که گفته‌بود تلاس کنید که اتریش رو شکست بدید‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24587" target="_blank">📅 09:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24586">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=V1xkx_g6tDAshpe0yxPDbpGNchF3sXCer-vVeMRRuBN2m2t_Hgjwn-To-azlYSuySkvWXGzE-3N5_M4JZNje25TkBC4BTZsHiPxWDY7Egi8yMcIzchJ0hCNPgVPBjHSCscjMMZo_4pjqT_zAD_tuRFQlI3rHN_tsEknUIeMYtI-N6TJpG9tcwDfXykK26tAa4hDnD7ieTUXalo-av1Nv9nNy_UZgK1RqjFtmL4a7bXYlotw_qpvmfCnOjQQPo7iwmzLvOZqNlDJiYAxlxJmCJj0cLIq7ItE6jDmq2BThmudpDyp-_XpJSivaIQR93hJs9JOdpJlBfEnj8heddvWdAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa6f9110a.mp4?token=V1xkx_g6tDAshpe0yxPDbpGNchF3sXCer-vVeMRRuBN2m2t_Hgjwn-To-azlYSuySkvWXGzE-3N5_M4JZNje25TkBC4BTZsHiPxWDY7Egi8yMcIzchJ0hCNPgVPBjHSCscjMMZo_4pjqT_zAD_tuRFQlI3rHN_tsEknUIeMYtI-N6TJpG9tcwDfXykK26tAa4hDnD7ieTUXalo-av1Nv9nNy_UZgK1RqjFtmL4a7bXYlotw_qpvmfCnOjQQPo7iwmzLvOZqNlDJiYAxlxJmCJj0cLIq7ItE6jDmq2BThmudpDyp-_XpJSivaIQR93hJs9JOdpJlBfEnj8heddvWdAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
فوت پسرتازه متولدشده کودی گاگپو ستاره تیم هلند و باشگاه‌لیورپول درکوران‌مسابقات جام جهانی میتونه بدترین‌خبرممکن‌برای این ستاره هلندی باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24586" target="_blank">📅 09:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24585">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👤
واکنش عادل در ویژه برنامه امشب جام جهانی به حذف شاگردان امیر قلعه نویی از جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24585" target="_blank">📅 09:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24584">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ3K_V7b4UVEFYb7B-_64hWe_SZBOMr5K1a5w9NLkCQ_HXaqKgZ2ip9j_iLrtmLKQqZjZQY29bgnTYHePM6DzG2hI3fYQ4GciId_8tNy9JXT3s6XLmjk8LRgeZv3JUXiME8cMJWWL1jjQyxzB9oitPymtQt9IyZ8tl9IrBK6N4FxrWmW3g5Epxxt_SHS63LFJxXtqbbR_wKz5a0H5qMQquJ7hAqgb5kjNBIDfOml5SGUCw-2Kll8i0gtsC50q72mg9wnPmor_xxpaGbS0PVXIGDpzebRH7M5TmmLPeCCnVTpgxGeXfgLTj7J3zzH4s3ziC76_cBeLaTUP9A9d7EVCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24584" target="_blank">📅 02:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24583">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkCHhYOeTUtcNliWOJaNWx8yb5NrsKb_g1dozBC7glu_SxffxoJiqR4w3ihdWKntqzJhb1hYnyLCPQlyiOy2Gx0XQnWda4okRzoBJn5dRJG1vIpfRevFaUGW_qFCweM-dJ4eJuOCnBGauNjKigUIbPrGuuZIpcgVswbASQ_x4Aqw8O-XIagde-XxArhiG-efyQG7V5eeAWjVG91pHr-vH4Aa0zODaTDarJsa2LP9s21TwFr4eQz5xnp8R4KhX7ipZHTXsckIAUtTAHBdUUbomuSdERdTaehC7CFt54J1JcaDPCOm3IUyJB-jE6gVEPZlO_t0cIQIZSqaTk2XEq0a1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
رامین رضاییان با گلزنی در دیدار امروز با مصر، شمار گل‌های خود درجام‌جهانی را به عدد ۳ رساند و درکنار اسطوره‌فوتبال‌برزیل کافو، به صورت مشترک درصدر گلزن‌ترین مدافعان راست تاریخ جام جهانی قرار گرفت. رامین رضاییان: ۳ گل؛ کافو: ۳ گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24583" target="_blank">📅 02:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24580">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j50smWJ72YskUhXyXkAs_ocNJgYtzPU7UMwH26NRzAtTWc50sH-lg6MdQDTfxcBTUVFjPKhpLD6ZH-T35DVgk-94ibXXItt4JPMc88Qdk8ijgu-dsaIH1RmLeaGof2oASpJVcTXqa0uC0oB9PHgcPjBHqcKmyeQ1lGl6TU5zUP_LEBHEJDhV5Wi09WkdkcaVomtVAcdMGkC3laaVfYZoDGtl_PWHW5YupzSyGI4pOBIE1yW4QU2O0jXdTxWvbx_YQRcvEM6uCv8j2VAXu6YzhIPta9_-Eg7UkOMhDlEbyBS2R5mBt_tCL6T0ohx6T6qwMC1frU2ZR7MgJDSHxOC0Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دو بازی، 36 سال فاصله، یک اتفاق مشترک!
‼️
سال ۱۹۹۰ دیدار برزیل و اسکاتلند درجام جهانی باوقوع زلزله رودبار و منجیل در همان شب هم‌زمان شد. و حالا، تکرار همان تقابل در دیشب، هم‌زمان با زلزله‌ای بالای ۷ ریشتر در ونزوئلا.  اتفاقی که بیشتر از آن‌که نتیجه‌گیری…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24580" target="_blank">📅 02:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24579">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQI3SLOomzPMcpPuzkw-fcbKypAwpDg2G_YBfp26hZ9UgtCUcwv_dVtj_zFITQv-8ar4eb56FuhMo6X5MODg1Sy_U8mZnGAhKmHAzRKZ97dFjuR3BMeFHNJiJF5kItqaFoweK-VSRLsgUd5CYF7z0S8lKAQJ-kznb1PYY-oeiO-hVvawd9dnDQe7DChS4uPYTaCHy0xigH0MQiqumgPqUnlI9uvYQfo2oEJWeWaNDiDB6d5CUD21uy9FDlUsTjDHldsu12ZexubagyE7CsTAm8ulS6mlhF6mJ8gDKFnvkE8sU6KeI7l8Tur2DRc_AmkmJQOfGinFJWqusE_8Q485Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/24579" target="_blank">📅 01:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24578">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qelPl_pbtOmLSGayUoyxfFbzevWP6_TqAl30lBWp9dz-gtkeI2C8X224XO-H98zVuDocJw8_7WKXs6bxH-vx8Tcl2C_s3KAkIdcqmsrwGSHsHiIHK5rKmJ2cfY1RPvTGeOLOGXRb1GR9XWnOT_Jg7vig2N3dMSSlJ8B8ZGgTbbZyUEUazlhgZvfD163lwl5FPT56LVColmOIem_WLSrxjwodYWrFA_wQiHg8U_W8j2hqLgLu6Ga54By-JSa1iKZkAdK0qMkEFxpdC0VOgGjBE3G9MHuTV9wBu1l-j7PprhQ51DI3-Iju2yv6zOwRAIX9sUa8MA652hj00aiL6BW_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌ دیدار ها‌ی‌ امروز؛
تقابل‌های حساس دور حذفی جام‌جهانی با دوئل جذاب برزیل vs ژاپن
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24578" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24577">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPp-jmvM-or6oeNk2bYBTuUd1uWAO_gRYPA8zwxWaYGEswGIvFs7zNoOLLl5LKZ__ENQJvw8E4wjNzB2Kw1ktH0pZOSWLbCCNTAQcMdAOAPg_GXIcaUrMGI0qYJWs0I9zo_3wFv5Loc3j7joZpvwJhmG_u6yDcjek9kNSSwurI2-C8OJ61c_fKMygYMcsrliZrRuoSfZorw4GdM0jcZSYYtFQEwNCzmQpLkn64l4_qV7BvCQaHMHmLCmk4WAbbysd0b-lZi91cAc9iVsLuqFZ8eDDtMD9l8z4ptD2mn2fZhU_J6TF_W989DFpEUfklBjvdNymX9-JaEx_-FAljycWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از توقف بدون گل در جدال کلمبیا - پرتغال تابردآرژانتینی‌ها درشب گلزنی مسی و راهیابی کانادای میزبان بجمع 16 تیم برتر جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24577" target="_blank">📅 01:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24575">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6p9BqhIJK4MEPVPNS7sbSFzAN6CTMxnWWIqhsrekl_x8dCuELIc8pn7Sy4YQbWN1RcQ9KkXKCCg4MegZam5oaCJzmS8hwPQULoBOakb7NqRVS3rnf200RdU9k1kI4Q6kOI0WOn6RyCweoUOBn6u6ySNFsnSk21NZNRHLz_nq2x2ZZ0QgVA4tIpePhUdGOSUlMT0upYfCEdZxK9XFQdbR_Dy3cDpZIyuqt-Ko8my46z7-2f_4WN0Y7WQX6cO5lDGdWaSHaXlSf6WkaAeZa04l4h9us9SF-5QS6uK4ntWHFteMyeZOLEfsp9NC3buU9d-mCOfTq7oy3dPLCdAgqTq6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24575" target="_blank">📅 00:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24574">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=GoYDq-11X1XzPKSrrB7cuwp8Nx1E5t0Ghrxae8Vz_CEt8E6H7Bdd5V-0FX5rEJczDKdCwbaQ9lDSn2FLbODxW4g2mnsEN8vJq4KD7pIo0Uy7PRi6KesfnWABbDkvHH8_1AEsCc6aYzU63onAg4eY9FPebUL1N7HgNway0n_CRjTdQGvqZtEGkxmsVaz-sXGY6OJLc2j3cfV9uc4Zy7rMvXYP-1bsmNvx7VmsMWt8upMcmxP-1SmzofUNTxyton3MTYS5Br1-UMCBve2YSCePygNR5fHSchYqkb61m-2wp-tT0mXHUZGg3mjjkGwDVfvDga9hojIa1k54bsoncsrGIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b80d476e65.mp4?token=GoYDq-11X1XzPKSrrB7cuwp8Nx1E5t0Ghrxae8Vz_CEt8E6H7Bdd5V-0FX5rEJczDKdCwbaQ9lDSn2FLbODxW4g2mnsEN8vJq4KD7pIo0Uy7PRi6KesfnWABbDkvHH8_1AEsCc6aYzU63onAg4eY9FPebUL1N7HgNway0n_CRjTdQGvqZtEGkxmsVaz-sXGY6OJLc2j3cfV9uc4Zy7rMvXYP-1bsmNvx7VmsMWt8upMcmxP-1SmzofUNTxyton3MTYS5Br1-UMCBve2YSCePygNR5fHSchYqkb61m-2wp-tT0mXHUZGg3mjjkGwDVfvDga9hojIa1k54bsoncsrGIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خیابانی‌این‌بارگیرداد به تتو روی‌دست امید نورافکن میگه حالا که‌اسم بابات‌علی اسم مامانت چیه
🗿
😂
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24574" target="_blank">📅 00:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24573">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcZTM9cPWm5F74ODCAWOPuRYXGkBt4HV9fGcNC0_Ew9qpFwyRW46gb5POsRROP2cwNRGlgBggX7dTF66EbGzb43JxfF-6LyjcDjg3MJq3mwZRsOaUueglcYJ8w1v_l77xft3auMPmw2g6P7sSpvtjfmnwzLN1QNxhnqODzSzxFGadN2h3NmDhKL0zWT20Cnb1fkv6DbpnN1CjrwTnu9uAoZylBFgxPNrjBc4ix4r44ybC-5oLk1AmXVUhbcxPuyXqKy5pxY-4OkrJqVO70_xPITdRT854URphMr-cx_Umwmsx6Wz6hWstTmK_f93YcP8LcQBtWXu5-Y6yRZlp-_67g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔴
👤
#اختصاصی_پرشیانا #فوری؛ مشاور محمدرضا زنوزی مالک باشگاه تراکتور که در نقل و انتقالات اختیار تام گرفته با باشگاه اتحاد کلبا وارد مذاکره شده تابرای‌گرفتن رضایت نامه محمد مهدی محبی ستاره ملی‌پوش‌کلبایی‌هابه‌توافق برسد و این وینگر 26 ساله‌باقراردادی 3 ساله…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24573" target="_blank">📅 00:13 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24572">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGc_3nDaj07JSxw_lUVdRneXwbpebnF7av_P8lG7wKRBLz7irZKdJ4iNi57zWKAJlJMiO3eiJrzP2nZpH9jsYM28IMYLc_7Xfw06tFSSD9Vt6uHtHNoEVLoyrEh71j6Gc0VY9gZnxKu8xgtkbCAZLduRxmFh89na8iHhj7CtPEc1qwjWajNVUSrHjesRp2Q_pmR6_OZM_K4Sb5PqspRfrvur9yd2jolrDiJ94d4Jei0agqWcR1-7gx6ZP7GjseiNTC6MIENLiU9JfCDT0Q-KYwspW3x3NB9pdQYwxpAE3DO37GhWT8NYniCBZnzadSXrIhCtCsxPFSEdvp8G9_OO9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جواد نکونام در کنایه به امیر قلعه نویی: شرایط جنگی نباید بهانه شود، عراق سال 2007 در شرایط جنگی قهرمان آسیا شد. پ.ن: این رو کسی میگه که خودش بعدِمساوی‌تیمش باد و هوا رو بهونه میکرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24572" target="_blank">📅 23:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24571">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=WogMJN-UxJ_qnqMV91ddUY2F6pXttU1xOB6mDMfYaYmMvKNtVdabK26r_8kLDiL6y7VTs5tZXHC6Od_Z54LgQTaewqswj-YajeXYToSbXCudPUFouUFxWUvQIAOsevge-USwonnB5lFW9er5jp2jz5IcU-uEtpacnOzUKhYYcVVHW_kP-g8Kwg82tHeXCkMy6z7zqVV_Cku0YHU05odBirEJw8ipbAZp5vvAUXzo2xR9Fzt2ur-pzRyW9O7vspGhJDeik8xOBqLd21Cqy6dO5DPf8-7aJSwkSLOMJgeoehIvzKjidysHcHwHZ1DI_KSrqv1K2gEE8zSmEU8MdrmU9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0bbd868c90.mp4?token=WogMJN-UxJ_qnqMV91ddUY2F6pXttU1xOB6mDMfYaYmMvKNtVdabK26r_8kLDiL6y7VTs5tZXHC6Od_Z54LgQTaewqswj-YajeXYToSbXCudPUFouUFxWUvQIAOsevge-USwonnB5lFW9er5jp2jz5IcU-uEtpacnOzUKhYYcVVHW_kP-g8Kwg82tHeXCkMy6z7zqVV_Cku0YHU05odBirEJw8ipbAZp5vvAUXzo2xR9Fzt2ur-pzRyW9O7vspGhJDeik8xOBqLd21Cqy6dO5DPf8-7aJSwkSLOMJgeoehIvzKjidysHcHwHZ1DI_KSrqv1K2gEE8zSmEU8MdrmU9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
صحبت‌های جالب ابوطالب حسینی درباره حذف شاگردان امیر قلعه نویی از جام جهانی 2026.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24571" target="_blank">📅 23:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24569">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxAiQ9P7N5sP6v22fqPUCjbtmkH5JxRWe9qJhbEMwmDpgaBmdo16cFeFVMxe2twDrZ00n7nrYNMUK9iNS0osrS67_qWK9Ve0FZ5SzP2Qnj4sTjqhCcKVhO69fDdxCm3enSj5r9WIF7Vys7iud8rW2r2qCx0VmMhokrCrtXly4eyer7zPtetX4nM28Gbd8fR4J0dJTL4vElZ39OQwMNpUsuiXzCMJHkvutTLSCgunNTbOC_8L6KADlNCGCbh-wZ5LAUKghxroBrUhWZObg-QkGR2uquzoRnvW5Jx9zx7asEgDou1zvUTAXrOoVzKvGotPBb3Nf7emzJIfY1XLzJ6c-Vvc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c12652e71c.mp4?token=oD-wAPhvc67vs6lOXccJKX1y0h2v2vH3JLY7VpbgGg0QLQTJPGBSsIOfcMfFhs1ViqFn3-78mTDFgl1eqez9Z5TFS90TfBXKRVMiEArprzqLDGqenO22jEiex7BmqeZyeCwzuT8nHIBR_QHiRa8ehoS-39Le96GLU7PGbMYk25Xf_NeorVi3IA2gPYVLznoFdf-JVsmchCIlMxw8VjtxN7bIctrex3RvnQwsJXA5ROfkqaIRs3RGA_Y98q9WozOMCjArevdAkWQO_YrTaQDgYPXP_czAm_v2TtAffSzUeYf18qYlJb9xlq-asg2LW6Q6OD73cXsdZ3nIfRiGqeTpxAiQ9P7N5sP6v22fqPUCjbtmkH5JxRWe9qJhbEMwmDpgaBmdo16cFeFVMxe2twDrZ00n7nrYNMUK9iNS0osrS67_qWK9Ve0FZ5SzP2Qnj4sTjqhCcKVhO69fDdxCm3enSj5r9WIF7Vys7iud8rW2r2qCx0VmMhokrCrtXly4eyer7zPtetX4nM28Gbd8fR4J0dJTL4vElZ39OQwMNpUsuiXzCMJHkvutTLSCgunNTbOC_8L6KADlNCGCbh-wZ5LAUKghxroBrUhWZObg-QkGR2uquzoRnvW5Jx9zx7asEgDou1zvUTAXrOoVzKvGotPBb3Nf7emzJIfY1XLzJ6c-Vvc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24569" target="_blank">📅 23:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24568">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUFO1oWGbpY0Tt63kJw6_jBhELC1syylh-Z4ADs0uDemoz12Mer_60kj7FZ596uPOlqVeElESpOoBRIENv4j8BMMMBD6400LlXAXu0bv4VdMk53Brh6AfrZEFZgxkl0Qvy5QQ8FbCz2PbadaDqBdvrdWBfekIryFzhHNcshjaGO53XJCILDU9kVxcOY-5UhRaZ248R5bTZjI3yiaSV3h7oHyoxZerhLztW4Wrzq1Yzuc8Q9fTXAVq7z1yaeaEX6ya5e3_zyF89z_j3XuOC25IzyfWbM_NbyDv6No9tV-JcsvTS-1HRkljaNLi-fW0tdMIfYGOd7zDH7z1vF-gKivbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/24568" target="_blank">📅 23:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24567">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=BHUuPtba9a845w2UfppZC5FXiZTUoLcdwVpIwedlA4ng9IDzCXby66B2pE5Tq_E3-2hHskGSrFOEdOeXyT54mbih56yMKFCG722mGpvBkl6zVF_w-RKAZDsZBmavQVxiw--hWo0y0LzFvg4fpW4bm9OZv_y6RRvx2oybmG-pvKyTrRRG5QhE9qXVMYHhKWWO-YdGIbTXi88KF4cDSSTKDBj9yIeEmpHwTgZE7T3E3F6xtQvxQ0RbnoeT6zCj0J-vMvYPHdk7pm0STzs4aDd5zNZ0ytNwHVwN0tXODRyGAbqAld6C0YRrcI4s_YzcQ8yT6HN-Z3Z70UG99r1hHUln0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b02328cf0c.mp4?token=BHUuPtba9a845w2UfppZC5FXiZTUoLcdwVpIwedlA4ng9IDzCXby66B2pE5Tq_E3-2hHskGSrFOEdOeXyT54mbih56yMKFCG722mGpvBkl6zVF_w-RKAZDsZBmavQVxiw--hWo0y0LzFvg4fpW4bm9OZv_y6RRvx2oybmG-pvKyTrRRG5QhE9qXVMYHhKWWO-YdGIbTXi88KF4cDSSTKDBj9yIeEmpHwTgZE7T3E3F6xtQvxQ0RbnoeT6zCj0J-vMvYPHdk7pm0STzs4aDd5zNZ0ytNwHVwN0tXODRyGAbqAld6C0YRrcI4s_YzcQ8yT6HN-Z3Z70UG99r1hHUln0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
سانتر خط‌ کشی‌ شده رامین رضاییان ستاره استقلال در بازی بامداد امروز ایران مقابل نیوزیلند؛ خیلی باید روحیه‌جنگندگی داشته باشی که با وجود یک‌فصل‌درخشان دراستقلال به تیم‌ملی دعوت نشی و سکوت کنی و فصل‌بعد با اومدن ریکاردو ساپینتو نیمکت نشین بشی و بازم سکوت کنی…</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24567" target="_blank">📅 22:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24566">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🏐
دربازی‌امشب‌آرژانتین - لهستان در لیگ ملت‌های والیبال ست اول این بازی به شکل برگ ریزونی 50 بر 48 به سود هموطنان لیونل مسی به پایان رسید. قشنگ به اندازه دو ست تو یه ست بازی کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24566" target="_blank">📅 22:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24565">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DUg_uCKQUZ5Iln6ELbtWz1QLeV8t0GV8RsjqF1loke6lVxSWb2itU4noSYlVG2BBJ4X84Mvzi9U38c7UIX3XY_obFaE8xE3sYYzEl3PSIqhLEW9xGhr9p62CZeRCgIj3mh_9_g4CNedX_e0kDKpKhQyKKL3oDyauFCQsoAepjLln3PWBTRdzFn3-gPTtzJIaVTR7xNzKwIrdXhzDiacRTftA5s7Svrqie5zuShRJRlzakmOaxp5hM1KSPej9cbvEAQ1ydiEw1wM2LM4UXFrGr1EMIoxTWGloX9A59-IG4dvyZAL1UW1bbifMuh_PvVSBVwJYY2Uny5T2tP0UW-alvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24565" target="_blank">📅 22:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24564">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=BTst1vH3nmUCtHj5puniYuE_Pl7fHD7fWMkyctK7fvifJiH-OfOmjqGM9_6YXn6-WotMJRdfbuGeoAaD5WoK_YrRsx4aqTMMflcBqP8bKE3P5LrpN8xzDKbupm6D4Iq_Yy-672yOZ1U1ObwH4Z7iNFiA0oVyrF6P2g1k1I4mGb5xjctpp2UqV_t_djU1wC-InxMCotm0XZj2EpnrpHfmoIN5ibxYrwAqfQIdqox-6wK7Q2ssqtmpD8xu-QVSXK7ZRmM7tGqC7Xhr2Bh2AutqJzZf_aKFH3lhMmK22a6pQjVg1jHzEbYaLfklS4xW6k8cIeWNGztd3UlGiTOxNqNF-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feee4e8bab.mp4?token=BTst1vH3nmUCtHj5puniYuE_Pl7fHD7fWMkyctK7fvifJiH-OfOmjqGM9_6YXn6-WotMJRdfbuGeoAaD5WoK_YrRsx4aqTMMflcBqP8bKE3P5LrpN8xzDKbupm6D4Iq_Yy-672yOZ1U1ObwH4Z7iNFiA0oVyrF6P2g1k1I4mGb5xjctpp2UqV_t_djU1wC-InxMCotm0XZj2EpnrpHfmoIN5ibxYrwAqfQIdqox-6wK7Q2ssqtmpD8xu-QVSXK7ZRmM7tGqC7Xhr2Bh2AutqJzZf_aKFH3lhMmK22a6pQjVg1jHzEbYaLfklS4xW6k8cIeWNGztd3UlGiTOxNqNF-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
🇧🇷
دلداری‌دادن‌کریس رونالدو به رودریگو ستاره جوان رئال مادرید که به‌دلیل مصدومیت جام جهانی رو از دست داد: باید صبور باشی تا موفق شوی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24564" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24563">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=cTeu3MYSyRPiGgIb97yvQ7NDO1Nt2RKozPJzoFqX5-0xEUQb-bf9K0turqJOoiqekIbhDg5N1cnDzVJecbKReBRfXAr0zrXiyzxzFH_S7fJI2U_jD2gA7atDQis33XQwisNTL7C9oBjhIOWrFYnP2VbngTv_lK7_ZGOc5jE0PxSrs6zecBY0hYeM6FQpj_NuRi6XhQDmJNgShCxw4w_eEpjp0TcNTjVvmgLRufRAMhwqXNTGT95bJdGhsRRXSixksr19cj6injHrHFyfI1ufShxJTZs8K0v5FFyATLnvDKwB_Bo8vNF90LYM8H2OzbfDHml5xA00JK0y38U6Uy3JWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1f28bba8a.mp4?token=cTeu3MYSyRPiGgIb97yvQ7NDO1Nt2RKozPJzoFqX5-0xEUQb-bf9K0turqJOoiqekIbhDg5N1cnDzVJecbKReBRfXAr0zrXiyzxzFH_S7fJI2U_jD2gA7atDQis33XQwisNTL7C9oBjhIOWrFYnP2VbngTv_lK7_ZGOc5jE0PxSrs6zecBY0hYeM6FQpj_NuRi6XhQDmJNgShCxw4w_eEpjp0TcNTjVvmgLRufRAMhwqXNTGT95bJdGhsRRXSixksr19cj6injHrHFyfI1ufShxJTZs8K0v5FFyATLnvDKwB_Bo8vNF90LYM8H2OzbfDHml5xA00JK0y38U6Uy3JWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
کاشته دیدنی لئو مسی دربازی بامداد امروز مقابل اردن درهفته‌سوم‌جام‌جهانی‌از زوایه متفاوت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24563" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24562">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzlxA0u6SwEO7lUitQB2kJ8fiiZV_7vSuJdipOmL98_EcpJToWsD-IZIzmDcfTh3pStPu1p7CI6nMdm-5GNaG-JmE5Tlh53w0cfLRBzD3avF3rd3rjRvUv9QNgy0nRPNejkgMP1WOK8Iq8K4qzBEL9kZBz5PxTuHmoXXpfQ8VTh7PQ8d8MDKQQ2WBgltCDb5eQgfePnM58B4T-yuHEFgFV36pc--h5hykqUrx1g3pnFvt9JJm9uvQomLd-6gRLYm7AEjQoZGtMKEvzbwwtCr1AAFyd5rhV4u_m3r9R7LusuLA_hg2Ni2xH08JnmWVt1n42liAmSHehNIIzYA2kL-cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمودار کامل مرحله حذفی
🏆
⚽️
در بتگرام پیش بینی کن کدوم تیم قهرمان این رقابتها میشه
⚽️
🔝
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
🚀
پوشش کامل بازی را در بتگرام دنبال کنید.
👉
🌐
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/persiana_Soccer/24562" target="_blank">📅 22:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24561">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=vjXowPr9YiVzeCPHqdaO_8OJkJBSoUvIGBxx4HeOBkGLRbUmGCq05bujFIgjC9Buiut2j7csTu63k3X02EpoNYInpesSI8axPXnB8j4QfoTgZsPjaTFZqNq9_OBEidwD7H_VULN-lLNstisr_Vr58jt0kxY2O0ZqProL6EYMxYfWJhYAqegSiDJoJNdh6YBuD9KzY7s_gfBtTN3-qziNdsJmojf2kdkX7dA3UL75SdmSuvAmSGxyBJ-DK0lrPxw5LjUxcl6VlbtONB4xjtig3zY_ggYi5CEEQgjUhnPDfMk01C9U9PQb4bycVon-lMK7XwJzGkZnMrvR6ogKaNLHdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc1de478f0.mp4?token=vjXowPr9YiVzeCPHqdaO_8OJkJBSoUvIGBxx4HeOBkGLRbUmGCq05bujFIgjC9Buiut2j7csTu63k3X02EpoNYInpesSI8axPXnB8j4QfoTgZsPjaTFZqNq9_OBEidwD7H_VULN-lLNstisr_Vr58jt0kxY2O0ZqProL6EYMxYfWJhYAqegSiDJoJNdh6YBuD9KzY7s_gfBtTN3-qziNdsJmojf2kdkX7dA3UL75SdmSuvAmSGxyBJ-DK0lrPxw5LjUxcl6VlbtONB4xjtig3zY_ggYi5CEEQgjUhnPDfMk01C9U9PQb4bycVon-lMK7XwJzGkZnMrvR6ogKaNLHdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌ های تامل برانگیز آیسان اسلامی درباره باخت شاگردان امیرقلعه‌نویی از جام جهانی 2026
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24561" target="_blank">📅 22:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24560">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=fwjzN-8XCH_cqpe99NZDdjQdFJdg0c0yhnK2LDIcEtIwxS7FMp_hC3KxziJOiZj5gGC8e99FDgXqO5HyhSnwCEEaiopAn4uOCvNYiRcl_XP2j-I1uYOGsW2IQG_x6sHsGDjL2rAbtYQ6He2nGDkaxedsJHPeqcFAmnkzZFzc1Eg-gW9YxzTgOGwdNv9gHtZSmm427YV-voLq5neYrIn9-RH62t88C5MC5svLKc5029cwFjMqmp2BczGTRCZa4zxeIiMpIRNk-c8hxtx8Poz7krxz06Syo6qra7uS6bCysT8f2Wl8JHCTfbrg8urbex0_QAaPx9VgIlvItZeHPJ19yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc38dbe3cb.mp4?token=fwjzN-8XCH_cqpe99NZDdjQdFJdg0c0yhnK2LDIcEtIwxS7FMp_hC3KxziJOiZj5gGC8e99FDgXqO5HyhSnwCEEaiopAn4uOCvNYiRcl_XP2j-I1uYOGsW2IQG_x6sHsGDjL2rAbtYQ6He2nGDkaxedsJHPeqcFAmnkzZFzc1Eg-gW9YxzTgOGwdNv9gHtZSmm427YV-voLq5neYrIn9-RH62t88C5MC5svLKc5029cwFjMqmp2BczGTRCZa4zxeIiMpIRNk-c8hxtx8Poz7krxz06Syo6qra7uS6bCysT8f2Wl8JHCTfbrg8urbex0_QAaPx9VgIlvItZeHPJ19yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یادی کنیم از این ناگفته های عادل فردوسی پور بعد از تعطیلی برنامه دوست داشتنی و محبوب نود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24560" target="_blank">📅 21:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24559">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLcTQ1cziJ96CpkW4ZsVTKieN0INcPds4sfLPmev0Wc6V_ufj-CuQap4rx-i768ld6px0gu3sytBWvke3sNEeKtKlV_eKUoLFKBR_isESDXlTr-EK_R8h0ig-4pKKi3OxPc8jJ8RQLByZQZfROzPIMh44SnLp9KCt7UZoCE7l-e_LEqAjN-EBGLy8bHz93a4nHGpzAp6Bost02OD5qyGlPKhcMQ6lIPKFECVb2r_PqxK55EkyYcWkPSF6cVyusanKiG1wWiGLwjNZ6aVHNLXLHdYXF_Jxk2_rNXljUrgXJ3BVMuiKV9AlF8VgtfTAuSu_oL6hBgQJMeoLeLH7xRlMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#تکمیلی؛ باشگاه اتحاد کلبا به ایجنت محمد مهدی محبی اعلام کرده که‌حاضراست با دریافت یک میلیون دلار رضایت‌نامه‌این‌بازیکن رو صادر کنه. مبلغ قبلی که باشگاه اعلام کرده بود 1.2 میلیون دلار بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24559" target="_blank">📅 21:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24558">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4riS3h0r0tuGGfnQarChPcaSBKZo1cjEOJ7s1-OpWGGLE7gVpMIrqqHx0GQULay40EclAirLhRveNaLZzmVWnuJLG_azKuP8Tqfvg3FV65CsL3IMTEJiOV9_woiVt4Xk5kyFKCGBD6GTRSb45qWuHdbqSKzqggDtOXKTVjTLEam8w-GQMEZ-gHcxkUITrGOUVWcvRz5K0Yo9Gf6VzyKXBxlqVYtsDZ6AebC7fbEBr6MvOFsSY9sL9l04_LYJtw8XKYgIavxBu6N2F61DfYcggMYHjhjQ4hMMar0kfoYTCG9zJZ6fNsF4zVsahgxgQAMN8l_1hIGQUCTJjiWsIQDXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
باشگاه سپاهان 72 ساعت به سید حسین حسینی دروازه‌بان 33 ساله‌فصل‌گذشته خود فرصت داده تاتصمیم نهایی‌اش‌رو برای موندن یا رفتن از این تیم بگیره. مدیریت سپاهان همچون بقیه بازیکنان از حسینی خواسته رقم قرارداش رو کاهش بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24558" target="_blank">📅 21:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24557">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEpKnlB4-s67gy2LK_dVIovc7O3f4sQlcd56EmXQBNqvSyfwdMFyEix8NvpAan0J9tC7PnhlXL9-WX4W-4IjY60mjJRVS9UcbYD5u9aCywd7sUByJqoYOI63spjyZr3Fm-bJaE2Xgb6Osv2E4VgAEJZhp-n1FlWfnDvwHJwNLH2jsWTD8wclLMxrn7y75JwmQj35xbk09d5nLztn2ESxnwWmEsvqm7iNH-oRbqwhSRcnMMhQGQW5J0So0WhNlLDIRk1sEaZo_bk77FcEl0a5BbUmtSyM6AMCKiMmHKussEihMy4fwYMt5h9vQXop97TTaD9RIgDg5PZr3jmKNgvELw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#نقل‌وانتقالات|رابرت لواندوفسکی با ایجنتش راهی‌آمریکا شده تا با باشگاه شیکاگو فایر مذاکراتی انجام بده و درصورت توافق نهایی با این باشگاه قراردادی دو ساله به ارزش 6M€ امضا کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24557" target="_blank">📅 21:09 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24556">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUa7RU2cxhw8TSNpmXKBSeQJQ4c6-jp13MbDF0Ur538GB9NJMiSgizd-NEPygsK40hwOsxkGXOL0B_4AZB_oEITAL9pn7uCM2UWfeN3eurySD8kBpFex1fBhKlEc7U53fKaFKLw1f6DAjZHDzl2gMEr3rxd7q2AtJs8nN8cptckC20_mIyjH0Ld9bHqQmkZIoyv4fNK7LJN6ut6HPFh4yziML-A5W3m0eE8c1dUB8o787j-JL50Zg5W_8--zC7mvpl_bhcnk54NIYFfflWfjrK2qzHjk8jGLilRxvgzmIYQFr_yBRmlqISC6beheN-AnxhQ0qaiyCnw7WDQH3NMTsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇰🇷
🏆
#تکمیلی؛ سرمربی تیم‌ملی‌کره‌جنوبی بعد از حذف در مرحله‌گروهی‌جام‌جهانی ضمن عذرخواهی از مردم کشورش از سمت خود کناره‌گیری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24556" target="_blank">📅 20:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24555">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=hzOM0k3C1z5OZkHvv6JlnhuxSIFKi8Sr95XMKNMQfNtYLPS2o6q3-4DjIOuS7PR2VhgDKw2OTP8A29d16viY4iSEM_caWZYf-sRMgBkf1PhkYGVsMX6_ZwM-ETTPdvLLEpkFtOhIvCwjQOOgKttuZJIkdYoUIETPlzNvPVA-WFlNoO4-JW7IYNjhUMW0deezNaRsphFWdqgboMctSGrh8WzGQYEWWPfhLP2pHCRw5KEx2xEn553feAs3ItUfLBXyYq_v6AaO_IyM2bEjSLwau4qxLPG2uaefmDVi_YOnJeKWiOW16knxCiK_OEw9ZfOVrYlMzBFaU-BAUsX2IAeY5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c72aac9a71.mp4?token=hzOM0k3C1z5OZkHvv6JlnhuxSIFKi8Sr95XMKNMQfNtYLPS2o6q3-4DjIOuS7PR2VhgDKw2OTP8A29d16viY4iSEM_caWZYf-sRMgBkf1PhkYGVsMX6_ZwM-ETTPdvLLEpkFtOhIvCwjQOOgKttuZJIkdYoUIETPlzNvPVA-WFlNoO4-JW7IYNjhUMW0deezNaRsphFWdqgboMctSGrh8WzGQYEWWPfhLP2pHCRw5KEx2xEn553feAs3ItUfLBXyYq_v6AaO_IyM2bEjSLwau4qxLPG2uaefmDVi_YOnJeKWiOW16knxCiK_OEw9ZfOVrYlMzBFaU-BAUsX2IAeY5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌ازتاریخی‌ترین گزارشای صداوسیما از رقابت های جام جهانی که تا ابد ماندگار شد. ببینید حتما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24555" target="_blank">📅 20:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24554">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=RfVo_nPI9C5HBw6iLYNM3vxRYJEbB7NJIYqnSKSxJHHb4r6KJM3Lnojju6s4JLW-idNDiYlChjjDaTkYcMafIU08AP6WCGhYhlls2xs53ZFzbOk5qMX4B0vpZ0JVqe7rPpETibmJWkswu_Eo0aKlbCSBsekagqjT7bhuj1Zd8rfI5VX5PP3fi_nrUk0E1qAV1diE3ltZae1j3laV94QDqtGfMXNUHlRMnkbu5nloTcpJUdUMc_t10ABEDi4ydXDUuNF8tC8M_O2yoj50PwZlZ7qY8HEVxFXmIYClkXZ1bztg7x4CRZ3QU_IK8vo6hM-9aXWH_SyPDlc4gHhbJ7xNXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df8b1e3bd0.mp4?token=RfVo_nPI9C5HBw6iLYNM3vxRYJEbB7NJIYqnSKSxJHHb4r6KJM3Lnojju6s4JLW-idNDiYlChjjDaTkYcMafIU08AP6WCGhYhlls2xs53ZFzbOk5qMX4B0vpZ0JVqe7rPpETibmJWkswu_Eo0aKlbCSBsekagqjT7bhuj1Zd8rfI5VX5PP3fi_nrUk0E1qAV1diE3ltZae1j3laV94QDqtGfMXNUHlRMnkbu5nloTcpJUdUMc_t10ABEDi4ydXDUuNF8tC8M_O2yoj50PwZlZ7qY8HEVxFXmIYClkXZ1bztg7x4CRZ3QU_IK8vo6hM-9aXWH_SyPDlc4gHhbJ7xNXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
باپایان یافتن مرحله گروهی جام جهانی نگاهی بندازین به جدول برترین‌های آسیا در این رقابت‌ها؛ برخلاف عملکرد خیره کننده‌های نماینده های افریقا درآسیا تنها ژاپن و استرالیا راهی مرحله بعد شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24554" target="_blank">📅 19:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Io7IbMABItoHhfDOraG0zvszp0yrPDUoG2n1SKcngjGb3YD1CWapG0zX7HHMVXSDgCTzfYt8Dw5tskA48XHhGxU7O5UrejWN3VnERPx4sBeGB8_vFiiePEVWRXG16sGqrFCJypyiKwfClL63FQKZ_xcACClAA558_-mwI2dmZ0LKBtqVcqXVKi6SgaY5XAgeU23hYqbBnO4jnnN8jINScec8hxlGVY9k2j-4TQUV8wCnwRIMTFZAlIl5YaZzGRuAirj_XQ7L1Bu4Yb8FkVozXGDO_3uQGf0oV3MCR-pPxscoG13gkrmqrEHUHeTn6sD5NwmJWhC_6QvDrYS5P5f1xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ دراگان اسکوچیچ سرمربی فصل گذشته‌تراکتور؛ بادوماگوی دروژدک ستاره گلزن فصل قبل تراکتور صحبت های مفصلی داشته است و درصورتیکه فردا بعنوان سرمربی پرسپولیس انتخاب شود به مدیریت باشگاه خواهد گفت اقدامات لازم رو برای جذب این ستاره کروات 30 ساله انجام…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24553" target="_blank">📅 19:22 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a030de140d.mp4?token=P5UKKdt01oWTNOSKDcj-ZpZEJINWK787VSVelBtbyqBNlv-LWxcc_sSD7EYsd_JUrRwJrt48c2OsyCO9xeb70dr2EOIhPa9E_YY0SoaUu4KZmoO8eE5g_2viPMaY1WT8juPgnxTPRP0ZRhzvwD-lL1TUzdxQcewJ9A2f3_lsEFF4DKS7y30cPl3rHGEXfBc6vrYzyZxc5TdkrI34TJsIhMCyLJ_vn0GtWA_4-SmWJVWrGGyKj3N9TDKj_cxnRNnKbkoV0bEdhtwf4utu5Ts3d5B8VaIh9KB5kbxeguesGnH3w18LQ6L-l_YF2kSw0gXMXc5_Xl-qrIpY0t-sclamYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a030de140d.mp4?token=P5UKKdt01oWTNOSKDcj-ZpZEJINWK787VSVelBtbyqBNlv-LWxcc_sSD7EYsd_JUrRwJrt48c2OsyCO9xeb70dr2EOIhPa9E_YY0SoaUu4KZmoO8eE5g_2viPMaY1WT8juPgnxTPRP0ZRhzvwD-lL1TUzdxQcewJ9A2f3_lsEFF4DKS7y30cPl3rHGEXfBc6vrYzyZxc5TdkrI34TJsIhMCyLJ_vn0GtWA_4-SmWJVWrGGyKj3N9TDKj_cxnRNnKbkoV0bEdhtwf4utu5Ts3d5B8VaIh9KB5kbxeguesGnH3w18LQ6L-l_YF2kSw0gXMXc5_Xl-qrIpY0t-sclamYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرمربی تیم ملی مصر اعصابش از کارت زرد‌های مارسینیاک داور بازی این هفته با ایران بشدت عصبی شد و خواست‌که مشت بزنه دید آهنه گفت نمیصرفه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24552" target="_blank">📅 19:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=k2OLuGZub043dL1gYsh0KMV6AmJ3Uj3kJ4bDLQ78Z8iYRfkQ7M9PcfgsXSeV3CQmsHUCO8SO4sVDneUglhWuQh8YDCuu4WWS_4bZivk56i6AtPEBb_wdIcssNu2eVmhF2G9YB6EdFGfd5TfO-1yDxuCbtPsTI_om9jtZUBloORRGfIwRdCmwpmwKwmB8dn7kl0dk5Ms52arbp5SWm13k3nwL6jwevCF8MHc6nuMuk-CQ4N8kX10V1HWEO64p50-wmsbd7vhyYfSbb0CHGszpAX20sAtwXypYpZuRubwREMmLqBKIYJ9wdc7V5Oi9QYGXLKepSzS_pIbsLRo_mu8jljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96448b3dc3.mp4?token=k2OLuGZub043dL1gYsh0KMV6AmJ3Uj3kJ4bDLQ78Z8iYRfkQ7M9PcfgsXSeV3CQmsHUCO8SO4sVDneUglhWuQh8YDCuu4WWS_4bZivk56i6AtPEBb_wdIcssNu2eVmhF2G9YB6EdFGfd5TfO-1yDxuCbtPsTI_om9jtZUBloORRGfIwRdCmwpmwKwmB8dn7kl0dk5Ms52arbp5SWm13k3nwL6jwevCF8MHc6nuMuk-CQ4N8kX10V1HWEO64p50-wmsbd7vhyYfSbb0CHGszpAX20sAtwXypYpZuRubwREMmLqBKIYJ9wdc7V5Oi9QYGXLKepSzS_pIbsLRo_mu8jljzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24551" target="_blank">📅 18:51 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkrLCnxXz0_rhShNijnoya5o7J1H8kEVX8qUQK3gvyJW0bulVNcPnRsO7ZYdVWEeOwk2n0jO1BV2V1c5-J3GS0xrsBFMBeeXhDkt4SeJpvUYPL4xH90NJGNlrzWp_75VU9DG2AFA61K1m_Ulf4Gw4j0BaZfiJgDzL9hnIr0hA1Tg8IOBAVLfLT4dwm9xtlmd2htxaRjgDnYVMFcveDmxmcRDfQefZcZGXMSFpS725BvCv_n8i3XHDegX1t9KbC96p_etzRmyj0dXel0197c_jxBF6UV7O2C63OBrqueS0Pat8yxtMQAe2g14k7izyAO_KwwPUvJtCgRwY59jP2s-Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه پرسپولیس 5 روز پیش پیش نویس قرارداد این باشگاه رو برای دراگان اسکوچیچ فرستاد و مربی‌کروات باامضای‌آن رسما سرمربی این باشگاه‌شد. حالایکی‌از مدیران بانک شهر از این اقدام پیمان حدادی دلخورشده که چرابدون هماهنگی با ما پیش نویس رسمی قرارداد باشگاه…</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24550" target="_blank">📅 18:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RdQOvAUs4VkTU0GM2jd7duk_n510GPMmWomUb4LR9Nehab9JSlil89EkdB4ALMbnekPzoha2tDc6sO2x8LV-TqZAORwvy8oG8moyiPUbgD4QsZUJUPVPFBCX8GkM5aUofOiGJD-RPBaHqY9XaCjMcedogFxxD9IvrLttOTGcxwMCORhDMEch9gD128Hlbp9TOOOhjiQ8tiCP7LxLLksZaXx2cgMQy8yOI_24_PscjgjvqRUhhHiqb3GH94BTTbCdpFwRYwkcu74mC5QHOyf3aqbiR15RBFN5xHlugmfhm27VUtNW0Nl8WbX5x2731rBhlBPkSBqhe5dyBhBB2wPRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمای‌صعودکرده‌به‌مرحله‌یک‌شانزدهم نهایی جام جهانی به‌تفکیک هرکنفدراسیون؛ AFC با 2 تیم از 9 سهمیه عملکرد فاجعه باری را در این جام رقم زد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24549" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YxggrEjFLOO7iSP-CrHqv8auYiCaxIxI5FDsKf19RIShRJFSKnx5fdml0Uqz59a71eov-1SpH0k1xtKeypJGrcLLtyeHeam1gED9ZNRSH8vgi7hpQylXwSzMf7DlCzL0v6CrcEc7_PMorMhK8IeXnnHbEgHerdB9aozW1DzL819wkMEkEPbhEAtkobFr3-njz0Ze1T3T_K0TZ1-lpF3uzDOjrjEH1DAuoONvkbgt1yQuoppocOXjJdHBS-8IvggGjoQuIbimfHcaABEzWONXswlt0Q-MGEepHim4VW651LyEylEiBrE0ijt--EwGKrj8h7qhkWpVHALpyWHY1eQY4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لیگ‌ملت‌های‌والیبال؛ پیروزی ارزشمند و شیرین تیم‌جوان و بی ادعای پیاتزا مقابل کوبایی‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24548" target="_blank">📅 18:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24546">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=QYUuHr8H5Qv_m7-9xQMIkr9PGDnWBIXDyOusEYpTrdOqXr0yFMkgg9DPxF00sn7e3MgyjYYEAI63C-USDILl3NxDIklOcxusZh5L2e6xbOX8nB8EAUUbADUJEGUv7XhzPMizcss_SMHqwGBPryFnd1qNq_AtP7K-SOHv_RtpixSe1oOYV0WVmMu8UipVzxfAJZutzno2zwYP4wZ_GY_vs6tmxmpS1XnPanv0QzTBEpr08cex59LyXQ56aw1Lkn0Q1gIQADRd_F4tK_bAPgEgUijh8AqV02BeIn1j1eUXcpKh09n9PGtm2QW-kY9orccamKFMdtNFWtsr_mPge-aSHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbcff344a4.mp4?token=QYUuHr8H5Qv_m7-9xQMIkr9PGDnWBIXDyOusEYpTrdOqXr0yFMkgg9DPxF00sn7e3MgyjYYEAI63C-USDILl3NxDIklOcxusZh5L2e6xbOX8nB8EAUUbADUJEGUv7XhzPMizcss_SMHqwGBPryFnd1qNq_AtP7K-SOHv_RtpixSe1oOYV0WVmMu8UipVzxfAJZutzno2zwYP4wZ_GY_vs6tmxmpS1XnPanv0QzTBEpr08cex59LyXQ56aw1Lkn0Q1gIQADRd_F4tK_bAPgEgUijh8AqV02BeIn1j1eUXcpKh09n9PGtm2QW-kY9orccamKFMdtNFWtsr_mPge-aSHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سه‌شاهکارتاریخی مهدی طارمی مهاجم 34 ساله تیم ایران در ادوار مختلف رقابت های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24546" target="_blank">📅 18:08 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24545">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8GsWWS50-5QxZudaSPVer_5eIwxjzxqNLx0mw5psKTU4_LN1hb7kCe7Acd-aNcqa1DeIDuep4KAP5JvYFhjkO8-UStNeiPBF4T8J7dXBq0FBOvKjClWM7AXau6JgFSJRm6MmyoEepnGsv7C8T_iVbMnxVao3CqA84LZ9YWi2s6c4FbE2DP-ymbd7t2C9PBYWiFDXZoRwJjVB4svVTUOL8MXXCa-R7os9SMxKveUVVUZUxGmOJlsAn0LqRX8-EjQ7wQy0Mjm49G2OyOVHrlQH19rzEcC_Lu_nw1X8lJVV14FmPricXbpmh_ydTYI4gx6PLLxkWzm66bMsgTChIkxMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
جادوگرغنایی: کریس‌رونالدو میتونه راجب من هر حرفی بزنه اما بازهم تاکید میکنم این تیم به دراماتیک‌ترین‌شکل‌ممکنه قهرمان جام جهانی میشه. کیپ ورو مقابل آرژانتین همه رو شوکه خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24545" target="_blank">📅 18:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgynik7nuKTX3kyn1cert5kRzVcntYH1FRozNK8atzqphi1FVHTb8KBC7lGsAsdLBbQed-k4haDc7YOmXEbtuuuFnO9yLVgkxQTAEhkbUT8XNqc41HXx2QwJZbVwXqXpDkiT2fDWCzZGv1OklbdyO42BdSVICo3Zr4Sxchq4TbZaWPVLk-iBwnS4MjQuFMfC3sJKQnA194tmiVXVohJZ5VBP8tB_BHvtiefQlCugWkEo4mO42HgC1EMs3GmQU30cPHoVvnrVFxzq5wCRF8cEDOsf7asydxwBd07PfT5bN5rrpznDTRdMiycozQGlbjJO2pDQqosimdb9_tLQciS3Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇨🇴
صحبت‌های خامس رودریگز ستاره تیم ملی کلمبیا درپایان دیدار با پرتغال و تقابل با رونالدو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/24544" target="_blank">📅 17:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_tYLGnaXg77GaNpI4PjqJH-9NR0jSY8UUXGNQwIdTqbAN5T2hPIEV-37w6ig55TDY1rEGT7zxWx3h303S4mWtLyLeLc8pE87Xrrrw99v8PHj_MN9jxVHQGEgLFwFwA3wY5xwf-M4X8tM4bF5D89c8P1QTqI1IQHb1pC27TkXjJrTDdBOX-w9lrnogX72eTGi6oh1ZptXBpGhub-1d-8TeweKjfOMmpRU9l9ZjUNZSmJpcNx_951ZJXz_st8sCpOPc0hPEZjxyehko9NK6djmecPmCzn0NI8LMWpdbrTRC_wKFlgWJUurUIGyB-ARZdS8VmE29mK0U4sIYG5qtZYtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصدومیت دردناک و شدید خاویر کونسپسیون بازیکن تیم والیبال کوبا در جریان بازی با ایران؛ چه زجری داره میکشه بنده خدا. مچ پاش خُرد شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/24543" target="_blank">📅 17:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24542">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oPKu4aQOWACmMMuPHXwhqKpNC7V1KhgDWXBiK2yjc39YFvOWLPSHRHdW5Qq29JRSIAs6Z4i-oTQwe5Yk-Y449uQi-OgeSwRSrrCST9wFnFq8oUIvcaI6RJzMq7TPUiJmftNDtpxzEs10xVGqV19I39iwR1pTvhCrU5o8NfC_dMSenCA3SDJ5sMeW8AHTlaoxPA9pUA2GCngR6d_AaoSh8mvMbRlvu35du6PzkBNPlbnpzjuuTdRnlaLRyl8v_WdX3lZlAV3lsc17t03TNadlSJ1-A7YtBeRTkFHKFmEPJNcYqv48qQawI5exX0BVo60A778oyNCdQ6KAdzfIQMw4Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر…</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/24542" target="_blank">📅 17:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24541">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SlRgDn57YkKCTMHjgna16I4UqxZxm-fcodGGif9ueE3NF-kbiwwUF6X_4mbj5LbD3a3YdIyi5J1wnDmsFt0oWcubRk0IjkgdD8PwllDbnCbEsDp7sGCUZ_3OE6ommUD6wRWaIn9qRJ0eWje7aplz46XkO8XnQ_wZuzeivy9ka_8RZPbnxRqM6vHQsXOZNC8FVfYiMzGS0MWaQXVM0JPuHvEe12wA8wvlaBZG34kaeBbqCtVpkAgMjpVYAPovOiNTQZtXbeB5Fped1q3pa2nAkE9xq5LL3tmCDdFgODAn1lgovOYdSrhoCdl8dgQFBwRZae7lFmv18M3xQko7CMXchQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/24541" target="_blank">📅 17:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24540">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roL_ohrSaCjSfmwcGuACbsZGl2WCGdWfLt9nmtgeUZDlCptezUbHs0wGkjWMl_cpEMAqt3KFJBtvuMqidQaa9py-eeGPi8dyH18F7SzcZan_pQTNfX6jXfdlzlgKT8Kk4pMijMk_Ks2YwwsGFVqYRN8LlR08C0iAKhoKX5T5JbyZ8ogx-3R0v3nB_ZhSzjqnPS7BNslavdD15H68y-i_4Xpj2asq3uOQQAtJZGHdYDasXtY8nZxPSivzylPwYdQ_1TTDNT5Y_Y9UB6wxTjil9VppoiwPw-qhLGzhVZkanz-_6m93FwIZ8Zh_29UYDwtEZt8GU9MZQgQZqCD0whH9_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌ مرحله‌ یک‌ شانزدهم نهایی جام‌ جهانی؛ این پست رو سیو کنید و برای دوستانتون بفرستید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24540" target="_blank">📅 16:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24539">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWLx7xqYiBeP_FG2iMgXTTrUnt_2VnmZcQstZ2NV3Tva47Gcog2eMgK6AlCzOVazIlkK7jf4ONjdqHP_8uHPE1qHYCVjkD-zsLEsGgXDx016Kg_83dtbpS1uW-L5GmrH4lf5eAHk6C4DUf_lEvdZIbMZ0Yg2uaO747mmF6ovmfn45R61Nn5OBDhm-VwSKChYjy5RrHV1JQeKKKHtRo6hJKo1IJk3pcMp1TLT5YZ0fiegyIBqxwcOn27dJ2AEBvqfoi4wYu5mVmbiseHriGWC4LsUx8AfwlaULqweweA8lka8xQw4YUCtNHEzSUKirYvUYKtQuUdND9acomzQNVjTwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
سوپرگل دیدنی لیونل مسی در بازی بامداد امروز مقابل اردن؛ این ششمین گل لئو مسی 39 ساله در جام جهانی 2026 بود و 19 امین گل او در تاریخ رقابت های جام جهانی بود و با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24539" target="_blank">📅 16:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24538">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAG30TAjPBp9p5FGS88fHOvXk5CGYa9F-J0Jj_yhk7PgiPs8NCCGFDzHEuTBTriDL675FVP_GTjr-Q_S8aTznp9Nzi_xnTAeWicR7nsGhpq-zIzwBWvvX3LaGtIa9WY4iKrYKgnDH57aMOmogZ_fBLXifpl8cCdsTFel5bAVmtIm7OQEpaUgNW7gGYYBCkTJzyZ5jHMZa7w5qO4JHQo1zpZ7IiTmjpj7HBW7xMXQdSlqK7larSs_XJCBR7v6NnTw2P2GV4ngjHhECEP7WWCTiqf3GO1o5qRNKZX4rKBEixNhKuoJ0htIdvWQp4P27lASz_FJPPB4qtaVnmHnGLcnYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24538" target="_blank">📅 16:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24537">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zcc9jChBk_X737IoYwgIKo67mjz30EezGUwckx1W1YRu4vSdOFhvQVY5BUIdUSDMdhFOYeCbZvK-6F5g5pNo-S2o8b0Hor6ZFmbhxDsOF_R_ggRxn_-06EK01x5KPytVKrX-B0aTXG8zAM2iV_B_S1xIes97GP6icAd93BzzG-KsmHK5Zsz5w59gxixdeBbK6uQ-GiCTRDU4ZOMoNlv_w_cJdG8Pim5UBRuV71WA-cDoiWg1NvUSb5509DMpSCifrk8Nc8M1OSWGHsk78YEAV791u2IEs-wqd7umvT2Z5FGkZIEerv6WO12ipu5XV8mxmtcep3YG5wLBNZPAgkwizw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc88812ea0.mp4?token=Zcc9jChBk_X737IoYwgIKo67mjz30EezGUwckx1W1YRu4vSdOFhvQVY5BUIdUSDMdhFOYeCbZvK-6F5g5pNo-S2o8b0Hor6ZFmbhxDsOF_R_ggRxn_-06EK01x5KPytVKrX-B0aTXG8zAM2iV_B_S1xIes97GP6icAd93BzzG-KsmHK5Zsz5w59gxixdeBbK6uQ-GiCTRDU4ZOMoNlv_w_cJdG8Pim5UBRuV71WA-cDoiWg1NvUSb5509DMpSCifrk8Nc8M1OSWGHsk78YEAV791u2IEs-wqd7umvT2Z5FGkZIEerv6WO12ipu5XV8mxmtcep3YG5wLBNZPAgkwizw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌دوم‌ لیگ‌ملت‌های‌ والیبال؛ باز هم ثبت یک شکست نزدیک و میلیمتری برابر شاگردان پیاتزا این بارمقابل سامورائی‌ها در پایان پنج ست مسابقه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24537" target="_blank">📅 16:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24536">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rwxg7mL5skMG_RVTh2Kf03iF9IWHX-mYUVIGvM9-F87ctdcCOPlGv5z5LDUVKiKZv9tRpPNfOf46N2fMRtB2Avb2OA9Lep0qyWXpUzRjUCcXgXD3xOY8p76qy2yLf-cR618bq5fxb-1dC6CJSGWOsem48ahpH-UB66KY1BJAiVe4pGrHm9QVUw1-aJNn_A4tlCel9YUTLc4KbE0pVCx3iYIEkFNpFQIPXpzalI62fFIFBIwhYhFlr6cdipwEbRembu6H03oxHCynFp9xFTg2zWwUgfDUfjbEdwb2bmhGCoSF9V4regBrg8sKMTAbN7O94tWzrtnlOwPdeH0pUAE0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
🇨🇴
#اختصاصی_پرشیانا
#فوری
؛ یکی از مدیربرنامه‌های‌حرفه‌ای و کار درست فوتبال ایران که رابطه‌خوبی باستاره‌های‌بزرگ خارجی داره بار دیگر با خامس رودریگز ستاره34ساله‌کلمبیا و سابق تیم های رئال مادرید و بایرن مونیخ ارتباط بر قرار کرده تا او روبرای آوردن به لیگ‌برتر درفصل جدید متقاعد کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24536" target="_blank">📅 16:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24535">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k61UlAC4_1BcE1VHQMW1uIgchUjcz-6EzEJuuTPRbqr4FhRQZPXAxAb9Grp5_z7JZrL-2OJkzXZtPMKqpemTyTdMWE63GNEgm0NBemARxBVpoVXgbQDTvQX5riqYGMO_oNDRqUhHdXA4UvnSFFPL24w_R_4hyV6lungCzFXVsbqYSeFS_Bq3nOK5er_ZNId1nEu5Jps9ZFKib40h6vXvvt8nMD98GgKfP2R0r8KcKhPWnDN5p70gOewdfHFUrpDWeBKJ2Ed1cJaorzGj3Ot7r-Vd3oiGpuev-r79sd3uPNqNQaZJu21Qnhsst8W0ev3_6nr0WPVwWOewSwCZzdOgNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
درباره اسکوچیچ پرسیدین؛ با پیگیری هایی که داشتیم پیوستن‌این‌مربی‌کروات‌به پرسپولیس منتفی نشده و اوسرمربی‌فصل آتی سرخپوشان خواهد بود. فقط بین مدیران بانک شهر یه اختلاف نظراتی بوده که تو کانال پرشیانا آنلاین بازش خواهیم کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24535" target="_blank">📅 16:01 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24534">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTq7cUwpAiZH31aZRElMLjoNN8LCEB-_6urwdXdcWLn5l0sHXoqi6kucUbNpRXoBO67Pq6-Ga7G0Y9NFeR_Q6R45PNa_N20Ta_ZXOs5v-a4HM8xyTE2hSYvjLZw8dwOksWeL-gqDUK7ptXl0D4f2MR9LqNpAoKoNPZhmEfCi7Lsl6DApqDdYhMsZS23GiX4izUUjsJxnwuPWNU2WZxfg4QFOhn5CWDRJ7IzvuHkefQxm2Xw30JNT9OauKk9AjvNQgyHpsmjSPSeKdQJz7G9dHx3hzUtfbfpv6-OiELZoBQdZG9CkDfzbj_vPPcQDRuerbrKMhCIL9sx8d4BzRLOJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌شایعات‌مطرح‌شده؛ پیوستن دراگان اسکوچیچ به پرسپولیس منتفی نشده است اما یکی از مدیران بانک شهر گفته چرا باید این دو شروط اسکوچیچ رو بپذیریم. ولی چیزی منتفی نشده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24534" target="_blank">📅 15:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24533">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🏆
ویدیو کامل گل های روز گذشته رقابت های جام جهانی در روزاخرمرحله‌گروهی این‌رقابت‌های جذاب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24533" target="_blank">📅 15:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsZPkVcSnsy6EAB-zDuCOljpx15arqWPFq9jAoKsRwD61e38mmWKDCZPjjCr5Zj0UvJJL9z0hmYhdkZH4yQ1WyEeybsVBK0Q1MZ5gim8t5YMMgzc5aD_cs_k57j_LdY06g0Rdoz2SjF_6p0albgTtKl-hp8qKL8gKa9KewJWZgeZnxvDTKzadPx3iTN0H35qjPNDzyxI8nA1wo7H8ZaVIOvBwyhk8Ke7ZcKMWYx78QbKoxCOMRCXMlZn_TGklQqqcTKY_px7J0LBpyRaTmccko6HhMF3_FS-5ZH6r5rdBoykKgQWAb7hN0oe-MdQEWfnuYkdf2F__DUs2acN63Elww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=hr0hBTczaCsERUIsvLjFvNsfatkDMYud3YM1bHLiquGs_tlWYWakY5djhbG9gTj8jt2s553i3xAKkn1RJAIET6bmV81_L29ZEHgBOafg5mEO2t6rLLwyumA3CstxI-U6PBmID3wFiy_QwIGiyhrVCkk7cn-bUSHWYzyttXFgPWgCRG3lI3ZB09GwRskQYIdZVoSSpcZAaKPEQhKlzEhfll_wDlbHgIJovlKW2nXlKVjjXgjitS3WbBKxuoBqUEGz0uTesb4kOEG7jvq35fgdOY1UNRjLppfimxEC_PEgrxbwNG8rKWQcF0naV9tUXwLeIQ4JBxl9wCvNTvH6INmQqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f11edc5879.mp4?token=hr0hBTczaCsERUIsvLjFvNsfatkDMYud3YM1bHLiquGs_tlWYWakY5djhbG9gTj8jt2s553i3xAKkn1RJAIET6bmV81_L29ZEHgBOafg5mEO2t6rLLwyumA3CstxI-U6PBmID3wFiy_QwIGiyhrVCkk7cn-bUSHWYzyttXFgPWgCRG3lI3ZB09GwRskQYIdZVoSSpcZAaKPEQhKlzEhfll_wDlbHgIJovlKW2nXlKVjjXgjitS3WbBKxuoBqUEGz0uTesb4kOEG7jvq35fgdOY1UNRjLppfimxEC_PEgrxbwNG8rKWQcF0naV9tUXwLeIQ4JBxl9wCvNTvH6INmQqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شایعاتی پخش شده که آقای هنکاپیه بازیکن تیم ملی اکوادور با سابرینا کارپنتر خواننده و بازیگر معروف آمریکایی وارد رابطه شده؛ سابرینا در بازی اکوادور مقابل المان هم حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24531" target="_blank">📅 15:16 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24530">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsA7CUVEKP75nDTxC-VZH5CgjMUopYVLSPg21A4Vw-AAZGGlH8riZYFhHcL7gKq6vTGTuebnECHsWOvTSafg807a9r-HYYYP7JXygi7sN-GFz6AE6M2ImynO5GRBt6Lz7ZtF60puKw2opqsv6cTTdzxSVenrT0fP8ycS2PrwZ81BPWk4NnUkni4uTw6gvf0T6Pys9gdDG0LSznAv4Gw1Z1TydTlSSIGAZhY7rVkieOlojYVz2-4kGGMcCuELOLVhkNhBAdEV1PyN_jvPL_sndHHFwyhcpDHungOQttShAKdFbho82cWUFWAgruHphnf6DOnFcXAQxqs0Vh6F1UmTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛ ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر…</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24530" target="_blank">📅 14:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24529">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vVqIjrAW-KH3jdOk45dzXsEaBZXk7Hnu2cT3nGKsqdzMZsCYx2NJCZAQdQgeesIcg0z2THhzrneQ7biYqQC8L9t1SR1TluRGDzSn-H_DAf-_4bahwLe5TN19fdjDnUrecEibpf_a6SV412GtulGd62dGMQXJleWNVCmzWNNArySV-9d17yjrhg2Cak0nqUtlslinJjWj9hwr1TYwucT9BNc6StsYMTQQZv8i5vMUwfuG8wxkA_H-Pj2y27YDDcG0uVCuqVWSJgWcRS4OsP1T2yMu5RW71oje4RkAu_rsAexAG_Q-AKiIFdYal50a8HORjM0esCx7JdZPNDV85KPZIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار کامل مرحله‌حذفی جام جهانی؛ الجزایر و اتریش در دیدار تماشایی سه بر سه مساوی کردند و همین مساوی باعث شد که تیم ایران حذف شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/24529" target="_blank">📅 13:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24528">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=dudQhF57OJOGjX3ZO9QEwvbKAjCTaBZ5gU5I4sgLGyOPVQliOrMpugb8E8ZM1_9ij3sVMm-65xEvFudEAJiwTiE3ofZELltrW5wPFJYbSK1uO0Q8cl0kHiFenIgA4bqjh-21RiK_iOiGZU53_pWcwyQohHS2kMcskALoY9QQlrlofYN6S15H616v4GyBqqldF1aM2y3hMo9oXNv11Mjvdn7TW46woM8uWDK6UxBFOaEohb6DQQoCblWH9cvF_L2viCOAPoZnFU1yyXNeHqcYG8V9FIvYY8nCma3YMAsez5deldyTiC8G1Iq6s322wNrCqoHS-6eNZV4-r6nuBkwR9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aabc5e40eb.mp4?token=dudQhF57OJOGjX3ZO9QEwvbKAjCTaBZ5gU5I4sgLGyOPVQliOrMpugb8E8ZM1_9ij3sVMm-65xEvFudEAJiwTiE3ofZELltrW5wPFJYbSK1uO0Q8cl0kHiFenIgA4bqjh-21RiK_iOiGZU53_pWcwyQohHS2kMcskALoY9QQlrlofYN6S15H616v4GyBqqldF1aM2y3hMo9oXNv11Mjvdn7TW46woM8uWDK6UxBFOaEohb6DQQoCblWH9cvF_L2viCOAPoZnFU1yyXNeHqcYG8V9FIvYY8nCma3YMAsez5deldyTiC8G1Iq6s322wNrCqoHS-6eNZV4-r6nuBkwR9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
جدول گروه K و L در پایان مرحله گروهی؛ کرواسی غنا رو برد. انگلیس با درخشش بلینگهام و کین پاناما رو برد. پرتغال مقابل کلمبیا متوقف شد. طلسم کین بالاخره شکسته شد و گل زد.
‼️
باصدرنشین‌نشدن‌پرتغال و صعود بعنوان تیم دوم، تقابل آرژانتین و پرتغال تو یک چهارم نهایی…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24528" target="_blank">📅 13:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24527">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=HWYK6va7qAQew1vpxCxeKuwTQ6sKohcHudIuEHndzJmnU_6lr0k528IbynRjMe0mxAYg8HeBfffSwlWuQeGN85BujvQA5X3Wj-OcTTtjJkPdLfONg7Gsx_jJRXBgPqVEKDximm5QFj1SNIo4okRXBL3SqB2RTy6X80BSUDozP5TsdoRwulcnoO1YZrEMtD0yrRPeC9PqhQZC4L0mbzu8rjBdBr_xZmrD-3Tob9cLpb6uZoL435AHkVR_pdd2Lx_ASy7lQ3b34sQ_ed5MKdCKS9mU-Baudq8NA6QHBbs2K0wmnDa51LsaDSKXhlMSINS6Mh6LxeeTs5L8JoG2gP3vWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=HWYK6va7qAQew1vpxCxeKuwTQ6sKohcHudIuEHndzJmnU_6lr0k528IbynRjMe0mxAYg8HeBfffSwlWuQeGN85BujvQA5X3Wj-OcTTtjJkPdLfONg7Gsx_jJRXBgPqVEKDximm5QFj1SNIo4okRXBL3SqB2RTy6X80BSUDozP5TsdoRwulcnoO1YZrEMtD0yrRPeC9PqhQZC4L0mbzu8rjBdBr_xZmrD-3Tob9cLpb6uZoL435AHkVR_pdd2Lx_ASy7lQ3b34sQ_ed5MKdCKS9mU-Baudq8NA6QHBbs2K0wmnDa51LsaDSKXhlMSINS6Mh6LxeeTs5L8JoG2gP3vWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قفل کردن تیم قلعه نویی روی عدد سه؛
ایران توی این‌جام‌جهانی ۳ بازی انجام‌داد که با ۳ مساوی ۳ امتیاز گرفت،۳ گل‌زد، ۳ گل‌خورد، ۳ گل آفساید زد، ۳ تیرک‌زد، رتبه ۳‌ گروه‌شد، بازی‌هااز شبکه ۳ پخش شد و برای‌صعودباید منتظر ۳ بازی آینده بود و در نهایت باتساوی ۳ بر ۳ الجزایر و اتریش حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/24527" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ocOwmEvcDcRNjL42bzKpY88R1ztzLQqBxZ40oWubZQtZpIjxRiUsqBK44wWeSgQYXkm6tpynqO034G-KLB65sc_qZm_JW2ui45XmkCyXZGLw7Pdw0vc4XB45TlI9orSGJP4BkXVxOQRF3yz21dQ1Iy2E0nXf4HVnsnDxqUk46aHowan7cQYtNr4YA_C6hGPLyyy9ojw5fzVgHOHBGHH6B8xBpmwFWOd0zQAyH4gx4x4PYJX8ZdoW6SKjKe0_w8H6zBn2uVHClyLberKkO_OQAxg0-ycI14anYKP0chuqPhYm6JITrL-cCjlI6-fbfr0j3i0Hvm_PJUkalIi4rxp2eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏که‌مردم‌ایران نفهمن و بی عقل آره؟ خدا هم یجور گذاشت تو کاست که ده سال ترند سوژه های جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24525" target="_blank">📅 12:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=ZwcwOSCkYn2aK49fdhJXRz8k7Jjih9922OhoTdzA9bbM_IH_ZZ5OTKwIKB6datdOdGDAwo9IO_sT_IXArD_1O76_u9TucNQneDQHFo8FmcGv_yI4YtZcSKjrMeJC1gZ-z4-H0u0OnXQxcEwxg4jg2tW9wx4xLnfGZVNzWYof-0WpwzztzYMXxhz7Q6jdwiDftMzjzbepgPGC7wbVnDFYXkKS8PQSMucmGtfTIW8IYxOXH4pNSgK14k2ZlALPks1lN_l3twbfa60d2n4ChhciZvxVQAVrtWExV3uoJoQk4nkQJClPv0E9Q95FC6ecCgVnrXHBCBieRIXvn0c7ZHtD0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e51a32c9.mp4?token=ZwcwOSCkYn2aK49fdhJXRz8k7Jjih9922OhoTdzA9bbM_IH_ZZ5OTKwIKB6datdOdGDAwo9IO_sT_IXArD_1O76_u9TucNQneDQHFo8FmcGv_yI4YtZcSKjrMeJC1gZ-z4-H0u0OnXQxcEwxg4jg2tW9wx4xLnfGZVNzWYof-0WpwzztzYMXxhz7Q6jdwiDftMzjzbepgPGC7wbVnDFYXkKS8PQSMucmGtfTIW8IYxOXH4pNSgK14k2ZlALPks1lN_l3twbfa60d2n4ChhciZvxVQAVrtWExV3uoJoQk4nkQJClPv0E9Q95FC6ecCgVnrXHBCBieRIXvn0c7ZHtD0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
وضعیت نهایی گروه های دوازده گانه جام جهانی بعد از اتمام دور گروهی+ جدول تیم‌های برتر سوم جام جهانی 2026 در پایان بازی های مرحله گروهی این‌مسابقات‌فوق‌العاده جذاب
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/persiana_Soccer/24524" target="_blank">📅 12:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMNi0qdbI6mZySYtU78ivpv-5UlGCWH5Bg7xr8McDrtgDHb9fVhkEgMkbVgRW-lb7xRlX9FhiToFgFctM4q3LcJuIiFTijvQFVZkW69JGMUeSWN4-BdmvsWU837oVUHEs1r2iONlw-GKkYTUG1YTogipJZ6GiuOwvHBOVkKtYxr9_FYMqUA0E5cciZoQLB_MGPJ59hds9Ulzh3W05ropTiDzXWl9l18fwnwbFsLIgheW3-OhBwQFVvFgaMBvVF6vHw3aEZ3NmPb1UdyTp3ZX0QwyIas54Lyx6Cwk6zdh237bbygQg9DebEPmR2sxSXXpyAUgatwYYtoucwv1lq4P7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
#تکمیلی؛طبق‌اخباردریافتی‌پرشیانا؛علیرضا بیرانوند به‌مدیران‌دوباشگاه تراکتور و استقلال اعلام کرده دو هفته‌به‌او فرصت بدهند تاتصمیم نهایی خود را برای فصل بعد بگیرد. بیرو هم از تراکتور پیشنهاد تمدید گرفته هم از استقلال پیشنهاد سه ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/24523" target="_blank">📅 12:05 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
