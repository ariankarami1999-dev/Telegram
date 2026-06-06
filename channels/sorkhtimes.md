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
<img src="https://cdn4.telesco.pe/file/SUxGcNw3Cusm7jNVQv1gIVaGYz2DFX355FudxtJT8om7qlQa7PEr_9U_pbuVBKHQJKgRnzZVRCAyVLSvBtZLAhMGe6YWouRsof8VaKa0crA57_GNaZ5he8JIsDOs5U6DSY50_wvNL12Bqy0hKHIP_ALjevqGxF-Oga07AS8cdTFkV2YnXxBErzwSGwFPEDbGaYr_ALMfLhu3U__ZNyMtwz7S4NHgbltZTRzoW-RHG4D3XfXp-RhprH9BySwjqIObxVc-th2t7sQqnCKMWgqTf1besP0OQXgJRAY4r5GkdXgPjOZPR5sEAkw3S-e2h0mndwx_8fc-xSEcSTXR_MCUYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 🚩سرخ تایمز🚩</h1>
<p>@sorkhtimes • 👥 21.6K عضو</p>
<a href="https://t.me/sorkhtimes" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽ورزشی نویس پرسپولیس👤🎗️«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس.✍️کپی کردن با ذکر منبع «سرخ تایمز»🖥جهت تبلیغات🔻@Tab_taems⛔رسانه سرخ تایمز مسئولیتی در قبال تبلیغات ندارد.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-16 05:55:40</div>
<hr>

