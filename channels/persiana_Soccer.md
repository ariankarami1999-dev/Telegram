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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-25 18:30:12</div>
<hr>

<div class="tg-post" id="msg-22141">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DqP8iIQnxTTOT25mIf5zQacLD8XvYu8HuwF-cHeN8IK0sPAk2qVGPV5ncoDUQvBTkqjWYq5iIKRx4rUDbgqMo6IREGOUMh8krVtC757WwGTRNPO-VJs19uPYqoY-BcH2UqEv3QImFp0-M_fIKqqADJP9qlWTVyeGCLlGx9vOMDEiPaT6GnXcmB1eetNX0Fy9fre0U0fabceR8cXgXBCt8qDE6YN887tuLTDrlA8RcVizl8kSiH9ELXpLmGvB3plS30SCUOXz5vTSsz0ICBQFKApXGZidcVFPti9WO3k1dEF8EvIaHSrNMnzh7wO0eCgmrBeagOsLAXI25xpsg-RPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/persiana_Soccer/22141" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22140">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqgN5LOZD2Hvdzefze-K98Xw7NAEgWEMQ8VVk2KWOpkFuhGEZml1u6tmF61Hmt1LEu1FOtJEWO08BhbFpfqJKQ9mxtx0_dwQAcHyDqJwl2VHXzpysjdGqCiquvsOwbsv3z892Iy5No64pQjH1OG6YEDyBS727R6beTKja3cYzFDIydfbTYjG7n9niWEw2jKpi37qWIgq0_EAqL5zSN_3XijXXje6F2bTALu9l7tXQ2-w_UQSpwa6El04Buif_rFz_YTwmeIbsY3vR_WmPyJqXOhQeKnwURBSBZoEs-ng_0NWeylOZivw9m_njhCl8_h_r8c2mCb813jCB7IEWSV9WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدیدترین رنکینگ بندی جایزه توپ طلا فوتبال جهان در سال 2026 بعد از حذف بایرن در UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/persiana_Soccer/22140" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22139">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/persiana_Soccer/22139" target="_blank">📅 16:58 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22138">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7rOnYaNqSM3-x-3e4Mi-FHsiG0ewKdbh7iHfgsbP7nDYtG2RhiSWXk1qi2QOj95ItR1aog1403wlag_eMNJoNeXdoYyEbl7yw2_qP_PNiWtp1GnGQFcLMA_xDybJ0GYs81t2a4LUrwDgpVbRvXZQJymnQFDzxdaRVKdUU01BHqtu5QXg3nziR9sET82hb1ikAkMJiPNcQJ5wv6trZZIsfV_D8obE5qVVwodvzKCW9nXCy9qqPt6CugdCUn-OG6C6n_p4apj6MawAxit7QmX4Xx6qsRFsAsY25lIi0qfnYmP7SpBP0jqrwEsdepn4StGSpw7jkTzTK3MH7chi6NuuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
ادعای رسانه الریاضیه عربستان: درصورت عقد قرارداد رسمی ژوزه مورینیو با تیم رئال مادرید احتمال به‌سرگرفتن مذاکرات با کریس رونالدو برای بازگشت به جمع کهکشانی‌ها مادرید وجود دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/persiana_Soccer/22138" target="_blank">📅 10:56 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22137">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r2OFps6B_wLFSCKY_EuviK-9fzFwjRXwTAkVY7xG8XA841s33zJDj6dfUuu13CRQ8WtS4ZfDWzYcpAbcZdbe3G9ONxJlkt5Uqq0dQiXKvC2dd-W8DTrXEgqyKTmeJEE8vLvguSCZPCtljyXW9yiz4a_q7CzHZWJaqW5IkFVHHCtYiiSETGo8z1cQVk2k643fKMeT6oV9G8E6OpWaRxWq9iBTh1NBXbIjW9H8ivuS53EZxtlvkb1EayiY4MtfOJgCV8V2962helMatPHUkmsLSe5DQgAr4YQqHD_wbHu7Qp0W3IxsQk00dzhG7eAbt90Rkbut0jefhhh2zv70EdC93g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
⚽️
اسپورت ‌کاتالونیا: هانسی فلیک سرمربی باشگاه بارسلونا درپایان فصل جاری قراردادی جدید با این تیم امضا خواهد کرد که به موجب آن تا پایان ماه ژوئن سال 2027 به آبی‌و‌اناری‌ها متعهد خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.87K · <a href="https://t.me/persiana_Soccer/22137" target="_blank">📅 01:02 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22136">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMKLV5drrJ7CbxX41gc-SYdLjGiY-UQlaPghJA8QtVTTYBkywbPVT2dn0HQMP7hyLK5IqTRpn9CtDoIICa4kDZB3awe_pkFzSYSLyb8_3G_u2gNHEOhg21FZrrt7QuK_UP_2vpDOPq2UlC7tV7GO4nxXPmxuGO2j8-tDbxAV0X8EvDu6Y-IftNaXqKodxukeQdha3Sw1sTSiloOTLmtDtljEQdiUtn5uxtnCd1wb7w1jGrYhW_JmgkMKDOBzG_NnG3q_Hn0XjjQuWfAlZq-SgxHRuc8qfypinxw6wa5BLhSCGQS2bYUN8gLQrahyDrqqcsa_RNSSCSpiu_B4JNUmHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بازیکنان رکورددار بیشترین تعداد قهرمانی درپنج لیگ معتبر اروپا؛ رابرت لواندوفسکی در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/persiana_Soccer/22136" target="_blank">📅 00:37 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22135">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nzjIFUHcTm7S4qWa9hLQF5QSqLmNCTCkfXQ_8jvs2dOTyZAkPg5J2FIH2I57IQOpgPQspD2mID-_HdD-lP3E79m-8wvJfwkMPWaUieAor-86YfGMR6uxjlFF2PEh7D165efizbeEW0eus9kgs0xxWbAadmADXGp2EhzzOGKO61bJLdNWREMwjr0VqWpUCZIQBezXk2ZqX6RUGd-IOl48WDNcK8lkAwI_cvUZyb-FlhqX43P3rfipWLProsLB06lJ6z9pUhJB-YQCFgQPq0vhSzr0seL95SH3r20fdbIlwgaG11qqWNP7xMOZoXPhe-teFc9hzSK-2prKOsTxZ8DsEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.64K · <a href="https://t.me/persiana_Soccer/22135" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22134">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/persiana_Soccer/22134" target="_blank">📅 00:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22133">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o7RDxvC66dKTQ1Wt0sAqwCXiWg2IFf7ZfjtbX6nKBWY1BeXjF_XiILB_nTK6_6zEIaWeTyiktX2r_e6YXd3uraB2tVIqFjnn_wb9zxMJs9Fd3vPDmArdMwIksTsYeKD_h2RssTC8KngsoIR9KmyNIfiO00blpMR4tpSvIgiUSS1SnD9TByiOWC6amZWz8X56INa_S54uEwKSywwxkzMc2K8Ppzq8JM5Apj9x4QC29lhATffFQj-uOICFsOxBq5Qi5T0ZrrlOoUy0czBpF2gndjMDbvJw-mArufTfCdNZvHU44JK9GjkQZPEyJbsHBdbMBvmbPu0HFzvLm4xRy4MgIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.04K · <a href="https://t.me/persiana_Soccer/22133" target="_blank">📅 19:00 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22132">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=j9JF5OJ9OioaMfk2PT2sYWcFuS-gdW1aaoBB5xA_DJmnkx3PGkV2C4uk5Udo0XULrpgJAFiuj5UAQQXb36XV8k5nbJdsIrCt2QbcUsSHA5UPvfmpiP7f1cERXfzAVenb_DFD5XE_tSjDHhKMzQdBVXkbWTm9K7ibhU2CfzI7S-EynqKLJI7QVB-rTvYwy2sYooOjif-gp1uU-nTDfK1JRbYYwzx3LpJjrwkE2j-KbnRvAsylWWUKPq1PnqIl2nqPj3u3I30-jkWR2O3fIgWiAq8J0iXMUZ88-LmOvZaNQPFcBk4VLgv6y3n0FoFtOStmPGveXbA07EuDl98uVl-laQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dbf7d2bbf.mp4?token=j9JF5OJ9OioaMfk2PT2sYWcFuS-gdW1aaoBB5xA_DJmnkx3PGkV2C4uk5Udo0XULrpgJAFiuj5UAQQXb36XV8k5nbJdsIrCt2QbcUsSHA5UPvfmpiP7f1cERXfzAVenb_DFD5XE_tSjDHhKMzQdBVXkbWTm9K7ibhU2CfzI7S-EynqKLJI7QVB-rTvYwy2sYooOjif-gp1uU-nTDfK1JRbYYwzx3LpJjrwkE2j-KbnRvAsylWWUKPq1PnqIl2nqPj3u3I30-jkWR2O3fIgWiAq8J0iXMUZ88-LmOvZaNQPFcBk4VLgv6y3n0FoFtOStmPGveXbA07EuDl98uVl-laQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
👤
در شب درخشان لیونل مسی؛
پیروزی پرگل و ارزش مند اینترمیامی برابر سینسیناتی
اینترمیامی درشبی‌که‌مهمان‌سینسیناتی بود توانست با نتیجه 5-3 به پیروزی برسد. لیونل مسی در این دیدار موفق شد دو گل و 1 پاس گل به ثبت رساند تا نقش اول پیروزی تیمش باشد. با این عملکرد لیونل مسی به آمار 11 گل و 4 پاس‌گل در12 مسابقه فصل جدید ام ال اس رسید تا صدرنشین جدول اثرگذاری لیگ باشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/persiana_Soccer/22132" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22131">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🚨
⭕️
رفقا با علیرضا صحبت کردم هر گیگ کافینگ رو ۲۱۰ میده
با لینک ساب بدون ضریب
اینم ایدیش برید هر چند گیگ لازم دارید ازش بخرید پایین ترین قیمت تلگرام میده
👇
@Alireza_mosve</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/persiana_Soccer/22131" target="_blank">📅 18:57 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22129">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gk70_6mFQl9Ox_2mb6XWNNY5xHA_MIyyBKqh321oIBID4uEjyOIEA2OcPXj943ami30L7j7cehiTUsIgvlLobU6gdIzCljRYPXu7nlcV4SWTyj9s7okliXkM0y95t1ltNMBckuLmOFHhN1KQbiZWv-AA-x85BFpeyXt90ftBhk-qycfGzoyt3v803MtsUWUagIXEurlgIrNEroQQGsZPgii_0TdNHJLr5EOPlL1CsAdS7UKkU7FB6Csz3Bgbq8s9U45-j8ESrd5AzwRPnbX3yHm1r0H2t2sJCjurHPW8xEihxQX0-53Lqb8Ul8wFhxDlf_h3lvqjZn8iXaT5PMQ2-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👑
معین خواننده دوست‌داشتنی‌ومحبوب‌ایران اصلا قرار نیست آهنگ تیم جمهوری‌اسلامی در جام جهانی رو بخونه. خاک‌ عالم برسر مهدی تاج که دیشب دروغ به این بزرگی رو در مصاحبه‌ای اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22129" target="_blank">📅 08:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22128">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ueFpvvFy0UB_WwzA4rQNEWdhh8gtmWStcjgzxhHqksXtWZSv_5SQxiaTwXbKChaLPqvR_NBWyzqJOb7_qrQMWsrn1Y2Gx_7hC7eAdbtDrgiu9lETLGUapz_fFkVfkNUI8wAhx_FI8uLRGHUwYvMk2pkpyzrZrzDlkbQY03eA8XJvFQNoP2XZly9c2UgZQRw73bZIaMpIcJVwT1JXa7MVOVokfo56nkKUYnwSk778nE2zMEt6v7wcUxRj8GUmjVFIzE0FCdzNHQtO6QYaXv8XYUsRbIpCmkYHFyMGGczpqRAU2hYXWYheAcX9ZRC6sUy0W1_h8m8dKl6Z0_FqSt5yrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22128" target="_blank">📅 08:17 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22127">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CA_tYi-DEabbG93JhXAK4E8gft69M4Oc7yF64hvRPZxRi4BQrH5rYLwcfr1ZrBEPNEe-cVYTX11ffoYWp4ItGTyUGNW_utUPxkc1-R4ztzsUqcKHkFPwwo6jUOfpHu2BITDNrMfgNFbzbqDqi0SFZOOUrPf4LQkckTO-zZBWviQtRK1hLOs2Y-Cnz7SUEjhNNqFQZQuxum7JRNtZN8djJU2aAeInjV1ZbTT5R5tZifORjypqAkhc2qvfoL-cFPCXp7JuycIAwwc6m-b0ueRlSASaRQffk5nTYcp_93qwCWxIVP0_R_7SnHVdSe1_GLXlVFiWGZOoh5XF764Qq2XvXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا؛ مدیریت باشگاه پرسپولیس قصد داره قرارداد علی علیپور رو تا قبل از اتمام نیم‌فصل به‌مدت دو فصل دیگر تمدید کنه و صحبت‌هایی با‌مدیربرنامه‌های‌او نیز داشته. قرارداد فعلی علیپور تا پایان فصل اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22127" target="_blank">📅 07:25 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22126">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uvMwPm-QRXgeiA44VhXcmxu4vQJCatpqA4HTVNlW72uFHDbp6J6DWT2VmeEIJ1PT7-2pmf4VWnQUfqKRMgKYDzrmZjaQ04FIvNy7Af7D-eS3spur06vgKp_hKzGfj8JV5W-HlBH6dX6YMnkHoBDLeToYZPKHToxXKWLCc6Uk94PrsEyT8pofYQisQOhAyUQ_cJlC65QLxAQV7jepUkK_YaAX6MO14dIA5id534sBJ7fI8Gfn7SMQl6YzNWHVmXgxccLuRy-ACKR6qiheYhgI7Cny2h0A0_0LxTqXg3gxEW1992qQp2OUASVReB1HnaGQdlR6zbykGqPAWG9XnCbOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/persiana_Soccer/22126" target="_blank">📅 19:13 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22125">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BO8XcOtst7VVpY8r0O9dtEIHmkL0qzEwnhiBxtvpJYbMcPC42Uo-4j5h43fledWMl7UunckA5nLJpxdgnamBLs7zymmgeUISupfevebD0gtld6AaC6nTyLpaE_M6uvul-O2eYDhtb4Z8ppLrzs4qEUUWxo8Up1ijWuMTFLIqqs4DkvVtG-4U9AmXitTLAk8U7g5ez0Kf67OOknk1Y3IedK7KVBeSWD5wzJRIu1CO9Lgs1VFeXUVTK7e_-dz9de78M516mqMTL32VAhO9wMw50dWIaKocNAZzevShds4ZlrxoxQeqB_gERAfedOUzCx97bOOp3gLKngBNjAUofJgQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
پوستری که باشگاه رئال مادرید به زودی از ژوزه مورینیو سرمربی جدید خود منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/persiana_Soccer/22125" target="_blank">📅 11:42 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22124">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ORGSskuYyOPVS0-TgRAEc2s-AGWcefXloFZgUf_2RPpm-5KIlW-65yZ1dqjfg7z2kkH17QaVNN9o3Dhg5RaAy7OJ10yNm4tvpp1C_2U3-HIcuycbj_mHuQZ1bIKT5cd_clD9X8PEYpunQVHfTH2BagB26V7FkqtWi9jFP6yCWDyjGGmsplsZ0nTNGElPIn4xlv_PbS_ymdwyXaBMiEhFg3kvNORDYFUneTFU7Nk844GIXecqXWcrMdVEquOp2rgBrinyEot4l4HlgsVMyaocj3zV0xEo_YisZLeLSpEb94G4t7IMZVd78YYYw8bpdmKF3JLV7CwOUueQKnfu4QlQMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛نماینده‌میلاد محمدی امروزعصر به مدیران باشگاه پرسپولیس اعلام کرده که مدافع ملی پوش سرخپوشان دو افر از سوپر لیگ یونان دریافت کرده اما الویتش تمدید قرارداد با سرخپوشان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22124" target="_blank">📅 11:36 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22123">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAfzjtqSTUcwSwvrFD1VIyVc3DhYSc2BnEKrgKRKv9klvpm08xHMO4kiKoedTe-y5eRoX8e0jyMnmvYO9zQFbSVV4srveDSTJqdu8XyScFgJk5VoVYZ8UY_sNC-lJ5pH_Pi3-2TTFnN4FNRhcZGNdV5eEhM2Uip0Wfzp6iN6QbTpx-CyzXiH5GRjMAnprbdXsvTrOWEGJrH2ICSyS4PwwyKMU7Jbr3S5tCkTmpxILLpTBDkTclZThIrWe2FOJufWx0CWRV2BUo8EkHO_DDJkB-4WxyPcoXEIb8bqDwA-QNCPxsmz-Jjfo-Uze4X9siYOARuU62JAQrwmvC9eFLlRwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
مسی درمورد وعده نامزدهای مدیریت بارسا: فرقی نمیکنه کی رئیس شه من بعنوان بازیکن دیگه به بارسا برنمیگردم و شرایط بدنیم کفاف نمیده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/22123" target="_blank">📅 22:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22122">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfSzq-2Q6YKC9WkECyfY5KMufuScUopC9Y9CjMac-XiNRrHoOdSbilgMkJ44fKtfnM37j0boSi0oUCxeyaEeGl2XqMa1lGSxyg3MGp-swxMzcjz2XlSC6XsIb1rFTqJSeRXa7nz7s2zHc7e4X8qPdMAjkwZarezCpNaI5XvrbaTI1ka6MW0FrEVAIg3X99t5bpKaTxPxb0Z90fPvainnsJ2d8SBk7kDsf4l2952APF-pXbujQmeUSNoLdCabAzIVclcGKjOBX_B3_ShYr03U9oU1VV3jBnYLWT3fMtlaqb767cqIbRbQ4GvtAxmS7xX_wEwdG0BETzk13YMH-7HcpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ بعداز تمدید قرارداد علی علیپور؛ میلاد محمدی دومین بازیکنی خواهد بود که بزودی قراردادش به مدت 1+1 فصل تمدید خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22122" target="_blank">📅 22:22 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22121">
<div class="tg-post-header">📌 پیام #81</div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22121" target="_blank">📅 22:18 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22118">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/goBBhfRMjsf5EStnP189oy0pHtTEh2ZCqVETT6DNnW9k_YP2-d0j0F1DzGdxkmBp1KyIPa6wGR0__uNHOp0Crt7dnauiyLFrMZBNM9o19MXzi9OtV_VKcrIe_2KnoEOrxcrz7uyF9RXTynq_6S0Kk9Kjr3D9vMzLAp3eaNj9bF17m9HZQwIbJolHG3ty7HvAQA8nXVBkkkEOKyyr5i2dxFT4g4lLgLASd0VONJyMcWhzejVWusCgzSy71TXcpJyHnCsTbetecUA9r5DQ51y2bJRkMhTsieCcPNnyPk8z_Zfj0mHmSVAzh_LGt9lJZ7KUuqhioDjYr0TJ2u5IBMw_1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
طبق شنیده های رسانه پرشیانا؛ باشگاه تراکتور پیشنهادتمدیدقرارداد 3 ساله سالانه به ارزش حدود 85 میلیاردتومان به علاوه‌آپشن‌های مختلف به علیرضا بیرانوند دروازه‌بان‌ملی‌پوش خود داده است اما بیرو فعلا حاضر به تمدید قراردادش نشده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22118" target="_blank">📅 21:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22117">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI-aS9QoLWdmidC7uZgc1VribhUPHJfDQXmmRsCd_dan7hr-m8t8lE5jpW13z-d7e9dzgngZGCZl_8qOllGYwnXyNxDQDDQGAltbeFl5Ru-oVIijW-wOl2-K7oTUB0CU_jdWkOo_yrm6ThtGBahpfDyOQlUL0qnPMopBJYk3ZIILDJ63qZnDfnC4Jk9D2203sHJG5dNkBBDRu-C_PJoIEpcbZvfzJHjHaKj00mVk09qwUYr0qh3lsZnFXgQy_wZcSDfye9bwR2om16pgozizRrNEO6pfgwXK5nQIU-H7Xyj2liIYTcz9X-UoP3BJdv_OuDkhGRlgkwM6HrvmweoqZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22117" target="_blank">📅 19:59 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22116">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=C8nkZo2G4pHzayy6zUBYVCIl6WWVhqfntn1ZyUrriXw6M0UrS9WCb4wR9rNTvFdabR19-67XrkuArQYreNu-oPO0FIRHbqM8BuM5IOYWOHgGfno0CekZVZ0aJ-02a2PbdIMafn90tGnl9WuMnRdvNpExspxhtK0vpIt9_hmlG4rB_4AHK_ocbF63mq4LeEfXYxkP-tVq42uUfNqrcmnHJ0x5LUVqfhLZ2TG_K1En8-dZNyw39E4EJq1-b5qQJLhH8jCYrl66brkA_7tmPvgREud338sOa5HQ0lpSjZ4FvERnAMW8aFzIFowdTAeRCfKFjwQJtUba8XPXQiYW1pdepQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec34492de7.mp4?token=C8nkZo2G4pHzayy6zUBYVCIl6WWVhqfntn1ZyUrriXw6M0UrS9WCb4wR9rNTvFdabR19-67XrkuArQYreNu-oPO0FIRHbqM8BuM5IOYWOHgGfno0CekZVZ0aJ-02a2PbdIMafn90tGnl9WuMnRdvNpExspxhtK0vpIt9_hmlG4rB_4AHK_ocbF63mq4LeEfXYxkP-tVq42uUfNqrcmnHJ0x5LUVqfhLZ2TG_K1En8-dZNyw39E4EJq1-b5qQJLhH8jCYrl66brkA_7tmPvgREud338sOa5HQ0lpSjZ4FvERnAMW8aFzIFowdTAeRCfKFjwQJtUba8XPXQiYW1pdepQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رئیس کمیسیون فاوا و نایب‌ رئیس فدراسیون فاوای‌اتاق‌بازرگانی‌ایران:با بازگشت شرایط به روال عادی، اینترنت بین‌الملل قطعاً وصل خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22116" target="_blank">📅 19:45 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22115">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upI8cSriONBh34NdwZnyZSvqSgB7dvLEPYe7CSGhH1AjpfbgRu-zQIEEdluaPxFdGzxAbLUxq6hIk9CB6V6GoxMHOkHS0aU8GOlC8rPUZ1OvFwimnS0DyXklqlTUu2CBzAS5OlWnU-zKrqY_WEVw-p_acfnO8A-Kk-A3ONG6H8WK4klcIFxZMnLFnhlwYcBfMwYpMGQ4kpwEgMnjQaJsDZ07Hc1HpLozn00hFXCgGjbDLiHEHnRhiVnMaBrFzT8m2VOkKac6vk26l1MfrjMTndXXOpGellzXE0Z9w19qFdpv3rviQSdTdW1CMisPUN-bg0WUg0TFMrizNkXwpjslMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ یکی از اعضای هیات رئیسه فدراسیون فوتبال: تمام باشگاه‌های لیگ برتری با اتمام این فصل رقابت های لیگ برتر موافقت کرده اند و تنها باشگاه پرسپولیس مخالف اعلام پایان لیگ برتر و قهرمانی باشگاه استقلال تهران در این فصل است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22115" target="_blank">📅 19:08 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22114">
<div class="tg-post-header">📌 پیام #76</div>
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
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MjY_iB1N95n5FnTOI-dbNxBnan1MoHllayXWQ4CagFsN-Z-XoK2OKqRStQRNnkZP8u1OElfVfjd1e7au3k8QMPSWiVw4_USCbf26pW35PbiJXkruRuO36fJ2NGsvvc2ps8650xD79fukpQjo-nrWNHRvMVnoYvSZXxfALxKGkWRYWyZyi0U7GXJ2VvfOr9FCnIxBAzRWZ86My5iXUDCxq-1ODHrtLFZwg6hDtBmzOUgfB-SBWqmhNwbB-b9W3grppJefMXOi3ZeYOj2hj388GnZxx5WD3t__f80zGC3LwPLAu4TQMhOho2h1V8T4k7E9PtZw4nGzYWiToLECVMGEMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌رسانه‌پرشیانا از نزدیکان مارکو باکیچ؛
ستاره‌مونته‌نگرویی پرسپولیس از دو باشگاه اماراتی و قطری برای فصل آتی آفر دریافت کرده و درصورتیکه سرخ‌ها تمایلی برای تمدید قرارداد این بازیکن‌نداشته‌باشند او از این تیم جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22113" target="_blank">📅 15:49 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22112">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rusbEwlwyV5fAoCQNV00Of3qiAMUJ5L1GKwedPDLPFucaq2aFcwpks1RaHf2u9DyA17c_tyFqgFBAmnPQ1kFpVsSD45U9hBGjWNGtSA09_HilE5luPTjlbjDfWbhua2EGeuRN2_3g_qy8IlBVcGvXduAQovQ1ckYyOi8RnUDzEvHrbqtYYRboCZAu4S9xKlw5hUK0NqCa7PFIj5wDT9vxkqQrq49gZPz6-qW5MYgiL-ycXQ3R_iXJc_KYz964NIyvi4o9rgpfdz3QiVMWqog-heDAObxMgVKTtDAh0Qqd-nQRQFeVM9Wg3UE_yRwhNWlnzZjg7q8lpbXjKyV80Pl1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
لیست‌ ابتدایی تیم‌ ملی برزیل برای رقابت های جام‌جهانی با حضور نیمار فوق ستاره این‌کشور؛ ای دمتگرم پیرمرد ایتالیایی‌که نیمار رو دعوت‌کردی
😍
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22112" target="_blank">📅 15:43 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22111">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FHdJCGKTXXOTx2icsstEETZp6zE7BDl_dVfXelEFeC-w00X_FC8DQBaizZrnn3WtRxPsDAKu9u-SuFIoZxohQGY0UHFTHL6FMDLfJIrRlgUgqxodvW66Ti4yMKaZNY-xwZUDFCmiU_PhGXIwP_b4vN0qBjjlo-h6W1rL4uXi4qFsPvmz1npc--5_sqT2XN8U-nr8uURo8KyufiHvNawgJ35MR5hLBgFlN_fERtoQ50XrigsM_9imgnGcK3V6OQN5SEbhfrrhL3r7AHykHCEWZqwZWGrAvFnsBdmnOka1AgLlqg6uhMFVjVXz120Yw6Jre9t-XL1qhxMO_bIJprkABg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/persiana_Soccer/22111" target="_blank">📅 15:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22110">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HG4LcWFR9KSOyp32dxiQXzSEnaHH9UpNUAckbLKigP4w5TqyX73BfYTGfQVn2KZDQAMhLiq7NPVZg8DEpZtWLfLdpRcxiHT09krvTzPspwWN4PA6YR1tlzFyn8eIZHOOOKbeq91mDvvXrjzcz_LQQjki0CGIQTFajCWl2sfaWp0RT2Qkldj4HkMhLg-hmkwlN4M4Rnj4aQbBZGL6Xgms2FOEA2fEZa3JcMGLQpnIwG--YLgQgkBogYzHfJM_TmyUHNmG59dowvYYXauHa-Kwwenz5tv6qsqLk_8qJaCKaCmvjFihu4NF2iowakHtbNBU3yA2QoGCHeURqwo-YT1c9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
سرخیو راموس اسطوره باشگاه رئال مادرید سهام باشگاه بزرگ سویا اسپانیا رو خریداری کرد و رسما به عنوان مالک جدید این باشگاه انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22110" target="_blank">📅 15:35 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22109">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vw6JnK7AruH_WftKSVqNrLQJC3tSMaeSSrDAkoZSbcKTGNQVyFzQSdP2SANkchwC83fEgR_fqRxwBuxI4SbjH7bUpHWrDeddjlaggy9sSFxmLX1eqw-iDbImJ1DLWV1azWwugHpkldwxsgsOFFHPlkEI0h0udG9xHpbtC0GkPhQj8eVaILiRGb27XCOwC7HXpLbRnDGC4rLA6PiA3KZnZae6sustzJzdakFwDLo_hL3HyHCZDSqYenGN6Z1rNQy5IT08hiPoW0vYjocFPhP_OINhK5596nHDP9bseRvQ3Lpq0xJDCI3uFMxC7cT2WCbM-_4D_8pwUBp_m2m6to0uYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
یحیی گلمحمدی سرمربی باتجربه و سابق پرسپولیس برای فصل جدید رقابت‌ها از دو باشگاه عراقی پیشنهاد مالی سنگینی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22109" target="_blank">📅 11:54 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22108">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZjTSBJFrkpe04OO6b5wM_HVmB8z0WYK-A1_J8Nt-WUFoao8f9ECyFYb4T8tAOvpyHmmrqMoz1rcStG6eWKjE3dLDXC22vp0qWDReUdpIzi5u3aGrnvfRuLZYY7EdXTcvB7a6LSlE5ZrZxtr7Z7PVJrmYGYpnyKVeMqi7ghjBvV9J0C1Aoh4k9ZYUk23kqHSJPvxQi2n7lXbzsJ9P4heXtc3dFDx737xEZcP20_S9hS1UyPJ204VvjvGLGOmUTdhg1zLrSJ5-WzxxJt-kOrZnxeodr2QIDiJXVf5KisiHND08yEgG_RdqD3aZ-78WFViXouS9WsXx9JycoCpgeHD3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22108" target="_blank">📅 11:51 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22107">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hRgYMYlqTtl6Nl-_6mXr7E9zdt0k9QAb1e5miOSZqMg97lVfaW9Nhzhe1YHv3S9aQzJgPL_MQxv5b2hXXWnm6tlcoLKoSjPAgGMkymW_ZRYC2YCMCBPvEi3CWKLvgBnMORj4VdUZNnBrcqc3C9_Adda4vEHcNvn1eePst6Nx6W0Rc1hhzIcn51OSktxltCwvfz-UluNz4HyYhkLTQLLm7F4_OYwkFC7gCmZgw_cp9GvRqhjwCn42WlkI5FPpc0ks_wM8q-NOnNhs6eFulcY14Mnmpdv1h-El4mmzm4PU4WPvgH4n_jJFb08xOWgMvDBhJe10pkNtayz3Mhvj52JM0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
بااعلام‌رسانه‌های‌برزیلی؛کارلو آنجلوتی تصمیم نهایی خود را برای دعوت نیمار جونیور به تیم ملی گرفته و ستاره‌برزیلی سابق بارسلونا در جام جهانی حضور خواهد داشت و برای سلسائو بمیدان میرود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22107" target="_blank">📅 18:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22106">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntKwZsdVr3jzdi8L0JRtbAT7HNYrLkWQPCKT5oHiuBhxROtOR2Bv8oCKdOoe7PLEmWM-RAoH84KxAQhyqlEmw9EXL7JT3Hndvc4lS2p8negj9VdtUoTCCPMuKXxAxFSZp_4KAyBcPqgPrUV4Z84adbjFuN6xrWBFGwcZhcr-la65Igfppd-u39aL3IdM-M2PAmfQ-ptg5FFGQqj7N2LI9KEDXqOlfsNmJR3rteQSScEAW8suxmOVSKnnML2BFia2dr3l0ish8dhDYQ-7CtuifZ6glDKZ9D79ZXP24XSCBQE7MUj_d4P8Z_AVQv5taRzAUb4bcIRyqj0OIY_raUWIfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
رکوردداران بیشترین تعداد قهرمانی در رقابت‌ های تاریخ لالیگا؛ رئال مادرید همچنان در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22106" target="_blank">📅 16:06 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22105">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z_KvE9YVYi8rGdjkR7lCivXwW57-c96Ad9w94OQ4yGp41UpTdefQuKxqrcrNu2FYuVjw0YBqo6f1iO1qCmv4mZxyxfOg1PR2uLgQ0KyExpUhNbgIg89Q2lFdHsVzY6xmwY2qPzHA-CYpm2yWV0LVV1ypgd183393V1zchu6CL6mA1Xuap-QdK_Gl9hqrvFe32gpoTZ8uCB_pVC9SxZcr-8QXyqL6yW5XN6AYX2UHxRYEvz-7HJj4TqyLjHr9SdOvzqfs4BDjkspYVmdU97841yWAZhO7SJNNU7kf2g2h_WKu_ksE-22w_95-_JekVBHan0V2Kqbld-O9kQld0qTIcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
محسن‌خلیلی‌معاون‌ورزشی پرسپولیس: علی قلی‌زاده علاقه‌ای به بازگشت به لیگ برتر ایران نداره و قصد داره فوتبالش رو در اروپا ادامه بدهد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22105" target="_blank">📅 15:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22103">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CjlCv1-tc8tkXW7YIWsl12pHwlaTshKvaArAqs2zc9nfWFLsdXA-Pn85aXpfwjxgds0lDquNyneQ0M1tVOGGU14lAT92Lb0ElWtsVtpuI1UE6eAzcdok3HX5CO8buNFFc4ZSFGkDZiCmUlFhUblv3XPGLGyevZn1dkf84-L5S0CvKsOuFychkw8rtTAjaC12NTI4Sw39-2GEMlCa20HD6jD5PB0vlF6ekG96BJ2lsbusO2zn-PFEBkKUMaCpBMCGnnSCLHvVz4KENzsT4IHkat_P4Gv9pCEeHIWziBKyQsDn4m7C02VBZ0YdV4m8LdoKF7zYgx340ecs9ZRoAmsBUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آنتونیو گالیاردی، مربی جدید تیم ملی در گفتگو با گاتزتا دلو اسپورت: «یه چیزهست‌که هیچ‌کس باور نمی‌کنه، اما بازم‌میگم. دوستام میدونن که در زندگی دو آرزو داشتم: مربیگری ژاپن و مربیگری ایران. من میخواهم سال ها در ایران بمانم و مربیگری کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22103" target="_blank">📅 15:31 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22102">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpsPEfm9SlcqXiyxE1s_pVYrE8g2j1ESrbGjZ0gvJ5UT_hCKM4uTVCkTVgRbeTYvpwjRsVesyAZhdyhoi7a7-djqO_giACIkTsPQmrAmEDLaOLmsDayiIuY3EY1AhyYZOIVd0wH9hlNaD4gBCP7WJneLWHKddL60q3K94OyROQCfOAuIOfF1qcCzbgPmxA-fHAXiLIzZZGit3adqWLYWjPfLiCutTXOuk9efFPewjIq3Mxuvpl1dFfCeqKDfdtDp-EIXykQPPuC03h_kUNXim2JH-dZM_bFSAypROzIfiMK5LGMMYh-4DT6fCkFdXqt_fQrFhdST9Aqa8rQ_A2-lJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
#تکمیلی؛رسانه‌کوپه: مورینیو با رئال‌مادرید برای‌قراردادی‌سه‌ساله به توافق رسیده و پس از پایان فصل به‌صورت رسمی اعلام خواهد شد. پائولو دیبالا یکی از خرید های رئال مادرید خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22102" target="_blank">📅 15:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22101">
<div class="tg-post-header">📌 پیام #64</div>
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
<div class="tg-post-header">📌 پیام #63</div>
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
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hjSM7-J97kFHfId0B5grS6HEKDxkkdgbOn5XMP7Rlbo6Ky6M3ul2gcAIUkECSDpCpj3sFkFpV1XOewvXmby3-rDeH486-0uXeJnAOOiMTd9AEtLlT7Mq6m9BPGnNY2JV2ZJCItA7ESGvusyhngFOyZedvyF-1IOP-x5ZZwcuIXqlCWt13xaK_OvLR6satttA9xzT2qg4nqRQP0TSHnazzrt6hBFOQDTztRg31zYD833BOZOGxI_6N2CxTJtt3-8fjJyddIsq4vaX3JXJD1XNm8n-YO3fk-1QwqwNGQFw8u3WZwnAXmsr2KwKps_pcmGU6wiH0qsW6XT9wS0m3t6x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛طبق‌جدیدترین اخبار پرشیانا؛ مهدی تاج رئیس فدراسییون فوتبال امروز صبح در تماس با علی تاجرنیا رئیس هیات‌مدیره باشگاه استقلال اعلام کرده بزودی‌ازطریق سایت فدراسیون تیم استقلال رو به‌عنوان قهرمان این فصل رقابت‌های لیگ برتر معرفی خواهد کرد. چهارده‌باشگاه‌موافقت…</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/persiana_Soccer/22099" target="_blank">📅 12:57 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22098">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMYFgkd9EOnsBgAXyCZZn4B7QG0LXOeQfTWgN9EyX8ZGAgVnGSY-5HFS5-ZJsxOdb1TIXINxU6wjd8uUKK7B94acWg5QJONDCUcJyjCC3VK7HMpbuiFG-6GRtNUKtWha7R8I57nWh7dTBzWjti3lBiDmE0TJ2JHTBr4uyGeaqXAQQeFfpXLYYjhq3-9qO5u2x0XmRCGIwRfRBYrsjX42a60ABEDla-Q5lWj7e-gxFjRPe4BMOk9-wLFHovrrFmqyDr-L9-RWwlPVgGHlFv5mL4NSlV89dywTcEa2j6I4Ipu1YlARW7az7XAUJ5pw4XOy_7EBxLIuV7rmDUGpzhZ8XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روزنامه AS اسپانیا: به احتمال 99 درصد ژوزه مورینیو سرمربی رئال‌مادرید درفصل‌آتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22098" target="_blank">📅 12:33 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22097">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaMklYo7kkH5bAG-KfHngT4LQOQmvwRa1ez27ObWhmlurdeA-GFmFEcTmKkITejNGFR-4Mc2Pcp9e5ra9imhjNMqhNZetvVTTcAbHdzdhqYkTmEjOMs1Uv0h2AxSH531c2u9aJcWvhPBPr5qN5UDhXpDcTdpoU3TLMs7hkxE58EVQTZN-jxZXzuzVizwEaVpyzn0NsxRq1KGpSN490QVRJp0Z00P6jZgJF9_z7x2K4AP1EI1TUg8VatDr264OrDlxj78Ag07TkkGPQAG8pF6SM-ob3pJCIZyWHI0ZABVBqfGiJbcMCSVRYBLPayKA4ErbpQW9PauWLSazHxqCGMoUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بازیکنان رئال‌ که برای‌ ال کلاسیکو غایب خواهند بود: کیلیان‌امباپه،فده‌والورده،اردا گولر، فرلاند مندی، ادر میلیتائو، رودریگو، دنی کارواخال، دنی‌سبایوس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22097" target="_blank">📅 12:05 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22096">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDEse8NDrGR3BlgbdXe_awpd9pN6J8L3APC99hXAbGKaNb_9BLa438I7fWVxHJLWzPgieVkAV4N4nL-RAhUl4a9Hcl4KSy_MMHjYxC001KpkPqIIbis-FBzDiY0LazKxtlmoBRSEU8H9RM5c8yMirBj1GL_kymQ19kqJt_8xv5Yy1LvlNlQtI_INTAMEHvpv0sFNPfUlMXs13oVuDSpJpvT-t9wDxVWKu9gVu5QS2fH6GZ631G6i2p2z9gj_MAy0yizNbTzMWqAxV7BIByvqY3sEJBwy_NfvbaMWo6oTAi2smdxrqBVvq3sMaaMWemHcsnFIkqJbS_focz8V6cgLuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
طبق اعلام رسانه‌های آلمانی:
باشگاه چلسی مذاکرات رسمی‌خود را با ژابی‌آلونسو اسطوره باشگاه رئال مادرید آغاز کرده و قصد داره با سرمربی سابق کهکشانی‌ها قراردادی به مدت 5 سال امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22096" target="_blank">📅 11:52 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22095">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSNjqXlAvKJ4SobIuZfnfLwWVIG_iVmasuP4xFtbzbS7xxd14wfeSYaCgr8zR4o_lpHfupE9g0XuCJCreH7P9YxtrHtLbRqbtw8pCiPXjj0NrHYHSOHUjwp2c5TgRza1nR0DtBqw660zsOjIgHYtmWPrdihOUfwL_BdlbX6Zoh3oNVb_KYZwGazefTI9mkdl38HBlInosHyjx93VTnLJ3c_L-pFVFZ7ABMflalcYsScICU0UnhprbhGdvSVxhfFx8tI34mZ_KHEy3Ht04Sdgk7Vj0edoRznd1B2744JDbYztEPVAmRDReyg6bANdCB8ler9arC4_6hE7ETXS6sEVoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22095" target="_blank">📅 11:24 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22094">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzoRioWWE4LPzByPinHeO_LU8KuKbEio3slXY6obpFYrC_bGUNvZVMGs74WVwnNV8-UY_3OtAvshq_omiEUymDisYRqL4YCLBCC-dQmtVBLrnmq5CTIMWwvXaVudBLNgn0ZZ6Onfwn-nkE6H6hNgCvID6rNi0KFPzKs88W4whNhy4nOdqngBSxzNCN4y85mRwdMF17RB_vk8AFLbK-czlmkRQYxq74Ri8Goej_YBYEubo-cmzxXHA-qtkaZJUjTXCoQwW4PJEpSRA6AXjcWgswaEWtpHSXO_nZmhtezoMHf4FaaLY5lj0e9e1IlgOD0WTof3xfB9AsIEOQPMdOCpgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری؛ طبق شنیده‌های رسانه پرشیانا از مدیران سازمان لیگ‌وفدراسیون فوتبال؛ به احتمال بسیار زیاد رقابت‌های این فصل لیگ برتر بعد از جام جهانی برگزار نخواهد شد و باشگاه استقلال بعنوان قهرمان این فصل رقابت ها معرفی خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22094" target="_blank">📅 11:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22093">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rck029C05HIaBiKDv5Kluh1_pO-uv6lVjP7e0uY_qPmpmjxp-e7XxWucry3OvD6xttv6kZSlB8_cM8LFw8-DHeYfYRRF4EvUjsNbQS7b-EHBc-dBhgiGNQYe41dDqHZGD0dsr8iEiAQqH7jQKV5rdG8unJZ4A-Rq3dAL1htBElHYUCFxg4ntFo-a4gPH81UjWfvRtpzPf0roAwn2qUm9Ct2tYwnPrz1fdsv24riQ7eTgtiBEktT50el6D04Sjsy7eHfvuMB7k2kTg8VupqcXxWgewANTeAzGReVs0Jik_DtoB-8QEQG68WX8LpzY5O_ftlsMo3aeN_uI8qXsDxiMTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌سی‌پنجم‌لالیگا|دبل‌قهرمانی‌بارسلونا هانسی فلیک در لالیگا با برتری مقابل کهکشانی های مادرید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22093" target="_blank">📅 00:30 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22092">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RiTta99UCxJnesHJLnH_wg36I8W4OUbXAtcDAdujno9D1l_b9xNqZY91wWn7T9IVNX__hssfpd1lbWkamxt6XNZCtT28Q2jiDizaV7C1N2UeFn3SmhMUkDflaN9Y-6tKlNUtrZOnqT1_Qq1LcNHFqmtMOB8BWmYfhTszeQVdR2Wd6u9mphgrvNdIqHd-eGjeUgeYCKTqhHkqiL4UEO5je43q2NuMCnWwyS0EMV9B4yUaNlX3QL59Qscyhg0dEiWzlSsobp-Z5d-udOzIdjtFXityC90q3x70Eej-MSReexLTtz6j3HHlbnmMj0vGGn3xzzJY2PAt3I1fUQ0Jpe6tPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22092" target="_blank">📅 00:28 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22091">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LhXNR76xXJKp-hWyu0SK5dIjwOKZsQK4lGgagx73B_ryYyRvl7PcazQsMT--a2bSbakbcHTpuNLBfl5vcGNfsa7MXTAgAfyPMZaxIdxIMcOUgXwqqMQpZ7fjORT-1FK6paO5tWYu_63EI462sWIE15V-qYuG57t5I0JW2H3e5FgT6CGVC51h3gcJCf1lMVgEdg99stDEZuWg-KUYTsQeukGO2R7eaKr-KaGTFUPnawAhb9gbs_3OvuT2WpEtA4kiTv1X7u9mInb7l8g-1Dr5bhNR-ZpTdWphOEb6LqdRfr4FaDhfPgTFx_NMLGmf70sWgszK6mvPRD5UCZFFxTfLIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صداوسیمای‌جمهوری‌اسلامی رسما اعلام کرده که موقع پخش مسابقات فوتبال تبلیغ شرط بندی میزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22091" target="_blank">📅 23:25 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHY6Gdj0fpj4kGiUFokKAgcxmPPnR-gYoJJLsMXs8S1qHpxFRSPoyQ6t7dp_s0WkUJLibFxtPjZuxXXhhRpvrMLr0PS53P7J1ob5FijNjN1e26QsY-ayqdcCum6yKJTqBAakpTQmEnTWOGggO-Dx01EUW-nmIr2uDqhpxVlAnBw4vi4d2SLyIQRJHlvsCQnTHT6lt-UifNzq7q5Q_9m_pU0L7TKqG2W-VqR4IQq3_Yb9zq0Tkir9uQfHKPNGYxqb4Wli22PnX5yZcOr9aIiTI3FDjLpE3OPwawVH7aP5LZo0AlHg3CINxpVkyyRd4NI_oTJkKtoznr9QtvPVQ2V65w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22089" target="_blank">📅 19:33 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVkRQUjVQkI8tzaverDpGHBhvzETm6Pbbjd-yLEq4GbOjW3tOGL4eChUps1BB5n7UIhpdzTeSu1AQbI9FlqFe6iH2PkO_i-HJXtdeEu518ppS0NbNa6FsTgu7H5DzuoIv3csWure5-xaMMiIDaEWOO8S2QdnZqrStxDKcOE4Av8vBOEuxv4XauIP6Pbv1okWIH3WRQoD9LMcYgpkQlqxyvRPtPufm4rpeZNrLaVoUD3reake_Zch91--aDiOL57CFVJfETA9Mgr_Z2tcAahDns2nYudzjD1u2ssjFIrPOr-bCVn2kubApIAtpwog4TFe5VGp5UsTJ7A3mCl0Iyw4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛موسی‌جنپو وینگرمالیایی استقلال درتلاش‌است که توافقی قراردادش رو با این باشگاه فسخ کنه و از جمع آبی پوشان جدا شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22088" target="_blank">📅 19:26 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eh307g78TfytlrOEunxKPd9uIKs-nIBduvxLxsGxbExIPTETUbpB7WOMjOODAxaszAcvQWX7YWEdUW5cLPbrRjMPLypc1kPNNVG6-iPd59u3vsHqyObzFWqOpbMTm8cXoWX5-ebIZDaN1ySCpKjLk_QwFJtXLprmS2criE10FFeF_MpnCEq3yJ0psGXBb2VlOiHuRfHhA1lMhWehOoFmJDoNTAPH1fgBQclgzr-KVLqRMI9JOrS1vPruJ-ry9pSIr03aXWdeftLEbn69TvXkVQJ3_waHOXj6K6Sin7kBqmDZ-vqRK3U7D455RAlGJfLlakqh4bQQEgrG-dLzcYkZsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
علی رغم اینکه ساعاتی قبل پدر هانسی فلیک سر مربی بارسا درگذشت‌اماسرمربی‌آلمانی آبی اناری‌ها از مدیریت خواسته‌که خودش دربازی امشب مقابل رئال مادرید روی‌نیمکت‌این تیم بشیند و تیم رو هدایت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22087" target="_blank">📅 16:16 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rct1dvBTYPk4M1YJDXTKrSfDxrLH30p4kS4PKSQQmBI4xnHAwRTD3yq4KpJdH6SxTvhuSk_jq7P0E7ktWCEAvA9DBks2wbi1Xb4RpbWCqSbvr1CG41He9rHWhCqDIxY8TmXCOumSt8wFGNhdJD4q_v1yBndjKYlDG_sguXdNlJC80V__umZBQ7N8m4S8alLO35Ykdh8RPeHT7cBT8dAkWETbUIvUHC7FirMHI60zYywTzAme-ofkSZu5otSPQTPjv9-4bJFibFVbkJsv89Ga9lN8H6pKMCpg-lxelPn54FX5y0m_5QEN1Pa8oHJ-vOUg8xRu-64XNPqjZ-iNEniOPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خلاصه‌اخبارتکنولوژی‌منطقه
؛افغانستان: اینترنت 5G تست و راه‌اندازی‌شد. عراق: تلگرام رفع فیلتر شد. سوریه: سوییفت،ویزا و مستر به سوریه آمدند. ایران: رکوردشکنی جدید قطعی اینترنت به یازدهمین هفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/persiana_Soccer/22086" target="_blank">📅 16:05 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LlDWIYG8qFegZ6vzxqdGycH3pBzTf22nyw9-lCnBjV1d3lgIg3m32AwwByr-iZ9fJNUZoSsiq3B65VHjbhCy99YDfOiwRCSL4PLPgv3ZcuJgt9hgXU7AEwsN-rqVN5a8y_4cCfptV1JEo382yn_ce613Hb1QzDS7NhaFAWSDYH_7o65v0O2JVHzVwQ9GDRoImVBnW9OlzfblpwCQ11Tb579RqX_CRV1THwl9o2ciTgu0Upn0AZzl92riXDwouaRBp9OnZSnbjMh70Xy2NQR3KMQqXWfMFG-fZ1s0R0_oXPs-TK24oxp8YmEFLE5vF075IgujqclM9N3OvZo1hKi7Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛ ژوزه مورینیو درتماس تلفنی با فلورنتینو پرز، آمادگیش رو برای بازگشت به رئال مادرید اعلام کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/22085" target="_blank">📅 15:45 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XzXjA6XkWpWPD1JWLNORr9tNskmXSzHNcdHQNxMsXsxYlE47-GeuLrYrlFUo19GZSCJk2IpvYK8as2ILpbPQr2_VZZoJlqkunisp-g6SXYHcquVjdtdTGH_oZlj83_jDRak0cStjjKheG1k6fB5M8ARnwSRVIlUA_Gi1LJbzz3YPdBc2SWB1aBjP0U-T42M-gnPKTshItGwjNi4dcPJiZ5_TYtR-jEJsKFZMfPGfIqi-zF5GJ-1dxdOuC3rdScDISlJWiBO0NtjsYaD4YHx-Aw0KdY8QrUVRZ73R7H2TDfNBPgh2KitD9GCQYi9t-W7jFCUFUoMQvdJIIxF32SG1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/persiana_Soccer/22083" target="_blank">📅 15:21 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRu1hwT-lX7G4dL66a0NYh1gpyGbG5Fo6i5ciGwM_8VbdInh9hyIn6QtwyO480V54ijFPbUv2Qljy_qNmAf8lKVygy6LWJAnyHWjRvqLyUxPJmzDLuwSI55UINdY2f31mueqU3pF9b8XxSwRv82t0VueDuFEw0j_MbQ8oCw-3wjZ1L0PE4oG-fWStG5KAFJL6LIXUUxEvqzTt6ekx5nKTMK6IH_j5fWVtlR0CXJB9_Klewxh6Qbfv_U0bTzW3w4Tc_xQGmMVrfUzv3JsZHCV60BdelTZmXAHSpaGdmC8-fmUuqYg95gR-AO3w1a4yMauPwnV8Dfhuo5fFVRLQjeY_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22082" target="_blank">📅 15:10 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22079">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E6ewpbC1Oph7E4zzCto3I9Crm8tHarjs3XYhWO1pGQlzqt8wqJDSqzr8J6cy55G5bH8jrFstHZRyY1kp6LAlgft7vvKAum8g68DDflQtn6f1hx_MjS_O0sm4UAxbo2npCkj0INStoIFOXj614r31hIzurTGF2XblBvXWM0QOBkysTbbBUm7sWSpKPRfME3ED754jfwc_x29NGBtI8LZv4JdCaWZ-5_6L45Dy1tHj--Z5Zq9FY0_iP-bKQjBQHMYJd9o923L2siYhlQ0RI5QKwIvtKdnp154KOw0zFJ5q3P_M8nTEop0-DtYi1htTuu4X4InXKzMjENuI1pRH9AHCOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لیست‌بازیکنان‌رئال‌مادرید برای دیدار با بارسلونا؛ کیلیان امباپه نیز بازی مهم امشب رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/persiana_Soccer/22079" target="_blank">📅 14:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22078">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KF0FwsT8N6AingkdYQNVBm3OLGeDBRNkazGmJmvTEUCTzjDS0ehmh6-QphUorBV-wfHhyUwWSFebKyi0qvktONcl1tc_z3FfKXTdoRJPfWdb3CKsqaQzDdOdG3dEZHHhwY7oVy4bVJHDCtRQfGaxAlsCxhLYHZSoWgt4dIr2cV2fLbXQb2lid9gdBRw-YlE31uKBjfKP3feBtMz3bZiIYezgN7-fbgVntajcJtQjdvhZVriAFfAXKFmLgMkCPQAAIT2Cs9MDJjXXiuKeAH7TjfQ53kxsFeHedO9deJWzJDVB8_deOThLEho0Ey6Ap-8UTm-Iwh3FCTyYyh4cHMOKKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خامس رودریگز کاپیتان تیم ملی کلمبیا و فوق ستاره سابق‌باشگاه‌رئال‌مادریدتصمیم گرفته در پایان جام جهانی دراوج از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.41K · <a href="https://t.me/persiana_Soccer/22078" target="_blank">📅 14:03 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22077">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjFQqdJUkz3KpKkXE98iN-WU2GACrFph60OV8TldImpkVnEF9w0vBdwpUuvJHfGrA-5WeEEbKU25RO7SgwHt1YYvihqSvv0OtyNal6pK-D8dKAamAiuKQp9c_dsak8fR8ArtHJyKO6ggeiTSesJHWwFmUAaanyc3ZrzFnBIM4CsDbt1Blg1zFCN8m6sMkrWJz-G2GWu_Al_FsciaLrK_OZqOTn9iCZcT6nFJvoF5ewBZhfLvp1LkDXA1Urdk9JIerYBIaFFRrS8BjwGvoNrj1BBvKVln6Jii9MbYNOCevT3OQF-9L-IAWIEw-Ubg6J3xbg07JxBA9HUU1EwD4X6CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
منیرالحدادی ستاره‌مراکشی استقلال: بزودی به تهران خواهم آمد و در تمرینات شرکت خواهم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.38K · <a href="https://t.me/persiana_Soccer/22077" target="_blank">📅 13:50 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22076">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ms8H6sfGL1UEq1GHJRy-W6qbJoFGIJP0HUcta3dewpaumXSIyAGu_tltM3L3gPIp7XH2vGwtb8YM0Ob1b7x6kvZ7T2ErfG3Tu81XtLyHuuR5ulyKPq51vwX9TB9DalDzAjAOZZ2HDw7ZLO7eD3vvF8PqLE1UAKiYfYwOXo57c-HAKA-74Osfkff-eu9Bh4RAyZuQt-ESE59G3TbIpCwiIMA7CFbdr-itM2AOProfMfaeml69s_BPgCfn6eRvAWyE2i4RBF-y0ry0nP9SN0zJjYrUJcIMJCD00FOF4wDLHcO59HfOLypkTSbE8zYMzaploR15EHnmpGkSPYLKEqKUCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
تاریخچه تقابل‌های رئال مادرید
🆚
بارسلونا در تمام رقابت‌ها؛ بارسا امشب به رئال خواهد رسید یا کهکشانی های مادرید اختلاف خواهند انداخت؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/persiana_Soccer/22076" target="_blank">📅 13:36 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22075">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dDwWVG7umeFUWDcbxZJRudu1TE2LeoxqkTsN8dXe6GmpjAGjXONsIwBTMotGF0qeLsawbZaHlDjTju2UHx9CU_rQLlVTR8neAp8LOBt1QBK0fjWfRC_h2DBCPGVkm8lw7GeZREA-ZPQk4WAZz6Wi_C9r_poTAfD5qbAVsY7dOtiJVfrUvMgLhavKBbCx1uQaj9INJEvIpUa3TTW09DAXSNOChMzyLlONzykBm-FrLTbWFLy2T7owcS22cDCBL57Na36EJfC_IxHkVL80YrWI6aBGIhP9kWMSlh9FSBi2QY0tO_fA-Slz8rbUgs42Qf516AIZSod0qDjZZ2sJFYNRVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇧🇷
طبق‌گفته‌موندو؛ رافینیا دیاز فوق ستاره برزیلی بارسا به الکلاسیکو روز یکشنبه خواهد رسید و میتونه دقایقی برای آبی اناری‌ها به میدان بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/persiana_Soccer/22075" target="_blank">📅 13:11 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22074">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
هایلایتی‌از عملکردخیره‌کننده لیونل‌مسی در بازی شب گذشته اینتزمیامی مقابل تورنتو در لیگ MLS
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/persiana_Soccer/22074" target="_blank">📅 12:58 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22072">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dAvJ87wQtG13eqHCzVla6F2GphGTFo6sKTWIzdjNXa3dQrhpKuApzx4jXmGLzzH70_3tQOq0u_ceQn7sAfhVN2U4gXaSyx0hSt0GmLa0i2ofrlk4G4YcKxQpZhvXzCkAuh8RI13aABzapBLNP8Malv0bpLPCv-QA2LVhgJlbuBwW2-kAbond46i0lvHvLMDzUBoKs98QGtqRU9-rX-R39Ni2biXqfV47WGkrLV5Ee1Jz_uplD34OpvlkcrHZr7MysDD4BAeCMUsMSTEVOuXTBtqrQ30QVmomSHatFP13GsgpLMoy1f4-_5Z5gFikCBOiGdhegYcjEJBHCkRvS-4pmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22072" target="_blank">📅 00:38 · 20 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22070">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDsSOjOjfaDJzWDm0HiuqR2Ig3pT0pCOab4pMdOLcYbCKdZaPnfLka2pFhjq5WWpuyoDUr4TRl6mc62yoh0V9bntrAbzcusjUJBgZLYbBX_IG1kogWNBEbbvggE8VWNux-hvbxXPHfHA_de3MGXMUSy8rAddsKAMHxNWb67nBrLAJgll1gbhJGpzebVBY32h6scqwVUYu2lJqWgTCSBW8tK2ZFGGHSP2RwEB1SMCbaUhwKcOfP-QaU8ekgRT1mC5ZQSkBNMdUiw_H29IbWFxWWeNKZVa8cIWRS9MjIgajo5fU7-kkbdInvKC7g7riqUiv9ezEsZwWRv6AgufbGmPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22070" target="_blank">📅 23:19 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22069">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=ja5tGllceKnBBLZ4hygU4aVeFKmHZ598e6UtM3GhqtLoCEFMomFnrczpzEcY5m9njy5AgB8NAxYHm98I3TYvfx7yaKqx0ckxyt9SnC6CpNz2uv2vw8F0ciRTZpOJKlKE6j5EjEAZ3UauaQ7NY6tpoI1t8zhJLxJrXXdlbpwLBNqJc1gmWr5TckKf0AH2SfAMc72soqh8TvbSyxdnafFnKjQbsNMqTQagRCXUFr-1DVWiHCyNoNbKY_3F9BsfApWQ07dG2LHPrpN2AOfN5tWRu-FVWdsTAvSTKjJGZh2mXl2utYsZYMsJO79xBdyj9ukd1IqoVMG-9YZH1GhdTab12Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f79af6ced.mp4?token=ja5tGllceKnBBLZ4hygU4aVeFKmHZ598e6UtM3GhqtLoCEFMomFnrczpzEcY5m9njy5AgB8NAxYHm98I3TYvfx7yaKqx0ckxyt9SnC6CpNz2uv2vw8F0ciRTZpOJKlKE6j5EjEAZ3UauaQ7NY6tpoI1t8zhJLxJrXXdlbpwLBNqJc1gmWr5TckKf0AH2SfAMc72soqh8TvbSyxdnafFnKjQbsNMqTQagRCXUFr-1DVWiHCyNoNbKY_3F9BsfApWQ07dG2LHPrpN2AOfN5tWRu-FVWdsTAvSTKjJGZh2mXl2utYsZYMsJO79xBdyj9ukd1IqoVMG-9YZH1GhdTab12Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
رقابت های جام ملت‌های آسیا 2027
؛ رونمایی از کاپ جام ملت‌های آسیا در مراسم قرعه‌کشی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22069" target="_blank">📅 21:47 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22068">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_fh-bchTMRYlhOKa4Syki_EN1uJ3mUynbgbizhp1jvRuxyb9RbovDRYT6zr62hMQP7WAgY54AnWy0Qo9mX8-46EWPUrUCN8F5NtcZ_WKQGcQEDMemwVi-XFdNuaVW_T396Kj8v7XZz1EBLhRCTVjRujRCcYuparFenq7bDWjybqZPyBWOY9H0S_1QJUQ5bzzewQu1gigr33EPudwdFg6t7C--P4eqIzEkd1wFQICy8YazO48RuLdA2g8L35oauMwaeqIkRKiOn26xh0ng0NA2_MMsgusnZ1tL1OWL0sX1nFtcmxvKsIKCCtpiaHPpWlFBLPCp_rDbitYPCnRwvoWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#تکمیلی؛ باتوجه‌به‌اینکه فابیو آبرئو در پایان فصل بازیکن‌آزاد خواهدشد؛ ایجنت نزدیک به مدیران باشگاه استقلال همچون‌قضیه یاسر آسانی به مدیران این باشگاه گفته‌نیم‌فصل با این بازیکن قرارداد امضا کنید تا باشگاه چینی بیجینگ گوان مجبور به صادر شدن رضایت نامه‌اش…</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22068" target="_blank">📅 21:08 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22066">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorxIvC4LfdBVUigPNmK43PGqgQ4OPzpaqtXik-RbA4YCO9jghVqlrJb3k1D7G6akLqUrRbfXlxgct3tI8UuOWACVQVLXW19lBIc-pPS6PiReEy94MnbtbwgdxfHueYcdwfMBFxyqDNqSKMWY_RXbMGcrXuantWOKIUfMagHxZAZMihlnmbyy2LR40Tu7B2yl31n6zue2SYuhGU-nDZZeCCOHM81ww9Qp1bS40fSTEpqdHsyctBDgdL0qsQCuG_Oe4rbR937nXQYuVeC5ur0DWtylig2PaMkrornlzs0cOZb_PGc7F6NHVhbKSpun0o1nJpS0b6dCVbzpObar_xoDufME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cee0f87bdb.mp4?token=BjAZDvvAJ0FyAaDeuoJ0YPRedyPuzIz8CzwyxWJMZHaSFmh0SgpphDHbXBbznVQ120tpgR2q-uL5hU_7fVAQkjEYEFnovcj7Bzq-76u940jAywWZ0fL-KhljU5sCo3CVllSlg0PSeCg91DqW05vz0SZXinW0s-ImC_ooBuGvn_NQET9y_VNCFijYs4xyCGrcoVm-bjTcpvhgfGMNp7pHaMr4L2zfgYEn1Az58v5qyS-hfGS_7hSSx6CcElfj-mZUMXQH91W_Q_JJElKNQrqPOyGbYzAje8cPN8j-TlU3ZZVau70SYZtf9KAuLbgwk-6CPDZpf2aCTvRll049EgyorxIvC4LfdBVUigPNmK43PGqgQ4OPzpaqtXik-RbA4YCO9jghVqlrJb3k1D7G6akLqUrRbfXlxgct3tI8UuOWACVQVLXW19lBIc-pPS6PiReEy94MnbtbwgdxfHueYcdwfMBFxyqDNqSKMWY_RXbMGcrXuantWOKIUfMagHxZAZMihlnmbyy2LR40Tu7B2yl31n6zue2SYuhGU-nDZZeCCOHM81ww9Qp1bS40fSTEpqdHsyctBDgdL0qsQCuG_Oe4rbR937nXQYuVeC5ur0DWtylig2PaMkrornlzs0cOZb_PGc7F6NHVhbKSpun0o1nJpS0b6dCVbzpObar_xoDufME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇪🇸
از نبرد تماشایی روزهای گذشته فده والورده و شوامنی دو ستاره رئال مادرید رسما رونمایی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/persiana_Soccer/22066" target="_blank">📅 20:26 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22065">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BvU68VoREKjHDnRMAVkcIxDz2OC_DU_T63Nnj3oy1NU_gesEmCpR0jwUfwZh8RzgaByFSia9uSAWehUqAlWSWeDhOsNBZzZZ0BOlw8usKeMShZyqTzF0olykfRzCa8fvxl-rNczonxR5CGd5Zp6vUzYlk61jWzIQbr3rGOJ4d7jgYJjfutK4bpPexyqgNSeX2HXVqSIA3ZFJVQZcB-zsdU-l0ok8g7JuQlP-wxAU7x3avpE430s5DuH30p1MJI_b80n2h5phr2ZUq884dPsittRrB-WSpuSm9H5qqtZmM6SNiB5acreDUKUywHDEorimQuUWUOnpfe4VKLHVN584ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مهدی تاج گفته بود داریم مذاکره میکنیم AFC وقت بیشتری‌برای‌اعلام‌نمایندگان‌ایران در آسیا بده که AFC مخالفت کرده و باید سر وقت یعنی دهم خرداد ماه نماینده ها به AFC معرفی شن.
‼️
پیش‌ترقرارشده که استقلال در لیگ نخبگان آسیا، تراکتورتبریز درپلی‌آف‌لیگ‌نخبگان و سپاهان در سطح دوم رقابت‌های لیگ قهرمانان آسیا حضور پیدا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/22065" target="_blank">📅 19:41 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22064">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TqiR_QCyBkV3Kf9_hNRXqdEEGLWfS5CSgwVclI6KZ2RWesaO72cPEvaqs7hkPqWQv7FaK-or1S-VP-utEihW6XuxGTMuxVY6fxXgntWHhzTR7MUlqED3rAmgJOAK8wNDSPrBJfx1zQBniV2ze8cKsAeyUlOOoeTlBbQsfskanj0yhWt4z5zcKs_Eg_faWs0e0f5sTrpUA9mcgbacSFUofyAb4dggthMiqwxM8sf5el7Vqs9nKFXJ67vh8Vmv_VwqA6e9vJX1PCZDRRrXluVQNC9NsOMSrGCXGXC0mxj2_eY8X21MNlHmc381rHtw9jnB4xsJLlJBSCLfuniFpqi0RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ درپی اخراج رفیعی از تمرین سرخ‌ها؛ باید شاهد کم‌کاری باند پنج نفره این بازیکن 36 ساله در بازی این هفته با ذوب آهن باشیم. رفیعی در جمع دوستانش گفته اوسمار بزودی پشیمون خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22064" target="_blank">📅 19:00 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22062">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVaGKSfalWPQXSp1NLeUuzZ_kC1uMSp7S6VJ9gFF2ntNaI0rnw9wiruE9mB8Tmvn15KNdULdWFCjAZByQkHwcdjv1Qjp7ZxK5bMVT8Pu03NtmWpPRoaZkYJhIo2ldHNJ378H2ZavtlYQBHOt01cXy5QndH-9BIWiIJJJYbjehdzfKbREANILAyhW6SffeaR5mGD4n6y-lYAabUqoaD8VN704WBneVZqP7-qTh_zm-66e9xHHeRi1fbX3mZ1XmeBDoiT5vqwWgBVBRS7IYiX-NpAMb3H2iwWqpFJoiVQOyezZX9BI0r8TlXpfHKk_buyTk4_rp8-gUiFqLkamC2KiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛ ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/persiana_Soccer/22062" target="_blank">📅 17:34 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22061">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlnYQwHQPGq_n6E3UqdDLOQ6jnWNBWMmTsylwzpXP4U9nJlkAhD7pifOoqBx_8KyJ0AR1nmIHEV9a80TlVlpTDk-Oy9xm40TJK8JWBhgqUsd8dKgdU0YXWcFsgdRk-uFTxeDP_3FzPJC94VKiwtZcirY6lcUSuR-Q3LuwLJ0_UNWn7hs-jMfsbs4soLQu5Uvh7k3l_ULdigmjfktQzssJ5km1XrR69Lz8YA8eXawys1ZuG7TZ4Sl1uQHLxbY3jmlzOjmgJX_liH2VWtyKQRqzaeW-rwzF-dPF9u92ita2f_08AqISaMEmbPdB-utF-OFu7ivj6NscAkBXiPeN34WVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
#تکمیلی؛ با اعلام پزشکان برزیلی؛ نیمار جونیور که 24 ساعت اخیر پای مصدومش رو به تیغ جراحان سپرد به رقابت های جام جهانی 2026 خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/persiana_Soccer/22061" target="_blank">📅 13:37 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22060">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT53toPwIk70wsxDlz3u1AGjzYI39dUuu-Co2LlzdLqh2oxd7AbBK2S_vpkNZ8XBv_o-xlr3kTe0pumItA8Pv5Bygj7uiQu12VJz-Rr7Z5Wd4DwE-AT5rXSycxJeSxUG0l9AGpIwKsgzoU3MDx4_d-zN7id3Kf_Rk0iuyz5s7ufliFg8TmS8wg7tvQywn7jP7Q5om2o82KYwgfz-13zyrvnmuHiHIpa6oGoHv1LOyIF3LRoNnLql--USFcrG31cjq4dPABToi_kM8vFVuuMVzV4W19fPHJu6J20zpsbBYbn2vzXIV_jLi5DGi9dg82TEBgfIXYmXVNfOVFPBLDOnLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇦
👤
کریس رونالدو فو‌ق‌ستاره پرتغالی النصر؛ با گلزنی در بازی دیشب‌مقابل الشباب؛ تعداد گل هایش در دوران حرفه ای خود به عدد 971 رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/persiana_Soccer/22060" target="_blank">📅 13:09 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22059">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GWvbUUd3C2lL0xX7VwHzHwGimHRtWw6WSQyvvIAiRKWh6LMUPk7jkY73XVCnxq0q83GoTv_ek6ytqeHAOTvxiwIVWiwtNoVgqMSWYll-iwdFjnhTag4SFZV0Ep-on1VOsKsb89BUwAIxaf9KCIhwFZDCV0h_0fg4VePConq6Ny_btHtyuaYnxGuvhVYOYmYSmNjdFBtJge108javwvV-zm4D2QyyCc9z8I8wuRKKnuhU6c9mJ2DHVkZoXnMqTeD7QwPyRkFsebeE-FN5fGgtGdGDiGNvu79S3J3UZYjfZ6-1g6j9WF2_u98EYdI1LlOGlt-AP-kqLcnllUYaX_4IqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
برخلاف‌شایعات‌مطرح‌شده؛ مدیریت باشگاه پرسپولیس برنامه ای برای فروش اوستون اورونوف ستاره 25 ساله خود نداره و این بازی در جمع سرخ‌ پوشان ماندنیه. پیمان حدادی مدیرعامل سرخ قصد داره قرارداد اورونوف رو تا سال 2030 تمدید کنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/22059" target="_blank">📅 12:58 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22058">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjSMTGypGKPNvsCwNelBTsfqGJR4Z1lQDcpBshbtoDGSk_TUS7bVzyoZNCBcqr-EZ7GjEk1kN47bKbnUI6TWvSGF0aDlAo6uG4SIFAGiOY6fYTKGmti_iVNUkn0AJMcboLD0DB9ChrC2GChqm3VgHoSc64IZO-0jNlCnLrqS4CjZUQUksM8YNdAHElUGkZzGvoKCOBWuLTp-OG2jl4dI-BmUWp_WxaurO0pEjmzXpnvdk1Bp_BpjpOFfha1_uMha9OOpUTEl7RPKDX6llyf2ZZelF1q3lsAYxYm_FdGph6Kp5zW4SJXjD63YV_86Hw09G5-l4Inuz8PtEUy79gkqZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛‌خارجیهای‌مطرح استقلال و پرسپولیس تا اواسط هفته آینده به ایران و تهران خواهند آمد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22058" target="_blank">📅 11:53 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22057">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxTjGKFCfVodXGJWn3RKFt-i28b9U8DjgQwxDTTDI6yIvPQL209QTrAwvjYyrL2DpN5NnqYaRNPSCRWU4_N0caR27VkNt7KfeaYa6mN3pWxPczyTBYLJZ9cpWbmYk9_vg-RQ3dvs9NLdRZSJy1zlBv-kkiKk66Si_hIeZPEfLbEeFfjdDVAef-qFU9MQux3ZwIy12vJA4Aulj6cwm8CgXtO2wLssGXInGtN6-QqqP1sMCYmcIqo4h-FgnPiXf8qvFhpz2L19zlcSJtQaCBSiWaTS6k10m7-GGgkSqpJpjcMIsfDIQrdveyBUunqnrINqXGJ5OSI-nCVK8P6jXzKtzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اعلام‌نامزدهای برترین بازیکنان فصل 2025 لیگ نخبگان از سوی AFC بدون حضور بازیکنان ایرانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/persiana_Soccer/22057" target="_blank">📅 11:49 · 19 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22055">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B09T_S2nWoR060wMAv_rTqlBLaRBtGK3rb7KOwD-f9el4ExVNRZQyYmjBv10vzfPhdAEi3XJRAxtTnVtSek2c7gXZ3u6Z-l0fOIcS-_0AXlwfI2MHod4iyxrI7PQ2qAFfu9ld6K0SRaVe3n753gE7Nk4CAPxa5U1XRNcOM3uG3qM9u6eiUCt25NJrGK1YvdKJWTAkQlM732-3SQwFFmIk5PYy5-p5JkWEdnUfZJAxoWAxoXCoQ9sM_nr4dW-IijWyFpNFrJcQAAiIDw4O0PZuljTJ5mJqzL0VtyhNbmSKt1IdkGbCZnmVBejte03bpoiDOsR1I5ej-p_N--sA_y-9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XxUbKxWzUJ_DbP_RlCQhWDK91nptmPbx6LP3mq_uQBWGYdZGxEJ9KjGWG9jbeMIJOx3bkZQuHJvETWIBmSS_eM6l2cqULXuUZ6zlaTRAaQL6QYCTD96_-oCdhlWL6L0dNa0BUu8iFK1VrHBFq7aF4vTMUvhSmQFxlxvY7a2P5sZ4_44XTNtPFBjqmhpZRF99seDe2iULmgk6u0Ii4mm_ylKJmq1qIKiBBSiv6kSxoziF8tym5h_xQGWFxZ7AMmLjhCo5Dh8CcHpV8LmPw4RoUq2iBgLSEgpiuxtxmWoxNr6sODAeo9xsAdWccOBAKY6bDjsM622fmBxkDv8EFT-74g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">طبق گفته رسانه های پرتغالی؛
ژوزه مورینیو آمادگی خود را برای بازگشت به رئال مادرید برای فصل آینده رقابت‌ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/persiana_Soccer/22055" target="_blank">📅 20:05 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22054">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZeIgLuYoIHS9IFwAR_t1tWo7A_OOVIBwatEf6757B_CphqZvzHIdS9T0DMPxlO3BGmX8lWBJXQraQ6s9EWq_hpUErFvgfMgat-SW45F7NcQLJ8MW_IItHttRC3avE0kAJIprdY_-Hds0CARduHTppRHEiW-Mw3TAw8blsbpwubJXIVMdww99zYEE2MuuC8nbMs681GVmTeW8ut018B8Jjktv7DBf0QVZ3K6Y7TQFmTwTEb6YJSiIE9KohfkJOlF_l0JythKEb1avXfZFDgTnmisdbfB1jWnSgJqA4om-zy35FT3pmGibYE0E5Ha1Z0z9bjt70urPpAgoMprSM4HSpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟢
دو گل دیدنی احسان محروقی در بازی امروز فولاد و شمس آذر؛ گل دوم روی پاس رامین رضاییان بود. حمیدمطهری درنیم‌فصل دوم و بعد از جانشینی یحیی گلمحمدی در فولاد نتایج قابل قبولی گرفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/persiana_Soccer/22054" target="_blank">📅 15:33 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22053">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57250d4705.mp4?token=VQ-ib4FdU_kapC-a_nR9LSmrq7T7F4kIpcL1sXC7EgwdJykUheMdW_jaGxmGlWkA4Ov6V8c3PUeIBXWhCbl5n1cVfiSlSsDojp4hmZ45dERMf4S1eyV62IGw6X_x0wnTr4GOi5C5Yj132Efd28YUA0hRAdh-kvq4mUQqGAIcQd8PU_uWS_66WOBDP-vJpy8kOWjzink_It8zAsIyoRibbrNDyLOcdi1BLn8SledS-uHtTzn2ZM4UoM9wtCwDZPRDwV5R4-3gNpyWq1HsNEMpyGRVU5SUuRbR1pDt8k6rYJ0hKLMJzLfwRvtx9jiAt_hc9ke0DfN3NelDMYZMfQnVnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57250d4705.mp4?token=VQ-ib4FdU_kapC-a_nR9LSmrq7T7F4kIpcL1sXC7EgwdJykUheMdW_jaGxmGlWkA4Ov6V8c3PUeIBXWhCbl5n1cVfiSlSsDojp4hmZ45dERMf4S1eyV62IGw6X_x0wnTr4GOi5C5Yj132Efd28YUA0hRAdh-kvq4mUQqGAIcQd8PU_uWS_66WOBDP-vJpy8kOWjzink_It8zAsIyoRibbrNDyLOcdi1BLn8SledS-uHtTzn2ZM4UoM9wtCwDZPRDwV5R4-3gNpyWq1HsNEMpyGRVU5SUuRbR1pDt8k6rYJ0hKLMJzLfwRvtx9jiAt_hc9ke0DfN3NelDMYZMfQnVnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ رشید مظاهری عزیز بامداد امروز با یورش نیرو های حکومتی‌جمهوری‌اسلامی به منزلش ربوده شده و به مکان نا معلومی منتقل شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/persiana_Soccer/22053" target="_blank">📅 15:16 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22052">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l0K8Fm0YI--l1NT4hwjbeWGBAXVB0EDyUlC2ibn251lifVhzpna8t4lq5wTuZhrlI_-vIK-2nTcR0tkLyX36I1yfTpht7iRERgD59-5wnjBvT1ErH2ZfTonRo9PKxM7k9R-30JdArTuV8Cyb1HwF66Xraa7XozssicdJQA53twFAk3uY0qMKROY0urgMGrp3UP1dFBYGa0RNuqvxkj7ygb3ymma3BNoKSOT6Sv1RCFJbxGM_lmqqPgiksewK2y_5-LP1ojvMHTKiEJtcDIUADs_ry9smU-GhDSTQ-lBxTLZZkjMXICEujJJe9D2spQhnhvG1Kf18w63bFtWEXk0j3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
ترامپ در واکنش به قیمت 1120 دلاری بلیت بازی اول آمریکا درجام‌جهانی: من هم قیمتش رو تازه فهمیدم. قطعا دوست دارم اونجا باشم اما راستش رو بخواید حاضر نیستم همچین مبلغی پرداخت کنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/persiana_Soccer/22052" target="_blank">📅 13:21 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22051">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-xzlB4nygStQd-Mw5A-bww6xW7vkrb2W7rwUQWE6ujq6Aj-RF27LVKt-F2gtzENzahR8mlwdF6DswTQ8Xu5SvwlNJBlgET4gqq7zKQ9LokmbbBTBopYmV9CiDYlVhiPh3c76AncuTgDSGSxhhI8QJY5v7RDxFs9QJD-RSlCJxAqS9ZeDRs6RYQSoEYnxgkV7t6p8ix2Ek2ioh9FnG_v9GAF_yijAwXd7IghiRHDntCK4CwCmseC5ul_BncmtimiL9t8nLfjgUycPzK9_IbQ8bJ3wt4ug_rImTeagI2etsW66MrX4ahfRYVUmzCnnRStB4ZeELJPkTWVhhsPuvjljA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/persiana_Soccer/22051" target="_blank">📅 12:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22050">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU5v-GQBnX4udOuNscH7eRYh0azykQ_j_bje-0kLPfCGEsK0QMRgxSR6JKmQUHO7zkvWUMvMWafjs5NMtZ6WoUYngr6-I_BZ855zyhX2-7Vidl0FHmSCEkVXKoeCbgiKeq8Oh1dM-qKHPJyyYVrio-DMIiWDeJyMs5zvKEIljtgt8uh4EQilmjcD8Vd2MeGO0xpGRmC02UDJjd4ccslMKZnzAMZEM8pYUzaH0PDxCd7z-O9jvoU_KWcPAjlgLIQTj8L6qM913d7mL82C-x6G05lONDV1eTICL6qEeB-nqSbvMGGqjkpcSseQo2dpJuIb5cclnq2tGAcuyuID_SCraQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6w4atH39fCouqU4JmG5L6EG7dBegNSKREqV2zLDwJc7Edcwq8W60LAF8cO2pR_J-hEZwr7qXXsMkDV7yGK37YB3Pcy2wdDSXnvq8Id1QKLGLob-V2xB1IPZBw9org-7Q0igQN-QUxxuPCBSGTmafU3uhq6i2VQ_1dsraqj7GAaqIZQrVkSwetQRRigBLeMs290MnYBBj3ihGWtZ0SOEYXKAlYPZC-Vyg9Jo-K85UW4B8SW_A-GMNDAMipRnLj6Z26m_9LgXc80nnhtdKYjQVxiVwtA3VhVUtZ73Fh-RlIesa0stsCzzCceddNDj5fQ_2fdmpL3oAB75HnGlPBrQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ با اعلام ایجنت یاسر آسانی؛ ستاره آلبانیایی استقلال برای فصل بعد در تیم ماندنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/persiana_Soccer/22049" target="_blank">📅 11:52 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22048">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODq1zW5c_BDoZXuVxS0-1z4YCH_2U6c1a2hqwEhN-Yrm919k7huxCmLE5SmZCkZKEGMqLG0UWYSa8y60hiYJtPG2RBxOylc17XleCpwsJAx0L9r0Pe1toksLhghrSL0d8bMjwzqabiUcDAXnV-Ee-OpuOEQz6W-LvfOWVu2Kko_MSS1G1g9uqarVmUXWYF7M4Ys8-YcWtodoAjPov-cPCeC-ot0pj93P06qaW_fLNEel8O-kRzCLGYJE8Z2PnMJvxMFF4noPiLABEbEEnRWyUJ87mEz2yAM3L_9DqO8HV5pxjiabIklmI-xzu_9_QKVKh2TsN1P5yrcKCSHmjKBxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رونالدو یکقدم‌تاقهرمانی‌باالنصر؛ کریس رونالدو و النصر باپیروزی مقابل الهلال‌سه‌شنبه آینده می‌توانند قهرمانی لیگ حرفه‌ای عربستان را قطعی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/22048" target="_blank">📅 11:47 · 18 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22047">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fNGHDEVnFV4Op4vTHS3KkFrfzLndhHnyOWNJUbf906dVw16HwpREd3EMFdX3tDBQnW7-eMdkmFoc27k4ubYOzWGioG-LccntG8tM9DbLwQ32Hxm7LLtY4z_yAHiOBL39Yy7TdUnt0NE-TKwzrNTYQOIj-VqLCiZnWUj55Fi6BPEK2ZNP4HJPABlHQxKtyc43Gw0ht6YnVI0lB9YD8ma22CS8bAfmI_KVkviY5s9_f5hnZgAR3Loo0rMsAH0vt_qKl4yDfPrmyzVB9FW2v_9-Lc8u-rPZzPiCYkyspYszKK3gmavDMLxMlg8B9bMpI9sm0C5gDFLAWERnxdbEBfJOTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#تکمیلی؛ بافعال کردن‌ بند تمدید قرارداد اوسمار برای فصل‌بعد؛ باشگاه پرسپولیس به بازیکنان این تیم پیغام رساند که هر بازیکنی که قصد کم کاری داشته باشد قطعا در پایان فصل از جمع سرخ‌ها جدا خواهد شد. ضمن اینکه تا این لحظه جدایی عالیشاه، رفیعی و پور علی گنجی…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/persiana_Soccer/22047" target="_blank">📅 12:16 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZIy7Dun4ijmD3qDN4oMAfFumybcmczrxN7uPcppj23o8HROa2AMQf8q-e2aTlHdn2iglMgLgCfhkVr_t4pRLlS2DHo3BkYUOlSYQT-3Vbh37Fu4ZIZLtONkEvcU6nLhzdrWcdiQQmHM3_MMM8JfTApB97x2NQkMq4WXs1sLlYovXSxfwPh0ZZzxx0PwcRYrkaGRm-DdazG96zDOzz2dScBjEUQq0PpAI6maF9JjHWPq_7FeKimU9DvMB7-5P6nzIJYL0M_JRk4_FL5P5ccXe3LIHe8ve5-DHEy2U8QlzWQuwJZvm9Sfhw211H_YHWyWIaB3RAsYO-s1wGuEHIykTdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔵
طبق شنیده های رسانه پرشیانا؛ ایجنت‌ خارجی‌های باشگاه‌استقلال به علی تاجرنیا قول داده که تمامی هماهنگی های لازم رو با این بازیکنان انجام داده و درصورت‌وقوع جنگ‌این‌بازیکنان باآبی‌ها فسخ نمیکنند. ایجنت آنتونیوآدان،ماشاریپوف، آشورماتف، یاسر آسانی، داکنز نازون…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/22046" target="_blank">📅 12:06 · 13 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Cxml0a9AClzPwjwDz4EndORVUOzPwPj6ASzk3WsOk10xDVeiUfiegxqqhUBCzf3L3-0IbAsw_L-eQs1aIUh0Kmv4ng_g4PPQbD-Sf_mGNfZJF0dR9KEtEkcl8Ffy8lVNWfv8J6gCVye-CdpQ8kp12-xFeUxC3f5bu_eQjjuOr6NZ-C1SmZT0lrdB69yFS5ZppQ41d5kYmJecv7N9Rp_k3LJjs-HSWp1GqXsIujw72sRtsuVl4bBBLh-wHohDds-PEqUSGxPwxDtHFeUcc37b1Y0iPpkHZ-iKvnXrUFrDq_8lex1e2gt5r2IEragqiorlNk9jYuko4UzdIkNlmpwr_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e82bd445b.mp4?token=Cxml0a9AClzPwjwDz4EndORVUOzPwPj6ASzk3WsOk10xDVeiUfiegxqqhUBCzf3L3-0IbAsw_L-eQs1aIUh0Kmv4ng_g4PPQbD-Sf_mGNfZJF0dR9KEtEkcl8Ffy8lVNWfv8J6gCVye-CdpQ8kp12-xFeUxC3f5bu_eQjjuOr6NZ-C1SmZT0lrdB69yFS5ZppQ41d5kYmJecv7N9Rp_k3LJjs-HSWp1GqXsIujw72sRtsuVl4bBBLh-wHohDds-PEqUSGxPwxDtHFeUcc37b1Y0iPpkHZ-iKvnXrUFrDq_8lex1e2gt5r2IEragqiorlNk9jYuko4UzdIkNlmpwr_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عبدالله موحد اسطوره‌تاریخی و بی‌بدیل‌کشتی ایران متاسفانه چشم از جهان بست و به رحمت خدا رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/22045" target="_blank">📅 12:55 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uSLAdrrU7r-3xlkvAGg-rwmLO7FSpNEgWzXPb1O2v4utoxJUjWed8kENhSPF3yntYt-bPFMnf3GCooM1rSwv0zag1x092DBf4ThomtWFOBG-jkshPue7RYdog3qw54bmObQ75fWrlttBlLq1HoNZw-X1Wbqni7WvJ7o1o5uiTAsXkRNTePjHLlY8BypEn4pXxJLIbce80PPasxYUAscQdXXlUto7_53xZ9AzsR0oerl5Q-m6cCxkujUnzBOr3-iYbFWSav_HFABrPvg_pI0O_5BCoc-0m-93QhrmyNnSCPHYlIgQqqvLZrmNIhgz_BnAfvX09jf4JGhkOQJKE1FnGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c204e378b.mp4?token=uSLAdrrU7r-3xlkvAGg-rwmLO7FSpNEgWzXPb1O2v4utoxJUjWed8kENhSPF3yntYt-bPFMnf3GCooM1rSwv0zag1x092DBf4ThomtWFOBG-jkshPue7RYdog3qw54bmObQ75fWrlttBlLq1HoNZw-X1Wbqni7WvJ7o1o5uiTAsXkRNTePjHLlY8BypEn4pXxJLIbce80PPasxYUAscQdXXlUto7_53xZ9AzsR0oerl5Q-m6cCxkujUnzBOr3-iYbFWSav_HFABrPvg_pI0O_5BCoc-0m-93QhrmyNnSCPHYlIgQqqvLZrmNIhgz_BnAfvX09jf4JGhkOQJKE1FnGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سوال عجیب خبرنگار:
اگه تیم جمهوری اسلامی قهرمان جام‌جهانی‌بشه‌چه‌اتفاقی خواهد افتاد؟ دونالد ترامپ: اگه قهرمان بشن باید نگران این موضوع بود. احتمالا تیم‌خوبی‌دارن. تیمشون خوبه؟ نظر تو چیه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/persiana_Soccer/22044" target="_blank">📅 12:52 · 11 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22043">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ka0oXkCClOLCTEZm6E1osuToEQRaiR_6jBGG-BPcAeNnEPPAdPeR374xKhPYrF7uB0AGUsr4B8o21my221Ucn_OTi3on2AvPfa9dmsw-0UA4TmuCQf9RhM8639SELQ7wUPxUpoRNeBUItUkGAA_ajRsWnyZ3KYgRyhoJhr-NhER9gUNtbqitovT8bLSg9Wis2cZKq2KhpvU_iIqdPmiOK5_VvzaPifCff7SvYm0Pm0N-CNmIQgl-TwXLBQcm7LJKjGRynAEWnM5sNiSKTIRDL4mK0tqm_w_7RWpDFT3QcHVbkJgMYp4x9AwIbwtXFEUFvyZCTPPTxfLIjnMXvZI3DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌استقلال بشکل‌‌رسمی با کلارنس سیدورف مدیر ورزشی این باشگاه قطع همکاری کرد. سیدورف برای تنها یک فصل 250 هزار دلار از آبی‌ها گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/22043" target="_blank">📅 21:22 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22041">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcCV6S6RNfPwZuUVqijNqB9seFHRPhETPo-kvKoHEbPwO1cpEQP193iJfp8WnimfhGTzbIgRKtFuDLjKeTYELyFz38a5j9rXbKhjusIjM2eenqf8nPhCCSkjMiNlMbeq-xTpDgXCmpt-2CvNp2vGJVK7UnowdX3Q2UUjsEmgNuT0WtFXs5PnBuZjbb7PQ5OMj5pSi98aJ66mFdeSWP5FRsgcRFyyIqVDBhQDjWS824bOQEXkF9E2GuL0J-DH4YoYS-bg86QSAF9RW6bcmutVGJ8P59hAZcpP0jvqufEnE9SyK2HFsKnmBb5wOmrLw3VyDyBidT8vXn-EjJ0aiDjbAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه پرسپولیس به دلیل سفر افشین پیروانی به آمریکا باسرپرست چندین ساله خود قطع همکاری کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/persiana_Soccer/22041" target="_blank">📅 21:17 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22040">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HjcZMQqiEwApRqxjSypQe5cOs9XultRNQcz-VkhAhi87BFYGDSwAo5z8WJubIyaxjJTyMSs16ZcGq-_6owvS-6mXpW6MrN4gguAx4BdtnluQZPDMnoDSWZMjZCK0s7p0V_pGjY0QKNUg0dX7X_Ae0jGPFdXItzWEovBOit_zvKAzKFrj_QjuAqELIc6gEwDXO15zC79yXBDG6gaWf3yFZcy3DJbJK_VzEYFdaeLnIqXTyZp3-34aeRH_WbCUMPLINm3xxGsbkPwDAw6yIV505FCLIPFnOozsErnOimEdEFf7qvnIw0uVdBegHpOf43ed40ObqBaWtpjObS13eH3JdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پلیس‌کانادا از ورود مهدی‌تاج‌وهمراهانش به خاک این کشور جلوگیری کرد و آنها کانادا را ترک کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/persiana_Soccer/22040" target="_blank">📅 21:14 · 09 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-22037">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVvhXfY70kc4H83svOP1-Fnwlqm7mTwGl2cBlIcezKpYlqE2H-CQQAIklfTgA5WjjLH2hp-q-r4qsEyuZ2l5hW9Mc7tHH-utJQsJAriC61EWRH9W234A_K_mU3VRCaoDbHfZTyC1qogeuBbGYeZMTwkl3X2cA0dbRIwERuRV_s1EZvxj-3gxGaNRsi4IPZJ1RdPxqrUrBYuW6x5CEWuvH-pPyXPzFX9l6bKyu2b4KyT-d3rJLsvkVklhAFYhsrq0COXkPa1TygpsFq3CHPLBv7t55QKiyDtGHYMbHFb4eQs5UCre00TWNl-OMVv4_XLRFtJlmVAEkHftmvC9c8o9Cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تاج رئیس فدراسیون‌فوتبال:
اگه لیگ برتر برگزار نشود استقلال رو بعنوان‌قهرمان لیگ برتر در این فصل به کنفدراسیون فوتبال آسیا معرفی خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/persiana_Soccer/22037" target="_blank">📅 11:35 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22036">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/el3c7rMDDH6PpWbURVu3gazsN2MF2g8x6-kLyOitqaUNf6qUBNjKFAjsE1LGCISjVdyxDqrkt8KvsqO5CJyqspRpOWlpXLX3np3SKy1PP3ZPAlZMEHdXFIORf3UJHt51Fwj2ZNAgj7lRQAiU0urXrhAlnxQhlxg6R1FZGHTx7VRn5SXNOSvH4eeXBfposcvFl8S9LGLZT2dJrMUsWrvAxPBkhFxdvjwz9_k4sRi-Ta1urQYml2ee32BYN-qSFD10QSvZ92Q_b6v-IrriHOzEL5dXyfsWizyMpO5T3L1kWkpKrPiTDZHlqKCw5_glnouS7Xw3jLJlbBduFoY7RanrCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پنجمین‌حضورکارلوس درآوردگاه بزرگ!
کی‌روش با غنا در جام جهانی؛ کارلوس‌کی‌روش بعنوان سرمربی جدید تیم ملی غنا انتخاب شد تا برای پنجمین بار متوالی حضور در جام جهانی را تجربه کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/persiana_Soccer/22036" target="_blank">📅 11:27 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22035">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SX0216GjC8BCKlvFAh9VYfDYSJfEn84vtC6w-7UevtsHV2JrvhHEqcGvJfiD8eGynUtg_McUYb0WcFVj_LgPwEM358r4svtO9nqrls7_DKVzyR3OX3kRVSQDnoIOTWmjqf_w96q0FexZ8mFdX9aEWTWrqpxS6Fjl-kBz4OSViRg8mBqsx9whDM-iWZypU6nu_uHt-99RQY9sO9CyUZuevBm8AOO_gWjgGx83E4rvUSsBIohDdQeCU-4yA09RXd-mULUC597oHOnEFmK9xFqeU9vTGpS_dxhEiV0gTzRl95rbriprYVheR5WHx0GArCAV-ePVt0kIUlron1m4VxnLug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به‌انتخاب‌مارکت؛ 10 مهاجم‌گران‌قیمت دنیای فوتبال
حضور 5 بازیکن فرانسوی در لیست 10 نفره نشان از خوشبختی دیدیه دشان در جام‌جهانی پیش‌رو دارد!‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/persiana_Soccer/22035" target="_blank">📅 11:11 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22034">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=UcvH4-M9yFUWUPt38V3INU0AguIx96VaAQ4IQYbXxXzMh_w960vIs-x9DUZarXeyVQdJjD3NF2ozxTytWzaFeLf6HiIDU7lAh9EkzOuPW-YDj4rlisdg6f0yqJ29QhpEADeoyK5WjVFCPEnq_b_kddLA3orRicW031JLEXUeBZlJWlIvFph3DqNr5aWAL3jZ0fodd2ma1w3NBp9NPlX4vXaWAin5PwvRfupZKNIDEJY0R1a5w1tff-ZkG1jOaXVm07h3lvICrkRj2-3aqTkl4gzGPJVgAhylQAOBuYNutXWiweOH0i6NkDmE7AlNdLOsedonvUyjzOWSlGVA7BlLuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a7ded1522.mp4?token=UcvH4-M9yFUWUPt38V3INU0AguIx96VaAQ4IQYbXxXzMh_w960vIs-x9DUZarXeyVQdJjD3NF2ozxTytWzaFeLf6HiIDU7lAh9EkzOuPW-YDj4rlisdg6f0yqJ29QhpEADeoyK5WjVFCPEnq_b_kddLA3orRicW031JLEXUeBZlJWlIvFph3DqNr5aWAL3jZ0fodd2ma1w3NBp9NPlX4vXaWAin5PwvRfupZKNIDEJY0R1a5w1tff-ZkG1jOaXVm07h3lvICrkRj2-3aqTkl4gzGPJVgAhylQAOBuYNutXWiweOH0i6NkDmE7AlNdLOsedonvUyjzOWSlGVA7BlLuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇲🇦
سوپرگل تماشایی در بازی دیشب لیگ‌مراکش که احتمالا برنده پوشکاش ۲۰۲۶ میشه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/persiana_Soccer/22034" target="_blank">📅 09:07 · 25 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22025">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXp33-RLfJUNi-th7PiXmN8tdh_HDHQgut03SPae7hRKUjqJl4muRnEqzahyTy8sdlurwiB0GTNo6mHzM5y6KkTk9oX78DSPZrzDWygW7Qxxg0i8a3cx5D9fUBkeIBECEIRSt3N-ZNK1SUiwa-R1Q8rZs7zJtM5qO_gaP9DKKIPEmF0LNg12JLqxtq4jjtF122a_MVL8xLdqYyIo2y3n8cSAddikTk_8fopUWKYEAhF_u6EPBVIu1qa2glKjrEFxB46-mERCjzp3Z28PDPiQXvx40jFasNtVP40VR_t2cgTORZ6354oMMZX4GydmklotRD-s9nZ_N15DQKP-IdxTsQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/persiana_Soccer/22025" target="_blank">📅 00:31 · 19 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22024">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J9i69dFoXd2B1z-lFklTHa6wr9HGi6WMuV1jQIsMp0DlF2E0d-uqCOkgW34R8ZCoVe5Y3UEqP3UZpn5rITeesQp0JSdIh9LBbJ2UKEDpOmc5QRz2oA39ROSBtVCEbeyGr7F6yMPMGLpaQtaEVdJ1RHlBaSw-3YJYyN10vUkrzj3MuTAZjepKBmAOcdRRX1sp-FKm3Ep4cV6wjONonG-3hr0ne-F8yLzTM21PK-lvn6NB1cN1tf1gXgk_0xgtJ5jmWU6kKOfMpg8CRUcFBRLKzuS7Wqs7AcwYiw5kPFOj8Fbd-ZAgsqu2J_ilUIz689Xm1CRr047QHydHaYFcjXqkWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
چهار تیم‌ نهایی قاره‌ اروپا که امشب هم موفق به راه‌یابی به مسابقات جام‌جهانی شدند. ایتالیا هم برای سومین‌دوره متوالی از صعود بازموند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/22024" target="_blank">📅 01:10 · 12 Farvardin 1405</a></div>
</div>

