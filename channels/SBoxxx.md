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
<img src="https://cdn4.telesco.pe/file/awpxB1YuXrfHQbfvuTrHGA2Oxpcicdnb0s9Tzx3wmc4-QM2H0ibOj9FrCI77eHO_TsP7pYQBGp8xCG3-uArCkoCNXTRDT41MTsIlmeTj6kq6wWVRvMPQg5XweoLJ60EhEuR8PluoZYwVsZ_JIhD817wWlKtsG6_CmUO1wGPMSIwO8AxW8CgIin5N6_BovNBjT6LNaD-xeakrp5x3BFzJ3e4HQPetC98gMayklYwW6esLDIKV5FyBdqlO047AHWnMzFmrUG6eJXwuIM1lx8_U8X9A1GL5EYUTDhFGrhZnfn7lPe0oLDyRNqSlaKLu3ALNhK28GoUSMMvfgDt8Io-LRw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.8K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 15:07:06</div>
<hr>

<div class="tg-post" id="msg-20805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">وزیر امور مالی اسرائیل، سموتریچ:   حکومت ایران در طول جنگ سقوط نخواهد کرد.  مردم عادی زمانی که هواپیماهای اسرائیلی و آمریکایی در آسمان بودند، به خیابان‌ها هجوم نمی‌آوردند. آن‌ها نمی‌توانستند طوری به نظر برسند که به دشمن می‌پیوندند.  تأکید باید بر این باشد:…</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/SBoxxx/20805" target="_blank">📅 13:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 27</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20804" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 26
جمعه 11 سپتامبر  2026</div>
<div class="tg-footer">👁️ 2.17K · <a href="https://t.me/SBoxxx/20804" target="_blank">📅 13:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qffdl_VNT5dnH07sWWlFgBOrGwdbWhql33aFQ2hbS9hwcoLUNE3Qx6fmCS1m16rVM0MPDlG4oVn6J7TaHWqoCB9mjObBJp4Z4dOGtn9cNGezMF_RymDb8FBzAREGjxN2lpruSCC4MoJDVZiyvL_EdCUGp6j9HHDtY-6SmvnGKibzAgkLqu2GPNDYXF32ZirbgUfXDCxubZNfb-qWXs97Co0nf_n9tpMta2k2cDnw2xwmdmc1jJVwAAkSMA8mSAS9J1knKZmatKINbLV49ijLQ7cQIQ9YHCrpQz4m_HM2vc-YdQ3JGoOtGvBxzR2BLKog-pxEzazsGklUoCAsh5pyGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/SBoxxx/20803" target="_blank">📅 12:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">پس از انتشار خبری در فایننشال تایمز مبنی بر برنامه ریزی دیدار عراقچی با وزرای خارجه کشورهای عربی خلیج فارس و مذاکره درباره موارد بین ایران و این کشورها قیمت نفت کاهش یافت</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/20802" target="_blank">📅 12:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/SBoxxx/20801" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">وزیر مالی فرانسه، لسکیور: هزینه‌های مربوط به بازپرداخت بدهی‌ها در سال جاری، 65 میلیارد یورو پیش‌بینی می‌شود، که این رقم 4.5 میلیارد یورو بیشتر از میزان پیش‌بینی‌شده به دلیل بحران‌های ژئوپلیتیکی است.</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/SBoxxx/20800" target="_blank">📅 12:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4NGeCWF4qttsqnWGozEbJmBq-YcWe2pJ17a2ZPYK7-IXg0XmHsgXQ0HzItDD4_e3tePjNMMZjOvZAbuk2C0D6Yt9Sg-whsR0db-pgAvqnhDfHGe2mqCq_xAD6cB4SYclcX0omwMr2PFdrY3mkGsCzcowsc56OmKT0RDX_6DqGO0mtesNSVB8XLf1IG4jhfwM7VGp-TevXmI0j_DWTr-XBEBcel3jiWteimmVnpZbm5wQFUuIRj5Q-O3QvzHBQmyOiU3joFttBivfgrDIuC7dHT2HGALhChRax7huIC24gQuIWVVjb5M8_BMhu6G7sCXeEmngx5UtqXYgwac-XBtKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز هم در سطح بالایی قرار دارد.
نظر به رشد بامدادی طلا تا کنون، فروش با تارگت 4320 توصیه می شود.</div>
<div class="tg-footer">👁️ 3.22K · <a href="https://t.me/SBoxxx/20799" target="_blank">📅 11:52 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3KYn-38m_rpNU3q768ml-SLGWXXcraVQs7Z3PmGPaaZyqb1FTS6gC1yVz82aOlKxh089yF5xY1iwY37ihQDSFMhnDkloO-qUQT03p3s61lUzDDOPIyNPB2xZSo9aWSzW8SXUZa22YMVvt3e-5LwL3LDTZEFN-qVX6OlxlkF_pT80zIt9i-fWPOroFYLj5-F_g0Nm5dC2ft5OJVhmVtVbbL8SSwy-BP-Wwh_qfCF2JhCJNs-98aFK6WV1HrYyq_aETAsrIildscRvcScw9ZoJ4zNY-JBiKCn6weyzIuEaoAftn71RSYjnv0rSUJb723eFPd6LYdSPC49Vz2lgF2o1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جهش بهای نفت و تاثیر آن روی تورم تولیدکننده در آمریکا
جهش قیمت انرژی، به‌ویژه نفت، تورم تولیدکننده آمریکا را در اوت بالا برد و
فشارهای قیمتی را دوباره پررنگ کرد.
حالا بازار منتظر CPI است تا مشخص شود این شوک انرژی موقتی است یا می‌تواند مسیر سیاست پولی و قیمت طلا را تغییر دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 3.19K · <a href="https://t.me/SBoxxx/20798" target="_blank">📅 11:42 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">گویا امروز حوثی ها این خط لوله را هم در 6 نقطه هدف قرار داده اند!  با ادامه این وضعیت یعنی عربستان حتی از مسیرهای جایگزینی که طراحی کرده بود نیز نمی تواند نفت صادر کند!  به نظرم تشدید تنشی بسیار با اهمیت است و از دلایل جهش بی سابقه نفت در روز گذشته</div>
<div class="tg-footer">👁️ 3.67K · <a href="https://t.me/SBoxxx/20797" target="_blank">📅 10:50 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi9-ik5qLBBztIq6IOz9qa_U5XYPtUmqorcOnVXNZYAXnzralAdEeHo4aeGIU0Y6XIrnLw4QCamDVHPi1Qci2qdFoIVpIMHusGyfchoIYHk_etVdEgCNSIB3nEbYJgI-tSq1ePLyE-Q_BtNzEO-jNGamPGZpFrnb0b5sHUD-bWLGLf8jFpA6eKfwEbsc3PqN4BVVP2QvgHMd4fw773l7bfQLRLxjasH80j8je26aG7Dd3A1twu709-wD-xpn29fPG-3gv8w2EhFEctqCi6k-54qi_NjAS6Qvnfa-ptukSjaZQh1lyZPaDSExI7U4R3gXlCqn-uOLn3zR3wnwAot_ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای درک حجم و‌ عمق بی لیاقتی و بی عرضگی ارتش پفکی سعودی کافی است به این عکس یادگاری جنگجویان حوثی که پس از تصرف بندر راهبردی مخا گرفته شده نگاه کنید!</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/SBoxxx/20796" target="_blank">📅 10:47 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">حقوق ثابت نماینده‌های مجلس ۵۰درصد افزایش یافت و مزایای جانبی نیز افزایش پیدا کرد</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20795" target="_blank">📅 01:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خط لوله شرق—غرب عربستان به ینبع برای خود سعودیها فعال است و گویا عراقی ها و کویتی ها هم می خواهند یک خط لوله از بصره به این خط متصل کنند</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20794" target="_blank">📅 00:56 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20792">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8aLHLSoiBGVrgyTkvCRew_gph3STi6rruqlT61W911L-XKQeNcQ_jeGoeDHKYfpEmX9kuh4VhO8snQ5p9rZM34G9oNh79tw8L4YW2gWfAhrqA2fFPd2eY7oVZsHUU83V75KGia6b5QFo-idjmgpkSKFPnlJ0BZuDyoR2vchgoFoX1-QsM374O6F73SWjA77ax6p66OLbcY_scplb8TbeNmb8EgQ82jX48SgXdmNVSN78XkPplmC80KYTrfiAnFlgVah-Huy3wtfxlxybO6DE7SE9rrL8AhDngda41bTiEItDnnU3n9xZkI8VoeQ6qkDeFJxdQFxExi_vcH3pwgrNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20792" target="_blank">📅 00:14 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20791">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">علی الطاهر!</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20791" target="_blank">📅 00:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20790">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mleMDzSiIdxec5syexpLGqKyV2seDpnLB3Fe96laCqUz2XoeG8TSCIb1va_TbD6Z1DVbxp_bmdY1XYuhizB81qGCkQDpFWn73tdWoQBDZbQxBwGBKkZhoD6nbDLbGtkobl2YJFNIDVbwpiuVyJNE6zIpRScYYqKoapH0h-0HjqCOB4ApAi_jdtNZ_5-gT-SCMvuZCTEgpWOnpHBc9FVabee3YjpIjR7AEUpJODiKlvBwy_c7c8d7pFWfSwyM68HqtZFXB8tNLmZxKQSCZkN9K3evGcj6aI6jm8NXRRPjcy1zqIyEA1rvA7z_KLnUitgaO_dDkeEN1OQnyLaR6WLeoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکستن انحصار چین.pdf</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/20790" target="_blank">📅 23:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20789">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">شکستن انحصار چین.pdf</div>
  <div class="tg-doc-extra">186.6 KB</div>
