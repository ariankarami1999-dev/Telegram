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
<img src="https://cdn4.telesco.pe/file/GxKT-zoumib3Wr2CavFRaVYZP5qZ4OSY3m1ul5MDLjkxXiQy47raeffE4r-ndc0Lzs6Ha5mf2xxNgo_imNyhuy0gVjoO39Vlb-QldyFxGw0RsvCYb794JDOlWddKmPrpkIXx2w18YIv4uhIN2AJ5ugCxbOLPnIKaBVfNT7Nb-Jz6u0ldLz0MLdXP5sJdZhii5XJ7pO5NtNR_O3slYUngReiFOwLR3CWp8JsRgXEkPEQKajdlUBruCRxM2U4ZTOk2C0T-3yGdRDJAvHKDBgIiMXBs5jcYGUCNlYqnmyX503mo_ozQR07v10cIA8zU1KN7i1q5PungZ0tAw5bnv-sPLA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 211K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 20:37:23</div>
<hr>

<div class="tg-post" id="msg-22143">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">⚽️
معرفی تیم های حاضر در جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 520 · <a href="https://t.me/persiana_Soccer/22143" target="_blank">📅 20:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22142">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evrGIhgOP7NiERScBMSeJEUuEbb-8bAwB0KMVHYhtyFAiJUbVvLFiosecGwjseJWXbAM0QABGF8Pvrtvl0AE31ljH2GLPwWQ8E8eyqn-pCXlJMeXJtf5_vhsVpBFz0OsNoWYdt8hpujDpd4_pOKLMtVuqWnuWKCjTVhwD_swRogAXo58deXhrV3Tm1EXbTDJEl1A6Nen-8mDTnpczva3KDDykm_ysgu3QcVpYSUpEevJKQg-WE2Pv-6EPs3qQ6tbz26XcntySNQTL8VhEN50rtXhToqkQyHnTdLkMGY_vsF9nkYV6ehmMWv9BAzIUen_IcTGaUr1Uz3Hj64_UwPBDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
مانوئل نویر، گلر ۴۰ سالۀ تیم بایرن‌ مونیخ قرار دادش را برای یک فصل دیگر با این تیم تمدید کرد.
📊
آمار:
✅
۵۹۷ بازی برای بایرن
✅
۱۳ قهرمانی بوندس‌لیگا
✅
۵ قهرمانی جام حذفی
✅
دو قهرمانی لیگ قهرمانان
✅
دو قهرمانی جام جهانی باشگاه‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/persiana_Soccer/22142" target="_blank">📅 20:08 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqP8iIQnxTTOT25mIf5zQacLD8XvYu8HuwF-cHeN8IK0sPAk2qVGPV5ncoDUQvBTkqjWYq5iIKRx4rUDbgqMo6IREGOUMh8krVtC757WwGTRNPO-VJs19uPYqoY-BcH2UqEv3QImFp0-M_fIKqqADJP9qlWTVyeGCLlGx9vOMDEiPaT6GnXcmB1eetNX0Fy9fre0U0fabceR8cXgXBCt8qDE6YN887tuLTDrlA8RcVizl8kSiH9ELXpLmGvB3plS30SCUOXz5vTSsz0ICBQFKApXGZidcVFPti9WO3k1dEF8EvIaHSrNMnzh7wO0eCgmrBeagOsLAXI25xpsg-RPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqgN5LOZD2Hvdzefze-K98Xw7NAEgWEMQ8VVk2KWOpkFuhGEZml1u6tmF61Hmt1LEu1FOtJEWO08BhbFpfqJKQ9mxtx0_dwQAcHyDqJwl2VHXzpysjdGqCiquvsOwbsv3z892Iy5No64pQjH1OG6YEDyBS727R6beTKja3cYzFDIydfbTYjG7n9niWEw2jKpi37qWIgq0_EAqL5zSN_3XijXXje6F2bTALu9l7tXQ2-w_UQSpwa6El04Buif_rFz_YTwmeIbsY3vR_WmPyJqXOhQeKnwURBSBZoEs-ng_0NWeylOZivw9m_njhCl8_h_r8c2mCb813jCB7IEWSV9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗘𝗣𝗢𝗦 𝗜𝗗</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZkgQzIh6HZctZyzEa27Vwm-i0KBreWyJQcDqQy6k4BkULvVv_u7nKbQ49CHmlpxR5WjR-aor_smeztIQqL4goc7F4GemmvbG8nuTNqU5tl0iNwfYAo3gsDTciJvtLm4FDmCIVFpKxNOWtv4vJmyyyMI3CenS9zcLaVNxETkbXh5o0k02J0PLwU-cLyDvsZ-ZXlJXDyP1kJNyyTOV4ixKrgspwhFtkbGz34iekg88T_x7FxaXaxO5eBmtIMlv59SnzDly3zFNtbK3CcLd8i6qjyz2H-oUiUiaWn9c5CbKVCyWQuY4DvXgcvQ73hxhMvHz9OO5MytrQSvOn5D-xnZYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
💰
شارژ وان ایکس با تتر ترون معمولاً دردسرهای خودش رو داره؛ کارمزد شبکه، نوسان قیمت تتر، معطلی تأیید تراکنش و مراحل اضافه.
💸
من ایجنت رسمی وان ایکس هستم و با پرداخت ریالی(کارت به کارت)، شارژ و برداشت شما سریع‌تر، ساده‌تر و قابل پیگیری‌تر انجام میشه.
🤝
⭕️
برای تاییدی، شما اول مبلغ ۵ هزار تومان رایگان شارژ میشوید، تا اعتماد شما جلب شود
⭕️
✅
بدون نیاز به خرید تتر
✅
بدون درگیری با کارمزد شبکه ترون
✅
شارژ سریع و لحظه‌ای
✅
برداشت ریالی منظم و قابل پیگیری
✅
پرداخت مستقیم به‌صورت کارت‌به‌کارت
✅
پشتیبانی ۲۴ ساعته
🔈
آیدی چنل:
✈️
@EPOS_ID
💸
آیدی ادمین‌ها:
☑️
@Agent_ir1
☑️
@Agent_irBet
⏺
⏭</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/persiana_Soccer/22139" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7rOnYaNqSM3-x-3e4Mi-FHsiG0ewKdbh7iHfgsbP7nDYtG2RhiSWXk1qi2QOj95ItR1aog1403wlag_eMNJoNeXdoYyEbl7yw2_qP_PNiWtp1GnGQFcLMA_xDybJ0GYs81t2a4LUrwDgpVbRvXZQJymnQFDzxdaRVKdUU01BHqtu5QXg3nziR9sET82hb1ikAkMJiPNcQJ5wv6trZZIsfV_D8obE5qVVwodvzKCW9nXCy9qqPt6CugdCUn-OG6C6n_p4apj6MawAxit7QmX4Xx6qsRFsAsY25lIi0qfnYmP7SpBP0jqrwEsdepn4StGSpw7jkTzTK3MH7chi6NuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.79K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2OFps6B_wLFSCKY_EuviK-9fzFwjRXwTAkVY7xG8XA841s33zJDj6dfUuu13CRQ8WtS4ZfDWzYcpAbcZdbe3G9ONxJlkt5Uqq0dQiXKvC2dd-W8DTrXEgqyKTmeJEE8vLvguSCZPCtljyXW9yiz4a_q7CzHZWJaqW5IkFVHHCtYiiSETGo8z1cQVk2k643fKMeT6oV9G8E6OpWaRxWq9iBTh1NBXbIjW9H8ivuS53EZxtlvkb1EayiY4MtfOJgCV8V2962helMatPHUkmsLSe5DQgAr4YQqHD_wbHu7Qp0W3IxsQk00dzhG7eAbt90Rkbut0jefhhh2zv70EdC93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMKLV5drrJ7CbxX41gc-SYdLjGiY-UQlaPghJA8QtVTTYBkywbPVT2dn0HQMP7hyLK5IqTRpn9CtDoIICa4kDZB3awe_pkFzSYSLyb8_3G_u2gNHEOhg21FZrrt7QuK_UP_2vpDOPq2UlC7tV7GO4nxXPmxuGO2j8-tDbxAV0X8EvDu6Y-IftNaXqKodxukeQdha3Sw1sTSiloOTLmtDtljEQdiUtn5uxtnCd1wb7w1jGrYhW_JmgkMKDOBzG_NnG3q_Hn0XjjQuWfAlZq-SgxHRuc8qfypinxw6wa5BLhSCGQS2bYUN8gLQrahyDrqqcsa_RNSSCSpiu_B4JNUmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzjIFUHcTm7S4qWa9hLQF5QSqLmNCTCkfXQ_8jvs2dOTyZAkPg5J2FIH2I57IQOpgPQspD2mID-_HdD-lP3E79m-8wvJfwkMPWaUieAor-86YfGMR6uxjlFF2PEh7D165efizbeEW0eus9kgs0xxWbAadmADXGp2EhzzOGKO61bJLdNWREMwjr0VqWpUCZIQBezXk2ZqX6RUGd-IOl48WDNcK8lkAwI_cvUZyb-FlhqX43P3rfipWLProsLB06lJ6z9pUhJB-YQCFgQPq0vhSzr0seL95SH3r20fdbIlwgaG11qqWNP7xMOZoXPhe-teFc9hzSK-2prKOsTxZ8DsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22134">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu9kKRmdyVXXLkD6gR8qSiLZDB7VI6H3UbAR0r1DMQnna_MXh3hx0Db1FijcVxaY-y7PJ8Zd-JdpkZZgun1gbzU5z3sfaiUzrpSAnP3nv6CVlaj9rbrEKWtdzTyJxaQIJsAOYfvpeXS--yZFWgyqp7rwVLql3SQC64gfUmqqeKuNaIPhLYf4Z6NOXsSxoXnpFYm2Z9C__F7y-QoECNjrLwVK0elPC-f_Tvx6nzHF2wBOoOCDVKGrv6xJg9NZfu67q9aSz5UHxNo54-geqcjrMoC-2G_wZKzXFT0xlAo_EoRG5wYo1YGCCITAwSGuXT17ik0Xn-vRCS7PGo_v1xC3Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ورودی کانال VIP بتمونو رایگان کردم
؛
خواستم یحالی بهتون بدم هر کی جوین شه تا ابد میمونه
💯
https://t.me/+--L2Hz5HpiY1YWZk
💎
#تبلیغ‌نیست
💎
👀
کانال وی ای پی رایگان برای همه
👀</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/persiana_Soccer/22134" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce7s4ke_tTYnreXVKu_g7XaWnUtNn9GLe2UUZXhQxW1oM2BnwQ_0CFFk_IcpNAEgyfKLhU7PGCFsqfhvDk7qbCyvpwUs0ow6jQ47idiqEhNAWSioAhf4WW6HCW_kHTlixCjJeulAW2Jc38Mof32Ku8lirGrGXqOeo2iVldS0Ax3pPjolyhk-q7hvbiyHEA5-MdE5xZEa-_Fd6XZbkiBZ1ZGn9IhBWXoGzBGLlg0_RpbixdZoXTx1li5R9HCDmw7rjkhHvvuz8ibyWxeO79tRlWdSC-rQzvouUgfDNy1ZlS2lSn2pjHupCA2HsjFJ6pXRHFQ0ddho6SSJpy7OZjzp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jlX6cApVaGAJ3eIfdIar7Qa3z5hbBMZ4rwPfvCHQ8boNw6z6LmaCopdFD8XVO0MWazwHv3p9cF8sll5iYsvCtjcPnyhS7gCjX6ozgtYn4Gu7mMt6b58V27boOQ5F976TDRmKJziV4fWOLrFtS7PuzrDim5_bDYSME-Pp8LUAZhs2LHRrPazN7Viq2wjWzd7PMNaXHcTuRXibd2NUmfDDOEs_TvsOvbH_OgsBdqelZJB27G_idgrPYh052VidhGzVFDD1sCpRrIGK7nqljtKYKpA-STsZ6ZJZIZP4m8vVR7OjQaJx4D_DR938aw61UdiAWrO_BYV4dRaDnuiLIGjCVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=jlX6cApVaGAJ3eIfdIar7Qa3z5hbBMZ4rwPfvCHQ8boNw6z6LmaCopdFD8XVO0MWazwHv3p9cF8sll5iYsvCtjcPnyhS7gCjX6ozgtYn4Gu7mMt6b58V27boOQ5F976TDRmKJziV4fWOLrFtS7PuzrDim5_bDYSME-Pp8LUAZhs2LHRrPazN7Viq2wjWzd7PMNaXHcTuRXibd2NUmfDDOEs_TvsOvbH_OgsBdqelZJB27G_idgrPYh052VidhGzVFDD1sCpRrIGK7nqljtKYKpA-STsZ6ZJZIZP4m8vVR7OjQaJx4D_DR938aw61UdiAWrO_BYV4dRaDnuiLIGjCVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🚨
⭕️
رفقا با علیرضا صحبت کردم هر گیگ کافینگ رو ۲۱۰ میده
با لینک ساب بدون ضریب
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk70_6mFQl9Ox_2mb6XWNNY5xHA_MIyyBKqh321oIBID4uEjyOIEA2OcPXj943ami30L7j7cehiTUsIgvlLobU6gdIzCljRYPXu7nlcV4SWTyj9s7okliXkM0y95t1ltNMBckuLmOFHhN1KQbiZWv-AA-x85BFpeyXt90ftBhk-qycfGzoyt3v803MtsUWUagIXEurlgIrNEroQQGsZPgii_0TdNHJLr5EOPlL1CsAdS7UKkU7FB6Csz3Bgbq8s9U45-j8ESrd5AzwRPnbX3yHm1r0H2t2sJCjurHPW8xEihxQX0-53Lqb8Ul8wFhxDlf_h3lvqjZn8iXaT5PMQ2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFpvvFy0UB_WwzA4rQNEWdhh8gtmWStcjgzxhHqksXtWZSv_5SQxiaTwXbKChaLPqvR_NBWyzqJOb7_qrQMWsrn1Y2Gx_7hC7eAdbtDrgiu9lETLGUapz_fFkVfkNUI8wAhx_FI8uLRGHUwYvMk2pkpyzrZrzDlkbQY03eA8XJvFQNoP2XZly9c2UgZQRw73bZIaMpIcJVwT1JXa7MVOVokfo56nkKUYnwSk778nE2zMEt6v7wcUxRj8GUmjVFIzE0FCdzNHQtO6QYaXv8XYUsRbIpCmkYHFyMGGczpqRAU2hYXWYheAcX9ZRC6sUy0W1_h8m8dKl6Z0_FqSt5yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA_tYi-DEabbG93JhXAK4E8gft69M4Oc7yF64hvRPZxRi4BQrH5rYLwcfr1ZrBEPNEe-cVYTX11ffoYWp4ItGTyUGNW_utUPxkc1-R4ztzsUqcKHkFPwwo6jUOfpHu2BITDNrMfgNFbzbqDqi0SFZOOUrPf4LQkckTO-zZBWviQtRK1hLOs2Y-Cnz7SUEjhNNqFQZQuxum7JRNtZN8djJU2aAeInjV1ZbTT5R5tZifORjypqAkhc2qvfoL-cFPCXp7JuycIAwwc6m-b0ueRlSASaRQffk5nTYcp_93qwCWxIVP0_R_7SnHVdSe1_GLXlVFiWGZOoh5XF764Qq2XvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k42BdJZEKdR8GdlL6DQ4-sEws1ucUJYRuSJbPKQJ-GM3Fx_0jYcAjvOrOqd6Hx2uTDK4qRO6zSw9dsHI24l-1JyDECYZxUNkPUj-vj8lPxLWJYd6aQvnnlG3i-QqAmKnGW4R0qp_fYZMBV79TmbUWcf0yh6a3l5ZFTiCyMEm6CYSmKOtqKnsTMvwYz0nfRk8FlNgyhbqf_k6QopipDumqrTc7JcWCmE1f7W8khuv5cewm1l6pH_FSMUI1fSM9uYxF3Uoi0l1UpoiaR6RhpL_joXDbW4TuW5uRXR5-Ib1XGRXw7c2SK8h2WwTm1SI9h97C2Ex07S2GHycu2anIxpOfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8XcOtst7VVpY8r0O9dtEIHmkL0qzEwnhiBxtvpJYbMcPC42Uo-4j5h43fledWMl7UunckA5nLJpxdgnamBLs7zymmgeUISupfevebD0gtld6AaC6nTyLpaE_M6uvul-O2eYDhtb4Z8ppLrzs4qEUUWxo8Up1ijWuMTFLIqqs4DkvVtG-4U9AmXitTLAk8U7g5ez0Kf67OOknk1Y3IedK7KVBeSWD5wzJRIu1CO9Lgs1VFeXUVTK7e_-dz9de78M516mqMTL32VAhO9wMw50dWIaKocNAZzevShds4ZlrxoxQeqB_gERAfedOUzCx97bOOp3gLKngBNjAUofJgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGSskuYyOPVS0-TgRAEc2s-AGWcefXloFZgUf_2RPpm-5KIlW-65yZ1dqjfg7z2kkH17QaVNN9o3Dhg5RaAy7OJ10yNm4tvpp1C_2U3-HIcuycbj_mHuQZ1bIKT5cd_clD9X8PEYpunQVHfTH2BagB26V7FkqtWi9jFP6yCWDyjGGmsplsZ0nTNGElPIn4xlv_PbS_ymdwyXaBMiEhFg3kvNORDYFUneTFU7Nk844GIXecqXWcrMdVEquOp2rgBrinyEot4l4HlgsVMyaocj3zV0xEo_YisZLeLSpEb94G4t7IMZVd78YYYw8bpdmKF3JLV7CwOUueQKnfu4QlQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfzjtqSTUcwSwvrFD1VIyVc3DhYSc2BnEKrgKRKv9klvpm08xHMO4kiKoedTe-y5eRoX8e0jyMnmvYO9zQFbSVV4srveDSTJqdu8XyScFgJk5VoVYZ8UY_sNC-lJ5pH_Pi3-2TTFnN4FNRhcZGNdV5eEhM2Uip0Wfzp6iN6QbTpx-CyzXiH5GRjMAnprbdXsvTrOWEGJrH2ICSyS4PwwyKMU7Jbr3S5tCkTmpxILLpTBDkTclZThIrWe2FOJufWx0CWRV2BUo8EkHO_DDJkB-4WxyPcoXEIb8bqDwA-QNCPxsmz-Jjfo-Uze4X9siYOARuU62JAQrwmvC9eFLlRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfSzq-2Q6YKC9WkECyfY5KMufuScUopC9Y9CjMac-XiNRrHoOdSbilgMkJ44fKtfnM37j0boSi0oUCxeyaEeGl2XqMa1lGSxyg3MGp-swxMzcjz2XlSC6XsIb1rFTqJSeRXa7nz7s2zHc7e4X8qPdMAjkwZarezCpNaI5XvrbaTI1ka6MW0FrEVAIg3X99t5bpKaTxPxb0Z90fPvainnsJ2d8SBk7kDsf4l2952APF-pXbujQmeUSNoLdCabAzIVclcGKjOBX_B3_ShYr03U9oU1VV3jBnYLWT3fMtlaqb767cqIbRbQ4GvtAxmS7xX_wEwdG0BETzk13YMH-7HcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CNkb_5l7HO-OAT5-VANksfCDFtmnfB-tF-qcqmn64Qbm7AzXCPXBT42wwVaNqCkoBhPxYAMOLOOiZuW1RNppTautlkUlbRJiJ7nNCuXp2RO4G5sCKfo9KQQK3l8K-rIdjS2-VdZ7LvWnj6XiYt4qC3slV4dLMIKEpNplSLSha6kFLSHSGMob4iSsnaI-fBkZOs8ov59yzUtQ3rhn9lnPRbq7OhDI5wlWGyPFEHcj4DgJnJ0HK7nX4L4h9H-iRqtIaj4hOkpPVzeaUQuIQivEML3tu_Ev6V9VR8ofokXw98SY5AIh1aWpFc-lzPwEc5vWkO_NCQB_aMaTB9Pz6aM7nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85dcd4c727.mp4?token=CNkb_5l7HO-OAT5-VANksfCDFtmnfB-tF-qcqmn64Qbm7AzXCPXBT42wwVaNqCkoBhPxYAMOLOOiZuW1RNppTautlkUlbRJiJ7nNCuXp2RO4G5sCKfo9KQQK3l8K-rIdjS2-VdZ7LvWnj6XiYt4qC3slV4dLMIKEpNplSLSha6kFLSHSGMob4iSsnaI-fBkZOs8ov59yzUtQ3rhn9lnPRbq7OhDI5wlWGyPFEHcj4DgJnJ0HK7nX4L4h9H-iRqtIaj4hOkpPVzeaUQuIQivEML3tu_Ev6V9VR8ofokXw98SY5AIh1aWpFc-lzPwEc5vWkO_NCQB_aMaTB9Pz6aM7nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های تامل بر انگیز محمد دادکان رئیس سابق فدراسیون فوتبال در مورد وضعیت مملکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMy6AWIkGXY3opc4psOgw0v5Yt27JDkp1Pa8ouFJ7eERmDQyAwVtIcCNBFSOe-IJofn0H51p-EYfXHEzPUWukGZ9_G9aAquWQnX4FMKEyaKT2Yl2mxBDYPBfhTTtsd3nX0RUiVFtzq8S4BMkszcR_vAe0GsnFFxPY43oO8GOFH-GdoMC0R9agx9A_XVGhXsKMRN0zjRtDeUw297USoPUxzksY-yy_J9dQTypUpgJV2IEYhS1TxKfIEnXG9vJ5jPNPGWpW0ZYKotBNdNdWtlsX29nHQQnT1i7kKFfAivN3qu8aU_TLGH2p6BtmKx7N3SwmJtMXa21WYm5XPwBSAS5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHs4o3dnnLr1jZNJKfSxDrvT33D4HehH8520RPMuBSfxf_Xs_vp19g8RuzbVXXuFQ7mDDr2reVcmmjqLLuYOl3YaCzRocDqhiZOootjkJlqdEIukcbh2wpbHsuWhS54DCv8ZW3VPVeFwoAFlhxx7_2t0W2KFhcUfeZ8PNeIi0qyArsckOVhiTPg-DAWBDBfTPa56jI2orobIlbjw9cwWSPqKeOM4CrlIdWKW6Q3K-TbgkXIfTDulTh5P7Wbnb9I3OD33b8mFhXMcLGs_AH2a4YG1BwsoRdcYuWU4MlhNspq1kqIGXkHEm-7N5naU4v15QYzLrTYIO_j1y50Ctm2kzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=l2vKO8eTaVMzWrRj0CQPKrYkEBpiJKjBrG7Pljewnsm1yUvHKm9s7El-7jP5bE_r4g3c9vDHSA2U9OV4T89Ikwg2GX9CP8JaHVBH81w1tsbq-k7owZF9oZFefUQepHqe_RXvAX0RacS2yakkQOLwcwuJXLIohs6ZdTjnqva8SE3P4fka3-oStJWhtLe7eNHkmNdEJt6Y9MINa8UiQZtNDLOoqk-qx0IVLtnvXsWa0Tu_oVHnS-MfDb_MxDzHgpFIO1nD560kXkjzBVUZP_s2fV3GSnmCR7Q6pHWexeScHLqeNVewu_TqSLs3E424Mgf93UQaiKolmO-b2vAnI8se6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=l2vKO8eTaVMzWrRj0CQPKrYkEBpiJKjBrG7Pljewnsm1yUvHKm9s7El-7jP5bE_r4g3c9vDHSA2U9OV4T89Ikwg2GX9CP8JaHVBH81w1tsbq-k7owZF9oZFefUQepHqe_RXvAX0RacS2yakkQOLwcwuJXLIohs6ZdTjnqva8SE3P4fka3-oStJWhtLe7eNHkmNdEJt6Y9MINa8UiQZtNDLOoqk-qx0IVLtnvXsWa0Tu_oVHnS-MfDb_MxDzHgpFIO1nD560kXkjzBVUZP_s2fV3GSnmCR7Q6pHWexeScHLqeNVewu_TqSLs3E424Mgf93UQaiKolmO-b2vAnI8se6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upI8cSriONBh34NdwZnyZSvqSgB7dvLEPYe7CSGhH1AjpfbgRu-zQIEEdluaPxFdGzxAbLUxq6hIk9CB6V6GoxMHOkHS0aU8GOlC8rPUZ1OvFwimnS0DyXklqlTUu2CBzAS5OlWnU-zKrqY_WEVw-p_acfnO8A-Kk-A3ONG6H8WK4klcIFxZMnLFnhlwYcBfMwYpMGQ4kpwEgMnjQaJsDZ07Hc1HpLozn00hFXCgGjbDLiHEHnRhiVnMaBrFzT8m2VOkKac6vk26l1MfrjMTndXXOpGellzXE0Z9w19qFdpv3rviQSdTdW1CMisPUN-bg0WUg0TFMrizNkXwpjslMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/aSBqJTSKC43bXdXgdWVFucMgedfxFBTtRoXJkopKI_obBdXPtcjkObhyF9_V4CIh5A6FKYS_pJveLdPruMD798zingKd1lIS_bNVb9iuHE3fGclA_sVBF4Xq--K9Te_tjP2eOAglwSjOfFPc7q1B56gqniv4pxhmoq2rb5fkYYiOKODCKGZAhtNdMeSI6cprx71zHz86ejzHYa2FJ3PWb-yjOzD9h_Vdd8wR5Kv6U73ghj3ma8ynF6e4LIO0fF3uwjwPS80gKJC5TOL9pxtcyuc9D5HM1YZw8wYR9h6p1K-lcdpvMVVWC3vclUF_hkBIo24NDVLJzjnV7xma6DuKkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه درکنار دوست دختر خوشگلش رقبای بزرگی‌مثل
امباپه
و
چرکی
روپشت سر گذاشت و به عنوان بهترین لژیونر فرانسوی سال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22114" target="_blank">📅 16:14 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22113">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjY_iB1N95n5FnTOI-dbNxBnan1MoHllayXWQ4CagFsN-Z-XoK2OKqRStQRNnkZP8u1OElfVfjd1e7au3k8QMPSWiVw4_USCbf26pW35PbiJXkruRuO36fJ2NGsvvc2ps8650xD79fukpQjo-nrWNHRvMVnoYvSZXxfALxKGkWRYWyZyi0U7GXJ2VvfOr9FCnIxBAzRWZ86My5iXUDCxq-1ODHrtLFZwg6hDtBmzOUgfB-SBWqmhNwbB-b9W3grppJefMXOi3ZeYOj2hj388GnZxx5WD3t__f80zGC3LwPLAu4TQMhOho2h1V8T4k7E9PtZw4nGzYWiToLECVMGEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rusbEwlwyV5fAoCQNV00Of3qiAMUJ5L1GKwedPDLPFucaq2aFcwpks1RaHf2u9DyA17c_tyFqgFBAmnPQ1kFpVsSD45U9hBGjWNGtSA09_HilE5luPTjlbjDfWbhua2EGeuRN2_3g_qy8IlBVcGvXduAQovQ1ckYyOi8RnUDzEvHrbqtYYRboCZAu4S9xKlw5hUK0NqCa7PFIj5wDT9vxkqQrq49gZPz6-qW5MYgiL-ycXQ3R_iXJc_KYz964NIyvi4o9rgpfdz3QiVMWqog-heDAObxMgVKTtDAh0Qqd-nQRQFeVM9Wg3UE_yRwhNWlnzZjg7q8lpbXjKyV80Pl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHdJCGKTXXOTx2icsstEETZp6zE7BDl_dVfXelEFeC-w00X_FC8DQBaizZrnn3WtRxPsDAKu9u-SuFIoZxohQGY0UHFTHL6FMDLfJIrRlgUgqxodvW66Ti4yMKaZNY-xwZUDFCmiU_PhGXIwP_b4vN0qBjjlo-h6W1rL4uXi4qFsPvmz1npc--5_sqT2XN8U-nr8uURo8KyufiHvNawgJ35MR5hLBgFlN_fERtoQ50XrigsM_9imgnGcK3V6OQN5SEbhfrrhL3r7AHykHCEWZqwZWGrAvFnsBdmnOka1AgLlqg6uhMFVjVXz120Yw6Jre9t-XL1qhxMO_bIJprkABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG4LcWFR9KSOyp32dxiQXzSEnaHH9UpNUAckbLKigP4w5TqyX73BfYTGfQVn2KZDQAMhLiq7NPVZg8DEpZtWLfLdpRcxiHT09krvTzPspwWN4PA6YR1tlzFyn8eIZHOOOKbeq91mDvvXrjzcz_LQQjki0CGIQTFajCWl2sfaWp0RT2Qkldj4HkMhLg-hmkwlN4M4Rnj4aQbBZGL6Xgms2FOEA2fEZa3JcMGLQpnIwG--YLgQgkBogYzHfJM_TmyUHNmG59dowvYYXauHa-Kwwenz5tv6qsqLk_8qJaCKaCmvjFihu4NF2iowakHtbNBU3yA2QoGCHeURqwo-YT1c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw6JnK7AruH_WftKSVqNrLQJC3tSMaeSSrDAkoZSbcKTGNQVyFzQSdP2SANkchwC83fEgR_fqRxwBuxI4SbjH7bUpHWrDeddjlaggy9sSFxmLX1eqw-iDbImJ1DLWV1azWwugHpkldwxsgsOFFHPlkEI0h0udG9xHpbtC0GkPhQj8eVaILiRGb27XCOwC7HXpLbRnDGC4rLA6PiA3KZnZae6sustzJzdakFwDLo_hL3HyHCZDSqYenGN6Z1rNQy5IT08hiPoW0vYjocFPhP_OINhK5596nHDP9bseRvQ3Lpq0xJDCI3uFMxC7cT2WCbM-_4D_8pwUBp_m2m6to0uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjTSBJFrkpe04OO6b5wM_HVmB8z0WYK-A1_J8Nt-WUFoao8f9ECyFYb4T8tAOvpyHmmrqMoz1rcStG6eWKjE3dLDXC22vp0qWDReUdpIzi5u3aGrnvfRuLZYY7EdXTcvB7a6LSlE5ZrZxtr7Z7PVJrmYGYpnyKVeMqi7ghjBvV9J0C1Aoh4k9ZYUk23kqHSJPvxQi2n7lXbzsJ9P4heXtc3dFDx737xEZcP20_S9hS1UyPJ204VvjvGLGOmUTdhg1zLrSJ5-WzxxJt-kOrZnxeodr2QIDiJXVf5KisiHND08yEgG_RdqD3aZ-78WFViXouS9WsXx9JycoCpgeHD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRgYMYlqTtl6Nl-_6mXr7E9zdt0k9QAb1e5miOSZqMg97lVfaW9Nhzhe1YHv3S9aQzJgPL_MQxv5b2hXXWnm6tlcoLKoSjPAgGMkymW_ZRYC2YCMCBPvEi3CWKLvgBnMORj4VdUZNnBrcqc3C9_Adda4vEHcNvn1eePst6Nx6W0Rc1hhzIcn51OSktxltCwvfz-UluNz4HyYhkLTQLLm7F4_OYwkFC7gCmZgw_cp9GvRqhjwCn42WlkI5FPpc0ks_wM8q-NOnNhs6eFulcY14Mnmpdv1h-El4mmzm4PU4WPvgH4n_jJFb08xOWgMvDBhJe10pkNtayz3Mhvj52JM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntKwZsdVr3jzdi8L0JRtbAT7HNYrLkWQPCKT5oHiuBhxROtOR2Bv8oCKdOoe7PLEmWM-RAoH84KxAQhyqlEmw9EXL7JT3Hndvc4lS2p8negj9VdtUoTCCPMuKXxAxFSZp_4KAyBcPqgPrUV4Z84adbjFuN6xrWBFGwcZhcr-la65Igfppd-u39aL3IdM-M2PAmfQ-ptg5FFGQqj7N2LI9KEDXqOlfsNmJR3rteQSScEAW8suxmOVSKnnML2BFia2dr3l0ish8dhDYQ-7CtuifZ6glDKZ9D79ZXP24XSCBQE7MUj_d4P8Z_AVQv5taRzAUb4bcIRyqj0OIY_raUWIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_KvE9YVYi8rGdjkR7lCivXwW57-c96Ad9w94OQ4yGp41UpTdefQuKxqrcrNu2FYuVjw0YBqo6f1iO1qCmv4mZxyxfOg1PR2uLgQ0KyExpUhNbgIg89Q2lFdHsVzY6xmwY2qPzHA-CYpm2yWV0LVV1ypgd183393V1zchu6CL6mA1Xuap-QdK_Gl9hqrvFe32gpoTZ8uCB_pVC9SxZcr-8QXyqL6yW5XN6AYX2UHxRYEvz-7HJj4TqyLjHr9SdOvzqfs4BDjkspYVmdU97841yWAZhO7SJNNU7kf2g2h_WKu_ksE-22w_95-_JekVBHan0V2Kqbld-O9kQld0qTIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjlCv1-tc8tkXW7YIWsl12pHwlaTshKvaArAqs2zc9nfWFLsdXA-Pn85aXpfwjxgds0lDquNyneQ0M1tVOGGU14lAT92Lb0ElWtsVtpuI1UE6eAzcdok3HX5CO8buNFFc4ZSFGkDZiCmUlFhUblv3XPGLGyevZn1dkf84-L5S0CvKsOuFychkw8rtTAjaC12NTI4Sw39-2GEMlCa20HD6jD5PB0vlF6ekG96BJ2lsbusO2zn-PFEBkKUMaCpBMCGnnSCLHvVz4KENzsT4IHkat_P4Gv9pCEeHIWziBKyQsDn4m7C02VBZ0YdV4m8LdoKF7zYgx340ecs9ZRoAmsBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpsPEfm9SlcqXiyxE1s_pVYrE8g2j1ESrbGjZ0gvJ5UT_hCKM4uTVCkTVgRbeTYvpwjRsVesyAZhdyhoi7a7-djqO_giACIkTsPQmrAmEDLaOLmsDayiIuY3EY1AhyYZOIVd0wH9hlNaD4gBCP7WJneLWHKddL60q3K94OyROQCfOAuIOfF1qcCzbgPmxA-fHAXiLIzZZGit3adqWLYWjPfLiCutTXOuk9efFPewjIq3Mxuvpl1dFfCeqKDfdtDp-EIXykQPPuC03h_kUNXim2JH-dZM_bFSAypROzIfiMK5LGMMYh-4DT6fCkFdXqt_fQrFhdST9Aqa8rQ_A2-lJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ov3MwGUTW_APdxwrvwf-9gRwKnDK0UgZGdT2Mf6J5c36TQ6R8DkJ0Zmn-8VCjWK6gS8LW7_7xMSJdROKveX52TIYzL2OUfEPM-sXzSXXDMD1wGG8gDMnkxFWdpHYQ4FFnnoC8eR9Ku3uCsf7UHi90nd3GLxlpi8pcX9G2WIyu5zt8LLDwwXyLc6piPstHw4_uK2Webv5y9rIDmtEMRgk8zWiselBH9LpzW-B4I8zKZ7dhmBtNU49HOjmt_o05G1L-LlybXaPG-8V3-Si8YpL6B_iA5Swj3SqCXFmNX0Gj-tTMjvsgXiuTsIHtpXy9OL8jXVtb36qFtWYX83OOF_m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس:
علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22101" target="_blank">📅 14:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22100">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=oDQX5HQmwldJipyTJml7_5WIJeLT58XWaOGtzD3E-TH-m7eoD6SaZCEUoBvFvLGTlKIo3v1vcKj5eLigqnV-H1DeIvErjAOTqbmZpq3TxizaYdO_U2SjZiAoOieITzOqJXb_qlpmH2KLF_rMRxRQYICKhmE6KRCqHsOe8J_g8Ih1q3U_6fTP0KZuyv-jTWHFEqKKoc7AAxCSfKNesNYIgAYL7-Pr5xgRsLI3xton5HP1qOPVVryec8V8g-tptBpfUaoE80HPXp8vNS8Zn4inx13GF7BW9uIroOYP9Ag-F5_JXDm-B_UxepY03zEbCpp1SlEKeR2ux0r-TSrbJYgVog" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7b3c3a43.mp4?token=oDQX5HQmwldJipyTJml7_5WIJeLT58XWaOGtzD3E-TH-m7eoD6SaZCEUoBvFvLGTlKIo3v1vcKj5eLigqnV-H1DeIvErjAOTqbmZpq3TxizaYdO_U2SjZiAoOieITzOqJXb_qlpmH2KLF_rMRxRQYICKhmE6KRCqHsOe8J_g8Ih1q3U_6fTP0KZuyv-jTWHFEqKKoc7AAxCSfKNesNYIgAYL7-Pr5xgRsLI3xton5HP1qOPVVryec8V8g-tptBpfUaoE80HPXp8vNS8Zn4inx13GF7BW9uIroOYP9Ag-F5_JXDm-B_UxepY03zEbCpp1SlEKeR2ux0r-TSrbJYgVog" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22100" target="_blank">📅 13:26 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22099">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjSM7-J97kFHfId0B5grS6HEKDxkkdgbOn5XMP7Rlbo6Ky6M3ul2gcAIUkECSDpCpj3sFkFpV1XOewvXmby3-rDeH486-0uXeJnAOOiMTd9AEtLlT7Mq6m9BPGnNY2JV2ZJCItA7ESGvusyhngFOyZedvyF-1IOP-x5ZZwcuIXqlCWt13xaK_OvLR6satttA9xzT2qg4nqRQP0TSHnazzrt6hBFOQDTztRg31zYD833BOZOGxI_6N2CxTJtt3-8fjJyddIsq4vaX3JXJD1XNm8n-YO3fk-1QwqwNGQFw8u3WZwnAXmsr2KwKps_pcmGU6wiH0qsW6XT9wS0m3t6x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMYFgkd9EOnsBgAXyCZZn4B7QG0LXOeQfTWgN9EyX8ZGAgVnGSY-5HFS5-ZJsxOdb1TIXINxU6wjd8uUKK7B94acWg5QJONDCUcJyjCC3VK7HMpbuiFG-6GRtNUKtWha7R8I57nWh7dTBzWjti3lBiDmE0TJ2JHTBr4uyGeaqXAQQeFfpXLYYjhq3-9qO5u2x0XmRCGIwRfRBYrsjX42a60ABEDla-Q5lWj7e-gxFjRPe4BMOk9-wLFHovrrFmqyDr-L9-RWwlPVgGHlFv5mL4NSlV89dywTcEa2j6I4Ipu1YlARW7az7XAUJ5pw4XOy_7EBxLIuV7rmDUGpzhZ8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VJ13tRt4Zcw69aQ3mO5iV1daNNPe82FvVoKHp9KNW5BGpJDr7vxHUkCC33zR1CE-KEpbpNtmwGWMbINitteWkXesk5aw7sVhmpLufBYVhSaYHJQIXRYl9b6nBCVSAt2zFvzlLQfIQrkKR7KL9PpZpEVByEt4u8obgMW8ercn4tt6NFUyOVBAr8JKwAXMRH9X1lYapTq7CfPd-Fl3EU_22CCbodTCu7GLCNRD3knzrr5NA0OyR_yerH7PLHZO8tT2hY_2Cf_El14XDlIB_QAkbF1XsGOJMloGADKQVXVtwaRDu76rGBJ3T1ZkKV29t_WJZsoRG0ESOIldmq5CtyunXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/REiorfb0wU0AZF412WwtkmF8QycAj7Sg90UJl-J1vm-4ZYJQoAAhW7MqL_QPVdPOMguz6QbK6ZLSwjbKvbCbFODVUwxxofdxm5WxiGLVAaPm-CmN4heC_bEgmcMXET8IY3Pv4niNvZp3zwRHPbkhBoGroeKTf6zaAfeu5aGNn8rG_Z3ADE041KOdLlbTp7RMefgIUVidRvCxT1O3tL6uySkRVDsvdAeURTQ7OsYHE63l4N-x-NXfRelThPurEsPM1ZFqMpkB9JTZ23EL80lQBzw2l-qDv6bU34j4rRTZJolChKk1clq8WMwcnafCHdWx0nwyYsCpBrO8G0GWs7N3CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bP0Sx6DySsopmyUWN6HfPdtbu6KK5B6UOsxztRMeQ1p_hxuqDtzcfkaCVVZQO4-Esya8t_dkSzKH6niEmiPwQWwlZKHekzGmMpaW25HS3pJ-jDAAbjNm_zuPMUkGmMNfllnEJ7oTwvJZJI3jn7XaCHKENCds5yLDTfNKOElW9GcVfF1e_uJSPBbrD7Wx92r99Z4EWuP2rynn5PuO_dFREavMBO4c1ZoxTJu_q5hj4XVBdkf7g9UItJAwiazJL6gQONKA9XtiVejxmcJVmdagjyheFnuMGQGyzXIHKA3f1CXcCq9zB4XtpGvYV-CDl1tuZtM73LPyTxZU6ZxCuG_FdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/agScLELUeBcDGfkkwnmN8F4mkau6Y8YqX6-jpmK0r9lf7kG9Y5zMTcfgGyNBkzYsMtXCkaqLWhDyBa7FNiXTaqGR1l82kx46zringCAO6WoJzB5d-8LPJ8lgxyihic_zXquMPvMSHf-gvRqPCP7ONQ7WsW_NRDWK3S4OWHnXPDQCPfcdv5AC2Os-dRtuqYZhZIBYXtcF5wH6G8ZhlQJnVKkYdGVTXSQeYOOPSYSCVMxMSzYFL8VnPH5uSfwzDd8MyHmYD4g5M1O2ebYMyRlo2IZR0jjxpCrlALtXcKBfAmhh2fvzkXIOlqf5ndmAmOBKieoxoZ5cGIxnCNd5NR69gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U--GCxIwp6IAgQce5cREIi6uo9FSFbW6PoUFshscuPLd78tA-efvey_WKTS58j9v7yQK8sIPjPsF_bLtOJ44kUpmJsZHkoTVn1Pig5TNmEObXUyUGnEoSFWDq-Ms8ETOs-HWJ-MuGzwveAwdYPFduA3nMdHA6XZ1Q4F5X4-uGbicugeRcxH2uxlHi4ItSuKesenuHPaQ2CqILAEqx90WY6RBBNGSQhCwM0MMJ8MNwnZdSXhu75gOmH-T2jCSLfXGd-XIy_SDhhzpfMK_s3PwSUgZ242mrJSH11jG5ccYFZmOlunlbN134ZHCLl_5msFYwGHn5ecwA2VoDKgnN3KKFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqyWvlC5zbGGQ_t4f0VycIJjJrj3XTrxqHPgcP-MbHX-XlGAzfkursZZgk8RmmXcg8rq8dXPgvWX1hHFcEFDp9yBRFVFUlI6VIx_uiAKMfYYzXS7PQt8fvEzqyG7paQhRlEpSHRuc24NPwrVbrMATUhS5ESHE-JtXR6pK7jgD8W33LKhMmjbwSjHBEVtlze9OwZQbCOl9lSppg2EJLwPYorWWCsOBAQVxdTAgr7zPX7RbVTBsiuomg4Zwu8zJfgPXufWBLdF7rWUNnMIowlBzNxz-49M6VioqBlVM7yB-RCtF6-SnbujvdyrvSXlzYQmijW3u9XkTne6VIWkpFe4PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtE8sx2bU_lhbeK9qXIgn7Mc5dSrLOheoSu1zkcPvnbUTk2Ek9UB_OsOIqVVrbfOON1Mmvnhm1hE0sdbfKexfykHS8f-AwsezskpvFO-KnRxJxNOu-QYE7jSjArAU6VjdiC5D5m8x8obozsM1yS20JWEeM9nJC7P5YV6-pCSqYOYC4q-VcXbgZzB18fa4mCwBYAMXkjxcdzj7UF8xy-T8xh-6a5zY35EKG4SzgFJjZE89wLPOMliEKugz1ySIwATmNf7I9R9DgSXXghB8nS9q6kcZ4pA9QNUIRG8eAyv97r2jhbhngkSWf03liO8JQFj9y0ggbpGB_G_zNajH3Wc0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHY6Gdj0fpj4kGiUFokKAgcxmPPnR-gYoJJLsMXs8S1qHpxFRSPoyQ6t7dp_s0WkUJLibFxtPjZuxXXhhRpvrMLr0PS53P7J1ob5FijNjN1e26QsY-ayqdcCum6yKJTqBAakpTQmEnTWOGggO-Dx01EUW-nmIr2uDqhpxVlAnBw4vi4d2SLyIQRJHlvsCQnTHT6lt-UifNzq7q5Q_9m_pU0L7TKqG2W-VqR4IQq3_Yb9zq0Tkir9uQfHKPNGYxqb4Wli22PnX5yZcOr9aIiTI3FDjLpE3OPwawVH7aP5LZo0AlHg3CINxpVkyyRd4NI_oTJkKtoznr9QtvPVQ2V65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBAtMLmfkFpmPI3-GXohL9byNJqNJCo4rbrpV-U93BT4SjQidQga_o8pJTE88F23IRP8NULFV9-JCiXjPtiFn19JTuymW32IyF4nHvE2MJiXztTF3NlALcHCnPYDBkZeUBCadYiXa-PUF0fg_GdfjurNczNx2b0oSiIg5vU_nAq33hm9rpMPlppSj9L74E4Xk9z0qA5kShAIyfQUuHS6hsDOQE5DUogZvLMN-zqqcQkQP29IbTRKZ37rQc-1QDNyrzsch-guAVuKV-sJqGKfAVQX9ZLU4rDkqwJyMLRxmqARwwo3z9rrUvnBHWyyERxgsWcN3r96hA_Budwz_qNJdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Je-leNDpP8JYwYTqXmshVLmkcTj-KbecS6DMD7mW4UiGmWQe0DoAgK8NqTL6uPYLasPnneg-M1IrDdUinFIjdcwYz6sVuwKz3NNqytu6uekYniLXyIVCA6LSHirvQWSIWqTB_ZlsleBWWds3fGC63g_PHRdjtSEo3BNFpmv85w4MBP3lgSrpyvMjUGnRQRMc08Qtq-tNLMILafxS7pAyArjP18d2LEvuSSKOZYWE2eMTUdtDgphiYps3oquHZcMu7XtFPqpnwj2KxyX6uuQlTu0f_f0yw3PMaUjNS3gVgKHPraA3-P5hGW7kCQdCUkbYNRrCeVk-usnUqNAmVVaNRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hl2CJ7-afUKEdAcO95YZUm56Zs1qQKo15DlFku5PYG2E02WkKKPK7LbGXYWkFl6I6vqVz4gMnuv51_i3Jv0Y_l1OWf1VOGN5l6d5p0F6wRVYH9_hrFTTqphy_VvWATU3BFxUVCaevlXuMfhwqMr_OWIol2qrAOrFov-ef7UuGbj8oCvaN308U6dq3xR2TqVbOg9FOdCeCR8Nxakz8uVkNGbaM1UQloxdQ2GfnfWjB4f7ZEZVduYr_uLGkHndC-OC81-v8FXqaiwRZ61azZZk8H1v24bqAVMWBo2kiJiK475BhC_wgvnIDQ5NAYVymKOQPPWtg4MXEMVxGLYVr-VsdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cdKi74ESop9BHrDq9CfBTfxzOBFBGTpcLnkSc1mNxXfQ_Mv-4AHEAseg0O31NJT73lwHVmEgnEyuR5QJA0rZvGx5lOtuVOkh7bAj5f5jWMR3au1aV_maZC0ZGa7IPp_zgvGF6RerDENN6E-rlSGJS6yANVeohWQvrorJ7GwFm789OmNtRUBYjrwHoHgXcqBtoL3DTwX53WPyR-dpC53c2czKNhdHjD0MIGDM7tuJKgLOVOlkbSyv8iV80r9fObHF3qN0ob8kxHxfnV2NQk13vq-n0dQOOAwek3n-kN1f9Uydqz2sjWNAa3B80digCxfYnOJLZTea0Q0gm5hd-XYLsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S_yLAFQ9jTMRRZe5j73fYnig4uzDKWH4jaSiWoZwiFtJVRid2e48LfIhqWpmVLhMjFxQUgyv544FeQF-HMPV5ZGCMs9NgdD_nPcVI02bLgeQHBGxhWT5kzeMUMEcQm9On6ywttxpOHpiTLcDg3rnQatxaAGOGF0XDQw8FPM8LMndiecaeKc6WpzErU_5x9UVDptd2yrq09iKBIFKWOxUSBt_BmkOUaJpwPBWKnAwhh-Q52BtwMDBmnhRfxIp_EDlxdezEUYrrzKOsCjHpQsbUlBGW4Zk8QvdrjdNDfbuzjG2jzuWaiJjFvJPvpftFj1Ddazr6eEhmaAxAfAJ_OryKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYuL8SP_W9vt-cTN_dsx3EGgBQWabB7iGIsUtKUaGNFWvE-A0TmKJ8dzi3A1UeKXKgp7Lk_eXuz5FEOKdao1CsB_Cb6s7J5R_GXaXO6jiynvHfL8g1Y8rIzbSvUA8aEFdNSdcErxEBCEvTQtQbDe8NrQI5nFrWWl-jjvBIVlYCDQXy3mUxGjqFVm1THWQyR9rrPKV3ejTcOX7IbT8hv2PYsVQHEoaIAxnDH-ZsHpXiLT7SR1MJ0FT-8G2OCo0gfu9EHsTSn4xolcUZocTH0-jeuAMiO7wMjgrzYB887LzmkYCc1s5zcPEmIm0UuVkWXqy69IcvoeZ1aMqQxkOCYrZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STDdUrFFbCqXNC5E9PlzILEwtfPp-Xq2ge8gap67N3C_ROO0ye3Ph9p1wEOUgMSYUoEKGDCbC-tPm8yn5rZ4CkAUagDGStHYXsqITcIYLUHyYZ7q8vDY9m9cPli_3_NR5Oxb1IfElItHTPG3mZbtVigiTsCg7rF6Pd4YGNHHNV7YrtWNAbgSpap95e7HJNhX1tNsVPdd1XpaypuyWAWXI1GlSuxuwGOoKLlut192OG5QiFr850b9Y7fDWEkWFemRexKGGtq1d8_mn4dJhRB2ZA3UjnuYs6kAV41KmB82C51MrLZpBwtjnYcXobgWyQas4uIWG_BHg86nTkSfLncbNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcIBxFb9gHiQ64cdz-eEF-1i_hokUCqlZ7uI92ArYVq1u-MczKDevNOYvGARbSTgkLJ1mHCFVEZ9u3LA7-1ATaJR-Q-ble-J83i_x_LI095yxR04lusV1XdGf79WGD46RbJvaMnUNcnSj8XsSpOcZKyslyrpMSl8dBuTpGsHR0QbtrPhUzjs3rP3syuu1qY44DK0FGzZy-cNQuaBfx8TYEpddxBiLHy-2jzjkKWzSoXjE2jub6RD4-Sd3AuEOUvm28Gdv5WlKQZqtpLiWKg_8-pf1AKa2x0sijbySU1RQczv20V5wUpaKSGPjIW7Nx8kSg9swiKuJsxbe36Voz3RnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjnPJrW6iCtxaOTUZnzISm3EOkxQeOXKahk3mfxO08uJl7JyqOCP2eUfhLAzC_rxP3hA9FpqAmE6D8GBYVdWvz8MNESdEB-j9tZfEX4DNrL2EdqHNZDHcXoRsQVJ_x70RZWTjnoLvwS6aZRkc_-GSnD8tl3yEePBZLZtlIJ5csI1x17ye0mgcD9H4hI1HSOfKOpOCMzYiTOR6aefLb9B1MXUnU8NnHhkEijY6FR8xBjKAhrTsPE_m5rjR_yfOUOKa6mSd_uK5l0qhPqHjZyiCkpw3xlpuYfvJP8YsF21wO4g3k5yypyfwW8jFxA_IAO2xPKo8oqa5MGlpAm_yN2ozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/idI1fViXmF5MkIRJp5T7bbODwaNKq0vQSpPF4FVYN4ETTIHeRzLPFVi7Ep9eA0H_GUQKxw9yERewB_DGF6v49Zi7KppL4oV0AU1qnIiRIaBzytZzG4kde7mRF6MZLTOaIEP9c3c1_SOg7qCcGK4DFLrYfhA0TAp7QuRLi1JBO7A8SoFYv5UXrPYM7YhaApRMII9_dxEnAaYIt3rc1x9H5fRqYYgV0zKHxJSapeOzyR2UkqIOpa7EyXAVwsKZNQZgRy48f8QBN693W6oxxQBSjKg3vatkp-jk3bsbl41bsjLjH345mwealJAhTK5p5WOSymKYn193Wvya_s2fEHl16Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q7oLwTbtXccvhD_3gY1tUKiWUgjsSsYa1vwS7IK7yXjZr8_wfTX0-fOdKjh5YKiYqbkhAg_zZgLUUlBQaZU77c1SUGlGtiGySa42vB54DNPoA7nLWFWhmv-v4mmuiJAl8U_I1u3PrDwRkSvfJYfG6aIcszEgY8EtjURWxFvegxaVLpeYPW2dL8wIFUewvAaugn7pdED-8Tr3_zTQno8YRj9of4JI8vAHQByuyZrqHa9q7nHyrSKs8e6ennapbvD-lu4lmxvsr4kZIpz5C_PHCo8G4Z06kQRbnn1V6jYFOm0ZHBsLUJuNTWXa75-5bobS_qZsOXvSLQ5MYfAlepUfaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pdGVVICsuwpK-InJvQ_6DiKTo1G2_wXZ-OwLRVxNL0958Gnu7xbqCvXo7rVhp7_d9Z68nDZk8lAu1DexhvfJTkmthoGYNWTJTjOtP7z6aLb86EEq6jgwE3I5JkLPviTfgfu7S0l0G9HaCSNC0btWJcgaVuUJHh49HEB3Zxwgal0QQodTvowLGvxr110jv55MElW5DzMlJMTIlsfDUWXQYWkmVUOmzlCNYEPjlMgS1WnDdBrWeRLY-hK1aYnbmkainVYI6zKMsDE1zEQJ6AklZl9_hTOXXF8KC8quAo-QxmvJ-mkZtK-dMz3o8VHeUeYok3DzEk_stima1bu8CDPgmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H3ACFyU7CoEGp_MAbmebZMprm4jqvs8zGwtm0mmUhZEOGkfwsP2hUT_HOTSrPHzpUMdOZJ1ITQTfbtMN69xKY1icaWX73QgGA8S8v5dValPByLGL6isGH6y7Z83FOe_9745ZqJM9Ny1WwGpjQnex28u0g3zT6glxU3y-iRsBLqU4SoTI9Pmfe2bUoHvr5RTmPokfWHguPhpxkC_UdY8gXhUga5wdNS2cylXnSjG3duN3vlczi87zxNt6Y7J5vWMzl0MQz9rXJMAg1DHe2l7vjMCmnOT06PX-tL7O9xmdFc0eNozharbiiSzp1iefZdiOuVaWEvBhS5cKL4QMygDCqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=DhxdjbI4o80jNaUksLXMPr3SXwagR3mylLbqfVieXDwoDCDG-KgvXoBhC2jltjeMOMljLGeKoCHiELCT3EKZ85ZC81Aiezswh6FMw1NLDGB064swr-qtnmnwaA4kkGAxeVuHyJDcxq-yKCBkB4uipNGBLGEjjKHBCLSc5s8oXukkSCgQsFrrFr9XzrPiYYT0GgYBHvv5LoJjrA6mn1uAurciV-BzkE26-LP6FK0pjFnkc4NDQjvSe6bo0QOSO7IKImTLa9VTunbsbKpGJ9-dGQIJ2bazGsXNmL-umvBJcZ0ZI0x4gShB6CJZgdaFd60ktRkSLDt-RjpNDQBgjvsEDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=DhxdjbI4o80jNaUksLXMPr3SXwagR3mylLbqfVieXDwoDCDG-KgvXoBhC2jltjeMOMljLGeKoCHiELCT3EKZ85ZC81Aiezswh6FMw1NLDGB064swr-qtnmnwaA4kkGAxeVuHyJDcxq-yKCBkB4uipNGBLGEjjKHBCLSc5s8oXukkSCgQsFrrFr9XzrPiYYT0GgYBHvv5LoJjrA6mn1uAurciV-BzkE26-LP6FK0pjFnkc4NDQjvSe6bo0QOSO7IKImTLa9VTunbsbKpGJ9-dGQIJ2bazGsXNmL-umvBJcZ0ZI0x4gShB6CJZgdaFd60ktRkSLDt-RjpNDQBgjvsEDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Om5fRmgC6eaKZnTM7g_yRy065Wx5iU04TJRknQAcPWpYtmD4F93h1-tO_dpbjmDr7jjKwqWl0mLEsWtKm747GtM1XwQPmV4mPr1mbsX0S3EEqJ02S0WRYIN66BXcOwNzlaxvNWGGBIgAsXbeKdjEjcqeJOzfEt456iCvToR7K9GqTtA5il2Yo-9oeadTkJOFzGXfV_EWDS4gB6MgLQXQcWWV188cyZE2-dEyKGT3DqlDa0GSly82j_n0jVZsISwu52vfQtCmtAZ1qBhbdYPVj1CIVOvws24OFYXg2Djq5_5maCFihKu6waAnqQusYP7LHr3VT2C7PgzP9Z7jGKgHEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4AqyfgSsZ1rw35TPo4YTBgitxjuEw_LOgw48ESpuhXP1kpNI2Gca5hIqV1-RHUbOvY6FILVWiUuGkbomzXbI0CrXYsBqtweBXGeRVXFtXis9RbJJXkVmB7TxAkwQZVXJKTO9wqLN_AvhNTEabQvGt3GycF5Yybz1h2cotCa-VE3_1xaWgjY_l1BIkBU7W_TRfhuqupnLwm0L2YmIHj39WNby2yVrMjh8SBkdLN_2xeW1oQXRWP4ad-jZyQ4BC34PK_s_ZxZiQWtNHKSkdryHqletbhARYJ5pJBqIl-Hc0oQo50Vgo7MmyewxP9kldKi-f78gHb4V1uHOOQUyt59WQ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049Egyor4AqyfgSsZ1rw35TPo4YTBgitxjuEw_LOgw48ESpuhXP1kpNI2Gca5hIqV1-RHUbOvY6FILVWiUuGkbomzXbI0CrXYsBqtweBXGeRVXFtXis9RbJJXkVmB7TxAkwQZVXJKTO9wqLN_AvhNTEabQvGt3GycF5Yybz1h2cotCa-VE3_1xaWgjY_l1BIkBU7W_TRfhuqupnLwm0L2YmIHj39WNby2yVrMjh8SBkdLN_2xeW1oQXRWP4ad-jZyQ4BC34PK_s_ZxZiQWtNHKSkdryHqletbhARYJ5pJBqIl-Hc0oQo50Vgo7MmyewxP9kldKi-f78gHb4V1uHOOQUyt59WQ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvU68VoREKjHDnRMAVkcIxDz2OC_DU_T63Nnj3oy1NU_gesEmCpR0jwUfwZh8RzgaByFSia9uSAWehUqAlWSWeDhOsNBZzZZ0BOlw8usKeMShZyqTzF0olykfRzCa8fvxl-rNczonxR5CGd5Zp6vUzYlk61jWzIQbr3rGOJ4d7jgYJjfutK4bpPexyqgNSeX2HXVqSIA3ZFJVQZcB-zsdU-l0ok8g7JuQlP-wxAU7x3avpE430s5DuH30p1MJI_b80n2h5phr2ZUq884dPsittRrB-WSpuSm9H5qqtZmM6SNiB5acreDUKUywHDEorimQuUWUOnpfe4VKLHVN584ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9HxKcGOBk0ePWYOFV8lpy1IwmS60XQm_g1M3thc1n1rXhEnC-L_bCc27ep7lTuHsr6fZeD4UXgOMMxsvvZosY6IODd5lHkrJOxfsUDKzx8uN1omS668iup0_h1ZL71hrLx-1FOZzyCzKfDmA1d5Ik2X5vIkVfF95I_GnV6QD84E_M4woMIRztkLGyUSbQ0U5vz7TNXGrwGOmEsosOim-Ykju7UrHm6ScaMbT2eIkZn83MigGSio09z9EhmJMGyYKLaKhmQJfuBbSdiXs5dBV2AmEyCZlDG_H0XpjwKV76yFjOwF9rQ_XjgpBwYllyJgPAN0ZjO4BspvPrtQ5cX33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1FfMUkXdCqvV4A9N-ZwbRDZF58QUwY16pRTYSRGuqF8FUBUsAcFJMgHGPicADYvSBJgrJXKFxDXMnWUA7QNm3pzjE5-FZMd2EbixM3Jx3ITnMH8suYbgC8FKCiY2ttr3rNE29slbrii6xpLgt-g7IMAO2SsZHMQnqE09Br1RzN8cXtDW-PbdxPwJLL1mLR9cnVJbLzWI5EOGHzik08096nj7yoGnE9DfAAfCIOQh3JolVJ4hUag_1MYJYkHst9Pl1FYUPLGvQKGOxjNEkb40vugJEH6JxhBn7rHYLItC0vPDbGUUjKOpa7ua6rgnIlqR4n_iPI0CjI0TRldpNuzpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uGN_YK8sxkhoeH9I_vRHBapYC3g9n3LwWZl6kfVuJPkJQayVJ8SYBAki7sri-hhhh4Y-4QuhRr4GcHzIfA-qHKQvknNOm_7r5ICsRlBcI9TtIoGl_cwipcnb2HYTl-ixj5htcMrROnDrfBaVuvEbLb9ZvEFNQjOlU6NV-WHQZdV7oe9-WyIgtObKfHu2Jxcuo-kRl67Qtv8wlEHXDGA_t9JYBsIy8ppwoceQJbBB8YYec-Ts0_wS87IWFeqG4thioQvNS8VwGIEBW1BAmlbopjpkskH93JUKT9fy_olqRLOLe-gl772q_8kiXRXTQ7HcqhjW7DWrtMZhc_n3cGLrnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uW5GcioJ0D__LTshtEKo6wNnVn7Iuq0c4D7ntjWwnJDylu1l50U6mpoIcM4mLt2jbQDd6V_tleMCVN-cjX-bMVgcDcmJOYNybSnOdijB6uX9sgoN-eMByj1gC8arasuVGz87viZuC54GixiwvX1KItO8P_uzd1PT7BbRPWaDWT5mc_lbd5Qa9sYLDmRpzykMpW2ttuzJWlA9Vh4q--kW1aV3sqWx3D3JTxYmNzAQVnmP_NCJGOQfbNLEcIVpXq8-NcOj_txw-yhYeTBGGa1OEhG6hLnkYn-ZpW4Fpjv--Qp_SAD9t0tyP9huR3BFaNhsN_r8iaUx7sjDplwIW69Vvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OYsYQEj-8FDZBNcMsFYqfVi9qE39ywJp8vY542ZuJDjnsY1x2k114kPL4hXDaHGa7ipsahhxdUo5GL2RfrlQAwYAE5qPZAETJwnprgau9UNXH7Ucwr8EK1rvjqIVop40e_PdHsM73p5QZCoCuJz3EQQoowZQWL79s9OrMpPwIKjiPXwz5RHvbBc79LorGYcWAY1_QzOHYmRQMZtziq4XPX4cTwOgUFcuqGjVBvqK3NUno-o438hdXlucsCLbznIwAex59BZeTd4C6kLpgovZFTyIz1DTDRoLrgo7VVuIaHzK7spz4Y6mopnLXZGSoLtb-d7GAsNMGKs1OrifyI2IEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHdOtsSlHm1CZLCgkyQBg4UYg5jvI98XilUG3Tarexs22N2SZ39cjXeSaVfoHiMvu5amYq0UuGJqgCY-TSaLCt2gtRh_6c-mLli51Q2_HmB6SbfwShHbNGkjmMbgeOEiPwYUML1CssHedgXbIF70cMVfXeAnRiYcFkPl49-3So3TUE9vwjRpGRBZMZil4WidTvztcFQr1ajTuzFesffOEz3P-zbzuXCIC12SEraI-zdDQVb7qCr8k1wCQdSq9vJJmQ7w1AU-sUkcTpOGIAwOYVUo4_Ht-ypJyrs6OPf8pYhQYecfSyHvIeQSfdMvp2Og8EY45PoiasszrlV8rlv_1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvpUqp2g8JJV_1M4LkEKxcUuoCAnkPYslCgkQVy2mXp3R9eRJ-mPh4WA3t_ZIrkCSH3thPYlXdJeZBpMXf_170Uwj_x2Fm-Z4mMh9wYk2M5BgZuQiwPPXs3xUy6rzDbNNimZpRoF7nzcDrTVGF_YWvOVQ6ljHNb5Z6blqiCLeJ_TuODO4S7IiFm4q4kq6ap_qd-p-2DFdmN273VL0O6rCT762eetMyZnodT1N-j4wJVgD8MvdnCWvbOdLFQ66HPwpUuP1COoZ69j-ifaGc5G-XvBDVDMkzT2lCqIq9nkRS3KVyMy63CD_AxTmOvJSNRpXd899raRxIYDmSVfEtmRSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xrxnwauj9-XJrNIBEnruQF7kBbPdJlX0pl2jAdntZYsYO2DWKrwuJfBDLfc-aiXcoB9tN9hbIbeyq1NVV_IKiWM0S5Imdc1loNv67nMFw0ojhR9zbFddE3CX8wrQtiLl-0UBcGRoUyK7FPLimyQX2Z9v27Z3F_t5S2RlGWtFJ9ybJXhjT31XfLN9ZyV_Ll2vc7OrCNfiPTZyk7kWjRrE3dMdo7hA46O4P9ItNU36sP5KYg7Wp_m4KK6q7jqPSPNwQa_ns2euGcqhPyUxU98Cxwa62e7YE0qMBRe0z5fz4ITpS7H2RPMl2Q43iUuNBrY0aLlTbFciV0ach7y10WDcsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nPsOz-GdVg9TH9DKt-XoZJ5bJ016juKBA60erfkGkyByZP4C0HDVZ_UItDXuBnW4Vlv9Egsn8YmNFmPEGKwRXYi8p8DvpkBMvjPG0yjfO5klXn_2E9G1_E6JXkJXCmtYnHRzIDkdkUzZxBYkxuBHsUITXhqlPVO2rfghDW0wnuLnqOxgRHlpfVueeBnNtHUR10tX_JO4h8F3sNadyyIV7I7qe5B3SdqjZ-20FwBwlfdsBdHnrejMQtBXPkCy_hFnSlERA7IEStGJPJG4lsF-3mUeSEmyr6cZ4VWRnff06M2rVguqCguNH8OlM-_PTfsIYZR3hnFkPhe55PlTP4BjLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DXrGPUSTXgp1OpVzgdTzf8nJsc1_5z_dK071lwPQc_LYvgz3OJYmZ4zMpTP8iPqG_BwsnVEsH6tqrKMCqLjOCoEtG7BgMR4VI1LTG0fihPQq77V1YxJqH2fEik8OgJKdwk4yjsGiaa54de8olmSPYB7_0t4MpsmrFighvdHY0Bk2dsLnEqCacg3W_yPe4f1bnq4O2vq2nYXOdDvGWKcWQY--G-YtblG1O8V07pcgMTGiPP_Ejd1kfLBv03zsGosPrKUKGyu3KGQhCXj6Nr78CUQC64FZNYMQF_FOCbgVUpUOnjWV9eHOsZ-KrpaL94ZeOUlpO8C2KohgSzISV-iCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=EdPXX1oNSQqY_Zepni_6iFUhTGeNUpyBiiCKy7A1ebr58gI-WJMpLZ9_RXBmrNxQ8FuotV3HSFIV0yqxNEcZybmHrPeB63cjZ5MGXs3lw_StTZX6Ea29WnaL17WO-vHNBY-JZhwmvHBfMCq-S2xW-FfxSlng4q6PifbXN5cXLAlJwYnBTzqbnpHg2m9e6u-UG-Q5xiQ7ZkeDf5Q4jdWXrKqe_ojsQRcir4aAEMExS30vO_UXdh-1um52XFuXKA6Ae170yOBbztv3Lh_HubBfjKDCr7DgZt73oJeKwpLNOPHPpnlpm9NVk7PfTyp-t_eudmpApIXRAwWarmb23opiTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=EdPXX1oNSQqY_Zepni_6iFUhTGeNUpyBiiCKy7A1ebr58gI-WJMpLZ9_RXBmrNxQ8FuotV3HSFIV0yqxNEcZybmHrPeB63cjZ5MGXs3lw_StTZX6Ea29WnaL17WO-vHNBY-JZhwmvHBfMCq-S2xW-FfxSlng4q6PifbXN5cXLAlJwYnBTzqbnpHg2m9e6u-UG-Q5xiQ7ZkeDf5Q4jdWXrKqe_ojsQRcir4aAEMExS30vO_UXdh-1um52XFuXKA6Ae170yOBbztv3Lh_HubBfjKDCr7DgZt73oJeKwpLNOPHPpnlpm9NVk7PfTyp-t_eudmpApIXRAwWarmb23opiTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bb2yC6wRyUs8ErJaRY43jecSbOe0Ui8PO0pKcSBJnx11k8uoxGNfohVyo1B5lTgpmwmJ1e8cRHm76wvLUhAFYa47wmMgl_KiZ98GjlD4ls1pM9hBfuct7URXQWmZV5Wtkf79WOUGEzZHxR6HV1tHCB5htvXVeO1hfmXVrf1C6kRPyK8rgqB704bkhb4feop7A5Zn0W_6gZDftthWs3V4moyrQrhgOsHqJ5ANVRnQL-KoFVAePUwghy34eoqo-exfp1X-YXTxrdLi2ZI-WaTBSkmLHEe6roltiD4E0csfEoOPSkDBUJav9aDExMyNrfpta-VRWIr7uZu-b6WFvKRLMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Aof0RwoT9Qlq3W1hIBgjaMJ05y8qEznKTo_udxP-Gg0WaY6gqQeD3rUXCkjX_E0c0tc1J_NTnan-Gw1m2g4l8xJr_w69fw34Xk4wbIk0lS4_QPLyMkkYcdMhqjC6XxwSwKv6PY4hohF3VXjjj8G-R77oZnB8kX4PI096FyWwcojnLSoM15yN_phgzsYLoZd_FEOU-BhFmPA4561VB0wK34napblLhoF8aQlJyJA_7kWDjBZQNQAuYGgeMNhIefZhsk1Gg0b9d8deTJAllXBc2yIzqgWQwb7zqIxByoshvQeq0rj8ziiqoo-zHLNBER7H3nVZjUJ-O-srbWlQhECv0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mqQrEm_eRDH2EjhG18MkbRTwnHyX17Ve3dwUmjaW2CPc92K5fUYrXk2IoJDIuROIwsrdr5LvihgpRWveoknEyyS4iERepKzZAYimwQLOpidDJfPr2Q64Tj1T4kPL24PNvUT4IvlIdqym_o1i4PM1OdeGdcR4n8XyG-N4O4YXTf-BEX2K3MTlK017nRgQ8k8xb7K0ZY7UxnZthj2vvqtGUl7Kt2b3aX3vpUp41fYPl2JbEvgWM6SLJzQv_Ws2Gax7AFWrOemmeaagtQAM6eXAj9_TP6oeD0FO1PZp3Qkrwpr2uK5Vz5JmCZ2983qAmZplt8keUHgOOR8BqyyBnOKYxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛
رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/persiana_Soccer/22050" target="_blank">📅 12:15 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22049">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y6Uw_0rOT5imKacu34w6UBK38HHSjPn2nCvEh1HXUoBVaxbjGM9bXJOYvS-gRPE3IZ9KlL3UuwkwySncMo8ZSZFx2T-bR0FkT_FrACpXVeARQ7SwzGQl_NN7_0u4pVNXKuB5j65YpOyQH5vXsf4EUTWOoZ56Q2Fw0ZJ43df3gFTBfI9ywwAwRnEDA4xQYF6kdBeSBFzbhzkpX082IFSgXYHWjZTfmIudw3XH7eDJUrg0LPqJYp_HtKjnHd-YkFBjxKvPbCtdowABaIenzgv3N4wyybeUyzHChXpkLYxPTcZjthJek25PGtsCHiEergWx-cXd-eWXQElu45hQUm7JlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyFv-ZaDLCnsCEanGlofzVNqmqrnLm1uVCmcYHt13x80qtW9S1Vh_AvQspop2z2SBB_9GIqFzaNQIVvhor-SfUP5iHJuLgsFeOoSzLrr23QO3Kdbk-pn2_2CIur-pys08mdmRgle4DE3b5khQUjONxlHzjqdy84zFCI6ZutUmvPjrF1nsVTs6J7u-FWhJWwdpAjZgspD3rOxaodlUKDSmdOte_fdBotYZrMd0P5CRPGn3sA1D2F5yT_dzAHePqBySk0p7xTUlZHxzQbzRU91brTiNTVWt3he7lwFx9iBFwW9UpPfyUg2rLes3b2tqYKmply0QjrHqTJnYRv5zjW4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9Jr98Xq58herRIFG-M9oOzGY1dQUPwxGMkjBLb5jK6ywZalzJWta4JCQxlFDjyflWXfGmvD-bqIlJP8Osjo9qxZOigYakydH2Qxq3VRhsPMk-b17D7rnCvhQyMgJLCDnFeJ83458JGMsCQtA4Df8kGwuDPrs8bbSJq3gIdKSmF2FPqJ__bi7M3QJpZhOnhb_KU_HSec5jJ1oY5TbES_DOGWuSOPGaCkChnvNaBF6zmDkNgQ1z03_oeXSSo7FSfqLbqDPo6FRia4dA3D1Zvg5zuaf2GsovOjH5GYw9_5qgXwCAMOo4hVc-0lKQeWQTtanNGjav9dtnRu5AuhURUUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sVooUIs0qfp0rdIllkoj6q26rlbsivkksR7iAm27ycsmu8pxqD7SLrTiw7yL5KPF2bBG_cniClHplIk2jXbsPxXnpXGnyi721OlpSKQs_TfyOfy-12WuooJFYTMQPZljQ_xTSmy4xSMkFG5uH99DP-3JV8FSrLq0W2zZnO_o3itU7MlXVcBZwPYA_OqFEGLK6Ta13x3mnF3-WCvF2oN-xTfUDGTIN8yhrWJhC1TEh3UyvtErV8uCwBfdppNaRyINFidzwAv0E7VgJuPZKq3WyhXNlgg9mY3ziYksWfSHNSRXZKBqXafHcSl12QbwmTXvLUWp8ex1vFPfzWZSZY0YVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=rJypChDronKk9jsJANrrg9eMzjWgmzhbGsj88ebwrwwxaGZzofD0_IZHsNiF1ZU4z2v0mX-BiJVvnDhqdlpsqmXkNaWe3CoBc52Ed5L6idioA1Or9n3V_yarzgYn_qbGdp7eUI43OHxlHtUFMpXvZs6o2QaP4hMTKivftJor_YcE02ZVL53DgdU1Z5GOBt6L1dP5SuEJhNbHbqtVFD9g5PLV4IKTvn69mCZtceyoLRsnQaLKCqhLZ1YJjExkr_qZ3uORo3fG2WsgA76KpiHCn1bnVJydqEuYN10ZhnCKSVH5RBXztF5SjPT2-hQFU1TqljNvsuqhLdI5aFfPsu0pAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=rJypChDronKk9jsJANrrg9eMzjWgmzhbGsj88ebwrwwxaGZzofD0_IZHsNiF1ZU4z2v0mX-BiJVvnDhqdlpsqmXkNaWe3CoBc52Ed5L6idioA1Or9n3V_yarzgYn_qbGdp7eUI43OHxlHtUFMpXvZs6o2QaP4hMTKivftJor_YcE02ZVL53DgdU1Z5GOBt6L1dP5SuEJhNbHbqtVFD9g5PLV4IKTvn69mCZtceyoLRsnQaLKCqhLZ1YJjExkr_qZ3uORo3fG2WsgA76KpiHCn1bnVJydqEuYN10ZhnCKSVH5RBXztF5SjPT2-hQFU1TqljNvsuqhLdI5aFfPsu0pAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=jqWNm_-KNXF8KYJDiubSm_8-RAEW5B1quM5q5kiCfIl7w364K_aPUovPpK-4v2RTaOlS08ZR2k7Z-j_AzJR67_RxkRfQvfvmzYDLyGtT0fBmkBWKIgDJRSGuQUAOLV4PzfXa-wIO7gOPq7oxyKp0yhJ9_HNV_8A84-wv-dQUAgAbtlKnrHqoflgiGlgQKORqQtDEUbI_u6Ynhpf2U8aSpt76jDf0EFg6anu40HL0my2sd_Xb4yLGekOeVaj4-6FATJoC5LXtiFe8Lg7-SbB4x-JRIXJm-x9AVUdOY_4nO_ThTSGXiRiPHAkStNyXExC2MbxeUxUwPrMRZE8m3rctTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=jqWNm_-KNXF8KYJDiubSm_8-RAEW5B1quM5q5kiCfIl7w364K_aPUovPpK-4v2RTaOlS08ZR2k7Z-j_AzJR67_RxkRfQvfvmzYDLyGtT0fBmkBWKIgDJRSGuQUAOLV4PzfXa-wIO7gOPq7oxyKp0yhJ9_HNV_8A84-wv-dQUAgAbtlKnrHqoflgiGlgQKORqQtDEUbI_u6Ynhpf2U8aSpt76jDf0EFg6anu40HL0my2sd_Xb4yLGekOeVaj4-6FATJoC5LXtiFe8Lg7-SbB4x-JRIXJm-x9AVUdOY_4nO_ThTSGXiRiPHAkStNyXExC2MbxeUxUwPrMRZE8m3rctTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hIy5ROqHVepxM1yPVrSoGDSGZWHQ8ETzAd3Xv4c0syisPoh7RfprIXOFB8D7-I90wbiyJ7bdhoEV7wFeO4VSIyF9ULAv3INuXUIQuy_jAl4Lc9UQFJr4s004UPnF_pHq2ATR3qjeoPaHQaieCxreE2xzAjj1OzKvNuBuDe5gv4nAK0urp7Er_WCn64VpYFGPyWxyl-NIbnvQSS962iMZJWbYTwnQOA-X8i1Z7Igo-PBHH_mNYLLDjDGlJBV1-fkS_K9bYZu3w56pKxbN-yoc_TGFR5oTXPaycZ2Ydh7RxW_0rWHzyYuavXmrKhJKv6POhUPEhYdAJB6XVlXg2OeEdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCV6S6RNfPwZuUVqijNqB9seFHRPhETPo-kvKoHEbPwO1cpEQP193iJfp8WnimfhGTzbIgRKtFuDLjKeTYELyFz38a5j9rXbKhjusIjM2eenqf8nPhCCSkjMiNlMbeq-xTpDgXCmpt-2CvNp2vGJVK7UnowdX3Q2UUjsEmgNuT0WtFXs5PnBuZjbb7PQ5OMj5pSi98aJ66mFdeSWP5FRsgcRFyyIqVDBhQDjWS824bOQEXkF9E2GuL0J-DH4YoYS-bg86QSAF9RW6bcmutVGJ8P59hAZcpP0jvqufEnE9SyK2HFsKnmBb5wOmrLw3VyDyBidT8vXn-EjJ0aiDjbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfZu65cBWBOMr41NO37P51ZebrmjygVtOhJ5gkS2kY6UsvBOx6NUURGblGZvj2iRWBW01q1bU1_KZuP6fAn1E44WCe9gZ3-3Jc_p27dveYM0sd7KHBbyiDnrd1Ax_dkfJGyjdtWt0AwKQoOsL1uChcgZgFras9YQo-qt3ZnbV1L-UJXxLz3leq6VR_7R0Fat7hr2R48KRy4jdsLHgYrnT7sZfUR1wYyLWHli5yLuTVHkdhkUfT2lf0odb8c3QUetDbg4GODr9OnfIxhB3EtBGC3nJ53mZaDcxEYDLcJ0AAOWSvWKkYeRF6N4hivWfbxSrNmSmujUYal5JJ1cSYLTfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r6cquC6u2nH1jH2j48LRYfkHP2F9UHzyNpbGKdYnRLxocueCnwvMMLo20lYrNPhKYd96gzwrCIyQ5P8UmX7b_p6ZRJl8F4T9znVD942uztL3Hr-qCRoTXFd3vhFvYBICu3EHQ__uCGMGQzX4S_djumr-cbxhf_aYxJbbJqFN3oEpeX5iF8k5ewoCE1jd-11fmSKoVlU470GVg3J0vwisG7erjUiqD9EP_RRZEjpz_8pLAK5_ROZpZAg2LbaF3KBFEYRO20yRIEMvhnEKXJ2twmEEj-KY7HHQJZOsfyhxMfXgbg4AZWPl_0uzt3Jq0G1phcnwP7I2PsXHimqbQ_PY5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JytOSiBR9aCbdWkyBndZn8uevqd0j0Z4t6_Sst0oC1tEtt8exh7oASf-k09w6UwG7rwsXan1Z7URaJ37SGQDRQl2bhj-eltC7cEkWYiWjqTjVHnHpgRqskDGXyfTBSSLDpnDIoUFev47H5Kf2rOsEK9tVxxYrjlWpZnQ_MCyf_UaBMtHWEqQtmVLYauXA57iyt_KM7siwoStRuYkJH6aE2mfu9KB9yXmpehnINV0pEO9cgdcQLH-Hb31nEb3p3NljDZ5HjcFe7BsIlvIdJw8H_wP1PyrLnEcNlw_WJW2SzFoU710K6euRtekOeIwOguYDK7SsX0cNmjEXO6O6zlotg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRuGcen3QP55GtRXrpASEdWSXkewBTALEWoOtzbpWTUNRecshSbLA2dqtJVTWegjLQLXNCRMt-Lvyt0sn2lF1W6LbjfKG-8NwtrxcKCrn9zJrQM5_aHtKQ8_0cCwFNrkMnkJcMppdkHZvThtEPxUzKN0THM5KXuRFfsN6YTa_khqCLWvxNi8KdXtglx261el2GkL6QIZiQ-5FjrPKkW20Iv70dRwL-PwZmmlGY7lEmZB_HNdrW5alpOPFcrGezs5YuqS54CbKrVxjc-1Ti8gZATv2EpZ5toDdQb4vy6lvz_6PPfCNqTnZCfN43DFDjfzVqfM_EsSGbdzlN0geZvh_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=lgYrtSOF4i7vvjTcNFoCbM20PzJJd7VROEmUC_Rtqnl6qkmb-Rj3GqONYW5GiqIDlbstfCwxwW1r-Kr8wXUiIxtPdymUbkPK16-HdK31GxjEwZ8M1LtnOlVD4teO1wnMGQXZZ36jPoTYbvdq_AIkXx6_DdHfwu8ywPdVb6B88yKKovWvbAlNzXVkptNeIBPpG6brqXh_6NGZfxktMcTH5x9MrsTf5WANJ8BnTfiyqOG3AAwOkzCQYbFCcD-aR1AzqPh-nSAzXNiDbLyRVsrXSZE6wX-c2tgEJTCa0IyL9zYZyC9D8H8kWp3bsA9z-qEqcn5RdprlIxLZGFSIP-w8mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=lgYrtSOF4i7vvjTcNFoCbM20PzJJd7VROEmUC_Rtqnl6qkmb-Rj3GqONYW5GiqIDlbstfCwxwW1r-Kr8wXUiIxtPdymUbkPK16-HdK31GxjEwZ8M1LtnOlVD4teO1wnMGQXZZ36jPoTYbvdq_AIkXx6_DdHfwu8ywPdVb6B88yKKovWvbAlNzXVkptNeIBPpG6brqXh_6NGZfxktMcTH5x9MrsTf5WANJ8BnTfiyqOG3AAwOkzCQYbFCcD-aR1AzqPh-nSAzXNiDbLyRVsrXSZE6wX-c2tgEJTCa0IyL9zYZyC9D8H8kWp3bsA9z-qEqcn5RdprlIxLZGFSIP-w8mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzfRwMsPIbwneX3uBziEtQ8xG4yD_DFOpoE4OzOPRSE1eoK9CVgPEC4baMc_ph3LwPxdPcs13USXtGw3vSyTqT0kNv59St6Mupg1F-CUHGXx0fiU8BjFLGtFFNDgsUIKtAQHh5LiNMdjSiunr_85hsqzSeW-A5lE7oGmSAZEvZKpNPH0ZuWFETNaWniBksb6onXZ07K8019g0JIJABucAH2Y3dH9LGqYH04zaLDlAw3feM6LrcjbOW8nFA3mGDrIGyyCzpdk7rOzLlVsRUVL6y5T_LJfWkhy_WeSiLSmpGNT2nTQ12DGLSvNycuRghNE2v0ZVuuZ3sKgv2Wr77SyJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتیجه‌دو مسابقه امشب ¼نهایی لیگ‌قهرمانان
🇩🇪
بایرن‌مونیخ
2️⃣
-
1️⃣
رئال‌مادرید
🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
آرسنال
1️⃣
-
0️⃣
اسپورتینگ لیسبون
🇵🇹
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aHAyoWAkgyOd-WTgDWOJ-3aYUq7e_gFVs1lMnPZ3kaECbyOtjR4SR291sJfNYgzjkGfBZ-78cFcaOM0ROxQFlbaebv7Syc5733gwyZ_wjMei10j1D4hteAeACLJ6XqIhuz1FP7KI7_nyUICOPHX48mwHhlDE7wFbG5mVRQfiW_TL8cL58KGAUCCWqfHFmspgGITAWQWVUSHO_6Ibxpgv4rSwFsd9rr-8EAGGasFuKwaoRSdNlKHydxk5481RRIAwh7GZl5A2gOueWIAlulZ7hbBBGAWOvF1xzaOPPrLH-kdzrmRqq9oyWmj2tF-rWOx4D0L6_8eXHjO6qc1Yuljy_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g61MEUGC-Ox-WH3z-CRJSF8FtsL7ZmjOlETsElOV8AUNCS0k1ABvDqjhnj_r7Z69jroEUE-9Wn-Btg_qnGDzUBfwwbUFuOIw0jwQeRs85vgTN3xr79c13Y_Ic04gYSToDX3ZbYYTq4UYwt3XCl769PHF70cpY5_8-8PMlYp9nlCLI-JLwpVy9rUYJ4fHdeLPBBNasmgfLG7aSgUxRa_CoSvR13sSYBYTtYC5aq_SjKRz_cTpz6Zldr6dUg_vC7MU0Vps7x0XPN7yuIdBblroJtnaLmNKgrk_VdceInkNsRyf8iRySlmKq63U_pUH3Vqc_SZnkZpkGNMEhq5Zvzha3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a75lqitXXneTOlh6w71vhZLQhEKqbXz4Ll1ftkh0PNn4bwnq0wvGNelK5lOw9Q43_soy1ltj4UxzaS0hE9UtwL1sakAqC_0XL_ewp89zN4a77XAW3Qk-PZSCkHdp1Fhc160Mv81A3-2ZfQbqT7QZjp-xZJTXeb9v3wSnu6lVeOsw1sztNi8jkdVkfqg8AxFr9pd_Fd3F_-UlAhluiPYtZX0S_FV_mYL3Ryjol-94A9K2leOyrBeP93uta2bks41dHrGWvWsi_aXwpXqQ7l80ed-93DQx9yWVXquSFkOwGGGCYrMx7D2C_kdTk3pi3jKECcVYuC_vzvcBoW50h_yf9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6ghztbnLYnFCGDBSVurSPbyb_dCWBbqeE2scZRNzkd61OWNrrBn_41SLMVji__Z3vv0L0SakP8EKPa5vLswRBFQ9LXy00DYT8Bkc-j-xmAicdTfJo9dFshPEg5oLwd6GuG7uBSBAg6XHqSELDI8uPATDRPiZGyPS79I7TLvczIFSlG1FgsW1BSB2Wtg_Qm92GWffLSh7JMXIIjV50iBd8QqD_G_Ctb1Y7LbqNax3HGMjYubl4T1j6eRfVLudMAo3VZFpgVV_ycmo8hoYuBR6sMVsyf0bsy6IDNQxl8JZ2WkQiulhPRwRtTNazjlSpUQrPFzPCqPskOUabBBBnbB1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rgdnD6RCdWc9NuDYg27NP6lw-bTSq_DGWG9oMFIdWavjScDPB4O71vN5bSTtQ9nndyKgvBkGOar3uHRpy7Szk73pgBbKz5IYXZ8AF6QJznFokOMZMc-ACiJs-H6H_STDY7aldGEvFOYTPXTzSOESp0g2vTVn9ozrhzaBG7joBaLUlMKsHM-IATTH32Dn3my2urvprp8AfS_lpJpvUIbVcc1H3olvQiaGGdDBHNeRIw4FD0sZLVxChWFz77QdRK7pPyFoZGXCkBLMtOX27uwhYQFdzk7l5kjy2P5nGQqeuQLgM7TJKe3mXanAY4kKx6cUFn1fDNu3FWc2lZ8RhIWbIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
