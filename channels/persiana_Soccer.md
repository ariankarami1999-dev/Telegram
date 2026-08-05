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
<img src="https://cdn4.telesco.pe/file/GBIFt5_l3E5RvyyurTKJXJqGSAxjUXZ4GtnuSkx76JLzPmlA7xjEdc551rw_WB5mWZSBIliwPzZuql9725tHLiqDL1dMvC0W4d8VeOVZ3vtqym1J35OId01CDRp9odD1MZcqGe8GXK249aiEHnVIjcH8hbHgXxkP6ga1A05gxv2usVDQcsmJzuVmuGGHbJIRAe9dq3-bjscYe5KewdUkuelfl2NqiuwmJzV-JuJQ4WmYHTtUctm1mv9VulBt2R4GPAOosvH1SaSD3IPbFkUVbaR2UNOraSHeOyyfq1GzRHU1x0u4nFqYU3gw8Z8LTYlc2eDAWIUVkf4fVjw2-QjY4Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 626K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-15 02:19:37</div>
<hr>

<div class="tg-post" id="msg-27179">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jhEheoWubFcQAnkzUCH0O6iKO-dwRBi1UUZFJtK0BTK-5ZM2eOd6E_Y1wonQdCvMPgBkqvxTEpgDllq0yZtsRuFATEh47A8KgRhTSYhMzTwFmfHXAIuYq-JxBkicznn_4YAMO4eAu81nL15PWGyXVoLgu5EpFT36sgVHiU3R0c88GeNzvA6iqiY7PLFZRbANr7RuPPxQxPkZDnovsaFv-ESvqvQPza3d3fjBziVMEQw-KKZvHC_rTSxh47d4EAA-XKIsAhMbolSofFFdf-vX_V0Kdq5wTWd1QMx_NeHNe0SVSoRcgbGMdVOPWbzHnrEL-cUeJR09poCLVuY1GGUSaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/27179" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27178">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55341bcb2.mp4?token=WoX70ySrdcC-BWsUIVqWP_M-mwNRBMNrJKpQPOvVMzEsg6C12P534TyEyKsB44Xhsv563HR7mNVtbbv0zceeG52xM9VfhFSM6-5CkWZ1sMnhQ6h6EeIpsJesYQdmPUSrNPs77x-8fBJvHwQ_7AUT8VDut0cplkD4e25c5Z67v_8oeVqAR1qRCsRM9vlK2AtgLKkYBBMdMdlK9vYCeVzjtP3Qoo-UQNpfIRWcR54L6JlXeYGpY1OaWqaPfPcncTul7rhPyC4bY6i_4chSrDDcMY8ddhKS1WzaTdMY-22AA6DUX4Sqg7wFyI4thKFNl_-8qE4eiWFu0kuX3e8JW-HUZV84Q8D4ElXa-uElwWxQ3VhK007wkUHAAC0sDpe-fcZiJXWXKWVT9oIeru4HG4JF7bex0u5VBjal3x4FugM8u3IEAmCFW_KIV6mWaGttyBZgJeybVGrPzrJ2sQtEKnUoRGhozftifpmx55RtMqVuNVGbVvD7kD6hrEG-8FnJZMCSx5J7dHd4nVcNjgBqNcUyYuQHhQC_mYNq5PP4nnCZ3H296nru0DDu_QWOfGNSKH2xUTzks6z6OgeLfQLZi13D65zzFrTT182yeVjvi_kxehsZFsn6q8w_bYy4JGVeC5i_1LBFhST4fRdxnbxx1cxJ4jIzTZmbC-FDEX1DTeDl4X4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی از گل‌ های دیدنی در مستطیل سبز روی شوت‌های فوق‌سنگین‌بازیکنان؛ عالی‌بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/persiana_Soccer/27178" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27177">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWzOruFSVo0zOYnfvzRi3rjkbgPKHwvtvoJvUDSZFSCwwexVToPMzmgt4TlLF35BKzDerEee5SDveIBnJPw3QVO3AWN6hgZYPd3Nps0kzqGj4TJXVcfXJ9GYa4V-lWub4xptbuuFwAoTMgMCM5-_RzSzxBcqHad1o_fkV-bwYfRGkSnxoX2VdO10JSRpD5NkfUjzd8lbBvIUetCTaE0FoFj0Wz8FxWYIMt0YyMD1TY1cXNsNVz7YNHXLITMOUtaN01Esvu4baIizx-JVbDYTHKQ-_bJQ6zaPwJ9cAbaZiQsKijCbQHO9SvqmQlxbfCtCret1_TdH8ybsjIxp5iHh5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه همیشگی شما
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/27177" target="_blank">📅 01:17 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27176">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=cznt0si3fuTDzAwoTsqWfgZFzgpCDT377fkrnIECu3VVvoamzrIUMP4ScC5AuWI2F_uaSRP-ouYZ6XUwi_uVTtSZ_iqq1revKjzxcg3knx4u7Talrv6-kEDdTSAtaYw8QiP65-xT1jBYAriZiOqE3weG2XOHJ0vkCREwjR10cfhpu3KVtngNHTgLcNb4z3IdcWwza1pePwukiunQfahmARUD0MXVGAc44ACQcjy1iZXW4ztQ1U_u_pSK4w7lKAI19bF8pdNKPvRjx9uE-UhyVLnuxI25wdv-J5qybGyZ2WIigqXWbkdUpoM8Nss2O3596aZgWWGSmlPUmWl5IEL23g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/729a2d9732.mp4?token=cznt0si3fuTDzAwoTsqWfgZFzgpCDT377fkrnIECu3VVvoamzrIUMP4ScC5AuWI2F_uaSRP-ouYZ6XUwi_uVTtSZ_iqq1revKjzxcg3knx4u7Talrv6-kEDdTSAtaYw8QiP65-xT1jBYAriZiOqE3weG2XOHJ0vkCREwjR10cfhpu3KVtngNHTgLcNb4z3IdcWwza1pePwukiunQfahmARUD0MXVGAc44ACQcjy1iZXW4ztQ1U_u_pSK4w7lKAI19bF8pdNKPvRjx9uE-UhyVLnuxI25wdv-J5qybGyZ2WIigqXWbkdUpoM8Nss2O3596aZgWWGSmlPUmWl5IEL23g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/persiana_Soccer/27176" target="_blank">📅 00:56 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27175">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1mkK8TGGTTgMDa2ngVskWUmw2ND8k9j28PI-pkiomUpV2BzgYFw0-kJ4OopuNvCzIL5wWF63bslLufhV2MnYmTf43Scm3i6qHSJvePOZXVV-KLKkV5BzxYyVoehrzgaHX0-a301wzxZGAAa0xlCYIGLPCUWqZwCyQaQAXEu6dThdsdEM48AR10L3QML-m9F-QBfHtkZfllsfEA3tL-G2n-YdoDbjlqxTSWRXieav9ATf_OkFinzVyOq3-rUDt2g8Jd2pxXsXGhmpen1jv2cbGOFTFtxxnIzvZfJWWkuL97r5JU0jbom6oetAv4FL0SkPqbn4TEKyZCoBCUB3y0bow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه ‌‌‌‌دیدار ها‌ی ‌‌‌امروز؛
بازی یاران اللهیار صیاد منش در دور سوم پلی‌اف فصل آینده لیگ اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/27175" target="_blank">📅 00:54 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27174">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cp44nDugGDQN7WGqw1eCesFdZwcPf26-d5ZOoofuF7CUyNLmSZ4Qdb5ue_4_RYTd7t7Od9IPugKxJWTZslrXZeN8fMNNlb9rnpjtfEKBUmqNv_xsTq9tV4FcPLq-QV3_LsFGtrtK6ty-2nFMkMGTqJri9SXf9mzeTRNqQA3ukXfMbyMBPABHoZUYA__cn99_LyS8OoMTbhhP_VnhnNdV4wcquKGA_VmcK91tUDXoSw_UrOXf1sJbYxGZ1hZPMrlOZR50ZM-I908dqh2JwBnPFNfIzRT1xP4AlTATwGH9EWf3Sjmw91rXzYkqOPT54uHPCmP1CR2VBHTsBrlGWz7S9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای‌ دیروز؛
تساوی در دربی میلان و برتری شاگردان اسپالتی در جدال دوستانه با چلسی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/persiana_Soccer/27174" target="_blank">📅 00:52 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27173">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gd26SkgujW-vnz6cab2PZGloAXjQC-87oozRL31oJwQ9LLOPn8Q7y2N6nG-Eo0QwYpa4f_sAdFianBeV2tSGpLxX4jAmOoxxUFEKgsgWV7P1-82ZHnG_PTlJ9wU5Q5H0NFyg2IBy8-4KNDcleRcHrG-4xpatlPEn-SPcFVOHTgoTQ6nXGlyp77ewVyt_NCdisP22yMyIDpXq3LaF1kQa4ufGtSp_te4uHpWw42QoJBBzbvPxhPpO5fDj7RTa0NdtED5nzh2-bsHW_qyMXB_Vd825x7N9mB57WA-9wJewOhCNSp15kQkSJDOBJdn9x_KhunHV9E-uTrQriE3RORC0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛بیانیه‌جدید باشگاه استقلال: تموم کارهای‌اداری‌مربوط‌به‌بازگشت داکنز نازون انجام داده ایم و منتظر بازگشت این بازیکن به ایران هستیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/27173" target="_blank">📅 00:41 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27172">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeJHsvkdfHZtnWZ5F4eBzLxtk8DdKa4eG5a-yhB26NW1jr8ltRkkPPOJzoHban9zFc8WV81FdNE6fzoK2fngSqyFE9T2LVsKS4jqO9QGAOtHpa5JleSATLMdnonM8wSIK5NWe9phxHvSu_ijiXTVOoAIg7ZfcLdE_Uwa4rllC37RamHlDlgL6QQc2cRMKJ_keeurUoELNDb5QRPKvIlKwM3Kgjz-lz2_vBuLQjera9HJX6FYmpT4T8A8YjR4todUqltBucl0rlqNkij3WIgCtE_xs-c2XtVoYjI5sRTkdFzJqRzrUwNt6t2fn9CWnmLFbPKL5KanV20SWnQmz7rRqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ با اصرار زیاد مهدی تارتار؛ مدیریت باشگاه پرسپولیس بار دیگر بامدیریت باشگاه نساجی بر سر انتقال دانیییال ایری به جمع سرخپوشان وارد مذاکره‌‌شده‌اندوقرار شده که این بار پرسپولیس 120 میلیارد تومان پرداخت کند و این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/27172" target="_blank">📅 00:30 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27171">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V4oXaCtkdQ9_f6towDPJTJBiopjDybnplYAd1tmKTTOkuM9ZGo8EdoG0kUNnnKCBGM5Lao40RVe1-U9qaaqely8UjQ0cy0G3DVwPfNwouhMnlK4y-nuDRBnYgRhDLtS46Tjk8_H0Q-SrgrbySeDG3yWQNwr563OApB_GkYQcZVRJit1khbEKF0UDb559u1ESoFJ82pQcWW2H4ywbhs8G-A7AHZ3E_8mp4qXzMriwrBoP3FZf1TgLAVNmYgueMDhxORSshEV5eP19MBfpo1y_syJ3g6f2tg--qB6EiXH9R8a-rhADKTLS6T3w-LCKGk4_b4maVHduJDYXxsgKVeSBfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیرو خبرچند روزپیشی‌که دادیم؛ باشگاه نساجی به احتمال زیاد به‌وعده‌اش عمل خواهد کرد و دانیال ایری رو پیش از شروع فصل خواهد فروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/27171" target="_blank">📅 00:23 · 15 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27170">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPJEHP84WYf4xSs3RKYyI6DZ-mNkq6k_71yiOnM05yFpEdtBLsG81NxkrdkNCjf-GhCqfXD7MkPHBMIsfOuWvwKTeY5pwMiOsmyp--dIKzthSpk6FVYA6e77_BvW4w6zxD78x3LBN_3OfHP3ofOqBUjPHYmfTiC8VzDbEIx4T_At8gqUIVMPk5J5P781bwWNx1IUQihDJGZHkVTQuL3Ddzkl1Bvv7B6yqKwc3IM9w6h6bZonAqVIpvpEG8A2DpDsEd-CEH5X4yjUltKa7IHgOanqatepludIj3hVF881wiTPffQCYcHUH5vrEqPIKpFnDiatuZ67D1WSr8haF5ynNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
وقتیCR7 از اسباب‌بازی‌هاش رونمایی کرد؛ كريستيانو رونالدو با انتشار پستی در اینستاگرام از ماشین های لوکسش نوشت؛ اسباب بازی های من.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/27170" target="_blank">📅 23:52 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27169">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T2pO6GPux1Hf9Wc9nIgR6LItBJrQ166HxsmPb7e9g91hx5sMH4xFLc_DX-eXeLah5EqVHjqIgRZqrUD9_H8LuO17r_LvDKgg1LykDt3W_ePpNslJK50XcdNlZw3Lg9eM5n5TMHRvjn1SEJkzwAGZ8zLxt5FbVRvIttANGesaQaOvkDfJmL5adCYriVmV5hKoFYgZoo9vNOisyr7UWX10AzeWx3QyrasocYRg0iGE6ph3OBVoI2Bt1QgJVLzKzorkX9ZI4Fkyn9VzOytPogcwIZXwlirymOzkPDZhXoMrRepRoGteNtwUhdhVmnfoc8sqBW1fIlB37ZdFCbhiZq7FMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
توییت‌جدید علی تاجرنیا رئیس هیات مدیره استقلال که غیرمستقیم‌اعلام‌کرد که رای دادگاه عالی ورزش اعلام شد و پنجره تا نیم فصل باز نمیشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/27169" target="_blank">📅 23:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27168">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WqaqFZb5FULcpD_WcQkzkAQaksXERYmh7tzVNuBVPfIdMr3kJ3KzWyvvNl6AfLjzS7hFWMMYKWHKpG_emVE3sZTvVdwzZOSaynf7mW52tbUibnzSRV3HDQIOs6xSg6ei83nkigUEVxdPTTukI2p_Q-R7v_ofF7UzFN-wK66Nk8LbyIEhXL-vRICqetNQYUYROhfg47kdUlh3iRvgGlpaH76g4l5xVBRMGFc09QDBpxqkOtDnQ317deFyH30D0MBm_19PX3JUMnHg9yksx-6EhW16EhZHXAh0RtvUoxP6QAfWGW2Hfbqny94e57NkwxdBMSGHAbZBImv3sy71Pe3sXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
👤
ساعتی‌قبل کارت‌بازی محمد مهدی زارع و محمدمهدی محبی دوخریدجدید پرسپولیس از اخمت گروژنی روسیه و اتحادکلبا امارات صادر شد و این دو بازیکن جوان مشکلی برای همراهی سرخ‌ها ندارند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/27168" target="_blank">📅 23:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27167">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b58266add9.mp4?token=Qqe6ljpu7PmUpjHt-AR_V4QgBiivRNcqxvl9UMMlzAm3KDwbtyFu16t_r_gGP8Ev5frsx2pPKSoigaeKmijc0A-95kI9AXGPfKIID0VZGitORai7tsetbuvoBAPPx3FI3lb8lwM4P4g2BcAXElz0TBbDYpMf9qgi-jjC2KRZ4OYC0qDm00LVondJRUp84cScrDnKK4FW7czBTLpx0UeKl60IEytciBZJaAXOAafrwE34wq2QvGpwfothqJoa3cHZIPvAMwCI5lda3cMojAa14czHec2uXITzmZGjbFNOoQ6tEk0FP04_V0Y8vrtOyYvz_9KqY2IfxfABoJ93sVvUyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/27167" target="_blank">📅 22:51 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27166">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbd4624448.mp4?token=K8j6nXIUadHX5_Yy0kE_SppnQCAymZyk9b1Au26obIjA2suV4UljMg3yQlwnqumbhkjQQUb9aBwpyyIvIXzY1ofvUrz0QvumB6upl5iUeR3XVnBq_Zozb10fW39wSeji7NKLLCIrXwRQgxvlOfoDpSLuCXroMM_RrnoU5HJpyfgWXZtT1wM8LCQYPbzJY4Vs8Wmrx3YYlVlAG5wumxTnAy8oi2Zu0pZvEEhHjAl6Ld_cekiERykGmKiP1GeOERa0jAs2aHeSAP0FQPrVKkVfDgBbOzIl9_zbr8R3VVH55CooTMFthXxKMHq2NyzDrvo-rOl-_rfm1wRK2fbncBq2dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
باشگاه‌فجرسپاسی‌رقم رضایت‌نامه یادگار رستمی وینگر 22 ساله خود را 50 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/27166" target="_blank">📅 22:22 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27165">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EAAK_qC1tKOj0092CNCwlbkhnMKNtmeWDubr-n_Z90gQn-WwsNwkDFEqauEuFRRTXV5gnhqn5KLTtD-eyx8vGWqqJu59i-N8Yg1J4sh2-s_RD1Y9znV_G8OgdWBf15p5bFxqG2-UqHZTm4wBvSrjyWF10bBMYYirRDXOxVRLdGkQ3A2QD9nEmegIzkgT5VRsK_zRMgCILBDsWlVNNSrZLGzqIv8w776fwS78PPGmus4vdPNVlT21gZDvoy1hWSiHlLUFTk3TkXWnEwdAX2J02D0LKW6hz7Ladk8_fYbrgGhy6qMYqhfGIlVnlhK0D3ycmFTocw4kj8Mc-kf5d3n_WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
🔴
مدیریت باشگاه نساجی به دانیال ایری قول داده هر کدوم از دو تیم استقلال یا پرسپولیس رقم مدنظرمدیریت‌نساجی رو پرداخت کنند رضایت نامه این‌بازیکن رو برای آن‌ها صادر خواهد کرد. ایری در شرایطی به نساجی اومده بود که از مدیریت این تیم‌قول گرفته بود که او رو در…</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/27165" target="_blank">📅 22:07 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27164">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/neDrS1C3c18Kjly-0oRjQ29fP16IvJSSgxq3HSfY3BcCPtWPv79qCcsyicB8KFVQ_jiJvljW6n0dgbjhKItaTflWvwqJKePqlD7sMyHkpRFK1537IZU91wlQjhsVL6RkDUGv8IE2wo0-CoWrKISZU9JfgmjrT1zdftOAC8vSDGVEM2j8OFEXqPNUGi_BwQEqo1M4yQ7t83rVGHCtvJPNXi27ZqSWFSRi9fesoJf_-1Kw2Pdv1mvgcWI2ubySCOmynRFMVhgn9OhJh_V4BM-ihhf5w3Jt1DhJXvx3132RE7GLxTehg4PHj7J2amUpDK_jnsOViusZ6m7XrsB7y9uAeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
🎙
محسن تنابنده:
وقتی‌حال‌مردم کشورم خوب نیست سریال‌ساختن‌ارزشی نداره. دوست داریم فصل جدید مجموعه پایتخت رو بسازیم اما شرایط جامعه به شکلی ست که هیشکی حوصله سریال دیدن نداره. هر زمانی که حال همه خوب بود میسازیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/27164" target="_blank">📅 21:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27163">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR8SaDeMmnWeGgR9o41eqZ1DorBPgo07-YhSs8nYgScDH-CAMkd-5g_DucUGVbsMnW_jXV410vKG5-DzO5shgAODX3xfK4qp5eqxAQbrTI-I-AIuXWaE-d0H4Udg70ZG4szWSpBuQjIM1p4RyqJmeD_l6MUaniVAxq2dxRmhpIul7e9nGdcQq5tbzgozBCkPHoDIpsoXw7nAHHiJy__XQwY1uVeJwUiho8aNWVdplU_wWCs6VMNuJPXEj3bUMSJz6sndOp1hm7TwxEJ014UfXeZ8LGL9zoC8j-3PN6u_dQJ76BfO8pQnbDPZGxlXpi0FZFaAlE3WDtktfntBO8-PhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اگه‌اتفاق عجیبی رخ نده؛ تموم خبرنگاران و رسانه‌های‌معتبردنیاخبراز موندن وینیسیوس جونیور در باشگاه رئال مادرید میدهند‌. گویا فلورنتینو پرز با رقم درخواستی این فوق‌ستاره موافقت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/27163" target="_blank">📅 21:08 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27162">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_BgRkJfEGcYG9Ax3MVXEihMWBShcZMW3mr_B0X-kdlKOxKf5KOUZ8-7jp9fF5pkgP9ScBhC2LZcv7oel9CIxGIdDYuuML11fSDKh7K4j8RWSJFObkksPngEhr0S1_5P_05NzejLK5fUg3xJz2NUoi2TczqF9sKwbprINwArcpG59swfsGObGcQJPqC6pnGqKtG3LSjpG0WBehxKyr7vuA6-sSKwkIFpFWgXM1F_OkMkAPhus2Yzle2rattXsuEZ6waJFkQMOidJQRierACEz4JaYFFxMvDtiXrNInqLPesfFEHPlEvQjHpqsYEbiJ1krqS2UuitBUDQXwjIqSr7KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق ادعای جدید مدیریت باشگاه استقلال؛ فردا تاظهردادگاه‌عالی‌ورزش"CAS" رای‌نهایی خود را درباره‌پنجره‌آبی‌ها صادر خواهدکرد و به صورت ایمیل به باشگاه استقلال‌ارسال‌خواهدکرد و باشگاه در بیانیه ای اعلام خواهد کرد که پنجره آبی‌ها باز شده یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/27162" target="_blank">📅 20:40 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27161">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ng0o-O3isV1l8CvPBMm-fybhgS4mf_cOWzbpfRNFQrQI2ZgxiQBWvUmmzfY0FVGckPF7SzL2UwuvHMPGBJP0zsEH8jz0CMNbON9QU85RD1KyLlgCgwn_PJagpxh99b2LwgdK1Y2ysC5a9meIn6y9NRaGnqEat5FCVUibkyo67WhNNZzZm93KHZTxDH43soompejqgRn-YeWwS-mLqiyBzoQF-n5UY95Dnf3Spb8TiwbABDYOli9Raf9eM0_ZV74CSmGVF7WrJMkoXbdVuW_owr-GD4Y6Ax8KPC7fZVvfwdSsVc556wh6olnUmpc5AUdUeFZZwn2O0LL6BmSpiPsF6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
ادعای اسکای اسپورت: وینیسیوس پس از مذاکرات با سران رئال مادرید دراین‌تیم ماندنی شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/27161" target="_blank">📅 20:14 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27160">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tq4YSwrtc709Q-GRM-AbWYs-OvJahaTh07knC3RmmnNUJmTG4TdsMZCITjza6C81dG88hWrSMn8iZa3BpCTXqnguM_pJeyYdt3MNHXzbXwCHf5CC03BlHcpvrO21-GoXWbAuJIt2roF-RUqXqdGTmpSiYLW-xyScwsNpdrhwOgC_l5oypZbWaLicJOP5gAGr2AtNAw_mWmpfRQb7JgNZ_FdJd5xa72_D0gpMntl7JpYfBYJSDc39USyqve9vs7ri15oDQgiRP9OPIbrL-uuEKxB8kipquJsDRp4n8KIzse_UL1Sqmhgaxz9LB4cr3z_kZWOMHqRiF1wOw4w1c4B7IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
باشگاه تزابزون اسپور ترکیه با انتشار این ویدیو از محمد صلاح خریدجدید خود رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/27160" target="_blank">📅 19:53 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27159">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ALR-zXRd-jImnhoRyur_-cfzyl-E3E1HPSKbLsSwrIl-lZVTLucqR3lR_JcpUrKfKRnvhrDQz9LgvlPloezpL2vXG8so2eZarga8sv3rj4wr-u_cfm1JzCWrICVoR9UivHJuYZgFxX8RwDAJNQP0Z8bRiTq-NNZ2B2wSGn1tOjIJQy1SO1IZrMLERav-A3FSiuwg2CrZMrApBDSQGNgUoGtFwXYmmavBtCMB1YDNqIHy_Lcp_kOyKed9CTiEBIwZdf00WfOd-JXYEpGTQXRbLId1DNFQC65CDvCSqhIOMOIdcuD_8KzDjdCCPdKJW4V9om-ZqSpVxYBJwnfle-9hWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بااعلام باشگاه استقلال؛ رامین رضاییان ستاره 36 ساله آبی‌ ها بعد از 1.5 فصل حضور در این تیم جداشد. مقصدبعدی او بزودی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27159" target="_blank">📅 19:13 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27158">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mylT040P_f6prCXpJX3P99zTYiQCT3klEDgQwV4akUhnxaluWuXrsj85-bQ8Cn14mX1IFR3YdbNn4Lb49Aq9au-USERRIgRSFLqIzdsjbPy0Jisnz3n5ZfxnFs6MNS022IPIJ8K-SakLpjiB5ooCIawL5weV_ggHiOvb3jzP6UOtiX1WqiLQr-IaUgsbhSiEAlN1tPQMswpNgScKCFCx7vGo-Csy77ma6T9CRnuzbrIqSDylWOunvtcHBVdLxS_9yN-i-fUNhYD9W6jbhWRVEOaYA4Pk9VMh5xnZV4fE1XhSryZzls9S_D5UcexwPNneXkZK1N9KrFoQfm1jJQKMfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ امید عالیشاه کاپیتان سابق پرسپولیس باعقدقراردادی 1+1 ساله رسما به تیم گلگهر سیرجان پیوست و شاگرد سید مهدی رحمتی در این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27158" target="_blank">📅 18:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27157">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ToFP031Ikh_m7KSQGopUT0FBO68R-tDwBXK9Dfo6tB913h6zX78zuaq_iF7OBSjjIgcbFfovE-4audo22XxrGc6mKsJYJvfVviY887gtWgpMyDsY4cknJX6vC95RVaE7KQN8rIIxUCnyyyIDW38JQyz7NDIXQukFEOfYGh3jSEdjfTzzyx0zfozQzI4LE1pF_tSwtAqIKheflS-MvwnK6EJKGRt6hrq2eKoWI2GsdHB14qz9AVkX5agPLnFBFs2xJJrchhIQeSTmtWN9Iu0cOCimRKCOoQ7TLi-POtJN1OGuAuHf6beGJxbVT-x1RjtWUvSSFIMzM2MwmXG-C1B90A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
خوزه فلیکس دیاز: مدیر ورزشی آرسنال به اعضای این تیم قول داده کارهای انتقال وینیسیوس جونیور به این تیم در حال نهایی شدن است و این بازیکن فصل بعد قطعا در آرسنال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/27157" target="_blank">📅 18:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27156">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BT9RLvw1mF5so-ypUsbGHFP5GmDz5GlI8b6TmLVYDbDH2mNyWN7aoxWXz1XLHMsxGdnHVMx4E86CvBfc0A-hk-Q3sbcVIECQcScdpfKoSUj0g03aVoWJVgDVptPrGf1IAPD5XwWuLOP5tKTeuqAgX1qeluO0hbdOszRRG8aEQV6vF24iujXDX_lJ60RYKaWlIS35IUtROCgQ0jSyY5JPUwH2rWAztg4yRCrYlc880GLq6bBs1sV4LKOrXGSJEZLJdDDomvaYNbthRVMX1MTMtnISeCtdf7Cq_76Cw3xMnq3GZrTaj4bQMKhiyDk5kh5XBYk9B73culuVAgH9sffc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعد از کش‌وقوس‌های فراوان؛ امید عالیشاه برای عقد قراردادی دو ساله با تیم گل گهر سیرجان با مدیریت این باشگاه به توافق نهایی رسید و بزودی از او رونمایی خواهندکرد. بعد از اخباری و گودرزی این سومین خرید گل‌گهری‌ها بود که سید مهدی رحمتی شخصا با بازیکن مدنظرش…</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/27156" target="_blank">📅 17:50 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27155">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITh8KjcJUu9qOKpV7ym3MWwR23xxMiZu83NvCyGh9nizmNKtK9BZj2S3ppFC0Z5Te3R0pB4jWKW48Oa37o1Zwl-qjWMsUC506vyv3fCDwjFONhlqpNuHB5UWW1962sHujwTVLqBanvsEBv29xZ4_zZAna3aqGMyPj2Ye8auIsnOSoHVpt3pw_jmniREF3BJhiqHfbwEIixw2USsovAPfdG37M5pPnqet_gd2FI8Zrgj4yFk81spLJ_PScGSDjsQHMG6fmHEcYHlZUvmHtsDaTr0kUKQdTttGL0A3KTw1z77qoDY7mW6zy3Z12fXW3KEVNY4oKWYg7xVNQyFj2cN4vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛ امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/27155" target="_blank">📅 17:37 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27154">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F4LFu_JNrj-L4auhMasA-YKIS6XROGekPkT5vuetmUua-X6qqXPA798MhSykBoA4qgfrsQGrkJDuvOnRac8NkqmEP_7hOfAXr3kTHn9dLnMuKhYV6-ryQCcOYd95xpLGA2LdanGZYez2CzPqUbmOBkpy63qMJW-EAioJF0A1R0xLItyeEEurIODzxiRF9uQ7VkQuyGTVveog_EQPMAz2KDdoy5gVL5k8k6YosOfQtfEuK40A7oYjmfVEUxcpAHoegs-O7ca5yIdNyvnNcVulLjHcrJZP0QfDj-rFZKNEHqUuLAOujb0B9kuRr3S4HEm0aFtw2QzUumvbgVTXOh7vsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مدیررسانه‌ای‌باشگاه‌ماخاچ‌قلعه: ایرانی‌ها با کامنت‌های پرشماری‌که در اینستاگرام برامون داشتند حقیقتا دهنمون رو سرویس کردند‌. هر باشگاهی که با ما به توافق‌مالی برسد و حسین نژاد نیز راضی به این انتقال شود این بازیکن رو به اون باشگاه میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/27154" target="_blank">📅 17:23 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27153">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b7185f121.mp4?token=rGok9M0MeRLQHf9hnxpzm15qvUg8nq03DXhJLRrYfuJWeJkDmTAuNc7caf9oTsTedQB-pMrF3D1Wa2ggHGNnjuY9ZysShymTKrPoFiD_W30JjCvqqqP0PqXamgiEWU2PjCzbNvpZOk8vDJQXCzQQKqw51EDKyIgv1pUeyF1i8iuDEHteN_qeEplRn1Ta496naCJP0KrCMjgDNCJJtInj-w0DBqWwjOcz0K1r3F2YioCJ7lYRGWhlOqUTA9o8FEPowmlCCUm7wgiNdp4IrbxHMSuBJdrcN_EeHt2sL3N_eERU0Vy8xIb5kI978bFrTW44HZuiughK0V6fb3bS61-xSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتیجه‌دو دیداردوستانه‌امروز درتور پیش فصل؛ توقف شاگردان‌آموریم مقابل‌افعی‌ها و پیروزی راحت سیتیزن‌هامقابل‌کره‌ای‌ها در دوران پسا پپ گواردیولا!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/27153" target="_blank">📅 17:04 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27152">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cs4W0y1Q2XkgcCWujiwjapIAskiKC49QMX7I9GNuTEiRHbYaT0x8PO2EHrp2F0KrBTsd6vEOJl8uvHYCnXoUKeW4sj2j6cwpJQ0XQ58CtTmW-X2GkFzX9J9mVp_k_Vw4VGhzWD80gnWjVuQYC1x0kUiiJVv_deKYWJl5HBJWMljVoc7x2pKiDZhBK_wO6cqqan8qGgwJAadZk6wRJDv2NBBA44Mh9Ul3hFp6qP7ZGwivYP81vqsfXzb-RMpXDTvj4kZKV--qtUJn4n0_5MWN0xvEr9dgpUYlo9DUMzigDwfV6Tx0ZB6ne0la-igMHqovQedVuyKAhFuCwn7YdtB49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/27152" target="_blank">📅 16:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27151">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D6UYbGC5aYcIgfjwGZA1078-Vs_gqioUcWfchMaugKRP69ziWnYPks-HieWuoxAHm9CDgSI8mTbmVKcD5kWEbc-YyxcEnCwUu8xh2iiCwMiLnrG_JrQfOAL71nA_gbkSLYCYbVxtwdE4PdmJxe-D_StSbTDsypQjsfkc-GLUp0QDuYEk4UoCiTn4MaUmBY06fj6hGMbscXFaZrJYRS6LOxTkqnzjD_vb_SaQDUMqgQEthRDkCNHXjjwTQ4db1CFoHczQh6tLXeUEPPv8liEW_Zy1cAZQFnEx2xx9Y3JeQ7WBJs2LvhLxhlcQzYmrdp6QJWUst13g23AhQFjc9HAlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇪🇸
#تکمیلی؛ امروز سرنوشت وینیسیوس جونیور در رئال‌مادرید و پرونده انتقال خولیان آلوارز به‌بارسلونا تاحدود خیلی زیادی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/27151" target="_blank">📅 16:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27150">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0d917f67b.mp4?token=QKmG589GxwyvpMfxFC4oZ42PWgnWncNDBZspw2pYdlSDjKrgeoELwU_dTtY4r5H7hA8u0lHN8m1YhKM_lFXVLiMTwMZ3E_k38yK62bd0Yq4iz1XTQs8O9aGtgd5ZTlyXJt7cAWYDJ_yTMtGMz9m2gicbyicUrbnTY3Bzc9a7kNE1PEq9Gs-zQCoyl29efk2vUjdvsGBx9Hm9chAeyELoUpCqJGgSwpxmu0h38bCTtRPD00ON2M5AD3bLhjA0Q40SJd9UmjiIOOaU8_tdeGxahB1NWSdLcCm9YunzOnToiuGv4F4fAikr8y0hWl_2eyTh3qhsZeFP34U0MaMq8d98gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
🔥
فقط و فقط ۱۱ روز تا شروع بهترین لیگ دنیا و رقابت‌جذاب تارتتا و سهرابیولا مونده؛ برنامه دیدارهای هفته اول رقابتای لیگ برتر خلیج فارس!
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/27150" target="_blank">📅 16:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27149">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sve9nRhjqYllKCS8UK_QQnDviBqYnDR2mQmDAiMeDKBS9VsQsucLfa24w-2FbrGZjOAFJ_6KyKF9wu6UZsr9Lc4mcBCk3pNDbY05KMGAA5681Da4oDtdqr-J0gv4p9zooMkNd0qQjKN9CGTMYfcKfCv5-nHszZqS9JirG99GclZLFU36SKMi-iZfcuPZxRDIQhTuHWT9C-DaE5TrkVyxemupKhbYWI9iko__45e5ANBN6bAaoGeMOVFsrE5psKqQ9OtuQNXf6uV786uVJfbcr1L7nqOF2B7YRR_qpuLcgZ5SYEp6rBAeQjXkme91C5TUPVk33w1wFV0OOitFrCEt8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
چه خبرهه زیر این پست محمد جواد حسین نژاد؛ استقلالی‌ها میگن بیا استقلال، پرسپولیسی‌ ها میگن بیا باشگاه‌ پرسپولیس... اون‌ ویدیو هم فن پیج‌هاش ساختند. انصافا شاه ماهی نقل و انتقالاته. هر تیمی بگیردش برد بزرگی کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27149" target="_blank">📅 16:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27148">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/315f795088.mp4?token=LDuvncOfWTY32MvH14AdeqjgaDyOVX6eIyuzqyPh-w5YGfdWSAHi07SWXJD1bTRKuWFHdoTPqwlZddXdMEEmfU4ji4PUY5S0Sv3hbp6lyQGNsCsqotZv6ZHP1XKIknaixVygvccpv1VhPmvWvtdnMWsiYm3_OAE2l44EdDkAP2JX2zS6Bp_9umg_Q4CmiZQAqICjQRZ9tA7O0V9sNhoS4SFjc9gEpIpGF9h7AIanuR_pw94dp3uunLs0PzhrFt8s3gEbSjM1JTry8fYfq5EnRz3145BPjx2P5-34KxFmt1PdKCgKYY3s4h-feJG9hd1kwK9y6T2zePxFtz7jMBJ6KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
امید عالیشاه کاپیتان سابق پرسپولیس بعد از یه‌ دور مذاکره با سپاهان، فولاد و ذوب آهن حالا با مدیران صنعت‌نفت آبادان نیز درحال مذاکره هست و هر تیمی‌ رقم بالاتری پیشنهاد بدهد قرارداد میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27148" target="_blank">📅 16:02 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27147">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aee60bdfdc.mp4?token=HwUa68fQeTGecnGMhZbgSc00WR3YcPHZ9ujX7AknxT9jhhO5-cy7iHpFdSQaZfYwY02N1Vk7_Vr11CjaV8eNlX35abETAyXjUvs_w85LoVPvSNcLvOGtas75-D9xqLcZ9rbh4mGvmM1uHl1Yxp802jwElJAvJ0kWHWL0ocobyDRpAlFfXbCdrysbSnW-9S4NlMqalzpORkk-F1PHHcZ3gp_0Ei92oVTMhhBicssffFgFH59KnQj2_FSiH-JQl2_q-wv3n5VwNfG6hbn_3nRODhyKiBmuB5MNEnI3u4hOpX3VosiT4EUTxjMCKA2mgnV_ubXD_zS22spPYl9xsQ6qvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
توضیحاتی‌جالب‌درباره‌پست‌جدید کریستیانو رونالدو در کنار ماشین های لوکس و گرانقیمت خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/27147" target="_blank">📅 15:46 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27146">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXsEFp6vSrYgwqJEua7GLndI6VnuCYZZx7Pb1Udd5ASz-PZa66nZ7KqUeHKoq0aaRxMhs1K_9yKXARzRdXFdegAlyDciTrpgQPOvvZun7hlMDZswBVC5kgQ3husROCuDlE_h8y6vtmDc1ftLiUsHtCsZVH54ldEZKg6MHpP81Yzkrr25XvYGsM8p0pBDtFvuY9sDqdsd_4BNqGgyasLhvudRAiTkLZNnZUgpxAQU7QqbvcZFGK9VouwwHKtf0pwOKou8OQEh5_QMSoWumUvDEsfPO7V7zzpjY6Ji6cdEeVhkEGOOz-bTke1jrjXSpb0_BOXd04oWR2mZrKTIu_m9CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
فرشیدباقری بادریافت14میلیاردتومان از پیکان قرار دادش رو با خودروسازان یه ساله تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/27146" target="_blank">📅 14:56 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27145">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMLlCyhnSe8-iuKqe-zbCmeuNw3dY-QcGmx1voVXU9lNmSU37Avc5KL1LLrqVj5Y4t9pfJtte4KNV_5NV9bwsHgdcSfFbODjZSXFYOxXxciMgRQZsAkljun1KVnvwmhhZldf4x52tYWlRkefSgrcJGYSxA6O9RSWE2cMfJZ-ydTocjQGHT0pnCvl2ufpCcMuC8g_U_6kRaaBeIiRwh33mgC8X6NCDv6sBfZNHDJaahxzXIlH08Gpd-IRP2VEbfwCNxCDpcr2iYHhVE_rr-WVrmh_jxN09yJXS4xbCXBAwYZYEEsFtZ9eYw4Z9pCW_A-xRKjouvurGhKmL54sLLb13g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق‌شنیده‌های رسانه پرشیانا؛
امیر هوشنگ سعادتی مدیربرنامه‌های رامین‌رضاییان این بازیکن رو به مدیریت باشگاه سپاهان پیشنهاد داده و مدیرعامل طلایی پوشان اعلام کرده در صورت موافقت محرم نوید کیا آماده عقد قرارداد با این بازیکن هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/27145" target="_blank">📅 14:48 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27144">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/09ea3c3b07.mp4?token=k4AMYJqc7qjn1jUPJgeWZEqmSEhtWBwySd1s2fV8T9LzKylHFhGgXlypFKTMa1pwqdr7PQnXKYCPrtWf1knF_f4pofp4SY5uRh6s5VAeFmIjFAPA_9moiZcH8vP3pKqdKlD8HcJYGoL034RG2Yjh0OS2n4ibIZSonmKCMQ9lVTBDim9yTh7Mh8pi0E06Xo0VL38fSk7DSP2i198ChJgbo9OggEmzF9TdNZcmFbgh7E_YYttpbEWmyyVS81GTbPWVZo5ioJjvixQjShME8xI90uztymxtw4WqjIbBBxEwiwoshfKV9sCFBLyMstEG_OSPSOrlgSfbDpMpW-Ul43lkp6nQOPdZM_wn-WPPyb_WlmIyxLALu6WH5egDP9MwuMogIwOFSktSSwHe4KMDt3xwDcgKhej4h4sSGNjtmOYB-Iy2N-g7X6xXHc2lzYq-pH_eD804O4MV2OEsDsZMC1MYOiaQxw2-XBgiW59rFDaIhQXJke19e9aFz59UowzEUD2x87yLfhvQ0T2hyFEVwlR2O3cJr7MhFEDcH2iOAPZapVFB_v9oMxSz6Tv_Tuh3OGZRHyczY9oFHjdbXtmyZ4673PKLFvwzfAI7k9aQCNQngySGTJ3Zr-Vw0UJDHHz4BhdrLjUQcJGqxkJ4S4YPEkz_lGsviVs7-YOvmH24F87yjio" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به‌بهانه جدایی رامین رضاییان از استقلال نگاهی بیندازیم به لحظاتی‌که این بازیکن در این تیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/27144" target="_blank">📅 14:43 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27143">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7uvKktxfBFGZEWI1SVoKk3CkPZWix_tCn7xaYxmVYSS6dhfUODwQWSbDWgNNDfTWFrbgHNVJ2fhYdQ6wcCKo4FidSuUsvm3kaiSLaJ0SHFzp1lSUTVMpkvEBq7FO2GzGTAHZvm8TgrI3AnDpt8UI5CVEd1MMGvuOBN8NUMWGxn3dl-5_ssVb4I9w0ocndjMlrIkcE45qWfE9BVM7ckpyCK8F7yrSAK2QxLlzTTchWAz1n3rcuykmm8nTVvCb6f4ZXZPOUnU33Mu2BS1ejzl8ctmu6-1LxhRE8QQq2blmh9m5giDQcWSJHdc5mRLERl3WMnFsQdkXlGoQUni3wGPlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27143" target="_blank">📅 14:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27142">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
اولش یه لحظه فکر کردم وحید امیری رو برده اون بالا؛ لامصب ته چهرش کپی وحید امیریه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27142" target="_blank">📅 13:35 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27141">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=uqVWvnUhLR-eVpl1k6ZUU-VxQXK2QX6znCAOfOni_pV1NfoynDCtDP-LpcDHu1eQfTSWpZ9eKNvQZLKKrlQy6spCcE3zFLzBK6tGl_Jj6p4wh7T9ZpM0ZAmZuMeunsS9qDPVfZaKfkoatX1MeJotdL1wSZn25xyL_2xjzWYFOE3hbCLAfc5yqTh2wMPUX4YF52e7GXX5rSz-iP_VgBXuv6zHU_P3t45ZLoMILNlp_NXJE_rxpj-dqhqNTC3HVk_qUA5MPI3WeU2MOiarMhg-H8VPfiUqdNLu1Y_G3vkKijcv3CfNpmW3MNqRMrLglD96BlZzEa12S2FuYe89lq1cPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/590b770d9f.mp4?token=uqVWvnUhLR-eVpl1k6ZUU-VxQXK2QX6znCAOfOni_pV1NfoynDCtDP-LpcDHu1eQfTSWpZ9eKNvQZLKKrlQy6spCcE3zFLzBK6tGl_Jj6p4wh7T9ZpM0ZAmZuMeunsS9qDPVfZaKfkoatX1MeJotdL1wSZn25xyL_2xjzWYFOE3hbCLAfc5yqTh2wMPUX4YF52e7GXX5rSz-iP_VgBXuv6zHU_P3t45ZLoMILNlp_NXJE_rxpj-dqhqNTC3HVk_qUA5MPI3WeU2MOiarMhg-H8VPfiUqdNLu1Y_G3vkKijcv3CfNpmW3MNqRMrLglD96BlZzEa12S2FuYe89lq1cPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
ویدیویی‌زیبا بمناسبت درگذشت فرانکو بارسی اسطوره تاریخی باشگاه آث میلان و فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27141" target="_blank">📅 13:25 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27140">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇪🇸
🇨🇮
ویدیویی‌جالب‌ازگذشته سخت و درد ناک یان دیومانده ستاره 19 ساله و جدید باشگاه رئال‌مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27140" target="_blank">📅 12:45 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27139">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e46D1h5xZ6XD9fInusUgtuaQBTsG8jy1UQm6s1TMe5OxzEIemInee5yJ93X-CzzHxubyvLQRihttSI9IwoCzO4-yIY2SwvQKV10bK_OKlvj8yKoXreXpCP2J6Xg0t_F4R9osP7KzHLZg64npxrBfY-SrzJQCmX0be4SRi4gK8QajQMdSn8ddlMDp4agCNY_20PgLq1h54R9b9pLzrew0tNz43inFBK3g9vQ36z5mERo6StnGy5WfcKEBCHGh_Smu7_sznWB0XGK0fbl8aKtZ3qjOpLgRwH234_LzmpdU_yha6Jt2c_eR6sHvrE0lgS7auxbLd8-FEL8AIyfWWMvneg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#نقل‌وانتقالات|فابریزیو رومانو: با صلاح دید کادرفنی رئال مادرید؛ فرانکو ماسانتوئونو ستاره آرژانتینی رئالی‌ها در ژانویه قرضی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/27139" target="_blank">📅 12:20 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27138">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upN7g5NhsijRwuzP5eypNgIiMOC9K5pNTm6gYKTy3xOKzIVef7tiPvdXBzod2j0Rl9sQNOAz4nbq0izcR4bb3rVboi8-HbbjWF62vsawwmkB7Dbe6GicBnFxq4VNbIxbayPuF1L31Ddax_DvLeZibZzf3nnw2vvaAvhSzANBgs00SXhg0-6LGnbjOz6YFoxseFWCgOiv5LLpNdG_UzeqZSwST--V33oD5kDjkJVhkbCV5bfiN0GGvwVC-f9i8y1pjrs5T510Q5LYrrUD7bcIS_ez2y3obm-v2FkfzVnj_DkrIl7FVhlkm4nnv9BO5pQuCYzZMsknn9GvuEo_fdGnKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/27138" target="_blank">📅 12:06 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27137">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNWWy0SATzYBYexkkdcuLGeC7jtm2eC2Ai8US4pKIJKu_p_JFxgkmWcREXPWSRzS3QOZhnZRdkGBJ73ZqhbazhhK1wCYWVnQGToVVgBsOanBjyb_IXyMble1BF9bSOExSyC1jlLdS-gO7FluwpERiY4kGd3CL6nenKpwXqCgQF2hMBKumq-5BRbKGDPqy8bYQzbKl6Crj1cbqJwMD3KmOLdEV6pNR9hhToxjem-BG1TEb-6B-Yv3CfQKfFRXNjY4M5Yw3JpOLYOkXU3WmAc22pjtABbdHDE8YOTrzF18YPE_eDrfX93GUG4HtfZqaz8MwW2caGA9y_tYcb5NXGJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌پرشیانا؛مدیر ورزشی ماخاچ‌قلعه به‌مدیربرنامه‌های محمد جواد حسین نژاد اعلام کرده که تصمیم این باشگاه برای فروش حسین نژاد قطعیه. هر باشگاهی دومیلیون‌یورو بدهد و خودِ حسین نژاد هم راضی باشه این انتقال انجام میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/27137" target="_blank">📅 11:49 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27136">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca19ec3ee1.mp4?token=Xd8K7G3H1Ix1vMUGu5e3Llcekp6-df-ffc1BR4We-w-mbkVaaSQ80xJAHp5q0k0yneo6S5uyFO6xXKhyocaRSRMxQExiKUaKmQiqrCPnsEhTjpAWPiviwW0eixGtTxiZ5ujAHKITdxiWGcSIPq5cRmkGJqsMcMdhq69CrrTr_LYBBRif2ILV1RDpsMulf9Zc3EezAQaRxC95mWmTynwJr8Sj1_oDM-LSSpoJCZOPnpeqyV8i_kmKfKU8kxmuKsDEcapTCYB3kWC9PfaxpS4AHBF0vf47Lvt3uZkn4W6Xpy9l9OMy1ERJG-hZAcjtsWpCabaIsMCMeBdkbhc4Ix-I0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/27136" target="_blank">📅 11:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27135">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WzLP6MXzVGAXytmgqIxswZPNU70ilDH3LW-1nsVmZYwQGPBJQx9--IkA-cEnqj366iA9hEd7fxCwAL_6-O_Votjl9jq4q60x-SGGzpUtMRlNermPIFgZ_iz5I4-FEckMDFYWCyFMkrZDBN_4mUL99t25A4uIojVkoS5z6uWmgSqqKUQkuVPG1QFGDRqneE9DibECH7WwMXPFt4gSSrgaL3a5JvypEjcNUk0tsjHQFiVI_cdE8w-x6icO15KmIALsiYeBjqij45eiTrzSB1S-WVgZAGWpdrt_tfrFrjrUH_1KwoeKebugWJhMEADL3F3nyfKfiSDfcA4RL5Sg08g6DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1ef6701e2.mp4?token=WzLP6MXzVGAXytmgqIxswZPNU70ilDH3LW-1nsVmZYwQGPBJQx9--IkA-cEnqj366iA9hEd7fxCwAL_6-O_Votjl9jq4q60x-SGGzpUtMRlNermPIFgZ_iz5I4-FEckMDFYWCyFMkrZDBN_4mUL99t25A4uIojVkoS5z6uWmgSqqKUQkuVPG1QFGDRqneE9DibECH7WwMXPFt4gSSrgaL3a5JvypEjcNUk0tsjHQFiVI_cdE8w-x6icO15KmIALsiYeBjqij45eiTrzSB1S-WVgZAGWpdrt_tfrFrjrUH_1KwoeKebugWJhMEADL3F3nyfKfiSDfcA4RL5Sg08g6DDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/27135" target="_blank">📅 11:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27134">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMM7X8wCgTx4Cjn_EU1iCvBYJ2g1LOXyhdXs3zmLyPl-nzJuNlJOXzHEdcLAqa6o2LklHTRflCp4_5u1ntZQgR8yNy0IDy1jaKVRD3cVEmaFVlIvoFUrUaFqQlh8L6FBoquwMXnzEsX7ANaPIXZ9COyxzqD9g28J3TzrGS4ZtAMS9P1J4Mj5SgaZS8FmpjQXI92eGc26OuLrVIm8-rogJpszTzTSEv7FMa-TUX1ilqUzhsMDwdY7gqgHP1XFEXdlH0AVma4hCbpZ4kT4qbfMD7ouspZGEDhTkBliKTpSZr7tG-Cd1w6WXuwfpT5jIHUuGEHr7HIF6m6J52LEq1fSjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚫️
🔴
🇧🇷
باشگاه نیوکاسل پیوستن برونو گیمارش ستاره برزیلی خود به آرسنال در ازای دریافت 93 میلیون یورو ناقابل از توپچی ها رو تایید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/27134" target="_blank">📅 10:59 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27133">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c293e9daff.mp4?token=EEiqmYuMJzUCQ_-3RRT9JyxAdCPBQjky5OTSThapb9spBthYirQkSA_jEjs6Duv0w_npUNzy8Nyied6ZHCkvj_9yZ6anFh7FP4bFBDIrCDsVQxBdbSWaZOuklGa_tR4vAKJdX2BCzpPeC-zOaRsJ3d8ZzsIE-ldQZXBwhemSQdpOczpS6S1SnELKm5Is1vUMZ5qwdnUfskXcHlRf8hfFu4WlLuPGag9vEbpZIgv_xqwT8WQJRywsvGAhFpJ3-OFESn2arNSueCny7J3_IgX2XdbSs7NNoS0SK9RGZFXXQueZDHpuSg6AT5d9hi2cvMJNNFpoLTCyD-LQNJR3Mn4Yfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
واکنش‌تند رئیس باشگاه رمو پس از رفتار نیمار و حذف تیمش توسط سانتوس در جام حذفی برزیل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/27133" target="_blank">📅 10:42 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27132">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mRg7RMSl48oCtrspFKRvh_qUNdNjiC5LRaXjlu8M_-T4vRPtstxnoQJAUgxDOtTtaobiSCVtrsrRsnNL5EOgvo-UoRRlxnSZMzFWVcIlq2aFRz6P1vKnwMEACKqUd9foBYCna1_D4R4uiKAraK7uH1UmK4ajw-IFl-DzH541p2oqSj5lZd3ubGlW3aQifo-ANTkKtdxrDNlRevC9Q9vv9RsYrNYpAFWkDVJ_qZUgfYl5mPf2qnsDZEuZW01ioJPhyttrWEQlkNRPvmjDzJh-60Tk9I10NlepWeWsxQDw7p4X-cQDryfmXKxfXOtPABJk-tM86ppbHjLfFt9PxWB8Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
🤩
با اعلام جرارد رومرو؛ دکو مدیرورزشی بارسلونا هم‌اکنون‌درمادرید بسر میبره و قصد داره که فردا بامدیربرنامه‌های‌ خولیان‌آلوارز جلسه مهمی بزاره تاراهی‌برای پیوستن‌این‌بازیکن به بارسا پیدا کنند. چند روز پیش مدیران باشگاه اتلتیکو گفتن آلوارز خودش رو هم بکشه…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/27132" target="_blank">📅 10:29 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27131">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl0dvr8zD-3uvR0nWwfvi5HAdNjqg43yfHOkkOyVM4o1vXDe23MMnQqfxlg8TGOdj97iGEqTNL_jw0iVaZf7_t0k-inE3DReKLuhr8cY_POKVx7ACPKNV1cBpTyfEsXTvgqKhzVDa64ASd2d5AnC0lFdJ7E5LpkYsFrGeInPOxIrV9n-RSsLHkWmSVFSMr7uqLhllA13qODGdJYsgjoEiiWVPZGB-32CuXY1cluFWWxmu4sjDrC23eU-miDTj--K9cvxjs1AzUSYaC_74I8M1NK_f0f9cMFTMdhb0fnGluPeedfTUYU_LkayT9mYKfpT0n2AEDQVowN_pYuQnhD_SQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27131" target="_blank">📅 10:21 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27130">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsbF6QW-wToEdGUsczpx7lARMfCsQQe0R8pTbKoBmIpO9yWb0MooCvST8LjnzmSYGRX3wIN9XxTrsQ7jJUqx88YgumXeWfvrxCgjulayAr2zIa47p8P7avjZjIPm9-YB6vkwVTxx6lm8uHfbgGmhq3Zf3uKxY4z4aHcTrt8w6igCaACz4o4oDSPxS67n6IxAjkVWx5MeUh54ZCIPkFkgmuEs4G0xyL6uCGxkvgZrqLO8aX1wgCOESrdAYAKTvzMTasGBSGZGKhzsunYgAlo9r2xKkQwH2UwK2chYIuLN2VTIuPbiB89hxGPdpRkIe9PcM__GuboBMuY8Qv1VGe1eVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
درحالی‌تموم‌اخبار این روزهای نقل و انتقالات شده انتقال وینیسیوس به آرسنال؛ ستاره برزیلی رئال مادرید بی توجه به این اخبار با دوست دخترش در تعطیلات به سر میبرد و در حال عشق و حاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27130" target="_blank">📅 02:09 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27129">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/un2AA-U6n7auEfQbS3_-7FAVjwpoVmSp0KoLxmxsar-1BA57PPoYRjm2lY70eleqTPrGb6APd5Q300qGsKkUdyp2I7ufOkaLUuipnnCPukSSWuaWMrKAFRYBeKctOiBi_gKrs2pODJCmwYRVzwI0sRLcA1wJXXUtdOM9G0mP3UrFbKqhKDHq-nHMxvBrfWkcYz1-GFwPPKMUOVUrjRvFJRAXZ5xE0rblOPRCZJoi7wycwwt0inytkh6okoAeID-SrU40N-3Blg2HTY-nCp4vPr7L0bReClxdq1X9OExyeRb_MXBa2JwhNFocsgGcpyl9GEYzfl0ciybZcRMXMu5Syg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ بهترین‌و‌باکیفیت ترین ابزارهای هوش مصنوعی که از همه آن‌ها رایگان میشه استفاده کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/27129" target="_blank">📅 01:41 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27127">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I1HJXV8RKIp5B1S8lBGvNhXzncB_xNYhgO2lXVzeC7QFZYdNiIK0boSI_dC4I0d9o3yQVqb_VHBsSjtl0ZiOasCKHLs3zlZAfgNbnbUPyPjhCiXihD7dH00ChxxdU_gOZuV5nnrh-fkvCq55w2fAHaLQ6dsvEN8GFtJTnDYNsmNx0JAsaHTfQ6KqJp2wAx8GCm7jlzcodbaErEsPL5pV19-oubLv0tmoRu4PCHUHFfoTmUdRPqbIcgvdLVEV6zfViHk8QO8RlrcA58N-R6O7ZgN18oxes7KxMAvdYXBxguoWkuvK-ngO6MqsF0jkAyfr-AYF-h7uunxXQFKXcVU1uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌امروز؛
ازدربی‌دوستانه دلامادونینا تا دوئل شاگردان ژابی و اسپالتی در کشور هنگ کنگ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27127" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27126">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw4l1sqBvaghEnM1n5J4Pm9RAF2AZtLSUrYUmsALah5-jV9nXxUE5cS65E4xBphDrMW2vqj0KyVJRNu1zb9atrCNS22wd7PkkZ4UDu179WlUpNGxXG60hvAxR5JHHRIcleSACkRIXzHr9YpMcJS5S8us7dzrnCP-q581pJcWeym9vvDPfW2hmEw0ZbU_Gd6KPoVt9AA0Zb18CekVB2SEaRa3T8tDGyP-Dd12C3UPFh8YhVlu-HVfEiUb05Y-3NfHj3XVOCTk6MnDAqVy1lyAw_esxqhhGqW7aVYapwYIJbStttsvRM7_tDCti6qeCBQCPrq6jDG9M2A0x91lS5GrZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
از باخت ماخاچ‌ قلعه با حسین‌ نژاد تا برتری بایرن و رم در بازی‌های دوستانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/27126" target="_blank">📅 01:36 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27124">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EqwfPnQAiTYLWODoMwg9Nd-Xfm1rsqAbkGM_WgwJOeDXrrFurdsxVCgh0YaDqkNijjt2MgEQBvVZZC5NlmLsNhSA1U077VoVImZog4vvcmEqS_VWdrN3D6fF4Glmykq2tZCAO7iqpEmcyTDK_9eSUMA7heIe5h7UQfoweL-exB1Riwker_d6VzBcoyAujfTpnlaNC76XIPdu1TIDuUEklfMbfoEANul9ax1lxeGm9iIY60dXkpsVoimNEIf3WMi0Qnm5int4d84L939r2PAMSNXuaGfBmtXnWSjmvxIBxRv1p4WN51Pdm6rpIvMCMDn0ryY_Hu8ZEuNQva3Qxa-fNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
تموم‌ شد؛ صلاح رفت سوپرلیگ ترکیه! با اعلام فابریزیو رومانو؛ محمد صلاح فوق‌ستاره مصری 34 ساله سابق لیورپول به ترابزون اسپور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/27124" target="_blank">📅 01:18 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27123">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bnZgCJ-hDuB_5JBbG-PpJCzUFeR4QHcNgu5KRd_Gak1iTnZjngnvvTyST4pUEB8hfZu5rCWswDa_t0qkoVK5Yf2Zn0bVL40nFLnYxnXSe28YXmOvnbanZeaGbE9B63qBE09_oS2u72NIeryE4InyMC0nbo_mqaGU5AVg8Cab6HyW2as9MXTNpErSLQV5Aa1vbDObBIae4BHW4kqb-_f-9suOLI2IYAGvgQD8O4VdWUw45MohUnO2EKphtmak8yEp5TwUICq49Qc0L_6Y_CWpRafKNARD1fCmB0urSQz_hRjgf9qGK-7k5L-qAGIsEJjfnrVVS8R9n8Ar0W0Y6KETKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال: مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/27123" target="_blank">📅 00:54 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27122">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cN9ge1IsHEtNqPzxeJBCVYsKoYXocCo-iPjlHerpdole2dZE6-nAXZeY51Zdc1bJixj-NJo5cWTEPyL6v7oEn_N44ajyibskqVmnFwK8G7NlNPTnUSAZglYTXwBWzRt7XggDJNgFKyjbhbd0d8B02cKrM3ER1adTW22WlZiK_mVoWdS_bRVZMSyuRrM6BUz2vS330cnokyWV8ONmYv8jzlRLRZt3YS06bFxhwLtEyZ7jTZHxAEA2noKVD8UJNkyJCtfR0XW9ZyU8Q5FTVRvU0JVMLLeDkx_YDxOsZtklNyDIPMjkHD5BouprHqc7v679ADRHN4aWziEF7E8ShLbT_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
سعیدفتاحی معاون‌ورزشی‌باشگاه استقلال: قرار شده بود امروز عصر آقای رامین رضاییان همراه‌ با مدیر برنامه‌هایش به ساختمان باشگاه مراجعه کنند تا ‌اقدامات مربوط به بازگشت او به این تیم رو انجام بدهیم اما برخلاف قولی که داده بودند عمل کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27122" target="_blank">📅 00:31 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27121">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oghhyo1Ci1cTxNkzVvwSz0n84J7KN0I8XT0V9D0PUORjj5SJNFYmwDxnDEgZKPFK12_HKjPOtGih5XA8puFh4uBHLXkL_2fLlpUaCvekjst5uzglyhEwqbCoclZSgxLWJczwP7l6yq3MlPJZFJTZSgVEHC5Rqt-FAPnAa0hWiCrshbr6uoa5VTtIChx3TYsOUgekTmqmHDeWz27vzGe8lIP9JA5W6nyWm8sNbI192s1uONgW0vzr64JN8RsFV4-GwIbFxhDOVjhPgWv6JLb5v8PXv5c7xtIKAGKrw6uH9V7rvb0WGxnHAKwXpz2vZ6PFDj4WqHy2dfROCBffEryDPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
طبق‌اعلام‌رسانه‌های ترکیه‌ای، محمد صلاح فردا ساعت 12 ظهر به‌استانبول خواهد رسید تا کار های نهایی برای عقد قرارداد نهایی با ترابزون‌اسپور انجام شود. ازطرفی‌هم رسانه های عربستانی میگن الاتحاد میخواد بارقم بالاتری هایجک کنه صلاح رو.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/27121" target="_blank">📅 00:12 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27120">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmO9QkAEg0eHRb7Z8GQ8lMCTs6-X-nMgeZ81YD-ZfzvnwHCe-kFFuXICWx1ow2GQd2tq3LiahdUuqu_Rrrj7BBmktGoiI1pc8DTkrc5Zq6kB_lvo5KdAvneU5xV4JA_sX8z-0F0zogUTTGGyrSC_eehVwrHg5Tgyie6--Cu6vCubG0WFamIrMNq7fDyAPxNtxsiCeppZOP2EEbo2wqez5ju5sycCC-ByP5cIL_84MkMhizlQj2jGVpR9H7TlEQRTKxqM8F03U770G5V1ql1bGD8L-bFxuj4cI-GJeotSx87-3JN7qjBxqDiBTA3XcZ_UPoqwSoxV8jPMPKNkm5KxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال:
مسی؟ فوق‌العاده‌ست. من به نصف دستاورد هایی که او رسیده بتونم برسم بسمه. یامال برای رسیدن به نصف دستاوردهایِ لئو‌ مسی فقط به 455 گل، 205 پاس‌گل،660 تاثیر مستقیم روی گل، 22 جام، 4 توپ طلا، 3 کفش طلا، 4 پیچپیچی، 6 قهرمانی لیگ، 2 لیگ‌قهرمانان،1 لاریوس نیاز داره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/27120" target="_blank">📅 00:11 · 14 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27118">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=Hw7sPqlrZF1xDvS6T3JudNPYAA_86q17B87lFxbbkEQF5W0LnLR10TkIE7e-hhIr2Rx4exYqEB5WKg1es2yd8XwfE4SuWwqqkmWmtm531qRhrR-lpBoHtxC6X_KwFu_u-abMuy3nRIph6oCaofKhjhQ8qAU2pukvogr3uaVcUTMYTT0v6XuA6QhNVcfYZQhddf-Zv8itZXqkikJmae3MNH7Wa8Cu8l3Hw0HAnNqHeused6roq7MZUKo-zjfJC3NKLoUsSi5Sk-0ZwdXiwjN6jlfN67XdfseAmUQskWK4-zQdQ1Ol98Vvp9_7s4uX432dfDGzjtB6CZhiv7GUiCrc9mMXL-FUu_D1rQJTRSyewBD_XwVYizc3Dz2m7ein5RXQ9kh0j1WaqnhzNARb0buiaP-kBhSXDOYGokNLl_vDSROAXnofe-DEqn9JFd8CzfgpGhXEscqpNW7P_x-UdvcfZJ8LlW097TBhCZSBVGSUBr5jCkwdwpgiu8In-wBR0PeypdG2VqQt36Q55Dn2MOp1OZvMtQIXbiCLNjULUy-FkQz89AztyyNuYpRhl2ZvNuPVlPmEMkOpP-Woqhpzgx7QClQ8CsKYpkYKz94AQR_ddQ4QflmrDZxGGn-gjTvjk4LPBNT8ZAqF2Y7aTjhzxS9DXmtrcinW-SeP4FtrjwGVBCk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a21ccb63.mp4?token=Hw7sPqlrZF1xDvS6T3JudNPYAA_86q17B87lFxbbkEQF5W0LnLR10TkIE7e-hhIr2Rx4exYqEB5WKg1es2yd8XwfE4SuWwqqkmWmtm531qRhrR-lpBoHtxC6X_KwFu_u-abMuy3nRIph6oCaofKhjhQ8qAU2pukvogr3uaVcUTMYTT0v6XuA6QhNVcfYZQhddf-Zv8itZXqkikJmae3MNH7Wa8Cu8l3Hw0HAnNqHeused6roq7MZUKo-zjfJC3NKLoUsSi5Sk-0ZwdXiwjN6jlfN67XdfseAmUQskWK4-zQdQ1Ol98Vvp9_7s4uX432dfDGzjtB6CZhiv7GUiCrc9mMXL-FUu_D1rQJTRSyewBD_XwVYizc3Dz2m7ein5RXQ9kh0j1WaqnhzNARb0buiaP-kBhSXDOYGokNLl_vDSROAXnofe-DEqn9JFd8CzfgpGhXEscqpNW7P_x-UdvcfZJ8LlW097TBhCZSBVGSUBr5jCkwdwpgiu8In-wBR0PeypdG2VqQt36Q55Dn2MOp1OZvMtQIXbiCLNjULUy-FkQz89AztyyNuYpRhl2ZvNuPVlPmEMkOpP-Woqhpzgx7QClQ8CsKYpkYKz94AQR_ddQ4QflmrDZxGGn-gjTvjk4LPBNT8ZAqF2Y7aTjhzxS9DXmtrcinW-SeP4FtrjwGVBCk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
فدراسیون‌ والیبال‌ ترکیه‌ به‌ این‌ شکل از زهرا گونش و خانواده‌اش بعداز قهرمانی در لیگ ملت‌ ها تجلیل کرد. گونش با درخشش در لیگ ملت‌ها یک تنه تیم ملی ترکیه رو قهرمان رقابت‌ها کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/27118" target="_blank">📅 23:42 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27117">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcpD4caA7ZHfaN-jW2DlIVZE-yngCkP52E6GjU7yrohbIdVfWCRdgpOHFIg1N0NKE9gZGjsPfhvRRWDb-d70xRdfZjL7ESqquWxGQiFjK1JzohD31ab4YO5ostXj0jrDtXuXO-XS3OjrjnOkBsI-5w7aTf7qQO2kMOzTbWIr8YdgoPudaZqHnoqPuF-TTw4fcJmvQR288ps2gTET27lbmHsPFNvjb2B9j8tVEdx2aKYBUkjANAFr0Prl8YFmTimbxtFi-0OaBNRs0BFXRQ6-OgNESAL6gcbmomDS3QM8Utx5ARNqx0TC14b6-mN4pA2sFS_yGDON5scytL44S5w7zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
رئیس باشگاه اتلتیکو مادرید به زبان عامیانه گفته؛ خولیان آلوارز خودشم‌بکشه نمیزاریم از اتلتیکو جدا بشه. 100 میلیون یورو که هیچی 200 میلیون یورو هم بارسا بهمون بده آلوارز رو بهشون نمیدیم. مصاحبه های آلوارز اهمیت نداره. او موندنیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27117" target="_blank">📅 23:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27116">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBtdyRi82lW4F23IHS31wL3LvR6wgi8VXgDvX5tugyF1UHiK3M50yx2WFLGHM88yPW_wkxT4ob8ZWw8t0YPCVJjQB1DQPc1dK3C0x_z6hSAPLFytrl0AgsekBe_TpXojWMdujyiZGw9gYde7GjOyr56JEzyH5kt7BBQ8VlPrQQeUO7tlILVEnUl2HILTz0NTo8QuLEmaeV4tWxB_zYQT6ZBi2WZKXlhYDEH4snQmKoMuKJgAaDU8KvSSxpt6plqKwI0ASu-cXC3HObIpENQ8lRUDLouIs1FEbJfoh6VyR7_ulfFgzPrDNmO5F-WfT-qusOgy7D_UCbulj2wMhdkbqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27116" target="_blank">📅 22:56 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27115">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52510ee628.mp4?token=HlefqiePnzUpDDRNPoZHgocDz-7EwW6D87H5qBKS2S089GsMGrNjdpdGmdy5_r3E4YVjM7udfrSpCdCGWbO-ff3pxtaN8VvxykXw32b1Ln70xGSKlDohq_CHDBlv_4RSnYvaSXAu15e8ec78su1IbuZy_XTRnGYEo7AOIKf_D5wQc_4IHPpQPhTSK3Gj-RA9eV9PHzTEK2ZVhbjBWDVFXCv6FH-85ZyepGtbgYjgPxtAAbfSMg1aG4pnkOS4nJB-tOE9Pb9gupCxjmEMym6fpzacyQq7FI9a7xFjCiosX6x5wXKXSSwJmb4EhZN1-CL7SYpnHrdNTG7KlevZCigsmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52510ee628.mp4?token=HlefqiePnzUpDDRNPoZHgocDz-7EwW6D87H5qBKS2S089GsMGrNjdpdGmdy5_r3E4YVjM7udfrSpCdCGWbO-ff3pxtaN8VvxykXw32b1Ln70xGSKlDohq_CHDBlv_4RSnYvaSXAu15e8ec78su1IbuZy_XTRnGYEo7AOIKf_D5wQc_4IHPpQPhTSK3Gj-RA9eV9PHzTEK2ZVhbjBWDVFXCv6FH-85ZyepGtbgYjgPxtAAbfSMg1aG4pnkOS4nJB-tOE9Pb9gupCxjmEMym6fpzacyQq7FI9a7xFjCiosX6x5wXKXSSwJmb4EhZN1-CL7SYpnHrdNTG7KlevZCigsmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
درمصاحبه‌جدیدخانواده‌نیمار؛همسر نیمار از قلب بزرگ او گفت؛ ازکمک‌هایی‌که حتی دور از چشم همه برای اطرافیان و گاهی حتی غریبه‌ها انجام می‌دهد.
‼️
البته ستاره واقعی این مصاحبه شیرین، شیطنت‌ های بامزه دخترکوچولوی فوق ستاره سابق بارسلونا بود که تمام مدت توجه‌ها را به خودش جلب کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27115" target="_blank">📅 22:28 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27114">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foeaVYWuzeSgDS_del6eD_a6w20dJbQo4MJOZ039YgY59UrBIWmjWsUGd_ng99T7TYWEr9mL6P3fiA5PRSbYgswEdz8CocnRNl59zKrAfJpLZbnlgWFCh5O2Ycgol2qu_asLHxGsxE4xZCYuS2emSj6Y6kvsaU0dWO4JvwhIYZKPZc9YIzYCk-DOx7-XQHHJGyofYyBgtFmjvSjsJlcSNPoO0V0lSxDZgV7LhcVwf7LMPp9cVNPk0ewkDjOUl-XWT5qKpjuY_hPhC4BvwZApe7h9DUerZPttZniI-meq1CeQ0jmdKxe_rR3VFlAQEPRPPzMXUL5nh0CZ4COaTwt9UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌انتقالات|نشریه‌ سان: سران آرسنال به درخواست میکل آرتتا به‌دنبال جذب یان کوتو مدافع راست 23 ساله دورتموند در پنجره ژانویه هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27114" target="_blank">📅 21:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27113">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/US24Hf0okaimJI8gtjQgEcT0UAcBL03ocezV_vDvf9Lj1a3pvXRIydpSV2KVowJpQLuGpALMGkciaLzMc4xtzbkmva4xSbU_3_tB2otWU1XXWgygouTSSUZVF4qwJCOm0WNkNXM1pNGL5ez-vwgMz4yCytjuiYidzvc8DPJ10ikW7FuV1x7Glj0UZqudEfhQuAHmd_zcXCByviEIyin5mbsuksRBIpCQ-jy_vFx6X4EvM30sgfONCulyctOhwSNu7blb_5E31kuX9LMWaSvboYFnbEVsERMjAP0YIKlDUW_ww1cb9gnRqXki2CqMGH3eN0Celu6LaTYolKoFvz12sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کارلوس اسپی مهاجم رئال مادرید:
الگوی من در رئال‌مادرید کریم بنزماست. میخوام با گل‌هایی که میزنم همچون او در مادرید محبوب بشم. برای دیدار مقابل بارسلونا در الکلاسیکو لحظه شماری میکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27113" target="_blank">📅 21:26 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27112">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkenzM3gJHEOmBjdOPybbMWV4euFGMpujnTtJKTiIc_FDS_MbY-eZgf7l-WiEs-LD1I5hYZuseXS-kno8_75nMFQOIrlutAIYi1gehaAGchf8uoml-KrdYZgOpwDVpm0pCut8DHTMevQWcZ1fGSnkGUSOQRFTO35c3Ph9RYx64Bs0eLlyk2zL95fhDhmArWFyo6pIo9ZbwWRJvMUrrYoDCTYTgyG-vFfnTpltTM_7sqNOrmBFwv-9peJDHa_eEusS0LbEMlJ4Si9JmXMCTapTsTqfQS_HvI2tMu79XVxM63ShXXMaFduXXWtj-43HBMK6K2ltnXE6p8C9eS0nvabZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ مدیربرنامه‌ های رامین رضاییان امروز با مدیریت باشگاه استقلال مذاکرات مثبتی بر سر رقم قرارداد این بازیکن داشته و قرارشده‌ که رامین رضاییان عصر امروز برای انجام مذاکرات نهایی و عقدقراردادجدید با باشگاه استقلال وارد ساختمان این…</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/27112" target="_blank">📅 20:50 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27111">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KybbyiepT1Z4iiYbu1b4xUQglXusjgjG5uOgjYjZIDwFl2ejA4oR6D1b7P6Q4qr59bBQ0p_MJ9ExbQduDSJL2UYnmANplkTCD52TZV1fDdKpmu2sfcKZ1PyvBTwrXYxJ4Ksc5j1e4jhMipoE9-aZtcKWlDaKyrzbZZU36z9enpIIX7g8B8C4iJ36Lr_1PThOPZfPG74wqwNknjAV9khuGY9pWFcvvFa4t-kh6Njl_TavQL6F6Mqib3aXNVWDpF4k9oWSjfgoCJZMtsMriyWSs7-6M13bBpOl9d4NFnzLI9qmiZFrPOj03wmdCfNtNBY2FzTQyIndKj6jcVAy3FDdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فابریزیو رومانو: باشگاه ترابزون اسپور ساعاتی قبل‌پیشنهادی دوساله به محمد صلاح ستاره مصری سابق لیورپول داده و منتظر پاسخ این بازیکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/27111" target="_blank">📅 20:45 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27110">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kddBI6t33BVSzw4yiTX7-q87fpgsfKVjAQpJrKUuRq7sDPF0FDihIfye65tpKC6HGwtMqL7-j7-NPv7RlpyYqwr1UA1Yil11loYY5RJM8HA4kjksHhXOMk3YEQWfn1mpMB2g0CRbpL6Fpfa5Re3A1xRCCQ3fKHk-8vocNLVICE4jSB1LR6j-RHCnchPJ1HjOKPwIHHpFIJJVRJ3QG4AxEZldkNeL4xRWgG4DokQI0h5kaItdqwBEaQwy3GVVwd9MVRGuaXAhPF1_rr-TBup5ghR3ZAKmbVJoZg3OOZ_UEA4zmF_CQHGOX7frkxoeY2zK44ktbkH7uBBoSLAjsquhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
استوری جدید آلن هلیلوویچ هافبک تهاجمی کروات سابق تیم بارسا و مدنظر باشگاه پرسپولیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/27110" target="_blank">📅 20:30 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27109">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gig7R9kV6PmXJiErCwEF0ims6LgxY7YlJ05LwNDd1RyKTprWvXNN77z5wubjq2kTBuIdwOSF1MgsD3FUC8ngTHI72FNo3zvNsDq7kZnrVgp8lelieDigxHLtvsoh_Xu-bKGrLK4KoIao9WMUYM8ofGkIRh_Nc64Fr2dcF8UQNp5953o6E33Z3fxI57JSLZNaV4EHayfG0CfDXWNqldldD3XicqB6H2m1UNLhZLPTw6YsU1bqrRlOZ1TVQPyOOM79bOUUmDYb7vFfwQixX3jiK_i1lEqUotNmunz6ZXYXSL7115vk4azJd8F3o5VsxOzy6Ch5UwRoXwJKGBr1ZJll9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27109" target="_blank">📅 20:15 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27108">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mNJrTHmSWsppw1cuXEb6ZlJEo7WFzmx6ZEcVGbB8wR2Vh5AWHkTCRu2RQfMJ_6Y9jPKShdx5yJ0I1f5LJ7t1oSZiUKCHkKh0lFeW9n2k59QXmY_7ZSlhDxrkMEjrQdnlw0Le0NMw81QqlT2CAbQCG-tGzOIj1dd2ZGLZEM0wsKFhGf-3AgOTwvuffBv3Rnv7iWDryol09uO7_kkFVu2Xiw3ENC9Q2ot4BnDBL5blM_6KtahGhzho_JfBJ6XQzI8B85kMPQ5d92pV7JrnRkepLusG01J_MaYxJmrYO_0E-MMQdqqyQOemRLpoKYk3VQhiVpty0NAmmo3fauf2PFCfDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
پاسخ‌نهایی باشگاه‌فولادخوزستان به پیشنهاد باشگاه‌پرسپولیس‌برای‌خریدابوالفضل رزاق‌پور مدافع چپ‌فولادی‌‌ها: 200 میلیاردتومان نقدبدهید تا ما هم رضایت نامه رزاق پور رو براتون صادر خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/27108" target="_blank">📅 20:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27107">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEYK452jq5H_KcO7H0v6wAHP7cDWpKdmTezbT6ii5o2QfYxs1S1MwUzWec9hYcG2QG6U-m-Qh419Uu8hyB6xhT20FgJsnm4STUGqO2pg6aOsSVV5MNwTzj0-KLNl94ENFTJQGj7sgAOPoArApt5_cRON7buBPuYeMaKNbRPIE8BmkDLQg8R-pdftkpNuWj-UJCk9fQSr6msGUb-hXRwOex2KzfdGUY2s2kk0817LFesUeaRzOfAqjYdDXKAaMIo5uaW6fsDNcB0o1VXhNTDwnYD9Fo_3GWLY4KQ7flVc344U6qDIbsHvxNYgw7IwRP7mC3xQJabZ9cQ5U3jp-8L6KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مدیربرنامه‌های علی نعمتی؛ این مدافع ملی‌پوش باباشگاه‌لوسیل‌قطر درحال انجام مذاکرات نهایی است تادرصورت‌توافق با این باشگاه قراردادی دو ساله به ارزش 850 هزار دلار امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27107" target="_blank">📅 19:27 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27106">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Ip93q_c5x6Oqrp3GvT7gy6J2pWZ5Lqshtowyt_dJWT7QHpmEGEm1El_FopNp6AqtYXxJEz0Nesnwr6NcR6Ygo29OGCb2WT_2g_Xn1y_K2fpc74NB5M8RQlX7ShxMqc1UbIw2vwEe_a-3UVKTu4pMQyvkatgoY0tuIS9FMfypSZh7wvV_A0V-UjFD575D9_iKkg6_IHbX4_RJlXKEzAMGyI1QRhHywkX-y3eW2K7E3i1ImJ6qaZrqbxoCnagFHBksSnDl6ICLtT7tPbRsWX1VX_Kkk-x70EgsRoUI-ve4TAaD2zPoODaqIdxe9jIDY6DYIga9evdspLdWaEIRDF1ETQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd6169d08e.mp4?token=Ip93q_c5x6Oqrp3GvT7gy6J2pWZ5Lqshtowyt_dJWT7QHpmEGEm1El_FopNp6AqtYXxJEz0Nesnwr6NcR6Ygo29OGCb2WT_2g_Xn1y_K2fpc74NB5M8RQlX7ShxMqc1UbIw2vwEe_a-3UVKTu4pMQyvkatgoY0tuIS9FMfypSZh7wvV_A0V-UjFD575D9_iKkg6_IHbX4_RJlXKEzAMGyI1QRhHywkX-y3eW2K7E3i1ImJ6qaZrqbxoCnagFHBksSnDl6ICLtT7tPbRsWX1VX_Kkk-x70EgsRoUI-ve4TAaD2zPoODaqIdxe9jIDY6DYIga9evdspLdWaEIRDF1ETQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پیش‌بینی عجیب احسان علیخانی که چند سال بعد به واقعیت‌تبدیل‌شد! حدود ۱۰ سال پیش، زمانی‌ که عادل‌فردوسی‌پور و محمدحسین‌میثاقی هنوز در کناریکدیگر در برنامه«نود»فعالیت میکردند، احسان علیخانی با لحنی شوخی گفت: «میثاقی رو آوردن که‌بشوننش جای فردوسی‌پور!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27106" target="_blank">📅 19:22 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27105">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTkXa3_OjKfDZCrQx8VAtHLFzg-lOD9Mj7tnTaWb3mISnyIha7kS5zhfl03xdNb0M8Ft4983MH-KczKxXxzAikjUGFPe_akWfTiNup6Eb4akqWnb84FzdCvMmqiKU3H6TXhaWfZ0n9WhdPovzj7CDfULgLATD-hVQ8Z6uQbl5MnzahdIU8FxYDr37DlNAT7faQbR3NQPieEVu59or3YMlXWNHWBtFi-JbLdk51aV0COQ8mORy8muoYTQYa8Ca1QSpS-6llVjE5khAEU8X6QPiui_dAuygIx_1lv_0aSFhfrgR9uX1mqCA3Qz1lIPsqt3aXDoN0fwNNsum864Ek1r4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
🇪🇬
سانتی‌آئونا: محمد صلاح ستاره‌مصری سابق تیم لیورپول برای‌عقدقراردادی یک‌ساله به ارزش 12 میلیون‌یورو بامدیران تیم بشیکتاش به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27105" target="_blank">📅 19:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27104">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=coSRkC_XOvWyv80BTth1G3DnqEljGYtrDxchKaMWlXBRw3f8zhf5_xdBYHZkR6KigUb4xq-mrADXqXHBNPIeHyRTPqSDHOWTRX-1dFiKP76nZy0AXw4ReSaypUvSTJ7wGl778mgKaSKK1Mts2oSmVdqwAEZlzS8p7LEAlhTR-Dh8IMXzAz9GPuNQub2K98sEzQDBFGde0KAVlK0c2sIT1mUX0i5CitUVmCUzQIHb9axrmaCmGXKCyr5-23yq3c9Ympmxs_03AjR0tDct2W_REM_6ZwtaqiI1nS6px1_FrnK28QtfLlV5VEks0nN-c7KOPNCBkfsbvsP7z5pHdREfXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe05053c48.mp4?token=coSRkC_XOvWyv80BTth1G3DnqEljGYtrDxchKaMWlXBRw3f8zhf5_xdBYHZkR6KigUb4xq-mrADXqXHBNPIeHyRTPqSDHOWTRX-1dFiKP76nZy0AXw4ReSaypUvSTJ7wGl778mgKaSKK1Mts2oSmVdqwAEZlzS8p7LEAlhTR-Dh8IMXzAz9GPuNQub2K98sEzQDBFGde0KAVlK0c2sIT1mUX0i5CitUVmCUzQIHb9axrmaCmGXKCyr5-23yq3c9Ympmxs_03AjR0tDct2W_REM_6ZwtaqiI1nS6px1_FrnK28QtfLlV5VEks0nN-c7KOPNCBkfsbvsP7z5pHdREfXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترِکپی برابر اصل نیمار جونیور!
ماوی، دختر سه‌ساله نیمار باشیطنت‌های بامزه‌اش وسط مصاحبه اجازه نداد پدرش‌راحت‌صحبت کند؛ همچنین حرکات شیرین و بازیگوشی‌های او دیشب بازتاب های زیادی در فضای مجازی داشت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27104" target="_blank">📅 17:05 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27103">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/835360d02b.mp4?token=WhRYqJ4zJo0qUJdgUEeh6rC8TBl6mK3wshaNkhxmgX0qzswt3ZL2kxE7ToEd2xWoMEikjhMpkp94iZgM_GV5kVEHPupm5v7cEBOSHR_1I-DNX2VqAR1koyKa_swQlbKmPdnhwhGhacHDXkNMK8hpaZ2PFmw9_qHCYGuvirkyY1--qPpUvUXjj6JWzwOM_EWUOvqXq-F8J-jdbBK-H383q7eP-Ypustap1gmW1CRj70gzAKwKg7aoYsALKJ325Y2AiKPsF-NyjAbG4VzYwY28jFS0txtp58LS0WLVWgyqWhizPG8fM03zTrgelJ0bsuXJRpoEDlWs78YdwDk9jK5xzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/835360d02b.mp4?token=WhRYqJ4zJo0qUJdgUEeh6rC8TBl6mK3wshaNkhxmgX0qzswt3ZL2kxE7ToEd2xWoMEikjhMpkp94iZgM_GV5kVEHPupm5v7cEBOSHR_1I-DNX2VqAR1koyKa_swQlbKmPdnhwhGhacHDXkNMK8hpaZ2PFmw9_qHCYGuvirkyY1--qPpUvUXjj6JWzwOM_EWUOvqXq-F8J-jdbBK-H383q7eP-Ypustap1gmW1CRj70gzAKwKg7aoYsALKJ325Y2AiKPsF-NyjAbG4VzYwY28jFS0txtp58LS0WLVWgyqWhizPG8fM03zTrgelJ0bsuXJRpoEDlWs78YdwDk9jK5xzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنظرم‌جذابتر از گزارشگران ماگزارش کرد در حد همین چندثانیه؛ گزارش فوق‌العاده گزارشگر زن لیگ MLS روی‌اولین‌گل‌لواندوفسکی برای شیکاگو فایر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/27103" target="_blank">📅 16:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27102">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lx17Tx6o3lTQ3JMqcB9nq_gChnZML5K0i5ya2qXOLGixdx8MqFt0LYP8lQTgOnGnZ6J2P7liEFDUfpAVUnJ0qPk-EKaZn33fvjxv4Q3XB7VvL14ZCrWt1mEX1FIHrPwRuBD7n0lMSZeg76cuMEmA_0ftyvn3FXwRBEl51qLeNKwk1w527j0SWWniVxfVRmrZDYVymz2BmO_3iv-BWhvr2taxmEaL7vVCa7e-nr2KT6i2qpZ6dgE3NW7SgqwINet9pu_Mq7HNqrl-Jfi7cFpSk01Po6GRAZ2wthyD03o8N8dq4wk8-6rqOnFobLEmEd7DMIIPVf0_4dTe5u8Myx5Erw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
رتبه‌بندی با سابقه‌ترین سرمربیان حاضر در لیگ برتر انگلیس براساس‌تعدادروزهای‌حضور مداوم روی نیمکت باشگاه فعلی‌؛ میکل آرتتا با بیش از ۲۴۰۰ روز هدایت آرسنال، با فاصله‌ای چشمگیر در صدر جدول تکیه زده است. اونا امری در رتبه دوم قرار گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27102" target="_blank">📅 16:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27101">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=RMHl2eS65MqndzX3gJveZWxxznGYeS_H9fSdC_nhNnV3T9CyoCkExIw6mrPL0Yg-m1L0x_j2RkIAfelV4BYNS7XrMo6gDxA9g75s4BwxDtrurqejNxBd1QfU1SQw_6dgfNcfGr3Hevn8poWqvsuJ3m7SfUE-oNOYhCOOAjaiNi0k33bWSuv1KpGxgvDnPR0R08C2ZuB5-WVmhdmeD8FB11B7T_nyWgNlG8beONBevZSYfC6Qrc4oD4-MumyMvxiLIMsV2ne38lYD1EJ1a0fhECpt0nGTsd8U1st2BN6ufOMihoTC8xiAW7cr5MtTRSKTVhCmlFyUtIoZ-Zijt8UneQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40f136b3eb.mp4?token=RMHl2eS65MqndzX3gJveZWxxznGYeS_H9fSdC_nhNnV3T9CyoCkExIw6mrPL0Yg-m1L0x_j2RkIAfelV4BYNS7XrMo6gDxA9g75s4BwxDtrurqejNxBd1QfU1SQw_6dgfNcfGr3Hevn8poWqvsuJ3m7SfUE-oNOYhCOOAjaiNi0k33bWSuv1KpGxgvDnPR0R08C2ZuB5-WVmhdmeD8FB11B7T_nyWgNlG8beONBevZSYfC6Qrc4oD4-MumyMvxiLIMsV2ne38lYD1EJ1a0fhECpt0nGTsd8U1st2BN6ufOMihoTC8xiAW7cr5MtTRSKTVhCmlFyUtIoZ-Zijt8UneQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو تو چند روز اخیر بیشتر از 12میلیون ویو خورده؛ رونالدو بفهمه تو ایران دارن باهاش چه تبلیغ‌هایی میسازن میاد از همه‌مون شکایت میکنه. طبق گفته رسانه های معتبر، کریستیانو رونالدو و جورجینا قراره بزودی بالاخره باهم ازدواج کنن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/27101" target="_blank">📅 15:44 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27100">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2JLXf1iiTevR3ovsh3YU2HCQdCqIZYk3mmfVeuEysgr2us5Fm23geB70BFRqeLR7uehAqkh5e57B5fb7UWk4Y3rH7Ui7doJB-b8LU_fkWmNC92QWCnXcZ7l4C8LNiZAGgXOInObZs65aVRBfvqOVTyHTAVM2rKpDswoYVqNe1VfDeFwjnNaGbmCU1dBtg_7aXDuQ-R4TDYahh5eWd8dNxrhH5puLyTnXu6Qy5Ov51Wwwy23-ddzEGJxWdPPH9CZ_8osqfKmmr6zVCvXIKnfQdPNyTqrgfQV-59lmF_Z6Qpk9N__ScYPvnunT3rEr0Eu-fcyHI0UCHx0vzeidriYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنایی که بهترین بودن ولی از تیم ملی شانس نداشتن و از داشتن یه تیم ملی خوب محروم بودن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27100" target="_blank">📅 15:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27099">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">قیمت محصولات ایران خودرو و سایپا 13مرداد
🆔
@Persiana_Newss</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/27099" target="_blank">📅 15:39 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27098">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NptsyxYkzEsS7xl0nGfYfIxujcXE_aswqsIVxppQGhHAr1M8xi7OzetwBw76kPjx19MSO_1xwTBHEVNZTmG7oFeC4Dwm6PlfdaCKBMiJoFc2GSya01tcJ3QMiN9YsQ4T-u8gZ1cm9Ib5X5rMKS8NOJ0F9eb-h4daJ4zzGx__JLTg7LhwNUv3tP81nz3TwuX_clflYC0hAwsWnPvvYfT3MpdQQ5PXxL5Qaa6y0MzX4cBeH47nNcvp79UoTeOcBQYDnF-xCdFzL7v7nqKGBM-2KhNzIO7pd6gW2-iEuQOIu0oBCTAQaPIAQ8TzLPq5dy7S6LvZ3LN1ExVqbdXxNGDsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
کاپیتان‌ های پرسپولیس در فصل جدید:
حسین کنعانی زادگان، علی علیپور و اوستون اورونوف.
🔵
کاپیتان‌های‌استقلال‌درفصل‌جدید:
روزبه چشمی، صالح حردانی و امیر محمد رزاقی نیا. البته درصورت تمدید قرارداد رسمی رامین رضاییان با آبی‌ها، رامین کاپیتان دوم آبی‌پوشان در فصل جدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27098" target="_blank">📅 15:24 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27097">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjwdOZY-u6BtEZWemFOscZtah0YhPFKLokKpT3a6wFouU23PobBnh8KR6xDU9mNl2ui5G78Pko2LMC2b4lV_Z-N4lLA6QBCZN-pE3-UgJsPRaRfRxVPZX9ZdgiKkCi-VveQEnwnEVoTpyLoloQ-fiBiebm2mIBLH4_k5xI8eHADjokt5Al7bcsxilMkeuLKrfZaNpGxvR0SQ_8iJbqNqkQa_e7UhVvn967YsKkJbnlc6i5RMWuv2D9W_kL7z_nStWFyfcRK9Sp8qu6D5NVyqJPRzRYdCS3iQYGgtr_Ap_4-WHFGxwgpB-1-770mNogFuN0qUMKwX-2iUrFnrVbsLYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟢
👤
عبدالله‌ویسی سرمربی‌ذوب‌آهن: دوست دارم کاری که‌سال 95 بااستقلال خوزستان کردم رو با ذوب‌آهن تکرارکنم. بسیارسخته‌امانشدنی نیست. امید عالیشاه مذاکراتی‌بامدیریت‌باشگاه‌داشت اما درجریان مذاکرات نیستم. امیدوارم که قرار داد منعقد بشه و این بازیکن با تجربه رو…</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/27097" target="_blank">📅 15:06 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27096">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzqCenDr1PQHjeepFaWc446r0hT6sNGHHyXy7RZg2mt9SE9SL8kjlVsH9Y9WkOUF0BNHEKgalDcO1BdYZtT91-fWKxyUYeQTC9K9eqARD1WkTK3fhv6K8xc-f4gTASU-n0x3oLjHhq7o7Q06M8bCsGYQLDvVC_qENulDEWZLa62IZ9Nw_YPAbN9EC7KY6uB8M7HLrDboxvvmAJKmPa7PPZV5gc7dlYFIFoA_4kHbKM-UiEzlsNedUNIShoUjCbyEAKGhMW-DkWssecqhpYmCTnOFQM_OMQB_fzoc-zwSZzJwqrcLq_kmcYS4M4QKJhUlRyGoTVrA4bTfUjrfHc1c9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🔴
#تکمیلی؛مدیرعامل‌ تیم پرسپولیس امروز به حمیدرضا گرشاسبی مدیرعامل فولاد خوزستان اعلام کرده حاضر است برای خرید ابوالفضل رزاق پور 120 میلیاردتومان‌پرداخت کند. گرشاسبی به حدادی اعلام کرده تلاش خواهدکردکه مطهری رو راضی کنه تا این انتفال انجام بشه. مدیریت پرسپولیس…</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/27096" target="_blank">📅 14:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27095">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSMIF-ByBkzmS-SLsbgB4G6Vs8gldOXfMvJkujIAMGdbZfSw9Mc2y79nEOuEvN-Ba_pkrfQHU2UZpqEU63O3cVU9T0hqhf-O0K15lFGSpQtK4RqywicKH-8QtRPNm_EQpJrvZQZxLMw9jxkqZBfX4IeiP8Ne4byewvTOY9pDPf3E29ZanaIvO7jSgEbWWh-8AOPQUwTeQRfpTbFHNMVRyGuTVjzO0bDEO6Clly9Ev53uGrC3i2LrYM79oVokjHITyMglMmL5L-PdNfM7FZABEcgytvSqhtZihm-7qIVbMip1ps8wdt8GRPPa6mijFCKyub2xcMZqy4bPF_qZUEfykA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی #اختصاصی‌_پرشیانا؛ آفر جدید استقلال به رامین رضاییان برای یک فصل حضور در این‌تیم 150 میلیاردتومان + 50 میلیاردتومان آپشن گل و پاس گل و قهرمانیه. رضاییان قراره ظرف 48 ساعت آینده پاسخ نهایی خود را به این آفر بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27095" target="_blank">📅 14:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27094">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGKizXpW1PljixpvbzYtAKIn7cvq8TmE3nsdjeK0E_wodDr1YpUS0qrnqmx2-pfI_lVHdwO5UmIsEvzn_hgT5ROR1QD4eh9Qj85m8g8UPFqR8f4UhItV_XR95mwq7RFyxh_6gFjn3b1UNO6jTBtX23Jwb9jXT4accEDKY_1PKNu14Xz6O8srXhJg_Esicu_YLUXV7jrp6aiJT0YhQ6RhddIxwPrFhRNdiiny5sWIpwlbNxyutUbgbavMdYRppZXcNmxe6rWGcpSx8CUsFLp8vxtNCeqkmOke2RqT06EAksExEROGvG2D3GmGxksNZMwzc8fwI-WX6x90UuM0O8xo_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
عملکرد نیمار جونیور فوق ستاره سابق بارسا و PSG در کل دوران حرفه ایش در مستطیل سبز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/persiana_Soccer/27094" target="_blank">📅 13:43 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27093">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stSxu_ahye2JRP7xbKRS_H7GimD7GEjawppPihYRRD2VTIttjksNUO9KGWVhLNh-EGVebkrGofFqba7Cz63j7uXe10HJiM8nvU5R-MONhUVX-Iou5SqFz-QZA329IkclIa2jDXDtVxA00U1E_VcIumDg7gey40Rp2MEpYEsC091jzS9r_G3FCH_GexuSuUzFVvpbI8zA5Yi8Pdw42gv0-dpebAl7jLSFBtacAYP3N59_VJm8jgic3_BF5Se_uIFT5NPLkUASL_0CSixEpySncpcYaD-lC8NG1JqIw5ygAj47neeakc8znKfx3IoBBa7cw0Mso92vMFIlE6JU3c28Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
روز گذشته شایعاتی بود که فصل جدید رقابت های لیگ‌برتر یه‌هفته‌تعویق میخوره که سازمان لیگ تکذیب کرد. لیگ برتر 10 روز دیگه شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/27093" target="_blank">📅 13:31 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27092">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JiKeluE1aGESy44nBpqGl4vA4bl6bkKVJqNxWdu6o9h7Lo1rOsTvPmEmqSQ2eb0-txSiHBQkuWAk71wOHw0AK_MP_wJsXDNAEMTlqP8IHs73NaPsnjaSyFrwtHS_sDJ55OA0_C8NfX7hXLHzO-XbUnE2D62pPhQ8OtDpQd7f_3yDiE8HNyKXElsCltlDr-TM2oPpPplYV61qWfnv6IItCQvNe2umb8n5LZTioty7i7PVA4IdQVkfcaESP0LzPCuwVTmMoK71S4Jx5i35GjLOJszaB3hsefKRUiJT7hj-6J9QmKeAORuOgEoT0iG275a9hIciusDVzruQV2KYM7vfGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
استوری محمد جواد حسین نژاد ستاره ایرانی ماخاچ‌قلعه: پروردگارا بخواه برای من که مسیرهایی نروم که باقلبی‌زخمی‌بازگردم. کمکم کن جایی برم که دوست دارم اونجا باشم تا همیشه شکر گزارت باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/27092" target="_blank">📅 13:12 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27091">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=fZGdwqDp5i-cREvQdeHj_eoPx4PMgcFtnLYyf5D9iajzEVg0Kb8-aQJWsju0IWiVmepru0BgdYHGrhpi7iQmSKYOsI5_SeykUaIwP4U_SN-zyBztgLWW1UUmHdLBzPNqEwyfn3819BNyTYnSR1XlYflrHxn1utbcnvEYOjxG3fpMcZe5i3MeGFvzYeIHjBmj9zRltO2IN3Xt0nnr8QsZTdi0Ow9ycxsnlbVczOpLeg3Lc1ddAp8q8JsoJ5WfvpjRXbywtV1g4bfNwuaC_FBV_bmUj-pfmGLtj2CRjQKfANF6yAIEKtUd8wTmi5mHyLzfyzVz-teroLRnNPIbCc5Sgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df9be54cc9.mp4?token=fZGdwqDp5i-cREvQdeHj_eoPx4PMgcFtnLYyf5D9iajzEVg0Kb8-aQJWsju0IWiVmepru0BgdYHGrhpi7iQmSKYOsI5_SeykUaIwP4U_SN-zyBztgLWW1UUmHdLBzPNqEwyfn3819BNyTYnSR1XlYflrHxn1utbcnvEYOjxG3fpMcZe5i3MeGFvzYeIHjBmj9zRltO2IN3Xt0nnr8QsZTdi0Ow9ycxsnlbVczOpLeg3Lc1ddAp8q8JsoJ5WfvpjRXbywtV1g4bfNwuaC_FBV_bmUj-pfmGLtj2CRjQKfANF6yAIEKtUd8wTmi5mHyLzfyzVz-teroLRnNPIbCc5Sgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی‌جالب‌ببینید از نحو پنالتی زدن برخی از فوق ستاره های فوتبال دنیا و واکنش دروازه‌بانان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/persiana_Soccer/27091" target="_blank">📅 12:51 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27090">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=nagTjAVgj8oFzYO4_aiXnVlgkDfCjEwMBiN2VefeeTvBJ1QFX0Og7llJrXQ-GXZfWa4hpQvJVrG9DwAS5W5Du4wo2D2TdejtlVp2TCpSITammH6VUQloB4tEKiYBvIFmU8EXOepuDyIMs_HGQcKzTi6ECs7prv4cA_jORwWpktHBP2x6n9K_sXQR2PyLJ98Lt7hgrf17fKMulJxSMHUmWVts3ReNkyQ8mTHiTIODnsTh8PdtQS1kD_HDFA32mMexQHtCHOUs85QnP9bVWddmChxF0atsHoagoaSdonHUi7Hm5aesDBP_tWH92szMCM3vGbx6JlVCrxkm3zc8bzWiag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17e27275fb.mp4?token=nagTjAVgj8oFzYO4_aiXnVlgkDfCjEwMBiN2VefeeTvBJ1QFX0Og7llJrXQ-GXZfWa4hpQvJVrG9DwAS5W5Du4wo2D2TdejtlVp2TCpSITammH6VUQloB4tEKiYBvIFmU8EXOepuDyIMs_HGQcKzTi6ECs7prv4cA_jORwWpktHBP2x6n9K_sXQR2PyLJ98Lt7hgrf17fKMulJxSMHUmWVts3ReNkyQ8mTHiTIODnsTh8PdtQS1kD_HDFA32mMexQHtCHOUs85QnP9bVWddmChxF0atsHoagoaSdonHUi7Hm5aesDBP_tWH92szMCM3vGbx6JlVCrxkm3zc8bzWiag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسانه‌های افریقایی؛ پیتسو موسیمانه در آستانه عقدقراردادی چهارساله با تیم ملی آفریقاست.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/27090" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27089">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370ff98a06.mp4?token=CwGjIp9Imw5JEBWb2nViqiJkAzYOz6AFOWMAcLIrbsQwKIze5UFGhtymwKipVDtCrHV3cxsRRz0Agj3077gFmzqzjfHLzQCfjwnb3Izxtzt_bSH2uOH2UHC5RAeTY9LAhkRyZ2gKPjsvyoEnRb3JgbbyiMjwauUhn4YVguezaCGut6Xx8mQHAJ_i8KHWl-ppwDuxw7YCUDdJl4AO9dois9dwRNZlShkhySSswjONR6i1CTIoc8eeHms5IZcb85dvaJZc24aZr5otfyjU4lH3ElARJi__OcKFvIK16GfA2RAdBVGb_j3nSzO9VxrVTuva-f4vVJ0OuMv1OPMW7DeI-rRJWBodoVbWAhBNMYpUNBwpeNauQujiHluPTVXd-lwA8urp8l5V8nMKiyHY8YopRpYv4lh_Q3DxAP7ZX2ITnoNF4scs8lhOgFXug0jwHX4F1CvU9F3o4CA9Yucr2Kn1MJjUlNwjn-uzBeyeHURjVQPwOcjjiLNN0XvS518dEukaMK11Fs4X6-hAs8Olt7SYOG_MMK6jKxGWGLTE7JG6DCHpuJmVYraYYIwACiLOR08KLoYgGekY1D5r1iTJWxfX5xndea2sYv7XTtcR9vhXw6a79wv8Q0X0tze1pjBZFgUQZ10dCInKiU6ljo4oSdIA47YDSxwypkgMnJ5Uxo2khQ4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ رافائل لیائو ستاره‌پرتغالی سابق آث میلان در آستانه عقدقرارداد چهار با باشگاه منچستر یونایتد قرار داره و توافقات درحال نهایی شدنست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/27089" target="_blank">📅 12:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27087">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RrhzkmhI387FaHPypX4y16bOocoI_31mE55Op5iaimasejjApH921WwsIj7ax9MXf5u8Q5oGTUKkdC8bJQ9Q4OYUPWSuw9AA_4qSTaaSlSgTO9bmqQdvD1IITizewUN0n8MqRtMRZnA4XCPDTR3_lhMzdxD8yL0ZhkuqmUx2JizMCaCY1bLJSZ80mAGPUa_20PG9wM21umsrlZ9ZLZMieNumKGYDK0OalAEibVY-BT72mo_mFSxy2pBDpDXsCwD8IU0TTpeFdFenSrzIonhwAdLvKg38oKDVjeY45qLTTrzYvtzCFjCxIOMJMC_t6IC4MJtlCYrI4NPX3xUpDuZe6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اینکه‌گفته‌میشه؛ باشگاه ماخاچ‌قلعه رقم رضایت نامه محمدجواد حسین‌نژاد رو 4 میلیون دلار تعیین کرده کذب محضه. بار ها این باشگاه به مدیر برنامه این ستاره اعلام کرده هر تیم ایرانی دو میلیون دلار پرداخت کند و خودِ حسین نژاد هم راضی باشد این انتقال انجام خواهد…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/27087" target="_blank">📅 12:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27086">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vnObwgIniXt2_RNU3powAq51oPuPak1kG6GNLtMwYAA5i9KM3Kei9EIWNODDmJEu8jPDHclHohurGPVzDQuZmbJRJtp5bIuGX_9ZSPHJtydqvx8NsofwOv7gxVgT8YvJgiGMw9mTbbQ0_8H6or7FTDhvYgb3kuUXFHPrt1Ube1PIOqimAxBCaKzF_SQnmMhkovr6jPUeZD6ftCpj1rPbNC0jsdKDNEo1jSzt3oWccnorbgIQD4BhnQG2bsfn8hzxEeo0oE0EOUyReUZSXJ9k--E6OJnaO_lRV7XYG2e57xv0_wTb9_tnDhvhRRuQ0u80pDrvAwMsVoFvVcleeaNe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رودری ستاره اسپانیایی 30 ساله باشگاه منچسترسیتی:من‌تمام‌پیشنهاداتم‌از تیم‌های بارسلونا، پاریسن‌ژرمن و منچسترسیتی ردکرده‌ام و تنها هدفم دراین‌تابستون پیوستن به باشگاه رئال‌مادرید است و مطمئن هستم که این انتقال‌بزودی انجام خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/27086" target="_blank">📅 11:40 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27085">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaMzwWn8FWH_yDRGVUknN5pli6rksEqvdv4I--haLXzFZ6YpscYSkKXdmsEIEgN6CuvoukKYqV1pNm-Ih0-oo-uN1fXCmGmJrXibjARoE8bM8v1fTzfbPnhFMxqAepvBjqBeQcbZnxbiYkDpCNIEz66KcwTTizF8kFzKjgOLE6eqlEF4tJo7m-Su4VgHAz5w5JvoA6BBhxAJ3WQcGDp-GbXH6LXurDViB8Jio-01yC2qGe6mRzJQlVHszyNSHyzzMNpaDg0sCohsUC6wB5j5tFMaRnooGjtxMmdAZsxI8AlNq-5HKDez74V8MvNWpd3F7ZvQAYHHCbvIFlBHZY5VWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیویی یک دقیقه‌ای از سوپرسیوهای تماشایی مارک آندره‌ ترشتگن در دوران حضورش در بارسلونا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/27085" target="_blank">📅 11:17 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27084">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uT9SPmUejTkijWzA2d_trXVZU8UHOa14uRAM8y2CXlFawDA27nw5dL_D5NNb0ACy-F8ydgrFUSNJf2gOiKgdIK3wRPQ9_yu4i7qDOADhAzo_nglX1kIUHPd-1gWTjEElS7TLQIqdOIEsquTqX7n6Z5XT6nNvS2-F8DTiaqsAO7f8cxABKegqSlB0fXw4XH2GqPZwwewEvrolwWRVyaXe1xXcq19CSNIPz9YW2ZDmkhxmyMqnKjp-fLlQa5vl6xh4MdkEKYgg4yDiykEc6M68AWV5YpRBbWDcdIbLR2dd6lb5oTXHuek_rWEGppf06iLU_2L6AsyCtId66gvS4otziQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/27084" target="_blank">📅 10:53 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27083">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=shcLnNX1bQj3IrNAQiP1v3ozBIKYCs-8y7z3C5TdBJm8WpFeztY3ilBElimiEatELmFVmopj2w2LYayLgsB0MFWiXz4eKhEJCH3Y_irCwDn7RvJzb_SvBuphuPeXAFT6yt2BZgKqMPMJvlV-qt1avEWYLJpGWg66xqmdERggoW2Y-eAN7da7fG1EGQE4VZUMyObrkUGBeJDrXCp4szA7lV5k9UX_dwwUCYNw78WRYGB2KPWU4_wMvLVDiKO7HOXZOapMBgNBqFW8P2KI0H0qo9rjD5PURkU13YiO9-TWjoUfvubA75epKJq89v7_CwkkzvvArMgo8gNGF8ab__0TPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/222ef9e7d6.mp4?token=shcLnNX1bQj3IrNAQiP1v3ozBIKYCs-8y7z3C5TdBJm8WpFeztY3ilBElimiEatELmFVmopj2w2LYayLgsB0MFWiXz4eKhEJCH3Y_irCwDn7RvJzb_SvBuphuPeXAFT6yt2BZgKqMPMJvlV-qt1avEWYLJpGWg66xqmdERggoW2Y-eAN7da7fG1EGQE4VZUMyObrkUGBeJDrXCp4szA7lV5k9UX_dwwUCYNw78WRYGB2KPWU4_wMvLVDiKO7HOXZOapMBgNBqFW8P2KI0H0qo9rjD5PURkU13YiO9-TWjoUfvubA75epKJq89v7_CwkkzvvArMgo8gNGF8ab__0TPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هونگ‌میونگ‌بو سرمربی‌کره‌جنوبی درجام جهانی ۲۰۲۶ مجبور شد دربرابرمجلس ملی کره حاضر شود! او توسط نمایندگان مجلس کره جنوبی درباره تک‌تک تصمیمات تاکتیکی‌ اش بازخواست شد. از تعویض‌‌ها و دعوت بازیکنان گرفته تا ترکیب اصلی تیم و سایر تصمیمات فنی اش، همه‌چیز زیر ذره‌بین پارلمان قرار گرفت. هونگ در ابتدای جلسه هم از تمام مردم کره عذرخواهی کرد و مسئولیت نتایج را برعهده گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/27083" target="_blank">📅 10:35 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27082">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lW0aRQyser6NSuwwMWr_mOqeB0dwLCetfwOFKsgTV61jLDDNy_1MYvKxyyaIQfRqkRDV8-2po_1dci6MvaIkfSeImYrxoguC19xg04Uykl2E8nly27hs8ZvlpdKukVjnP4HdGwITDSHKGlkd_deJkZUAyQ2WOK3dPT2t6ZD-xxJrUHOp9gIZaFn4ZKWHiI5muJBOBEESce0w5n8fpa4tinydg8ZWZs3iq53-sebOS6csql38nFkcOqaJ_jNWG8GrSejfDUzXehBZdkxOLtG0qtoKldls5TVdj_AQm2dqDIu44UF4o8GKCmSTTjE7Ds5j-332UkGRhLg4kYqTI3niow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
نشریه‌مارکا: انتقال رودری و یان دیومانده به باشگاه رئال مادرید نهایی شده است. بعد از رونمایی از این دو بازیکن پرز پیگیر باستونی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/persiana_Soccer/27082" target="_blank">📅 10:23 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27080">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4YnBJRbZp45wLVBMy1SFN19jSYzcmO-nNCPzT2yWY-BN5Gr-S7K63jiCjg6tsckI9I1Ntb5rk3MmATxrkxhr9NTfzR2RVvaGhe7AXyJKks4x6g8csPzIVCB7KWrKaynFXxcvzmJFZrV6xC9NIEhBG3Leqp7t43amlapCCeTb9TEnfDBZIPDo0SHwjIp0F0dIdKusaYKDGCVGe4-RbcFiDcsiVEhevRWLF7HYaCfCpwRFIh4UO3wTaVh17qpQziNPCB7qSYd7QNZAwQBhG548Ugzil_iFQiSrD4grm0YUzGkyU_r6NhH3bdvagv5JjwYi_Y_wzxvsA88AsEBX47HRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه‌جهانی تیم‌های ایرانی در رتبه بندی قدرت اپتا؛ تراکتور تبریز درصدرتیم‌های ایرانی قرار گرفت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/27080" target="_blank">📅 10:10 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27079">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sT6VvSoW-9P7m1QayOxWZ86y72GPgNOMjt3MgdiVFDQhDI705hQXaueUPJwQieNlYyLqiHCcS4_2rSaYSm-yz569cQ2nPX01usnX3M4bzf3f4iAiVGpWMwbtaVAQFR8UmZHraXY8pf5lJu-NI0u7sf7eB-cQhwbP8IzOiDEsA_NNJPOlgakiBifzAreRJgQnGJggyEz2K5G1HwioAHPkI9KpROJXz1NtMN4Z5sNSLytFAKlCoD_wsG3CoF5WD7_V28ocBKLcgYY6jZ740kWOwB5we7QOWf7TGm4krXgeF1W0SUUooeKXK1i0curc-2iHpHbjhxMY6XSiBQe5afNerg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
طبق اخبار دریافتی رسانه پرشیانا؛
سعید واسعی هافبک تهاجمی‌سابق تراکتور و مس برای عقد قراردادی دو ساله با سپاهان با مدیریت این باشگاه به توافق رسیده‌است و بزودی باحضور در دفتر مدیریت قراردادش رو امضا خواهدکرد و رونمایی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/27079" target="_blank">📅 01:02 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27077">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2p8BtpdTRXlUeRg6ifKE-K_8-D_OQ-X7iiXXdqXv3yGgvOBEZyi6XHJCa4Re_a8oejBxZNcRjZRFa0exxXWS0eNWyKMNthSwWJnt1NPnzMHzyWgXVhisMihhSj9ux_di7d3w22uuRox_FWlyOBFK8hfQjT7v03baG_rpPAERhs6uyYlNM1um0zuYX8V9WlTok0yWyoPJs_i3A2fc41VR37U_PFaDpDYFE7xZPYU8fCxUyJ_WOiGRMtVpIPOm5uF68Ci1xRYmShNXg5t9upFOYCUyAiegQTF7S6iX2juiPKNWUFcT1CXU259NGDp0_5Y5pWjtpYPN919Ei4B0vPfhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌ امروز؛
مصاف تدارکاتی و راحت باواریایی‌ها با تیم میانه‌جدولی کی‌لیگ کره‌جنوبی
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/27077" target="_blank">📅 00:58 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27076">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPFQKN9XQOTWc0Ob7TQJ4_nfDD1J41ZLmak2PCJeIPdjYyp_YVeJh0-vwsPdpeyN-Yj6IHZ_XH7BJVD_gvXrt56J9CEGmT2kmgEoa5iajw-Rx0WjAzcr8eP7v2rPlu9c7wsr-VlFk5qmKRsqqdsac7My62Dks5bxDYEJE5PWagCk4i8fRP84VxzyBbubl2jT3w59PemJdNU_CalQYgr6hBWDb2WWYElhg6HkvhotrSTXYKxPx0jC-UyTX8GKJ0cg9UxUR1Xs1v0haXAjfZaXuAH5tiRvcVWYy1kOgzh2rk44Zyr8VqDuVig_mmLhME2d22F7Z6t9SGw6X0xASnhNkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
روایتی‌جالب‌از آیمن حسین ستاره تیم ملی عراق و زننده دومین گل تاریخ عراق درجام جهانی: در سن 12 سالگی یتیم شد و پدرش رو از دست داد. بعدش داعشی‌ها داداش دو دزدیدن و هنوز هم پیدا نشده. بعد بخاطر جنگ آواره شد و یه‌مدت هم بخاطر اینکه مخارج خانوادشو قید فوتبال…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/27076" target="_blank">📅 00:47 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27075">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJx-7-8ovgjypChMHJeCImlX7ZC9Pi97VavC-zNb0U_VbHXwDKAL7OlgNPiMdoeVGus6gTw2odR6_gxWV0apFpchsLSPpnK_WCG34_xzkMynSVo8PcuOWBesHU2Msyi4LE1XDslmueJmGxn0FMzlKLP3Nl-2M2EEXe-QNMzG0mJB02DedpZzns_vzKYAHwQF50Is-VX4eoZInSi_NtZwn8r64CyDNeF_cvNf5kQlQ4jJLWOq_0LBPO_eXfAuCylscfwDaND2YoT_t6gl3j6RsiVSPQD9UwdeVqP0OhZ8GJOfTNOmOkTMGsk4rIhIfKE7JrWeq7fbbUcrtqTMRF6W2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
👤
محمد قربانی میگه‌الگوی من از بچگی تا حالا کریم باقری بوده. حسین‌نژادمیگه‌من از بچگی طرفدار مجتبی جباری و فرهادمجیدی بودم. خودشون با زبان خودشون دارند میگن که دقیقا فن کدوم تیم بودیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/27075" target="_blank">📅 00:03 · 13 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-27074">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BD5-tfhBkllwEDf2w7Sdy_HdPjxH4jq4DwQPhFuE88lREhmEvAP6o8_CgEqZ_a4dqP6CbXcjbV1SQF2D5pWZk1DN5DnK9plo3ctKWawHGJxinsyz2uS2RJyZ9hsGwuswj3OjcoCeEQjAaqnF_UHYcmzhcu6NeuVPmsg91-BB2dFAVbatXq2mq6phbrJbiOI6cheiU-NqxvbL49dNUpuIPc37hyixwJJiBnaGjuMvIza6VNQYCm5JDi7LkZ4SyNEJlWH5aU7u6IJFkyVwtLApPWfN102a_QVAiLNBHZBoiVGsapBM2Y7JXswM63BoFAurRtC6iWcXtXMAVkZdZoOy2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/27074" target="_blank">📅 23:56 · 12 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
