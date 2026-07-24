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
<img src="https://cdn4.telesco.pe/file/YOxq070t0dZpYCmQekig9NwpN2t5iSn8K0puPFdDOuw6kYkM-iX5o93MwX78NngB6NM0MupEDeCkOhrk1WYB4Ep8Rc-yVOaJ6FDhhaT6ueRmlY7orW8ZStiwUUYv7ixUXvhDlc9UMfQE8BtvR-xSGDGBDQjc7jdQoLo9WYeF6AxAaF-z1OMkR4Qqhu2K5Z8nRSM2Dy0L5uelWHHXnhZE5YUo8JYWLqvck9Z8d0rOXCwYU8w6OEMoPChu4YUD9vBRNMVcX9KpEDsQ52S2msuZDz1Px0NMuLaDWn9TJCL8_-QI8rf1wYJhWtQmu2EuEy6RqR3lI3NZkxsXR9gFJ9txaA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 559K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-02 11:14:09</div>
<hr>

<div class="tg-post" id="msg-26393">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pmojt7hyWGPFraUZ4q-FWXjsJOgd91WQUxO369ez33Rb6gD2plyMywgScDxDt0bA5ui2cTB4alkcCP0wy38sXSn5RXnlH1ZF8Rmgzxv6h_zJrC48bFG6hmmL_VZrO6H2mCxGMmIeERSFuIVdJd27rT_tjOsqe0DpsqF23Jjtl_1EQhE3PMI11qd9WKioLcOdYdRWv6LUSm0ueBSznhueh05JsIp23zJhepSvMOOgANLM6JQM6XOi-hbEPvAnfw5if1fOqkm9kIx09zPJLFGGBmz0YGpG6RR4xaJB66JAtTlhVrTNzYXJyoR-9VrWgfEuIRejYmDlOOzToLVjbxO3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
🔵
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه استقلال صبح‌امروز باارسال‌نامه‌ای به مدیریت تیم سپاهان خواستار جذب محمد امین حزباوی مدافع میانی23ساله‌طلایی‌پوشان زاینده‌رود شد. نویدکیا سرمربی‌سپاهان به مدیریت فولاد مبارکه گفته اگه رقم بالایی دادند مشکلی با فروش حزباوی ندارم.…</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/persiana_Soccer/26393" target="_blank">📅 11:10 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26392">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OdWUVoqjWY-b3rOEy7hbjrDruZjULMBKn5PTyDL-Oaca_wsMlW72DYYCjqyXhfZCYyEzpWINFLW4vJaM9XXR3VJnHNlM40M7McaSzVdalhNlXrrFtP6LG9JSWu33U3FQqNf2T3ZKOsp1N3garWiCsuqnunL6u-Vl6N3YEusbe0VbUMx4xxakNxPNSs54j2pUAYbD8HGjhZGbT_ids6s7frebdWSyF7CXXL6MIwyMqltmndmwLMEhwO_NYlbCL4zdCeRi6hDPoomVvD1RkAFNIpfLG-8-1jPY2fXx9oUz30JS2JXLm-lQpADs7HPrA6v53foStMFWQ74uoCovyZWBYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه سپاهان خطاب به نماینده محمد امین حزباوی: هر باشگاهی او رو میخواهد 70 میلیارد تومان واریز کند تا رضایت نامه صادر کنیم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/persiana_Soccer/26392" target="_blank">📅 11:05 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26390">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vDHQ7N35JbBIhPt3J6T5s89hTBNit8hUrYpHx747j8mkKwHe4DKMq_B_gCP_SVKM1mVSqtLtWAAKd-E5EK2DlbZueL-P8WyVDPSu-lwChAGs2gtSFAuTOXx7eQd8unl1Q5bqXDHUxk_BCAAcar_PJjzke0C_VsI5GBghvMnm4reOSztcPsy-5qXnLNvUILwwc8wsYOrIFmImJlFjlxsSqqsWfSB-hpOQ3hZVGo7J6k_su10j_aOBMvkOpVGZmdNNZREH2uzxbT2DObr8cH0G0fEntmCdyTqjLg6bb_JspT6MWZU4HcKRypmM0AFcuTR12MOSXWtw1PfmHfSOEP1tgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bafI0AUhrdh4oop5OyTbv7ieB_uCy-vra3V3zR80ssxge8RUQFVUQK8CVNi_FUOSTbuoOG_ftvNFt6kKLFm3KIcOJsfeOxlkUfZMHTFbCN_epNp4krIoAp_M6GwX4eRUn0tGdx3M4WrazW7G0Z14qtA0mXCGmrbPDvJPkdPgD4aTnQMLcF5j11WoKhDcVFwJ4NjoAOEe33XAf-NLqcDTpxXlch-hXH-qwRqh9Oxqs1pS1wzCpah9DslGNdJFr751gzkbZyc7rTW1BTdSylJ7I7Nr4re1dDrsQnVOBq1hCJdfUnlpA4sSw9c1xcMgG6slO8jMTJsz27x_UXykWkEBwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی رسمی باشگاه رئال مادرید از کیت دوم کهکشانی‌ها در فصل جدید رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/persiana_Soccer/26390" target="_blank">📅 10:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26388">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G-HGK8fXC8_8EyN4JgPJ4c5nh56YK5Imczf7Slekowi1oNOzZMiVVShjKTIdViWYfanMaHQaCdcT_poJpNXy4fX7Z3SqppAANWOIWrQybYLDi3tn164XBJ88LcVFWg42-uNsYm_pWtgpx3B2IrfDkigy7ZwhhythbNOyQ1IAkCOWnU8KG4cAoTZHFzqVo7TorH6Cn_F0N6uLjChAUSX2i4_POx1ZLOZSX1IEU5GadlW27CqBNLzQAIAV8y0j6d7FE7fKoD7cl6vtPA8uE_t2bC6WkR301mtpB6VDnsKDFPvkDJnOFBGU0zTu7EuW6BFrAT42eMLow2gJ9hq1uYdppA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bTqJ9chgkRZKg5mxehSFvGs_ta3VLcvUrFG2MITsDA2wBGNCZyU6Imum_JUBbeE4fHjCcpflaT2_-uwrC-Af-iOttLnJQ4XlU--eQO1oURBMbsxo09y3QCfFs0JziP1WnlbJl_UBaqVKMr2fF3YXHiakxZoVHR98c3r1mFGUNgZ0nXrr-EwAslHqksYfKhvDxYgDkhGEVIUQnQA6cZMvFxnhtussblLpAHqRGBIlc2DYKVvKBDsQbSv7DV3PKBQZnFB0nNg_49XhbVJTnVYG5Zi5GfMTjoX6tpXzVKPPoLdfGy7pQLcafAlt5-5HpYy9nSQy7l1CSc2WM7Q9a2MycQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
ارزشمندترین‌ بازیکنان‌ دنیا بعد جام جهانی
‼️
یامال پس از قهرمانی جام جهانی 2026 در 19 سالگی و ارلینگ‌هالند با درخشش در تیم ملی نروژ در رده‌های اول این فهرست قرار گرفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/persiana_Soccer/26388" target="_blank">📅 10:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26387">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDB-UUoU6kvIdGTeyvRitFRnl79klHv9QT1h8cpM08k-l2fJC60RheHrZQHYLzeJq_83wdytW073erZpwQqO7LwfGn8e0cB0KqXAJY-bIvWoSmznlpn5tT_PT8YG3pqVpDgX12cSY5mGawunreBB13AskehI2ovNkfb20sZlPNTtfkdNoEIlizg2jFdpOzy6WTMnCL6WIymXl5g7Ia7sEoVoqsq_jaVObUp_PwqV8biVN2VaSmGVEH4PmsM1q9VwVmG_eXefjnJogYYvBB40tq-A0_5LnklGnBr7K8zyMp-CPp-oqomtkyAuJ81v3I1CnaPGBTkzovqFNfKORAV23g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛ علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/26387" target="_blank">📅 09:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26386">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STCix7UQleNaCEwRbm6zVQdaXo6pJ3mjEtKcnpmW4VL3SLuS6Ts6tGfQpfR0N5335B0mnMelh7hMg27PTZTEKgewp1ahitURFiz3oQ0G0IOXbKLgIybtVmlA_4iS5NinUFglTca8k1qVcFVdNVVKyq_jEopV3QVp-VPmgJbIdz7GRtan6RBoPEv5i_F2cGUEVf6uF_pQImWRJD1nkUct_T1UPGs_W5BxKqcXeoCfhX2drZdDR_9hpQZq2p5z7XNNt4CKFvQOPxvN5WWd-fAV-kN1kuD5gqyX12iOGipsk5YA1UEDa9xz4_C10EmOk01adNF-OXVBlc3jWk7WWghmPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
🇫🇷
نشریه‌بیلد: کیلیان‌امباپه به فلورنتینو پرز گفته مایکل‌اولیسه کاملا اماده عقد قرار داد با باشگاه رئال مادریده و این فرصت رو از دست نده و با بایرن مونیخ برای خرید این فوق ستاره جوان توافق کن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26386" target="_blank">📅 09:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26385">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoaC0xkOp2Itn2OYRr5OHps5WDVLt7Ue-464SK-OlsK_SaMubqRsNjiuw8d9X9wYk6_VBEqmXxa6vSvpnNEKg7CD2YGWgv7zJWmKf6DsDHN8fTzjFkarOb_zsSx6bAm2yQO4tli3Eb35NuXca-5IAX5sqxNMMYkujkkyWappEhxU4xaX1OVc4TmIFDYbcLfdWYhCQKhvA1jJ4ncEaCc7TmCkCl-v7NqnGui3pYLTFBWTurOBHIqRJQEHlLcq401TmH1DsrGE8ocMsPOhikjnaBlXs4WZ76uSqcsdWrZRKQbDEdZXVLwWatQadSHYS51LEGveyhmNFcLwDMg4a0CGZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
با اعلام فیفا؛
علیرضا فغانی بعنوان دومین داور برتر رقابت‌های جام جهانی 2026 انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/26385" target="_blank">📅 09:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26384">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PBNHjvocCQ7GzuPnVvPI17_wTP6ZyGOsFje8dep0ZY1reympYfjdpuuYZAUzGSTuNMpebNDuGSsUXal9791UkBY6T9YVnDLFQjn0fUySMusGOjwF-UzhZ_PNHzuFsluIbe40VLwyrqdWP3o-vMtLlrWIRzrKmU8zQIYAFTR0KuqsUalC1eL7tFohPVfBalyK23X26_Hm8YdU8LPTo6vtj0TvJQ6g-11Bj2saaEjwhAy1LS9O2iqMUCMFr7psqPqDze9bGO_o3Rq5zwdc5qGdKWyYOjtfpF0PjGGpWfV-sqw_XiZISI9sK_DId9HxMyGP-tLY7NoyU0f_mPKIkdxqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌شنیده‌های‌پرشیانا؛ باشگاه پرسپولیس برای دانیال ایری و کسری طاهری دو خرید جدید خود نیز بلیط ترکیه‌برای‌اضافه‌شدن به اردوی سرخ‌ها نیز تهیه کرده و بلافاصله بعد از رونمایی راهی ترکیه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/26384" target="_blank">📅 09:15 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26383">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">📹
مهم‌ترین و معنادار ترین لحظات ویژه برنامه‌های عادل‌درجام‌جهانی2026؛آخرین سنگر سکوت نست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/26383" target="_blank">📅 02:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26382">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=twe-Aal6lmSLjpEpIKVoNsvT40On8RkKbq1zuAtSJ24yszkUR0BOJ1dPIZTeM8kmDVmUpRJlI4AcEx5fc2qfgEhR-c2tYhGGV2kTYsUk9GEziCBT0hY2eePzgUbpNkQvUQhZZMzLwTJcwRjsmdBs29JYb-rnZWQZ_fnMkEAbAstyvGhQKrV9Of5EM9CDS7UNpCOJYyJ92fzPyJGADIe7MDyAc1yBqzhPFEuxDdJKDFha5k7czJPob8rp4Jt05g1yzt-Bki66WMK00Un7FX562-eTCbCEiSuITXo5Yu8BIXD6NkcgA8nxviwioLPeFbwwfEIYwlxv2fkOSlXAAYIBYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b82b96591b.mp4?token=twe-Aal6lmSLjpEpIKVoNsvT40On8RkKbq1zuAtSJ24yszkUR0BOJ1dPIZTeM8kmDVmUpRJlI4AcEx5fc2qfgEhR-c2tYhGGV2kTYsUk9GEziCBT0hY2eePzgUbpNkQvUQhZZMzLwTJcwRjsmdBs29JYb-rnZWQZ_fnMkEAbAstyvGhQKrV9Of5EM9CDS7UNpCOJYyJ92fzPyJGADIe7MDyAc1yBqzhPFEuxDdJKDFha5k7czJPob8rp4Jt05g1yzt-Bki66WMK00Un7FX562-eTCbCEiSuITXo5Yu8BIXD6NkcgA8nxviwioLPeFbwwfEIYwlxv2fkOSlXAAYIBYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درجریان‌مسابقه‌مردان‌آهنین‌یکی‌ازشرکت‌کنندگان هنگام تلاش برای‌رکوردزنی دچار پارگی شدید عضله پا شد؛ اتفاقی‌که باعث‌شد ورزشکار با شدت به عقب پرتاب شود و فضای مسابقه را در بهت فرو ببرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/26382" target="_blank">📅 01:59 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26381">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nHTWZYFZ5zD1ZWnRzLkslwLxINTQZ_jc9Pd06xVhj_Xbe8GOLlVxtMRM9pJj5IJhUJ4E8RSYAiTdYCgqpUFeWsZ2ADrkwIc8dbbKHpvnnNcTyqMKvT_vs3eVm09YFkNqWermI9e8wRKTNEHP-4YSZl7f2ZwuYPH0HMWfndH9XYd0J0fZaQoBd3i7AAnxph7zJAptF9_N58oGzYSQQyZTrkQ_HR_CBTCyZPPHkRb_ptQpX0pVVBXvBmoCq2IkWq2jXGKQV0cKLeFWKvZ3RmSkY6wqeqzB8mHUlgLMV5-0SI9HvJNF9C19HIKfe5FlQGeJRAFOILX3Q8r6CxZ_X6btEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/26381" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26380">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ire9VSPqBY3GYMldU21AOm99mZbtV328E5wFi9VR_lHNwCvP0x8KqXao5qSXEvHOCTDCW9efg5ERg_v8aaW2flwkSBCsHh1-JSyhvs0uguC7eRooEhciUe-cwD8BdU5_1bngb4ZVw_XySIfyCo7D5vueKR81qkh061JxRD2phIrcX_WdKWaELe1BOaEohEBTrQd7RnlXqIeiDEIHwAHPHDRUQ-bN0ZfgLwCtJ9yRwP4qNpWSpC8x7ng5AT2yURESofn8WtKRuXpClVFbimiQfebFQi0XsgqQ8jEBOvt1C6iNvLGKsxlKIgr2QugjV1nqNwdHRZugssuwLwrp4YuqUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/26380" target="_blank">📅 01:12 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26379">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fyf3LVEK4iLlQ78XC9DHqNFO5l_1YZBB0iBCFc_5sAGHT4ZVj6YpDDY2z9uK3_fSMZ-X_a4n1s00rxJBCj0YB0K5U1qGZrrq8u2tjumo0AJDPibTVFi-eseEsV8z4qGzstmvBetMpA-1B3TM6C-tuYNYdlQV7-euerhQdEvNd5JLBqvklF9p7AFQqxRmNUt8YorZYGLRhWzPs4qjV98u7XIDVt0lABn7sq7c7OS7U63J0HgP0jiExFh0_EkAuZBlmBrNN3BeLoTT8AQshfWSdQb2G4oWtAY3akaotzbVuMzJetR4zSusrZ1MdfdsC8jKYEfGJxr7bNSQBHvH_GLrfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
👤
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان ظهر امروز جلسه‌ای دوساعته با نماینده مرتضی پور علی گنجی مدافع 34 ساله‌سابق‌پرسپولیس داشته و مذاکرات بین طرفین نیز مثبت بوده و احتمال اینکه مرتضی پورعلی گنجی بزودی با قرار دادی یک ساله راهی این تیم شود و شاگرد محرم شود…</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/26379" target="_blank">📅 01:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26377">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/chOSnbt9t7jMrdcBmOuI4p4GWUVulKFcOzch2KNBcncTcYq8Z1sHh7HFIiObK_kcp3yCyiWuplOqcIN-ArygJlb0PXT8d8lL5uYts10KqOpLrGPzwhK7iI3arBnbre0E5nx8vO6ujHesNBN4a_FQLzcJq0Da1IK74A6hTvswzUYOrRLPCtMf3iam7jAOAvdg5_Y4icAFl-Xrvb54Z4tWtCMN1Z09WUvKNokcf1uSHvxv7FPcWnIbPg-unpECSBcj07L2tWTlhoqinjHzcHdvjNdLqqxjjqDpbruFWhR1PbYABW1xG_vO7CxqlvvcvMtRv8Pk9TL9rUVuNDzGPOYA4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
لیست 10 بازیکنی که در رقابت های جام جهانی 2026 بیشترین تعداد فالور رو دریافت کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/26377" target="_blank">📅 00:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26376">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a867be5010.mp4?token=jYWjwUze9EwEX9N-MAiScBfdzYpeZ0IkRb4M5_oRpGcsHQv78hb6gugnHl9w6KyCpG9AaNiNSHtgZqkDVtA5Nio5Z8SA24npmYuZ9UcNhmYCE94KGnh_ITVwd-o8fdxx5iY5wtwsohfL4W3oyZj1shzdPkSK5j3ARzLLKd615yC-GHs3JhDLLsrrH4DAJ3R2xLAdrurOuMHPceyLkh4v8y_1FvwIwTga43L2O0K7eyHvbQlWJOmcicm90zt9Rerfd7bu9De--3LX78MxXwxx6-mQu3FIjyy86Tyy76IK81z3m7mSui0sAU5pmYCOrzdq9aGxDLz7_BO0q4dqmfb0QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
همانطور 12 روزپیش خبر دادیم؛ مهدی رحمتی پوریا لطیفی فر رو از گل گهر سیرجان کنار گذاشته و این بازیکن بزودی به پرسپولیس خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/26376" target="_blank">📅 00:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26375">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc41d29ec.mp4?token=tReC_iqAMh2Dhcb7mr1R1z3sPDdxU2EDGh_J2unvCqMMC7TLnKgUd5x76CUKuu0Ipq-VthzLPin6cim4duxnnRu_CZTvqKk5DlOge5nNl7y4ESH_orx02oKGmmKGDNYNBc2XFvRBEOQOZd7T_-y2KDLKYExBRyQXBp0wuGzPqNUrb4LfglmPIkiJUzuPOucdVpRIEli9B_yaW2wWFxN5dmjY9FOkpt0_JLtj3xoBhC6eDGcNUQA8e9vAhLDCMrt68NtnqMMtQ5SyVhqpCsat4drMsVzCMi3ABXm4feQ5FTz1DQ00DSbat8x-wI_79CX7TwfSzoS48eSCLCfqSjT94A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
عموپورنگ امروزتولدمادرش بوده که هفته پیش به‌رحمت‌خدا رفت. اینجوری براش تولد گرفته است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/26375" target="_blank">📅 00:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26374">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxup1R6uOgKsGrqptE3kRRbBI-fJ6ss4TJsnXNfu3rtieBoLBgyYZngo2jP7YzuqWjEUlfAW2eGOlmh33es47WoxYivHAH1vtkJPmCc7GwVP6qqqbvBvKel-xJqSP6JBLX67KInz78VcLG1IowsMY6L38RcgzhELNg9o664gPLCrTePdhNa0PY12irkQY4_riljRwvgI7erBsoMXQw-6AFvsmbVskK7ry6yxApRJMqiHZfxZ2KnOi2pkBWamffrGMq17QbPaajTAZFtIxQuSR0wttjzWafpIGrzFNmUzTV6Ak3Mg4LPRt9mPVFb5jWoJ5FSYR54Fcn6TRx-FRSEA2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه استقلال عصر امروز به مدیربرنامه‌های یاسر آسانی اعلام کرده درصورتی که تا روز شنبه یاسر آسانی به ایران برگرده پیش‌پرداختی‌فصل جدید رو به‌او میدهند و قراردادی سه ساله با رقم مدنظر آسانی با او امضا خواهند کرد. احتمال بازگشت ستاره…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26374" target="_blank">📅 23:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26373">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOaozIsvkTSsCcY3W2hNl3EH63tCBs2QJ2GDkfnXfyMts518coiC6ZCYRmyM3xLk2Sqr4g8FYwq7a9qusTzVlA3lFzOslPnV8RB7b6aKb_WclSV3xjoX9yBdpvzaHD2lVgJppRnEGiyYCD1kYKuApJJiN6n4msxxsuGxqTnOx1Zu3OkFUk7209CG6DP0KHOFCYL8AiRisfNKlp2ppMVn_CgZXMrFwmF0sE-XeQ8IgojVf3uBszjLRWZx6ny3ieWti0B_MiB7Sd5j06tD4bHwDmKYC-JLIOm6PspsgONOuLVCyUvlkSpiF9Y66OzNsS9JTfdZgnJpyZWWuWk-LBmJ2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇷
برونو گیمارش ستاره برزیلی نیوکاسل بزودی با عقد قراردادی چهارساله به آرسنال خواهد پیوست. طبق‌گزارش‌رسانه‌ها توافقات بین طرفین انجام شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/26373" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26372">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uuh6kDsCfZoHAXKekzCB7vxvitITaKsJe9WldhQVzyM0lXeVcq9tlS0KVRJOlOQA5igFGynGfr0Y-7tvEHjt7cWSze6f82qJXYYghpZG_Rv3A2FrR7kdt1tdR8jfBxxqh-bEmCiB2Dltvb5n3Cb7CF-_iQmFshZtUglUFPzglsYq3JMZadMJzRgeLgXWiKskqaU-v64fL19tx8_23VW_t58UyKzGZR2WNfPgRN6IgNlVZAusLuGP6VnYv3zVoniJQ7DNs8wN1R-NTyQ_lcmwYhbeDDU9HrV2AJpIiiEGoLeGMio0QUhHsVPHrJIzURR0lp8sf5tu1OFs7adwl92g3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
خوزه فلیکس دیاز: رودری به سران منچستر سیتی اعلام کرده علاقه‌ای به‌موندن در این تیم نداره و میخواد در این پنجره راهی رئال مادرید بشه. پرز حاضره برای جذب بود 40 میلیون یورو هزینه کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26372" target="_blank">📅 23:07 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26371">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKOpHwStnorTiK4Z-SiQk3FqSMhPZj2KkaObMHwuXKbM-BtoIRixA7FNWDCNeymbMFp7THu0M8K1UuAN1Zo-hWv2Oo9_uJzjuUeuR8o3jhaKOKXHxrHU0szKu-XGRb3xDcWySelafIePI_hdX-z_cN2bpDsq9hQqa8TERvcnd9Zqat32TSBtowqewfrdOzspALGFRgEcHucS0SIWbdkFf7xhuArxAIe5wqtx9lLOHeEYeojC8mnTNFQkbml_gMSy-t-8R2DwbR3w4bNf5dgikTxEmi9p4wtTbhNWq8USU5IMGbvwsXgDJyOd4Io6Za3uuMNfIRr1mUkpIOy3cJ4QIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
صحبت‌های جالب مهدی ساداتی گزارشگر شبکه پرشیانا درباره زندگی قبلی دوس دختر لامین یامال. بزرگ‌ ترین خیانتی که یه پسر میتونه بخودش بکنه اینه با یه دختر متاهل و متعهد بره تو رابطه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26371" target="_blank">📅 22:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26370">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jZ0v9ovUfAqxqcvK8roBfrKC3L52A4UjnoWDdTInLl1ulSAJrq7uuXxUnftPpl-7MU3M0Tlza3W-sNLFG53yKIsmOOUS06xsU3DcjFzWkWUM7jWujsJQmBYuAckM1cHIa-5BGv2upVzmkpaUj1p6Xb5gKE0RS9QXlqZ7L9MVV35IV6Rn-BJAMTpCn-NbbpGypY1RSz6PbBKTflArbn3noadlODambS4r2ahEOqv7Q06Z9WAPgueWqrFKC4cbh-aGkAe3SuIMJx5wFJ3viBK5P-s2F6MuIPACDZ_4_0i6q4nmctjwhd1L_TY9NTNXMVl_knb_tId44kgZ4YB5phiBLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26370" target="_blank">📅 22:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26369">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZeTN5MrJMXgARW-TzZznfoYxqIrvBIIlOlSGc8scUPfI8-kED1v8dFpLJXDD7oqLx_dK4Keqgbi8xcVzy-eVlglEqwRyggo1ZgAQNKo5NK018vffRkcx6mmmz14N1ExxERRhbooVSLi5zUsGD3CCIfvbCZOew677OO4i0fP8hzn0eKy-21KBt_MTEb2mBqRSHf9JrN49ZdGBbZfDeOpgZCxNTy9A7kOJvYCBwoY2gj8y2AjJypNg54ownPyLvwobMkqqlUWKNFmOdeqzI0XBtRpj6YpRBuH1eUKLOtiq7gCFIswvLddm13YwH2zhbfI7Ddm63560i_JiAnsh2ADAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
مرتضی پورعلی‌گنجی‌درحال‌انجام‌مذاکرات نهایی با سپاهانه و به احتمال زیاد راهی این تیم میشود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26369" target="_blank">📅 21:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26368">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5Jg4nNuwtWZ7HOpObUjAk05EC_1APtmdRdugAydHI2RNvFsDsNSO87ejxAbTdzaSeFfGqDWhqukqyZHg0SPEwOI_oXndmseMmuIMdQrzza_CVqxsPCZCvmAzOfLVOqdTkjn5kUtjIbNMEHb7VrdgpvO6bYyxcA6I2uK6HY5Hr1Q5EpvOlDaawoNY0wrAFSSx77TXOYrrEtfBe1g-sNRZLNjH9vjxyjrj4QVilzm9qsXFoo7L6iRsN_DN3Nc4Plb7RJxaxWII5R12Yppo57xuNLGaYZoldqdeuDHWa99qVUBKRan6d2dKpsE3SgvD7ce-WQEInMm7nAdOBhak_qOig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
نشریه‌گاتزتا: پپ‌گواردیولا قراره آفر سرمربیگری ایتالیا رو ردکنه. اوسالی ۲۰ میلیون یورو می‌خواد که دوبرابرپیشنهادیه که فدراسیون ایتالیا داده و ترجیح می‌ده زمان بیشتری رو به خانواده‌اش اختصاص بده.
🔵
بااعلام پائولو مالدینی؛ اگه پپ راضی نشه، از بین کارلو آنجلوتی…</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26368" target="_blank">📅 21:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26367">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdFwBPAmTSiZEgpavRRZzWR2na5_l6A7rkW7OegCTlXpaU8po4ir_Rk4OsBUJZdVJjycquv94I8oUq3aguXZLzvBhi-n94fW4bABu2UOGzeK5hFzE8Y1ajCE68UyJPHWpMuVNS_CZpmYfpkc9Pa0kjFktZHHHeHuqKU7mxosmgUAhI11EAe3_r61K7HoZUuySDW0rcMdOAcsPbWy4HZnQmgMd5grfzxQsec-SR7fMnRZn0MITF94WsV6-wGoR3iEHLNCxK54ieZMLY2UMU1ikzTK0tI9TyyavMELqJwSuni3-dkjAuF_672KYiodpIi1kSXoODJglIjcvr7Q2Nze3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خب دوستان برگردید گویا کاور کیلیان امباپه فیک بوده و کاور اصلی FC27 این خواهد بود.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26367" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26366">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3916c5f5.mp4?token=tyHMOQdAWycA6sTyxlHyo9ExOYKLa7ZW7L_g5yJV6H78ysInXpXmqdwVPR6D8op65f05PnsbUKywglaMwWOGrOOONLVVSW40_NX9lUPOEwjQSK7XdjIr_41M_5Ky5lCFzGWNTmlnnM30Ng1TFX_9z_CTJFmGiIKe0kBQo7tZlf4dTRIg9tydbyvc1FzY1TbOvxXnjt2iEl_BZHWSMcYoFeKfIWXfWOpobnmb_JXxZbJTJtk1TEcQfIb9GoFdJIjONRQo15LjVRICakaCs1FdkozqAYmKUbdu0pRxcaFlF99qKs2LWn7UvQ94F2d-b6Y6qRP5bMvxVz8eltNSz8xzi01I6pIOowKsPEEPARZFj3etff2UlV5FN5IMN8Io09KDibO1MC4eof57KmP2roqcgwQ2AsgE3muEwndaFmGi7H1LxPPC1FXnAMMNb7FK9X4o8p52umCWZnakGg7OeEj_q0zVdR8CoYEJ4oo5_ZpJmkENi8yMMMxeZ-WgdUCGezuAi_6K6V9TcJDoldRw3kg7V4OvbGHjC3SjucAOqfEbbIRvafrMngWJe8OVPuZdBasz7mBrmBC6loFkdVh1j-5ef8GzmT3ZMRySPPGhG_dX_Idej9VtmIRqW2Hd5nC-9tug1BhTCGTlSyw8UjTOfvseaM6ujggT-82ZWgWtXFadvBY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26366" target="_blank">📅 20:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26365">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unGyYLy6hAegd0GC-jM4ifYQqQlkZZzCb9wncQTe8psRzl2BzsSAFMoVvEoJwByGWwHoyBcJdlggTQMdrOTY1lumAG-Js9D7jhAm6qjtO-GB1csbCwnzHMtlJN0ERNFbGCBSHXOsCCYsQHI-H8X3w07DV0okDGKgw1oto6FD8s8NYdrutBDvt6OEY89QnQHjg5OUB5yL_0zfDneSOIY956ixyOK5Er8Sp0u5VciecC_InVnAMMEH0wCJrtgMQFo0cX2t2OdjF60eOd40jHkGuhAHt5W8HTljr7AeuUHZ752nDIPdcDz9w7iJl3z089_RHl4fHf3NNsjLbr_XTk6ehg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌جدیدترین‌اخباردریافتی‌رسانه پرشیانا؛ باشگاه استقلال شب‌گذشته دوباره با وکیل ایتالیایی خود ارتباط گرفته که ایشان اعلام کرده در باز شدن پنجره نقل‌وانتقالات تابستانی آبی‌ها مطمئن هست و بزودی این‌ پنجره‌ باز میشود. چیواله وکیل ایتالیایی حتی به تاجرنیا اعلام‌کرده…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26365" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26364">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9TkAfOOzAWELPk8s1n3Bpn-rH3M6TAmSpM6DvFF_mDnNjTYOXFORvp4SFJ7S22uH6gTaANKFEvGyaNmMf90DoFRdyFD9rYXt2J-A8EWQngkQRvFPmqAvgkU2XZmkRK2qM0fs-0PVnvxVg9pCV0YhJNGJYmxyPBVueROIM1uHvPmZam1CG6BEeosxPSnh3EU1Uk7T1nzDvch8a4HGQf-0WDH2N4RBxbmWlXnlt-crKzrgCGlDBwfDqy9QQxzFF5cUWBQtCZMlU4zLMWiR7NziBsDPCYtQZYnnav8BVb9CiHr0aaIBCsXJ1lqhdzBfIl0WDmTThLBgGgiraJaB0AeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇳🇱
بااعلام‌باشگاه‌بارسلونا؛
فرانکی دی‌یونگ کاپیتان هلندی آبی اناری ها رباط صلیبی پاره کرده و حدود 6 الی 9 ماه دوباره دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26364" target="_blank">📅 20:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26363">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bwc-7qyEft1wT-ndxx_hdiVXCU0qBnUEGoxI0WeZ6DX8gpo_OdFnxMb0oH0SPn6vAsZzpyYRxn07UM5ZR_1Kll5C4uXFn1_TOSEiNJytzTz8nvnw3HICAIwgBDPNo0PbOM-LV8qHeN1w2moRgs6YX-WvqmrPSD_iJ1Llo5CHBdt2xvm6VIbE_oaCH81VP1u18fsIFF87e0YnEjg6bgHTI5Zc_x1EyN-5kKj8bBFe8qhqPzNksleGEhzm-MnhfGMJEVGe2y4i3AHcvVhbZCOPn1182OuBEHDhK8WzcVGeM1lF9mADv1iDUkNAShR9HqC3xh-Zx-4oF87zkNY23yBtUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی؛ برخلاف ادعای رسانه‌ها؛ قرار داد جدید کسری طاهری باباشگاه پرسپولیس قطعی و چهارساله خواهدبود. فردا هم قراره پول رضایت نامه او و ایری به حساب باشگاه نساجی واریز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26363" target="_blank">📅 19:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26362">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🎮
دقایقی‌قبل نخستین تریلر بازی فوق العاده جذاب و پرطرفدار FC2027 به این شکل رسما منتشر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26362" target="_blank">📅 19:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26361">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g5eIEcnWQA65ZIy67PMpWw0HZnTE9hCnE8pQlf6JXJAuSk_YUw-e2_1AFXGSmjIeghB-LsQSdgnAxPL8ZBhgs-u_-accrEXlyVAKdZD8UIfXn--5X-kxSWnudiPIIABSgq9X2OqC-t8F6zsh7IEFbP4FpWoaFgkV0wmwOoNjwMhEUOEsA3V-G7eL11qj4lKo3MP3rjxqYTvy0HQZz_gdGtrNgtuJpJNDQCunwlQBRbPIjzYuAhDcEXdDzV4JPUTpNTKBmQk5CeqPuzfphG4DjFa2fqKzXgiaQWDPc4fPsiEzGLevtlNuwKyb1DakPfyvivAR4Fod7Vcu1JrodEPfTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/26361" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26360">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tswsxmnPB6gW0SLtPrQc8UCx2XI4mE8UvcZQ6787-47AMHxEFKgESesbOptTupV-lKveyGITX32U2UNblffmPHffOri-msBDFdKrw1dHymlkWnyP_xvvOQ-1liNLNKPChRm2E4N6f6dfiLxtULZxPrUw4gIN2XsVitpBvjT7lMyj0OTGFW72huJso61eAy1LajeRXBa7Eh8LVzzKljbYKjozl-mUZqEsLV6yFo7Xm84ufRrMvIuqZfkWj7F-Y2i3JqGOyOWrmpJ4wuvC9sdNANRH5b0SfJXfNIrOCQOqEnTiINsrAfaBV4ktgIMsHqzrBAbT8WkE19XHRhFYdtjzWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ باشگاه منچسترسیتی با پرداخت 150 میلیون‌یورو به باشگاه ناتینگهام‌ فارست الیوت اندرسون ستاره23ساله این‌تیم رو به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/26360" target="_blank">📅 19:42 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26358">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3aD-yQv_td-0dLRb9X9WPIU1t2oNZLJNoCX24ahDb3HpNmX_Oj7Wpn_MSEMAlFDF6BG8_5JFgREiLi9ZTMf2_0X43eXETJK8Q2jD3EBJq97ayIGPGcy43jXH-PfNqOxrDkBgrFc2OY29Zuuq3Gxj8KuHYYJc0l21B8w7fz2cva4xW2PjkRherWaBAFX4mO0q4bcqmd-z2-6WElQRdxIk09FH5ryCly3Flwh_q_tFSk2_7t1BqFbx8h80Q9zxG6-eZcYXqZLOyb0RMDyqA9wlKqpHR1HUhevAzQHMLH4vP4FZYbAAT-TbOwcAmaVyO2Q8Xf-HoyrW8k3LWGFkn_p5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26358" target="_blank">📅 19:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26357">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aqO2jwoK0cZc3hik18ZHZRy7TlgkbFS_OG1KUxBxZdjc6o2OY14MOWGbGyN-uUU7GpCNeha6OQRyhxtvc56EYvaExFG9CPHT1ZWVFBUETuNN0313Q7nvxfjLeeIxoGOV9nJ0kIfftFKITD7CcO5wyPqwFYAoiSteMomWVez1Ys2Y2cWEMRb3QoJT_cwTJ47_ZZoo3AzSozFObHeW-EPnhgbdhVXrs87JSLHYySMZzHcAgceiRZGWOSOrn-BUdhRBHUdKhvH7DAtlQXYUHG8eNgezi4XTIs9F43A-hpbQg5QcoXAc1WGc_CPR5N9XzoD86xhOMlRjDnuRmAaPvtMe1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
#تکمیلی؛ کریس رونالدو تصمیم گرفته بعد از دیدار با ولز در لیگ ملت‌های اروپا در استادیوم خوزه آلوادا جایی که نخستین بار فوتبالش رو استارت زد از بازی های ملی و تیم ملی پرتغال خداحافطی کنه. خورخه ژسوس میخواد رونالدو رو منصرف کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/26357" target="_blank">📅 19:10 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26356">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d49c56b2e7.mp4?token=kgdKe35U1HTFKrfD_qYsgKgMrDL2uNnldRbgc4XNjAV7c_LEMDaYsqTi2wCuz3nO85Kloxy2lbzg-tq5GoEyUBbj_Io5Ltf5m4vgRfO6LBMjXqMSQ1w4zSKOwl_HYFto2peTJ3O1FEoUcaIcaf-Qiz9mWWab2O9kGBQt4aJIW7RRS01gOCamAUt8ff3N59cIIueZWQq4m-E3q0npHKMg-eStc-vjpYtAjIzy5t9JCP9TeDFYM6n992_KNjM4dwrXVH7O7XIM5Ha9UT-Wg4WFYlW6yn83DpQW_7mYh8qTUEIXHl67_XvFpCg_ORT4KLM-umUEiUkyvd-7FTucIgKzjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیو باشگاه بارسلونا برای رونمایی از کریم ادیمی فوق‌ستاره جوان آلمانی جدید آبی اناری‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/26356" target="_blank">📅 18:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26355">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d68f1c7718.mp4?token=Fo6UXcc_C_Q99PwzYfF6yGXFDytd6aRjcbzG_bho51epeK0vR3kNRa70O22MXvqV1UPsc-qsYoszcLoBDCWsq8YAOZ8QaC6k8Cs-KV-UoOp8W-nYT2NHhF5bHt1VxK0SGy_I-xO41JvM75ToqNHwhgLmqOTtYQPbTmu9SXQw7mSleTtSuP_4P-vu4h6n_0iDU7NdiR7vDtksXgXV55o4XoAW_zwo-ezqGuJqUeXbH8VA9Je69rHSj4eQc7GTFLCn0UtJqovHi1Io-GXF8cW0jm20Tfxzp3im1PBWoC4dPgn2YngkrgCuUaQEI5PQh1H0IksSZxsBoDNnCi1wmwUC7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
اسپویل‌از نبردتاریخی جواد
🆚
خداداد در ویژه برنامه‌رقابت‌های‌جام‌جهانی2030؛ جام جهانی بعدی قراره تو پرتغال، اسپانیا و مراکش برگزار بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26355" target="_blank">📅 18:15 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26354">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWxmBggWwQznbBepo12YLLjelbnCb8_hPGWlLv4mxlCm8eyxPWE-Fup52Dh7xwlt_2MNU09MgD9f9ag8CuR3DekXx0WQaHDy6x-nxj5E4VAx5PS5DrvFJWSUhCc6QUNWSnyIxPiIyY2i5GkLRdARYzndOUGrO07ZjEKEmCFyDs3_aceDPOqioncQOGSUvOx8KL9eS9qIWlXM5AWiaasqgwzqfjGZ5vviXWBB9hkHv6Zp2S6V200GLKu2bzdiO-POPzOoLZ4klWFd6_jcfBmWqHwo8Vz0p7jo8nV84m6PY1E4TDDQ4o2piifuFtMnXGws8vhEEwijGGkbMwrij_lHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس…</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/26354" target="_blank">📅 17:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26353">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3hsx-5lUESpKLQTlj8idWdTVFXDTttmCSflYHDt1VR3pW4QHnEu6Ww1cbq08CeE6BASxRlcPR6u8fcxY1dBfr3cdMGf7p9zJmim4TUKdi0BPkzD0ArX6jWQua1cnvbNfrLzTPbdHaC_4kcMC-Ab-gp7JjeqcixIFnK7Y8YtMs1UrbiPiIavuFhEi2MO4By_cckpWTZuGVK8TcLOc5c52CJ2x6cQzF2jGqHO6jGUA4CTlYNqUg5tJ7vBXo53s5GJ3GbGuVz8lXroHCHl4J645xR2KoCaStpWcHEHdZmUlMQjvxvj5-dLpQA540KTD_ci5r_x7P2DWMxQfoyHWSUc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
بعد از انتخاب یورگن کلوپ بعنوان سرمربی تیم ملی آلمان؛ درصورت توافقات‌مالی باید شاهد حضور پپ گواردیولا روی‌نیمکت تیم دوست داشتتی ایتالیا باشیم. چه‌پپ‌گوردیولا چه‌روبرتومانچینی بیان قطعا تو یورو آتزوری باز پرچمش میره اون بالا بالاها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26353" target="_blank">📅 17:29 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26352">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgHSp4FQPT5edCGRTVBS4QeTExlLZg2kkiMvoQDm2_uQyxSODprtlQzd-pCi6KasAlo2-Sjn9XQBV7v_9JOuN41texcBtD0mxF_3NPzGZlgJlf9ewYGTkwyUlewLYA0NcSRCiBzKeQZEY3foULEt2hOzOu4rYOQ-3eiA_qQg2YraEXsmBFY9r5VKweY4xzv6Ecgewu8ELjD4PLf9XSMs7cYpjOyjjmGpPWYI4f4khLuzR8pRp5hz3ibNsetVT1slA2rPIPOYMKKiP9x1OhEbkfRdhhybMmvNDTLHmiDaHJd7wHeaMc9ZTVfjJyNzNI5yxza-O6XjFafkSXQNit4u4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
رسانه‌های‌آرژانتینی: لئو مسی بعدِشکست مقابل اسپانیا در فینال جام‌جهانی به هم‌تیمی‌های آرژانتینی خود در رختکن گفت که این آخرین بازی او برای تیم ملی بود. و شاید پایان دوران یک اسطوره در تاریخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26352" target="_blank">📅 17:11 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26351">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/voXfS-YhRjK86VpLbhCrWjLv0xUto9kt6PSW4f0w1YFa8cqfnJVC2FWSw9iSCD5K5gX8EDSz1VDmUcpSZYckxN9sTggw66OAo7EKuKUTzoQLw1yCaxGGHjI72SVtnBNyrZ-NtqcjDCG54ocXjsm2MgoM3e8FNMYJp8CsAsETzp4LN6AHB_jgapucI3iFqwigWBJId57BWwPRq8EJv35KbsM6SEgsab6KYdqhEBLraKYksZGVd5noXwQnPOZH_8si0dvIN4rOyrC3gDQgWs7fGrbiT-hxZqs_XN062NlQzuL8p30MthVhFoprZn-FC3-Rs3lC4cAB4KOnkH862ZgM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
این خانوم دونده چینی‌به‌اسم لی میژن، در هشت کیلومتری پایان مسابقه‌ماراتن پریود میشه و علی‌رغم درد احتمالی و تغییرات ظاهری که داشته، به مسابقه ادامه میده و ماراتن رو به پایان میرسونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26351" target="_blank">📅 17:02 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26350">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMxXLjP7tuytREexuB-ZsYJ_AP4kYCbL_4hqS5ywH7X1rs9yfAOHQ2FUhSfGXiw_M5YxY8ubwh7ZY5s9ff_DJXaB8OGvPIK-L6gueY_6Lp8C8D6TSrima8xIH0iTQOB3wSRS06cjrCImBP8iE4Uy8HfQKB6dP8-IabpwIsfSR-Lk3w1IL0tnvi8pSydox6qlYfD4L6Iz7toQLOo7csPZMQyFtpfinUyuXyQu6EKbavmONuC7bvW2evFviyfRlsYTWxpuXBlTb4K5y3Fn5uytp2yghYU_AAbqgpbdD_ku3OxGavlxdswnzNE2C2z_bTckheNvgrCRuwojdDgoDvFxTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇬🇧
🇫🇷
#فوری
؛مسئولان بریتانیا و فرانسه در 24 ساعت اخیر سفارت خود در تهران را تخلیه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26350" target="_blank">📅 16:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26349">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AjjI4Sz79ysutr64hbWXUgDLfRV8pKIPaj7jOmtST5EI0FF9dbVJScNZgfn8EIDDkxd86CzXkXxkAeXeyOUd4pKtMX-CUwT5XLjaNqyPt32-shXraFYebK_PiDPtez1gaklRx4xvEfoCrUBQePCr5Vy-LXnyRhnQUobPM7M_BRkaP9tSTtWfMJ06NRH-Iz-vrCXoVWjJ-NFmI9zP-xbU9orxrcihpeTYSJBuEtqZIvP1aVrL5xTG9fSQI5G41y6TDX5SwYke_K0UVg4--4kKPz6fNQF_iEfyxRew7eqoS8jbBAkTCI5o1kzuw5CIe5sbJ5QjjfWTrNIyhNKRFfs55g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیوید بکهام به لطف قراردادهای تبلیغاتی خود در طول جام‌جهانی بیش‌از 22 میلیون یورو به جیب زد. ازسوی دیگر، شکیرا 17.5 میلیون یورو به جیب زد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26349" target="_blank">📅 14:49 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26348">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJFb7yQgoTuZtg50X1f2eXsWSiBQM-l4suzT6WYQvpGGmfyQnXal3gyatBAFkg7CgxrAImcA9iRyt5TYOhE_NW0f4RFLtIoN9hH1l-O1pM3L7QvxKCLPAxfXlC2Y2EavJP3dvwKqC0iQiNHoqK_NmoMGurZfNss1k_79mwcM0xOkbLE2aHy1fO16xMEKYAK-xPiJG39_Ee6n7fTitxI_XJTHRDe5rBlgRHB-OX3Uv7bjxy15cBM7CbVdaOPZHL6em9RlcvqqJ3outtzMEweeLWG3ON9a1R7z6wYx0FdGN7hlrWNyAEKDqToiXslBUVAToiaLeVqd_hbaMqaskJtnIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26348" target="_blank">📅 14:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26347">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c13bdc2f0f.mp4?token=oBq67LJqkBl8nD_PZcFwIzbimLlgVt4iDVz2RGFWLyALHgEMdT8hDOW8AIv22gOOXBVx69T_t61fVO4mE2P02HdkJz27FxZBhxQhdWUPtd0ujmcZ-Sq7CFfO0sP1_d6Iy0C5jtpngm9C9s6Jiw_D8gX2HHanZ6bUa1NQj3hWkIvBENh8pxCp2N27Ug4s-aUCLtR0RPQU5GydzPwc4pPZfMuopXy0jx3gkFYAyeb2gU9hArJ_QEgK9EZkoMZo9EfgFaF5olqXRINq7YpnjdIYQNMo3l-K5HCagPfI8Hwv1F9mXDfM1uYJXfzHh4yAtrhSdISuQLqplA_BrOqtRqJ_lQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
دوست دختر کریم آدیمی هستن که به شدت طرفدار باشگاه بارساست و روی انتخاب آدیمی تاثیر گذاشته‌. ستاره‌جوان‌دورتموندی‌ها ساعاتی‌قبل با عقد قرار دادی پنج ساله رسما راهی باشگاه بارسلونا شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26347" target="_blank">📅 14:06 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26346">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWagqnPWTc2Rgnz37aT8k3zGW4d1jGTmGFZ8aIBdnKLNywpsxBMzm5ruXOWctfQZdfNghkhiIaqThmiqEopC-AbRrqvP2cJMHnkbL2WJmCV03IEmtw8BhdBeQF0WtPlSRVbSGl7Q6cmVjwglgNRbZQzD2s_ayPwElYqFM1SwtQjF08X7AfneA-yb2TiBdRgdQzaM93xjsShm9CtK3imDiwF0PEE2S545TUvwancZBhRhq__XFSq3Y3t5gjBUHV9fwlFEh02jwT6USsRfbyI7_0FIQH_TCwRuc5kqGSCfSfK04aZs6zFPxGm1mLTluq8Daa6IzOl1k7E8X0aPwXh9gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
طبق‌اخبار دریافتی‌پرشیانا؛ مدیربرنامه های رامین رضاییان شب گذشته به باشگاه استقلال اعلام کرده که این بازیکن مذاکرات مثبتی با باشگاه لگانس اسپانیا داشته‌است‌اما اگر رقم قراردادش رو افزایش بدهید ظرف 48 ساعت آینده رضاییان به ساختمان باشگاه خواهد امد و قراردادش…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26346" target="_blank">📅 14:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26345">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b24632cd0c.mp4?token=lT9Ff4vYYJG9f8p2HWiVKKJAxp_A3bkD0nV1ij_AThBzUJlG7UVsV5odkh8-KEgZK7lsWFmSfNJ0DX--3aqFynhZ0Gr_KuBt4E1alY7uLWvo_oEcku0Es_HhtyNnd-1fe6oJMOW8UTqAyw3XJwtDnyCuyBAyeMpGcrFJKsLbWjJo21y2Or7aAqRjzG6ppeb8NtAeusM2rNZD-GD2wZ8Z9rcUF80w1b8tbjSh9k4XjWOx4rNCqw9jPyDbtxZG4xal-2dv1g5g-z_SJYXQmI0hpRDJovObcqFTpSyEMPjN29tCT5chJ_DCX4CaRSliSF6WTeD_4lSI8SNt5b7g_yHORA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه‌ بدونید که‌ چرا مارک‌ کوکوریا مدافع‌ رئال موهاش بلنده؛ پسر بزرگ کوکوریا متاسفانه اوتیسم داره. ماتئو درتشخیص‌چهره‌هامشکل داره و این موی خاص تنها راهی است که پسرش میتونه او را هنگام تماشای بازی از میان ۲۲ بازیکن روی زمین پیدا کنه. کوکوریا بارها تأکید…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26345" target="_blank">📅 13:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26344">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rqOZGWiUSsTKHwQC5sB_khgQEj1I-qB4F4oZ3dw_6eLa1D5ECh4Xc4CU6yZlCwhPxq6WGHLmZs-c-an1SCbuZD3li0xHRqitd3HUhyJu64o36ru1yO6SN3tB5aJ-bYJ1xjL8R6dwQssbv47YpECPD4ZgblIXYntaItIHqepBjKzyNe0sqM9ZyFSgoP3b4StOKp9-XOFbcep3JTbFD3F3evxbCyT6FUIRuHvgv2DAS_x8pTVFTEkl-UssKeq97M9f9UjD9XwnOMS9It6Eeu87eUq1TVGOU3LEoXGxADhy3P_SS_BB8IBLmckJ_-cZkagf4ZNO5v0282wLRVIzaipoIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇮🇹
🇦🇷
#نقل‌وانتقالات
|
احتمال پیوستن فرانکو ماسانتوئونو ستاره جوان رئال مادرید به میلان بسیار زیاده. مورینیو از پرز خواسته که قرضی اون رو بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26344" target="_blank">📅 13:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26343">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac2f696a95.mp4?token=WP5cZfMvGM9T-_6xlIrPtU_D5oH9qVTGmzo3wWmnGet8N-u9GtguJKXOiB21rYTveNlQWEDdK5Rl-IMtt4KX5u8gsa1lggxiGnkNe-j2c2I4O3PXw2-eRb3HejzmNfC1wOrgHAIwVrBozNob6p2ACxRaCy-gaw6iRrjreTe3iU1sODyKxPy4pdsD97_0i7M7NY9yyXml1h4OZwB4oY3p_iCbLcTrVir3g1NwvSHXf2c7hDQ4Xc_l78Fy9Cc4sQ4MQOob7wiRPRzbtNyHsA7DucyMJWsEtbj1uTlJSXC9_iK_ZIxWF4PwBS9kZSjn9BbkmTaO6NkzsiR7qMqaRJzxVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔴
👤
💣
#اختصاصی_پرشیانا #فوری؛ طبق پیگیری‌های رسانه پرشیانا؛ باشگاه تراکتور در روزهای اخیر مذاکرات‌مثبتی با مدیربرنامه‌های علی قلی زاده ستاره 29 ساله لخ پوزنان انجام داده و قرار شده که زنوزی 700 هزار دلار بعنوان رضایت نامه به باشگاه لهستانی پرداخت‌کند و قلی‌زاده…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26343" target="_blank">📅 12:55 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26342">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur1OfUBdn70HhtK5vDyYNONIbGvN9v67zx3ogAYV9i3AFjs4_y8O358j5ucieDLgmByhvRPK59j8onOUBztuQnIP11h_QhpYeUlqAZwp4CzCYQ_VUyECUaIxiVE1sDgQOyjNbvtp8hhToYtG_QU6RaYBVq_K0JLBuGVXkR-JVcwuwn2iMI1w5G7mO4dyhaMfjetBZ771dUyOfGnUv7Fn8ULra7UxsGITyJdVmhGtohQBhGGVLzHdBE1jlGenStg6aL7c5AZsHJuioiLNrXpmK_X287m1IwbkvtDKTFfn67sKty2X33__5Y9PeJ1jRHlL6Y-9dbU8ltQbp6jOTl_oNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی_پرشیانا؛ اگر اتفاق خاصی رخ ندهد؛ محمدمهدی محبی با عقدقراردادی سه ساله به تراکتور خواهد پیوست‌. تمام توافقات با او و باشگاه اتحاد کلبا امارات انجام شده است و به محض پرداخت رضایت نامه از او رونمایی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26342" target="_blank">📅 12:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0YfEMtBcAN6j8kBKL0rg85r5yLXXBw53KzHgkdtW_sPJ5vaM0Q_Xxu5hCTOjuI-Oufb1I7VAhiZR4OQdjFs2-lkJVDF0I5REU02uLKXaadiHklrUcwilAi-7Pagg2on8hq_lVrLyhlNTtr__rJZpDmG9G2k2z15RFC2PeQI7eB3eICV94Zi91V-ic6JvAaFjCdZOViVyZZYyDr8k1hFqbAe8eFkEcazAG5vPJszVJTTDXsg8fXO1HRoQheuXPNpzAMAbmV3aXaB7BNnASNKJFDshgSpgIvUh8gzR35UxYpPhGJvbMb6-03yOz5eF1sjdLT_0CZiQ1JLjc-kwzo6sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
یکی‌ازمسئولان‌تیم پرسپولیس: با دانیال ایری قرارداد امضا کرده ایم و بزودی از او رونمایی میکنیم‌. علاوه بر ایری چهار پنج خرید دیگر خواهیم داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26341" target="_blank">📅 12:21 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXddQAdZVQApQvtIKorUJwma3ukGAkc2TKOVFtyDSf6Fzg9L-wLgwlwthCqdXm36lE_eQk3I2gf-0ap5w8xTiga3JyUozxVfLM8Gx2J9df224UMQXDPCn2BoeVf6lDN0OQhwLIZ2EthakqAuA1iTV2fbXe7THs8jPsUHQnOQlpu9Bl6cwYz9GC9q3j8CsZduXQ7oJAHePqAmzaMy38bJXIqtZ4ksr1eBSuQBGm1Guq2GuBIQdReoFaPD6yz0MkxDwEetg2fCo5cfL8YxAhOLmAM0A8B1vjezRZBlDY7qqAKKD13XScSsA3yI2ao7EfIOu00X7w_XJSlZ0OROmfF2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26340" target="_blank">📅 11:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26338">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D6BQ2CTzMycdQfKgUqs1yGsHdzUAqXA6-VdS-F2QcJIfzKQL6M8kdjOf_oCJZydW3-zf9Bz5u4H32hAMhcGF1zpixw82gG6NHDfbuTzUbb3zHXLnUKUMHVPNNGk3swBVWtZuBBlsAUTRXyiFAplekbbiEeeH8YhkF-6m8Rrgj6Is1cMu2_FtSfPku78vJKWYLLDM88clSkJqyXjzFz9h4w61NV9gaHQj2WsIoYYG3Ic-P7btHnJpEW2d7YTJlxCV6F4_L7CKQr7001y0ErJ_FOPejCO-vj1UFzG0_tkmXWPJaXh_3CEidJoAPRPIdYGPf7wtm__CxbO15DvFE3IU4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q3knMjHRJgF-dclwOY-xooqhZ07T1LK2Q1-V_YDoM0QBaJYwWUcibeQVGatf86NOwlA7z-7k_lQ2uNIsTUzWj89rihc2BTfgVC4PnGtm92IZkGAUj9IFz2s7CrpAG4olSo1_k8T-YaM941uVDhu33v--zMCQlVBNUrJ4QIJedX2GlJOGJzGc4JfV7PEmY_RBMYk3bwhjauFpqN2ImYH3CIwm_uxEM7lGELZTvejPzLwoAEwxOoQOnILEzGRDo4RgatkMGGpWJgFA3RLaF3bHyLX3ukRdDddwz3YkW99I_kfUutCYH9bpc-HIXpHSWG2A41c6cloxtLWgdmpz7uKDdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
رونمایی‌غیررسمی‌از کیت‌دوم تیم رئال مادرید در فصل جدید رقابت‌ها؛ فکرکنم باب‌میل هوادارانشونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26338" target="_blank">📅 11:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26337">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUAiyg11op--ytOQghfGqaBnUXCmvMAXbCjlUGQGNKJcdaEyRVRJwf9bsqmDxItU3xiYgCx-J5gCmxpI3L4kJfaTTvyCFuzrTd7YHFTHnhI5i0cxT115r7DzZr7mo0R9YXSai4Z8Fbw9Jq8MTBVBgovmy_4xCbr24hqrBEtAgNPg6AQnK99f8t3Wsyyu6RJMFx3wSxv8UJa6x2-V5JjIPlRB3CkTMO3LJZ8e0ypzavpfy-_c7XaM2JpRzqEZYPYBVOutcFXZaMCKl3wcJiFY4ZQYjb8C7iutXoWm8WFjq70ZMOg_RHPtEPxxH38QsjeiyKr4UysljYXt_WFBbRvH8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛محمد خلیفه باباشگاه استقلال قرار داد بسته و بازیکن رسمی این‌تیمه. دلیل اینکه باشگاه فعلا به شکل رسمی رونمایی نکرده به خاطر اینه که هنوز با باشگاهی برای قرض دادن او درصورت بسته بودن پنجره تا نیم فصل به توافق نرسیده اند. این مشکل حل بشه باشگاه رونمایی…</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26337" target="_blank">📅 11:41 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26336">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=VuyVlP9epd7W7_9El8EXsiwrJRX0Dj3UNEOg6qPKI1heM1r3QkAhKMq2-yuYLgxtOykD--riklYmf9-q5nvBINr1HSzKfw-NCijJNoivG0DRnaaq9X4E9BMZ1NxIjwC82Jkfy6rwovWBJl4Fl3IumOvuwI6gIHaGJ23ZjGN9ldwQ-RmDd6z1A4P1XUwi0nqTzHhnKN7V9GRu2aiTte1XUSCIB3iXcgv5UWjpe_HRElzFWG4ASmhMhAhJ7bo_lGhluykw8FQDUvuZohUfbkcAa9TKz9x3CdxJmD-QCfCtjN0hq8fCnzNcq59uGb31eVIEDSDl_ECx46sNGBMZQ9rH3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/250e2c2025.mp4?token=VuyVlP9epd7W7_9El8EXsiwrJRX0Dj3UNEOg6qPKI1heM1r3QkAhKMq2-yuYLgxtOykD--riklYmf9-q5nvBINr1HSzKfw-NCijJNoivG0DRnaaq9X4E9BMZ1NxIjwC82Jkfy6rwovWBJl4Fl3IumOvuwI6gIHaGJ23ZjGN9ldwQ-RmDd6z1A4P1XUwi0nqTzHhnKN7V9GRu2aiTte1XUSCIB3iXcgv5UWjpe_HRElzFWG4ASmhMhAhJ7bo_lGhluykw8FQDUvuZohUfbkcAa9TKz9x3CdxJmD-QCfCtjN0hq8fCnzNcq59uGb31eVIEDSDl_ECx46sNGBMZQ9rH3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26336" target="_blank">📅 11:27 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26335">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SThEuOpA0Di8fEItz51ERnepYSYwiJkNMWn8Ti3BLHvpL8Bw-vusaXgCOW4MNVa9oc7UoIWb6Nz1tJ0f80kAZKC8nc1Ou3STY0xjfr7N9q7wj3HdyGKsSxTEoFcqcUYp7IPQnM5NGW23dc3w1in8dARtrLvOOWVCTfMF8AnvPGj3XKljy669g3gISR2Wo0U15lyue6thu574U2B5VpeR5e19ICUm0e3I0rD84ylX7b-uFithMKjTpIO7Pd8_zQSL1NLxSMaZw-iornl9tcp9KAJrrSGMLCv7TxDpZwPwBWhv7OYNl-5z5WBvU8uKr2TvuYZ7N1RDKmR7OhGkgmBYTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#فوری؛ بااعلام‌رومانو؛ باشگاه PSG بزودی قرار داد لوئیز انریکه رو بلند مدت همون دائم العمر تمدید خواهدکرد. حالاخداروشکرکریک با یونایتد جا افتاده ولی بنظرم تنهامربی که میتونست یونایتد رو بدوران خوب خودش برگردونده همین آقای انریکه بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26335" target="_blank">📅 11:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26334">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWs9wZ9uzv4O8kUclJKcTlkmEsHog6CsyTPQi7wCKnLqZSJy1pc8BazjHQOy9xBVo1Qk4dLZnQKi1060NbkPFV_pz1bgl7I43w2C0iD7qQoMTeV5QUji-IgCefyMpyu1x3H9uNHApJZCLLNHfUkyRisk2mS9nI4Bqw1u0gfg9BUemerdUTNQdsOEQx21jUpLbvR5nx4OVfeYK4QMrmuPjyqJbX6IkksEO6h-aUOL-cQJhs83HAP0aSgl0KtBWQYKGuYwAyCMDINY6-K97yOJqNxsdfctS8MtSJ4aWVWXoA8Xh0ucImiFsiUlE-G9DO-aDGByofRSsB3FHiag6RNWWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
پیرو خبری که ظهر امروز گذاشتیم؛ باشگاه پرسپولیس ظرف‌فردا و پس‌فردا و شنبه به تریبت از دانیال ایری، کسری‌ طاهری و محمد رضا اخباری سه خرید جدید خود بشکل رسمی رونمایی خواهد کرد.
🔴
عصرم‌گفتیم‌کسری‌مشکلی‌برای‌رفتن‌به پرسپولیس نداره. ایری هم‌داخلی‌بسته وکار تموم…</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26334" target="_blank">📅 11:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26333">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAHtHJhNR5qvSeyP-EoBkZhJKhM8VugqFVGNXB14gNwdaEJfu4cjt6QtrXfSIJGC_vo1lBG9VoYAKo0440vWBFDm-bJ9460ijR0hNTzjNT6zjxEHL4AVq4uiqFEpHqJZHcnXXJk0HGMf3O_FuPgaHeK_Bv1QzZST0n4wYYELc8eLBlEVXUVMbkBqirWY4tvDKpoRlB7l2XTtaN3c2-He5xZGCzCekBgm4-t060mjngmVbQn-QQ5zEOs3z7iwsCqhFQbOarCcAGdn4_2dX5xiMUcnNwyM8Zz0DuR5fqS0kip5wKaXLf1xW0SToXoD9U8V2cqpEIoidkjM9vWf_AzhAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
اسکواد کامل و فوق‌العاده بارسلونا در فصل آینده رقابت‌ها؛ بایستی‌صبرکنیم و دید هانسی فلیک به طلسم 12 ساله قهرمانی در UCL با این اسکواد خاتمه میده یا باز هم ناکام خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26333" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26332">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR0PBcJBRWh2SSQEB-RPFwWrTItKxEHg1Oi6VI3BtBIS5PLAUU6EP4FyIg5NJCDziA14cqd_os_V5bWQo9PfaZz3DPxZJT94DDcE6P4qb4Q2kuekLLP76mwCilpG2AcpaxWFdVehoWbQPGpqfRk5rOcbCf3FWAJey06HWqhlsGkSLYP991WAbvMrHyMdll6upgWhIu4LUoJUbmOpEdO4KI2Vl0xFd4QKG_x68hwD0gTe1p2CDSqshj023dPctuYi-jMnnrSzgMk5I1TywkhHkza7iD2jvLpU5usxFyorXKPy6UGGFNN9Vkf4TUpAJ62fPB6yD-0xsw6sqSshjWsmE-gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bc429eafa7.mp4?token=TdWHIhyGwpSPsZKR1xDneC3MBohQH2D8wiwKmZQTUyZ7OMNH9Tl5moTXxIXb2vUtzch0YX1HQFNTW5Mxx0hMJyrz5Nn11uEI1CDfHiiPnlzHMz4s7JC_NAHRYvbFjUqIQADEsUOrExn8deFWl_BDyxfhH1USILf5_ATyeDhd2rWiZWjbE3BgFjdjyp-mqJU_Skq7Kl281QojfES1wv3FCs0hSjBeF4zHtREDNAEf5Bdk_T4cQqQlJJmykxsNTPFoIJ8l6jHKaheXUf8SdUgM1xU-2CRbfPiJcsCpBMiQeehV0nieshPC7nIRrQmYIChXkg594cjij1OJKIs2dlcxR0PBcJBRWh2SSQEB-RPFwWrTItKxEHg1Oi6VI3BtBIS5PLAUU6EP4FyIg5NJCDziA14cqd_os_V5bWQo9PfaZz3DPxZJT94DDcE6P4qb4Q2kuekLLP76mwCilpG2AcpaxWFdVehoWbQPGpqfRk5rOcbCf3FWAJey06HWqhlsGkSLYP991WAbvMrHyMdll6upgWhIu4LUoJUbmOpEdO4KI2Vl0xFd4QKG_x68hwD0gTe1p2CDSqshj023dPctuYi-jMnnrSzgMk5I1TywkhHkza7iD2jvLpU5usxFyorXKPy6UGGFNN9Vkf4TUpAJ62fPB6yD-0xsw6sqSshjWsmE-gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
سوتی برگ ریزون دروازه بان تیم اینترمیامی در بازی بامدای امروز مقابل شیکاگو فایر؛ اینتر میامی این‌دیدار رو با درخشش سواری سه بر دو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26332" target="_blank">📅 10:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26330">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=Iq9vW2fFsg06-yffxgpISXRivBpqAFxQSLKlUG59-cZ7u90F6ODDXbgsfXfMsUzw9yf9CyihSX_0vSJCBJdegKfqHe-cp8aObUsBv-ayIKl2stjpbkIFGLV-y9sa4cPLOlkMUp-QJNwhsO-A_IMWj575PxB7BtbMeHMza9JzptU1o40q82iKPYzrnmorUSQNE56pVdA4MwyNQqLhCwVWZwxrt7mUrV1fEdxA-catRBj3OKM4gm9ejmgxKN0fJ_icA4JTadJKimNMOhv1j8mw0xJh30Oj-cYd8Xzsvs9PLTNz-dRjlSd_AYAhMbMt-ZDAWLvLIKPXEn9Pauul-2E3_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/967d8465e2.mp4?token=Iq9vW2fFsg06-yffxgpISXRivBpqAFxQSLKlUG59-cZ7u90F6ODDXbgsfXfMsUzw9yf9CyihSX_0vSJCBJdegKfqHe-cp8aObUsBv-ayIKl2stjpbkIFGLV-y9sa4cPLOlkMUp-QJNwhsO-A_IMWj575PxB7BtbMeHMza9JzptU1o40q82iKPYzrnmorUSQNE56pVdA4MwyNQqLhCwVWZwxrt7mUrV1fEdxA-catRBj3OKM4gm9ejmgxKN0fJ_icA4JTadJKimNMOhv1j8mw0xJh30Oj-cYd8Xzsvs9PLTNz-dRjlSd_AYAhMbMt-ZDAWLvLIKPXEn9Pauul-2E3_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌مهدی‌قایدی درسال‌های اول حضورش دراستقلال: رحمتی و حسینی بشدت‌باهام بد رفتاری کردند. تو یه بازی درون تیمی به حسینی گل زد گفت دفعه آخرت باشه این کار رومیکنی‌ها! مهدی رحمتیم گفت این کار رو بامن‌بکنی شلوار رو از پات در میارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26330" target="_blank">📅 10:05 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26329">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=oHiUWKnFFcclPIjC6yulCpRgCb6yKNKG2bd8TuHn_Oyuguc3bUWMrjsk0rHZqdKdIUxfgw3lhqsFcBEFLQRjuVWdcRi7v7cmLsOAEf8WKkSJJvfcC-soHKyIBie0sNbDGJ7EtneC5yDG0C3LqgUcKuk6gHIEGKkVBriSwcIgVROgclZAQ65aDDul5AOQb8rjFAyLV-3RW2LQADL2GDtJedq8vJNgKY8cx_bocSBH5KVH-x6Ujzjwda9IV-SqFkaPzsDrPlPd-qFbDbRQH0GaGjiEt0nzPk_0UiShvln3IqX3EOg8yBu03KaevXlsXHYgE7Tx2uxAt-MFnJRC9kOdpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a30d0e41d.mp4?token=oHiUWKnFFcclPIjC6yulCpRgCb6yKNKG2bd8TuHn_Oyuguc3bUWMrjsk0rHZqdKdIUxfgw3lhqsFcBEFLQRjuVWdcRi7v7cmLsOAEf8WKkSJJvfcC-soHKyIBie0sNbDGJ7EtneC5yDG0C3LqgUcKuk6gHIEGKkVBriSwcIgVROgclZAQ65aDDul5AOQb8rjFAyLV-3RW2LQADL2GDtJedq8vJNgKY8cx_bocSBH5KVH-x6Ujzjwda9IV-SqFkaPzsDrPlPd-qFbDbRQH0GaGjiEt0nzPk_0UiShvln3IqX3EOg8yBu03KaevXlsXHYgE7Tx2uxAt-MFnJRC9kOdpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
بدل ایرانی مارک کوکوریا ستاره چپ پا تیم ملی اسپانیا و باشگاه رئال مادرید هم پیدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26329" target="_blank">📅 09:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26328">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=k2qNcB7szteXrD0FmJS-PA_ZuuXzRvHpTgxmv1TJ2bgPvHDOBFqZMhVgzrIqH3Az--RN8VAwm8EP_R3Z1knBHF7THNfTKHdULy1dex1KjaBpg4waeSCztPHV-RP6XjDjWy6F276i9-MH1ur8MdkJKPK1hbbI5coO0iVMl3k0ZAmQNCam59p0nCxS4E9mHmR5s3mK3yqtCVQUxOT0LUU211C5WdpU4-DsuYnore2JcUB5O0ZafsHYTm_RDeSLMfkUgZnDaFS6zHobwt-CrNxO2L2AYssKlEchDzPC_jCEgIjZX71ekkU8mt1TwwDXZiWE4atSBEPN6wgkhXfJOlzBPn2echTBKaxBo8Kw_ZpO9edPnWDVrl5x338h3j-XOlzTlutzpd_aRzSbS2GlUpXEyWjGx8o9gA77jnqzJ6HtuiIm0ZA9qAOCMBHa89mITVNEaVSWYXlC39507Zj-2xG9sa7mI9gcnlZUaxM8vitlPqJbCF1c-NxNqXcC5vjBCyv0nafv8lRFZZ9zPovd7ESynOT8ZjU0R0lmdh2KbW8R-kg23OhFFfnSn-w2vzSMA5pno2w4e3SUPOk-UE_uEI92lD8uTwMI7PLs1Am5wmBZ2Nj32ECAsQk9ghfY-P6MyPiFRI1jxD2dSlXys2kddHkUAhOFvm6RDcJDwcAZsv-xNtk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88237cb2df.mp4?token=k2qNcB7szteXrD0FmJS-PA_ZuuXzRvHpTgxmv1TJ2bgPvHDOBFqZMhVgzrIqH3Az--RN8VAwm8EP_R3Z1knBHF7THNfTKHdULy1dex1KjaBpg4waeSCztPHV-RP6XjDjWy6F276i9-MH1ur8MdkJKPK1hbbI5coO0iVMl3k0ZAmQNCam59p0nCxS4E9mHmR5s3mK3yqtCVQUxOT0LUU211C5WdpU4-DsuYnore2JcUB5O0ZafsHYTm_RDeSLMfkUgZnDaFS6zHobwt-CrNxO2L2AYssKlEchDzPC_jCEgIjZX71ekkU8mt1TwwDXZiWE4atSBEPN6wgkhXfJOlzBPn2echTBKaxBo8Kw_ZpO9edPnWDVrl5x338h3j-XOlzTlutzpd_aRzSbS2GlUpXEyWjGx8o9gA77jnqzJ6HtuiIm0ZA9qAOCMBHa89mITVNEaVSWYXlC39507Zj-2xG9sa7mI9gcnlZUaxM8vitlPqJbCF1c-NxNqXcC5vjBCyv0nafv8lRFZZ9zPovd7ESynOT8ZjU0R0lmdh2KbW8R-kg23OhFFfnSn-w2vzSMA5pno2w4e3SUPOk-UE_uEI92lD8uTwMI7PLs1Am5wmBZ2Nj32ECAsQk9ghfY-P6MyPiFRI1jxD2dSlXys2kddHkUAhOFvm6RDcJDwcAZsv-xNtk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
واکنش مهدی قائدی به حرکات عجیب و غریب قلعه‌ نویی کنار زمین؛ خودش از خنده رود بر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26328" target="_blank">📅 09:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26327">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=Xy-jtGqR67tvAcGQJhzpXmOVWCgsbnFFPH95T8Jk5LEVDhfaJk_z3ourC-AAasiHzrxATtbfqt1tESjkcIGgefvKrt8GMg-wdXWEJFSp8b5H9oa0K6hDByQ2G_3NP6UeO_Zu1VQBwq5CcaJDn84dGi399RSC-iAnrqQQ_bEFlekrzzgN9v0Ef1u1i_fg8-5O7m46TXAta02pQKC1V6j3arXf1G71mvjXMLUMVNqslkpTptHkwOubbLQLOdpdOwrsHjP02Jf10Yvf3iI1i3TYsYfW6-fRuQ4kqEYdjPa-y_U9Loz9Xq43MPx2YZNJCPA9CYu1No6BhF16CSFl2ay_7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf26064c7c.mp4?token=Xy-jtGqR67tvAcGQJhzpXmOVWCgsbnFFPH95T8Jk5LEVDhfaJk_z3ourC-AAasiHzrxATtbfqt1tESjkcIGgefvKrt8GMg-wdXWEJFSp8b5H9oa0K6hDByQ2G_3NP6UeO_Zu1VQBwq5CcaJDn84dGi399RSC-iAnrqQQ_bEFlekrzzgN9v0Ef1u1i_fg8-5O7m46TXAta02pQKC1V6j3arXf1G71mvjXMLUMVNqslkpTptHkwOubbLQLOdpdOwrsHjP02Jf10Yvf3iI1i3TYsYfW6-fRuQ4kqEYdjPa-y_U9Loz9Xq43MPx2YZNJCPA9CYu1No6BhF16CSFl2ay_7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این گیف عالی بود؛ امیر قلعه نویی حین بازی با نیوزیلند بدنبال‌ساعت گرونقیمتش بود. مشخص نیس کی ازش دزدیدتش که اینجوری داره از هم میپرسه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26327" target="_blank">📅 09:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26326">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5PNhTCggxUUubjDgzgYpNxjGibQmNBHKvBUP-UW047k0LLZ84E-lKk25AGxxMfTAyJ4jOxPKUP_9LhRuPwmBMVdYQ68rqQ3hvQm_73fMEXQ0dLLZr-37wh4yvnx1p9bZe3UYq1yzQvmu-x2i2GRu5W83_IsGqYHI6enRqP0xJHY1TrxmSLo1TQ7yU9HomJjqveijKKosT5ohDl0Eg6cXGGhPPicmituo-m-rSWVvzlaDVMnu-_3Wo_A6v_bCx9E0AJfKCqBhpabuD4G6_qqj8l95cVCe5iwUYLuXyFfX_ayWtooV7h9MfkzhQ-ASba9PaO_t8kq0RItN-MErWSMnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
ادعای پپه آلوارز خبرنگار رئال مادرید: من با شما شرط می بندم که رودری بزودی با قراردادی تاسال 2030 با باشگاه رئال قرارداد خواهد بست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26326" target="_blank">📅 08:51 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26325">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=WGdL7ClLnEjJha-I82UE5FdcZIbQj0D_geej6C98EdOO4v4nTsUW2oU35qLn10xywlsLhWUuPt0SPYmL7JS47tqk-pmnBNZdjBc7ctiD-GVFE0m3KoflWxvCz1KyAmpj-FYgBwAwyXPPV-hJCs24kp_0qwWza3UJQzkWRqnRGOGngcDC4O_sKSTpy1HfAN4O74e6c56lsfSwhnlJPPdrVTIQezJvGqqUGSlOBF7Rlbz7OXqsEbjcAL2qiTjrwBIyKGkcOjNT2N7nCUXsu0vmzD34-bWgc2GNkPuMvrYIx-FqsFXmquPvHUqtdEw3AW_iM95ATn3u2m9Dex522v-6yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00ffe3dc96.mp4?token=WGdL7ClLnEjJha-I82UE5FdcZIbQj0D_geej6C98EdOO4v4nTsUW2oU35qLn10xywlsLhWUuPt0SPYmL7JS47tqk-pmnBNZdjBc7ctiD-GVFE0m3KoflWxvCz1KyAmpj-FYgBwAwyXPPV-hJCs24kp_0qwWza3UJQzkWRqnRGOGngcDC4O_sKSTpy1HfAN4O74e6c56lsfSwhnlJPPdrVTIQezJvGqqUGSlOBF7Rlbz7OXqsEbjcAL2qiTjrwBIyKGkcOjNT2N7nCUXsu0vmzD34-bWgc2GNkPuMvrYIx-FqsFXmquPvHUqtdEw3AW_iM95ATn3u2m9Dex522v-6yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
تیم بارسلونا دربازی چهار آبان‌ماه با رئال مادرید با این کیت جدید به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26325" target="_blank">📅 00:44 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26324">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851f45a809.mp4?token=ia0o5FBiHH1lr-TlRryGK-4mBiE_SHQ-4UhvLkvCh0DT1kzMraUAZS8kdNI7FYU76XXqGyhFLZr35zVi44axY4BehffH15eWbaSrVX5c7qc2GxCw8Z4UbpqYFWOjtiaHo7pE2zrR5fz3WhB8JCNK0e3isFLMv1Bffx28H6KxpLPv2vcpFR3UzvDS7-m4AfVHnJQ5HfAxNsv6otMP6UpGdBNWUtbshh1ZLHFGqb2BbObChKV2J_jVUiJ8UbvamQZ9B2pAPf-7WWw_llhlc0x-pNrN-FBaPv3GUkmuHsPKF2PefBYbcSiBk2QGrMJkcKBrQytySaOCctts6gVgtNfVHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851f45a809.mp4?token=ia0o5FBiHH1lr-TlRryGK-4mBiE_SHQ-4UhvLkvCh0DT1kzMraUAZS8kdNI7FYU76XXqGyhFLZr35zVi44axY4BehffH15eWbaSrVX5c7qc2GxCw8Z4UbpqYFWOjtiaHo7pE2zrR5fz3WhB8JCNK0e3isFLMv1Bffx28H6KxpLPv2vcpFR3UzvDS7-m4AfVHnJQ5HfAxNsv6otMP6UpGdBNWUtbshh1ZLHFGqb2BbObChKV2J_jVUiJ8UbvamQZ9B2pAPf-7WWw_llhlc0x-pNrN-FBaPv3GUkmuHsPKF2PefBYbcSiBk2QGrMJkcKBrQytySaOCctts6gVgtNfVHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
صحبت‌های‌ابوطالب‌حسینی درقسمت‌آخر ویژه برنامه جام جهانی؛ هرچی تو دلش بود رو گفت:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26324" target="_blank">📅 00:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26323">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBMqoahe9Uzet8fBRQam7F0Pec2sDDcXSazl4emNAiuNr57nBd_gNRCurZSbF_o_GZrOOCV5qhbapKzg9kvRd22k-Oq54w4qB1Fz9Xp97q-cdzPDncOFFQ6f3n9szRGgU63AatYFintj7JWbGSa3R9tiryUdwC0zOwjOLddwkAldf3xptSxRXfWUxQRj9L9-P90qYqRgre4ibikWPMump9G_5ps8b-PT-6F9HqyJ0RIpk1dCbd5tYYDaXcGfSLjYUBchxhzlYIVPvNJyDPzEZcVWpdfFdCtPz-Nlg21O2Kq4kqO0jnRZJbEWKrUojLiGFzXZ4UvFiAYzYlUSDlZFVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ دقایقی قبل استعلام فیفا به دست مدیران باشگاه‌پرسپولیس رسید؛ فیفا رسما اعلام کرد که هیچ‌مشکلی‌برای‌عقدقرارداد کسری طاهری مهاجم جدید نساجی با باشگاه پرسپولیس وجود ندارد. حالا باشگاه با پرداخت زضایت نامه طاهری بزودی از او و دانیال ایری دیگر خرید خود…</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26323" target="_blank">📅 00:24 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26322">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=fLJr6FERm-ukjZuCi6-iLojgFg8ehcuf2LNXUJiyKHtl-wj4BjgmyalKYJQtufTLEiUmhUxCMqnkd12e5BCU6u5nUu-M-LBPuE3Et9DG0ao7rTYtOpOYko7evafYKzslg07XnrCXDxo_qM9owPjIVZn2qbFrh5ASy7PeUEvA2UqtaWscjemNX5SJ1qvL4FnaOV_cSBnZGxRuuZsm2-kkmr8TukJEd14d7_J0LuTM8OpfT2iX2nkSkBbRCZ-E_7fioX3mb09Bb6C28ye2YRgaYec-CLzmnw-qxJs6REKsV_4pLIWbrJLY2J-X60B5oyIuv_Tn6k4HvBYfuOHLnnNMEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f7044ec9ae.mp4?token=fLJr6FERm-ukjZuCi6-iLojgFg8ehcuf2LNXUJiyKHtl-wj4BjgmyalKYJQtufTLEiUmhUxCMqnkd12e5BCU6u5nUu-M-LBPuE3Et9DG0ao7rTYtOpOYko7evafYKzslg07XnrCXDxo_qM9owPjIVZn2qbFrh5ASy7PeUEvA2UqtaWscjemNX5SJ1qvL4FnaOV_cSBnZGxRuuZsm2-kkmr8TukJEd14d7_J0LuTM8OpfT2iX2nkSkBbRCZ-E_7fioX3mb09Bb6C28ye2YRgaYec-CLzmnw-qxJs6REKsV_4pLIWbrJLY2J-X60B5oyIuv_Tn6k4HvBYfuOHLnnNMEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه چیزی بهت میگم قول بده به کسی نگی؛ دو ثانیه بعد: چه میم‌هایی از صحنه در اومده. بازی قبل اون حرکت مسی مقابل بلینگهام میم شد تو بازی دیشبم این حرکتش حالا حالا میم ازش میسازند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26322" target="_blank">📅 00:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26321">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
ویدیویی بینید از پاس‌های فوق العاده هری کین ستاره بایرن؛ مهاجم‌نوک‌باچنین‌قابلیتی به یاد ندارم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26321" target="_blank">📅 00:14 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26320">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViPmD5yfFM_7RvOePMKZFMp6-wt8gz3kqWAZgn3yOe2Hh3rGSspwSfGNeuA2fd0-GrqyMxOmmxsj8yJSRyuHNQPOGaU4jeryW2RXixnF5RFT1cpwI_OMj1kUuceefUe9SjuPcN5U5BcteEZ6NMpBC44viyL6tSLXDhrXUtSoE5IQht9DE1fh5psvFCDPbsu04KGSCp_O0NIT2FD83Ypv8HZqyZuTGUKi_lE1SWCqvvClIglFqe3cRMsIIe3M6hItfCJIDXMjwvg9sXbG24xJm-Lgz1Bnj07dtj1nm4op6MNZIIm9Ahs4LwQkr0bhdmOzzGN0tRKNy6n-FY3epFmqxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🇪🇸
رومانو:رودری ستاره‌اسپانیایی منچستر سیتی تمام تلاشش روبکاربرده تا در این پنجره راهی رئال‌مادرید بشه. رودری حتی دستمزدش رو به شکل قابل توجهی کاهش داده تا این انتقال نهایی شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26320" target="_blank">📅 23:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26319">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EEPSz8JKThjT32_v6PVNHOuJ5JmVGHn-sDQHpPWVGD3ifD4x5iK2mgr_TkLZKxxDTQBjLOBq90KnuoguRSivyZX79E5VQEsiQhuS2S5EUqQvttTevPXH8S9FQzjw7NqLRSreqG3jGLnr4IYOuqTJBhSFdbHBp0aiy6b1tAviTv4kivRtJqU0ElIwTWeOIJdmKSlFdqrmy61V8PyKtVaJVLp3pQjnsO_g-x482cmyd_b6_nIpuNkqL0JLpLTCYoRKyf52HpbYQCXAEwRrXNAzSf3N3depUh3nxpbz5HEgQY4Fr8XiRK7vHJGqtxt2trS8qsSfz0CgElXlLO7ARIudFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خبر اختصاصی‌پرشیانا تایید شد؛ تاجرنیا رئیس‌ هیات مدیره باشگاه استقلال: با مدیر برنامه‌های یاسر آسانی اختلافاتی‌ داشتیم اما درتلاش‌هستیم که او رو به‌‌تیم استقلال برگردونیم. آسانی فسخ قراردادش رو به‌فیفا تحویل‌ نداده و ماهم‌امیدواریم که او رو راضی کنیم برای…</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/persiana_Soccer/26319" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26318">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uwg_8b71nC1TgrsiHY_c__MNc8jWMvYAgXfDjfvka0-YyVduiWkW3Y6q5_4f9XqnE3ctsRAnAzpz_UYvoX9YgeCeTmZm7BIHruBeXlTdIHnFZHJvxWtOBDwDu4DcZR69haulllTu2nxPZe7Lx4NMOkTijTUlFSbFZjZddy3zQAxV1IBrQmdeWvBNhDiDVGJOPhHp6sOeRwE38Rm0UqM7I8gkJXKb8IdSCOzoaAsIqYrgB_ijrV1KgYD4GpUReQiRxtHd70NcNCwjTisw6VViXbv-arkYabKWkR7vNAUf27a5L_q_hPX2zK-CmdIXNvhgCuy_BVnquh2gdH1ARYHi1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔵
#تکمیلی؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مهدی گودرزی رو 500 هزاردلار اعلام‌ کرده. این مبلغ از سوی استقلالی‌ ها پرداخت شود گودرزی 22 ساله با عقد قراردادی 4 ساله راهی استقلال میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/persiana_Soccer/26318" target="_blank">📅 23:25 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26317">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyAfho0E0QyrncH9jSGq4auopxPbpByrEl7x5kdgSPmBlb5OUH2IqOphGXy_mZBEfiLTznIKR4xNN-Yj-QROzTHLk-nHMUnfdICp0Hw-rDr5AQzhHwiJAl_-zow2jiLigwiCuKIY307X9HQTdU6DLMi48awnN2Tqp2ZhkO6idqCCFUnSL6CUc3gfq0dxYkuW118ycqEaZdFsvm7tD8fzveRu_omTok7TNwthqmId88oMasLVTV2EiiDjIlikK04ifIxcvWTmH96N_NnWMVqZW8tNMPVWSicrhiMdA4rmWYDIHMUQOM6nCV4nSkY83MnclqsXFCXIUfoMk-IXqIPDXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
آخرین وضعیت دو خرید جدید پرسپولیس؛ محمد رضا اخباری صبح امروز به پیمان حدادی قول داده امروزعصر یا فرداصبح برای بستن قرارداد خود راهی ساختمان‌ باشگاه شود. دانیال ایری هم دو شب پیش‌باشگاه پرسپولیس‌باهاش‌قرارداد داخلی بست و به‌محض پرداخت رضایت نامه از او رونمایی…</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/persiana_Soccer/26317" target="_blank">📅 23:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26316">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iufSu4jBXjzCsYhBAOngrfMxRUAkMSAMIepvZ1RvYlgeHS4K3elLXvc5ikl1kGYXP8STjlepxgUTv6LLo867Gl17FkYVRPJUsD4A0j5cFJAl-DEiB8ELrn7gpneQ0nHC0gX6n4DHHocpwM9SLjUW526xfJNn6hTSeuyDmbD2wy6QtMleG_0aOWQz8SIlHx79dbTN7xm1YbsitUgLxb6AxJariFo16RmzpwFkMs_7Gd8gCJLe_vg5zp2UZvg6TtvkjOHYQtXnqUgv4MZvVuhjKGjMf3MYUS3ACYS2vAg1rjxFqVFSIViUUNwD5lKxlT3cHPZWOUW4V9pOGdHltG-2hA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق اطلاعات بدست آمده؛ قراره امشب یا نهایتا فردا سامان قدوس پاسخ نهایی خود را به آفر باشگاه پرسپولیس بدهد. مدیریت سرخ ها پیشنهاد مالی سه ساله بالایی رو به قدوس داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26316" target="_blank">📅 22:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26315">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PphuGoWthF3oiHGf9pv54ZiViO5SJO4D_aS-gTB0xqRiv6G55XHLS0qXc_HuSU7np6NbuKrKWexSIEDXAFLJPBWbIjYn182HUeGCMhfUevodKtczeZso0NFkbbIbRh3hJl8_iN6EatlotKKg1EFOpnqe1FV9dz4rtt2iIk_Y0RZh-OyZ7ys-me2X77-HjeVBvnm7dAt3Arz2VKTS0dEj6qRkRSTUTjMFnUz82PTyKSG4iM0_IhdgaEUh09xZnpKS8GG_ktZj1zJJAMaP5xSaWkh8CRxmYm0CjS6xEkpsSbJvpDfb6hD_Z-xBK7r2txuKv_TEnOlFUYihQDZBTMIUWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
زین‌الدین‌زیدان‌سرمربی‌جدید تیم‌ملی فرانسه روز به روز بیشتر داره شبیه بهنام تشکر خودمون میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26315" target="_blank">📅 22:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26314">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDadMxYYZE5C_L6JUd7ct7EaAlre6nsbgrhqgi_EC3CZ4btUTs2L3ieYGRWIb60Y21OWyFN7-BHjBP2PdhmdRP1W9ij6oJP_3NRwF3_LvmHKcwyXOblDR8ef50p6VtprRGO-M-H9_qUoyxM0MoQgzbfokm3QqJoBIFYTwduFBlPqxH3Dl7IDC9RQBbkzareqdy9UKC3XoDY_9rWc_QfYZ18Ozb3eczWjzMvWu8g89uyPU_KsueVKpo4RZI1wWMF_-Zk3MWhj-T6hMmcNOO_4r8TzSoNwFBJnfb8gYiD_UKj_mLRAKZHB2I8c-sHB_nmeKBs8saV-UqnynQpoZZO2kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
خوزه فلیکس دیاز: سه هدف اصلی فلورنتینو پرز در این تابستون که قولشو به مورینیو داده: تمدید قرار داد وینیسیوس جونیور، عقد قرارداد با انزو فرناندز و مایکل اولیسه دو فوق ستاره چلسی و بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26314" target="_blank">📅 22:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26313">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/roZ6MjaVkX-dF7t2W1ZdzhFUvHL3yBdW5bSysgsi9LGvzjR62SSEFAVRZ8jgM4I-4s-qOjcsRoJ2vsil5ixS6NCBbZuu4JYtxZCUSvigID_ID1ZCmHu691maLOSe6ONG1X7KdwzRD9ErDHsi7e7IiBFNFN3l3tXKgngI2PRDVWsqkTgosdy4TeMmgXl1gbJ6QJNC1eSX48hBRbu9OibfU6LnFEWuGbO_WrLvHGPVeFvVOkjf1ic81eQLHjEbsjlxaytp4ZAlz035jKwNjRl-nNxqF_-t2sT1MVhY7c323fo55qIpReUsjCdpeUesmRbG3gn_Rv2FMNb1DdoZtRhs6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👍
#تکمیلی؛ تو 1500 تا فالور داری. دختر مورد علاقه‌ات باهاته. 5 سال روباهاش گذروندی. اما ستاره فوتبال کشورت با 50 میلیون‌فالور، یهو دوس دخترتو میخواد. دختره تو رو درعرض 2 هفته به خاطر لامین یامال ول میکنه. حالا در کنار یامال جام جهانی برده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26313" target="_blank">📅 22:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26312">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzPylOdJeRaSrUCTdI9nDpo7ZIV_tPoGRVVcA2ffpQaCVXb2YewiIyG0L7FURF131LZw1pYpvM0QnVCXhrKu4WltlIXgetixwnIKSMyuM96uD424rqztpPuSYvK4GhJ1Y8nMkGz6UgLCXHlqmNv4uEL4gWHhgWXLiVXYFDa0nB1yWXdu7eIvnP--b2e3lOrmqXJp-Vdo_xizKdAKMfuyrX4QzJqqIpUEZ3wxUenCfi_66WpiX4Sv_hPgpQcP04it1kyU2Q9Tz5wWQaUpKRo1woAssUwcYufjwdQVJkEIc6T-MyIAf8hRzh8b14P3fT6ycKt8bdwbSoqEPG1GyzAFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
فابریتزیو رومانو خبر داد:
کریسنسیو سامرویل، مهاجم 24 ساله و هلندی تیم وستهم با قراردادی به ارزش 55+10 میلیون پوند به الهلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/26312" target="_blank">📅 21:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26311">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsmsFNn28xebGx2c_zKlzIxmnrp5MY-kfCdWJWodAcViCqg9z2VPX_YE0HK8NiJ77ocd8OhJ1Q24rE6lwtXiPN641oLAXcFoBJZm2O8N9w79HLQKHy-4cBcNfi73IHGTH5C_osfCP1XbdMPafiCxUk4okYKKqcDl9LEc9VM4-XFIFqxhwvp_cN7jaFHVYHNdNr2GdsPVpVorPfwGZLAWSzDFjXEqDbANScvVcH0-gWpTkyen_YBPSLstoIzs3ZtFPcX0weGv4tjuzWhR6XeHTDbw_zRvA1_wdLhWh9TVMKH3UBMG7zTYy-o9klmmCT5gCly1fwMFGdW5Y4Jrq_irbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
محمد خلیفه امروز عصر با حضور در ساختمان باشگاه استقلال عکس‌های‌رونمایی رو گرفت و بخش رسانه‌ای باشگاه استقلال پوسترش رو آماده کرده و فردا در کانال و پیج باشگاه منتشر خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26311" target="_blank">📅 21:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26310">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h1yjuNyClLzJ60auPK7xrEBJvpJczXxkRlIyPZIGkgVUGLaHZygUz1hxRSY_DEtC3zToTqtoQfsNeZnC_HqFHxt182gsfU0gkiq3tBoSz8BaUMOTTKo1dAoq-rPl-t5l2iSxQ5uDOHNTNcpjbTqcFFxKW_z4C1ySuUCkDiQIwyOn2twUHY3Crbv8Nc15Z6S7vgrMIK7_1sQPE0BJh0ij9GrgCxZG7YQU-fycfgYgatw4FpBK7on0xRiI2Ul4Rm2NbEUzPvafdqfTRwI9zWpJ9FI4S3wt0RZadM-GUI8NQi_JLdIOLt6ntEPpZB7iks9RhKZ7YkU8BTKlqj8LQT-60Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول و نتایج رقابت‌های لیگ آزادگان در پایان هفته سی‌وسوم؛ صنعت‌نفت بازی پایانی مقابل نیرو زمینی رو ببره‌میره‌پلی‌آف اما اگه تبره و سایپا بتونه پالایش نفت روببره سایپا میره‌پلی‌اف. اون سر بازی پلی آف شاگردان مجتبی جباری در مس رفسنجان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26310" target="_blank">📅 21:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26309">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZmsxrqnhhDn-GFObNvIoZj2djfO1BXUNPDvovOXfeSye8Kxw7oTtNHFy8NaCI56H_Q674bb_Lb4P5zQ-Lwv1eKTW-uNuLR3jzTa59PU_KLh4-3DTllzGyoafxUu-fDxsuAwLVqAAi_5_hpwV8PPDRejA9cgYmslZLbeBeSbHY_1e3bfO1SNhmAAkRIzNhp9wc0w3A4rJZy7TtLgJ6oTCQszIpu0HnbJe6ANhtfFUXg6455GM7iD4PXMS9ZqKC00iZsezjCfBR8wlvTkUI86r94TzFPJ_OGpQt8gJ7ARWzW6VlCo4_o0Wy2N26NhOwjYFz0Mopbz3Pwl0V_9EBJLrrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛درباره کسری طاهری ازمدیریت باشگاه پرسپولیس پرسیدیم که گفتن امشب یا فردا استعلام فیفا به باشگاه ارسال میشه. اگه منعی وجود نداشته باشه طاهری فردا شب با حضور در ساحتمان باشگاه قراردادش رو چهارساله با پرسپولیس امضا میکنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26309" target="_blank">📅 20:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26308">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a142133503.mp4?token=DfNsmIkXJw7kP_WFl5uZMZRdpc-1ktirHDW46p8ruAOFcKOMosYHvrs6I8VHtX8QGcO5A2Sskzuv45akNlu0V8S8vfK5b0MNXHW20ha9H50ewoIVMN-lsRxuuckNs0tHBAupF2GFMK_QaD0sdaM81t6ExxS3Xt3zzHGXTby5H4QNVJGKKOtCir6qmwD8U0SVLc6nS977XVxvwTaKNWJEt_kwwq2lPQjq71AhX8CsRg6aDhB2KY2sm5gel-XHJH2xZXfN8VsR3Jj9mOqAbRheoxGzi-jOvp1f3WB-Rc6GmE5IBZxw62Bq_UHcwzCbF8JoJEB22tYZXK-UjKKZyV6pOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a142133503.mp4?token=DfNsmIkXJw7kP_WFl5uZMZRdpc-1ktirHDW46p8ruAOFcKOMosYHvrs6I8VHtX8QGcO5A2Sskzuv45akNlu0V8S8vfK5b0MNXHW20ha9H50ewoIVMN-lsRxuuckNs0tHBAupF2GFMK_QaD0sdaM81t6ExxS3Xt3zzHGXTby5H4QNVJGKKOtCir6qmwD8U0SVLc6nS977XVxvwTaKNWJEt_kwwq2lPQjq71AhX8CsRg6aDhB2KY2sm5gel-XHJH2xZXfN8VsR3Jj9mOqAbRheoxGzi-jOvp1f3WB-Rc6GmE5IBZxw62Bq_UHcwzCbF8JoJEB22tYZXK-UjKKZyV6pOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پاسخ متفاوت و معنادار پیمان یوسفی به سوالی درباره گزارش نکردن بازی های جام جهانی این دوره
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/persiana_Soccer/26308" target="_blank">📅 20:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26307">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=kOxqeoLM63-y8uahyz-aeAAvaN2H3a3rkipT1-d7ab6gVqdOglxEPsGlpfjEDN6eZMAdLHlRsaaTLuF0MnLO_SzVVKFdtkqPoUTwPQodbQOIbbOzgU-CkWrgn4PkIm-nS5ErtOEufdPn2Nierc-xewMtVjmISC4-eceVNwTE-QU3vU3L5ue5OsnoEApal8QnzSMexylaRwmLuonaqAAGhnGDljgQGmzftgFG_-ZR_0DdVhd4cUbxrPd-pmtjyQP7Z3asAOgSQs4-p68xCcDhwhh7ALrRQGQusWWC2JY3zXMPbRb48TeLY7BWYym0hYF9fG-v4JIcKmwf7XUsPgvR7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9a6a22a0f.mp4?token=kOxqeoLM63-y8uahyz-aeAAvaN2H3a3rkipT1-d7ab6gVqdOglxEPsGlpfjEDN6eZMAdLHlRsaaTLuF0MnLO_SzVVKFdtkqPoUTwPQodbQOIbbOzgU-CkWrgn4PkIm-nS5ErtOEufdPn2Nierc-xewMtVjmISC4-eceVNwTE-QU3vU3L5ue5OsnoEApal8QnzSMexylaRwmLuonaqAAGhnGDljgQGmzftgFG_-ZR_0DdVhd4cUbxrPd-pmtjyQP7Z3asAOgSQs4-p68xCcDhwhh7ALrRQGQusWWC2JY3zXMPbRb48TeLY7BWYym0hYF9fG-v4JIcKmwf7XUsPgvR7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
بادستورمسعود پزشکیان؛ مشکل پلتفرم و سایت عادل فردوسی پور در حال برطرف شدنه و عادل پر قدرت تر از قبل برنامه اش رو ادامه میده. مصاحبه مسعود پزشکیان رو تو کانال دوم گذاشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26307" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26306">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tKyrxY518ga9_zMQgCzsyoby5Mof3SD6aGqz4jr1J1yOw1aPfmPP8iNF_dtqCrb6aaH-NbeKxCk-wwOauEPvytXQHsOpSjppyNQF2R6y-5DLolHadeHAC63WqG4rSWEmOpD6h1upZJONf5aa1sxh3xFk_4XFHDtZOZ5zIRCVHAFZULDddBRTcPkoBytjx6ThqPzIAwwdLOFAq_vFMO6Vdk_db1jFeQkwD1Vi2-0eZkb_XdJNRpy_8x-XGfQoYNovOjFUeceybizKqt1lkT7ghbSeCvGHJ4H8JD-kvkSa0hSuji-PJsGMTSeBroqGPOAsgk8C2AkoXczu1MO6icnkRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇧🇷
رسمی شد؛ کاسمیرو ستاره برزیلی سابق دو باشگاه رئال‌مارید و منچستریونایتد با عقد قراردادی دوساله به اینترمیامی پیوست و هم‌تیمی مسی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26306" target="_blank">📅 19:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26305">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KB25zv7o891AWESC0r8nFgJoyB_pz0qmvHlN5f_5lSp3wM4D2wiIlpjhV90N42-RYORlY2BYTnR1JP4tPC3H4qrxI2tVp_SsktCdBrS0z04vULbUjUcrBGynqcIOI_yV9jOBpB2sPUp-fYB0TxQ3ixirdl0qQYvIxVybDChZYBfjJ0rp1dPagbU19KOVJiv7Ye66HNTIYqumJA1uYjDyGc46eFuhZE4JaSkUkI--X2-AFzoz-Xbtzdpg5FbQEJMk1Xswx1P2mmKyiGSKimsX6vpSmQ93KiMP-hdMxE4fCyNbAW1ZNG1zhhXq-IkJeYClomzdwpXwipbGQWDNOVLo5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های اسپانیایی: دوست‌ دختر یامال رابطه 5 ساله خودش رو با دوست‌ پسر سابقش به خاطر یه درخواست مسافرت از طرف یامال تموم کرد. گویا قرار بوده ازدواج هم کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26305" target="_blank">📅 19:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26304">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRL3WAtRrDGmEl_fC24hMUg78b7PkoXcLrH_J5nuFOFu3PQtZjaWb8N_AeAeL937JPca_530SAVYOce9C3GpeqI2YBACCES17oC43VMyDksHP2odUO2NhvCAgHJGhI5OWSmo_aO3DRDd7SWC477iaDn0jSf79L0-0UE8ixADdcTjuDZIj31S1e1lK4noxbwfsJT00HprKvlSBrcKKsDhXDqQkjmS1b5lBRq3Yrr9U5tOzH5Iw3nUWv_yr80NgsBUdwRIJIkWFk4pr6UwUeooU17sYFlnRt0dU_16xyVG9pcRZAhX2vKlLhnkjT4fi8r25ZXoD4ldnmrgtKudC8v_YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب جام جهانی 2026 از نگاه فیفا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26304" target="_blank">📅 19:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26303">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRPj8EK8tqtCpoi-98fb0J60UR2qotzjAriZwAn9xu4AjPOGt52L9rb_GWzfUDs4Jbx9OBXCvyQF_4Hpowvnm35g5OzLA9YwK90hy0_p5uG3Q371OYq0HOWf269HQveLho263iBkrYA8F88ZtRTF97g6n1ZueSk59d4SXPl_h6YoDZ8Imt0hZXGhaVrxdJy5SwRnmAT8b9UOYwS7-9n-kwZyu6DuNR-nl30A72T7tmzFP17TVO6F2lrbLHVhwUOUNFv8zd6cgGZbdrMUzZpLRWk4UvIFBYB24YXx78mtEKwEwtK7QdLFyOsF0E13u9m_q3DRKs146L7FrsvtpnYa4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
برترین‌گلزنان‌تاریخ‌جام‌جهانی‌ و برترین گلزنان این دوره از رقابت ها؛ کار لیونل مسی برای آقای گل سخت تر شد. لئو اگه آقای گلی میخواد باید امشب در فینال برابر اسپانیا دو یا سه گل بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26303" target="_blank">📅 19:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26302">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YtOsWkaMqpLurUsfj_xb90DMsPlLR92uKObQzflZctg3ufw51wgGRSTn4MWkvPbEkl25DGwrCfh0J4Qb9dQF-7z7KyKShy4vji0CVv1KUm_lKPnwW41MdhQUmjXrK-qL0hZ8cGSz7Tj5JhcoXm6BVUO76pChFr3rRCUb_accv7DOrguV0VkC2LyrP1yxxxFogLS_TQOOpBVo_REQtU4lL_Uc1uvwym4ygk65e7PyAn33dI1e6i358PHAvRv4mpZnzpwjNdarjkfBI15j865pI_izmPQmOHXJ7yijrT55tfzyoFof0409gAZo044PG4VTPcuD4leF68iT3Av4dYtAaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان: کدوم‌پلشتی‌خایه‌اینو داشته سایت داداشم عادل فردوسی رو ببنده؟ ناموسا من در جریان نبودم و امروز صبح دستور دادم سایت عادل رو باز کنند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26302" target="_blank">📅 19:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26301">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UPowZW1KKJtd--S4UuEFa7AmaOasdT5PdTeoWENF34tvTVWw8s5TN-81hhAD4fpKyd-bEwOGZJTvsKSeVR154adh1vydL0KBGP7YwOzkkW8mauWCAVs_snNGTkHiw8BjsKuDEi7-d3VN9LI-v-YPle6cT5oJCJ1EbDQn2IH8jdcNslwuNYZkmMUsbKwI1AkxO9UWDXSaj_VLSUzqnYYz1sz08H9oWbC5tcAZZzcpWW5QBkIpSptx-E_XsJ2v93LMccOwovy7rWnr5bXJgd6ioeX3sxqB1eJlT07J45EMynxkqqgqd2kE1BhjwyNpA0FUOtunT0aHx1M3U23lEdRnlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ سهراب بختیاری‌زاده سرمربی‌استقلال بجای محمدرضا آزادی خواستارجذب حجت احمدی مهاجم‌تکنیکی 22 ساله سابق استقلال خوزستان و پیکان شده. درصورتی که باشگاه با این بازیکن قرارداد ببندد و پنجره باز شود محمدرضا آزادی از باشگاه استقلال…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26301" target="_blank">📅 18:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26300">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iCndoZENX608J7NXPEk0RLqdjanHCR4e-iCV7ymf9E4_pnykF9DLUwsZUyWDPIvGik7eYzKp0M-AwdUActsfsU9dT6H0hMkNwJ7ikV-pNLVtLJgZO4S1jzWiNmpIE6_mF1yTRY-F8R2dmm4DjmTztx8mnlA50XQgzfumkKtg6T0h6yn-TQLe7VQYyuSvfWf3DXsm3-iyqqhVasVbvEMU0ktksui3sqR8jPuP5_ESGS47sJOMb6Rz3u2I_JFzM6Rs-rwJBUjn12fBiXwCCJ5lbnO1RdYhL8eBu2C0ARZbtTHT1lNB7ZDuxIsFxUvMWJ1MsO8rFpYCbJ2Quq1pJLLpPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کمال کامیابی نیا هافبک‌سابق تیم پرسپولیس در 37 سالگی از دنیای فوتبال خداحافظی کرد. کامیابی نیا قصد داشت باپیراهن پرسپولیس از دنیای فوتبال خداحافظی کنه اما باندکاپیتان سابق که خودش این پنجره مازاد شد باعث که کمال کامیابی نیا در اوج فوتبالش از باشگاه پرسپولیس کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26300" target="_blank">📅 18:18 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26299">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXGd0-bAkCf1tq3rvxYUiPSFT49EIByWVSnZNNHaxjRnWs2ohy8peM9LfGrywmS9-qSG8nVRKQ_AnZhA7uw_JEjqmZAZLHqCF_v4Op8kNymE6d-3ts3XhRYyRghHxlv3Zn6T-RXy67mRMyczhkmZiet8TIqE6TMG3_eU9HTlARtGGtERrtw-9IDkpSyuLeledTg0Ezi3fz1FAxJ2MGx7o4ldu1hqy-JByUl-ktWgKVFM37cdIr1xkH50DV7Csgrvmv5dFxfehP4wRCM8gxC2eHPwVLxYrjhCCferpQIH3eOFsCELbQc_NbwVNs7IGpspUqgGJdrXOD58mJLokpd6UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ فیفا ظرف72ساعت آینده استعلام باشگاه‌پرسپولیس‌ونساجی رومیدهد. اگه پاسخ مثبت باشه کسری طاهری بزودی با عقدقراردادی چهار ساله رسما به عضویت باشگاه پرسپولیس درخواهد آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26299" target="_blank">📅 17:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26298">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLKCXMjoJsTS3A1Xnm8DO2Iqs3sv26l3s1hG0gQh5aBX9-YvCXfPZorjQEB09g_9JSclr2FE56SFN3R8BglPXJ5vKMkhTnJ3i3kRTbx6WORrPzqy-ubjD-5bpVh1ukY3MWYfD4rr5ghEyGll6Lwh1FpOBg2TRdhAoChvHwChei21yFuSvlz9u30cYLQ4JeuM5k0kULe-7C1pdB7_6JrwMQgmRYyIecYNYKpjTfSca76qUCoZ0Xw_7u2tyy-vf90fSXByjWmdsHSByd4DI8WJ9W5B0o-8PVdnZ6GF65n_4RYcWszVpNFvOICn1MCNgfSD-zgbOP0Ly187X_6eAl1VPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26298" target="_blank">📅 16:46 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26297">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/azc-M9AaYDJh7ZZ4DFGI1tE-bQcul_-p5EQQYq2pM-8U6gqlKQBZjzQKH8biDcRVX4VBMD1ECzlMfQO_H_O0mVzM6XpLHA92WbXJ97x_cX9WyIE3lI7j5LXXtrxVpiTljGyTfhU7C-yLCiZyuc4CqWLqohF77WBVxZ1-wtRV-7WkruWMLdzsGLtO6DwW_oQfnjay4BXdUTw5vTvJ6ExPWyfWFgchR9vvNynMNs5cqH_LP9MPjr1AyYWB2j2lyJ-hnwyShD7ItdPW99XaKZUgl7klkYCNyVxkK8EocwwwA8Ixrh7pIjeJkoNj7RIkistvfOBmr0weqQQqPXNL0ornqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26297" target="_blank">📅 15:56 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26296">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SI8paZ70PVkDEn9oBN_V8HG9FKNnUKEAbZhjCSZR8o2HQE-PhVO-8S1g0mrAG8iq6lIaTLU1WDbkA0sB0xpoCAuGmWYReay-yCflDYWuMK73Ha9m9ioWRInU5mwKIdzo4eHxDoTK6zbyctRvTHHoVYA4gB4ys6K27mv9B5lZxsN8BGZ4QgvnHjKShcSCM_2cPs_MY_9nE7E4MIFnGZrchNDuzMvXN_83_1L24mTQQVjCs9P6conikzpVHiJO2QCiytRfKc1Sa8ldWc3DvRrIGHjjBS-P2b7QkXlqa4iz8w_JJtmLX0zlvAaD6SKmIANsc4Rf_2DouPwTJN2K28alNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#نقل‌انتقالات
؛رضا جعفری وینگرچپ‌سابق ملوان وگل‌گهر با عقد قراردادی دو ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26296" target="_blank">📅 15:45 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26295">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYFsauE6YyRI25rA7iCxFnfKZNhshg7UoF906EnsF-_BzQHo5zkz8srjykk1shj51rjkUH_v0tnosxTZneUv4Ur1pk_PRxKH-T0oMP8Uq1sJNSvY8gUSGonQYw_1shNKo4cmX171AtWUhSWRiSZDfW_S63WKMODF02XbvuPSbtXx9Xm-noeb9htJfibUCt_VgFpvngn0A7xMOOuURysjqGZnO8RN8yfP5DmKj0s4A-vwGxAvrogAOU0GVvnVqoua5hAgmW6iEWIZkbssiy8rhcwG81FA914B2T0CwBeBuAYUla3hUs2EUc6hJcNN2weELRaBK-6KBhjCUj-c55LWpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رسانه‌ های عربستانی مدعی شدند؛ باشگاه الهلال پیشنهاد مالی بسیار سنگینی رو به فیل فودن ستاره26ساله باشگاه منچسترسیتی داده‌اند و قصد دارند این فوق ستاره انگلیسی رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26295" target="_blank">📅 15:38 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26294">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O11VIkN-C3J6tHDt9mjfULfGyBGkE3BxQgwpBW8x2xHxU896ZM76DfXHUbGYjW_Lx41HS3Oyg_AfZJb0mxbjyr15R7e5AGo3j-i2ylvjgW4c0Zlt-ArLKBRG7Z_Ted1GBfGxEvo6MSk-bDFpXQdkZ1zckSQ_zCjCUWiY4og5iL-brGLP5MJ8O5M_yberJszYxQagNrQS9Z1M0H54AMaOKTqnYUWdODsDx_o7mEz53G3v9--8m9DleydUrvtibmCBwZmDDxlRyLsKKb9hqxUlLGCNaJz7Cn_EarX58zHct7voJ8720Vpfa75HgUbTWW_MZVDd-GzoIK4qyjLbfKKFhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اگر اتفاق عجیبی رخ ندهد؛ باشگاه پرسپولیس ظرف 24 ساعت آینده از محمدرضا اخباری و دانیال ایری دو خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26294" target="_blank">📅 15:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26293">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzJoy42aNH1k_FSjLEWwyvPvfhZe5AiuuEKB9qgSRqH3yluUxlzDPvDaPY94Q4AsdrTTtLwljmpi6Td9vTwZeRTJ7Vx4ij5hNJG4W7V-EDVoNrgIgePALJHgrIpZySx6HW5jvQA6lVfyN7TcqLw2NIfkNfdLwv7xa7AkCPaHMzy18Zo8oDw51dQqI6IWtD_1Ape6B9e8_BPeG6Xt4nqVCyx_MM9hKQckctVyXBZSDzowEeJg4UpRuomNedKBDBgHpQoyTWtCwOkMW5WUC4IWZ6rRuKZuXdZbGoJDnMe36W2NxuddW4uKH_9-jTJ9F3-uSB72cVBVr6xjRyGL3XMFqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌قوانین‌فیفا؛ درصورتیکه پنجره استقلال باز نشود این تیم درپایان نقل و انتقالات نمیتواند سه بازیکن آزاد جذب کند و تا نیم فصل حق عقدقرارداد در سازمان‌لیگ‌رو نخواهدداشت. این‌درحالیه‌که رئیس هیات‌مدیره آبی ها امروز عصر گفته بود که حتی اگه پنجره باز نشود ما…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26293" target="_blank">📅 15:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26291">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XG49o277tR9s22YVhvThznZAvVbo9yveLM7yL5xadPQFaphgb6Nf0idKkJ4mNHnp1MpnNTEXvq71ke2qGHBkDrWWk0x9CZ5FI9vbGcSw-lB0VX0PDe9zVsbxyA6J1n6lalfOe0qdWgSyuzqD5mVX-v-7aedjydcuWBW_900oiiK2_cephlCGw9aYVOBgY8KzKwT6aT2cqbWH-FWbt25Az9IU-jmbrSY9K0ISTzo80P07RI74a8X02VAx0kP0BNfeZu5hYrT2hSv_kP65yuk3n9ln-nIHF94-Wd0-0Qf2cqo3QLLqueimLPbf4CC0Fp7F25qYpSpSQdW5G-MnG6wc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a400n1eOkRw4rFWQs1Fv65QaQuItwlvau_3AooZWXVN730NN57Vu66C5SX00RL8A85OShJDApYH4Pp0qtSiHsKam5dTokSZnfSSOhStqjFMZQlBJLlYf_MGtJklRLtBGniDD4XTd5TaygAm66rJcOjNlRQnVXazNgtAlsFuOmI4lCq-mYur0EIkr-fOWJI9HiItw6jIUxUjP5nm_JsAUiDJPxnzwiPeQ-qFjay3McJYwAA-Xc9Ei17fJcmTxEVlJIeZuq9vqXb-Sk7jo3yhH3DaDDNcp7kzippRj6kKSGH4YzDkhYl8kgzUrZFsI9xWPnUwpnULcy_YQy8I_0zy_kQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🇪🇸
ملکه‌های‌آینده اسپانیا فعلا دارند با کاپ جام چهانی که بروبچ تیم ملی این کشور گرفتن عشق و حال میکنن هرجامیرن‌اونم با خودشون میبرن و چند شات یادگاری باهاش میگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/26291" target="_blank">📅 15:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26290">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JqgBYLmORnwoJb9A9FyxlmRP28i598_YkHTcknuBMpc7cIMoAV_CCuxPA6L9Ww8cMNy4mFt1gYGaIEQcFR6waFQ0dyXs-Kc9xRB7lavTW3p6qLruW-QuwGAb7cQjFzueGqA9TPGDssiDqCXtaf9xamsu5FUGfGp3SIr8QhZUISQFepR4rpr-A6lkZzIPqpgz41p5i4ML8AZ3v01C3jUgGfCCcJBu2mIzgOmISjvLlZrEWWc6mDZmjfH3KiJczOpvIVuavuLJZS_6JvqzvYmCB_FsdQMorAaTgS4OPkKgRgyTKU2IzNgRo94_uh4GXhd5LoDwVssatisqygDmx5ZYQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
خریدهای لیگ‌برتری پرسپولیس تا به امروز: مهدی‌تیکدری‌نژاد، سیدمجید عیدی، پوریا شهرآبادی، ابوالفضل جلالی، پوریا پورعلی؛ هر باشگاهی هفت سهمیه لیگ برتری و سه سهمیه بازیکن آزاد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26290" target="_blank">📅 14:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26289">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hXB8SypnwLLQcVs_iyPMVpFiXv_8aNihrf-8cuEI3kPZHiuDp9NHh8-aAfcPIuRX21JTo-BeZ3NRjhBLeyG-eWzoqUAoIavNyB05tm5mxm-o2L99FREuxU9GKVKXfQUk5ub2XNFUNeA3nplGnu_F2SOixRCPglh7ioiRHH52JvG6gqti2anr4jy6weq6ov2hGzQKkAgR6_M8sYBq2WNvjTE8jPF96PNYFlDeSIPKBUQZmYRjZsbpB-Gj7khLBFxRBKCV9iVPnwV43tX99Y-cfg8CAdyfZe0iwdzbi0eVvt52PHPY9548IFgYRpLPk6w9Xcx8ewCYu3I7gkBywSRoJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیمایی‌که تو جام‌های‌جهانی اخیر تو جریان بازی نباختن؛ ایران 2026 و نیوزلند 2010 با 3 مساوی از جام جهانی حذف شدند و شکست رو چپشیدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26289" target="_blank">📅 14:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26288">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ndb_HtoxM8Ssc3usX3cjufD46zfP-02M0gWf49aDbO5GSlFofHRD5dh9UqbL0EYucSapOv7aK_hjo7ZXnqvzKNZkuRj3atCfP-wnS3-FTTyRsj2FU4QaqQoB8HvszS8GW1rXqDFkjrcAExJmdFz4yeTQsEqRCdplVi-lte_HWwVStfltMd0T35sTupCnmJZCs0_FK1m-KklACOUYJjAn2gCpi926OTu7Lq_XkvKyPyCyi8Tq0e_xXfKmpptdeDND9NFmz039QRn35JZEE2ApE-q7iS8oYkVPDk4_fRrh45_8sTcorD8_92zSCcpRbfEsfj2xu6IPJFbr7gnIxS_LfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط 7 بازیکن در تاریخ موفق به کسب قهرمانی درجام‌جهانی، توپ طلا و لیگ قهرمانان اروپا شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26288" target="_blank">📅 13:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-26287">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy4RV62lhpyTZP2EW4qINqU98Y5vg9CDA5_rrBS8JjJ4Qe0HtY3phow6rIUorvMR-IffLGCoCgl1XL1x9rbytJupYIpzsHnxTuWqP5a_BsexUheXR3RFMtC9sN0GPPy2oSSHc4RdugH-7Mtq55vbRfoTTirYa8TciToHMDi1qkmuIakcrkIKmCpAVbZnUomqfCk8fa3sViQMmuGP_xxr027Vf4Am6I6XWD5uyca71jE6pT7FEiy7b4yFqPop74EXCPDSWu-fpXLOB6uW53EAOX9T2ivBhZBSZiNkyA4RpWx3SOKtjbAKAsKX8wtXMZ2N-vLE6zGIVFrrRmKS-0rq5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا؛ بعد از رفتن محمود بابایی و مجتبی‌فریدونی؛ بزودی علی نظری جویباری نیز از هیات‌مدیره‌باشگاه استقلال برکنار خواهد شد.
❌
علی فتح الله‌زاده یکی از گزینه های علی تاجرنیا برای مدیر عاملی تیم استقلال بشمار می آید. تاجرنیا نیم نگاهی به حل کردن مشکل…</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26287" target="_blank">📅 13:40 · 31 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
