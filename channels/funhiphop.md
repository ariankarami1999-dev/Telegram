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
<img src="https://cdn4.telesco.pe/file/spoNgI4P8vDqVaI98Ts1y8zphx1-NeVabJYxbHHQ10GcuhWwABlsazd0DeeGhmjSxHZI227tDD_MqS4d7hmxHkxoo8nrSoPiaxlLXyeDN7XugsIJ7QWpodL130a2ktpckk43WXDqcQnemK9TM5EZZrzCBmHVgdy29anXWjVvQnDo7I-D_qrQrzBVqxj_4NiB_aelxWjia5xxH7xMlv3Td2uNRJ7WqJF578QKiR1ULw1W7Xx2FhnbnmMVk5ShfBQLPm0juQtlj8BPUvBwKVJiu05YynK_6cvupHajUdkJ9qatbUo_fDKll6GKfvfyySqy6nVtN9crKVdwB6ddjADq4g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 148K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 16:29:40</div>
<hr>

<div class="tg-post" id="msg-75161">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پشمام معین قراره برای آلبوم جدید دریک آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 472 · <a href="https://t.me/funhiphop/75161" target="_blank">📅 16:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75160">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خبرگزاری فارس: وقوع چند انفجار در امارات برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/funhiphop/75160" target="_blank">📅 13:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75159">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">خبرگزاری فارس:
وقوع چند انفجار در امارات
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/funhiphop/75159" target="_blank">📅 13:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75158">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فارس: آمریکا هم در پیشنهادات خود علاوه بر رد شروط ایرانی، پنج شرط اصلی هم برای مذاکرات گذاشته بود: عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران عدم پرداخت…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75158" target="_blank">📅 13:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/funhiphop/75157" target="_blank">📅 13:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">عباس عراقچی در کانال تلگرامی خودش اعلام کرد که کتاب ‘قدرت مذاکره’ به چاپ پنجم رسیده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.74K · <a href="https://t.me/funhiphop/75156" target="_blank">📅 12:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ژابی بنده خدا رفت چلسی
از اونور رئال و بارسا میخوان چلسیو لخت کنن</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/75155" target="_blank">📅 12:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GLVLSfIusStYNU_J1QFEZrAXM_2suWi2e3AFMN0tmnBPXU4s3UcBD_bw3khFEcA5M68aSFII-I2imcXDFHVr2oAxXBrmkQwazV4-aufqJT6bUqIWp_B1jk5h2sbrkJNLsc6GIMZl4q2As8i0Z92bX0sLpQcHqXWeqOQZuxoSCnP_BEXs0KISldkd2-3Bgbnel0MtFNSuZDUdf-DnIy_Xx7p7ck-d2Lf7KdX4uv3VvUimI-CHUu98qymvW84ylThyc4dcDQOm7ZDD2xiLQsUu-4nxboQVU3FhQ-P4NmUPDkt6xSQ_8WSsjyQFHtAx_MDWaoNnpRsgDDJpF0LrJrgKew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😵
نت بلاکس
آمارها نشون میدن که قطعی اینترنت ایران حالا وارد
روز هفتاد و نهم شده و دوازده هفته‌ست که ادامه داره.
☠️
🤬
این محدودیت گسترده اینترنت باعث شده مردم کمتر بتونن آزادانه حرف بزنن،
اخبار دنبال کنن یا توی اتفاقات جامعه نقش داشته باشن. انگار مردم فقط دارن اتفاقات کشورشون رو تماشا می‌کنن، بدون اینکه واقعاً بتونن تأثیری روی اون داشته باشن.
☹️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/funhiphop/75154" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75153">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">😂
معاون سازمان بورس
بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها در روز سه شنبه بازگشایی خواهد شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.17K · <a href="https://t.me/funhiphop/75153" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75152">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJWPRTvqaVQMQ6vPQqv6UwEBhv1tVVWjv-NVzSkccaRmoOFwj2ot6Tox8bJWB4jOs8SdGo_s2sWGLPs2MfEVQaY15P_cbZiXrMBGcpwKYqjH4p5K8ScBUg9QhzbsxILn0I9rZDl35QpsFoiBn9X-bC142cfa9hFXXFTT4I_b_rKAOaljHv6zlgjmqkVBJoxw_ELoh8xEJ0XtvqrIJ1912VoJbOvKbj8eRWLHiMFStJrr5PSIswiiVooTx3BqyBD0b69w-q907elXneClGK6Fh3pyX1SFHBNWyOiN4BPcsm_ArJDTtSn_aTCWmOQWGygOS6VARrlQeBmJvFlkaWjnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ روسیه در آژانس بین‌المللی انرژی اتمی:
کارشناسان غربی معتقدند که ایالات متحده و اسرائیل ممکن است در روزهای آینده، اگر نه در ساعات آینده، حملات نظامی علیه ایران را از سر بگیرند.
اگر این درست باشد، به این معناست که آمریکا و اسرائیل از اشتباهات راهبردی گذشته خود درس نگرفته‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/funhiphop/75152" target="_blank">📅 10:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75151">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3jkgHSFlsvKzhbpqZBSfxzZkluPNDbjmRO-NSg8tTryGSXGsYFQQgbVKebH5vo3xfoNrkpePLHONo8BIGsN4vdqn6zdSEI_-NfoM8IpH4K07MWATLGmbyTd1i8NgpNKXNIA1GF_cIWgtjgj9RXT9_OrLXQm6vmD2mOiS__E3Bw2HpiHjMh3JlFJRDnR9uWFaQI9SYRz-weONKOB3NYb8EOfzzz2dyk7tJOpZRJkgzs8yimehBiMDBoh0x4kKfmldgaxofnngd3cdnWhf5klGGXKAMA4qvIJW4TX-I2mvbzuuox_k6e5cdBekzsaJBks3Mf1IayrCjGu5InBGthu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید کاخ سفید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/75151" target="_blank">📅 09:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL8Gy_KMkgyve-yXlaluXaG6BoEmh-02gaZ-8g8XrUnv0PRB9_XIfniC6Mpl8nj5BYehQOGQK3HzB6ZTuSDm6xoPtouvZOPZjUqyURh80OoF6EACFUHGjfBWBXLGsGbns0-5b2HwubjKm0YpQ6EeNb99gV5hterMHblLnkOcSreiNtat28eo_H4dDCDKGn7uysinJnJNEIKRKRAPJVayn3QdRmBCmnCDwyKPsvKQ8uBiQQwHWLk9E_nCqWAeQywIih_WAFSu9FSqkLZ-Xxy-efI0DcQks0qRi-7PrJFhmHREeiTwmumHlLM5VqdgwsXSsByx6K9NM-zHaMKJB5e4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47
دیشب : آموزش کار با pkm
امشب به حول و قوه الهی: آموزش لانچ موشک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/75150" target="_blank">📅 09:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خبرگزاری‌های عبری:  یک انفجار در کارخانه شرکت تامر روی داده است. این شرکت در حال توسعه و تولید موتورهای موشکی سبک و سنگین، از جمله موتورهای پیشران موشک‌های آرو ۲ و آرو ۳، موتور موشک سیلور انکور که هدف‌گذاری شده است، موتورهای ماهواره‌های صنعتی هورایزن و موتورهای…</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/funhiphop/75149" target="_blank">📅 06:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pv6weEkOkzPoXPqtpUwbHnzEdBDWXmS3x1XoNXgsd2k320lyhL4uExQVhjoi0i12-p3yL4Gc8NyVtK_gUYHA9DksUVnnYFSutS_d_aGrV9zrwd3SX4vc-I6O4CgGzALpM0p3TwoRwfbofiFqC928OhgLVIWfhBtY_9EnpybuVH9hqyUYMWzset_4NHuAUzFtHIiHPBhbgvRVpq876-xi4VOyh_A-085rrweEitYveJ-OYGoxLVitCLb6v85PjMen6uoQdTFUp938tKKYGlxHpBk-E7J4J-1I8PciVTj9QzCm5QIFXzQU5-sZm1MNGtmVPsdStxeiSERUYuFLqM2f1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIszL30dv719VvSVHbqlKOkoEOOPzinAsIBGXfsrjOrf7IA8yWo4q6VEG02hQUwITc3EvEoCIgN6il8DAQsICo_DfJRZjFArK3PNZiG-lkBs3RDDcBGvt4uZynUI2Z7dK3aqAvyvBKwLvwZPPXSLl4rmooMIrh8kBlF_mYewwm8ClWGhWNfStWxOr99LbrNjNn2269PDGAi8Hht2bXL0au9snasuSqNYieoXZo-pOjSSucvMLsh-EwbPI_26QcGDKTPg-L2B36AeW_AqKiTnq1JNObP9Nd8irMyr9RuCvKCyG9Zd0K6P-VKoelDwXCR5GYzdL_0_HYqa26DgxPRTOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی چنین چیزایی رو پست می‌کنم احساس می‌کنم خرافاتی ای چیزیم.
ولی اتاق جنگ اسرائیل چند روز قبل از حمله قبلی یه ساعت شنی که قسمت بالاش پر بود رو توییت کرد و دقیقا یک روز قبل از حمله هم ساعت شنی ای که قسمت بالاش خالی شده بود رو منتشر کرد.
حالا هم هفته پیش یه ساعت شنی با قسمت بالایی پر رو توییت کرده بود و الان یه ساعت شنی با قسمت بالایی خالی شده...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75147" target="_blank">📅 05:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXG8lOY73khd8AI-j8TmkoLUgIaNJISgjCO3X-InjuxNZ2jMhpZN_pb7LCiVc_sAyVq98FPwr0n4rjSxhNvfGunCEkjX0bO6N3RTgRZMMrDZ5dV_Nn30TCB76G-1hX3JOWAiqgdav8cLIYdhNYBWTUv4lCpex0GH8SdpeLs9alvu6AgN7Vv9T_YX0Z9eJOLxyzbwyf26Uw1oX2o2_CVRzdE3jaNMmH2aQsyZmTkJ-NfyYIjN9tpqMYIPWdRvmpBNOb4jMjTwEiq8PeVfGl8oziqN2Ux2OjKFgNzapyEYdfwLcSb6q0gnze3WX_m_q6ari63C8pO_LLnokvDWtUM6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله جدید تایم درباره دیدار ترامپ و شی جین‌پینگ دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.  حتی اگر توافق…</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75146" target="_blank">📅 03:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کیر استارمر یا همون نخست وزیر بریتانیا بعد کیر شدن تو انتخابات محلی داره به نزدیکاش میگه تایمر ست کردم از سیاست لفت بدم.
یه حزب راست میانه رو هم داره میاد رو کار که احتمالا به مهاجرا قراره گیر بده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75144" target="_blank">📅 02:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">اونایی که با شیر و خورشید وصلن کامنت بزارن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75143" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الان گارد جاویدان باید ضد حمله بزنه
وپن بده به اسم فاطمیون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/75142" target="_blank">📅 01:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ولی من دیشب چهار ساعت با سرعت نور وصل بودم جدی همش اینستاگرام بودم چسبید</div>
<div class="tg-footer">👁️ 6.22K · <a href="https://t.me/funhiphop/75141" target="_blank">📅 01:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گوشیتونو سه بار خاموش و روشن کنید
برید توی سیتینگ
وای فای رو ۳ بار روشن کنید و بعد ۴ ثانیه خاموش کنید
سیمکارتتونو در بیارید و بزارید تو یخچال(تأثیر داره رو سرعت بر ثانیه)
بزارید رو حالت هواپیما و بعد ۱۴.۵ ثانیه بردارید از رو اون حالت
به سرور شیر و خورشید وصل شدید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/75140" target="_blank">📅 01:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مجری: سلام مارو به رهبری برسونید
حداد عادل (پدر زن مجتبی):
من هم از همین طریق صداوسیما سلام شما رو منتقل می‌کنم، امیدوارم برنامه ما رو ببینن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/75139" target="_blank">📅 01:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75137">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-M1SlJmVW1bt2vjI5IRd892Ru-dzp-tq8FULU0OKG4Jop8eSGSBsDBHZUzf4kKjuPfz7B-SRnJTOGw9c6WcSEW65dwXWrZrbW-_8vqOEPp3FO1kBsCqpjwxy9D6mO01r-ED27bxzWkWlHAKxx9M68C8ToxvvT1bFkCjuM9BvznzOsyxX3qCi7qo4C0kDbrjFDWSNajUrfSpLIeO9xQs-T63qszGxSTraOxIRFqOf-NvCdejxiA78mXkCj_FfWllzG6hspP7aJHnVo6iRtjYJ1pbti6u7XZRM4vPeC6LIR_SS_iRIEwccQdHDabFgaGlayo7l9V0OddtFeXpmjZc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6C7Ga_nBARK5tZDgl13zOrkvOYQEWvkbC9tadPKEnGJMnVEFfljyMRnbf6yoAGpt-d6oS9kUnMWHrX_jXTA6cSWbDyyYVN1xk8t4tsr26NuVX3JTm4rl_dZika8ZZ3iMoGBRGJhs4Tn_X8ZLlJ4gv-x5nBT_iwTyu5OKEZJBAamWRPKlkCLcbWpZ0dG2pnyFrOMzDntP5IdfVJZqOXgk_VqpEaOO2toktkANpN7J9LqvK__OkmQtPc-uo5KT5I6ooF1RO2MGTTDJfixH8ku4HjLd7wcgjKbSn2vNG6Bnlyd3bbffC05jOaor9wUMiZfggsiq8WoezUm92jrepx5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبل و بعد جنوب لبنان
اره داداش عباس داره بدون عینک دنبال عینکش میگرده بره مذاکره کنه این جنگ و تو این جبهه هم به پایان برسونه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75137" target="_blank">📅 01:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75136">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4bLvpUqFbfFyyPtyj5633lsCophzlGHN5Grmo4Ifb7_1K0TR2PPovcr-vnCT3nHUIxAkaHENeM-XfGyD0fx8AHJuErI19qSTHZEYeCrvNypPnJHnzI5qQnV9F0fnpGU5tcTmSxYvRQvShMijXolNKohaS6EGhAPejV2T8SLe8YvTjJfL0GiRShVgaALx3kdXdp4oBT4Uqmtuew1AnqyNRn8CSZVrvTD8hcmx00i4u_U9E6GmSbZbdtqdZI-RuUhR7L_68PNZljjGEYl6Bdbl19sHxbmjFphS3i4_ymGEFpyiE0y081d6hIC-jNHTMGHA3mC-4Ry9MJYvAOLRLzVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهمیدید چرا صیادمنش تیم ملی دعوت نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75136" target="_blank">📅 00:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علی رضا بیرانوند
با صدای بلند و رسا کف آمریکا سرود ملی جمهوری اسلامی ایران و میخونم.
مخالفا هم نمیتونن کاری بکنن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/75135" target="_blank">📅 00:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75133">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75133" target="_blank">📅 00:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75132">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6daymFM94Uj0dIOFVK1lm9KRdn7ZZbpUbp6R15l1mbp-UJOcesokQzam_0_8U6eE-_MAxETSsE36L1jgSMFqyii_FXHIMp9c9umSGJEZ_8DqXVqeLBhfhC0PPV6ye8rVeqyTrGbD7Nw0nNfdtePjqEGtwbXCseqnvaLKFYC2W4TlUs4FX-28dazCI5iA459WgVXpiABpkduVC6_46Z46erzlIEGbz7ZNTTa5_lTzmc6PN8JKPnRNkBx7E57JaAjv31fsoZa9Mykw8g-c9gA8fadTl7fpLFbYfrWuXam1_ISSWXRObuSk-Kt1NQpftCfWUPFsX7MiXN2d2sNasIDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی. این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:  @SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75132" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی.
این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/75131" target="_blank">📅 23:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnnkAB2dTMCbeWfb9rSrh5cY_er6mtwX3Sk4mRMVCeJl0dJpGTjHPGe--FWfphTjjf5LIKDf57faEyfEpp6VCLAy9K4-9Bu36sJsJPgJtLAhQPKtqJGs-NhP-flf6Y8QdkghSYcsa7PapoAusrG4_nNA8YanpPM9QVaCYhQ86AZpbGNd7GeFjKtGtNTFtaPuck_B1bM8LW_FUh10lVCkYr168GOtL09PZYY1daGzUajUebCIH2e6Eklyp_iJOS37h6Z5jX7hi695JfTFl3Ic6LGkjs2bIFdcIJgID3HkUElaWvQNrSo2pLG0a9eXYLjWug9_RdsXimsq1d-pfziabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پس از اینکه برای دشمن های فرضی خودش با هوش مصنوعی خط و نشون کشید اومد عکس خودشو شی جین پینگ و به اشتراک گذاشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.63K · <a href="https://t.me/funhiphop/75130" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75127">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ffwaC8VkBVPtrNmApAvsmSroLs9R8HtAtCVaI6VwIgmqDNrfNZ0stSVdZC4afTPP6NXsYBTve_bHzO1C-4BG1Gut4-ESwX0d3XVcK1YU0iVLDUdyIdkavcZQ1cOxvNVOHNhRBb1gqe-VkxduWmBBscRcnEsWVCcgyTaK9Kt4nU8Lb98HBVvLru5qWeELaR_zCf8aBcQyanioTXmeQgZ4dv-2ZMgKTnircv5KHi9R9myzuczpt0dH4WF5bqxkBoqs7p0vox4RbBCZrxyfUFVTQAc3vMsX2vkj1Dpmc2K0ZPcZ2yVybUw3riW0cUMLLBQOvz1L60nu3aOABfLMOIUtrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت رسمی کاخ سفید جمله‌ای از ترامپ رو با عنوان «شوخی نداریم» پست کرده:
اگر شما به آمریکا صدمه بزنید یا درحال برنامه‌ریزی برای ضربه زدن به آمریکا باشید،
ما شما را پیدا خواهیم کرد و شما را خواهیم کشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/75127" target="_blank">📅 23:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75126">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">ترمب: این آرامش قبل از طوفان بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.75K · <a href="https://t.me/funhiphop/75126" target="_blank">📅 23:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75125">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TVWmagmJMIP-KyMYT5FEP6LXR3fH-latix1nuV1EMf5pxZAYFXBKU4EERbf0ttC0fyFcqo6bXhW6hiVb7yT1oEPGXJQq-fX8u0vLImRYrTF1Oy5I6-abUoSNuEm7UlAmkaSEOcPZTiXxYEdNEYChNySZpYDJQQ0ty5LX8-uqqeOY_heAha32FSHUxb0U5CoP_osiUFe9jRfNimKDqXjQvUosiIz_iVmtiTcRl9-FTJnidJK-_yX6HR2sVks99V1ngyhnBu1FtyTWzb9yq1G__ctlOwcIMEwupFv-Xn0N4WxLH6UrOtPs05ZLlX30Xey6zGNxiU_299zuNP6JNm_tTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب:
این آرامش قبل از طوفان بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75125" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75124">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UDI2DpuNyhvMjRHaJsEKWs4ZUVXEcOD-pz033B4cU3BHrtlk99sginbIciSmVQyrS_eSeooSj0ujzKtyUv7Wy39UR18Lf1nVrRWUITK3-XSnvSiO2eKGtZAIyJVTV38eCjTbrXT-ABGmHn-LUl54vy85FJzg42Fijt5KmUrrbIKT-WP1yxXL6yiJebtj0JDh7wHvPd13QO4FUw-Ui8cIndgAA6f7sxCPo6Rsoe1emc2GOMRdVX1p37_1vAvgkFl-O25llyoI_hY1Pk6WT0jSIOv_5LbgDA6uyU3V3_MUc14_9yJaw_Tm43uo2sLvCiJcMJVADhJX3eXltoK4cM4o6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه اداره گاز اسرائیل از دستش در رفته و یه انفجار عظیم با منشاء نامشخص تو غرب اسرائیل باعث طلوع زود هنگام خورشید شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/75124" target="_blank">📅 23:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75123">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=NMo0PcSz1Nkk6o3qt1titGTr282J1UErwgjWS1IHPo5OqWTPSzR-FLwDZNQoTG-lutBP-XcbGp4HqdD_LkBHlDkgZUkhpTW9iDga0kOOx8YUv8k-ThJF73mtDrExyLFbWcrkRhQkDboq7SUgl9JCOMg9mcNRKZZ_7H9cC23x8FwG-QOts7eYhEdzStzjZhYtoZ0qqRAR-GqWtr2mvaWPnPgjg26t6lFeslmc9rQEXV-Hh5wA1_3rciWQ0UPl__7xzEAtFfwGNiF_UO7yG_JbhHxH8WHu5Ymor7mfCx4B8r4BQuzdhZj5_JCKo9RfHNOj467hK61qrAjh_BzFu3Dxpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=NMo0PcSz1Nkk6o3qt1titGTr282J1UErwgjWS1IHPo5OqWTPSzR-FLwDZNQoTG-lutBP-XcbGp4HqdD_LkBHlDkgZUkhpTW9iDga0kOOx8YUv8k-ThJF73mtDrExyLFbWcrkRhQkDboq7SUgl9JCOMg9mcNRKZZ_7H9cC23x8FwG-QOts7eYhEdzStzjZhYtoZ0qqRAR-GqWtr2mvaWPnPgjg26t6lFeslmc9rQEXV-Hh5wA1_3rciWQ0UPl__7xzEAtFfwGNiF_UO7yG_JbhHxH8WHu5Ymor7mfCx4B8r4BQuzdhZj5_JCKo9RfHNOj467hK61qrAjh_BzFu3Dxpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/funhiphop/75123" target="_blank">📅 23:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75121">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">به گفته خبرنگاران فان هیپ هاپ نیوز پدافند تهران فعال شده و درحال درگیری با اهداف متخاصم میباشند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/75121" target="_blank">📅 23:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75119">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">هم اکنون صدای فعالیت پدافند در آسمان دزفول در شمال خوزستان
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/75119" target="_blank">📅 23:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75118">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnakWeSVVndDRrbbBXXhlvRCQN_KNrOzUpv-_byfcjnpPzoNk1t4IXZvxGnxbYPnEDOUQzYvWtyfBikpxFQuB20knwelhveYK57PLtUa2W3jgTjBHhyhHX0Pv96qdPZCj7BaETUw7syYgDT6VlYBx4cm1B0HSJ8xtbPYcfKFz1BYuXctqygCBW-vi0OW9Dln29Pq8yl58G_LEVxtp_2MC5IQXAYh0NteGoE_GQizsczJggKA5F7GDV1abauG6mxlSshrArG22CR3miZS6tOrkWJcl3OYVXsw9KOI1F5QkPJweJ4t7Z7lxwi5tNoowbmuu_6KAlrONS_SofFBMUn52w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین اکانت توییتری محمد باقرشاه قالیباف:
جهان در آستانه نظم نوینی ایستاده است.
همانطور که رئیس‌جمهور شی گفت «تحولی که در یک قرن دیده نشده بود در سراسر جهان در حال تسریع است»، و من تأکید می‌کنم که مقاومت ۷۰ روزه ملت ایران این تحول را تسریع کرده است.
آینده متعلق به جنوب جهانی است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75118" target="_blank">📅 23:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75117">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رونالدو از روزی که اومد ایران دیگه روز خوش ندید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/75117" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75116">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">النصر فینال سطح دوم آسیا رو باخت و کریس رونالدو باز هم نتونست با النصر جامی ببره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/75116" target="_blank">📅 23:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75115">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">درود بر رهبر انقلاب اسلامی ایران
مقامات امنیتی اسرائیل ارزیابی می‌کنند که مجتبی خامنه‌ای رهبری جناح تندرویی را بر عهده دارد که با دادن هرگونه امتیاز در مذاکرات مخالف است و به‌طور فعال در حال آماده‌سازی برای از سرگیری درگیری‌هاست.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/75115" target="_blank">📅 23:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75113">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فروش ویژه OPEN VPN اختصاصى
🚀
🔐
ارائه سرویس‌های متنوع: • OPEN VPN • L2TP اختصاصی • سرویس‌های پرسرعت و پایدار
⚡
سرعت بالا + پایداری عالی
🛡
امنیت تضمینی و اتصال بدون قطعی
🎮
مناسب گیم، استریم، دانلود و استفاده روزمره
📱
پنل كاربرى حرفه اى براى مشاهده حجم،زمان،تعداد…</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/funhiphop/75113" target="_blank">📅 23:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75112">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHpvHFspjPFVF8g9yvdkfpgycbTZtAVruEmMTP-30QNowI3xXDx9ecFuAqiCa0IZxC6aqkdaWABYBeNaut5vuoKRUzBvy6W8wMeYSb9k43rcBnaot5qxZlPAdJFqQ26PiV3E-w7BQiX3dvQ3CwZ7lYfZGPlKZ0RjthZlSpiVZ8ErWk7SNe7rYjM2LaSQW9KfctV7GtQtPuwDhIHXbxTQUcz1mLDct5BnkgiE3QXldsfxXZtJu4-Jvo_qPjl12EFYbOPHRtokZM_I0E9V9JCA-P6qcIPB2F5WThIqS-2Vm5GP3NEYC-NeDKdrkxxiOGL4GSr8j3Tb6O4PtdgVVwafhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش ویژه OPEN VPN اختصاصى
🚀
🔐
ارائه سرویس‌های متنوع:
• OPEN VPN
• L2TP اختصاصی
• سرویس‌های پرسرعت و پایدار
⚡
سرعت بالا + پایداری عالی
🛡
امنیت تضمینی و اتصال بدون قطعی
🎮
مناسب گیم، استریم، دانلود و استفاده روزمره
📱
پنل كاربرى حرفه اى براى مشاهده حجم،زمان،تعداد كاربر
💎
تعرفه سرویس‌ها:
• اوپن حجم بالاى 100 -گیگی — 60
• اوپن + L2TP اختصاصی سرعت متوسط گیگی — 220
• اوپن + L2TP اختصاصی سرعت عالی گیگی — 350
نامحدود  ٣ ميل تا ١٢
📞
پشتیبانی و خرید:
🆔
@awsvp9</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75112" target="_blank">📅 22:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75111">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اینهمه خایمالی قایدی رو کردید تهشم سردار آزمون کیرشو کرد دهن قلعه‌نویی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/75111" target="_blank">📅 22:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75110">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مهدی قایدی با شرف هم که هستش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/75110" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75109">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به تیم فوتبال جمهوری اسلامی
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق‌نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قایدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپو
ر
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/funhiphop/75109" target="_blank">📅 21:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75108">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=QsrZ2tKLDvpzQ3u34jaqHWWq0RODTeZwubUNjgmSJvSHWpMH5yGYQk66AWKxI2HJAr_dGkMyAo1AXXlXp3zOJQi4iVi0H_vYwbaKRutceaz0pl6kRncC8GYgzme9_35_vue2yyh5pTiGSi5q2QUjn0tVzcM3b3JPjOfRfhDdtQTrVYGms9xDRuekzVjfsUa5BdPo7cAaOMKECuGRoQhupw7AjC_68W5wH08sv_AxAN-813mb97FUgIufNSyQuWCOIbXDwr90ViGeIuDtrssSmFX7T7I4UuYJ2yOlQJ3rNp0jAPboiS6izfXt3fcNS1dKhpBa_O8Q1qcC-dgXUQdGbA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=QsrZ2tKLDvpzQ3u34jaqHWWq0RODTeZwubUNjgmSJvSHWpMH5yGYQk66AWKxI2HJAr_dGkMyAo1AXXlXp3zOJQi4iVi0H_vYwbaKRutceaz0pl6kRncC8GYgzme9_35_vue2yyh5pTiGSi5q2QUjn0tVzcM3b3JPjOfRfhDdtQTrVYGms9xDRuekzVjfsUa5BdPo7cAaOMKECuGRoQhupw7AjC_68W5wH08sv_AxAN-813mb97FUgIufNSyQuWCOIbXDwr90ViGeIuDtrssSmFX7T7I4UuYJ2yOlQJ3rNp0jAPboiS6izfXt3fcNS1dKhpBa_O8Q1qcC-dgXUQdGbA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تروخدا یکی ترامپ رو متوقف کنه» قسمت نمی‌دونم چندم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/funhiphop/75108" target="_blank">📅 21:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75107">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">عجیب نیست دفعات قبلی کسی از حمله خبر نداشت اما الان همه میدونن دوشنبه قرار بزنن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/75107" target="_blank">📅 21:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75105">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yvv611pa7vP_GA5-cuwVtthpBU08x7II7p5JGQm7W30D-RUsSWl7CoAp3BLf3HON-PJmf_oGXYIgWbipesm3TKugqvGlDmD6nM9oOPaLacT5EWz2ORNoMDRfeeWR-ymS_Q4tVdDrzT167KKtD2Vy570pML2txsNTrEg_2cS_jywEn5jFZZehHxnhWMQeHcUz86vKO4VZV56ZEDh4Etx7io97snUoD_PRWZc2Banplc7_iFRhP6dWZFYGUi8XfZYl28askZW-I3DG7sr2j7qXbo7ZrvPrpyr3twK8MP2Ts6l0C5AvRDz77rWBc2Ei62YJryOEKuXIOCcOxasBjJBadQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بس کن دلقک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75105" target="_blank">📅 21:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75103">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34831ab3c.mp4?token=pH0Df0RNhG8hBagEX1rsJOOAIXAuDFCiL1qnvhNp7nuoPbD8cF1qi8Or2uqFyzLRyS5jYHkEh1i-ymwzn7Mw6aBJOvdK4BrRDRSIea0BVuP2WSE6lMx4Bu0e90PYYqvBR1Y2X_LGx2xbrr5KqBwo8rJpQLUEM-9YvwG_ASTwux_bYyf3Z-oCbpaZrc4PJmyfs_yWvTXSpb1KpMYx_BkAs25maEQgWQ0F1OYAOWy8zS_WvvOP7676gu_bsrrIL55dCR8GVx_1FQALaFseWS_vlwHMr7mHOAmsCZ_D8Rh5pvo7BxkNNElwhge90R80h7zN7qC1MONxMlDmupuN6HuR4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34831ab3c.mp4?token=pH0Df0RNhG8hBagEX1rsJOOAIXAuDFCiL1qnvhNp7nuoPbD8cF1qi8Or2uqFyzLRyS5jYHkEh1i-ymwzn7Mw6aBJOvdK4BrRDRSIea0BVuP2WSE6lMx4Bu0e90PYYqvBR1Y2X_LGx2xbrr5KqBwo8rJpQLUEM-9YvwG_ASTwux_bYyf3Z-oCbpaZrc4PJmyfs_yWvTXSpb1KpMYx_BkAs25maEQgWQ0F1OYAOWy8zS_WvvOP7676gu_bsrrIL55dCR8GVx_1FQALaFseWS_vlwHMr7mHOAmsCZ_D8Rh5pvo7BxkNNElwhge90R80h7zN7qC1MONxMlDmupuN6HuR4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه هرمز از نمای آسمان
🔥
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75103" target="_blank">📅 20:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75100">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یجوری خونه لرزید خایه کردم</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/75100" target="_blank">📅 20:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75099">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=g9BRAbvy9HD6fjzdutxEM4wj_S0JW2EuTs10oYFuc9Y7Az5sjiBmH3cgyZkSivgK7lTVMAIbbp8ATWGKTqiaoM7Y-bE366M3smeYk8On2zn1OZmL9gRzhcTwSlKdzs8RoKWab8VClC9S9D4JMujW2NfOnerjUMxfVOloSSy-Tbq-wZxyJtDC7w0d7EfP7a547h_6yj9qka-cAPUg3mlOKcs6UNnGbBwFbPvDw5dFLCqAw67lEqWob6JBxV2m3kiFJh-j5gIP6g9w8TLra8RWTyzqE-NNBeSb2XZEf52gQ0159X4J5VMTeDDKr9ZoISNAwzh4XB3fPHpXT9q6CF4z1rKEy5FUw5hgdlKJ-dCdgrCgaUoMkEgeexywuBOFDmvwsRUoCE8mq5wgZ83EdgpELKn2d_feOkD8I4Q4XZSjro_wLKTMrSWiYLxlMNYr3NwGIUQStrZydcxicnLH15fgQpT-4uWou2eRsQmP79NfPei_znWPoQNIeRkoTPO9DYcR2JcT6E_vYJVZGcFQxNDMo1UQ_p6oB-Ha-nMOO_wVisMkzRGF8rLJXUpNOwW-Ym-meXcX-d7qlgv5GkiNt7esbGdDJGf6jW5dl4Rk2ErwLylIuISM9kJkhmDWf2H-D1vbKlV-PkLaB907lDPFPZRadyo2adBccxFvBvqujwPr3q8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=g9BRAbvy9HD6fjzdutxEM4wj_S0JW2EuTs10oYFuc9Y7Az5sjiBmH3cgyZkSivgK7lTVMAIbbp8ATWGKTqiaoM7Y-bE366M3smeYk8On2zn1OZmL9gRzhcTwSlKdzs8RoKWab8VClC9S9D4JMujW2NfOnerjUMxfVOloSSy-Tbq-wZxyJtDC7w0d7EfP7a547h_6yj9qka-cAPUg3mlOKcs6UNnGbBwFbPvDw5dFLCqAw67lEqWob6JBxV2m3kiFJh-j5gIP6g9w8TLra8RWTyzqE-NNBeSb2XZEf52gQ0159X4J5VMTeDDKr9ZoISNAwzh4XB3fPHpXT9q6CF4z1rKEy5FUw5hgdlKJ-dCdgrCgaUoMkEgeexywuBOFDmvwsRUoCE8mq5wgZ83EdgpELKn2d_feOkD8I4Q4XZSjro_wLKTMrSWiYLxlMNYr3NwGIUQStrZydcxicnLH15fgQpT-4uWou2eRsQmP79NfPei_znWPoQNIeRkoTPO9DYcR2JcT6E_vYJVZGcFQxNDMo1UQ_p6oB-Ha-nMOO_wVisMkzRGF8rLJXUpNOwW-Ym-meXcX-d7qlgv5GkiNt7esbGdDJGf6jW5dl4Rk2ErwLylIuISM9kJkhmDWf2H-D1vbKlV-PkLaB907lDPFPZRadyo2adBccxFvBvqujwPr3q8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر USS Gerald R. Ford پس از 326 روز در دریا به نورفولک بازگشت که طولانی ترین ناو هواپیمابر از زمان جنگ ویتنام است.
در ژوئن 2025 برای یک چرخش معمولی مدیترانه حرکت کرد و مدام گسترش یافت: ونزوئلا، دریای سرخ و در نهایت عملیات ایران.</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/75099" target="_blank">📅 20:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75098">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!   دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
( فقط 300 گیگابایت موجوده! )
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin…</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/75098" target="_blank">📅 20:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75097">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">تلگراف
بر اساس گزارش روزنامه تلگراف، برخی مقامات و چهره‌های نزدیک به
دولت
ترامپ
از امارات متحده عربی خواسته‌اند نقش مستقیم‌تری در درگیری با ایران ایفا کند
؛
حتی تا حد تصرف یکی از جزایر ایران در خلیج فارس
.
یک مقام ارشد سابق امنیتی دولت ترامپ گفته برخی افراد نزدیک به ترامپ پیشنهاد داده‌اند امارات جزیره لاوان را تصرف کند؛
جزیره‌ای که اوایل آوریل هدف حملات مخفی منتسب به امارات قرار گرفته بود.
به گفته این مقام، حامیان این ایده معتقد بودند: «
بروید و آن را تصرف کنید؛ در این صورت به‌جای نیروهای آمریکایی، نیروهای اماراتی روی زمین حضور خواهند داشت.
»
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75097" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75095">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/75095" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75093">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
تخفیف ویژه زیر قیمت کل تلگرام!
دوباره تخفیف رو تمدید کردیم!
🧃
قیمت هر گیگ فقط 149 هزار تومان!
😈
(
فقط 300 گیگابایت موجوده!
)
💥
✅
بدون ضریب و بدون محدودیت کاربر
✅
دارای لینک ساب برای مدیریت حجم
🛡
تمامی سرور ها دارای پشتیبانی می‌باشند.
🤩
@TornadoAdmin
| خرید
🤩
@Tornado_Ping
| فروشگاه</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/75093" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75092">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">عزالدین الحداد آخرین فرمانده رده بالای شاخه نظامی حماس هست که با تایید چنین موضوعی (ترور) یک آسیب بزرگی به گروهک نظامی حماس وارد میشه.  اسرائیل تایمز هم گفته به احتمال خیلی بالا این فرمانده نظامی ترور شده.  تا این لحظه بیانیه رسمی از حماس, گردان های قسام و…</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/funhiphop/75092" target="_blank">📅 18:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75091">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o1AT1xD33iBvEYsuqHSUT4Iutzlos2DBycDj6wLtR1N48o0pQDpYydXOWZQiEN8EbIIwhqid3hl1MBsWol50GYpRp6SJT18mBvED8nLZVh9Sp22D9UqsqlogxvSlptYFjS2YmWxU4ZVh_pjlL4CBX-t9aSuFK0NxnEAvE-rrBrULmItASqYDIKrCaffmBNppLaIymEo-jiDSdeadIzV_ID7nLPG_Ph6COds5xIMy0Kp7nN75vivxdJVZhcTr08ChYhGVs6nUGkOfUsZ9RW1vQwjpScTq5yoHQ5Ndbf8lsvjJLlzUSVru49F18YeSrj-XY2LiE6CQjuNNiGCMdk7JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیتر چک مناطق محروم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/75091" target="_blank">📅 18:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75090">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">😵
بحران دارویی که راجبش صحبت میشه چیه اصلا؟ بررسی عملکرد 36 شرکت و 121 محصول دارویی نشون داده که قیمت 24 دارو در فروردین ماه بین 101 تا 3380% افزایش داشته : بطوری که قیمت پرداختی بابت بعضی دارو ها تا 34 برابر در یک ماه افزایش پیدا کرده.
👍
مهمترین دلایل تشدید…</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75090" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">از اون 682 نفر یکیش قطعا رضاست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75088" target="_blank">📅 18:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oWiaA4W_u2rZdV04CueT1dM3v_64Egj3M1ZGDbyTk0qEmpu_kVXpo0_H7Dyyc2a3-qA3b8VlPRWJsZsMdvAnlgWDx3CykDI-MxxxwKCJjAUavbv1Ewyot_JN7516b0Gyy0zqAaMQT_l-hDgsMNff4FWhwgOdd_3iY0pMYgHmFUGUi4I4CuL29EaOebZUdUk1YNtZDIkVskN6KME6BGhCzr5CZJGJf7EMNwRT71FJHXXvLCOJWll3syQLwbXCO8DO_BXsMxbRx3N9cJvgwax95o2zQNqkDKRZj6nwq-Vm0Msty_2mePqfILpTiHUIFZ7yZglOnHawWl1jGM-PgI-Z4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کله زرد:
شوخی نداریم!!! ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/funhiphop/75087" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75082">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">😵
بحران دارویی که راجبش صحبت میشه چیه اصلا؟
بررسی عملکرد 36 شرکت و 121 محصول دارویی نشون داده که قیمت 24 دارو در فروردین ماه بین 101 تا 3380% افزایش داشته : بطوری که قیمت پرداختی بابت بعضی دارو ها تا
34 برابر
در یک ماه افزایش پیدا کرده.
👍
مهمترین دلایل تشدید چنین بحرانی موارد زیر هستند
🖤
اختلال در زنجیره تامین و تولید
🖤
آسیب به روند تامین مواد اولیه
🖤
کاهش ظرفیت تولید
🖤
مشکلات صادرات و تجارت در شرایط بحرانی
😞
در پی افت تولید و کاهش فروش و صادرات کارشناسان حوزه سلامت هشدار میدهند که
ادامه این روند موجب تشدید چنین بحرانی میشود و امنیت و سلامت جامعه را میتواند به شدت به خطر بیندازد
.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75082" target="_blank">📅 18:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75081">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">فعالیت جنگنده های ارتش بر فراز تهران
🔥
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/75081" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75079">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پاشید جنگه
منابع عبری تأیید شده :
ایالات متحده در روزهای آینده آماده‌سازی برای حمله دوم به ایران را آغاز خواهد کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/funhiphop/75079" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75077">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dVEH16aNPUtI_kSQWcK6QA9yKujTQ_WTkonsD0p7FAgbEE598vbDHMgSGTxQTjb7SxjrgsNh2s6gQuauVE_e_jDGvqZNei1VicQblTXgdi-nKXLGO5N-QciERJgw5lYJv-Qpqy6U53_JnukIC2wWrUpRhyX_erebMkncK9IW2uVxZZCNRjoiBbLz2zZjvA5vXvPa6rHPX58pNaatjJOxZYudp_MtlThODqd7wpBdYRSlit_SkQJQMVQVtvsP6AO0Goc4V1EvuKs-QEmFzXZ7JP8_FN8RI2w9CtSNy__D0487N6d09i6rbp3Z-jnqyysYTrtajPkyy6UtkGHV0PFnlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OEwaMROtPPblYoVOBwB_qheELFSd1Dr1AcDs_z7PdoLpkOjHDO7a0kNXplAwM85SoXsET4zQ34Yegn0DetZl-rt43w3JkgXDLzdr6AS6V0J2DO7BZ3uiW6HDDCeKmRn5zsUlgAesfK_bHUTrLpQVmqHp6c0zQpr4uE_ytOTZ_AN1QPG2pdoBd47XNcNfYDwKx-LkpyGniBsZJ5T9lQpEWrxitMSoPsTndCAYspLTC8xyozY8XnaV4ksf6bpEH3qmDhvJnUQOtgtZxHRt4LLkhH05hPYLab2RRd21dq7mI1unKwdvjvKaNj6Lwxnhze-YwhHO7C7-l_mV2t0gmp2N3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر یو اس اس لینکلن یا شاید یو اس اس بوش امروز در شمال اقیانوس هند در حالی که توسط یک ناوشکن در ۷ کیلومتری شمال شرقی اسکورت می‌شد، مشاهده شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/funhiphop/75077" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75075">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">پاول دوروف
دوبی دوباره حسابی شلوغ و پرترافیک شده. از همین حالا دلم برای
«آتش‌بازی‌های ایرانی»
تنگ شده؛ چون باعث شده بود آدم‌های زودباور از شهر بروند و دوبی خلوت‌تر شود.
پدافند هوایی امارات
هم عالی عمل کرد. جالب است که اینجا با
مالیات
صفر
درصد،
امنیتی بهتر از بعضی کشورهای اروپایی داری که مردمشان
نصف درآمدشان را مالیات می‌دهند
.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/funhiphop/75075" target="_blank">📅 17:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75074">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">با کشته شدن عزالدین حداد، تنها ۲ فرمانده حماس از ۳۲ فرمانده که مسئول حادثه هفتم اکتبر بودند زنده هستند
بقیه به دست اسرائیل کشته شدند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/75074" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75072">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.69K · <a href="https://t.me/funhiphop/75072" target="_blank">📅 17:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75071">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/75071" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75070">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">😠
ترامپ
ابو بلال المنوکی
، یکی از رهبران ارشد فعالیت‌های
داعش
در غرب آفریقا و که به عنوان
دومین فرمانده داعش
شناخته می‌شود، در عملیاتی مشترک آمریکایی-نیجریه‌ای
ترور
شده است.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/funhiphop/75070" target="_blank">📅 17:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75069">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">سنتکام
تا امروز، ۷۸ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/funhiphop/75069" target="_blank">📅 17:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75068">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tRQpFnkrTwBRytRaCqHfaHBfN9A_L9aPJUXiQlc03hAU3glqNE2ZHAJRWiJnqbo6chFAUHSlGHFv4opMO4dq3rcBS-dSkXaZBxZY6UxkRp6q9Ty7SAxziVweCLEHTsa3ElByn3jZLT_phlGp2yQXtyiD2TZZtFzzbyzLNRcP5GRYS1TV18OSIj8GyGbQfWKsPrb2R9l5eXXYWuIOhbyvlnVesBzc6KdyOC0xqJ_D7KAZ4wRFiN-IP6y4mPihgv8ZDKi1IAMDhyP0qicyvJBiOJ199_J1KktcqX6oGS-ydcpwtg4GpaGmiNqixgTumOrIh2fAGSEm0CiELEPx1SLhPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده باش آماده باش
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/75068" target="_blank">📅 16:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75067">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCC4PUucuuZqhnUbi-wL-fNiHqPu9Yc4WZE97Rgz7neVdjIqQlSmjFECHbLsVYTvyDR5_djMfm4DrtnPJqBX1FaMgxFRVET-VKJtd8wsY64IqvLJn3h_yfRH0CZVSeFelG5V4qh0Z8OEmHDEEsj9SQQi48x4g1UHCexT8FytJgkyDmqqG0gWviX28I_gahNcmaJJXZmJaOtzD_mofReWz2HM4C0ehzEN3uly5ouj93bSVKn26jhwXkHN0Gz7yf-6f3lsuXwjpEtzm-B7jWHg_PTbq_D_zkJrx-nZlQhRjGAEmBM9LD4mfKGwXIelPYTT9FkJ893awIbcg1jXZd2wLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75067" target="_blank">📅 16:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75064">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/funhiphop/75064" target="_blank">📅 15:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75063">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMuJgnV0S-9GOe1rFEdYewykAjiO4lw3lsWeN19m692gIM_Tbw1uuGXYkgVw5dlPHOKmiRsb4qs408ClabwKkNC1nFNqWdmeni-z9Fzc25w2WtU6RhA56TlCfv94gQy-aek07tCKl18XRYtOLtXrT-bs9X-WjJWUQLAlEBQug_p-ldzX85XoC7gR4_HYTsLJe0242Xc4AJnzgQItCAkkjn1vmk-fY0rKO7Zt5VkeX80FsYesPF4wrz5o1icg-MmTsZLjxL8bsJeo55PD8a5WLH-hQT7YGmTCoemuhFkDjEpRNMPcxNnemm1fSEIIlf9Nga9yWYCDhv-6Mcru_B3CoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/75063" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75062">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">قبر بهار شاه‌مهری، جاویدنام ۱۷ ساله نیشابوری که در ۱۸ دی‌ماه جان خود را از دست داد، در روز تولدش توسط افراد ناشناس تخریب و شکسته شد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75062" target="_blank">📅 15:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75061">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">در همین حین که رسانه های جمهوری‌خواه معتقدن آمریکا جنگ ایران رو دوباره از سر میگیره، رسانه های دموکرات میگن ترامپ دنبال یک راه خروج از جنگه و نمیخواد ادامه پیدا کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.52K · <a href="https://t.me/funhiphop/75061" target="_blank">📅 14:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75058">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بارسا داره یه رافینیا دیگه میخره
ژائو پدرو مهاجم چلسی</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/funhiphop/75058" target="_blank">📅 13:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75057">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wlre37W04EW-BVvISvDHHdamKAMNDmp_e87n8HzhsxUApxfWiKzL1C_EdY79_dqQaaweoNTaNSNmxHJ33S0byIttJ0jM_pvN_VuQ9lLdt9FGzVu-jAqZYIWEhRfGCoQGg0eM0sKzdOEE9JRWiHSKTlJMUWZANe5W8j1_FNc2PkaoHVsy6z5CagVWCqfxm2aP3WtpByUQ0Sw2oso59xHCItN30MGM0CPQxOe3gwRQBfvxaEdpxZ7WLhBU9ocUJklWW7kzNvzKUbNfSypsKJgDsym9gs8Bbl9g5ZQuJrTngT_7WpAuYzd7m-CqEdJqI-UMddx42Z3gLhdmUCtHZWlV0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی محمدی مشاور قالیباف :
ای لشکر صاحب الزمان آماده باش
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.78K · <a href="https://t.me/funhiphop/75057" target="_blank">📅 10:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75056">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">رسانه‌های آمریکایی: ممکنه دوشنبه جنگ شروع شه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/funhiphop/75056" target="_blank">📅 08:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75055">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">جسی واترز، مجری فاکس نیوز:
ترامپ درحال آماده‌شدن برای دور جدیدی از حملات نظامی به ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.56K · <a href="https://t.me/funhiphop/75055" target="_blank">📅 08:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75054">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">علی یک تنه ی پایگاه رو با سیگنالاش پولدار کرده دیگه شبا نمیرن تجمع بخاطر ۶ تومن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.62K · <a href="https://t.me/funhiphop/75054" target="_blank">📅 07:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">فعلا برای هر معامله ای چه خونه چه طلا چه دلار و کریپتو تا اخر این هفته دست نگه دارید ببینیم وضعیت چطور میشه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/75053" target="_blank">📅 06:54 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">از ساعت ۵ تا ۶:۳۰، چندین پرواز در ارتفاع پست توسط چند جنگنده میگ۲۹ و F4 خودی در غرب تهران انجام شد، که صدای شدید آنها در بسیار مناطق غرب و مرکز تهران گزارش شده است
تا کنون دلیل این نوع پرواز در این زمان اعلام نشده است به احتمال زیاد شکار پهپاد متخاصم(انفجاری گزارش نشده است) یا پرواز آموزشی بوده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/75052" target="_blank">📅 06:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75046">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">درس امروز اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن هر دو از یک میزان ضریب هوشی برخوردار هستن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/funhiphop/75046" target="_blank">📅 04:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75045">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">درس امروز
اشخاصی که پرچم های
🇺🇸
🇮🇱
میزارن جلو اسمشون
هیچ تفاوتی با اشخاصی که پرچم های
🇵🇸
🇱🇧
🇾🇪
میزارن جلو اسمشون ندارن
هر دو از یک میزان ضریب هوشی برخوردار هستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/75045" target="_blank">📅 04:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75044">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OAL345a8Qal7_MV4FMBy7kOk5eL2UtsvQ5nLlC4jeUlKeP0sr8GOaYg4FndT1n9yEg4S1_jpETl4tnppv-zpbZ0-UQ1G0ivteF-AG6mKoEkOEUeYRrSUPxu9bNIpeuiE_IZpHRXBW7Tou4GtPhrVd1-aN3LPwA2N5cqOpkYxcCAoaWLaRLAUfTUjSPooKMNm6JyKcX9WbA5dFl5bkv0wcdhThT0zcE2Fa0MPGsW9KznpVX858trnxfdiDadsDI_Tsj6J2imQM-Vp24iWu33zfiNkWNzVhmzeVcedGbENQd2_xEc4a8FMgvWcPPuJ6wWY-mz3VHhjJQI24oNLZ1vxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله
جدید تایم درباره دیدار ترامپ و شی جین‌پینگ
دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.
حتی اگر توافق بزرگی هم امضا نشده باشد، خودِ تصویر کنار هم نشستن ترامپ و شی یک پیام مهم داشت:
دنیا دارد به سمت چندقطبی شدن می‌رود
.
👍
🤯
چین با قدرت اقتصادی، صنعت، فناوری و نفوذش در زنجیره تأمین جهانی کاری کرده که آمریکا هم مجبور شده با احتیاط بیشتری با آن برخورد کند.
خلاصه
آمریکا هنوز قدرتمندترین کشور دنیاست، اما دیگر تنها کشوری نیست که بتواند به‌تنهایی مسیر دنیا را تعیین کند.
👀
😎
مطالعه بیشتر >>
لینک
مرتبط با مجله اخیر تایم
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 7.02K · <a href="https://t.me/funhiphop/75044" target="_blank">📅 04:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75042">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.  @Funhiphop | reza</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75042" target="_blank">📅 02:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75040">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ببین اینقدر این هکرای چینی خطرناکن که آدم میمونه چی بگه
جدیدا رباتای چینی زیرپستای فان هیپاپ (
💞
) میزارن.
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75040" target="_blank">📅 02:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75039">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_JEn9ri9lKqAoab9QTcwwf-1nLB3k1V69s30e5HznyR1IhTHsZKSVyNp8Dh6rtAiq7IFUOQLGLJrTUrp5mGUXvcmcyS_F0o4h-Dgyr-137U2ZPvBE9Mur-5ho6q6yItZE--qxHlta2IF6Qz_R2cqZSS7cFcQeAPjNRjIElJzE5XnNMXKXZea2R6xHkQnSNO0LR56HvJIkEBsOOhGUizkuXvH5o8KLU8CjXmmSth6hBMQgfu4ThhYFybT_nRmuEoKqkWvJ7UiBZ3imEyHKIXeZ4jUdb357yw5TcvaZ2ZIPOdffFtloG7hqkoS0q3eAW_VWYYmPWQUhpLCsHb_ru0hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید از آلبوم دریک حمایت کرد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/75039" target="_blank">📅 01:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75038">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دست مغول‌ها چهارتا آجر میدادن تا الان اسرائیلو نابود کرده بودن
😁</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75038" target="_blank">📅 01:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75037">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تایوانم پوشش بدیم؟
@Funhiphop
| reza</div>
<div class="tg-footer">👁️ 7.1K · <a href="https://t.me/funhiphop/75037" target="_blank">📅 01:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75036">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مورینیو:
سری آخری که سرمربی رئال در الکلاسیکو بودم ۲۵ تا موقعیت پنالتی داشتیم هیچکدوم رو نگرفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/75036" target="_blank">📅 00:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75035">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">مورینیو:
خیلی خوشحالم که این افتخار نصیبم شده که سرمربی وینیسیوس باشم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/75035" target="_blank">📅 00:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75034">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">فوری از فرید رومانو:
مورینیو سرمربی رئال شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/funhiphop/75034" target="_blank">📅 00:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75033">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">[ Fun HipHop ]
pinned «
رئال بازی خودشو برد و یک قدم دیگه به قهرمانی لالیگا نزدیک تر شد
🔥
🔥
@FunHipHop | Farid
»</div>
<div class="tg-footer"><a href="https://t.me/funhiphop/75033" target="_blank">📅 23:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75032">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ65u3LWQR_d4NBNgrM5NX2wfeRcGSP85GC5en9QjlelE1Ww6Gko21Ll1gp9GQc8m84_l7mojv9IprG3oj4xhbxrh9WgDSjD-LttkN2aVVALb2p8t4WCVoCa_E1YcI8da0X52Tqz-UknC0NTrXQfbhZOEUV7ugiHsML_CcQ_Sx_iWWCNANOPGYege_YobKzvjVOs52Xo_72G0xrPtHKgXhly3jOPOPtFSaxXeiQXUhS5Jem9LT_fszciZ30eMTEGbe6dG0892WO0WjClVXRjaHCVbPAfrdtkEEuoPnYxESWLk79Ricyev4pJLDi2Phsww3nDhclEOvzgxusfjJB5rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">د اتلتیک: راب دیپرینک هلندی که قرار بود یکی از داور های VAR جام جهانی باشه به دلیل تجاوز به یک پسر 17 ساله دستگیر شده و از لیست داوران جام جهانی هم خط خورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/75032" target="_blank">📅 22:49 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75031">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بیایید بالا دلقک شدیم.
هادی چوپان: ما با زحمت و هزار دردسر به قله رسیدیم، نباید بازیچه دلقکان مجازی شویم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/75031" target="_blank">📅 22:30 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75028">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JPMxqvpUbogtWXvqk7-o_b5mN-wZsjqNZIvNC3WBu6mzUskeni8UzvHaeliZE0DljhkH6_24p8w5lR5_4kKc3GqCk2oRjeamWKJSd0RH4Kb1UlP_VuOn_nF96sl_NQlCREZ4bZyi-D3lXgfHvAm_R9L8DwWV9jcpTXgyjlB3sxkQxGmCSD3fYseI0jUwi5PD8uC2hQwu4Kc38Esi12jZ0tU4OFEZ8sUp4sGbYaZzD4dhat_EVWQQ2aE7_-ER5KuH5xvR9NzvRmrs5XSXk6ozB5yhIjuPQSgSpFaFMexZUfGa3ccRXAkSGMnUvBe94zOF_Mv4En10_CDSUXcjefMKJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/funhiphop/75028" target="_blank">📅 21:48 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75027">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/funhiphop/75027" target="_blank">📅 21:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75026">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">گزارش های تایید نشده از ترور فرمانده حماس
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/75026" target="_blank">📅 20:53 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75025">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">امشب میزنن</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/75025" target="_blank">📅 20:35 · 25 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
