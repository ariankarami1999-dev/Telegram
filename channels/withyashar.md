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
<img src="https://cdn4.telesco.pe/file/OER4rwaYjGteJr2OTltTXzJUy7PKVDg3lU7qmVfAO2YOXIhlIYPfOi5O7fuMpzJz48R9STxEzydPbtn3LKEryNiyTCKC0MxV_LUScdRp7m7IMqeWIDb0KRpLqqHoOTzvgR2hwyN_Kvlx3X9xaDrsi5XkrDvMbu7e3bhuZrpIFD_c7Ex28nV1M8PRF_VfCNMOJqoWSUlj_0bYQDuCf_QVHg9JDa3McVWu-z1Fa-BkfTHnqXC2ngYhnlhgrwsWizTOTkcpa3mDRsQXyLTUN-2GsG3WRAo_HKxA-3PRxKOqACyuv0uNHLRlmyMf-QZ8l5WhrXEY9URsPLRqvd15w9Rx0A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 284K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharDonatePaypal :https://www.paypal.com/paypalme/yasharrapfaUSDT trc20: THebHKGpmnhWZzNZAbdSdr4fUAK3qkxDgkhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-11 13:09:42</div>
<hr>

<div class="tg-post" id="msg-13136">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گالانت : نتانیاهو اعلام کرده خاورمیانه دیگر جای حزب الله نیست و تا نابودی کامل جلو خواهیم رفت
@withyashar</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/withyashar/13136" target="_blank">📅 13:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13135">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قالیباف در توییتر(X):
«اعمال محاصرۀ دریایی و تشدید جنایات جنگی در لبنان توسط اسرائیل عدم پایبندی آمریکا به آتش‌بس است.
هر انتخابی، هزینه‌ای دارد و صورت‌حساب آن هم از راه می‌رسد؛ همه چیز سر جای خودش قرار خواهد گرفت.»
@withyashar</div>
<div class="tg-footer">👁️ 7.7K · <a href="https://t.me/withyashar/13135" target="_blank">📅 13:02 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13134">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بنیامین نتانیاهو به همراه وزیر دفاع دستور حمله به ضاحیه بیروت را اعلام کردند
@withyashar</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/withyashar/13134" target="_blank">📅 11:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13133">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سخنگوی وزارت خارجه: ما حق دفاع مشروع در برابر نقض آتش‌بس توسط آمریکا را داریم و امروز هم مبدأ تجاوز به خاک کشور را هدف قرار دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/withyashar/13133" target="_blank">📅 11:27 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13132">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ به نیوزویک : مردم ایران از من تشکر میکنند چون بجای یکبار، دوبار رژیم رو عوض کردم
@withyashar</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/withyashar/13132" target="_blank">📅 11:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13131">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromThis.is ⁰²:³⁵</strong></div>
<div class="tg-text">داش جان جدت ری اکشن
🤣
رو باز کن</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/13131" target="_blank">📅 11:19 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13130">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/withyashar/13130" target="_blank">📅 11:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13129">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZ58Wkdt3R_ztlUafyAC3gPA8J_5rl7XER3n242LrExDGEMezBB3Co29roLgMaJBL2loqSze39H9XEGHL8oWC3Z6vRvjV2gJlCVPx62PpVo0Q4a_bsUZVcTowadHc6wb9uunIQsS7NppTKxjrxB-5T77vqIM9UbiQUHQoGc-jUbysAR14lNOllYju1EoN83VzEWF1xwgp3aP-wmHb5SHDdEYrxGs9WCjFDB-O_3kl-N3DfWMEobxjhjju90yPs4FWj-Q0nLVrB-2EoPuADHl_bcN1lpERNphfblD4VshkF6Kux96gwRV2deTh9ai-mQN1tAjYbryrK50SkRA4p2M9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥴
🤣
@withyashar</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/withyashar/13129" target="_blank">📅 11:12 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13128">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اطلاعات  تایید نشده بهم رسیده که  اندیشه ترور هدفمند بوده   شخص‌ مورد نظر مسئول قراردادهای بین صدا و سیما و قرارگاه خاتم‌الانبیا بود @withyashar</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/withyashar/13128" target="_blank">📅 11:11 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13127">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">گزارش های از مشاهده خط شلیک موشک از همدان
@withyashar</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/withyashar/13127" target="_blank">📅 10:52 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13126">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">صدای انفجار مهمات عمل نکرده اصفهان پادگان پانزده خرداد
@withyashar</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/withyashar/13126" target="_blank">📅 10:21 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13125">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">البته توجه کنید که گفته بودند از قبل که خنثی سازی مهمات عمل نکرده دارن  @withyashar ولی با توجه به اینکه سنتکام ساعتی پیش گفته حمله کرده و رادار زده هشیار باشید</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/13125" target="_blank">📅 10:16 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13124">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">گروه تروریستس ۳پا امروز در بیانیه‌ای اعلام کرد در واکنش به حمله ارتش آمریکا به یک دکل مخابراتی در جزیره سیریک، «مبدأ حمله» رو هدف قرار داده و هشدار داد در صورت تکرار این اقدامات، پاسخ متفاوتی خواهد داد.
کویت حوالی ۶ صبح از فعال شدن سامانه‌های پدافندی خود برای مقابله با حملات موشکی و پهپادی خبر داد ولی مبدأ حمله را اعلام نکرد
@withyashar</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/13124" target="_blank">📅 10:03 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13123">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اتاق جنگ با شما : یاشار تتر داره کندل سبز میخوره همینجوری
این صداهای امروز مثل اینکه جدی تره
@withyashar
اتاق جنگ با شما :نهم اسفند هم همین ساعت ها بود داشتن حمله میکردند خدا به خیر کنه
😂
😂
💔</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/13123" target="_blank">📅 09:48 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13122">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13122" target="_blank">📅 09:41 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13121">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صدای انفجار در اصفهان
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13121" target="_blank">📅 09:39 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13120">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دوباره صدای انفجار‌ در بندر
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13120" target="_blank">📅 09:37 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13119">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13119" target="_blank">📅 09:33 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13118">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13118" target="_blank">📅 09:30 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13117">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeb</strong></div>
<div class="tg-text">یعنی جنگ رو پنهان میکنن ؟؟</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13117" target="_blank">📅 09:26 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13116">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">اتاق جنگ با شما : صداش دقیقا مثل جنگنده آمریکایی یا اسرائیلی بود
@withyashar</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/withyashar/13116" target="_blank">📅 09:25 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13115">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گزارش های زیاد از صدای جنگنده در تهران
@withyashar</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/13115" target="_blank">📅 09:23 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13114">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم. @withyashar</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13114" target="_blank">📅 09:22 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13113">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارش چندین انفجار بندر عباس
🚨
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/13113" target="_blank">📅 09:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13112">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k86X0NuFFVge8UQSZV1XrJRIxpcKm5ZChVW4mMTCErpkxrbZI0zrxkpIqUDxyDtcvQsDkqjO8Tas5is3OcUTmJvl1PjmcJeLubcKUApGaVbVcqmtIa20hXRiGc999eTv5FMRmrTW5vZMUkkh7qnxTrSg7FkKbBKqF-s_y02LdXd0cMPmLQxfegOQP6GZZkXOa8ioPpWD60_u2IfcRUN732JOfwhpTxybmr7F7mruV1hRBiDIaV5punxQBxdjC489G9idb72n8yrMs0Q-7YoG7bQY-QZN_oCbQpIwH0g1RT12oP636wyxWd7A-F4Vn67hXFwVDosSJNqU5KxYbby30g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری رسمی قوه قضائیه ایران(میزان) اعلام کرد که دو نفر دیگر از معترضان دی‌ماه ۱۴۰۴ را به اتهام «آتش‌زدن مسجد»، «لیدری کودتا»، «تخریب اموال عمومی» و «مسدودسازی خیابان‌ها» مجازات کرده است.
نام این دو عزیز که ساعاتی پیش جاودانه شدند، مهرداد محمدی‌نیا و اشکان مالکی اعلام شده است.
@withyashar</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/withyashar/13112" target="_blank">📅 09:04 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13111">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">سنتکام : ما حملات دفاعی به رادار پهپاد و سایت‌های فرماندهی و کنترل در گوروک و قشم ایران انجام دادیم.
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13111" target="_blank">📅 08:53 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13110">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">گزارش شلیک موشک از امیدیه در استان خوزستان به سمت کویت۶:۳۰ دقیقه و ۸:۳۳ دقیقه
@withyashar</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/withyashar/13110" target="_blank">📅 08:51 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13109">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PENkF-DI0t3Sa7KpiwGWsCKq4m5BXI27rQASyzQ-rEUbTq3aUsrLkGukRgN5jDVYsyYmtRBnjE0lLuK9ktiQ8iiwZIIYBXdL8AH9vsWE3Ls9eZ8vgzZ4u8eQ65ZAnvc5vO6oBWiXLY5FvPJZ0p7b9T-yshm0G-tsdrtNg9tMzM74vaPWks8gKISm-WxhVFCcfOipb8jQsMlAQGiML07FEt4pMKsjjxjXzE3saw9_qt9ZVIJjBiT3JE067S17L5LnO8E7DCA264-dhdXUsq3zBcFVVAt7R915tj3tUUfe3yi0Rk5g4lEfYIuwyr8T60ektQveb0adYtcBlH8kex5fEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث:
ایران واقعاً می‌خواهد به توافق برسد، و این توافق برای ایالات متحده آمریکا و کسانی که با ما هستند، توافق خوبی خواهد بود. اما آیا دموکرات‌های کودن و برخی جمهوری‌خواهانِ ظاهراً غیرمیهن‌دوست نمی‌فهمند که وقتی بازیگران سیاسی مدام، بارها و بارها و در سطحی بی‌سابقه، با نیش و کنایه منفی می‌گویند باید سریع‌تر حرکت کنم، یا کندتر حرکت کنم، یا وارد جنگ شوم، یا وارد جنگ نشوم، یا هر چیز دیگری، انجام درست کارم و مذاکره کردن برای من بسیار سخت‌تر می‌شود؟
فقط بنشینید و آرام باشید؛ در پایان همه‌چیز خوب پیش خواهد رفت همیشه همین‌طور است!
@withyashar</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/withyashar/13109" target="_blank">📅 08:45 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13108">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش‌ها از حمله پهپادی ایران به گروه های مخالف ایرانی-کرد در نزدیکی اربیل، شمال عراق!
@withyashar</div>
<div class="tg-footer">👁️ 88.2K · <a href="https://t.me/withyashar/13108" target="_blank">📅 00:38 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13107">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0qvIh3-QSoX0UDWmrnxJeI98VZX74ogzscyVG6vKiQ9rf8_lWJ1CMFX66IXgqCR_xiPabITW_iGApI9All9JJtkf0tf4EDX60U8HeRaOcVJPd2bncaV7QKsKvPBGXr6NmKzoVAU6WszNfUCjaKk6MWE5mhjFXkehfoErznggEXCJGhWBmRzKGEwlZXQZ2YKT9W2hSGJLorldv4OesoCEQByer2BImh25XeL6H3mTEQbyGwGAY_6RD_tAvWw8JtLeNiZOSNa0unJZgP453ZEXJpeX1q0BJE-3OoN2Lk9d3yaBHgAFcoe4zmTdzuymLaR1pVGvSIdQiHLrikuxgKIkY5I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5eae745a43.mp4?token=O_MnzgdJzkQ1DStZh3WSCoKRPErXGj_KO4KAQMQXQ4tUltSvkwQO-CGzUflsiNs3uHCbh2r1ZrPJkp4LgmHRPdi7vS7HQuHVR_pvbbzUbfgB3rqRLu3O87tjLODSR_g6-61KLhCCA9F5sYpz5IXTUFpe51QrWcEog-ILap0NeOIh1d0bHNPF_buMs_JFCZu4gElHrVgG55RP0t0Rmx_7Ow6IoAx1QIMSf1uYjybXV4b9wMdXtyW5exEH3aVYRuIXxb_WRMN3NFRD5p3ShZ-GQP92nSgQOYGw686VnDxqtwrtPiej3N4745mjBVd2P4zkOBfsnJaj69ntTBCCdGYP0qvIh3-QSoX0UDWmrnxJeI98VZX74ogzscyVG6vKiQ9rf8_lWJ1CMFX66IXgqCR_xiPabITW_iGApI9All9JJtkf0tf4EDX60U8HeRaOcVJPd2bncaV7QKsKvPBGXr6NmKzoVAU6WszNfUCjaKk6MWE5mhjFXkehfoErznggEXCJGhWBmRzKGEwlZXQZ2YKT9W2hSGJLorldv4OesoCEQByer2BImh25XeL6H3mTEQbyGwGAY_6RD_tAvWw8JtLeNiZOSNa0unJZgP453ZEXJpeX1q0BJE-3OoN2Lk9d3yaBHgAFcoe4zmTdzuymLaR1pVGvSIdQiHLrikuxgKIkY5I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : چشم آسمان ، هواپیما آواکس
@withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/13107" target="_blank">📅 00:08 · 11 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13106">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-footer">👁️ 92.6K · <a href="https://t.me/withyashar/13106" target="_blank">📅 23:47 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13105">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته  @withyashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/13105" target="_blank">📅 23:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13104">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته  @withyashar</div>
<div class="tg-footer">👁️ 97.9K · <a href="https://t.me/withyashar/13104" target="_blank">📅 23:27 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13103">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8091569054.mp4?token=hptnnu1uSp_YN_tjYxyXXbnYURDheL00dVh0N7fMWRqwrz-EB5GjPWvifThJT84WfClFhwgQ504AqCQokNEqauGWRkgVJsCoSmDfvObsAVnav9G7LZlpQu1T9QOVjyoUONwJADJ3Zb7FptRAa6J7MR9EoKMNzisaDmyWfPhwR1QkhYaINv_npBv5Q5weL-Eqpf-RPBqbFkULmghS8OIrjhQyNBG09-9cC5rtQNC0Gt2qSd8iM4mkqTeHNtZbwdjjE_ExIvlFQLcL0Qq1SdIZvoTepMyQZJWFUZRF9CUrCwqfDpovTYR2nef6-Gr00xPZCIkLoVMk1krEkjbRKTAjnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8091569054.mp4?token=hptnnu1uSp_YN_tjYxyXXbnYURDheL00dVh0N7fMWRqwrz-EB5GjPWvifThJT84WfClFhwgQ504AqCQokNEqauGWRkgVJsCoSmDfvObsAVnav9G7LZlpQu1T9QOVjyoUONwJADJ3Zb7FptRAa6J7MR9EoKMNzisaDmyWfPhwR1QkhYaINv_npBv5Q5weL-Eqpf-RPBqbFkULmghS8OIrjhQyNBG09-9cC5rtQNC0Gt2qSd8iM4mkqTeHNtZbwdjjE_ExIvlFQLcL0Qq1SdIZvoTepMyQZJWFUZRF9CUrCwqfDpovTYR2nef6-Gr00xPZCIkLoVMk1krEkjbRKTAjnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/13103" target="_blank">📅 23:24 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13102">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پدافند قم فعال شد
🚨
@withyashar</div>
<div class="tg-footer">👁️ 93K · <a href="https://t.me/withyashar/13102" target="_blank">📅 23:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13101">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48b4864ff2.mp4?token=aK18Mpdh11lSrLJWBn7XbYxNrtE8LCI0NI6yfBNRFSa9uo5KZy-_TNHIWuBOoVBiRLwvW2Tlo3U-ezmC2ugsWRJGEjSfucdUkvdnJFcV1q6PlWQZBgy2e9UeEAtUcyX0ZRMmVFls6VI_c6m_LEmKv2ep5G7jTIFD1BYeYg42jq2hnBvsJTPQSqfIVl71YkvhKWQemknPH7l0YDbQShYJiqMjTrCn4gH0LSXt3tSn0uAZpqfi31IxH1KlA27P5bU0qcHaKvcMMe59HgDNdRq-_J9VuumESn0BvJ71IkJGnDSwM-k-2Dx4DuJk18flTNXUkLylpl28snuQIIl4RgNqPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48b4864ff2.mp4?token=aK18Mpdh11lSrLJWBn7XbYxNrtE8LCI0NI6yfBNRFSa9uo5KZy-_TNHIWuBOoVBiRLwvW2Tlo3U-ezmC2ugsWRJGEjSfucdUkvdnJFcV1q6PlWQZBgy2e9UeEAtUcyX0ZRMmVFls6VI_c6m_LEmKv2ep5G7jTIFD1BYeYg42jq2hnBvsJTPQSqfIVl71YkvhKWQemknPH7l0YDbQShYJiqMjTrCn4gH0LSXt3tSn0uAZpqfi31IxH1KlA27P5bU0qcHaKvcMMe59HgDNdRq-_J9VuumESn0BvJ71IkJGnDSwM-k-2Dx4DuJk18flTNXUkLylpl28snuQIIl4RgNqPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار در فاز یک اندیشه شهریار خیابان شیشم شرقی در یک ساختمان که چندین مصدوم داشته
@withyashar</div>
<div class="tg-footer">👁️ 95.6K · <a href="https://t.me/withyashar/13101" target="_blank">📅 23:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13100">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">تسنیم : ایران تغییرات بیشتری در یادداشت تفاهم ایجاد خواهد کرد. اینکه ترامپ در حال ایجاد تغییراتی در این یادداشت تفاهم است، به این معنی نیست که این تغییرات برای ما قابل قبول است. ایران کاملاً برای شرایطی که هیچ توافقی حاصل نشود، آماده است.
@withyashar</div>
<div class="tg-footer">👁️ 92.4K · <a href="https://t.me/withyashar/13100" target="_blank">📅 22:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13099">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">حمله به کشتی حامل مس در تنگه هرمز
در پی درگیری‌های اخیر در تنگه هرمز، یک کشتی خارجی که حامل مس بود، مورد هدف قرار گرفت
@withyashar</div>
<div class="tg-footer">👁️ 91.8K · <a href="https://t.me/withyashar/13099" target="_blank">📅 22:32 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13098">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c322df9e96.mp4?token=CoNLazPBd0YGNn2-dv6jIta9cyTgTLK-s6E3v-v09D0VDyry0Nx-01lEB4jrJhlLR65wfgXc5tNIScfM42gmXmaS5TpUAjdgekmkv3FHFL-LoquPSa5l0QyrAoOABXKUpwfngNsxTJihGHQlNNKxJZWtVpcq184C4tcGQTehiaQPnr0WtnSrobFcwMOIB2JWrhF4kSEBqxA-7ffq57OV67s3_fDepKQIz37syYzD9S_DnimC1nEDeIb-6pmeXOSbZ2alCkc5rTBQvDwBXbDjBXVmhHpw5bKwvisM2wWKoLkbDzdrzKmTBIpQ-ExXTZiMPR7N9jsvZbElYWXwUBlzDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c322df9e96.mp4?token=CoNLazPBd0YGNn2-dv6jIta9cyTgTLK-s6E3v-v09D0VDyry0Nx-01lEB4jrJhlLR65wfgXc5tNIScfM42gmXmaS5TpUAjdgekmkv3FHFL-LoquPSa5l0QyrAoOABXKUpwfngNsxTJihGHQlNNKxJZWtVpcq184C4tcGQTehiaQPnr0WtnSrobFcwMOIB2JWrhF4kSEBqxA-7ffq57OV67s3_fDepKQIz37syYzD9S_DnimC1nEDeIb-6pmeXOSbZ2alCkc5rTBQvDwBXbDjBXVmhHpw5bKwvisM2wWKoLkbDzdrzKmTBIpQ-ExXTZiMPR7N9jsvZbElYWXwUBlzDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تردد خودرو های منطقه آزاد در سراسر کشور آزاد است
@withyashar</div>
<div class="tg-footer">👁️ 91.9K · <a href="https://t.me/withyashar/13098" target="_blank">📅 22:16 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13097">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/481d5e13ac.mp4?token=RzOz5xlklnzNgqGwMG6Yq-HM52KHp4BpoPiylcljdwexi_YC8pnD0qVJNCyAQj7pPXoMWyGMT3uvkTIdLXqc6Ew2U3gMnB0v6lzmQO7BWSujq9SeIrsxPCdgR3Lk_d_wG9EssIL2MuNwu-PjiqILQ3btQi9GV1ZJNU9SV9NqMkuy3JgbIU89VksoeEy5SUluySmwQ3YVcgWFcD8VUUEldaoTRjif-8PiNAeSqDkcdobT9FSHpXZ328A9NfZ4BhppCgbi05D9ez4HMWNO_RXBB-KqCj0RBye0JhjJfrNho1sXVA4Eow4VYLn8uMwd2cLz7ewUj3wUdAzk2WAfLkPuTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/481d5e13ac.mp4?token=RzOz5xlklnzNgqGwMG6Yq-HM52KHp4BpoPiylcljdwexi_YC8pnD0qVJNCyAQj7pPXoMWyGMT3uvkTIdLXqc6Ew2U3gMnB0v6lzmQO7BWSujq9SeIrsxPCdgR3Lk_d_wG9EssIL2MuNwu-PjiqILQ3btQi9GV1ZJNU9SV9NqMkuy3JgbIU89VksoeEy5SUluySmwQ3YVcgWFcD8VUUEldaoTRjif-8PiNAeSqDkcdobT9FSHpXZ328A9NfZ4BhppCgbi05D9ez4HMWNO_RXBB-KqCj0RBye0JhjJfrNho1sXVA4Eow4VYLn8uMwd2cLz7ewUj3wUdAzk2WAfLkPuTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری ایالات متحده:
اشتباه بزرگی که ایرانی‌ها مرتکب شدند حمله به همسایگانشان در شورای همکاری خلیج فارس، همسایگانشان در خلیج فارس بود، زیرا ما متحدان بسیار خوبی داشتیم که شاید در مورد پول با ما کاملاً شفاف نبودند، پول ایران که در سیستم‌های بانکی آنها بود، ناگهان بسیار مطیع شدند و حاضر شدند حساب‌ها را تحویل دهند یا به ما در مسدود کردن حساب‌ها کمک کنند.
@withyashar</div>
<div class="tg-footer">👁️ 89.1K · <a href="https://t.me/withyashar/13097" target="_blank">📅 22:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13096">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">کانال ۱۵ اسرائیل: گسترش عملیات اسرائیل در لبنان با هماهنگی دولت آمریکا انجام شد.
@withyashar</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/13096" target="_blank">📅 22:00 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13095">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جروزالم پست: منابع به واشنگتن پست مدعی شدند که مجتبی خامنه‌ای، رهبر ایران، هنوز به آخرین پیشنهادات ایالات متحده، از جمله تفاهم‌ نامه‌ای که در جریان مذاکرات اخیر مورد توافق قرار گرفت، پاسخی نداده است.
@withyashar</div>
<div class="tg-footer">👁️ 86K · <a href="https://t.me/withyashar/13095" target="_blank">📅 21:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13094">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">عراقچی: ویزای تیم ملی فوتبال ظرف یک تا دو روز آینده صادر می‌شود
@withyashar</div>
<div class="tg-footer">👁️ 86.1K · <a href="https://t.me/withyashar/13094" target="_blank">📅 21:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13093">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37fe276eb1.mp4?token=kZTCT1xan0Xxti9002ks28LYfIr8ISL8dUNFXMqluEB_BrmN6NdXga65mOKtnxjf4IMG82vfvPn7T800vyeZsi480ETJ1gIXaWeOwQdheAXe_SmQsUCvVyVWRLikzxr6PbKKC5FBX--GZ10UmiOTw-LAaiz8QqFh0DpZhpSJBI1B8TtmJE1OQcxbt3JK1JaS6o85a2oYxYiCppNAzkITpP8tQEjh0ryPsWyZiZf08dkJ9SEwQeBcrVSccxkRfhxXt-wf8YuDlevfqYDtG57c5kj1y95GWRekTjkwzQIOb2V4BMwMUmp3YyBY8KQUD0mO_8Xqx2Vj-_iUHfIyu0opUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37fe276eb1.mp4?token=kZTCT1xan0Xxti9002ks28LYfIr8ISL8dUNFXMqluEB_BrmN6NdXga65mOKtnxjf4IMG82vfvPn7T800vyeZsi480ETJ1gIXaWeOwQdheAXe_SmQsUCvVyVWRLikzxr6PbKKC5FBX--GZ10UmiOTw-LAaiz8QqFh0DpZhpSJBI1B8TtmJE1OQcxbt3JK1JaS6o85a2oYxYiCppNAzkITpP8tQEjh0ryPsWyZiZf08dkJ9SEwQeBcrVSccxkRfhxXt-wf8YuDlevfqYDtG57c5kj1y95GWRekTjkwzQIOb2V4BMwMUmp3YyBY8KQUD0mO_8Xqx2Vj-_iUHfIyu0opUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهزاده رضا پهلوی:
آنها در تلاشند تا قانون شریعت را نه در دمشق یا تهران، بلکه در خیابان‌های بلژیک، خیابان‌های پاریس، خیابان‌های لندن تحمیل کنند.
تا چه حد اجازه می‌دهید این رادیکالیسم ادامه یابد؟ این تهدیدی مستقیم برای ثبات و جمعیت‌شناسی اروپا است!
@withyashar</div>
<div class="tg-footer">👁️ 86.6K · <a href="https://t.me/withyashar/13093" target="_blank">📅 21:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13092">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منابع اسرائیلی:ترامپ در تماس تلفنی آخر خود با بنیامین نتانیاهو اعلام کرد که در صورت همکاری با واشنگتن برای این تفاهم‌ نامه 60 روزه موقت اسرائیل کاملا در لبنان و غزه آزادی عمل خواهد داشت
@withyashar</div>
<div class="tg-footer">👁️ 79.9K · <a href="https://t.me/withyashar/13092" target="_blank">📅 21:29 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13091">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">به گزارش رسانه‌های محلی، فعالیت جت‌های جنگنده بر فراز کرج در استان البرز  گزارش شده است.
@withyashar</div>
<div class="tg-footer">👁️ 80.5K · <a href="https://t.me/withyashar/13091" target="_blank">📅 21:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13090">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">صبح امروز سپاه اعلام کرده یک پهپاد MQ-1 را در نزدیکی جزیره قشم سرنگون کرده است. هرچند اسرائیل یا آمریکا این موضوع را تأیید نکرده‌اند، اما چند ساعت بعد یک حمله در همان منطقه انجام شده است. منابع می‌گویند در این حمله، «محسن سپاسیان» (مسئول تدارکات سپاه هوافضا در استان) و «ستوان سینا نجارپور» کشته شده‌اند. تاکنون هیچ طرفی مسئولیت حمله را بر عهده نگرفته است و این خبر را تایید نکرده است
@withyashar</div>
<div class="tg-footer">👁️ 80.7K · <a href="https://t.me/withyashar/13090" target="_blank">📅 21:15 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13089">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13089" target="_blank">📅 21:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13088">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">زرشکیان قهر کرد !  اینترنشنال: مسعود پزشکیان با ارسال نامه‌ای به دفتر مجتبی خامنه‌ای خواهان استعفا از سمت خودش شده. @withyashar</div>
<div class="tg-footer">👁️ 76.7K · <a href="https://t.me/withyashar/13088" target="_blank">📅 21:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13087">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-footer">👁️ 75.1K · <a href="https://t.me/withyashar/13087" target="_blank">📅 21:09 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13086">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/withyashar/13086" target="_blank">📅 21:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13085">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromNd</strong></div>
<div class="tg-text">مشکلش چیه اصلا همین امشب باشه چه بهتر! هرچه زودتر بهتر اصلا! خیلی زودتر از اینا حتییییی
🫠
🫠
🫠</div>
<div class="tg-footer">👁️ 73.8K · <a href="https://t.me/withyashar/13085" target="_blank">📅 21:07 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13084">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">و اینکه لطفا خودت هم یه پست بذار ما شاهزاده رو تگ کنیم</div>
<div class="tg-footer">👁️ 72.4K · <a href="https://t.me/withyashar/13084" target="_blank">📅 21:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13083">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرار‌ ما فردا شب ۱۱:۱۱ دقیقه تهران</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/withyashar/13083" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13082">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-footer">👁️ 71K · <a href="https://t.me/withyashar/13082" target="_blank">📅 21:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromT</strong></div>
<div class="tg-text">مگه امروز یکشنبه نیست؟
😅
قرار نبود دوشنبه باشه؟</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/withyashar/13080" target="_blank">📅 21:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13078">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-footer">👁️ 69.3K · <a href="https://t.me/withyashar/13078" target="_blank">📅 20:48 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13077">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">متن کامنت بررسی ‌کنید
جناب شاهزاده رضا پهلوی گرامی،
پدر ، این پیام، جمع‌بندی دیدگاه‌ها و پیشنهادهای گروهی از ایرانیان داخل و خارج کشور با هدف تقویت انسجام ملی و ایجاد مسیر عملی برای دوران پیش از گذار است.
عناوین چکیده از هزاران پیغام مردمی به‌صورت خلاصه:
* ضرورت ایجاد ساختار منسجم برای سازماندهی نیروهای مردمی داخل و خارج
* همگرایی و اتحاد جریان‌های مختلف مخالف
* ارائه نقشه راه و چارچوب زمانی شفاف برای اقدامات جمعی
* آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
* تقویت تیم‌های مشورتی، تخصصی و شفافیت در تصمیم‌گیری
* توجه فوری به بحران معیشت و فشار اقتصادی مردم
* ارتباط مستقیم‌تر و مستمر با جامعه
جمع‌بندی: جامعه آماده تغییر است، اما این مسیر نیازمند انسجام، شفافیت و ساختار اجرایی روشن است.
درخواست پایانی: فراهم شدن امکان ارتباط مستقیم برای انتقال منظم دیدگاه‌ها و ادامه گفت‌وگو با جناب آقای یاشار « yashar » که از طرف ما به عنوان گردآورنده و ارتباط‌گیرنده این مجموعه دیدگاه‌ها معرفی و تایید میشود.
این متن نسخه خلاصه‌شده است و نسخه کامل از طریق ایمیل، دایرکت و … ارسال  شده است. ممنون از توجه شما
پاینده ایران  و درود بر خاندان ایران ساز پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 74.1K · <a href="https://t.me/withyashar/13077" target="_blank">📅 20:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13076">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">EmergPhase_FA.pdf</div>
  <div class="tg-doc-extra">6.2 MB</div>
