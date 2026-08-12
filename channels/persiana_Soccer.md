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
<img src="https://cdn4.telesco.pe/file/uyYRkaWMvZu9kuh9YKWQL5nHcb_Gx-4OVgOUQ4zAC0hKUVaIYCf5jyB20HKE06Fd_YX8_LHo_VWR2hLh4eC7OJV24LMZ5MLg42CwgotgtjyogtG5qXshHvE3k0Avj-NMNHf2KP8lRZhZ1fzpbBPzp5sOIj7zBq-1yjzycgcFCiee_EyHbIv9AELSDVVPcEDrV5LvLKbmkAvJb3Q3-oVJrkLd0D2lT9ryPRiGGXNYAP-jGbZ56JB20iEliCiUH0qrUumqmRHNs6VH6fXQaUcb8VACa8MD7sxYjsCQ_MuxEpkV-6FusoYv67uw4Xr9ftv1znVYa2Ou9XI-AXEGNqEUSA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 625K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-21 04:40:03</div>
<hr>

<div class="tg-post" id="msg-27562">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofRPtuAG0dJ2mXea8OJmpjenqw9IpmBFFTg_vuv9R4iu0bIfmHk_k1v85nTR0r0PR35WN_e-z8DOxAawo7EO9sxadxwYUKSH7IfGqKtJ20IEg_1nM6nstLEJ_VBGM0NTu3yZZDNOIbO36J3LwEME54qSQsynunyG4RHJkPZr1HpPps0TJqsjHHjAoGVW3lrku2gvmrN7BvgFsTGHzUcgm639Ylit_8X0jPJuNaDtWfMqaQ_aqbwe8ALsHuHJGeBE75VLCuxF-hu8Z158xXdRgq89OSIY0ROM_5IeX7VFV0Tk3oYapCCtdgSJ2Q4Q3s384jZu74UA6ZmXemDV6hzQoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
#تکمیلی؛ باشگاه نساجی 20 میلیارد تومان تخفیف داده و باشگاه سپاهان نیز قول داده که فردا 150 میلییارد تومان به حساب باشگاه نساجی واریز کنه و قرارداد 5 ساله‌ کسری طاهری رو نهایی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/27562" target="_blank">📅 01:22 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27561">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TbVgnyGVe1jxYavEKUeiNQTGtgRuJsH3AWxeaDArRUIZqkec1sN2UzsYHLzGHbHc7FldtRqt0bkj5gkfQWUZo3ZdCZ-Za0ooEuQeIgCdcvixiWyPUy10eTBtLfvO-nhnDqxKJtQMBpFKbS9tJyN30ejkWnHj8PFtDZk5b9nOjsV3Rp2Ppkb5xOOP0yNI5Gr1HiPAkZBm0SYlZWIYanZtF1a5xi9IcelqjIZs2jCqdtyKpLJE-eR9PHRgL7Yg3rr-1Z7meGW965Dx7IEiHvRHp1hxsLPd4mbmBYbqf66EJlwounYQDFQYPUG2DlTCaDkwa2S22jnYX8QXe9TI7xGaug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌بازی‌های‌امروز؛
تقابل‌شاگردان‌انریکه و امری درسوپرجام اروپا و مصاف‌رئالی‌ها با یاران اوبامیانگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/27561" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27560">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9XRHXE53NnmG1S9XK92xD1JOVTk2YWHyh3MqFdvY2NtO_ho5Vvi3ZU-ejDsWU13j0QhdW0wjZw6IXSwerP2JKnHg8dx4fo47NKjlgbZnlQiEdzWy3Zm8JYSst9zyda_IXjE6o_SIV8Deyxd4IHmrli3wZsSaZp3m0qM7Buey1t99ZnPSOASgBdPWUcy3_regaB_zExAwAAy0CTi7Oj9antWJZCw-3I_I1h-psOFJlqYO6s_eK1q1EMc655n1iL2fnEnSu1WfUQcOpPqyy6xaJqy0KPTZtYpflMaIkqMngBGsMvkDwwVCufp-Biy0TClkvFfKOEwpPpaikDBJA9ikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
کامبک‌المپیک لیون در بازی برگشت و برتری فنرباغچه با ‌گل تالیسکا در دور سوم پلی‌ اف UCL؛ کارتال و فنرباغچه عالی مینوازند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/27560" target="_blank">📅 01:20 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27559">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f71c3312d.mp4?token=YHL8QWijSaX2D5uIYMtKLc4RHsHVkKVrCplzxzyqEhQFs1zxA46Xeeq1auf9Lquq6eKHoXQ8NYHYWUhapleFrPIMMQMSeanD4GrUp4VzQkQx25eNh9I-4MhocFp644WMycL0XQtflKlJuA3dDJZI348d4-ecFpUfg1lb2G8yz_nAZKiAtEJjbdJdAkfc3OFzBFcE0KKnohpJfU0XVVUM7MMOXD4cGgWcGD3MGa49Wr2kC9ILPojGYMRSJptCfgyOHO84H34jaQw3BrSF_Y_IZ7a7i6eU1YOsexRhWBd-CA4Od5YbiNttC2SfmF4PuenxK8Ncgdy0NI7yzMEMRT_7vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارما به‌روایت‌تصویر
؛ روایت تلخی مردی که به خاطر مسخره کردن پدرش نابینا شد. حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/persiana_Soccer/27559" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27558">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea240a7d2c.mp4?token=N5WvrAXeFC2TsLq_Yo-2lEkm4yjEjj-wnMW0amzXo6vZhQFLBJu06kDLFGMG8XsfDP4-iWT2kHF9lSZVhilijs_Cw06JENfrzaA-LKPBylW-F_vkW1mq9cugZ5N-G5gUau3vEm7QgPQu8TP1bayUuTS5fldb74s6ycgrOOw4Bkx4osfsCN1vvccuB3MppmiVwSoPHJw10NNdbobGUnoeF4Ia9Fy_uVOi-iOFl2U_WVozs6rgssFuegcgslLE-Ud99nDtcA7sSb5tNzJ9MV9gMBM-jTPhHhKr98za4TQUyfUmEmwXg_v5wpcbF0e8BEm0M3d19gmeNFwSlMG4qO1PUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رکوردی‌فوق‌العاده‌برای CR7؛ پست اینستاگرامی رونالدو در فاصله سه ساعت از مرز 10 میلیون لایک گذاشت. فک کنم بعد از 24 ساعت عدد خفنی بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/persiana_Soccer/27558" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27557">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d21OJo6dZHKd1HDjtVHE3TIxwzejfF5GYqPoBbveGBRCk6OlZR3ReSd-9cnrpG5O9ALjDDfuMH7TolV6kASq2B4x9ih_Z5g87tN9PLeM0iKFuLs7vOf4inZHPNWnVvkbL1Fg0WWLY-WXE-oJ4wc2Xx9BoFWPUTJhzL5JNYfs-7FYDUKZBZzv8I19oiQzHM_8ikvGThDODdEpsPojEnD0I1eREfpZreYDAB1YCuJL9tfK7db_AxYZGCAWDHXS9dLfcCpKKqnWaxY00URg61BFIER4R4fb0ScVz9gFEVGg1sEkE0MGFm8MY_6MvtqOcy6uxlh9ExoqGnD76g78LkKkqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎲
بیمه ی
🤩
🤩
🤩
درصدی سوپرکاپ اروپا
برای اولین بار در ایران
🎲
درصورت شارژ حساب و پیشبینی اشتباه بازی‌سوپرکاپ 2 برابر مبلغ شرط از وینرو فری بت هدیه بگیرید
‼️
⚽️
پاری سن ژرمن
🗼
✖️
⚽️
استون ویلا
⏰
فردا شب ساعت 22:30؛ ورزشگاه ردبول آرنا
🎲
با وینرو همیشه راهی برای برد پیدا میکنی
🔊
🎲
ثبت نام آسان و سریع کلیک کنید
🎲
✅
🤩
🤩
🤩
🤩
بونوس اولین واریز
✅
🤩
🤩
🤩
بونوس واریز کریپتو
✅
تا
🤩
🤩
🤩
🤩
بونوس روی برگه‌های ترکیبی
✅
پخش زنده ی تمام مسابقات
🎰
✅
درگاه اختصاصی برای کاربران
💰
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sa20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/persiana_Soccer/27557" target="_blank">📅 01:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27556">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuE3ELj_i-FK16QcAqNud84zrIlJCXnV4JBeo5NohIz3ozW1AIzH9LvhVNMPcEi5HUFQPu70HPK6VPy8_2sAgaHfhx30kiHBJlra0yG1ujah9Q-t-_XWNlEURCNahxT1gvtsxoml7TKF1futkAsLtAsLjHYPgo6KznH5U7qmE5L92UpW_x2pHmkb31veu7aNKhrJ7rjmNSmYHDS15aL1Dqp8Gnx6cI2WPtOryLF1PMYfRGCoDrRdJBHAvkIGpsah70Q-cP5v6duYgJvG5QaY1o-xmQnJHAdUN0h8kYrRqpiuc18jZGXl7wtcAYKeuojNwFPjuuEUVLP3Xqn1a8rfxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/27556" target="_blank">📅 00:55 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27555">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdQnsg-nraAx5n0o20o_l4loAG9fVpqwAkiuSjYVx95sdM4y3CFAeRJ-lCqKoFDtoGYE9J5lDcsQcZhAqtJoY5Mgnu7hhDFJq7SSdncdkrlWcLLegNqsCSoydWvRCHy9joHwHQz2s924hNpWr9N1o_kyrmGknNdBUUAIX0-MlE9sS1p3JIaK7asJWA1UpLMZpsCyKne6aNnScU_kC8S_jmF5SZugGc3Tch7AkZWKgdyCXHOlqXJT24FTr8TvOpZbmouj0DJnqWqbn9FlLk1hG6KJ80JZNOCtcXGfvSLSTYW5WL1UkAizjVFrqtkpkJq6CF7CGuXOCp4A-NxhT23QUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها…</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/27555" target="_blank">📅 00:38 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27554">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNW5oIcKsYbwEOQZqfJYJxrqf8eLU7DXhCQHOARlVQIO0UozW2XCwPsYa10pxRn72-NysQo-LkFAEb3ejQ7TP_z1gzw4Nzb19xsYyQ8hms4k9Bd4dQvFGp_fnU4fVF99eLHLkIzbIsbJW4cCXjjmEsq182YRjEwtBUlQ9pf3b5FIvGZOVWuaDpF7yoTEBkxxzowawUkyLqgoaaXY9wc7yHm3RGc_KkbXfqROSvKx3e0ecLjux_ERbkqvUgFEzgO2Te7HIhasbRwAQYBHz6QF29EE6uNzKGajRtt5cyBDadpB5ZLE3g5SKtgHZ7P8snya0FQ16hFmaX9_-Zu0SxXhnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/27554" target="_blank">📅 00:19 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27553">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nto7IK_lgOhNJe2uc2mu5C4H3V5I9M7iqrx7A6utf78qA9QlfeYwf5nRujXMxWSiZOANQJjI4MtAe1hzEZ7TVZerw5DGzIj4Gu7GeZto6eMVAcHbu6Wq8FRNuh9rY4eRhcPJXjavD6gXTrxWseMm7gRPm5gB5uD-bPM_SiR3Qf_zYD6HEs8AmRk2BfzHcAtcNCZt0MNCe7hhdM39a4S-JhLPZfiIZh15NN9eCIVupsT-JPSYUBf1CtrpC1_KJEo1Bddns9-2ipjzHFVtdgn2acgpXJJo0gVp1g7Rv_X-URq6WHoniIH8g6mzPkIRoYvww87dF_Dx6rj7KWkQ-_-J8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو اسطوره‌پرتغالی‌جهان با انتشار این پست خبر از ازدواج رسمی‌اش با جورجینا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/27553" target="_blank">📅 23:54 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27552">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇹
🇧🇷
ویدیویی از عملکرد فوق العاده دیدنی و برگ ریزون رونالدینیو شاعرفوتبال‌جهان در فصل 2009
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/27552" target="_blank">📅 23:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27551">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch3uTWBc0w-xy80GWTBNt8u_iNkooBUwCH17kNVKC2UF-AMMuPexXOqH21XOfDu_nfOpSfHrvpa9K11-OGXhsIOFOvqlOeneMtKgUb_bsuQhJ5QiG03pafEV7Hpq3aih98jWEy-gGwU78ljAzMU21UdQMCaudxZrFxRPfUKp50VYvZzqNd4pJGgJPxZGRWZHw-6Trg9CgCY-kbLzqWJ4WiZAWZmnU-BNVfwbmBXNP9Nr2njBS06Lk4ER0PpV17Q0M3Kqr2_J1WWMIXuoIg8gU99J7SWEZ_sFRaeL6WE56XF7MI0KeImPnrT2d7shcd2TBj5V87jInECvDOpkSY1YSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
شات جدید دوست دختر پسر شانزده ساله کریس رونالدو: من درجام‌جهانی طرفدار پرتغال هستم و امیدوارم CR7 قهرمان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/27551" target="_blank">📅 23:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27550">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m3Z7j4FhQSFdJOXtXAWwjpviYQX1Bs_DsE3g30yu3nGUgZ9Z7025PAkkKmDTYJYrsX5DO7KjT_GnklK96kUqktkpmsC7jX2n9ASRQeTSpOAvl24hNN0cRcXE2mW83Gk8qRoyF7hKdWraM9_q2WpQOqOXRRBTEZGoOg5NoZ8W0tqCJ8hwUJOWKODIY4e-HkYRNkAHj5qW0OsjXLE74bHl1VCzKUvuwr2ZdkdREEpTdEq8qht_CdW4HgMrGwY0TZFydVjOLLvCc-mNxPSpaHqETR-S_QMiaiuOka_xYQXUDcacLT7ddWLuLB0Ad0l1NRzm-Yq5wTx2i6iP0hm_767evw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/27550" target="_blank">📅 22:51 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27549">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v31WyMptgYfZRzIqhO_IB7L8Gyy7OFx1a8B8cA6VwTMIsHcC8CV_dkjBIqrRIE6usiSXls2y4GMfbJQ-34KP8QZ0cNeJqEnA8Ae59xdyUX1FmcmcxGMj_fs4RU4ezUJ5J0YbH6J10E9sUedYDJtfvrGFgljofK1R7UKtkgc9ne3aXQROH0p0SgRaAGa_GZYm6bNVVH1T-dWBZkTuxcfpfksdHvmhLXjQW4VNi949e39cPY08GOJ29AQdAhVYE6YKbc8sRnQ7QO-jpgviGDdygvRgb-lVzzQfawr-NvJA5Bt9HFUkEKyiY7Tmmj1HDH4VAaeZk6xeddyVjaV-U4cBjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/27549" target="_blank">📅 22:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27548">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWLZ8HV115EvUQp5SQDjjx-MGSekB5cCc3dhAmSrmiaC73RnQ5vfi-RKIQu6niN0lEwkN7UFoyuURuq7N9LuA3Dz5gagXWiGPbA47Dnt_8kK7dcLH2_Hn4TXpJzKO85f9RkPnpdbWQl6-rSnTRm2uo_GLv02XZNR0XpshzSUV50NoHDAfmpaHLyPj1ulux16c4mtIX5PWPTm3vqnOPpmK67_CxjLHHfYJY4OmZes4n2u0oNgfQ2dEWMW5qdL7NF_LXWGp-cy1LJLQc32VS0oyJAx8JsFZ7K9L51VFCZlFrXJXQdRg32P6NRD20V8ldplpt4EMKkPk2j1HwMtUrTfKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد...بااعلام‌باشگاه‌پرسپولیس؛ سرژ اوریه مدافع‌راست ساحل‌عاجی بعداز توافق مالی با مدیران این باشگاه رسما از جمع سرخپوشان جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/27548" target="_blank">📅 22:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27547">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgRm-lwBmranb387ZLOd-WL_0gIG1ZeqO8W-cFmi4D5XDYBtb3og1arQeAJ7GPeMJkrD2Wb_LJcbRVkH85V5BHW9cKCH_YDk8ZpQBfI-FAxZzS9RoDrTytA5eNTogsAvK5KhlDgGFf6SCcAEwfY071hQc9NGTDI4bu1Gz2yCz08TMXLukXFCAnmdWrQnbcNH2M7XVlSBF_jdcypWkVOgjz2r0m4TTnfQYor4nTkp6uqKUsb0-VChnvCnUHTvRL-L1QS8FOgOtCkmH20TQeljORcUEz9T1ZflkPdCpXbzGTERYcCj7yRpyl6YXoPCEhQTpaqqB59XbiqIF1sBUf4-FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
پاختاکور درپلی‌آف‌لیگ‌نخبگان در شب گلزنی بشار سه بر 0 الحسین رو شکست داد و راهی مرحله گروهی لیگ نخبگان آسیا شد. این تیم اخیرا مرتضی پورعلی گنجی مدافع سابق پرسپولیس رو به خدمت گرفت و با این بازیکن در آسیا حضور خواهد داشت. پورعلی گنجی به بازی امشب پاختاکوری…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/27547" target="_blank">📅 21:40 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27546">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEk8JkR0rTvTv5Kh6A_UruZNMFYgYTugf-hmP19LfDMECxyP668bP-sTjZscbaknTVaF9fDUb3skA3OSPzqky6B26eDYzSLbfLl1gNq4mc56EsKQeGimaLZVNeJzpH_QELYWUzRNT3RZ2pWmKPBW0UnL6fIgzdg_6qvPeeKfERTLc77aUv0ut24Uo5iwuPs0IZjAtbcjdMkjAB3yutKyBFMbyu_nN_Rs99SiecMBIoMy2ky7KROfwA26WF7-L6uAA9QbVs0N6AoJM-MlGQ_BHJ1bl0Y6WvxFGRSupehWdkTiuoDc5lokCwvdZRfA4KXfWgjp_pX6ZAcgAm3udF5Sow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ توافق‌نهایی بین دوباشگاه انجام شد؛ نیما اندرز مدافع راست20ساله تیم لگانس برای عقد قراردادی پنج ساله با باشگاه استقلال به توافق کامل رسید و نیم فصل به این تیم خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27546" target="_blank">📅 21:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27545">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o4PE7r1WrwewpjwqZC6d0FLakOgYSWImANbpD0Pwna9eHHp6R76gmwVdpa3h0vVu5kgsXUIm5MCihUugaoyLjZ3OHhOCjrgeyKP0KCA83uqTd0D7jVLPfqkNTXAYpad67a23e4zyPws1YH0aWoA8VKCAFKLtwjvnW8wdTTAjI8_mCPfYtD5VIZ_7jf6QhlZ4DG1N7rkPdJz02ByFEoZ9RU0Kneq66YN6XBAq8ODIWGXsoKwRpccArZYs4-IYdGbdlxpeDYW6Q4LA63s1X0lGpZd9F7WWHPSWMcXfaL7th7XzEd-SyGxvZAH6YthlwsKyI0CUkiC-C-5AuwkhjrCN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزیکشنبه پیش رو یک جلسه مهم در ساختمان فدراسیون‌بین‌هیات‌رئیسه فدراسیون فوتبال برگزار خواهد شد و اعضای هیات رئیسه برای اهدای جام قهرمانی به استقلال رای گیری خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27545" target="_blank">📅 21:18 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27544">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RIly9VknKn6pViGsUQbC-PlVOLo6vL1UltMpzX1ntZNmHf387SrgcBJdZzQNCp8CcSGVRSs0wHAv18IFDpxW9sWD9StDnhWsiYNTP6z5ucEv1jb5o3HeeOondMJgjTM9hOT1h82enQD27SAiDFnhF5BzRYelG8WUCnxLmlefODrkWUf4o_8i-goE_0d1jL6r1pE20tW0_HIgquFxydT8L-Dz-D8X6UyC10RZcgzSzLmMBB9A1BC-NJ7Ftrtq761GMOlluJ1D64jQoE8urx8p1d6yKzGte6ChA6OwMXwf6FLddIJN-gni4cxQmRSyfNhxxJTNC5QLMiaMayQ0S5MCCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
🇫🇷
بازگشت‌دوباره‌پُل‌پوگبا به‌فوتبال پس‌از ۲۶ ماه دوری! در شب شکست ۴-۱ موناکو مقابل رن، پل پوگبا از دقیقه ۸۵وارد زمین‌شد.  پل پوگبا بلافاصله بعداز سوت پایان مسابقه سجده شکر به‌جا آورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/27544" target="_blank">📅 21:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27543">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lh8D2xOVAP7Or_u76l2FxY02OTlXgDAZP2jAo3XEOiDFfzfYC5d2zdJ-y4kbGCfEiliJXSsTkE2qBjYzXL7oS9hSpUY6js3gXbmrg1nTDWmOwudVo-f1zkLIU-Y59sAyTT94s0efak5UeY5SwJnQaeUAH_y4r79-EY5R87pRhgKco7MvReT2j98G-Q-JGwAEsTgS7p3EHSosMqA40Qud7M2S076I0oMTxgIpCOSfYAWzRWpgcn9pqHiMbsZTFQxc54vUhm9V8h8ZlGr05sKYgZTUqMXTVBMTfruf04rcWyequ6KgTo-g2EyhNd5ztdSHYcxjjc-n97lv5eNRLbuu7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مرتضی پورعلی‌گنجی مدافع 34 ساله سابق پرسپولیس با عقد قراردادی یک ساله به ارزش 600 هزار دلار به باشگاه پاختاکور ازبکستان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/27543" target="_blank">📅 20:35 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27542">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">✅
#تکمیلی؛ 7 گل فوق العاده تماشایی در مستطیل سبز روی ضربات‌کات‌دار و ماهرانه ستاره‌های فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/27542" target="_blank">📅 20:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27541">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jU5LjVxZKMs3CVN8nQoTsU6tSG7XpqmAaguLiATVl5ponkvN8zm66KmSLrdm_57rPCJO9a8jDjTS7v1XPSjLemvSlX5ok63KNBsqceX6de-VwQdfsY2snCB8Zc1u1-MH1AP0bJ4_q-gJl1hwVXzL2Jm943bzSM7uCSPcKP1P8J0iACyo1hWGiN_-yuMLHUoQQopEw4Z9v8jZdLc_clBAQrW5St14Ei7S0JQA6G_VKx-LxC_SjlaPUPSX3PhmWRTmiV_A3tf1dKD-CYI2qkePc5avNANm8CRGa1TkrIVVT0sTV88yusVasuCyps3RI-1cgYd-_B_eaqmrOmWkSwkmwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🟡
👤
#اختصاصی_پرشیانا
#فوری
؛
باشگاه سپاهان مذاکرات‌خود را به‌باشگاه نساجی برای جذب کسری طاهری آغازکرده تادرصورت‌توافق‌نهایی بر سر رقم رضایت‌نامه طاهری باقراردادی سه ساله به نقش جهان بازگردد. رقم رضایت نامه 170 میلیارد تعیین شده‌ اما باشگاه سپاهان هم به دنبال تخفیف است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27541" target="_blank">📅 19:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27540">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHAf7PuqAyEs3j7nLMGExFhIwHcfHgZ8BNJF0-ln9DV3cQxr-v-E2elOYh8Ty5HurSjDcY-t8wMkkbytVS-dHb-EUGnMXBVjatbXAoCLlShe7Y-yPrOdV47pAC9RNKeQHmvmUe9eP18m9TNMXPwPiemZlFx5GWNUw1R9cliR1N9aK10Vw7Oga_gYT6CuWm2R8OGotYBtUWzbKcn-NGH0nuuwJoowG8N3o4kdq3Yb5n3U2UIdaFqZ3Ch2w8xBtTLlUDTi6XT0UdJ7260tb_d6MxOXy80JlNiMs1-C1pxcsNr4ebl1-m1qv4WaaWkBucz1Pdh2m8qW85eqkNavmr74dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی‌پرشیانا #فوری؛ بعد از پرداخت رضایت‌نامه؛ دانیال‌ایری مدافع‌میانی 22 ساله نساجی باعقدقراردادی پنج‌ساله رسما به پرسپولیس پیوست.
🔴
باشگاه پرسپولیس دقایقی قبل مبلغ رضایت نامه دانیال ایری رو بعدازکش‌وقوس‌های فراوان به حساب باشگاه نساجی‌واریزکرد و بزودی…</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27540" target="_blank">📅 19:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27539">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57Aw0qXC6wxngR9FP779GuAtR5PXaO12aSdo1FIXSIqGlY3pkjwIoxomOn9x4TpycIDPRYcPBUVcF-55rroogJLgQ7Kvi4ZEPH4xXP6klXFGxMFeewkOntMl5OPtMPHASb8U4IP7zsio-P6nNhGWzngGmhYg4fMqJ7i0nGwUxcReVbaKUVWKmCp3aaBGhrHE1GIYh0kf21wm80XerXvsvwRrNsbGJIXLtEJjIxDSi43BizIK5s4F2HJukiLfDsxQAp17X6aHuM9m0sU0hvoMcS-BpTTEKLtMpvceDKUGPIO3EOY64CIzhBAUMap09m3apnwOj5svGK0GyGrFXhzTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخبار دریافتی‌رسانه پرشیانا؛ بانک شهر بودجه‌لازم رو برای پرداخت رضایت نامه دانیال ایری دراختیارمدیریت باشگاه پرسپولیس گذاشته و انتطار میرود ظرف 72 ساعت‌آینده این انتقال انجام شود و ایری با قراردادی چهار ساله رسما پرسپولیسی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/27539" target="_blank">📅 19:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27538">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aGloovSskvzaluHcF47PUOraKFwEeQZyP_ffBUhJQ-i3TMBlprBG9KhErT3fc-bISfRME_Ghv1t21olYrVCnektEsE4Vd8QRUZACKu184Owkqwppm8yCNX0dz8xF4VnWSQUoulf0HTd_hR1HEOWXhJte-Nf5C9_IyXUo0gSKv-L1TxnUSd-M5akR5hRGwtkqUSPTqszO8jqoavBVX6e6fFbz9rH1z8sUOmMfXc6p7KGMTYXy3FIG4cUSXUv7MHci5Ki8Jav4POPgQhQAvx3mZv_Bbr-QIUi3a95qF9nW_YDKQFvLDopHv6Ieu5Rotskjig4R7w86KxEkZoFJKyiaGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
سه‌روزتاشروع‌لیگ‌برتر
؛نگاهی‌ به‌ ترکیب احتمالی چهار باشگاه بزرگ ایران در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/27538" target="_blank">📅 19:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27537">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1YI0XWB_JEtpE_RooFS3ehofuAJ3rRXg2bMrQt3VkHSImmW3gb9Rx2nX_3x99oKT_QMNsp8KrQ0h11Y3CF3HxvWcYZFfmRURRw8QIn-FoYYpzYKcx7_kFtm8eeGHwfwKE_9_xHLk742mWtjHLLOdmZkInVW_XFm0sZu_tOtgrporHTEszfuEwcrnd1XW6xZDnrsM6lT8Ju_E0LqrlIR64f7BNmyHSz1HOusEVLRaL-hPTxeJZkHBFfLcAp4ApS7JbRu7QGq36tAZH4JpY2x9saQ6yFom9GlO8qCx_jyfaiDjHJStAPkQz2dtXQ-3XKqNu72wYbbvIC01nDjh4L6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
آنتونیو گالیاردی مربی‌جوان‌ایتالیایی‌که چند هفته ای دستیار امیر قلعه نویی در تیم ایران بود به عنوان دستیار روبرتو مانچینی درتیم‌ملی‌ایتالیاانتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/27537" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27536">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ceb12a118.mp4?token=cEv8_r8_zzNqrCJQ2OtY9yimc6OGmE9sH4ajsJr-mkl6fO8byHAMSGUBAvg5TPuNTChJJS9Pb_E_hZSJHOiCx8qBJ5M3jR7x1Pz8N44bJUVcbGP9Jl1x4HBtd3Ur_Aib9Z7ZLn5gp2ABsiL7IxgLXyqlrNTeUEPU-OXZ4FJhWwy7AfgeTEbza0GQTYEmvYAtTvAYcsVgFN2hTDJKvJqq9EaRIIDLonbmHthDynKZ2WMBXNVRXkXIIp5BEOYANkLG7epVgNLdw0nwy22BOsgUOkzGp5e4Oai0e6EeQWj4eb5uLXZfFsPpeAsojZe4wNqHJGLkHbfIdm2mxTZWD1l7dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
جورجینا: به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش…</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/27536" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27535">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaOb43imQyorzrgnWJ49TQy6vBp6HGOO6qxWldqQoi2l3M_Zh-mLFROlf61DGsyfhqtnJALMErsgPAouXXvTwqF0h3rs7cWj-jt7DEbg4vrJIpNm2-JQTw-_3J9nVkCdrGyP7L82mSTJKsYK1PKaSMFydP4VA9LBSTzsvN0CYkm3YPzM0Uri1GSs6eBlJQgc5U2KCPxyIqf2K2TJdyq5qTjebRSutEv4NhH5ZphIuIJw_5ZkE8wjlFtQVsQb5AEc00fEbabZoBS10bWMwyEyvyG7L-RfMiQhDK1CRlKWdmPTkGKDtUS7Pvo-wKvncsKVOLdnmDeVxLtHQQ_5JZqTog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😳
هنوز شانسی بت می‌زنی؟ حرفه ای ها قبلش تحلیل می‌بینن.
هرشب بالای ۸۰درصد آمار بردمونه
میگی نه؟ یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و از فوتبال دیدن سود کنی فرصتو از دست نده همین الان عضو کانال VIP زیر شو
⬇️
👇
🅰
g20
https://t.me/+OSLrSo8D0ck4YTZk
https://t.me/+OSLrSo8D0ck4YTZk</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/27535" target="_blank">📅 19:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27534">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTm7pbjkAUvnOz-wr2Hwh4BMkhNGXD_uHdfVctDdvmGbaXWrgo1tnDH1YisV_e9aMLPaCvP2y3zYgg3-hUZXDiXdf5kczgL3ZHaSLWKeNPapHgAtF5ijztktx6wjTTuzzYv-o57Phrb1bQuKqEJvW1ul3QAKTLEKFxnKe-T4b5QgyT3fZdK5aQxhyoGplhchkwViTlU7g6w710BtzZg2zP7quG3r_piKj97LHC1K8mF0LRSbV9rLYPHSYRnVCyIzMGRrQhKu6nGzJI1Zbbty13NF6WA3VlUHTsDZL4fPdU0ye_8QI6QlGdq25e10e51l0MqtIfQ1HIt3shCoFYHPyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#فوری؛مدیربرنامه‌های رامین‌رضاییان ستاره سابق پرسپولیس، استقلال و سپاهان برای قرار دادی یک ساله با فولاد خوزستان به توافق نهایی رسیده و اگر اتفاق خاصی رخ ندهد بزودی باشگاه فولاد از او رونمایی خواهدکرد. رقم قرارداد 65 میلیارد تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27534" target="_blank">📅 18:38 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27533">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqrbbuIS0eFlYGKIc5RJWnJYzmPgPmqHUL3UaY1Dz3u7HmvkGp0pUkQMWapOxGnUQn61czPvSmAY9BL719fokLtnYLuNNzxolqHQgbozie5omHhA3J8CCYw8J5o-z4g-2G5DR8C8R-Dj7b4Qclb5S6Ia8uGfmh6BAMUmyKQKrb_-ErWjOzomEts8u3qqAiFzyuX6g5AHUQpng_XVzuxTI7eSE3ZCTTmGNJV1AIrne8CtXJMhV8QfPEr_YMI0lMZsdAFh9AtiDx9_F0EG88r_zng81oQXU53sXc6hs-sgLrN1VDwUUdC5ApAVevdhrE7dO2gVdBchs3stDu3dtHsdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/27533" target="_blank">📅 18:28 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27532">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e61nFTOXuevQrnPDApwNu4_0o3bVTnmWkCQH-74iciaS5Nc7YI8ITKgfMJrbnLAdHxUOZY-tZuur-QNol4DkWBxvB8unowCX22bGEFBSx742USbV5Cxun4VLa7ZpAYzs2f8FxgaqNof4I3g2jkaY9DwZLwaHqbz5td__Wsy1lnZj7N2ZPk5-DfW4Ax_hJkCoSlJlt44DN-UbE7AUY6CCxr_XcTf59rau-IA0UuipuISiQe8MAh93baxuXTaCW-YZYKetnBhnVuWIzmB1m43dXpbnZFwtXJ9x5SHKsqJtwGYAOi1-h7-cio5wSkU2i6LWlAgu2wUtptaemP5l2pQEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
جورجینا:
به‌‌کریس‌درباره‌درگذشت خورخه مسی گفتم، این‌خبرواقعاً ناراحتش‌کرد و گفت فرصت پیدا کنه بامسی‌وخانواده‌اش تماس‌میگیره‌. کریستیانو هم مشغول برنامه‌ ریزی عروسیه و در حال حاضر خیلی سرش شلوغه، اما من باآنتونلا تماس گرفتم و تسلیت خودم و به او و خانواده‌اش گفتم، ازدست‌دادن کسی که دوستش داری میتونه آدم رو کاملاً نابود کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/27532" target="_blank">📅 18:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27531">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/27531" target="_blank">📅 17:52 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27530">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V0uj_KN8AD3M1YqvDhdS6ME4d5qQTv2FkFpGnZdc3_Z58jgiuXdOuaEk_UYonEPn3vgczi55z2ZKUis1qjapre5U2NCA4WGrFjoH9NQ-MmiufXmZGDcRL_E4DmnMTnWDCxGgvVtVfbLJZ1do4oF0ARAWH8slQUHTqZVa-1GuIks2nJlYWlOdSV8FaTxh--N3Ol24Zy-alOkNNad0iTkXSY5ZxHvgKP14puhw60WWXXtYQZAcSSTD6KXv3UwwmFAmIwYGBFs496GOtexLebh8JS3NOTBkr5InJKPXwWtY5qDKdMPoGOAQpDDMR7D9LJdg0w9jPyLbbeO5n3D7Vwg5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی برای عقد قراردادی یک ساله با سپاهان به‌توافق‌نهایی‌رسید و اگر اتفاق خاصی رخ ندهد فردا قراردادش رو باطلایی‌پوشان‌امضا خواهد شد. ارزش قرارداد واسعی در سپاهان 10 میلیارد تومان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/27530" target="_blank">📅 17:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27529">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uqIGVvjV8rk11gWKoAcz0mDHTg82nII8dTN41zSTTPiwlBpDir4wByXQcwpo6t3jqrsmyUNKk0SpJyGUuTHUMFaG_So7r2SlswVwNoBFFQVw5Bs3OX9qmxy-Gae5Gsco7GEiAUEk30P_6YnvCU9b26iAc6ZkRSZMvK2uWlduxdMqN3AO5G8KIZdElhojZkmoi4dS7-wXSaH4CvRvRqiSVB7aFtMveWFKODJbOODDEOqjeyinqlqmhA8ZibXy9UUdHK1aihrCQHcl5e2a3u32PuqVjGKgBB2zqo4FDyG0r5whljjR4s6NnlNosD9j8U9qoLfQtVpcXtdtK0-WAKLKwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🟡
طبق شنیده‌ های رسانه پرشیانا؛ یاسین جرجانی مدافع‌میانی22ساله‌سابق آلومینیوم اراک که فصل‌درخشانی دراین‌تیم داشت با نساجی مازندران و سپاهان اصفهان مذاکراتی داشته و بزودی راهی یکی از این دو تیم خواهد شد. شانس نساجی بیشتره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27529" target="_blank">📅 17:25 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27528">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CcCoE78pJNNVokLqnTqw7KNKp3tbMLE3eXkqQRNnTWnB09w2N_qbzdgjlvYLKEBrKTlgL8g-bM9g5kxtdm3M86KOh8QR_doX7X7_CvtT9lj9vXZK2UNhNB2DtFKA6bIvp3M-IXQU-w3cWIi9PbjwqfDD_0QQgq44A2XxMkOS-ub_xiRPvG4-Lsv_BYQpQyB43ir56yNjbaptjRDHr4ioPpRkb-YBGrk3tJnXdcSJ2WeCKxBwNfWo0zyGw9kk-JFUxlj5OsEFL2-x5nPtafT-RgjgOJ8Z3m4qzxJIMGo1Kjx9LjH76YF1ydoujkofL2mBkr1uHRg6Df-N0HxBX7B8ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
🔵
بیانیه حسین زاده رییس هیات مدیره هلدینگ خلیج‌فارس خطاب‌به‌هوادران استقلال: استقلال تحت حمایت کامل مالی هلدینگ خلیج فارسه. در نیم فصل و با باز شدن پنجره قطعا تیم رو تقویت میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27528" target="_blank">📅 17:24 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27527">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V67aP1a_U3k173OfqWWGeZ9w3G_brTVtK3iL3ULt2ZHqo2VX0kbv1Vf2R73DIto3FrKHpmBhfGISrEV9cuAVmRgsMMglq5fNZ8qqeFGbuA41Hl4m5WLC4HvnLDk03zLUSlLZ_uuCjmEx2mWEYbi650I502uj9ZCF9mWtgR4_4IqZJYCCtNGRkd6f3DcHNm0a8MuGnSV0Epo5F1VXtbEFrxArr5L3uHWfTHvMx8hun1ELsT4TzdEDDpKgckE5D7Ypabe-HaEAVHkXJCHJVuSu3aHIWiS-krGd1kAwnbZFlwFlbUWHyI3ZnMa6GbDv9cee-0ko9rzrfABqcq-77AgjXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق پیگیری‌های انجام شده مشخص شد؛
باشگاه‌جنوا ایتالیا باارسال‌آفری 1.2 میلیون یورویی خواستار جذب آریا یوسفی ستاره 24 ساله سپاهان شده و این آفر روی میز مدیران این باشگاه است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/27527" target="_blank">📅 17:08 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27526">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZ_xM4MKk_wcx7guv7_FFspK9If7Akc4PjmA0sYmQY4xjziYPtvtPZKx3kOZMS58Fo57c3ABzqaeJfKkZuZZEDA0FrEzaGCNz-gCZPD3Ac8v-Rg_RT21yCEh4Dh_nMsj3H70uc6wIelJY8-4-6UVCszlvnTjP715IqLtyYTxQbEVdjhzchzISHCDZAUXenwTI87wY-VEs4S8z1BqYY-_OGbO19lcKPHx_Ji8rysdELSMAmWkxnVXrJT0qh4MEyAhrVXeidq4cgqAW2dj_FZ9H4GmjTVQ8GoSwpxp98lVN2F8TYPYKy_Ew-U8QKMHwNg0pICC72DKd1DfrhjWqKdxBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇪
#تکمیلی؛روملو لوکاکو مهاجم 33 ساله سابق منچستریونایتد و اینترمیلان با عقدقراردادی دو ساله‌ به‌ارزش‌هفت میلیون یورو به فنرباغچه ترکیه پیوست و شاگرد اسماعیل کارتال دراین تیم شد. کارتال دست گذاشته رو هر بازیکنی مدیریت فنرباغچه نه نگفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/27526" target="_blank">📅 16:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27525">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=n1Me4pJTQjVDWnc9ah1rj42wJjHxZDIm1zpmG68AOiD0ZZ8TmnE1pin_0nZcgJvKQLNIsg3tpJO9Pg3_avGQSlU5K2fVmWq93cgTEqVWmJ2NBV4MP9Omo0z5jW_47yIFUBIlkdDSHqpTZL0NQMsyHYrsLTiblWNCcXWTyoG1lB0RRRMnuY9mBw5vpk5ek04rQXxtSTVtK6Ggo8uAj2OKog7cUhs0Greq7VhQU2nhwS3Kw-pNHgNhesj-wSs1WLFxKxRDDt2bNRrxZX_OmVF7IJNUk9XPxbU6WqqmAjIXHrz6bSnDq-tPqcsWdQfmp-cddRu2Ko8XrGdpk3Nz6Rmyvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed2d2f027.mp4?token=n1Me4pJTQjVDWnc9ah1rj42wJjHxZDIm1zpmG68AOiD0ZZ8TmnE1pin_0nZcgJvKQLNIsg3tpJO9Pg3_avGQSlU5K2fVmWq93cgTEqVWmJ2NBV4MP9Omo0z5jW_47yIFUBIlkdDSHqpTZL0NQMsyHYrsLTiblWNCcXWTyoG1lB0RRRMnuY9mBw5vpk5ek04rQXxtSTVtK6Ggo8uAj2OKog7cUhs0Greq7VhQU2nhwS3Kw-pNHgNhesj-wSs1WLFxKxRDDt2bNRrxZX_OmVF7IJNUk9XPxbU6WqqmAjIXHrz6bSnDq-tPqcsWdQfmp-cddRu2Ko8XrGdpk3Nz6Rmyvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
دخترخانوم‌رضارشیدپور مجری‌سابق‌ برنامه حالا خورشید شبکه سه به این شکل که در ویدیو میبینید پدرش رو به مناسبت روز تولدش سورپرایز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/27525" target="_blank">📅 16:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27524">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U156W-p9QxzxVp_ytHA9cy5LyHgKbRXj3oazYe9D8qhkSohibheBqb8lBrrIrodzvrWG6Jd653We0MHugtQ-FEfKR7HMOInruinFUgxQAV2gNQKbAdu8xAFB-_4ixVwytCFjpDxHPDB-gmKGqisNyZr1a66rt-3q6BP-JowDfNzzaZfiWfFtu7jW6BjV2oVujAjXhvv-_T0zgYMQk99rjJiGOgozwsqs-t6t45QC3P4K_MQjQQP9K44Zgq6yrxBsBHuoAd680olw8EgPVcdddCjVXvxfNbZLlG458_wiIo7RPDEv5nK9z0n9vdRSRjyPdtwwKVj50ldsihq3-lZo6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/27524" target="_blank">📅 15:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27523">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">‼️
بااختلاف‌بهترین‌ویدیووترولی‌که‌میتونیداز دعوای علی دایی و کاشانی تو برنامه نود ببینید؛ شاهکاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/27523" target="_blank">📅 15:34 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27522">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-yA198ZPnX9EklAdHbhtos_NQ27QEqobeYPABnuz9wPKYT_LgMPy6hRJKE5177aT3Qnu0HyWWXb-DTa8g5lsOXhw61ZYjx-ziWrUrXeImG6srRJUWP3szcMoSEqLr3iKPvf1HIxxhgSGS0fZJsCAW5uGgU5XFRRFIq4yQilOqmXuEE4PvME59VG-0wVJgSo6-lfS6HVlnQ4y_60G3lkVG2o7w4KvMRGegwz5L6U7RZ3qf49yJbVJ66sRrnOUzWT37wwjfrWGwVI-pTg92tgZCvbQ4juITX4PUCIzsXDbL97ql7SkruRFUcI9wOTdNcAyt7FhoynY_Mq1gzmAHuIrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه افتخارات کریس رونالدو
🆚
وینیسیوس جونیور بعد از 9 فصل حضور در تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/27522" target="_blank">📅 15:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27521">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxYOBbUMgl6xcTGjDaKWoiyFtVHZFUXAkFzvFKwBBodjm_Y1kyb60zqdNcSd_rRIxd21cn4hhHfGxh-P2SzZigZLSZvscAPwhZ2nYsLMaA1AYdMV-UYyOxn4aQIne8kW4xIJSfVMNx-tVC4iCiOLRL6IdopFPZDTS4jXHKGVRVca3oA5M4Clwl6cuOEZJk58nvr6NttoXSyP0dVLME52Tx9pdGDneUwJrZt4EfLgupnWlLBnk_ZrvZzpXF-KYpoi1VQHiZ9NFTkPR177CCRtiGKHbddx7FALrqEumRr6Z213m8G7y3CWYLPf1kiTc28ullYJui07fDYAnzFV2l-CkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بعدازجلسه روزگذشته مهدی تارتار با مدیریت باشگاه‌پرسپولیس؛ سرمربی‌سرخ‌ها تیوی ییفوما رو از لیست‌مازاد این‌تیم خاج‌کرد اما روی جدایی دانیل گرا مدافع 33 ساله باشگاه پرسپولیس اصرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27521" target="_blank">📅 14:44 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27520">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RScRuEFgJu_LLuu_gXBsCKtQw26LEe7kbhj_g29XAJxQ7cELIhiIZKdxgX02iaYdmOKe3AT8Oi9qBVqfkkgSU-hIUJ9rvgo6XFfMCfbqiz2_LKR2PUeVvSrcp_zyeRJAtGfchYzpLC0PvwY-5XvdCVWC_xJ9ybdPPvSQHBfkhya9zs-YP3SyFP2dhJ5LE5hZ4BoQEx_uKKNB-tBGSa34R6r1q5m4ScCuIbgCvlt3GCZu2rLSElYENT8DopJBWYTJPBEBiR8A_-KT6T9_D1J7gRs-90eOk7XBs2cwbhDBf9r4DuGEomYDhm5Qoecvzvv5RzvaCOb6C8gqmYrreQXqrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
باشگاه استقلال تنها 10 روز فرصت داره تا طلب پنجاه هزار دلاری زیلیکیچ وینگر سابق خود که یک دقیقه هم برای آبی‌‌ها بازی نکرد و احمد شهریاری اون رو به استقلال اورد پرداخت‌کنه درغیر اینصورت آبی‌ها از چهار پنجره پیش‌رو نیز محروم خواهند کرد. پرونده های ساپینتو،…</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27520" target="_blank">📅 14:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27519">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=qCaV-r98Prs61XACggSbmvQQARzIKCsRyNl9LibyGfxgxhp8uMbhzNbG-ox3HtEYM5CQ9Y1OiD1nBXFhq8zYvHxL2jk1asJh-ofRTlfDOTrarKF2p7chaXg_DbEVA4jyiiY4AwsPhWisYmocMd33ptTIHjUdnxeeEBuhZ3vLVntyJwyaiGLk4CR3FzgO4gtJmsCRc9W6ZbbH2VtJ1ADD8sMGzhSrzPOgevFPWsfT_ldmiWFem0Ziy8zMdPRqL5WNL99Cc8s2ES5n2C3nNXQvETzTUD2EL4WnJzd4vbBiE8sBu7xuN4LyPsm3SVkbJTH1c-bqEIv31vLAt7rLNNk7zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a376b4a33f.mp4?token=qCaV-r98Prs61XACggSbmvQQARzIKCsRyNl9LibyGfxgxhp8uMbhzNbG-ox3HtEYM5CQ9Y1OiD1nBXFhq8zYvHxL2jk1asJh-ofRTlfDOTrarKF2p7chaXg_DbEVA4jyiiY4AwsPhWisYmocMd33ptTIHjUdnxeeEBuhZ3vLVntyJwyaiGLk4CR3FzgO4gtJmsCRc9W6ZbbH2VtJ1ADD8sMGzhSrzPOgevFPWsfT_ldmiWFem0Ziy8zMdPRqL5WNL99Cc8s2ES5n2C3nNXQvETzTUD2EL4WnJzd4vbBiE8sBu7xuN4LyPsm3SVkbJTH1c-bqEIv31vLAt7rLNNk7zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
🇵🇹
ژوزه‌مورینیو سرمربی تیم رئال مادرید:
هر کاپیتانی نمیتونه‌رهبرتیم باشه. رهبر تیم رو نه میشه خرید نه میشه ساخت، اگه یکی از این بازیکنان توی تیمتون باشه، همیشه یه گام از حریف جلو ترید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27519" target="_blank">📅 14:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27518">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtYFOH7RE7tkCyGb3JvP4WClXqKsGSvP5WP1bw_QH5E9Akka2enfM-O989M4Z4ymOLCAfkr9zlUzd6BiAfyRkglLHWWVWWGgwKylbl4PqOBqVof3gE3-SzQuQDB1YVfnTB84lpL7a7P8p7lGK3YkAjjKlwka5PuboNByDH3L7R0hbNsZOr0WdRbb4Lj38Hi98dBLYC5RCH-rHk4keAKWTHO2MFcIwfo2XV1kLBGEVHwDLQAeD0TLn6sM_3vyiK2InZerlZS4cZp9-MOQxcKPwV4Xl3Qp1iP8xBQeD8xK9A52hs4Xy58gtlzwRx-kJ6o5_O-cPPgJvU9DK1BMi20jRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین‌رضاییان‌ستاره‌سابق‌سرخابی‌های پایتخت: ظرف 48 ساعت آینده از تیم جدیدم برای فصل آینده رسما رونمایی میکنم. در لیگ برتر ایران خواهم ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27518" target="_blank">📅 13:39 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27517">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SrwZkhwZXvA95_bCL9ySvE_McvdPEVp1RBVzcQ2hbV_GBThWNnvzBNLdpgJZCiVnzqLEX4Hq_FvTGDsKJR7adttWF8Yr00yxrSWs0NrwDKDD4e6AcdaWh9GoLNw9SMy7zEQC6EiZH8Fw3OuPqpXyqp0qy5IyuXX_EMRoz837gOe_dSe3xFi8ACfMlh-6OE4OXUUfaWskveMJjTQkdJ6E-w_lFWSqnqGBUAZ8c3dZkSl082-rfS-P_RiU_l3n76xXRa6I4Fa7LfYQ1eCLf9aDH89PC89ClgRDwepmO-lHCa33Mh-zRhxHVDU7ImjG980gWl_RUNEXT6BQaz3kUXHrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇯🇵
مورد جالب دروازه‌بان سامورائی‌ها؛ سوزوکی دروازه‌بان تیم‌ملی‌ژاپن‌پدربزرگش نیجریه‌ایه، پدرش غناییه، مادرش کلمبیاییه، تو آمریکا متولد شده، تو پارمای ایتالیا بازی میکنه، تیم ملیش هم ژاپن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27517" target="_blank">📅 12:57 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27516">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🇪🇸
🇵🇹
هفت گل تماشایی از روی ضربات ایستگاهی با هوش و زیرکی بازیکن کاشته زن رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27516" target="_blank">📅 12:45 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27515">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J35B3tTN7OITlJfXrelHsNLpAEbV3dMjiA9Tb1KXx0Gt5TzpTZjepy8_cdZW5nlSNqfy2XcQX9XhW6Ie_W_qcYXRFoBkSv5w8Wa-yjyYB0ACqHhXK490-SsX1EGYkBhux2iH_ZZOOc2jafeZEeSqq7dmDyC5BBqlwrIGLmhrhUO9_RH1Wb8kQp1U0PCSKk76OukLemyqzLG9KvbhuDI2No-zCbuW-F32Dr9roKRYeQ3LkxExWLeS10yvUf3fP-0AsQkreHQLWtJLz0tlBdkrqW0gjFikdBlRPeifdognuEdwJuK_CBg2fELPR5g2bruDr_DH14qOiI2KUmIIDL7yBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
🇧🇪
باشگاه‌‌فنرباغچه که سرمربی‌آن اسماعیل کارتال سرمربی‌سابق پرسپولیسه برای عقد قراردادی سه ساله با روملو لوکاکو به توافق نهایی رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27515" target="_blank">📅 12:23 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27514">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DX2myvtfnrdStmaLD5_kX0sZvD5Rh6IguOVgTY0hkpsXrZYFFS06Wnt3dhu6ydfnsOWvROlUOq6vAK1oxO18JeXpSOtYXF_AQ0kfybQjH4B3TCnVh_jGhysTdznPPcHBPhwtfe0WYX8Nn9pwrdaktRacfaUk7AJlMljk4msdhAykQzPF3ApLYP1OMTEuXy6Rk_pvR6pDbZJW4KIi8FW9knJI7dGwZwKBgcQupMGJadTuxyVIkH9EMKKhh91ViU_ypX-sDpQ8QmtF05hFM-23UyEJgUgdytccrHJIOGsD51SizcBnhENruljfHssl5M7sGHXgupo2coOy-MWH56uXvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
سانتی آئونا: باشگاه‌پاری‌سن ژرمن و بارسلونا برسر انتقال فران تورس به‌جمع شاگردان لوئیز انریکه به‌توافق‌کامل رسیدند. پاریسی ها 50 میلیون یورو به آبی اناری‌ها خواهند داد و این‌انتقال‌نهایی خواهد شد. کار دیگه تموم شده‌ست تورس پاریسی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/27514" target="_blank">📅 12:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27513">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWHO341BQnB6oaIU-_dbfb2rAT3d_LljdRdx_olmD45DExUNjF_2UpzX7U5F0zg0DN0QH-kYrp8qw1z0u4_btI9k56Vm9Axu2iSqIwxi-a9HdOkLdiDmeGbdwpKsmTSQca2EaSM7kXHkU_xXXbGSg9Ul1AIjEgE8-Q8OMMgrYUGPdcx7_Ez_osiHAXLLgiKbYPFUjJ9q0PhxQT00ogxf3h2kBjU0FFuOpwVKEh6Ct8Z61EikhIqvoQvI55T6HmCVNwetIGrN1jMQ4RkMw1sFpeQFOx7BGVmIai8MS4HEUpDQj6nq5kcaP_YHdQUUjUCtCuM8-QOMFAiD7sRRmqhK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
باشگاه المپیاکوس ظرف 48 ساعت آینده با مهدی‌طارمی و مدیربرنامه‌هاش جلسه‌ای مهم برگزار خواهد کرد تا طرفین برای جدایی به توافق برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27513" target="_blank">📅 11:43 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27512">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V2wCyRNswqiAFs_O-vnSkVEkcPik5btmvdoGMMFbt5Iu3AorApfEvyxL8hT5YNOT08NA7Cem4KwhX3unAeGodBb8R8Oqa0cySme2htyRZ8elEbAzNz6oZrStNCwLvkq9JddzV0HKvsK8YMBVtzBvUQBNJZuft9OBzbNcKA5_xstyp15DGaMar1XZXzq_H-Xo1eQ3vJhJcmyZlQQC6pBMzMc73Mq8VvE7AMHYiCpeR7yJtE6Qn9-gYz3WwX1QR_FYeOYbcL8ayJA4MVQ5uR-TFUF2Pg0ugWgtU_4NHRzftU1kdP0Lnnnraf0LKjbK90zMytmJwkiayh1h9r2i84m4UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
رامین رضاییان فوق‌ستاره‌فوتبال‌ایران امشب ابتدا به‌این‌شکل‌وارد برنامه فوتبال‌برتر شد که یکی از دکمه‌‌‌های پیراهن بازبود که با تذکر عجیب اتاق فرمان مجبور به‌بسته‌شدن دکمه پیراهن شد. داشتیم تحریک میشدیم که خیلی سریع دگمه لباس رامین رو بستن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27512" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27511">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DCshaN1sJPcx8vT6h57M3V35dxVSe0RTDKGOnn9WeW4dZM8CLofjRrqtJFemfzI9FHDFZ9V3qUOAHGivDiWpINGMfiY2hOSAsv92rwoL5wtLriES5nwHW1dbCigxtnLlmuSqOIIyulVlG_RGHAG6r791ewwPJvfplbqLaFyRYghwI27ielryr3lJli_iwIwI2HXD4KrazVK2K93DEXoKMqKj9PXGD6Q3UcNC4dMBs0iMtIw1i0mCyY3INvLIAQBBoW0RUZLZztMsdJSVhae5gmBLFY656laQCEXS5lAWVv6r6nt8Gy6Nr1wiyuTQ-XZay09TO7YSbVKKVGO7OpKz5SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aeb87b4574.mp4?token=jrOtY4oyZ3FsoXL0NRWh9Py0vEOVlcMu-NiRE3zqaYOI4_eKouTGBCVqmvckfTr_W0u8Jxpk_n2r9Mdg1r9cegGGJ6e2KOw6ZiRCO86ocdZBNwExrcsDjl6opZmhgb-sgzRB3rEylhPjYsRDZ06uwE7nmxHb4_-Bxs7IO28MHme1pHaj_AltzCcTE237fMDfrCMnIJQUxDgX4751lw49D7HLkPF7cmrrYXfTzAdVGrl4JuYg7-w_4qMPyXUbbC5ljPk-eoApidsVzktDKhhKzsephYeXTjcnJALPdUZkMK3NJRRvGWaWjKO7BrtTCVXWQxVr9djh9bXZK-lHFve1DCshaN1sJPcx8vT6h57M3V35dxVSe0RTDKGOnn9WeW4dZM8CLofjRrqtJFemfzI9FHDFZ9V3qUOAHGivDiWpINGMfiY2hOSAsv92rwoL5wtLriES5nwHW1dbCigxtnLlmuSqOIIyulVlG_RGHAG6r791ewwPJvfplbqLaFyRYghwI27ielryr3lJli_iwIwI2HXD4KrazVK2K93DEXoKMqKj9PXGD6Q3UcNC4dMBs0iMtIw1i0mCyY3INvLIAQBBoW0RUZLZztMsdJSVhae5gmBLFY656laQCEXS5lAWVv6r6nt8Gy6Nr1wiyuTQ-XZay09TO7YSbVKKVGO7OpKz5SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇦🇷
5 سال‌پیش درچنین‌روزی؛ لیونل مسی فوق ستاره آرژانتینی درانتقالی‌آزاد و با قراردادی دو ساله ازبارسلونا به پاریسن‌ژرمن پیوست. عملکرد لئو مسی درپاریسن‌ژرمن: 75 بازی، 32 گل‌زده و 34 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27511" target="_blank">📅 11:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27510">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSqqxO5ZNv_j9jRHqzOZX-tWeYXRy2RObSxSsBPNUOrWZpB5Rq1XrhMJhYONLNytyGUd-Wzp5ccFA5lvYVvmG2dQC4NT6uF6isszox6gp993zx9BFHeifFNhSf09uGBtdBLijBcdcJJgWR-yvI4L0xh2YJHr_v9uNF7jTpMnAdeiLXJEsYMZ95ZjHkrdM7xEsqtQG8-pKvlPHUpzaJJy1ruO3iYIQSpAiYcxdD_vsg5P6wWIH6zjmvds6m-RpfwA_btABk4z5NMigTp4Ajxx23semKzddzRnDfAqeoRCTCuHthgtPRmpjmDR_4pEIX84Q86HFn1ji3A2jn3tqeOjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
همین حالا موجودیتو
🤩
برابر کن
❌
☑
️
2.5 میلیون شارژ کن 10 میلیون شارژ شو
✅
برای اولین واریز تا 15 شهریور ،
0️⃣
0️⃣
3️⃣
درصد بیشتر در وینرو شارژ شو
🎁
✅
به ازای 3  واریز اول در وینرو به ترتیب 300 150 ، 75 درصد بیشتر شارژ شوید
🔊
با شارژ اضافی بدون ریسک بازی کن سرمایتو چند برابر کن.
🎲
ثبت نام آسان و سریع کلیک کنید
✅
درگاه اختصاصی برای کاربران
💰
✅
پخش زنده ی تمام مسابقات
🔊
اپلیکیشن حرفه ای
📱
🎲
🎲
🎲
🎲
🎲
معتبرترین سایت ایران
📱
کانال اخبار و هدایــا
🌟
sr20
📩
@winro_io
🎲</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/27510" target="_blank">📅 11:20 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27509">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3C9U5pfLlI_N01DL1SDOaP4F3dP6qsyKzPd9Ze-Ohb4BIXOS1xZ-LPUfH0gRDqGhtzd8F7mKBLB_YYt1LY89Ya6OI9GHH6mbUR4QM-WHqjx0axrbyyEmVpFCDnU0Hm9MmyjrqTyNwX_-fQUq4HXlRfquUPQv3QKkdxLf_JEx7lc4ASwnoIZEuovBlXjQJJKMh7aZ8NSC0ZWgMZxeiBFtQR0MNw_2vGzDf1SC2NA6kwaifMdO3KvdFsxSCRFn8d91Qy8JYbmTvHjGdHDL9eV7y4CxwF1ZaqFNa1TqGmLyZ31iMue8sO75N4t8Uc2o8d8wOQPWh_9dYfy6J2Y-vINMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی تا روزچهارشنبه به‌باشگاه پرسپولیس فرصت داده تا رقم رضایت‌نامه دانیال ایری رو پرداخت کند. درصورتی‌ که ظرف این 48 ساعت مبلغ 120 میلیارد تومان به حساب‌باشگاه‌نساجی واریز نشود این انتقال منتفی خواهدشد و این‌جابجایی…</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27509" target="_blank">📅 10:47 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27508">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ETCA3FTH4-HBK4YxwGxcBx5l73zZU8TRZU04z1Y0DJeBfvawI3yoJQuMQGH9MQ7EvpY-bwrjVu6pWCg_Js-R5vh42Wyp6N7QFH52G34g7yJ3bGpCLcdOqo75-cPlhd1jV86_L0ep5LWGycXfY_9a3n2rr4aQzj44JN0Vy44pdHl2sstmpPjDLy4iVAG-vquOHa1QW5roxGzYlXwCftwxV3lJtIxqzMkU3PeC14JaR7Q_LF4-pwPd-W6lxegsPjctvcf1uqjzMxr8IFjmD0Wx9RPcdm5z_4p3ety82OJNTHvXDvbL7BRVApWIw8-c1LtTRpa15kajZ8Xojl-Aq0DsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مسئولان تیم نساجی: دلیل نهایی نشدن انتقال دانیال ایری به‌پرسپولیس‌کوتاهی مدیریت این باشگاه است. برای چندمین بار با ما تماس گرفتند و برای پرداخت رضایت‌نامه 120 میلیارد تومانی ایری اعلام امادگی کردند اما موقع پرداخت تعلل میکنند. بانک شهر و مدیریت‌باشگاه‌پرسپولیس…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27508" target="_blank">📅 10:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27507">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=BqpxHyd-DqOjO0u-Q3_dziugspUBIGbbZ0Ufm3jERadVjGprV0fiQFwC9BP4LuLavBdb8trIlcwVuwsezZlYxQcH2SqipZcaQg9Vv4xnLHF3pOtjemme5c7YLP5FnKLgGVeixePaX6Q55lmH-WR9Nb0eXcqCnsZ6fnAP804SzD18nYFkdFumgtNaRl8mAzXfVmr5xYxiaiUq4HcVSwhkF9xT7iNmronaubxWrRAPeUPGdd11-TmxLI7Lp18QdYGmmQ5m8GqUP0wVQTD8v2ub1KS9CKhSyNiHsRrh6jThUW0b2ocBnG3SSfQS3fCvZl6acS8FnOophtfoTkqdGP7PPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6296bc604.mp4?token=BqpxHyd-DqOjO0u-Q3_dziugspUBIGbbZ0Ufm3jERadVjGprV0fiQFwC9BP4LuLavBdb8trIlcwVuwsezZlYxQcH2SqipZcaQg9Vv4xnLHF3pOtjemme5c7YLP5FnKLgGVeixePaX6Q55lmH-WR9Nb0eXcqCnsZ6fnAP804SzD18nYFkdFumgtNaRl8mAzXfVmr5xYxiaiUq4HcVSwhkF9xT7iNmronaubxWrRAPeUPGdd11-TmxLI7Lp18QdYGmmQ5m8GqUP0wVQTD8v2ub1KS9CKhSyNiHsRrh6jThUW0b2ocBnG3SSfQS3fCvZl6acS8FnOophtfoTkqdGP7PPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
شماره تمام بازیکنان رئال مادرید در فصل جدید رقابت‌ها مشخص شد؛ دیومانده 25، اندریک 9.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27507" target="_blank">📅 10:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27506">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQ9ScMUZ4eWO9i_JvoJTdLbUM3b2mEon5UCEegKr9rnj5wK0KsAhzhVlW18Zq-FVbNbq2315DaO6HRomIDhwy6d96nh6ArtEdJS1yfsS0mVx50JPOBMna9wBaJiNaKR7nRedvs_TYQxYAqHroYUng7Gbin26pjWs2NlrP84eE4om9yxzEHH-mD1aDlLTQrGH9h-sr90-W-KLotHAylJfg2W-bHpkX4TjYaJjG7FxP-eCq8EVUlBOFyCZTX4V9vcRtD7JUKBp6K9JqrrXgbBRzzutJiCNLddCy-XWwPRt6Nd0AczOZrSZZK_WV77FFm-jeTEvz-w3lZwVAYfYTMWjUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته اول لیگ:
موعود داور دیدار استقلال شد. بیژن هم قاضی دیدار پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/27506" target="_blank">📅 09:55 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27505">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKEc84rLIyhEmx7grXv9oTyFFgE-_WmjDq8fdw9Tm_AXY3EwD5JkTLU7CJafgfRN_iH6DExReUm7zDE6b7HNcbpuJ80dh4MuFBhphXfkDHVTR6RMLMmi7b981E_sl6qEZOk52lGbLCpRN8z0fEtKIbRePcxN4M-dZI4BOFWMtspFYprWWjx-bIBBr27eXYeD-94OInewRSQnqN5ccBjT5jHj0UbItUCuEFmWcDmms1ImofH4qDejEYg3qUbmoL5bAGLztuSS03z0zesTtUFhAfY7tEfznitaK8I1vj-I1k7aCHp5zthye9HaQEdAj4ilCIoaoNtez1URcFEThdmxGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇬🇷
👤
مهدی طارمی بازهم‌ازلیست المپیاکوس یونان خط خورد تا در آستانه جدایی از این تیم قرار بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27505" target="_blank">📅 09:36 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27504">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=GMHXS5JUsGwUz9APrcjrx5fyfISGn73kUNRVtgPihtWUWWRv84jgs_u_O9YxHAVqenocVS3cm2uaxpjvTQ8IADjRO30xtSwu-nE2X8lHWMLWNvv1JivJkMEaCDsoo_YZrN0ULJF9Zb3hteM3NO8__Q-hPPJX4-aWEkrp5iQULD3lxemqFHh3DqULxxLsrE0L5PtlNxz7543A3vJ0EjdrplgKQWZRPgbqmCd6LdD0HikosB2UZcPjRVcDhxZVsUgleJCeCvcWrkm2p71SGpod9zzugRLfRFLNs4648bhbGl0OX_US-EOogZs0vIetCm9t_qx09vC5UECFSvFP6PA3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83568bad0c.mp4?token=GMHXS5JUsGwUz9APrcjrx5fyfISGn73kUNRVtgPihtWUWWRv84jgs_u_O9YxHAVqenocVS3cm2uaxpjvTQ8IADjRO30xtSwu-nE2X8lHWMLWNvv1JivJkMEaCDsoo_YZrN0ULJF9Zb3hteM3NO8__Q-hPPJX4-aWEkrp5iQULD3lxemqFHh3DqULxxLsrE0L5PtlNxz7543A3vJ0EjdrplgKQWZRPgbqmCd6LdD0HikosB2UZcPjRVcDhxZVsUgleJCeCvcWrkm2p71SGpod9zzugRLfRFLNs4648bhbGl0OX_US-EOogZs0vIetCm9t_qx09vC5UECFSvFP6PA3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مقایسه‌درامدبرخی‌ازشغل‌هادرمملکت؛قلعه نویی یه‌زمانی حرف خوبی زد گفت 40 ساله هیچ عدالتی تو این مملکت نبوده از این به بعدم نخواهیم دید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/27504" target="_blank">📅 02:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27503">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiGLAc2AZaG2Mw91pjxU7hbqjS0igaSt5eiLwhFYN4rizN5o3FzalvQQR9QOxT7J6vqzZydCcOMo1n7moNvgO11FnjDLvVZiWVGb6qNMBlk0ivjQW2ng-CjjpgAfo4te3tHUaUFxS1q7YvpXJW0vYEzqfN-dLWcRWSAHfvf2wK4hNS3YqjEvR0tA64IRWaSu9TdyghFWdLNZdxG_2a_heS7HLZS6ikOZsgij0h28Vd7VjcYYqrzmi7nOafjytHOp5Kfc2NU3acAhXitGRXaNATW_INUmlYITyNeKNDrZXAWLZK3444KdwqjUoUXi31JUtG5ReS54EHlBoLEujFu3Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
الکسیس سانچز ستاره شیلیایی سابق آرسنال و بارسلونا: من‌درجریان‌اعتراضات مردم ایران علیه حکومت کشورشون هستم. میخواهم به مردم ایران بگویم که جهان صدای شما رو شنیده است و قطعا پیروزی نهایی از آن مردم مظلوم ایران خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27503" target="_blank">📅 02:29 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27502">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=svenWz5d5YCC0vLbfryaMF0AFRgGOJaVj1GUY9slIRWj6JVY8vfHDV5-89eK9XC1AMorsETzdpdEIn2J5MdF7c3an6wBckEMpzPn0W6Jnwj6w7W79R4WxgDxqwT_a8maDjxA_udcW-D-iEmxKQ2molHl3Pwl_r1ZyOMFMLvZR-46m0Bm3G0LBno2WzFUfL0dvLXvCWK-MZLN_hwwo0V5thnpwW2Cj-3I1MfLWK3UBtWhkouBh0om-5QSP0fgx_P2TXb2WxRd55rEJCOkTIaQGbWpFEo7IIxRIZJHO6FpFfm3tzle5thzNrvgLVFj-ErzP6yDHsQruRtXcvXSIua8dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0ea74d7e98.mp4?token=svenWz5d5YCC0vLbfryaMF0AFRgGOJaVj1GUY9slIRWj6JVY8vfHDV5-89eK9XC1AMorsETzdpdEIn2J5MdF7c3an6wBckEMpzPn0W6Jnwj6w7W79R4WxgDxqwT_a8maDjxA_udcW-D-iEmxKQ2molHl3Pwl_r1ZyOMFMLvZR-46m0Bm3G0LBno2WzFUfL0dvLXvCWK-MZLN_hwwo0V5thnpwW2Cj-3I1MfLWK3UBtWhkouBh0om-5QSP0fgx_P2TXb2WxRd55rEJCOkTIaQGbWpFEo7IIxRIZJHO6FpFfm3tzle5thzNrvgLVFj-ErzP6yDHsQruRtXcvXSIua8dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
بلندشدن رامین‌رضاییان‌از روی‌صندلی روی آنتن زنده: بخدا منم‌فقروبدبختی رو یه روزی کشیدم. الانم نه ساعت دستم کردم نه گردنبند گردنمه. همه لباسامم ایرانیه و معمولیه. از مسئولین میخوام هوای مردم رو داشته باشند که با این فوتبال "تیم ملی" آشتی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/27502" target="_blank">📅 02:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27501">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9CfHTQQDiK3t2I_JMLj6OOth6nqA_Eq4f9lbRuWyb7KzqnGUCq8_S35JIqJLaS7PkCWHbUnoTQQaKHtOEtsDfV6JpiDhkpA2Qw5-qfZ_rWIdJcUkQoyaIXNTJp9P59m_3knYrOfhsXGkjMKpgrsP47x2t5BlUGz-SOhMVHARl90UD5VnOnxr1aYZZA_7xPnDK1M64DB1WMZOVbAOYzERYzEKN54i1QaJcg5qTzrhNOnIS2vH18lL674UMECR9cUShbi3vkJiJgkcWSyxFK4o5fC3ZdCp7bc7a6SBiDjQIWtaOjDgU0Wb0VH01TEKcInIRLmtBZg2MhcFLtQx9A9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
روزنامه AS: با صلاح دید ژوزه مورینیو اندریک مهاجم‌برزیلی رئال‌مادرید در این تیم موندنی شد و شماره9کهکشانی‌ها درفصل جدید برتن خواهد داشت. آلونسو بشدت علاقمند بود اندریک رو برای چلسی به خدمت بگیره که مورینیو مخالفت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27501" target="_blank">📅 02:15 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27500">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f41aa6e732.mp4?token=arddpJ_FTWHIAPvOM6y8U81reRLPCRkHLoBaoPDIao-OX4lj0q1QE3Bgzq337V-UU2RsBgaheYqd9TM1Dx2uJ-PW9I-bd0gPBHMaZRjK4lw-FTXOQKXRlMgElG4XMUFP59NXf4XoqjwsiUFoUbYtKfO_DP4bn_G-B7WCtuy5FcIwJJX2RYKUDnj39SAGK_zQ_pAeSMtYo5kKLrjuHcTi4kNeirhhwbOSb3VNyuhM613Yhn_31Do_kCVVCCW1Oh_R31mf_FbmzdunA4asGcyhR_u0KE0tdmsK-k3F8SzsA5dyf8NqrorPebNVldz8mpf3hDfOdTsjc0iGtZ0kLaapwoyJYyMtUhaOchhRIRibBg56e61GjfuHPYFyKljmXTABil9mmgoAVYVs5JbH2HXvpEzvFg4ztwHe0t1SRwFWZfgRrwUe-aqEAJzbOifBhjGvzybYk8nuQGsmTzUiEHhQtHDP3bBoux9iVgDxsTXIKdDhzHvcmL6mq0LY8vr1STUXFuoDztuk4V3UUUgGbndjCsadNFNQ2N3jE21C3I03PbqMDi7sqa2CNplh8eLTc0IivOwhTOb1leo0RBQhvAa63oZ_vkMS9q_gUNLYtcCuRO-cOXeWyjBDmL4dJbXkeWXkChL_SvtUjELFr2ftSavUTpv7bMb2ddVvrPJWwIYAD8s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده: ما با پرواز زمینی اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27500" target="_blank">📅 01:26 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27498">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=JmXt0kjtxA_eyO1OEJjaHdHmobdsnySBE11W1Nx1VPMZxxbl0Yx26VK5tZCI55kw5HSXWXekMl6ZlQ3qCUWkT4W0pLVFAMBwrBABI6ZckMRI1902FnZWLnjqF-oGQPrUpXllFsR_ksXLekR6yOO0zPWEacGoxidUmka8-C2tKWo4alg_LFr-fT3JXG_4AvHp_Yexzb3nITMEWJE2g3vLdQmBY85kxORrgE3_IJY1YOOhRJui9ZIqRL_WwKyKhStKi0RhrWy9M08c8QcExXLqPlTo8q-xNOc6EOappengxcce3WOAniNJ-C8PyYuP12jmK-3N02kjBlnG5_m8bKjpFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96336dd60e.mp4?token=JmXt0kjtxA_eyO1OEJjaHdHmobdsnySBE11W1Nx1VPMZxxbl0Yx26VK5tZCI55kw5HSXWXekMl6ZlQ3qCUWkT4W0pLVFAMBwrBABI6ZckMRI1902FnZWLnjqF-oGQPrUpXllFsR_ksXLekR6yOO0zPWEacGoxidUmka8-C2tKWo4alg_LFr-fT3JXG_4AvHp_Yexzb3nITMEWJE2g3vLdQmBY85kxORrgE3_IJY1YOOhRJui9ZIqRL_WwKyKhStKi0RhrWy9M08c8QcExXLqPlTo8q-xNOc6EOappengxcce3WOAniNJ-C8PyYuP12jmK-3N02kjBlnG5_m8bKjpFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚪️
با اعلام باشگاه آژاکس؛ مارک آندره‌ ترشتگن گلر 34 ساله بارسا با قراردادی قرضی یکساله به این تیم پیوست.ترشتگن‌اول ناراضی‌بود بعد راضیش کردند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27498" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27497">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kzewnVg9UsXG0ECJLLVdl2GLsJ4BfhQW9GxuZvg4P18AUBScM1DfhS_13ZWk_tz7gaGKF8f_WvNN1jqw76p9hC2ZJCmH6wqPtSS89en38KqdpvFHGPcssPcygK-WbVcUze9ofQ-8kvcXRojZPKp0zeI-yg15ZeL9k12TgHO7wKFYQW_OSIWVUjp8Oyz4RJ0jaK7T1gMe2kbUkortCYhnFTDJKdoAl5IS2Z4CVUwFxtrSsPRbejZ0h44pxjXpfaS5sBTQXg6MESdhGY6C8xFpG628fDsWIqxXEH1bos21PWIoGQwsuFpv2b7c-UtUqxSz1nn0QcJWA1kHk7iKOXFgwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌ دیدارها‌ی‌‌‌ امروز؛
از بازی دوستانه یووه با پالرمو تا بازی پلی‌اف لیگ نخبگان و چمپیونزلیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27497" target="_blank">📅 01:19 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27495">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18c2114992.mp4?token=BQlRetb2wyP5AueCKCBR6KMF7FfXnnfS2gqSidYWIip0KKxfrXrEKWa6sAvzxDtFva6SznK2y3fj0Np69_HZvrVcbmQj3Kd5-yjU8sXZM6tHbY8zvnlzHI7AYJIwldrwv7ETeORKOlo0l7FctEmSJPpVKEht4RdNTCoEwZYcyfHVdm_y1qg6lXa1mQo9GI8zAwb2MI-TtJ7r4MTrTEsSHuf8Q-WeknMEP1JVY7NUEdK1A32M5uOtDJf6SlrUNbyl-lLmhwrehB-zGDOdpKH_HKIdUTFsuj_W15Zoh5JMg413MgbFqWJVt7uX-xfT4ypWoE9aBTTlz0SYSP8elNhqHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18c2114992.mp4?token=BQlRetb2wyP5AueCKCBR6KMF7FfXnnfS2gqSidYWIip0KKxfrXrEKWa6sAvzxDtFva6SznK2y3fj0Np69_HZvrVcbmQj3Kd5-yjU8sXZM6tHbY8zvnlzHI7AYJIwldrwv7ETeORKOlo0l7FctEmSJPpVKEht4RdNTCoEwZYcyfHVdm_y1qg6lXa1mQo9GI8zAwb2MI-TtJ7r4MTrTEsSHuf8Q-WeknMEP1JVY7NUEdK1A32M5uOtDJf6SlrUNbyl-lLmhwrehB-zGDOdpKH_HKIdUTFsuj_W15Zoh5JMg413MgbFqWJVt7uX-xfT4ypWoE9aBTTlz0SYSP8elNhqHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوتی‌خفن رامین رضاییان درگفتگو امشب روی آنتن زنده:
ما با
پرواز زمینی
اینو اونور میرفتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27495" target="_blank">📅 00:46 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27493">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naTtVQYVZD2ASYFwHQNfFHNftEg0piS4uwRgTaDxhPW82aG0gr2W5000rakZrPFnPYEHZMOF_jBzy1EhboloJtwzYlw65VMuLUXeaVQLJJqIVqmAY786wkATdsEM_uxzz5v6SUJsLMGF78NyI7t4HU634EVQ2oo-vOKlWIx9qKomZQ6ygiJdmnO37pSA-Ot2FiBgP_Fs8O_5SN4aiIp6G-HUb0GxUb3kZx8likiJZ_YYyGiZBZzVKoIZ5XgRk7qQ13jKpNp4BotIM4VwQryMH71rFzFutaC0wTU7c6XcvuzYffDajOv8NAO88QRCofgbXfu0tJHCejyoo_vORBNy2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
رامین رضاییان: قرار شد ۵ تا ۱۰ میلیارد بند فسخ قرارداد من‌باشد امامدیران استقلال به جز علی تاجرنیا گفتندنیازی‌نیست و مبلغ روکردن ۱۰۰ میلیون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27493" target="_blank">📅 00:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27492">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQ_FxBuxIdhItwqjVWCAMsUWX3ytUhy6Lq0tMiFzbMDV4-FfD7UShmI3KbKeCDOy5Sqxb3eY9D3eOKl23yKWli8zmJPhxkeazaYMcilysnTbgfOE5IF9k_FFm16Q-1z0x4Wedso0anYye12L2t7PILcnkSuJ-iw9w5skzW7UzOM5bCIuWukjgTC0VSRC_vHHfvwWwy0lUODcYJMqzme5_r-JCaWUHyhmGE0K9zxcnN93W-MjrlF_st6z8tNBwSOnbtz4MkvoZgZABHrriPbkE2o74wxBSwh7EFirVfNNbxldb8grtvXb3GsK7H37zFntib-FjfWhJ9hzeyAaUoG8dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی‌تاج‌رئیس‌فدراسیون‌فوتبال:درروزهای آینده جشن برترین‌های فصل گذشته لیگ برتر برگزار میشود و ممکنه جام‌قهرمانی‌لیگ‌برتر به باشگاه استقلال اهدا شود و این تیم رسما قهرمان لیگ معرفی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27492" target="_blank">📅 00:22 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27491">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bYIMtrZmYSpWtq8_ygwCsVDAFFENK3vcUsRYHjToPrvqgSSR3XfZwr63HGNF_1lHkLfIc_DUxfrIWHKCa1yHdffJuHM2ZK9l4T46ieomEp9Fn0tdd6rRSTxmjpHo-OAs_g4ma-_4G2EbnZbvqiaQEuSAl9IY7P7hq4QAh4GT5b5cAUENBeMcYB541vdvO2zKMeMhlMAg7ZWaJOp2YonSR7EF02ipItmWE5a1qgM-A1CiPjYUOircmGi_Tyg04kTvHv1L33gQm-iWuQiIpM4UUH2vcPvhEh_VxemRW4yWA_gluhmtTIV-zfrVW5R1azjMN2kD1wfSmCdCySEe3zG5bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ عجیب‌اما واقعی؛ رامین رضاییان تنها باپرداخت 100 میلیون‌تومان قراردادش رو با باشگاه استقلال فسخ کرده است. در واقعا زمانیکه نیم فصل باشگاه استقلال قرارداد رضاییان رو تمدید میکنه بند فسخ 100 میلیون‌تومانی‌درقرارداد رضاییان میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27491" target="_blank">📅 00:00 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27490">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvS2GAi7qBdUZKNeo73X_M-1ae7J9UtLFgDMyQwjzQPoCTm1_4nJooNMtRM1tA0Ucqgt0YMCCoKXIlf4urGsbBXKfSPyXd3VXY5wykAXQk1jvk4ynmz0wvssWaw4ZlmKqJxsVfqH7R7AcmYdaY8YuqEAf6bJfMseHgLtcogdKf5whLiZBrrHplCMrMOwOsFTco5TLBcU4iVyXwbi_Dd-wjP4irMF8c33E_RCw-sIzq_hWikSbBTuOeL05OYcs3cVf43PqMeW0iuMtfryYF2JfkJFkUAuaHkF6NzmPZdY7J4Z_Mg9iQruixfjpqxUe6x3XobURvyjS9FIHsgi14kdyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دقیقا 19 روزپیش؛ صبح 21 اردیبهشت؛ مهدی تاج با تاجرنیا رئیس‌هیات‌مدیره‌استقلال تماس گرفت و به او گفته بود که فدراسیون به این نتیجه رسیده که امکان برگزاری لیگ وجود نداره و بزودی استقلال رو بعنوان قهرمان لیگ معرفی میکنیم اما تماس‌های اخیر حدادی مدیرعامل باشگاه…</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/27490" target="_blank">📅 23:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27489">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mmv5zhjGvePewn4U-B2bwVyzx5UtAtOviRXaVJFu_MkPiJ2a2kpF9X-uehjoGErck1LwRYzl-jEH_mBJMTkUHYSbOIPlWGoKWjJtkTMZbRZN6ynHDAEXbIt7BCb1Fjs1tCVIJkBCdSh9TDsCb70ZYNpDowA9_2yOVkOTgOfv8OyxSMOzrq0d8qUiyOZ3LCLeDt1ay4EfOG56loA7MUGwfAzZz9_i7brlxrLuicztEbFNcdUkCCj229-X8BENwFWHfVuHeCfe8xqOF0DbDGEQWjKFilXwwWvJ-DBHT3CE9NvjZoH3HfI1BFG7BgV98NmG3hEMNqGljaP9wS5iFCW9ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
سعید مهری هافبک‌سابق‌استقلال و پرسپولیس با عقد قراردادی دو ساله به فجر پیوست. رقم قرارداد مهری برای دو فصل 30 میلیارد تومان ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27489" target="_blank">📅 23:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27488">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXP_viflYQtJx_TYDCnykqHSzhljFhh_0PuHJ3khLbT3r2GMYlAfJuL9qk9exJnl0RJVX7KLP0lo2o5kQBB578MMYaYYT-vo63XosOeK-gaoqNG7F80aAHmYp-BhDzP-E6AnG7fZT-0Fs0NhAwurBmK1uTrbxxA9oNvP4YM1Ew8r3fTVVXBhAtSQ_msMd2CSSTr-aGmK4r7zV3YEIn66yZpZ7X0H2EdubyhN3G82KO13iXo6Lf4SXYP2MoirfnUmgIky3xdFhxnCRDOtEWHiMMHoXSyJFOBAKxtqY9yJZyW2KHRHp7SjEnYo__GHwZ45qvcOgD_Ew9Dra2UrWhu_mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باصلاحدید سهراب بختیاری‌زاده سرمربی تیم استقلال؛عماد زارعی وینگرچپ 18ساله‌آکادمی آبی‌ها به تیم بزرگسالان پیوست و در فصل جدید با شماره 99 برای تیم استقلال به میدان خواهد رفت.‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27488" target="_blank">📅 23:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27487">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dKK-bxoFGQP_2SFsxZiVnFHGm7NItrkVOU4GXfSSBAJKAnLocKtjTViQp0sP0Ri7HktZDrLXUNz-OZfJI7Iu22NgcdKvjEp7a1IXv60EP68ELf-M4ioGZL2NIqapUAvyao4egWCzCpKbLlYmsCrVJNLHxGqPV2H4-fsbtuNH6clN6Nlq5nSTF5pvIXR1nhcUeS0mCD5EpM2fGDQyExmj-19XHFIDKqYSIvNAkxiU_Xw4ilXYaaHToKpIF7MgL7jJkorgYuFHLku13C7sZxcVLB0SUgttJKP-eAh_WaSYdsT_LOD6cRYul3u4BDFAQRBon7c9GvZgEaftOS5GeD3Y8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛ سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27487" target="_blank">📅 23:03 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27486">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXIOrbxy3K28a5xuurzLECFwD0YZ-2SW_-MO7FahMHo1LIzGJEebdUlnJGL3a0zrvqyyS0BY2V2tS2-MQLFP-Dq3xMYN1jIjNPflEZmZVL5zxQg-8NOtUsRNq1R90mgfvFt6qhNrHPogcefL5oFZFNWylRQspVWL4OemXPanEWjLjJUN4vfFs3fhU_8MMbHUnqa8hs074zQdiFJipyiVwGUJl3VEdac32Sbw20A0MkIg0ArgGCXosM7DBzX7Kw1hxyxoUq35MRMhqSpNJR6JYbpYSHXpb9gNfxbTBCoH9bTCU4Zjile6EoLszDoOUj_CnbToLCbXIuR0pRM-NxR69Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇧🇷
ژابی آلونسو بعد از اینکه با جذب دنی ولبک و هندرسون تجربه تیمش روبالا برد حالا طبق ادعای اسکای‌اسپورت ازمدیران چلسی خواسته اندریک رو جذب کنن که پرز گفته فقط قرضی بهتون میدمش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/27486" target="_blank">📅 22:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27485">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEjZ-F5-jph4S-VvOAksdv6NKqIGc0PRjzKYL6LAqsdpyn8Pt4r7yYRIeRxgclXjWl08dyrt4T0lp_EZxZhpF_ySreElCC-mq6Lfr277AheKVmWdiyI6Nd-XovW3iXIoYBV6i5Ptq4wcmENlztQsl-czP_ugp0SMMZ6AvXkDecHnUqUgoCHSk374Gukkq2GwkK-0iPTEI16gSZbF9XbsjfY7nk0M9mkI7CX-wBrgkV7Ktp1sZ8G2jKVydvdxJqPyrnWwqQmqgNjLHliFwwaw9RTtSxrVbCqKo2L7e4S-81jJUfYRUcjlbF3GfMBVHvbYN5lFthqlALRfE9Zlk8vxzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
باشگاه‌سپاهان‌دقایقی پیش به‌این‌شکل‌از کیت‌های اول و دوم‌خود برای فصل جدید رونمایی کرد. باشگاه پرسپولیس و استقلال هم ظرف 48 ساعت آینده از کیت های جدیدشون رونمایی خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27485" target="_blank">📅 22:25 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27482">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W8f0SSyCrpTSyRKGBPKMrC7v1Oa-ZYgOcgOLqM0A5eqkCoU1GC3MdLCTQNDpfmeJVNnrO-pMgKk68-1-HjJ6GFFw2tA9JJpwAfuWSwf2BtRjy-EWBEUh2gFPTetvYbm5myk2YFSX7tD8dlxtywkMexy1GZV6A_I5bQIOSlshHy0Ffx3GhcQlPJTrquv9hUw0F2ycmeDvRcRMAh1JQ1CRRfgrdR_fGEcseGraDZX_s-Kb4g2gXEerYK9igSu5ow9AT0IkRtalEwFhDhMQYDOiNHfGrXciSvNhCkKC9bfAINQNf8pSDeI-BMJJ24fuk4rS6Ouul-TzE9TqotujpSEEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVNKZU45fIyAYBUnoAd-Ks3kq91IZkd9DO4sUZ89o8xJnR1JpIr7Jp8QKp_k99zOizZTEEwRCMNlp5ieDup3eojDw2-fgO1Dx2MGFasX2g8dO61clywy77ZI9my80UDFFpDUoNXTy_BQ69eX-Tu7YgpFMTFj6GRkXOTfoEvrB-N9Ai_KmmKqf_4vwotBmtQD2vWIMIiUWIaKAnEv_szN2Sgkz9Lh-u3ttWspadvCtBsNf2pTvTS7lb-pQP3_fh_q340Cdx6suRfVdpRWPoENeVtDzQreG19o5apcVZwaB-IFbwyP-7VQagBLfOufOKAacHzqIVSePRMRZYahAgRw_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
پدرو پورو مدافع 26 ساله تیم ملی اسپانیا که بهترین مدافع راست جام جهانی شد اخیرا به این شکل از دوست دخترش خواستگاری کرد و پاسخ مثبت نیز از او گرفت. دوس دخترش سه سال از پدرو پورو اسپانیایی کوچیک تره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27482" target="_blank">📅 22:00 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27481">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NkrGHKC1iXTTP7rQuhgNIFHwTnXkxTtDzFOlgr-s-ZoWalKzGYi1pM8nfWwhvQkwvDII7Q04ayS_YseqDv1ZbyEay7ktF6BUA9SZKdyTLEVv49ZYH7r1cqSabKNX5wYZXr2Z6Hqa8szisM-8Ep-ww0WflQD5VNw7SYAxnlVVSLCfwMau-LOa-wm8OCk60Zocx669BRWi3NfauLfaE6INV0fHzz83kQg3b8csxQH9Fl7pTGSKNvnSIk1zIJi5bctUXOWX7wpZNV8gX50pN9JUYw-K3BB6uKQYrDSVYRxORp2ZMBvf155dT1KksVRrgO7HcW0TIG9AmVoRiepoyc_2rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ سران‌بارسا قصد دارند بعداز نهایی کردن‌قرارداد رودری برای‌جذب‌کریستین‌رومرو مدافع میانی 28 ساله تاتنهام و تیم‌ملی آرژانتین اقدام کنند. رومرو برای پیوستن به بارسا چراغ سبز نشون داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/27481" target="_blank">📅 21:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27480">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OvA4Dsogkin1uTFvqibzGUXfa8CY7jPNm1B_6KNofftPGI4HWJ8-X06-VRzxfSGHEfcgrWoujw5VPtfOR2Zyy7M_SrZxQpzxjTS-QrhDV8aXUMKjFNYp17ifBwc3bOONSFa6MBjpDoYUb1yZJRfzd5BZrU08SnevpJ_IVFudwI0DzVF0jO0sih8ZM-Qdr3tIkzUBYWXmKfFFDeDW6q7Zh8OmV2my9JvlED-88LOsbKVrdbpGywBioCFbN63HpGFDWWbZ-XHcbICAdmur8MbVsxeBQYfODwy_tV_N4lbRhhM1TvJPpPaMfZ1UUniDL2_bHa4n6jbbR7kjPj36UQJ-JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه استقلال؛ استعلام فیفادرخصوص‌قرارداد یاسر آسانی صادر شده و این بازیکن هیچ مشکلی برای همراهی آبی‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/27480" target="_blank">📅 21:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27479">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZBNuojhsAgoJn3Hl04jo0SoJRlKkkvhwjNGQ-9hlZ-LauFlge723oQOkUOdkg4t0LCJCMNwuSp4vA9tnP2XwtUnFAhIkimvzD_C9e62nap28Cxv40xnFQQGQv16NTEuO1x5H0HrFmYUI8A8QXW9M27CNmnif7SokRigR1Myq9ru65zNuO98hwdoiuwPME2PR5yYenwE1NVmG7OM1Q20xiW11WHL9j8zp4-85S9rLY92uj3jYC5Tbe67o9SmJH265fQ9sFIhEx55Hf8KNdgVzygD9hCdF2wBTCEWgS5cag1c4gt0PYpeems-ydm3BaJZgVa2T4ec1ldWEWyqYMtJqVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇦🇷
#تکمیلی؛ 8 اگوست؛ تاریخی‌‌ که برای مسی افسانه‌‌ای‌ دردناک بود و حالاهم دردناک تر شد. هشت آگوست 2021 اون‌خداحافظی‌تلخ رو با بارسا داشت و 8 آگوست 2026 هم با پدرش خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/27479" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27478">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZFODhDMLhAsJUEifvirieo93zfmQSqEUoW2SyGfSus0rRlnZIizJ0AtP_wsLJNwUNVIx8HDjfEWHY5-1Lp9-kmpkIYeNrZOcaWbp6NkpBNNRBqva398ZVOaSDUkQ5lj_OzJamtUMJfXkt024_F-HiZq4PKo1bIKIa-o8A3cXqdHQoEePJkVQIs_r1-SI0KV3qwdF7M_zvVOueZG05l4K1IfEA5NNhkIMlGesozSyCvb-H4DNINgP8I8dfY_VxjV0tYUHhbA56wZInlxqNtovW_JIbXdVGFaEmMV8yr1KO1vIrVr9R1IPrkbnkLxI96SkT9Pb5Ydv4HCB1l6SX22JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🔴
🇺🇾
با اعلام رومانو؛ لیورپول خیلی شیک و بی سروصدا رونالد آرائوخو مدافع 27 ساله بارسا رو باعقدقراردادی‌قرضی‌تاپایان فصل به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/27478" target="_blank">📅 21:07 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27476">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Edtf4-zZmBW-4pixpXKm5L0I73MRxd4i6goceKvqwrzrho36tJlsFXuGaY6r3bmbwWJDHiHpzJRTUWgJIsdZN6xRXhbvCvfjymviyFdwCTMtF7_lQ9KGpFWH61nWr4McfJDRwJWwn4Tlkqtmk1oDCvZmSiXUOI1PH5J10fWiQhth1yG5L5S_JT9GoiwngkQNafm87E42zU-d_OQOcRb4dsc8LbKsH5NX5Qy97Z6IT_7Yrb4JLPQovy6Ot0PiNShbtCJBoPLA8kyQh7XAB_haOEyAqfgj-JJsqGMphXCotEGMhgi6GBcsBpnMHU8YcWzYuIcmyBFkQJYFewpojZOBdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یادی‌کنیم‌از جوزپه رینا ستاره‌سابق دورتموند که رفت آرمینیابیله‌‌فیلد و ازباشگاه خواست که در طول فصل براش یه خونه خوشکل بسازن، این درخواست رو بیله‌ فیلد قبول کرد و چون رینا توضیح نداده بود که چه خونه‌ای‌میخواسته درپایان فصل باشگاه بهش گفت که خونه‌ت آمادست و با این شاهکار روبرو شد:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/27476" target="_blank">📅 20:33 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27474">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dNPOvrPJwfBSsZMolEQ6N_snkbAjMJRGI_5x2LFUJ1sKXVLd4R0g8akhvDJcLjeC2I1phYUKFgn4uKjXbv61pakSiQEz5m_mvb6ltelRfBBWucf9yJAP8xnG-3FNTEWrqHK9cOCVug4qtIvt7lcmtvwx3XEhOUp9OYNiHhN3JNUx1sAX-VUezHxJG-MO1YGdH4vJ-kc76v7eMR4bZqiYJ3_cFEpAbWm1fKjcpEHc56yXsvFQzjpv5INam4bZvDPR13ro4OnJXZrZ3z0Y9Opaej4u40NXsuIFB4ii-_a1IRD6kIIFkSYLb6Oty419ThYmgA_SmftNNmngcT8PRNQqDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PSblPs8l6uLCBaf6aXoSl2yv9gzWhbRueCqgdPeSWirrsm3RSzSFDiqJ17m8J9ocD7sqt2QSw89R1tNK_d-3wMmS3IFpuDpwhs5UOlzakryph2HSl0fRxZkJkyS2q9m_ECEfQH9g4JoAawHjutJra5hShfE7aORy0pBB5FA7IrUjTq0RWwrR04xusHwoyXnoHpDrkFlDVzmF3ArQLom_jJ969T_fSeCwkKKIIc6rUI9fO-M3eZojFYV5OfmtNsy6WOCYiIu_kHyFLQmeB6OTlnEDoldjoJAs24HFwRLkrBg-Rl59tBGHi9tVCiVbcVxUu3Y_7beGZpPJhoB_tovuWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🇨🇮
پوسترباشگاه رئال‌مادرید برای یان دیومانده ستاره جدید خود؛ قرارداد تا سال 2033 امضا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/27474" target="_blank">📅 20:17 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27473">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hNZYrbMirwNM7SEKvnCj08gGCpe23v1qMptJmEfba2ShHF7YgwYV5JQVEQiDUSIA-9C8eQAykgxvmiywRrqKT0tCppLWYHqVnSKRdjVLni6mHlrmlxWkHUPOxvzT43odFXdOcV7Jxy2RtV1Lyj8okCid-wJlPZUBU9wAS5jf3hoKkSaWmfhOlyxPMyBcfSusT1cliY_s5o7qXTd9_c1JNy23oWTpL7DOE7if5Lew2rejrgPxNoJ2hLuxA5daQLvioHCsc-uMhA2N20yjl4HjWcM5O6RU2inlC4hvJeN-Gpa129r0UOAgtEoRYVbnab6dDqHMiC0atEi5quI9mm2wyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27473" target="_blank">📅 19:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27472">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKT45KxSkQZ-zs5pnAGYlcTnnvJ0pH7YJoVgB8zgRXBXWe5xVTEC8CbQd5FKMNFARhJouUAJTUfVySu7ao028UUtW8IbKf_xlJqP_2CZu5T5UNdquMoJL5cEF3UwGTBI8iHqf9xftoAHeAxhArxWQNhMXSbOvMZHf-McLDBdhRn0_fhIGitl9iftjX8_Mh6H_5hEQiKDxPuzucFLQ3-M81cLAgxbOuIHm4qzzyvpfnQb2UkNJlVAwlaJXXaYgeAMJvm9JBnwwhTghZ7LrdVZEK24Q0eRcMQBryGx2zWuEdo68mc6lVEKC89OrTS7-VA9QsRfJjqPpeHURVOVBwmTGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
ایفمارک و زهره هراتیان درحال‌برسی پرونده مصدومیت‌آلمدین‌زیلیکیچ‌بازیکن‌خارجی فصل‌گذشته استقلاله. درصورتی تاییدیه ایفمارک؛ سهمیه هشتم و سوخته استقلال تا پایان هفته احیا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27472" target="_blank">📅 19:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27471">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=NbCPfTVEmoLsWqRd_4VDMbm5J_S1_vf1ecchLOT36wyUUrtR3dmzcfBLJCp0JXwvr1wf4gdWxaVC74-gEliUkuVFY9umESs_xPMa2T2kbLgufrN1Yf1dFshqW9OKHEbMGqcrLEZVZmvID0XZXZj-Vj89iwmlxsIZ64S0M4sGyuf47lSJmM8CG0d_QXfp0hcI-4ju6THyEd_mQFT4h_HXyOQvuY2SPgUjrKvhRiavap5tziat8jX9k9NYOFypCb_nIBQJQw4EfIA_k-aQTN4Z_NCDpzuLRkCYjxreq8u4_xQgTBOl43fcQkGyyn3y5_zXW6YJQvnD8dEST0Fu0yZJ3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4510b5b722.mp4?token=NbCPfTVEmoLsWqRd_4VDMbm5J_S1_vf1ecchLOT36wyUUrtR3dmzcfBLJCp0JXwvr1wf4gdWxaVC74-gEliUkuVFY9umESs_xPMa2T2kbLgufrN1Yf1dFshqW9OKHEbMGqcrLEZVZmvID0XZXZj-Vj89iwmlxsIZ64S0M4sGyuf47lSJmM8CG0d_QXfp0hcI-4ju6THyEd_mQFT4h_HXyOQvuY2SPgUjrKvhRiavap5tziat8jX9k9NYOFypCb_nIBQJQw4EfIA_k-aQTN4Z_NCDpzuLRkCYjxreq8u4_xQgTBOl43fcQkGyyn3y5_zXW6YJQvnD8dEST0Fu0yZJ3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
عمق اسکواد رئال مادرید درفصل‌جدید رقابت‌ها؛ کنجکاوم‌ببینم‌مورینیو با این اسکواد جام میاره یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27471" target="_blank">📅 19:10 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27470">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=J-cWz-7D8dmuxHueRO6l6H3rbQJebXihqfuMpNlM8dRWHAGvuPZ4uIfbY4zH5C6ZN9CspNmKyGGdNopc01YFVVLHIJlTTcv8b4FBWG_aJm-iFE6EY4fFiqZ47OktLr0aSlplXB1XM9milLXVlkIBK-f5RTK4bIrOYv0LhTcLX_uU6biRW1EA0jzBpzHc00l3btVIA6_7WSw6kM0LClVA8icpVSsL0gRmXIidrIUyilopjNSdEeYRLbZPwIpNmfIbtbfGUm2L0XeWs16cEo2r_R8vevwjw06nCteWqdWXA8jUWQtS210HC2QL-SJ6a54fAtOl79oYr4nFso3efli1EA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35efbc9710.mp4?token=J-cWz-7D8dmuxHueRO6l6H3rbQJebXihqfuMpNlM8dRWHAGvuPZ4uIfbY4zH5C6ZN9CspNmKyGGdNopc01YFVVLHIJlTTcv8b4FBWG_aJm-iFE6EY4fFiqZ47OktLr0aSlplXB1XM9milLXVlkIBK-f5RTK4bIrOYv0LhTcLX_uU6biRW1EA0jzBpzHc00l3btVIA6_7WSw6kM0LClVA8icpVSsL0gRmXIidrIUyilopjNSdEeYRLbZPwIpNmfIbtbfGUm2L0XeWs16cEo2r_R8vevwjw06nCteWqdWXA8jUWQtS210HC2QL-SJ6a54fAtOl79oYr4nFso3efli1EA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیتر ورزش 3: کاپیتان‌تیم‌ملی به صدرنشین هلند پیوست. واقعیت: کلا یه‌هفته‌ از لیگ‌برتر هلند گذشته و جهانبخش رفته تیمی که پارسال سیزدهم شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/27470" target="_blank">📅 18:58 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27469">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paNUT2T-8PdYHLL_AOYXt6IoUTR9Sa61W2gHWF1AE8w2v2VD6NMhsnMOc-CTqADA6M4g6pc1Hghu8TEdPSGSwvS0iuS0msvMjonYrknC_s55_xcz1c9b49rOcnUpdUaJmIl2h1jSdtvNZFS-w7y2aA769xzDh6YbTg_OsZWfxyoGEqUWjG80ZsoNfqKOYylXr2Z8Pp-nQtUcQAANaH4ooVrQNewsoEqpi4T7FuxkszeBey88yIKQuKTEQbH6OrJNHZcVthNm2a46t_zzwwwPPG9fsxCcBA0kGFvskZfESj45b7a4aeAvuMJk3bvaEnlKShZzVZ6lxYkURU67gEfs_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مجتبی‌جباری اخیرا باقراردادی یکساله سرمربی تیم لیگ یکی شناور سازی قشم شده؛ و بعدش سریع مرتضی‌تبریزی، امین‌قاسمی‌نژاد و داریوش شجاعیان رو با خودش به این‌تیم برده؛ جالبه هر ۳ خرید روزی به عنوان بمب نقل و انتقالاتی به استقلال آمدند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27469" target="_blank">📅 18:19 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27468">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDcew0OSWCwpUSYVqoU3cKOfqjnHDtEi1sK3fsiknrI4rMLJLPRqcX0BMfqZhoc7W-uIullbPbu8FXWRqrWmcqMOw1SIOZ3HQZKTsQa39w93oaeA46eeVI7vf9QiEhO1XYxZ-FRMpqX7M8F5ufT_gyaxZsLTDf-Bs5PdA07ivFZVTgN8CAaBAVi-TgfwqmItkLhNUdq3iMpMPFvtJV3XXba-BdhL5SewlhCbgT1wBfIj6YoPJ-VQlda56X2cjtt5wPnWhH75zCrMjc09fDpyUxWPAxk4f7by_Am_PKHATLZsf5VAZUC7G2kmA2uttQBf-ZwpQxw_M8fqJTl8yiSnOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🤩
برترین عناوین تاریخ‌فوتبال‌جهان در تصاحب کریس رونالدو و لیونل مسی دو اسطوره تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/27468" target="_blank">📅 18:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27467">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWLN_tt_G5Y12UicjfmK09iaSN9DyEfz3t7Q_sCN2x_SrRn21DS-c2qkeUtK_qAafbG0oasFYLXAwMkIKRq7dHIryld99BZf8U4JpqxI1S4CLw9pV5eim5iJDfO42wQFqpQkiodD2wDap5m19pfFDQrEastP7BOjNrWsclnsyclAV3jCVXgRqbqnJ13tMttw3YrqxEZAyKkoOxgnuUvEppJCS-aYfcQ3Ab563iOLxb3Bni4yqE3NaO7MhBt09_GuCWj2oNOTxQ2MQblThYt9ajhQUeFHMDYMdX3CooZyGzxaKLbtVbuJp3zkpx85ALCQVGVYkVkHuo72dK00XatypQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛ فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27467" target="_blank">📅 17:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27466">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz7kyV5rKwFAzSBl1SmvylEXB-4PIxY_pzb1eLeV_THSK3JJd-p8c3_lDwMyZuOgjefZaWIZZPdBjW8qlreorVN9IjaUrTOsVRUpmgnZyVVdMh0LNLYHS6SZWVYDTNXKmZgV2t5SifXRhwVbcUnwCMoJhwnhauXXsnFvte2qlf02WRqjNW20c3WvVs6l9te3gdDhVUdBZtvfxUPAxP6P7Q1dYF_zA6nmflPs-3EbN4p5kg0PwqAmwo3jiSgJNIgft9KZ8zrS5wo2MceEQr9vHjFbZwc0984ZcqLXiWhw81w3UXeJQPEjE58Pp3vQ0i0L-5ecfMYcxSxKBYg0xv7vPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه‌دیدارهای هفته‌اول رقابت‌های فصل جدید لیگ برتر؛ تنها چهار روز تا آغاز دوره جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27466" target="_blank">📅 17:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27465">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LB75ww_URJu4YuyJqBh9i0VusQGWel2OM4aYFunc45SkTePetrLc6AbkoqK0MoWr39XVoR_NOwIw4InMSDQryt0CbAoZEW_9wuMc_JtzH5v-Cp8VPiCs98UCDZtModJIb6DOrUnmDWoDZWP8nGJbBar_hjNIrLPZRoASbL73EeA1ienkrgu-9dqz9PUpRixvRhiiV-g1PQbQb0DKf1dnl_MkOdwugEY1lrXPumsBiGjDFds_l-wwY4mqRlNwnCiyxVhjN4ogHvwOOTtWT30s04rvtGPS6xZQKNA_KRSYvBAriiA99vLBhjmkYUxMAlIBxCUEP4gvQ4GFcUYh8WL81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا جهانبخش کاپیتان 33 ساله تیم‌ملی بازم قید حضور در لیگ برتر رو زد و با قراردادی یک ساله به ارزش 400 هزار دلار به اکسلسیور هلند پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/27465" target="_blank">📅 17:09 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27464">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=lsFudZ6tVFgwX_rMf0QqI4-PFRoRtRCiuhGzwAVxLgm6hFgkkSK4T-9xo-y45oS3QPDXdoYxYA1zrZ9CBctH0vByeUjKqYJWkd5Nt3lf6wbtHgrbNicaQaqriSc-YF4lIFxujlW5CDjW4Qf6ARut-5e_se3E8mFcPNwr3z-TSxj2bl3VWrTbHiVVzY-a2AmmLrcSaaXNjfySQvI1ZQ-haiFDtRvlfyCe8HUHyc5gGbTaxGezoe2oOgVecrwGZ8EEqgAXhkDQ_bud4-vlaULsanZnNgH2z65RqWnrr6FjnZ3n-zh2J4LRzNXMNwd4XcaB_hcERriQ13hm0l2S-czBng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1c733196.mp4?token=lsFudZ6tVFgwX_rMf0QqI4-PFRoRtRCiuhGzwAVxLgm6hFgkkSK4T-9xo-y45oS3QPDXdoYxYA1zrZ9CBctH0vByeUjKqYJWkd5Nt3lf6wbtHgrbNicaQaqriSc-YF4lIFxujlW5CDjW4Qf6ARut-5e_se3E8mFcPNwr3z-TSxj2bl3VWrTbHiVVzY-a2AmmLrcSaaXNjfySQvI1ZQ-haiFDtRvlfyCe8HUHyc5gGbTaxGezoe2oOgVecrwGZ8EEqgAXhkDQ_bud4-vlaULsanZnNgH2z65RqWnrr6FjnZ3n-zh2J4LRzNXMNwd4XcaB_hcERriQ13hm0l2S-czBng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
توضیحاتی درباره کودتا شبانه بزرگان تراکتور که منجر به برکناری محمد ربیعی و آوردن نکونام شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27464" target="_blank">📅 16:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27463">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVgvj1X2vIqaL-AXz9VxST5XPGuczsOX5JQT-94iMroOsJoUj27Lcfp4L3sSklcQ1Sx8_NZIsEGHQdvSCkDz-Jow-N91ZwrBi2HI_IHuR0gm1TAecqUK1PSQQL1aJUHrcFz_Utr9vMyXFhYgfQZshECv3iNUcDz8P-QTkGX4LClZhRPEUCCqh_BNcx0dgG34l80Un7V6BSyQr32_rhBz1lFLM909BolRcxrkQeWtYlsQ6FfszZFc5IXqJOAUeZ-uP0vhfDoHmKSKLgdCpCzQuu-XFYYbrp5sffWrsx3MXVoFqUnNae_V6HbwcMKcJl-HOzuy63JXKigJeL9LfN6Iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
پاسخ علیرضا جهانبخش به سوال قیاسی به اینکه در آینده به کدوم تیم استقلال یا پرسپولیس میره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27463" target="_blank">📅 16:28 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27462">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_5jdofcXZ7ymy3Z97usPLc5W2lBfec3GoL5w1lXslSlqvebM0ifmVvFkQrt0xXy_ESE6TRWTUeIel5eZg7vAL-y6qdkdWjCS_g0tuYVEtessU3XEfYG2lsuTsjmsCnqBmQneQrN50YoUL_ArYu6bU2kWqVFqjspsyGtUntrQ8enPy127nY0Pml8ZlJk4ECpcZxNQ99eQ9xQBHsZsA5ZIG1MVLYBHqgE_w1qmv6efusu0AuDge6QvVSJGJaEze0slC-HjkkXPDehFx0wXZZYPhwQrMuMyGeYJqq8Ca-UWdiC6wl9TqVBrYTn67dP18Pp1K1uBq6ODJ2mYtUMNMk9eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ترکیب احتمالی بارسلونا برای فصل جدید رقابت ها در صورت جذب قطعی رودری و خولیان آلوارز!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27462" target="_blank">📅 16:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27461">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z8AvpLx6vtib87jAPkpYGDiUtSHZm3_A3jYWm_LkEqQlfWgES2AtZTeBzxWQdFle977bgHPwJHNK_UwiZaItd6YPwISnyot84t3fG70YFFlc8wx9HbAxii-_7VM_lc9WkHFgHllprpeYuwV32uXocH23TZQPqgixQR--w2gM79ZSZ4koZgYIqus7n5oo9oprA24QxHlSDc6yYO8uZdifQRHHACXsZM33rhTXodX652m7_1-T3kH0nQZSeZACEFAHKzf3Jcd9LoTGb6DfmAilu-wqiD_in5E6GzK27shWz13wNgo0oAM5x9tkA0X-OFPOepy2Pwty2KoTr9sL1VsxLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
باتاییدیه مایکل کریک؛ مارکوس رشفورد در تیم منچستریونایتد ماندنی‌شد و شماره 14 شیاطین سرخ درفصل آینده رقایت‌ها نیز برتن خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/27461" target="_blank">📅 15:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27460">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwmi0BaBNqCQ9bY9HzcBvM7n6x7oeJ-gy3hlhOsodt_DKMRYm1aEWFH6442bdE1Y8LUuVtalZaUnruadczDNcq3U8hYxJQutaYCFMxVWrxjMt5GaCnufLyKoXZTRj1FJv6kmkDNdvXLgJm_mwVWAAGIq99ERrji9Qj-By0FSctZYgAhtMUT4QMNozfGpN07QZaJw7tNzoJtf5pTS-dPluTnA6nRe_KyJRGe2qH2BN0rAbmwpf2pOv1fc29hu8H3VBrRTZFSF8IfGJRKGwhqhjUI9hTf1OyQVAxFCXjeJQxee3-lr74daMPRx2A0Jt5AaQfCTGrkGj3HwEq7YHYrheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
خواکین گیل مربی اسپانیایی جدید تیم استقلال فرداظهر برای‌ عقدقرارداد و رونمایی باپیراهن آبی‌ها وارد تهران‌خواهدشد. خواکین‌اسپانیایی دستیار دوم بختیاری‌زاده و مربی تمرین‌دهنده آبی‌ها خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/27460" target="_blank">📅 15:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27459">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKlQxTV3SbiSyIMwratiVkNmV94XqMSdhSdA7tKJEdEVWBVZdGouvRMEKBEohDDZ6qazIjrTv9JVF-b9pu2mWvLtDQUO0Dx0kpw151JpiHW347E5TliGCva4jvOD4MFuExCpqNTT-cMqaS5T69ivSR43oEVQyZ0KWTwIJGDI648FyGMGhiUnB4FT2sdwoC7jB8P5Tfauv0IuJEJZFa9TfDF-7sJTT6vgnJJlCK-qPxa5AKKgpSubrMsAkz4_yjVz6SWABp6zEtyGerQcmS-SJJzYQu0w5RZnUZCzTH55FhkYLp0fFN5k4Z9nnLsmPuyrAMHLc-xdzmKZAdATbAksgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/27459" target="_blank">📅 15:18 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27458">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/643163ded4.mp4?token=VOPMiUIH59lEBUWxIHxUE5BzqypwKq1TthHP9eLEVUHtw94CT7iobm3QOsb9-XsyGXcMBnSFfuzOpUyohmskJqmS2IOJtNn838vEynVBB4gTj_BdJym66_6zsTRbpSbtXqXY_ofR8DAhlBZ6Swexddlm2BrcSWa9IE7qSqoJPNqCHbaXLHzmc7tmKSISzKLt1BC1gDGyJcl0HqjPYsCcK-jDajrQY3A7Biv1NW1_e_p8Aoouy3wiF-3nqFFgq9WnVJi-qHh5ra5BCAZY_MJLgG8Vunmdlnz_WzCkL0QiM3dxqnz_qggYnz1fhoQTw1E4wezmRoCm0LT9f86ofV8SE7dl-1knUtel2TIxw_t7mU4BTt0aQ9C15SXMn2vUNbCkNYq5SSVSWsUZnZh35XwWOlM-lnrh9pnsfMeZ6NPI4I9tPYVFNYDM9pVALtOmB4RtnBbOGbTgtXZsMME4SdSWWwFe4UxquCg3BOJo_MKbyHVDaLFVd9TbNdX8C6UKg6ttbEDknv2zgN4APCqLa57vlLFdND20M6GpOhXZjkavypPyb7ZLbL6NmClg_bU_65Omq0cS98B2tdXwdZdxPO6jL2v92uLS6jjf6hVZW2N5xeIuqgELaoL1hST0TA6GMfip5bXkTy2Xp2f7vxnD5cOBFyRcWP0EmP31EdoDeyk7Igs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/643163ded4.mp4?token=VOPMiUIH59lEBUWxIHxUE5BzqypwKq1TthHP9eLEVUHtw94CT7iobm3QOsb9-XsyGXcMBnSFfuzOpUyohmskJqmS2IOJtNn838vEynVBB4gTj_BdJym66_6zsTRbpSbtXqXY_ofR8DAhlBZ6Swexddlm2BrcSWa9IE7qSqoJPNqCHbaXLHzmc7tmKSISzKLt1BC1gDGyJcl0HqjPYsCcK-jDajrQY3A7Biv1NW1_e_p8Aoouy3wiF-3nqFFgq9WnVJi-qHh5ra5BCAZY_MJLgG8Vunmdlnz_WzCkL0QiM3dxqnz_qggYnz1fhoQTw1E4wezmRoCm0LT9f86ofV8SE7dl-1knUtel2TIxw_t7mU4BTt0aQ9C15SXMn2vUNbCkNYq5SSVSWsUZnZh35XwWOlM-lnrh9pnsfMeZ6NPI4I9tPYVFNYDM9pVALtOmB4RtnBbOGbTgtXZsMME4SdSWWwFe4UxquCg3BOJo_MKbyHVDaLFVd9TbNdX8C6UKg6ttbEDknv2zgN4APCqLa57vlLFdND20M6GpOhXZjkavypPyb7ZLbL6NmClg_bU_65Omq0cS98B2tdXwdZdxPO6jL2v92uLS6jjf6hVZW2N5xeIuqgELaoL1hST0TA6GMfip5bXkTy2Xp2f7vxnD5cOBFyRcWP0EmP31EdoDeyk7Igs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دریک در یک برنامه دوست‌یابی با حضور ۲۰ دختر شرکت کرد؛ اون در نهایت از بین این ۲۰ نفر، یک‌دخترروانتخاب‌کرد و حسابی ازش خوشش اومد و حتی براش واق واق کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27458" target="_blank">📅 14:51 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27457">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=aTJNu8uCksfhB1XE6-IgIjMZl4oXQi1yfcT1a7yQR_ZPASHrD_aGzw0W_ubW4UicQrEGx5KYLQDjMsnSOyWzVha1tLCTWMahKzBT1xQgEOTmCuCEjJCr-frofWF9V6bnoiGdxYACFJaxMaLIBKOEkgiITV-Iw9b8tO-IiIEQCDfiedOAF4ykWbTpYBaCwCaw4CAaRUbR31oY5onskx_CfZvN33L12_wiqJ1uYKa-Nr26DtHmiJ01clM_38fLZonyJTOrSlEsKJNgLZkNH7aTjHX76xXOT7lyB3UjNisULF7obp0NTEJoEmB2XhA1TSXg-U4cHd0TdacxOR2yMsBhZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e350019bc.mp4?token=aTJNu8uCksfhB1XE6-IgIjMZl4oXQi1yfcT1a7yQR_ZPASHrD_aGzw0W_ubW4UicQrEGx5KYLQDjMsnSOyWzVha1tLCTWMahKzBT1xQgEOTmCuCEjJCr-frofWF9V6bnoiGdxYACFJaxMaLIBKOEkgiITV-Iw9b8tO-IiIEQCDfiedOAF4ykWbTpYBaCwCaw4CAaRUbR31oY5onskx_CfZvN33L12_wiqJ1uYKa-Nr26DtHmiJ01clM_38fLZonyJTOrSlEsKJNgLZkNH7aTjHX76xXOT7lyB3UjNisULF7obp0NTEJoEmB2XhA1TSXg-U4cHd0TdacxOR2yMsBhZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
«رودریگو دی‌پائول»ستاره‌آرژانتینی در بازی بامداد امروز اینترمیامی‌روی‌یک‌شوت تماشایی موفق به باز کردن دروازه حریف‌شد و به این شکل گلش رو به لیونل مسی و پدر از دست رفته او تقدیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/27457" target="_blank">📅 14:43 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27456">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dd69k4alPeEZeTW2cEwXrVmmH8QsFQTf5exbvFE6NTlNturBy2aznjy7joZoJcZ-qSc_eHuFMqG4v1qpF4SqYK8k5JFfJ9hWufFrWqTkEX0_Pu-6vDsR6bKrpbsmHrBgUwSsl2Yzt-cfAR_1JdS-fIdbouxKO9PlQrmcBOWAr1QIGcnIhxUhXVvskK-7WjCc8fyOhFs7sy0ip7aBrmw9Yh0YohJBiPP1DPOBG-Ovpa1ObMwzysYofNBAlyLBUklXBBEfOCPFpo7tdUGuexSfboinUTF6ne1b0QwsvG77-Fzv5KQ8ITeH_3t2VvZGzNQ_7XtQjrwZMyoEwm4kxRAjfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
کار انتقال فران تورس به باشگاه پاری سن ژرمن نهایی شده و این باشگاه بزودی با فعال کردن بندفسخ قراردادش از او رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27456" target="_blank">📅 14:22 · 19 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