<div class="tg-post" id="msg-22014">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPH8ETYGWoCotoNKdVG4n52OMpRamN5jwlQU4zD_pn8z0ftXcRk1y_58HUeELCoKHikIfukG2kAPGswSkvQHiugyY_6HDKM7-9WMwPc3hcCObPlNAloNKKR-zl2Y_Jy2l6K7_SQJi0Vb7LCYdXcuQvC6c9Tyn2h3dBbTyb-4BboVTgNO6XYPVK4Nz99Klnskco18aG55UWI1JrZZJBEckSwZqHhc5gH97ETAJGE-KCOa0biM9_7Tl8GMiA1Jy4unMmzkQBvj7RHEkM2YdlaK7gDqFII__X3HU6ArCTlyCFnwnHhM4N3h4GKbSKpW8HBdmgCxeZRpO44HMFrN0RPI-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏مثلث رجزخوان‌؛ یکی‌را ترامپ‌زد، یکی را نتانیاهو و آخری راشریکی‌زدند.‌عاقبت رجزخوانی بی‌پشتوانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/22014" target="_blank">📅 10:29 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22013">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IanADwHQxBiPFzgyyeJf8P2w2zGQ6vB8Gl9KXAkF9S7O_EnrlGBbLYHhffTqpEk4O7hK7_tKLaOWIeRtM8gzSXsA09doBMLyb6zOMMovOpqHTpxbNVRq_t_cmnm3Yk5P9qn0a2lEEnWTsPKerz3uc2esIOwPeYFnb9OI5nEel8yrlduZd8qXyGezMOWK0MnK-iy9H10pV5J5j4vu1-NQwYeRXajikOOSuehWDAIeCO9axM4dnKbMaTacAmxVqJzB304sEWsA1_oUM86O-tZ-Qi6v4gqjXcYRHozuhbUu6Xb_56mykdFNw9m4g-myKCUXnpCl3ho5pPai9CJDud2-8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ترامپ کشته شدن رهبر جمهوری‌ اسلامی را اعلام کرد: خامنه ای یکی از شرورترین افراد تاریخ مرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/22013" target="_blank">📅 01:26 · 10 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22012">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eElHPlCQzuKa6cQzzn6LKp6Lk98wzFHxQDwaGmimXevqLNLMApo_47B4Qz-bvbMqFh27slxK1arlmto06dvgVyaq_iSpcMwvqrm5IvE8MbRvSy3J13MGBF4kJ1LTL24Xsxe8HFiRCTgaorevyOminFYvVQlSOTO4tNe3hfCJmPYdK0n5_OU5MqKP9IhqS17dagvKtU-S0vXiE2lRVPY5ucyJieAl8AIc3gOUXxIyuNCtjtqwPfW9-jE-11VgEcQQORN7qX1GRoQoPf96UXhK09ctlWL_51IzJ5GKYxL5ZXn7IhgaF_rjJRDgA3fuRNZqzPYvxvAxWgSZXDDKXEs5XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
توییت جدید مارک لوین فرد نزدیک به ترامپ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/22012" target="_blank">📅 11:23 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22011">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nLQvvLgOshmO3vNlMQu--EXJCxyK1zrHGgpnz7R0cZx-W9HgewpB_TQzO5dTT67rsauL2ExEAqi0UrYVp24jiLZXOGWW0rar6RF_7u-tu-FotdK2WvRndfyk9wpUz6t2iQbJW9FxPT_zyVbMD1EL5KgCl5FyIKBVKPoSko1rnwwy4-xa2yDPv8r4mFkxp-gqpg6kwMXqcHzmbPITi5f5RteYrj7HloFKP2iQ4bn0bXjAqrnbp5jUv5A9IAXruOwzPisuUz4Fln9nP6wORS7ABWyQbg8SivtiDQogXx2az-1afJdQLEA7brbDRWzqsdsmJl3-NngbYhRRFWWSolXoYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گابریل ژسوس مهاجم برزیلی آرسنال کل این زمانو صبرکرده‌بود که انتقام‌شو از موسکوئرا بگیره:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/22011" target="_blank">📅 10:40 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22010">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUfxd1cnJ3dBnP6Xk5BigvoEz7gOEUrZYh6g29kcWSnLNLlHWVAYFw8HuptE34CPzxmtSQL2yYaixP83irhfA53KJxRqx_dZ6vYoj7ddw96tgfAp7Fgb74ihjb-F4hFsRdV372dqVzEz4k0WDF97u8i2bCGy9Ob2jHribBC6_X8I8qG2xj14_i9DVTu6tVA55GmA9Pv68k-FK70qCwVBHyGa4UXKOMWCstaYJzPeZKMxS_b6iGMIdV7toIPDf8MXR0h6A8mAO42P7W1AmZQ9KNYzinSN-8kQq1VuAfUpP7TpYGhdfI0G3dkGuhXtOp2ShKv6FEC14PbUYAJwUr4kMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی جدید استقلال از پژمان منتطری کاپیتان‌سابق آبی‌ها و مربی الشحانیه‌قطر خواسته که به کادرفنی‌اش اضافه شود. درصورتیکه پژمان منتظری به باشگاه استقلال برگرده وریا غفوری قطعا از کادرفنی آبی‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/22010" target="_blank">📅 10:20 · 09 Esfand 1404</a></div>
</div>

