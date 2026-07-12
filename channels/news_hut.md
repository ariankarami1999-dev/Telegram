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
<img src="https://cdn4.telesco.pe/file/tqyPWGgS29dBqWB_cTpsyJeCKGnSmYnqJUY7dm68an3Yvw_gsguum4DbR6seRAcB7lMzB-eAiRQU7PgmyKfPLjo4oExLBH5KPKsFFCmhc-L1PK4-8O99kf4dxtHeTbaM7Px9FJ-RgjybB_7Et_oJsNmzGVaZqhhGn3qLpVWeFjGqfSn4rRTnDy9g_n25Hv1_xI5U_MNWrEnps7wo7QVEyBOu8-jOS6VzKhDpb2zgyKrqmHIksFyJ_1DAnqyYOSMpXPmmVe9GRW1yzbFppZS0nosustvNTnqRLNKJ7aUy0rwaLkZ2fyHWOFcwI_Ju4Lwoa-Bzc862PgU6vuVpPPmQUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 181K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 08:49:22</div>
<hr>

<div class="tg-post" id="msg-67884">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7O7-qLkfYWOHBltPeXc3djqJb35nVjJzjPYJvxVRzFqV85_lr5HvDbirnm4MdlN8IPKFxqQ2iPBJAanOVHNAgGucLeVZbnpA4oFKHRXaMGJ5bWuPU237nSPdMDEO_uT1utycWaZnph5RMQz-zWGHpdJ-MAEG9CbPk64cJIAC7AAhd1vO-n5Dm3eafE-sU-v_Tu4dKb7Vjv_DmMyoN86TK9ePKPYWy2lHCQ-c4uwvFKzJJIg_9l9zAkpw_Fp6hleY-SUSRImppCotZVm_qAiaDX3J5RA-H6esKu4zmqTAbkz9SGLTKHxXHE-vZxJUfmemkmwFQzz5_FLDi7ExgXXRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
قاليباف: دوران معاملات یک‌طرفه به پایان رسیده است. به شما گفته‌ایم: به قول خود پایبند باشید، یا عواقب آن را بپذیرید. واقعیت در حال نزدیک شدن است.
@News_Hut</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/news_hut/67884" target="_blank">📅 07:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67883">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2431b44fb2.mp4?token=QFdu2H_R4Nk7otBKyVUIVgzkNfwPi-TSAniY273mIgOm8_Zgx1ocb8kwHCcx1_czbFAUjkXFenCneJIIa0tK6wP3jKzgtA2SGPrBUY8G3XGsR0D6A0XDoUfpOg4-X28Ispd3GJ3h5QaXGNQ7bNIy4hEwKsH1F2wvXzYzm7GkFYvVDdcDAIlVzF9MquaqKTxltohP8hBt_uAE4sng-Efc7wF_P-yDlZiTOxjwfjiEBXCl5sk9kyhB-bDLwWzf79z3gP7K1wBiBuuucdeidjiWovprrmueJIhKTJyy3oUZUwAYy6LeRTHOxz2BenXTOobp9K2A6T2kPJ6dYe_2e4BpEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
ادامه حملات سپاه به کشور قطر
@News_Hut</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/news_hut/67883" target="_blank">📅 07:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67882">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
سپاه مدعی شد: مراکز لجستیکی که به کشتی‌ها و سکوهای سوخت‌رسانی متعلق به ایالات متحده در بندر الدقم در عمان خدمات‌رسانی می‌کردند، در یک حمله شدید و غافلگیرانه منهدم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67882" target="_blank">📅 07:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67880">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ebf6f7e78.mp4?token=Vwwq4dwz5DdAgQX8ZLqKwRW12bRWxviA2T_ZVLQBA1Hh94H3qAbFH81uULOvmUHElafW_rD_zcu2KVmLQJZzggZA6sfSbTGZqMm1f4QN2VUY25L1QYA4DepYUC3IDHlbuvmZjARiikXx4KUG2V40QzQMOYT3_YqdJ0SAjMc0Y1MFo4H9Ph6ZcmC3HuKhD5r33rb7NuP0_MvlDBK2kD78Q_dJ45cbXWb_UqjERSzYCJ83ipb3D3iPe1IVwwTry2Xpn0gwlv3DCnJ5M4H8e54pReTY0odfnPhsR5fdU-8-mBw_B-EqknLhnrZUayJ4LVCLtlNz0DuTRJ4cT-oyt4UIEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
⭕️
تقابل سامانه پاتریوت در قطر با موشک‌های شلیک شده سپاه پاسداران جمهوری اسلامی
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/67880" target="_blank">📅 07:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67879">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سوپرگل تماشایی خولیان آلوارز مقابل سوئیس</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/news_hut/67879" target="_blank">📅 07:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67878">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">🚨
🚨
🚨
سپاه پاسداران مدعی شلیک و نابود کردن یک کشتی تجاری دیگر در آب‌های خلیج‌فارس شد
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67878" target="_blank">📅 07:11 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67877">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67877" target="_blank">📅 06:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67876">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5ceab82eb0.mp4?token=nSh6pJBIsNlLSwlVbFeE5FLzqWz628rCtUt8BEFD78wohB1UGmK3TCVjG86QJeHyX30FenPgRylxE3lCffJdLe6ocnci2pA1DRaRkfNnzlHpX6jZ9L0gmdqQI9XLN3z9VlA5veynnpSG2JOFVMpA8zxIYpyyp4aWfHLMRyvu1yDGgzsJdlm30kZ2ia9I2wLDPzrP_8zNLXuEAfoOvzfmLK3WGEaChIeftzH0HTFCY51v7TTSacZLBwQblq1FuzzjTL1lBk4oDwShpTZNv33DC-DCedPWwgBYM4Lt_lcUch_LkOAO-aCKNB2nSco9Pm6qYmsJ4V7whqbjV9W-bpUACQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات سپاه به بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67876" target="_blank">📅 06:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67875">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app (7).apk</div>
  <div class="tg-doc-extra">53.1 MB</div>