</div>
<a href="https://t.me/withyashar/13076" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">پروژه شکوفایی ایران : برنامه اضطرار
🌐
@withyashar
🌐
instagram.com/yashar</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/withyashar/13076" target="_blank">📅 20:26 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13075">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 72.8K · <a href="https://t.me/withyashar/13075" target="_blank">📅 20:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13074">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromM.!</strong></div>
<div class="tg-text">درود، میشه بی زحمت اون 250 صفحه رو بفرستی تو گروه ممنونم
🙏
🙏
🙏</div>
<div class="tg-footer">👁️ 71.3K · <a href="https://t.me/withyashar/13074" target="_blank">📅 20:22 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13073">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">با توجه به اینکه بخش محدودی از دفترچه پروژه شکوفایی«اضطرار» حدود ۱۰٪ به دوران پیش از تغییر رژیم «زمان حال» اختصاص دارد، لازم است به دغدغه‌ها و پرسش‌های مردم در این حوزه توجه بیشتری شود و برای آن‌ها برنامه‌ریزی دقیق‌تر و اقدامات سریع‌تری در نظر گرفته شود، زیرا این موضوعات برای افکار عمومی اهمیت مستقیم و فوری دارند.
اینم به متن اضافه میکنم</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/withyashar/13073" target="_blank">📅 20:17 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13072">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">زرشکیان قهر کرد !
اینترنشنال: مسعود پزشکیان با ارسال نامه‌ای به دفتر مجتبی خامنه‌ای خواهان استعفا از سمت خودش شده.
@withyashar</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/13072" target="_blank">📅 20:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13071">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/withyashar/13071" target="_blank">📅 19:58 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13070">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/withyashar/13070" target="_blank">📅 19:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13069">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/withyashar/13069" target="_blank">📅 19:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromabol</strong></div>
<div class="tg-text">یاشار جان سلام یه سوال فنی داشتم ،
بعد بر اندازی و سقوط ایده برخورد شما با عرزشی یا حالا بسیجی که دستش به خونی آلوده نیست صرفا موج سوار بود یا اصلا همراه بوده چیه اوناهم باید مجازات بشن یا باید گذشت و همکاری کرد ؟</div>
<div class="tg-footer">👁️ 69.1K · <a href="https://t.me/withyashar/13068" target="_blank">📅 19:46 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKsoE99e5lJskRoZRSTCm_acahFsHW4DKIq2iyzMzdT6D36GH_6JcIQ_7lhTDEmKja_LjcPyVgxL6b3WghG8sjZNL1naLlQn5fukF058fbP69ekkYI3Qgr62110WSDUWwJkPS1BAcfBClmTdjXl4fxZYMGefMbfVrgECyIQa1Z4dFQQ6EP5bvRA0EPnt2c9DoP_6AOTJfgfJfyVaEoIyYYd5FWU8oEs9MLNnHWEVlvjZHR2vTsZ31q_q28FJTknhg5EtzBotCDGEtinrxKd9c66MXemtXxhyvoojzI5KZRe-KuOrTCmNysittqOSGsgKYOo-t0UzlpQ7KQcGVY6JjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کشتی ایرانی به نام «IRGC TOLL COLLECT» به معنی « اخذ عوارض توسط سپاه پاسداران » در تنگه هرمز ظاهر شده است
@withyashar
مفتبر جاده هرمزه
🤣
تلکه بگیر سر گردنه</div>
<div class="tg-footer">👁️ 69.9K · <a href="https://t.me/withyashar/13067" target="_blank">📅 19:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یاشار همین الان مرکز تهران دو صدا  مهیب انفجار مانند ۱۹:۳۲
@withyashar</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/withyashar/13066" target="_blank">📅 19:36 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/withyashar/13065" target="_blank">📅 19:33 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromShiva Abdolahi</strong></div>
<div class="tg-text">من اون 250 صفحه دوره گذار و خوندم واسه وضعیت الان ما بیشتر شبیه رویا میمونه
الان برنامه برای سقوط مهمه
که هیچی در موردش توضیح نمیدن
🤦‍♀
🤦‍♀
🤦‍♀</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/13064" target="_blank">📅 19:31 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/withyashar/13063" target="_blank">📅 19:23 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/13062" target="_blank">📅 19:11 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سی‌ان‌ان: ترامپ با آزادسازی هرگونه دارایی ایران در توافق احتمالی مخالفت کرده است.
@withyashar</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13061" target="_blank">📅 19:10 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13060">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/withyashar/13060" target="_blank">📅 19:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13059">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/withyashar/13059" target="_blank">📅 19:03 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13058">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/13058" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13057">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLord</strong></div>
<div class="tg-text">آقا یاشار آخرش یک کم باید محکم تر باشه شما‌ فقط پیگیر دیدگاه‌ها‌ نیستی بلکه کلی قرار‌ راه کار بدی
درسته ارتش یک‌نفره هستی ولی تعداد‌ زیادی از مردم‌ با‌ شما‌ هستن . آخرش باید قوی تر بسته بشه</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/withyashar/13057" target="_blank">📅 18:54 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13056">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/withyashar/13056" target="_blank">📅 18:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13055">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/13055" target="_blank">📅 18:37 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13053">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">متن چکیده نسخه  ۲۱  بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی  پدر گرامی ،  این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/withyashar/13053" target="_blank">📅 17:57 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13052">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/withyashar/13052" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13051">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">متن چکیده نسخه  ۲۱
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
پدر گرامی ،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
برای انتقال دقیق‌تر این دیدگاه‌ها، پیگیری پیشنهادهای مطرح‌شده و ایجاد ارتباطی مؤثرتر میان مردم و جنابعالی، لازم است امکان برقراری ارتباط مستقیم با اینجانب ، به عنوان گردآورنده و منتقل‌کننده این مجموعه نظرات فراهم شود. از همین رو، علاوه بر طرح مطالبات و پیشنهادهای مطرح‌شده در این بیانیه، یکی از اهداف اصلی ارسال آن ایجاد این مسیر ارتباطی و گفت‌وگو مستقیم است
با توجه به اینکه بخش محدودی از دفترچه پروژه شکوفایی«اضطرار» حدود ۱۰٪ به دوران پیش از تغییر رژیم «زمان حال» اختصاص دارد، لازم است به دغدغه‌ها و پرسش‌های مردم در این حوزه توجه بیشتری شود و برای آن‌ها برنامه‌ریزی دقیق‌تر و اقدامات سریع‌تری در نظر گرفته شود، زیرا این موضوعات برای افکار عمومی اهمیت مستقیم و فوری دارند.
با نظر جمع مطالب مطرح‌شده در این پیام بر خلاف همیشه، عمدتاً ناظر بر مرحله پیش از گذار و چگونگی تسهیل روند تغییر رژیم کنونی کشور است
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار منسجم است که بتواند نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کرده، نقش‌ها را مشخص کند و از پراکندگی و موازی‌کاری جلوگیری نماید.
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای همگرایی جریان‌ها و گروه‌های مختلف مخالف حکومت است تا انرژی سیاسی و اجتماعی در مسیر مشترک و هماهنگ قرار گیرد.
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از دغدغه‌های اصلی مردم، نبود زمان‌بندی و مسیر روشن برای اقدامات جمعی است.
مطالبه عمومی این است که سناریوها و مراحل حرکت به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند و در صورت امکان، برای اقدامات جمعی و هماهنگ، چارچوب‌های زمانی روشن و قابل فهم اعلام گردد.
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهای حمایتی و سازمانی برای شرایط بحرانی تأکید دارد تا از طریق شبکه‌های امن، هماهنگی اجتماعی و توانمندسازی، هزینه انسانی تحولات کاهش یابد.
5. تقویت ساختار مشورتی، ارتباطات و شفافیت عملکرد
یکی از مطالبات اصلی، تقویت همزمان ساختار مشورتی، ارتباطی و شفافیت عملکرد است.
در این چارچوب پیشنهاد می‌شود:
گسترش تیم مشاوران و کارشناسان در حوزه‌های مختلف از جمله سیاسی، اقتصادی، اجتماعی، رسانه‌ای و امنیتی
استفاده از متخصصان حوزه امنیت، مدیریت بحران و مطالعات راهبردی در کنار سایر تخصص‌ها
تقویت و حرفه‌ای‌سازی نقش رسانه‌ای و ارتباطی
ایجاد ارتباط مستمر و مؤثر با مردم و مشارکت گروه‌های مختلف اجتماعی
فراهم کردن زمینه ورود دیدگاه‌ها و ایده‌های جدید از جریان‌های تخصصی و فکری مختلف
افزایش شفافیت در عملکرد و تصمیم‌گیری‌ها همراه با گزارش‌دهی منظم
هدف از این پیشنهادها، افزایش اعتماد عمومی، ارتقای کیفیت تصمیم‌سازی و تقویت هماهنگی میان ظرفیت‌های مختلف جامعه است.
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در حال حاضر
نیز در نظر گرفته شود.
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا اعتماد، شفافیت و هماهنگی افزایش یابد.
جمع‌بندی
در مجموع، پیام مشترک این دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها با انسجام، شفافیت، ساختار اجرایی روشن و ارتباط واقعی با مردم ممکن می‌شود. هدف این پیام فقط بیان مشکلات نیست، بلکه ایجاد مسیری برای رسیدن به راهکارهای عملی از طریق همین ارتباط است
⸻
درخواست پایانی (از طرف جمع امضاکنندگان)
در پایان، جمعی از امضاکنندگان و نمایندگان این دیدگاه‌ها، با نهایت احترام درخواست دارند امکان ارتباط مستقیم برای انتقال منظم دیدگاه‌ها، هماهنگی بیشتر و ادامه گفت‌وگو فراهم گردد و پاسخ این پیام  ارسال شود.
این جمع، جناب آقای
یاشار
را به عنوان نماینده و پیگیر دیدگاه‌های مردم معرفی می‌نماید.
راه‌های ارتباطی:
….
پاینده ایران
و درود بر خاندان ایران‌ساز پهلوی
@withyashar</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/withyashar/13051" target="_blank">📅 17:40 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13050">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=S5OPrVHolKgRjNRC4ciI5NQEsFaKccx3RuJ4Qn9bkm4mOlvyoeA4dBMw0UwZ7OOoYlFwLErnnmjwKlVKjDSk3VvDRZqlf6mHEf8JCexJg5448dW2C9VRDzgoRXcxy5Xph7682Agsi5OTG5qZd83_1LROVC2Cw3jrTBNVLYnfdNnM6DA-EEcQcHgFV-JokWcTZFU-gXHnxhTH07kzHqZ_4pMHa4Mp4iRToCMNUtNasoCd7nt3LVoLiIS8B76Vbyh9pZpSPYpZQynhCgUSFS0kyMrKg5w-aa3QhJX09_j-rsSR_Kt2Syr5NSgCI3vn_2_Fd6idq57Pdp8MSpsVS2kihw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205d44aab0.mp4?token=S5OPrVHolKgRjNRC4ciI5NQEsFaKccx3RuJ4Qn9bkm4mOlvyoeA4dBMw0UwZ7OOoYlFwLErnnmjwKlVKjDSk3VvDRZqlf6mHEf8JCexJg5448dW2C9VRDzgoRXcxy5Xph7682Agsi5OTG5qZd83_1LROVC2Cw3jrTBNVLYnfdNnM6DA-EEcQcHgFV-JokWcTZFU-gXHnxhTH07kzHqZ_4pMHa4Mp4iRToCMNUtNasoCd7nt3LVoLiIS8B76Vbyh9pZpSPYpZQynhCgUSFS0kyMrKg5w-aa3QhJX09_j-rsSR_Kt2Syr5NSgCI3vn_2_Fd6idq57Pdp8MSpsVS2kihw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از یه زاویه دیگه اتوبان ستاری ,جنت آباد جنوبی
@withyashar</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/withyashar/13050" target="_blank">📅 17:18 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13049">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69bcf1699.mp4?token=u8cG7Q5dBW5aItJO62vBGxF0uHQ7NWbPPWjeEdW7vWJIuWOOxgj7dYHeg9ouvPF04xioez-2qLLqkfkxnCRpeTefw9Da_wcpYD07Zy8ln49P8A_jypuRzSUXSitZyQO1ostzZYjyMOPxm-DqBXR4z-Qce_Say-NTeetb1AwB55DnwYZDfvbo01eapwS70IreqZarqAupH9UU_deMmBT54AyfQojzczDD0D6UvfWPpdTLXOZpVvE9Hy3aQMtYcFBLroIoD52jgVP7vLcMBtfWtg7zAYKZgH7O_639iLIJ7_1DAQ9_FCq9otQEeVoG1ZcNrT9pKYLTFOvAjQ6RyBFckw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69bcf1699.mp4?token=u8cG7Q5dBW5aItJO62vBGxF0uHQ7NWbPPWjeEdW7vWJIuWOOxgj7dYHeg9ouvPF04xioez-2qLLqkfkxnCRpeTefw9Da_wcpYD07Zy8ln49P8A_jypuRzSUXSitZyQO1ostzZYjyMOPxm-DqBXR4z-Qce_Say-NTeetb1AwB55DnwYZDfvbo01eapwS70IreqZarqAupH9UU_deMmBT54AyfQojzczDD0D6UvfWPpdTLXOZpVvE9Hy3aQMtYcFBLroIoD52jgVP7vLcMBtfWtg7zAYKZgH7O_639iLIJ7_1DAQ9_FCq9otQEeVoG1ZcNrT9pKYLTFOvAjQ6RyBFckw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبروی پاساژ کوروش
@withyashar</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/withyashar/13049" target="_blank">📅 17:13 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13048">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اصلاح ۵ بخش ۵
5. تقویت ساختار مشورتی، ارتباطات و شفافیت عملکرد
یکی از مطالبات اصلی، تقویت و گسترش ساختار مشورتی و ارتباطی در کنار افزایش شفافیت عملکرد است.
در این چارچوب پیشنهاد می‌شود:
تیم مشاوران و کارشناسان در حوزه‌های سیاسی، اقتصادی، اجتماعی، رسانه‌ای و همچنین حوزه‌های مرتبط با امنیت و مدیریت بحران تقویت و گسترش یابد
نقش رسانه‌ای و ارتباطی به‌صورت حرفه‌ای‌تر و منسجم‌تر ارتقا پیدا کند
امکان ارتباط مستمر و هدفمند با مردم و گروه‌های مختلف اجتماعی فراهم شود
از متخصصان حوزه
امنیت، مدیریت بحران و مطالعات دفاعی
در کنار سایر حوزه‌های تخصصی استفاده شود
زمینه ورود ایده‌ها و دیدگاه‌های جدید از جریان‌های فکری و تخصصی مختلف ایجاد گردد
شفافیت در عملکرد، روند تصمیم‌گیری‌ها و مسیرهای حمایتی (از جمله رسانه‌ای و سازمانی) افزایش یابد و گزارش‌دهی منظم در دستور کار قرار گیرد
هدف از این مجموعه پیشنهادها، افزایش اعتماد عمومی، ارتقای کیفیت تصمیم‌سازی و تقویت هماهنگی میان ظرفیت‌های مختلف جامعه است.
@withyashar</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/withyashar/13048" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13047">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/13047" target="_blank">📅 17:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13046">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">گزارش WSJ: سازمان ملل در حال ورشکستگی است، زیرا ایالات متحده و چین میلیاردها دلار را از این نهاد بین‌المللی خارج کرده اند
@withyashar</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/withyashar/13046" target="_blank">📅 17:02 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13045">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/withyashar/13045" target="_blank">📅 16:59 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQer3LdECB9u7P_EDTCb3D5hakw7E0RKHJxdUQ0tfFauACgu-8RwMXxAmjZkBdlP_oXbGdBVTCx6HDSEsXdn5TWosYNpbwTtdKt89V3AYSVhed9PvVyJs8SnCkXzDK_PvtVOgqP8YCQ7jaYCkBRdKkQiiwcZtac9r_ydGGnzdfwME_1B3V3868yfjZliFX2uRAr1pWIS6XSUKeGxn_AZYNPVYyfgruWqcJiXtFGgCRiJ1oVYG2yE1ConURP3QnjkMpKJ63tIuYwywRvwWRvJHcl2fSRNStSb3n3bOJK5ktbZA5ooOmMvKF8jSLt7tSsc3QTg5V1q-B72-f0Zi0O_0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان آتش‌سوزی غرب تهران سمت ستاری
@withyashar</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/withyashar/13042" target="_blank">📅 16:45 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/withyashar/13041" target="_blank">📅 16:42 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/withyashar/13040" target="_blank">📅 16:41 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">سی‌ن‌ان: ایران ۵۰ ورودی از ۶۹ ورودی تونل‌های تاسیسات هدف قرارگرفته موشکی را باز کرده است
@withyashar</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/withyashar/13039" target="_blank">📅 16:05 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">سی‌ان‌ان: برای وارد کردن آسیب به تاسیسات موشکی ایران باید از سلاح‌های بسیار پیچیده و بسیار گران‌قیمت استفاده کرد، اما عملیات بازیابی با فناوری بسیار ساده‌ای انجام می‌شود، فقط با بولدوزر
@withyashar</div>
<div class="tg-footer">👁️ 69.2K · <a href="https://t.me/withyashar/13038" target="_blank">📅 16:04 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">متن چکیده نسخه ۲
بیانیه جمعی از ایرانیان داخل و خارج کشور خطاب به شاهزاده رضا پهلوی
شاهزاده گرامی،
این متن جمع‌بندی مجموعه‌ای از دیدگاه‌ها، نگرانی‌ها و پیشنهادهای طیف گسترده‌ای از ایرانیان داخل و خارج کشور است که با هدف تقویت انسجام ملی، افزایش شفافیت و ایجاد مسیر عملی برای آینده ایران ارائه می‌شود.
در شرایط کنونی، جامعه ایران تحت فشارهای شدید اقتصادی، اجتماعی، امنیتی و سیاسی قرار دارد و در کنار آن، یکی از مهم‌ترین چالش‌ها، نبود یک ساختار منسجم و قابل فهم برای سازماندهی ظرفیت عظیم مردمی و تبدیل آن به یک نیروی هماهنگ است.
⸻
1. ضرورت ایجاد ساختار یا پلتفرم سازماندهی ملی
مطالبه گسترده مردم، ایجاد یک ساختار یا پلتفرم منسجم است که بتواند:
نیروهای مردمی داخل و خارج کشور را شبکه‌سازی کند
وظایف و نقش‌ها را مشخص و قابل اجرا نماید
از پراکندگی و موازی‌کاری جلوگیری کند
مسیر فعالیت گروه‌ها و افراد را شفاف و هدفمند سازد
امکان هماهنگی عملی در سطح رسانه‌ای، اجتماعی و میدانی را فراهم کند
⸻
2. انسجام و اتحاد میان جریان‌های مختلف مخالف
درخواست جدی جامعه، ایجاد سازوکاری برای
همگرایی و هماهنگی میان گروه‌ها، جریان‌ها و افراد مختلف مخالف حکومت
است تا:
اختلافات مانع حرکت مشترک نشود
یک محور هماهنگ‌کننده واحد وجود داشته باشد
انرژی سیاسی و اجتماعی هدر نرود
⸻
3. ضرورت اعلام چارچوب زمانی و نقشه راه عملی
یکی از مهم‌ترین دغدغه‌های مردم، نبود زمان‌بندی روشن برای مراحل مختلف حرکت سیاسی است.
مطالبه عمومی این است که:
سناریوهای مختلف به‌صورت شفاف و مرحله‌بندی‌شده مشخص شوند
برای اقدامات جمعی،
چارچوب زمانی تقریبی یا بازه‌های مشخص تصمیم‌گیری و اقدام
اعلام شود
مردم بدانند در هر مرحله چه انتظاری باید داشته باشند و نقش آنها چیست
همچنین بخش مهمی از جامعه خواستار آن است که در صورت وجود شرایط مناسب،
فراخوان‌های مشخص، هدفمند و زمان‌دار
برای اقدامات جمعی و هماهنگ صادر شود تا انرژی اجتماعی به‌صورت پراکنده و فرسایشی از بین نرود.
⸻
4. آمادگی میدانی و سازوکارهای حمایتی در شرایط بحران
بخش قابل توجهی از پیام‌ها بر ضرورت ایجاد سازوکارهایی برای حمایت از مردم در شرایط بحرانی تأکید دارد؛ به‌گونه‌ای که:
شبکه‌های حمایتی و سازمانی امن شکل گیرد
هماهنگی میان نیروهای مردمی افزایش یابد
آمادگی اجتماعی و مدنی برای شرایط حساس تقویت شود
هزینه انسانی تحولات احتمالی کاهش یابد
⸻
5. شفافیت در ساختار مشاوران و تیم تصمیم‌سازی
یکی از مطالبات مهم، شفاف‌تر شدن ساختار مشاوران و نقش افراد در حلقه تصمیم‌گیری است تا:
جایگاه افراد مشخص باشد
اعتماد عمومی تقویت شود
از ابهام و چندصدایی غیرسازنده جلوگیری گردد
⸻
6. معیشت و وضعیت اقتصادی مردم
در کنار موضوعات سیاسی، بحران معیشتی یکی از اصلی‌ترین فشارهای روزمره مردم است.
درخواست عمومی این است که در کنار برنامه‌های کلان،
راهکارهایی برای کاهش فشار اقتصادی و حمایت از اقشار آسیب‌پذیر در دوره گذار
نیز در نظر گرفته شود.
⸻
7. ارتباط مستقیم‌تر با جامعه و گروه‌های مختلف
مردم خواستار ارتباط فعال‌تر، مستقیم‌تر و مستمرتر میان رهبری اپوزیسیون و بدنه اجتماعی هستند تا:
ابهامات کاهش یابد
اعتماد افزایش پیدا کند
و امکان هماهنگی واقعی میان گروه‌ها فراهم شود
⸻
جمع‌بندی
در مجموع، پیام مشترک این مجموعه دیدگاه‌ها چنین است:
جامعه ایران آماده تغییر است، اما این مسیر تنها در صورتی به نتیجه می‌رسد که با انسجام، شفافیت، ساختار اجرایی روشن، نقشه راه قابل فهم و ارتباط مستمر با مردم همراه باشد.
⸻
درخواست پایانی (از طرف نماینده جمع)
در پایان، اینجانب یاشار به عنوان نماینده جمعی از این دیدگاه‌ها، با نهایت احترام درخواست دارم امکان
ارتباط مستقیم برای انتقال دیدگاه‌ها و هماهنگی بیشتر
فراهم شود و پاسخ این پیام برای اینجانب ارسال گردد.
راه‌های ارتباطی جهت پاسخ
پاینده ایران ، جاوید شاه
@withyashar</div>
<div class="tg-footer">👁️ 70.7K · <a href="https://t.me/withyashar/13037" target="_blank">📅 15:56 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/withyashar/13036" target="_blank">📅 15:51 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خودمو یادم رفت
🥲</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/withyashar/13035" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromSoheil</strong></div>
<div class="tg-text">یاشار چرا درخواست اینکه با خودت حرف بزنن تا اینارو بگی رو نداریم ؟</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13034" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBenyamin Qaem</strong></div>
<div class="tg-text">پس این متن چه اشاره ای به تو داره؟
ما میخایم یاشار با شاهزاده در ارتباط باشه</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/withyashar/13033" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-13032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHannaee</strong></div>
<div class="tg-text">جاوید شاهم بگو یاشار</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/withyashar/13032" target="_blank">📅 15:49 · 10 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
