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
<img src="https://cdn4.telesco.pe/file/V2VEBOYmAQ_uahw2NGUfcn2pZG1_y4Axe8PquWEChYFVJCI160dbLBZNujF4GGUGWj1UrwElqOubUygrg0O0KtMcRQk_bmCthTAuZR6pdY4ivLVJk8uX0LiIf0j0jrR9zcB909O3y35zLN548jcKsaqDJmiFuZlb_MtgkoFuU32BhTVw3s_XoRVFrb0nor81IQwKXu1msiqFJBnd1l1t9D_a1uhE_yFz72KYdPpUBZ7Gd6G98qQOkIN__0AjbxC2yQI4UqjkDAdI8W6gbf-zdskWEqUft7SUTuTmXCH0Ih0PSbJ9lFi9OAUyPzP_ro2VJfNdJUf2ydTBe7sJS77Fug.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 494K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaaa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 11:42:18</div>
<hr>

<div class="tg-post" id="msg-31235">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1sNDwAD3zQve35udSJQydO8f17W0CZDCQnavwD-XJlgwTpIQxxCkQlnMIioXafNM-m3_WrslCbtvC3ljMMT8k0ip_bwh8oQEkuxv_eXJj9kKJ_r2eMcxvgSG8G-7TY9ECwZQoHbJ_kCCbvG40ejX6f4_39Hky49RsO_QnBpekzI9aSUyEhq0ZPPfg1bzDA94YoWidKVmAbSYarRlyBSxNqOxQ93VxZXhnOKsTs-GgkWt2bRz0_0w8WuLKrsqNnWUS4fEvEbx7d0TlfSsFj7BTUHe746oYu-cN-3dRdChBHFodnBBS7zLmJZLn-AdXpONlksbOuKx8_HlbzIGx5fPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تعدادجام‌های‌معتبر کریس‌رونالدو و لیونل مسی دو اسطوره تاریخ فوتبال در کل دوران‌حرفه‌ایشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.42K · <a href="https://t.me/persiana_Soccer/31235" target="_blank">📅 11:38 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31234">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TuVhOHozvo4vlrV7FvM4_sqVD70LUTEdYS2cjoCk8-BTxcN3qBkRej9Z_FMKLS6m_MBlObpGyS8NjctfUKIb7vDY6pYPfiPJPsC38jhcKqCIkXHgNfPyRDKbsAt1owkILawkPu7CYEKCTbC2Y2aTTOi2GgI1Bc-zaNdWVK45FpRXmyJOnGdmH_ExNBA0KHOPdxkKC-3cqoelyKo5A9Ie0SJn-iOigX7K2H5gjUVaXFDfpsYOYS89V_9XQNLxlucMNgzhZPARVSxLA7Euqnhar51paOS_aKrO9gf9E4Z7M54ue-VUXspvMn2O2iVkoP6z7XMiefU7Gn830AzjRieuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
باگذشت‌دو روز ازبیانیه کریس رونالدو هنوز هیییچ بازیکنی از پرتغال این پست رو لایک نکرده!
‼️
این‌ویویو روببینید تامتوجه بشید که چرا کریس رونالدو اردوی تیم‌ملی پرتغال رو اون شب ترک کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.57K · <a href="https://t.me/persiana_Soccer/31234" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31233">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/31233" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31232">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZeFKTI9KLu5mi99KnOof30mJA0WH2Ssu3c8GllqnpDP65p46N7UdEJX7xXkJl3sz0BUllKUi3fq76G-0W6A0kJZzjl5f_yjEinYc9i8Wae5iIcdqQ_O01cbz6kPkF3vpJAbcn8F44UCSaxQ3AQx0A6Eep-3CHQlksQGj5cVrbzJm1uJIXsZYCL4GFKn8cQ4iDzEFJ8tzWpqZTwtPH27i48xcKlsP9ftEyBBekwdRnRpI7OAhQk6t678zViOJS7JqOD53Iq4Ed-8TGyRfqjbvbZJ2e7214XthGz0p-xUHdla1NPRtahioDb6oD4XGavvEu4G1CmvA5G1VtGGwjvKiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جاییکه پیش‌بینی فقط حدس نیست، شروعِ برد های واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌ن
ام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری مثل قهرمان‌ها
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع و بی‌دردسر
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته، همیشه پشتتیم.
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!
🅰
r17
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/persiana_Soccer/31232" target="_blank">📅 11:21 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31231">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kG9bZn1saMpVmshqEtSDou6cU41eF51-vM9mDfVa1CfRIpoq5E1EDTwPa8_FEmzWrveMPY7ejNs46hZp_or3yWjJjIlztVJC5zODot3V9-b6wPLvHQtcVEKAODIUNws58pCewn_oYtK0X11niAKYRNACUKxWlZqx24UhNWwrhME6uHOR26McRDe1kNQlLfP9O3Y0KrTY1ZCZlgtkUtExKMv-rFPL0Co4cvO47mzDQxpnmVHJ9kG7qPwqaN8lHdMi5zxNY6RJIiu2Zg0V94WfCCqvA-dWwY4dofzT-m75xyVyGWkuYxTCe0Pbw1yejWUaOSALTwbZRjOalgHmlZ06CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/31231" target="_blank">📅 11:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31230">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VPfcN95V7ywktdTHs7jAKChuuzSLGXn87C_EB0af_IlbcdxODr-cuNHMQ5mjm7uUqbM8K1F3eA7vu3TV5srSeE13gFZZKCsZ5GJm9XSTxVeNZdhC2-1uUfZc28rIPXnvJ68798MzjQdTLeCzPdOX6AqLIZaM4QOrypbzsVcJxQj21xHosmlc11o2lIgfdifxvBEtVICORm5jiltvn_udm-q2-zWDAXBv7zFZSZOnWn8_9piI5ZMCxHAFhAsqhy13OJHDvcPMnpWlUOD9juqpngf0zv1oK6oRJwTyLbwNBeRGBqaH4n8IyoS7ZEapF_fxTV1Np2TNJXrn0v_k-5lK2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/31230" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31229">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=OPuqTlaVEW4TggvnycvmLyF_d2Iuvpy84Q-xOjxRYjx35If0IbfDIhdUfleLT1B7YbKWzhTg8wRZHgF_xff_BJIaA7EOeqNiriSji9PFLyjlRs6IiuAgA83rAk3r2HxqDJ2H9rOkpfeBQrKAZ18EVodhQg3tVWGQ-ELE_hLSIzZQF-n0MG773zom9vDNBH9oRe0H-F-Pe_NFDoVmmjKfbhhq-_Xmx0XUGWBTiB06Gf-x4XGDOQJ-i_nBn8WiQotJFjNaUVmwjrGV84SfA8FEWE_055LXnIf1BQMmZ6A5hG7JrxNX9rm8X83P7MHsaj8OPP6MdEp3eN2SF19F1BDkZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9af88968.mp4?token=OPuqTlaVEW4TggvnycvmLyF_d2Iuvpy84Q-xOjxRYjx35If0IbfDIhdUfleLT1B7YbKWzhTg8wRZHgF_xff_BJIaA7EOeqNiriSji9PFLyjlRs6IiuAgA83rAk3r2HxqDJ2H9rOkpfeBQrKAZ18EVodhQg3tVWGQ-ELE_hLSIzZQF-n0MG773zom9vDNBH9oRe0H-F-Pe_NFDoVmmjKfbhhq-_Xmx0XUGWBTiB06Gf-x4XGDOQJ-i_nBn8WiQotJFjNaUVmwjrGV84SfA8FEWE_055LXnIf1BQMmZ6A5hG7JrxNX9rm8X83P7MHsaj8OPP6MdEp3eN2SF19F1BDkZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
ادعای نشریه فوت مرکاتو: نیمار زمانیکه در الهلال بوده به سران این باشگاه گفته جزیره میخوام اونام درجابراش‌خریدن. درامدنیمار درالهلال به حدی بالا بوده که درامد سیزده روزش رو به خرید جزیره اختصاص داده‌. نیمار در تیم الهلال به ازای هر لمس توپ، حدود ۱.۱ میلیون…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/31229" target="_blank">📅 10:19 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31227">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBJG8VoGWtRArqggSkZ45sWqDP0LO4eKoLHVy7DqfUk1_hsnxOm7-qjY3zRg5-HFMxc0ONhFhA-1edP9oFnhmDNUAkpKU2O-DY0sux8e8z6yJjYSH0T7tW_V-Vl70_B8z3EeqRFKg994c_flr5j6XO_KiZWvisO-zZUxL3Q17U_lbdL0KzxSZXnjOLgto_pDdI2zi2KC3Z7VAqGxp9yjAgDJxukE0-9CnE-bbVs-cT1Tr0bZrs7GmsOCirnfRvLQ3y8JzVAyNr8rZGHssWKCaIsMkrJ0WZYMnnGlV9JT1hcKQsXocEQZicR4PRjtjHpmDthRgUnYRMFihltZPSA04w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
به احتمال زیاد پرسپولیس امروز عصر با این ارنج به مصاف صنعت نفت آبادان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/31227" target="_blank">📅 10:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31226">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dgk7WrcmWjIinNKvNskTMy9Xmob4VleIPjgglD2fWxeq1s6KC4zCuDqIBhzk1PmxJ5WAz4SecVP__lWKeslxzk0kyOmMkJPlqBCwobfoKxK25zwMMPR86DLdeLftGdA1QoZD-Zrg9tt7lJBeAa-KcQVJLHaNvoS2CkNKn5NeU_mBUXSsueQSH3GY8YuTaqJj1gyPIT-2Gawwd1GaY5aJYVYB4JpbAy8MT1WWRSYdFh2lw21S5THN_oRIcATZRFh3DTEk4QbyEEJ3mubUCGF0vKNPa9psjxrfeLWipqh2m30SZhDDNSNb1oa4mdeVckdURhtOKVPUHANa-NgQg1uvpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ نبرد شاگردان تارتار با صنعت نفت و دیدار زنبورهای وستفالن مقابل وردربرمن برای حفظ صدرنشینی در بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/persiana_Soccer/31226" target="_blank">📅 08:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31225">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcjesIShIhK8sdUCqphQuahEAbbPeNOikPurddx8cLM4cBiqWs919PVPmoUP9ntjMF7asA04xXxE_V2SGf0HKMcEgZU5Yjpvpj1Hsz9W8aUwTxTvGr8DWtQ6OvWkrSQ4g4gYhJGlQNZfD7pJNJ-zzkFY8TF0FelFFm6P9rjFFifrs9nAkUiy7lYig1-x1kupLLWJ3J79QPwcWL5B07chjODu--esxgMWGDQD4gFqc_SJci-aKJg4CWG9u2awATtvnhn5jtdnCW4MJwYFlsEQ_jzkS4SmfSV1weD8wDte3SgGkcDR_nfCOBoesP_Cx9OuHR5VO3P-B3Eqhk6ipmrRnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌دیروز؛
از تساوی‌در نبرد استقلال و تراکتور تا آتش‌بازی سپاهان با درخشش حاج‌صفی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/31225" target="_blank">📅 08:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31224">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛تساوی‌شاگردان بختیاری زاده و نکونام در یادگار تبریز به کام پرسپولیس و سپاهان.
🔴
تراکتور تبریز
1️⃣
-
1️⃣
استقلال
🔵
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/31224" target="_blank">📅 01:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31223">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om6yiWgUfibJjwO_CEdCpLhq-_FNWEyN9679eby9waMcFmuLPtLsgTsGLdIpRJBeSgb0JofNLgiMR5X_Y6qjmf-izX-sMemkcITpvig-jLEcbCHDN_xqKU3c0WOjs5ZCp_W2wE-W8OnzeD7Va2Mf5a6c0sp0OGxDPE7GgEccOYgbVXswx4RYODDlXN7if3ZOh4oO8-U6Aw5pFWt3j-kG9ApjLb2exQH52NkL4-6wJ3YDNXjCvfB-bmexDt4NI6JoEp6OxJrpidKC2UzjLlYfMhuKIT5hRA9-qnvkX8XSFWaj2taA5yDoepSBn9edMMcMK8bYVYLl5P_Li8wZ4wvNlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحنه‌ای‌که علیرضا بیرانوند درپایان دیدار دوتیم استقلال و تراکتور به‌این‌شکل‌سراغ‌یاسر آسانی ستاره آلبانیایی تیم استقلال رفت و جویای احوال او شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/31223" target="_blank">📅 00:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31222">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">‼️
علیرضا بیرانوند به‌دوستان‌نزدیک‌خودگفته تا تیر ماه سربازی‌اش به پایان میرسه و در نقل و انتقالات نیم فصل با قراردادی سه ساله استقلالی میشه.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31222" target="_blank">📅 00:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31221">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a328e3cc8f.mp4?token=XUxRbu2kZMmQzcUB1HregAIlKJWfRqPjlzI2e151DpPsPll0C1dCiHIqYX2w41NmGvlZ6fkCce9REKKo3jQDHLYxgdgWy4_15gErG0e7Xy3O4hVC1gfe-phfX8uIVgQgolOkP8MacgNoQ0Tipp7KKPRs2qndGBDO22L7SasRQOawm4kJmkTpTZydh3IzEB3UWkEZuRRPxlhh166nNgXTDO3cwNL_fXD3cWJoLfIjMZDV4aDEEhX27oLQR8VbD2RDac66dJ49pjRkxgPPNVDl6ezAUJJZDum94ofXEi9m5NhmHDgilWn1IZWOSYRnXD5z875cO2kN-pqmZVtIX-X80A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های تلخ همسر خدا بیامرز هادی نوروزی اسطوره باشگاه پرسپولیس که با گذشت 12 سال از فوت هادی هنوز لباس مشکی‌اش رو در نیاورده‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31221" target="_blank">📅 00:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31220">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y-Fh7Hs-2fjnKzjxTVjq5e-5LsgEzcQUut1fWu64zYBl3YGfkBur9c2ufOM_mITBs5QtrYRWw_SR9DaPedIy-jXoo-Q4gd29Fb9IFb_FDtezwrIgxJ72gKMsekhJGH7pzTUXxw8I3Xw3lJ82ucYhVG9j92gXr33iEvGH3Nl_B756erGrtqsBGxQJmcLqzyu_ZP3XkOXPOH_gKGCdC24dDK0yKBXehRUBGeLR5h-6YYDrlIKshDZ4GKULbcdfLBNYls2hsdu4HEdsZVEIBH6H_WICzJE8VU1Vlk6QjIHHO32qGjWvsygkz2zx7o5G8rw6wvElQ5gUh2uBe4hTN9jzKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت؛ کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/31220" target="_blank">📅 23:48 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31219">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jAw2wNidsLIR4VLLl8gHu4JnWfL9SEtar4cuIDdO3BrsKb0_Z8v73CfyWU00l7O5Oq5qF5_UbcPTM2o2IZwqHpb2rvPsLQZ1AETPjqiiSo92xTRVH0AuSdS-tOwUAusqYcZd-r-AY3_fotja_6BouvwD10niTMlCU4qZwwrgN3QJO3iglohkx95F33ebhFkSnm-k4VXbX8D7MHpC908985zTHWjYXSPbk_z0rn9pBRVjt2eFebY_8WmVYwbpo4rJSMVuTJyw95BtroM0OiCIU0r75D74Vbm87Vf4Xc0atyIPNxHz7g6qea-s86yJVT6GsvtNsra2Te964V18CJWJ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شجاع خلیل‌زاده بیرانوند رو آنفالو کرده و از همه بازیکنان خواسته‌که‌این‌بازیکن رو آنفالو کنند. بیرو بعد بازی بااستقلال گفته تصمیم نهایی‌ام رو برای پیوستن به این تیم در پایان خدمت سربازی ام گرفته ام.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31219" target="_blank">📅 23:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K_EgsKk_5PKAcgAfyakOJDWbkC7ldgHDr5BsYH9RQyfAFWYGrFyW-jSa2-KiQ0PneSq-tB0BMLRRa2yI46XYe0pJsTdheFIfLzQnxUnGo5ibGEkCCWW47b5L_F4GidFv3793f3vcYGrMbM6eEp-R-dKnuIZ0cE6EXjOasHQQ9CV30eUKjorbpraijZyL6LdxeR8Mr8A8BnRowTlZSA3fVoNs6aqxiZ0Qd0Hl2ufu8E4cTNtN8OvRYLeoWb11MZW_AAZ6Ex1fKzXkLfubjp8-wNLAoOg5Ui_fmVdxlp-QcLAnfZ-vUH3ByXREzUwMfvSzUreca1lHc74vIFhDBYZvbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
#فکت
؛
کریستیانو رونالدو در طول کریرش مقابل 159 باشگاه مختلف‌گلزنی کرده است. اگر فردا مقابل باشگاه‌الدرعیه گلزنی کنه اولین بازیکنی خواهد بود که مقابل 160 باشگاه مختلف گلزنی کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/31218" target="_blank">📅 23:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e52465a28.mp4?token=L6ABSrcjym64gq6C23YDkof1ZNzhrcAOxljPrBKeiXgYUG_CkFj80Z2nm7gj7qqbXxVBWQ4T0ljxQCs8NtfX8nMTqArTKZhep6nHSIilxpjy2_feqa1QAOZ2fG6kJvsMpkPxPBmGJ-DGVF_C9dwnkT4FM_AxurPhXZSwj8V6JUY4Hrl_Bxy_JilGqAIi-dLB4aWt-y6vNSUYJQDuNBYck-hgwhRixHzuwJ6t3o19Tv1PKx8sX80jfP_f4jUMGpqKNfjb08cbQMWNuuVYHc99Hh3Am0u2DohUo0CB2rv2RG4QGtDUikkwNZ_dCRNPwSxtYN1C0xaa-dEwpEeUIl3FUrNEcWEQH26b-LvOprG7DeRhXePhIBo_T8FdkV76vm72pKvQ49UVqBWCfvTu50AuwUWwu51m7EaiAzaG71VhHDwwDa9LXYRcZURXha-XHFn0TVufeVYN049dRFJJFi71RpgEi1dDaT9dGdvhAs9-bfaUsZvTp82VzRL48PL6mAVvht8ceDsCgesdQoM_mI3dXDO0O0Qp_EmGRVPLMx_v7gerNIT49Ei2TAUJJ7CrIgvNYIq400jSUfcdGfVSJ19l2xRHroB-bx-inSKQTQHa0nZ1-vRn6gSyCMjb78wqMe6U6nR4pHcc1Zx_T4RRfbzoSvEgXekAr1XmwU4oQ-wjio0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
نتایج و جدول رده‌بندی لیگ برتر در پایان مسابقات امروز؛ تقابل حساس فردا پرسپولیس مقابل صنعت نفت آبادان در هفته هشتم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31217" target="_blank">📅 22:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Upsjjw6-k-BhnW875Dx1XPNB8F_zYzobBAIzlDTP9wXPW4NuQo_C86T3qZTdd0oYWbYKSuxL3uKTR-vHGguiPRbFS0y0haMrzKhaCjYhZskJWKJZXLwv7PkHcxdnZbpJTUbp0mJIpjjNo5V8w0cDoJEhz9dlg8wuHJdSV2ijes-KttAsHVTSPRq0FT772JE1rxsCKd2ter0yEhbIrRur0wVpsle6KxiRNZi4bnc71nNKd_5eSY0i_4aTclo8NsBGwJYVN0pLj5HpkyOd-sJMXxI7XLiRGYrmUBKGy9vxm0FI5joWmA9PeyYjNzDcue5oWSazrXGgAvgfmQktCIOXow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛جدایی‌دنیل‌گرا و مارکو باکیچ در نیم فصل از پرسپولیس قطعی‌شده‌است و مهدی تارتار به مدیریت اعلام کرده نیازی به این دو بازیکن خارجی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/31216" target="_blank">📅 22:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GSUENjH8-aLB_VQM-igD6hfmwr18DAATJus956WBgUL93cQdCatDlhW5aGFl-UegfEJv-BdX5mzZHef9jrWlwGnJsIQvyhGlCDPx0tOUpl4Q0zjqexq_GMayJab2sfTH9isUBxAfcyUhIybo3I2aDzMryH5cuSquvF_ZvKq_d-uxaKjjuU_n7mPsbYuO_m1MAokh6x-5cuxSmH--dqeFCh3jHT495soIy2x2spIyOnoHdI9jo5BhBssomvyB_PsyHvIlH-GVVtNN9svdlHDcoEx6L6gttmwZOrnwQhTu3AUUKYV-Ry2MS9QAEZeqXPEnOuF8tQ5rOfP0GtMKG0IVnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ژاوی اسپارت ستاره 19 ساله تیم بارسلونا قرار دادش رو تا سال 2030 با آبی اناری‌ ها تمدید کرد. اسپارت قابلیت بازی درچهارپست مختلف رو داره و در واقع آچر فرانسه جوان تیم هانسی فلیک است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31215" target="_blank">📅 22:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31214">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpR1m-y0nEzS8JwnLYZ2N0O1rGFGRjR0o2uXEy4zA_HFeTzRbXxO6dXJ0gQcewUQzcUNHqx6M5Yw5OUEUcWy2ASaD-gdNE3asRCragfJDZhVJgR1qbRW2_JKDdlRZDc85FbCswvD_WoC4qtcTeXIc7iWh7Ztjccu9wKylUNr0h1fXd8MI_HjBrbdAJPSRVcajza6rYS1__khH_fnx9sRCk7X-sepFGKzupzchAjDkz5V4bw6_WSRSOPyV54oJ2P5hsQQgcNDm-3IydDXqvgWbcWnzsw9MzFraX63Hg0T2fCaZ7prfeOxMtsgWI0kuVgjNEAYeuw13w_EsS8m2bpOGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31214" target="_blank">📅 22:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31213">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=XBidfChwVa0kHEnbwloG5QhsYIy9FCnlAyO0ZMQH7ldZvkPVr1GjBNXgt8ZldDXyiohsEN426k6xlhK8QUAUYBK-MRuYVaw_6qkvrOdQmlvzwTPndvQPkHw9_QpJzwc6X4mvBENW9elBEZVVwvTXPZrqsKwK2jKndVmvbbzrIeX_HEhYxMGVvADUfnXvLI0PXqPgrII_fpTjz1-jWJew9RcKIMYsViYI-FKC3InYt9oBy_jEef5J69rgZMPec_DAs54qMrW5sVAMSHM6LtcwbwG63eY1wFqJW-qfYz8jqZUThSR5t914y0UuVy5C2TF3GfMMfTXCvYUypAcBHl7-kA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e828d2e24.mp4?token=XBidfChwVa0kHEnbwloG5QhsYIy9FCnlAyO0ZMQH7ldZvkPVr1GjBNXgt8ZldDXyiohsEN426k6xlhK8QUAUYBK-MRuYVaw_6qkvrOdQmlvzwTPndvQPkHw9_QpJzwc6X4mvBENW9elBEZVVwvTXPZrqsKwK2jKndVmvbbzrIeX_HEhYxMGVvADUfnXvLI0PXqPgrII_fpTjz1-jWJew9RcKIMYsViYI-FKC3InYt9oBy_jEef5J69rgZMPec_DAs54qMrW5sVAMSHM6LtcwbwG63eY1wFqJW-qfYz8jqZUThSR5t914y0UuVy5C2TF3GfMMfTXCvYUypAcBHl7-kA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
مهدی طارمی مهاجم 34 ساله تیم الوصل در اقدامی خیر خواهانه 8 زندانی در تهران رو آزاد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31213" target="_blank">📅 21:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31212">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X-F4Sv2JPKvI3Jw6VdaDlT5A7UFatw1ydRVlZVAjsWOEFoxtqqfkF65szgWb2qT_56KnsqqavnI6LSmJDzwAZxgenQiiJ0yImBpxwLLBHBZLiGCkYfhNNwDE3HjmL9_P3aOXeKIKfJAuGcluPCeV6d4CVz5hikSTKeAiNGCFK2YHUoI9tkdpaSNnOMP-_ECoFpX6Rm3MRTWEBafO1EohZsTaorE3G3kqEYKcwspTBGLhU8QfAChSJ7uXZOPZEYMqqBWn2ip-hBSYQR6XCIvGTfFpLOULne5BYxB1xvtlqzXKEDtgRSkir4JRRNU5C3W1YGMRoVxS5ZoGU_-egN2klQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
واکنش‌ علیرضا بیرانوند به احتمال حضورش در استقلال: استقلال تیم بزرگیه. من یک تصمیمی گرفته ام و 100 درصد روی تصمیم هم هستم. من نیم فصل سرباز هستم و بعد از نیم فصل بازیکن آزاد هستم و تصمیمی خواهم گرفت که به آینده ام کمک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/31212" target="_blank">📅 21:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31211">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31211" target="_blank">📅 21:08 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31209">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wiz7CK6HacdKc_YsuYVfKIqzyHz-bqs-8ksJc_zlySX20qDYny8m0EpBfFwVz9YDD5IiviNpc5jcUJAB_LFk1AZZRl-1MNpafMxfVw6uZx29_japZC4EYpVj-SxXYWrhZLVRLEpeqJ3_BwmntRvucUUL-gnkqQL_BfCMKb1ienB1osnT5BmLf8pfXGidkPIcH7x0BA0cz1UX1xIiEM7ByTT5jg0gjrzHIKmtkgpXLD9JJDc5_2AyHQrLurap-qiMjg153XxKgcgRkptgx5HlFI2if3lB-yPXctHOmDv3MsYK4uq9w1qoBEgueZexFBTC64KGFiqS4Adlfsynj_HidA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vK2bcJiD_hhInAiHsLSiL7bBwlgclLzSMfFi0uLvLo7qntUZh14GxDgrOEupuwZb8ab0F57ZeosGs-tlpmjXdrw6hWSN60nx9SxACZQ2rMhyeU7pGPK-qhFpaE48FCeZ-JJ7j21pZ5c06TO9iJjETAJEsnmqj37i6L9h2aP2-2BU9acRVADQGVcL7klRZhEcKl0g_c6mG2cEvkq8wIskWMKoJG6f0SH87soMfOWDzGRfCvqlalCLkCP1eFySXgaiA5QHcf0-H-Pz4ja6uDMPA84Mrv-vcB3y3BSIOChkNriqL1NibuX-kgQu7o_6mbsOvWKWtb8ipMb8umgZjKpxAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟡
گل پنجم و ششم سپاهان اصفهان به فجرسپاسی توسط مهدی لیموچی و آریا شفیع دوست؛ هر دو گل خوشکل و تماشایی زده شد جفتشون رو ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/31209" target="_blank">📅 21:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31208">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=fnctLGFDE00axwLWYxAVhpophiVp7ado9CZ3w_wpADZN0Iarf4s0_gP_2O1MCgpLYLTeawsYtCJ3JuFcKI4Z4Zwe7t87q6yO9MYx9wYQ30AbbS_jqAczhSJJhB499mECr5ocea3Nw7dycSwz_RmWf1JorQrVjkB3k8XpHVXCMj8gy8HgCAs2nGO8qEbN5og9L0m-f3wRdC2RWq1CO-4CdXtjnaMoY7GotWAdmccLa1sVofPiRECuQJPHMMwxZdKm3c5kRr77QwkEcTw4HLdE3PaGCRFoSAXBD5KmM8CTOpLZo_qs1g24L9z8Gau0FEDBCnuRU9vsQjYcTTW3B9E0hYWbe4hZGPhaRT8gDDhwstNUNETXLPDigYhdKmRImcLOtb9IJSCY8A_wFygf4ovory9icR9PFdhWhqZ8w7zOQfgCK0gx8KDBbkQU0RYc6m_Ib9WYFHLTf_LZBtdh8uCoxJ959UDX0uXAEU9zCgPi3KnnODef08LIjHqyKXG2qX-5DZOQ5vNTHyz2TIMratMuw8HfTF0P9pC6ndQtCxRsPk010z8D2vkQTLLkVJGc-jQBQ-3qvKRZTCXRAURlzfQyM0O_947FQRMWUWHoec0EtI57uXsBAo2PvaUeDWWodO1XbtbWyIzwJaM5V24st_LrD2JLnoMwpAluZxCTB_2VQ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd5e0f0ae9.mp4?token=fnctLGFDE00axwLWYxAVhpophiVp7ado9CZ3w_wpADZN0Iarf4s0_gP_2O1MCgpLYLTeawsYtCJ3JuFcKI4Z4Zwe7t87q6yO9MYx9wYQ30AbbS_jqAczhSJJhB499mECr5ocea3Nw7dycSwz_RmWf1JorQrVjkB3k8XpHVXCMj8gy8HgCAs2nGO8qEbN5og9L0m-f3wRdC2RWq1CO-4CdXtjnaMoY7GotWAdmccLa1sVofPiRECuQJPHMMwxZdKm3c5kRr77QwkEcTw4HLdE3PaGCRFoSAXBD5KmM8CTOpLZo_qs1g24L9z8Gau0FEDBCnuRU9vsQjYcTTW3B9E0hYWbe4hZGPhaRT8gDDhwstNUNETXLPDigYhdKmRImcLOtb9IJSCY8A_wFygf4ovory9icR9PFdhWhqZ8w7zOQfgCK0gx8KDBbkQU0RYc6m_Ib9WYFHLTf_LZBtdh8uCoxJ959UDX0uXAEU9zCgPi3KnnODef08LIjHqyKXG2qX-5DZOQ5vNTHyz2TIMratMuw8HfTF0P9pC6ndQtCxRsPk010z8D2vkQTLLkVJGc-jQBQ-3qvKRZTCXRAURlzfQyM0O_947FQRMWUWHoec0EtI57uXsBAo2PvaUeDWWodO1XbtbWyIzwJaM5V24st_LrD2JLnoMwpAluZxCTB_2VQ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/31208" target="_blank">📅 20:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31207">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=Ug5RUaV-vvg0yAydkTAkqzrmyuXZqBlBJBpsn7hJ_DyPuCPKoDBe1fN9kT4ytFDy8Ntk8dG-y1SQlZQ-CM3Cdij9J2WdPKndof6pqLb6ux_2QP7YE4Tt1kYd2__4NoZdw9_KfKdVArzhc-la-BE701ACoEsoI03Hj9cE2TQp0aRN2yOox9eXvKH0jTVKsj6aZ_xnNszXHI3nV_XA-BIo_LcWshhEzqBu8WH66WqL7sMnQUnOHafNi0bvRhegIqOUfRz4_iM0KU5kYUC2HMxuoMdeCYA2bhc4AGzzsaVpCRSBhg3bDsP-t2xo0HYFadU_7U6xwuMWmbomacnRdicwXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b78ef0133d.mp4?token=Ug5RUaV-vvg0yAydkTAkqzrmyuXZqBlBJBpsn7hJ_DyPuCPKoDBe1fN9kT4ytFDy8Ntk8dG-y1SQlZQ-CM3Cdij9J2WdPKndof6pqLb6ux_2QP7YE4Tt1kYd2__4NoZdw9_KfKdVArzhc-la-BE701ACoEsoI03Hj9cE2TQp0aRN2yOox9eXvKH0jTVKsj6aZ_xnNszXHI3nV_XA-BIo_LcWshhEzqBu8WH66WqL7sMnQUnOHafNi0bvRhegIqOUfRz4_iM0KU5kYUC2HMxuoMdeCYA2bhc4AGzzsaVpCRSBhg3bDsP-t2xo0HYFadU_7U6xwuMWmbomacnRdicwXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
گل سوم و چهار سپاهان به فجرسپاسی روی دبل دیدنی احسان حاج صفی و آریا یوسفی در نیمه دوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31207" target="_blank">📅 20:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31206">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDwve4ppfYWgKQGTxq-nw8g1fwPX646WulJA9Hxpbphxz_lUDGFggMvjbzhcdPENy5cpFzDKl7PEIJU7d9q-LxTxACT7rfPLN-dZRsWhzguD0nWSrH4v_JlhXxa8YcPlYgbTiVMb-eFUHOsTzwoP_aNcvqse6TFSYKIADe3neMQIthpvsZtT_kcsuqengpDgm9aXbP3V0-iQFVowWzBp9yWMqLr-g2KNySOvKD518l4pUB33GjooE2hB5CZr8UTFsPEqT7A2PSj28hNKK3qQVkVpK-q7vxPBwi7UzfUgHPb0TLK37k3P2b9AalKQN-7oAc5lJVwq4rbOXsvi5ig23w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دونالدترامپ رسمااعلام کردکه تاقبل انتخابات که ۲۵ روز دیگر شروع میشه به ایران حمله نخواهد کرد.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/31206" target="_blank">📅 20:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31205">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHqHpfYakhoDVTBUfmlODAtGA1NdnWm7EBK1CvNMkMO11kidqmgRGxPfARNK0bcN_7d-_E79J-wDZnitpaDQUWFruWybFBmr_VhBTw6MxwM7ibqkuzNEKDHiJfpRWSOxtSQBoUwxw1P_t25-zhs0PoKopSAGBj-oJnObXjWSpNlSUGe_TRdCjJStlZsKoqdZ4eTof8eb6Q7NUCG_tlYuK3ardLTkeO4eQuo3N646fV-saLuJmPa9IqiLDr4dooVPV1RYzfHyTEglWje7ggWPuMo3NkC8x-O0anT0oVAUuGswFjjw2F9hKnKWfQC2gAu1jtZ16vsexqArZrdsEE3_QE4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20c2c2b307.mp4?token=QPVBFaOMPNQyOMIVMYpMHAq_w_YptGpHC9RcXWnxjqL8dpd5OnlUU5gjNFdY5lA1ksvQyIugy56qqH69Hz6Y7zEcZb9_fUCfsLz_qVucFjnMydwctQslrLKXt58G05UEPl0-1e2MbYxU1o3ixlb67Krrc7mEY6I9XCTdNs-jBJVy8tkDIB01vpA-tYzkhPKGFXhvC7-7w8lwgC3OcUvDtdAXeNJIjIr7aT6o60JYVxtfyox7BTif72-g1lRX03YJ8Kosr2qUJhFRYea4BjKgYJhrLlSE3gjqAgQPPKg98PTLqjPZwu1Vo5F8Z6djFfz1Fi56PYW7BGOOGmY1XrcVHqHpfYakhoDVTBUfmlODAtGA1NdnWm7EBK1CvNMkMO11kidqmgRGxPfARNK0bcN_7d-_E79J-wDZnitpaDQUWFruWybFBmr_VhBTw6MxwM7ibqkuzNEKDHiJfpRWSOxtSQBoUwxw1P_t25-zhs0PoKopSAGBj-oJnObXjWSpNlSUGe_TRdCjJStlZsKoqdZ4eTof8eb6Q7NUCG_tlYuK3ardLTkeO4eQuo3N646fV-saLuJmPa9IqiLDr4dooVPV1RYzfHyTEglWje7ggWPuMo3NkC8x-O0anT0oVAUuGswFjjw2F9hKnKWfQC2gAu1jtZ16vsexqArZrdsEE3_QE4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
یادگار رستمی ستاره 21 ساله فجرسپاسی به این شکل از پشت محوطه جریمه روی یک شوت تماشایی دروازه سید حسین حسینی و سپاهان رو باز کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31205" target="_blank">📅 20:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31204">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b8e357fbe.mp4?token=g7wXQuAVCtvwTx54lTBJix11fCV9Ra9-A4QRKYy1VTAfXkpku5ARy_PF3NQdzSAHhhT6y9D2bpfzv3J9wugMwYWEhwn26egL62-Py-cSsnKJW8DgsFRRnHztymtUaUkwuUcvlfHMLHuxh7-X8saynQwObwOagRfLHd8zI3Hy55Ru3l24_l4M_XzjnymoCRksSbMvv3N6BbljuTRYHAvJMPWJkYC3iCG5UFWJel4Y1Squj8dW61sfSG97OTZS9NQCVkbwFkcyaH68RGTbi2hezosJFqS9OsV0PBI_9WR_4sBe964DoIe6s3ZRMYhBWDtD01q3VdZuoHr8ZLA7nSukZUrFs3HZoAtrF5les5TezTwpiTijQpmkb-rvbSf9_gPoah55tZXHiLpReeFuAMSUmKZNqWgdkC6VwuLrXLAh0lfy6vjBY-HIfR2upocJPdqqyTnGSz90VgTQloox0sudJMqbBdhBjNkZkKYOdH9eAmThz8_MllUJKbVBpkUbd3hDrUWH60IiwqouORclpy5RysTw-D_cGtlcKdRKkfsMi2NZQwu_tm1zE-MN7P2ReJy1HlBSJU6kdt88kiPWLchVEmiUXJIdM1uWXyItr_hBdRohYZBZ1cRGzbFw69-lboJA3bFu2YU_pMT11qiOzYPPBwc0LVCNFonWfEiecB8WEVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ویدیویی زیبا و دقیق از آنالیز بارسلونا مدل هانسی فلیک در فصل جدید رقابتای لالیگا و UCL.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/31204" target="_blank">📅 20:02 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31203">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbbf119a08.mp4?token=rNf26FXw7py_uU5IU6JluPsav11AJfsyYeXvsWSO-UOfVTa8vz9GYteQDlSKUijBhnkjo73ftR67PQoOg1IVnpEKg5Gd4UasEEcsFChBtInu-ZcOSudhTv7L_d1VbA9YJMw7u_XyZRSyBoU5RpT5yaQF8TbOVEVBw19qr8njfJW4F_ZdY5EEf1MEqbzLy1J4Thpz5L4WRUtt4kCn9EeU3hxEc3acZGtPP47sWWfCriArOIcmU4QKYTnYhp_1GmQqu447bMgfSSpoz0NW4rjDep-xEOzsuXwHKtoB8tGkibmP2AIfQEvlTsLg4wUnxYD8zJqJystWvPtkudmgvwWwvw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گل‌دوم‌سپاهان‌به‌فجرسپاسی‌روی‌شوت دیدنی احسان حاج صفی کاپیتان طلایی پوشان دقیقه 38
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31203" target="_blank">📅 19:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31202">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVJ4Cigl8oA2vAS_vi7Mq_-EaP0MqqAKVXC153opja8XIWUv8VFAe2Tce-qqRwOnrEIEZpY7gtWeaYgUOrqBQI0b1GgeK2YBoXQq8o7SqZUj8vlFXt5nx7u-nSIfPdGhGKLxD9iOaulhCG0Zt3tRZ54CbJeuA2EGHQZmhDjrG-oDWCCxc2dX5nnMFztH7ASq1T9Mnp23CwDWrSWXgKxRtOX3u8jinNTYcJFmo5xGEnrW8ZBhozexxY54bbXneUELVgHtwDbI48reB3b1pkyrkIM-8hMEzLssk8Jh-RucoDJc3yNYprpVSNdfkuuwqckzAWMeB9XIJV98F92AB5YpqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خرافات جواب داد؟! یاسر آسانی ستاره آلبانیایی تیم استقلال به دلیل مصدومیت در نیمه اول دیدار با تیم‌تراکتور دربین دونیمه تعویض شد. آسانی چند روز پیش با حضور در برنامه عادل با او گفتگویی داشت.
‼️
پیش‌تر نیز عباس‌کهریزی، پوریاپورعلی دو بازیکن  آلومینیوم و پرسپولیس‌نیزدچار…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31202" target="_blank">📅 19:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31201">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/194218a84f.mp4?token=O5D-e-J4yRihxga4lFNneyXo9wUwIbDwjILEi6j7-PNXXiUZRHBQq_DxoTHnlbQ72xNsnnNIg2BeWrSulb259QAe5f9-Mn16pARlFnFKjkCGKy0zgG2lOlhggbKyUrC3FG8wKyV_lB-skb2SkcqtyeK02p4dbMaUH3oExJNIFLFI-tEldGCAQMypHjSoSAjFnjTYMwzjC6mmk1tHx83YQTFjMgTkOXEfsqHGaduSnzheV4_7CySYGUMsG7FqrVGU_LRTY3on8-yBoaQ-sf_ffSxmTV73FsS3ZpGNn-Eh0aT2C3pT6s2PQ_7dNA52Y9XQ2hlkJlyJhvhrVBAHe6Q0OiAzT_3ucKGAgypdVMJZwhEm9OwDX9JWbhOhugiMhwYXVtXxrhlGam0OX94JsRkybp2Oizy7skbCFflOrFEft7F4W7q5SI_cTnFd5gohQ8EEihzRMN9cjruAxkwjTd3xt_nZW4Y6b-UNGVEp41OfWihgV7Ogzp-H4NF93HS89--THzbk_vvOQxEYUmDZrOudtxNQDc5W0-IHZ5s1s5ELpr9hTAzJgOByWdtYErqhgxYWYzyEW-oig3h5KONGWEyBXgIuKp-BFYsFKy4X1jB-SxIxsYFyBxVykR7yV5w37HxiDMuxaadLLUiFCHNxSsjvqEJcM6c7RGs_Vd0V2vBBjY4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
آریایوسفی ستاره‌سپاهان به این شکل گل اول طلایی‌پوشان‌زاینده‌رود وارد دروازه فجر سپاسی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31201" target="_blank">📅 19:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31200">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b6aefbc83.mp4?token=SPLRJ-a2vKzdj27nKNW2hW48-1q4M4XiUi5UOcHXqfsENBdzmRPBu5Cob91vWAThaFObGUSGM6MTIoWLzBuNfiXIKTU_1NfN-QeZG-YSfOYohc6ustfTINmavc5gVLvtqeVG9pygXyk2LqRo7BccbeT-_xUvrxjIUAeQ5-EYF_v6nLny2_adJ_1Z4eZi4SSf9MqA0wsuxra6keGRu2m4SqK1BdT5GPbGgGUwBqIHV8r-UK9A1a1CmQS6zCYpAfBh8ZxaygdT5HIQySzc_7DC0ESTOdyGcQ-kTewktRcUoO5Frr5IMWosfQtqTLuobIx8DvwEmIcmiNLdApz2LvHJUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31200" target="_blank">📅 19:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31199">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CrLJNDEmu3Ch2skcHs6xqp11KUvd6f87V9miTvKFmDCMeqtR07pVlMz0GF-cbnSEiBMPuZhcfyhGKVkQ8jh3P-QLjhF2BSkRQ_E9CwG8BjWHTuQlgOSt1qs0bGflSTJd9Wpby38O2TELoGPuUX2b_zinzuMllFEU9xl1ZU4vjzwpIKixvR7slrFqtnXsUY4gZ7dud3DQyVFh8tqj1UZpZEgARGvZWwZYnR3A5VqqHsvRpW0g-7EWwgghe1vR8m8qQpHqf6wtQW9omVO2M--IX51YqjuvK12L8hhmOlqtm-3-l2mlYiB2tItFMmydkQEshkOafJLQeynX6PQTO4BA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بالاخره آبی‌ها گل رو خوردند؛ گل اول تراکتور به استقلال توسط سید مهدی حسینی در دقیقه 74.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31199" target="_blank">📅 18:57 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31198">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=P2GUANIjZ6hkxSHEv5AQvqkzrSeD96YaeWlAqpoeiAMvFUxIVLLH0SQrso-6-5sPhXflJv5G34iYpkyW2v1B3JnxdI9_zj2GP8hArWY7exbu_qcn2zJ2V7BUtM7cQZjUVIc91CQ4dNZP2MbcYZOXYbXMqYZEmdYaEUtf8GRVDjukgOev_RVXbV19h7dxbhjYpQHm2kqlw1YNIvl1iH5Hwjdf2zgSLrXfHQy9c5rjLm3yQLB8sCFBKRWA_BZ0yFMfuGJJDUgRmuWS5_wzNaYjvgGV_ShrFLtyCynrdVKhcQTNIF-ru90wqd5UXBZ3RDXWWwsoMHUi3C9SHgCzmiFNGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5e1b0fadf9.mp4?token=P2GUANIjZ6hkxSHEv5AQvqkzrSeD96YaeWlAqpoeiAMvFUxIVLLH0SQrso-6-5sPhXflJv5G34iYpkyW2v1B3JnxdI9_zj2GP8hArWY7exbu_qcn2zJ2V7BUtM7cQZjUVIc91CQ4dNZP2MbcYZOXYbXMqYZEmdYaEUtf8GRVDjukgOev_RVXbV19h7dxbhjYpQHm2kqlw1YNIvl1iH5Hwjdf2zgSLrXfHQy9c5rjLm3yQLB8sCFBKRWA_BZ0yFMfuGJJDUgRmuWS5_wzNaYjvgGV_ShrFLtyCynrdVKhcQTNIF-ru90wqd5UXBZ3RDXWWwsoMHUi3C9SHgCzmiFNGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
گل اول تراکتور به استقلال توسط هلیلیوویچ در دقیقه 68 که VAR هند بازیکنان تراکتور گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/31198" target="_blank">📅 18:38 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31197">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7d03b757a.mp4?token=UMAq3XnGFLcwqe1bhFxak370shKkDHghQT3IL_0F_F20XavHp-DpbdY1WIDa53_1vq4AksxYjRgSFAoasMkTlSRMUlr5xneOUK7ttXYj1nX12fYd163BS8zsasf-zd-UOg3eAXWAbOeSPBJZut6Hkf9Vz-spi_13C85_rsmdW2peYxfxDyHq4Dy0rYLefQwvpQGQhISScH1G_zmU1ZaD0LkfUfw6QlqU9t3CLS2avMCucjTHyM2L9xRdLTiRbVc8dam_7Vv6EU2MHKAkGeP392Ipp44x8K1nDTP744zwAm6UGw8L6m9dfAQep0pfqceGAbUY1ouOx_ZN3FGGjrZQ9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/31197" target="_blank">📅 18:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31196">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsC_rsAsxqwFueO1tzh1gubQqPZu8ZfxLosfQFnG6FXhSHkpEL50TYyFs8ZvjvVfu6mEtU7ogJZPhaAyOgSbbBT534uW5sMkLAjQC-w522HujyCShkFJinq2rz0ipJ9qIoNNsOMtR_ouIS_3GJ9M9Re5Yy6UrrOl_9a562xkd4LZswcegFcc-F3F71C6rrhThjb7TgVBD8orPfJZYkE4ieCU3NpyRI_USoAo7DBdwKUjtmuhyGnpfUw9ip7ZBWlrq9_Bg-UK6BqFAFkX80w85ikxSYqult8J9YlzZQu9RLz9ikEIDcJytlkTmBqur71l9VEJEmU5oNaXiSkMbe-T7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
سپاهان محرم نوید کیا امروز ساعت 18:45 با این ترکیب به مصاف فجرسپاسی خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/31196" target="_blank">📅 18:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31195">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVKQU3UFImzyd5xIGGfzcfAt3ErVevc6kw9fvHDoQjF73iTKTCtRRoPXpJ1cpTM6RinqmKjSrLuf7ZY1Qx5cwN4bCXgsBRufI3KS3SvaIARJzI4bREJEdMKELiTKWHZTYI8TMLbkbNIT-jJ-6Gixhwsa5tsfj2xaq_h9HyJnseVu8uEjzYHl_yBv8vJnsnww098T-xlPV_821R9p4Me8Kd67tHWHgJ493puWKGD81jFSMEC3Bk3Wqt9mEC5EyilLqN0a8EUZs7OwEYospQIw7LPdR0zO8vCmd6azsU6sv2Q8wm5_nlM7JSiU0-NbAbqVmdhPq0xgnr3Qb_L0x9G4dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
استارت‌انفجاری‌ستاره‌آبی‌ها؛ گل‌اول استقلال به تراکتور توسط سعید سحر خیزان در دقیقه 28
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31195" target="_blank">📅 18:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31193">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MXGrRlaub0GZOrrsojrW7PzxcxtV6EtLcJxhfPd2Hgq1EpXnhTm1LcO-NrVGYQybHmF2aDzqwTma5Wo16YGJWphFzZuHwoZwgZTxPKnpUCP6C9Clm51o3pyOg9zfl2ZUiEKiV0pO3RxWTOB0WwP8ys_LuqsNovwLYnTt5gzC1XsQWY2zx8aePC5PtuyE-zBp0j1evp3mLgl5Tpvx4VPY3QHIyfSl-VvuIWTNJ2rNoiyEwsNxKmNrsriFyC7aCcc7_Qy4euaKTA-oPkqPUmZCce4ZBE9mNxre4X8d32IDSooVE_FSFvJVt4cyMkDLmw3CmGHq5vpoJsNOeiXxNVWYBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aZ_gXZQ8dNRsD5kuvIw2zKFiw9jqwaURj-3wOVQRJquw2Ylj9odMd3DxgQPFuQVkGy6acSuo090p5FylKEnNoFC7lE9dcAtwxUAuLrCK94DNI0JIQirZQu8XvXC1VMYHhxb6miZsUDsgvSr2qv4TqeMIUCGPjSCFGZ0RIt1OIxBFlaCG083f0_I5xiquI5EF2NtVqCFyOdCrEFV-qPr_UFRpxm44Qt0dgDCmCa8nt90ukw86z-q_Kx3WprPUkOLuN-k6QeB_jOIbugH1NrHGkXCY7nn3BjkTyPnl8VLd-VSwrPe7Zyl2WkCzjDjxowDGnsPljWQwTT2GYhiEVDZIbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سوفی رین اینفلونسر مجازی مدعی شده که لامین یامال ستاره جوان و پدیده بارسا اشتراک 12 ماهه اونلی فنز اون رو خریداری کرده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/31193" target="_blank">📅 18:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31192">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b022014318.mp4?token=Wh0T6kUoeIcSLAwVdHuD2rwRDHzvcDA-bLhB3m05URkaNA0QMa_hkervb7Cy4CzU05KHliMvcmQ9I5HOfsawmqPwHPZyTvgx7Xdeq06x32c6fTk2uQbBASmtYvDAvJoxZGzsyCYZEljkz2RbmEG5iOpew_S7A1uvyfxYw7o43_5fEFBgmpeRoMZX4_JOURfixhyW6xFsA8hlxm8W-3BU3KWYP1k8_2Z1-AYIuSELYJtJAsEOAjRpmBz9hv-P8lyiSo0ONoaV72X5M7WlOsy6Pi7jWw5njxuqYQOqxnKZ3f_8Rown7PzUFj77AFin-Y6DH7OqzCGhBIXM_O7CssCcTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
گلزنی‌سامان‌قدوس‌ستاره33ساله الاتحاد کلبا دربازی‌امروز این تیم مقابل خورفکان در لیگ امارات؛ در پیش فصل باشگاه پرسپولیس خیلی تلاش کرد که قدوس رو به این‌تیم‌بیاره اما مخالفت همسر او باعث شد که این انتقال انجام نشود. همانند مخالف همسر مونیر الحدادی برای بازگشت…</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/31192" target="_blank">📅 17:55 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31191">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5UwhbCmReQZZdplv35jhMFtPODMOxaXPELMeo5dtETgeFHNMTSHBnmAtB9h3HtJWLL2OMosVlaWhrPHZG6yFJMvBL9jj7vZxqxzRmKGnE_qOfAgjKOEV5Jz_fw_O53lpoGGWF526XGqfWMpgq20DtQRZ6-M_vcy2Yzkft8YBzazjk4WLF7S1j6unoYCl2CHBiVx-TUQsP-fOaiuXlEjhWP9SDNmEMWFYKYE-I0mzr909264hq812dJIUlvYiQpbz50WIzLNIWddYdMLhjdSH4IIjEWTxevzQfjOid3yFSOI3GozBkWRyxJ3Y4QcWD3uSxK-_MHrjfPYu7_ohsvMyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
باخداحافظی پدرو از دنیای‌فوتبال؛ از ترکیب استثنایی بارسلونا در فصل 2011 تنها لیونل مسی باقی مونده و همه خداحافظی کرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/31191" target="_blank">📅 17:47 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31190">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=s3TbmSUQylWxvSGLzQrnseSwCB-xTvdOFcUKJp4QeEpCYCPh39XEFt6ifuQw9WpFAlUwcimcCCRxAbMr0uCm_JuMRiH0A24jUOu6ttn9Gebo9c3THhkasIoHqpc0eCHpujajPxama59vYkktlpr9Icy4WnR9yDoNf-dcGsWyAi38jQ9O0RXZG6QWkq47OdTLLSPudvP5wQROuutyV_gmll0bJiJA9yRTtr6MRfdLIRCfg6qA1nBKrVb-_-sc62XrLuXdfpwGUSYkvqKkaGS65yjpHxhVmZp9MY9QgoNjqgyBSGASi963ng9f9r74yDcJnQUJ337nv8mCacMav9qQZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5be0608b6a.mp4?token=s3TbmSUQylWxvSGLzQrnseSwCB-xTvdOFcUKJp4QeEpCYCPh39XEFt6ifuQw9WpFAlUwcimcCCRxAbMr0uCm_JuMRiH0A24jUOu6ttn9Gebo9c3THhkasIoHqpc0eCHpujajPxama59vYkktlpr9Icy4WnR9yDoNf-dcGsWyAi38jQ9O0RXZG6QWkq47OdTLLSPudvP5wQROuutyV_gmll0bJiJA9yRTtr6MRfdLIRCfg6qA1nBKrVb-_-sc62XrLuXdfpwGUSYkvqKkaGS65yjpHxhVmZp9MY9QgoNjqgyBSGASi963ng9f9r74yDcJnQUJ337nv8mCacMav9qQZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
شماتیک‌ترکیب‌تیم استقلال برای دیدار امروز مقابل تراکتور در هفته هشتم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/31190" target="_blank">📅 17:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31189">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04026264da.mp4?token=XGaAxDb9AII_GA0uR6j5UJtIOexgB4xJsr6N99l4fukZBA3NBZFNyvJ4RX1-9k7SqvUR2eIk-Z2AeKu70u-g1P0MecH-PmrMlLjk-UOlgB_vbE2e_DfeFtVoGltBkFypvAMa0Rp14tN1M-GFYJsq9H5R5T6iCWf13ycynBf_7pvBzVqVX05yupiNE3s8w-DJuHA6XyRL8mM72OJtwDucw2Dsu8W8bAcEPo5x0ZZSH5c6I1DbhiiCNgAQtn5t2riGnb5tuaDSlOe2OxFwlKknJq9VuXx2I4OC-XjuXS6Fs17W0v_lZWGQ1WegGzyHiRNUJWyFKNmjSHix--fFfWpc-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درحالیکه هفته‌اخیر سارقان تو اتوبان همت تهران تلفن همراه‌آیفون17پرومکس پیمان حدادی مدیرعامل پرسپولیس رو زده بودند. امروز همین اتفاق تو اتوبان تهران - کرج برای مهدی تارتار سرمربی سرخ‌ها اتفاق افتاد و گوشی جدید آیفون 18 پرومکس او مورد سرقت قرار گرفت. خداروشکر…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/31189" target="_blank">📅 16:40 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31188">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5Bj0XN50YnqgXIhQ9pv1yd4Ssz52DsZz0yFe2zvGRarxHE2nJnl9nO165Laz9l8vfMNlXJHA12tJ9_8HXZIUXqGw_y720RSFFIunO7G8eefsS65pBcbXoScAakqAM_1tMgLzpmFHQdLzumsh0rK4VAuWfgz8STQKAE50dijuNqKSkBj4mPyN2SNv_Tl7bcUBU5y-XhSyD3kWxPRxRxLoff_-OzHP_mfNAA22raBISLYzwB7i3p_YH1G1Hgk6kNVnTPE0vHA0kPZU7q9v7qSGyKo77g_EziYWBz5sD7jBs_fMrmQ7w1PMm3_zBfGZRI-3rD2do4r2g5SolcN975kjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرونده‌پشم‌ریزون‌وجنجالی‌فوتبال در دیواندره؛
دو مربی به اسم‌میثم و ادیب 5 سال توی تیم فوتبال ستارگان دیواندره‌بودن‌که توی این پنج سال به بیشتر از 50 کودک تجاوز کردند! به کودک ها وعده میدادن که اگه باهامون رابطه جنسی برقرار کنی توی ترکیب اصلی میزاریمت و میفرستیمت تیم های خفن تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/31188" target="_blank">📅 16:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31187">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sbLLG_lAOd33JpKa2V3UzQ2xbVS7ieacM24-YdJsM5QSZP7OaFNzpvPhhD3EmCHOnOehyxDxG_2TBODCmNx4f6Id9lkYrEswP_VbSlHoKHoTbE91gSrkF7EDB2dxqtYiIKO3YUMtZgACPhRMrnjDQIOTJTS_CWQgYJPvN9eIIVqKq0Nu8Ywlq-8ZE2px05hR3MAolb65SSvsK39sQBZuX8_fPxWe2MfKJ4XzlxP5fwxLgm_95Gr1kuwVE_lJxzfk9jqLVt8N5pm-H0yXF008nN864yEP6-L9a7cDJzNiJdP-tyTS6xuPGHVEqo9jSUOz0vy-1y6ngzAopmiGxs1mWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب‌استقلال برای دیدار حساس امروز مقابل تراکتور؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/31187" target="_blank">📅 16:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31186">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O9p97iOjHR_zCtEIY1MsZG1qErDWd7kmXdUZUk9ndWvAwdjaXNww0wiXK7_F3cKnMVXfWKvT6hjDCPgJiD8MlIHH85bTN5VflPn5w8rfGwzleCM9knBe5oM1q8ZyblXtIHxWShQX5K7lPjt3j_L5s5-1d6jbvoPHUpuTLuHeSlGSTD__JcfuFNoUY6ixraR6oAkOCQy5Ilo58K5gyyGmaDISZ41-1cPbF4gorHLzxAmvGOgsRZOoiiWA4ocASN-gG6p0ePfnAOCy1okWSmH_sxnM2zGmWzSbfGVNwNaXe9_yD0e3zwiaOyean6BShKbkumJg5sfT5slLYOcfDljUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌هشتم‌لیگ‌برتر؛ شماتیک‌ترکیب تراکتور برای دیدار حساس امروز مقابل استقلال؛ ساعت 17:00
⚪️
Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/31186" target="_blank">📅 16:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31185">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BZ63jdLzobLayL9V01MAIcoXB1KFEosKYdMxmVGXgkUVIm2w6bmPKopSSqiIr09tL7gG5CG-4VYerfQDRBByv_wxu29ZJZyC0tV1ZBLik6uUpXP3oLcJZr9oUngVfonz8c0ZAoFolfYqTZ2IeJk2fql1MXoizpGod2QaNqsPaLt8-AQYidW5o0GRwv-6D4KzzlfjYpm2WcYCPVHIu5UXI5i679WiJ-yZFFLeBmqtemq9-ucnxntGI3SOVW5pK_Pzlj5KEa7pyuahJQ08DAoGcHaJMimQ2TVKc95B1tU_mnpRp2RfT1vS6FlWaGr8dGinvxhxBjFMKfJljZvOkJiaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31185" target="_blank">📅 15:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31184">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9307641030.mp4?token=ZCD-UWWYT-16sMWZPelZOPENTdWfRNq5eaqqLJU6UWSNCZOewpPsKJieeQrzp7P7KLLeLfwHnfTZXUmdlulCWP0A2xCjuLcxaY1x9XUOiAAKxUncF8ycEAWgiQcKEu86aCQsx52jYiRPP388zTdyYHijiPnkl7HUWodKQyx3HQdhxttcq3wHHfwGEkGuJ1CbV6oOwrB-iGBbTHOeMhNowkGhooj3MsYvboICSB9LfsmGLax62IiPYl9CjKU3HpWqoXsmgsccEDAmouqhwLpHrwGDySYOiwq1FuP0w_fI6fwSD1vXMzuoGK5EH8rUVehTsEJXfD0FypBTfVH8Lv7rFiwXI_CzULBot8qEG5vv3mWgmveBPtRumXlPB_J4kQ0fLjk0-ZkyRhkpMMKs4Cdp2EQcPv4QDbUwAWbLteIVbwmVMOH9iNrm0ALLxGvNZUGmDEOuhOxtOawsCJ-gL5NLaAuLex7yNjpGCPIqFbw_z-6g22_yvnA9ibaW3khUJp4Cy9d2hUUfdlkpFzl7UT0VBtGWZ_nLIbWELxjVzm6QOqubTK-GQkoyw4Q8udqXwJ5KZoo8Q0YYzgAxpA0IoOxFxv7esXF9zha0FFIlMVbDl9Yf7HsFgMUeJzqn79CwheWWJYpJURHUyggbRhkDJNjl1gQ9UvhWTDxIi7FZO3tswZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9307641030.mp4?token=ZCD-UWWYT-16sMWZPelZOPENTdWfRNq5eaqqLJU6UWSNCZOewpPsKJieeQrzp7P7KLLeLfwHnfTZXUmdlulCWP0A2xCjuLcxaY1x9XUOiAAKxUncF8ycEAWgiQcKEu86aCQsx52jYiRPP388zTdyYHijiPnkl7HUWodKQyx3HQdhxttcq3wHHfwGEkGuJ1CbV6oOwrB-iGBbTHOeMhNowkGhooj3MsYvboICSB9LfsmGLax62IiPYl9CjKU3HpWqoXsmgsccEDAmouqhwLpHrwGDySYOiwq1FuP0w_fI6fwSD1vXMzuoGK5EH8rUVehTsEJXfD0FypBTfVH8Lv7rFiwXI_CzULBot8qEG5vv3mWgmveBPtRumXlPB_J4kQ0fLjk0-ZkyRhkpMMKs4Cdp2EQcPv4QDbUwAWbLteIVbwmVMOH9iNrm0ALLxGvNZUGmDEOuhOxtOawsCJ-gL5NLaAuLex7yNjpGCPIqFbw_z-6g22_yvnA9ibaW3khUJp4Cy9d2hUUfdlkpFzl7UT0VBtGWZ_nLIbWELxjVzm6QOqubTK-GQkoyw4Q8udqXwJ5KZoo8Q0YYzgAxpA0IoOxFxv7esXF9zha0FFIlMVbDl9Yf7HsFgMUeJzqn79CwheWWJYpJURHUyggbRhkDJNjl1gQ9UvhWTDxIi7FZO3tswZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افسانه‌یاواقعیت؟ بعداز ۳۰ روز در قبر چه اتفاقی می‌افتد؟ روندجسد انسان‌ها بعداز مرگ به این شکله.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/31184" target="_blank">📅 15:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31183">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4rrCwIYpavfo4vIMek1sxLLLdi4DMqq-5zGx0NZ8Vjx8r8L42LbBrDtORZ7EoxpgQKR322f4V9j7bf9z9fP_SgPtdshiANM7NNlCqNX8Tv9rSWLvE2aT4pShqpL-0RLLt3BPNRzbeUzGsPB1erfIFRq-5qZTqLiYrYmDYPXlrzu7mAUkR_7Eblid_cTm_1p7LhVRz2-cXHFYFbRq6SE_hLg4O1iVn8tobXHc7jptzoMW0mD2qILWbkVoJwtnRgqYpBuhKhPzpRPGGJrORPJzoJYNRbO3c4IbAjc346id0F-O5Xw5Qag56wwKeWFxXdOALuPG60mfWitCLk6PIAHsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌امتیازکسب‌شده در تاریخ 5 لیگ معتبر اروپایی در یک فصل؛ یوونتوس در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/31183" target="_blank">📅 15:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31182">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JDQGmEPWD1rufQIdUCbDFrPuD8C880nf-kRLGVqSgFjDZp4KdzSk_Em06_b3Lhgs-IprH9GvUfwPOrEkn13MeYLYyLMrMtFEsZkJKcnnOfLYuPYj2KBfWJ4PfQU6ZykwJeWTXq6gKy0axI5-3ouUNn6MAHpa7576ipQDIvn6mXliayJyf_mtQFfeEdL7VeNRobJA-Cd0W_yJZ-9-dHkO0aSP0zNfVRy0z_iEIXz4Ky6scVeqe-YEG0jnCHDzc2u_qcEnncnnTYwUq08HljW-kocMNiIACbO2NxCTIZo0oSca4-ncaD04HCMuB5PJbTICmhAfz3056ESbZWaVHs5Vnyk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c815bbaf15.mp4?token=uYlrGVlgRL0h8UszYl7elCoHLQQFY7z2DSAqwFDUuk_lmO_kstoibf9dCaNmHebqYY2OF7-UhKPNiIMfjf51Zc20vEmGO2Gtq1scScZaQbB9WNj9pEGcxTuf5DDvjPVtgi2MEARJQ4HXeVqGIbGM_Mq46y8gmBRnRn6qZJ6pRBy6cthbEoq5cfEBZbvhCKweikrY-82SSiEZVlUeBwNmOXujNO9joDvf-a95JXccRWw50bhknCW-GlmHxxza-51yf1hvfkXShntFhbv1UklSgZ1Wj5gOYav724X7U0GPAwp9MkC_g93346JzKJdDmdZyMCXWVGVkTZlSV7Klcf21JDQGmEPWD1rufQIdUCbDFrPuD8C880nf-kRLGVqSgFjDZp4KdzSk_Em06_b3Lhgs-IprH9GvUfwPOrEkn13MeYLYyLMrMtFEsZkJKcnnOfLYuPYj2KBfWJ4PfQU6ZykwJeWTXq6gKy0axI5-3ouUNn6MAHpa7576ipQDIvn6mXliayJyf_mtQFfeEdL7VeNRobJA-Cd0W_yJZ-9-dHkO0aSP0zNfVRy0z_iEIXz4Ky6scVeqe-YEG0jnCHDzc2u_qcEnncnnTYwUq08HljW-kocMNiIACbO2NxCTIZo0oSca4-ncaD04HCMuB5PJbTICmhAfz3056ESbZWaVHs5Vnyk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زرگری حرف زدن جالب و عجیب و غریب ساینا کریمی ملی پوش تکواندوی ایران که در مسابقات آسیایی ناگویا مدال ارزشمند برنز کسب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/31182" target="_blank">📅 15:03 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31181">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OjAquGmFGvjHkProacQxYopNyIxEl_UiAh9jCebB5rtyRehGcXPNoNKpegebtk8h8ZQKwGLQp67ziGtIqdjV8S68UwqkYYZD9qZsXaercvu7xYcMBz4L2S2F-h_y_0om-a-93zYWXUxqMVz1Izx4FS8DJGz4AnO_lMMD2CSqghKtajX5nThJue0uuGbVpZTBI5Wqc17ruta4GB5vjKMs_PEGKEKt9VoN1qB8fEJNsHt51unYp6oYv9eFQFJ4xgnJ6H3p4wl0xqfZ_odtvMdGjnSkREgoVDDUKtgficIKD4ZVt-F91d9UuKFw_vWbo6KlZV6xIY92wE51gLV7lVoRMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31181" target="_blank">📅 14:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31180">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FMGi0ydpixFO_GKqhz699dgWGefWt2Hj40SGoHiZchHkUKzZOrFML_SK_acLOLi1bQSq51oR_8CyigQa_Y1XzrMnnOhps9p3mw4PvCw0nd8_Nt6eaOsYhuLFdOA-NmZBrneQAPOSBigwf8B_aYFEdctrg2jzaEB5gcKIScbsxjVuk5bP0pDOK9nQcd7g2XPb1FqvZ3Pf14ffrDDB1ODsjQsAeUPo2wYaQyNpHoQGvczOLYup9Wpl_npRh6iyhUUOye5Vf2cltfSUE7RKijQSHJ20VcakSe70lHAMquvXoSVZHvSTLWfoGrXNWYdh3okrddI1jOplaDsYA_NeIeWM5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک…</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/31180" target="_blank">📅 14:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31179">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja4AzGK6C1sX-uUOwSfsXQH6gDExuh-J46S2vvG6L-id-kinIHfbt3I0e4H-jb6R2dCu_eTSP-doYAqCsReRLTTB49ZzblJ2SmWLYWJMGhxB3Jfju-DVt2wMRhAfJR1Sm45Wq3RRxJnKp6Dnv0JUkk3AksRmuVu0dXnjM7xFbkeG1lndra2wrqdCUrtniRASKjpSxfV7eKqNyNkdRY51nYd7Lk33C3e9xQ59GgO95idpo0AFxcZ2B1yUlxUMPfZpb3FnGGN6dW-WrOlCKma_X0TnnPDtE4sPzo32UoJ2hwY9_x-puu32ed0FYM7MBNGWOmIJl0cDRvrUoarvoluDfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
ترکیب تیم منتخب دو قاره اروپا و آمریکای جنوبی درقرن‌بیست‌یکم از نگاه هوش مصنوعی بنظرتون اگه باهم بازی کنه کدومشون میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/31179" target="_blank">📅 13:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31177">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G4CwrmkgJ2Y6rWdjD_uRPcwNNvXYe5wWwZeY3BeLZ9WESkcCcVbYyCcgiAEzDkq9vR3AxZjolaijaATrPxZGjiYVqonhQUo8gISIcVwIH-lSKa5Oq-fc-SnDwyvVWuhhsI4F0yXG3_zUMC6qpUp9d3Hz7kU8c0ptV4q3bFFPMaMveyPQ6uDFpP4Z4YSzAE2pb1WP4jcukTmfpIRQXWxKOIturt4oNswKoerEn5UcdjCBKPuTdEZCxfa5JQPWGz_kdsxR-5-1YCutyr0RVyJoKTDgx91tdMYHfXCZ39ff8ZaUhDgyF-ZALI93S7vcWjh6Yy9YEl6W-qeUOITeJe9Gnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p79H56oYdWm9FeRrOuaBfeObLjnMl1-R1DVtNv1fWhA28MJuPG9DJ6gRLkmjKCBWG9b0gaHYClt5dhAgOCE5JPHMOCPkKIOKVs-kyUyKgsoBY21qxjFWuBjVbdhuh0JxKL60E1v2Y-igSceecA3prxaLpHLhebScYRkQ436QMk4eRX6CYIzRevuVPBH7EehgoREYrdt7DfUs9ztSHX5hfiboAjsluHQqfkmWVyQfR-hSS7bJ1DdQGtHfl-268tXPXg37D3bkv0smlaWimUKTWUMa4eTJzU95luecYn3yb6_xjusrU3FDts6v1C2eCr_5uIogdzOnwAK5QZp_TKp6lg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
پنج‌بازیکن‌برتر قرن‌بیست‌ویکم از نگاه هوش مصنوعی در دو قاره آمریکای جنوبی و آفریقا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/31177" target="_blank">📅 13:34 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31176">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_TrZeRST9JinW3iB6wbBAEx16amX3EcvR7X_MjLhnOGT1fV-MKmgpFktPSzdjLqxEXPoaH0giIcvkBCYB5uhTB-kiWISsKM5VjDbEVqm4R3TMikv2u3ay9T8U46SFBH7nAKpOErk49NSVaTbO21WZiNwnLinMHh81Q5nJ7GOB4wRErlYrceRbtnLjysC90XD7DpLxWWzL27eBj86j1wV1haHt9K41P1tuWYe9J8Jt2IC3Z-eoIhNy0lA1Kfiud-9K6bd9uSZFD2lTKYVPM5Kqmg94oDvzitO2Ez809NFC-kpkLVOvcXPAlUQOye-Vkb2Iyx2Xm7YZHLyriI-Hs-lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/31176" target="_blank">📅 13:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31174">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/txqcmF9HL7wiOEkudNOTdAL82rlxHY4ATr3zpSGdx7UaHNolPon01VVQyrA8_93-C47LIJcLGy50SrJxc2WdSs1HEfWLbPr6sC_yDwmmuJDo3mOAJ6dkB3qlEQPFGv0SBBuvFgZAVB_d1Y7AVODli7U6NhzRu_IpBGUh7CkB5yIU3X9Pkr71OLUAOlKhCvIic_b4V8fpSe-zH6OGhJqeSWt-rw9gCEZ6AgS-9oaAOrSnoWZgOgkvQvwzxW6UDcgD0wAsSdAe01YKfuHxAxQMUKKYd2ivgl277OO2nxjvgyL1usP0Vt5iaZKP4mBtVE8vtDdxzJ59qdLhKvT8bZ2sWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد پرتغال، هلند، کرواسی، ایتالیا، فرانسه و المان در فیفادی مهر ماه با کادر فنی جدیدشون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/31174" target="_blank">📅 12:45 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31173">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=tYIlVrlLXcIpV1SaioiL9v8y-_goSmeq0hHiM-cnqAgUIVxHh0O6mdvb2jNTdhnNa8_OjjJi73bDixfVT-jloWorURpeJL1_P3_ZwOSy3zY3P3BsDAFy-eXdtqL5vLg1pEGjt0VASJCPuHDmpMQEzHQkJCvQ0T0ywCl7hdsjRjHzslTxuCnCs02BV58stJqQn0eFTlfgzInaxoZhqmfJQavyyx7sI7cU9nvMGHNBtLd3LbYn4kDffilsqkRpWyWOQ7wooePb2GAFILDshibendBilOBsFL8CJp1csrIAehLBWf_AsiJ1C7si5hmxp7ef-6ecv5ZUMrQtK8Aii3vRPGWSJnlFtdYQfCjTItGcXjU98fW0FYLChD0VB5qNKbpYLhkvgCjkwf2QyKUO36qf3C7nNKqf08xUipdO8EqLfrt6piSmsHzHINa6i4kGP70BmtVe110Z5rFZKrM_PofuTA1-uZgkVi4Pv7GtlQjWGZ2_N2MWo4UUi5yldyBNR1rfalvvyj5efO1f_i9EQLHTX05_Q5VAWZ0jwfrDcXSZgNaC5hgfft0XCkOWQWYgBFwtUBdowBs3L5i0rPeMFnH65_KCuJRQil7rGlcvYxZUaSeUH25hIHXOHcxPxoPDxo4mOPmDFzqufK9zSmpUzXpssVsDkpXXHYOdvDcMsG433G8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8eb012b6f1.mp4?token=tYIlVrlLXcIpV1SaioiL9v8y-_goSmeq0hHiM-cnqAgUIVxHh0O6mdvb2jNTdhnNa8_OjjJi73bDixfVT-jloWorURpeJL1_P3_ZwOSy3zY3P3BsDAFy-eXdtqL5vLg1pEGjt0VASJCPuHDmpMQEzHQkJCvQ0T0ywCl7hdsjRjHzslTxuCnCs02BV58stJqQn0eFTlfgzInaxoZhqmfJQavyyx7sI7cU9nvMGHNBtLd3LbYn4kDffilsqkRpWyWOQ7wooePb2GAFILDshibendBilOBsFL8CJp1csrIAehLBWf_AsiJ1C7si5hmxp7ef-6ecv5ZUMrQtK8Aii3vRPGWSJnlFtdYQfCjTItGcXjU98fW0FYLChD0VB5qNKbpYLhkvgCjkwf2QyKUO36qf3C7nNKqf08xUipdO8EqLfrt6piSmsHzHINa6i4kGP70BmtVe110Z5rFZKrM_PofuTA1-uZgkVi4Pv7GtlQjWGZ2_N2MWo4UUi5yldyBNR1rfalvvyj5efO1f_i9EQLHTX05_Q5VAWZ0jwfrDcXSZgNaC5hgfft0XCkOWQWYgBFwtUBdowBs3L5i0rPeMFnH65_KCuJRQil7rGlcvYxZUaSeUH25hIHXOHcxPxoPDxo4mOPmDFzqufK9zSmpUzXpssVsDkpXXHYOdvDcMsG433G8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/31173" target="_blank">📅 12:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31172">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EBFLEwsw8eWyxHZtQwteUfOGyFFIzTb_lUH0W0lsaCu3Ga_YwVlB6lYDFcPCoWFbGYlcIACFNOvw_O8WQsDUSrwVtmzT_Ws9oQRm6um9l5C5pnNjUC5gceizwJVroe7xaZ10gzjmyGB0M9tOJp-of_MSSBefp7FJg6Xo_95E804y99ohgsDJDRWLMZAwiic3bX6R7eSaerhhIqWUwJ3G_t9xbycjO0Zheq2t-sQwRlJqM_OCehvUTPKT2EVMdtT37JsBM1Dxrf1n1szjnC0uZaL0hvlFHKdeZLv-rd9OsRgkE7tg9VRzx_8TsD3kwt_mljdrZHr5W9ajqYzWGe-PMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:  «من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود.…</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/31172" target="_blank">📅 12:06 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31171">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Od0WaZX2ebK6TYKDn9ExHvNyzAtQyF3-1JJ2VqdF6XZyvun44Ugv_jcG6JhS5P4g_iBdRNAfh-8BG5fJqUwdY1nb7oOTW0KdPJEMbP2MIHHTmfoQSraQgZxuU74svT5lzdaXHtujPTIVdsq7ot6NXSFlUsHXBsJLTUOfpXr3bA4c9oZrybrYJBkAQ8IIRYHUzpc6RkfOHaXV-NDYInBtkqFGdvelFiaNKicarBo6DPULZ6z0u_GyWDcUJ5xXI04dD5j-TXp7AWSJaHoJLbPMUNy5uNn6ON3m1QLKY4uOZTIRafSfdVGhxSRIC3pOnubhEx0yhttm5v4bp0RnisEAsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
سر الکس فرگوسن اسطوره منچستر یونایتد:
«من از مرگ‌نمیترسم؛اماوقتی یونایتد برنامه ساخت ورزشگاه جدیدش رااعلام‌کرد با خودم فکر کردم آیا آن‌قدر زنده می‌مانم که افتتاحش را جشن بگیرم؟
‼️
امیدوارم‌ساختش‌زودترآغازشود؛چون اگر ۵ سال طول بکشد نزدیک ۹۰ ساله‌خواهم‌بود. اما می‌دانم که به‌هر شکلی در مراسم افتتاح حضور خواهم داشت؛ چه جسمم آنجا باشد، چه روحم بعد از مرگ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/31171" target="_blank">📅 11:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8MpXMCz9kcBTrtpHJIXYOFwYjpLxhRk2M017uy3MpOB4p2SermRD6TiAH9w0PvG4pdDGG1uGpsX-f2Qj7ZiuCXF-bfggJtmrGb_Lcd1SmfXl2YxMxSw9RKyxXVNvHekazJp-2AvG8d4HisdFlgIvOEVvIvTw9McV-QtVJ6bjc0YpC0vK74Xd7BXwFFO9isSYoJCbwC2EGyu63F_PXkQIoe2C9vzZjWvWaJmWMyoMgKDzkZD5AgKF0zHXhqncnVzxX4DXT7vr_Q15GzphN817rRmzstIAiu1LZ0eV10LBxigre4w8HSimWnfXWAv_CCpfrbGeP1CpnLI3RcImXQdcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
به احتمال بسیار زیاد تراکتور با این ترکیب امشب به‌مصاف تیم استقلال خواهد رفت: علیرضا بیرانوند، خلیل زاده، محمد دانشگر، دانیال اسماعیلی فر، محمد نادری، سیدمهدی حسینی، تیبور هلیلوویچ، هادی حبیبی نژاد، مسعود زائر کاظمینی، امیر حسین حسین زاده و شهریارمغانلو.…</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/31170" target="_blank">📅 10:33 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dC06njPaUZySHXjlJGPczhmQ0S_416OZ9ZHSUeZazbX7EFaSzgdRPBl2CnPpRAK_S0v9oF5lZTih8X-FNlB0g7cNmLvgxdf8M6Lw2v_mI0MkkoiGS34fpM2kj56q7Xt9Lw_Bx9bES9mTrCIOzLKpl91yXBIaF4igcJ3hSkEks3dqpbvvEWWrDoB3pEUvSBGKTPF7EEDMz4pr8kudVn0Eb_Y15Z3-QH7pGg9YeEkbhqPbgecjsnOeIrNhciaaZ5hkuYLVjdIJTeyW8l-qusHjsNjLR31JcPf_murlitc_SdSUu_CT49NBEgMb1Nqiiq8SSW5jVLzyQvT4pwhc6GtS7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل تراکتور در هفته هشتم لیگ: حبیب فرعباسی، صالح حردانی، سامان‌فلاح،عارف آقاسی، رستم آشورماتف، حسین گودرزی، امیرمحمد رزاقی نیا، روزبه چشمی، اسماعیل قلی‌زاده، یاسر آسانی، سعید سحرخیزان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/31169" target="_blank">📅 10:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=m_IHD7eyWTfAxE1HOG6Jqq6gGA3onjge58WrkxcpMbRk0ejakAwkyBimB_i5H0GVXRqXfzJL60T43KCYLxhtVL-J1o_0tMKHp4iytWUyp2R7CS1gsSuL_BU5hZLrlsHdnmq0_k69AnKdec2PyXfKou0_NW2gQ7JYpaCJT_nK_lPi-bT6rCZyRqqc62OYdunHSXvkfDcghgNZY_cuMEGG8bMXtriqFB_EiXzOGfMnv-Tg6H0UJBH_NHfY8AbKAglfoldzTdWtK93e3CHME_pwpia1Y-w9WxEvNaakN9-Md5yx4_D5uJPJmhZSU5H2N-qqAGf-Ju9cbCGWcpJkAF51qQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0fe9b0bc7f.mp4?token=m_IHD7eyWTfAxE1HOG6Jqq6gGA3onjge58WrkxcpMbRk0ejakAwkyBimB_i5H0GVXRqXfzJL60T43KCYLxhtVL-J1o_0tMKHp4iytWUyp2R7CS1gsSuL_BU5hZLrlsHdnmq0_k69AnKdec2PyXfKou0_NW2gQ7JYpaCJT_nK_lPi-bT6rCZyRqqc62OYdunHSXvkfDcghgNZY_cuMEGG8bMXtriqFB_EiXzOGfMnv-Tg6H0UJBH_NHfY8AbKAglfoldzTdWtK93e3CHME_pwpia1Y-w9WxEvNaakN9-Md5yx4_D5uJPJmhZSU5H2N-qqAGf-Ju9cbCGWcpJkAF51qQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استایل‌جان‌سینا و همسرایرانی‌اش دراکران «مچ‌ باکس»؛ جان‌سینا و همسرش شهرزاد شریعت‌ زاده در اکران فیلم«مچ‌باکس»محصول اپل تی‌وی درکنار هم ظاهر شدند و توجه رسانه‌ها را به خود جلب کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/31168" target="_blank">📅 09:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=M_cP_v8NG8VBWfudFAxhT7sTbHbI7Lt1GBJicmLtY8xatpMLREwDKCWtFqgETISy8qQBwLd2scLGofGrR-dvnozo3xBnbuGuHi8DWjrOrEko-52T2tjEnDpnQWhM3-OlAk7xWoTOX7zx6wqy_Pu5FnaYqAhMdsJmuuJY3No3bv9fvd1TCvL2MxX75x8b6UR9a0uzk_FJhyRPeVUKBZOqQZOO9rWDLkw-27lGlBKB4k6A0yGzT3bLVm-fVZZWLAuNQ_QtntF9eoGraqnGAXSy_4qhD7lQJWAdnBqj7gWULkE3IkfY4jLHRjXQzaWm2TwmiYvsDQA2DaXQY7NDWzRFZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff9398a1a1.mp4?token=M_cP_v8NG8VBWfudFAxhT7sTbHbI7Lt1GBJicmLtY8xatpMLREwDKCWtFqgETISy8qQBwLd2scLGofGrR-dvnozo3xBnbuGuHi8DWjrOrEko-52T2tjEnDpnQWhM3-OlAk7xWoTOX7zx6wqy_Pu5FnaYqAhMdsJmuuJY3No3bv9fvd1TCvL2MxX75x8b6UR9a0uzk_FJhyRPeVUKBZOqQZOO9rWDLkw-27lGlBKB4k6A0yGzT3bLVm-fVZZWLAuNQ_QtntF9eoGraqnGAXSy_4qhD7lQJWAdnBqj7gWULkE3IkfY4jLHRjXQzaWm2TwmiYvsDQA2DaXQY7NDWzRFZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
شعرخوندن‌بازیکنان تیم ارژانتین تو اتوبوس برای مسی : "لئو تو مثل اونشب تو قطر جاودانه ای. مارو ترک نکن همه میخوان تو بمونی و..."
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/31167" target="_blank">📅 09:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=EwfIjKJ6QS-Ajm6Y1lXdgL9T-8pXYM1s_YO5nBbYTZFz-OhdcIgFrrdq85GfDpmjh-ZFDqkcElcUlDTHuUjoxmVRJUc1pidnZZbLfDjshEeB28Ud2onU5K18-saG_0b85LdAfpXFMmomPddD8rrvVfVOSyDSSlXWvNDZ7vFJ7-GUDnsnJ13ncEDfXxVh5WxDNZ_MHOcLgL8CJheOxHovJn-s5idgEPxx9UyPvD9Yh51CBDDi4bWo1DMhQmCKVzpdLYJVmWxz2tQnxL4ls8L3EhzI_4AgCt-ntBa389tgsWHZ5j_TJGy_Re6RzMuJJb3RUifBd6PKZgxSw3mxJeia_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc91c2c757.mp4?token=EwfIjKJ6QS-Ajm6Y1lXdgL9T-8pXYM1s_YO5nBbYTZFz-OhdcIgFrrdq85GfDpmjh-ZFDqkcElcUlDTHuUjoxmVRJUc1pidnZZbLfDjshEeB28Ud2onU5K18-saG_0b85LdAfpXFMmomPddD8rrvVfVOSyDSSlXWvNDZ7vFJ7-GUDnsnJ13ncEDfXxVh5WxDNZ_MHOcLgL8CJheOxHovJn-s5idgEPxx9UyPvD9Yh51CBDDi4bWo1DMhQmCKVzpdLYJVmWxz2tQnxL4ls8L3EhzI_4AgCt-ntBa389tgsWHZ5j_TJGy_Re6RzMuJJb3RUifBd6PKZgxSw3mxJeia_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های امیرمهدی‌ژوله‌درخصوص وضعیت اقتصادی سخت‌واسفناک‌مردم‌ایران در شرایط فعلی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/31166" target="_blank">📅 00:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31163">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JJQU-y5Z3AvpIWA2Umx-O6-pmJw65c3CVStOwWePIDxIXhkIOaBsdnBZ_EQGMVAFjWxO2TMYnrXb5D9_VhxU5WFZFtQJgxrOX_FSF_fXZ2Fj74-7GUbnW8Dzp331L8D3BTlq8K0aYRoli9Q1J5woGxWQrf0cs9HK8KCPIuZrTkQ5H_AHsvk7UPKxPwkIzuWymvQiNOf5tIWV2K5E_s0OSEmnTltih3PKF-9omeCnVuLtuV0kfzuYXqxNBl9P34i83Ex5bA60aMZOMANq9vAQksZPphcAMU9gON1hV4ixf5D5WaQgCgIcT01aG525zx3QvU6AuCfjwgOraJfPaXxDWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌‌ امروز
؛ بازگشت فوتبال باشگاهی با تقابل حساس استقلال vs تراکتور در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/31163" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31162">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIGFvSCZ7nex9cOkey2XQSXnhbDtBIL0z5hQsz2i0Gkv_6IFNbleMOiuuL5cieWEVfwn40lifN8iF6Y5u68Vln10xrMF17Rrz0kIbiUuwt7S7th_aQVvuxEOhP1aDQi5waycX7bOJLTMb05JBbJyDQVHGmMnlBcwZa3UTCdgNjFwahjQe5-7_QoeDh35uNpxDaktp7NhjBgcL0UpQI8Py5RBCjFLJOrRf65gTf5ut69WUXKA_vqABfq2pZsxxipRUpJbp9qZfeTrJYkMWBtuPw_UlAsxTnZ_ijYzhBaP1bBa_aVsXVkvd4lCf5rwU5Nojc03bn-5-mnK0pXEM1EMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌‌‌امروز
؛ لست دنس مسی با پیراهن تیم آرژانتین با تاثیر روی هر 3 گل در جدال با بنین
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31162" target="_blank">📅 00:24 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31161">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kphY_i_hQxu4e3zfRM0Pv6CF5srem-Vg8dA-iDZdSk46WJ1XrlmtlVcT8ahlA4b5qrRUIXzCcEdS5XhTREqeXrhReCZfPcQvkboeNjvvoAD9Ito_X7mJQXw36p2EDtlzg1xKA1k7mI0518JMtYJnGNruB5_2_LousbF35OZNSKBlnvi0LFsRytdnNGBxyQA-cusb3KOWMyhi62WWnAiqJCcHmf1p7E14FDQSWDd4fdMYJYAiFm1MCTB_RELPoOXEeNfeur1S37QTSkDB_kkeGqsZbSMcGJq0765l-B-opNYHlaXBqHWNbFB2WeMW4Ll7SyU60l4AvmE2TCIe6tAxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/31161" target="_blank">📅 23:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31160">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GvRrVfSnvPVPUrxuAvHZNjUdgLEU4SzFduUM3n6o5G7ttYx9Y6tG_YDjjyrANMGncUKf2mgmQfAhKSDw0lFi3aIKiZx9XlOB81pafJqyKCkLOrXDEKuZioU8FeA2wC-3DJMmQ9BizQP5MeX0aKQ8rtr0oArxul87xcB3egip4c5gv6_2lFpyb4AnW40Z3sz-XN2P47qSDLSmX0VQFISyiEKX58RZGTYHkPIO8CPdlycjXDKBk5S9drs2cpEjIsMArtx2n0vWjfvZeoMVkrr829JaqelijSs-lz9Zc2SxwriR-EWsx2pqG_qn0mfgLqOSpZghcSDhAKV6ev6DM2aJDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ باشگاه استقلال به جمع مشتریان مبین دهقان هافبک‌دفاعی 21 ساله تیم الوحده اضافه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31160" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31159">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=g76yf0oUBFfVuQzd9wicqsk2D41aN_Cfwz5nNFwV7iLho3nykieiw-CFd_-Q1dth520qwLPFQfdjbiaY_hPyvn7Ir8uIzEYbdg8jR3acEBCBIA2VWQuryWESxjeFzTikjCAuZAz0KDMRuzq4QhQGlZ4ghwl9yrSZermIN4eWOe5PUEHSF1Bn1bdPJeGCkJQ_SAYH-xnB8DiiHgs9fi2_zZnSStJMVN9SjBOdPxDAzG50ZL3eXd1_9m3PNEoYrGLT-BNB7khETVtegNcuq7Lslunq5hpPu6IOWIqF1nc4hYoCArKLXn_gzJZmAecnoKOaDdh9dSZRKa38_Yvxbip4SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7faf22359d.mp4?token=g76yf0oUBFfVuQzd9wicqsk2D41aN_Cfwz5nNFwV7iLho3nykieiw-CFd_-Q1dth520qwLPFQfdjbiaY_hPyvn7Ir8uIzEYbdg8jR3acEBCBIA2VWQuryWESxjeFzTikjCAuZAz0KDMRuzq4QhQGlZ4ghwl9yrSZermIN4eWOe5PUEHSF1Bn1bdPJeGCkJQ_SAYH-xnB8DiiHgs9fi2_zZnSStJMVN9SjBOdPxDAzG50ZL3eXd1_9m3PNEoYrGLT-BNB7khETVtegNcuq7Lslunq5hpPu6IOWIqF1nc4hYoCArKLXn_gzJZmAecnoKOaDdh9dSZRKa38_Yvxbip4SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریستیانو رونالدو زیرپست‌لیونل مسی: لئو، سال‌های زیادی برای کشورت جنگیدی و یه میراثی به جا گذاشتی که برای همیشههه موندگار می‌مونه. بابت تمام کارهایی که باتیم‌ملی‌آرژانتین انجام دادی نهایت احترام رو برات قائلم. یه بغل گرم رفیق.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31159" target="_blank">📅 22:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31158">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uObrAUvL_lqk_3rIcREvYpFXG6d9yjhQuC9bIC7bAhI4JSwUb5Q-HRvO3yX51DYQTTYvll9egtTSkPerKITgvE8rhOFI2KSrs3i2IyQOnV4ADZWHz-umcdvLbP_PEq_V27hF6FGfipmevtwzLktdDrTbEB4dcWGPT2IItZ4ewSjUqv7yD3YzQob74K6BgEn5t-6dDSWBV59QMYAMYwl_YE9LBsNuPJg1-R-_xGehCTJMbHIByDvxHKdTgF6l3jMLTpEkZ7RCtCTsq7cnQA71VZDgyqHYQoAQn0AL34EwQaqfJzDAfi_ikAfGozyhSA52mI5WIYeG38CodoefCXkdDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آپدیت رنکینگ جدید فیفا در رده‌بندی تیم‌های ملی مردان
؛ اسپانیا، آرژانتین و فرانسه سه تیم برتر رنکینگ باقی ماندند. پرتغال با ۲ پله صعود از برزیل عبور کرده و به رنک پنج رسید. ژاپن کماکان بهترین تیم‌آسیایی با رنک ۱۷ جهان است. تیم ملی ایران با یک‌پله نزول به رنک ۲۳ ام جهان سقوط کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31158" target="_blank">📅 22:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31157">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2nW8ASDoUylDpMbSNGBV6PnsZ3yNCvRPSp1YMvic9DAmxMbl-kcb49YFHt1KtKR-YpziGJRcs1WP6QSsJ34cad7ra4Ua2g1VnNdSWbcl8hSnjXPe3C5wdqRvAux51fFSZblpxev9WZqNgLiFGjiSTVTeaW2W2kLc2wGzzXYPV_ElPYio_kwrKN11jayvl66nXcefDA5HtTtnA-OOQraiPN9NDQfBCaovb3VWSJCj5VcRAYpBGEwKvVuqpbVP6xHR9GdU3upEeTJb3xx69kYXidCvFTegUTg0tM6QleoeFcDJzRh1H-O78abuzNwZ5xAsFLC0zgqfQq8NhCWlBar7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان: لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/31157" target="_blank">📅 21:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31156">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPXwUMghNT43JTti_wDpj1tuq_FJDCRmDkun5fmL4L7KDSBu6AEzykkoSKMj6mdmEPwMi_-Xx0mcIu0AQXxoX1jZ9oxskNqQKnlhf_Fxt7j3dSEIYViJq8T_GEy3PXduhVBO_7i5lAXzBUOwk0mbIwGPYnTC2yUV78w1C2l90TJRNNn0a5QG7NyA1F4JJcTwwbTjJost0tr2QgUVwSZ_9JR2fplGF70tXT_vKLuUuuyZ1r3abg_m-5mG7S8NsLITZ3WhO0dGiAdxKTbrYqX3FM3JdupJqq1HIA_sBAIw5yD7AVtxY9i6igI5ui3W9eM4dTmr9vqcVENAbbtRykKyCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
محمدرضا زنوزی مالک تراکتور پاداش 500 میلیون تومانی برای بازیکنان این تیم در بازی فردا با تیم استقلال درنظر گرفته است و به اعضای این تیم اعلام‌کرده درصورت‌برد درمسابقه‌فردا به هرکدوم از بازیکنان این تیم 500 میلیون پاداش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31156" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31155">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/etRhLfGc_k_4Wl8hdrab7IxcqUUI6rsi4oxhm0Auv-GGi2TxM8Wt6oiG2pkLFLXqoo0215yOtSG2WwSM_SyI1SzHtou_cCws7bkDN0PVC4rZanvS6KNwLYMcf6ly8WhydGjBCvnabIhhmsv_VWhKOQYOkDmWor4fMot1UL3VGmd-XxikuQMesEqP357P0EdLR0YvqlOSvq-kAQePhX8YxemdLSP1Ks5HR9WuAjW7_pR9vbygpTpVtbQpiJdnPK1WhuKaBG-VR0j3A0vh7cvmr3peZ13T0HWF-gCqp5OxD69YhckeMxTUmnJOIhLAV5hIggg5Dkky9O9VuCcKv9ei2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پیرس‌مورگان:
لئو مسی خیلی‌بازیکن بزرگیه و از خداحافظی اون من ناراحت میشم ولی مارادونا بهترین بازیکن تاریخ فوتبال آرژانتینه و رونالدو از مارادونا بهتره و بهترین بازیکن تاریخ فوتباله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/31155" target="_blank">📅 21:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31154">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">‼️
هوادار تیم‌ملی جمهوری دومینیکن در پایان بازی دیشب‌این‌تیم از ماریانو دیاز خواست‌که بوسش کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31154" target="_blank">📅 20:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31153">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tYaAPmLCjz_Ov-N8UGJK8KFdads1eR-5pvQpb-owo1e4bHQkxc5ErTtEdwTHxEJ8s5gQjrVOOVWIR_70ZtBipr1aSFgqthOFD5_FqZboHIQkyiHuhqitOsF7YlWNynPg5VpChTl8iRihQMEoDa9p68r536CFKQp-QV34VMYxbSVtMKfGOne3LP_Mh_Ysc-an87GCOwx1uI3-m0iRIGqXfvyMGEmzHsxDtQH6a2hDreYF9rvdxvCUod1-aiZmCD9N2L5AAtsuuur3cy9W-ANF3jEMKs-1NeXrbM1mdF6nnuX165AZeb4I1kaz45_tEHPaPV3wG0c-s6ljvjFlF4BokQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌ادعای‌رسانه‌ها
؛ علی دایی و همسرش دیروز برای‌حضورتوهمایش‌یه‌مجموعه خصوصی رفته بودن قم؛ امروز دادستان قم به خاطر حضور بدون حجاب همسر دایی دستور پلمب تالار رو صادر کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/31153" target="_blank">📅 20:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31152">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=KV3quZ8OEbskfHF-HIvP1Q0zuSU8MUXLEJbcG-T_-6KzsCHAk9NBZ1OaeySZC7zP5xxE8iw9Zw8-QoD6CNtKGoQmZldrF5LjKV7DcpHzD5AAHHd5CL_yxvPsuv9geLeRDN7zTh8yVZu8J4bTE3GnfgROpgDjO7474KQawpX2531-bWINfACpNsfWMJA18SQBkJ60Nj20E9BQ4y-Uf7PVRjOTRYtHIyWWPXKHZk_R0Hvg1__JKdz0YO6yWOu6MsylTRmsfJC8RY-hQ0TPgRqPcaTaIrBPs1GsiSdi040lyIagT46Y8y1eXa0VvOdnByL8W4LAq70xhERJIpnQ9eWXGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfe648d4e8.mp4?token=KV3quZ8OEbskfHF-HIvP1Q0zuSU8MUXLEJbcG-T_-6KzsCHAk9NBZ1OaeySZC7zP5xxE8iw9Zw8-QoD6CNtKGoQmZldrF5LjKV7DcpHzD5AAHHd5CL_yxvPsuv9geLeRDN7zTh8yVZu8J4bTE3GnfgROpgDjO7474KQawpX2531-bWINfACpNsfWMJA18SQBkJ60Nj20E9BQ4y-Uf7PVRjOTRYtHIyWWPXKHZk_R0Hvg1__JKdz0YO6yWOu6MsylTRmsfJC8RY-hQ0TPgRqPcaTaIrBPs1GsiSdi040lyIagT46Y8y1eXa0VvOdnByL8W4LAq70xhERJIpnQ9eWXGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید شد؛ با اعلام حمید مطهری سرمربی فولاد؛ رامین رضاییان ستاره این‌تیم 6 هفته دور از میادینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31152" target="_blank">📅 20:10 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31151">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxMp2hmXhZP9Kq1vyjIgUwymqXZZ-m4HS6HIErm1_4-qubQSyWizq4yYsavreyvSIZoK_kHmG_0-GnbfXJPk3MnmmyFaWR0gcznOW95XtVfFtK07TzQ0-QO_kIAyerHnMXukh9tv8lJmlN5Tkx98AlE-Jra_mv8ZUHq8YrNCCsQ2YWR8Emy-kPPGe9NZpVqTp-PxSfXoroyEOkoM8E2LvS2YIB9yhaVREk-eGNA-2VFMWmF9hl8sP1d_bLvjj5_5h_2BcA8WpOvNmcukSagIjbIdx-iAOdP83frd-l5wel3esgiO2Wt8MaaD0Pa1VWw8IQz7w5qqueGv1kND1XcNeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ پدرو ستاره اسپانیایی سابق بارسلونا، چلسی، آ اس رم و لاتزیو در سن 39 سالگی از دنیای فوتبال خداحافظی کرد. پدرو تنها بازیکن تاریخه که تموم جام‌های معتبر مستطیل سبز رو برده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31151" target="_blank">📅 19:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31150">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=kiJ06TU6NQplP7XYzLgiBPC2DdlBkpWGaKSMwvg_zjOpQanhCD8m2UjqGHSrUKZAhis_uOM7wToBLT_ifzs5f7gj9W4pjNYrtdZ-11Qmzd8TMVB8Q73Wqpjk3gvPIEmJCME413BeI9i-Gotc7UaITyee3KH6cw6vdRlMozs2Of36OcGDDps6qPOTAhUYRzRCa6BYaPuJqOAZBHRsIBiMnWB0iaGATObPl2tHHrTxmveQnLi8XB1bVPrh5YUMwZfqUpzhC6UccBkQ3K4elxSxcNg54NcnURZY3e6AIy5OZorQGWoXe5E2AiTwf1Z4B0gnW7hOwCuB7PzyffI-2TPASA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/819a21a6ba.mp4?token=kiJ06TU6NQplP7XYzLgiBPC2DdlBkpWGaKSMwvg_zjOpQanhCD8m2UjqGHSrUKZAhis_uOM7wToBLT_ifzs5f7gj9W4pjNYrtdZ-11Qmzd8TMVB8Q73Wqpjk3gvPIEmJCME413BeI9i-Gotc7UaITyee3KH6cw6vdRlMozs2Of36OcGDDps6qPOTAhUYRzRCa6BYaPuJqOAZBHRsIBiMnWB0iaGATObPl2tHHrTxmveQnLi8XB1bVPrh5YUMwZfqUpzhC6UccBkQ3K4elxSxcNg54NcnURZY3e6AIy5OZorQGWoXe5E2AiTwf1Z4B0gnW7hOwCuB7PzyffI-2TPASA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عصبانیت شدید نادر قاضی پور از سوال مجری صدا و سیما که گفت محمد رضا زنوزی مالک باشگاه تراکتور ثروتش رو از راه راند بازی در آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/31150" target="_blank">📅 19:46 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31148">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWJ8h0blkcK6eDZZB57pYT2wO-6fwqo8jJ2hkbaqaHEE1r5rng0QP9bTlRgF22AWk28auE3Cncdfq8tOdrxC46hXfofulICWr1MwJuqwUeM9gWzikS2mXTxsaBJIxdZQ2nLWKmYetGDUzX5K6-pYtmNowNql4b8zB9vN1eruzws2KGNw_A3kDo91NQ1qOER2SsOrxYdvKBNYxpEzU5XZR9X4jfUSd5W3NRXh4EhUlEIDarfQ7y3PIGOX0pzt0o2RvuLzbfiepmquz982s_2Fuw6oRqScaITUMdpe4VpLDRjs9QNRgzfQRNhExPUVQ8dflaPchhhnf0rFL2avFNoXfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رضاییان از بس گفت تو دوران حرفه‌‌ایم مصدوم نشده ام. این‌بار یجوری مصدوم‌شده که هم کشاله‌اش کش اومده هم از ناحیه خصوصی بدنش آسیب جدی دیده که ممکن تا اواسط آذر دور از میادین باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31148" target="_blank">📅 19:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31147">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOyric9zZqlkhROBe-KpL87HUgpOjE_HtxB6gY5xups55mQ6-L0-WdbR87UQ9uc9NTlCHDYThgdpZexnTt_5AavWPUlqTfXfdDE4XTXyX_t9Xnmo55u0RcBA6uK7JQc1dT9GejEIgGWe2yfJPuWHRPt95JZqh8RjzID1AUzhNAN2mdWBcuW9fbLz_LzwU-hljFJE1jbNZ0Dfnsom331z9InG2FJNum7XwvKCjBFlP0KKgvQMhYPl757-9wpY19UhXWPKPMe7BDmRHda7h3Dao23FHWgpOLDNax56LuP31tQf9usoQNu1_6r1HRmQascxjVDHTNEcmCQScGFjShEhCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بعدِ 3 هفته‌کسالت‌اور و حوصله سربر فیفادی به پایان رسید و از فردا فوتبال باشگاهی شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31147" target="_blank">📅 18:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31146">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=dCGUJbp52Jx3bHAmn7oKLXFCnDFJWvoevJwkrRNPGYvuWiFuOsPdnKUo1Bosk_7_EcfS8vAQor7Mb_iVDnCKn25Qa-N8v1JkieSBy3yIptnd3-RBEusOqiTb8RRwOk-ddOJuWpaBAwAZ6GhdsHUUEgGc5asr_5Z63K26hfco9HB72bL5xYRlto0bbcOFpsHjTguHg8cmxoqe0ZoLjkc_ZuyUAVe2Dfnus0yTx0EXUPZOAZ5Cg4YAUFp0rUEkp05hogl92ajxTlVYRGeP1HhnswG9kOxZPbtAcDg9HbHdgZor-xlSdadt53fhl6K-CssKy0lLF8Y6UwaaIhpbg-3P5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a875cd8726.mp4?token=dCGUJbp52Jx3bHAmn7oKLXFCnDFJWvoevJwkrRNPGYvuWiFuOsPdnKUo1Bosk_7_EcfS8vAQor7Mb_iVDnCKn25Qa-N8v1JkieSBy3yIptnd3-RBEusOqiTb8RRwOk-ddOJuWpaBAwAZ6GhdsHUUEgGc5asr_5Z63K26hfco9HB72bL5xYRlto0bbcOFpsHjTguHg8cmxoqe0ZoLjkc_ZuyUAVe2Dfnus0yTx0EXUPZOAZ5Cg4YAUFp0rUEkp05hogl92ajxTlVYRGeP1HhnswG9kOxZPbtAcDg9HbHdgZor-xlSdadt53fhl6K-CssKy0lLF8Y6UwaaIhpbg-3P5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این هفته هرکسی برنامه داشت امیر قلعه نویی رو تیکه پاره کرد؛ این بار نوبت به تیکه های سنگینن ابوطالبه که اینجوری زنرال رو چپ و راست کرد.
‼️
ویدیو کامل قسمت سوم برنامه ابوطالب رو هم میتونید از طریق پست ریپلای شده مشاهده کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31146" target="_blank">📅 18:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31145">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iWcoad8fbLlbzLR0mbZEOua3VAZIvDCsz0XvS_tFjXXQCa8x2LUiMO7-MSdjB7RB8AG_0_cWMvfZMP7_tcPHUHpsNC48VLQNyYfdzrLnyIW43sToiB6v3iNVQs4PncV29TQJJNqELYbnPXKmZO8A7qbWcWAuRzbzy0WGcO4ilqNhwGrHvzqMIXsIyxUxRfl6ITm91CVsWWjQdPS06PLjBvvG8S_tvkqg9-qPiBBqsWsHOJWmOF1MH7KyLorh6tF0SYMj1bXiu3wYRRpUep_lCs_nSb1U4PLXzDfQ66decoiIng11JUXv1dfitcZCXTFX9XL0TGI_gb_9OniKNhTwMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇫🇷
نمره‌ فوق‌ العاده‌ و‌ خیره‌ کننده مایکل اولیسه ستاره 22ساله‌تیم‌ملی‌فرانسه و باشگاه بایرن مونیخ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/31145" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31144">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=tVaVjHSEtI29w1fsk67OH4ozscyvCqTZY42RxV15vAyiJYKAZWVDrooXSqSMJe9hT36tMLQsf99vKP4jQb5nLAegzbTtJUmLym007B5eSiJP1mx1ZeASu2XU4hY9FHMI2vUV5IcitALmlAevCLMrDv50ULrBngUedZWBWnQIDiQOrsH7x4K3xV_t0ejocBB9EV9zBmw9t8lOgqzDHtz1LFwQOHsWvxTuLb-Z_poP0y1OcDMbAcxW4jedrR6ZOOK2TQREc5P7b86Ny5bHrNS2MFmaa5pKxRS9qxFtfjvBl6_8PrrdYV9SbwygDSh9Z_B866oieO76oV7wnChIxqlE_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fa4ce212.mp4?token=tVaVjHSEtI29w1fsk67OH4ozscyvCqTZY42RxV15vAyiJYKAZWVDrooXSqSMJe9hT36tMLQsf99vKP4jQb5nLAegzbTtJUmLym007B5eSiJP1mx1ZeASu2XU4hY9FHMI2vUV5IcitALmlAevCLMrDv50ULrBngUedZWBWnQIDiQOrsH7x4K3xV_t0ejocBB9EV9zBmw9t8lOgqzDHtz1LFwQOHsWvxTuLb-Z_poP0y1OcDMbAcxW4jedrR6ZOOK2TQREc5P7b86Ny5bHrNS2MFmaa5pKxRS9qxFtfjvBl6_8PrrdYV9SbwygDSh9Z_B866oieO76oV7wnChIxqlE_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
استایل جدید مجری ممنوع التصویر صداوسیما در عروسی؛ ایشون سال 1401 بعد از اون اتفاقات تلخ پاییز از سازمان‌صداوسیما قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31144" target="_blank">📅 17:56 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31143">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=RIk2TzZ-Z2jm-t4gKKOj5Mn6w0vCdjxR9n_QGJIE2SvF5sOSS7lhdnjgLBlibiG6GhNEuFsoGepSivUCsWeelTbEmACngAdLOvI-w9WHtlHNnAKhthn2HXoXf0WtfNDbQR49zSdgJyp8rVS4vilZSmAee8tZr_05uus6DaUcts2j7ypic7XSdJyhwMFqLqTDldEeQRhVNqfSYgLDWVzFxcKge3-M-AZfAQgGx9O5k6dAph4W4JJq5E1_vpsFO8ZgiYMPfH1LHhTikY_aMhF4CAXs21p8FCXeo37qYs5YAcPfv-vwWlybOTNMS824dLw_LtrsRfOnP9JmHZ9N1sDHXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9ec12f29e.mp4?token=RIk2TzZ-Z2jm-t4gKKOj5Mn6w0vCdjxR9n_QGJIE2SvF5sOSS7lhdnjgLBlibiG6GhNEuFsoGepSivUCsWeelTbEmACngAdLOvI-w9WHtlHNnAKhthn2HXoXf0WtfNDbQR49zSdgJyp8rVS4vilZSmAee8tZr_05uus6DaUcts2j7ypic7XSdJyhwMFqLqTDldEeQRhVNqfSYgLDWVzFxcKge3-M-AZfAQgGx9O5k6dAph4W4JJq5E1_vpsFO8ZgiYMPfH1LHhTikY_aMhF4CAXs21p8FCXeo37qYs5YAcPfv-vwWlybOTNMS824dLw_LtrsRfOnP9JmHZ9N1sDHXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های جالب رسول مجیدی مجری شبکه ورزش درباره اسم یکی از پسرهای لیونل مسی که چیرو هست. چیرو به فارسی یعنی کوروش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/31143" target="_blank">📅 17:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31142">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BWvNDfgZKjjEe70ahSpW4wO8MkQaR89QOtuzP3nhJ9RY82ilEAhBsKxm5D6R1w8I84SVW67USatZMYvlo5qaASlgs3zhrJ2xP2P8nrxaqJkfjnznsPyPOx5mOK0L-u0u-GUMsKFeyp4NKf8uqpjKEyZzkvCdHOgU10wF-hxttaBrFWP_fI8NAP1tI2xPLC1SorWz6iEcPGGVNR2Jqx28ChLUW0tzx2B8mRPffJWE01cr3KBmBBUqhlcTPhPEc7N_b7WZXcDO0mjQX2Vk9cxoMmBcCXYanL7Sf7dsQa85-T1iVTmx3dELn0ButmlQ4Os_FsrzH9dFj4DwupZQCFZoRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌عجیب‌دیفنساسنترال: کیلیان‌امباپه تصمیم خودش رو گرفت، اون آخر فصل از رئال جدا میشه و میره لیگ انگلیس؛ امباپه فصل بعد تو لیگ جزیره:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/31142" target="_blank">📅 16:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31141">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=hQxyA07mG1-PUCAeaS62sJvXMO9CfeWE8P6I6f3dPdxuwkake16DRTOi-unonMEf7NZ9s_-d2HrhQQctPoWhSlzNO8eRBcG9-PiyzExdFXjfMDHCyUnxoY8CXtsj9SxVyWJY2aze6OtC5MrgCKnp0jFi2VW0RmgtnRIht8c1MlxVw43FrhnZKui2uujVjz2weYJjoph0M_VVyn7qNhtGNVfxYWj5pWb7HjOQjXB8YIKeWgq5lGKBLf3FqGhjLHamdS1Fnvz1uyF7P0Q9x1Qa32VcPX9OWnvho47fGRlJEeC06PZ8XM57O70e6E3rkUdH3UpWVkPoBZY5GZZIiw0ULw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae97c5b61b.mp4?token=hQxyA07mG1-PUCAeaS62sJvXMO9CfeWE8P6I6f3dPdxuwkake16DRTOi-unonMEf7NZ9s_-d2HrhQQctPoWhSlzNO8eRBcG9-PiyzExdFXjfMDHCyUnxoY8CXtsj9SxVyWJY2aze6OtC5MrgCKnp0jFi2VW0RmgtnRIht8c1MlxVw43FrhnZKui2uujVjz2weYJjoph0M_VVyn7qNhtGNVfxYWj5pWb7HjOQjXB8YIKeWgq5lGKBLf3FqGhjLHamdS1Fnvz1uyF7P0Q9x1Qa32VcPX9OWnvho47fGRlJEeC06PZ8XM57O70e6E3rkUdH3UpWVkPoBZY5GZZIiw0ULw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناراحتی شدید علی آقا دایی اسطوره مردم ایران از خدافظی لیونل مسی آرژانتینی از مسابقات ملی‌.
🟠
@Persiana_Arena</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/31141" target="_blank">📅 16:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31140">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3fghlMOfi3GGj1NP_UkovSK3lPqsdqJRadbR5Qk1z8pWkzebJlPIbvBDmGR2jwYOBhq-kjMj6qH98HgBe3Zy5H-m1uqLveZH0auIALHLUTjBCAtNwK7kpXAAE1agUDQzSSztzXPzPlHEUqIweg_jLwL_XfZstHK_FiY4UDo31Bf4Ks7vvtXJjMP9BeHde95yrm7xw8wAFY1zeuCLZepcDLofzApF9ZS7WAzOxsng-PGf6VBKZc-WM4SJrtvz_hxAHbyOkO8KFDYndDWmwQlmPncGVoUM0D3TF11xNg_PL0uik2-B63uBwONDuCng_fAYArxc96HOtltDZG-TsMN2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه آرسنال دقایقی پیش با انتشار این ویدیو خبر از تمدید قرارداد میکل آرتتا تا سال 2030 داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/31140" target="_blank">📅 15:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31139">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fnYHE6YQeWtBT4WVlz-NmWfsONn46MtFH6PYbp32KdTnQyDwxmYZxm0aKP1y2VsBebk_UdOXdU6sK59a7rtSe08wl7BsvmxJ_hja5hdGMBxZP7RDwe0kEpJi-VgRAUK5KkA-Mgio8TpgSdtm81gXMyjRw_D89hAZX1q_JMQPKPdZTz6QbPr21WGdD_qjhLsrpwbVR4PyQLLJqsl2S-2buojimfI-Tj-cK3iJhlI_C2dSKwTzUm8l41i-63U_8w7whpSjpBbKAPFAlKKlm-dauXerO2fwxkfCwZDK9SDtGpFw8SaWC9MYFbIcU2wWX5z73rGHqII_u_PMoZXKgG6uvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج10دیداراخیر استقلال و تراکتور در تمامی مسابقات: 4 برد استقلال، 2 تساوی، 4 برد تراکتور!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/31139" target="_blank">📅 15:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=pkwrKL6pbpwOItqohs6BL9yAehu3az_Y5lYYPbRS-udiqWk3JlGnN_VTHQ_1pm_ylwG0mr3nVKihuoAGZW74jU4vScwYm69DbEevUVttV7DjXGtorDY9gki0S-Xpzpyb-3FsQGDn7kpqR-gempKhGuxKFdycRlPvgzaKsQeC3YPrLsvXf5h7crhi-947-BKp3ss-E6W3MX_H4OPKB3EO31EtLoLHQx80v7khRbA5OM3oMf54w4QbbIrBebjnuEvgP4IKFw8bOdLnvhYzrRu3k72A-HShvR0IoazmJup_0Fzo_iSkL_-4cZ00Oi8ivckSO85_pV6sUPsoTtIlnRsZtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b5a302929.mp4?token=pkwrKL6pbpwOItqohs6BL9yAehu3az_Y5lYYPbRS-udiqWk3JlGnN_VTHQ_1pm_ylwG0mr3nVKihuoAGZW74jU4vScwYm69DbEevUVttV7DjXGtorDY9gki0S-Xpzpyb-3FsQGDn7kpqR-gempKhGuxKFdycRlPvgzaKsQeC3YPrLsvXf5h7crhi-947-BKp3ss-E6W3MX_H4OPKB3EO31EtLoLHQx80v7khRbA5OM3oMf54w4QbbIrBebjnuEvgP4IKFw8bOdLnvhYzrRu3k72A-HShvR0IoazmJup_0Fzo_iSkL_-4cZ00Oi8ivckSO85_pV6sUPsoTtIlnRsZtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
میکل آرتتا برای تمدید قراردادش تاسال 2030 با سران باشگاه آرسنال به‌توافق کامل رسید و بزودی با حضور در باشگاه قراردادش رو تمدید میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/31138" target="_blank">📅 14:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EXfhh-xXfnvlieZF9V5qLtosmUdtcuSLjADGRmU8UGojAMosDZDausMdl4jyUEWc394GbKqK01oTeBLtIoIntirTtUgx7ye4_RQ6xWexadbs5we25cte15HQkTmQ8nqzQDokmbR-V7QHV1a6Bvw331iHktubI7YgZOUMhskcW_rZOk1Vym-s7u3yst6jzyVm0NLEdjjBgG6Je5iLFXXgU1QgiUYV82MOzqirqZrnaTmQw-JqofLxh5-reNPXqekDFldgC6_WuZ9QuR7t6kLOcpYpT_4qbzUa0tnyFeLjdhHztbQMjlvptccmklXUTqTGpneXgFDUQP3EGZSEBxQX3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/31137" target="_blank">📅 14:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uHos952xGP-4LeI0JCqQ4XC6wAcBQwjm2eVWbz9thvlyCqBnOpU5CW6FQ_a68yEUDXMRnzzckbjTO46Po19Sr-mFerW5lt9liTil17mODTpkHopmR2RQ-O0SHeXGSVBtxYFrV0tjwqO3I_PCCGC1yXF-vUd3Pq8u75n2VCKScDNbn_hpaOe88LUfG8tvnwfiOoAdo2cYa8RKkNVaz2ikiL8IhjG2IBVsu0XiDIbxV9K0yPPQWIXRPCInVgdidEexSKWP06Qy43GpzL0E-_YwkfvxbClP2oYpvYXFxw5O5njhDytFxLRd0jEuafzrVZTnnSlVH3Uc8YFTVLpojv1tuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جالبه‌بدونید؛ پدرو همچنان‌تنهابازیکن تاریخه که لیگ قهرمانان اروپا، لیگ اروپا، سوپرجام اروپا، جام باشگاه‌های جهان، یورو و جام جهانی را فتح کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/31136" target="_blank">📅 14:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31135">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=PHF1vgpTZMH4Lhez_ym9lH176DluCWM6PtByZvwoul2OkrIBb4S1UuAc8WLdOhbHYsTX9ApQsUJfIndfLd-g7YxKRb8mIWvld05xGyeFCGdCNVicERojEXgEnHRoQvMlv9fwnoxEMpKSxSmtucR7kBcIBVRAUw6eJjFIFi2jT4vxW1ojkVyKzdiXJW-GXXZ71U64f1O4vOs-e7K03IA1jqvAmUGX9_sTh6lF2mWuHIne9sbnPs6uCZjlbfMdPp9zI97bulzZ8qi8M-JClviZA-Xz6CZQW3lvdrgDLhC46BynurlFYBgyGXX2vwnJ6Teiml9KeCQAcvqhfoMcLEpq_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d783b6322.mp4?token=PHF1vgpTZMH4Lhez_ym9lH176DluCWM6PtByZvwoul2OkrIBb4S1UuAc8WLdOhbHYsTX9ApQsUJfIndfLd-g7YxKRb8mIWvld05xGyeFCGdCNVicERojEXgEnHRoQvMlv9fwnoxEMpKSxSmtucR7kBcIBVRAUw6eJjFIFi2jT4vxW1ojkVyKzdiXJW-GXXZ71U64f1O4vOs-e7K03IA1jqvAmUGX9_sTh6lF2mWuHIne9sbnPs6uCZjlbfMdPp9zI97bulzZ8qi8M-JClviZA-Xz6CZQW3lvdrgDLhC46BynurlFYBgyGXX2vwnJ6Teiml9KeCQAcvqhfoMcLEpq_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
مقایسه‌ارزش‌بازیکنان دوتیم تراکتور
🆚
استقلال بمناسبت بازی حساس فرداشب دو تیم در لیگ برتر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/31135" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31134">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=hQVKICbVOoJhILXSvNerkmfdHZPpUrhz2u6V3bIM1NSlC0YrUqOvMhqrXxHTdNwPsrZm34q5bnA5QW5djcuCrQ6mqZtQVH4i3H6-CvgXloxoAQvtTvD9P1HCRwB40cu4VsBj3ayfYyzaRNrLyPGJ0b7WE8fxbR1VH57qE0cZF7xE1mshoMdx6cgdeSpQ26qEOVR4Ko1r2RM4WhMLwkG3aS1mvOwaxWqrmOhBCQPw-fRrI4VhnhnNrnMkpYGqWIayrVfWY4C_Ky6udu1q_Hm8EXOZTJLrCzcvu2xhY1Yoi6F5_Zb4ggCDLPqT9hHEnmyR5xBYbNeLPBwusLVludusK2F4nOHtuTLr8GjnBMKU3rx2cH2SYmxCjrOrCgeHjthuKVSI5bh5eJuYbO-HjovIHftearQEWePwqTdlpMjgSz-wj32mjttAGjA0m4P2miV5iaHk1nSbyZesJ1yfNKIOlWR8qBaxfnS4SIhqbsaStNsvPLMRg_ipE8phItN1aMjYd17Egn-813zG6MgUePKwFlJZhbo7Bd1-5efkZoyPrL5KRUN3E6XvrT8e12tj7RP_8ZJ8DwlOcJsvs_v2ROOpIXThnidGvZYdu7rjcj-2yNWdeVS_lnJpE3HgAYEXIXMAmoohOhR0tBfIaWrh34BZgNqQbCr5P-e0jWCVKYvSVvM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3866613d1.mp4?token=hQVKICbVOoJhILXSvNerkmfdHZPpUrhz2u6V3bIM1NSlC0YrUqOvMhqrXxHTdNwPsrZm34q5bnA5QW5djcuCrQ6mqZtQVH4i3H6-CvgXloxoAQvtTvD9P1HCRwB40cu4VsBj3ayfYyzaRNrLyPGJ0b7WE8fxbR1VH57qE0cZF7xE1mshoMdx6cgdeSpQ26qEOVR4Ko1r2RM4WhMLwkG3aS1mvOwaxWqrmOhBCQPw-fRrI4VhnhnNrnMkpYGqWIayrVfWY4C_Ky6udu1q_Hm8EXOZTJLrCzcvu2xhY1Yoi6F5_Zb4ggCDLPqT9hHEnmyR5xBYbNeLPBwusLVludusK2F4nOHtuTLr8GjnBMKU3rx2cH2SYmxCjrOrCgeHjthuKVSI5bh5eJuYbO-HjovIHftearQEWePwqTdlpMjgSz-wj32mjttAGjA0m4P2miV5iaHk1nSbyZesJ1yfNKIOlWR8qBaxfnS4SIhqbsaStNsvPLMRg_ipE8phItN1aMjYd17Egn-813zG6MgUePKwFlJZhbo7Bd1-5efkZoyPrL5KRUN3E6XvrT8e12tj7RP_8ZJ8DwlOcJsvs_v2ROOpIXThnidGvZYdu7rjcj-2yNWdeVS_lnJpE3HgAYEXIXMAmoohOhR0tBfIaWrh34BZgNqQbCr5P-e0jWCVKYvSVvM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم از روزیکه جواد خیابانی وسط گزارش مسابقات یورو 2022 ول کرد رفت. عالی بود ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/31134" target="_blank">📅 14:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tSEuD_OHmx1qQKt57o5SatjX1LNxKlpOShXEz_FjFRMcygHMRANe3ye9Gfmxa65Uu6iaVcZOOfjY6xZTGNcKMGp1SwyWVSMOTAy4n1smfGgmNzmWQ9aDnTba6simhRbTmoxw36ys64_p0sGORsccVxyIalwcUrVRczby76sh7oxn2UaIe7sdIRFK0FWGaT8DNwZ4Y-Wf4iK8FHUuQ2H7YgePNGoupHm6b6TuY0rRlQB77TghjD10nYK27BtZhgjhojFUF6E-207ALDbA8HmRNO55t4Gbyuhw_KIgO2PB3DjrXtMETAbdOMD15sP64TpEr3GTY3x2P3Toj8eKNOCVRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
فرانچسکو توتی درباره‌ افسردگیش:
بعدِ اینکه فوتبال کنار گذاشتم و پدرم رو بدلیل کرونا از دست دادم، همسرم‌کنارم نبود. بااینکه بهش اعتماد داشتم همه به من‌میگفتند همسرت‌داره بهت خیانت میکنه.
‼️
من تلفنش روچک‌کردم تاببینم راست میگن یانه، کاری که قبلا هیچوقت انجام‌نداده بودم. بعد از چک کردن تلفنش ديگه نتونستم بخوابم وانمود کردم که هیچ مشکلی نیست، اما دیگه اون آدم قبلی نبودم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/31132" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sY-OKPoTVHeCP45HwiwXaxqXHVirMR46sfCFPydDOfEzEUT8GrvqFTxC4XDZhm7ruYvzK57B4qc2ajy5uHICAosyS1E_ioROC4T-zRu2W5D_bDtgjWHqVwNPUzCikRlg9UU8an9uC0QB4WyCyKlPuZizpQQEYlpbucawewxVOMnicFnjcgow1PjDNtswtuBtxltmL8lDgFG36m1oaETh-7BtQyhePkgpBdsPDCWo1bzPJ8JXMo5_eYYDmDujAFP-Pnf7vD35BtWHSszGXKGDOo4j5FAPnFlCI63-Hvx2cxUWOfVxq-pjK0MqBT_-4YOuLPm0w8KEeMFrTSgQxqRKOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
ویدیویی زیبا از تموم جام‌های لیونل مسی با پیراهن تیم ملی آرژانتین که از 2021 شروع شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/31131" target="_blank">📅 13:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=YmYhKU96DDcqRhjuYEMaPLg28882ePQxbiLdWJeOh7ZOq4NqjeiL4HWUGMT-izTTfC5lf-agvtSl5vG6T4oK_V3VX8u3KtMjFJ_rrZs8V0fUAjoCVgzR4KjFaSKgGIKaVcsCEmesJZnaqKxyHEsejqNyDZmzdskLLAWe6cJjOsn8VSDa1WYnQfwCNUvdYXZIU6Pa16Hv8CReHeehxQ7WqeLlhtLNWkY9-jJoinUjqr0CT_tzIGca3uha-3yUF6nPFfN-BROf9VHrC0a6XydD3XcnseHkMcDLFmoCUr2316sE6MeF_OKtvmH8thbuhGmOtiKyCK8qC1WCMf0ZjlSnww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f3ceb15f26.mp4?token=YmYhKU96DDcqRhjuYEMaPLg28882ePQxbiLdWJeOh7ZOq4NqjeiL4HWUGMT-izTTfC5lf-agvtSl5vG6T4oK_V3VX8u3KtMjFJ_rrZs8V0fUAjoCVgzR4KjFaSKgGIKaVcsCEmesJZnaqKxyHEsejqNyDZmzdskLLAWe6cJjOsn8VSDa1WYnQfwCNUvdYXZIU6Pa16Hv8CReHeehxQ7WqeLlhtLNWkY9-jJoinUjqr0CT_tzIGca3uha-3yUF6nPFfN-BROf9VHrC0a6XydD3XcnseHkMcDLFmoCUr2316sE6MeF_OKtvmH8thbuhGmOtiKyCK8qC1WCMf0ZjlSnww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
دو ویدیو از علیرضا بیرانوند دروازه‌بان تیم تراکتور در پادگان حین خدمت سربازی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/31129" target="_blank">📅 12:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4O2T-Re1_3JmbD_mi8-tQypOnHpceLbYAij4HS0OQY2bPv-6A-TQIofENi4wFaNjKtomYokh3uLxQYelr5WOdxMavhkxmXPJ2YweNdEzVXCr078_kXYot-Q8BJBahwDWxq7Tc2ijPni6OqpkRLSZXPGdzSiBha1Jdqm35vDGPgeziqo5S-ek0OkYgy5ETy5uJQakArdFIlaMUo3yZm0SaaPjf3u-9HXafmlWPBq4ukv89LcLnl7uNNZ1WHbdMaHpIshIinJSfhm5uddsV8-D5ceRDXx58NKuTOFUERyISa_E28hf8psphuDl0TudvGmR6uZipiYrUpFllS9NTj8nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
👤
#تکمیلی؛ رامین رضاییان که‌دربازی با روسیه از ناحیه خصوصی دچار مصدومیت شدید شد حدود یک‌ماه دور از میادینه و احتمالا دیدارمهم مقابل تیم پرسپولیس درهفته دهم لیگ رو از دست میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/31128" target="_blank">📅 12:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jRXtBd4hP7kobvqDPFYCc-bqvubv3GT78PBu6Xwhm9Uekw1BOeaQoeuIbvn60yQEwyIFXotMLWO8QIFsKz2tRl1isD8-oMtgGYLj3jVJStsEVKa_1wU6CtalyvN68PmHO_5mR0xAyALqWFM0qNKLwATIammzm6ejjk8gaRU5-y_X4qzK9bv9se2Cj1kaEceTHw61oMwenIpw5NjgCzYI6LI_IGdJCESMwh1m0jhGAkZZJAMRcEqOVT5ffElXc2Uzs5dbE-EfUUnZVJZ75VKwi681VW-mrELbDzGchZVvJkEtQ8y9Qfx8GzudVQe1TF7sI--uZWR96egVBZKT0YqzVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
#تکمیلی؛خبرنگارباشگاه النصر امارات: کادرفنی‌النصر از عملکرد مهدی قایدی رضایت نداره و تصمیم‌نهایی‌اش رابرای قراردادن‌ستاره 27 ساله‌ خود در لیست‌ فروش این تیم در پنجره ژانویه گرفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/31127" target="_blank">📅 11:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-31125">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=jNV3LbBi6KqkdeSFJ1p6f28EjekTGAGxfvTKtzE-_BOlAwmarVpX85P_-WZWPZPulwr6d5PZWPTRmGjhzxoYKa75qJnVaQVLNqFA_8j1rh411ScufweSTpAm0O3QbWWa6DD4INoXkTN-UEFALGvfURSy7BDQmzxEFs8NdQUer0bQn6hVunkuef5VHKBvsBK0tEoEGsTqgAmZiGf7F_UGxtoWXmTZaXjDtmTaG7K7ES_g49GF4WSXM_KEnebj4PDJPKd4_3Ox0P6B5nDW6HoyxaSjxElUeVGsKzwlwWJWu-22_KTDuHsk4EZKyOP_jOuyE5PhUi5YZHznGO7Zo17sPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce783c6799.mp4?token=jNV3LbBi6KqkdeSFJ1p6f28EjekTGAGxfvTKtzE-_BOlAwmarVpX85P_-WZWPZPulwr6d5PZWPTRmGjhzxoYKa75qJnVaQVLNqFA_8j1rh411ScufweSTpAm0O3QbWWa6DD4INoXkTN-UEFALGvfURSy7BDQmzxEFs8NdQUer0bQn6hVunkuef5VHKBvsBK0tEoEGsTqgAmZiGf7F_UGxtoWXmTZaXjDtmTaG7K7ES_g49GF4WSXM_KEnebj4PDJPKd4_3Ox0P6B5nDW6HoyxaSjxElUeVGsKzwlwWJWu-22_KTDuHsk4EZKyOP_jOuyE5PhUi5YZHznGO7Zo17sPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تشویق و خنده‌های آنتونلا همسر لئو مسی درشب‌خدافظی لیونل مسی با پیراهن آرژانتین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/31125" target="_blank">📅 10:41 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