<div class="tg-post" id="msg-132842">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PH7pTosBp447mqIlOCgyNDqpmAy71mKDHqtY519eDIrnQZcShpdWgP1ptctH7_BqEDUPkrB3OOgKxFaL82TaiMiuFD6DpOl2ffuvZqApqffQoim_UIfsLaL0GGKiEU1I3CrycXlfzUOpL0XeJfQQnjjgBqkY-yz5Flp_cwakeSaLN8mqrDfoAwoSHyVATvm-ujDUF59SYLTvhrMwuXWM-qBAulRRh6ehBkXCk82OY6BzQnfHObLHbniBgazU0D3jbiM_mmWPLXPootPzAjYuAlrkjCnhnEFGtRK5hbTzRNHdzu5R39-VPvSDJpyXZTyddkSpGH14xZMwvI95-P30Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
بونوس خوش‌آمدگویی برای کاربران جدید
🟢
کاربران جدید وینکوبت پس از ثبت‌نام و اولین واریز خود می‌توانند از بونوس خوش‌آمدگویی استفاده کنند.
📌
میزان بونوس تا ۱۰٪ مبلغ واریزی و تا سقف ۵ میلیون تومان می‌باشد.
📌
شرایط استفاده از بونوس:
حداقل ۱ گردش با ضریب ۱.۸
🔗
همچنین حداکثر مبلغ قابل برداشت از طریق این بونوس، ۱۰ میلیون تومان می‌باشد.
🔗
همین حالا وارد ربات وینکوبت بشید و پس از ثبت‌نام و اولین واریز خود، بونوس خود را دریافت کنید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/SorkhTimes/132842" target="_blank">📅 01:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132841">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی: @Winstn_Churchill https://t.me/PulseGatee
⏳
ظرفیت برخی سرورها…</div>
<div class="tg-footer">👁️ 1.38K · <a href="https://t.me/SorkhTimes/132841" target="_blank">📅 00:37 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132840">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">✅
ادعای الجزیره: ١۵ نفر از تیم ملی ایران ویزا نگرفتند!
🔴
بر اساس ادعای تلویزیون الجزیره، درخواست ویزای ۱۵ نفر از اعضای تیم ملی ایران صادر نشده است. هنوز مشخص نیست که این افراد شامل کدام اعضای تیم ملی هستند اما به هر حال جزو نفرات اصلی درخواست‌کننده ویزا محسوب…</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/SorkhTimes/132840" target="_blank">📅 00:27 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132839">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLcxeiC9medU9ubMhLV-qvqYUDSWDLw5eND7_0XqfP-XqVsK-GIVNHJsxmeHEVQsyokdNzdAE5SrFAy9m8JjUuGXoyV-2JDQkkCxDvBOAEj6HwDr2_cGbGaEt5ARgNAu4LHh-dkh89fkvE3fO8y-kCv6L49DnsbFTvdFVBQyDjNNnbmw32QeUEY5UYYABWhblaoE_GeVOLpSMP9S2r3sMt5hIw3Rmxb44SdL_p8Ak_JKUa6xOoWs2aVBbQgHyU79Enj2RbTnBkcT4ASJnX1gHicRGHv-kJGs83Ws0FqerwdZbx0bbMQcjLeHXHw1Sg8BoQoIpPTLTR2fxz60K6FndQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
شهریار مغانلو:
❌
می‌خوایم سه پیروزی بدست بیاریم و با ۹ امتیاز به مرحله بعد بریم
😂
😂
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.74K · <a href="https://t.me/SorkhTimes/132839" target="_blank">📅 00:25 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132838">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LAaCbepwIqO7PITFKkBYD1Y-aZdOuNhvpxWz--ClW1RgFQH-HF83eYbkczBBqfDqJ7ExrUv341zXtAoFC9IGgLHKcl1R39ceemrdJclOLMA9Rf5ne8jY4QxE5cFKF-ig5oPyUEtZ-lvr75UEqlVJhCuhICu5os8SgXW4bNHIZnIy6ea6wly_WYJjiijN4Xd8pTDo2IXRh7l1WY6hlF643c6rBkS9YkZwghvT77SJ8rY5VtGXfy85-dY5TLEnQZz6Y7QT3BEqo2JNfP17yhuopl7pA-o47XBeEQ1xSKM1UrZp9KJGYaQ7SUtKR4-T0b4hfUaUpWDgjxBx1KgIbK2ZOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرهیختگان: پرسپولیس پیشنهاد داده که میانگین امتیازات سه فصل اخیر رو برای لیگ 2 قهرمانان آسیا در نظر بگیرند و طبق اون نماینده ایران در این تورنمنت رو مشخص کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/SorkhTimes/132838" target="_blank">📅 00:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132837">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🔴
👈
خبرگزاری فارس : آمریکا هنوز به برخی از اعضای فنی و اجرایی تیم ملی ایران ویزا نداده
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.82K · <a href="https://t.me/SorkhTimes/132837" target="_blank">📅 00:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132836">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده…</div>
<div class="tg-footer">👁️ 1.77K · <a href="https://t.me/SorkhTimes/132836" target="_blank">📅 00:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132835">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=H8A89yT3DBeIkwWBo85sq_kQ9CNoPbuGaSKRlDUjzB2u1EEUcqAt2EE3Am0qSRXm7m1tKJHwt9wx42yH70rbFOptxTsMlz1fxYOjF33pv5doGPji8GNlXj29xQNpVrKe0OZRnPd0iTtwb1qQjwzpzWAx7Z4vTbrU3ClcF74t1wiQUI2Mm2IV-5bG5FBXE3p3aAvbFR-sebhsHUWW_Yql6BxURCVyH3WZLfRuLMm5VCVsxdQ4Or9XvgFsZsZEvzQmqvUm9o_S4_PV8kre_MGqJPzxgzWgBjJ8LOOgDmktD545TmUd8w9zynbxWlAtBTSAYrZYk4rWCUjfz7Oqs0K3qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7a60445fb.mp4?token=H8A89yT3DBeIkwWBo85sq_kQ9CNoPbuGaSKRlDUjzB2u1EEUcqAt2EE3Am0qSRXm7m1tKJHwt9wx42yH70rbFOptxTsMlz1fxYOjF33pv5doGPji8GNlXj29xQNpVrKe0OZRnPd0iTtwb1qQjwzpzWAx7Z4vTbrU3ClcF74t1wiQUI2Mm2IV-5bG5FBXE3p3aAvbFR-sebhsHUWW_Yql6BxURCVyH3WZLfRuLMm5VCVsxdQ4Or9XvgFsZsZEvzQmqvUm9o_S4_PV8kre_MGqJPzxgzWgBjJ8LOOgDmktD545TmUd8w9zynbxWlAtBTSAYrZYk4rWCUjfz7Oqs0K3qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💢
ترامپ: اوضاع با ایران خوب پیش می‌رود
💢
رئیس‌جمهور آمریکابه خبرنگاری که از او درباره آخرین وضعیت مذاکرات با ایران سئوالی پرسیده بود، گفت: به نظرم وضعیت با ایران نسبتا خوب پیش می‌رود.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 1.83K · <a href="https://t.me/SorkhTimes/132835" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132834">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YuV_OEl5xiSJZTR_NpyeLga5COyxVEjBbLCnBCOiB5aEf-AwrcfiocIYTkd4a-7vXOas9-F9Y8G81afLMP6QFZ0Hj1UBdNnJ6FI6Vrey4CCvNYCNFxPp2UvVhFmATPskH-b-1mRIEJJgcbwa95rpuw2VcpPPVIylpx-XvrRR8CW5l-Qu5F0T7vjVNiWBDXAT-XGjqpgIoYFYsY2AQmJuctT39QrAl8Vubto3S-AVa1c6g0ChASiFK1ALxXPZzNx4l9UA3hSKzjfs4ZjWJdLrRKXLqslTAWcHAEMfEybYY5xja-wrNBBfBpcrxk6Zs2gGjh9Rra0f24SnbfN9TVSH2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
PulseGate | اتصال بدون مرز
🔥
اینترنت مخصوص نت ملی
⚡
سرعت بالا
🎮
پینگ پایین
🛡
امنیت بالا
📱
سازگار با همه دستگاه‌ها
♾
کاربر نامحدود
💰
پلن‌های اقتصادی از 250 هزار تومان
📩
ثبت سفارش و پشتیبانی:
@Winstn_Churchill
https://t.me/PulseGatee
⏳
ظرفیت برخی سرورها محدود است؛ برای فعال‌سازی سریع‌تر پیام بده</div>
<div class="tg-footer">👁️ 2.1K · <a href="https://t.me/SorkhTimes/132834" target="_blank">📅 23:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132833">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👍
🔴
استرس در آنکارا به 100 رسیده .شایعه ویزا نگرفتن 2 3 بازیکن.و خط خوردن آن ها از لیست جام جهانی.بد جور در اردو داغ است  .و چند بازیکن استرس عجیبی  دارند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/132833" target="_blank">📅 23:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132830">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: امیرحسین محمودی در حال حاضر هیچ پیشنهاد خارجی ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/SorkhTimes/132830" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132829">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=Xe4xttWL-FlAlMYg9PlVOWewWnO1b4sGVqEYw1JxyXyo0NrF9J4aYwGQRtlTXTj2A-Z6TONdZZnt2Q9sKzq84gZQbOvWpYGvtQV0wnhUksCaOYN95gDMNc11Nt_Ai5o4tpRcH0P8pk8DFj6ROQVcBFoUDmFwSAK2-Sx6HGz795GpUDlVZDd-idY2U6kM_t__gDQ4i3k7sgb4oQLhGC-tLS0B0kV_JlcSMyNZHlDdQC34RFb7cYC9y9HIH1MVhH7B4tPSURaXYfTcWGmLVpT5UFiUcDVRBIeEkDDSRd-3MvfCn-7eK1Xz1AAdzvyuGWrMZbi1jpAexp6_gHBzN_FJRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d48505e0e1.mp4?token=Xe4xttWL-FlAlMYg9PlVOWewWnO1b4sGVqEYw1JxyXyo0NrF9J4aYwGQRtlTXTj2A-Z6TONdZZnt2Q9sKzq84gZQbOvWpYGvtQV0wnhUksCaOYN95gDMNc11Nt_Ai5o4tpRcH0P8pk8DFj6ROQVcBFoUDmFwSAK2-Sx6HGz795GpUDlVZDd-idY2U6kM_t__gDQ4i3k7sgb4oQLhGC-tLS0B0kV_JlcSMyNZHlDdQC34RFb7cYC9y9HIH1MVhH7B4tPSURaXYfTcWGmLVpT5UFiUcDVRBIeEkDDSRd-3MvfCn-7eK1Xz1AAdzvyuGWrMZbi1jpAexp6_gHBzN_FJRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: به هیچ بازیکنی نگفته ایم که برای فصل آینده قراردادش را پایین بیاورد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/SorkhTimes/132829" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132828">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=vc20332e5ddiJr50o7RtVBZTZxw3Rd4PoekvjxwA614x5atrowshqEnVai4lWiwIjT63vNkjFOhyARYr4XG2jxhXxEj5tf9kRhcPf2XGjliTUwPaZz7N3ZUaN52_44yiNNzn4TC-Ii2nUCDrQd_kaRChj1u1Dts8fGX7-qHnebzzrUZ6K9BG-sHc8j5GeaQITrNybQpu3IZivZDojrz4QXCrxJGLZEZI-MiskW4uhcGC3uwZfJ3EAdWnzdf5o9yhsu1Jz3jAPDzIkhEdq--wElwiOaI26Aik3JJmahEUcfas26CsJ7ZMi_kpXNFbuhTIzo0G9v33FENKOa-MoxqhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3f362ea01.mp4?token=vc20332e5ddiJr50o7RtVBZTZxw3Rd4PoekvjxwA614x5atrowshqEnVai4lWiwIjT63vNkjFOhyARYr4XG2jxhXxEj5tf9kRhcPf2XGjliTUwPaZz7N3ZUaN52_44yiNNzn4TC-Ii2nUCDrQd_kaRChj1u1Dts8fGX7-qHnebzzrUZ6K9BG-sHc8j5GeaQITrNybQpu3IZivZDojrz4QXCrxJGLZEZI-MiskW4uhcGC3uwZfJ3EAdWnzdf5o9yhsu1Jz3jAPDzIkhEdq--wElwiOaI26Aik3JJmahEUcfas26CsJ7ZMi_kpXNFbuhTIzo0G9v33FENKOa-MoxqhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏅
حدادی مدیرعامل پرسپولیس: اگر نمایندگان ایران در آسیا معرفی شوند دیگر انگیزه‌ای برای ادامه برگزاری لیگ باقی نمی‌ماند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SorkhTimes/132828" target="_blank">📅 22:57 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132827">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🔴
فوووری/ حدادی مدیرعامل باشگاه پرسپولیس: در صورتی که سه امتیاز بازی گل گهر و چادرملو به باشگاه گل گهر داده شود به فیفا شکایت می‌کنیم. چرا باید فدراسیون فوتبال در روز تعطیل رای صادر کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/SorkhTimes/132827" target="_blank">📅 22:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132819">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=X6ODib_Ghl4XuFhDWAGQOtmmt2xYl6gtlYfgeK3-t1LhCC4lrmkE0n0cd80ABSRYhTkUuZJh_bdbDX2bpWgp1J6apU6-jANTQL5lSsB3g7dLXIfOJAwnJ8oqIe0S3ynj_5C4qqEa9KJXuTP3P8OJIQu17VYLTTJSVE_MljvOre_gH-1B8ixOjVnxz-R4ipHSDGH83gyb6UDU9VpU-Akoyu65z0Ymy3gmGur-dghpHHrCMscZPEijEUeGOcZf9u9PRP-Fse9k-OlWeciL3z6k8K57bZRbmzvcXf4LgKxwDXJOYVkMv2rkXKA1ICwfRY3xpyjGQC15EqSH_5bChLy9dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cfc635883.mp4?token=X6ODib_Ghl4XuFhDWAGQOtmmt2xYl6gtlYfgeK3-t1LhCC4lrmkE0n0cd80ABSRYhTkUuZJh_bdbDX2bpWgp1J6apU6-jANTQL5lSsB3g7dLXIfOJAwnJ8oqIe0S3ynj_5C4qqEa9KJXuTP3P8OJIQu17VYLTTJSVE_MljvOre_gH-1B8ixOjVnxz-R4ipHSDGH83gyb6UDU9VpU-Akoyu65z0Ymy3gmGur-dghpHHrCMscZPEijEUeGOcZf9u9PRP-Fse9k-OlWeciL3z6k8K57bZRbmzvcXf4LgKxwDXJOYVkMv2rkXKA1ICwfRY3xpyjGQC15EqSH_5bChLy9dDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:  گزینه اول و آخر ما اوسمار است مگر اینکه ما اعلام کند که قصد حضور در ایران را ندارد که فعلا چنین چیزی به ما اعلام نکرده است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/132819" target="_blank">📅 22:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132818">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=mf_vhG0cPmh3sBE4VM1KBdBPBZJkgpxl0dAgk4LW_9UYB1exbGTdn_h9nxeDqjDVVbIz3O8IHAIZbdA_k8VimxBu7uu5-PsMhbaK9HBwzr89n95oirVfNxbVHYWErN99Q942v5yKP-kqv29fAG7yElSvU4v5ZQbHyzGhAsOrsoDRHZiBRiK1hqP0Eniwf5QJ7n84g7hKnx5VMRk5Qaq4Tktksbs1wXp_e-0kx-Nncn6bqC16WMS4hVQ2t2Hg64B3MgEsXMBuX-LDWFrV60NJZfhuAjCf5Jh6hmap6aVUvovVZ3j6C00vrx9L4kM5SWjRIzhgtZ1pBNzflql3Y_elnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33b0f1c642.mp4?token=mf_vhG0cPmh3sBE4VM1KBdBPBZJkgpxl0dAgk4LW_9UYB1exbGTdn_h9nxeDqjDVVbIz3O8IHAIZbdA_k8VimxBu7uu5-PsMhbaK9HBwzr89n95oirVfNxbVHYWErN99Q942v5yKP-kqv29fAG7yElSvU4v5ZQbHyzGhAsOrsoDRHZiBRiK1hqP0Eniwf5QJ7n84g7hKnx5VMRk5Qaq4Tktksbs1wXp_e-0kx-Nncn6bqC16WMS4hVQ2t2Hg64B3MgEsXMBuX-LDWFrV60NJZfhuAjCf5Jh6hmap6aVUvovVZ3j6C00vrx9L4kM5SWjRIzhgtZ1pBNzflql3Y_elnjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مدیرعامل پرسپولیس خبر داد: با هیچ سرمربی داخلی و خارجی مذاکره‌ نداشته ایم/ فقط با اوسمار صحبت کرده‌ایم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SorkhTimes/132818" target="_blank">📅 22:45 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132817">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e073252128.mp4?token=WvgVwISaRl2PRQUOFQCktXBWtQ4XKuyo0C7siL-zHr1TBcmoKkkP6Qf3e5di4iilhFMHaW97CnKkfyHwrVCvioYsywuylVBY1XpnYItY9jqjqoyfjDyXnwYOEUAnpBpkdMVQ2ARPue5-Dl8Grq5g-lGLEwiV1p7n_ePp9tFHJ34BYNIGJj69rDqpabdM1ZE5DddPcvLDncBq6rQz78L_0G94C4SabIvKx00sonG_rqVoUlZrBEu6faXKShE2ljsq-pvKlES3AMvJ-50tGYbSo94qmli1_S3VqhhF41kYTiz1MMl7N1lVBvCzBSR7h4Pqloee38_HbW6-5dZ9P_Vd-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e073252128.mp4?token=WvgVwISaRl2PRQUOFQCktXBWtQ4XKuyo0C7siL-zHr1TBcmoKkkP6Qf3e5di4iilhFMHaW97CnKkfyHwrVCvioYsywuylVBY1XpnYItY9jqjqoyfjDyXnwYOEUAnpBpkdMVQ2ARPue5-Dl8Grq5g-lGLEwiV1p7n_ePp9tFHJ34BYNIGJj69rDqpabdM1ZE5DddPcvLDncBq6rQz78L_0G94C4SabIvKx00sonG_rqVoUlZrBEu6faXKShE2ljsq-pvKlES3AMvJ-50tGYbSo94qmli1_S3VqhhF41kYTiz1MMl7N1lVBvCzBSR7h4Pqloee38_HbW6-5dZ9P_Vd-4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اگر عدالت رعایت نشود حتما پلن‌های دیگرمان را اجرایی خواهیم کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SorkhTimes/132817" target="_blank">📅 22:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: برخی‌ها می آیند روی آنتن زنده و می گویند قطعا پرسپولیس نمی تواند در آسیا شرکت کند، بهتر است دوستان در حیطه وظایف خودشان صحبت کنند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SorkhTimes/132816" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=LtURJXvMg89wpwQ8wBnziD0XN39BlVQKXLAgCdcL9CegE6Rqh5mfkpGuPwZMmjAgUJUomtqfMImCpHhhvmuYDPZitGix6_7wPLlqLflCYpRhCt5sI8qkGgYFWoMZHsIkDytH791ir7LkTb_Z_pb2m8ey3DU8NfWPNzoNYEb5daynwYc94fjoGriNtgryJHQWJqmgKnEDqGmG98gSCOG_EOFS5OEqYu6phT3mxz8Kv4_mIt9KseCgw-N_hWiPphvWOEdbgTajG3pSPqSYNI0cfBGqlC1KVjpkKDrelSlvFmmfhe_wWgiLfL2lMXuqIZd2p0XoXvAiYM0-ceauinS3x3JE5HLea73jO1XQJIskgQfPDcBLLZ4VHO7p8OgXFXsSUQ9l5R8Cy9xp4otTLqBvBirGuOM7mif09g4oJwX2TA77yWIE3Jbb5xllZCgXgj3Kb1-SovRsjzJbxA6IJkCniSPDDT5JywooMvCX-e4adDTmx-KmUrLR6VxxljersXFMCYGFebgJ_uXiemr2l-lt0NQ9mhpSP45ZkhhENjwtEhe_ZzLcaO3e8og7GNBdc5I7m8NyoSWyHQz3HCM5rRKyzU_Uc5hRRA_-De_u0e-6iQ1qn2X9hZTfcePzXGvjD2ceJbcVesDj-hXiAMEuhj6kit03BhM7_GdWz_uPZwSWDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50b4c5477e.mp4?token=LtURJXvMg89wpwQ8wBnziD0XN39BlVQKXLAgCdcL9CegE6Rqh5mfkpGuPwZMmjAgUJUomtqfMImCpHhhvmuYDPZitGix6_7wPLlqLflCYpRhCt5sI8qkGgYFWoMZHsIkDytH791ir7LkTb_Z_pb2m8ey3DU8NfWPNzoNYEb5daynwYc94fjoGriNtgryJHQWJqmgKnEDqGmG98gSCOG_EOFS5OEqYu6phT3mxz8Kv4_mIt9KseCgw-N_hWiPphvWOEdbgTajG3pSPqSYNI0cfBGqlC1KVjpkKDrelSlvFmmfhe_wWgiLfL2lMXuqIZd2p0XoXvAiYM0-ceauinS3x3JE5HLea73jO1XQJIskgQfPDcBLLZ4VHO7p8OgXFXsSUQ9l5R8Cy9xp4otTLqBvBirGuOM7mif09g4oJwX2TA77yWIE3Jbb5xllZCgXgj3Kb1-SovRsjzJbxA6IJkCniSPDDT5JywooMvCX-e4adDTmx-KmUrLR6VxxljersXFMCYGFebgJ_uXiemr2l-lt0NQ9mhpSP45ZkhhENjwtEhe_ZzLcaO3e8og7GNBdc5I7m8NyoSWyHQz3HCM5rRKyzU_Uc5hRRA_-De_u0e-6iQ1qn2X9hZTfcePzXGvjD2ceJbcVesDj-hXiAMEuhj6kit03BhM7_GdWz_uPZwSWDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: قطعا برای گرفتن حق پرسپولیس کوتاه نمی آییم
◻️
ناراحتی دوستان از رفتنم تا دفتر ریاست جمهوری؟ حتی اگر لازم باشد از مراجع بین المللی هم پیگر حق پرسپولیس هستیم
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.29K · <a href="https://t.me/SorkhTimes/132815" target="_blank">📅 22:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ApwK5ayK_rKTzs3ePenhQkENL4G8IsgcBBDHJNDGgSX_yE9FGKcgAKJ4e0Sa1AwyOWcmCL2MliGIA50NvfdfrEhE8GHOF6_BvZ7_uMnYLNlhiB-m7PqviXiIt8UwzALdD3vDjCdArQlcQQNUN1Fe7WBDH5p7lNNETdmwToaoz7OI_dez8TEl4baP0noqzLIGCSxYOpqQv9oEknNbaaFCxlbI3zkpodzZ0qao_bgrCgORS34uXCbw_2um4UTjaRaM8O8sGV3ASc_NuVK2aX3799IwvthMHKm4l-dxbk6sWbcYU6lAghpkNhx0nZeFqPxyI4_hrrByLuX6cmX3BHuHTFJxHVWmLo09IhJbiUyIYwQDtgGWTLNf85h9cA9wCVwKc1yfNVDf5abdLfKR6TDjMa5jbaXNmaP9sNm06dFzaTCdhWPqpixRE049FBSKECjyNtqqY7zJBIC0E_L9kabO3aESFUrwBJYp_rXGh1EFGr6w0G7AxVXMupLMnmECkADYPqpKG55s6mo3tbBI31971S7w3TS4tSSMc95BeikClw21DNvWWxnD5KeXX-ZEoOOnVNr8AzA1EuKF4yb-kcKRpd4hYqh9T7k_4Z1PAvIktehc04ljgDvpqWtSPdPt3YqzWP-TxW2U0-WKsoluRlf0UdU1v_RnoSRWGWcR40Jq5iY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c7fcad3a9.mp4?token=ApwK5ayK_rKTzs3ePenhQkENL4G8IsgcBBDHJNDGgSX_yE9FGKcgAKJ4e0Sa1AwyOWcmCL2MliGIA50NvfdfrEhE8GHOF6_BvZ7_uMnYLNlhiB-m7PqviXiIt8UwzALdD3vDjCdArQlcQQNUN1Fe7WBDH5p7lNNETdmwToaoz7OI_dez8TEl4baP0noqzLIGCSxYOpqQv9oEknNbaaFCxlbI3zkpodzZ0qao_bgrCgORS34uXCbw_2um4UTjaRaM8O8sGV3ASc_NuVK2aX3799IwvthMHKm4l-dxbk6sWbcYU6lAghpkNhx0nZeFqPxyI4_hrrByLuX6cmX3BHuHTFJxHVWmLo09IhJbiUyIYwQDtgGWTLNf85h9cA9wCVwKc1yfNVDf5abdLfKR6TDjMa5jbaXNmaP9sNm06dFzaTCdhWPqpixRE049FBSKECjyNtqqY7zJBIC0E_L9kabO3aESFUrwBJYp_rXGh1EFGr6w0G7AxVXMupLMnmECkADYPqpKG55s6mo3tbBI31971S7w3TS4tSSMc95BeikClw21DNvWWxnD5KeXX-ZEoOOnVNr8AzA1EuKF4yb-kcKRpd4hYqh9T7k_4Z1PAvIktehc04ljgDvpqWtSPdPt3YqzWP-TxW2U0-WKsoluRlf0UdU1v_RnoSRWGWcR40Jq5iY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: اینکه هواداران پرسپولیس را مقابل فدراسیون فوتبال قرار دهیم کار درستی نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.45K · <a href="https://t.me/SorkhTimes/132814" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=vB_rahYrZ6qiL-uxDBYvqaW68FrA58WSOAAFTl747Ozrz_DElcwlMYcsjOGmYEvOJf9StCf2jyvRxM_F_yZmsOSh_1pIEP2IjV7q6jAG_9akCb1DekqwHqtVdvl6k32PCcXkCOn7YObh-rUpbj6Iu7ZLHp-pb_EpPjRfi52k1yWXRmIsYc_-GYabqWPrNDZfad1PMIUarh2MATF_ZfuT_k09qGQQK3XAxvARAY44kdbs7xX0lYQlriN6ZXk4U6WvaC7npioug1a2eQOHsLIKhn_9Iza7oXXOZkOvXr1gyLEy0cgRkSkgst7wYWroAqZNBpdJH5P5ruIKxht-4912iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73ccb46629.mp4?token=vB_rahYrZ6qiL-uxDBYvqaW68FrA58WSOAAFTl747Ozrz_DElcwlMYcsjOGmYEvOJf9StCf2jyvRxM_F_yZmsOSh_1pIEP2IjV7q6jAG_9akCb1DekqwHqtVdvl6k32PCcXkCOn7YObh-rUpbj6Iu7ZLHp-pb_EpPjRfi52k1yWXRmIsYc_-GYabqWPrNDZfad1PMIUarh2MATF_ZfuT_k09qGQQK3XAxvARAY44kdbs7xX0lYQlriN6ZXk4U6WvaC7npioug1a2eQOHsLIKhn_9Iza7oXXOZkOvXr1gyLEy0cgRkSkgst7wYWroAqZNBpdJH5P5ruIKxht-4912iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: واقعا چه اصراری است که رای کمیته انضباطی شکایت یک تیم از تیم دیگر در روز  تعطیل اعلام شود؟
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.5K · <a href="https://t.me/SorkhTimes/132813" target="_blank">📅 22:23 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=lnlTFtDQX4w1YOj2pzqJjl8gk-5l0TQhQrDTO2W35LueXZU0vDp-K2PXNUXapKzHCQO_CtoX9QTM1arm4vrFt5nB038tKB_6ZmR3NvC__JakW_ZQbDavvv_TIGN5g8XAgKk7xCksyYVeAWr8NbjoxZywtjaDO8rvaN46JdN-D9Y_MCge3o6lk1SxJv1sScvU-O9RFG6JSZDacuqZkEVCywn_tPbBZjYE2MGZMVrj6zAyGVpL85kMK28dfLg7CSoHaK6qdJb1eMlUz2-Q7QU1ZkHir9E7J-Tp0OojT7tQWroBdIaMEtISKCuvOBlpYUwaDpuAO9HQxl3Q_EGJ8ITzCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d515e687b.mp4?token=lnlTFtDQX4w1YOj2pzqJjl8gk-5l0TQhQrDTO2W35LueXZU0vDp-K2PXNUXapKzHCQO_CtoX9QTM1arm4vrFt5nB038tKB_6ZmR3NvC__JakW_ZQbDavvv_TIGN5g8XAgKk7xCksyYVeAWr8NbjoxZywtjaDO8rvaN46JdN-D9Y_MCge3o6lk1SxJv1sScvU-O9RFG6JSZDacuqZkEVCywn_tPbBZjYE2MGZMVrj6zAyGVpL85kMK28dfLg7CSoHaK6qdJb1eMlUz2-Q7QU1ZkHir9E7J-Tp0OojT7tQWroBdIaMEtISKCuvOBlpYUwaDpuAO9HQxl3Q_EGJ8ITzCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس: کدام جریان به دنبال ضرر پرسپولیس است؟ همان جریانی که دنبال این است که پرسپولیس به آسیا نرود، همان جریانی که مانع برگزای لیگ برتر شد
.
نباید از این موضوع به سادگی گذشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SorkhTimes/132812" target="_blank">📅 22:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🔴
حدادی مدیرعامل پرسپولیس:
اینکه چه جریانی باعث شد که بازی‌های لیگ برتر برگزار نشود واقعا جای سوال است/ در سال‌های گذشته هم که پرسپولیس قهرمان لیگ برتر می شد در هفته‌های پایانی امتیاز جمع می کرد و قهرمان لیگ می شد/ این احتمال وجود داشت که باشگاه پرسپولیس به صدر جدول برگردد، واقعا این جوای سوال است که چه جریانی مانع برگزاری مسابقات لیگ برتر شد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/SorkhTimes/132811" target="_blank">📅 22:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132808">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🚨
لیست مازاد اوسمار از نگاه رسانه های تلگرامی:
🔺
تیوی بیفوما
🔺
امید عالیشاه
🔺
میلاد سرلک
🔺
محمد خدابنده لو
🔺
سروش رفیعی
🔺
دنیل گرا
🔺
مرتضی پورعلی گنجی
🔺
سهیل صحرایی
🔺
یاسین سلمانی
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SorkhTimes/132808" target="_blank">📅 21:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132807">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jIBTp4h1iQirC_A7VG0gxYqX9qAXiNEYlu4ivwJYYjfxxKC0mXLXfO6qlSe13HZ7mZtpNz9NIZ7pg1B2QhMbuZjAM26xqNrCRhNYgcVxyVHNiqmRg3fHxzP1zxN3xaqkSI21vRg1a4c9RSf90iOJMzsB2d2S7BqnRL2UUhql4Y_gN1XlWV52zAne3RtYurU3cMDEPrBRfcQcD3oWucWldGidXlgObKpTVoi-t6wZiNSDzjw0oYP785EsXDFKlkxzpwZ5S8kSuhMKtJW_oFImSFQ3W2IUyV3B4mGIqGUQOdagx_vBdINzxXWBi9zXt1RE0c_8ten98sZ3qJJW-KPaag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس نیمه‌نهایی رولان‌گاروس بین
ماتئو آرنالدی
و
فلاویو کوبولی
رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/SorkhTimes/132807" target="_blank">📅 20:21 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132806">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">❗️
ادعای علیرضا محمد، دستیار تارتار در گل‌گهر: باشگاه پرسپولیس با تارتار مذاکره کرده و اگر اوسمار برنگردد، تارتار سرمربی میشه! او می‌تواند پرسپولیس رو قهرمان کند! باید چه کاری دیگر کند تا سرمربی شود؟!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس…</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/SorkhTimes/132806" target="_blank">📅 19:34 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132805">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🔴
خبرنگاران کاخ سفید میگویند که ترامپ پستش را بد نوشته و در واقع اعلام پایان محاصره نکرده و منظورش این بود محاصره رفع میشود اگر رژیم ایران با این شرایط موافقت کند
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.46K · <a href="https://t.me/SorkhTimes/132805" target="_blank">📅 19:33 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132804">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/SorkhTimes/132804" target="_blank">📅 19:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132803">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🔴
شانس دوباره محمودی و حبیبی‌نژاد در تیم ملی؟
◻️
امیرحسین محمودی و هادی حبیبی‌نژاد هنوز شانس حضور در فهرست نهایی تیم ملی را دارند و به‌دلیل احتمال مشکل ویزا یا مصدومیت برخی بازیکنان در اردو نگه داشته شده‌اند. در مقابل، امید نورافکن ظاهراً اردو را ترک کرده است/فرهیختگان
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/SorkhTimes/132803" target="_blank">📅 19:09 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132802">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🔴
باشگاه پرسپولیس:
‼️
ما با آقای تارتار مذاکره نکردیم. این حرف‌ها برای بازارگرمی است. پرسپولیس تاکنون هیچ‌گونه مذاکره‌ای با تارتار یا هیچکس دیگه‌ای نداشته و این ادعاها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SorkhTimes/132802" target="_blank">📅 19:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132801">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🔴
علیرضا
محمد:مذاکره تارتار با پرسپولیس را در رسانه‌ها شنیدم / به خدا نمی‌دانم به او پیشنهاد دادند یا نه
💢
من در آن مصاحبه ویدیویی هم گفتم که در رسانه‌ها این مطلب را شنیدم و منظورم این بود خیلی از رسانه‌ها گفته بودند که مهدی تارتار مدنظر پرسپولیس است. خدا شاهد است صادقانه به هواداران عزیز پرسپولیس می‌گویم من اطلاع ندارم که باشگاه پرسپولیس با مهدی تارتار مذاکره کرده یا پیشنهادی به او داده است یا ممکن است بدهد.
💢
من فقط نظرم را گفتم و هنوز هم می‌گویم اگر قرار است آقای اوسمار نیاید مهدی تارتار می‌تواند مربی خوبی برای پرسپولیس باشد. ولی اینکه با او صحبتی شده یا نشده به خدا من اطلاعی ندارم. امیدوارم پرسپولیس موفق باشد و وضعیت کادرفنی زودتر مشخص شود و نتایج خوبی بگیرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.8K · <a href="https://t.me/SorkhTimes/132801" target="_blank">📅 17:51 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132799">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/plDQM9C5pBQnnkSWyr3embziZFaqIXFGw0py_Omh4DrYnjm6F6MznRilP7g4M6VocGzZaj9Virw_lG_1U4LAR9U-8I9uLho_-y12UuT--gS9K2eMAtw6B9DNA0Dn_jnYnrOLi0qMhOP2TwFT4DmcksKH97WyLxTkYfVuay-lDqo6yuopCvETYRsb6pjyEeBm-SorO_oUqrjEOWhe9wFyelIT99zLwbHw7dLU17bJsvaBWmqqtEF-37WWTSX6SFmyc_VO8WEZKv4WWFoOXS3CgPBhy3PQEhqdDChAu_b3s2QDuBTbZL2FRgqRW3CAsGjsVzhBhHoK-n5NwKabtX9mKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
🇫🇷
دیدار جذاب و حساس نیمه‌نهایی رولان‌گاروس بین
منشیک
و
زورف
رو با آپشن‌های مختلف در اسپورت نود پیش‌بینی کنید.
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/SorkhTimes/132799" target="_blank">📅 17:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132798">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJX2jafniNiMRehF71SlVl2lK_UnT8nZqysSUtljwtxhJVluvVreuJhuXtRmpwCX737yivcIGzuv1Z6ewQ8Z-nEDAwxzFOA4UZ_U4I8nAXRMwxsZTNNjg62auEUflN9TgvAQPBRGNjzrYTUPl-NgW-nsVgAwyHPbJO4nzHmTdFjZlhFIg8k2lXR2j6RW7C-8XyaG_cUFCz8jMSJrvTHT-_gCOAP_Lty8stoAZiUQJHPIzK_FJrotza5-2CAaVUYJhY_Ioo10xwhItCxQiE0CDhLn49zmPV-OF51bVFIrlpQCrPLR3HWXiBYkG6Lfw1BtgKpKqOQRxKX2qszAnd6xtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
عکس تیمی بازیکنای نروژ
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/SorkhTimes/132798" target="_blank">📅 16:32 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132797">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🔴
فرهیختگان: پرسپولیس از بین محمد مهدی زارع، دانیال ایری و مسعود محبی، یک مدافع رو میخواد بخره.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132797" target="_blank">📅 16:31 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132796">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyCOjgQtldEg4iA4u4GCzP1qpUn64XTJS-TLEGLRzPx1DYQ-sZSMLbzcSU7OHF6RVb9GCfuOXOBmbDXRzkpgYXd0I4oeG2v-7qA9GN7XiehS6NSTWrkpg0N_z0muUO0bo7W6dmmcBLszZ7qJAqL5pkD1Q1j6R9AxVtpYKE_5yYTPnSsn7IqoOl4nWox186MX61mtMOQoqFn8I-hsw4EF_LVLDYH9RLchnttWJO169XFIKSkDLvtnBGsuaRAydsDIWGQVp4MF2V-hMR4K_o6vFoXNG7gm1zKN96INs9YXLVZd1Nntdj2QbVVg8tez8-OF5P4tmwtwNbAXCdb9yrzW0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔼
صعود یک پله‌ای در رنکینگ فیفا
؛
🇮🇷
ایران دوباره در جمع ۲۰ تیم برتر جهان
🔴
در فاصله ۶ روز تا شروع جام جهانی، رنکینگ جدید فیفا اعلام شد که براساس آن تیم ملی که در آنتالیا گامبیا و مالی را شکست داد، با یک پله صعود دوباره در رتبه ۲۰ جهان قرار گیرد.
📊
در این رنکینگ، آرژانتین تیم اول است و سوئیس و دانمارک تیم‌های قبل و بعد از ایران هستند.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SorkhTimes/132796" target="_blank">📅 16:29 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132795">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔴
🇮🇷
🇺🇸
🇵🇰
العربیه: ایران بطور رسمی به پاکستان ابلاغ کرده که با انتقال بخشی از ذخایر اورانیوم خودش به یک کشور ثالث مورد توافق طرفین، موافقه!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/SorkhTimes/132795" target="_blank">📅 16:28 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132794">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBCSR8fq6NtUQWkAFDlfs6WfmYPloB53aLFvcPM0kfA3ePmtuZHzvlpEz0U5ycwg4rtObJQSzVsEfgUDLgX_5IrxkWAnS47VwZwUfozInxTmkcmumQBqv9XQno9Q4_s6F0hvO7JKIO7oD7d5lbR1XNkKPmdKwvQZlHU4LPWQgLZGBtdHav_VsFyxd7k75vkWvWwHmPXBAMCh67FJSk21c2ZUxIb0CLv6KssydVEpQ1oQshMJ5KsAGgS9h00WOPctu4UNTn3G06u0S6b1F5f3D-2nz1Rk8gYO3Q4Bo9aAvkgNnOc8jdqinM2aDlpuPBctgMBHzZpNF5GlrkMn5So8Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
فیفا تأیید کرد که نقصی در وب‌سایتش باعث شد ده‌ها هوادار بلیت‌های رایگان جام جهانی دریافت کنند!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.9K · <a href="https://t.me/SorkhTimes/132794" target="_blank">📅 15:49 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132793">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txP1-AwyUvMmcNcREm28OuAhGBGWLu07XNo7UAHGFH-xilcPjNF5T6wHmQKnAOA1soPc0Ei86Gcki-DDFzx4PG1xsMD3PTJkPYMhVw5pONRdju607h-jb6uTsfYo5utauFlD1vLWI-w5aqb76Ve3tgj4whZVkWsl8RWZTaYnD0FF0Qod2C-Bvl7LAmb0QdLCzTKfcpSrJNA0dqQCOfzjsG4Py4cNJfOmVdatJ_V4arxDEiFOPT8w60j6xCO589LkW2q48SVhJkKYSmi3kKOaC4bfRTF_RSjcoI19XZnL1eaOVhjuUHMdle6ZMjJy2O9bn2NcD_NwkaZXlHPJeXaYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سروش رفیعی به طور رسمی از پرسپولیس جدا شد. سایت ترانسفرمارکت هم این بازیکن رو بدون باشگاه اعلام کرده.
🔴
رفیعی در فصل اخیر طی ۲۳ مسابقه به عنوان هافبک بازیساز، آمار صفر پاس گل رو ثبت کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/SorkhTimes/132793" target="_blank">📅 15:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132792">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVl6oO3cPc6tDecdl7DJ_174wxRNWRHv5RnDzlnE8U2pTVMv-QSIM02_XVZwEhPcJBLjNUO8Jg0GzvviUxncRIwsSRlk2XaZyK-seDzE6NNpDSgmxsjo7AmNtMXG0txbpdMTJYgRvE6I_f0glve5MXFpmIhBdTpmuubtbcP4CZLXxU-jn3OXz_F2yN_sWKvfgsOhn3OHQBO9piv5asLPXZmqOW0AjO0aUVlIMRa-WT7oQVUiSLhFEGu4YmzsBdOF8HiHkFYAgy0r_VdbouCEUsi5mnywGtkSRtG7OUVfxqYKtg0Rk4e1zy9Yq4vWNFI9Vz1NbN_IrqAsBg1vZpUxNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
با حضور در لیست تیم ملی، میلاد محمدی سومین تجربه حضور در جام جهانی را خواهد داشت.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/SorkhTimes/132792" target="_blank">📅 15:43 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132791">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">✅
🎙
مهدی تاج:
⏺
فقط با فیفا در ارتباطیم و هیچ تماسی با ایالات متحده نداریم. کشور میزبان حق اختلال در تیم را ندارد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SorkhTimes/132791" target="_blank">📅 15:42 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132790">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔴
شبکه العربیه از منابع مطلع:
🔴
جمهوری اسلامی میخواد اورانیوم غنی‌شده‌ش رو به چین بفرسته، به شرطی که چین تضمین کنه این مواد رو به آمریکا تحویل نمیده.
🔴
به گفته این منابع، خیلی از نکات مربوط به برنامه هسته‌ای جمهوری اسلامی تو مذاکرات الان حل و فصل شده.
🔴
بر…</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/SorkhTimes/132790" target="_blank">📅 15:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132789">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🔴
با اعلام ایجنت سروش رفیعی، این بازیکن پس از سه سال از پر‌سپولیس جدا شد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132789" target="_blank">📅 13:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132788">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132788" target="_blank">📅 13:06 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">‼️
اول یا اخر هرکسی بیاد و بخاد بره؛امثال سروش و هرکسی که حاشیه سازه و از نظر فنی به تیم کمک نمیکنه باید بره
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SorkhTimes/132784" target="_blank">📅 09:13 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132783">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">❌
در سکوت و سکرت....  فعلا،مذاکرات داره خوب پیش میره///قرمز آنلاین
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/132783" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132782">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SorkhTimes/132782" target="_blank">📅 09:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132780">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCWBqUvTQ7wkHSrxVscme6vc7d3b_a5H8Dw7T3uSL6DH8GVcZKCBBm3QXc0UzrV6Qr-CmEXcBarlhuqRq7wjXFdbE6Xzj2xVci9YdBKc_J0Gu5QA4RStI_gJ22UhMGg63djweRRIh2CamskEsDD8paDbjFsSryRTMpr5EzRbj_39qxj35ML90Nj64UduTqn5nFUQkFyw0Cqv1xdcRmT-WT6530YdGC8O0r5cEeTHLnQw4F3anxv8jHDWKT6fZrRpMdJeZ6pKaJjsKcl4LTIOmzprlxvosHxu9mUc0t1jigr-up1NjyHDpSBrUqoRnnRzKIWdl6cJ68hWwh594VOtvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Sportnavad
➕
| اسپورت نود
➕
⚡️
هر مسابقه یک فرصت، هر انتخاب یک هیجان!
🔗
ضرایب رقابتی و متنوع فقط در سایت معتبر اسپورت نود به همراه:
👇
شارژ از طریق کریپتو
واریز و برداشت سریع
پشتیبانی ۲۴ ساعته
کازینو آنلاین و بازی انفجار
پیش‌بینی زنده تمامی مسابقات
🎁
بونوس ویژه ثبت‌نام برای کاربران سایت، با شارژ حساب از طریق کریپتو ۴٪ بیشتر از مبلغ شارژ حساب دریافت کنید.
🔗
برای ورود سریعتر به اسپورت نود از طریق ربات رسمی سایت اقدام نمایید:
👇
🤖
@Sportnavad_bot
🤖
@Sportnavad_bot
🔗
کانال رسمی اسپورت نود:
👇
✉️
@Sportnavad</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/132780" target="_blank">📅 01:12 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132779">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
امروز عراق با اسپانیا بازی می‌کنه و جمهوری اسلامی با مالی!!!!!
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132779" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132778">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132778" target="_blank">📅 01:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132777">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=bc8glIggcduFS1hW6I4hmAmuG6PruWGMgQJu9nto5E8fIBQVa_tPZOsd91wKhApViWG3itnQH3nlkDdYjCg-C39vPLGmHNjpwUCws7UrDnQr4Nk7Le18lmbX8BGAVGo9ezpujZhkafQRdBkWPFafaUtQr2QY31eFq0eMsw9WBZI6clH-yYKsMlJywuNuM2e-3BUYunDCKPHdhxGtuDJpJXS8CJ7NZ49pm9qOYSOZZrN3HTr8U9gDZPGrCV19Sq02vusFbm1rKPHdX08Z2vHhhiEpoQ3GmcF7Q5vygzzO9mBN8PcSUnG9Jff3Kxv7qkpQRmwMGuH_LEJnk07lv_dRnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85f9110aac.mp4?token=bc8glIggcduFS1hW6I4hmAmuG6PruWGMgQJu9nto5E8fIBQVa_tPZOsd91wKhApViWG3itnQH3nlkDdYjCg-C39vPLGmHNjpwUCws7UrDnQr4Nk7Le18lmbX8BGAVGo9ezpujZhkafQRdBkWPFafaUtQr2QY31eFq0eMsw9WBZI6clH-yYKsMlJywuNuM2e-3BUYunDCKPHdhxGtuDJpJXS8CJ7NZ49pm9qOYSOZZrN3HTr8U9gDZPGrCV19Sq02vusFbm1rKPHdX08Z2vHhhiEpoQ3GmcF7Q5vygzzO9mBN8PcSUnG9Jff3Kxv7qkpQRmwMGuH_LEJnk07lv_dRnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ: مجتبی خامنه‌ای کاملا تو کارش حرفه‌ایه. البته یه سریا در موردش بد میگن که دروغه، مثل من که یه سریا به دروغ در موردم بد میگن.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SorkhTimes/132777" target="_blank">📅 00:58 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق…</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/132774" target="_blank">📅 23:04 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2Rt16BP8reIhZb2u-zHP6whMrKIpsGub9g5JOb_T5kgw4raA3IaFW7VRsEinXVzNyDx5LahkwovmoAg19_nLLM8-P_x74bAtyh9SZCxaWDB6d9cp8hAOA0r5wiTeUGKP4MT96li0uQntnivDIsWsnPoGwpENDhduPMgIxQUYMoO7DpzicBkZNNoREFr3DjiN3cOMAauz6EDGxEg61K3XnztgzwbjlYkZOuWNjrdQeMgNCJz-oO0HewkpujIFRy4qsLf0ERuVmHB_tRLuEsgahGDAvKYr5vMFFjipTFEQdMG1ATX-PM68VvA8Cf4oly9AbgNJzkB7zB-YFEq24OH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
ایران با دو برد مسافر جام جهانی شد | سعید عزت‌اللهی دقیقه ١٢ و رامین رضاییان دقیقه ۵۵ گل های ایران را به ثمر رساندند
ایران ۲
مالی ۰
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SorkhTimes/132773" target="_blank">📅 23:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
فووووووررررری
🔴
حمید ابراهیمی : با توجه به نیاز حداقل 2 هزار میلیاردی دو باشگاه چادرملو و گل گهر سیرجان برای حضور در آسیا وزارت صنعت با این موضوع مخالفت کرده و به زودی انصراف آنها از این موضوع رسما اعلام می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SorkhTimes/132772" target="_blank">📅 22:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132770">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcF12O_PMv0euIG-6qDi9XM8kuGFnCoPnZqzSu5NFl67AzZ_5YKazJetf45DChhPrHu9l9nmvf1p5Y__KLDv57h8LVu1tqjD42K5Z-1hQias60I-Q9k5_x3cN8Eq5lzzm_dztdlx-o2WolnxRwcn_gtPCobjgq9KV-IaSYeNvukYrlGmmzRFTnoSE3HN7L0A_04OXZglAQble7ndmAzmozYidACix3_vncs4jpsRU60Tu6KeBmI36a5eGtDzFNrpoVhm8H75AGKUouEHy3tN-wk3HOSNy2CekV_VFVimosnMR3ILoLJqhfnWns-1fo7V9S4t-tMaqu60U-DdDid6AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❗️
گفته میشود که قرارداد امید عالیشاه با پرسپولیس به زودی تمدید می‌شود
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SorkhTimes/132770" target="_blank">📅 21:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132769">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X8T1lIILIfXf51Yp1IP0j7a7uBCXNveX-woJEqS0hE_g56uz0740Uj5M3RZ83Ja7ywOS-PMSZlKFQ9yk91XsiqkNNq-rT3JDXwIBjQ4xroqpV2lqv19t_VtBVlIGxYaItR6zQlay6M2FIpaRSt7DYEYnMCtDqgUiLo2BZRac7ExZWLcbIm2JcPvdMyVsgRuy7pq4rafA42_p8HL8AXiKMoSDEYCj9pkikX3tACMzyhPKLbhxxaCqDds-kxUGw4ssaCjrxuP6-9XNCLEQ3S4S8GEO0yW9XJOG-P9iksDiXuE3x47khB0Dak9N08B_EbquDpyocWTg-HdLyz8fBfbGuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
تسنیم:
🔴
استقلال درحال مذاکره با اسکوچیچ سرمربی سابق تراکتور است و جزو گزینه‌های خارجی این باشگاه است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SorkhTimes/132769" target="_blank">📅 21:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132768">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔽
تیم ملی امشب از ساعت ۲۰:۳۰ به مصاف «مالی» می‌رود. این بازی پشت درهای بسته برگزار می‌شود تا بلژیک و مصر نتوانند به اسرار تاکتیکی قلعه‌نویی پی ببرند
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132768" target="_blank">📅 21:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132767">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">✅
فوری کمیته انضباطی آندرس بازیکن چادرملو را غیرمجاز اعلام کرد و نتیجه بازی این تیم با گل‌گهر، 3 بر 0 به سود گل‌گهر سیرجان اعلام شد.
🔺
گل‌گهر با رای انضباطی، به رده چهارم لیگ برتر رسید و اختلاف امتیاز آن‌ها با پرسپولیس به 5 امتیاز افزایش یافت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SorkhTimes/132767" target="_blank">📅 21:22 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132766">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwv7SftfzPK7iEuL-YI0NsYAY8WuqItOi_o1hzOINDHaIYhcDma7tY3kbp0zZT2gHqjQ1iDYAPtjANcq9RuSXpH3aimmLv1bzhGf6gfzATxtlrV7A0grpmeQn68Dg8GvWMdbfwbi-bpJWDcw_AcL0uMTlibYLTdZAHQBOFn52mRiKblY3XICx13sKM0CzAAZK4RK-VNOK8iUrGS7rkEW4z6bZ0NrPtU4J1BQjJcCb8Pwumflm7fYg9DIsYyNH7hL2w7jWkIYz050FhXE-KLn6aXEm9lsgErXDuSD0E9FFYQzGYigCZjJyp_GqkdqnDai0I9kuqW1gzB9t0aLxJ2jiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امیرحسین محمودی علی رغم خط خوردن در اردوی تیم ملی حضور داره و قراره همراه تیم ملی راهی مکزیک بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SorkhTimes/132766" target="_blank">📅 21:21 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132765">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=L_Ad3D3f_YQqY0_YWJlaVhgbSObEmg2-SHJh2wtab3B2vnQxEyddJyn4jyWo0b4kbpKW0g_aHQq691V2Dm0O59PW_wbtopp1aV7HbQ4Gxot4mcgIMT_f_-sVa7GaEN872rX0h6TWe8BYG_JDB6kwJuq1T5ZzVVTIvuQm6CLqA37IDYG3FcbKf9-EIf_O3tT_jL3FQFvt3HOr2Ddb4yrZ_lUhTaPJJFjMviSax_xDOh96OI831QHtZAhDwpko2uwMVPbHGhK_SQhnjhve081kjcVJLXBEA_83jfCdBC-MwzymQK0t6tCtGkluzWieLSUvWOuqVeYu6lxLEKy34pRAUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e786c6b741.mp4?token=L_Ad3D3f_YQqY0_YWJlaVhgbSObEmg2-SHJh2wtab3B2vnQxEyddJyn4jyWo0b4kbpKW0g_aHQq691V2Dm0O59PW_wbtopp1aV7HbQ4Gxot4mcgIMT_f_-sVa7GaEN872rX0h6TWe8BYG_JDB6kwJuq1T5ZzVVTIvuQm6CLqA37IDYG3FcbKf9-EIf_O3tT_jL3FQFvt3HOr2Ddb4yrZ_lUhTaPJJFjMviSax_xDOh96OI831QHtZAhDwpko2uwMVPbHGhK_SQhnjhve081kjcVJLXBEA_83jfCdBC-MwzymQK0t6tCtGkluzWieLSUvWOuqVeYu6lxLEKy34pRAUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▪
︎ اگه این روزا سایتا سخت لود میشن، ربات تلگرام وینکوبت خیلی کارو راحت کرده:
👇
🤖
@Wincobet_bot
بدون اینکه از تلگرام خارج شی میتونی مستقیم وارد بخش بازی‌ها و کازینو بشی، پیش‌بینی ثبت کنی و حتی واریز و برداشت انجام بدی.
▪
︎حالت Mini App داخل تلگرامه و خیلی سبک‌تر و سریع‌تر باز میشه:
👇
🤖
@Wincobet_bot</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SorkhTimes/132765" target="_blank">📅 20:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132763">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfkYL2ROK8gSITswy-EHa_1rO_qbrr3Q_ZJ_5GX4NDQs4LaVLgxmmmu07jVblCMsUTyvY-GK3dRQEHRe-E-AR8gG5ORZkgWwBUMdbo3H074nwIh66RcM59Xbm7zpOtmpLslODAQ2PE7nv75OBg--tdQEZzAWlFWSWHAbW2P7INZyS8FKmLCN_bi6Munj-iKxcZnV-QxlUU7XAcFuumKoVSDuHYqN7o7BHdpLijEkuSEvV5Wuj3ZkTdzJsaDf05sUPCDi3kO2EYB0AKSRIuPJknZV8elorFTvRJD_qh5bLh9OtyZ0OgIfPiJOHQQuC6QrtlAFN5RCsUKA15MH0mMp4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#رسمی
| با اعلام رسمی باشگاه بنفیکا، رئال مادرید بند فسخ ۱۵ میلیون یورویی ژوزه مورینیو را فعال کرد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132763" target="_blank">📅 19:36 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132762">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">✅
فوری کمیته انضباطی آندرس بازیکن چادرملو را غیرمجاز اعلام کرد و نتیجه بازی این تیم با گل‌گهر، 3 بر 0 به سود گل‌گهر سیرجان اعلام شد.
🔺
گل‌گهر با رای انضباطی، به رده چهارم لیگ برتر رسید و اختلاف امتیاز آن‌ها با پرسپولیس به 5 امتیاز افزایش یافت
🎗️
«سرخ تایمز»…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132762" target="_blank">📅 19:35 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132761">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❗️
باشگاه گل‌گهر از چادرملو بابت استفاده از آندرس، بازیکن پارگوئه ای شکایت کرده و خواهان 3 بر 0 شدن مسابقه این تیم برابر چادرملو شده است؛ در صورتی که چادرملو در این پرونده محکوم شود، جایگاه چهارمی خود را از دست داده و به رده ششم جدول سقوط خواهد کرد و پرسپولیس…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132761" target="_blank">📅 19:34 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132760">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔴
یاسین سلمانی در پرسپولیس میماند؟ آخرین گمانه‌زنی ها از ماندن ستاره خاموش پرسپولیس
◽️
یاسین سلمانی که پس‌از پارگی رباط صلیبی خود بازگشت موفقی در دو فصل اخیر سرخپوشان نداشت، بنظر میرسد یکبار دیگر شانس به او روی کرده و اوسمار ویرا قصد دارد این بازیکن را به…</div>
<div class="tg-footer">👁️ 4.39K · <a href="https://t.me/SorkhTimes/132760" target="_blank">📅 19:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132758">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🔴
⚠️
طبق تست های انجام شده روی اینترنت مخابرات و ثابت ایرانسل وضعیت اتصال به دیتاسنترهای خارجی و اتصال به VPN کاملا پایدار شده است !  اینترنت به حالت قبل از ۱۸-۱۹دی برگشت
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/SorkhTimes/132758" target="_blank">📅 17:47 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132757">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59133ac2f8.mp4?token=qPgFdBdcG4IHVHNeIhrfb0ruRJ76TM7jYhEDfwQSnuYbBlBi72C87egSWOFXVMXMBn6Bio5JohhfKID_iEl7YJ0H8UWTIuLMvGe8g63PTRZ96zxT6pTEcvxfGuCbp-V6FaFemrqBALTZ3GkcxwNxkjNtDozu17h5A704a7998-y8HiDLk7UDYX8WiQoh9yqR-T5uWtCYSDCAmOojetcEdlJ4Z3mCniehuRDKV6mN6FKgx23bB-2UPsdxQTCkH1hm1IPYGD7Ckgpc0iNmv5VwkI9AuXe8AS5S8GfjwQbTKBg52S8OgbiLy8U3VURKSADYdPFDPxb_OR7M0g3WJUDZPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59133ac2f8.mp4?token=qPgFdBdcG4IHVHNeIhrfb0ruRJ76TM7jYhEDfwQSnuYbBlBi72C87egSWOFXVMXMBn6Bio5JohhfKID_iEl7YJ0H8UWTIuLMvGe8g63PTRZ96zxT6pTEcvxfGuCbp-V6FaFemrqBALTZ3GkcxwNxkjNtDozu17h5A704a7998-y8HiDLk7UDYX8WiQoh9yqR-T5uWtCYSDCAmOojetcEdlJ4Z3mCniehuRDKV6mN6FKgx23bB-2UPsdxQTCkH1hm1IPYGD7Ckgpc0iNmv5VwkI9AuXe8AS5S8GfjwQbTKBg52S8OgbiLy8U3VURKSADYdPFDPxb_OR7M0g3WJUDZPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
🎙
صحبتهای عیسی ترائوره مدیر تیم ملی مالی و بازیکن سابق تیم فوتبال پرسپولیس:
🇮🇷
ایران در قلب من است
⚪️
کشور شما به من همه چیز داد و خانه دوم من است
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132757" target="_blank">📅 17:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">❌
خبرورزشی: اوسمار تاکید داره درصورت شرایط عادی بمونه برمیگرده و نمیخواد جدا بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132756" target="_blank">📅 17:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
♦️
تاج: مانع اصلی ویزای آمریکاست که نمی‌دانیم در چه مرحله‌ای است/ سعی می‌کنیم با پرواز به لس‌آنجلس برویم
🔹️
رئیس فدراسیون فوتبال: پذیرفته شد که بدون انگشت‌نگاری ویزای مکزیک را برای تیم صادر کنند. دو نفر مانده که آنها هم در کنار تیم هستند و تا ساعات آینده این…</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/SorkhTimes/132755" target="_blank">📅 16:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‼️
بزارید تکلیف سرمربی برای فصل بعد مشخص بشه بعد درباره لیست ورود و خروج صحبت کنید،باتشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.21K · <a href="https://t.me/SorkhTimes/132753" target="_blank">📅 16:42 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132752">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">‼️
بزارید تکلیف سرمربی برای فصل بعد مشخص بشه بعد درباره لیست ورود و خروج صحبت کنید،باتشکر
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/SorkhTimes/132752" target="_blank">📅 16:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132751">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس تاکنون هیچ لیست خروجی به باشگاه اعلام نشده و حدس گمان ها در رابطه با مازاد شدن برخی چهره ها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس 𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.26K · <a href="https://t.me/SorkhTimes/132751" target="_blank">📅 16:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132748">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔽
اینترنت بین الملل وصل است اما مردم دسترسی به پیام رسان های خارجی ندارند
🔴
قطعی حدودا سه ماهه کاربرا و به پایان رسیدن اشتراک های فیلترشکن آنها باعث شده، تا با وجود وصل شدن اینترنت، حدود 80٪ مردم در اتصال به تلگرام و سایر پیامرسان های خارجی دچار مشکل شوند.…</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132748" target="_blank">📅 14:50 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132747">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkJOj5-Cmg5i8UaTkM3uubmSl7j6HJdorSv75WBXVvJ1fU1Tf8MF7q0VMcBOWM1zXZL5nxE7ibwlMG-Pg6TWFEwrAsmw76aGOufEA0JUAgX_IJcd3lyk9YtEQMkD_2noRQ0KFVZO-KEYX8buzgWMdGpwlvncxsU81J5qLVAOYYtCTPhP9teY28tnqLegTv1ZBJ8zyvmgUvYR4L0r9WAmRsSdzX7X9V8JP-P63Mvb-SM5fTC8YdGNAIDc6gh_TV5jrPGZ3_WMaxp2XAuRKLIdLEnTPtcNCRSH2uF-N0BXcvkQBSYjdQxfcWKkIS0EVs3plmwftdmMptpOpqE-KuT5JQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی طارمی در گفتگو با الجزیره: آمریکا باید به این اصل که ورزش از سیاست جداست عمل کند
🔴
اتفاقاتی که در حمله آمریکا برای ایران افتاده خیلی بد بود و ما فقط می‌توانیم با بازی کردن دل مردم را شاد کنیم.
🔴
ما ایرانی‌ها آدم‌های صلح طلبی هستیم و دنیا درمورد ما اشتباه…</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/SorkhTimes/132747" target="_blank">📅 14:31 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132746">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">✅
فوری رسما امریکا پایان جنگ رو اعلام کرد
🔴
روبیو، وزیر خارجه آمریکا:   ما دیگر حملات مداومی در داخل ایران برای تضعیف ارتش آنها انجام نمی‌دهیم، زیرا جنگ «خشم حماسی» تمام شده است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.03K · <a href="https://t.me/SorkhTimes/132746" target="_blank">📅 14:24 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132745">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">❗️
علی دایی هیچ صفحه ای در توییتر ندارد و این توییت هم که وایرال شده ربطی به ایشان ندارد.این را با اطمینان می گوییم/قرمزانلاین.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SorkhTimes/132745" target="_blank">📅 14:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132744">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔽
تیم ملی امشب از ساعت ۲۰:۳۰ به مصاف «مالی» می‌رود. این بازی پشت درهای بسته برگزار می‌شود تا بلژیک و مصر نتوانند به اسرار تاکتیکی قلعه‌نویی پی ببرند
😁
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/SorkhTimes/132744" target="_blank">📅 14:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132743">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⚪️
تاج: ۱۰۰ هزار دلار به مالی برای بازی دوستانه پول دادیم؛ هزینه پرواز و هتل‌شان را هم پرداخت کردیم.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.25K · <a href="https://t.me/SorkhTimes/132743" target="_blank">📅 14:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132742">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">#اختصاصی_سرخ_تایمز
🚨
🔴
به گزارش رسانه «سرخ تایمز» و با اعلام مسئولان باشگاه پرسپولیس تاکنون هیچ لیست خروجی به باشگاه اعلام نشده و حدس گمان ها در رابطه با مازاد شدن برخی چهره ها صحت ندارد.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
𝓣𝓲𝓶𝓮
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SorkhTimes/132742" target="_blank">📅 13:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132741">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QTTRhfiOvRnP9ZRkZ3pPvHQQekuVp3ri_RQfQPkVg7w_by1Lcga4B54-Dw6YcnVR6EPnQre_cfnEIcCh8o4vlcu9Bmd0oh9_V2cMfT0vgml1l9nr3sv0Y71J2jy1uIFzniftK7JTAb_FU5sMoEewDTinpkzS60ayl8THgp9aCIPF03rI2YfIg-RJIWwFawVX46EqmtLx3uTwi2mHrQiz6C3NLMh4c9r137Lvfxsh08yawZdg6nrcC_SvB2QOnXL__ovZ1eGWMppSJtxZRvUPIqtsyBWans2eYbHJ6R6bFpE9TNEmr_QxjhIw7VqkW7dBPFfRUF0b8vo1DTAl6pJ1nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
دسترسی سریع و مستقیم به وینکوبت
🟢
فرآیند ورود به سایت به شکلی طراحی شده که کاربران بدون درگیر شدن با لینک‌های متعدد یا مسیرهای غیرضروری، مستقیماً وارد محیط اصلی سایت شوند.
📌
این دسترسی از طریق ربات رسمی انجام می‌شود:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
🟢
به جای روش‌های قدیمی ورود، این ساختار یک مسیر واحد و ثابت ارائه می‌دهد که همیشه قابل استفاده است.
-
مزیت روش ورود از طریق ربات:
👇
• حذف جستجوی دستی
• جلوگیری از ورود به لینک‌های اشتباه
• کاهش زمان دسترسی
📌
کانال رسمی وینکوبت:
👇
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SorkhTimes/132741" target="_blank">📅 13:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132739">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YIO2qm2FmEcsfzsXqrTHEYfCPPXSkYL7cc2eZsQI5QiDJIm_jgaNkBjBwWU0f35zpAC0kuYVMHfB--3GEdj-EVGCyZ4MlJz7HVKNSUIQEiDOfZdVMyMFSMVMBeVM93zwTuRmAS659HFsZGAPdaaLrv33_YCJdnZ1Y4BA6k193JiHaJr_6C1VqHK6xXV8cfw5YjYdr4L0B8misP2CEiWVEGYzIe53ustLWmrnUGwp1UarWWe96nFh4lygJdhnsqogzCPSdMhxi844w_qiEcj1rcYlKJTGJGERiOQofNu9rPmEMALpQ_1EP178J4f9wZFFc4ZR03gTRrSd_VxIPdRjpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پست جدید بازگشا مدیر
پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/SorkhTimes/132739" target="_blank">📅 13:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132736">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇷
👋
خداحافظی مهرشاد اسدی از هواداران پرسپولیس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132736" target="_blank">📅 12:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132735">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">⏺
⏺
⏺
یحیی گل محمدی: با حضور گرشاسبی آرامش قلبی پیدا کردم
😐
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132735" target="_blank">📅 12:12 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132734">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فوری
⛔️
‼️
با مخالفت Afc, سپاهان مجوز نگرفت و از آسیا حذف شد
◻️
کنفدراسیون فوتبال آسیا به دلیل اینکه پنجره بارگذاری مدارک  باشگاه سپاهان بسته شده است، مدارک مجوز حرفه ای این تیم را نپذیرفت تا به این ترتیب این تیم از  حضور در لیگ قهرمانان آسیای فصل آینده حرف…</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SorkhTimes/132734" target="_blank">📅 11:55 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132733">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CepLIK1aTzPD_YilG76lvyH6lHpWkVpNFx1lxE2yxXrZADWv9tMStaR79O0Eb1tQg_WBq6NozCxFneEzcN83m46GQneVxQT0LHy714bdiWepQADO68WXjp28tcnbSOdAUY3qy6u98Wr3kIAhjnx24bV7UjEKtj8Kc7c7yx2l4oBPnNiDWp0RsY1CK1C70L2O-EbIzVXfALd8rhax5oHKvBLMI7837nXRJa43HM0BDlSo4sHf4iZNcecy2egTiwKYEktp3SDQ4uVxPKNCln15XhEUUNekjGM17aaypqa-K-2NOIjNrmwgE76hXRpLsKvzt7FG6_MnWpAEgb766eI96g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ریکلمه دیشب تو یه حرکت پشم ریزون پیراهن 9 رئال مادرید با اسم هالند رو به هوادارا نشون داد و اعلام کرد رای بیاره قرارداد هالند رسمی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132733" target="_blank">📅 11:03 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132732">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BqjRdXew1lcHYHdzW3PizIahkwTymMdddlrjDWm663Wj5x70vksGG7NgvDKDaYN1YmAIZ0Y3sqJ_NrlW8sAL-wHUAmEqNxIg6ukridOhA-_7weWFROvWTboleEJRP62Xl5NL-mkeXIjdPvAw_nNj75UyfidZZlypi47cx4GSxqJJOUyaomY-ljfY8GVedragJRqXAhXT518RuJl8thsHKbD8X7msFoygCiPASRsVHZH9vypFeKc7qoiTNUUfdAXFeUOAr-Ft3FZaBNED7r5PL4pUFEy2oOrhi4aw7yfsBi-L1Q8s2y88J_SHaDvQTcoMHFBhi-qbPWdFCf5VeBp1XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
ریکلمه دیشب تو یه حرکت پشم ریزون پیراهن 9 رئال مادرید با اسم هالند رو به هوادارا نشون داد و اعلام کرد رای بیاره قرارداد هالند رسمی میشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.95K · <a href="https://t.me/SorkhTimes/132732" target="_blank">📅 11:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132731">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0583b73b4c.mp4?token=s_k2k9u7DrYhulvhwFWO22Fg1i-xz5h8P6SnKjANH9Lm56uutTT2Hpc0ALgFpqLA10q2vKaeyY7j0di1eug66nV0FvPWISg4u-iIwY-7x7c1J-_piOEcr5rNgjChSlNV_iA6M22WdYlZCcS_wTojrg5v9gWf1njGUInJtjg4ZpNRY6G5-UAfiXGukEIoHO9gGS26EUn1Ee_aM9SiL7vnztO2jqIaTef2gccv7WNxJI5AiKMi8pW_XQ7IGMYDZ9D-TJEkaD99CLOf3SM71O5u4h6UMIZaC1bvjBVLenqWbihjiPqBpcM0GTw52Irr29FzYCyF6buKuwo5Pcr3Hy97RQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0583b73b4c.mp4?token=s_k2k9u7DrYhulvhwFWO22Fg1i-xz5h8P6SnKjANH9Lm56uutTT2Hpc0ALgFpqLA10q2vKaeyY7j0di1eug66nV0FvPWISg4u-iIwY-7x7c1J-_piOEcr5rNgjChSlNV_iA6M22WdYlZCcS_wTojrg5v9gWf1njGUInJtjg4ZpNRY6G5-UAfiXGukEIoHO9gGS26EUn1Ee_aM9SiL7vnztO2jqIaTef2gccv7WNxJI5AiKMi8pW_XQ7IGMYDZ9D-TJEkaD99CLOf3SM71O5u4h6UMIZaC1bvjBVLenqWbihjiPqBpcM0GTw52Irr29FzYCyF6buKuwo5Pcr3Hy97RQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
فووووووووووووری
⚪️
فلورنتینو پرز رسما از ژوزه مورینیو به عنوان سرمربی آینده رئال رونمایی کرد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/SorkhTimes/132731" target="_blank">📅 11:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132730">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">✅
ترامپ همین الان
🔴
خود مذاکرات خوب پیش میره اما ممکنه انجام نشه اما اگر بخواد توافقات انجام بشه باید تا آخر هفته انجام بشه ؛ ما نیروهامون همه آماده هستند و بیشتر هم شدن و راحت میتونیم چند هفته دوباره وارد بیشیم و کلا کار رو تموم کنیم اما توافقات انجام بشه…</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/SorkhTimes/132730" target="_blank">📅 10:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132729">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vs6Ui54_SC_P9tF7b8Z5WwnjXKQiGJQ5Q4IjaUUqbAz4zI26Wghr9rmiu_dYBS113kEQVNwxdbUfF_fYFIj4kqUOTyra4Dx314sy6i163IbDgthxOw2v5RLbLoUE6Y-a_lJDYQBwG6vj149I_pRIRb8c5pnFKrZqeLS9t1BlQUYnkSIZUixbzOCi0LwUtIRnTCPmmrZXPjZqn01w7zlt00aRPfh2RSyjq4npy_i-iSffdVQjtpmI4EoITixTsf5QmHfUS9dIM3liSo3AjVfWRbGJ9g5RbN5ba0ue6VmczQesC8DWUA1aT23PFqV3Q-vosJEgEJ3zxh7UK3_J6F9gWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دلارزاده با ارزش‌ ۱۰۰ هزار دلاری، جزء کم‌ارزش‌ترین بازیکنان جام جهانی لقب گرفت
😂
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/SorkhTimes/132729" target="_blank">📅 10:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132728">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAlkrBNHOmw-otsrbXkPjT7GyDwJu6Lr1Tz7KjB9lypHvchZgwLBzH5NcpMoG3Rq_F5xNtR90tH62_y8x73fXhqal5mS3t8s1VxitGhs1QsqerbyFiMscqdqvgeD5HsVH19eIM3coitYAM2xle6Zbb074KthQAnznDzjewECTcEI4bFRmxRj7PuJf3vwZlt6mHesbk53mtkzZ3xObmErtnne3WG5KSDvFxqdwgholp0q7Z5rEQB9ByhsuTOSPpvv9HXdvzgacHO_No2-6hyN6d-nA6sDJ3yTVmtuaXFDPD6rp5tiy5s3ahUMj60VAw17c8Nv41WJH0fLrTzt7s45FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🤍
مهدی طارمی:
⚪️
اتفاقات تلخی رخ داده که همه دنیا از آن آگاه هست، اما کاری که از دست ما برمیاد اینه که با بازی‌هامون لبخند رو به مردم هدیه بدیم. ورزش از سیاست جداست. ما در ورزش نشون می‌دیم مردمی صلح‌طلب و محترم هستیم و نه اون تصویری که از ما در جهان نشون داده می‌شه.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SorkhTimes/132728" target="_blank">📅 10:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132727">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔴
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
◻️
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
◻️
ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.…</div>
<div class="tg-footer">👁️ 3.94K · <a href="https://t.me/SorkhTimes/132727" target="_blank">📅 10:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132726">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jf9zSgwc3ygow20P6aMMeUZFSfLr_lb6it-gz6UYBkhv85KN6nKMe89tUVUGaFmtZLbkTqlVi4C5CyI150YWC8ExwO0Jc_repRf0kFcsLO0CX6G22oQgVUSvDo0Tcua_jDulni0NFjo72C6J-bX8Zyu3zY2Yhh1axu4P7vAG6ZqLLg2WiY2XUNOofu_Y1yzxlSX0ad3KMg-QYlg1bVD9k4V82OPuBrbcjhat9RQ5GzD2oz_4iMaKEy9FnXEMbnn6dO9ak_0yqh98tDVfdKI0_b7G8GvdbS99ZzPFVnCeNyMtfouCB-1nck0CmS_IrhokrLKwarZ72dbJlscsG_nAdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی دایی: هیچ قدرتی توان شکستن تمدن ۲۵۰۰ ساله ایران را ندارد
◻️
هرگز قدرتی نتوانسته و نخواهد توانست تمدن و فرهنگ ۲۵۰۰ ساله ایران باستان را که در قلب و جان یکایک ماست در هم بشکند.
◻️
ایران زمین، روزگارها دیده است آنچه سرافراز می‌ماند همیشه تا ابد وطن است.
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SorkhTimes/132726" target="_blank">📅 10:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132724">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=K02dRjZDwV4t3zYQlE9PwRAIkDkbsOka2NDRIx-FfI0IfwZMOehdKDPNZefTci4s6u2t3wQq1V7BTtD4heWdiEP2lTBVndyOwZcYcGNM1SShap5CdPzuoUx3_TLaJTR7QanOkSeRRrVEaJrZ9ANPWigLx1PRkyI3j6IJ54LE_AEJ7QbhFwsRKCQApFHpeUAXMAt2csfWm4ArGyKt9P5-xYWrm0NGmi7BE9XkWPb3OYrFVQSwq8vuClfkzliIPO39Oyp2EDs_KqVSSfI4TxQYo_HMIGRECp27YEuPUwq7_VB_I80QKP8Rf7eg143Gj0ccP1I2y6nLEXSmdWuVVWcTng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08f4d5075d.mp4?token=K02dRjZDwV4t3zYQlE9PwRAIkDkbsOka2NDRIx-FfI0IfwZMOehdKDPNZefTci4s6u2t3wQq1V7BTtD4heWdiEP2lTBVndyOwZcYcGNM1SShap5CdPzuoUx3_TLaJTR7QanOkSeRRrVEaJrZ9ANPWigLx1PRkyI3j6IJ54LE_AEJ7QbhFwsRKCQApFHpeUAXMAt2csfWm4ArGyKt9P5-xYWrm0NGmi7BE9XkWPb3OYrFVQSwq8vuClfkzliIPO39Oyp2EDs_KqVSSfI4TxQYo_HMIGRECp27YEuPUwq7_VB_I80QKP8Rf7eg143Gj0ccP1I2y6nLEXSmdWuVVWcTng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🕹
گردونه رایگان وینکوبت رو از دست نده!
🎰
هر ۱۲ ساعت یک‌بار شانس خودتان را امتحان کنید و جوایز نقدی متنوع دریافت کنید.
🎁
تا سقف ۱ میلیون تومان جایزه روزانه
✅
فعال برای تمامی کاربران
📌
برای شرکت در گردونه شانس، وارد ربات وینکوبت شوید:
👇
🤖
@Wincobet_bot
🤖
@Wincobet_bot
📌
کانال رسمی وینکوبت:
🔵
@Wincobetofficial</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SorkhTimes/132724" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132723">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">❌
اوسمار ویرا :
◀️
با 40 روز تمرین پرسپولیس را مدعی قهرمانی می‌کنم.
✅
اوسمار ویرا سرمربی برزیلی پرسپولیس همچنان تاکید دارد که در صورت برقراری صلح، به ایران باز می‌گردد و در جمع سرخپوشان باقی خواهد ماند.
✅
ویرا از بابت شکل تمرینات و نحوه آماده سازی بازیکنان…</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/SorkhTimes/132723" target="_blank">📅 01:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132722">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
🚨
ترامپ:
🟢
نیازی به حمله زمینی به ایران نیست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SorkhTimes/132722" target="_blank">📅 00:59 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132721">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">❗️
پاداش ویژه مدیرعامل باشگاه پرسپولیس به امیرحسین محمودی
🔴
دکتر پیمان حدادی به دلیل درخشش امیرحسین محمودی در اردوی پیش از جام جهانی تیم ملی و راهیابی او به عنوان جوان‌ترین بازیکن، یک پاداش ویژه برای وی در نظر گرفته است. این پاداش پس از بازگشت محمودی از اردو…</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SorkhTimes/132721" target="_blank">📅 00:57 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132720">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjIlQMlU7zM4polo_6bM3sJoxzokHGoHTWjlbQw3RqP2KiE9KbqToAqza5DoS5r67aLf3DjzeC51YUjNSfq2tPU6i9S8MKdfHOY2J-gWeTfxsxz-pvOCnsjYy8HYCnu-OkmXfXwVvQm1Dd7aruZaLRsLRxKBnn9tjc-KBXx5xdbWBKXsOEnjhAkJtNxD_Wk_GjufI8WnN5p0jA3GTYXAFg9medmGEVPvE7QwmKP75paKV6ihIHYYzTtR3vssxsgYun3UyxLEavIN03pMYmWgvBQg3UNF68T225SHzmLtk8qFsLv44lrNFwpDWRLIT578ow46qJXKCENV9jkuKc8YQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قدوسی: باشگاه درحال مذاکره با اوسمار تا وضعیتش برای فصل آینده مشخص بشه
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/SorkhTimes/132720" target="_blank">📅 00:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132719">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔴
طهماسبی، سرپرست هوادار: پرسپولیس مایل به خرید امتیاز هوادار است اما ما تمایلی نداریم
⚪️
خرید امتیاز هوادار توسط پرسپولیس؟ این موضوع به قبل از جنگ برمی‌گردد. پیش از آن، باشگاه پرسپولیس صحبت‌هایی انجام داده بود و جلساتی هم برگزار شد. آن‌ها تمایل زیادی داشتند…</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SorkhTimes/132719" target="_blank">📅 23:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132718">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
🚨
🚨
عصر ایران نوشت: سفارت آمریکا به طارمی،شجاع خلیل زاده و احسان حاج صفی ویزا نداد
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/SorkhTimes/132718" target="_blank">📅 23:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132717">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🔴
تاج: هیچ مشکلی برای صدور ویزا نخواهیم داشت  بخش چهارم صحبت های رییس فدراسیون فوتبال در خصوص شرایط تیم ملی پیش از جام جهانی 2026
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SorkhTimes/132717" target="_blank">📅 22:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132716">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔴
فوری؛ سروش رفیعی از پرسپولیس جدا شد /فارس
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SorkhTimes/132716" target="_blank">📅 22:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-132715">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">❌
یحیی گل‌محمدی به تیم دهوک کردستان پیوست
🎗️
«سرخ تایمز» دریچه ای تازه به اخبار موثق و اختصاصی پرسپولیس
🤩
@SorkhTimes</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/SorkhTimes/132715" target="_blank">📅 22:39 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