</div>
<a href="https://t.me/SBoxxx/20789" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">آیا چین راه اوپک را می‌رود؟!  در دهه 1970، زمانی که کشورهای اوپک در واکنش به فشارهای ژئوپلیتیکی بر سر حمایت از اسرائیل، تولید و صادرات نفت خود را محدود کردند، کمبود عرضه نفت منجر به فشارهای تورمی شدید در اقتصادهای غربی شد. با این حال، این شوک عرضه، نوآوری…</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20789" target="_blank">📅 23:35 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20788">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftxoz17Xt_-qR_2q7ixx764kW6wfxGENFLFQ6p94ddKNtKmUQsEfkSn72TgjEhw86UmqpbOvcZkkyxJISHvz41l0AhMm0wciAJaoaZ5iSlQYqoxzULa6gKsWW-NLkYVQs7WRGN8nYcIqs30WtnaNsZluOHWtALbiaRiKMNNvhVu7C8VkCWCUwghdzMczY6nbfSZejP03YPbWL-b0ELZPEb5Rm9p0Wwtj_h-57ySMpLThjppnXxGEt8oy34ppwNZl5yriQq13SbqK_XnMYRp1pHGGPSNrfySRw1mkORvuY3hbreLY3lDdtLS3tPEtX4a4EsptwgViIlGW_O5YTcpGCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:  با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.  این زیرساخت‌ها،…</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20788" target="_blank">📅 22:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20787">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اسراییل کاتز وزیر دفاع اسراییل:
با توجه به دستور نخست‌وزیر و دستورات من، ارتش اسرائیل هم‌اکنون زیرساخت‌های زیرزمینی سازمان تروریستی حزب‌الله را در منطقه "علی طاهر" نابود کرده است و بدین ترتیب، ایجاد منطقه امن در جنوب لبنان تکمیل شده است.
این زیرساخت‌ها، یک شبکه تروریستی استراتژیک است که طی دو دهه گذشته، با بودجه و برنامه‌ریزی ایران ساخته شده است. این زیرساخت‌ها و مقرها در منطقه "علی طاهر" قرار داشتند و قرار بود به عنوان پایگاهی برای اشغال جلجول و کنترل و تیراندازی به سمت شهرهای "متولا" و "کریات شمعونه" عمل کنند. نابودی آن‌ها، به معنای تکمیل کنترل عملیاتی در منطقه "علی طاهر" است، هم از سطح زمین و هم از زیر زمین.
نیروهای ارتش اسرائیل برای دفاع از منطقه و جلوگیری از بازگشت دشمن به این منطقه، آماده هستند.
ارتش اسرائیل در این منطقه امن باقی خواهد ماند، به نابودی زیرساخت‌های تروریستی ادامه خواهد داد و از هرگونه تلاش سازمان تروریستی حزب‌الله برای استقرار مجدد و بازسازی توانایی‌های خود، جلوگیری خواهد کرد.
دولت اسرائیل به حفاظت از شهرها و مناطق شمالی از داخل لبنان ادامه خواهد داد و هرگونه تلاش برای آسیب رساندن به شهروندان و نیروهای ما، با قاطعیت پاسخ داده خواهد شد.</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/SBoxxx/20787" target="_blank">📅 21:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20786">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">وال استریت ژورنال :
ایران در حال ازسرگیری تولید محدود موشک‌های بالستیک در زیرزمین است و پس از آنکه حملات ایالات متحده و اسرائیل به تأسیسات تولیدی آن آسیب رساند و محاصره دریایی واردات سوخت را محدود کرد، در حال مونتاژ سلاح‌ها از قطعات ذخیره‌شده است.
تولید همچنان به‌طور قابل‌توجهی پایین‌تر از سطح پیش از جنگ باقی مانده است، اما تهران هنوز یک زرادخانه قابل‌استفاده از موشک‌ها را در اختیار دارد و در حال ساخت تأسیسات جدید زیرزمینی است که برای محافظت از ظرفیت‌های تولید سلاح در برابر حملات آینده طراحی شده‌اند.</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20786" target="_blank">📅 21:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20785">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">موج ۳ از ۵ در حال آغاز است.</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/20785" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20784">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">نتانیاهو
:
توانمندی فوری ایران برای تولید بمب هسته‌ای را دو بار نابود کردیم و آن‌ها بار دیگر در حال تلاش هستند.</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/20784" target="_blank">📅 21:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20783">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">تنها دستاورد موشک پرانی های یمنی ها در دریای سرخ هم بدبخت تر شدن مصر بود و نیز برجسته شدن مسیر جایگزین ترانزیت دریایی از چین به روسیه</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/20783" target="_blank">📅 19:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20782">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8Yaplv5toYH2F2HMeEUJDeoM8Xn0-MDkW4pjOKO3R5__CblRXNKVsa8NbGkT0gtJVk8eW-Cr7_ARJp0hvVNMaWAMyWcZs7F4uXKJnbpnb4CB-TDyAg3JOTctZDSe6rbmAOziCsMMf45ark4pvO9Rz98w8IZhikb57P72ttAt1o7PG1jgpjGfJPvCjXFpgXZJMuryjMVSvLlQQjKcICSTyi4e4KXBxdesAy3xzqJhgVIkH6Nn5EYTa3X9V6toK8Z_BGLsFY1nsb5LR9XgFOofOGUNgHgDTNvV-62Egh6_m1leHJgQa-H06qDfs1C-Leohfyx0Ju7QBnzRAJGpW5qNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/SBoxxx/20782" target="_blank">📅 18:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20781">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عربستان سعودی به اوپک گزارش داد که تولید نفت این کشور ماه گذشته به دلیل اختلالات ایجاد شده توسط حوثی‌ها به ۶.۲۴ میلیون بشکه در روز کاهش یافته است که پایین‌ترین سطح از سال ۱۹۹۰ است.
احتمالاً این ماه، پس از حملات به جازان و ابها، این رقم حتی کمتر هم خواهد شد.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20781" target="_blank">📅 17:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20780">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">برخی اکانت های مربوط به جریانات تندرو، خبر از احتمال تسلیحاتی شدن برنامه هسته ای ایران بر اساس مواضع دبیر جدید شورای عالی امنیت ملی خبر می دهند</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20780" target="_blank">📅 17:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20779">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ذباب هم به تصرف حوثی ها درآمد و سلطه شان بر باب المندب تکمیل شد</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20779" target="_blank">📅 17:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20778">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZcQsvni6tRoGVwX8U4GWnLsBPPZOJGh4vQMyE62N9oRrlvU0uhxtVSjL558AhFs7M6iGnaaLah2Abpq0OJ98qWARYv7Jmc6wZ3g7Y7haRqIzfcvhaLJI_g7az7AGWlkAPPH0SrgivS1-RsC8ha9r83O2Zt4nVq75HfjAOOsdRu0qRRb2kG455Z7r6O3Fv90Eub1--73KJiMI9JGQ7dcnQbvo_lY4b08OlYepg1GEGE-xpYBZbdgj6F7XS88EhEeCTa_RyRyHQawuKoRFuLDsTs51baT0i9Q1dTL2AkQpRlSrlJTQre4bnK6NGgMWrWFSOEn7rdupcyrDSJ-0pofCbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به این ترتیب باب المندب هم بسته شد و ۱۲ درصد تجارت جهان زیر ساطور حوثی ها قرار گرفته است!</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/SBoxxx/20778" target="_blank">📅 17:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20777">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">نفت را دریابید پیش از آنکه نفت شما را دریابد!</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/SBoxxx/20777" target="_blank">📅 16:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20776">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اخبار اولیه حاکی از آن است که نیروهای مسلح حوثی(انصارالله) جزیره میون را در قلب تنگه باب‌المندب تصرف کرده‌اند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20776" target="_blank">📅 16:38 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20775">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">گویا طلا منتظر انتشار خوانش شاخص بود تا ۳۰۰ پیپ بریزد!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20775" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20774">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">در یمن شاهد فروپاشی نیروهای مورد حمایت عربستان هستیم.</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/20774" target="_blank">📅 15:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20773">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b73ZnyTS_DKEG6L79UMy9p_OKtYpEsoFlacYXg1pvIEyaBHdVMAH4Ke1G_zhu3LQ8aYdx2B-b2THkm0oK7ovoj-Vz9m6f_UShMgSWS7NCxx5KO6ztcN7RolfHh7yYFjON3GtocQT3WuuV5KZJfyao8Omg-L0mXRj70xIXlsZB0z3NeiH7fjqMzrTfJm5q4VjhrpO9egpNFYBxqBqCwCcud0p64pxBfg0sNPgeRpU15wuja7Zl0F8UD1dXBUV6oKIBS1gCQKQUFvBcQ_X3ndT9MdhohNr7zgb-ucyrqT6BtpmWb5XCx2kIKqKlKX437pqEQ3wKg96ALUNaXy2gSvoww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جزیره زُقَر هم به دست حوثی ها تصرف شد.  این جزیره در مسیر کشتیرانی بین‌المللی در جنوب دریای سرخ قرار دارد.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20773" target="_blank">📅 15:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20772">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.  نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20772" target="_blank">📅 14:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20771">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20771" target="_blank">📅 14:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20770">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S6Akvf-220lzwNpot3L_4GFjTGwYMYVhMmde5gTSoUvT-WdP2maKbOobNwzWInlS5YROXgkAhmBe-XOU2EYQ1aP48khlLptUVZX6S8Qpau72M83HT_MpFP9Tg4W8XuMbx9FrAT5SkDWaDKKOOChrjA4SCQ_b1-3eUnX_9XaQrWwQONQxaHgbfc1ZRFvYx3Oamgl2I5iSEKc84y8UprLNBRcaNMUNjxi1MUrSUvCTb-seLTXy-f0s1xLpqhC8FK6kVliipPEgYSrpF-ylcHKtqdJiQNJIdIDMdyWB9WJFLMSfPB6TSZ7AE4PFb0qfRCmnJu6WlMHVkXiLJ0B03cxvVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Ali SharifAzadeh – GeoMarkets - Podcast 26</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20770" target="_blank">📅 13:36 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20769">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">حوثی‌ها در یک پیشروی ساحلی سریع، حدود ۲۶۰۰ کیلومتر مربع از قلمرو در غرب یمن را به دست گرفته‌اند.  این پیشروی به سمت استان‌های غربی تعز و جنوبی الحدیده هدف داشت و گزارش‌ها حاکی از آن است که نیروهای دولتی یمن با حمایت عربستان سعودی در سراسر یک جبهه گسترده به…</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/20769" target="_blank">📅 13:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20768">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">GeoMarkets - Podcast 26</div>
  <div class="tg-doc-extra">Ali SharifAzadeh</div>