</div>
<a href="https://t.me/news_hut/67875" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">1میلیون شارژ کن 1.200 میلیون تحویل بگیر با پشتیبانی آنلاین ۲۴ ساعته
😍
🔵
برداشت آنی
👌🏼
⚽️
تنها سایت مورد
#
تایید
ما
✅
اپ اختصاصی با
دسترسی راحت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/67875" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67874">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2hsyane3XEPNEsG2LlSqlWJmRsZwTNbo-yE4CcFWZJ9MbA39BxPIMZvQqwsq9Vrl6QxC-FRK_8u8d8XM_DF-c8YyTFD5pivHBIq0aPXw36xsK_uYblI4BnyN8zqkXvQb8Zd9pv2Dn7UTlCWZiIEfj6EFDqOMh7kZLcBh7hmKu34mkeqPBBF-Ui691u0iiY57yMAM773n91kynupOYwlcjelYSRJi89qiQ2xHdiaXza5dWpblv5ygXUH_d8uvCvp3XgJf1LWkx8sz9qxnwj5MiEGzT9mfwOLuVJEKPFEjVA0ZtOo3GzdFYJgfbIbWDJk4GoXE5VyECuLcdDcadLfxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
تنها سایتی که توی جام جهانی هوای مردم‌ رو‌داشته تا باخت سنگین ندن
⛔
📣
خودم بدون نگرانی از باخت شرط میبندم با کمترین استرس
🛍
از این لحظه 20% شارژ اضافی همیشگی یعنی به ازای هر 1,000,000 تومان واریز بهتون 1,200,000 تومان بدون قیدو شرط میده
💰
🤩
🤩
درصد هم برگشت وجه در  صورت باخت،دیگه چی میخوای؟!
🌐
betinja.bet
🌐
betinja.bet
کانال هدایا
a20
@betinjabet</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/67874" target="_blank">📅 06:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67873">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JaRDi0U6p-B7CoKTA_bF7zuxt6Z4v9jX4c6NnYmmDQovnGge-v5KKdCZxn2MLGmgJTL72FlUhWM6GArfK-FVFCqcbxYf4zLjdWZ6nkm4Ww597s_s1vqbAnlz_aamZXCweWfvKR0gLRAbzY8Wwe3cKV5Z4uX3ozTrcItyqCCp7y5jE0C6Dzq_gAtqquAl3KOw2urdxvZZOPQJ8lWFJFAwGJgmUe-8bFRTBAgpLz60e34OnE9eb-rq4eMAWryUx-4wN7G6datWoCb22Y4dp7hZNB7tAQF1kfsi4F7IM0CthK6eNOoanMoS7pLfrVvpV0cBQljSChhtSJ5HzpuQrPMmyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/news_hut/67873" target="_blank">📅 04:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67872">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو: تو جام جهانی طرفدار آرژانتیم،</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67872" target="_blank">📅 04:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67871">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپمپ بنزین</strong></div>
<div class="tg-text">ما که منتظریم اقا
❤️</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67871" target="_blank">📅 03:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67870">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67870" target="_blank">📅 03:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67869">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
🚨
🚨
انفجار شدید بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67869" target="_blank">📅 03:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67868">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
هرگونه خبری مبنی به حمله به تهران یا فعال شدن پدافند تهران کاملا فیکه
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67868" target="_blank">📅 03:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67867">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گروهمونو که دارین؟
😴
https://t.me/+5NElXlQWt_05OTlk</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67867" target="_blank">📅 03:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67866">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=G1-bSYBBgRiJRmXLv4TZkQyM6ufL7lO5z_1M5Zvonf99hshwCgZrcJiiy_J1Yo57zD7L_QDNoVU0TYiBTfWOEOORyo0dC9CDEucKbSh4-yyt1EwpJ6BZvQPlUF8NswcX2E7_CBwYpDY_2KeNpdK4wpYn6VYDC_jsP6YJr9J_EUQDNwu_lkcVq02gQnVyS4n4vQIVI-lVn3gJmEXqetjIY_lGPP_PrWzDatoCqjgwjrf6Pg0UcxJlJpj8H7Hs9cbx8xwe3fxGiZA27xateFOqfkGdUV6jParmuPG8CQAK3N0PwxeNwS5MuY8jOHVpalmbthvBar1fC8Y27vQYrsb_xQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff21f4d079.mp4?token=G1-bSYBBgRiJRmXLv4TZkQyM6ufL7lO5z_1M5Zvonf99hshwCgZrcJiiy_J1Yo57zD7L_QDNoVU0TYiBTfWOEOORyo0dC9CDEucKbSh4-yyt1EwpJ6BZvQPlUF8NswcX2E7_CBwYpDY_2KeNpdK4wpYn6VYDC_jsP6YJr9J_EUQDNwu_lkcVq02gQnVyS4n4vQIVI-lVn3gJmEXqetjIY_lGPP_PrWzDatoCqjgwjrf6Pg0UcxJlJpj8H7Hs9cbx8xwe3fxGiZA27xateFOqfkGdUV6jParmuPG8CQAK3N0PwxeNwS5MuY8jOHVpalmbthvBar1fC8Y27vQYrsb_xQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی  جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67866" target="_blank">📅 03:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67865">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRazis</strong></div>
<div class="tg-text">داداش نمیدونم صدات به جایی بند هست نمیدونم چی
جونه مادرت یکاری کن امتحانا تعویق بخوره</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67865" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67864">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فکت:
شما چند ساعت دیگه می‌رید امتحان بدین ولی من زیر باد کولر می‌خوابم
😎
#hjAly‌</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67864" target="_blank">📅 03:42 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67863">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝑨𝒕𝒆𝒏𝒂</strong></div>
<div class="tg-text">آخرین باری که کل کشور باهم دینی خوندیم رئیس جمهور مملکتو خرس خورد
امسالم که اینجوری شد
فکرکنم سال دیگه انقلاب شه
😂</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67863" target="_blank">📅 03:41 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67862">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PueNhj8zoMxnwHoe0W-yoC-yeVLaoouk8dGPz_XJ77IfnKDIVbmIWnAIrYH-6H3vgzNFwNPRfc8Ro-KJrL5ZP_lYdXL_deydUyVoUiWM83Ea8ssssDA9dVkZ2CfLnz_4ozTbSab9czO_mMzobCIzHscTJ-uPpLssGA3_f0POaDLD75AGy3_e6IoRogwIdN54QYu03xvnTErNtLZFLNXKW9eE1N-dIxjIfw2KA0KeASuJoBgmX3_ax9D9GzE-spOBQQ9BuC_aKYbSlCEJGtj68ZyDNFk49Iml1ePVKVA5y2omZ7F6u4ZLskwMYVE0kYnkfF9xLANgMOuMEPGWn5XDFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منطقیش اینه به تعویق بیفته حداقلِ حداقل تو جنوب کشور، ولی اینطور کل سیستم امتحانات نهایی بهم می‌ریزه و باید بخش هاییش داخلی بشه، و البته با این مسئولایی که ما داریم چنین چیزی بعیده #hjAly‌</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67862" target="_blank">📅 03:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67861">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djTwWRD__Dr-IqmPrrIX-OMWNtNZDvMdkLekNYjmVWE-w4UwdNQMadSkEq4lGKbbc8KTEjCbWJtc85ZrXpcubhhe2JvLYiP_aoJsASbebr2cROFBdPviduxXwUCmZzuwe9mCyiMu42t5BH4Fbk1Hmr95K8SLBtFgpE_dz7V8RZS7Hqxdvlj2_KYYEsTTnhWZ_SAp3rwVu5tJWyDMm88BtRqegaCVhlxvVVyMHrh_JIf4mEuhI3N0xAIsjYMGa_i2n0iBEUQ5FshKidDxNtUrWI3jr0p2kllYg_w6al09GJet1QYk5gIujY41i49S7llM7D9e06L-SFCfhXWinG4YYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه #hjAly‌</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67861" target="_blank">📅 03:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67860">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqy5Lr1NW54vHjtHNx-1N2xkBw6-42DJWR8QCCXioz7SabYHVEnBAFsxcqQwjJIAUy0yopUDRe1LHMgrWuvHdk1MigDGF6jzDoLTofhzMTLR4u4wmMGYcrEfgzOBNMiJQ3-LEN2vEjXQxYUOW0VDacqCg8wyF6fxjrz9gtSVrzlrHbMoLXES8Y41Hs8XjfKVMNWVKqWHFAA_jofuAoEBr5K9sFUJxikJtGPpASqCcfeVpNcO-Rr75hCt9ViyT0MftZQ6-KAJ8N8bMfUOZxqWGnejXHfD6ApyLGT1wsCk3ZNc3NF8ajNA14i1gYU8ISGRdlr-POsqP242nDide3xEJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
کنارک
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/67860" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67859">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO_S966yIdDbiRiupYKJbvCiXOwu7bvYDhdG_4lIIlrnr4ZVAtNhxaa67CimuMTYvDkDzqESmET-b3BhwOXOpWEuUtr-KXku6tBfyY78Ec4RZ3-XmXaFnPX2GS4C9_T7TbaLr2Ccu3zEERL-RJQHypSqb8p3Z6-YwFXVaGTPVTrf49Ww1fLqF1iX5mqh4s3d-eREwSoCII8zCVOhZQaRe5skjIndEUGp6Vtz9Az-TGEUo9f9AwHgS3lNpUvtcTZsOGrE7MZTabXxoOhB8gOV2AKHDyUWmzx4zgDCKZcLSZuITaKiBJeTDNmRv8aG7LF6o00B6NGs4boG_RSHT36lFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:  ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.  @News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67859" target="_blank">📅 03:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67858">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🚨
نایا:
دو انفجاری که در جزیره قشم شنیده شد، نتیجه درگیری‌هایی در آب‌های خلیج فارس بود.
نیروی دریایی سپاه پاسداران انقلاب اسلامی و ارتش ایران با ناوهای جنگی آمریکایی درگیر شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/67858" target="_blank">📅 03:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67857">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🚨
🚨
دو انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/67857" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67856">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=JnHGkkhwMtnbaHDU8rtS8Dw2950svNx4Wk_jJgBdnI3on4Dmojzrc594s-2DqG60tggtUGiaK38fuFYtfe4W7S_AYjHKviZtQAJ7WnKN7ebgvOCmqEx5NVefn4MQ1pNIiWNXmeolqPqbs54sBRzpMrhmQ0M7pfWhPJIzT7_YznQHC--g7TSYuFg5T1trV_4o1ECx5rWL29IAyPStndyn4UUvGVGlhzpI1aIHY3fu9zPEku-KZRSAaG9L-Sx5UFymuHknXFu1r8OalnqYRLFBQsQ6S91fxm2FyovEHKgKJNkpJ15u_ilQG1VE5fTVTr4kjqIenUt4j67daWu_7qDQaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfacedd54.mp4?token=JnHGkkhwMtnbaHDU8rtS8Dw2950svNx4Wk_jJgBdnI3on4Dmojzrc594s-2DqG60tggtUGiaK38fuFYtfe4W7S_AYjHKviZtQAJ7WnKN7ebgvOCmqEx5NVefn4MQ1pNIiWNXmeolqPqbs54sBRzpMrhmQ0M7pfWhPJIzT7_YznQHC--g7TSYuFg5T1trV_4o1ECx5rWL29IAyPStndyn4UUvGVGlhzpI1aIHY3fu9zPEku-KZRSAaG9L-Sx5UFymuHknXFu1r8OalnqYRLFBQsQ6S91fxm2FyovEHKgKJNkpJ15u_ilQG1VE5fTVTr4kjqIenUt4j67daWu_7qDQaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
فارس:
گزارش زندۀ خبرنگار صداوسیما از آخرین جزئیات حمله به جنوب ایران
تا این لحظه سه انفجار در بندرعباس، و سه انفجار در سیریک تأیید شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/67856" target="_blank">📅 03:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67855">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
خبرنگار صدا و سیما در عسلویه: صدای ۴ انفجار در این منطقه شنیده شد
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67855" target="_blank">📅 03:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67854">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🚨
چابهار رو زدن
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67854" target="_blank">📅 03:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67853">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
❌
شنیده شدن صدای انفجار در قشم
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67853" target="_blank">📅 03:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67852">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9l40-2_y1nYwp1_QYCcH2-kFIO1f2BSm79J8P8luk96OH2AJ-pevxT8EQWw4MwJcJ1GcFRQcrm1qTGrL2xXgsS61N8hbvullUCe3Zo4pGMf7b5G1zHjcu5C5TJO4AYzZXc4YrUeJM8XQtcJ5AhUvEZLTi0Hvo3m7TEW-o8qfUR-HSMEzi0yBFfW_5lVIhimP3QqET3tfPguqlSoXcEyw115aTcaQzbEvHgaF6a7DRTDuyprcOvi2r6pAljuYBD4VUsMpZBL4NCGLVj49Jb1DKXKQ3qm4TNISI0UxIYPIdGIrYcg6_Bw-P1Fp6uSP-OHUDg8UzOsJUb0yADbCj4xMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزیر جنگ پیت هگست:
ایران انتخاب ضعیفی داشت. حالا پرداخت می کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67852" target="_blank">📅 03:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67851">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=UKlPdRNo861gdhH9Ad2Kw3skH-0_2edL85KgqC1hwc70xN6VGeeG6X93Kjya3qByYOCtUsnHD8P5UFMv7M77lFel-E2G22HH1y7f1heIpJ43MxRO_gL7zCphCDPcRC7oQ837bvfMgD9Kec7MChUYDuMhn7NgUiW__jp4pYb72fUILYAkaPd44wGgKvHXZHL3TA7lTjwjYQIkY_U4mguZO9oWnv_TDT2M7jvvsIu4KfiyqZIWc2_SyswFPjJUbeO9hLjSJErfNHzPyDtlCSHjpE78nREtBaxJAtjkpslT_3sUdHxJxH65qH1fSINAlQfMOOVzr9DY6hM5OgAbtPe2ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ed7140b74.mp4?token=UKlPdRNo861gdhH9Ad2Kw3skH-0_2edL85KgqC1hwc70xN6VGeeG6X93Kjya3qByYOCtUsnHD8P5UFMv7M77lFel-E2G22HH1y7f1heIpJ43MxRO_gL7zCphCDPcRC7oQ837bvfMgD9Kec7MChUYDuMhn7NgUiW__jp4pYb72fUILYAkaPd44wGgKvHXZHL3TA7lTjwjYQIkY_U4mguZO9oWnv_TDT2M7jvvsIu4KfiyqZIWc2_SyswFPjJUbeO9hLjSJErfNHzPyDtlCSHjpE78nREtBaxJAtjkpslT_3sUdHxJxH65qH1fSINAlQfMOOVzr9DY6hM5OgAbtPe2ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
شلیک موشک های آمریکایی از بحرین
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67851" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67850">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام):
ساعت 7:15 بعد از ظهر امروز پس از اینکه نیروهای سپاه پاسداران انقلاب اسلامی به یک کشتی کانتینری با پرچم قبرس که از تنگه هرمز عبور می کرد، M/V GFS Galaxy که در حال عبور از تنگه هرمز بود، به طور آشکار، نیروهای فرماندهی مرکزی ایالات متحده، سومین دور حملات خود را علیه ایران آغاز کردند. یکی از خدمه غیرنظامی ناپدید شده است و کشتی به دلیل آتش سوزی داخل کشتی و خسارت قابل توجه موتورخانه قادر به ادامه سفر نیست.
ایران فرصت دیگری برای نشان دادن پایبندی به یادداشت تفاهم پس از پاسخگویی به حملات قبلی به کشتی‌های تجاری در اختیار داشت، اما باز هم شکست خورد.
در پاسخ، ایالات متحده هزینه سنگینی را با ادامه کاهش توانایی ایران برای حمله به کشتی‌های دریایی غیرنظامی و کشتی‌های تجاری که آزادانه از تنگه عبور می‌کنند، تحمیل می‌کند. این حملات به دستور فرمانده کل قوا انجام می شود.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67850" target="_blank">📅 03:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67849">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=hbze7NT9gZ2jNZPs2qgbFQazIUgPghANlrbYxPUewXWh-JSscbwvpyMSEbL7o6ym5ZpaatLY3APv_SW9h__tRJ1ijl0CSZGK7xYLtW5hqKKatq20NXvWO1rOWW9XQuWjMpbcTdLzHlIoXnjq60QI-QNKu5hG7bUghN0N9jg_A23kZUSZPfX8DezhrW9KV0U6b5Nn2buccJz_hVUpU3DEu5W3-NM5JGlrLuNuhsVEglm1PhFzVt0-56fgFrkMa1BW0QyPT_Kh1X7GA5SbtJrrJMkqjzTXq3Gxaq5X8Zb1BNMkLZe7LJHrU6sUchx0jNkFtLPupDE119Qw08TVbMauww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c16f69bf83.mp4?token=hbze7NT9gZ2jNZPs2qgbFQazIUgPghANlrbYxPUewXWh-JSscbwvpyMSEbL7o6ym5ZpaatLY3APv_SW9h__tRJ1ijl0CSZGK7xYLtW5hqKKatq20NXvWO1rOWW9XQuWjMpbcTdLzHlIoXnjq60QI-QNKu5hG7bUghN0N9jg_A23kZUSZPfX8DezhrW9KV0U6b5Nn2buccJz_hVUpU3DEu5W3-NM5JGlrLuNuhsVEglm1PhFzVt0-56fgFrkMa1BW0QyPT_Kh1X7GA5SbtJrrJMkqjzTXq3Gxaq5X8Zb1BNMkLZe7LJHrU6sUchx0jNkFtLPupDE119Qw08TVbMauww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/67849" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67848">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇺🇸
🇮🇷
باراک راوید به نقل از یک مقام ارشد آمریکایی:
ارتش آمریکا در پاسخ به شلیک سپاه به سمت یک کشتی تجاری، چند هدف ایرانی در منطقه تنگه هرمز رو هدف حمله قرار داده .
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/67848" target="_blank">📅 03:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67847">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
🚨
انفجار در بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67847" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67846">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🚨
🚨
حملات آمریکا به سیریک هرمزگان
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67846" target="_blank">📅 03:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67845">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
بوشهر رو بد زدن
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/67845" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67844">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🚨
چند انفجار در اهواز و بندرعباس
@News_Hut</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/news_hut/67844" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67843">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.  @News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67843" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67842">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=oX53L49BjNkuJXYCIDaRuFekIRZCFKe5dyuJUCXzKJ-bgTkffRBXocdQpHNPX3lQ1jWiIfKKF0uneUqkioA7cnnUEaB_T6Ymo7Ki_qilPYsOvqYhFnRb4hWD8b47IFrJC5vN8SWqQpvO6G0guFwuh5-1oEQeGcpV7N0TEjSnCm-0sqm7q2k6zXxvOsX2wK1xFiK0t3zTZJD_g3_XQdqcDh67i5TB0hf9Tyn12chlCziwLisBKNH4BI6_ntpVwJAzqtRTfhVJvO0e4X77yzY1tFS3sA7LFd4Wj-53T6r-JWukKQiE_K-hBZVfH9EOlSM5X3MaRyioGXrXCkrD9smbI0WWS0ejOjQH0OxaxjN2sD556wNc7XIlyjKXe9p8Kn2S1ndTFBYs6fgW8yKwbb4x6u52z78eZQNtxkgkqDxubL3HgIkacLPSOmV1H_YmROKFbi4x60olk1fFP_bsIEndBWbjTRtbKVYR0SEDNWY8WuE6Zr_HdX8YrOuvruf_y_LIa8jP02JGU2D1K2DPCwPb8UgLDZ7YqLgS5iFpViIsvWoheoVUsQfuOe5oTXZYuQ1jTbcpBiEdGcXGdqilOVOJ40fSD87S9xBys5847Uy0vM_pMtoewO7vOCBFxnCfjKB8b8EXEsbOJfhZJw5yYWV6PsmMnXgmyDN2nGM4u1caLgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=oX53L49BjNkuJXYCIDaRuFekIRZCFKe5dyuJUCXzKJ-bgTkffRBXocdQpHNPX3lQ1jWiIfKKF0uneUqkioA7cnnUEaB_T6Ymo7Ki_qilPYsOvqYhFnRb4hWD8b47IFrJC5vN8SWqQpvO6G0guFwuh5-1oEQeGcpV7N0TEjSnCm-0sqm7q2k6zXxvOsX2wK1xFiK0t3zTZJD_g3_XQdqcDh67i5TB0hf9Tyn12chlCziwLisBKNH4BI6_ntpVwJAzqtRTfhVJvO0e4X77yzY1tFS3sA7LFd4Wj-53T6r-JWukKQiE_K-hBZVfH9EOlSM5X3MaRyioGXrXCkrD9smbI0WWS0ejOjQH0OxaxjN2sD556wNc7XIlyjKXe9p8Kn2S1ndTFBYs6fgW8yKwbb4x6u52z78eZQNtxkgkqDxubL3HgIkacLPSOmV1H_YmROKFbi4x60olk1fFP_bsIEndBWbjTRtbKVYR0SEDNWY8WuE6Zr_HdX8YrOuvruf_y_LIa8jP02JGU2D1K2DPCwPb8UgLDZ7YqLgS5iFpViIsvWoheoVUsQfuOe5oTXZYuQ1jTbcpBiEdGcXGdqilOVOJ40fSD87S9xBys5847Uy0vM_pMtoewO7vOCBFxnCfjKB8b8EXEsbOJfhZJw5yYWV6PsmMnXgmyDN2nGM4u1caLgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تصاویر بیشتری از اقدامات تهاجمی آمریکا که از بحرین آغاز شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/news_hut/67842" target="_blank">📅 03:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67841">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEi6iznbuXtLo36aVp-Pdhu7bkCIaxgAE4F8ehAnV474LwQ_DR62V3ZF55d13nsWY5rWc-vuM1n8SOnUHYTYdyk3Tnuxt-x2H-yXwrPS42-Al4sC8dmiZvYT2DpWH6pmkoX0I7o5dahgirYVVpJGsB0GHJS7oEo1ora-faqI8TvttYLs3TdVjfIXEiZjP7RwnyES5-th4_XajW89tj9b5lwwAfNRK-z-OMlowjVgW3yEY8u92gREN9U4TfhbH1EhXjwoP5gtsuHytKbXMRODucKEHqkzsbBcjAl87TIQDkA3-YDBiBQZAwV5wlL1GEkgWJZln7PBzCII4q7P2WpsRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منتسب به بندر دیر
@News_Hut</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/news_hut/67841" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67840">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
چند انفجار شدید در اهواز
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67840" target="_blank">📅 02:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67839">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:   من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.  @News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67839" target="_blank">📅 02:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67838">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
انفجار های شدید در عسلویه
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67838" target="_blank">📅 02:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67837">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44b4e512f5.mp4?token=EebxJ-yVxdnKyH396roQAzeyw7Bqlza9YurW4fwy6-RvL47pCr3vly14rfRoEoU3laaojPvj4Ceq7znqzvmn_45FjXaWcaJm5oNYDp20O4wAS9y3re0MdKdwXmDhj0pmOb0fbk1cIzBKs-SoMo7LvpgaVkU1RA3IW6CHkrHWdT9D2QSl9axap4oUcN0mdZo5iGg8m9MaQvUTK6uw2FPLOzqGgz5FURjhA8IT8o1wh3sKQSN_p5HfgUlFrlFHJmuXqbr2WRTNNUSYN7mABdGmNa7u1r_5I_oE1kCB-BMtj0HLMa3xbP3jT0C9hFBf3XdmF7MTQRZwHud8XY-f0UfzfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
شلیک موشک از بحرین به سمت اهدافی در جنوب ایران
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67837" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67836">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خسته شدیم از این چص‌حملات خدایی، قشنگ بزنید جاکشا
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/67836" target="_blank">📅 02:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67835">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
ارتش آمریکا رسما حملاتش به ایران رو آغاز کرد
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/67835" target="_blank">📅 02:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67834">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از حمله به بندر دیر و بندر کنگان
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/67834" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67833">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
🚨
🚨
گزارش ها از انفجار در بوشهر
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67833" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67832">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
❌
گزارش‌های اولیه مبنی بر شنیده شدن صدای انفجار در منطقه عسلویه منتشر شده است. منتظر تایید این خبر هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/67832" target="_blank">📅 02:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67831">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=LLQkp6rvU9hM8PhAW5SYegRFFh4vA7Ovpl_bu23DjHxzbhEwIJsDnotlMRZcxeDCH5jfIOP5Jh-EJhznIv4qbS4UQrAI1V5RRQRyX30BghEaVqj5FWGz-sv7X8GZNMDKvu_taMPPpZ07K2Uo0FPSPBO0VEKVgDG3AMqdFrWWzkIqldIaG28NKHBPhzwqVaRZjdHMDdrTr_L2XPR-g3jbNDr0WIsvZd8Fpu3hGtbFq09vJ63IQWwW9g1w0t4EB6zC5re9dCzzZTHdxBAMLaONJJ0WdYVX2obhc7LVSr1wzZ5IkWIwNW-5z91LiPYYMYY3htpgrta4nnq4blnlFY2EFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4398edce9.mp4?token=LLQkp6rvU9hM8PhAW5SYegRFFh4vA7Ovpl_bu23DjHxzbhEwIJsDnotlMRZcxeDCH5jfIOP5Jh-EJhznIv4qbS4UQrAI1V5RRQRyX30BghEaVqj5FWGz-sv7X8GZNMDKvu_taMPPpZ07K2Uo0FPSPBO0VEKVgDG3AMqdFrWWzkIqldIaG28NKHBPhzwqVaRZjdHMDdrTr_L2XPR-g3jbNDr0WIsvZd8Fpu3hGtbFq09vJ63IQWwW9g1w0t4EB6zC5re9dCzzZTHdxBAMLaONJJ0WdYVX2obhc7LVSr1wzZ5IkWIwNW-5z91LiPYYMYY3htpgrta4nnq4blnlFY2EFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
کاتز، وزیر دفاع اسرائیل:
من و نخست وزیر نتانیاهو به ارتش دستور دادیم برای انجام عملیات نظامی مستقل تو خاک ایران آماده بشن.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67831" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67829">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
تابناک:
گزارشات تایید نشده از حضور تکاوران ویژه دریایی سپاه  "S.N.S.F" به صورت تیم های غواص مین ریز  و قایق های تندرو در تنگه هرمز مخابره میشود.
این تکاوران از یگان های نخبه دریایی ایران مستقر در مناطق دریایی سپاه در خلیج فارس هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/67829" target="_blank">📅 02:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67828">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">بابا اونایی که نهایی دارن بخوابید توروخدا، تعوووویق نمیفته نمیفتههه
#hjAly‌</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67828" target="_blank">📅 02:24 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67827">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.  @News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/67827" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67826">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stOnr5Y1BX_VOc5QBKwVDa-uvMLz_9MIxWtu-5ZcLclqabvo14I9-el1EqoXtqOEdDFzoZpeFdVdjF5_W1wSKLQbtBWKNMbzazRX_7A8Mw0NGDz3Ua0DfLVLVMNtahM0ItEh95WorjoSf6XeygOHf8QDozMRNzXdEvq_Y0SY5RDS-l1RFZ6i6QqyhVdTR7-iM74lA_VXxMw-AJDuJEEY7TUFxLnr0O9VlEv_uSpZnd05zxHEHK1glVnUHkOQ0zWqUreU3-6q5Er6wSsu7ZHLdMmYKgo8Agf8Pt7lHnGxluC-vUyraJiJo0wW9T347JoCQCGQkmzrIln_qcr1i78m-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.  @News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67826" target="_blank">📅 02:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67825">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1InL_zxX_6EHUOQ6b4g8CO1EBoW3x0w_0dznK26xlpmoy7JUj3sLB6UWDnAXk_xmaT-U0sth4UfwvJIUKrZ_53R7F4YnEWSUVhbMMDLFnaWZmFJCFyPWAMQKWaa3VJW23mlZzRLYcKchhKrfyT7SipjNA-t4g0WTlv5VO9zKj6w4N5KTAtmjMD6ydzE_eVJSqsHH-kKjE6Ktaa4gOsy5mttog-Ad8FOSRwovdq0EOfgb8ls3eMxY5g1t-7TTudp5uAVpTyDLIIeD8_gWLgLKgDT-yP7rEP4cpKlrVGBj-9BJUS-M3SLh9LxolMieP835DuhYQIJw1I6p2eGxuBpzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
هم اکنون زیرنویس شبکه خبر
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/67825" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67824">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYNkFOYpA8Fcb3FxNINQEVUhBHG8rSu0nr8wzXPIBQfLgfKFedsruHV5Roo5wI3tyF5oIH4tSN14DAw6zUvalaOaU-YWQf9KE1Ig1Ceq2-kQjw2cvHtQmP4os1d_Fd6uyUKj_hxMxt6w4dToP9OKcOnF3Gb0M9HH9nmrUn063dlIrDF1_KHqC9HPSuuwTII6NxuUyg8-HABd7wBgOrnq_hJmg_D5Vt6AjyivGYiMUgbM6zNrucYIiuHrsuLKDIpv4FAkrkEzarzirjhT6qcVZ9bdmPUJ_ksvy-LNLXYAjsYW-yXyIUj52xXaZvgxSd1AuH8o8XtqHhQNQaNu2s7cHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇷
سردار عظمایی فرمانده نیروی دریایی سپاه پاسداران کسی که دستور شلیک موشک به سمت کشتی در تنگه هرمز رو داد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67824" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67823">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇷
صابرین نیوز :
به دستور مقام معظم رهبری، حضرت آیت‌الله خامنه‌ای، مدظله العالی ورود به تنگه هرمز مسدود شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67823" target="_blank">📅 01:54 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67822">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🚨
🚨
🚨
حدود 35 دقیقه پیش یک موشک کروز ضد کشتی از سیریک به سمت تنگه هرمز پرتاب شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/67822" target="_blank">📅 01:52 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67821">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
🚨
🇮🇷
بیانیه سپاه :
همون‌طور که توی بیانیه قبلی گفته بودیم، هرگونه دخالت خارجی و تعیین غیرقانونی مسیر حرکت کشتی‌ها در تنگه هرمز، با واکنش قاطع ما روبه‌رو می‌شه و روند افزایش تردد دریایی در این تنگه رو مختل می‌کنه.
چند ساعت پیش، با وجود این هشدارها، چند کشتی با تحریک طرف‌های خارجی سعی کردن از مسیرهای غیرمجاز عبور کنن و به اخطارها و دستور تغییر مسیر هم توجهی نکردن.
در نتیجه، یکی از این کشتی‌ها که با خاموش کردن سامانه‌های خودش امنیت دریانوردی رو به خطر انداخته بود، هدف تیراندازی هشداردهنده قرار گرفت و متوقف شد.
از این لحظه و با توجه به شرایط امنیتی ایجادشده در پی دخالت‌های غیرقانونی خارجی،
تنگه هرمز تا اطلاع ثانوی بسته می‌شه
و تا زمانی که مداخلات آمریکا در این منطقه ادامه داشته باشه،
هیچ کشتی‌ای اجازه عبور از این تنگه رو نخواهد داشت.
همچنین اگر دشمن متجاوز به بهانه این حادثه، که خودش باعث به وجود اومدنش شده، دوباره دست به حمله بزنه، پاسخ ما قاطع خواهد بود و پایگاه‌های جدید دشمن در منطقه رو هدف قرار میدیم.
کشورهایی هم که اجازه دادن نیروهای آمریکایی و اسرائیلی از خاکشون برای این اقدامات استفاده کنن، مسئول عواقب این دخالت‌ها هستن.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/67821" target="_blank">📅 01:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67820">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🚨
🚨
#فووووری
؛سپاه پاسداران انقلاب اسلامی از مسدود شدن کامل تنگه هرمز خبر داد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67820" target="_blank">📅 01:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67819">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromARAD GROUP |‎ سیگنال آکادمی اراد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3WwLHtfgNUvZR7CH8rQXbEsRStNM2fG-MxSD9FbtY05NJTMGyNXumld0Za-qg05YhqbTTFwNS2W4x0hqiO4AaYCWceWWzUAPluNAktL078q_o5BUxfqPZ6gM0labFQuOrh6sAfE20C1rvURWmOuPMurUUlux3SSGT3Nn_JTmuzPlQfyhR-W4THUOwTMo7hREagzm4wjxMkwMj2jjr3VGrC6v-mc0OfsJ9Uv_dzq4McNNq40fGb3AIksLIcLxKTp2ahYZx6B9dtSjKJkZc8tC-3F__UnuAEVJrDpz2B19qNANu6TQSqfqebCxbihJDlJVdwBsL-XPY9xo6hlIbv35Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
غیرفعال شدن تراست ولت و فریز تتر برای ایرانیان !
بعداجرایی شدن تحریم ها جدید امریکا و بستن حسابای بانکی حال نوبت شناسایی و غیرفعال کردن ولت های ایرانی هست و طبق اعلام مقامات امریکایی ، به گفته انها این کار برای جلوگیری از پولشویی دولت ایران انجام میشود و بیش از ۱ میلیون ولت شناسایی شده است که به زودی مسدود خواهند شد
نکات مهم برای ایمن نگه داشتن دارای های شما تو کانال قرار دادیم حتما رعایت کنید
آموزش رفع مشکل
https://t.me/arrad_group/2450</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67819" target="_blank">📅 01:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67815">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m2G5aJQs4QaiXU8alxvk9Iix16QFXcbj_Ueud_zKejfd6QKzTfNSR3EKfa5hBwK-OHyA6RjG1qzs4koqjzj5LLs3e2U-IzuiYXYpPGErgy6IMGXgzj1fwNpNuh8Cplo9qXKepE9I4eN8BOukm4sE0HXHqyIyjcfBuDUegDbAFRiyDeL-Zst-xGS68XpCdC3iq34VDON7AdOk3w6yBlYfhYmB8I9c85QdTg49qt_M8CC5PMas2k4AvZgeX0ZIqg8TUxvlKVzJZA6MYl1oykzQHUw9gv4N0yDwRqf4upSLcBAga7m_b10FaLcb6Jt3g1rrdUbgYIrLT-WUQtiaVWsNBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JTDRD5hbtc3zNuLXNIQ81luRd2GpWSl1DSC9s6Y4FNT-XotQuaSsOgMfU7KMs_LXzGYeR-DyKZjuBFcHLCxkiEdujQnfMqRkp6C5J_pGIdeUdnWqBHMG06BpmsEi358IUlN40AnN_-V-XtdJVzNSEuFJ8J9cKCbGcccALd3MqhO93gh8X6CA9TGqFgBJs2msd77zIcClOzlII4No8A94QOck-JsFM0ljKl2X3QS2E9Zry3D3K-5kxpLqU6fIGoa7FAfxqnhve9apCbFpMnxnzjzPaw8_WWxPRrsAm_7f5YcRz9ezZ312qkNzeICnTdh2Hlpnaa62ssGUO8PORLfdeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HVKeY4sg-BMnG02YajuWP7rt8xIVunozg9AtxXY9pgo7FXCWSAKtKbCzPM3w5t8I0y5FxFc-mk1YBxAJ6x5ZglCMUw4VKcdkbAZxPomPyVfq7ZHjvIBdRvj3SmaR0tAIuFt2W2PzKONqN_Q9kAgL9wuFYo2CzUAQakLNGTux_ynDvIlDvrHeyIQLmsOaipRrZN8ONk2mVfQSo8sHkvIXfFZLbS2AbKq3TV43ezIAOeZrUQ9frOZiqetl0WHsBkLRoxlhoJ3CWbdmSEoHbD374AtO4HYgkxw-LETie9ZOVmwCkcaLouFppflsdiUbVPixYidyyK7EXeXzRpi0LmKiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YMfapwhErKQLP4ZuV79kj594HvL44AfID_Kh2Db4g0anGBf6Y3JLTM5oO6uKasq1wQUozLIPBsgevV3rkcWnbvtzqqBD2Wh05Ywzl9yfm7jUvmRh1s6HwrrDLk5EFC4rvpGifKpmqx9Zs_XBSxEhD3L0hsbiwf3SQmFAZLD6M8a6kmZ-_EGrBCLRIenIW5PlyVw_ah2B16k0XvYPZlYHrzTCc4w6sqL_iOaf3CECrJdG6eqKzx-ujdAcPaBKaIgrgJcaM7Eac0orJ1GFzzzgVIYzJJm8h4zWSLNwDIR6etpR45wGfr_MXLK_O2Q3SXa5npymA8B8Jj_vR9PoRmdknQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚠️
هواپیماهای باری نظامی آمریکایی از نوع C-17 در سه پایگاه نظامی که توسط ایالات متحده در داخل اردن اداره می‌شوند، فرود آمدند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/67815" target="_blank">📅 00:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67814">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbae51b67.mp4?token=humdFprYduvy1vLGanHwNISfP30MoesgUBcPHAQeyh7JD2Yj_Ay7InJMlmDQohNRmcAynOkPyYaKyjpAIKWkqD3L2Zm2Bf2Thy4_IdYQuc6O24bMVjlh11cezP0Nht3SntdRa1wv4CbDEqRhkVLpvtVZp1ooYznszwQSZQoyBDWkVyuz2bv1G35KOenHrK2prPhPF5NispMJHuDqDV_W7i4hXHwsFtH06x_gVqAleCH3ElrD8NuITNG1_yN1xEHSh5iWkh-AuohvzvtJ6LcWcc5aNmQH2Okn3TbgCszPknTg31wNnqcnq8OlapSF6sCM9FamX7Rtc6xo2kYImVkfQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک پسر هیجده ساله یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
یعنی رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67814" target="_blank">📅 00:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67813">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JTwwQCV3_97xVktyLNW26IMNq9JqI-FofyvrCtrmglRhuGnFav_8C_qUynClfyT0NEct5OsazdmEESCWapcNBzRa7bnVyFo3LKp1X7vr_8GvxOovt_nMwN_Vfl26m0E9wykGbRQ04DWOCYRfmNS3VspuoxJgNNyHO3vo__CcceqLgAHB1abXJNTlAqtc__t7y7kKnn-zDMh-PYW00SASW7-Q8G4gDmxMZ-XAVuvmQZVSxLb4GpR0NdL4hWaPL9-Xc_ObJiBHiB-O9Jt-sTfXRBF7b5acr_k8VFMdu2gfB_pOt9GKJpaxyLqG9OLxmbEIJ0Id95oDFiCn4fsd9zKseQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کانال 14 اسرائیل:
اعلامیهٔ مهلت ۲۴ ساعته دولت ترامپ، که روز جمعه، ۱۰ جولای، صادر شد و از ایران خواسته بود تا حملات در تنگه هرمز را متوقف کند و از آزادی تردد کشتی‌ها در این منطقه اطمینان حاصل کند، در ۳ ساعت آینده به پایان می‌رسد.
این توییت دو ساعت قبل زده شده و تقریبا یک ساعت دیگه مهلت یک روزه ترامپ تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67813" target="_blank">📅 00:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67812">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
🇺🇸
مهلت اعلام‌ شده ترامپ تا پایان روز شنبه به‌وقت شرق آمریکا ادامه داره که میشه حدود ساعت ۷:۳۰ صبح روز یکشنبه به وقت تهران…
تا اون موقع به ایران فرصت داده ترامپ که اعلام بکنه که تنگه هرمز بازه…
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67812" target="_blank">📅 23:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67811">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TSaeq9_lx3B74WbosOjnaZROFUFG3Wd8VwaIK8oY0sgELkMs6mVFQ2D8MVokOal1tv2sv9UaCcrQgHLsVGju3dOR3NfMsL-IO7703kbrih1IrdhBg5Zsf2l4jUeNkARFao8ARMOSSxCeCFl8HPxZ7nCVeMWMHR7nP-p_qMO7oJiWm15txI4DWB4hTmqLwnoaB1cwj9heRHl9JEjxiJHWLOOMo7XBC5SdGdVmIgU7E9bf3KsV8KcmJyi40aMHcm-Dmhj4C8Pemj1DseIBjfaZSm_gPB5fohqMK7XcmILKrJ1ZeMiEs4_r6HGgEeZx8REZL3TffJM5zx-s-lsvKW4I4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پویان مختاری گرداننده‌ی سایت های قمار که خودشو مخالف شاهزاده رضا پهلوی جلوه داده بود و معتقد بود عاشق جمهوری اسلامیه؛
امروز صبح ساعت ۶ با هواپیما به فرودگاه امام تهران اومد؛ که توسط وزارت اطلاعات بازداشت و راهی گونی و منتقل به طویله شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67811" target="_blank">📅 23:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67810">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6SQAYQEacjJIYewbt08DmeYsnXCPconFZFu4DaSj2WxAcuwlKJnwGaHhcRF3p-uhZmR6YNn1CSuL5IzMBNH2pnCAWBqhKhKel9jbLwW4D8Vk5zVsRuYQRQIWZWI4AnhIOfyIJQvKE4Lv3n_rWE9CWfew-Gj_36I2X6UV2SD3vE9eRPDJciU5GDhduyDBCGdkva2l4e7SebSAPr3LKCXBVC4DhRlxxUqPIjz586yyZ9YuFzSP7xQQRKeEESIbgIoK5UzM1S8tn_MqwwMQK2w9J8Qleataxjx3RH17nXSz86_l0yF7iSYKuyJFptSwFwCeXObtVySDBupuOV0RK4pMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
علی قلهکی:
قرار بود سفرِ عراقچی به عمان منجر به صدور بیانیه مشترک درباره مسیرِ شمال و جنوبِ تنگه هرمز گردد و در ادامه نیز «قالیباف» و «ونس» به مذاکره اضافه شوند که با بازگشت عراقچی، گمانه‌زنی‌ها درباره به بُن‌بست رسیدن دیپلماسی در مورد «بند ۵ تفاهم‌نامه»، بیش از همیشه تقویت شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67810" target="_blank">📅 23:08 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67809">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🔴
اکسیوس:
ایران نتوانست در این جلسه، موافقت عمان با این پیشنهاد را جلب کند و مجبور شد این پیشنهاد را برای بحث و بررسی داخلی در تهران مطرح کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67809" target="_blank">📅 22:57 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67808">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHZbzYSGDz8f-9G5srP9cFpHBl0kBs9jVnTeE_Va4wJjyE9FqWS3UVPYiUMUA_VcpRuG8fvPHjbSfXA9xEELec193cseb37jxJyn9fyIAG0LoKPbjzQbtyyna-wv3Q0vTlnILu4-fh1FJZBlQ4MBYZm4K9HWcDGZHVWPCUl9XPzm3LFNqxVjxa1DrgHNJnx1i6KUXerEUcX2sidmTfavHPfewvGf31blWVS3icn5a6S6k_r_aC9WZcAQKfXzPbhLMdXI0AClY8HAvuoLRGSi4USIqRj34RuiEchm7Ksb6hPvoJnB9XR9f_B1oh671onzjjbGsjQwvi-haJVyeKQfUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سی‌ان‌ان:عمان پیش نویسی را برای مدیریت کشتیرانی از طریق تنگه هرمز با استفاده از دو کریدور جداگانه کنترل شده تهیه کرده است.
بر اساس این پیشنهاد که هنوز نهایی نشده است، کریدور جنوبی از طریق آب‌های سرزمینی عمان برای کشتیرانی آزاد در شرایط پیش از جنگ باز می‌ماند.
کشتی‌هایی که از کریدور شمالی از طریق آب‌های سرزمینی ایران استفاده می‌کنند، به تایید قبلی تهران نیاز دارند، اگرچه ایران هزینه‌های ترانزیت را تحت ترتیب پیشنهادی اعمال نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67808" target="_blank">📅 22:39 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67807">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=XggZXsrDY8wCQskmalkT7gh6KDM_yjLH0CbLOOteAUxYkhaXBT_aqVk9jipPeikfIqTrGFBfSCbomGCSjy9yJ62ljB5jk7FdlBN4QbKwaXBct-QGI-Kzx5hytrf9XuqMvPoF6nRWHX-r-JMES_6sAIDkTPEI4Rb11elCLZQZPrXYLIK-lG_DfKfJW1JNmnVFNbH7rrNyUqf6ifhUZF4udaYy8nJxcloTGnbJW8a7JtJeFK6RClBuTYDPHk_dtCKr5J_ITE4BkUGsawpxxI1ZXJpTEhK4mZKO3YKzZ2UQ1sBjlJZGPv63zp3JWUQ54npjE-Z_rcnaelZaoMMBTxkRgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12d2e49f67.mp4?token=XggZXsrDY8wCQskmalkT7gh6KDM_yjLH0CbLOOteAUxYkhaXBT_aqVk9jipPeikfIqTrGFBfSCbomGCSjy9yJ62ljB5jk7FdlBN4QbKwaXBct-QGI-Kzx5hytrf9XuqMvPoF6nRWHX-r-JMES_6sAIDkTPEI4Rb11elCLZQZPrXYLIK-lG_DfKfJW1JNmnVFNbH7rrNyUqf6ifhUZF4udaYy8nJxcloTGnbJW8a7JtJeFK6RClBuTYDPHk_dtCKr5J_ITE4BkUGsawpxxI1ZXJpTEhK4mZKO3YKzZ2UQ1sBjlJZGPv63zp3JWUQ54npjE-Z_rcnaelZaoMMBTxkRgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
سی‌ان‌ان: برای نخستین بار جزئیاتی از حمله موشکی رژیم جمهوری اسلامی به ناو آبراهام لینکلن منتشر شد
.
شبکه سی‌ان‌ان در گزارشی به موضوع شلیک موشک‌های رژیم جمهوری اسلامی به ناو هواپیمابر یو اس اس آبراهام لینکلن پرداخت و جزئیات تازه‌ای از این رخداد را منتشر کرد.
این گزارش در حالی منتشر می‌شود که تنش‌های نظامی میان واشینگتن و تهران همچنان در سطح بالایی قرار دارد و موضوع امنیت ناوگان آمریکا در منطقه بار دیگر مورد توجه رسانه‌های بین‌المللی قرار گرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67807" target="_blank">📅 22:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67806">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
کانال 15 اسرائیلی:
ایالات متحده منتظر پاسخ ایران به درخواست‌هایش مبنی بر توقف حملات به کشتی‌ها در تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67806" target="_blank">📅 21:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67804">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08bce6837f.mp4?token=DfTxbI6w8w7m86O-1VOcNeUUd0NXRMnlAk8Ua-Xvek3YQLLD9_XcFWfp-qT6NLxrZtf_qAdyYNq6Y4_-wHEINPUtJFiaEsHAB3-7RaCuuqZhunpVmdbEYtREd6w5JnwKzOG_ZpJNo_iGksz8f5eHZ_yO2-bb_i4laMj_17fE-SBDbR3trLoK8ygvHg4zREW-OC3yaQm3SoAh3uUz1utZm6FWq6Xs97nxgnpPyhh0XRiaFlIkCBPw0t-NWBmmKsIhvC3yvf2V0BIViC8bnm2w583HIcBizCcJSsYPLet7LsMtKVhThMFTnsm8SoRBNdPkF5bIMAYRtx6HMjlu2E6T5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ارتش دفاعی اسرائیل:تروریست‌های حزب‌الله در حال انتقال موشک‌های ضدتانک در داخل منطقه امنیتی در جنوب لبنان بودند.
این تروریست‌ها موشک‌های ضدتانک را به یک ساختمان در آن منطقه منتقل کردند، که نیروهای دفاعی اسرائیل (IDF) آن را از هوا هدف قرار دادند تا این تهدید را از بین ببرند.
پس از این حمله، انفجارهای ثانویه شناسایی شدند که نشان‌دهنده وجود سلاح در داخل ساختمان بود
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67804" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67803">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e14ad8a91f.mp4?token=qLKniKMiuujJzWRqIcoyi1IhTSj_XJcIIHvVmN19wKB0I7vBM3QfnbcRQlsAOZ4xrkr4qBLxfSxgrVKD_ZFCHQ_3aqMPSMo36bUi2g8bCHjzFqkc1i0sHEVKozHfhWYbW9EKLjm187wlVzLQFIjOhlCQS8LNN9248ohwCDNL3ZPtFpPdyllE0uABtN_KvjTQ7oc6IvENb020LoI87QgqaLtm7LT_VpYrKx9KsPAVB8tZYVAyps8iU006MVQLFZKFPGcBBF4vtEcR-KIz-NQnxW2f9jNVRz6vh0Jc6AMo9TyWmb-n2xDcnv6hm92WX_hwiQJVPAWImGj6aVO3EluKlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که رسانه جبهه پایداری از تغییر موضع ممد سامتینگ نسبت به مذاکره با آمریکا منتشر و وایرال کردن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67803" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67801">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iz47oX4HCwlfkPryYs7n9U5n7J2U5tT5z8Grm_ewaNuF5hMtmAl00JuZl2fxrciAXrnrAxMr_pKAU0psEUwj52obDXIJBFyAZAaloBY0M291PiwLDEHBlD1ym_k7WYaaGttDQwNN9Q11WJSHnGDGnpP3_fchB4LB_Ub0L08AsxZNnyj3MSamSX6FwacP4dNoxxFN58iNLpbaajet-R1cx_GZH-Tthue5ea8V4wzhTqzV_1pxUSXv_LIXrOqN1laRQ3qSxbuAAaNQJ_qXh4ryaSoT2V3xXPvf3iqQJtF6F_lwmk8NIp7QRbg-PcE6_TPCNjeRTGLYMjNdKceDUXu46w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rQg1odY-yEUCL-LYsgG9F8cquKXFPWK6_PuzMb0zDFsYCpz_xXeg-f6eeJImnXpWffpzKX7H3SQDVAVa3L3I07iT-H79akB-Zf017DsfAQAINwCgv85gXWCQU1bsY3apepDv0LMxY10CS5Xz2J4BEm3A46n33dV_eaEnD6VxsRUXg_LlODD4LpCwGaK6ZDSia0EoM-KtNamBQySeXaTRln6-Cs-Q1k9DkEB9bMvf-LJGt957yefaoBuFebaclFPbq8XiZRGrxDMVd9uEoewT_XdN7mc7JZiAhwiJpvVPHOqSu3FL2yhhss8-plMctu1XLIKt3MEn1UfwkAwsOzjcSw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
بسیاری از هواپیماهای تانکر سوخت‌رسان آمریکایی از پایگاه هوایی الامیر سلطان در عربستان سعودی خارج می‌شوند. این هواپیماها معمولاً پایگاه‌های خود را در منطقه ترک می‌کنند، زیرا نگران هدف قرار گرفتن توسط دشمن هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67801" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67798">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mM2TcBq79wEhytebcB7FQbq8WXShpBg9uRIhACJytvxYB_mFT4yNOccNBLQrF8X8A_XhiUlovw7kqkVVFs3GdnRZD2DRq_U7217v4MW7w4lhLtAJ3ZrctoISdWW9XzeGGsrRmsMlnWDv3RAkK2hhvgAGHaIHPQCJc7YhdzLzM16Lb5HShckTZV2zEkyVdsZhYGP-pFSBPglrMJmPx4DCyjjQe-cxewhD6YvKWU9jU7mTfM2vIrGxL8kY-fUS4MgWDyFHUvi0LXabeteImvWbkEt450Z057WCfZVRnYed1fXQSSbvL5VkCyAJul_e0cA5-uQcu6GJEsagrR5hxjNkOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنالیز و پیش‌بینی نتیجه تمام بازی‌های فوتبال جام جهانی 2026
💻
📈
🇫🇷
⚔️
🇲🇦
وین شد
✅
🇪🇸
⚔️
🇧🇪
وین شد
✅
پیش‌بینی نتیجه 2 بازی‌ باقیمانده 1/4 نهایی انجام و در کانال تلگراممون آپلود شده
⏳
🇳🇴
⚔️
‌
🏴󠁧󠁢󠁥󠁮󠁧󠁿
󐁧󐁢󐁥󐁮󐁧󐁿
🇨🇭
⚔️
🇦🇷
لینک رایگان ورود به کانال
👈
بت جی‌جی</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/67798" target="_blank">📅 19:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67795">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgD_8dv7aLb8S6xzrgq-OFTHueI9s9WVu6uwbWtMcguMQ5wFo7oizJSTq_-lnI_lF7vPGqsZXPlrZBorcGWvNCljQ-IUYFGhFChwsvDRSYXZ14wp-mheXV34YZlpwvGx7xBgrMSCv3rXci-J0h3DLW6we4uEf-kLRLrhbdkIgnaeeXb10dMfK_ra2BfbrNjcB0Wpg03NQZ0bfLaGdFiwYMTkTueyJcv0SjEeaY4bhXdROAhuHoFbvKCuTSPVDZPLvwUfTLV0e0NjiDYXuMJEf8ADzHx_mkEpfGojgPnWQIqI-HzwLmr8ssHRJimgbMRhIDocBFVa9B1sC5fG0xAVlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
باراک راوید:
به گفته یک دیپلمات مطلع، مقامات قطری در حال مشارکت در مذاکرات میان ایران و عمان در مسقط پیرامون تنگه هرمز
هستند.
یک منبع منطقه‌ای اعلام کرد که طرفین در حال گفتگو درباره بیانیه‌ای احتمالی برای بازگشایی کامل «مسیر میانی» در تنگه هرمز (که در آب‌های بین‌المللی واقع شده است) جهت تردد کامل و آزادانه هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67795" target="_blank">📅 18:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67794">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a00f69c138.mp4?token=tNB1Z6PA3IGDPlnwXTqUYDEY8Bo4LGhl1zjy8VW6p-R9vVfHVHcRdmeS2Ui_W6pXi2Dqq6tNXYu02eamclWWxGXmoWSuzEzBgpoBqBfKiYzqAwKDMUxYZIDElV1pYc1rj-ZmRNZpIhQNUNXrSbFl5ct73gkLdghOmFQJVMUCUJXLgf-j6Nif8c8Lj8UuB-TXz4NtJw0eShIs7fegLDg34kqpNM1U799modQRbXB8l7PtI1bCoFeDBOF-x_Sbo1cCnRSUPRfRGJYLo1WqRcyJB9nRF3wIVpa2gIn5XZViL__qXSPteDYvI3qSSr-UEDOexe7IRpC2o02huoxeD-5U1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریاست‌جمهوری core:
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/67794" target="_blank">📅 18:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67793">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KySb-tBVe_lgLfk3Q-0xfTvWBdP8P8leVnsU7w-u3CbqrZlIKzDuiCQjF-8F-OGYGTcQ1MtNy62BmfDwVybsDEQ3AXtKtvMGGOESvl3oVhLC65lD-2YHO2HOIMd8A9i5XbapJgTGi9NfZZYK8rWS9mp1zcHeg4QmLQ6glHuonlmLn599BFSdi0aJ1CAemUv1kaTVv1YJhOPmA9tDQ2TCTkSLJ4hlNsuc6lxE0ttnAOpvzTsr_9gVJYq79FX3hAlkHTGSdwIUAjKsAcg-hYmoTN8PCb5PeEAhuOiiIgkfTMS5P91VdsTJV9SOaIJKT9HOyjGVBhp-NrKLbzScItrePA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری مهر:
یکی از نهادهای امنیتی برای حضور فیروز کریمی در  یکی از شبکه‌های ماهواره‌ای گردش کار قضایی برای برخورد با وی را تهیه کرده و در دست اقدام قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67793" target="_blank">📅 17:32 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67792">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJUvuQzhnslbkp4rMznMiIBNOvAETStYvkvPUQM9veLN0euFmhog0K6I17oR4lV56eC5giZvY-8cU8-uNthIZby3JIkiT0HRiRCFm7wL5z0g1Pb0Qsv9SpTWmptCSz7-m7Y0U0s9k_4Bgw3Xat9ce0wzclHdPRW2fV5FBfroRzjQHbnTO83cxboe5liifN2xsLG2iugynAhdhexaXzYNoxorDspeu5DOikZKjjGc_Jvi2hYTaKZbQIlZvxZcq4NeSSBaErUkR6f_K82eWRp8TGd9h5xFuNgYJSfq9hD2pIdh2ZaJ3iquCEIGtL6g9IXk75gJj3WEXSyUOAN5nRztmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دستهای این توله‌سگ خمینی رو ببینید؛ مشخصه تا حالا حتی یک ساعت هم به سیاه و سفید دست نزده. یک عمر از خون و جیب مردم ایران مکیده و حالا هم نشسته میگه «جنگ جنگ تا پیروزی»!
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67792" target="_blank">📅 17:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67791">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c1e2ae31.mp4?token=GFL2jq7Ag2Avgkvnq-4_pgdlbJtQJjl7uqVWDq9yEd2DYOcQ1Y6qWiO740bQ1F2QYF8PmmAPilU8xXBJzjvbTeVz2XLuzN2wPwDvWLpNysSnqJz3mFC9FTUj5svyqOeOuvHyOD1XiKvDB8eY1i_am-603uDAYHtx-cPTKVnS-shiMpFeibLHQSuitVkp4n-XurUNmW7cS3Dwxx_huP9ndUF5ufe1mcYRQGcEhQOSxlepAjmz70Vt-1chkexLBogEGPFl16TU4G2viB58tNG0ZwJArQb8eXLLZ2ab8s8WMxBFa6kqvfJHm0W2zZv2_Qbl8P_iD8DthDHV0_B1WOOnHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کوچه پس کوچه های مملکت، یه دختر و پسر شروع کردن بوسه و مالیدن همدیگه، تا اینکه دختره دستشو برد روی شومبول پسره
👀
یکی از همسایه‌هام وقتی دید داره کار به جاهای باریک میکشه اومد و گفت جمع کنین بیست نفر دارن از پشت پنجره نگاتون میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67791" target="_blank">📅 17:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67790">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">‼️
ویدیو وایرال شده از بساط عرق خوری لات های کرج
😳
امیرعلی امیرعلی امیرعلی....
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67790" target="_blank">📅 16:16 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67788">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uMwdbL0FVYWd4cIG6LE_K2BoCxAtaetbifhHLdrK2tF-OnWxudqG0wHSCaDvRZklCBa4j5KRRqzhvkEBsYTF8wmPun9zLFrvan1u_AQY6ID-z1MVsMYlq6ME5hevwsOxIR883yPciATbIK06jSRWVqobYxFpJ70qRu_mVvo_c3HC0Tl8Dg_qAaRi8EvtdDGE9cWGMNdl73DcUAK8ye_DSuY12J_x5DaeKiw9e0rzx7oywnXioZHatPWTjedgZlX2dBmEHG5JXs02Cc87r-aJaTyP7erjlbGbvBPNLKGxTJll_xLRhKrpDhVmAHZTV3kMX7RJq-m4vc4gmU7RqPUMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=QTxy72_WkoJ7doM_P_LNTkDp0LxRDAJ-NdGFgp3Ah1IqYYcY1pPRNUkZ-n8Vid4TsJQi0tmgZsJwNS3OnkU75Sx6KOQNO7iler4OF-_FkIsIyppLPOB2UHH7y_vuUZ71w7l7IexIkgVjjpO6_fbFt3q9KN8yf8gPODtokDlDy6s1mwDeR5VLvEI6Kwvp-AJGteIRFTDgpqlPJ3pfzvubTYmRi3cmfcH5ZKVrBa0Fq1XEMuSwBU_z8FU8SwiX7gjANQf5FyGQ1yAuw2Z_ek9peuE_SIDeMhJEe-iFZkF1nVrJnc39caVgQcIIp-vjsHIljcIw_xHiNkxQjGzGGyHSAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3354c0af73.mp4?token=QTxy72_WkoJ7doM_P_LNTkDp0LxRDAJ-NdGFgp3Ah1IqYYcY1pPRNUkZ-n8Vid4TsJQi0tmgZsJwNS3OnkU75Sx6KOQNO7iler4OF-_FkIsIyppLPOB2UHH7y_vuUZ71w7l7IexIkgVjjpO6_fbFt3q9KN8yf8gPODtokDlDy6s1mwDeR5VLvEI6Kwvp-AJGteIRFTDgpqlPJ3pfzvubTYmRi3cmfcH5ZKVrBa0Fq1XEMuSwBU_z8FU8SwiX7gjANQf5FyGQ1yAuw2Z_ek9peuE_SIDeMhJEe-iFZkF1nVrJnc39caVgQcIIp-vjsHIljcIw_xHiNkxQjGzGGyHSAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
حملات سنگین ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67788" target="_blank">📅 15:45 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67787">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a812a42d8.mp4?token=OEZsxJon_7lc9kOSenL308nSepiVO16LyNtaF9mGLYkXuP65sj5Brp9gmLVWCGLDfAmLY85NCBoUvtxdaCi9zEGInHp6x60kNco57sVp6TOK0luYCq-G5ALOMgZ678JOBWAbKs3TOa6T9ZGZCxcnm-lAekoUzXup2EO7Nx2STKPJPMJiUcyJhBT_CiF6bWGD-A7JFxbNGDLvANKrqoVnQTdBY7gQawVwVaEgpttrceG_ZufioQfU-VbyMlB0brmmVPnVgRBuEDQTEykAfG6nzWh6sNroxd2d4Q19PJM2ji5Q33sPbJqJ44J5sjzKbwc7veDWhnmhPivjbuQi1fsAVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مجری فاکس نیوز:
رئیس‌جمهور می‌گوید ایران دوباره به میز مذاکره بازگشته است. آیا شما واقعاً معتقدید که ایران با نیتی صادقانه و با حسن نیت به میز مذاکره برگشته است؟
🔴
هارلی هیپ‌من، تحلیلگر سیاست خارجی:
قطعاً نه. البته دوست دارم این‌طور باشد. هیچ‌کس خواهان جنگ نیست، اما ایران کنترل تنگه هرمز را رها نخواهد کرد. آنها به اهرم راهبردی‌ای دست یافته‌اند که به‌گمان خودشان، شاید حتی از یک بمب هسته‌ای نیز برایشان ارزشمندتر باشد. همچنین قرار نیست از تسلیحات هسته‌ای خود دست بکشند. بنابراین، آنها به دنبال حل‌وفصل مسالمت‌آمیز این مناقشه نیستند.
احتمالاً این وضعیت تا ماه‌های اکتبر و نوامبر به شکل اقدام و واکنش متقابل ادامه خواهد یافت و پس از آن، ترامپ میداند که در آن مقطع چه اقدامی باید انجام دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67787" target="_blank">📅 14:59 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67786">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
🇮🇷
مجتبی خامنه‌ای:   آنها باید بدانند که این امر، متوقّف بر وجود شخص من یا سایر مسئولان نیست. ما باشیم یا نباشیم، این مطلب محقّق خواهد شد و بزودی آحادی از آزادگان در سراسر دنیا هر یک بخشی از این مأموریت الهی را انجام خواهند داد.   @News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67786" target="_blank">📅 14:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67785">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:   عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد  @News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67785" target="_blank">📅 14:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67784">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🇮🇷
مجتبی خامنه‌ای:
انتقام خواست ملّت ما است و به‌طور حتمی باید صورت بگیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67784" target="_blank">📅 14:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67783">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
🇮🇷
بخشی از پیام مجتبی خامنه‌ای:
عهد می‌بندیم که انتقام خون پاک رهبر شهید و همه‌‌ی شهیدان این دو جنگ را از قاتلین جنایتکار و بی‌آبرو بگیریم.این جنایتکاران آرزوی مرگ آرام و در بستر را به گور خواهند برد
@News_Hut</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/news_hut/67783" target="_blank">📅 14:09 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67782">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🔴
پولیتیکو:
آمریکا انتظار داره جمهوری اسلامی در بیانیه‌ای که قراره امروز منتشر بشه، «به‌طور صریح یا ضمنی» قبول کنه که در حملات اخیر به کشتی‌رانی در تنگه هرمز مرتکب اشتباه شده.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67782" target="_blank">📅 14:04 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67781">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rLEHfARz3jb64BoYFXOnUcV084qIXHXGWcKg4tPO48XhNmQk5JYl0KJH_0CyRuVQgI3UrbAtSYVtDJp_DR0HE-0xrVooRXaq2PIJkuD0HlYZJLiijWJ0yebAMSScNNDkXA1tK3RCx2-an17aAo7lrRsqieKcSoP-RHWxQpHvEe74obxekTRKp0tdU-lI5C56yRqlV_HVHF8rywgNbaDlTwDTB4GWJTvZkEyrF-2-Yix7dsx0RSURikTEB05brzwTj-ZgQ-IdxuT58U8uIQpTKDrzKplpCv80oqLJdYIo2mTAQL9j7hCOfYkDjM7NEUk73d9bEHnKzeuu2FuRWvfRAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
امشب رو باید تا صبح بیدار بمونیم که ديگه کم کم جام جهانی داره تموم میشه؛
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس vs نروژ
🇳🇴
| 00:30
🇦🇷
آرژانتین vs سوئیس
🇨🇭
| 04:30
🇮🇪
کانر vs هالووی
🇺🇸
| 02:30
[این فایت خیلی مقدمات داره و احتمالا ساعت 5 صبح شروع بشه]
🇮🇷
دانش آموز vs دین و زندگی
📚
| 07:00
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/67781" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67780">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآپارات اسپرت | AparatSport</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XqNwnQvmoTCgFesfL9YIP2F0Dc0_YkpQQSPo_UXP1bzROD6Nbt6tDH6M8yzHAbax0KnGuUU8SSCf4BUy5MqcLd0W0iYNB4joJeIP204ZH2SIGJyrlNK7cl56mdU7j87onnaGHjK08hOeBEpIoATmb1Dozxt6UkXE3UKIIFE6Aq3bUAxizFalMe-WMwpPQtl9sGe4ePMh5bgmvSZl6KPwuHAAY0Ehw7zkqyCkF_OazGuxapXgTBqB2MbHVdmt5fTORA8zDKo1BRRuDxTTMwdnHEbfaYsEKFiGb90n9OhWcOJVvkfD4ajBeGepxCjxp4V04l-TUklQcMfnX9hKOZSA5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پخش زنده و اختصاصی بازی نروژ و انگلیس با گزارش محمدرضا احمدی در آپارات اسپرت
📅
یکشنبه
👈
ساعت ۰۰:۳۰
🔗
لینک تماشای مسابقه
(بدون فیلترشکن وارد شو)
@aparatsport</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67780" target="_blank">📅 13:55 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67779">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kluBnoYlJnWW1CX60iPHsYAbb-x09CQnYL2FSivaQM-I8UpuosDb6oHxoVV11yLdSMYCwSszXTwpBj2ewzMU9iHHfpC-CgpZ6V2J3n2ovrn35aaXLuZwEkGB6ou8-HV427OdSbSAbq0ztzKs1VVsuztZaMaG9cPcq0Cpzc4vrzlle3nRKpS8B9OXe_Dn7iL3nVd_xBwKF1p3_GzmxeKdDZW1C8QNm6u7USolSBxpAeg7rK8je8L2638nc2_xjCdV-iZseNmgiYg32u1Z_nJLQdr6vy4HMtM72skZkAR_gCX2QYy4C8v_Cgjs-cdgBxI_Cj_0j1yVvmykUZw0G_oRwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67779" target="_blank">📅 13:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67778">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2gMhdm4QJlQte11G4BKVfP-iwldSbFoZvUccA2PP9h-tmaH6TyylAKaBrhA9oy_nQmakrEX8RECMamcmnNTipv4GVTSv8O1HyWUk_MIvU6s60BYihPVbyIkJ5Us5qDn7520HYyKzMNmxkOQue2zIyR8VvpUCAY6lsEALqqpgbCI8mdqbvd5fKZeiH7UY23d_o4QpEouuxG97t9c80gsRosNZZLBlQkfOzm7U697j7XLaR1gQyd5P4oasehFSNqWDaZwzTfkt87lzlwtLf1N3odU1OH8QGZmUBwj1orbYF2-az39nLsjsL8YjN7sy9uaVX3iBErZzGPb1zVbVUAw1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.  @News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67778" target="_blank">📅 13:30 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67777">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e80649858.mp4?token=Sab8sSjKmXcGaZbO9K8VjYQ2UvyeTxGvC91t1tXe-dtx0Jq-WYgOqSnEZTeEiGZnj8vpXLguoQ43OBxrSui7FvIj9G3F6kBw82AOQUs4EcJ4mRjLvWUS1Bdy1Q7ugIDuI5KxXk4can04pVSlQRHjWh2W_xFIOjTQkZuekC6RzQ02TjaZ8sguxog21BvKQbkRwTHHN8en7L6fqWfLehygHo7aq-vCC3We9EIIZuFHyAT6hq9gM3B_B9cteV61S7j_KTc4oP4szlbkWHjYu2c4JBJIn5VgCchZHqqKMwHTDOflxyQJKqQiyoc5bmgDLJK_N1WPlg1GlZUvaQlfzEn6pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
#فوری
؛ تصمیم نهایی برای عدم تعویق امتحانات گرفته شد و شبکه خبر ساعت ۱۲:۵۰ امروز زیر نویس کرد: با اعلام وزارت آموزش و پرورش، امتحانات نهایی از فردا و بر اساس برنامه اعلام شده، آغاز میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/67777" target="_blank">📅 13:26 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67776">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:   1000 موشک در حالت هدف‌گیری شده به سمت ایران قرار دارند و در صورتی که دولت ایران به تهدید خود مبنی بر ترور رئیس‌جمهور مستقر آمریکا که در این مورد، خودِ من هستم عمل کند، شلیک خواهند شد دستورات از قبل صادر شده است و ارتش آمریکا آماده، مایل…</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67776" target="_blank">📅 13:22 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67775">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
ان‌بی‌سی نیوز به نقل از مقام آمریکایی:
اگر ایران امروز در بیانیه اعلام نکند که تنگه هرمز مانند قبل از جنگ باز است آن روز برایشان روز شادی نخواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67775" target="_blank">📅 13:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67774">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
مجتبی خامنه‌ای  قرار است تا ساعاتی دیگر پیامی به مناسبت تشییع جنازه پدرش علی خامنه‌ای، منتشر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/news_hut/67774" target="_blank">📅 13:02 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67771">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70c6c6a4dc.mp4?token=q1siNxInuXuiCaTXg6_4ZRbyt87NbYucMdo4Cnw2LLMne6Yj_AbA9AZQzcTTBMxK9Sx56KvHJ49809FEM9HafaE9AK52KLy4de2f2_aNsN1Z71n1HMnnUZjKjPcu8y3wGtUDH_-tagD6NbVFdfGiaXTSDKiTRs-Snlf3x6dcjDkz75i-Im2mRydoNFCZfuzTFh36PEDbyGF2J-5iMW15rLjZ4Sklnj6h4biUAYoKHPAKt3RFDD8Qee_rV7R3tNmublvtVYMKsS0BIEBz9o7LlSZOBwUEt0rxzydRcKixmUCiLPETWd7aTl-f6obZPggl3N8cmnyr-FOc9aQu0LtcTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بعد از انتشار ویدیویی که توش یه فرد ماسک‌زده برای علی خامنه‌ای نماز میت می‌خونه حالا طرفداران حکومت مدعی شدن که اون مجتبی خامنه‌ای بوده و بصورت مخفی و بدون جلب توجه توی مراسم حاضر شده.
@News_Hut</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/news_hut/67771" target="_blank">📅 12:00 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
