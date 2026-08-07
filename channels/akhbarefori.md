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
<img src="https://cdn4.telesco.pe/file/gWifMOeti4AiOPQU_FI4zCHOaAdgxrqeXbzynWSQUzlWwRcfBCYJjWQLBiTFbhnTA0dLHo39_FkghtME6cOEjBmunTvvIsTTFdmshRgxwbYIShUBuv43MKGn45qxcmb9-sexRQAzyp7FGXVU_YPlnglqMQoJvF7RSvCvsy0bgJdu0E89DghmXRVX-gHahk-9-9TeinoVcwtDJA-RzYD9w9pqDo5091w87TLKGzn1Isef0sko3QxWZnq944Z61xBKrB8WgGwRPrxpyAYY_P4kVCIbsFgjUjcK0LZI0iVcTTDRNr4OTtCJxm_MWkEQAZH_SSnjvlL_dkUgiFv1-C7rzw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.02M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-17 02:32:12</div>
<hr>

<div class="tg-post" id="msg-679299">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromربات هوشمند اطلس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbMJ3d0IrpmIh8_6EE59HQOSw1shAQVHAZJWWnLZ9i35OPysPdbOxPyqTnI8-U5R6r-ETocndkrwRqJCEg_9zDuf4sI7YaJq2gNBD-6u2pnV_3NNM5vVyCygxYZG2Egt7kw8knE9_1Fw84R_yJmK7EzqnT24aCN0tp9sIrIzLAnh0LyDfCijar_SDqJlyC-buJLTtxwKGUwtNLTrGIPVkNs6NgUvlDARrcuhvysLa0piGqGCbW6bcRtW_4b9V_Vxz4CfNndZTECvU-iVSV150Kbf5FyKO0LTk2c7qQGpwW53r8Gh2Fhx5JnHhtpmloYX9-ilDVv-RmqUB6iZsfFN4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📉
📈
بازار می‌ریزد؛ اما
آربیتراژ
متوقف نمی‌شود
وقتی معامله‌گران از ریزش بازار ضرر می‌کنند، ربات هوشمند اطلس اختلاف قیمت بین صرافی‌ها را به فرصت سود تبدیل می‌کند.
✅
برداشت سود روزانه
✅
گزارش لحظه ای معاملات آربیتراژ
✅
شروع سرمایه‌گذاری از ۵ دلار
✅
بدون نیاز به دانش ترید
🚀
مشاهده عملکرد اطلس:
@AtlasSmartBot
اطلاعات بیشتر در کانال تلگرام</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/679299" target="_blank">📅 01:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679298">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">♦️
ژنرال‌های ترامپ به دنبال «راه خروج» از جنگ
🔹
شبکه سی‌ان‌ان در گزارشی فاش کرد که یکی از فرماندهان ارشد نظامی در حلقه نزدیکان ترامپ، به‌شدت در حال بررسی گزینه‌ها برای پایان دادن به جنگ علیه ایران است.
🔹
طبق این گزارش، گزینه‌های نظامی آمریکا برای پیشبرد جنگ عملاً محدود شده و مقامات پنتاگون را با چالشی استراتژیک مواجه کرده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/akhbarefori/679298" target="_blank">📅 01:15 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679297">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
برکناری شوکه‌کننده فرمانده لشکر پنجم ارتش آمریکا در اروپا
🔹
شبکه خبری ای‌بی‌سی از برکناری ناگهانی و غیرمنتظره ژنرال «چارلز کوستانزا»، فرمانده لشکر پنجم پیاده‌نظام ارتش آمریکا در اروپا، پیش از موعد مقرر خبر داد.
🔹
این ژنرال ارشد در حالی از سمت خود کنار گذاشته شده که حدود دو ماه تا پایان رسمی دوره مسئولیتش باقی مانده بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/akhbarefori/679297" target="_blank">📅 00:17 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679296">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">♦️
ادعای حکومت جولانی: یک عملیات تروریستی را در منطقه «سیده زینب(س)» خنثی کردیم
🔹
طبق اعلام وزارت کشور حکومت جولانی، نیروهای امنیتی با دو تن از اعضای گروه تروریستی داعش که قصد کارگذاری بمب داشتند، درگیر شده و هر دو نفر را به هلاکت رساندند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/akhbarefori/679296" target="_blank">📅 00:06 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679295">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjJafNuoBjePNwrYMsaSK66tvj59nKuRfeB2WEFufWN1ZOIAYNIQnBcda09PY0KcYqUIXuQekfN65VoGLYna_estqlZLURwc3tFY8AK5OU5htoXj-FGIWFf3yuiNp7bQn1qiC1YQjWhRPD2_gBB1xDsou_mMKYEJNnyGb6hWPbSPo-bNqAHcQjLxwmbMhYz1gDckIfLsmWK3yT2ES4VNwk3nXFe95OnjoCFY8KptfWWh6pxJLMxwfFb7s6_o_6gXdZlykl06e9g8pTzOV9yh3_IDS1hCj2TSSf_sv-icAHQfGGM6sqNMTgq8F5JF0Wx-STEedwoU7Dy7zPqtdkjH9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یک زن هندی پس از سال‌ها کوتاه نکردن موهایش، با موهایی به طول ۲.۷۱ متر نام خود را در رکوردهای گینس ثبت کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679295" target="_blank">📅 00:03 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679294">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ساخت سالن رقص ۴۰۰ میلیون دلاری کاخ سفید با حکم دادگاه آمریکا متوقف شد
🔹
دادگاه تأکید کرده است که رئیس‌جمهور آمریکا بدون تأیید کنگره اختیار اجرای این طرح را ندارد؛ طرحی که به گفته منتقدان، بخشی از هزینه‌های امنیتی آن از بودجه عمومی تأمین می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679294" target="_blank">📅 00:01 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679293">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iA1JWeZ1RXuH3qgN_m71hOE-EuCOm9m5aOocKqtg9qnSuEgAQq05YRZoEi-PiPBEDROb0EALuTLedzY7AOqfMKuW7YaRX_cnxpilS_J9dxVTByGpV0LU8rr1jlDaP3HBZe_luxj4loy8pNMtUBxtqrPvrwNATwn4uxzbB7V35PJVqj0vyqltmtofpNxPUYwSWso70mhE0H3ja5lJGKE2sklgFdGe78ydfZv7-U_qkF6FtnSTLwKgvRBZoHeiGQlUQdIlf4lz6-ZQSjL9lvj5Ri67KK1Sk5VRyJylng5g_KnA0eKQ9w0tIzkOKx15r6Q910SlcJyOhzpwnS7_0ph6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/679293" target="_blank">📅 00:00 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679292">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32bb8067c5.mp4?token=X3mh7xduqLXAm0mbG5hn7PGg2Ys1FUUURZvNtzfMyyEjs46X5jXY3o6Pf3qjLuFM5ZC6WPT_Fxc9ZxfWocxeiHepHLJ8Q7eolwhzBzIDVWZekYGfhE2c_IE9pwLPCIldh55c58q8zTl_6LIhEmyEbm9Sd_jaXAwDRAMPPaTuNzfQTDzuKM2PnNjzR9OEexBL8G4rZ-Ww95oI9dv1mjozS0S4Ld23S98Z9zchr3W0vOXxf7C4pfd5M9r0TGThGo8fgX7vLTVHWL5QYohDghE8qcbPzTCX8dw_dJf1cXEng3T3tCu0ghQouLtE4mKP_rp2sGxwl5XHcze7izjnYysiRr4atY9ddICHv0wwEZrTV8eGwP8p2Qww2smVenodffaMEf_ZCCtCn8L02jasmHOPuxxtTu8i_zGMIW2PnGZ1BVHGOfFaCQE-9mpjYaZ7hai8AbcFZn06sBn4M98BzA76_NJ8qyanLt0q5cWsA4aRLMc1Dg-HGWH_dgg20DJ2J3s42CcOqFa2PruoQGd2RlhfXk-s-irrnA4TdQGOxcLpZJVwmqB7F083AMnYrlynQJyM4vBAoz1bKPxtnxLUOwpptVa9EP5-rCm3Olo40ss669Wa4wf0-4hOi06efEwNdxkXy4EbS7FWkMg8H9BJJXjggpiNP5YnHE8xhEBmzhTnW4s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32bb8067c5.mp4?token=X3mh7xduqLXAm0mbG5hn7PGg2Ys1FUUURZvNtzfMyyEjs46X5jXY3o6Pf3qjLuFM5ZC6WPT_Fxc9ZxfWocxeiHepHLJ8Q7eolwhzBzIDVWZekYGfhE2c_IE9pwLPCIldh55c58q8zTl_6LIhEmyEbm9Sd_jaXAwDRAMPPaTuNzfQTDzuKM2PnNjzR9OEexBL8G4rZ-Ww95oI9dv1mjozS0S4Ld23S98Z9zchr3W0vOXxf7C4pfd5M9r0TGThGo8fgX7vLTVHWL5QYohDghE8qcbPzTCX8dw_dJf1cXEng3T3tCu0ghQouLtE4mKP_rp2sGxwl5XHcze7izjnYysiRr4atY9ddICHv0wwEZrTV8eGwP8p2Qww2smVenodffaMEf_ZCCtCn8L02jasmHOPuxxtTu8i_zGMIW2PnGZ1BVHGOfFaCQE-9mpjYaZ7hai8AbcFZn06sBn4M98BzA76_NJ8qyanLt0q5cWsA4aRLMc1Dg-HGWH_dgg20DJ2J3s42CcOqFa2PruoQGd2RlhfXk-s-irrnA4TdQGOxcLpZJVwmqB7F083AMnYrlynQJyM4vBAoz1bKPxtnxLUOwpptVa9EP5-rCm3Olo40ss669Wa4wf0-4hOi06efEwNdxkXy4EbS7FWkMg8H9BJJXjggpiNP5YnHE8xhEBmzhTnW4s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آذربایجان غربی؛ سرزمین تاریخ، فرهنگ و تنوع
🔹
از موقعیت جغرافیایی و مرزها تا زبان‌ها، اقوام، شهرها و طبیعت منحصربه‌فردش؛ در این ویدیو چند نکته جالب درباره این استان رو با هم مرور می‌کنیم.
#اخبار_آذربایجان_غربی
در فضای مجازی
👇
@azarbaijan_gharbi</div>
<div class="tg-footer">👁️ 30.9K · <a href="https://t.me/akhbarefori/679292" target="_blank">📅 23:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679290">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RVhvCRer1Pv2vts4KZKy1chiXcRM98nojMnzNgQK3RPB88Qwy_caKBUN9aIz5RAWQw_PFfTpU6dK6WIvW0bFgubdwx29Cqa_CA0GKU7mRNH4ZPSLc13SRjnEYDLYUniqxGOsR26mAanhz4GKZtkkJl5gsZjuyZDrAUFOMTHAgCV9hrrRPap2UUUBGSsnw6AlOSLMkkW_E_fJITyQmR-r1YfLH48LpSyzROAJ6pCgBJDgUF82AdK1AKP9YgSn_VdlbneJKIu6JAbJQj8IDnMYM8tKyA3HQiG8lS-EB42AXtMQkVan1pI7JLXTFYjmruXujrURLv3qlpOYdUm8LEmYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخورد ۴ تن آهن آمریکایی به ماه
🔹
یک قطعه ۴ تنی از موشک اسپیس ایکس به طور غیر عمد به ماه برخورد کرد. به ادعای کارشناسان این اتفاق هیچ خطری برای زمین نداشته اما انتظار می‌رود یک دهانه آتشفشانی در ماه به جا بگذارد.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/akhbarefori/679290" target="_blank">📅 23:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679289">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
#چند_خبر_کوتاه
🔹
ادعای سی‌ان‌ان: پهپاد که در فرودگاه آلمان کشف شد، متعلق به سرویس‌های اطلاعاتی روسیه است
🔹
مدیر سابق مرکز مبارزه با تروریسم: ادعای ساختن سلاح هسته‌ای توسط ایران بهانه‌ای تبلیغاتی بود
🔹
ارتش رژیم تروریستی صهیونیستی بار دیگر به خاک سوریه حمله کرد
🔹
زیردریایی اتمی «یواس‌اس سن‌خوان» آمریکا  پس از ۳۸ سال خدمت فعال بازنشسته شد
🔹
سازمان ملل: منتظر نتایج مذاکرات درباره تنگه هرمز هستیم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/679289" target="_blank">📅 23:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679288">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AVnW9FtOf6qUE-lp9Qp3Yjyfs3jEAncA3-Tqw3o_2B7lAQ8izwbs2Nx9LxJ8Y8wBcf9kdTD29zimkcztBbAyMV59KCPSc9mOcp0oKqMyOp1TZ3Is7ZPnnCdKmXrR0SJV0s23dACsn5d6PhofnJXxBtTjMNpoqCfBHa6HNite1UF-54zrvQb0hGZPKZDgrzZley0K6KobwqUdGqTSEYk9p7_0ZQ96DwZD7WJNUbjsFRwBdLtkCTn7JFebl5D2wv455SFIIfwxKBKrwpUFvJXJMsw6ttw6R1p32kguWGVc5kcEcz5E6uhe2-8p9bSn9KJqktM3BrHpH5e-56QN7i8lZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راهنمای فوری لکه‌بری؛ هر لکه با یک روش ساده پاک میشه
🤩
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/akhbarefori/679288" target="_blank">📅 23:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679287">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">♦️
اعتراف شرکت نفت امارات: ۱۵ شناور ما در جنگ علیه ایران آسیب دید
🔹
شرکت ادنوک، غول نفتی امارات اعلام کرد که از زمان آغاز جنگ علیه ایران، ۱۵ فروند از شناورهای این شرکت با موشک یا پهپاد مورد اصابت قرار گرفته‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/akhbarefori/679287" target="_blank">📅 23:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679286">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2d3a7d45a.mp4?token=XvE7ZQ3KN1L3VnZgmTmHcP4qshALiHocUcZGTVl56uYPDjMssst4zZC9BUDsFuUt9tc-Y3AGVeZ-Ybe18zxgyYJ-1sNjob8zUHB3iWjeMcLzI-euIvue5LszXl2AlDY4bRDnCLQestQr1f2tS5zDovq8DRlB-qscpS651-nybwHdD0CM_Nb30lIkQyhViqdQVsx0ApZ7jt4mAL5TA3s8GLRFQTWGLpgjd05yMp1j-cRwyK0_XZd170CMns4X8KBFzZaT0sRsTe0_AzCcIXc1eci437imY_Su7pJqAkqmtsZZnqlYkcPvCL-IySthSeA8oxJxQ6XPLRy4_0546mUn7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2d3a7d45a.mp4?token=XvE7ZQ3KN1L3VnZgmTmHcP4qshALiHocUcZGTVl56uYPDjMssst4zZC9BUDsFuUt9tc-Y3AGVeZ-Ybe18zxgyYJ-1sNjob8zUHB3iWjeMcLzI-euIvue5LszXl2AlDY4bRDnCLQestQr1f2tS5zDovq8DRlB-qscpS651-nybwHdD0CM_Nb30lIkQyhViqdQVsx0ApZ7jt4mAL5TA3s8GLRFQTWGLpgjd05yMp1j-cRwyK0_XZd170CMns4X8KBFzZaT0sRsTe0_AzCcIXc1eci437imY_Su7pJqAkqmtsZZnqlYkcPvCL-IySthSeA8oxJxQ6XPLRy4_0546mUn7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به حاشیه درخت‌کاری‌اش در پاکستان/ من بلد نیستم فیلم بازی کنم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679286" target="_blank">📅 23:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679285">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHLIeWipcDUqk3aOXTUl6bMH_gqboRn-cTamSXTFElEsFMqQySv_VsRo0Xl7-1seP9i1DsBiBMOnXsuSg02jNXiqWZc1jL9sqiSvquEHm3_vxuAIam1wHEkPdzTBfTkmHbrADWoW29wsKkR8i7siY4Y-aT5piafkbwrDd7vyb1Yexyfy01ossjjKvqPE1ufQR59ju7Z_IdUV1cj0Ygujz4pW0gU1E1juOiO0RpmRodLTCie6m1j1E5svfq1jlMFft0OzEBMuYyX1zKL21I9EvsrLfuKnIFs_E7bSjJD12qNhKwQxYrCKYnAAWZu6P42oeHbqh9mPv0bPV0wYzFUnWSPU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7910a5b25a.mp4?token=BZjaJTTjZPGfIaeMqgCTGEo0dygRkZ1kLM5VihNgus-CSxyZJ_wqA0ib1HpDV6aFft-00XyMUI_h0Pjcw7QTQI8PUPVJyNBLcMe3HutcakzO2rUiHWiUhjIIiyMnZHWzi89TqOldlohRj5A1WblZtY30Y1aHcpkYexlFecLjB5xv2QSUgoweEBIdtcNbB0gBi7o8r7HEvdkZxRgKAIoRgiMQFGZzXV0EejQRH1a4ZxG2ica4ueYQs3GSM9PWpPLNPRETIul6boBlfTCc4T3wmlF6lyipVZLV_8yAUNuzm5VuJcei0qWshU6gDvbQzVcGuQyRJ4FgZyi0sJgTfU_eHLIeWipcDUqk3aOXTUl6bMH_gqboRn-cTamSXTFElEsFMqQySv_VsRo0Xl7-1seP9i1DsBiBMOnXsuSg02jNXiqWZc1jL9sqiSvquEHm3_vxuAIam1wHEkPdzTBfTkmHbrADWoW29wsKkR8i7siY4Y-aT5piafkbwrDd7vyb1Yexyfy01ossjjKvqPE1ufQR59ju7Z_IdUV1cj0Ygujz4pW0gU1E1juOiO0RpmRodLTCie6m1j1E5svfq1jlMFft0OzEBMuYyX1zKL21I9EvsrLfuKnIFs_E7bSjJD12qNhKwQxYrCKYnAAWZu6P42oeHbqh9mPv0bPV0wYzFUnWSPU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای بازگشت یک زائر گم‌ شده در سفر اربعین به ایران در برنامه پرچمدار
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/akhbarefori/679285" target="_blank">📅 23:15 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679283">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dyNiTMuJMIXGtV-8-OkuaNMbA-79ENh0jEa3pQPaXFv2EnVhSbav8yI98kx0TCC01jNNxJ13VtzT_S6ao3Xq0UXXCIcbaaSG8Um1017opFNzY6A-3W0e4JccG63DkR7G8nFPnegufwsXcAS53Nq2IvK20un--GL_kMSMuwFdsRlKSQrtT_Jf2lTYtsHYCSJB-1XBUnjiFL8ZGgeY_TFgEuJtIv9J9sMyp0Ybi6AJ4oJSArNXanIG569N5EUFSJvKQvBRkZfU-bMaYP1uVhwRpxHPHDiVQwUaqLhMTVbZhb2BJya5zlGMON19L9xC0kDdO1wSQAqRP6c5V_y36Hlh1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mCwsDn-E8N3DXh6bfTTwpr5rXMNaIP-eCBEYGbfWA6bqymCstUsGfsQQ_KyABsMxuj5wkZhS5RlpZD7VQbEfTSl0G5I1NNEysXDjfqGrwLUW74ca_6zEjpxJhOKucm4pBEPe3bs-Ouk-hw87YNUTwCUmtaYvCTZDCME36guGdjlqtGNVJDDKW9jSNfc5cODpGLpUNgQt-wrJJeDXgrBOj2xiggirKa_wnCqR9fbR19wAHhLfDm2h4HrToWWpR3XafwylIHKaFSAoqwpv_S3OY39965FPbkwsZ8BIIiy9NnzVlkSNWdpDxIkwcokVeY08No21Obc1KYCqYAIhoJ5qig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵۵ ساعت شنا در دریای بالتیک؛ بدون توقف
🔹
یک شناگر با ۵۵ ساعت شنا در مسیر دریای بالتیک، رکوردی قابل‌توجه از استقامت انسانی به نمایش گذاشت. وی از ساعت چهلم بیداری، دچار توهم‌های دیداری شده، اما همچنان به شنا ادامه داده و مسیر را به پایان رسانده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679283" target="_blank">📅 23:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679282">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔹
خبرهای متفاوت هر روز را در وبسایت خبرفوری کلیک کنید
🔹
🔹
ذوالقدر همچنان دبیر شورای ‌عالی امنیت ملی است؟
👇
khabarfoori.com/fa/tiny/news-3236165
🔹
ائتلاف نظامی عربستان - ترکیه - پاکستان/ یک مثلث شوم برای محاصره ایران؟
👇
khabarfoori.com/fa/tiny/news-3236126
🔹
نتایج آزمون مدارس سمپاد اعلام شد/ ثبت‌نام پذیرفته‌شدگان از ۱۹ مرداد
👇
khabarfoori.com/fa/tiny/news-3236142
🔹
آیت الله محمدباقر خرازی فتوای کشتن بی‌حجاب‌ها را صادر کرد!
👇
khabarfoori.com/fa/tiny/news-3236163
🔹
رقابت زنان برای ازدواج با سربازان خط مقدم جنگ | ظهور عجیب «بیوه‌های سیاه»
👇
khabarfoori.com/fa/tiny/news-3236085
🔹
اخبار لحظه به لحظه جنگ ایران و آمریکا
🔹
https://share.google/8EImhrm9fBFYjsyZr</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/679282" target="_blank">📅 23:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679281">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db145f35f7.mp4?token=n5sgZfC5KO5BBXJlk0gGe48IN_uqXjnzXfHN9rdLktm4LXNolgvrwsLbEmWKNwpIf0hib4sgNvxzg08ViAAZFWm5FKbl_lDhOvtlsPR0aSlzGXKL0Mg-Do-vYYjQcOUz3k33ADO0B1j8NLjIGVpByke_XHLm0F0j-r-ozcv4NXrw6TRRAk-S8arpUbax6KTvelz5-T6Q3uiUXgKNSVw5Pe1FHykqZlt5Kk5jbmezLoNY3OGOsp6WYfZFErM0viaqqw1QwEgdJy8Gm-uSMeDZm0SbPALQDlXe5H3wc3zRLk9HI7PKe55v4NC7PeHCTtrmSQf8m3MVv8JutxpYc45JUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db145f35f7.mp4?token=n5sgZfC5KO5BBXJlk0gGe48IN_uqXjnzXfHN9rdLktm4LXNolgvrwsLbEmWKNwpIf0hib4sgNvxzg08ViAAZFWm5FKbl_lDhOvtlsPR0aSlzGXKL0Mg-Do-vYYjQcOUz3k33ADO0B1j8NLjIGVpByke_XHLm0F0j-r-ozcv4NXrw6TRRAk-S8arpUbax6KTvelz5-T6Q3uiUXgKNSVw5Pe1FHykqZlt5Kk5jbmezLoNY3OGOsp6WYfZFErM0viaqqw1QwEgdJy8Gm-uSMeDZm0SbPALQDlXe5H3wc3zRLk9HI7PKe55v4NC7PeHCTtrmSQf8m3MVv8JutxpYc45JUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اگر بتوانید صحبت‌ها را کوتاه کنید ممنون می‌شوم، چون ما یک جنگ برای پیش بردن داریم
🔹
ترامپ برای فرار از پاسخگویی به خبرنگاران، جنگ را بهانه کرد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/akhbarefori/679281" target="_blank">📅 23:05 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679280">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a3c86a56e.mp4?token=TZCNC40oslAz4stwdXugwylsJTeBYnFrz_DqFD5--X_ncqQGf3mSkqo4Az8l8n8Wp8YhwyrFJs-bWeg44PJCSq_vqlCWJUVYzK2sa3UrEWxvCBQh4TdXEcjSmPgv40fPVXzmeR9Up6PTpXklv7Kzt7YNdnevvKuMKi2ueINbxd9xNJkKjrW2-W7Maj27UZY9t9HypJFksD9RZiqoVldYd9JLqZtZvJu69XEB1-4IspbEHO2BkpAizYAfRPpOMyE-g5WgKKmU1CS7ijpFcgLsczo0uO8F7nBbWx3Gu5jUQngbfPBcQRv3NsV45yDMFe6osLTD5-v09DPaTaMl6hmPHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a3c86a56e.mp4?token=TZCNC40oslAz4stwdXugwylsJTeBYnFrz_DqFD5--X_ncqQGf3mSkqo4Az8l8n8Wp8YhwyrFJs-bWeg44PJCSq_vqlCWJUVYzK2sa3UrEWxvCBQh4TdXEcjSmPgv40fPVXzmeR9Up6PTpXklv7Kzt7YNdnevvKuMKi2ueINbxd9xNJkKjrW2-W7Maj27UZY9t9HypJFksD9RZiqoVldYd9JLqZtZvJu69XEB1-4IspbEHO2BkpAizYAfRPpOMyE-g5WgKKmU1CS7ijpFcgLsczo0uO8F7nBbWx3Gu5jUQngbfPBcQRv3NsV45yDMFe6osLTD5-v09DPaTaMl6hmPHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعضی‌ها با اطلاعات ناقص درباره همه چیز نظر می‌دهند/ این افراد جامعه را به انحراف می‌کشند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/akhbarefori/679280" target="_blank">📅 23:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679279">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ubX59O-aRbRZ_FxngK975Vh4QatJ1jNn1v6yO5hzfwC1CUnTh0qaX3JpzKwt5NLQKMbS5Ewv1pWQ0u3JsGSvBOha9G8Mp88WhObsbTgVibpui1SCDHiI2s04MpPKz3jP8QS6hM5wq20XOEKhYO6ZUnyRzPi93VD4ySCFxbtht62QJzce30KJo2wDq9oYFPbUQNW5GD3qldpfYJG2OXoPvztN6T1McGXL5g0MvZJt8CpYZ3PsHj_GceXyJqz56jDmMkOkqrzMDGJ1ghtLE3K6yedR0L4zPpgHg2R4w3ckrMWA9DjldfLsSRvvv8OzX9pUTKz9EgvPK6VwRiqQNvQH9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فروش بلیت رفت و برگشت زائران دهه پایانی صفر از ۱۷ مرداد آغاز می‌شود
🔹
معاون حمل‌ونقل سازمان راهداری و حمل‌و‌نقل جاده‌ای از آغاز فروش بلیت رفت و برگشت زائران دهه پایانی ماه صفر از ۱۷ مرداد ماه خبر داد.
🔹
مهدی خضری گفت: با توجه به پیش‌بینی اوج بازگشت زائران از ۲۳ تا ۲۵ مردادماه، توصیه می‌کنیم مسافران ناوگان حمل‌ونقل عمومی جاده‌ای، بلیت برگشت خود را از همان مبدأ سفر و همزمان با بلیت رفت تهیه کنند.
🔹
وی افزود: زائران می‌توانند بلیت برگشت خود را از درگاه‌های فروش بلیت و [*سامانه سپاس *](
https://sepas.rmto.ir/landing
) سازمان راهداری و حمل و نقل جاده‌ای به آدرس
https://sepas.rmto.ir
تهیه نمایند.
‌
🔗
لینک خبر:
https://rmto.ir/s/mfan7J9
⬆️
با پیشنهاد به مجله از کانال راهبران ایران حمایت کنید
#اربعین_حسینی
#چشم_به_راهیم
#سازمان_راهداری_و_حمل_و_نقل_جاده_ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🌐
@cheshm_be_rahim</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679279" target="_blank">📅 22:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679278">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">♦️
ادعای
رویترز: در صورت توافق ایران و عمان محاصره دریایی برداشته می‌شود
🔹
یک مقام آمریکایی در گفتگو با رویترز مدعی شد که پیشرفت‌هایی در مذاکرات میان عمان و ایران در خصوص تنگه هرمز حاصل شده و انتظار می‌رود به‌زودی توافقی در این زمینه شکل گیرد.
🔹
بر اساس این گزارش، به محض اعلام توافق برای ازسرگیری بدون مانع کشتیرانی تجاری، ایالات متحده محاصره بنادر ایران را لغو خواهد کرد.
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/akhbarefori/679278" target="_blank">📅 22:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679277">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16b40ffe4d.mp4?token=WIuDlL2ijH6RSCNVm-bis-I93z-Fl0WiilmXxHwKSNHtRbcn9XbK-DnLv9bqpIGapKqFyckjoIIEyLAlSj1QOAnSjyCaRYNjYFtelT6zjDgFFCPG6B0_7LC2y9nHf3lwBSQEMJSZx-RTW22olw9-qv8Y7MTgHsVz7iGBEayqeFyz39cdc76Z3WeCnRxsgHVKGOXv3HUmcQg6rAczHUsTE0g0VD8XRafTBW9sdBGjvlL9ajk7pxi-Km-fHBHBiScAwRAFn-dSQryMNxWVMJPnFgcG6bP_lPYmtlbqFVH_Cw1IzU9Y8oABRrM7lJHt4FPPgZqixbj1kI6b-QEEucn1ayU0fK4Z-9fTQR9al_O5CijH6tp4ZkgeUW_bXnjn5RB3N7kK7bX7qpUjSrOcFSLCR4gxaiJnRgMlpDSakGUT10lILG34_pfCsNeYzalnQrWivbQ34p59KNo0cBBqw5_FNFup1mOiLlgaHY4F68_tMzA6DagnEccFtao_xf3R5Kv-MnVpSsfkuMqO0iuz9yYatuTCQ9U3Bm871ysKOd89uWkCjrtuaZ5Z7NaNQBwecg-28JCl-YjJ2dZ45IDQafUbmgxrSzEE9W1ahvZnJlKGDd44-GCj0Eg7_m1Kpq-AqBc73-hdpn4w9yYIJPAOP9o0jIHXZE39NNzs5UMhTND365w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16b40ffe4d.mp4?token=WIuDlL2ijH6RSCNVm-bis-I93z-Fl0WiilmXxHwKSNHtRbcn9XbK-DnLv9bqpIGapKqFyckjoIIEyLAlSj1QOAnSjyCaRYNjYFtelT6zjDgFFCPG6B0_7LC2y9nHf3lwBSQEMJSZx-RTW22olw9-qv8Y7MTgHsVz7iGBEayqeFyz39cdc76Z3WeCnRxsgHVKGOXv3HUmcQg6rAczHUsTE0g0VD8XRafTBW9sdBGjvlL9ajk7pxi-Km-fHBHBiScAwRAFn-dSQryMNxWVMJPnFgcG6bP_lPYmtlbqFVH_Cw1IzU9Y8oABRrM7lJHt4FPPgZqixbj1kI6b-QEEucn1ayU0fK4Z-9fTQR9al_O5CijH6tp4ZkgeUW_bXnjn5RB3N7kK7bX7qpUjSrOcFSLCR4gxaiJnRgMlpDSakGUT10lILG34_pfCsNeYzalnQrWivbQ34p59KNo0cBBqw5_FNFup1mOiLlgaHY4F68_tMzA6DagnEccFtao_xf3R5Kv-MnVpSsfkuMqO0iuz9yYatuTCQ9U3Bm871ysKOd89uWkCjrtuaZ5Z7NaNQBwecg-28JCl-YjJ2dZ45IDQafUbmgxrSzEE9W1ahvZnJlKGDd44-GCj0Eg7_m1Kpq-AqBc73-hdpn4w9yYIJPAOP9o0jIHXZE39NNzs5UMhTND365w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره پزشکیان از ساخت خانه‌های بهداشت با همکاری بسیج زمانی که رئیس دانشگاه علوم پزشکی بود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679277" target="_blank">📅 22:48 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679276">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9d1f13f40.mp4?token=e8p8MoIt8U1_n4gEGPnGrzCRMohFupQdSTBpTTwUTtM-gjDDgRljgSKF7d8vsaAifoimJ4Nb8eMh7DA8VSfORWqOeVqTYi0-vGmNcHOXBjaXGBgP3hSFBDsHyLIq4r_3zQT7KPxpneVOJ-hHIfKPhXwihwlk4KGBCLIvj-KSe_CdJ2aJCsYtNfy2wUyhlQ7eUVcOI4_jyWaCe-_ilA1oOGY5Y1h4gS-EIJ0xyrR7oW2bgJz4mWhOGYpX0HjZwXEiwltWJjTDmY03ZvN-mkfUzkExNdI7ESRXwuGrKmfOf0VSdK8g1au3b0nZAH803Uka8SK0HoRRSq5IBLxNLeRjhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9d1f13f40.mp4?token=e8p8MoIt8U1_n4gEGPnGrzCRMohFupQdSTBpTTwUTtM-gjDDgRljgSKF7d8vsaAifoimJ4Nb8eMh7DA8VSfORWqOeVqTYi0-vGmNcHOXBjaXGBgP3hSFBDsHyLIq4r_3zQT7KPxpneVOJ-hHIfKPhXwihwlk4KGBCLIvj-KSe_CdJ2aJCsYtNfy2wUyhlQ7eUVcOI4_jyWaCe-_ilA1oOGY5Y1h4gS-EIJ0xyrR7oW2bgJz4mWhOGYpX0HjZwXEiwltWJjTDmY03ZvN-mkfUzkExNdI7ESRXwuGrKmfOf0VSdK8g1au3b0nZAH803Uka8SK0HoRRSq5IBLxNLeRjhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: وقتی می‌توانیم حق‌مان را با گفت‌وگو بگیریم، چرا باید بجنگیم؟
🔹
با گفت‌وگو توانستیم جنگ لبنان را متوقف کنیم، محاصره را برداریم و برخی تحریم‌ها را کاهش دهیم. عده‌ای می‌خواهند بجنگیم؛ همان چیزی که اسرائیل می‌خواهد تا ما را وادار به تسلیم کند. ما کوتاه نخواهیم آمد، اما وقتی حق‌مان را می‌توانیم از گفتگو بگیریم، چرا باید همان مسیر اسرائیل را ادامه دهیم؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679276" target="_blank">📅 22:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679275">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">♦️
پزشکیان: کسی که نمی‌داند همین‌جوری می‌گوید بزن، تبعاتش را هم باید بداند؛ در شورای‌ عالی امنیت ملی ۱۲ نفر از موضع ما دفاع کردند
🔹
در شورای امنیت ۱۲ یا ۱۳ نفر حق رأی داشتند و ۱۲ نفر صحبت و از موضع ما دفاع کردند. کسانی که در میدان ایستادند، آدم‌های ترسویی نبودند؛ همان کسانی بودند که این افتخار را خلق کردند و ما به آن‌ها افتخار می‌کنیم. همین افراد بودند که کشور را تا امروز با قدرت اداره و از آن دفاع کردند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/679275" target="_blank">📅 22:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679273">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be2bd08c43.mp4?token=vXfxsXWbgwiw8LZ-rHXO-CUgCyPJRSOytjnGIi3IVNXjxfLWJmExbGqVRyHlRIO86z7u-Z6jCb76jKU-TDXbgSnlILja2BQmIAg-o411tVxvZbGBIJaJq5HEj79u_uxJLPktiK-bmZ71pOCXYQA6LvZ3shcat3-6-Hw185xYiYnW83Chq8KrIljhI0H4jQ6mlC4chci5xK6sAtjZEtIYABZu6wdgeX9Rj_1F0hSoYPVNHvVbMe6sqoYQEqRqsoyIeyjM_OEiy6nhp2_mVj5TnPgufrfEwcXp8DsjMy30vqys6Y8MMJMXM902wMWCDnIHj48Kt0aMys37rUTVu2ZzUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be2bd08c43.mp4?token=vXfxsXWbgwiw8LZ-rHXO-CUgCyPJRSOytjnGIi3IVNXjxfLWJmExbGqVRyHlRIO86z7u-Z6jCb76jKU-TDXbgSnlILja2BQmIAg-o411tVxvZbGBIJaJq5HEj79u_uxJLPktiK-bmZ71pOCXYQA6LvZ3shcat3-6-Hw185xYiYnW83Chq8KrIljhI0H4jQ6mlC4chci5xK6sAtjZEtIYABZu6wdgeX9Rj_1F0hSoYPVNHvVbMe6sqoYQEqRqsoyIeyjM_OEiy6nhp2_mVj5TnPgufrfEwcXp8DsjMy30vqys6Y8MMJMXM902wMWCDnIHj48Kt0aMys37rUTVu2ZzUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا پزشکیان به جای قالیباف تفاهم‌نامه آتش‌بس را امضا کرد
؟
رئیس‌جمهور:
🔹
کلیات توافق نهایی شده بود و برای افزایش اعتبار آن، قرار بود امضای نهایی از سوی ترامپ انجام شود تا امکان عقب‌نشینی از توافق وجود نداشته باشد.
🔹
اما کمتر از ۲۴ ساعت بعد، روند مذاکرات به‌طور کامل تغییر کرد و توافق به سرانجام نرسید.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/679273" target="_blank">📅 22:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679272">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=YGOIxQc_KL9YGFXDGIZB0BnqQT3NY7GCoXroNWtOJgrzGw2g-gPzPraXztmjAtGq05WSgt0JnkcPpvDVIiCr7DRxlcPby3ygMaTZ9p02Eze7I3v6sEgcPWoYqhPrC402jlo_DnI6ElvQ5OPDR4wDyC680Oma-0g3PguwOrZMxytFLohXuCzR26_BxFadKS4KJNpezjECvzLCVl1QD-CYcvCyGgHdiTy5Ka9dExSmylPLzVfiGR5g7sqyQ4ZNR3qL_pVZPXvzXDQfWws_N47wGkahLkimTZMtynjcHmP_evV1ZXDD_VTEZgvaAsrOc98gQTXJjnqkr1yiT8FTitUYPxxyZcjB_2VVBtoTQ3FtLaeWKjSxcfZCN-EXyd4QpO5ZMEMk4kFiK62p_pHRIL7f5kwE49dAjw-JbSpZ-R9G-7JHRfjg0PXhJFVqf86xR_0_4eP5Yos6UaMg3ahRhwreRcl1SCgpYXYPyixiDMgzrHYtEoVRseZVQgRUofMfZqp-_k5lwu4ETXczpqjMet5rnasAvPJhL2ol0m3FvsBIT5Jva0K3baZ2073b-puu1zvvFw3x86EshepzIpnB2Bnl5CZU7Jws_iAQtPkkQTZRbgn0NtXHALiR44rv8oH0HSl8hh99v4PsO2T32o-j9YvAtghT7tf6w_wu4X_R4ppv5jk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=YGOIxQc_KL9YGFXDGIZB0BnqQT3NY7GCoXroNWtOJgrzGw2g-gPzPraXztmjAtGq05WSgt0JnkcPpvDVIiCr7DRxlcPby3ygMaTZ9p02Eze7I3v6sEgcPWoYqhPrC402jlo_DnI6ElvQ5OPDR4wDyC680Oma-0g3PguwOrZMxytFLohXuCzR26_BxFadKS4KJNpezjECvzLCVl1QD-CYcvCyGgHdiTy5Ka9dExSmylPLzVfiGR5g7sqyQ4ZNR3qL_pVZPXvzXDQfWws_N47wGkahLkimTZMtynjcHmP_evV1ZXDD_VTEZgvaAsrOc98gQTXJjnqkr1yiT8FTitUYPxxyZcjB_2VVBtoTQ3FtLaeWKjSxcfZCN-EXyd4QpO5ZMEMk4kFiK62p_pHRIL7f5kwE49dAjw-JbSpZ-R9G-7JHRfjg0PXhJFVqf86xR_0_4eP5Yos6UaMg3ahRhwreRcl1SCgpYXYPyixiDMgzrHYtEoVRseZVQgRUofMfZqp-_k5lwu4ETXczpqjMet5rnasAvPJhL2ol0m3FvsBIT5Jva0K3baZ2073b-puu1zvvFw3x86EshepzIpnB2Bnl5CZU7Jws_iAQtPkkQTZRbgn0NtXHALiR44rv8oH0HSl8hh99v4PsO2T32o-j9YvAtghT7tf6w_wu4X_R4ppv5jk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تفاهم‌نامه آتش‌بس با هماهنگی، تفاهم و همدلی در شورای امنیت ملی شکل گرفته است
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم. کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و آنها اختلافی باشد؟ شکی نیست که این تفاهم‌نامه با هماهنگی، همدلی و تعامل کامل شکل گرفته است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/679272" target="_blank">📅 22:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679271">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229a1d9bf0.mp4?token=uP-lItLMN8S_HmvhjOcLLYN6ZfpF0LVvqKweFD_LY7WgqsHMQjZsCXNJ8p8hx1yMwU_ymTZJ5an8bCCjqz9C_THR5-M84q8wMkoNeYSX95dJAuSWC2dSSbg7D3iqauTODQna2DzUpxHq7ZGyGVamiLwq88fji58GzJMg_vLH23PluMl-0hnxAdKu6L7i0b1fxsmSKz2f6Mgcooku4aoGbJhFG1nXZvdA8L1cqkyem8SGMRD-F1VXBjiKmX2r20vnLtLyo-VAkJey4_vqUPoMpoLrmRwQUviT5de0b2swq67ZOArem69Gyjy3ALwdOnywSBjY7rq9Qir-UKPY487G9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229a1d9bf0.mp4?token=uP-lItLMN8S_HmvhjOcLLYN6ZfpF0LVvqKweFD_LY7WgqsHMQjZsCXNJ8p8hx1yMwU_ymTZJ5an8bCCjqz9C_THR5-M84q8wMkoNeYSX95dJAuSWC2dSSbg7D3iqauTODQna2DzUpxHq7ZGyGVamiLwq88fji58GzJMg_vLH23PluMl-0hnxAdKu6L7i0b1fxsmSKz2f6Mgcooku4aoGbJhFG1nXZvdA8L1cqkyem8SGMRD-F1VXBjiKmX2r20vnLtLyo-VAkJey4_vqUPoMpoLrmRwQUviT5de0b2swq67ZOArem69Gyjy3ALwdOnywSBjY7rq9Qir-UKPY487G9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد، خواهم ایستاد ما نوکر مردمیم، در خدمت مردمیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679271" target="_blank">📅 22:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679270">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7398bed0ec.mp4?token=GTyivKl6drWm1u7-Uk6GbTFnCNOjZbZX6BSa4fwJ3pMNMot-73YG-T_4fpI8twTJx4NY54kCNPDpIf3a0BH36zNjOnR6LPSIAbJNVfWeu3Y58yRKpShP5K8OKRptkFwxZwpY8EDiidqhgHIE49rhUswA5_dz2bBuXaHe_VheDvf2azaRfuIdqYTp0sI9a3BJ7CC3q7ciNf1_YrFI2paKqqCMIsf2uonZzAFU5k8HXLV341CYTS6V6Ou_Wunt-eXEsKg5zvQbsUHfyawHXpIC8Fzv04u_zFhTL5xkpnvtzFVk0XHmjOLFV6Yl_PyVC_6biSYX5KsAHUdvlTShtN4PPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7398bed0ec.mp4?token=GTyivKl6drWm1u7-Uk6GbTFnCNOjZbZX6BSa4fwJ3pMNMot-73YG-T_4fpI8twTJx4NY54kCNPDpIf3a0BH36zNjOnR6LPSIAbJNVfWeu3Y58yRKpShP5K8OKRptkFwxZwpY8EDiidqhgHIE49rhUswA5_dz2bBuXaHe_VheDvf2azaRfuIdqYTp0sI9a3BJ7CC3q7ciNf1_YrFI2paKqqCMIsf2uonZzAFU5k8HXLV341CYTS6V6Ou_Wunt-eXEsKg5zvQbsUHfyawHXpIC8Fzv04u_zFhTL5xkpnvtzFVk0XHmjOLFV6Yl_PyVC_6biSYX5KsAHUdvlTShtN4PPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ دولتی به اندازه ما در جهت سیاست‌های رهبری قدم برنداشت
🔹
اینکه عده‌ای اختلاف‌سازی کنند و القا کنند رهبری چیزی می‌گویند و دولت چیز دیگری، هم در حق رهبری جفاست و هم در حق دولت. با قاطعیت می‌گویم هیچ دولتی به اندازه "دولت چهاردهم" در مسیر سیاست‌های رهبری گام برنداشته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/akhbarefori/679270" target="_blank">📅 22:33 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679269">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ce7d20fd3.mp4?token=PTqTTL3mkJ3D-HZCmliAIlFKweSFaxUPo_VwTK5sh2NYDBEU8-d1AyqFSXaXC4-o58YN5UZ5vjFyyaqkRruXwDnNrrK3k5HXQDzSGJ3iACXSOHzur-ITmHzPo8vciYnb7Ts9s1t_03-8ica_fcGEQZKtz5n23eJDFdv9nMeBmH7JBMwprM4rMigHkl1nHJPMbuIlnVOJL__Kxw6v23EWSHzheBVEUPyxNPEbBD9tORRU8JMvnhoAzc57sjDIRQYOoWItdjYIa7QwpM6CHPxzwYO4_fH5WA5uydM1njlCHaBdK9cupKOyyLXgqSzHcr6Tq0Y9-4XbO2Bm91m5JLoqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ce7d20fd3.mp4?token=PTqTTL3mkJ3D-HZCmliAIlFKweSFaxUPo_VwTK5sh2NYDBEU8-d1AyqFSXaXC4-o58YN5UZ5vjFyyaqkRruXwDnNrrK3k5HXQDzSGJ3iACXSOHzur-ITmHzPo8vciYnb7Ts9s1t_03-8ica_fcGEQZKtz5n23eJDFdv9nMeBmH7JBMwprM4rMigHkl1nHJPMbuIlnVOJL__Kxw6v23EWSHzheBVEUPyxNPEbBD9tORRU8JMvnhoAzc57sjDIRQYOoWItdjYIa7QwpM6CHPxzwYO4_fH5WA5uydM1njlCHaBdK9cupKOyyLXgqSzHcr6Tq0Y9-4XbO2Bm91m5JLoqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: استعفا نخواهم داد، خواهم ایستاد ما نوکر مردمیم، در خدمت مردمیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/akhbarefori/679269" target="_blank">📅 22:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679268">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=CIZTepZnFDAnNjkLD8_ICCGiCaPjEQkGp-3ek6aYUvk63v39xhgqR7uoaYZbdlgJM0dn30wK0lV6M7uJ3LPhvEMG9I6OC0Nwjgt-xSnNZNo3hwwpUYLh5nUJnyeVwBgPiar9BVtfzWf4o6O3xAffQZFVsp9SYpjzol7kZg1pF-xWn450Pn1jBnRfpcgZBLD6WFQdbk54nLAJEDHur88F21DmhyXv72d2HY87Loe_FB2aNyl7Xkf8buFkTB_BKl0yrjVWufvNRiNvT_g_O22-VPD4wD-jpYANfWxajevRHhOrZWH6Yh0YZchH9D6VIr4RqKamn4e7cCUU0GybbU_-xpGCBpMLVTZGT9xtj8MDB-WQdgHL8bg9hOkJIaMY6yvOVnqwLsjo4mKlqrPxLEffOQbj-pclELrNWkUTdSRdE3D54ddEPMhpqGzU-ROXXc38hm-6BwgmV9cgejgRL1yIdHSI0IYtAfX0ZfpSiwbzT_QXm528kGvBy9egive8oeZ_Ee9u7ZFgz2p65rpP_oevqTW8W8ZeoC865p3DV3XyEq812T99YBrbsXmYvL9JyXJfM_4gW2L3OTzLUpsQ0YhTq-0O1r9L8wIA6wPVdYJ9moDfnaQCKH-TGXi-Q_d2xYAy18-Gy4jW10GPSnVjdMa_pfJrnSzYyGXPS4npSO2LjwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb3e9b49de.mp4?token=CIZTepZnFDAnNjkLD8_ICCGiCaPjEQkGp-3ek6aYUvk63v39xhgqR7uoaYZbdlgJM0dn30wK0lV6M7uJ3LPhvEMG9I6OC0Nwjgt-xSnNZNo3hwwpUYLh5nUJnyeVwBgPiar9BVtfzWf4o6O3xAffQZFVsp9SYpjzol7kZg1pF-xWn450Pn1jBnRfpcgZBLD6WFQdbk54nLAJEDHur88F21DmhyXv72d2HY87Loe_FB2aNyl7Xkf8buFkTB_BKl0yrjVWufvNRiNvT_g_O22-VPD4wD-jpYANfWxajevRHhOrZWH6Yh0YZchH9D6VIr4RqKamn4e7cCUU0GybbU_-xpGCBpMLVTZGT9xtj8MDB-WQdgHL8bg9hOkJIaMY6yvOVnqwLsjo4mKlqrPxLEffOQbj-pclELrNWkUTdSRdE3D54ddEPMhpqGzU-ROXXc38hm-6BwgmV9cgejgRL1yIdHSI0IYtAfX0ZfpSiwbzT_QXm528kGvBy9egive8oeZ_Ee9u7ZFgz2p65rpP_oevqTW8W8ZeoC865p3DV3XyEq812T99YBrbsXmYvL9JyXJfM_4gW2L3OTzLUpsQ0YhTq-0O1r9L8wIA6wPVdYJ9moDfnaQCKH-TGXi-Q_d2xYAy18-Gy4jW10GPSnVjdMa_pfJrnSzYyGXPS4npSO2LjwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
واکنش پزشکیان به شایعه تهدید رهبری توسط رئیس‌جمهور
رئیس‌جمهور:
🔹
ما با نیروهای نظامی کاملاً هماهنگ هستیم و پشتیبانی از آنان را وظیفه خود می‌دانیم. کسانی که جانشان را کف دست گرفته‌اند و از این کشور دفاع می‌کنند، مگر ممکن است میان ما و آنها اختلافی باشد؟ شکی نیست که این تفاهم‌نامه با هماهنگی، همدلی و تعامل کامل شکل گرفته است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/679268" target="_blank">📅 22:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679267">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30eb98c40c.mp4?token=Lp4pcVduyjXRn4iLX7YAbCb9Gzi3SeDZpounntXR3L525Vp848E0ZeAGoo7GDa5jl7OvqCfT6_CBjGy3yhc17f1Qg0_PReJkbR95cbuK0PZRpAf1i1CsDlE76nfQ_GEUjgPaXTdOs5DB0s7NG5FhvzU2r_CRR4igQ0U0GJdtlbWOrfFrUD3X1dyR3C0wa8iX9xHZj7pNVlx1XUoDWMAY-llIrAvwTRjrFlq5cEu6zkcsNvGrUL-JQAuy_15cukeja3tYj-B9yd9hX_45i6Yr_m0WOT0rHdNmkpsOiF6GUxpZAQ1xRym049segutI7AalJnH8rERKX9ITC-gdrdAGDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30eb98c40c.mp4?token=Lp4pcVduyjXRn4iLX7YAbCb9Gzi3SeDZpounntXR3L525Vp848E0ZeAGoo7GDa5jl7OvqCfT6_CBjGy3yhc17f1Qg0_PReJkbR95cbuK0PZRpAf1i1CsDlE76nfQ_GEUjgPaXTdOs5DB0s7NG5FhvzU2r_CRR4igQ0U0GJdtlbWOrfFrUD3X1dyR3C0wa8iX9xHZj7pNVlx1XUoDWMAY-llIrAvwTRjrFlq5cEu6zkcsNvGrUL-JQAuy_15cukeja3tYj-B9yd9hX_45i6Yr_m0WOT0rHdNmkpsOiF6GUxpZAQ1xRym049segutI7AalJnH8rERKX9ITC-gdrdAGDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هیچ امتیازی در تفاهم‌نامه ندادیم/  نیروهای مسلح موافق آتش‌بس بودند؟
🔹
تا جایی که آنها عمل کنند، ما نیز عمل می‌کنیم. آنچه به دست آوردیم امتیاز بود؛ اینکه آمریکا از محاصره کنار کشید، به معنای امتیاز دادن ما نبود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679267" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679266">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
پزشکیان: از شهادت نه تنها نمی‌ترسم بلکه برایم فوز عظیم است. اما اینکه نتوانم مشکل جامعه را حل کنم برایم قابل قبول نیست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/679266" target="_blank">📅 22:25 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679265">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f0d5912a0.mp4?token=ajOfdYJaIsQz6me6rIT32coZ_JVKmn_OM8qiDrPnWv71oeM__6pyWTn5q5T-A9B4O3MSyWte2zNJFSzsIHhAF26CF8bbFdLfN5MFXicBmpwtswxidL8S2TiuEY309E780DhuHoCnWLd2GfULApbrQpYqGFC5kLsQetm30lvWnYDva6kMYbZJDQTaPZ45k6kqVnSLiYSnHCci_PSDAy2_9ZRRGzUKNl10S4gHFaN1-tNNRfqjZbOJtb1Uy0j5RbUwDs06NcZMszfY6w2YcnGO1FRaLxlTNv_F16lCzapD2iDETpXaPr_qxOmxoyfiVONfBxGKbjdndpRGHe0gKUiAgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f0d5912a0.mp4?token=ajOfdYJaIsQz6me6rIT32coZ_JVKmn_OM8qiDrPnWv71oeM__6pyWTn5q5T-A9B4O3MSyWte2zNJFSzsIHhAF26CF8bbFdLfN5MFXicBmpwtswxidL8S2TiuEY309E780DhuHoCnWLd2GfULApbrQpYqGFC5kLsQetm30lvWnYDva6kMYbZJDQTaPZ45k6kqVnSLiYSnHCci_PSDAy2_9ZRRGzUKNl10S4gHFaN1-tNNRfqjZbOJtb1Uy0j5RbUwDs06NcZMszfY6w2YcnGO1FRaLxlTNv_F16lCzapD2iDETpXaPr_qxOmxoyfiVONfBxGKbjdndpRGHe0gKUiAgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اگر فشار و تهدید علیه ایران متوقف شود، دلیلی برای ادامه تنش وجود نخواهد داشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/679265" target="_blank">📅 22:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679264">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24f311bf58.mp4?token=BN_8MOwig3SRiS4krcRZVoYk1th75Rqq3VnQgsYTHS85eejLHlHdcuuSgfWBFFd6P3KF0tNsyqB2dV2jrS96d1I82n5OYxGYEd3brOjSzFK3CarcXYzZGJXnttY90TQ62ZourugoP8cFKUjaqn2z0SBKz6Of5n9QGg-bZGt1BlARln73nu-rlCjPiMdGxiu-V0QGuxR4vwBK-xkNZCoYHTdC0HU99OCuK9Q9UPwoLrHhwWsbz9RvdAxWzPSfUw-f9L5MjJH09Xm3lLd6l_DcVkMzDoATykMkm0ogX4NrBQkUCK4O0hKAzl4pyyg7LJuTCdo20uT_LkoczqX8ZmgwoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24f311bf58.mp4?token=BN_8MOwig3SRiS4krcRZVoYk1th75Rqq3VnQgsYTHS85eejLHlHdcuuSgfWBFFd6P3KF0tNsyqB2dV2jrS96d1I82n5OYxGYEd3brOjSzFK3CarcXYzZGJXnttY90TQ62ZourugoP8cFKUjaqn2z0SBKz6Of5n9QGg-bZGt1BlARln73nu-rlCjPiMdGxiu-V0QGuxR4vwBK-xkNZCoYHTdC0HU99OCuK9Q9UPwoLrHhwWsbz9RvdAxWzPSfUw-f9L5MjJH09Xm3lLd6l_DcVkMzDoATykMkm0ogX4NrBQkUCK4O0hKAzl4pyyg7LJuTCdo20uT_LkoczqX8ZmgwoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رزمندگان ما دنیا را به شگفتی واداشتند
🔹
شکافی بین دولت و نیروهای مسلح نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/679264" target="_blank">📅 22:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679263">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cb2826d71.mp4?token=N_xqLQT94hp6AvmrhX-aVOdjlhfBxz0qGkyywMI3ukG4N-EIK00BE4_EGB8TIJp1BMlxEE66fHV2O_LiKC3GksWTf7J3A9NCJx93OM4MbcKrgghQ3YOPWP0Y8EdVjQuU-WqDS1M1BPaji5hYLLn4jO-29IkSSQo3_fpeqnPD9t88kgbRCSu8Pra66qwuEARsnSrXbMUTxvUhiZxI8RHOZclz90oTSpg-GyPJe4tnx7GrkVcsJrBfzFiWSMoF2Ju4wAg0PQpHRNsMM1pJyqsdr49ojdBnj2eivULq4hAwk_Rz_L-S0-im05QMMlamL6OmAnPFV_VDVfGnZ3a75PC57Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cb2826d71.mp4?token=N_xqLQT94hp6AvmrhX-aVOdjlhfBxz0qGkyywMI3ukG4N-EIK00BE4_EGB8TIJp1BMlxEE66fHV2O_LiKC3GksWTf7J3A9NCJx93OM4MbcKrgghQ3YOPWP0Y8EdVjQuU-WqDS1M1BPaji5hYLLn4jO-29IkSSQo3_fpeqnPD9t88kgbRCSu8Pra66qwuEARsnSrXbMUTxvUhiZxI8RHOZclz90oTSpg-GyPJe4tnx7GrkVcsJrBfzFiWSMoF2Ju4wAg0PQpHRNsMM1pJyqsdr49ojdBnj2eivULq4hAwk_Rz_L-S0-im05QMMlamL6OmAnPFV_VDVfGnZ3a75PC57Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: آمریکا از سرزمین کشورهای منطقه به ما حمله می‌کند و ما باید از خود دفاع کنیم
پزشکیان:
🔹
ایران قصد زورگویی به هیچ کشوری را ندارد، اما زیر بار زور هم نمی‌رود و دفاع از خود را حق طبیعی‌اش می‌داند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/akhbarefori/679263" target="_blank">📅 22:18 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679262">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d23fec037.mp4?token=q9IhBvtL7BGprDroV70EhG26a67CB9x0Ra4nln5DWMxGevS2pckfUn4R1sbXf2d5w3On-QqHYXKPe1DCiD4Uo7Fum-nxk76FNmrXCK-Y5J4N9Dmrqx01qKLrnVMh86lHtUT8Rk_jOairDsSLlwdGd1mDg9p0mIqttYAgkptdz4P-FTAuZkKfDeZwje12bVBnzbv9kA7NiD5kYIn1yWcZ8bNY0W4uHAE0BZzFtjNtLBI2Kq3D_0NochRyUc35Ee1FtsMNXH6zyIvyJ7_x2PSA19m1gAEvXT6t_mb9XKNJM4t0vtZSX-FDXbHtKDbPX9QXVwzMb6N1YmkIfknpm1vFJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d23fec037.mp4?token=q9IhBvtL7BGprDroV70EhG26a67CB9x0Ra4nln5DWMxGevS2pckfUn4R1sbXf2d5w3On-QqHYXKPe1DCiD4Uo7Fum-nxk76FNmrXCK-Y5J4N9Dmrqx01qKLrnVMh86lHtUT8Rk_jOairDsSLlwdGd1mDg9p0mIqttYAgkptdz4P-FTAuZkKfDeZwje12bVBnzbv9kA7NiD5kYIn1yWcZ8bNY0W4uHAE0BZzFtjNtLBI2Kq3D_0NochRyUc35Ee1FtsMNXH6zyIvyJ7_x2PSA19m1gAEvXT6t_mb9XKNJM4t0vtZSX-FDXbHtKDbPX9QXVwzMb6N1YmkIfknpm1vFJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور: ایران آغازگر جنگ نبود و همراهی مردم، محاسبات دشمن برای فروپاشی کشور را برهم زد
🔹
امروز ایران با قدرت و انسجام بیشتری مسیر خود را ادامه می‌دهد. دشمن روی فروپاشی ایران حساب کرده بود، اما ناکام ماند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32K · <a href="https://t.me/akhbarefori/679262" target="_blank">📅 22:17 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679261">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd37423c0c.mp4?token=hovs8vavyddplU8JjgAkT59748ENsG9UWIOK8_Zjx_4KzsBk26e_NhcovVXFSogUFxrZ5ylaIDGNoQ7SBVuQnbW_8jQMrYNBNEvtDQ3C9omefddIIwIXlmzENShXVUPfFB6SaiSqQwi14dGtPpX09C2zZig_EfCn9pZk0U5qTkCcV-kAgmoSDs04umnHAgjYfaI4_gy7jDkgSFwE_CUP2n2i6ZXFnixPjuJmBSBKdz6Azsyc-MxX61jOJwYePHea0gDYM3STgcK3gU6bKj3_iEg-K_AphlNmmbLcQp8XzyJNf_ehVRTTne9RqRnbXxcUQ8uIE8zXQrpcFcIQ8KFbMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd37423c0c.mp4?token=hovs8vavyddplU8JjgAkT59748ENsG9UWIOK8_Zjx_4KzsBk26e_NhcovVXFSogUFxrZ5ylaIDGNoQ7SBVuQnbW_8jQMrYNBNEvtDQ3C9omefddIIwIXlmzENShXVUPfFB6SaiSqQwi14dGtPpX09C2zZig_EfCn9pZk0U5qTkCcV-kAgmoSDs04umnHAgjYfaI4_gy7jDkgSFwE_CUP2n2i6ZXFnixPjuJmBSBKdz6Azsyc-MxX61jOJwYePHea0gDYM3STgcK3gU6bKj3_iEg-K_AphlNmmbLcQp8XzyJNf_ehVRTTne9RqRnbXxcUQ8uIE8zXQrpcFcIQ8KFbMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: اروپایی‌ها اختیاری از خودشان ندارند
🔹
در جریان مذاکراتی که با فرانسه برای لغو اسنپ‌بک شکل گرفته بود، به تفاهم رسیده بودیم اما آمریکا نگذاشت.
🔹
این روند با هماهنگی رهبر انقلاب به تفاهم رسیده بود، اما آمریکا توافق را نپذیرفت و اروپا نیز اختیار تصمیم‌گیری مستقل نداشت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679261" target="_blank">📅 22:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679260">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0001a40725.mp4?token=u15MBG_1fhzCnxf8RUxdjrO9qzCcnZOQHuUXdsi9vyz5accjIy9uxTvzR0F-YNWGCRR6tdh4ouCuMMDnVhzQvTA9yIXRuJ37WMxoKn5rDtajSngOOgb-RiEWqZdDvtdkNxtM1xU8yzWNStpi6KTBdeMye2h6wgrcgFAwBBot_Ucy6aPA081qzxWZKIwhsQ9bhgZI9V_QLHsX4Hote_tker8Kggikv731FWxDBOCsc6Qr6emr6URAhG2FgkSCOSgId3oy36mgc8j4WTBvkdcMPpjjXZScnoBKPnZ9zt9WtAvptw-MbC7BFV09XA4ooU6w0j8unQQfAsofYtpV6Nj3NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0001a40725.mp4?token=u15MBG_1fhzCnxf8RUxdjrO9qzCcnZOQHuUXdsi9vyz5accjIy9uxTvzR0F-YNWGCRR6tdh4ouCuMMDnVhzQvTA9yIXRuJ37WMxoKn5rDtajSngOOgb-RiEWqZdDvtdkNxtM1xU8yzWNStpi6KTBdeMye2h6wgrcgFAwBBot_Ucy6aPA081qzxWZKIwhsQ9bhgZI9V_QLHsX4Hote_tker8Kggikv731FWxDBOCsc6Qr6emr6URAhG2FgkSCOSgId3oy36mgc8j4WTBvkdcMPpjjXZScnoBKPnZ9zt9WtAvptw-MbC7BFV09XA4ooU6w0j8unQQfAsofYtpV6Nj3NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: با امر و نهی نمی‌شود جامعه را اداره کرد
🔹
مطابق آنچه امیرمومنین(ع) در نامه خود به مالک اشتر فرمودند امر کردن یعنی فرار از دین و باور.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/679260" target="_blank">📅 22:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679259">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b87f6a3558.mp4?token=ajFBiCQhn3hkpEWAZr3uGauBeSmZZwOwBqCbUM-a2MrPRxkJgvAgqCUr_K-50DCK4WQMgBY40_G7Js_aw-tHsW_qSXBkFyhxBsh02NPY5pY_OV3nRMehermi9vqgUUZcjgFCR9VnCjVqI3KDvqMummyWDnQ24z-0OT7HwcB_JXr9720BMTvoTaLzxA3DR_zzIi9o1lJcFYVRx4F4KZj-6S4nlDiLpta5SNjstJruI0yZurvNgaR9bZQFMavazBDK_Ra7iDLVtdjGPlivHxba0FNBKzygcudUILFQ_f6oDTK3fGaiahIzUpksKmp5uz3Okoqr0UHQvmC6DbEfyoFu1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b87f6a3558.mp4?token=ajFBiCQhn3hkpEWAZr3uGauBeSmZZwOwBqCbUM-a2MrPRxkJgvAgqCUr_K-50DCK4WQMgBY40_G7Js_aw-tHsW_qSXBkFyhxBsh02NPY5pY_OV3nRMehermi9vqgUUZcjgFCR9VnCjVqI3KDvqMummyWDnQ24z-0OT7HwcB_JXr9720BMTvoTaLzxA3DR_zzIi9o1lJcFYVRx4F4KZj-6S4nlDiLpta5SNjstJruI0yZurvNgaR9bZQFMavazBDK_Ra7iDLVtdjGPlivHxba0FNBKzygcudUILFQ_f6oDTK3fGaiahIzUpksKmp5uz3Okoqr0UHQvmC6DbEfyoFu1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: آمریکا تلاش می‌کند همسایگان را علیه ما بسیج کند
🔹
خیلی از مشکلاتمان با کشورهای همسایه را برطرف کردیم اگرچه آمریکا و رژیم صهیونیستی با توطئه و جنگ اخیر به دنبال ایجاد اختلاف بین ایران و کشورهای حاشیه خلیج فارس هستند.
🔹
طبق فرموده پیامبر گرامی اسلام همه مسلمان باهم برادر هستند چه شیعه باشند و چه سنی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/akhbarefori/679259" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679258">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0226b4a748.mp4?token=TjcHtWOmYtUBeKC0ViXif_W_ZSNXRSO3H1ODkVp5IXNM6pQbe9y74-mU8AzInTx1Hd3SxV5Pk-rmN8Zc4TQj6yl7dt05NnWvZOth1NSoqhaBcj_lYjFPm1IPYUYx1Q8jZSXVI2VPw31Xsr-tW8AAHk-eJ44FJqKJ1hp_QQ-nIqEV7XiT9auBJUGT8BMjFpKRIUW_MCPxFKjkdLZB1hy0tew84mT2-HAWLrNJt6dQHvi2yPbLZkLJVJSt7l4xx6deQheXqrtRaCkB4ux2GHO5HvLGUrxoJ2ilT8ByTaBRj9QFgS0TWboTJsDoMCr_TNwgFHMVPZuVFqi-aaQcWHv-cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0226b4a748.mp4?token=TjcHtWOmYtUBeKC0ViXif_W_ZSNXRSO3H1ODkVp5IXNM6pQbe9y74-mU8AzInTx1Hd3SxV5Pk-rmN8Zc4TQj6yl7dt05NnWvZOth1NSoqhaBcj_lYjFPm1IPYUYx1Q8jZSXVI2VPw31Xsr-tW8AAHk-eJ44FJqKJ1hp_QQ-nIqEV7XiT9auBJUGT8BMjFpKRIUW_MCPxFKjkdLZB1hy0tew84mT2-HAWLrNJt6dQHvi2yPbLZkLJVJSt7l4xx6deQheXqrtRaCkB4ux2GHO5HvLGUrxoJ2ilT8ByTaBRj9QFgS0TWboTJsDoMCr_TNwgFHMVPZuVFqi-aaQcWHv-cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: مساجد، مدارس، مراکز بهداشت و شهرداری‌ها پایگاه‌های عملیاتی هستند که دولت می‌تواند برای اجرای برنامه‌های خود در سراسر کشور از آن‌ها استفاده کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/akhbarefori/679258" target="_blank">📅 22:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679257">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc165756bb.mp4?token=VOTE05qEIsM0zhE9FjSCqqQE4WtFnHMvzr5Wlyxr_7kDPp2w3OkeVK-iytpW7VEXslbPta1jyl_UDxRGGkdxNJhB3QVQSMAjLr8zo0JT2CzpBBYSCEq-YSMmHPK5ICK9EFoML8s2fAmJLYuJEr6OvxomzIxu-eHEPZxTdi7xM7Z-YxB6nzMV7j8S7tMs0cDuqS-UH-5f90o2_-yIQDSHMD9kx0AqG3-ge7ODYlpd3Jdt6LgFoEsm43kcwUlGZsLoC8_MNaHj-85fdejla5XJkaWenJt7X5WkJERbLbpP4Ad1CoD4mJp4Fnphgjal78GByZc4oaaaeiUW7jqaKdiLmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc165756bb.mp4?token=VOTE05qEIsM0zhE9FjSCqqQE4WtFnHMvzr5Wlyxr_7kDPp2w3OkeVK-iytpW7VEXslbPta1jyl_UDxRGGkdxNJhB3QVQSMAjLr8zo0JT2CzpBBYSCEq-YSMmHPK5ICK9EFoML8s2fAmJLYuJEr6OvxomzIxu-eHEPZxTdi7xM7Z-YxB6nzMV7j8S7tMs0cDuqS-UH-5f90o2_-yIQDSHMD9kx0AqG3-ge7ODYlpd3Jdt6LgFoEsm43kcwUlGZsLoC8_MNaHj-85fdejla5XJkaWenJt7X5WkJERbLbpP4Ad1CoD4mJp4Fnphgjal78GByZc4oaaaeiUW7jqaKdiLmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس‌جمهور : مسجد فقط برای مذهبی‌ها نیست، برای همه مردم است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/akhbarefori/679257" target="_blank">📅 22:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679255">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c17aed4be.mp4?token=joLZ64X00uW0xDbnVEpQVAlsrwk4k7Iwib4QXb6KddE5JdFFqempDZluU15AqRMvKhSbpnFxhOiQRtOE_Bkz6YtP-5fjlhRc3Nu44YE_2ZKum4zBvFOa4B-SlUpDCx6ilwc5udCAE0QrvaDgYiMaz5vLRXUiIPfTKwbTWFHoVbMHlniUKPoNs2Db3oCVBbNRuy9Jum3ilC4opFeXrSnRIhN-dOQU6A7wg5mBY5DsKwzpOB77WpqCav17QBgdYTQgf4eQyjAzQGP9QX14-SnTb1VIrsKZlKaFm404ptPIn7TrH-7ZZskB14nkUQcX2wi9O2D2mi8AfCZCEk3RsvTZFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c17aed4be.mp4?token=joLZ64X00uW0xDbnVEpQVAlsrwk4k7Iwib4QXb6KddE5JdFFqempDZluU15AqRMvKhSbpnFxhOiQRtOE_Bkz6YtP-5fjlhRc3Nu44YE_2ZKum4zBvFOa4B-SlUpDCx6ilwc5udCAE0QrvaDgYiMaz5vLRXUiIPfTKwbTWFHoVbMHlniUKPoNs2Db3oCVBbNRuy9Jum3ilC4opFeXrSnRIhN-dOQU6A7wg5mBY5DsKwzpOB77WpqCav17QBgdYTQgf4eQyjAzQGP9QX14-SnTb1VIrsKZlKaFm404ptPIn7TrH-7ZZskB14nkUQcX2wi9O2D2mi8AfCZCEk3RsvTZFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
پزشکیان: باید منطقه‌به‌منطقه مشکلات مردم را شناسایی و برای رفع آن‌ها اقدام کنیم
رئیس جمهور در بخش سوم گفتگوی تفصیلی با مردم:
🔹
هر نهادی بخشی از جامعه را می‌بیند، اما برای رسیدن به پوشش واقعی باید مناطق مختلف را بررسی کرد و نیازهای مردم را منطقه‌به‌منطقه شناخت.
🇮🇷
✊
@AkhbareFori
|
khabarfoori.com</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/679255" target="_blank">📅 22:03 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679254">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
ادعای رویترز: عربستان حدود ۸۶ درصد از سامانه‌های رهگیری پاتریوت خود را که تعدادشان ۲۸۰۰ فروند بود، در ۳۸ روز اول جنگ استفاده کرد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/679254" target="_blank">📅 21:56 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679253">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X7gNfyL7KymWPg6Rd5GJlX8SUceWDKuTTZSczdTMLi-tnoozjnhCSU1rKvh0B_X-FWrT4RD95H7W_zUGJ9saP3hYWM6yxjnaOAvTtUx6W-UN624Kw0i9woMtYZ0Ar2jVEIXfhzL2KSRmU7kHOiCfMJMdk4gFfOLN-bMXh4ZAg9xBUTsPd73FW5yUmtZjVN-i5f8Uwwzqg1B0wu_W_DojGfMHgE_fIJI7WQgIqxU2RVR3DQUfkv9-huLZRwnsoIN1KFK6q2iLrU729F19SmnbgeqFj7x7uNQ8u90L4Sa8T1cI3HFGI7p-PUNGehw2irELUAVq3_6q9yfdW5-HGQGDYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از کارتر تا ترامپ؛ چرا واشنگتن مدام در مورد ایران اشتباه می‌کند؟
🔹
از زمان بحران اشغال گروگان‌گیری سفارت آمریکا در تهران تا دوران ریاست‌جمهوری دونالد ترامپ، تقریبا همه دولت‌های آمریکا در برخورد با ایران با یک مشکل مشترک روبه‌رو بوده‌اند؛ این تصور که می‌توان با فشار، تحریم یا حتی تهدید نظامی، ساختار سیاسی آن را تغییر داد. اما تجربه نزدیک به پنج دهه گذشته نشان می‌دهد واشنگتن بارها در شناخت ایران و نحوه واکنش این کشور دچار اشتباه محاسباتی شده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236097</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/679253" target="_blank">📅 21:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679252">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlU7hcr1Mrpmgmhja47uVW1DkBjnBBu7_sswYD3UKntX6xwiq0ViO1LNpBbsKFgrjbgS41CrablLSgGiBISpmdvYUetAaXYvG7skwauRrs41BMLga9df8ZgXUFs7pdN6RwO5o79Cg3sWhG3Y1uuamBWF36MeD9ragJ-uKQV6jDrDCsR4NACDhmC6MI6TOgavgnkjRS0Q8dxWawvUMCeRU1kncgz4YImlBSXIOp4PJqO37rfnXxE-PYe86oRPKbFKomkTmy-hf_5bJP2SWlvD88yCTOJe0lK7glc3eX_OSiUmQGMYvvIvNCtfTJnR2aT3-TqJm-MIJMVqM37n3VVeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤎
تسبیح سنگی ۱۰۰تایی
ذکری از جنس ارادت...
این تسبیح از سنگ سِرپانتین، معروف به سنگ امام‌رضا(ع) تهیه شده و روایتی درباره این سنگ در کتاب عیون‌الاخبارالرضا، باب ۳۹ نقل شده است.
✨
💸
قیمت اصلی: ۱,۱۴۷,۰۰۰ تومان
🔥
قیمت ویژه: ۹۴۰,۰۰۰ تومان
⚠️
تعداد محدود | تا پایان موجودی
🛍
سفارش:
@gharar_order
👀
مشاهده محصولات:
@ghararshop
🌐
ghararshop.com</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/679252" target="_blank">📅 21:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679251">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q653Nuu954khXv6AnxJtTWa7Ty8SgRKO1UEaLnPkYx80NOSFTWhG8_zFPlXncCYFMZZq_gHbxjJwmy5Erl7vWbj0XhDZI7CNfSYcqgPd6_-ZXdGfg5RjDzp_lzHFgga_66yhYx6_pZHxT5oOOuebt4OOz6_NBM7f1bSCkXHJ592becPLOTvm0g9YawtJuHehgKg_HejTGbjlTfDpo0PnxSBaeiPqGinMI-4BNQESS5wtKJzHpZwaedvr4IvZJCFfkx8RZUrWIccNnhABfNserlRUVnakpb79ekCsmM4bRc4FlfGnE1ccbfaC80J5FV3WVGFyE5n4-pLMf-h3csjMqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیام عراقچی خطاب به همسایگان: زمان آن فرا رسیده است که به خود متکی باشیم و برادری واقعی را در پیش گیریم
وزیر امورخارجه:
🔹
نیروهای مسلح قدرتمند ایران، آمادگی، توانمندی و اقتدار خود را در برابر پیشرفته ترین نیروی نظامی جهان به اثبات رسانده‌اند.
🔹
هنگامی که مسلمانان در کنار یکدیگر متحد و یکپارچه باشند، می‌توانند در برابر هر چالشی که از سوی بیگانگان بدخواه ایجاد می‌شود، با قدرت و قاطعیت ایستادگی کنند.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/679251" target="_blank">📅 21:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679250">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
رئیس دستگاه اطلاعات عربستان پیام پادشاه سعودی را به الزیدی تحویل داد
🔹
نخست‌وزیر عراق  امروز خالد بن علی الحمیدان با رئیس دستگاه اطلاعات عمومی عربستان سعودی که حامل پیام پادشاه این کشور بود دیدار کرد.
🔹
علی الزیدی مدعی شد بغداد اجازه نخواهد داد خاک عراق به نقطه آغاز هرگونه اقدام یا فعالیتی علیه کشورهای دیگر تبدیل شود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/679250" target="_blank">📅 21:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679249">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q89tBiqfCAS4BAZ6SLpHSHvJcaJaRYuzrYyv7flddiWYcTcnCtAV_-DKIqt3osC4J1p4rTWyPOaVuqbgI2B-20gFz13-kEtBxmIK03q1J-cKcDcu6qpjI3Jie4Sk8JIeKE3xntunQ2WjsnMUH6624TkNEx8316UUjfnnBfwc8YXPCAgyiortIVWpcg9_pSo-Psg57AW4zT6VnS9x6IW8aVuP2XrQfhivaiJmqEpiMpZE5TEzy2uVbSQ5ZaSuoRroIsk0wotTD1hClELMJOBGPusJGGiuwUe_MLJfdTwSy2towXuNWUWxnWdsME3zuj-CE-GCvYOHaRRAlRWvU80uAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استرس و اضطراب؛ دو حس شبیه با دو ریشه متفاوت
🔹
استرس معمولاً واکنشی به یک عامل یا موقعیت مشخص و بیرونی است و با برطرف شدن آن عامل، کاهش پیدا می‌کند.
🔹
اضطراب ممکن است حتی بدون وجود یک دلیل یا تهدید مشخص ایجاد شود و برای مدت طولانی‌تری ادامه پیدا کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/679249" target="_blank">📅 21:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679248">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6OXN_rTPGSSDfSqMnHa1GbZ6_a8naXBid3ggz4T4ncBaf7d00cPklqC5TD3H9HYxFJUi8VKjn2f_kQEVdEEnHDQadsPrkM17KcGQJlrGC3OaW7L2YDvia6eG9IGnyvHO41bGXFD2MLZQhE1HkXYQ6pb8s4RsqXCvtO1lFe0ECy3y-lKL39SzbygQ3BTXEvCQgTW2HskAOgh7yLDhVOgkE7a_5VlSzoqkSzOKMCMDCO7yynVPAYW5nah0v-aHzcPARL70Ks96_T6MrVTG2oQsdbJ7_5oKOH1GgHjIzEaY4Xrybnf2TT91vRsDr7ofvQ9M9lLj0VWv9sUXTvgPPKZXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفریقا، موتور اصلی رشد جمعیت جهان
آفریقا با افزودن ۳۶.۲ میلیون نفر در سال، موتور پیشران رشد جمعیت زمین است و آسیا نیز با ۲۹.۵ میلیون نفر افزایش سالانه در رتبه بعدی قرار دارد.
در سوی دیگر، اروپا تنها قاره‌ای است که روند منفی را تجربه می‌کند و سالانه حدود ۹۹۲ هزار نفر از جمعیت خود را از دست می‌دهد.
@amarfact</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/679248" target="_blank">📅 21:19 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679247">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McGIDagYCLWNpcDpzXaPyvnj9jOJ61Yr4I9SgJBX1o78c7zw4_7G2Kp4bP-mdDYOG9YQL6QHS_LQhDh0xFHhh--rsZGTP9AY8XD8izEjVJbuHGWfg3he89lhcnojw6nY7hM4Tlvt3Ti6qX0UQEtCiAX2Cy2sk2vrTwQF-bwcDSWDN8Av6RfKbGNnMd0eAlc93R5ELrv_b0KLSEbkaru73-ZxdT-_c4cHVNvwln9d8aBLtgiXvyyCen1fXQTd1LxwU-jS9aa4nFGMTofQ73wRN30mUfBhIHSf9PAmq5j79DWalE6ZL_dd6OyyB_tSHjJXfDAXOX1YwiJLqXhbSxOM_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای آکسیوس: مذاکره‌کنندگان ایرانی منتظر تایید نهایی شعام در مورد توافق با عمان و آمریکا هستند
باراک راوید، خبرنگار آکسیوس، به نقل از یک دیپلمات از کشور میانجی:
🔹
انتظار داریم این تایید به زودی انجام شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/akhbarefori/679247" target="_blank">📅 21:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679245">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ2GfW4UUHgjK7kjn0fzju6BIXHH1ZTKouidIWUCnIZJ7TNkiTB_dcRR4g5a9wjG149-xRWHcK5iuDxEUF-wMtI2qHxTSKq8j3OXUNCLdY07wMCZNPkSzB4KnG4asjzJorSeQKRfCiLz31Z0DTEV_xng-SwG8YX4wAslnSKKRjGDbMcUETt90Lim4lm7em1GcKC4imBz8zJB4PKLRLuZP9a5KBqO_OLRYm__MYrD7lBJorcehnMq2oTsxbIPHLOxjkXXjBBHi-nw96wDtQDRo53blWaAn1dVBEw-ls4xh0jMMLiztkymlYdc5JlzedGeoh3WJCUfc1mOtBxCNZf7qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ترامپ در حمله‌ به رسانه‌ها، ناخواسته یک افشای محرمانه را تأیید کرد |‌ پایانِ ماه عسلِ اطلاعاتی!
🔹
در دنیای پرتلاطم سیاست واشینگتن، گاهی یک پیام کوتاه در شبکه‌های اجتماعی می‌تواند به اندازه یک گزارش تحقیقی بلند، ضربه سنگینی به اعتبار و امنیت یک دولت وارد کند.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3236110</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/akhbarefori/679245" target="_blank">📅 20:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679243">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HLnMQWg6kfspbrDWITL7e5ccgUhBVJ23czP5G0-LiGLQC_rlpIKRRQFN92fjzoIapey7m3JhDHmVFDheVQFu0Zs6lFh2j463icTeOgBwoKG8n6-cgBK6yyPDx3CS7Vyb8dPbx16jE2TkL1K_YAVI0ojDl5wYOaifSn2fdV69FvF9j4R49VgqX5iIBKO0Kc8iaNYP5Wc23x8GTPm8TRJhDwnhaGcGErewObd-VoRwh_lD7xnWYP1aTtzZv6KDSwoM6KEetS_f7q6w0YApuCym2bFEIJ0DJkNxfVSjErifwL6ksau-PkQAneYU3zUYyg5_Bdjr5vEnAvUERkRi5i0pkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
زمان طلایی مصرف مکمل‌ها؛ بیشترین جذب، بهترین نتیجه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/679243" target="_blank">📅 20:42 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679241">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
طلب مرگ، ایست قلبی و بازگشت از برزخ؛ ماجرایی که زندگی یک مرد را دگرگون کرد
🔹
00:08:15 طلب مرگ از خداوند در روزمرگی‌های زندگی
🔹
00:18:30 حضور در ۳ مکان مختلف به صورت هم زمان
🔹
00:24:10 رؤیت وضعیت ناراحت‌کننده کودکم به خاطر بداخلاقی‌های دنیوی من
🔹
00:39:00 تغییر رنگ و موزیک در گل‌ها برای شادمانی من
🔹
00:41:10 مراقبت اهل بیت حتی از افرادی که منکر وجودی آنها هستند
🔹
00:46:19 تغییرات رفتاری تجربه‌گر بعد از تجربه
🔹
00:51:50 متولد شدن دوباره و تأکید بسیار به رعایت حقوق دیگران
🔹
01:02:00 چگونگی جایگاه برزخی خودکشی‌کنندگان
🔹
قسمت بیست‌وچهارم (پرنده‌ طلایی)، فصل پنجم
🔹
#تجربه‌گر
: رضا معظمی گودرزی
🔹
قسمت قبلی
#زندگی_پس_از_زندگی
#فصل_پنجم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/679241" target="_blank">📅 20:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679238">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WkNO7yczzgPKQMBZBleecwed1XWYLuru5fG60sVflK7lBp5ZZsa1REc8lUFeY_AbGnUEjPkj2fPNz710jgjZvmwxZ9oz9crRszCqABSbW3zT_VTv7J9oEhlZrzl8nrJXS3uHEVDHubX092YPdempk65xDqCVn3z_vpRSfL9QhvUx8rfg99PGuRDS5Ocnh9bYBvJKFz3J9bJaFn15pTqg0QVE_3DUAangUoTobCbPWQJ1bu6xkeUBuM1psUdH7s7a72fm8YrFsopmXv4mBLp9NCi-PenVMlRl3uJh6jBSOe_r4WkkWwvxqK7qN-eZdgYS9cnUGAyvsmfMMjzEfo9oQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
راز تازه ماندن میوه‌ها؛ مدت نگهداری هر کدام در یخچال
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/679238" target="_blank">📅 20:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679237">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رهبر شهید انقلاب🇮🇷</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kb0UzQhH2n3-7pQBztpa-oJuik7IQs4m_p48UWvGFJiN7SKsIPQkDQKlsGgnoov1s0svV1FU-8e4lba644TPJ42yCmKLfnii1HSU6imyX-c7K6E-CoVUqOOF90Brx0KltqObxRgYa5Yv5YT_hc3mAjAa6SkcRfVQKvlTQDLUkGkn84RFc5TU3ypZEvcRUvpSWodcZaAE1zUFo0mBw3Ko3asD0tF6dq36J5mJWcX7udfCi231JCDUb96PF90wFT_gZ7BtBIkS1LVVtdAOJzNMJGk23-9GXbQxPVVGokRJAD1Uraw6zwpMZb8YK3tHXg1MypmWXHn21xba2Mkc2zihag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
توصیه‌ حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه به قرائت قرآن و دعا برای پیروزی جبهه مقاومت
🔹️
رهبر شهید انقلاب اسلامی در پاسخ به سوالی، قرائت
سوره فتح
،
دعای ۱۴ صحیفه سجادیه
و
دعای توسل
را برای پیروزی جبهه مقاومت توصیه کرده بودند.
💻
Farsi.khamenei.ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/679237" target="_blank">📅 20:08 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679232">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
واکنش امام جمعه اردبیل به سخنان باقر خرازی  آیت‌الله سید حسن عاملی:
🔹
از دستگاه قضایی سوالی داریم شخصی خبر دروغ به رهبری بسته و دفتر رهبری با صراحت آن را انکار کرده است آیا این جرم است یا خیر؟ قطعاً جرم بسیار بزرگی است چون علاوه بر ضربه به جایگاه رهبری هزینه…</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/679232" target="_blank">📅 19:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679230">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8367154b7.mp4?token=vMIOrY3hf4Ru31-j7cKgSRom40co-7cRGShtPxpbt_Z6igCD5vW_iGpLSRTuc5KCSYjz2sqH0OHShK8IdQJcUIT2kBNUQ55LDPJuHie5fhvkDIxUrLgK900HBlNzO6h5hH4fyXAhB0RymTjXHNot1jULT7Z6EVToD3AOMWRJQ5tw673CgRprVEuGws2D_sSc2Comj49rpbIJ5_0IBkGzVavtvVMLTlZYmNngymSlxoPAJk_7gGz5L3Jlm02jP4cBOkwyoGMz8tnbrTRdkd_lMYh_J2d5etAK9-uQ28s-Ux-gCNRF2vm455RPMUHiCQ8Fb6CkJVgZCNJYRTGEFHvXRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عطریانفر:
پوست قالیباف به اندازه‌ای کلفت است که خیلی نگران اهانت تندروها به او بابت مذاکره و توافق نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/679230" target="_blank">📅 19:45 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679229">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61965f8b55.mp4?token=k3T5ud3BpA_8CHS9hoPiHAWPSEoQocCJvjf0jSvC2JgWrLodwqy6gp0dQbFggI7xuSL6v7TnDcXVin62NVS0hn8BJRmbi1zWDmgpB4utWVnPa0z37ruHXBvFgA3VqMAkoIVG5utokWjHzuX_qwFUleMhwaw2awbodSVxencXoD_akDy_yXic1-MLCl6fLD_UMbsGwR2wiJN8muIox9ahMHn2jrHBz0ALPw6W94P3FgZkWa7YzSKIvWj0ug62iUELk1jPS12gt-SIuy0GejdRifa17WDcHpxCxH-XriQXGxPGsnt4tIsvJ_av2HN_xzLzG3AbOdcsPWk3LIRxqY_1A2kzTu7TdEUOB9HNZJPU6G_87xofJeZIs0iLoQ-ScH2biW_aDVC7azllgLfmMe19CvNk70wy0azEmCxCc-FrnrofVPVDOsZ62-0SIwOE8b60kiit1lkBkGlsswd3Q4O9SSYUSoUkKnNJ8UuYLKbawSQTrPKvLQY1nolj5h-bu4mg-xkKzaCjuESR6Qe0JXXibfUl5ovE3aPZNxP-CZKCh5yez_DNVjq2v-iTioBBREYAocl_lWgNGwLyfhWxt-SEyDa1QpiTHxEwlhniuA4IkPRkdoj36wiPm5_PxieuNHnmuveA5U6vB1aslUq_czJG6TX5Iepp5su16dQzY8Nreow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61965f8b55.mp4?token=k3T5ud3BpA_8CHS9hoPiHAWPSEoQocCJvjf0jSvC2JgWrLodwqy6gp0dQbFggI7xuSL6v7TnDcXVin62NVS0hn8BJRmbi1zWDmgpB4utWVnPa0z37ruHXBvFgA3VqMAkoIVG5utokWjHzuX_qwFUleMhwaw2awbodSVxencXoD_akDy_yXic1-MLCl6fLD_UMbsGwR2wiJN8muIox9ahMHn2jrHBz0ALPw6W94P3FgZkWa7YzSKIvWj0ug62iUELk1jPS12gt-SIuy0GejdRifa17WDcHpxCxH-XriQXGxPGsnt4tIsvJ_av2HN_xzLzG3AbOdcsPWk3LIRxqY_1A2kzTu7TdEUOB9HNZJPU6G_87xofJeZIs0iLoQ-ScH2biW_aDVC7azllgLfmMe19CvNk70wy0azEmCxCc-FrnrofVPVDOsZ62-0SIwOE8b60kiit1lkBkGlsswd3Q4O9SSYUSoUkKnNJ8UuYLKbawSQTrPKvLQY1nolj5h-bu4mg-xkKzaCjuESR6Qe0JXXibfUl5ovE3aPZNxP-CZKCh5yez_DNVjq2v-iTioBBREYAocl_lWgNGwLyfhWxt-SEyDa1QpiTHxEwlhniuA4IkPRkdoj36wiPm5_PxieuNHnmuveA5U6vB1aslUq_czJG6TX5Iepp5su16dQzY8Nreow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای وزیر خزانه‌داری آمریکا: تنگه هرمز هرگز مثل قبل نخواهد شد
اسکات بسنت:
🔹
ما از نظر اقتصادی ایران را خفه می‌کنیم؛ آنها تورم ۱۵۰ تا ۱۸۰ درصدی دارند و نمی‌توانند حقوق ارتش خود را پرداخت کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/679229" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679228">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iKj7McahBnKF_53uBU_8DkZbHLEJvrHqtgU4JKVtkABTkYyNnlpCgdixNKTN39EPd2LVhRgbRLFTe6bRjx9ewsjwZKKYO3vHs9tNXqZ1W_xY9ns6nuHUgqcdWCCFxeEsuPzVtDpykMdJzRESoYDCaZCLMmlW7NfB3RPNMvlusBj7qbugYpVkcZJL97BORd2PeRocS8RPCyHNwF1FzSbYXHCzfgvAgD_JhIcdJi0fe2BYIoiMN5bWSP0ZPDh-RLUVyH8uh0jMzqOQfZyJHkNGQeVk-a2v5I_a_MFs7QygTKNPa-GiZwqYoPTl86u7m6D5UZUqb0EWTfR3X3sBKHRoXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین زمان تعویض لوازم مصرفی خودرو
🔸
بهترین زمان برای تعویض روغن موتور و فیلترها، هر ۵ هزار کیلومتر و برای فیلتر بنزین، هر ۱۰ هزار کیلومتر است.
🔸
لاستیک و لنت کاسه‌ای نیز بهتر است هر ۸۰ هزار کیلومتر تعویض شوند.
@amarfact</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/679228" target="_blank">📅 19:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679227">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e930289fa5.mp4?token=oaGG89CvfE5Kx59u3o2vPHvmNBXpPAaIK10KrF70JG0BTdl4R2ujdev8rOMsx-yRfg-96tsXOrQWR73VIZQFAlOchyNd8fhp4FGWBFN6PDLC2vjz9PMCDi9ttt-mtocd6Lv0056-_dpxSypbqU8XeYRvqZJZKV4iRZfjreXxzuqGrajeTFnqAcY7mWMnyOjt92pVQHFnToDpzJgqxyEHgFY2mCy3LV-xs4Rpo9CMnEBjC6PnlHDdZTexF6WRetw6Ofw-Jg0s4tSIYpoPQlMdM-F0MCWEWBhzPQKFp-tRR906FNCSQ8QqnszS0jpQAYgMjAYrUPYSIePeCzRbZxMIFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درخت بائوباب؛ غول آفریقا با توانایی ذخیره حجم عظیمی از آب
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/679227" target="_blank">📅 19:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679225">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJCULMDbM9HOjG-Ah98jYlzMTB4numXzSwAdD5mvLbssimGcfAQDdvyNqqwEHKtJd0cTcCrfolJCdiC5iXgq3OnbkUWZzFuE-1Zlie845tn4qdBW77l7BKxH7TBrFalF6sRIXQZajKsnShfEqUgFKp_dSbLJdwqqvWTKK2aE95sAU0snToUDvPbVi3i1P7YA0_AuIg1HdIKff3MHkwyXDSgTlx5nMVQ7Xl0FOd-U4EEdgB-VLcSurRrpICuZjXBuhiuBk1W3cBkXapYUTbC_7vAM2w-2ih4nkTxfrU56t4IkA-FTK5hgkAV4xNbJjLsX8t1HZAD5jIo4Yse77ZySUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/679225" target="_blank">📅 19:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679220">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y1zc-fDI_nz3XK-TF9DpQLgzkEMRBt5_lBndxjRJy98r32pZNhpoN27I3F6jOuZuAiFllLqbxvzU9uN0KHLZtJrgRCbIlM4agtXNQ-3QUeBZUMwZID_ss7k5S5_4mc84rXQKdo9dXQORrb5oO-cRLxl_aMHqTLtpzAa6EsZSBxKcDAEf7ChXBOFxFvmrPgCKeb6Fp84b0zvGnfY4WMMF41iBhW-bhbLF2zqlsWofy4wLiFiaEzxDotdQ48OHB-lj-CTNNschl9c9nb6q53makQEincXUcus76aFQXN-gPloJs4lfZq_UNyKr0ct_MCRzNWokRtNtbNwF_R9LyF6pBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ائتلاف نظامی عربستان - ترکیه - پاکستان/ یک مثلث شوم برای محاصره ایران؟
🔹
برداشت ها در رابطه با سند مکه متفاوت است. برخی معتقدند این ائتلاف، آن هم در زمان جنگ و درگیری ایران و آمریکا، به ضرر ایران تمام می شود. برخی دیگر آن را معلول و پیامد جنگ ۳۹ روزه می دانند و معتقدند این سند واکنشی است که اتفاقات جاری و وضعیت سوق الجیشی منطقه را وارد مرحله جدیدی می کند.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3236126</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/679220" target="_blank">📅 19:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
آقایان مدعی! زخم تازه نسازید.../وحدت، سنگر این ملت است
🔹
کشور زخمی است؛ زخمی از سال‌هایی که بر شانه‌های این مردم، تحریم ناجونمردانه، گرانی، جنگ و هزار رنج دیگر سنگینی کرده است.
🔹
مردمی که هنوز ایستاده‌اند، نه از سر آسایش، بلکه از سر عشق به سرزمینی که خانه‌شان است. این مردم دیگر تاب زخم تازه ندارند.
🔹
اما گویا عده‌ای، رنج ملت را نه می‌بینند و نه می‌خواهند ببینند. آنان که هر صبح با کلماتشان بذر اختلاف می‌کارند و هر شب با شعله‌های تفرقه به خواب می‌روند، انگار از ویرانی وحدت این سرزمین ارتزاق می‌کنند.
برای آنان، آرامش مردم هیچ ارزشی ندارد، مهم آن است که آتش اختلاف خاموش نشود.
🔹
تریبون، امانت است، اما در دست اینان به سلاحی برای شکستن دل‌های یک ملت تبدیل شده است.
🔹
هر جمله‌ای که می‌گویند، خشت دیگری بر دیوار بی‌اعتمادی می‌گذارد و هر فریادی که می‌کشند، زخمی تازه بر پیکر جامعه می‌نشاند.
🔹
کسانی که خود را منتسب معرفی می‌کنند، اما حاصل حضورشان چیزی جز آلودن فضای عمومی به تعفن تفرقه نیست.
🔹
تریبون‌هایی که باید مأمن عقلانیت و همدلی باشند، به دست آنان به کارخانه تولید نفرت، بدبینی و شکاف تبدیل شده است.
🔹
آنان با افتخار از رفاقت‌های دیرینه سخن می‌گویند، اما در عمل، هر جمله و هر رفتارشان خلاف منش رفیق است و خنجری است بر پیکر وحدت ملی.
🔹
آنهایی که فتوا می‌دهند و دعوت به لشگر کشی می‌کنند گویی تمام همّ و غمشان آن است که مردم را در برابر یکدیگر قرار دهند و از دل التهاب و اختلاف، برای خود اعتباری دست‌وپا کنند.
🔹
اگر این افراد احمق نباشند، قطعا یا جاسوسند و یا خائن که در هر سه صورت باید نهادهای امنیتی و قضایی کشور به مقابله با آنان بپردازند.
#سرمقاله
@TV_Fori</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/akhbarefori/679215" target="_blank">📅 18:34 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ab5c7b282f.mp4?token=IKVKDSWtz3TgjRfBvy92TfkSekpozCNN_TzQmF4U9lTrOEjQonaEwS17YTYYyJibAwHvA2Ab4iOxslbQdmLZ9865pG0SYfQQ8-DqLR7ipPDgTbPmm5lpHdg2AOIKk6cwlCxdF7sMSSKRvnKuNZjzornY1BZq_Il-7bzIIG7QftqQqCnkNRvOYZ1zDHxWJIMNad0J2B1gIX1fXa4FRwFNDr-i2e3WymefB2eGbgBlA5MeNUTIWGkVes6dmHChWiMLQdlMjf9oZDNJi72gUJpnSHe2_miC8JcQizgEqEQ7syeXW1WLjDDJbOPhVhQUQkT1dxHmNNoeQtm3ZB5HGlXUZIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ دستور انتشار اسناد موجودات فضایی را صادر کرد
🔹
در پی اظهارات جنجالی اخیر باراک اوباما درباره وجود موجودات فضایی، دونالد ترامپ به نهادهای فدرال دستور داده روند شناسایی و انتشار اسناد دولتی مرتبط با یوفوها و حیات فرازمینی را آغاز کنند.
🔹
ترامپ در این…</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/akhbarefori/679214" target="_blank">📅 18:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecb3d1485e.mp4?token=teu-kxp9CJNkzwJrSpgdIaxH6KYS4yptzB8dhsVAGMnj9GY6kAKKojnbAfFhPZGo6w5lsZWU4w1y_IKq91XJvQmE8a4Zn0MJK4VLfISkO9YSUG85Ic0ctdCrY-bZZMytmjU4xvA8LLyma3V3tkc-U20RCU39YJ2XXX1_m5fNbFoYj1o2qEgGQLTln43gn3WvQpNGkk1B4SDTClhDegVuZJs8TZ_HLIm3klQObI21WYRxxKOrGzyfDuZllTN7iFvN-mDIyxtABH3Cij8CC1KcozWP5fjmu9rej-n_xULitGWQb70QEuM-SOpaiMJmJBLShxm9BZ-ln-7n8YiSONmu9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
قنات نبادان؛ منبع حیات سرو کهنسال ابرکوه
🔹
قنات نبادان در شهرستان ابرکوه یزد، منبع اصلی تأمین آب سرو کهنسال ابرکوه است.
#ایران_زیبا
#اخبار_یزد
در فضای مجازی
👇
@akhbar_yazd</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/akhbarefori/679213" target="_blank">📅 18:24 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daff06e5cf.mp4?token=FnZQpc01PNGt1msfptBFeJRdmiCZcKiNFj-nxRuby0C4z-3V5IV6_-tSn7iPlCEa1bM9i8-PJjdppMwyk06ZgffKd0NDx7DH6XTklXDEz4psWKy1ryT7JK4KLBdZwEVkwB3xvFzXoFRYuFi9wlP24c2PIIUxmFPoBgo6XueSXILYyVuOldka1Y2gpRXNoIheu9M94Mpm6s39HSKJQvvsViBAbb-KcyBLUFgJCai5W3885Ej3jcnirNCjWOyWpM4JOUZESjhRf-kKsMHY3rgvt-i1_vYnHlPVOy9tt2AgeW9MELPvKJ9pHqkLM5Hu1ZwuaXe2XIAJ31iRPczcpnOFbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚿
✨
سردوش ماساژور و تقویت‌کننده فشار آب
رفع افت فشار
💧
⬆️
+ پخش متوازن آب با چند حالت
🔄
بدون نیاز به برق/باتری
🔋
❌
🧼
دارای فیلتر تصفیه + کارتریج جذب رسوبات
🎚
کلید تغییر حالت سریع + اهرم تنظیم آب
💆‍♂️
ماساژور مکانیکی و بازوهای ژله‌ای
🔧
قابل نصب روی دوش/شیر/وان
🚿
🚰
🛁
🧱
بدنه ABS |
📏
۲۵×۶×۳.۸
🔴
قیمت 1,098,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
خرید از سایت
👇
https://memarket24.ir/product/brief/58323/180124/</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/679212" target="_blank">📅 18:22 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
آمریکا ۴۳ روز تا مرگ نفتی فاصله دارد
🔹
بر اساس داده‌های بانک سرمایه‌گذاری آمریکا، ذخیره راهبردی نفت این کشور به کمترین میزان از سال ۱۹۸۳ رسیده و اکنون تنها معادل ۴۳ روز مصرف نفت خام آمریکا است؛ در صورت نرسیدن نفت جدید، این کشور با کمبود مواجه خواهد شد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/akhbarefori/679211" target="_blank">📅 18:20 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
آیت‌الله جوادی آملی: با ناقضان وحدت مبارزه کنید
🔹
حضرت امیر یک بیان نورانی دارد که بالاخره ما جامعه را متحد کردیم، و تمام کوشش دشمن این است که این جامعه را ارباً اربا بکند. شما مواظب باشید این جامعه متحد، مختلف نشود، پراکنده نشود.
🔹
اگر کسی خدای ناکرده عالماً…</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/akhbarefori/679210" target="_blank">📅 18:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15425cb351.mp4?token=NE9-IbPLWu6YHa0viG3hXuGetgIxGQAQJ-vHDstvXlrXtRFYBs-En_mC_t0V91-LH9CTgJjWFgyFNE0WQ2uHvR_B4wWSdrkDHGaOCeYfkTaKSTXbYR0_zZW9Fc02i5n3kFMPNcRFRe6StZS54p-wo_33Iq1C98LBBTb8aa7oe5L3sKEGxGUV4Vo6drFWzsTSr1HTvEE7pW4HhFPFTjjZR_gniMC5ECoRJ7sy2tVP2LAJonfcL8MFTp13htsOf_BNv3Ha_sLC0VINhOSukRqcvpjV8WAlrTM3QnAcmvJVfWvBn9VGfMrbspMwWI0gn_DVnTN-qrzjqBGRqP2VaOoIxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار، سوئیس را تهدید کرد
🔹
ترامپ تهدید کرد با محدودکردن واردات کالاهای سوئیسی، می‌تواند اقتصاد این کشور را با مشکل جدی مواجه کند.
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/akhbarefori/679209" target="_blank">📅 18:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679206">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/akhbarefori/679206" target="_blank">📅 17:40 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679205">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">عضو کمیسیون صنایع و معادن مجلس: در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس می‌شود/ فروشنده نفت وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند
🔹
علی‌اکبر رنجبرزاده، عضو کمیسیون صنایع و معادن مجلس، با انتقاد از ابهامات موجود درباره بازگشت پول حاصل از فروش نفت توسط تراستی‌ها می‌گوید اگر در وزارت نفت «رهاشدگی» و فقدان پاسخگویی احساس شود، استیضاح وزیر نیز در دستور کار نمایندگان قرار خواهد گرفت.
🔹
علی‌اکبر رنجبرزاده در ارزیابی عملکرد وزیر نفت درباره فروش نفت و بازگشت منابع حاصل از آن گفت: «موضوع فروش نفت و بازگشت منابع حاصل از فروش آن به داخل کشور، همچنین مسئله خالی‌فروشی که گاهی از قبل انجام شده بود و عدم بازگشت پول تراستی‌ها به داخل، از جمله موضوعاتی است که مورد توجه نمایندگان مجلس قرار گرفته است. وزیر نفت خودشان را مبرا می‌دانستند و تقصیری را متوجه خود و مجموعه‌شان نمی‌دانستند؛ در حالی که فروشنده نفت آقای وزیر است و تراستی‌هایی که پول به حساب آنها می‌رود، باید توسط فروشنده رصد شوند تا زمانی که منابع به خزانه بازگردد.»
🔹
رنجبرزاده در پاسخ به سؤال رویداد۲۴ درباره احتمال استیضاح وزیر نفت گفت: «هر زمان احساس کنیم در دستگاهی رهاشدگی وجود دارد و پاسخگویی به حداقل یا حتی به صفر رسیده است، استیضاح جزو وظایف نمایندگان است و انجام خواهد شد.»/ رویداد ۲۴
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/akhbarefori/679205" target="_blank">📅 17:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679204">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
ادعای وزیر خزانه داری آمریکا: فکر می‌کنم به‌زودی، شاید حتی امروز یا فردا، شاهد دستیابی به یک توافق، شامل آتش‌بس ۳۰ تا ۶۰ روزه، خواهیم بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/679204" target="_blank">📅 17:31 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679203">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/571d5e5bb9.mp4?token=DLcH2tBL-rECQfF5GJ_b1OEnb4UbcYNlWTA-X-9Vk5K-Oh9gzyKbX02K0FHzdTJPRsVkotmhy0Y0n2H1GkuBVJYspd_GrkTb5__S7ChKrbX-AMQUQ51pUjyzN_PyvjoE7vA-tZCCDva9FG1sWADE_u62JEVEsvKQj858JmoYn3QnTZOAPPcvoWBuhDwfvuKv4Y-jxP7TBGSNl7IjolS7HyN0gyPMRVLPAhdoUdja2snzMwIFTtKYp_ChGd34tyWqq7LGhO6aiLaxnX77pM10a4L_fkk9UVeIXDGa-TA7fNuxx-KgUokdniJ16vPC0b4-jgq5YlpNgokOwz0erNi9CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده مساحت مثلث
🔹
توضیح محاسبه مساحت مثلث با کمک مساحت مستطیل؛ روشی ساده برای درک بهتر این مفهوم توسط دانش‌آموزان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/akhbarefori/679203" target="_blank">📅 17:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679200">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دعای خاص امام زمان علیه‌السلام در عصر جمعه
✨
گفته شده هرکس صلوات ابوالحسن ضراب اصفهانی را بفرستد، حضرت حجت ارواحنافداه برای او دعا می‌کند.
✨
بیایید در این جمعه‌ نورانی، با فرستادن این صلوات، دل‌های‌مان را به عطر یاد امام زمان ارواحنافداه معطر کنیم و مشمول دعای حضرت شویم.
#گنج_پنهان
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/akhbarefori/679200" target="_blank">📅 17:10 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679199">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqpX-4W26-D3Xwyxjdaar-MSjo-8bcyb-MxFXjlKb1Woq74O1BANE51FL4iztaFKXIVQ-Rwh9yUhfQKFgPZaSFQHTzEKR1l91C9ntY6NC4gjfPGo9N9p-BlcjzvnKzawY0s1yyf583mhmsJxEwc_oBnbdTTMrq75k6D7349duyPLWC8P3M8nOIWs_aBg1zdmex4wajYY752K6509nC0iV1d9F2aEWV0ZZGwDcQ_xv2srmXPKKwqRLyS1t5keiW5nqMg9SMZGTHeI9ojPA620Y-eJedxJ0Ny5wCRnqanCz0Ekbz3x-Ud-WrR7rdYNdr_wRm-QG995kx4sFM1iLJhxWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
وسیله‌ای که بعد از خریدش میگی «کاش زودتر گرفته بودم!»
🥒
🔪
خردکن دستی چندمنظوره
✨
سریع، تمیز و بدون دردسر
✅
اسلایس، خلال، نگینی و نواری
✅
بدون نیاز به برق
💵
پرداخت درب منزل
🛑
موجودی محدود
🚀
عجله کن! لینک خرید اینجاست
👇
https://khabarfouritel.affdn.com/lead/48457
➖
➖
➖
➖
➖
➖
➖
➖
➖
5000 محصول تخفیفی دیگر
👇
https://khabarfouritel.affdn.com</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/679199" target="_blank">📅 17:09 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679198">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">♦️
تخم‌مرغ؛ بهترین پروتئین برای ورزشکاران
🔹
تخم‌مرغ به‌عنوان یکی از کم‌هزینه‌ترین منابع پروتئین معرفی شده و مصرف آب‌پز آن توصیه شده است؛ بر اساس این توصیه، افراد سالم می‌توانند روزانه ۱ تا ۲ عدد و حدود ۴ روز در هفته مصرف کنند.
🔹
افراد دارای بیماری‌های قلبی‌عروقی و کلیوی نیز سه روز غیرمتوالی در هفته مصرف داشته باشند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/akhbarefori/679198" target="_blank">📅 16:50 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679194">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fMsCLW7uCT0b2m85l_b4yGg49lLAEAqSQT-GG_FeByIkqt6DA7vXWdZs-D4guyUACJVGIij9mVJxtoJACpsc-L9QeAkqYgwMznc-BmAJI8M6kAqleXrqbxAie9b6UJAwl3jZJ5D7TfqFUvBFJWRc-GutnAbkL6_hPswr0miHVSUYIvUIZW6PdMjYoGl2KwNlmp4Ur1pqhRZjdRFhIk-z_4uegKUU4qDrCtbR2gi4mRHGBxmgh8eo7ExWsv6O-QpAWsMZ53rAmSrQrELVfZdCWS50m019LGdiblU3NJ9euitbWNdb2wpn_R21WXByY7276NhTHqeSlAJGzyvKn0vlmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wma4bTDlhpSyypM2bYBwPse-gzt7Yzdrole1Q_cgIFkmHiSxnrhslBb8UPJLpEXl3LF3pZUXExNA5v1pgq3nB9qPWsOHuO3kxYoWI-MQiZFDuDtrGFZbK_l2xie3aTIQ-N5xZWWDEArZXfocSmydYRsuAocOkj329Faiq_Ex9UtwzPE7kHQ1yIaRiH48IXZIpgrZ5YDqNZXTU1u-xU01Qnd5ZuDKVNDEgxKlGdnjd_sF1aA2qpXjt-YfxFT3E2QjHSfCjh6s7lYqyDxvF9ZfOg6nl2Yfa3svNaBCjjmQgI6qho6Q0myTohjSyPUPZcS8qZFhkC6-PUjAS4Wj5Wpdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LvBrZQQ1KZcB951H8AtVJPKQnLlLKty_3JGjRrIS3gNeTaXc8vXLjklz-zg3VSGH2dOX90uWiAt-UYI5uuw6J6SXboOEaS_4tZVFe2jsa1TO-uWsyz56b27s3z1yIAhL2htJPfTB3EPn6WJDN98iZQYEW0jczdPPHdnVFo_-laHJUSUvkoJOd6fBfdoPaQ8amTKKUDuKO0_LP2-doE4zzcge1F_U90osnVUXk0H_IcLqmRGY_XJguldcoL3L2wIgb0oyUMys8jb9eCvjYg6Ep7J4e9QbmjOENZPX6fn7hZR458bJ1wQIoFjWPiYzI3FAhHU3ayXNjj_f0bQIG57KOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RFQQ2qymBq8yeq3A-57_MxT6hMCW3WAevk_SKrfBbZpQrNfOBeQiC3d21FZczYlGi7OAArQGHHdv_4w0RcutorzNda636X4yyQpYh_GMOKKmkA5jVXdNp0qx74Fu8eJO4jgIBCSFK2YAnPUq2g1rCZM39BzKDJkPVYXTBsF3Gui-YuJgGUtXyDEk9kCypdb0mNuX9b3nVvk_JNxgG6-JD_V5s3bJMXRfqSnNXLzqHTnswNA1aIe1-g3Jw3vO9S2EbWQiFjumCdoP-vr1T2k_jDE1V_abJ__c5tDgkB5EUCzZ2CZ-jBluX4s8o1dPaMPUj6Sn2d8NE-WrOHCLgXF98w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/akhbarefori/679194" target="_blank">📅 16:41 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679192">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4478015bf5.mp4?token=djcS8gCiJei8wl8uAWG5ZiyToGgPB4OtbHDM4kqw7rgTrVyFsf3wc_5R8EtvxHDrxDMpOv_Ti_QM3HgVEnDluxxs0qc-MkHQiHcmzK2Po4DFPEsF1VwFU-e60KMOm9_lGr9ssxjqxvi8a-HA3yXv1KLNx7-tLvgSHhgTTqmQ6ZCHVkSwXaWJNY4kiQ-FXZBapEZAOuH9RqdTFXuxCsSjsO4kSqkZzBf3Qa51eLMNwrBhYG7iqlhwY5sec1pzVN3RFYCZSx8uSHk2Uaq_ZqoHSnReZbxrT4BogbkF4-BbajCK8jXhS2ql4tqXgDY4vJ5H4ntvqSt_D1MDWkKqtWifRQoF35rbfJT9feLgNqthstZ-niGYT6C2qjefjWVy9B9uq9Z9hspGB0es__ij_I1LGNYO89nkO-zsKEwzeOIi9lgsxqGRsRDXa7D1GXSsetvM7MvQ_z4c58JOYVhPzDEvLD4zdK8-8ob4txRl-2hZt3PsChAFQxvHhpy2QzZh-VPVQ-hRkvQHC3T40bAZ-RJwkeZEfv1NPn0xhgQmLIRR2Ulu1fkxE0vmH4TuttrtEf80rVRmXnp8FGtUfz5xRm1y06mq_m3SadM2ell4Inf37_QilYhE02KpKY2S90_yMomDzEP1zYPKhaPITjxTSytkLDBHZuftvENV1QBMd-czDf0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
درگیر شدن گردشگر اسپانیایی با نظامی صهیونیست با شعار قاتلان کودکان غزه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/akhbarefori/679192" target="_blank">📅 16:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679191">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/akhbarefori/679191" target="_blank">📅 16:21 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679189">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f3fdfab4e.mp4?token=t5Nn3x8V2VBk1i8OhjTjaA2GsLBCgBA1JC10lloDniDo3WHAX-9G_o7WLVfs1xudPmsvzlfubSTxdCN981OGjli2AmsMoLS2hDexVUWeSMePK-EgP1H4wQ6YD83kWr53RThhq4hXi976h-ptkuqC0mbHDNcLhIyicZ7ShbBZBpiFD5-6hnTfplJMFNeI67BpQOCwxZo8gnH65_gVUFweKMqH9OGju4p5xfopGxOl_2pbth1IVmh80mg-TQ0QqmOWLN5HnUkKxwt8enZ8guZs9CnQv0waLxdjJqToaaOlCZ_wCxSrYKqTlC643M4M-UEaG8xodbMaRa-nPZ89zSOaIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورنکردنی اما واقعی؛ تبدیل خودروی اسپرت به ربات غول‌پیکر جلوی چشمان هزاران نفر در آلمان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/akhbarefori/679189" target="_blank">📅 15:52 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679186">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c638a3753.mp4?token=ZkgwXHp5xgVzJFe0YVTyc5S5IbVuEwYn6sRjoQdUG1dQlS5GAM-TOa26K0J85-pR0qOV69kFChbjOHugqY0QBw6ZZDuT_cKBcY5qEId6nTvJprN2yZmxzX2BfBOjPLTZkzuHa7eAOdMYaNidopocN90XNgZKzHA6GjDiXoQS63mygM22jF9ux4Mqm3kmCjMadEVpV8fqL2DSW4piSDDyfHvySm_wpvix-gzIMToKnjgAScE4Addry8_I8XHTK0rxkP1cgYtITLvZWNcic1NbPy7X2YOloeRpac9IGMYMcrighDHzEPNXPAINWXAtib4DkzFc8ZjnIhJNjgsz4zRrUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حملات هوایی سنگین روسیه به مراکز کنترل پهپادی اوکراین
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/akhbarefori/679186" target="_blank">📅 15:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679185">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aab0df4751.mp4?token=qcO1olWNQtWOlYW38ElsUbmelEC_4xeVQBTiyNpGuHKDXDvfXrhb2l37WeMfwrxdFipTVrjqzZhClOYNp3lDtXKMU2dhk4jXLo27BT2iPJaJSunED2kotXVMnnYIuAOZx6BQ-lfnQWZIk0wD6JPuVTH-28lY_FU76kFQmpp5zACQnpeeMob5QbqatrzDovs4oouRJVWIDQCMpx9KJzFR-nStF5W_KQlkWna9e8uxYkfLVHRNWiVf4kaVLnIVJnY8Dpw_u3_6TSVqT7RYsipYcdr2fG6Ga7tXJ6UoUx_EBNQVSmYYkwS-nY5MfyZlrNtVhF9sxXtfIfuKV59e-FB-RxsVLFyBcnwhaeE4ePeqf4O4dmEBXekwW38TXbPuw56ANrqy1jEubITLjw74etaad9hmpdZX19MuxQYDg0nnnuq4WC05-qSYeP0hAcdxZTSpX4Lpq-yBejHtjU12rhM_nEMgh17vjY9h1lxpzCskmMfNkBew2A_if5KBN20S475Mg103B7OU0EfKp4NjoZme0ru9TD0g6Q8irJJfkYl3KbQ1vOhAhtPXn7Jg6fcwVXinEkM1guKiWu0E9y9uQ6nOZBkl7cnvxFInxStxYSQCQ8b1MLa5lQVsAx5sGQMiusD8nmw2A1xaqN_Xjljh0UaKtl3Mj-guD6mUYg5TRCnWtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
از صفر تا صد ساخت آباژور؛ آموزش ساده‌ترین و شیک‌ترین مدل
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/akhbarefori/679185" target="_blank">📅 15:32 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679184">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXzC6i5SvZzTugyF1wSw-vFLIbOYuXwzFx9gI3BTG_lHC-ktV_N31JaYlG4dt9RKg5PjqLnMmzNPTkeudw3fsQ9n62K8yfYfwdebpacxpQ2pqr9HSBUhCVCDFMW2GF-o2BTKN_JLnfq1KqWtz8k9GHdIw5oIKM4obAOIg_SpqTHr83NvhhkIKAe9CgXs-xUX4P1hnsD8UCDpxka-Vr3UHSmDtao8I02In9GNxRmFqgUmtGRpxElFNOoXskRt8L8Ux0qpPKM4NBCoCu_-cPPAaAc9NGd6YFYPk5PXtl6Y66rcaU-DmUoid53kdkEPsR3ZmCNl3XSjcBXlIi5j0r_zDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/akhbarefori/679184" target="_blank">📅 15:28 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679183">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/785649430b.mp4?token=hvB5zpij57Cy3Nt5zvQCKkrdK_jnxud1x75sR5BTLEJ-q7a3zdxosQsCFj7ndXV_2--qO7hqjrGU8AmgGSGf0Y3UFTo3nuxoiYOqT153xsgH6qsbE15KFpYCFISmvfN-dFQUwZwUVU-RE5CUvLOoJpI12uJ-q6_BdvAplU3NsbVAEiJ86JT92QUWJ8-HWWlJDYLEVRhcXDVtul_f6GhnAdeM85xyFvm2iOammq3n1lKHWMcpr-sv5vWLZbozTB5EWumhbNiP56ZOoKsUp4Yo8A0H3NsY667eyUuB0I30PNBntNJkflFRk5ZJW0_-ExIzAwTGi6NqIxjuPyzXud0Faw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌و‌گوی اردوغان، بن‌سلمان و شهباز شریف پس از امضای پیمان دفاعی
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/akhbarefori/679183" target="_blank">📅 15:26 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679180">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fUSYKw6htpsTkJLfyDJZB6dBcZk7SguWKho4IhIHs2-PsIMDhOus_fY6sk3qIYcytk7y5OrSbrZRavFBvIvy2214_J-IhMNgudZt0j6-I9C4rDw7pa_kHhpp_aXKWe0EVhe0_3zYsTUQRFKgh0PjcOKSPOmb0xnYBxsGdUBvZT6vRuXpGAs90BRHUmEkZDHwHActKs-9CsXly3WXZ_3WPBc3JKsQfBDT7mCIVAJ4Wh0aYTe8aZ9MSqcMZpUbkVvkssCbLLjHXmzNnLKTuUmOxHvUFxE93f2QLH0c-gVFXYBCwzVwRU15GPwEXy_aR3ceDtk269xSGM0ByLHrweNDUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همسر اکبر عبدی برای اولین بار عکس های عروسی خود با اکبر عبدی را منتشر کرد و نوشت: ۷ شهریور ۱۳۶۵
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/akhbarefori/679180" target="_blank">📅 15:16 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679178">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
چرا قبض آب و برق خرداد و تیر ۳ تا ۴ برابر شده؟  اطلاعات:
🔹
هزینه مصرف آب و برق مردم تا ۳۰۰ درصد افزایش یافته؛ مثلاً فیش ۳۰۰ هزارتومانی خرداد در تیر به ۸۰۰ هزار تا یک میلیون تومان رسیده است.
🔹
دولت باید ساده توضیح دهد که آیا الگوی مصرف کاهش یافته و مردم را…</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/679178" target="_blank">📅 14:54 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679177">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9f391c287.mp4?token=YDW3SAXpjKimc0PZazz3H-oALlzH1SBqXtzE_2299xfJhqtpxVv9ppi7E1o3VNreblcoo6a4I3sctESfSCUlt_X5gUhunXGpIKdfJ_6K-z5Y8gfGP2SCH3gehmj04thabDeKLvsiLjB010FL71fhfGCyGUApOiiaNf0E2rnW3x78F0lSUDJh7_Scq07V8Pop2dV8oBPdrseaXqssgLEeUBgQ_RzIoS1kL9FzvLTTZ0y4EJBbnjk6kglvhotCwRhBtrFZAzCh4E3m3NUh6lhAAYafPqME8aHztky0mKhCYk7TWWADkXRNTdSK0lT1BqtVJBe2EaDcNsEhm49ZwOAAnaXpH2rcuer6OaPUOoY2gUSFs2_94TvNtvfxXGJN_kEzsRfE84GcQmWSMYGUYKusxid-tARyhCXfn4Fbtz8oUJPCFEYMwvu2eOkZjPvImyKA8aFY7YXIyWbM4Fy8Vw8sW6fXhduGHyqSOMIJB5rujdlMIaQO9M2nJYOTEzYWyk8zPIZ6EtQ__EQ_Oh_UjpDw_QDos4VJyTxZKpecZWKNdiqsVbkXpK8h975j3A7AyTjgL2QWEjdFrOb6I3OxjBkTb4-XsMT01D8gDbmPRGbhQu6YUi_g_4Sbml5mnc2ozcoGM-STfM3cIl6IsDrwO-FqagDPEqhhbrKaVolzInbR3QY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تیزر قسمت بیست‌وچهارم از فصل پنجم
🔹
در این قسمت روایت تجربه‌ نزدیک به مرگ آقای رضا معظمی گودرزی که به گفته خود بداخلاقی را نسبت به تمامی اعضای خانواده حتی کودک‌اش اعمال کرده و به خاطر شاکی بودن از زندگی، از خداوند طلب مرگ می‌کند و دچار گرفتگی قلب و جدایی روح از جسم شده و با تجربیات شنیدنی در عالم برزخ و بازگشت دوباره به زندگی دنیوی، تغییرات رفتاری محسوسی در ایشان ایجاد می شود را نظاره می‌کنید
🔹
قسمت کامل این برنامه ساعت ۲۰:۳۰ منتشر می‌شود.
#تجربه‌گر
: رضا معظمی گودرزی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/akhbarefori/679177" target="_blank">📅 14:53 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/327d4601f9.mp4?token=rM41Vmng7Hn_uu02sh-Gn3yBcHgJh-vY90hONM7HzOoA3Am8_aza0SW4gLxdArjt9eVJo63Fj1L8K06QcCPp2QY0KRBwqOgsEiwdmwoaN6RF2ldVlcyZxsXjWinPxSG2-rC-OVpqYapEBOxuTTlRjRfTOa2uZvlpA7hqlGCIE08dJivbCQVla47Z751zcY6TuF57SycS13WHSiSlOYa1Bp8OZElhh-fgAsEaIM2WK7sfoo2qBFtC6g1YPvO2krStCHiPCtgdann1i0dNbNorkTxZup4S0F0Ac67qf5d3jhYkzlcaHs5gfV4sHtiCmHC_6IJU04IpUlPPmxNY1zCLeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/327d4601f9.mp4?token=rM41Vmng7Hn_uu02sh-Gn3yBcHgJh-vY90hONM7HzOoA3Am8_aza0SW4gLxdArjt9eVJo63Fj1L8K06QcCPp2QY0KRBwqOgsEiwdmwoaN6RF2ldVlcyZxsXjWinPxSG2-rC-OVpqYapEBOxuTTlRjRfTOa2uZvlpA7hqlGCIE08dJivbCQVla47Z751zcY6TuF57SycS13WHSiSlOYa1Bp8OZElhh-fgAsEaIM2WK7sfoo2qBFtC6g1YPvO2krStCHiPCtgdann1i0dNbNorkTxZup4S0F0Ac67qf5d3jhYkzlcaHs5gfV4sHtiCmHC_6IJU04IpUlPPmxNY1zCLeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله از حمله پیش‌دستانه به نیروهای همسو با عربستان و وارد کردن تلفات سنگین خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/akhbarefori/679175" target="_blank">📅 14:47 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hTvmH1Jp-ArTZD5sF6shLM-g_yHJKLP7GoBB9xUkbuoU-BPKVOggFa6q3xFZBgVgDZ1bxQGQSXIsm2f3vyOo6Dc_RO8ccjnM7p-T0wUKGJ-idRs3E1Mnkg_MM4qt0BcR1YWH_YnDHoEKWtd9o0WLnyJ4aAarj-uq8oCFxMRnAPJBJM8ycZty6UsSXHhF8CcrkUOqqVOX3Kkv-jtXVEsgfMH2ykN_5f6Z7tQSSPf71CgUBrj6fwlOa9Yw9Y97Z_sSRtySxBMUyCA_tWlpynwGzxmjd7I-yJfZ-cbA0OIGBZe5qvPoWowDWkfEvZ8dbETFZQv7wQBCojPQpwfbVN1uDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تصویر تازه منتشر شده از صندلی اف۱۵ سرنگون‌شده‌ آمریکایی توسط پدافند سپاه پاسداران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/akhbarefori/679174" target="_blank">📅 14:36 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f7102a082.mp4?token=IjxgTXKgw-LauEAUU3iukblCGCJD8zYTeR40sNRhJ76Hl6Nnzt7vUkapSLAHn2PmGPJPefdV_IWb0roLi7-FshHsscFToje2QtQgQpwITVYdPmq1mD0PNNN72KuLk40qX8bDqni8S965Q4YkEqJC10Z3hbw8kTZmtpwG1aXVfPVQVviBqzzeENjv2cXaIDYh6SrwxK3DNwCL1XVP_NS-d9PGbPj4Q-g5JPrgQTYS0Jp7SNVOdOcr_m8HuTRcTc7j5oyEuqepzaj9GGxuepxk7aZNM3WQrEACfX9qUJARE68QnPZq0BaUOTmMICwTb7gHTai8uAxTo4x20YxfDW0oJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری از پهپادها و جنگنده‌های منهدم شده آمریکایی توسط نیروی هوافضای سپاه پاسداران
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/679173" target="_blank">📅 14:30 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679169">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HK3yydbxkbqUPtzWxWAzY4hM2On5mLe3-WbrSuA7b_ai8SLFk6LLJxxrXqnL2KoIm9DqC2P2p6O0wzp0p80h2N3Ft2NKtR278NrkDbh_hHRUDSu1nHJS7YY3bykuBjGPE1iqs7SBSj7hBtrwGp2oitX67Ma_rIYG8fAIOIOTczpZNXJrrjZxpCHSsIOEU_HUvxb5q94A9AtyhSkykIPMfPcVMAFIjalXzCQ_xcztpSrYgpU87FXDqM1RZpwMv-SzjcbFr93haI3nVe5xy_uyAPOIDqqKgNKk8oR5o4zrYCIsl5iEoB2hrUArKWSbbAWLh5VceiJCl3hVGkJF6Cz1OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iKgPI5kuVy9yMSK0QLzbzZ_60yCVtW5qHxX2A6XoZj55XP9CLK_nNqgdDjYBOqeqfIod6mNBel4P40uFzy7Vi67gmOTqsCsVGangUU0Ng_v2VqdWoTX_IHXPzlLmq2xSvcTx0hb2QTfP1JJJZ0wPeD3uYu75y_1DebvwGuokDA7eWIrmUPmlI0tnAXxk6UuXxUcTU3H_WsLbI_3XT1TJbr80ZHslTWYSL1eQpo5Y14qnnAfnWhLlSzw0UApp8zidV0wbWK0NvMInkECsfTjWscXkgDn6-O6B7m8wq0U8vD8gpUr6hTIUU-s1o4UXSWch0_duydQoV4bqSc_XqLYTiA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
کوچک‌ترین گربه وحشی دنیا را بشناسید / کُدکُد؛ شکارچی مینیاتوری که نمی‌شناختید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/akhbarefori/679169" target="_blank">📅 14:13 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679168">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYBJixopkVGzJwA_T-eCFUhXnlfhbY7BB3ZaRw4mQKkbuGK0PayUB3QIszlX6C50cvtFjQ8Xj1NaCNQNpKQIpVteAYdmEk2PpIglJTbwdJxps89xbsMSs3pHsq2RuHpIP_RNmVS6turqeAjrSq9Hc7YFzMJtD7IokzzDWuO41Y89IkVcKIuDc7FppVTe-eOkaMqAEuaP32Ch82euK1sd29foCeTR7_GT7ghKc_LOgx0S4jOWi3HkdjGlqq3buL7jYXDO2A3Qk310he9yX8hAqQq1Q4JfwQGZ93iPVlojt4PcRN_Mgp0A8VPzuS9irHCG7Istzg8vJx9P-4TBqjMjQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام برنامه‌های هیئت قرار در دهه آخر ماه صفر
علی جلالیان، مسئول هیئت قرار:
🔹
هیئت قرار که به همت کارکنان خبرفوری ایجاد شده است، همزمان با دهه پایانی ماه صفر برنامه‌های متعددی را برای خدمت‌رسانی به زائران حضرت علی بن موسی‌الرضا(ع) تدارک دیده است.
🔹
این برنامه‌ها شامل برپایی موکب پذیرایی از زائران پیاده در محل تپه سلام مسیر ورودی به شهر مقدس مشهد، پخت ۲۲۰۰ پرس غذا در روز شهادت امام حسن مجتبی(ع) و رحلت پیامبر اکرم(ص)، آماده‌سازی ۸ هزار ساندویچ برای توزیع میان زائران و همچنین برپایی موکب اسکان زائران در نزدیکی حرم مطهر رضوی با ارائه رایگان ۳وعده غذایی(صبحانه،ناهار، شام) است.
@Heyate_gharar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/akhbarefori/679168" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679167">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LCbNJ7sL6RmBtzDYORS90w2iLq92W1PFXwSW8bEdAe-Rhm5bcm0UMkNlCywWveRp9OyQJ_W7QwRZSCSg0-RrXbaXe_O50TBz8nPp44425FfU4Pi0bwGIaNd-bA2LxZupeOFp39A1th0VvUoPggI1ZEkwoq1OZ8OLz7Jb3Nt8-hfZOL65OQE1CmJD-MoxywRdqL1ISi7VOur_KWoxasHVhMngm1ehKXWISen9lOWu_GorKOoQze6VnK_HVCrmuUUrlrdZpJ5z_5SymWYGuzdC7PaNU65YMS2iiApxuFXQbnG98YfKi4qAjQ06HAVrPT7d0VElBD0NSOPl7KF16-cArQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
«توافق مکه»؛ نام پیمان سه‌جانبه نظامی ترکیه-عربستان-پاکستان
🔹
همزمان با برگزاری نشست سران ترکیه، عربستان سعودی و پاکستان در جده، گزارش‌ها حاکی است که پیمان دفاعی سه‌جانبه‌ای که قرار است امروز میان این سه کشور امضا شود، به طور رسمی «توافق مکه» (Mecca Agreement)…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/akhbarefori/679167" target="_blank">📅 14:07 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679165">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F_OkTvNIi_4JzAZs0OMkIYd78vpWo_RtVRNWWXb5RQg4BrnVVz4LRhmLNfAFbVIRyJREzouOgGFplQd5ZdcEp1mJNOKlFekfjDX5sFZUXvw9IuhdKscM5SctGH9TguUTuuekRsO1nb9y1jMpatinQlWUixG7m_2edRfQp7QZ7BW-SQSCuLwTbSDdzaAHwif88H1TeJt0qMMoFgYO8ozkB4x90jkF2BirmY6RrqpWQXJ8YjmjLtR4Blpc2TdhOxfjK1Ghh1Q2uVZKpHDrcqKoCOBMXmOg9sUuijtCW-2rLrFOTzpJYLYeS0RvfPJICj3yReaPKdIoYpNt7AUVCjzomw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
خرید قسطی طلا تا ۱ میلیارد تومن از ملّی‌گلد
فوری، بدون نیاز به چک، ضامن و اعتبارسنجی
با سرویس خرید قسطی ملّی‌گلد،
می‌تونی طلای مورد نظرت رو همین امروز با نرخ لحظه‌ای بخری و هزینه‌ش رو در بازه‌های ۱۲ یا ۱۸ ماهه پرداخت کنی.
✅
بدون چک و ضامن
✅
بدون اعتبارسنجی
👇
برای مشاهده شرایط و شروع خرید قسطی، روی لینک کلیک کن
🔗
شروع خرید قسطی طلا
🟢
ملّی‌گلد؛ پلتفرم امن خرید و فروش آنلاین طلا و نقره</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/akhbarefori/679165" target="_blank">📅 14:02 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679164">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YyH-Gc6yoVCJqGJhXlgFeVOsTMWK8l1x-Rt-etSurXi0xIR3Kwiu5wvvb9a6ZmpX0o8_p8lwBKM9LOHQNNyOkFQWnbIGJ1MRDomSt-A4PC7SzpMaeOSftwn5tMzuyYQN8YUZRbyQnW4Ig6mBdRt3QJVvh5VzthCnfbtjgrvSy8TOTpXwYPGPiwlJ14sTbQkYq4oXmvfC6lJRIgXJM38MTgkpvZbw7SbOrsHwwNwrTBSyw7UsgZRZUoFO5BWEufpOGNELM5wd8zG8p8lkIQnoq2n5ED0anDRQYTfX1kqEgCnPSbWNWWed73B49ejB4U1kS0i3eqxt1TTe26vw_MFtQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مردی که با لباس عزرائیل به بیماران بیمارستان خیره شده بود
🔹
مرد ۲۶ ساله‌ای که در ولز با پوشیدن لباسی شبیه به عزرائیل و در دست داشتن یک تیغه بلند، به بیماران و مراجعه کنندگان به بیمارستان خیره می شد، دستگیر شد
🔹
وی در دادگاه مدعی شد که لباسم شبیه به کلاغ بوده نه عزرائیل!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/akhbarefori/679164" target="_blank">📅 13:57 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679161">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04bfdcecbd.mp4?token=ReThIQRB7Tw4r0PVCJ_kq3knEEVLyM2Eoyf9F_rI2rGs3vU-9JOVUl-XlIpU7kao0cLqco9re9v_NxUH4sWrvQSQpMpOI_JBUtXsTFpo_XSz3wFBwy2b8mwJzXgSIHlZw6_Tb2yY67bJfBXvPO11FsKwjPG_2fGg1GCRnVqjvVPGg_98oGKluRRlbyaWFOBRa5gsyHvbIkQYM71vVg-cqWTEOhKS0qXDqC36FGN9ItDQjHQLMLx2IFG2xPwVLuvEo5qWDjmikEeFwuHoqUjUw4Gu5DPt6DpR2CwhvyYAbv4xK98xi-FXOiryVVG9njWqAwdqnVBhBXd06r-S5UCqzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ جنایتکار: اجازه نمی‌دهیم چین با رمزارز و هوش مصنوعی دنیا را فتح کند
و پیشتاز شود؛ این دو حوزه برای آینده اقتصاد و فناوری حیاتی‌اند
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/akhbarefori/679161" target="_blank">📅 13:49 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679159">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
نتایج تحقیق روی ۱۰ میلیون فرزند: ترتیب تولد بر بروز بیماری‌ها تأثیر می‌گذارد
🔹
فرزندان اول: بیشتر در معرض اوتیسم، بیش‌فعالی، آلرژی، آسم، اضطراب و مشکلات مغز و اعصاب.
🔹
فرزندان دوم: بیشتر در معرض میگرن، زونا، سنگ کیسه‌صفرا، التهاب معده و سوءمصرف مواد.
🔹
از ۴۱۸ بیماری، ۱۵۰ مورد به ترتیب تولد وابسته بود./ دیجیاتو
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/akhbarefori/679159" target="_blank">📅 13:39 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679158">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e47a188ac5.mp4?token=XwqSPpGZJieENBwOo0YE0PEzzmJLC30slm1Zvcr__r_uoVXcrIljszK0ENdEU5HJ-Dcqhqf2gIfLwYMx0u8oX3pEm0aIEsbcu6emBvOZlpqIk2KOcCm5Ds-3bfHHp_BqdxlMMJJnDcmILNs8K1CfhNFKmjBjcCAs0F9A4k78hmF2Vls_z10H-xzbteba11jNC_Ywwo_b4KUgtfXonqWRzFZGfQsaFn3NSsJiGf3sNv-VClaftGQRlV7l5LMekQzKr_S7CWUQaT2bDl0DynBa7M_pHR6grFvVVNjxbUfoTJUjYCLoVWsCPoC5x16pMzm34CJG-vh6mwcEyqRAJYOmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هر ویتامین برای چه کاری مفید است؟ این ویدیو را از دست ندهید
💊
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/akhbarefori/679158" target="_blank">📅 13:37 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679156">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromچِشم به راهیم</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f5a76ab56.mp4?token=N4kyn6TkvoE15Pd_Q8a269o4B86rltz0_UwhhSnvCDMioOYMPfw1VrQvr2C7dEW1rm6PAJUvI-Sk7KHc7Xe3O2McbDMlp-X8ERhwAbV5IMPtu0iNguLnqaURlHxPBS1DjWhHXUOMeQ6Lh7CX7Ft3bDtEr97NNcGe9TX3nAJcs98igLLRLVUNcj6RCAr2TiOXx32Kgi39nMQLQmmYbkiXjdKlcjw_HHXWzlxMa0_5Xtd4R37SJF3JWM6wBX66t_DcN6-r77SVhtQrRsavjH4yZLB8-2G-8I7CuwKD7c1aXuaWgDgR231jBh466nQxPnZ5ahiwXXDduwQEQ_slF718-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎦
۳ روز پس از اربعین/ پایانه مسافری برکت در مرز مهران همچنان پذیرای زائران
🔹
۱۶ مرداد – ۹ صبح
🔹
تازه‌ترین اخبار و ویدئوهای اربعین را
اینجا
دنبال کنید
#چشم_به_راهیم
#اربعین_حسینی
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
@Cheshm_Be_Rahim</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/akhbarefori/679156" target="_blank">📅 13:29 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679155">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8105dbeb2.mp4?token=teKhNWTOLrAQVRtz9H1k8-q6G64GWmp4UsSSAq6X77PBE7bnjhTthKMALt-4YnRjefKFAOJwXWkIZK-KRxibMdOv3l08liPtJbihyUiP2gXUelVOaMC6sT3_fPN0sTpWymkATCBLg-k6SbLlBihZpDtJd4QBBv1fuWO2EUdCwUCj141tDTYOci7CpDT9Hg7WGBqlcRas174IR9KKdsZX9Ug9G5Z5FIuRwYSEm4sxgyg7AhUqFX4GfiVmZ3dXHuBxSOQOuG9iHi-XxE1M_wc44R7P4vW_eMmeF87OzbOPWR86k5Z6EgkowZBrmKTDabQNyPaTsxn7NSXhJRsXeD8ZNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بلاگر آمریکایی: بیشتر عمر به من گفته بودن باید از جاهایی مثل عراق بترسم، الان در یکی از بزرگ‌ترین اجتماعات مذهبی جهان هستم و همه چیز کاملا برعکس بود
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/akhbarefori/679155" target="_blank">📅 13:27 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-679152">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZurXuxHgQLpJm4oiyA3vBB4TTsrS_XDde1KTM-lLYyhA00FvTZEvQNGFUTtkBNglu-bqY0Rb-lY8iZL-o6eVu-h0b4NG3Gl3RuC2igydIFtcEmUwojnsNLwbFDhFiQT4_uqlYe5sRctAoI2NwhkxU6pGA-cFNeSiTCnKEZQG9qFlKzauddbfdkXsnj8YL5CiIK-sWhlGcPwJUUAoSb9TKtlKmLpWj7PuiYHIG4U7qYJwjWY_kbRSYXvBb3oAvFh8e28d6fMhhUZK_KlT4anuS2Tt_sI6I0E_nVuUwBRFBdmt4BEuZkEGHkP5e6txKa9qDF-LTetfLgYsI-pg6QnIkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uv-XQ5HnPJoyaKADsB-gUZTkfPtX6mquRsH-p3K6mpWtD4u7LxeEaSscLYEvVwI397uDfDr5HhYIEr4leuSgHtVfZuv_SdHSSXcIl0aYzzBVPN5alZRMACa4Qh--FECbkYFPp1v9g0JpN09FfmxSPkF8CrD1LYYvY2wePoZSNnzZIRx3PJecBsNQm4ARW9uLFNdBORODCCzATapu-Eb41STYFJf80PNYMElsscjF9VIkHRE7OAynihDNqSpUuOZN5iEqVyYraY7pNatrXQoeqc5EwfLuEpbr14KYk_AGzRau7_i_jUQ4uWPOY1mJO7a6GxTSIDMlZJDSfCjbHNA46A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویر هواگردهای منهدم‌شده دشمن آمریکایی-صهیونی توسط سامانۀ پدافندی نوین هوافضای سپاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/akhbarefori/679152" target="_blank">📅 13:24 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