</div>
<a href="https://t.me/SBoxxx/20768" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">#پادکست_GeoMarkets
شماره — 25
پنجشنبه 10 سپتامبر  2026</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20768" target="_blank">📅 13:05 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بلومبرگ به نقل از منبع ایرانی:
ایران تا زمانی که اطمینان پیدا نکنند آمریکا در آینده برای حمله مجدد بیش از حد محتاط خواهد بود، جنگ را ادامه می‌دهد
دولت ترامپ تنها به تهدید و تشدید تنش پاسخ می‌دهد
تهران آماده ورود به جنگی شدیدتر است و اگر واشنگتن به تجاوزات خود ادامه دهد، حملات متقابل خود را تشدید خواهد کرد</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20767" target="_blank">📅 12:20 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bLzX-DX-I3M-S920Q2ZpcpVrYx8ggBOyU9JCDv2GycnYuLeWWHUEyEl0vxYd1zvuQpj4aeoCsz4LazL_tecoh5JqhA3fGaCzKLv18p_qySUtsHvKu32Z7uqOC3uPqqaQ0lwo-YKwYaAWOVBSJkr50pI3v3sIoT6uUr2_Rs8wXfoOyICPhKv1jOcYgxEOFerDFcBvXSoEurawWO6NPKGuQmuZGnII-_L9SYZXsmoKrT8vPexMGHAjORV4c1ONZrkWbBXW_nOAWnJDLrRd62f4K8iJ5jivOuIPrrGvm1ReCafefylQ5vfKopo2th6ipifsj3_-Uy1sXj3-2YjjwXbF-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20766" target="_blank">📅 12:17 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">راستی فرهنگستان برای shemale هیچ برابر پارسی پیشنهاد نداده یک چند میلیاردی بدهیم شارژ بشود استاد؟</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/SBoxxx/20765" target="_blank">📅 12:16 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">دارم حداد عادل را با شلوارک و پیراهن هاوایی و کلاه در پاتایا تصور میکنم!  اصلا آدم یک جوری می‌شود!</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20764" target="_blank">📅 12:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jeMepYYve6LVfi2M9BrCLzOG-o6tGEyLmCtkwlKtP6TlbBCww0Y-o8ojwkdHhJvxHYzxyxnTFBDH9g9a3CDCp1blcoug-AquiCqxS1uoixhHjTHXAT1nRercNTG3a-TxorVJ_jimK6LvPAOhdekSDH4hLjHLDbGxucfnvW1VVZ4aeWR8NeIWn0XKmw4nTmQWn5p6XfFC0U1UTw03c45N9Cs3vb6dg-0bRmm466zQDKjm5cY_Fq1tv_1-o7KVxgHKOB6g6Yl7Hq5vj2ZW85Isj3tC1E-0G8LT1MJ58O4RcQd2EDqM2OD_Dkf1ZqhLCLGITjqDDGqqFfxAEQjFF_yVfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
آیا انتظارهای تورمی واقعاً اهمیت دارند؟
انتظارهای تورمی زمانی بر اقتصاد اثر واقعی می‌گذارند که مصرف‌کنندگان، شرکت‌ها یا سرمایه‌گذاران بر اساس آن‌ها رفتار خود را تغییر دهند؛ از افزایش دستمزد و قیمت‌ها گرفته تا تغییر در سرمایه‌گذاری.
بنابراین صرفِ افزایش نگرانی درباره تورم کافی نیست و سیاست‌گذاران باید در کنار انتظارات، عوامل بنیادی مانند عرضه و تقاضا، هزینه تولید و قدرت خرید را نیز در نظر بگیرند.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20763" target="_blank">📅 12:13 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20762">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پس مشخص است سفرهایی با اهداف خاص هم داشته اید کلک ها!</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/SBoxxx/20762" target="_blank">📅 12:08 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20761">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:  وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر  با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی…</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/SBoxxx/20761" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20760">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نیکزاد و حداد عادل از مشاوران قالیباف:
وضعیت برهنگی در جامعه طوری‌شده که در برخی سفرها دچار تردید می‌شویم آیا مقصد پرواز همان‌ جایی است که اعلام شده یا خیر
با اینکه میدانیم به دلیل شرایط جنگ فعلا نمیتوان آن‌طور که باید وارد جبهه حجاب شد اما از محسن رضایی انتظار داریم که قانون حجاب را تعیین تکلیف کند</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20760" target="_blank">📅 12:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20759">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-If_UvBZxZjGpofzd6OKcCKK-zGfjDKsSNt3L6V8u9ofMEJg8lEMdNl5cFc-0R1XywlN9RVWEJ-gYsyyKgzo9MWtAf5Wz56fHR1XcbLID89O3RGrsAN1DA5uNVgttR22Go1snKBsXWEVc1QAAYpAbDvx1SAYTTJMOpL3gShK9Ho1HOwu17IjE47MCApChAXzVnou92ERDo9nZVIsehvd3XPCnwxinUX2ezx146ASM-es1jZ-45Xu29m_qH1UvBuLjSBChWfAHGdp964QmEMBUnxOM2R66Ibxfh9HW9yKM1t1kMqWCs8TnFrbwXk21CMS9X0SoS8SusNGKhMQjs_IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در بالاترین سطح ممکن قرار دارد.
نظر به ساختار تکنیکالی طلا، بالای 4420 فروش دارد.</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/SBoxxx/20759" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20758">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ درباره نظارت نیروی فضایی آمریکا بر کوه کلنگ:   «به لطف نیروی فضایی آمریکا، ما می‌توانیم همه‌چیز را ببینیم. حتی می‌توانیم نوشته روی لباس آنها را ببینیم؛ محمد الفیاض، ؛ هیچ وقت محمد جونز نیست مثلا؛ محمد العزوری.  می‌توانیم آن را از فضا بخوانیم؛ باور می‌کنید؟…</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/SBoxxx/20758" target="_blank">📅 11:24 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20757">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8qfGdbXHwYpl1yU_ZTPNPsB6_hOPauJWAStVfhtmLYr21w7s6kBQ8mmwYSg9vXpSnqsSusCreN2OxU6_YwsqPtOZStWsG7cNCcjNfZraMwvKViL4-Qg5RhnQF_IH23Rm-rAK8ekLcegGBFOPejAjPB1pgK5u4GMD1h8DnRPY-dxVzmppBYIfJ1qAz93p8IN0ITT57fzvUiYhEBjZxrq1hzVwmVBeSWvlSYyHlS0kLZ0jNNVrBUpykbCEqQ2L4OEKG0d6YGq4i3IihdpMCeKzbvyb0xOSAUqGncfWoSrGXUAYV168Ztw5HUd6uhLYsBJHCaSwEgLCtuWWSkhzMmfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهر بندری راهبردی «مخا» هم توسط انصارالله تصرف شد</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/SBoxxx/20757" target="_blank">📅 11:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20756">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/20756" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20755">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترامپ: «ما همه کارهایی که در ایران انجام می‌دهند را می‌بینیم.آن‌ها حتی نمی‌توانند بدون دیدن ما به دستشویی بروند»</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/20755" target="_blank">📅 10:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20754">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">شبکه سی‌بی‌اس گزارش داد در پی حمله موشکی ایران به پایگاه هوایی «موافق‌السلطی» در اردن، چند فروند هواپیمای نظامی آمریکا آسیب دیدند که یک فروند A-10 یک بال خود را از دست داد و حدود ۸ فروند جنگنده F-15 نیز دچار خسارت شدند.
بر اساس ادعای سی‌بی‌اس، نیروهای آمریکایی مستقر در اردن برای مقابله با حملات موشکی ایران مجبور شده‌اند، بیش از ۳۰ فروند موشک پاتریوت شلیک کنند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20754" target="_blank">📅 10:25 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20753">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaEfXQ7R3Prb2gfPduxLqq1mcv73IeDxVHT4zgNL9nZrG6N7sqBLblbtzwKAlC-nOcMxT5B9R3KfzwqqnThjf4p7NZFc-rvopfvAjkviDw1McuAkxZfoEU4lF4s1MS5tbcCUUe9GlAeaQoNCWAInmbu58vqwh_ykE3BL6WNNHftpPOzLyU36XIaXuv7sEd9E2AKRqULFpSzf1Xy1F5_GoRx_OFJ9gNVq18wXvR6eyRIBepaVy9vG98NAv8VgwOHK2PQsr1rI_jmwkm8mnjD1vnlJoetl7xkFYFsTm1cZseuChs0p1PviI1Si9hLpsoimTIOyRgRWpvv6hK7SRGE-Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20753" target="_blank">📅 01:44 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20752">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دو انفجار در طائف عربستان</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20752" target="_blank">📅 01:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20751">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5q_rOEyUA6eHSpu0RVXaLSVgOz7KDKcjOJBLMd-lwJP_ub12_W_7uRsEdJlyS3nGO60MFCsU9CVuq7OHHbLirsJLvxWrk7ZfAt0jOEnt3lO0tpADpW2uYl2566iZMTSNNkyRPnYgBqZDVRbch3vDg8ZM4z453vQSXsht0aaCxMr5Y0w7eJIgOsDWdePXMjAp-HTtcWTf5n_WV3PYaymOL1JpnrSEUYE3BQQKyIZLneYXEUkjTxC0u4nGqNmtFFRO5-ffAC4cTRjG9V6stfmjvsNfCRu0-DN62L9m_rYKhh25NtGa5A5APoroaX5RLYihwkswnrHJTugnfp52Hohkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موشک؟!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/20751" target="_blank">📅 01:28 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20750">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">پست ترامپ در
تروث‌سوشال
:
این رژیم به‌زودی می‌فهمد که هیچ‌کس نباید قدرت آمریکا را به چالش بکشد.
ای مردم سربلند ایران، ساعت آزادی شما نزدیک است. وقتی کار ما تمام شد، حکومت خود را به دست بگیرید. این حکومت از آنِ شما خواهد بود.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20750" target="_blank">📅 01:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20749">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">برخی منابع عربی از پرتاب موشک به سوی تنگه هرمز خبر می دهند</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/20749" target="_blank">📅 01:12 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20748">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/SBoxxx/20748" target="_blank">📅 01:10 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20747">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">لینک ویدیوی ضبط شد
ه نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/20747" target="_blank">📅 01:06 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20746">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ja_Q1BjYBjozaSKBLkBdUwyB9QlSSkjf6ib-yqHnq0iJ1TQYZ0v2dKpHZzujRT50w9l9hZP1K5RI51EtoTWPrSvW51LBueK-iWgkvPu9sH1IkZmlXczqnaE-OvVvW2dyctWXWETi4ckyViA618A1C5xybis-PIqSuSOm4LVmsJNCWIvL0tUWyeguhq55j2yZI1FNqDpmzpQGrKlnjXrq0F-kHSwQ1HbXjGo5p7IKUkK1RlkUpO4I7BJitqLk4-ebedJpRK886fbeO4x923UuK5rZvAnbDCH7MRGYo_jQVCn7adHaJ2cbdS9sVa-ta9o3GTKvmIetC9LuTa400jEUXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترور یک مامور فراجا در ایرانشهر  به گزارش مرکز اطلاع‌ر‌سانی پلیس سیستان و بلوچستان، ساعتی قبل افرادی مسلح به سمت مأمور انتظامی در ایرانشهر با سلاح گرم تیراندازی کردند که در پی این اقدام، استوار یکم «مهران سالارزاده» به درجه رفیع شهادت نائل شد.</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20746" target="_blank">📅 01:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20745">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20745" target="_blank">📅 00:58 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20744">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیروهای نظامی اسرائیل: آژیرهای خطر به دلیل نفوذ هواپیماهای دشمن در مناطق مختلف شمال اسرائیل به صدا درآمدند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20744" target="_blank">📅 00:57 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20741">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">صدای انفجار در بندرعباس و سیریک</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/20741" target="_blank">📅 00:46 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20740">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">شهر حیس در یمن به تصرف نیروهای انصارالله (حوثی ها) درآمد</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/20740" target="_blank">📅 23:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20739">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U-gZj4E06zcTlwAdBtTz8UFbbZrlVyxe3wMcWdlvb72srIR8a6LyxWCaaEDLz_ujDpAbhDZLCEMM9vVcEm3pfwdEnuZy_uSd5-DRg4dZ8EJWE2TiMZpsi_uvnnU2sSVnsuz_hrr-tL3X6CtesYfKhFtShac6c1k7dtXkCvhB9uFCr82igZhgvmq2BUCROnCAkI0-T3-1fTw7hc7wyRV7d5X83kEeAJbDRK2WdRiTF9W01g-F_Jf5V-kd7U0XgR-7B5m8TuZsNWE1vdm3MZj_U6YSoKghhVIP0uqKHd1VZSogBpeTMz6xdbWl1YaxURFiSiQ-SF-OCachljGFh1ItqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/20739" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20738">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامپ:
باز هم به ایران حمله خواهیم کرد؛ مذاکراتی در کار نیست و جنگ علیه ایران بعد از انتخابات پایان خواهد یافت</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/20738" target="_blank">📅 22:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20737">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDigiato | دیجیاتو</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVonQ9pbQusKx43T-NgoTj4C9AyR6noTLVo315FtVKSAOk4toi7dQBTqtQ0yPO77pUQAf9gOf_xsk6OMWWeHG6wRisLoYLHwDhxPpe2yHNlbyZuwFpVdrOQIgEkVY8MjJxbWlgC7XArEXMA06mzKz6Lj1WcNxsmR27c99kVJSagJCpNPwLM0EGxmmWH_fZAhDtKSmFpFkxSdtoRRkNevsWqu518mo0OBUWhbHuJVvX6aDo6kLnYdDOW9Yydq8Q_XgAUQ_u5qUF9N327bHs3yBPN38axiDn8Jdbul4q19_Jyvy8sGLqazBEhnqhAmG2A9T8tIx5e9pE963yWscptAFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
مریم عظیمی، مهندس ایرانی اپل دوربین iPhone 18 Pro را معرفی کرد
یک ایرانی در قلب توسعه دوربین آیفون؛ مریم عظیمی، دانشمند الگوریتم‌های زیبایی‌شناسی دوربین (Camera Aesthetics Algorithms Scientist) در اپل، در مراسم معرفی iPhone 18 Pro درباره فناوری‌های جدید دوربین این گوشی توضیح داد.
عظیمی که در تیم دوربین اپل روی الگوریتم‌های پردازش تصویر و بهبود کیفیت عکس و ویدیو کار می‌کند، درباره قابلیت‌های جدید سیستم دوربین iPhone 18 Pro صحبت کرد؛ دوربینی که حالا با دیافراگم متغیر، کنترل بیشتری روی نور و عمق میدان در اختیار کاربران قرار می‌دهد.
حضور یک مهندس ایرانی در یکی از بزرگ‌ترین مراسم‌های معرفی فناوری دنیا، بار دیگر نشان می‌دهد پشت محصولات محبوبی مثل آیفون، تیمی از مهندسان و پژوهشگران از سراسر جهان فعالیت می‌کنند.
#AppleEvent
🔵
@Digiato</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20737" target="_blank">📅 21:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20736">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیانیه ایران، روسیه و چین در نشست شورای حکام: ارجاع پروندۀ هسته‌ای ایران به شورای امنیت مبنای حقوقی ندارد   راه‌حل پایدار برای وضعیت کنونی تنها از طریق توقف فوری و دائمی تمامی حملات و رفع تهدید به تجاوز بیشتر حاصل می‌شود   همه پرسش‌های مشروع درباره برنامه…</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/SBoxxx/20736" target="_blank">📅 21:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20735">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.73K · <a href="https://t.me/SBoxxx/20735" target="_blank">📅 21:22 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20734">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">میراث مقاومت: پیوند اسماعیلیان، دروزی‌ها و مبارزه ملی ایرانیان — بخش 1   مقدمه در عصر جدیدی که در نخستین دهه هایش هستیم، یافتن متحدین استراتژیک امری است بشدت حیاتی و تعیین کننده پیروزی یا شکست ملت ها در آوردگاه جهانی. برای ملت ایران که به قولی دچار یک «تنهایی…</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20734" target="_blank">📅 20:26 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20733">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شورای حکام سازمان بین المللی انرژی هسته ای پرونده هسته ای ایران را به شورای امنیت سازمان ملل متحد فرستاد.</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/20733" target="_blank">📅 20:12 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20732">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تغییر موازنه در یمن؟!
(این مقاله ترجمه یک یادداشت در یک سایت ترکی است و لزوماً همه موارد مطرح شده در آن مورد تایید من نیست)
جنگ یمن در سال ۲۰۲۶ وارد مرحله‌ای تعیین‌کننده شده است و ائتلاف ضدحوثی به رهبری عربستان سعودی پس از سال‌ها بن‌بست، بار دیگر ابتکار عمل را به دست گرفته است. نقطه عطف این تحول، توافق دفاعی مشترک مکه در ۷ اوت ۲۰۲۶ بود؛ پیمانی در سبک ناتو میان عربستان سعودی، ترکیه و پاکستان که همزمان با شکل‌گیری یک ائتلاف دفاع دریایی ۱۴ کشوری برای مقابله با تهدیدهای حوثی‌ها در دریای سرخ همراه شد.
این ائتلاف توانسته است نیروهای پراکنده و چندپاره ضدحوثی در یمن را تا حدی متحد کند و زمینه را برای عملیات‌های هماهنگ در تعز، الجوف و حضرموت فراهم آورد؛ مناطقی که نیروهای دولتی توانسته‌اند در آنها بخشی از سرزمین‌های تحت کنترل گروه مورد حمایت ایران را بازپس بگیرند.
نقش محوری پهپادهای ترکیه
یکی از عوامل اصلی این تغییر موازنه، توانمندی ترکیه در جنگ پهپادی است. پهپاد بیرقدار آکینجی، پیشرفته‌ترین پهپاد رزمی ترکیه، به‌صورت عملیاتی در یمن به کار گرفته شده و سرنگونی یک فروند از آن بر فراز استان الجوف در ژوئیه ۲۰۲۶ تأیید شده است. این تحول پس از انعقاد یک قرارداد دفاعی گسترده میان آنکارا و ریاض رخ داده که شامل انتقال فناوری و توافق‌های مربوط به تولید مشترک نیز می‌شود.
توافق مکه به‌طور مشخص همکاری در حوزه‌های پهپاد، جنگ الکترونیک و هوش مصنوعی را دربر می‌گیرد و به عربستان سعودی اجازه می‌دهد از سامانه‌های پیشرفته دفاعی و فناوری‌های عمیق ترکیه برای مقابله با حملات موشکی و پهپادی حوثی‌ها استفاده کند. اپراتورهای سعودی که آموزش آنها از اکتبر ۲۰۲۵ در ترکیه آغاز شده بود، اکنون از عملیات‌های تحت رهبری عربستان پشتیبانی می‌کنند. این مسئله نشان‌دهنده یک ارتقای راهبردی در توانایی ائتلاف برای انجام حملات دقیق است.
تأثیر فوری بر حوثی‌ها
تأثیر این تغییر بر حوثی‌ها فوری و شدید بوده است. پیش از این، مزیت نامتقارن این گروه ــ یعنی توانایی انجام حملات موشکی و پهپادی دوربرد ــ به حوثی‌ها اجازه می‌داد زیرساخت‌های نفتی عربستان، کشتیرانی در دریای سرخ و حتی اهدافی در خاک اسرائیل را با آزادی عمل قابل‌توجهی هدف قرار دهند. اما ورود پهپادهای آکینجی و سامانه‌های پیشرفته مقابله با پهپادها موجب کاهش آزادی عملیاتی حوثی‌ها شده است.
پدافند هوایی عربستان، که با فناوری ترکیه تقویت شده، توانسته است چندین پهپاد و موشک حوثی را در میانه مسیر رهگیری کند. همزمان، حملات هوایی ائتلاف، مواضع و سایت‌های پرتاب موشک حوثی‌ها را در صنعا و حدیده هدف قرار داده و منهدم کرده است. محاصره دریایی حوثی‌ها که در ۲۰ ژوئیه ۲۰۲۶ اعلام شد، و همچنین حملات آنها به تأسیسات آرامکوی عربستان در جیزان و ینبع، واکنش بی‌سابقه ریاض را به دنبال داشته است؛ از جمله حملات هوایی علیه مواضع نظامی حوثی‌ها و تعهد عربستان به استفاده از «نیرویی بی‌سابقه» در صورت تداوم تجاوزات.
حمایت گسترده‌تر دفاعی ترکیه از عربستان
نقش ترکیه تنها به پهپادها محدود نمی‌شود. حمایت دفاعی گسترده‌تر آنکارا نیز موقعیت عربستان را تقویت کرده است.
توافق مکه امکان اشتراک‌گذاری اطلاعات، ایجاد سامانه‌های هشدار زودهنگام و نظارت دریایی را فراهم می‌کند و در نتیجه توانایی حوثی‌ها برای گسترش قدرت خود فراتر از مرزهای یمن کاهش می‌یابد. اگرچه اعزام مستقیم نیروهای نظامی ترکیه به یمن همچنان بعید است، اما صنایع دفاعی ترکیه و شرکت‌های نظامی خصوصی مانند SADAT پشتیبانی لجستیکی و فنی در اختیار ائتلاف قرار داده‌اند که اثربخشی آن را افزایش می‌دهد. گزارش‌هایی نیز درباره انتقال تجهیزات نظامی ترکیه به یمن از طریق سومالی منتشر شده که می‌تواند نشان‌دهنده حمایت غیرمستقیم اما حیاتی آنکارا از نیروهای مورد حمایت عربستان باشد.
تضعیف موقعیت حوثی‌ها
اثر تجمعی این تحولات، تضعیف موقعیت نظامی حوثی‌ها است. این گروه اکنون با برتری هوایی، جنگ پهپادی پیشرفته‌تر و نیروهای زمینی متحدتر روبه‌روست و توانایی آن برای حفظ عملیات‌های گسترده در حال کاهش است.
شکست احتمالی حوثی‌ها می‌تواند ضربه سنگینی به «محور مقاومت» ایران وارد کند؛ زیرا تهران در این صورت مؤثرترین نیروی نیابتی خود در شبه‌جزیره عربستان را از دست خواهد داد. چنین تحولی می‌تواند توازن قدرت در خاورمیانه را به نفع بلوک سنی به رهبری عربستان سعودی تغییر دهد.
در شرایط کنونی، به نظر می‌رسد برتری فناوری و انسجام راهبردی ائتلاف ضدحوثی در حال تبدیل شدن به عوامل تعیین‌کننده‌ای هستند که می‌توانند روند جنگ طولانی یمن را تغییر دهند.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20732" target="_blank">📅 19:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20731">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.4K · <a href="https://t.me/SBoxxx/20731" target="_blank">📅 19:37 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YioF_d5ZzZwxUDpKpnHP3bLPSVIRkMrglDHr-rg7TkeA4_K-xZDGfFBtjRxl78ZoNEHSlrJoM_68dD7408YKNcTNqdnurZVv0FoksAM30f2oIp4vQP_vsu-2RAMrL1c8q1cBcB8BohpvfvYGpy9UhEE3yRLylR_QkrxTWNztzmnc6h4LBOhA4z2QPZYV7AFBErx3Wo-enUtha3XxrSpn5B27nZdhXxJwzErSPVV3P0_q_zBm9_N9y5eDNAuOkr8xQJByNApx8dVO37iK12ESXzlCPnwJbZn0XwacxjnlcJC61go5dPPWZmys661giS6KZ_sdmlI1iUDGUJcaxbSVFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FwRxxuercwJJ-nsI4smgE3iTZgW1R9zdajwtvmt8Ms7ln_LmHNmMVkwKXCFLyyDFw-8E1gPdspBYeU0-iCH_1q4_h6cmvE06PF-cFrbownaJJbLprrHHuYjW8l7nkXF1Ud145mODQ2vL0UVM8uKHI0MebP3a1K2pxLU3l5wpnS_5ZgsP83Xh92QZu6CF8cna_3i0DrYk5ndD1uPZ5_BnXnUTrZVe4_uPl87VYQj_h2Z_RGbxZk_gHRqkUMLOQvrMctykoSCFWs_obeEWkORdJugH_qkNlXRKRrZMB9R9OGCvOsIqKyGlZTedJOqGaRoyC7UjfiLKM-8c37JDX6_kHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">میم‌کوین کریپتویی «لپ‌تاپ» متعلق به هانتِر بایدن پس از عرضه، ۹۹ درصد سقوط کرد</div>
<div class="tg-footer">👁️ 4.74K · <a href="https://t.me/SBoxxx/20729" target="_blank">📅 19:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.64K · <a href="https://t.me/SBoxxx/20728" target="_blank">📅 19:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">بازدهی اوراق قرضه ۱۰ ساله خزانه‌داری ایالات متحده به بالاترین سطح از سال ۲۰۲۳ رسید</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/SBoxxx/20727" target="_blank">📅 19:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20726" target="_blank">📅 18:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یک روزنامه ترکی:
عربستان سعودی از پاکستان خواسته است که در عملیات نظامی علیه انصارالله شرکت کند و مداخله نماید.</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/20725" target="_blank">📅 18:07 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfqhw9tNCWJGtWXOJt0KBmk7fauRJ_9DmerCZpHs0MhZ5BRHGbOJwFIj_AnMYKSXGuUatoYyAhbI1b5MYnA2T5Wdu9DGJyga10dotd8Tdf_4qG-SiiJpLh22LHD3peCwA-7SqoIBW73mInhqc0lbvfCp_Sz9ozXBCAsBb6uU72MvkWtKDVS80Brb45jI04BXPv5eP5xewGk703NpNfzkNIhZ-QdVXTaMZxYL3xxNvLQ_hIpCmVp52w6QtSqcnykqMvURwAK2TdI0LFYjg_tLffWXzUlYbug5nV_HZTQuwVVoV8kUcq87_qBVDTjQYqOh0JU-gxJs5XTYJIj6Yf4ho_hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a244fd3e09.mp4?token=oHlTndrCO5LsrQ8kPn8F917HCpKpdijLxhmMzPO49_ZZ_8k2-EhFQa2b7Xef1vt-Pa7fVZt1q0BF4ECDQF_Wf0wFBNf7zZAmT4P63viI_cSrZeN3A41iFztBXcNkRpcoS0rceKw-69BBTntXdGJppouHvr-QynrO26murivi4yWWsb8SQ4Ro4A6b3A_JkjD7CNrRvk4CSf08L1ulnVfZGurpZZiENi-U9yRgyggWk7lc98GlVE1kbldzz_3OrQtrV3_2oqtdu-wqv14j3qAT6rXM_0xpEaIchF90ciFhKumePp4TDqSFGua0WcGmFo9qLZP8mmClI_FAflk0Q6zqfqhw9tNCWJGtWXOJt0KBmk7fauRJ_9DmerCZpHs0MhZ5BRHGbOJwFIj_AnMYKSXGuUatoYyAhbI1b5MYnA2T5Wdu9DGJyga10dotd8Tdf_4qG-SiiJpLh22LHD3peCwA-7SqoIBW73mInhqc0lbvfCp_Sz9ozXBCAsBb6uU72MvkWtKDVS80Brb45jI04BXPv5eP5xewGk703NpNfzkNIhZ-QdVXTaMZxYL3xxNvLQ_hIpCmVp52w6QtSqcnykqMvURwAK2TdI0LFYjg_tLffWXzUlYbug5nV_HZTQuwVVoV8kUcq87_qBVDTjQYqOh0JU-gxJs5XTYJIj6Yf4ho_hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آمریکایی ها عموما از اوضاع جهان بی اطلاع هستند و خصوصا سیاه پوست هایشان که رسما توی دیوارند!
اینجا این منگل در پاسخ به این که چرا به ایران حمله کردیم می‌گوید چون ایران داشت نفت ما را از زمین میدزدید!</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/20724" target="_blank">📅 17:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">منابع محلی:
بیش از ۱۵ تروریست هیئت تحریر الشام (HTS) در پی انفجار انبار مهمات در حومه شمالی ادلب کشته و زخمی شدند.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/20723" target="_blank">📅 17:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">خر تو خر در یمن!
نیروهای ائتلاف جنوب مورد حمایت امارات امروز سعی کردند طاهر العقیلی وزیر دفاع یمن را که مورد حمایت عربستان است، گروگان بگیرند!</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/20722" target="_blank">📅 17:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20713">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآرش رئیسی‌نژاد</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0xcwsFhp4lxk3jlCKMKF1d8ZZ6UTKm2z5xq1lZIbo2GSvPPlffRJLIcTFxWG707TE-J4FHXRz7sdirdU3Ie8BU6ey6VA3PcO-aBPRg4GtcnzYLxZmSj1CIK7jL-Ks6zMWlEKcduDEkQPcJBWZq7_5IJJsrC7AbI6Lz4jSjwA_n3ho78cVKV-gWLdtRAjTIvuIpcuH2gWjT-R7DPSXR51XLahQ0DBf5FZOgPgMuo1_FjkH3PS978zRiNhTwV7ehUNZ7feh8WTpb819_uU4fGwaUxZphuLdHhV_BJpOYuxBLGNR1w7cefqdORyZWrpIIPYFPZWlPSC5E93AymqYKV8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mo0E-wTnCt2Jftt7jFJPN8xaQ3Fc8le3torXtFLwFDPbgYsNADO4e1ZTxJdGOt7k03v0On84MS7DzFzQamZsF6MyEeaf1sMWlcoaPwhbWyh0UF3Lp7Rr-miJkNRETgKuYZSYRAhnQdMMiiACOjQN2LPEpUAYIsWjD86pS6AhxzyDTYR9UL0TpHzpD-1ynFR7GanjtPwkMQxR9Sg_NscwAd43QHiJ4NWHp0UqoQ4-Dm6ivjK5LELv6Qr-BLhwumRzU_-oLWMN3myb-T8GPJucCreTAOnqQQPw2CaZpiy9l0Cg05Vb0ef4-fduXwDRnCh17wwlpl7iua1G_vIqOMFLVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eI0JdV5M-22ueB__OsziznZAKAaS3gVfNwcYgqvX-gYUglbrhAkSnSs_s5EKcelmtBT822idLR78gEyX-WdsoXCtKTnO8MZYcAx0Rkrs_3lEio-GpX9AHoXmetxD6OLTqEaqUxQ7tynA_VndoFR6LzIZmNYXXlouhJKYj9YDzJXIvuzCRla5s9o-J8L60Icw4a4DlXMmT2uvN4fg4V6Zqk5z7Mq7H37rNg1UeheOSAxQBgEE4Xs7fEJ886zTyKP57YLWrlgtsGGdeJcxopxQt4akQkl6_SeinGGSuU2dIBqg4grnsKqBb7ta8GfxMc-0O2Qj0EXWM5FG6hC8JTb7PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NOPJWOVbOhyoSwkeWAgbdgdEJ5d7-IwW7A2SVndf-eS7J0E7i8QxFBfNuXxdnFtL-H6YQXeuVCwvLt6Ztj-fuBpVoFmqZGOKXRGcA9qLeIDKkDbUJRjnT0mPCdrmqAYNWFduz2AuPpoUvaN9Q14dHQ9dJ-aXs7gv96NocWlzQCP-Aj0nQHFK4CdI50NgM3ZQrT0DsiIhJ3Qh3pMjSJUCtPn7jxqn_sEIb5HmA9bEnitBBWk3oTm-yJ1DYqcvGdP3Xug9etocpdiV33LcDyJXhZT1jhxVaOBDYZWaxgWzRyuXEfXoxhOM5cUoRajmnV_JogrikU4eZVFo7mTpCeD5Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/esNrxYtfK-aTlZORey7tkC3y0MaJYRKdEznSFXMdarCT19EdPsFgqoioPwgDiZrohvLjcx-ddzlxgOqtqfILL1SLQ9HdclUGmvGhq6y6oC1H6A1OuPEWJWGAAxMc187PW3V4cgEiNigOGaX5X9NImuiSRlj2ccPVtCZgU33ivj27MuOPgwow7j3fxj39If0L6Ta3LRY0kK5NpfkxtHn9o-nA4kni0TwOy0OOjm0Qsic7w9vv4hGh6zqcqLOzVQqM2osfOjD0_osPs0_KLKIUOOj7PbwVvMv8BAkbU5A51lM4-o_SlbfV8PWpSoikD2Xd2h2BLdNkI-aFQISlWIaBGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A6wZe38Aw676y9n7MkbWjD98aGhQaUGvz9e4Dqve-UAqgyKwXLLRKXkcHwphzml1H8eZZ-SIQbyfI8Q6xv20acAk9mqdx9Zp9BXzJLpIqNdr2tudifJ8enj8rPYewJZ_1qmlYRHpdkUa3reNd_GJMHSfwO0LddMk6zkcA9j--7Jod4d1DYtjA6SZQ6XbzwxnaC3rybaVnl_8VMmcqXUq5dOFOHFKTBoluhJbHj6bli2iXCAu_va-PYWQzQ1lrzfJwRVJifF_Gl1oA_xzFIXwDS7CmPYVBsOZzbd1mXXElA2iXk3qsbA2zs7qjbKmsnjBG9KO3ssxOVQtrvRTUAxjwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nIz5r1MxlLtzdm402nrGW_qXDF_0hVXmv7O5-PNhIJt_b4YCLzn6LcA5YtATMFFoKlWbM9LY-G4Xp07-RQEziwrZ1t0Zv10_fggTkedE7I8Q7zWWVRvQPSJ7aoxTm2zvlv42JdM7wUYh2gNhL-mzzwA8uQeazM5rR9BbGwbw2YuJJ0Oy9_joqdUBn5LvqeLU5UAEVisESq1eOaR2j7i6jOji6KF91BsxExauMVqoBnnzV4AWLWUEgpcdAv1gkV8C6QpgkmRKKv6Ai_K1SwdjdlrElxIR6i5XC2U9uVZd38DVUuQIKISs8e0rYEK-HUIUhD2cqlsVeie2tLi_tgFJtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oAO5sKvVdsvrEXmmDH5aZMPCy44r5YtDyAInXJ16OH88S5r6H1PoFGAChSRW-Nm7QM9mUeenzJsXhmL1dW_TaxoutxmPEMhqYwddv7TgOB1DGKGQwoZPIlaDZPVQiCSOXoTThkH7MN-Dk6gyy3zdQ7xZ-pTXZzQC4Z6Vg8v9YKON5_tBkfQCvLq8VtNvM2LeOF1Av-h_sju0YRIJFevAkVwVb6dGjLH22dLmq71poVmZ13GrFOPUAXDQp7LQnnV5xWfev9w1BWm_JxLJd8Rxcycthq-fj6PH2A_NgaVprM65uWNTBGgZ3P0I5ysmdb4vtQN6g038TtKv--VJzW0IlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aecrA8PRX9nzsxe8ie0iyhTWkG2RLOuu06Zw4XFPBJX5695VNCuFm7Vh2PPmakPxrI96rY-nOkBP2Efc0W13aUWn64OogKQ0wMzdToKNkJyNPxjB8nYQfKmpxWPPOE2JePqGhZV_2EGYgPSt1CnjoMaTz5vwXosE35FVJ7Mq0Zt2Izcw6IxyFOPzfZ6k6LzmlF7TvutucFyT1kUt_Vd2f0ad5qFExherAITEB4ePFNJTI00tdvKBXRjrLfP7p-qizRWSTrDgCwOiRNesGoJa1zay7iWVSpR-RD3JaV-Uz53Iv6Fv3tNJq0W2kQLfCpuURsQEKJbL2-a6j4EJecfgzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در دره پنجشیر، یک تنه در برابر ارتش سرخ شوروی ایستاد، آنگاه که کل افغانستان زیر سیطره رژیم کمونیستی کابل درآمده بود. در میانه جنگ‌های داخلی، کوشید که ثبات بر این کشور گسیخته‌از‌هم حاکم شود؛ اما نشد. تا انکه طالبان شهرهای افغانستان را یک به یک تسخیر کردند. این بار نیز در پنجشیر جانانه ایستاد، آنگاه که دست یاری‌کننده‌ای را نمی‌یافت.
در میانه سال‌های جنگ، روزی در تخار در شمال غرب افغانستان، در جمع مجاهدین و خبرنگاران نشسته بود و دیوان حافظ شیرازی را می‌خواند که خبر آوردند طالبان در منطقه‌ای حمله کرده و در حال پیشروی است. مسعود توجهی نکرد و به خواندن دیوان حافظ با عشق ادامه داد. یکی از فرماندهان از بی تفاوتی مسعود ناراحت شد و با صدای بلند گفت: آمر صاحب! طالبان حمله کرده اند. مسعود گفت: بگذار که این غزل را تمام کنم، مگر نمی دانی که جنگ با ما بر سر حافظ است؟!»
۲۵ سال پیش در چنین روزی، احمد شاه مسعود، شیر دره پنجشیر و قهرمان ملی افغانستان، ترور شد و جان خود را از دست بداد!⁩
@Iran_Simorq</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/SBoxxx/20713" target="_blank">📅 17:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20712">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">نتانیاهو رفته از جنوب لبنان بازدید کرده!  از این جهت خیلی شبیه احمدی نژاد است؛   منتهی احمدی نژاد سفرهای استانی اش به شهرهای ایران بود اما نتانیاهو عمدتاً به مناطق تصرف شده کشورهای دیگر سفر می کند (غزه، سوریه، لبنان....)</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/SBoxxx/20712" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20711">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع خارجی:
بر اساس تحلیلی که از بررسی تصاویر ماهواره‌ای به دست آمده است، در سال جاری شاهد افزایشی در ساخت‌وساز در محل زیرزمینی مشکوک هسته‌ای ایران در نزدیکی نطنز بوده‌ایم.</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/SBoxxx/20711" target="_blank">📅 17:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20710">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر خارجه یونان، جورج گِراپتِریس، درباره ترکیه:
«ما درک می‌کنیم که این نوع تنش‌های بالا که اغلب از سوی محافلی در ترکیه همسایه می‌بینیم، همچنین به این دلیل است که یونان به قدرت واقعی دست یافته است — صدایی که بیش از هر زمان دیگر شنیده می‌شود.
من فقط می‌خواهم اشاره کنم که هر کسی که فریاد می‌زند، همیشه قوی‌ترین نیست. در واقع، اغلب آن فرد ضعیف است.»</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/20710" target="_blank">📅 15:58 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20709">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/SBoxxx/20709" target="_blank">📅 15:56 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20708">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/20708" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20707">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwMU0IzLTXF_j9TLpJZnvGVryXYt50d2gbUeHd1b_X2YUTZtxTeFjASU4ji0sW555KzBu4VqaHlUwzNMHdLzDH-jNsC8jI-g90O9hC9ggh6q7wzaj8CFSEVDsJTex1iFt_AFBEpypcRKUDe_L2dIdFQ4FOFQMAP18JFDaib8QwYQzTiKQ-QxFbJ5K7bfFou-IOmNFfR5qnK3wBNBsTJB3BzRixDoWqhu1pSlcB6_QWBNC9cJXEnCTy5xHn3PX-FvY7weLkHI5Ni1cg_Ua3RMkU2TyURqrlM8v9OmQZ_1ZGSdEsrYjK_wgCVIGZik3aV3XDQcUIjVSBA9iKwUd2Pe3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ولادیمیر پوتین، رئیس‌جمهور روسیه، و دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره ایده برگزاری یک نشست سه‌جانبه با شی جین‌پینگ، رئیس‌جمهور چین، بحث کردند.</div>
<div class="tg-footer">👁️ 4.77K · <a href="https://t.me/SBoxxx/20707" target="_blank">📅 15:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20706">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سخنگوی سپاه:
هر کشتی که از منطقهٔ ممنوعهٔ تنگهٔ هرمز عبور کند تحریم می‌شود
در صورت عبور هر شناوری از محدودهٔ تحریمی تنگهٔ هرمز که مختصات دقیق آن اعلام خواهد شد، ارائهٔ هرگونه خدمات دریایی، بیمه‌ای و پشتیبانی به آن شناور متوقف می‌شود؛ به‌گونه‌ای که حتی در صورت تردد بعدی در تنگهٔ هرمز نیز از دریافت این خدمات محروم خواهد شد.
منطقهٔ تحریمی تقریبا از سمت چابهار شروع و تا بخشی‌از دریای عمان و دریای عرب ادامه دارد.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/20706" target="_blank">📅 15:23 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20705">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">این تحلیل برای 1 اردیبهشت است. تارگت من برای قبل عید 150 هزار تومان بود و تصورم این بود که از یکی دو هفته پیش یک اصلاح موقت بزند تا حدود 120 تومان که این پارت آخر نشد.  با این شتاب، اگر 150 تومان را رد کند تارگت مرکز تحقیقات مجلس در 240 تومان را فعال خواهدکرد…</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/20705" target="_blank">📅 15:21 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20704">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">شروط ایران برای پایان جنگ توسط سخنگوی سپاه اعلام شد:
۱- ضمن توقف کامل جنگ،
۲- از تهدید مجدد دست بکشد،
۳- ارتش اسرائیل از لبنان عقب‌نشینی کند،
۴- محاصرهٔ یمن پایان یابد،
۵- ۲۴ میلیارد دلار دارایی مسدودشدهٔ ایران آزاد شود
۶- و از هرگونه مداخله در توان هسته‌ای و موشکی کشور دست بردارد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/20704" target="_blank">📅 15:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20703">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9OEo_bUqHYIFfr-v_Y00vLmupuxQwLiURY68iU2blwe9h5G4W7bxc0mtGmvJA-i30ZHGi-VFRayi-yBGSbDbMcEK1y2xqhLflKBGbHwdejPqw1yGraK8piF6SHn6D-G11GaDWdyvPAC0Yr43lQD3hQ_MnyPUg0KYv914buhaa163Mmt8n-jEfxpOT7MMnEwrAu0e-Pu3KKKboUhb7o2S7Qkg7ZwFGBu7IWDZTU4cdwQpD2wOz6-xDmfUXBpr-liLMEFVbif-midS0xaEQBkfhku3_s9KQBcNdxQfp1PA9BFohzr2D9nr6-O2LL-2dpMmwZ-UGj_ZNUAQ_uowo2KcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های رهبر حزب AfD درباره برنامه های اجرایی این حزب  دقیقا کپی برنامه های خاویر میلی در آرژانتین به اضافه:  — کاهش حمایت از اوکراین  — مبارزه با مهاجرت بی رویه</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/SBoxxx/20703" target="_blank">📅 14:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20702">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏اکانت صابرین نیوز در توئیتر:   حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/SBoxxx/20702" target="_blank">📅 13:59 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20701">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
اکانت صابرین نیوز در توئیتر:
حداقل ۴ آمریکایی در حملات دیشب به هلاکت رسیدند</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/20701" target="_blank">📅 13:57 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20699">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شعارهای شب گذشته امت مبعوث در تجمعات شبانه
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/SBoxxx/20699" target="_blank">📅 13:35 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20698">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">#GRI  شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/20698" target="_blank">📅 13:19 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20697">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EzeFWkbAN8Q_VpF1_xy3Dn9hWTof-_WSGatzxkWo5JF5OzfQlbFh6lgDlLGGakBkqKdN9vZhggOWuWMrPf5c3fD35N5MbtXQPJy6b4ZdNuTg0fml5jmHnp4UhzkEoy2djhqNSmZJzzRsyqUsDYKRPa9Nob2fpCyRMRR_K2WgevLfQdNg5-8syi06evfkcK8np7avwZGGdD-yxTtp9yDxT5yQigLUAELsOQ02_NwJ_h7yVCclsn6ExujWKXCbeVbInEOzylBLcHiEVQ0rb2kA7njBSZSrqRWdQZWkRuq_13xi20qj8RJfG9mOU7zodKI7416BVY2SEIxNYD7MFP7Vxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی امروز در سطح بالایی قرار دارد و فروش توصیه می شود.</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20697" target="_blank">📅 11:36 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20696">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">وال استریت ژورنال:
تلاش‌های اخیر ایران برای هدف قرار دادن تجهیزات نیروی دریایی آمریکا این نگرانی را ایجاد می‌کند که ارتش این کشور از سلاح‌های پیشرفته‌تری استفاده می‌کند و ممکن است از چین یا روسیه کمک دریافت کند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/20696" target="_blank">📅 09:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20695">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جنگ اراده‌ها در تنگه هرمز؛ ایران و آمریکا چه کسی زودتر عقب‌نشینی می‌کند؟
جنگ ایران و آمریکا وارد مرحله‌ای شده است که در آن، اقتصاد به اندازه موشک و نیروی دریایی به سلاح جنگی تبدیل شده است. تهران و واشنگتن هر دو تلاش می‌کنند هزینه‌های ادامه جنگ را به طرف مقابل تحمیل کنند و در نهایت او را به این نتیجه برسانند که ادامه درگیری بیش از دستاوردهای آن هزینه دارد. به همین دلیل، آنچه اکنون در اطراف تنگه هرمز جریان دارد، صرفاً یک رویارویی نظامی نیست؛ بلکه یک جنگ اراده‌ها است که در آن هر دو طرف منتظرند دیگری زودتر تسلیم فشار شود.
از یک سو، ایالات متحده با ایجاد محاصره دریایی و هدف قرار دادن برخی زیرساخت‌ها و نفتکش‌های ایرانی تلاش می‌کند صادرات نفت ایران را محدود کرده و فشار اقتصادی بر جمهوری اسلامی را افزایش دهد. از سوی دیگر، ایران با تهدید شناورهای آمریکایی، ایجاد محدودیت برای کشتیرانی و تلاش برای افزایش هزینه عبور کشتی‌های تجاری از تنگه هرمز می‌کوشد هزینه اجرای محاصره را برای واشنگتن بالا ببرد.
ایران؛ فشار بر مهم‌ترین منبع درآمد
برای تهران، مسئله اصلی اقتصاد است. نفت همچنان مهم‌ترین منبع درآمد جمهوری اسلامی محسوب می‌شود و محاصره دریایی آمریکا مستقیماً توانایی ایران برای صادرات نفت را هدف گرفته است.
بر اساس گزارش شرکت Kpler، حجم نفت خام ایران که روی نفتکش‌های خارج از منطقه محاصره ذخیره شده بود، از حدود ۹۰ میلیون بشکه در اواسط ژوئیه به حدود ۲۹ میلیون بشکه کاهش یافته است. اگر این روند ادامه پیدا کند، فشار بر درآمدهای ارزی ایران افزایش خواهد یافت و دولت برای تأمین هزینه‌های جاری و واردات با محدودیت بیشتری مواجه خواهد شد.
اما فشار اقتصادی تنها در سطح صادرات نفت باقی نمانده است. دولت ایران هم‌زمان مجبور شده قیمت بنزین در بالاترین سطح سهمیه‌بندی را به ۱۰۰ هزار ریال در هر لیتر افزایش دهد. این تصمیم از این جهت اهمیت دارد که افزایش قیمت سوخت در سال 1398 به اعتراضات گسترده در سراسر کشور منجر شد.
بنابراین، تهران با یک معادله دشوار مواجه است: اگر در برابر فشار آمریکا عقب‌نشینی کند، بخشی از دستاورد استراتژیک خود در تنگه هرمز را از دست می‌دهد؛ اما اگر مقاومت را ادامه دهد، فشار اقتصادی و احتمال نارضایتی داخلی افزایش خواهد یافت.
آمریکا نیز هزینه جنگ را می‌پردازد
با این حال، تصور اینکه تنها ایران در حال پرداخت هزینه اقتصادی جنگ است، اشتباه خواهد بود.
بر اساس برآورد لحظه‌ای دانشگاه براون، جنگ تاکنون حدود ۱۰۰ میلیارد دلار هزینه اضافی انرژی بر مصرف‌کنندگان آمریکایی تحمیل کرده است. این رقم با سرعتی حدود یک میلیون دلار در هر دو دقیقه در حال افزایش بوده است. به‌طور متوسط، افزایش قیمت بنزین و گازوئیل از زمان آغاز جنگ بیش از ۷۶۰ دلار هزینه اضافی برای هر خانوار آمریکایی ایجاد کرده است.
فشار اصلی در هفته‌های اخیر از سوی بازار گازوئیل آمده است. قیمت گازوئیل در آمریکا به حدود ۵.۹۰ دلار در هر گالن رسیده؛ یعنی تقریباً ۶۰ درصد بیشتر از یک سال قبل. اهمیت گازوئیل بسیار فراتر از هزینه سوخت خودروهاست، زیرا بخش بزرگی از سیستم حمل‌ونقل کالا، کامیون‌ها، کشاورزی و زنجیره تأمین به آن وابسته است.
در نتیجه، تداوم قیمت بالای انرژی می‌تواند به موج دوم تورمی در اقتصاد آمریکا منجر شود؛ از افزایش هزینه حمل‌ونقل گرفته تا افزایش قیمت مواد غذایی و کالاهای مصرفی.
تنگه هرمز؛ میدان اصلی جنگ اراده‌ها
اینجاست که اهمیت تنگه هرمز دوچندان می‌شود. ایران می‌داند که نمی‌تواند الزاماً آمریکا را از نظر نظامی شکست دهد، اما می‌تواند تلاش کند هزینه پیروزی آمریکا را بالا ببرد.
حمله موشکی ایران در ۵ سپتامبر به سمت دو شناور آمریکایی، هرچند بدون اصابت و تلفات بود، دقیقاً در همین چارچوب قابل تحلیل است. تهران می‌خواهد به واشنگتن نشان دهد که اجرای محاصره هزینه نظامی دارد.
در مقابل، آمریکا تلاش می‌کند با اسکورت کشتی‌های تجاری از مسیر جنوبی تنگه، نشان دهد که ایران نمی‌تواند به‌تنهایی قواعد عبور و مرور در هرمز را تعیین کند.
اقدام ایران برای ایجاد یک «منطقه محدودشده» نیز بخشی از همین رقابت است. تهران می‌خواهد کشتی‌هایی را که از کنترل ایران عبور می‌کنند، با تهدید به قرار گرفتن در فهرست کشتی‌های غیرمطیع، جریمه، توقیف یا حتی مصادره، تحت فشار قرار دهد.
بنابراین، هر دو طرف در حال تلاش برای تغییر محاسبه هزینه ـ فایده طرف مقابل هستند. جنگی که هر دو طرف می‌خواهند دیگری آن را تمام کند. ماهیت این جنگ را می‌توان در یک جمله خلاصه کرد: ایران می‌خواهد آمریکا زودتر از محاصره عقب‌نشینی کند؛ آمریکا می‌خواهد ایران زودتر از استفاده مؤثر از تنگه هرمز دست بکشد.
واشنگتن امیدوار است فشار اقتصادی، کاهش درآمدهای نفتی و تهدید ناآرامی داخلی، تهران را مجبور به پذیرش شرایط آمریکا کند.
تهران نیز امیدوار است افزایش قیمت انرژی در آمریکا، فشار تورمی بر خانوارها، افزایش هزینه حمل‌ونقل و نزدیک شدن انتخابات میان‌دوره‌ای، در نهایت افکار عمومی و سیاستمداران آمریکایی را علیه ادامه محاصره تحریک کند.
این دقیقاً یک جنگ فرسایشی و روانی ـ اقتصادی است. پیروزی لزوماً به معنای نابودی توان نظامی طرف مقابل نیست؛ بلکه ممکن است به معنای آن باشد که یک طرف زودتر به این نتیجه برسد که ادامه جنگ دیگر ارزش هزینه‌ای را که می‌پردازد ندارد.
مسئله زمان
در چنین جنگی، زمان اهمیت تعیین‌کننده دارد.
ایران باید پیش از آنکه فشار اقتصادی به یک بحران داخلی تبدیل شود، راهی برای کاهش فشار پیدا کند. آمریکا نیز باید پیش از آنکه قیمت انرژی و تورم به یک مشکل جدی سیاسی تبدیل شود، بتواند به یک نتیجه قابل ارائه به افکار عمومی دست یابد. به همین دلیل، جنگ در تنگه هرمز بیش از آنکه صرفاً مسابقه موشک‌ها و ناوها باشد، مسابقه استقامت سیاسی، اقتصادی و روانی است.
در نهایت، پرسش اصلی این نیست که کدام طرف می‌تواند ضربه سخت‌تری وارد کند؛ پرسش این است که کدام طرف زودتر حاضر خواهد شد هزینه ادامه جنگ را نپذیرد. و تا زمانی که تهران و واشنگتن تصور کنند طرف مقابل زودتر از آنها عقب‌نشینی خواهد کرد، احتمال ادامه این رویارویی بالا خواهد ماند.</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/SBoxxx/20695" target="_blank">📅 08:42 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20694">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد  تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/20694" target="_blank">📅 07:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20693">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">سوریه مدعی رهگیری چندین موشک‌ در جنوب این کشور شد
تلویزیون سوریه با اعلام این خبر مدعی شد موشک‌های ایرانی بر فراز استان سویدا در جنوب این رهگیری شدند؛ موشک‌هایی که به ادعای این رسانه، اردن را هدف گرفته بودند.</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/SBoxxx/20693" target="_blank">📅 07:53 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
