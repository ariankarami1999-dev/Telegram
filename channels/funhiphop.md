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
<p>@funhiphop • 👥 149K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 23:31:51</div>
<hr>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فعالیت پدافند در اهواز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/75199" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">محسن رضایی:
ابوظبی به عربستان تعلق دارد؛ امارات ابوظبی را به عربستان تحویل دهد!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/funhiphop/75193" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کی بود میگفت اروپا اینترنت وصله؟ اونم بزودی قطع میکنیم
خبر مهم شبکه CNN درمورد ایران
:
تهران قصد دارد شرکت‌های بزرگ فناوری مانند «گوگل»، «مایکروسافت»، «متا» و «آمازون» را مجبور کند از قوانینش پیروی کنند و از شرکت‌های کابل‌های زیردریایی حق‌الامتیاز دریافت کند.
همچنین، اپراتورهای بین‌المللی به دلیل نگرانی‌های امنیتی تلاش کرده‌اند کابل‌های اینترنتی را در بخش عمانی تنگه هرمز متمرکز کنند، اما مؤسسه تحقیقاتی «تیلی‌جئوگرافی» تأکید می‌کند که دو کابل اصلی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.86K · <a href="https://t.me/funhiphop/75191" target="_blank">📅 22:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🤡
د فیلد مارشال ماحسن رضایی
آمریکا یا شرایط مارا میپذیرد یا با موشک مورد استقبال قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/75189" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGodZillaVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAiKljxwkHHbWgBln1lbFsFwCLjsM9hWRARBB1VSJafIL7oQqLjrotfUfS8a6tt20oSKjMnbmo5veV8SBKP015VGidHZ3sATUmEWLaPlXQXz8DIPsiIf1V1nbHJVlsYXdElXaG9KiD4MV7HzWY1ag_82AJg87f6Ruy_tquTMK2cma37ronCQwzfxqy9YdNdnzfPkEGF9mfpDCfsd0elipC4d6HaEMpHdZ7Ms961gkkN9BBScxyStVwtcDQbnYya2fnAPKhL6Zx1SgM2hFQ9mhQQMQRp4WHUx5XNEDewSvHconEdjRnCRQIvjrXJWXwQOB2OfdCbOfbmLa4QjD3maZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➗
پیشنهاد ویژه خرید سرویس
🔴
فرصت ویژه و محدود !
قیمت هر گیگ برای ۲۴ ساعت فقط ۱۹۰ هزار تومان شده است.
و همچنین یک سرویس
1G
هم روی سرویس های 10G بصورت هدیه دریافت میکنید.
این آفر ممکن است هر لحظه بسته شود، زیرا ظرفیت محدود است و پس از تکمیل، قیمت به حالت قبل برمی‌گردد.
❗️
پیشنهاد می‌شود در صورتی که تمایل به خرید یا تمدید سرویس دارید، هرچه سریع‌تر اقدام نمایید
تهیه آنی سرویس:
🏪
@Gozilla_VPN</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/funhiphop/75186" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ گفت من یه پیشنهاد دیگه دوست دارم از ایران دریافت کنم که حمله رو انجام ندم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 2.74K · <a href="https://t.me/funhiphop/75185" target="_blank">📅 21:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید  هرکی درست بگه یه جایزه پیش من داره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 2.68K · <a href="https://t.me/funhiphop/75184" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید
هرکی درست بگه یه جایزه پیش من داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 2.87K · <a href="https://t.me/funhiphop/75183" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک فروند هواپیمای ترابری VIP C-37A نیروی هوایی ایالات متحده که حامل مقامات ارشد نظامی/دولتی ناشناس بود، حدود ۴۵ دقیقه پیش در پایگاه نیروی هوایی مک‌دیل، مقر فرماندهی مرکزی آمریکا فرود آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/75182" target="_blank">📅 21:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=iOX-XuOU32QXiAGLyNEL3iHSuNFT38Fl_QTcXHA3SoGK41QAcB9sUnW66ivE1slDVedYHaD2WO9xOtdPadT8WO5kjDlmiscM7iD_vb42_OJ_waBIoHTEkEFAzo9BT1kv2U8e74trEBp-YguSi52iJpqlZ2thQ0J1yhqyXUtF1TmRKbYSJt_D6OIVAcbqZt2TK7yFlx8tquW5jRdvn20U7dUhIfq0zu1aMw-uO32SXJWEe_67yCohU6FtoBq_CX7cP0GHMt3lmRR05XQcCtLeVBB5BxandxV8NM2nZl5L2zG5PsIPjQwhbPOr4GQBQTtR-HBMOK8VvtiMpvVQtAqhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=iOX-XuOU32QXiAGLyNEL3iHSuNFT38Fl_QTcXHA3SoGK41QAcB9sUnW66ivE1slDVedYHaD2WO9xOtdPadT8WO5kjDlmiscM7iD_vb42_OJ_waBIoHTEkEFAzo9BT1kv2U8e74trEBp-YguSi52iJpqlZ2thQ0J1yhqyXUtF1TmRKbYSJt_D6OIVAcbqZt2TK7yFlx8tquW5jRdvn20U7dUhIfq0zu1aMw-uO32SXJWEe_67yCohU6FtoBq_CX7cP0GHMt3lmRR05XQcCtLeVBB5BxandxV8NM2nZl5L2zG5PsIPjQwhbPOr4GQBQTtR-HBMOK8VvtiMpvVQtAqhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/75181" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آکسیوس به نقل از منابع خبری در دولت آمریکا:
نشست روز گذشته تیم امنیت ملی آمریکا با حضور ونس، ویتکاف، روبیو و رئیس سازمان سیا برگزار شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/funhiphop/75180" target="_blank">📅 21:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjolbI4a334mllpP4QTj8hGWWieF_pKfy3cf4Bh39vN-br9whIeVkpPpwC2IR85s11LZKtLYfaFL1XRX2pH5tNdKIJClXJSVbSz8f1P0DfEyCMW9wPaIk9XOQPgt9zF8K4hgJZWq1YGae472Rv_VWvLETP_dQxc6TxO97MpYhrUnJBOeQsNo8k7m262ExBmgwl7beM_D5zkDhDCCypdSsxhgAIsaL1DQMydhQbcUNOIldlb-l1Y6pu1Ppa7BmCXnvwOKA33tZIif0-m1fb-BSPKH-RTM4qLParM093e8cTWVEEkDmcsiVcMeKmKOAgv7vU_sVv4xyg2xvbY3Uzbzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47 دیشب : آموزش کار با pkm امشب به حول و قوه الهی: آموزش لانچ موشک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/funhiphop/75178" target="_blank">📅 21:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75177">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/funhiphop/75177" target="_blank">📅 21:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6kNN9FDMUpMPPiSaNbyKteQBUFyz-eALnfIRFTSL0zXSGJu9r_j7tzvn1nRIhPiWcuchmiPEVQbZSQI1EnNX3GU_QFK_1rre5mAPQvGSRWyG4uFZCl2BkU3I2KfdUd7dPSKJiRlpCUcFo9uwYkGxG6AY8nXLPXNq5vyPm-U7Sn_r9Kp6ZrSDtoc7ToMg2vd36SHvbbWBUDawEb2BBEwqv9PCdLKqfyIMiYfHgoiOKXHkYeoe58vQsf77EYsnTT5Ia2d1eozG9ErxfcgOGRbYw5N3UFNUk3zvpsbwBx9nBcKoeRQg6SA9oqchpZhLNbxPlwuC4vXBAQ2jvQbX2Fy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/funhiphop/75176" target="_blank">📅 21:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75175">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی: انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/75175" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75174">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی:
انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.96K · <a href="https://t.me/funhiphop/75174" target="_blank">📅 20:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75173">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یک سری رسانه عبری:
ایالات متحده و اسرائیل سطح هشدار را برای احتمال از سرگیری درگیری‌ها در ایران به شدت افزایش داده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/funhiphop/75173" target="_blank">📅 20:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75172">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران باید از من بترسد و مراقب باشد.
ما منتظر پیشنهاد ایران هستیم، اگر ایران پیشنهاد خوبی ارائه ندهد، ما به آنها به‌گونه‌ای حمله خواهیم کرد که تا کنون هرگز نکرده‌ایم.
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 3.18K · <a href="https://t.me/funhiphop/75172" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75171">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJBAkhexUF4n_mO9dbtxXZf3XoGlwjwr2zKiY4xSn2xeBBjCbe0Jd7NPXK2YNwB_tY3_iiVj6nvac8Ii87SvGCoyvW7rg8V6jpCuTp1BahnGeEdJFDm5rbdXX4HsxqOYkTAHuBd4n-OiiRlqFn5a4dGktFVY4aqqXo1VjRVUzVNVnm0ZJR1aY9k5UB7sIUMVJ_UeZQX6xP-M0aZrqWEVpmE-4G3TRxgTPcn6VOx1lTEUgc6qzS6dR9mus-hY-JUV8TmR3iJ7BrcKAZFRejh9swjG36zqBvY2BWWUEsUO_5IiMds4ONgg1BwJb8JAkrA_8KIaS4JVNNY9PSf0jSFMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ساعت برای ایران در حال تیک‌تاک است، و بهتر است خیلی سریع شروع به حرکت کنند، وگرنه هیچ چیزی از آن‌ها باقی نخواهد ماند. زمان یک عامل حیاتی است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/75171" target="_blank">📅 20:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75170">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5ZpnY-hFAhCdo3reOK7OFgCVC3C1Gl8wMVrHcSt4c9pUmPg4ja_5Ugro5BdXUohD0lR4MMFbxCFBOjAYCMC_gZlWRBJbigy489-rytDHylE-rxPr96TGDd1oK67jaC5MAdemesRXX0MN5gAEeTfWxRHtgFFrpQw8cEkPUXQR0rv1p0BexkPKzw42vd49FdCC7Jh4yMeRZofEQDR6YStIdEv3z66yMuglgBsn7AH1k_XT7_HSKMhxaFVdP0lbOesgbbdJjm2HVQB0_tS0aIMmGXYuM5y6MXgF6lB5CZ3xQPwiPpep2CyzaBvzG1H-Vkt-9zCKUEdaTOlNe5Yll-EKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکه خدا لعنتت کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/75170" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75169">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">‼️
یه جای جدید هم پیدا کردیم قیمتاش مناسبه میتونین چک کنین. هوش مصنوعی هارم همرو جوابه هیچ محدودیتی روی سایتا نداره.
◀️
یک ماهه  گیگی 170هزار تومن میده همراه با تست و ساب اختصاصی
ایدیشون:
🔴
@Plus_vpnorg
ایدی کانال
🔵
@PlusVPNorg</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/funhiphop/75169" target="_blank">📅 20:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75168">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اکسیوس:
ترامپ و نتانیاهو راجب ایران گفتگو کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/funhiphop/75168" target="_blank">📅 19:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75167">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">وزیر کشور پاکستان:
پاکستانی‌ها شبانه‌روز برای موفقیت دولت و ملت ایران دعا می‌کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/funhiphop/75167" target="_blank">📅 19:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75165">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hVmw8tJg7jldo45xDT3OUJTw_u93fdv5aOmd112Yonpoij3oB6eu4JghNJr4hP21VOtYeeWIhSIDGl0dJOCz_68rj2vIQlkg7bIlZwnYXo3wa_EQ2v7S0AXwc5AWQbLv0JnRO9wngeK4eKtAcF3VweoI6qHrcfaTvhbc6_Lb8nNQ9e9l7HeM0LeouLiZia1UTS2fdexQtDFIKlsCzqS6JHw1q3Zum93CL41hfjf8ZxrXJjEwad68H9VH1VqoKw4Yl_JZbccphMZB5ov90RfozvxAH3TfbJZeUXI1lwHcEpzFRAolfekb0gPfQcsxri01xM6ocS8k-rTzRqQqzeMulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WJ3WRV8e0QhQhhh0KS6_IGoCsI_rlqXaERt8Ry-hynPo0cZz2eCY4IbzCGgOnfFyiQevpOeOyroeyN57wEFTQxPCJSBHdhrrn7d01mwBXqD9D61NvMUHSJF99-eLOCtHqVJIWqb8Cx3yYzDaIWcHaIJFbFpaDummYOZ-FuT3MKyPTyzguN-fvbqUcB_NSBzqJL0g7sVi3KLvwZWiF4WS1Ie4nHlYWwsTh52jXS0-Kz0Vj6ZujuI8W6Fb3_1-5rRNiz2B8tvipxCf2we4wYO87W2PMh2f5tI5JKI2psdR0Y1u3LzyUMV8sueobh2STu18hACdC-s0H9cVgDGkpX3OzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آنالیز تصاویر ماهواره ای نشان می دهد ناو هواپیمابر آبراهام لینکلن در فاصله ۲۴۵ کیلومتری از ساحل ایران مستقر شده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/funhiphop/75165" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75164">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=Jame0w_aYmj-5O1m1ENrGKjlWh7G7z6iGCGxpjFaFqWqyYV_wqOZ0DInya6G7gBOw4e0N1goMvEddGv28-qMfdYPAFD_sCcRfW6e-lEX5NXtOkjPrIEhelPMgRRBEhNNXtZsp2uStjWdZElfXlrg4I_zU_48TpR8wkqjqtkBHAT0AhNrnh3oqLi0aHzJDGNeVvbvvFjF6KGRaa7D50_lf8Mk4OBGCjiXtPO_hS5MSYSo0Cdikz5VVALOTNUtEL2YAYHbK9asDEB6H1BEVVNIPRpEBMmdVJx7dGGLYOJwcSLbYpezNZ-G1xbHR6JlHIoBzX6EaJbkN7j7fbqyWKNOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=Jame0w_aYmj-5O1m1ENrGKjlWh7G7z6iGCGxpjFaFqWqyYV_wqOZ0DInya6G7gBOw4e0N1goMvEddGv28-qMfdYPAFD_sCcRfW6e-lEX5NXtOkjPrIEhelPMgRRBEhNNXtZsp2uStjWdZElfXlrg4I_zU_48TpR8wkqjqtkBHAT0AhNrnh3oqLi0aHzJDGNeVvbvvFjF6KGRaa7D50_lf8Mk4OBGCjiXtPO_hS5MSYSo0Cdikz5VVALOTNUtEL2YAYHbK9asDEB6H1BEVVNIPRpEBMmdVJx7dGGLYOJwcSLbYpezNZ-G1xbHR6JlHIoBzX6EaJbkN7j7fbqyWKNOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/75164" target="_blank">📅 17:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75163">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCY6YmJGB0VOPTnaKsfk_FRJkMXwwAOK_jRmbPubSEnYMT1d40fcBFumJJ-lj-ELRZl2pXpXgjt6LUoRryhxygLuAzMHrDLZ2PA_emmJ3YB4tiWYANIg0HtLAkLNPtuvSl4VIOxvT9-7E2GZrQxxaNcrsUZQhsMYTImIufx_e0UOnxXZY7HHzpUsQub3pkvo3-1UkH68g5XJRC9VvPj0FgraFfuerB9D1OCKHERHXyi3QGDcLbI9KeHqq5XoaFAmooj9VkaVDpZmMXnFw7MwxEDIA3kzAzAqwNrclk4v6Crk7W5FmkZ6QukvmH4kSppddpCVIQMgiyyIObrTBMXSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/funhiphop/75163" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75162">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این بدبختای فلک زده رو کی میزنه؟
وزارت دفاع امارات:
ما مورد حملات با ۳ پهپاد که از سمت مرز غربی وارد شدند، قرار گرفتیم.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/75162" target="_blank">📅 17:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75161">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پشمام معین قراره برای آلبوم جدید دریک آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/75161" target="_blank">📅 16:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75160">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">خبرگزاری فارس: وقوع چند انفجار در امارات برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.88K · <a href="https://t.me/funhiphop/75160" target="_blank">📅 13:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75159">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">خبرگزاری فارس:
وقوع چند انفجار در امارات
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/75159" target="_blank">📅 13:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75158">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">فارس: آمریکا هم در پیشنهادات خود علاوه بر رد شروط ایرانی، پنج شرط اصلی هم برای مذاکرات گذاشته بود: عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران عدم پرداخت…</div>
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75158" target="_blank">📅 13:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75157">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75157" target="_blank">📅 13:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75156">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">عباس عراقچی در کانال تلگرامی خودش اعلام کرد که کتاب ‘قدرت مذاکره’ به چاپ پنجم رسیده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/funhiphop/75156" target="_blank">📅 12:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75155">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ژابی بنده خدا رفت چلسی
از اونور رئال و بارسا میخوان چلسیو لخت کنن</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/75155" target="_blank">📅 12:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75154">
<div class="tg-post-header">📌 پیام #66</div>
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
<div class="tg-footer">👁️ 5.81K · <a href="https://t.me/funhiphop/75154" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75153">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">😂
معاون سازمان بورس
بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها در روز سه شنبه بازگشایی خواهد شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75153" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75152">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJWPRTvqaVQMQ6vPQqv6UwEBhv1tVVWjv-NVzSkccaRmoOFwj2ot6Tox8bJWB4jOs8SdGo_s2sWGLPs2MfEVQaY15P_cbZiXrMBGcpwKYqjH4p5K8ScBUg9QhzbsxILn0I9rZDl35QpsFoiBn9X-bC142cfa9hFXXFTT4I_b_rKAOaljHv6zlgjmqkVBJoxw_ELoh8xEJ0XtvqrIJ1912VoJbOvKbj8eRWLHiMFStJrr5PSIswiiVooTx3BqyBD0b69w-q907elXneClGK6Fh3pyX1SFHBNWyOiN4BPcsm_ArJDTtSn_aTCWmOQWGygOS6VARrlQeBmJvFlkaWjnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ روسیه در آژانس بین‌المللی انرژی اتمی:
کارشناسان غربی معتقدند که ایالات متحده و اسرائیل ممکن است در روزهای آینده، اگر نه در ساعات آینده، حملات نظامی علیه ایران را از سر بگیرند.
اگر این درست باشد، به این معناست که آمریکا و اسرائیل از اشتباهات راهبردی گذشته خود درس نگرفته‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/75152" target="_blank">📅 10:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75151">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3jkgHSFlsvKzhbpqZBSfxzZkluPNDbjmRO-NSg8tTryGSXGsYFQQgbVKebH5vo3xfoNrkpePLHONo8BIGsN4vdqn6zdSEI_-NfoM8IpH4K07MWATLGmbyTd1i8NgpNKXNIA1GF_cIWgtjgj9RXT9_OrLXQm6vmD2mOiS__E3Bw2HpiHjMh3JlFJRDnR9uWFaQI9SYRz-weONKOB3NYb8EOfzzz2dyk7tJOpZRJkgzs8yimehBiMDBoh0x4kKfmldgaxofnngd3cdnWhf5klGGXKAMA4qvIJW4TX-I2mvbzuuox_k6e5cdBekzsaJBks3Mf1IayrCjGu5InBGthu7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید کاخ سفید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/75151" target="_blank">📅 09:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75150">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nL8Gy_KMkgyve-yXlaluXaG6BoEmh-02gaZ-8g8XrUnv0PRB9_XIfniC6Mpl8nj5BYehQOGQK3HzB6ZTuSDm6xoPtouvZOPZjUqyURh80OoF6EACFUHGjfBWBXLGsGbns0-5b2HwubjKm0YpQ6EeNb99gV5hterMHblLnkOcSreiNtat28eo_H4dDCDKGn7uysinJnJNEIKRKRAPJVayn3QdRmBCmnCDwyKPsvKQ8uBiQQwHWLk9E_nCqWAeQywIih_WAFSu9FSqkLZ-Xxy-efI0DcQks0qRi-7PrJFhmHREeiTwmumHlLM5VqdgwsXSsByx6K9NM-zHaMKJB5e4Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47
دیشب : آموزش کار با pkm
امشب به حول و قوه الهی: آموزش لانچ موشک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/funhiphop/75150" target="_blank">📅 09:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75149">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">خبرگزاری‌های عبری:  یک انفجار در کارخانه شرکت تامر روی داده است. این شرکت در حال توسعه و تولید موتورهای موشکی سبک و سنگین، از جمله موتورهای پیشران موشک‌های آرو ۲ و آرو ۳، موتور موشک سیلور انکور که هدف‌گذاری شده است، موتورهای ماهواره‌های صنعتی هورایزن و موتورهای…</div>
<div class="tg-footer">👁️ 5.91K · <a href="https://t.me/funhiphop/75149" target="_blank">📅 06:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75147">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Pv6weEkOkzPoXPqtpUwbHnzEdBDWXmS3x1XoNXgsd2k320lyhL4uExQVhjoi0i12-p3yL4Gc8NyVtK_gUYHA9DksUVnnYFSutS_d_aGrV9zrwd3SX4vc-I6O4CgGzALpM0p3TwoRwfbofiFqC928OhgLVIWfhBtY_9EnpybuVH9hqyUYMWzset_4NHuAUzFtHIiHPBhbgvRVpq876-xi4VOyh_A-085rrweEitYveJ-OYGoxLVitCLb6v85PjMen6uoQdTFUp938tKKYGlxHpBk-E7J4J-1I8PciVTj9QzCm5QIFXzQU5-sZm1MNGtmVPsdStxeiSERUYuFLqM2f1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIszL30dv719VvSVHbqlKOkoEOOPzinAsIBGXfsrjOrf7IA8yWo4q6VEG02hQUwITc3EvEoCIgN6il8DAQsICo_DfJRZjFArK3PNZiG-lkBs3RDDcBGvt4uZynUI2Z7dK3aqAvyvBKwLvwZPPXSLl4rmooMIrh8kBlF_mYewwm8ClWGhWNfStWxOr99LbrNjNn2269PDGAi8Hht2bXL0au9snasuSqNYieoXZo-pOjSSucvMLsh-EwbPI_26QcGDKTPg-L2B36AeW_AqKiTnq1JNObP9Nd8irMyr9RuCvKCyG9Zd0K6P-VKoelDwXCR5GYzdL_0_HYqa26DgxPRTOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی چنین چیزایی رو پست می‌کنم احساس می‌کنم خرافاتی ای چیزیم.
ولی اتاق جنگ اسرائیل چند روز قبل از حمله قبلی یه ساعت شنی که قسمت بالاش پر بود رو توییت کرد و دقیقا یک روز قبل از حمله هم ساعت شنی ای که قسمت بالاش خالی شده بود رو منتشر کرد.
حالا هم هفته پیش یه ساعت شنی با قسمت بالایی پر رو توییت کرده بود و الان یه ساعت شنی با قسمت بالایی خالی شده...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75147" target="_blank">📅 05:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75146">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXG8lOY73khd8AI-j8TmkoLUgIaNJISgjCO3X-InjuxNZ2jMhpZN_pb7LCiVc_sAyVq98FPwr0n4rjSxhNvfGunCEkjX0bO6N3RTgRZMMrDZ5dV_Nn30TCB76G-1hX3JOWAiqgdav8cLIYdhNYBWTUv4lCpex0GH8SdpeLs9alvu6AgN7Vv9T_YX0Z9eJOLxyzbwyf26Uw1oX2o2_CVRzdE3jaNMmH2aQsyZmTkJ-NfyYIjN9tpqMYIPWdRvmpBNOb4jMjTwEiq8PeVfGl8oziqN2Ux2OjKFgNzapyEYdfwLcSb6q0gnze3WX_m_q6ari63C8pO_LLnokvDWtUM6Vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله جدید تایم درباره دیدار ترامپ و شی جین‌پینگ دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.  حتی اگر توافق…</div>
<div class="tg-footer">👁️ 5.78K · <a href="https://t.me/funhiphop/75146" target="_blank">📅 03:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75144">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">کیر استارمر یا همون نخست وزیر بریتانیا بعد کیر شدن تو انتخابات محلی داره به نزدیکاش میگه تایمر ست کردم از سیاست لفت بدم.
یه حزب راست میانه رو هم داره میاد رو کار که احتمالا به مهاجرا قراره گیر بده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75144" target="_blank">📅 02:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75143">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اونایی که با شیر و خورشید وصلن کامنت بزارن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75143" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75142">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الان گارد جاویدان باید ضد حمله بزنه
وپن بده به اسم فاطمیون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/75142" target="_blank">📅 01:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75141">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ولی من دیشب چهار ساعت با سرعت نور وصل بودم جدی همش اینستاگرام بودم چسبید</div>
<div class="tg-footer">👁️ 6.81K · <a href="https://t.me/funhiphop/75141" target="_blank">📅 01:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75140">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گوشیتونو سه بار خاموش و روشن کنید
برید توی سیتینگ
وای فای رو ۳ بار روشن کنید و بعد ۴ ثانیه خاموش کنید
سیمکارتتونو در بیارید و بزارید تو یخچال(تأثیر داره رو سرعت بر ثانیه)
بزارید رو حالت هواپیما و بعد ۱۴.۵ ثانیه بردارید از رو اون حالت
به سرور شیر و خورشید وصل شدید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/75140" target="_blank">📅 01:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75139">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مجری: سلام مارو به رهبری برسونید
حداد عادل (پدر زن مجتبی):
من هم از همین طریق صداوسیما سلام شما رو منتقل می‌کنم، امیدوارم برنامه ما رو ببینن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/funhiphop/75139" target="_blank">📅 01:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75137">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a-M1SlJmVW1bt2vjI5IRd892Ru-dzp-tq8FULU0OKG4Jop8eSGSBsDBHZUzf4kKjuPfz7B-SRnJTOGw9c6WcSEW65dwXWrZrbW-_8vqOEPp3FO1kBsCqpjwxy9D6mO01r-ED27bxzWkWlHAKxx9M68C8ToxvvT1bFkCjuM9BvznzOsyxX3qCi7qo4C0kDbrjFDWSNajUrfSpLIeO9xQs-T63qszGxSTraOxIRFqOf-NvCdejxiA78mXkCj_FfWllzG6hspP7aJHnVo6iRtjYJ1pbti6u7XZRM4vPeC6LIR_SS_iRIEwccQdHDabFgaGlayo7l9V0OddtFeXpmjZc6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HV6C7Ga_nBARK5tZDgl13zOrkvOYQEWvkbC9tadPKEnGJMnVEFfljyMRnbf6yoAGpt-d6oS9kUnMWHrX_jXTA6cSWbDyyYVN1xk8t4tsr26NuVX3JTm4rl_dZika8ZZ3iMoGBRGJhs4Tn_X8ZLlJ4gv-x5nBT_iwTyu5OKEZJBAamWRPKlkCLcbWpZ0dG2pnyFrOMzDntP5IdfVJZqOXgk_VqpEaOO2toktkANpN7J9LqvK__OkmQtPc-uo5KT5I6ooF1RO2MGTTDJfixH8ku4HjLd7wcgjKbSn2vNG6Bnlyd3bbffC05jOaor9wUMiZfggsiq8WoezUm92jrepx5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبل و بعد جنوب لبنان
اره داداش عباس داره بدون عینک دنبال عینکش میگرده بره مذاکره کنه این جنگ و تو این جبهه هم به پایان برسونه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.18K · <a href="https://t.me/funhiphop/75137" target="_blank">📅 01:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75136">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4bLvpUqFbfFyyPtyj5633lsCophzlGHN5Grmo4Ifb7_1K0TR2PPovcr-vnCT3nHUIxAkaHENeM-XfGyD0fx8AHJuErI19qSTHZEYeCrvNypPnJHnzI5qQnV9F0fnpGU5tcTmSxYvRQvShMijXolNKohaS6EGhAPejV2T8SLe8YvTjJfL0GiRShVgaALx3kdXdp4oBT4Uqmtuew1AnqyNRn8CSZVrvTD8hcmx00i4u_U9E6GmSbZbdtqdZI-RuUhR7L_68PNZljjGEYl6Bdbl19sHxbmjFphS3i4_ymGEFpyiE0y081d6hIC-jNHTMGHA3mC-4Ry9MJYvAOLRLzVvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهمیدید چرا صیادمنش تیم ملی دعوت نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.05K · <a href="https://t.me/funhiphop/75136" target="_blank">📅 00:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75135">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">علی رضا بیرانوند
با صدای بلند و رسا کف آمریکا سرود ملی جمهوری اسلامی ایران و میخونم.
مخالفا هم نمیتونن کاری بکنن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/75135" target="_blank">📅 00:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75133">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/75133" target="_blank">📅 00:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75132">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C6daymFM94Uj0dIOFVK1lm9KRdn7ZZbpUbp6R15l1mbp-UJOcesokQzam_0_8U6eE-_MAxETSsE36L1jgSMFqyii_FXHIMp9c9umSGJEZ_8DqXVqeLBhfhC0PPV6ye8rVeqyTrGbD7Nw0nNfdtePjqEGtwbXCseqnvaLKFYC2W4TlUs4FX-28dazCI5iA459WgVXpiABpkduVC6_46Z46erzlIEGbz7ZNTTa5_lTzmc6PN8JKPnRNkBx7E57JaAjv31fsoZa9Mykw8g-c9gA8fadTl7fpLFbYfrWuXam1_ISSWXRObuSk-Kt1NQpftCfWUPFsX7MiXN2d2sNasIDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی. این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:  @SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/75132" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75131">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی.
این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/75131" target="_blank">📅 23:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75130">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AnnkAB2dTMCbeWfb9rSrh5cY_er6mtwX3Sk4mRMVCeJl0dJpGTjHPGe--FWfphTjjf5LIKDf57faEyfEpp6VCLAy9K4-9Bu36sJsJPgJtLAhQPKtqJGs-NhP-flf6Y8QdkghSYcsa7PapoAusrG4_nNA8YanpPM9QVaCYhQ86AZpbGNd7GeFjKtGtNTFtaPuck_B1bM8LW_FUh10lVCkYr168GOtL09PZYY1daGzUajUebCIH2e6Eklyp_iJOS37h6Z5jX7hi695JfTFl3Ic6LGkjs2bIFdcIJgID3HkUElaWvQNrSo2pLG0a9eXYLjWug9_RdsXimsq1d-pfziabg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پس از اینکه برای دشمن های فرضی خودش با هوش مصنوعی خط و نشون کشید اومد عکس خودشو شی جین پینگ و به اشتراک گذاشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75130" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75127">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWILECmdBnPZCMWIwze5xXNZ8FdzCdLbKZ0fRJ3Vp2A9rGPdSZlfPeKtTY69SIhrIwTiqP6ZrGSHsaeilyRjF-b6YaYa-DxilXgXVvrXqq2ZxIimmTGU704PkwU2IeBjZ0KWf2TrhzIUv-77hDyM38AV4wWhJJn5TLVKVMlCgOOio3Tl74d1SI0kpGm0tSAxwevYwmcabrwlnIIKbNQ90mtzUMQ7raY7OVkXjI1feIg6gzAENQxizBa3P6laZ1H2Y5kzhvCJbbEi9XnwUgtXbJa4jmzLguTQYN0KewW5i_0kzA3toRFOKzNmOssQ4kXcUBP4bq7_6fSOxlRkdSA0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت رسمی کاخ سفید جمله‌ای از ترامپ رو با عنوان «شوخی نداریم» پست کرده:
اگر شما به آمریکا صدمه بزنید یا درحال برنامه‌ریزی برای ضربه زدن به آمریکا باشید،
ما شما را پیدا خواهیم کرد و شما را خواهیم کشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75127" target="_blank">📅 23:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75126">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترمب: این آرامش قبل از طوفان بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75126" target="_blank">📅 23:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75125">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGrKNor-WbVbrVjMpKvCHJ8GY6SFORSbnJj11TL9vvybjtcPbSMuo3Hx0E3NQMYGHnw3DkZfESxqC6MjXjWpKoHfZolRxuEvuFiIbsRmNgyafHy3jZVNNruNIV0zZDPE4zMUVKjT-17MMXXKYyqbRtArvzILij09aMmjr2WyobYCuUJy3Xza5dLY8dTyrQmvjvJwsMLeDgayVUh_oV1Pq8c_5FfC5fiQTv85ia9tEke3yUBem_4g9OTwnPRpjVhsDuk2l_wTQNQuT0YVkiWTJKcxom8ZuPHpMtUzu4NnvSMluvykuJ3vtKDm5umBRtfpyn7b3U_XT1nvNjvwxyuIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب:
این آرامش قبل از طوفان بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/75125" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75124">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtRaczDEIzcTd2H1_l2DJLsExkDFmTYwoQ0gdwuM4ycleTW3CZM7Fi_IWJxuYjtSyudM9WResBXriq41Iv01n_m-vKvmWEa42R_UT6a2do4FxBWFVn-hwn2k1bC3uEBmiNT36B9OgAXlKPo1NnOZBO3lqReMlyRIjxhytoNQj0fchly-ZYQJiwNl-rykIJDpkKLzcGRhCZAR1yjCOrgxF2bewKmUGsyK9-jEOBQUSk2Q1SsSIfPinBpOtSS0lTZqQuwMKPG8WCo55sRNSRwU7beOdx2IkFrF-YqQMf8RclCuI-65nJ1ojMfzH8vFCWOaHeZeKg5wizY_FBM4jqNsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه اداره گاز اسرائیل از دستش در رفته و یه انفجار عظیم با منشاء نامشخص تو غرب اسرائیل باعث طلوع زود هنگام خورشید شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75124" target="_blank">📅 23:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75123">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=R1XGNqFVl46lSqLMX2MqvsfJqnICX52LDQX0wUerpy1y8AnpvcBzHvfX6J8UP3WKB8WjLoK-nnNxF2te6Zs9jxIYOA7wySUMG60aVEx498JHeeqf-zKEgl5xx85swXlQ1tSm5imqgAHYQvoYRcEGYth464B3xhK36veNdjmpEtmHbLNqqiuqqt-04Eq_AN8vSDVd0q9Y-4BJkURZrtVs-y733H4RKXlFLspPfc7vx4eiRWovOGMj-o1Oe3iMxLbjPKEvFyOalZi5kyKnQ_e1m23aD_A3VSGMU6BMWjYEKAvFOlzUz7iuZiPXMkpYPyskyjtw4hFJ5rSc3VMYUhCgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=R1XGNqFVl46lSqLMX2MqvsfJqnICX52LDQX0wUerpy1y8AnpvcBzHvfX6J8UP3WKB8WjLoK-nnNxF2te6Zs9jxIYOA7wySUMG60aVEx498JHeeqf-zKEgl5xx85swXlQ1tSm5imqgAHYQvoYRcEGYth464B3xhK36veNdjmpEtmHbLNqqiuqqt-04Eq_AN8vSDVd0q9Y-4BJkURZrtVs-y733H4RKXlFLspPfc7vx4eiRWovOGMj-o1Oe3iMxLbjPKEvFyOalZi5kyKnQ_e1m23aD_A3VSGMU6BMWjYEKAvFOlzUz7iuZiPXMkpYPyskyjtw4hFJ5rSc3VMYUhCgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75123" target="_blank">📅 23:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75121">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">به گفته خبرنگاران فان هیپ هاپ نیوز پدافند تهران فعال شده و درحال درگیری با اهداف متخاصم میباشند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75121" target="_blank">📅 23:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75119">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">هم اکنون صدای فعالیت پدافند در آسمان دزفول در شمال خوزستان
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/funhiphop/75119" target="_blank">📅 23:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75118">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYmFGE1j0B1YnF52iAvRt4k3MFwBHvh1hZ9O7v7rXSSnXMKkKQuJx9ZHP4TBM5uMujvAAgWkSdeV8015DaYMbdFmjAdrYVUP4r8_sIPqa28yO7TqJuI5JTxJgQScdRKzEZGaXUFtjHFRS82hBnPC-KgLvWw-Ff74INVmu40QbflJqkBX6DHGMCGFO3nQgcLZ_AUSMYJkavIocyNA8wsTpkJmU3wrkviH-CaK-3Ees7EgmUcc2a6N8KDArJSxdncrZ651bVZGH2j1Dt7btOP4a-y0tRO2LR9fD2boSje6NO9HrXHo4ij0Ht5hEqNEmB1jXIqSPSaqnhejR5tJflPYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین اکانت توییتری محمد باقرشاه قالیباف:
جهان در آستانه نظم نوینی ایستاده است.
همانطور که رئیس‌جمهور شی گفت «تحولی که در یک قرن دیده نشده بود در سراسر جهان در حال تسریع است»، و من تأکید می‌کنم که مقاومت ۷۰ روزه ملت ایران این تحول را تسریع کرده است.
آینده متعلق به جنوب جهانی است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.93K · <a href="https://t.me/funhiphop/75118" target="_blank">📅 23:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75117">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رونالدو از روزی که اومد ایران دیگه روز خوش ندید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/funhiphop/75117" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75116">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">النصر فینال سطح دوم آسیا رو باخت و کریس رونالدو باز هم نتونست با النصر جامی ببره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.07K · <a href="https://t.me/funhiphop/75116" target="_blank">📅 23:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75115">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">درود بر رهبر انقلاب اسلامی ایران
مقامات امنیتی اسرائیل ارزیابی می‌کنند که مجتبی خامنه‌ای رهبری جناح تندرویی را بر عهده دارد که با دادن هرگونه امتیاز در مذاکرات مخالف است و به‌طور فعال در حال آماده‌سازی برای از سرگیری درگیری‌هاست.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/funhiphop/75115" target="_blank">📅 23:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75113">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75113" target="_blank">📅 23:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75112">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRNJVjj2bpz0NrTZht3uztg1YYy3RMBW7Tmcyyy2rYvlI689F8XeczlldnR3O8Z4QBqZbhXYSJQ0BNnF9HK5Yp5E34LT-ZpRyRCS5URrPt6mU8C7Vz8yHz5wmKEMLaqBCOKWkvCcyXiKmi29Ptr3zB6i266HBBqdnZc2QuXhX_6g5Cmbn_VAYMh_ijPJhdl7iDaBvPnDnONZVdnIabEO_14Pw-erleSGlHv7Nah3PflL5vKBgztXCOG2y_YdPF9nEfIl2yIz2hNiw0-10HfLVarhN_VHsPMAp6I8r8C5gy9n7MeJ_06gzzWwp8W0TWz3hKILkqSRsZJ3bjpGTq_qFw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/75112" target="_blank">📅 22:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75111">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اینهمه خایمالی قایدی رو کردید تهشم سردار آزمون کیرشو کرد دهن قلعه‌نویی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/funhiphop/75111" target="_blank">📅 22:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75110">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مهدی قایدی با شرف هم که هستش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.59K · <a href="https://t.me/funhiphop/75110" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75109">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به تیم فوتبال جمهوری اسلامی
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق‌نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قایدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپو
ر
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/funhiphop/75109" target="_blank">📅 21:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75108">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=h-V8aqh27thZcOhLPIkLLpUKhmkba0RKbJcG4VaHovTJZtCh9DfYYgSt-17c6McylbMouYNr2_dYAaC3mpnUg7z-2-FnbdLU0-D4z0HYZapEvk5yvrHZpr_-Wj-y02O4xcsZ1BIUJqmrySAFYy6MZb2asI9XOJ21eRLUy7u-3C0D_qqX_2aHc_hBMkTQscDv1WHJFE3qqGc-yC-wZpLYzcE0-thhW3igIp3PPkwXPoBs0c8_F1h0xumYXapN5g0Gd72tDxCGf33wF1IeikuADGm-h_r0C3BtzK6OGz9xYx70dII2-0hGL7C40RF5Vg-y4NMoxRf0R5BKhJuJ0IbFiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=h-V8aqh27thZcOhLPIkLLpUKhmkba0RKbJcG4VaHovTJZtCh9DfYYgSt-17c6McylbMouYNr2_dYAaC3mpnUg7z-2-FnbdLU0-D4z0HYZapEvk5yvrHZpr_-Wj-y02O4xcsZ1BIUJqmrySAFYy6MZb2asI9XOJ21eRLUy7u-3C0D_qqX_2aHc_hBMkTQscDv1WHJFE3qqGc-yC-wZpLYzcE0-thhW3igIp3PPkwXPoBs0c8_F1h0xumYXapN5g0Gd72tDxCGf33wF1IeikuADGm-h_r0C3BtzK6OGz9xYx70dII2-0hGL7C40RF5Vg-y4NMoxRf0R5BKhJuJ0IbFiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تروخدا یکی ترامپ رو متوقف کنه» قسمت نمی‌دونم چندم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/75108" target="_blank">📅 21:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75107">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">عجیب نیست دفعات قبلی کسی از حمله خبر نداشت اما الان همه میدونن دوشنبه قرار بزنن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/75107" target="_blank">📅 21:51 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75105">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTGJ1dP-TWioWejK6hu7Ot4yU2P6OOIqCIhQDIct17orpeFuJWotpQkEPz5wa2zzy77ncTiN5AB17ff1G0_l0aXmf5eJJoEcG4T_PPMfzkbG5TkOhAUSGR_p9AZ9E9TjeU3HVp0qpGr7DH42K3ll9vHX02FKSaKhFsNUg2kOQw2YeWtljNYgjj25rYhHKBdMf9EwfgJrrVnO9VpTPzGvwp2ERgA4mwOXaPk87CnY_4EemLnIMr1O51tipJDUc4gzMIP36BOYUOtFC4lXgaOOdzqabjUbbO8r65LCPe3kHYhOsStGtX0zS7FZU3WwaXrfhC3C4_k3C3OhtepOkx7O3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بس کن دلقک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/funhiphop/75105" target="_blank">📅 21:35 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75103">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c34831ab3c.mp4?token=p-MJxD0xF2ChtzqOwlwjuGLY_Bky2N6-m4PqB306EcBUxTj1UHliHW_vccUCvldc_xTMnP3GNuwnZIlQE6UuMe3nK06NIXujxBaOQ46t_BXu7KjrDZWeJCP6-kUHWuGEcid0Jr9pyYCa72WDjPM2I3NsH8YQolIVv5ZX57lAJSUWzSSZ9p6dP0yO1GQ5ICushbngVLM_1julsDVSIMsG0fpglcfcNlf_eN22vghKoY9MvZt2Mli7qJoMw1AP8aIHT1ZrkMYtHVtsQEsA4ugFWNUEME9d6ITzTQ5KZe4dH2ZEa4bkL-dco69mL3YCSuJ2a576450W3lz2gmufEywabw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c34831ab3c.mp4?token=p-MJxD0xF2ChtzqOwlwjuGLY_Bky2N6-m4PqB306EcBUxTj1UHliHW_vccUCvldc_xTMnP3GNuwnZIlQE6UuMe3nK06NIXujxBaOQ46t_BXu7KjrDZWeJCP6-kUHWuGEcid0Jr9pyYCa72WDjPM2I3NsH8YQolIVv5ZX57lAJSUWzSSZ9p6dP0yO1GQ5ICushbngVLM_1julsDVSIMsG0fpglcfcNlf_eN22vghKoY9MvZt2Mli7qJoMw1AP8aIHT1ZrkMYtHVtsQEsA4ugFWNUEME9d6ITzTQ5KZe4dH2ZEa4bkL-dco69mL3YCSuJ2a576450W3lz2gmufEywabw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تنگه هرمز از نمای آسمان
🔥
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/funhiphop/75103" target="_blank">📅 20:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75100">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یجوری خونه لرزید خایه کردم</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/75100" target="_blank">📅 20:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75099">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=vtC2dhgQzP5oRDb11wPTNHLddk0Kqr2ZXiA2aKPJwqkco39DuBZD4Aosslqvk9bAUWSVRJdh0V8EDkXZtu173aVAqqBKEYcMDeI63uZPsrokyyB4zgDd0HKbHQUxnbYPZdK-ofu5gwoVsVlhC6g7VQyRgpExy3FBFLfnSNf7aKagIhD8lmOECZ4xwlUzv4Sqr1Ke9w5gzVSKDG0c18KGqNFRDO_VosfzlnCFsnhwpOttPigy2DCdPj8wppHglcdw1JfwyI2z-ziPFGwKWWPI2lsEjkt3VcFaUrDrQOf7gE2USjV6vMj6QctywPZT8v_0tSsmYVqEN1xHWnlt0RTAZpQKdoMSLFlBW4brivFbM_R6JS_-aWXVnfhoZavu3rRR8_ccOgdniOoUAMWJjbgiCbot9EY89lYFhI0_hUI-0jDZH5jYMHTwf42qOYiB8pBY6aBSwmGruGALZoxzuFvvU9X1MRIL-8CPtDyVXja5vBDz63RvtsUbOM10YdQaxqNXr45C0WvCylFiOMbMvsmXmxQsY7zlwWh5kR0luVsW_Tf-b-HzaJ0yWCBQ5iI-6OgL3iRPKxOUi4VloUmq4Nk-wvu4ytp1MS80pTOseU01GqovKDgRYoAsifbZqTfmNPFdXAp7QGbIEEEz6EOUq-Xo6vfTrWnQKm02E8I8owTBeHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c616c935d.mp4?token=vtC2dhgQzP5oRDb11wPTNHLddk0Kqr2ZXiA2aKPJwqkco39DuBZD4Aosslqvk9bAUWSVRJdh0V8EDkXZtu173aVAqqBKEYcMDeI63uZPsrokyyB4zgDd0HKbHQUxnbYPZdK-ofu5gwoVsVlhC6g7VQyRgpExy3FBFLfnSNf7aKagIhD8lmOECZ4xwlUzv4Sqr1Ke9w5gzVSKDG0c18KGqNFRDO_VosfzlnCFsnhwpOttPigy2DCdPj8wppHglcdw1JfwyI2z-ziPFGwKWWPI2lsEjkt3VcFaUrDrQOf7gE2USjV6vMj6QctywPZT8v_0tSsmYVqEN1xHWnlt0RTAZpQKdoMSLFlBW4brivFbM_R6JS_-aWXVnfhoZavu3rRR8_ccOgdniOoUAMWJjbgiCbot9EY89lYFhI0_hUI-0jDZH5jYMHTwf42qOYiB8pBY6aBSwmGruGALZoxzuFvvU9X1MRIL-8CPtDyVXja5vBDz63RvtsUbOM10YdQaxqNXr45C0WvCylFiOMbMvsmXmxQsY7zlwWh5kR0luVsW_Tf-b-HzaJ0yWCBQ5iI-6OgL3iRPKxOUi4VloUmq4Nk-wvu4ytp1MS80pTOseU01GqovKDgRYoAsifbZqTfmNPFdXAp7QGbIEEEz6EOUq-Xo6vfTrWnQKm02E8I8owTBeHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو هواپیمابر USS Gerald R. Ford پس از 326 روز در دریا به نورفولک بازگشت که طولانی ترین ناو هواپیمابر از زمان جنگ ویتنام است.
در ژوئن 2025 برای یک چرخش معمولی مدیترانه حرکت کرد و مدام گسترش یافت: ونزوئلا، دریای سرخ و در نهایت عملیات ایران.</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75099" target="_blank">📅 20:16 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75098">
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75098" target="_blank">📅 20:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75097">
<div class="tg-post-header">📌 پیام #22</div>
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
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/75097" target="_blank">📅 19:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75095">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/funhiphop/75095" target="_blank">📅 19:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75093">
<div class="tg-post-header">📌 پیام #20</div>
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
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/funhiphop/75093" target="_blank">📅 19:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75092">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">عزالدین الحداد آخرین فرمانده رده بالای شاخه نظامی حماس هست که با تایید چنین موضوعی (ترور) یک آسیب بزرگی به گروهک نظامی حماس وارد میشه.  اسرائیل تایمز هم گفته به احتمال خیلی بالا این فرمانده نظامی ترور شده.  تا این لحظه بیانیه رسمی از حماس, گردان های قسام و…</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/funhiphop/75092" target="_blank">📅 18:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75091">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ctt4iRq9c9CzWhmFYnEy50QElTaBWCvHL0TEl5FCz89OzG95akIOyRgQRSD4gxHYWMBkvTbZlAE-VAk6Pn_x0bch9kQ1oET2rJ62lvcxoiUS8RoUnq_ZF6bSOcO-r_oUxN-ve3C3YGHoeeegOvMWZg2ZoHY6sWwGOBxsRJfsrn27oXB_sKF15dTB9nxz7dI_V7sKP_vwNwXYq8lFgshvL7eJ3qRzQU4zwlpxZktesSsXgK69mnQp2EHxm0gsLWvvgYifyXkbRlqom8PojV_kMd_qCsjH3mvZD38iIL5hgmSBWtTsu8bGGoK9_PtrpLa1RP1XR8EQQQzdx5aanmqQhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیتر چک مناطق محروم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75091" target="_blank">📅 18:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75090">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">😵
بحران دارویی که راجبش صحبت میشه چیه اصلا؟ بررسی عملکرد 36 شرکت و 121 محصول دارویی نشون داده که قیمت 24 دارو در فروردین ماه بین 101 تا 3380% افزایش داشته : بطوری که قیمت پرداختی بابت بعضی دارو ها تا 34 برابر در یک ماه افزایش پیدا کرده.
👍
مهمترین دلایل تشدید…</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/75090" target="_blank">📅 18:27 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75088">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از اون 682 نفر یکیش قطعا رضاست
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/funhiphop/75088" target="_blank">📅 18:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75087">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iHHy-szTWmz4B5PAcwETmqMZbCxKsBBwlCD-xl1BD0ApLPjTXI1ddL34bN4wV1KUVkjxsZvLDlkrz6FZLPdZmsHChEX707Y2bvrgoS1K2sDiTsz3GQtEqVIjmkDgEZR0P6lQYd7RnQk0v98MryMOfjtfvn--56W0bSmHp7fdIqNfxNnQ1rSUfpX2En7lAlzpH5LXK9vUWiQXY6byC-7E9Bo2NpcLI35xucGngMeGt8jW7xhCqFpU_DURRUCyA7HkxixqnzeUsewkaOMsKCUODDs_YJaA8BIifeQHcyFqEdXTgvc9hipDP8T7R8nQY5Rzj83nvH5Lq6ULeNnQXiLKGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ کله زرد:
شوخی نداریم!!! ببین قراره بعدش تو موضوع مورد علاقت چه اتفاقی بیفته!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/75087" target="_blank">📅 18:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75082">
<div class="tg-post-header">📌 پیام #14</div>
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
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/funhiphop/75082" target="_blank">📅 18:00 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75081">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فعالیت جنگنده های ارتش بر فراز تهران
🔥
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/funhiphop/75081" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75079">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">پاشید جنگه
منابع عبری تأیید شده :
ایالات متحده در روزهای آینده آماده‌سازی برای حمله دوم به ایران را آغاز خواهد کرد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/75079" target="_blank">📅 17:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75077">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVl4KLgV00uA6OyJLwy7KJbzt0j3vuZshAW_UOdgDifaPI60iituOJniWaWl1Dbx8UGpQNcomRNvPsX0MFg40HZxLQYyILf36_QJnjiJJLcoVrYFuIAhKEQRIfOcSZjx8y2mGZGZ5mKHaEO5ge0jGF9y-JVci1d_NoeFHvAEaEOZAnxiSG19swEhDVkyKDH7l-1vmmsNqEdTcKjr1TcxC9z-KazrpkCTzysNuiFO16hEyZj5Ig6nSB-4DiCwANrMux8X5CsK4ouhuS2ZupqHzAuAHcCmXq_vNPJxZKpiqg7ExD5VxELrADNScaFfC-ovqXKordrzc-wz45AlNhv1RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VHxW6KPLSUvpNm9lTK0_f2ysrCqQea8EZuaYs-ZW1KbXC18eLaTQlP-4c1eUqBVQWm1obzDQmZkTDUZD3xVLQn1fOnh01UVOzL8U-zDLGoM1oKDkQK-B2ea2my8E_uw8g_0eGEi0qWX4WBarqPHwzpmexx3utUUKx-7OyB6PpUZTDhK5Pf9-kz1mm-2G-ShdyGsTLPCSvkDCvgtPmYDeyGKyIdrWFKHcmgtOtiqfREfS1RXXchqa9mW1O9IANnkA-zG_93r53MWjKZg_Jh1I-swHl4P7e4tA3NNtSrQGItcu5e81R1N_4BapD_KNy2mSZvHzqDzi9DB1_tU3QLbpbw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر یو اس اس لینکلن یا شاید یو اس اس بوش امروز در شمال اقیانوس هند در حالی که توسط یک ناوشکن در ۷ کیلومتری شمال شرقی اسکورت می‌شد، مشاهده شد.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75077" target="_blank">📅 17:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75075">
<div class="tg-post-header">📌 پیام #10</div>
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
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/75075" target="_blank">📅 17:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75074">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">با کشته شدن عزالدین حداد، تنها ۲ فرمانده حماس از ۳۲ فرمانده که مسئول حادثه هفتم اکتبر بودند زنده هستند
بقیه به دست اسرائیل کشته شدند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/75074" target="_blank">📅 17:30 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75072">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/75072" target="_blank">📅 17:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75071">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">شایعاتی درباره آغاز دور جدید مذاکرات ایران و آمریکا هست.
@FuunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75071" target="_blank">📅 17:20 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75070">
<div class="tg-post-header">📌 پیام #6</div>
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
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/funhiphop/75070" target="_blank">📅 17:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75069">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سنتکام
تا امروز، ۷۸ کشتی تجاری تغییر مسیر داده‌اند و ۴ کشتی غیرفعال شده‌اند تا اطمینان حاصل شود که قوانین رعایت می‌شوند.
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/funhiphop/75069" target="_blank">📅 17:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75068">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6WZf4v3PbEmIBEy91X7b3dMbUREVG9J9L-oJozYbIhzT0TjuXHR6b7m9uNFYUJJ-680VIVCFctMBt4Zgap5UHO7dGTn1bD-J3TTaLbMRX0w2wU_Lzqb3CWZizIQryTGnnT28k3VhDU1YOKSuE6ZELR4K0IboTX9AehNAAeTZhrmZUK7e4qOSEyXk7NpRkw0mYYBB4fBX-baus8VQoMzXXRpb3HA_e8hewCRPFcU6ZGQmPsvJYykBvvOefVGsXSV9J-I2np_YCol3tpxQWln8WOZfH3RRkRKO00_Z7-3G-1ivP7-XLXTTIDS2_ROvX8OSgu01gz8sHj_AM-VhKsWxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آماده باش آماده باش
@Funhiphop
| Reza</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75068" target="_blank">📅 16:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75067">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oCC4PUucuuZqhnUbi-wL-fNiHqPu9Yc4WZE97Rgz7neVdjIqQlSmjFECHbLsVYTvyDR5_djMfm4DrtnPJqBX1FaMgxFRVET-VKJtd8wsY64IqvLJn3h_yfRH0CZVSeFelG5V4qh0Z8OEmHDEEsj9SQQi48x4g1UHCexT8FytJgkyDmqqG0gWviX28I_gahNcmaJJXZmJaOtzD_mofReWz2HM4C0ehzEN3uly5ouj93bSVKn26jhwXkHN0Gz7yf-6f3lsuXwjpEtzm-B7jWHg_PTbq_D_zkJrx-nZlQhRjGAEmBM9LD4mfKGwXIelPYTT9FkJ893awIbcg1jXZd2wLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به امید قهرمانی تیم محبوب چلسی در بازی امروز
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75067" target="_blank">📅 16:43 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75064">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/75064" target="_blank">📅 15:04 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75063">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMuJgnV0S-9GOe1rFEdYewykAjiO4lw3lsWeN19m692gIM_Tbw1uuGXYkgVw5dlPHOKmiRsb4qs408ClabwKkNC1nFNqWdmeni-z9Fzc25w2WtU6RhA56TlCfv94gQy-aek07tCKl18XRYtOLtXrT-bs9X-WjJWUQLAlEBQug_p-ldzX85XoC7gR4_HYTsLJe0242Xc4AJnzgQItCAkkjn1vmk-fY0rKO7Zt5VkeX80FsYesPF4wrz5o1icg-MmTsZLjxL8bsJeo55PD8a5WLH-hQT7YGmTCoemuhFkDjEpRNMPcxNnemm1fSEIIlf9Nga9yWYCDhv-6Mcru_B3CoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین نوک تاریخ لواندوفسکی از بارسا خداحافظی کرد.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/75063" target="_blank">📅 15:02 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
