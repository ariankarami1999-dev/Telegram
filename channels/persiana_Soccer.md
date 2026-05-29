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
<img src="https://cdn4.telesco.pe/file/G_wCbs8BWU0C2nl5NuCqMlHG9PdTL_uDYsRduZM8alQ550Xe-kUonwghcU2-eh6UDipHFBZsRDKFXeBk0ye8RkW3ArGnSFQ31GAs8anRvJSxRCUYyQsq8y0a3Pf-v12WxXoxur0yveGZ2xUUe4pXy93JfWm-HhSqlCXdRHC5lxLikLLn8jvxcWcRAKtfHeKdN-U3FG1LhTmR0uDRgZ5kXhb7aaIT03Tg1HtY7bigW8hg5tZ34cJgZaqcSvO3WTIFqKOk62w5ZCtDiKU_a_8w1XGJ90N7TK3XKWZZuhs5sXBJ4L7nS5FK9kbVi6dPcheD_wFk-zHroE1V7ftG8pmN7w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 182K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-08 14:09:23</div>
<hr>

<div class="tg-post" id="msg-22423">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OA2QeNw6AQYtn59xWNq8LZfiFn2I-osK2tHQRtVacn_vgHrBRO8IH4DshTc2N3DrKMDK83XZW8mkPBkJMiH1gH25sp9HAVhFDJi1Wk8sfPyH4enJOMSlARiRfU4h3sUjxxVjElbObBs1B_Z9y4J9kTgbnOvAceGlT5vzh1qISIEPjCFhZbpK__6BfcWL1joUbzwkshfU0bET9pUmDUW0qmbUfxnKlgK5_UAZtPg_DuFhUhShrHrdY5j5fhKCarPjdk2RDflZO_-vNXlht9bLFJln9nsSZCMgjqufcYhqU1-EF3AAPB_iPZzF3sl0Gl7QJwiCpM9ljzqSwuD62wqrpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جرارد رومرو: یوشکو گواردیول مدافع سیتی نیز همچون خولیان آلوارز در خواست جدایی از منچستر سیتی کرده. فلیک عملا با تماس هاش داره راه انتقال ستاره‌های مدنظر خود به نیوکمپ رو هموار میکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 908 · <a href="https://t.me/persiana_Soccer/22423" target="_blank">📅 14:07 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22422">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/do4m45Yt3X5m91rb3bqMPtd-FgRJjrwmmvppRunJOebxfp_UNyQ3xYV0TBWKtolNwxHtlfdUFvmsmkll00EA9fgPEE7GerBwhS43IVwu68HJSmjoPk9fL0qom0ET3safwaaM8judu67LYnni2RxX6ELaKd1aK3deApB_8T-61R-VGIQU1Vr4pQ54uG1K6okPlswqvR75_EFJq_CIcCF6sR7c0E6csWVWevlxGPjpTaBVrx77cOMO4FR-NBT3fykO6t2V5BD84unfutcFT040lD52KwCkspT_FLZhbk3v1yxtrUZhzQTJtkOFYnuTjhS2BRmhvwATM2jHmeG_cONZsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌انتقالات|ادعای‌رسانه‌های‌انگلیسی: یوشکو گواردیول مدافع 24 ساله منچستر سیتی هدف بعدی سران بارسا بعدِ نهایی کردن قرارداد خولیات آلوارزه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/persiana_Soccer/22422" target="_blank">📅 13:55 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22421">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5jpgXcipW6z4Vwg4OAETnl67lundILyPe8hYIcXLj4xOzr6Yj--9avJLLpygv130LfkVej-M3ghLlvZldNSPG1wYHhf_9gu6Su63zIHOS1Qs9kIzyKnSwy7A_5udfme49vEka8tpdBhyvPWWWXCugxeDDrQvgFdWHBN1yvnzrTeeVCFEKUdC2NQ5FrLzZ7JyBlsXT7PGPowTdfhjum8l_JAXchchL0NsEUz0MSNaf2BHOxDcg8dxRs0IpR3vznC6Ur3_xcWyVpF225K8JdIQ1qqqTSUIvl73iBAo75R0CtTYFsGvPdoy3eiYjjvpHj6p1wCcGriGNnEWq2PbRrpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات؛ رسانه مارکا: رودری ستاره اسپانیایی منچسترسیتی میخواد از جمع سیتیزن ها جدا شه و باقراردادی 4 ساله راهی رئال مادرید شه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/22421" target="_blank">📅 13:06 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22420">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jq4b441M34tyELi16tz4F-N3OHz2lzWN-OK3j8ncDJ8TQcA9AzdvkP5ad17YLaxZf7y1KX8EcWswUseL1uqExrWLpSZNfSr5B7SE3E2ItPDK5OtFXpa_KvfkoBWC51lE1e1Brx0lg7VDAf6PRmigpv1um96Sod9JAF_2YJ0evzFHGZu2j5-CzQgErhmqiFf9a8cixPaRUCvnKmDAfUwfnCAJ3Pnkpc-zsuT1I_Rc8R5pgj87uqDUOlVUbpjagr1m7J-yGX0qyGSqNDaKdmLSCHQ_a5ndPTib7DNlLZicy6KUJMjMkyhWRX5ULhgLmd3XykIw41hq-0d-6qquJTCc5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... یاسر آسانی ستاره آلبانیایی استقلال امروز در تماس با علی تاجرنیا اعلام کرده که فصل آینده رقابت ها نیز در تیم استقلال خواهد بود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/22420" target="_blank">📅 12:37 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22419">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uim-hmQB83m5MwaH5enr-yZJVVTh3gmBOfoTUZ_ELE6RcJIE84yFbcwVDj-LKo-fBDSqKEskSiokH2Ed-AqoFO9M3BtrXcDFO7Zt6UNbGO9hnal2EtrnMadc5zUs2W_0Xuc7cTwmTEY6XaZ6uKRSnjymsh24HoKEvksMTEFm9WadL2NEdtNW-EYup4_w88nuMt5LPq_GdrSHQNXx1izO0rlo09L2KyMdb6sMH96_U9mFf3jXLgelIw8g5p8O6X-0bBGDuM1A-ATU5HGgUU2eLVf9D0r4EDEZlgfJmUf18hbCYNcxWaQ0ClVukip-kzBIt-fkXdwLP-rWXpxcxCrgRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/persiana_Soccer/22419" target="_blank">📅 12:26 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22418">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ej9myXIU1TvvAqXoWkr48rV0TAwQ-6FYBXgezSnUZh1W9ULuQoWUIKH-f_SPrqOiEsXxr4985HpxiwW7ocGmq91QPBE2aH6Eh4KEAxiK5eOxejgjQ4SyZkLPtmrhpy1IjbuiMswTGTlk6FQPWeJpZ8pglUPKmplZ-pIMlhpNsKhbcmCADvcSqKadwk6E-te8VcC5e2oWTT7qFo8PS_d4GZ9Ewt71rhDsz-JCYwd5_FWz0gWsq4kbK6vF5ROiSfRDkxwJ9TdM28PSzMBV4Fdz9XNhlRjX-lTje3SOA6SCfbsfhDLQ_HicWdO99VtdliIairROo_NZUJZ_5-We0WX-fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🇪🇺
به‌مناسبت فینال لیگ‌قهرمانان اروپا نگاهی بر ۱۴ بازی گذشته PSG مقابل انگلیسی‌ها
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/22418" target="_blank">📅 12:13 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22417">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djM8NsMnK4eKisCZKTOgSf9J-INEKfyRLkYdMzC4EtIunnHOifZmRjVbKLOBhuj8p6_RC3ZflDvnDFHxvbOtMZtldyp14w3___FxWgRsv72lGhcghTCvBoEMhOZGKERBJ-UgGdzhoUjCzoWdeLXdnTZYw_q3dlTdV7GgwhHxoUKNV6qx1xEg6YSVkrbzgF63mHKhZVHnVPgs9yV8PJV3Qi-EQ1UzRTP32Npy2SBHhaXef3GkaXNyEBY180zgFdeQVB2Bin2583GZrKGsuQijOuxqoWtx6eOeUW4IO4b8b4_ymc_NeL6DXwxpEXhh5vHcGzPszdJjbcBA8_jLkSExKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#نقل‌وانتقالات
|کوناته مدافع‌ فرانسوی لیورپول به‌سران این‌باشگاه اعلام کرده که پس از جام‌جهانی از جمع شاگردان اسلوت جدا میشه. از رئال‌ مادرید به عنوان مقصد احتمالی این بازیکن یاد می‌شود.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/persiana_Soccer/22417" target="_blank">📅 11:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22416">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IhVw6WSP_THRF8iiwjGFV_XTo2-T2RZB2tt-Nzytp9o_I8qO8QibLl_10js4SF99K6UyNXVx53midcYO-8EP62OIz8x3qFalxUf9dfBK65xoGPFG2gUW6Fr7Tkp-FawotW_P8HdDxR7FEbQzgTpXmygmSxmy1B5O4JSnM0qQGjwO3qkx2F4MAq9PwWi2p5dd6B9Usm8yn6RgP2R3MIcv2eImQhmDxwR6nv_qBV4kS5ify1Ukcmd2EizSKuDYIctO0V_X9IpUk8qWsW9-RVcYdCCvGLhVxPkU2BKcIgn3qwWpE_gZR2G7ueCzbmVqJwPLyPKgm6JzKG6JFyWrJ6SFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/22416" target="_blank">📅 11:33 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22415">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XEAhzTdSCwalIpWcUUQ5xrPv0HcbVoemG9sWDZDBNXN27IaITR-5kFGioCt2QntTFqCxnudE6lxbymj0bOEbtznK7sGLJzRwO-QVwLG7Y8X-ghYBhtH9IcxNmArQKBvZwt2Oz2aOO3VohD5Ase0SBMIebzGqqwsFYJnop0vTT0KFZMpuwp5kXPUYS16CvGj5VdJjIB3tkO_0zNbJvUkWtmmTMzANjIw4vRO2k84mqoxgIJpeB6_6kvk8arjl_LPcUS6U5XcadmbJlmFXFwqFVjIPC5T62SGewiphoXuCrT246X-zdx9h3jqqH9_85hEsQiaJ-yjIx6XaE5ZoVhHSNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه، انزوفرناندز، ویتیتیا و ارلینگ هالند چهار هدف جذاب انریکه ریکلمه درصورت انتخاب بعنوان رئیس‌باشگاه رئال مادرید؛ انتخابات ریاست باشگاه رئال‌مادرید روزیکشنبه 17 خردادماه در تالار بسکتبال رئال‌ مادرید برگزار خواهد شد... فلورنتینو پرز و انریکه ریکلمه…</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/persiana_Soccer/22415" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22414">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lgCDfsZT0Y3dc8T6iaoGeMEWg3QudUuEm4j3affHhSeTOE09OQ75vf1mQGhCIHBpE_x4j4QFpZCDrfBc-yb-u6KWwJhHPxX6vhrKZSFNeH0yDHYHOdaA-BoJgFQE-NpN80H70Uj3XjtQU1hVpQHa_1Vk_z6TdN6OjpTJef27d1SR5I1M1NCox3ebdTkg7WPd1DN5-JR72uLvG-VC-17tUsXcqU28tBzJlBq_955bi54LHwkwlNcJDC01JtFZiw23YenUJwsBw5iU4p62aqWk_5yNBLlZk5skDIAQyqoR6Aa_mA6UmBiuNJn3eXkjYeYw4bMeDYK-9vtVXVki6K6DSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جذاب عملکرد ژاوی هرناندز و زین الدین زیدان دو اسطوره تاریخ دوتیم بارسا و رئال مادرید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/persiana_Soccer/22414" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22413">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mI7rrWcaQCPrbpOcv8uxyvD35a0wgge0srchUkaEBNlzDKJsIgOnjMxMbVGQJkXgMr7uL7V5zj_PtrsbJDE7oUV1eqSKKsmdd6pY99DxkJMdqz6fBs11RtbpNnld9FRdtVZab0J7SRQ1xFF3TBLMwN2G7QuHuzkGXSGf28cq6O47oHcR7ReKZU9lsmsw9noQbXLrqE9He4KGo9o_QhcKlwv-VH70Lrualm3mqnIcnZc-UQGKzwaB2Jl1t2CIY_dCbZiCxfMRm3WSuiQWt9Os6Krfm02ljPK1vb9blzCjf_u9lTVunKHr3AEcGIh2kfozfqf2jAa-NRMC3zHkhDPuvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭕️
بدون واریز شرط ببند و بازی کن چون وینرو با ثبت نام و بدون نیاز به واریز
۵۰۰ هزارتومان بهت میده
🎉
500 هزارتومن رایگان فقط با ثبت نام بدون هیچگونه واریزی!
💳
پرداخت مستقیم و سریع بدون واسطه، بدون دردسر، واریز و برداشت در سریع‌ترین زمان ممکن
⌛
پشتیبانی 24 ساعته
🌐
Winro.io
🌐
Winro.io
کانال بونوس های رایگان
r8
📱
@winro_io</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/22413" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22412">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfkJXdVRy9CW_JMITsWKbCTqtY4gtIrSamvbO99_QoNZhbg5Sr2yoWrDk0yqYWwACujQVPfg_vSjIAXqCmqcpShXp2u-hBimRKOmMZxxZezCE_Q-wjQxtvMrU2mW0WBxM3SiHPbOj_C3Fms95sPpCRqxxgoLTcyXrqUbDBEfjt5DzftYEVIhZtA7pPqcXtRAB85J-zoyfUrYb9dCSPwVr8skxh5aXutb5RIJyOGvoXojU_OY5YCZtr-Nib7khfcBgxeBicMiYyWUDMYlfOiWsPAdUpfVkULcouxVTFyA7MDKQlx_3T8gUOJeP0mxXk0v-NU0s0hzJ5CO_gjYQI1usA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
برخی رسانه‌‌های عربستانی؛
خبر از مذاکرات مثبت الاتحادی‌ها بانماینده یورگن‌کلوپ برای پذیرفتن هدایت طلایی پوشان جده در فصل‌آینده میدهند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/22412" target="_blank">📅 11:21 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22410">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ضد حمله‌ و بیلد‌آپ های تیم رئال‌مادرید؛ طوری که زین‌الدین زیدان با رئال بر اروپا حکمرانی کرد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/persiana_Soccer/22410" target="_blank">📅 10:52 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22409">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c001aed77e.mp4?token=JP6N-XimTclLmfbybgC9B83PjLZsP1rezNYz_Zx_qx0wCF61PLNkdV0GV8-1UX4OnnmwCrLAkGBGju6T1XDw2OS8qjvTE91m8dcsIETAPUo8QNL39G_86l6xRhlu0metHXhC65py6DJBddituQhPFOkLgoIknPFMTrzTLOrV-4qSgO8N5eQCGVYwkbjx_yZa2wBbmewj4CQ3vWeTvGhZFze3IiNgmbVZzPsRTLE8RNlVT0BBROcbjqJtV3dP1WGzEMeshRG5k10ZZwNGamg2XZ54gieLAIswwXUVUtJ2bThcy3xPcjV_Mjkd1XrQsLg0Gpe2s6YKFlMbFJU_0_YX8AIS2bYKnfldkLbWAKLYGJyUTFh1i6gUyy4nhQK39rgThu8nP88gn1qJ1tUsDk8xQx7q9z2Am03A6eDVE9V5XeCR4BsZ7wKU-0MTR7GJ6GA1Iqa4SKalWWxReOSZNLebZUcoeSQ6v2N77T_bFQZayMgeGFk2SkLqGLO-iFKK7K1Z--ZpTuedAuc2U3w7uEW8KTYMm-DtFpQPExT-rdJCX-R1mDcNdGSUFcwYrE879biflB6BLEkjdpiEPJ6aDtTac5t6Ml7C2orcqi0479AoWUz2v3e5JdEj5Vr1tsQw-XwgBpO9BPs7vHYX0PeZ3_epAFQisvq6XxJ7VeEj3Sl0HC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وویچک شزنی دروازه‌بان 36 ساله و لهستانی تیم بارسلونا، بعد از ۲ پاکت سیگار و مقداری آب...
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/persiana_Soccer/22409" target="_blank">📅 10:38 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22408">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3294ce3a0b.mp4?token=XFp6X7peeTiSe1i7gSOwDbJJ5pVEB0Uwl41M5XohaW47pYFcmwy1jaav2zsvz9acWFTgkoBvc-IWrBMWLxXP0-vZje4yRs7GBm2gEdsyOlCuaIfSXxGZmx7HwOp8VtuatToNjIf2Mk6Ap5fwpXc6QH6Qp9BsvhrP2TzoFhy9ySv9B5Sw7EcIL01oN8T53mWU_lqI4nW4JEDJY0NzGzwnJJo5PW1F_7sz7bqXj2cf7pxvnC78p4oFysnLNaHc4FgtYz_QrESHDpLqci5j4akfklo0JiXGAZo9XNq9rL7uaHPHqkH0Y_M-SDYh6WHcICrN563jTS-9QKHsKhbFeSBpm1eJ62zQngb1StfZ-51Xl8sIxJxjYdqDwmLw2IDnQB-3HZNZM6FTu70_ElJ_lABwN6hHazePuCiMdsUp5IrSKw_FSNYLNXrCjvDB332WQ9_UAlSsq6ZcOarRQ7W_-ljdhc0lwhc8HFE307aYliS2v_lo4CJIgv2Q0Cp01xLpaItoUGDg8IAYftM0mQ6cGtVXuLlH2RIbLcx9whCzjgftP0dZU0Z2-5pWjw965KWFdKAXCxFbhS-hK5BOyTtFfDnsmmTDx6JXadubJuJ_B2Mc5Q11pZulANN2gNAuEeqApp-MWUjAK2zVUIHQ_4E91q5SV_jWqAxcG-4PZ-MMcWBscZk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
یکی از مهم ترین دلایل‌موفقیت انریکه و PSG
: اون برای بازیکن‌هاش‌بجای یک پاداش بزرگ در پایان بازی، پاداش‌روبه‌بخش‌های کوچک تقسیم کرده: مثلا هر پرس = هر موفقیت = یک پاداش عصبی کوچک (دوپامین). نتیجه: انگیزه پایدار در طول بازی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/22408" target="_blank">📅 09:50 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22407">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc6b58323b.mp4?token=aqLImRWNSvZnqAcWIp3qrb_Fv4JNYTaubxoAUvE_y_wbN-afhYSuXvnuVPTmmHZsZiX5AHsF42i36m15_yMRk3OGULtqMEzU4vE8G_xGf8be-Khnt8lhM6Pb_KB1qhXf0TU6f5fPJURjrbtIGNHpV28UR0zVfcsLI2v7AJAa4Jtduqf5zU-28NNbEXoLNk9FnunIjRN99tCTkz79fYzBXIFK4Rsu9RIFV40xZM_p032wPf9xogjybiAaz2QHUFbShJoP7XctTJcng8w5JcVv-yF_f_fnS4Cr4A8tdRpzqQuQmDPhRng2JaQv04CSdHqRQhVQXwVvUfLbSOg7xsAz1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
وضعیت شنبه:
آرسنال با یک گل مقابل پاری‌ سن ژرمن پیش میفته؛ داوید رایا گلر ارسنال  دقیقه 34:
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/persiana_Soccer/22407" target="_blank">📅 09:35 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22406">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pyP72RC_c90Tqm93TJ0pTuMpbpt0gZcI8iACfQJa7UJS8LEoTFES_Qh9eDzly_LYo4oLWTZM0xyVULy5JmXnp7DyPG7Jg44RfpurcQjUkL-2qVfHv7nbpEAOZ3-Ign3xKVGNGjqR0qQa9v28We3m4g1-37lVtw0sHIPNiGZZ4WaY1jong5xRujhgFHx4lRwH-aIy6MsMPrH2zSoD0j_uc_LqzZuBVk2PXozONBivvFzKFY86EnFx5bt7I9Svz5q6eJl_bCooCNncgyY5SymYZQatkvOzFznonaLIkN8kVO8HsCnmEewD0GuXqfCpW-ucKuCaSLpnu1KixEPX41Appg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ خولیان آلوارز به‌مدیران اتلتیکو اعلام کرده با بارسا به توافق رسیده و دیگر انگیزه‌ای برای ماندن در این تیم نداره. اتلتیکو حدود 150 میلیون یورو برای فروش این بازیکن از بارسا میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22406" target="_blank">📅 09:15 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22405">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DRPaxrshZG3NsQqqBi6oX_8-Con_8bTkV5Tpo_BawT5opN9xnEEkADPNhtiWF-bO0U_hWApYStgVebi5SMTOsoMDCWTFcw2aP6fUYFSo2Cw1bn-OJ85xuyADgV8tXV4-TGWBy2ihHPFwfEBE9UX1lQmtkFpD-XhImlCODUa3XkdHWF0doU6wdIh-NLRFgXFwrUhTY0w2X2Ck2Yso2DBNyYVd4STUhskdJsDdStOtGPPiYNlBQyiEb5f0CL-6shPdSXQO2IHU6rjKnn-ajSLxwlHTiUn1Kjthf2gn--KRYpp6DcreGvg-1Jngk5eEd28I20DbrxjLBuUqUkaVqb8kqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویدئو آموزشی‌نحوه‌واردکردن‌فرکانس جدید بصورت دستی در رسیورماهواریاهست؛ شبکه‌های یاهست که بالا معرفی کردیم همشون تاپ ترین هستن که بازیارو باگزارش‌فارسی، کیفیت فوق العاده، بدون سانسور و تبلیغات‌آزاد دهنده و جلوترازصداوسیماپخش میکنند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/persiana_Soccer/22405" target="_blank">📅 09:04 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22404">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DegpXKVFUJR0RGLocKI0KLL9i32iTERupG6lm2wt933tJ2uRY21-gzkx57SRTfsi9BO58IdqRG--ACUKsf8P0fBeiY9Q-0VGR1jtBpWNYR2qArcOceuU-UUi5ktdjkLTxxCp5cUsvMW7GFWKhk_Y8gJ1aOEhqHQ1JC2RD7zRokx4XtX1ro7wm_cYZGOQZJ-u0DDY6yg2jvJrDADwZPjn0AlV9eWJC5jUZ0d4L5j6X7PzU7GufFGNZcsntpGLjAOr_P0gWn5J1n5XULAQrKuFKBKrO15yjpalQ3qLq-jLzq4EkwkQcVpJ7ZhIbox5sdS5XFhm_2UTAk312O2R1RAfqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ الهیار صیادمنش مهاجم 24 ساله سابق استقلال و فعلی اوئسترلو بلژیک رسما از این باشگاه جدا شد و در حال حاضر بازیکن آزاد بشمار می‌آید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/persiana_Soccer/22404" target="_blank">📅 03:51 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22403">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ2ESnQvbbLZDbezUGSrUHMYAp5zT6I2RtILOIWwQ0FrmB7T-13zLHHMkyMQ5RG_Ub21Z-_p8Ocy_X7uMoAL08TOUQj9xyzDZR7Y5aIs_9TrbPwRggv4CiEa0TVed3246E6_bmyark3sIFctEYkMn1SNevBNlwijOmvWFh0NEghPDE7eYWMH5ZDo45P8DshQOMAzj6yClmaUmYlQgNJisJ-XmHfXN0BxskEba8ahNxiRRLCVQxmGKvJRJJAtKEr4FkFGbce66Ezq0UmsCtaUcmlCNzIGK8h9j3fDHroMOY9QaW4iI04hzTxAgzPt-xSQXfvocGyzEeDX30hzW0CHzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
لیست بازیکنان تیم ملی آرژانتین برای رقابت های جام جهانی 2026 با حضور لیونل مسی 39 ساله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/22403" target="_blank">📅 03:08 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22402">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKFlxHNOKvVwVN5P7YpSoxzPcyjBpe3EtTT-OlG8kWAuW9z-2QV1Y8DrK9V2HJSO145sK58WATa3ZsZiHRZKxtuotMtv1eBBzNdLDuDfSujYTWgGWBYoK_BBxrebmz-uQf_RHubhF5xnS43pjwRxjYQnFqaPzNhPZ-XuUTuni0Ybtw9jiuPkZlOGVM67RDdiLwSE_kBEWqHYaO3BS_dUalDLdSjvX5_yywB3XyiupFT8yTe6D9KTwBXrlAqn3PS8V1TWtFLLnNFmeldlV94knkeGgXDh28soNqnKdsalBCWmmL4ZcnqlmsmjOXdDReVNH_5_7viqQ7Trz2H6YnfJzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه بازی‌های‌ امروز؛
دیدار تدارکاتی تیم قلعه‌نویی مقابل گامبیا تیم رده 116 رنکینگ فیفا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/22402" target="_blank">📅 01:30 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22401">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlQg3qP8cr8DJ6npHK9KVzLkoDHnygABJ6CHjpe7EeYVOsCw61Lugf0gK_mTdDsKd_k3iKFVNKUg0g36vEmTqnMUBMeJmNd84nmsWe2tk-DMRMfgKrIHrzLERc9YRLhUg05lgb52slng4df4TLYsf26LNbuE3dIqiLxr-S91xAVb9UNjie1TuVlEaUYGGM-fjdLmQS9SAtvNtKIHiWj-t1p_Y6vaQGQol3tCMK80zla4QbD7__sebDpQO6leiA6EMSB8pxpi7wr2ASc0FqIjwT22QI2Aw1W6gqmlo-swEMSHu3PI4D9xj2jTov6foOWPo6m-9F-aVtlZZikRvmmdrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
برتری مصری‌ها مقابل روسیه و شکست یاران لوپتگی در جدال با ایرلند
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22401" target="_blank">📅 01:28 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22400">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tmmkXSpVTQNtIU29tC-p6klsnuVFxKvuNrrCreeFnGN1ipfeurS14pE7zhl1iDbUzb947ZjRWmU37MiOLhwHK4UCWO3Mxnk_fpk1LIHYS8gQdW9AUKA4VIWWCn0gWUNmdRcJB4rBq1_7yoDbYpx3fmbX3jKWOQ4D8223f_XgLdSV4sVeXZtbvP1QR8fBhkhi0XC8jiAnMNEWZtR_uFUqZCh1Cu2ZH5gLPfl64RLqKjDdHnXlnvRu0TatHLRdEhgPBhINgAqJTVwZ4FidykspQ4Fc4j3mqnsKElrJNAF5XOY-c6AZiv3m2r3WKP5aS4y27Pvn7nIFauICxI88eR8x2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22400" target="_blank">📅 00:02 · 08 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22399">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STNpoQX6BH4KqSoUqQEYUJB-34vd3anQK9d5aCmrd2bQRS4dtJ4maH06htCJYk9_dJ7phaeBLjtyU3mZVxS-fQu9cIARDGVRSnxOMvBFNinW0-WZwfulRw9PKFoNtEx_6jMIuQj5SWV2E1EKPnLNryyTFouSNHEEx_UiIXkP7ApQu77v25xiq6Yv6uFsR5Fg8FNEptewAQ54fttB9fqsN-A-bJqF4C9FsyAQi-qY3HH8N1b-F1dvVVyEUpD3eU6TkPtoD6yYHqxbPcBJumQAnSfPZbrkDT6avkeDCIt26lCB8bIVg3JrE9lxhBkJQZRH6HmPWdn9hneXSVo5D5msGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برای دومین فصل متوالی، کیلین امباپه فرانسوی بعنوان بهترین بازیکن فصل رئال مادرید معرفی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22399" target="_blank">📅 23:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22398">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gkOT3F4u0D1VeaOrqmIiBfNVZBSroYEj6Rkz9tto0Ueu8As4QUXFs7CUMRZBXzkiB8fgEffeRXWllVoEM7SSS9uMoEu7CLutBD13u2zSv8zOKrCu_OkdUTUd7CxNBf4smWMm7h9cVbvjjof-uryAyrmpevyA52CHQtxzykJxHC1bg0P1ngN44mSZbE4fseLCG79camv18dtsTSO9YVoh4ejlep74jYRC6R1vI5ifQ95kT5_Q2HfBKS7p6WIIkn-Ci5AwCP9uUaBOabP9lqX8ZByzV-EHEZF7ohB3Tunmh74-HS9IGUHT1T5bCHPYF2ICICrqTADr9gPQD6kfSdExxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی #فوری #اختصاصی_پرشیانا   دو باشگاه تراکتور تبریز و استقلال تهران از طریق ایجنت مونیر الحدادی به دنبال جذب حکیم زیاش هافبک تهاجمی و بازیساز سابق تیم چلسی هستند. دستمزد فعلی زیاش 750 هزار دلار در سال است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22398" target="_blank">📅 22:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22397">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=jYoI5XUXaS-u6hBLQtBEa7uGl0ytpObonWfxbo9Rus3WlIAnGT8wdqoMi5bcExSiKI_M-ZWHRrv5ZsSlVM0yjWfw-b6gIaidIhRht__-QaxZCTsSNqgPhr_MOuwAq-i4NPWbuyX8dUlCAm7Dr0mWm8MMH91t4EmYx2lp1t0qM_fgBfp5JwbSFiCOH6K-x8VmQB_rOPBlVInVeUiAVnt2GZ7PnbHKrwiMDZPWu-zLEerxLWu4FPE3UXsKppRVkF-22Suh_8yQyFqkG-nIa58AqGdlMIa4JYEU43p6bYd6BCaK9h2c-l5el7tR0_XS74KnkuV2zacniT1aTyt2CymxYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4da3d833bf.mp4?token=jYoI5XUXaS-u6hBLQtBEa7uGl0ytpObonWfxbo9Rus3WlIAnGT8wdqoMi5bcExSiKI_M-ZWHRrv5ZsSlVM0yjWfw-b6gIaidIhRht__-QaxZCTsSNqgPhr_MOuwAq-i4NPWbuyX8dUlCAm7Dr0mWm8MMH91t4EmYx2lp1t0qM_fgBfp5JwbSFiCOH6K-x8VmQB_rOPBlVInVeUiAVnt2GZ7PnbHKrwiMDZPWu-zLEerxLWu4FPE3UXsKppRVkF-22Suh_8yQyFqkG-nIa58AqGdlMIa4JYEU43p6bYd6BCaK9h2c-l5el7tR0_XS74KnkuV2zacniT1aTyt2CymxYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نت بلاکس: این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/22397" target="_blank">📅 21:33 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22396">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7ISqg8f1RetRfXdDROvOgyMW1sjnB8FGjrPQ8jr28RRAZ1dJ7hSTcVdehK7wxBevZwEJsJFSNl5r_KhldkxkZmIyEmc69gFPqwbkiYfo20UIWtJIQSmoDoFo5mhIaVl-vFIdKBnVkiNfYtgO2KiEbQ-rI6as3A1rx9Tvamm8_U_4wrpaXuJ9y7A3FogomCTii_Jqq0eEQ0MBGtyHN3iiAeeKpusiP4QPOgKLKSSteFUw2HNhpm9XMK1JVbLQ9wng5lgTzXPNuhO3vZGihgcPU13_xA4QY1j57nmXT2Y-fQzIp2_2yUD0s_NcZ53bxNqHp3B9Cik9zF6oaqeiTKEbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ماسیمیلیانو آلگری سرمربی فصل گذشته تیم آث میلان با عقد قراردادی 2 ساله سرمربی ناپولی شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/22396" target="_blank">📅 19:53 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22395">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7629a35090.mp4?token=pyBLVSo7VyCAj1T2tj25NXWToLcTK4Qbq_c8WqUnTQtsLrizxBPyf9TxJ_dcKfJtJDEL-AElFx2dE7Ajj5Lht0y9PHPFq7kGspyQaAbPTJw_1xpg_fq_v1uRiYf2RWu2ACbO_9PgXOtU4YsexE3hI5UskIJSkWgMxz-3zPjy5qQ2u6vKkg-b8wZfWgAfNQuubYrg2eZLpsxKMRSt9snkGAbo5GEfn5rxKeblkw0xn30rJMB3JjRNLuHDU9b7gvbd1vyd0vJW59GgH5GkCD-ov0ram1ifn-GHoNnxIqUxXQw0LYJgoqokjXwVzLFkia0QlaNn1aegDa6PBbvJhfnBBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7629a35090.mp4?token=pyBLVSo7VyCAj1T2tj25NXWToLcTK4Qbq_c8WqUnTQtsLrizxBPyf9TxJ_dcKfJtJDEL-AElFx2dE7Ajj5Lht0y9PHPFq7kGspyQaAbPTJw_1xpg_fq_v1uRiYf2RWu2ACbO_9PgXOtU4YsexE3hI5UskIJSkWgMxz-3zPjy5qQ2u6vKkg-b8wZfWgAfNQuubYrg2eZLpsxKMRSt9snkGAbo5GEfn5rxKeblkw0xn30rJMB3JjRNLuHDU9b7gvbd1vyd0vJW59GgH5GkCD-ov0ram1ifn-GHoNnxIqUxXQw0LYJgoqokjXwVzLFkia0QlaNn1aegDa6PBbvJhfnBBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22395" target="_blank">📅 18:46 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22394">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWI63ELZfbHEiCc4d4DQTaSi5bPIjDpyKv3zGJGRb3UkN1B5EX0wEJ6JGZ5cqUwC97U5RkQawFG8z9VN6X4PdmeLMcgWdwS7cFCxbsDwttm4lBlwIDPKbxH3uL7eb4S56SHnf0fXAN5yeB3Pvv8M_tW8jZOStXq_0c-1EHg7b-O2HE6fHfdNbPEx1Tdi-lYRg_xNbNT5HV4rzW7WhP04b1Uva9IAdGUuUkIdOOMjdXKWOOsWZ81SzbeIUyZ4PaODxScRxyaqA5lsbSg_ZkO6s7_UyG5Qo9OaFATJSMw9lM-kjVwdSzZbzr4e27zoUnynGVIv7NABkoblukr4dsqasQI-Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e8d402777.mp4?token=piZlHNXhqrFf1G0MJeVLYj-I6zA6G3C6llBQiLOJHF14eGSZxLFq_TJfcZvm-qE2-dZ9xkYVzINhVeG-CrUqLx3xn1q8fg4vskY6hphKTt0XK9C1Ek7mT3zB_XR10UqA5EStYD1tQLg6yfjuU7TqbXvuq2kFqUoDsrA1tE1cSVzQJhi00iR2tk8kqickhi__Iim1cVVeaMb4k98VtBVLuU2TA2WjX3pjAkthYBnWWYJbJHH25lO6mqpBAsALqa0m1r2Q3yj2nOCMrhh7nAgg8zznrDIzRrgRLgtLBm0D9uWLU5qKMwT_JxIwRh-4StgI4hIPSNPhRbhaPxfPMhPWI63ELZfbHEiCc4d4DQTaSi5bPIjDpyKv3zGJGRb3UkN1B5EX0wEJ6JGZ5cqUwC97U5RkQawFG8z9VN6X4PdmeLMcgWdwS7cFCxbsDwttm4lBlwIDPKbxH3uL7eb4S56SHnf0fXAN5yeB3Pvv8M_tW8jZOStXq_0c-1EHg7b-O2HE6fHfdNbPEx1Tdi-lYRg_xNbNT5HV4rzW7WhP04b1Uva9IAdGUuUkIdOOMjdXKWOOsWZ81SzbeIUyZ4PaODxScRxyaqA5lsbSg_ZkO6s7_UyG5Qo9OaFATJSMw9lM-kjVwdSzZbzr4e27zoUnynGVIv7NABkoblukr4dsqasQI-Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌ببینید از تکنیک‌ناب نیمار جونیور؛ فقط ببینید چه بلایی سر بازیکنان حریف میاره‌. خدایی حیف شد همچین بازیکنی توپ طلا نگرفت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22394" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22393">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH1j4Ke4vRT15LOWI9hTy9R-HYhHMqV-D6Awc5i7ecdE8rjPDJhuzpOALsaMcQ-OVz3d0lWRgm7OaGVkPT5XgFd-XLpl0gJE3kvGhka9-Xv-0cuWOC2MlmhxMaug3RbJoL0J00FXEFkl9VjiiU7LnzwRRSpyoENxkJgp-4lyAAflfN-P8s40mFdFU0mVj5URvdc7yLr_Ax9jgAv0Jf6j_5ZA8gTv49dek4yERwlYK9dipBPqO12G2LimqsviB0zkIio8GXBxTL4duL8K0801PRuSycexGHUphAiAWnAk4OVk0s5-h_-fD01szynPwP3ZbbDJTO3ll-hvxYwGgPyoeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22393" target="_blank">📅 18:36 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22391">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD0QxuQ7yXKIaAn6nyQ0SfKmjaCwyfuHNEqi8oGdSD5Ksv5Z2lfQF3TP1TggNzQJ8YRunwCso2dAsu6jXM0Y3fq1J6xJKUDQ5iqth4aBWIJpOZGyL4oUeeJ1aq4DDPZ6Jtu9ZMrosbP8_LPjaLW_O1RDkXhMhgAPNcT4vbqhb6jzpGRN_C9553o3K6fI2iqG-AKHMcCnMoYuM1QnK6Xlr49Z5QrKXOwyYGoFVCF0cYlAHDqq-f6qdSXGqFBKLENobql8NZ5QPSUoPypnHWTsobFTB_RvC7F7pA5AcG2KDe0f90rYlX7SVSTYnqGpAEZLaSY2bGWSL0iCqwW-5EaCyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
#تکمیلی؛رسانه‌های‌فرانسوی: کیلیان امباپه، مایکل اولیسه رومتقاعدکرده تابافشار به سران بایرن مونیخ موافقت‌خود را باانتقال‌این ستاره 23 به رئال مادرید در پنجره نقل و انتقالات تابستاتی اعلام کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22391" target="_blank">📅 18:15 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22390">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GVM_yA5AXOiauwtglTmUDw-l1Wv2QytRe0AKXG2sx9D3UVvKqy0aUhharxHk1HjT9CkYHuyvEwHdJXINWb7lHtVz3hNI92GZ8dZDGiTAOhFsBGXMviK_59ZqIx3tTcA_F9EWTcBIFQX0mytdKcA2JqVLIGkFkQyPn_h1klCk54TFpd_3LWVzThwlTIeRhVsTtMqaIhRS9IP_zhrkbz2ZkJ7fGLHAep9Bi6BOiuHweoTAig_akEVR7PSgB7wCt0Bn1pPU1cxAy85wF76-R3y--RGMLRAZxUmM6_BKw3_c6YPTWww1zYXVtZkTSw6wceCktOe8szbap3abwl_gWtY43g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نت بلاکس:
این‌دیگه چه کشوریه یا ابلفضل. اینترنت ایران برگشته ولی با اختلال و فیلترینگ شدید! هنوز تموم مردم ایران به اینترنت دسترسی پیدا نکرده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22390" target="_blank">📅 18:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22389">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3q_oC8xYTAH9TGYWwZoGxJ8CH-OPfEsPZq06joF5CxJICFbAFe5gblg2M4JUXz33RTKQ2hdctDZ84nfSBJPXNsNSEZafORIAeCnt6pC8iRZ-OgQo5K1j5n_UsJzmzV_Dj0GCfPCTg4060QkZaAXy52djKX_LTzeLkfVBk5S-3cFMDAzGz1NII3bI30QJG6Jm2EnzcwAeX-Q26GKEafl8QXvtnmvmCVu_LaK1B7dlXZNAgjq4UmqUEvEmFhByxhU4KjICsvSsWxENG2H9-Zb12ytgl9W3zz_OZHnBOwAuh2JeFVq41qP0BkhLvPQm1cqiHwCB9eI2W3md012SJEsGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فابریزیو رومانو: باشگاه‌بارسابعداز جذب آنتونی گوردون و خولیان الوارز باز هم خرید خواهد داشت. هانسی فلیک امروزشخصا با آلوارز تماس گرفته و به او اعلام کرده برای فصل بعد روش حساب کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22389" target="_blank">📅 17:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22388">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/czkh0AcZP6tfdGjW-w7R30bZOY1pbFq21pSxZb9JDeUZB9oEASeeHpiOsEfXApGAZ8UHAyIgM5-TvqxTTm2ZvkpMZnlHd7nOZW34RAgi4QHiDRgrivF7Nw-lVvYffK45CSayQ97iSdQvqCHp2ZHDNRc1eSmHHqTgIBEscvQ5ANUSaQBI8B8JvuOUmDRWiF4BZucyDFhFfrLsaqtuGsS5FB2KjW2deDjaOx7bzmnOaPt_m2_eblJZOZZ7hEEyeNu75hTvcR1XS-MB_tSI7a3wYAPm6zC0dyOcKlUzvWy8YVZS_46guG2qG50WlGBPrwdH40E5cVABlNjcMpBl1T9oZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بعدازجذب آنتونی گوردون؛ هدف بعدی سران تیم بارسلونا به خدمت گرفتن خولیان آلوارز آرژانتینیه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22388" target="_blank">📅 17:48 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22387">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kbsutvsyRaWeFbjaGZv8EKX8pEzWIE_z4sGowFeeBf5M_HIirHyN_8IKg3jEb7P9q9_duxLwwrs9LJpDf-bhSfAE5v32mJrc1YxjyG504ek956K0gLLFbKfDO_1dYDSyOJh7bbdWUiNT2dnR6fEHEGETAJ1f-fh4I1wzB_9S9Nxinn3nk3mNYnOEWkZHmMM4_MbXUyZ0_Tger1Mg6uP4bKDiBdA4kcWZLPirWNkA3hsJMxkKnupaalF81vcMNJS2NRSCSwDQBwBFdk-ftRRwInIHS11vYKN3B5xyT6ClVJsarxlqJ0JCBBnnEo33KkbTiK3Ad9wO-6s9Ds9ovGDM2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بااعلام‌رودریگو لاسمار، پزشک تیم ملی برزیل، نیمار جونیور از مصدومیت درجه۲ساق پا رنج می‌برد و ۲ الی ۳ هفته از میادین دورخواهد بود. به این ترتیب، نیمار دو دیداردوستانه‌مقابل پاناما و مصر و احتمالا اولین دیدار سلسائو بامراکش را ازدست خواهد داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22387" target="_blank">📅 17:13 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22386">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=YmV2Pp8JjJ29lJWAMo6hcchhpO4tJwWwVfLRdpfAEnKppQdL8GgP25kEziRd1dKrYlfQK53Bsfh5L8rwNcABOfG2ZgXCfNXnKORjGL1AX8Q2iasK9Y4fTI_bggG5YIXIj_M67d_NBY3ura66bQcZJ0nsus2N55TrAbNZTC79k_lUYFDNEZkw3odspDjM8mYMMwMliSjSs3eM-tfLF53VILY51eTqI2Sf4ACq_l26VeqLXtl1kU1WJqTv1gbQSzVFNdWJafdegivrC-4AAT7-2Mreef-izCM_lEZodIcPmfyyD1inVr8vZvX_mLK814PtVbcO1m83AHwl6FztTPwlNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66baeb4dd4.mp4?token=YmV2Pp8JjJ29lJWAMo6hcchhpO4tJwWwVfLRdpfAEnKppQdL8GgP25kEziRd1dKrYlfQK53Bsfh5L8rwNcABOfG2ZgXCfNXnKORjGL1AX8Q2iasK9Y4fTI_bggG5YIXIj_M67d_NBY3ura66bQcZJ0nsus2N55TrAbNZTC79k_lUYFDNEZkw3odspDjM8mYMMwMliSjSs3eM-tfLF53VILY51eTqI2Sf4ACq_l26VeqLXtl1kU1WJqTv1gbQSzVFNdWJafdegivrC-4AAT7-2Mreef-izCM_lEZodIcPmfyyD1inVr8vZvX_mLK814PtVbcO1m83AHwl6FztTPwlNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
اگه‌چشتون‌خیلی‌ضعیفه‌هیچوقت عینک رو از رو چشاتون برندارید که نتیجش میشه همچین چیزی.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22386" target="_blank">📅 16:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22385">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=BLxOjELy_y3qn0DeIJGDZOyAJf7Nvos5sZy2oZ7Ed7FilnSAfL7YbADQ98j6qHjxM2J-nN8AAr5lr0h4v1g9oEb3PSL2HML7zNbIGcBD5OhuYirmmFMOsq5fL4UHuoA1y9JBi20PdZHnKGgtEEBoKXqO64eGjmcDLBTujQPYCJwkXkYcCfxpyJNxg4yAUZj1LoeeTsiFukyj3jm_9NJWrFquy7QDdMXZcbhSbeUJP3ZEsOPREZwU8WkDqTEgwCLptFPjtuv0BrJk4LcwnMkG5dwqiqWBzr2tpKT_2VbkqC9BtKnA9pn-netbH36z24jCr2ypdQg30c1NMXaCSQj_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a0eb9ae9a4.mp4?token=BLxOjELy_y3qn0DeIJGDZOyAJf7Nvos5sZy2oZ7Ed7FilnSAfL7YbADQ98j6qHjxM2J-nN8AAr5lr0h4v1g9oEb3PSL2HML7zNbIGcBD5OhuYirmmFMOsq5fL4UHuoA1y9JBi20PdZHnKGgtEEBoKXqO64eGjmcDLBTujQPYCJwkXkYcCfxpyJNxg4yAUZj1LoeeTsiFukyj3jm_9NJWrFquy7QDdMXZcbhSbeUJP3ZEsOPREZwU8WkDqTEgwCLptFPjtuv0BrJk4LcwnMkG5dwqiqWBzr2tpKT_2VbkqC9BtKnA9pn-netbH36z24jCr2ypdQg30c1NMXaCSQj_pjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
هایلایتی‌از عملکرداستثنایی آنتونی گوردون فوق ستاره جدید بارسلونا در فصل گذشته رقابت ها.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22385" target="_blank">📅 16:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22384">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQYT30T-10xkhxTgNn_bg6U2ztUkNOA7ehWe0BP5CtnWppZS0Hkiv2EU6cFTJQ2GpyX-bfflSGnTpbVAO--JxCglhC3F_zWGhAst1xGOnvv1BM0Ldd7Cg2P_nG1syhKx3qRrlyocnPNeIK60fxvFGHrTq4VEHE5uvinnc6-Shl8qVLLKPbH9CpkoIHo6jI9T-_KulF0ueHFMwzLZ1hyDzD7WhuvKOC_cvCmGG8Wr26XO0kal2URpfKmCqVoQqp7gNEgriTby0yWV40VZLWuXmCbB1oNkOUm7KjVhpwP1HEnMxIJp5GWCcQDck84u5UuZM5BTFFK98N9JXYYfuLJR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست کامل شبکه‌های رایگان پخش مسابقات جذاب جام جهانی؛ بنطرم از صداوسیما نبینید. اگه ماهواره دارید از یاهست این فرکانس هارو سرچ بزنید لذتش روببرید اگرم ندارید روز بازیا خودمون لینک پخش زنده میزاریم ولی واقعا از صداوسیما نگاه نکنید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22384" target="_blank">📅 16:21 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22383">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beQgdmoQdxa1qJ5N1rmI0OcSLnPSyb8aV_UTjSUTZHWPqsOu9MdyEcUtTUNlcgIUVR_g-hnevi07_We8a6EGFR9fUM2e0BweozdifWigmS2JOuYrxiSdisbhWagZGXxmXYM2gdsO3AwIVCvUF9enUZ8C8YAVpRsfT2BumoOG3aeuOg6WuAaoSfcBs5y8EnTNPsrfIwGblCi9eY27pMZOPeQ-GqDI2NPsNZ4S1hJsfnzPwRpwBzd0WC3KjRbHHsCwAbevw0ythWCCbkl3ch4PhzsC2XGPKkK0V9jdhA4n5DHKXRVDO4uE2RcsJ32-vVDQuyySqiuyuE022l56EZVPuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق شنیده‌های پرشیانا از مدیران باشگاه استقلال و طبق آخرین‌پیگیری‌های علی‌تاجرنیا مدیر عامل آبی‌ها پنجره نقل و انتقالاتی تیم در تابستان باز خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22383" target="_blank">📅 15:34 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22382">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VmGomVO90J51CqhLERi2I912XiAAzOEVVJx5X5vloE1pwbDAChVvj6MkZuz8Gxy9ts3VtlXzHjqCk0tfDDaOGzyQTgGXO4KlNkr6Y-1mLzBJaxrzZFSPy8BYvDFrwgJ2yGoQ0TtBsIvsC_lBLuXdW8eZffraZ-9FwpUyL3TFqE5JU8vuQvBUziGRikxuXGgr3K8Tg7W8_ryglxh43spaVrctNiluy_2o7aZBHHPWMDgmaqqVRbNepXzcC42yARfxhL_LPAUKLrG8zTfYMsElK2ki9eIlA_PS-4IBSMowEzIqLdFPUU01ykHw79qYcC9Hqfc27uKbifUeNGwTb7GCdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ همانطور که پیش‌تر گفتیم؛ اللهیار صیادمنش و علی قلی‌زاده درپایان‌ فصل قراردادشون با باشگاه‌هاشون به پایان میرسه و درصورت توافق با خودِبازیکن‌سرخابی‌ها میتونن درهمین پنجره با آن‌ها قرارداد امضاکنند و باعث‌میشه‌تیم‌هاشون با دریافتی مبلغی موافقتشون…</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22382" target="_blank">📅 15:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22381">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lpsXgFmhuXVFbgvh9VeSp2hj7dOvyPqQhEtdCiJCO2fP_7eqGJ6E-JP1JawYjNcmxyZ6VUYbVylr1VbvL4niwjGyTPc0YNGlWJN_jDe7fqFCtKY_9BmjGOzDGIiTErMVTgHTX67ICCK6gO8fLaNXTI5mziSO-xzbhGbAwPj48RoySd66bwJ3opefynMRVF-kiUoGohTz26pWIP05rzeqr0D6icliRaiuIxVLp1iUOxTp1aVDTGmvb8CTNZMX2nVWYDTNEtqJ-5UQ0zpBzoJii5BgRBOwcwHX-36WE--o2hdKOcx37ENnTA3wx5g-lHsoLqo0YTObDaIHux-l30_Qfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
جلال‌الدین ماشاریپوف کاپیتان 31 ساله تیم ملی ازبکستان در گفتگو با رسانه‌های ازبکستانی اعلام کرد که با تیم استقلال قرارداد داره و در این تیم میمونه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22381" target="_blank">📅 13:30 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22380">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">▶️
#تقویم
؛ 15 سال قبل در چنین روزی
؛ بارسلونا با پیروزی مقابل منچستر یونایتد در فینال لیگ قهرمانان اروپا برای چهارمین‌بار قهرمان این مسابقات شد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/persiana_Soccer/22380" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22379">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGPAzhXIdrJTuGQDBJ1iSW8HfEDfha3qKOwR6nLqLbZ8dzJ1K6KyhIucHONm3_eYKLmyZlsNC6PXHCyCGduRWiTPUtsu8SIxy9oflGaOPTZC5GPcjiQgczR-niy2YQHsRy2oVtHOHjNXEyiCYN7Fk1ZoKouct2b7-Vsk9-Us1-Zo9r-cK_RMvPCmUlwYjOlCzgTVeDnnfdUK1ZSo-3JeQPSVUmJa4RuNZmF8Rfdx03i1AlQv_g2iZgGN2qosPBxXVxWdnW3z4CILzUz7Ny0qo5IRC2nAUkjc1ikPI47--44gvV8PsICnEhZruh79Aftrmdke_ALbYOGUcPFC51mu6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ محمد امین‌ حزباوی 25 میلیارد تومان از باشگاه فولادمبارکه سپاهان طلب داره که از طریق ایجنت او اعلام‌کرده حاضره در قبال دریافت رضایت نامه‌اش ازطلایی‌پوشان اصفهانی طلبش رو ببخشد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/22379" target="_blank">📅 13:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22377">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LAI6qOfp6h8IMEIAQmYjxHxvk_hiTX2Gi86c8h1jcbROzdx9xp3UmzObMBvK8-sHrCI1B3s1am4tTtEUgOpl1nVGv-8BqaZY1ya9cY3P9a9fpy3rf875eBxvB4OUlIe7x_3zypSa8qpdxDe63MU4uWVjA5XI815HPJOftidWvCx36R9UNLBTXg_XC7ZTpL7UVC9wCXuC5JpyLmv-Sy-_YOgiPY3miyYXqe992jBNFJi1-5kninbGV5QYffoEc6WuQ76p9BdzzU9ZDFgUenS4uZ1xH7lbNnBGSbzk9wTFAyTEEKEU7CAopXSbVdi2JT90CEICL1GqZjm4RlAEdpUC7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbe2dafeed.mp4?token=LAI6qOfp6h8IMEIAQmYjxHxvk_hiTX2Gi86c8h1jcbROzdx9xp3UmzObMBvK8-sHrCI1B3s1am4tTtEUgOpl1nVGv-8BqaZY1ya9cY3P9a9fpy3rf875eBxvB4OUlIe7x_3zypSa8qpdxDe63MU4uWVjA5XI815HPJOftidWvCx36R9UNLBTXg_XC7ZTpL7UVC9wCXuC5JpyLmv-Sy-_YOgiPY3miyYXqe992jBNFJi1-5kninbGV5QYffoEc6WuQ76p9BdzzU9ZDFgUenS4uZ1xH7lbNnBGSbzk9wTFAyTEEKEU7CAopXSbVdi2JT90CEICL1GqZjm4RlAEdpUC7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
نروژ ویدیویی از لحظات پایانی رقابت علیرضا فیروز جا، استاد بزرگ ایرانی‌ تبار شطرنج فرانسه با حریف هندی را منتشر کرده. به گفته فدراسیون شطرنج نروژ، پس از تساوی دو حریف در رقابت کلاسیک، فیروزجا با تکنیک آخر‌الزمانی و با چند حرکت حریف صاحب‌نام هندی را شکست داد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22377" target="_blank">📅 11:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22376">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/coVidznOaVp53mIZpKaRdF6nG1lmiTEJBBWEuQgdvPvDGUCh7wBYGkgI4fDRfesTROsUl1H3xSRnwwb3gzyD2_pOIIIZkZNBSZtETiutEGjcmnZFR7E77Ud3wx6bT1sgYvrEYC8646CoZ_NxOV0c5MyQU79K4j2iIlfT-q93swEuUg4Fp5Vz7FfNlaVSjZCRPGk8ehY1PuvUROJDipJnjr8slD677HePioqmVv2-R11rm8w6L-Q1YhXoJrMm7V7xtIB_mEKhLFA1UMf0dkmntUUnnrzrCyM5uwQ1NFzMnJUbHfU-CuYtymZBjlvxlzmzBQebqd_Ykoe2GAVd_G4g_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار فعلی مهاجمان خط‌حمله بارسلونا که ممکن است آلوارز نیز به این فهرست اضافه شود
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/22376" target="_blank">📅 11:22 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22375">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BaPSNg9q3fUMMr66qqwn-go-3h51gxPgxOH7HAJSLfmaZRQMNVzORiy-Gylo2SJXNRNbnn-8dbFVbgtlZFn1wF34cSx_DjCn0Uv5D6seIwBx6KOYMYGJIti9JALYsUHxbyvaGGH6XDY8_A4RbIAogr1SDcn7s739c4TRiNSpzfcbmEK0D-x3iwbjt1fuuFrY26_GJiNc5KWHHDUazKDW49q0UCVrek_EJf8RRBfrnXJEJkIENO5H34l5oPgDpWkOx2Neyg4ahEBYG6qQy3aWlKd4X7ezhGn4m8KK6SLSRK1-bCLy00WUOQMjhe1MW1DMQHrGnv9dfBPehaiZnJGf4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اسپانسرهای پیراهن تیم‌های حاضر در جام‌جهانی
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/22375" target="_blank">📅 10:54 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22374">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRbo4_6dBcJGr2jrBfSR2LLEZdLsBUFYtMO1J0cv3vlfVUVRLd8734O0qJ0sUFAggwRE8hq8V7PPbaEggLvPkXdRL4ovIcN59st4fvjIOIGgwC6X56L6JVNr2L_baHhf9mDKzWcmBtb_WgOi7ki-kxsq5Sx6gLhkEspoRdYiMDeGHh7DCB35bK2Mucnx4PgXfU3drGD-MmgLPID3bakEzvoSX2jF19Wflo_9qFXgOGtOAzASMNdYT_24Q8lGAO2TThlYL2EipexOCcjfF8r85tmSJdQcfGQ-2UJUb0fx-T63kiM3-t-RLilsdCKhjWcvBaEjpbC9fl5gkfeZnw48qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ کاسمیرو هافبک برزیلی تیم مچستر یونایتد، آخرین بازی خودش با پیراهن این باشگاه را انجام داد و پس‌از بازی‌از هواداران خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/22374" target="_blank">📅 09:05 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22373">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Diq4iCM3I-DZzKs8XfQmd98Xz6KhbUocKmtelfn7teGw-UcXSEtDjgI3PryRXUN2t4lRKCiUtEKVFL8kzqUnUnr-MZROOXfuJfBVA90FkMVIHxgYpYn_7KD7dPRBvieD9lCbTougLnj86SLHvz2X8g965aSlBVi1De2DdkGyGV2w_IuJh3C9oS3wDHE_8WQ2a46ULx7SO0QPYYuCpdBNynDy2P7CDA6f2SJ_ma4FV2LJhhfcTtqG6AqtM0RWIJMITPqqBXE_GEFlV6iVyUJ3jgPcJh8AZD8LW1KPdI0YGeW3nfWUDlzphgbVHeSJ3TN6wBZDV8PimZGjJpqvMpEupA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
کافو تنهابازیکن‌تاریخ‌فوتباله‌که‌ توانسته 3 دوره به فینال جام‌جهانی دست‌یابد. حالا لیونل‌مسی و امباپه این فرصت را دارند که در کنار کافو تاریخ‌ساز شوند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22373" target="_blank">📅 08:45 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22372">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=UugCJr7EHOmZ7HERlAsxzuAqj8hK75-6ckO-MyWWsuXhsaS17XEJuWqQ67ssmaWRr1hs4X5LSnC-EHsPW12TabnWrIsXQfdW8YwTizfd_MfXy1FbVSSkOy_XwdHEf4lIzWNLXolAE2hZ2KXzBP7cLND26J5g6kCe1rmA4c1qCiRXYf-ybhDtgyDyIwHQLBmlEklxi5ODQ5io0nad_uVILYyjDqIaWTs9_laRdNBu38FZnOHwh348lXaars0I6vkz1umSTkDDKec2NJdnmepyMq-hmjc-t2pft49i3rOjneVNAhU0342MY7wMno830ZqMFjf1VjUZWM7gXBLdhvYhUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20ca45cde3.mp4?token=UugCJr7EHOmZ7HERlAsxzuAqj8hK75-6ckO-MyWWsuXhsaS17XEJuWqQ67ssmaWRr1hs4X5LSnC-EHsPW12TabnWrIsXQfdW8YwTizfd_MfXy1FbVSSkOy_XwdHEf4lIzWNLXolAE2hZ2KXzBP7cLND26J5g6kCe1rmA4c1qCiRXYf-ybhDtgyDyIwHQLBmlEklxi5ODQ5io0nad_uVILYyjDqIaWTs9_laRdNBu38FZnOHwh348lXaars0I6vkz1umSTkDDKec2NJdnmepyMq-hmjc-t2pft49i3rOjneVNAhU0342MY7wMno830ZqMFjf1VjUZWM7gXBLdhvYhUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
صحبت‌های طعنه دار ابوطالب حسینی به وصل شدن اینترنت برخی از کابران بعد از حدود 90 روز. خیلیا هنوز نتونستن وصل شن. از 70 هزار نفری که همیشه پستارو میدیدن 30 هزارتا آنلاین شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/22372" target="_blank">📅 08:35 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22370">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jxUpM7Z-AOiA5eFvJVfP-Njv-uSjcngJReKZXZBN2X4yNnP01Uzrb8Xk9l2CweAgisztpanSih9coWrNRQEeVWWcVZ_oiB7DVE7YS2SHxa2vUp3ZX2QxoQWokr4bwyIm9dtoLVE1vy4HCISV44Y8UNP8eMNZ4fiVb0RNvi4bXwGagFeSO3i6PYGwa3EMEckjMWmyTXG_FzlaEXmVIJaN5Wp9E4EXADMt1v558lbuG5YPz3yXKqs3N_z0cmlbSuf5JTgrcA4On-47lTapN2gvLlC7M2qYDaiiYweVRBbp74p7xFgiyjNniX5zOd8zkw2m-ftQNTBPVs7Koy8I1qUxVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌امروز؛
نبرد یاران‌صلاح با روسیه در بازی‌های دوستانه ملی پیش‌ از جام‌جهانی 2026
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/22370" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22369">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IYnREREchpf8tYF02I2JMblu88QRaJJqgXwSp3nLBKSeV1eIKRoxm6qa6LI7RczhgoEPW0l-CJ8rFTwOUr7EoYZZgJ0eu9ZYHV2S7nXlP53y5BPAPKFUYOrHilQsPgtzATy_NbEajWoATzkixrCDV2e4dBcuVErkyCApXaesMgRjVmQN0vA4rKJg31zCtAGaWKZAi9cnLsEjKR27x0sL7dVbeJOFxmeP830ggUxax3xR0oDAd4ZGmF1oA_97ikWy0vaEtLkYwLQ3S1iNeO3A63ZNdDdzKZAILrLRquZWKd2hN4aWH7oLoVlaz8oacUBon96s4Y75HxgBrrWIJIcaQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه تنها دیدار دیروز؛
قهرمانی شاگردان الیور گلاسنر در لیگ کنفرانس اروپا با تک گل ماتتا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/22369" target="_blank">📅 01:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22368">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ItRfQOoV5kHFovjZr5apvNa_vfJRYtXUcSKtY1q0B03XRgYnxZxLvkpOBIoCY1y11Gr6tXLSPwYo8Xgr81Or4QKCXjgXr5fNLx2yfLnIBs8lFi82dwWbATAHWa6uZ7RtiDALZoqZVTYspT-JiyJ_wSlZ5S8Y7ecPoEAcLomGXqeaOoCAajIhCs1bQRHv_n-uCHS4iIWdtZ_ZSxw8y86fnORK6ZsD1jzg0SLGbkssG6IuIV61ndjbcTuskCmVh2yq5nG-pbxbkiivDXmwOhvpBrrseAdoCwqKVF_9LmYhId_ROA7PSW03X8LCuWBB_lbwVhohZYF1AJEPLhMZAO-RKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
اوستون اورونوف ستاره‌ازبکستانی و تکنیکی تیم پرسپولیس درگفتگوبارسانه‌های ازبکستانی اعلام کرد که در باشگاه پرسپولیس تهران خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/persiana_Soccer/22368" target="_blank">📅 00:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22367">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=YBdvA-1PocY1JKhOjI0gq1PNKK3rJJ8sr9KbX9J3_vwskfTFVdhKo285M-e_jFrCM55NGcZTjftL-RgOpOCPxS3vt7WxR3p9QYidUGkXB28CrJZiiyEyaYf8T8-_sYT5zCao387t9JYxbElxsOSLzRuR4cWE33BIQkoOzdxNuXXExI0UMtP_mT_elCbkfy0rE5TsN_FCAps9S5RTtUo8QsRreUoMmJSsClm9OrBnRUZAVWktLIIOfl4HplQnOypiIUsKgjSzr5rl8FeIQjt-CsBUc1gyrK4DN-2ves1HkB8v2N-FFDkXCTQEfw-XSaVS9wy3vr10g9chw44fyZrJ7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42f6590fb1.mp4?token=YBdvA-1PocY1JKhOjI0gq1PNKK3rJJ8sr9KbX9J3_vwskfTFVdhKo285M-e_jFrCM55NGcZTjftL-RgOpOCPxS3vt7WxR3p9QYidUGkXB28CrJZiiyEyaYf8T8-_sYT5zCao387t9JYxbElxsOSLzRuR4cWE33BIQkoOzdxNuXXExI0UMtP_mT_elCbkfy0rE5TsN_FCAps9S5RTtUo8QsRreUoMmJSsClm9OrBnRUZAVWktLIIOfl4HplQnOypiIUsKgjSzr5rl8FeIQjt-CsBUc1gyrK4DN-2ves1HkB8v2N-FFDkXCTQEfw-XSaVS9wy3vr10g9chw44fyZrJ7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تعدادی‌از فوق ستاره‌هایی که جام جهانی 2026 آمریکا آخرین‌جام‌جهانی‌خواهدبود که در آن بوده‌اند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/22367" target="_blank">📅 00:40 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22366">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RSYt7O5i0NJwJYRbAOZ2olAdgpomBTVLTHKCRkKrvw2S237sQudvFoffhEDQkbIrSthv2YMGeSvZpKtvSLOmQa9TC1IOHEJ9Wu4Csc1YfplAMWXHTe4dhRdZO92iYFg4t4RmoIy9VtWRJ8gRd-uarxO5HHAxn3I9FEp0n4YC8xm40qm1JpYJpZ96u8d7wXpeY56gfrfS4Z8Ilt4pJrV7Hc2phi0OVQ4vZiIQ-l3sGYkgo_4Rdy7vJRYxGaJUUj6YSCgF5QUEexgPzSpUFDIO6B71Q733FeNpINkbnvHTdtGO94FQrBtp2QAmlPD1YWRxYhpd6Hl6VzGWDqHneidjYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه هتریک متفاوت و قابل تامل کریس رونالدو، لیونل مسی و لامین‌یامال ستاره 18 ساله بارسلونا!  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22366" target="_blank">📅 00:39 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22364">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UFL1rhRQM5rtH07rspBedJMqi9UV6uPc-5hhv7rDkgiSvfeEFrefNlZuPHOUWi3hnpcQGXjyy4_V6eK-Ud1Z8qkxbho6QfUO-PwTdkO7LiMydZS11v5QwQCGTEEAwgcnMaSoW6rTF4ADhAjfeetCIqV14JnB9-HQehK28HvBAWEFeLdkdAKYKb2ZDOZ4Xpl6VMDfqO6ynKqT5p1NFQaSjtapjmQqn5rnxeYCzF85UNrJC8QVTCZZgjn_ysQX_LW7eqDB1UDsKAKVoFCmyYIxak6WfzkshSwtDQ1t2QOtJllscLYLBCNUoIANXe6wcfpt8gpThNq3BqR9FuL6cqivIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ طبق‌شنیده‌های‌رسانه‌پرشیانا؛ نماینده محمد امین حزباوی بزودی یک جلسه با مدیران تیم سپاهان برگزار خواهد کرد تا توافقی از جمع طلایی پوشان زاینده‌رودجداشود و راهی پرسپولیس شود.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/22364" target="_blank">📅 00:26 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22363">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEPQci7lK04vrw7smLgAaLiw62MmDWDc6yxtvGOO-C7TsuwnZTB6Sc7fiGPpH751a6R9GyNpQ4fNVzQMPehhE7dW2RSXbRInOK0I_N7Ev-RM_tX4Xp_Ua7qA7TSXQ29w8vOM0V8oU0aCecofXj6RbfD8AO78iiA2HyFMQbEKVwOcaWCBHXOVj6g5zc8xdZEtYJUh76sLs-_TdnrjTb5MqTDAb_jowJDnTzyeaGzC9z7MAyX2vnrq1rfojI4eXRGaO6t2ewylG0IiWfmDqrwJA4HryVIvXQsiT-BO4rIUWEqqQObAOFBelanR2CwrKUk9vuTKSFjwx28M3Lk2RdFvIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بااعلام فابریزیو رومانو؛ آنتونی گوردون ستاره نیوکاسل با عقد قراردادی رسما به بارسلونا پیوست. هزینه این انتقال 80 میلیون یورو.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/22363" target="_blank">📅 00:19 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22362">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkXlael2Yo71DngrQ612qRueTLjm0NOkZhD1kk_t0zdSQ2LaPWnrUNX45jSWBQyxOXev46IMl1R5-tu8uiw2qplVKtiJ6_3tK2AQaowuQYkDZsyl-hL3GCpQq6YIwVA13bnEwoKfrysMbYTGSWFtnLwQcQiLP0CGwPHi_lQeLQ7jiRYPaew_PslVo9Wsjmqf-Gls1H9S_FjSB8DwNLwv-NncpBvxnWW4AAV4k-TxkR9PSVFW9bu6WGZkiHB5KNwb0UdNszphLA40N0mw8YEwpSEbeIbElKR8IoNmgYFsGLSMBdX5aCzCkJMGTq2YaIfKrO9eF-6T3BIVoPh0Xh0gXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/22362" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22361">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=Xxr2Xx_ab3_1F2O3NihKXxGi84-Sb4H99tcNb1uxq3IyhkiIrk5KKq3V2ghnGVgxs2Q644yPAmM6cGNm0-tr-EmzEgkJRX9fNaN8h3NKilTXoBGVedM_DxUCTOSuC4mI0hAJZaLZFjxo4z6a0kEe8d3iQTvslGPOd1I4w6fxLW1dBUEosPDCGua2HB2yq8uSG9redgf8CeHRRrQpnhYmwg0tk2FdYTn0rO3CkVjHvkq4Hc_6uIKK4wlvx6wr5Rc2egtV4RnTUJ72uuXyNh1Cbcl8YRAPMDokMZhe6lX3FONnMDLLSsLsgER92a5_8CJye9gTyGvxGEhtoGkIMg3y0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be02e7f18e.mp4?token=Xxr2Xx_ab3_1F2O3NihKXxGi84-Sb4H99tcNb1uxq3IyhkiIrk5KKq3V2ghnGVgxs2Q644yPAmM6cGNm0-tr-EmzEgkJRX9fNaN8h3NKilTXoBGVedM_DxUCTOSuC4mI0hAJZaLZFjxo4z6a0kEe8d3iQTvslGPOd1I4w6fxLW1dBUEosPDCGua2HB2yq8uSG9redgf8CeHRRrQpnhYmwg0tk2FdYTn0rO3CkVjHvkq4Hc_6uIKK4wlvx6wr5Rc2egtV4RnTUJ72uuXyNh1Cbcl8YRAPMDokMZhe6lX3FONnMDLLSsLsgER92a5_8CJye9gTyGvxGEhtoGkIMg3y0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از عجایب فوتبال بانوان در لیگ MLS
؛ بازیکنی باردار درحال انجام بازی در یک مسابقه کاملا رسمی!
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/22361" target="_blank">📅 21:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22360">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oEhcFqk5lQcDF_vj5dQEaYleSSIyAdAjAgsfxrLEcbu_Xg1R_tDPpgmrR2dliIbJQF2y0G-M6BBYUGxFXtHpTU8ZJ5A0mvx-rl1pTgdx722rJGOsKVISGFQG9OxH0qRyQnG8IN7V-ND_h8TsQ2jb9HRCqe9pN0cc2cA7FlHfcZdnb1uUdkdvsw3HY-YK35XVKsjUlzfqoPSYPlUCHRuXDUaElFuGlWCgBXK1ZjKZUZg09BLwmVvY9by08Hb6gpV-UTP8yjsRVl19kY4tW4fIxOTJqvqVUWpyavQ59UnQ7M7CUnqmFR0GIg6cKS35SxL9SIOTI1z8XGi7VNadjG1vWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ آنتونی گوردون ستاره 25 ساله نیوکاسل درآستانه عقدقرارداد 5 ساله باباشگاه بارسلونا قرار دارد. توافق شخصی بین طرفین انجام شده و تنها توافق نهایی بین دو باشگاه باقی مونده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22360" target="_blank">📅 21:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22358">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=j93Td6KgTjNITC23XTeWNQ_ux1sBoaDEsC8f90-1JBK7jfy5m_VypRGJBZ_3bwZKTftRHgBeyzyQzIGYqeyRfVM6-pLCa-2gJpu9N8yU9BSXe2thUzFLDqEoRfOAoe2iN7iF8FWmbAyi8JsIKDU-wcUwR4XxLcz6JUR79EVdBS2mcrBEXxlceG8Z-5NS2GQA4Er58iHEZ_ori6w8L1QnGRkyVX5sparrwvT3CHDL0EWhJt4_eZca_2T9g78AQtQBbx7uvSPCOoeOSM_O6WyhvjPR3diTf4GSRt_Kwl7WXy9TiTUNNPfEoT3Sc-npm-H7RNmutmc_mOuNDhoyOkMSgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30152b67bb.mp4?token=j93Td6KgTjNITC23XTeWNQ_ux1sBoaDEsC8f90-1JBK7jfy5m_VypRGJBZ_3bwZKTftRHgBeyzyQzIGYqeyRfVM6-pLCa-2gJpu9N8yU9BSXe2thUzFLDqEoRfOAoe2iN7iF8FWmbAyi8JsIKDU-wcUwR4XxLcz6JUR79EVdBS2mcrBEXxlceG8Z-5NS2GQA4Er58iHEZ_ori6w8L1QnGRkyVX5sparrwvT3CHDL0EWhJt4_eZca_2T9g78AQtQBbx7uvSPCOoeOSM_O6WyhvjPR3diTf4GSRt_Kwl7WXy9TiTUNNPfEoT3Sc-npm-H7RNmutmc_mOuNDhoyOkMSgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوست دختر جدید کنان ییلدیز فوق ستاره تیم ملی ترکیه و باشگاه یوونتوس ایتالیا هستند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22358" target="_blank">📅 21:09 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22357">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVDjbek9SeHiNmoV2t-dqvm2qDpy4cxFTUOME_wNJfzkiFVjNIgkcRtjIjBB3Q3WrDFsAkONSkhzh-SYAWpWCBvVb9eSlTm9UJk1ESyDcWRZmb8V9oLZcGTizz7WwCemuQo9Nisd-UT0EUxmHv3ANDJBCLVtqgYFd1WQQHnkqqn5cwy-wrcip0kXpThNeBW1yy5D1IULJdIzOZv1lof6_DGm_74XkEtt8buAiCemh5AgwhlJbO5StL3zdgD0FoK2w_idoKhiV6XxoqBfWEwGEF2HllZSDHOOKGrP79Sit65ddf0XJWvSTGFt2uuY2dunUDTICm52CtslBEMUG9neXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
فرناندو پولو و فابریزیو رومانو: بارسا گوردون رو از بایرن و لیورپول هایجک‌کرد. بازیکن تمایل زیادی به پوشیدن‌پیراهن‌بارسا داره و حاضره‌دستمزدشو کاهش بده. نیوکاسل برای‌این‌بازیکن ۸۰ میلیون یورو میخواد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/persiana_Soccer/22357" target="_blank">📅 21:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22356">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKu0Bhv12a7TdSLH7WZyDyw7xs9t3oh0mgMDdnJ5L7hp5TJqG_I7cEyCmoQCPwxxlIthAzblno28929WsrDYfsm0ERXhA_I5J34hF7SQxT0gLD2c9NhcycZYlXbNI-tVSw0I7sziBpr8aubicHkIReD1in-fG5GdvL-FvSKg7jvPqTH91vzZqpnZJUdIgxj85D6PJbJb5PU9fBnaFqsFyxtRAOLHEw5AUADCJYtRJ8z6eiRnGrbLGxXnWlCviJu83FdGiRHeEasyLFyaKqMcLH_XO3jMXt4RdMHGm3R0LXiiKeU5UaCSOBxJDbIiW223lwt-Mb0kpTiRzXkgMqyABw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ آزادگان درپایان هفته بیست و سوم؛ نساجی سایپا رو برد. صنعت نفت باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22356" target="_blank">📅 20:58 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22355">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UmN9i0EHK2uzUXxkMh3P3lmIVGc4i-1YI842n20pCq2OR2EGzPkT4VCPQQJfHjw2w-jBwM64vaTEr_OovMG1P5HkT2WXEuHQOyJP89tgi5MkxDy-5ohdJPdGS1itrHcB25MOqcafFImYxGUAo6FwgAQEb5ky2MmBOyqloobG5yrO_0Qr189bE4RaTHe-lvYebf_XK3zDiAFaaEyFMVdP3AUdYnykuRFTflnmPgeaZjwH28bbqEb6QpCJcj9nvgFSD5AnLMuqx3rQfKqCIJsEdN0VIeA7ONPfz6P-8y2Ms5IUSaj6I2ksenL3a0Wd3K6Z-5NWlOVA6onXu7aDrthP0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛‌طبق‌ شنیده‌های‌ پرشیانا؛ دوباشگاه لیگ برتری بار دیگر سراغ‌جذب‌حکیم‌زیاش ستاره مراکشی سابق چلسی رفته اند و این بار احتمال اینکه زیاش بالاخره به لیگ برتر بیاید بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/persiana_Soccer/22355" target="_blank">📅 19:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22354">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJQan0FEeZKSx_poD3jtb_wB-BEszDlk77clCtcCG0Kx8AwTvFv0YNWpmzM8ZDAA0an2qyQz-A6-3QVndjkazkGDbU0bkKR9BcEURC7Z1hCNHfZTREggC-vSgmfWeBN-OSaN-1qAEEwhoRqvlaA4ifXJ4gCb-mzHdLlMbKcRuA0xjL-ny5pXJIpLWfHTyR0ZhL_7w6rVyRFHEnIdQUgS0ukgJlrbW-JJ6lEofRdI4TepEDJhq94z1JbUoHXSnIpv4HZFx3mg5XLt7SPzLhcJNRoNXvqJ7hw-gtm5HxRwEkR6tAUN8-YMnNknILmZ-VohGZxmL6Btrn6NY1rJKEfSpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ گارسیا دوست دختر جدید لامین یامال: لامین بهم‌گفت‌دوست‌دارم تو آخرین دوست دختر من باشی و دیگر علاقه ای به رفتن تو رابطه‌باهیچ دختر دیگه‌ای ندارم. لامین بخواهد براش بچه هم میارم.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22354" target="_blank">📅 19:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22353">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JuDgvTjRk33xGe7vHS5tKI1RseYOK44wsOmpY-cMzFR5yMgwy0XCExHROrdrID66TtThqXUKoF69bHJ2nZ9gsiV7YqmOgIkLmSIDUT68yHYRhbr6ZyY9NnYw8F0SXjlqNvuIcBzbJY5M4ZDvBtrTMQBwJvGYgWYOevS9GW9ws0WE8BLxsfAMYCxQtYT7WVnf1tOVRdPKIDsvwVEdkSXk7DfVB3poTIaOtFDKJvR34bKHBHK4vA_kVSy07xQ-f_ToxwI8CX1PkPh0qpR_0s9trfCGgNLk82f3j8Qy4DUrkA3GU-drEkd70IYtNFoZPKs5krr0t1Sn7TYfCaIQ7Q8R0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22353" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22352">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30945cae67.mp4?token=eXK50q5MkkOdINl4bQltbk4triz1L8cM6XVFX03AhMaxtSzLR3iFvIPgMYNmjmw52l9ApTA2oxiLQP9yR2Vacabo6I9Dqd-Y5AFL4IB9o8BfzCnpEcp--MAqUK4qboHnBChvcknQ482bJcnrT5xgRNT4FNG3oE3pckEdQJl7ZaQW9791Br11lPGyjRsDTP6H2GelDBoHuPupdw0A0kC8PGTfH9zcA2YaCEbBduYFfNV6zt_swRMViFr5CGAoivAPIwKZB4XTIfj7sTRKkov94e7WkEdeFT_RaxdLEuXq07H2i86UmPednP2xykNFuSBlX1ylbYjPPKjAWjsHvmjJJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30945cae67.mp4?token=eXK50q5MkkOdINl4bQltbk4triz1L8cM6XVFX03AhMaxtSzLR3iFvIPgMYNmjmw52l9ApTA2oxiLQP9yR2Vacabo6I9Dqd-Y5AFL4IB9o8BfzCnpEcp--MAqUK4qboHnBChvcknQ482bJcnrT5xgRNT4FNG3oE3pckEdQJl7ZaQW9791Br11lPGyjRsDTP6H2GelDBoHuPupdw0A0kC8PGTfH9zcA2YaCEbBduYFfNV6zt_swRMViFr5CGAoivAPIwKZB4XTIfj7sTRKkov94e7WkEdeFT_RaxdLEuXq07H2i86UmPednP2xykNFuSBlX1ylbYjPPKjAWjsHvmjJJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
از حواشی بامزه مراسم خداحافظی باشکوه پپ با سیتیزن‌ها و شوخی برناردو با صحنه مشهور پپ
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/22352" target="_blank">📅 19:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22350">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G7zkMWOe7uFvTB8l1RBfXFhDhajZoL9uoGU_N1-IOj5Rj0qkCR7ta16_Yar_rF31foqs7IX5tj9hIag-jHkt1x8KwJHJVPJQf7ewfUChpZUCU8weGjwCD6jV6cEzBzzF4gGkZfnhf8_cs0VeN_qYze7JK8SexHR2GnKDC-kvofIiebO3nilMe7wvvTEnRftqVzTYLaO4s7yDxOyMco6PrnTX3_1aMleHaYwg45Gkhui4NZiG8y2qP7DA4CmqfKKQU6zyAMZ0NWhW5BLA4FeGicn_fAnBGISIF8xl4-L2HmsI5jp2j2yJL4TH3OOaVxOovZ845ILMH0mw1aErWgX-yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
#فکت
؛ قهرمانان دو جام‌جهانی اخیر در مرحله گروهی در گروه C رقابت ها قرار داشتند. تیم ملی برزیل مهمترین تیم گروه C در جام‌جهانی است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22350" target="_blank">📅 18:12 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22349">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYOaBXqF3_QCDF5lwFo423W72BybbLobIcMkRnnKOVk_WRNPg-7UHw2g89atoG3TT0FLEySIaQH4nXZ_CYIwasXADyLyQia3zJNRBsq89tCLEt-_FuJQIOZZV-Wt8FjQlV50MAQAn7y592TX3PZvnw4F15m4hbDF_fdxJ3TDNSIuNkehGRqydg-hrKwpqbQNzW3zdG3-ZSjtDJS630T3uFEz7vbh29JojSi5e9t8NHJWKmZDRNornOKl5JKeRf5OY_kqgWUZbrvTu-CNB9O6gUNnGXTVu5bt2y8uQZENc0IUPWxXyV4bLUwlXPO9mQGoBthWUpAJwwFyYQyMflUcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#اختصاصی_پرشیانا #فوری؛ یکی از مدیربرنامه‌های فوتبال ایران حکیم زیاش رو به دو باشگاه لیگ‌برتری که یکی‌از آن‌ها شهرستانی است پیشنهاد داده که میتواند با قراردادی دو ساله به ارزش 3 میلیون یورو به ایران بیاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/persiana_Soccer/22349" target="_blank">📅 17:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=Q7XLEUH20n1ooqJg8pvx4BkM0RkHI8gC9gxuVF46yCIXLejjZ8nhgWT9EKJYEbFfOeSbZSd-pagVvM9BsRKy9nMAVBL7SummPb3UsZrLqtJrk2oCwFEG8UpOaETE-IszVPtGCRDU-ItvxijgfBxXRMdIyxtjcxkLZu-xUUkRLkjlvumMctpEGZ5RZY_JfU5ciy9kClB2Mape3y8stc4O4x7NvjfHiCmnGuQTRaF9tQSqRJLeC-9KECWSfDROdX31u9TEhEzHmlYIRqRvcHQ_e-S1L72LP1yfm5UUA5CwVs6wk8s94NI80OF9IyoGwjp_-n3JbKSJ0sBwS8jVSQNDyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6d0b75c07.mp4?token=Q7XLEUH20n1ooqJg8pvx4BkM0RkHI8gC9gxuVF46yCIXLejjZ8nhgWT9EKJYEbFfOeSbZSd-pagVvM9BsRKy9nMAVBL7SummPb3UsZrLqtJrk2oCwFEG8UpOaETE-IszVPtGCRDU-ItvxijgfBxXRMdIyxtjcxkLZu-xUUkRLkjlvumMctpEGZ5RZY_JfU5ciy9kClB2Mape3y8stc4O4x7NvjfHiCmnGuQTRaF9tQSqRJLeC-9KECWSfDROdX31u9TEhEzHmlYIRqRvcHQ_e-S1L72LP1yfm5UUA5CwVs6wk8s94NI80OF9IyoGwjp_-n3JbKSJ0sBwS8jVSQNDyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تنها 15 روز تاشروع رقابت‌های داغ جام جهانی 2026 آمریکا؛
بنظرت کدوم‌تیم قهرمان خواهد شد؟
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.2K · <a href="https://t.me/persiana_Soccer/22348" target="_blank">📅 16:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6QdJNBKi3h3wmEcaS-S3tBg5VXuR7L4EHgf3V0QCZXS1v5Gd23-q9rNdAT1cdXOiV-J778hHfS2-BvxWzD_LcLCzst3LfzEdIEYVcVCVHF6WS8dU9t24-lYxyGpzjYHN1h40fnWc1SlQVySmdTt8YhPeI8GnZWltWXesVU4gDr6_ISOFGdCmGhGMlhST3AuE9heglbLkVRlg5t0_oBwVHw_97bqDFegM0BnxW6A2NUpeHoQOE_qthrM9cIJwAQjjmjVbqJ62KibNlkQIB5qkOsz10TzXzzDrfBjGYDFHRm01WiFPOoajoeYYy68rAs38IFyCag-ehwi3ZhV1GUuEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکوخمز سرمربی سابق تراکتور: از طریق‌فالورهام و چندتا از دوستام متوجه شدم که مردم در ایران وضعیت خوبی ندارند و اخیرا جوانان‌زیادی در راه‌آزادی کشورشون کشته شدند. جا داره به مردم داغدار ایران تسلیت عرض کنم. مطمئن هستم که پیروزی نهایی از…</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22347" target="_blank">📅 15:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22346">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_0k5aX8DbFjd1iboIIDC5jr1JKy45Wbwsuzk02_nNUqYBd4Gw33FRgrb6ov9Go5AXPQPRomze9g9416yI98g7o0zDT-RvdGcZHC_gcEZjHVbpffxESOrcaeR6EFnKfIMdXmUw8iIW0A9DR2y8w-8LGY7_U9rcr5qtOTW6FC0j0S7JrXzgehJvKI09KrWjo1BbOBCEtpa_yWaWVXgYEviYHWfe5gwKALvIrVOJ_Bw7tieuVHvtgNqSqlS8RNVmk1drRkudfhZL47kV7JV5fG4Ucj9qTOukFEZNcNy6fXKEh-mLEFenK9t6O7JH4Yjs2N2Ee99_Dbla35nMpm7__EIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
لوکا مودریچ مهندس کروات و محبوب مستطیل سبز میخواد بعدِ جام جهانی 2026 از دنیای فوتبال خداحافظی کنه. این‌ستاره با کلکسیونی از افتخارات از جمله برنده توپ‌طلا و کسب شش عنوان قهرمانی درلیگ‌قهرمانان نام خود را به عنوان یکی از اسطوره‌ های ماندگار رئال مادرید و تیم ملی کرواسی در تالار افتخارات این ورزش برای همیشه ثبت کرده است.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22346" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22345">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lt9RUK7W2GUlUXuWrtN0B2jmff26XPrpUerHzaTGahXlOp1gs_KKHytilnQptBhMBveozTm6ZoighDiX58iEtDIkEQCqb4w-NWO37gP9Goa-67YOnd8yFDTCoZ0gQVcDAel4uZmVaiZ8ouQkFCpuYPjBiU4D822R5vNmZ5VBytKBjuQ4BvL7PmdiL8dU4p9PWbqRD7fNdDY9-jjLWogons4F4qQe6ajBUcPp3acimXbyw4W9eE9tvI_ZjN9MlTAxw8NNdSo2ZAe-aZx0AUnRaXHjypCr160C5X2o4s2yb9gL96UO5n5XGPIMCs2G1Q75ApCMPh0U7yuKN3TRfU_KJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونمایی از دوست دختر جدید و 21 ساله لامین یامال ستاره جوان و اسپانیایی باشگاه بارسلونا  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/persiana_Soccer/22345" target="_blank">📅 15:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22344">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AvoEmGHyHroAyMeo5FSrxTAk_WZa9Z3RL7WSo9zHKq71DTyk3cLx4vYAE9uarmZXSm-_TkNwIFA6eOTp7pHl-J3A_I0aIajpfmfpnh3p5y3McDT7YY3thdCW8QCIrYP4NljdRzalwK8QauQvbqi3DLu8880IwmyJw8LuQpznvRgqHY8X1afbK0wANRbsTCVChPCzsTOEQNl1d8SpwsFEW-jSTffmcFYMuN4W0DDl_I3A9DxkMVEeYwQH8SBtnGztwJvJk_KVj4HSuBdK1IFKr0-Es6834LiRL3epEP6SVg6OrYoQaEsp4FMwvq2owK2BSAwQajd7Zjgvkn_bcAchIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اکیپ:کریس‌رونالدو از نونو مندس خواسته برای انتخاب تیم جدیدش‌عجله‌نکنه و درصورت جدایی از پاری سن ژرمن راهی باشگاه رئال مادرید شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/persiana_Soccer/22344" target="_blank">📅 14:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22343">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLpJNOobDNuv6AJg2wA_swAb3Q0C2f_q7J1tmu_j8AHQqoE4BK3ej8X08IOxg4QXPqdVYsxvkZ0deFOgz9dDrGddlxiNKHGwZ74aY_KyiLZqR_TLE3EaLdjm_PvIbjBmU1o9wtI9nVWGkg48EiGPBjyEdYIaNjZ0KnoCI62SC8A7FocUxYfY4gdo2V2rdVWjjw72P0bzR5UUzkr4PYLtje68a2oTbbnqPkJkdmK4avp-sAfCg2f41YlAPoEDLrLTXVAGR-d-CexmXaA22tH9K01B-2OjhmyCPI9wijV1tEhZiNBgSkudjrhkkSu4DWG1EJGvETbguOx6-OC5V4bHMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کنفدراسیون فوتبال آسیا؛ سه باشگاه استقلال، تراکتور و سپاهان سه نماینده اصلی ایران در فصل آینده رقابت‌های‌آسیایی خواهند بود. باشگاه پرسپولیس ازفدراسیون فوتبال به فیفا شکایت کرده.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/22343" target="_blank">📅 14:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22342">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snon7AdJQR7tRH8Jmdrmg8rDj_nDCN1Dk-1DoHKUMiiBsKAW9pdAZwKpV5CGc5P09SXeU999ZVUZJQfUyLdOkY07LfEwKDvMeFa7xTeL639U4rqzw92WaCch4vuzls3g5XaDf_rXvupxvhaioNnQeVLji54zE81Z7UJDhXwZ94UBgU-ngaOYDiWagmWyIhdRXZUmD6505y8IAaws7QcUgmWdYcPUiRm6JoTVjmXxkL8zGL1lmrR6HYDArKE6MPEyGn-7Tw1SKW6OC8bBQVAK4KD6qFkWAakLxXqpa7B_G8P6Gbzs5pernYdy0HkOJL5KZ97YA102nD8hFrQzj6k7iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ رسانه موندو: خولیان آلوارز تصمیم نهایی خود را برای پیوستن‌به‌ بارسلونا گرفته و درصورتیکه آبی اناری ها باتیم اتلتیکومادرید به توافق برسند این انتقال جذاب طی روزهای آینده انجام خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/22342" target="_blank">📅 14:34 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22341">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ku7Vt3yXTGVDt0hAIcxMxHHJ7takcbwwk3l7X3fqu66JHz02Vmus-ptUTongzR3aZ6hIwEkFdeBRRbyVvY2wFJokT9tGufRfJZoHXUbZ27_keQ303bpSBb2ovAEmrVzLuZuvr3uR8aWMx9vNzfN2u2djjO9-BWdiIDuzoAb59qiRlFMZAycET8z3Io41IAsLRbyhhb6-sg4hftDkt8GN7VvD8Ffi-WTbNC9bOKdNgfeKpeyel82ArD4SggqxYKn2r2id0ORkK6J0_0aZy0x1WKbj0TzLPh3xmAZYcFKjY61DqGf7zzlR43_rfoFslVKN7GXEB9PyHxAUnJ4CKlXCXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انریکه ریکلمه نامزد انتخابات رئال مادرید: دو بازیکن کلاس جهانی جذب کردم و اگه رئیس رئال مادرید بشم باهاشون قرارداد میبندم. ممکنه تو همین چند روز اسم‌شون روهم‌بگم. ریکلمه‌درادامه پرز رو به مناظره دعوت کرد ال موندو نوشته پرز قبول نمیکنه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/22341" target="_blank">📅 12:37 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22340">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QiQAxx5j1nI24tkDC_fwG1Leij0GlsY3gPjwEqqdtnQEijgSXhctcTVfLWnSsAVdXPcIXPbl-PAGcToiG30n0Kre3f4mS4dHDJ_T57p4x0p_7kwKGRyDeHgOSpJrIIQbdh_3_ogUwIvmIFvrBS20kBgrxP9FF51hgeCeDoE70MzDJLDaphnO7XNVJlId78EoKWDKe5uwAD73FrruMcHwpqakG84JlIh7tGWVwMnJfcdg_zTYNCSXE7fyD1P4_FCXdGjI4erjD65aAMpK9n4AhTRCFVUxktfs94r0OjuZRpk3Hb2r564D2UqSec9Nj42ahr4I1Vu25Ds2pMA7e6j9xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ مدیران باشگاه بارسلونا قصد دارند که برای‌جذب خولیان‌ آلوارز 25 ساله؛ فران تورس همراه با 70 میلیون یورو به اتلتیکو پیشنهاد بدهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.3K · <a href="https://t.me/persiana_Soccer/22340" target="_blank">📅 12:23 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22339">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ii9M99tcgCvCP3sjbdWVTfRns1KDNFVfzZyW6g396y1_8kDr7tmbgx5PPpxJuz-qMw-vzMczMEBo-nNKcFp12Et_t5qNsG2SHc5v6BuwR8V4rUeL6mgBz-n9rNNDD8W5B7cS0lk1PgbBSeINM0zZF5UeUaexOlck32Ntjzsrr_MK1m0ZArG3pEFvFTzuxB21h5qPgxLx82OZzE9VuCY0f9TWpSctivJsKfq1M1EVdNs5AXasGLur4PXF8T-xyitWNgJi53jGBmUVxVtB7wYKmYzIKNOnwheTEpq2tYdM8LZQoKF-3BZjlR5OqFtaD_I86PeBnHGnpCh2eB_tFCwUXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
آنتونیو رودیگر مدافع میانی رئال مادرید به دلیل مصدومیت دراردوی تیم‌ملی‌آلمان در فیفادی از ناحیه ران پای چپ 3 ماه دور از میادین خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/22339" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22338">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UHsg7tY1M05KAnbVv_iWdg_d7iEGVN2rafzpVNe5uqHHOgBSbHUBP7WQ7YR7UNfYHNkYRDWOQM8G7CvYIZCyPCnDQZYjKYiVoSCARTF0fGDRQjMCyiB7GKlTELRWJTqnJqSr1KA2Uezp4SRIuesajFkaVzI4tNLFf9rUVJM1wQd8BTJ4BE4a64yGUCjop3SJaJmVNp8nWVsBfW6PtISstfR4DwlfizAlq4c6qB9X5FrNuiHIeMdNJG2tM8AWu-dc9c-FNjJdtB1bubOiHwhPbbQUVYa1VSwQUp6tx-QSN4kyEe-bMpkcAvWlDvCirGbwc1no4ttSbgqee_XW-hIUtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی برزیل؛ مصدومیت نیمار جونیور کاپیتان سلسائو جزئی است و او قطعا به رقابت های جام جهانی 2026 خواهد رسید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22338" target="_blank">📅 10:19 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=jgUg9Xw7-BQhMe6z36x343ruB9pOAV0dPmU-a7uCJCOAN3Cg3v6a6P4dKAckZEWNTYsRVTyfi-i1poosIe339qWARTxd_3KtLlYGuusQgFhedRLKhmdtwz2bEXIqm55nneJy6jnMLiFIPqQAsN2-H382ORzCuwd2_V8KFAi-XQIB9ATGmERK5YnYVKKlmo-NsFDZD0Ifc1brncPBpSquGIpwhwZ_mMWOEouSmdPj5C7JshB2IHkxKYkxSKJ5kH_zXtslt3LUATy-1ALhu7RcuMSyKUuUCo7av9r53Mc77PYwMLofrLPPm7LAcx_aHwqax6NOIfM-A7EXKGXm3XH5iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561656d5b3.mp4?token=jgUg9Xw7-BQhMe6z36x343ruB9pOAV0dPmU-a7uCJCOAN3Cg3v6a6P4dKAckZEWNTYsRVTyfi-i1poosIe339qWARTxd_3KtLlYGuusQgFhedRLKhmdtwz2bEXIqm55nneJy6jnMLiFIPqQAsN2-H382ORzCuwd2_V8KFAi-XQIB9ATGmERK5YnYVKKlmo-NsFDZD0Ifc1brncPBpSquGIpwhwZ_mMWOEouSmdPj5C7JshB2IHkxKYkxSKJ5kH_zXtslt3LUATy-1ALhu7RcuMSyKUuUCo7av9r53Mc77PYwMLofrLPPm7LAcx_aHwqax6NOIfM-A7EXKGXm3XH5iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
ویدیویی‌از فوق‌ستاره‌هایی که در پایان این فصل رقابت های باشگاهی اروپا از تیم‌هاشون جدا شدند.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/persiana_Soccer/22336" target="_blank">📅 10:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22334">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DwIWdMsl0JoeNwOU-6JrSKBoSSTtZLV6IfqgqGhC0Vsp-WagUDgKc2oN9-mnVTZlzj1suR-eIJcdxp4riJBjkq05GQYUXI1ZaZ0v1NxjugTMtQ7v_HG6Gh-6dVJ3uwDke78XJOkT_5zDY_NzR-NryGtlt64NZ1z2u9X-Xtj-bzkk600Uiwt_MozXEzPmwZ0WKQepGF2jjNfpzhue2sOQyVZ98ovYyrMH9n9m4tt8Qs5if7KNnncdym09DeW4nyCsSSm3wMPn_u6dkGvlK7-hAgFmD-q5RfiWJKxYf0p4jsF3ec7Jzz79zjTCzAUHLolcZRwqDjwPrzOuKEPrZuYauA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dzx8fczVFXw3aQ2NOXRcAxaSvc7xIQBIJa1wJsBP1h2hdFPU0smMqjyqmO9uvJ0KpI_vFauL3BT2n5GaIzGW92TpcVDnGBC9gGU0i0VH3ZWbS8x0uRPnd2vm0WUZuAPu5XtDW-w93l7NVlVXrYctSGuWNYZpYmSHje0CRbWox8HnbI7ye5pkB-mxAzLw-ou_jyttF7G54Sy2abV8kAbPqSXq-DFWujo6qxAOCoCjRno3tbt5qLAzmsme3N72FIMv-qYfTIdOVK3ZRRINn9TOdGurtBpNDDqaDrb3wsw1APPPvRzVWNCWcJTizYxYLSBL_kmjQBRCzQG6vEg7mh3xcw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">#تکمیلی؛تموم‌سرمربیان‌حال‌حاضر فوتبال جهان که روزی شاگرد پپ گواردیولا در مستطیل سبز بودند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/22334" target="_blank">📅 09:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22333">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uzcJQyJgLg1FhlI3gcOqDaOM4AYviSHKfoV78PJbtbfEUfjAae3Sy2NSZo-hzwkYlQYnDfRnOTedqrlYxJyofTETNlGnf5-HiMJxGE3BPJEHv8PNzHvzx6jEBtm5IoSBhxXuVHYKkVennaShg7UXV9IhiTkEQKCw9o0ygQCXZ97Jmr2TwYz1tqPNKVgk9w8V1oah_WgEiFWW44yzkL3-dVe2lPyCGKGJSJtfe12pSSnjL83MZPEKCnxgqNKZ0hVLoTLhqeCGNrW2kc5p0ffL3tc1wOAJVQ3WRgjgMd7WqT1_wQtY_1HlsZUnNX3TpNNn7_hmVmIQYtOqlbJVN-4-rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی #اختصاصی_پرشیانا؛ نماینده محمد امین حزباوی امروزپیشنهادمالی‌مدنظر مدافع میانی سپاهان رو به مدیران باشگاه پرسپولیس ارائه کرده است. درصورت موافق با این پیشنهاد به احتمال فراوان حزباوی راهی پرسپولیس خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/persiana_Soccer/22333" target="_blank">📅 09:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDNMLRUmBc2gmyJ5yhKKRKOwV-bmfcb2ZrphMi7C6ID57kWRiF-Tjut8JdxYHDyRLqkzFWWlarka5APBA1D_xizOZSwlEG-DmJYL-e9Ax-_OCiQbKFeovOs6SXN0vil7Yn805Om96rRdDrkwZoA4ccd5bTKSfv1KsKEX4fSCIU5-l_MPYsQPYjOdlR7HF5UeOovX0vj5T8pFMvpqKK4vq2KLVQNcJiIJ2PruJrHcEJQDui3_d-NUbUhbz00cKuFlSmljEF6JcL_WYG8AwNDw48t5SGABVxtGdMX3iX1JJtRYy6iAjwabieNfW22SPyZYWkDFvigfviTHI-BQ8n9mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#تکمیلی؛ فوری از رسانه مارکا: خولیان آلوارز تمایل خود را برای جدایی از باشگاه اتلتیکو مادرید و پیوستن به بارسا نشون‌داده. اتلتیکو برای فروش ستاره آرژانتینی خود حدود 150M€ میخواهد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/22332" target="_blank">📅 09:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzPlpoRrsLe2TFHjRyK8VvFRn06qYAQhpQ6ptREI3n7LpOHpjSnwvtjSg49Tg16zyzl8IlKFcjqDLqOCUnR_BA32u9GyFrtYSjo1lXdZEZb-GIeYJQkMXSoJbEKA0660VnQdce_nK28UgCG6plFY0_Pw0zPhz-_irLubCpV2epI0w7onNqL8IaNb8toRo4AhFKw5kLYfZ5vdoDwaCRr7eLHnpLUmzhJNTwR9LpWi2nCsafI5rif6Rx1DEIs4Kg30BNJesKPzZ94VclBdQWmFNv90Tb_jGePloQyGPPIOR5uXQLL5CPoxGjZA5DPtE-BsXMeg55L7nVb_DEPF10pJfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ رقابت‌ های جام جهانی؛ میروسلاو کلوز با 16 گل‌زده‌همچنان درصدر جدول.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31K · <a href="https://t.me/persiana_Soccer/22331" target="_blank">📅 09:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22330">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lp7JERQDDWKXBWqBrSTkbsS5mSNz6ztNFVlmf6eG-vOXA8xtI_LZLaMkLS0QQzE60O8tlTCACN1WQv0GeYB6AZrHCm2H8oXCAQXlglcB8GeW8Ref3sQP-UU3aBZyBCVSmjq2IIx6psrEfELv6X2GXsXshvekiKCJGr-bV_V53GqdEAnNn4I0ihRhvI6Jl4e2SQLZAq92fjz9nMWFaBBdIb9SCnQCvJ5TbIqPIZXja0kXjHp3fIQhwnks3gIThDBgm4KloZxcmmfT50WYR_dn7IHFySHpjNGLj-3xR5AjHp8F9Loa3JEkADS1ezDI1fhl7NLRhc19nCpeKQop1mkZPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
طبق‌شنیده‌های‌پرشیاناازتبریز؛
مدیران تراکتور با علی نعمتی مدافع‌سابق‌فولاد و پرسپولیس برای عقد قراردادی دو ساله به توافق رسیده اند و بعد از جام جهانی قراردادش رو با پرشورها امضا خواهد کرد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.5K · <a href="https://t.me/persiana_Soccer/22330" target="_blank">📅 02:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22329">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fKw04saTBqkGTbfmOliJZgOmR6p3Kb7-wP4CdQXHEYy8LB6RlPY9yg1kSy8QeGEROdGbgyxkgZ9aH_gX7EWmJgwA-FHq9rzbfCf0XQflv0_Wtdm-nZJqsSzBO48xqaj63CIlQPEKOnZv4Ol96RdukVOsQ8hTguM-sSu3B3bGWDErRmr4C69JdFFEyI_hcDHi8x30DZjk5q_8nStALJu1Vc6mIwTdjazQ2DMvVbBDKH4QmxmF3Z70cPnwNJnlW4ds_2RHDVWiB0S-tMRw5qe0E11l3rViilERHHxLXkcvVfQB3ZKRuWULPBNzgFUJ8xB1tvkN8V83RAYfNg9mHU1pww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/persiana_Soccer/22329" target="_blank">📅 02:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22328">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/339ed28585.mp4?token=K-Vuy1vKEf0g3oxtfSsJDAu3eFlCxn6RCxCxVH7b3vGbQXBeKD4zEgM32Xu6_MJgcMTVLoLjWvdRiKpNKdjc-X8P58n_Fe39I00H-xG_8N3pbNmLKtSOHoYLPGkBAZbWh45aQ7Cuzy_X8dUcMTZGaLUs60LDa6Z7E1R305W8htoNEWES1rE8eCuqa06ZdCP0ku0k52iM5t1-ro3sry-fzlXr7XVy9FT9IkvdRyStsr42v6H3yH_OZhFDtGbY4Ruq1BlwpHMM2SxYtFg1N2koQYrCBaP7bvsJH9waZDE68lC65fAxU5VtPLvK_7-oZKCZuiyaaut2ix4ycK5-XiwcBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/339ed28585.mp4?token=K-Vuy1vKEf0g3oxtfSsJDAu3eFlCxn6RCxCxVH7b3vGbQXBeKD4zEgM32Xu6_MJgcMTVLoLjWvdRiKpNKdjc-X8P58n_Fe39I00H-xG_8N3pbNmLKtSOHoYLPGkBAZbWh45aQ7Cuzy_X8dUcMTZGaLUs60LDa6Z7E1R305W8htoNEWES1rE8eCuqa06ZdCP0ku0k52iM5t1-ro3sry-fzlXr7XVy9FT9IkvdRyStsr42v6H3yH_OZhFDtGbY4Ruq1BlwpHMM2SxYtFg1N2koQYrCBaP7bvsJH9waZDE68lC65fAxU5VtPLvK_7-oZKCZuiyaaut2ix4ycK5-XiwcBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طولانیترین‌وعجیبترین‌قطعی‌اینترنت‌بین‌الملل تاریخ جهان بالاخره بعد از گذشت سه ماه به پایان رسید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22328" target="_blank">📅 01:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22327">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Baf14DlfoKZeF43PqeFxjzF92nVp2cdExOvfqfNIzXSejelkXWupw7aZIEIkna1JFFXj05Iiiwn6BWY5favvO1NQM6Y9S-Bm2S7voqIOVYCl2u7n5WjhAl-GjoVKx-OgSlzlVyVQqmfC8imwyuw4zSDL2jvP-apwrWPBx7YY3B8OTe0mzvTAHFZvWY_q9md0IiqbRtZeG04CL2VvQN67NnNgF-ViwI4CYce3Y3btoffmAlTe3RAr0WUXjj1T5nV_VNF8vRYYhF5GV6u8WnmUIV2E_ECgWJKDgJntJRfNGuWSn4M5v52e4OhJ9B9rOEQxj5z88Zf1XcIzeh3Ic9KFrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ سران‌باشگاه آث میلان قصد دارند که ژاوی هرناندز رو بعنوان سرمربی جدید روسونری انتخاب کنند و مذاکرات بین طرفین آغاز شده است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22327" target="_blank">📅 00:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22326">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Erpeb1d6WdBrO9j1HE_AM7A_08KBuPC0e-10skrsCCn3mQTp6YahvTsZyIF91H3k4XZznTftqpT8_AA4hCOLyHrMzQzXwVFtsePVovVMo2fFRWtqR4R2d_bTims8CIYiOorCfbhV6R9txkXJBeq_upQ674wWcsxn2-_Q_pAaEL3KBOgrpUOUKyESd5jyyupvMsNpzIKIyoXOau14SfhMDekjuArqpyUZgnm5kbQvb-QntRT2CnYAswwDiEbfHC45TMLYSa95zJWvWgM4g3hzES5qH1aTIVITlg2AjjLSi80sA_aWSGYJo26_RMXBB0KAD92yOMx1V3Z1EahZ-ZcGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق‌اخباردریافتی رسانه پرشیانا؛ باشگاه استقلال از طریق یک وکیل ایتالیایی مکاتبات خود را با فیفا برای بازکردن قطعی‌پنجره نقل‌وانتقالاتی آبی‌ها در تابستون آغاز کرده است. برخلاف‌پنجره قبلی احتمال باز شدن پنجره آبی پوشان در تابستون بسیار زیاد است.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.2K · <a href="https://t.me/persiana_Soccer/22326" target="_blank">📅 00:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22325">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=kO6Rbg_CigGJu385cobWp-eSH31TqHhhoKi9d8FT3YDxlPYMojbiYeRTL2Wy3iaJl4xThqpSi_YxTy2W46Haf_Ct3WhFC_hvsvluQPQrczDh8Wtu1ggDrN0BajhRycyFVC6qZZ8Zk0tNouK654Ri-fjlcrrbauMYfb6N7WGWS5vV0qop6eLIMIBGyWRe_gyrsWWZgt-wSeDTIRgoG43UXhEaKJUF1RWh4CkV3WAsX_hfx8vERldIKQX94fhvS4ixumAokIPD5Rk4qfaC-k9RozW9VaGfn3QEkfOxoxZYpjVyLACA2e4SuE3rUUplNVH7VyqWpbGIqMEs-wXiP5mBmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/437e19a5b8.mp4?token=kO6Rbg_CigGJu385cobWp-eSH31TqHhhoKi9d8FT3YDxlPYMojbiYeRTL2Wy3iaJl4xThqpSi_YxTy2W46Haf_Ct3WhFC_hvsvluQPQrczDh8Wtu1ggDrN0BajhRycyFVC6qZZ8Zk0tNouK654Ri-fjlcrrbauMYfb6N7WGWS5vV0qop6eLIMIBGyWRe_gyrsWWZgt-wSeDTIRgoG43UXhEaKJUF1RWh4CkV3WAsX_hfx8vERldIKQX94fhvS4ixumAokIPD5Rk4qfaC-k9RozW9VaGfn3QEkfOxoxZYpjVyLACA2e4SuE3rUUplNVH7VyqWpbGIqMEs-wXiP5mBmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
گلزنی فوق العاده تماشایی و دیدنی پسر لیونل مسی از روی ضربه کاشته و یک خوشحالی خاص
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22325" target="_blank">📅 00:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22324">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/STXuEyQZ0igWOP7-Dd7DgjcBR2QsK9Wok0p67Iy6nvrvXz8TzahyLqo9sgjCist7LuCSyqA5tHvYA05OJWDzNMODczfrCtKH0wfgQfnbJ9Dr_o4eQgB_mwnetklvvX4IQQzLR8CpMPPDDWEn6399tvhwz8xKCS4w_g6nwedVejt9xiV6DLY0l739GaPHx5YETFADrk7za9r-wKp1jCopOM227Asbz0IRZ8CfROmeJDtyqUjFEwHeiAKXKdD_fw_F1vZEYwLaWt5gHMi72Svu0lNUsVHiIZ5yUIoyb77Huf58AI5v8kbMDkXDfsLXmz9X9eCL_RylnLvtWmhjdQ5vzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
#فوری؛ باتاییدیه رئیس‌مجلس و رئیس جمهور؛ اینترنت بین الملل مردم ایران بعد از 80 روز تا پایان همین هفته رسما وصل خواهد شد و نت به روال قبل برمیگرده. ایشالا هرچی زودتر همه 70 80 هزار نفری که همشون‌جز خانواده‌واقعی‌خودم‌هستن آنلاین بشن اخبار نقل و انتقالاتی…</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22324" target="_blank">📅 23:10 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22323">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZNtUJtTNgXJoh9quaPDYNfDaS2u4sV6kyeeRMi-J1TJblm2-OP58d7HVa5-5IKTkGcKk7jGPNQ2X3o7kSOCJFIwCxWAmz0Tock3BzsAqByNo1WpmYGUHmFHoYxHyPNg3VRTwWsOKKxqi-pDf7Q9Jb8_w1DCwc4OZlU6BC9ujzr5D3JsE6IwR_RjllxE4dh-f2oBwMiUxulUmcg982TFW9q-aUyTarA0FwjX6ziOeT1vjmXGO_OxGGvEa3OLqLa8CmFB7bljQynvfSQI-OkXL1J60jkefOicr5nKKF1GhbHNP4N83zTWobKd5BYYgofutghbnJrMUwHdOaek64AHUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/persiana_Soccer/22323" target="_blank">📅 19:05 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22322">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RNbyaCgJl5mlw6ExEAJ-ZI3zqjvfDtsAZ6Nauevuno6BzV_kk2WORsbPyqNA5ApUlmQdVcKEhILkei7YIOIZYKj6iKsrF7laPCBi-FKISPPyCOyvgOygo9MpP6xYVA69XIeuNg7BeCOBwM1i0KHNgrHlofPIZze0rn16wm3ezjSFS-IFU0gQDPTiWpd8fHvZREtXpmA4nIvaXj8iP5bGy4oCFWE1jZil87Z8hKvLLFimbXXlwjRgfGJVMfvDdULtxoj8hal46jq1I6LSunuQeFRt0yNbGQOqcxz8un8CxNe3eWR2XRQoQzjPerZJaCQwvQKbyQqdJ5XMbe0tpsZzUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معاون وزارت ارتباطات: در پی دستور پزشکیان برای‌بازگشایی‌اینترنت تادقایقی‌دیگر فرآیند بازگشایی اینترنت‌بین‌الملل‌رسما آغاز و تا نهایت24ساعت آینده دسترسی مردم به اینترنت به طور کامل آزاد میشه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/22322" target="_blank">📅 16:48 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22321">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUf4lBDhHQuwVrqWQGvwypmQa6YXZW-_xCywffzxIBq0OQ1JFpYPq6YZ6Nbf_Ku2c5NkrDCDhKuSUHPRXInD-PxYqDeAK9YKhoM5pmXr91YLK03YNiRrctYbDtbQlOIrD1mBcG1IWSlcbMY-6lCsTD06eeekwnF1C-vc2YdWT0P_kMUDL2KoCtBz4JMVdWzA-2Ql_vGpi6LPkqjsOsBOXtJFU5BAiFdixSe6h46rCanrvkrTLzoztCjdr7asEzDEp1oy9EOcEnCNaTTKruYCv8Uo6h3hxXMKExca0G0gLwgGmEZ9Ue9UuxbsDVsb_AKBtBjzL8DQ61rZqTRiKU7fkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#تکمیلی؛ بعد از ناکامی تلخ در گرفتن سهمیه UCL؛ ماسیمیلیانو آلگری از هدایت باشگاه آث میلان برکنار شد. اولش خوب شروع کرد ولی بد تمومش کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/persiana_Soccer/22321" target="_blank">📅 16:45 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22320">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2231444b22.mp4?token=eOJ4-2LIueXu1TnacL0JBN9iAJjmmVD9n5DFI71fUENuo3yJDHGlb3_9rb3CxQpA6Yw3BzKvu9pmL93_FEfuzlgERtV1057HdMddriEVUX9TOGC0crcgyk1N7i2JKjyDD4YbYpn5GkP0mG0ewcW_O40kBEzJA0e9FJe7FkuLdXXhKC1mSnsJUvuaMxidVcyjEf6Y0hIMZzam7TFsiudPHNG6pCM3KN5HsDx0NQAe6oxsCTl9Z_Jz4AiqTyfAv81SWmUlbuk7gTJremEE6J2-cO_elHzuo_39C-k1xS1UpSiWIYjt9WaC_4D1zE9ASn0m7FqTYBetjuxld5EvADeRhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2231444b22.mp4?token=eOJ4-2LIueXu1TnacL0JBN9iAJjmmVD9n5DFI71fUENuo3yJDHGlb3_9rb3CxQpA6Yw3BzKvu9pmL93_FEfuzlgERtV1057HdMddriEVUX9TOGC0crcgyk1N7i2JKjyDD4YbYpn5GkP0mG0ewcW_O40kBEzJA0e9FJe7FkuLdXXhKC1mSnsJUvuaMxidVcyjEf6Y0hIMZzam7TFsiudPHNG6pCM3KN5HsDx0NQAe6oxsCTl9Z_Jz4AiqTyfAv81SWmUlbuk7gTJremEE6J2-cO_elHzuo_39C-k1xS1UpSiWIYjt9WaC_4D1zE9ASn0m7FqTYBetjuxld5EvADeRhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
#فکت؛ آرسنالِ آرتتا جاودانه شد‌. آرسنال در فصل 26-2025، اولین تیم تاریخ لیگ برتر انگلیس لقب گرفت که فصل را بدون دریافت کارت قرمز و دادن پنالتی به رقبای خود به پایان می‌رساند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/22320" target="_blank">📅 15:22 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22319">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcU1Ln01xSfLcoGmNUhjNIX6_oasXYp92WNBJxXRiiQShcDEclAW_IPdewwpS5AExn6JJu1m5CY3E7kAZLMocUM9VTqBSMiXF58JZZB8GS4k0CpU_hEIkJVqjPMcsOlZ1XnTW1VLopLLu3Aq2L4PWREu6nZwcEayssLNGqboz7aPpytDNkPdx2-LbADPz7xZG96XHNNUHMTVY6KQrLoOig1Rw_cZJ1KKY26zHMf_oBbjvwZMMyqu3q9PBlM111uW17SqCkSGnw7aMJTUbA0OIertTK-VN9u8-TJRHfvb29ILV8fTJ0tJqgc1olkBJD7zxfjC2WvhZbPcApwxgPnR7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئال‌مادرید قراربود امروز رسما ژوزه مورینیو رو به عنوان‌سرمربی‌جدید خودش اعلام کنه ولی انریکه ریکلمه رقیب انتخاباتی پرز برای ریاست باشگاه خبر داده که اگه من بیام ژوزه‌کنسله فعلادست نگه دارید.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/persiana_Soccer/22319" target="_blank">📅 13:33 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22318">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RotXVh15S_O5UTKYbPBqmeJgo22REjRYXF4n9JHG5d-J5S5HOfLcsYikQDWiElhMb4o3IHmSfafPo1qE4I0ZJQXMAdeUMGDT5XOjaT95trpN8NDao_Rvb1btNHyiCPktVcGdz2IpKSlAAJSX1Abs9SV9wqEgOAfksVKxaGFRATQCQm84_fPTg3H5CyAXtqKdATyBDy4S635e0EJxJ01QAxnOqheXHAomCvBRKHh9h9xorVzW0z_n-CnAwvDk_fD0efISd4VId-fPJ-25WhXIlo9i1DfReuAtxxUAlrmx1Vfz24HV6uUIgVlmjPB-kyn_iFwR2krbj9_f_WTwiIBezA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری؛مصاحبه‌جدیدپزشکیان:اینترنت مردم ایران تا ساعت آینده به روال قبل خود باز خواهد گشت.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/22318" target="_blank">📅 13:18 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22317">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gq0qVosREZd0ZfiLq2z0J778AwFwTXwqFKiRQ4elBEq0iIo5jLomid3AFYhKgVIWob1I-N_NyIb5UmN4yesPRGaVQL2Bpmk7EiHlOQYoZqwHBCDL1XdH6CaW-uwuFicUOQvDL3NK8knPSOqNE3FmtsiUkr5cc4eQowmrBilHCEkjW4bHhIbNnaJHHULW38ThtRiqoCQidC9xVMPKgfo9s9i9rHsfi0cwiqFmYPMatRhMDJyXxoEYfeEIZbVAuDk-4D5JY6fpZA5Q_xPxCQW-aZ5kZf7Mv69vGAOy58iDDK7ecSzkUKkYC_C5ZSsCNg_T9HT8wYjxgCMFMlVHo6lS2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه کامل‌های مسابقات شاگردان روبرتو پیاتزا ایتالیایی در رقابت های لیگ ملت‌های والیبال.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/persiana_Soccer/22317" target="_blank">📅 13:09 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22316">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t8gV_T6pbRCsok2cEbKVY75d2NndJcrKUmp0gcHdTn_7exUjChlLxeYnGg-opPxNLyg1a8xvi4VgyGQqdwlF7L87vd2wEYPwKT3tqDrffkX52G6nXUqJPbxXsYWuOLDngk_1cVdrqco5v_xrSradyWTuR0EFEoHM6uoYJFH_4ShTEbWtXf8KeK53Kbag7K_stgQdfTaBcTsshu9iOkW0rYtLdG7tLAOjpUGe5Y7VhhJeBXHjd0ejJf1PfYXz9pgsq4MNO8UyZYOKphATXmalgrBAyWtpToCq8Jmqy6X0IPNGkodpD6-JgmFgMCcKv7luuRrFRqMLDDn1rrzS6G-5eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇯🇵
شهاب زاهدی که علاقه زیادی به بازگشت به پرسپولیس داشت بعد از عدم تمایل مدیریت سرخ ها به‌جذبش‌قراردادش روبا آویسپا فوکوئوکا تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/22316" target="_blank">📅 13:01 · 05 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-22315">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KiFr_sSyGq0H7pQP4pQFkCn1NguIPZ1V9d9f8MqKhU5AIhRsWMYe6TcgMINEv-_aOokBFUkivZhlXsutFUcSKWcNKShMz3N10kyto3z1xdgsXoiscWeaSpSpwp2awGoaRinQc38ve1bKmy1sQzmK7toYPMSXxvd3wwdDdxc5hcV8ACDRrEtYmnGu08uyKYf7rFV0ksP5Gqqo8Vn8BJidbXRXNK7ifhnYSBsJEuBqn__YE48S_57Aysa1aMTx2hCYWYb2FHGs5mCePhdZ0IcJUAmynMP3JLwcbLLeQpE6B4dnmloLQpq_o9f12m74unH89oXL42VWJJKK0Bxjd9tS3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام کادر پزشکی تیم ملی آرژانتین
؛ لئو مسی که درمسابقه‌اخیر اینترمیامی دچار مصدومیت جزئی شد مشکلی برای جام جهانی 2026 نخواهد داشت.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/persiana_Soccer/22315" target="_blank">📅 09:53 · 05 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