<div class="tg-post" id="msg-22009">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD5Nwt8OMaAFz_SUSuMW7JtnGXfqnqQfrTivFbWBjjd8X06Gn7wMYwLVX1tTXA1Czs70YsTF49UeQMhCP6kKpDUYGgl7U5OKQs3pgJ8KP4JfTxgN5dF8rvsFc4lvryDwOdJoASgdmjF17MWlIhCPJ3HK9JyLB0DZzxz_kMzmN_dPps1QSpy-wAvKAbFlDodCWQrtwbTtmf6ESFduZRYt1S0J42NHzk-O5bNLagLYcDTP9YwfW2AJNDq1vxzkrQmOpkhsSbUhIjysGZQhAArJuAg_MQXKfZj9hf_FdOlD2CTvyAptsj3Tp5dYzFkeeIW29LWQN0R5IcShFA-PxC9bNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
​​سال ۲۰۱۶
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۰
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۲
: رئال مادرید من سیتی رو حذف کرد.
🔵
​سال ۲۰۲۳
: من سیتی رئال مادرید رو حذف کرد.
🇪🇸
​سال ۲۰۲۴
: رئال مادرید من سیتی رو حذف کرد.
🇪🇸
​سال ۲۰۲۵
: رئال مادرید من سیتی رو حذف کرد.
⁉️
​سال ۲۰۲۶
: نوبت سیتیزن‌ها یا هتریک رئالی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/22009" target="_blank">📅 09:55 · 09 Esfand 1404</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
