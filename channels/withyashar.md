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
<img src="https://cdn4.telesco.pe/file/RVZYYWzaUqyi82X1EOAybPjls-dKsXvtMnCEMhggy13j9qS7bVEE8TvubgnSF_Y0eKlxGar7kOgXMHjOreL1uPRB8JdEjgu9DgGXLsw-MoPvTJiDdnPhL6MmRCsj8GxNKyVj6vYgXapDjumHZ-uMD3ZEaXNU5dNPXJ9SXF-VxsPLYWYxFO3CDubf79vtWaxxDuHDOrF_qxEqA9UYgPYcLuPertbA0Jc1fAKVRhOE6EEt2h1t_zqaVePMPIJrJOIMsI6vB0-JaEi2BmYvdzlHeO-xz8xko6SuSCo7pQsReNkte2KcSXANCsI_BgT2SulYw1ox2pPrVNY25_TU6aNsfA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 416K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 01:08:35</div>
<hr>

<div class="tg-post" id="msg-19135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">گزارش انفجار شیراز
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/withyashar/19135" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWarRoom with YASHAR</strong></div>
<div class="tg-text">تحلیلگر ارشد</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/withyashar/19134" target="_blank">📅 01:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19131">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کره جنوبی:
از شهروندانمون میخوایم فورا از کل خاورمیانه خارج بشن
@WarRoom</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/withyashar/19131" target="_blank">📅 00:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19130">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_IifnEAeXw-smT4GIFfFHTro2JDvs2znTIoKUGKTzPAZ5sfJYr2CXKui4m4sHFu30ilefbb-y-PfYTDNR_NnNvoiEcT-htMB9GdfGGo06H5tC9X33wltAyXdpZlZ8SZwjzs3fXcrS7AEe0O0u-AaHg7WycepasAa61nkSfjoHOArXjDqW-0Zb-yxDIYiNRu7MYaOzouh0UOak-rJnsBnu4U4RDRhfxdDSDtvNAGHSqu_9ZTKVMajbDbiKva6uGNdZihf5XSmijBTg1Goy9FFrvb9Vm1gt7sJ8riVVxPh2PWpY31i28OnDBqNBIVP29Obkq8aJRW9ATIAY7ySwoBDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیراز کوه دراک‌ رو قفلی زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/withyashar/19130" target="_blank">📅 00:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19129">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گزارش‌۲ انفجار بندر کنگ
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/withyashar/19129" target="_blank">📅 00:47 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19128">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">شیراز صنایع رو بدددد زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/withyashar/19128" target="_blank">📅 00:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19127">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گزارش انفجار شیراز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/19127" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19126">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">گزارش انفجار اصفهان
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/withyashar/19126" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19125">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یه حالی بدین اینستاگرام رو هم بابااااا اگه ندارین فالو کنین دیگه instagram.com/Yashar</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/withyashar/19125" target="_blank">📅 00:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19124">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">رویترز
: حملات به جمهوری اسلامی ایران در مقیاس بزرگ نزدیک است.
@WarRoom</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/withyashar/19124" target="_blank">📅 00:43 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19123">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">استاندار بوشهر: تاکنون هیچ گزارشی مبنی بر وقوع جراحت گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 73.9K · <a href="https://t.me/withyashar/19123" target="_blank">📅 00:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19122">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from❤🦁💚</strong></div>
<div class="tg-text">اصفهان یچی زدن یاشار شاید باور نکنی شبیح ویبره</div>
<div class="tg-footer">👁️ 75.9K · <a href="https://t.me/withyashar/19122" target="_blank">📅 00:30 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19121">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">سلام من اصفهانم
ی چیزی زدن صدا نداشت اما شیشه ها لرزیدن
@WarRoom</div>
<div class="tg-footer">👁️ 81.1K · <a href="https://t.me/withyashar/19121" target="_blank">📅 00:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19120">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 84.2K · <a href="https://t.me/withyashar/19120" target="_blank">📅 00:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19119">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7Xr_FAnNfYfC301IVE6CUpr439SxdvCieqpC5Sc3nJR3AL3rpjWg2tESdDo1KpKpmgcpWONBH7pgWi8_ZQM2RdNUHTne3a5jH3_0J8Xho5f8rpT6jB8UcxixwidayPcV7l5zAUXa7q7OBv1GjxlZrNRWLIUSBt88M87Gfub85iMAs2ZwGlMObeBjzdwO8REnmc9xnVdiZIu34tZ_gV7rIhcgcGJKMIapQQXhWXzN8p0Lz-trMu-POKWzTpoLZGiaRv_rwlCp0wKjFvaTND9eMrxPg4wgFxyEuvWF3lEc9FdUgE-fTyWDgzhq8PoW1RNgfwQN7De02TtL77wsq9mUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایی از پادگان امام علی چابهار که نورانی شده
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 86.2K · <a href="https://t.me/withyashar/19119" target="_blank">📅 00:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19118">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اصفهان صدای جنگنده
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 85.1K · <a href="https://t.me/withyashar/19118" target="_blank">📅 00:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19117">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پایگاه امام علی چابهار رو داره میکوبه
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/19117" target="_blank">📅 00:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19116">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صدای انفجار در بوشهر
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 90.3K · <a href="https://t.me/withyashar/19116" target="_blank">📅 00:13 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19115">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چابهار رگباری‌ داره میزنه
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/19115" target="_blank">📅 00:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19114">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">فاکس نیوز: دور جدیدی از تنش با ایران در راه است
به گفته فاکس نیوز احتمال بازگشت آمریکا به جنگ تمام‌عیار در خاورمیانه بسیار بالاست.
@WarRoom</div>
<div class="tg-footer">👁️ 95.4K · <a href="https://t.me/withyashar/19114" target="_blank">📅 00:09 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19113">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کنارک رگباری میزنند
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 94.4K · <a href="https://t.me/withyashar/19113" target="_blank">📅 00:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19112">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">چابهار ۲ تا دیگه
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/withyashar/19112" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19111">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">دوباره کنارک رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/19111" target="_blank">📅 00:07 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19110">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یه حالی بدین اینستاگرام رو هم بابااااا اگه ندارین فالو کنین دیگه
instagram.com/Yashar</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/19110" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19109">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوستانی که نمیتون عضو بشن فیلترشکن دیگری امتحان کنند ، اونی که دارن لیمیت خورده
❤️</div>
<div class="tg-footer">👁️ 92.3K · <a href="https://t.me/withyashar/19109" target="_blank">📅 00:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19108">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گزارش صدای انفجار کنارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 93.3K · <a href="https://t.me/withyashar/19108" target="_blank">📅 00:04 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19107">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">صداوسیما: صدای انفجار در بخش بمانی شهرستان سیریک شنیده شد.
@WarRoom</div>
<div class="tg-footer">👁️ 96.4K · <a href="https://t.me/withyashar/19107" target="_blank">📅 00:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19106">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گزارش انفجار چابهار
🚨
🚨
🚨
@WarRo</div>
<div class="tg-footer">👁️ 96.5K · <a href="https://t.me/withyashar/19106" target="_blank">📅 23:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19105">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">گزارش انفجار دزفول
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 97.5K · <a href="https://t.me/withyashar/19105" target="_blank">📅 23:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19104">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19104" target="_blank">📅 23:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19103">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">خبر گزاری داخلی : دقایقی پیش، صدای فعالیت سامانه‌های پدافندی در اطراف نیروگاه اتمی بوشهر به گوش رسیده است.
@WarRoom</div>
<div class="tg-footer">👁️ 98.5K · <a href="https://t.me/withyashar/19103" target="_blank">📅 23:53 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19102">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">بوشهرررررر
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 99.5K · <a href="https://t.me/withyashar/19102" target="_blank">📅 23:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19101">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">شب دهم شروع شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 103K · <a href="https://t.me/withyashar/19101" target="_blank">📅 23:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19100">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گزارش صدای انفجار جیرفت
@WarRoom</div>
<div class="tg-footer">👁️ 106K · <a href="https://t.me/withyashar/19100" target="_blank">📅 23:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19099">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">موج سنگینی انفجار بندر از شهر های اطراف احساس شده
@WarRoom</div>
<div class="tg-footer">👁️ 107K · <a href="https://t.me/withyashar/19099" target="_blank">📅 23:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19098">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بندر عباس بیش از ۸ انفجار
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19098" target="_blank">📅 23:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19097">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">۵ انفجار سنگین بندر عباس
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 110K · <a href="https://t.me/withyashar/19097" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19096">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شب دهم شروع شد
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19096" target="_blank">📅 23:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19095">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">دوباره بندر رو زدن
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19095" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19094">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صدای انفجار بندر قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 108K · <a href="https://t.me/withyashar/19094" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19093">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">صدای انفجار بندر عباس
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19093" target="_blank">📅 23:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19092">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">شاهزاده رضا پهلوی در گفت‌وگو با رویترز:
داوری بی‌طرف, و پلی برای رسیدن به مقصد هستم.
@WarRoom</div>
<div class="tg-footer">👁️ 109K · <a href="https://t.me/withyashar/19092" target="_blank">📅 23:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19091">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مقام ارشد آمریکایی به آکسیوس:
ترامپ دستوری به ارتش آمریکا صادر کرده است که به دلیل کشته شدن سربازان آمریکایی در اردن به زودی از ایران انتقام خواهد گرفت.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19091" target="_blank">📅 23:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19090">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تنگه دعوا شد
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 112K · <a href="https://t.me/withyashar/19090" target="_blank">📅 23:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19088">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-footer">👁️ 114K · <a href="https://t.me/withyashar/19088" target="_blank">📅 23:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19087">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شد ۲ انفجار سیریک
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19087" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19086">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گزارش صدای انفجار سیریک
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 115K · <a href="https://t.me/withyashar/19086" target="_blank">📅 23:21 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19085">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">خبرگزاری سی بی اس :
یک توافق موقت درحال شکل گیری است.
@WarRoom</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/19085" target="_blank">📅 23:19 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19084">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">وال استریت ژورنال:مقامات آمریکایی جزئیات سه حمله موشکی جداگانه به پایگاه هوایی موفق السلطی را شرح دادند:
حمله اول به باشگاه ورزشی پایگاه که منجر به زخمی شدن تعدادی از سربازان در مسیر رفتن به پناهگاه‌ها شد
حمله دوم به یک آشیانه خالی هواپیما
حمله سوم به یک خانه کانتینری که سربازان در آن خوابیده بودند
@WarRoom</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/19084" target="_blank">📅 22:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19083">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">@WarRoom
وسط راه</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/19083" target="_blank">📅 22:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19082">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FwK6tms8r6IMRYVG9T9OIApBENAwjzaDfo0CCsEwAF5zjlIQyCcpl7a_o4ORHMsJFtWeJD9ii__BgvRE4FQKRm2T3hTxx0zp1Fu_COQInOMCI3ITaiJcs4QHdzRchHTneuAl77XWSTr_n_QVtqM2e7F0xKYz9XmlLT-UKVfRpk8Uif21ig92ZYDfFkAFYtsLtsawkhARhI19vi95OCPRx7CWK4wLZPTFvFLmct4cmD8kT8WAp6yGitAPT2Xpb_yv95Hc6KMo1x74GNBtsVJSDJQXDHjnTd8bCbNpFQVCodv_kt6Cugwxz7pOq79dRPcvaTsdkHHJ0ghsgKs9jmEfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپاه کرمان: یک موشک کروز آمریکایی در آسمان رودبار جنوب رهگیری و منهدم شد
@WarRoom</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/19082" target="_blank">📅 22:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19081">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">فایننشنال تایمز: بدلیل فشار های داخلی ایالات متحده آمریکا کاخ سفید در حال بررسی گزینه الیت (تغییر رژیم کامل) در ایران است کاخ سفید قصد دارد سریعتر پرونده ایران را تعیین تکلیف کند
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19081" target="_blank">📅 22:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19080">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">شرکت هواپیمایی ایرفرانس، تمامی پروازها به کشور های خلیج فارس را به مدت هفت روز متوقف کرد
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19080" target="_blank">📅 22:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19079">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">کانال ۱۲ اسرائیل: شنیده شدن صدای انفجار در بندر ایلات
احتمالاً این صداها به دلیل شلیک موشک به سمت اردن بود.
@WarRoom</div>
<div class="tg-footer">👁️ 140K · <a href="https://t.me/withyashar/19079" target="_blank">📅 21:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19078">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jyGJnMmkbM6Eopfz98Dtoj59_5W8kTIqeL0WOplmNcH-CaSTy-_KxaOY96VCDLTLomGIfMYSbHpyYMbUOIVs5mxGaZugZEwjI9ZV0MTCMahdSg0FHVxcG0ETNvxYQa_cN2hCXy1YHLZsRB_Dn5p-lueMF0ZPyOhKe_bb1rUsv7lUhf2cMjyiRIRHN6uzrdR1DtZGg0auBRlFzQCn_5fI1Qqk9qhMnQ_YXRIpX_8bKb9Q4ha-hiigiw18kWh6Yp3EcrGFfLZjVxIfda2r3bAuOsTq-cZQVlb-IsTb2RPCs9NU1AbwkQKUC2QMHZ8GMQxifqRRg8p1ZbnC8f87tiVVWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشار همین الان سه تا موشک از غرب تبریز فرستادن خیلی صدای بدی داد
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19078" target="_blank">📅 21:31 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19077">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شلیک موشک از تبریزززز
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19077" target="_blank">📅 21:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19076">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">یک منبع امنیتی اسرائیلی به شبکه i24NEWS: ایالات متحده در روزهای آینده، مرحله بعدی عملیات نظامی خود علیه ایران را آغاز خواهد کرد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19076" target="_blank">📅 21:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19075">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">کاخ سفید:رئیس جمهور دونالد ترامپ، فردا شب در مراسم استقبال از تابوت‌های سربازانی که در حمله جان باختند، شرکت خواهد کرد. این مراسم در پایگاه هوایی دوور (Dover Air Force Base) برگزار می‌شود.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19075" target="_blank">📅 21:25 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19074">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPSYNB0p-X2QayUiWWehV44ImM3WVlzLVXUUClUu8ktFytOfizM_fhdO067tXnrLDhQ7xbKpV3aunCplvFBvIAQPhMXXXRMgS8gLNLHsiUqcCkwt_mEnK0w6D9FC0bQFwuP-PJNehjzA-w4CyZHImW851X5BgvDIfuogngV8m-CJGm_pIldUkyfVlb5Nn4wCuJEi2688RI4hgwtSDV5qYELDQoBeuYneUlyXtPbz8sxi8ffE7BbI7ilzYXpb8asKwsbeFPirLnv8IO7bMmehA8MMP9_mlcSMMc_Imu74SUAmx2AL2CJ1C0nlDxJ72ZsoaXdyTbPk5CgOYPw0RPgQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز عملیات تجارت دریایی بریتانیا (UKMTO) اعلام کرد گزارشی از وقوع یک حادثه در فاصله
۸ مایل دریایی شمال‌غربی کومزار، عمان
دریافت کرده است.
افسر امنیتی شرکت کشتیرانی (CSO) تأیید کرده است که کشتی توسط
یک پرتابه ناشناس
مورد اصابت قرار گرفته است. خدمه کشتی با ایمنی کامل آن را ترک کرده و توسط یک
یدک‌کش
نجات داده شده‌اند.
آتش‌سوزی همچنان مهار نشده و کشتی در حال حاضر
بدون کنترل و در حال حرکت سرگردان
است. همچنین تاکنون هیچ گزارشی از
آسیب زیست‌محیطی
منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19074" target="_blank">📅 21:18 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19073">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">منبعی در سپاه پاسداران به نایا که از افشای نام خودداری کرد: تیپ ۶۶ ارتش ایران از دزفول به سمت آبادان منتقل شده و نیروهای ویژه هم در آنجا حضور دارند. این عملیات احتمالاً در جزیره بوبيان انجام می‌شود که محل پرتاب موشک‌های آتش غیرمستقیم آمریکایی ATCAM به سمت جمهوری اسلامی ایران است.
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19073" target="_blank">📅 21:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19071">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmmL2u25teoKJq_RtuZMxEy5cA4rKJnOyOUdmDV9Aqw90JNzntEDkd-Nhn6xKOoipLPB47_LgZBNFvTnyppxQXQYUfCAo76MoQLwHt-MNRCmQ4LbSeFF388qpLv2pLy-2YTzyzcmyEIFjkTeVKDqVHvooNL5cv5P6T9QGkaXdMTCHcrp04Os2fbohyDX9zNJT4AaZNB_LlZOi_5xlWekBNRLx3KLE3YgCYs3XAnuvdAXPwwy_VSLf9gFRgIDHC2XiNDxY4YVWSEf4_LCOdgtq0aJfdfT2VNR1gdIGAM6Eb3qqOZloZGYBxIOrbIdbUuzW2lXCb_QPXcILurRxGg7YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرکز تجارت دریایی بریتانیاUKMTO: یک کشتی در 17 مایل دریایی شرق دیبا، مورد اصابت یک پرتابه قرار گرفت و باعث آسیب به چرخ دنده فرمان شد. تلفات جانی گزارش نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19071" target="_blank">📅 20:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19070">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">کانال ۱۲ اسرائیل: جلسه کابینه امنیتی و سیاسی اسرائیل درباره ایران با حضور تمامی فرماندهان و رؤسای نهادهای امنیتی آغاز شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19070" target="_blank">📅 20:35 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19069">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ReESBOCDqpsHY1YKuSWJPfZn-Zy8R5ST5ArWum7_v3abphytjSmEVSYJokLDgzYpyZ59e2slKlxh1QU0rgUX921x2CeMWIfgMXyoy0oe_fr7SvJ_KMEYH6WlqPUKunjD5uty9fwBu0wtwDL9158lm2yxss39ILUdJEWWCo0pm1BxUs-ozUAx5wWxkXeJ3yOeb5Fp8vcNyrlxsqbENJYtJndkr7z76Ef72ZD9wz2BlCDzqlsw1Q3bo-Uy0bIkjKrFpN2TY9q7CQEy5FU-b9w2WxUr9X1DU9UZarX8g_sAWwQiMIk-zctiPCUszEIn1psdqN4N1HEHjLGhA6GQlOQcZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
بنیامین نتانیاهو در مدت حضورش در ایالات متحده آمریکا،
به هیچ شکل و تحت هیچ شرایطی بازداشت نخواهد شد.
او در حال مبارزه با
جمهوری اسلامی ایران
است؛ حکومتی که به گفته ترامپ،
به‌تازگی ۵۲ هزار معترض بی‌گناه را کشته
و طی
۴۷ سال گذشته
نیز مسئول کشته شدن سربازان آمریکایی و افراد دیگری بوده است.
تنها کسانی که باید بازداشت شوند، افرادی هستند که ایران را به این
چرخه بی‌سابقه مرگ و ویرانی
کشاندند؛ موضوعی که
باید سال‌ها پیش و در دوران رؤسای جمهور پیشین آمریکا با آن برخورد می‌شد.
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/19069" target="_blank">📅 20:27 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19068">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">رسانه تندرو عراقی : ایران آماده حمله زمینی به کویت شده، شاید امشب!!!
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19068" target="_blank">📅 20:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19067">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KMgcDSybx6_yHUwa7HyLWWx5mbZ3i4yDN-k_HWLKsLluy2bVDDS33beBncIXYR0KS6Nvls5Ag4Gm71zjHRQtT1KDnVBYkDUCREbYOYOi9vVDdlbDv9S-ibb3oILl0xif_Qxz5h-Y9ae19c0TFTTwIM7LnVrDfoh3diLfIok2H6bGSczLt57PaQ4C8_Vg9BQpXb4V5vvM6-7XDi2UQNvsriAHKLkA7CWIKWKnL8YJmv-zi67e0Bb5Qg4RZ2UhFazSe-E0zYeLtdGn_ta5t7yAkulgmfZR0ETp1of2xE_gD9leLzT5hQjg7OrAb7tZD9vwl8SRvwNA7gFiGENa1A33Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ
در‌تروث
:
«هر بار که ایران یک سرباز آمریکایی را بکشد، بهای آن را
چندین برابر
خواهد پرداخت.
این دستور به
وزیر جنگ، پیت هگست
،
رئیس ستاد مشترک ارتش، دنیل کین
و
تمام فرماندهان نظامی
ابلاغ شده است.»
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19067" target="_blank">📅 20:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19066">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اف‌بی‌آی: هزار دامنه اینترنتی پخش‌کننده غیرمجاز مسابقات جام جهانی توقیف شد
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19066" target="_blank">📅 20:10 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19065">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/naaqSQ3UzivlNb8Iu-k_DI2BAlN7dLPIg9Hi8HxOgZzMeM0SyB54M7Kg2HQPBbNrniuY1URLvi-FxJFcyREZhv2DnDht3i_9GSJtGRhPXfwkTCedUDGLm5wC5A7x5DdZ92L-Wss_lytu29_ocjupRFd085xiekhbsI25eILAYxQikoJu64dyoMVHgzJR3rcIdtmsI5rxFfyvu8MToCB0T6DtYkN19qjDSHllt5NDWPN9d53iHJTEaHWCHRPZgGSflU9Hy1WPFEJh8RwEdsjBfEEKTr6Bt8SfNLmUOc3y11EXBXDxRj1HX6gi-DuF7wUG5kjo6nHCErcCf9gxWwUBog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فدراسیون فوتبال اسپانیا تصویر دونالد ترامپ
و اینفانتینو رو از عکس دسته جمعی لحظه قهرمانی به کمک AI حذف کرده حالا همه توی کامنتها دارن به این قضیه اشاره میکنند
@WarRoom
😁</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19065" target="_blank">📅 20:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19064">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک واحد صنعتی در حومه شهر خمین هدف حمله قرار گرفت
معاون سیاسی امنیتی استانداری مرکزی: این حمله حوالی ساعت ۱۹ روی داد که تلفات جانی در پی نداشت و خسارات احتمالی در دست بررسی است.
@WarRoom</div>
<div class="tg-footer">👁️ 129K · <a href="https://t.me/withyashar/19064" target="_blank">📅 19:56 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19063">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23dac038f.mp4?token=XSlhuLJcQe2OjpeNvULVsWTVWxZx8UtxHBDLmHFmQPkRM61yOZxeIUzALmi3nGEm5kn0YlF08dFwV81PUHghWTKlarUHRHavp1wbBGrC29uS05ssRRi_kOXsOeLySZsHtJuavEoWVB8xwhOjpdhYWxNoGDPW9_r-O531jYE6eJbm9JDw3Bq8UnxsP9ShItCTQmxQ9PxHJxXCD5yKk14574D57aEHf9s0v7b3cO7F6mG8llcUwN-XZxJTl_rzr4QKXPbXaAMaVRHZcwpaAh6PAxIXrvdi2JJcrUgWF-VB7fzR-jDakau6XZ5S0o0es9PyASLRncuLA_5UXzIEJJ9iJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23dac038f.mp4?token=XSlhuLJcQe2OjpeNvULVsWTVWxZx8UtxHBDLmHFmQPkRM61yOZxeIUzALmi3nGEm5kn0YlF08dFwV81PUHghWTKlarUHRHavp1wbBGrC29uS05ssRRi_kOXsOeLySZsHtJuavEoWVB8xwhOjpdhYWxNoGDPW9_r-O531jYE6eJbm9JDw3Bq8UnxsP9ShItCTQmxQ9PxHJxXCD5yKk14574D57aEHf9s0v7b3cO7F6mG8llcUwN-XZxJTl_rzr4QKXPbXaAMaVRHZcwpaAh6PAxIXrvdi2JJcrUgWF-VB7fzR-jDakau6XZ5S0o0es9PyASLRncuLA_5UXzIEJJ9iJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجاری در نزدیکی ساختمان فدرال نیویورک رخ داده گزارشی از تلفات احتمالی منتشر نشده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19063" target="_blank">📅 19:49 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19062">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">سنتکام : نیروهای آمریکایی مسیر حرکت ۷ فروند کشتی تجاری را تغییر داده و یک فروند دیگر را از کار انداخته‌اند، از زمانی که این کشور محاصره بنادر ایران را از سر گرفته است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19062" target="_blank">📅 19:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19061">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارسالی : شیراز صدا انفجار اومد همین الان سمت قدوسی شیشه ها لرزید
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/19061" target="_blank">📅 19:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19060">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/039c676d1e.mp4?token=jUvn4v5Fblhl1rKdYmdOJoZeml0_4Q1mfTzoT-0S_CgWdzJ0pCG-Wr6uHVldVjLO7urw2GHztji29sKwcItzrOrncTTipp7erZ6ZGohOaVqtnvCiQY5erzYIK4IVUFSA-1OY3aNIBNo0UW0vWfwJSkQldaY_YGl-fLLMuaHWbsQG1nsQ8U9rDNoPw4ldB7VaSyCCThcthvP9P-N4WB8Y82Qewns8WUd5ni3DESczAWILhe5ban60ikSkr2bBKUgII5l-DzoZRFblbRzvisZOKT-j_DG0KCnSwJN6dXiN7VP2ibvy6QVOBB2Tn_JHONcC8eHU41UVZ14Uh1eeMoj98w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/039c676d1e.mp4?token=jUvn4v5Fblhl1rKdYmdOJoZeml0_4Q1mfTzoT-0S_CgWdzJ0pCG-Wr6uHVldVjLO7urw2GHztji29sKwcItzrOrncTTipp7erZ6ZGohOaVqtnvCiQY5erzYIK4IVUFSA-1OY3aNIBNo0UW0vWfwJSkQldaY_YGl-fLLMuaHWbsQG1nsQ8U9rDNoPw4ldB7VaSyCCThcthvP9P-N4WB8Y82Qewns8WUd5ni3DESczAWILhe5ban60ikSkr2bBKUgII5l-DzoZRFblbRzvisZOKT-j_DG0KCnSwJN6dXiN7VP2ibvy6QVOBB2Tn_JHONcC8eHU41UVZ14Uh1eeMoj98w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب شدن موشک از لار
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19060" target="_blank">📅 19:26 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19059">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">وزیر امور خارجه فرانسه: امروز، تعدادی از کارکنان سفارت ما در ایران برای چند ساعت بازداشت شدند، مورد بازجویی قرار گرفتند و تحت فشار و تهدید قرار گرفتند. اتفاقی که برای دو کارمند سفارت ما در ایران افتاد، بدون عواقب نخواهد گذشت. دو دیپلمات در سلامت هستند و در ساعات آینده به فرانسه باز خواهند گشت.
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19059" target="_blank">📅 19:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19058">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">هواپیمای هیئت ایرانی منتسب به وزیر امور خارجه عباس عراقچی، در حال فرود در فرودگاه اسلام‌آباد پایتخت پاکستان میباشد. @WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19058" target="_blank">📅 19:05 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کمی پیش پرتاب موشک از شیراز و هم اکنون پرتاب موشک از لار !
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/19057" target="_blank">📅 19:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NphZNytb8tWBnnxc7IJMnfrYCdAtcXatPAUSNj6lOFYR9Xg2hon-eJsyWrbV90XWToj5ZZnbj-HMNf-gneUV3htSMeJrum9zqHyAZp_Am5o-aqx2cg-9X3JhDdSY_840h122nAw-Lo4Gh-b9wVJTW9vH8W9yi95cLSagNXVhp6OcNIUeZv7JkXOQX3w_QMOnbEQq4mGLM5REr1LAFYHgMTtnlsxNiHbWQBkyDiESZQmno9hoUv5Q_Abvl8a0wXKREZhQdo3ZS1WMz9dVgO24PqHxxfbVOBUlrhFOvsYg4wwIK7S7Gl_l4WPleDLc4NyMD56vkuAmTbTeYWz_sYDHog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای هیئت ایرانی منتسب به وزیر امور خارجه عباس عراقچی، در حال فرود در فرودگاه اسلام‌آباد پایتخت پاکستان میباشد.
@WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19056" target="_blank">📅 18:48 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">تنگه دعوا شد ، صدای انفجار‌ از تنگه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19055" target="_blank">📅 18:45 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">‏
اکسیوس:
عقب‌نشینی ارتش اسرائیل از "مناطق آزمایشی" در جنوب لبنان، فردا سه‌شنبه آغاز خواهد شد.
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19054" target="_blank">📅 18:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85ddb70d86.mp4?token=rwVPM_BRSJV-TjKifjlURp7NUcLga8R1H3uXC4WAOPlql8_0MwT42bW-yxmIjzKqB8hFMaDmhW6PGt9grW8Wf-tWrfUNfBYYZ87xWUBWub1gys3cE7htA9xeO7MIbQekqG_w4GIEncdV1vX1jMgK_uWzmIscKMgvddGcLcaIbSjNsFcFMMYJ5LG4eJpMlf8A13NaYZWhfli8KeRYzW8-m9ZtO9_nUwYWcg2zxTWXynUPRZy3mR9hJaZc-U0HmobKrVBPqGWi2EHcmtwQ7_NhTn5xersZ3UtIJLs_Yi0H-aILzVvLjJqLZ8DH_dl4UfmOi2JgOXpZCefK_neEcXjrpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85ddb70d86.mp4?token=rwVPM_BRSJV-TjKifjlURp7NUcLga8R1H3uXC4WAOPlql8_0MwT42bW-yxmIjzKqB8hFMaDmhW6PGt9grW8Wf-tWrfUNfBYYZ87xWUBWub1gys3cE7htA9xeO7MIbQekqG_w4GIEncdV1vX1jMgK_uWzmIscKMgvddGcLcaIbSjNsFcFMMYJ5LG4eJpMlf8A13NaYZWhfli8KeRYzW8-m9ZtO9_nUwYWcg2zxTWXynUPRZy3mR9hJaZc-U0HmobKrVBPqGWi2EHcmtwQ7_NhTn5xersZ3UtIJLs_Yi0H-aILzVvLjJqLZ8DH_dl4UfmOi2JgOXpZCefK_neEcXjrpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدا و سیما
زنده : مردم
عرزشی
بندرعباس با زنجیره انسانی ۵ کیلومتری به آمریکا پیام دادند: اگر از سد نیروهای مسلح عبور کنید، با ما طرفید؛ هیچ صلح و دوستی با ترامپ نداریم
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/19053" target="_blank">📅 18:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">دیدبان اتاق جنگ : سلام یاشار بندرعباس کلی موتور کراس با اسلحه  دوشکا ار پی جی اومدن ساحل مستقر شدن
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19052" target="_blank">📅 18:16 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبرگزاری صدا و سیما : بر اساس گزارش‌های اولیه، یک نقطه از شمال‌غرب شیراز هدف حمله هوایی دشمن هدف قرار گرفته است.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19051" target="_blank">📅 18:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش‌صدای‌انفجار جدید شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19050" target="_blank">📅 17:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97808c9f22.mp4?token=Tk329aaA5pFtIBMx5Tipi9nZK8u1QqxKOYyCzC3MfCgp9uyrYV7gUMmDouc8-vHi6piMj2ju_W1slLI0xIxlW0CmKaM9A5wNEU_Q5UZ420vr7kkM6yPSyKx57IOxCwhMutcXvJ4luUJsEszzMQle_JurTqbE-pZetb2TuzY3AK9KZafCHq88L3gdo3Esk3KDLyCJ9sg2J2zmv5pNwp9kBGsX6UHsN7bZmwGbZa9ymjeCd_j8SainAKcnlQd9xDkvUexkR9vTaB05q8TpoPI6vRYTTqN6WJk5h3xtOceNfbo7QbZGkw2ubg7Mz_8y7Jxjs45xgRfToumq1CVNSEVduA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97808c9f22.mp4?token=Tk329aaA5pFtIBMx5Tipi9nZK8u1QqxKOYyCzC3MfCgp9uyrYV7gUMmDouc8-vHi6piMj2ju_W1slLI0xIxlW0CmKaM9A5wNEU_Q5UZ420vr7kkM6yPSyKx57IOxCwhMutcXvJ4luUJsEszzMQle_JurTqbE-pZetb2TuzY3AK9KZafCHq88L3gdo3Esk3KDLyCJ9sg2J2zmv5pNwp9kBGsX6UHsN7bZmwGbZa9ymjeCd_j8SainAKcnlQd9xDkvUexkR9vTaB05q8TpoPI6vRYTTqN6WJk5h3xtOceNfbo7QbZGkw2ubg7Mz_8y7Jxjs45xgRfToumq1CVNSEVduA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار شیراز ، گویا صنایع رو زدن
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/19049" target="_blank">📅 17:36 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">عضو کابینه اسرائیل، الی کوهن: "ایران به خوبی می‌داند که چرا در دو هفته گذشته به اسرائیل حمله نکرده است. اگر مرتکب اشتباه شود و حمله کند، ما با قدرت بیشتری نسبت به عملیات قبلی پاسخ خواهیم داد. ایران به اسرائیل حمله نمی‌کند، زیرا از عواقب آن هراس دارد."
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/19048" target="_blank">📅 17:30 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گزارشهای متعدد از شنیده شدن صدای انفجار مهیب در شیراز
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/19047" target="_blank">📅 17:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/65823663be.mp4?token=sMuGYp_WhoSikOhzuFytCAX9-GYAzA_5fIHOHfoUZ4Wm_qLWXmTELvNCZ6iTGLrZPFNm82YV0MvDI4ywwnp4hCCe_Xj1fDtpMyYWX-cTejJhive-9hn0WuMRc4hN_Qn90P3Accd7nmQ3Mr1iELkXwkrFutaYwSxnKSvAX8QeieM_qP0oQ8xyBrF2zutoOvk7ZH7JOZMmBMcv42ADyohBVYkWqp3ZZMIPPJuLS6OCZ3KHZvCKx6biiBCZmZvmFbHCVM2_xaROAaehPWp9_4St84b6J2OD8jx5FgQRDE-p9QWIpUBgENQ0AmOAzOBAdBAI0_l2Zbu4JR0FK4mS7qsIkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/65823663be.mp4?token=sMuGYp_WhoSikOhzuFytCAX9-GYAzA_5fIHOHfoUZ4Wm_qLWXmTELvNCZ6iTGLrZPFNm82YV0MvDI4ywwnp4hCCe_Xj1fDtpMyYWX-cTejJhive-9hn0WuMRc4hN_Qn90P3Accd7nmQ3Mr1iELkXwkrFutaYwSxnKSvAX8QeieM_qP0oQ8xyBrF2zutoOvk7ZH7JOZMmBMcv42ADyohBVYkWqp3ZZMIPPJuLS6OCZ3KHZvCKx6biiBCZmZvmFbHCVM2_xaROAaehPWp9_4St84b6J2OD8jx5FgQRDE-p9QWIpUBgENQ0AmOAzOBAdBAI0_l2Zbu4JR0FK4mS7qsIkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشک از امیدیه خوزستان الان
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19046" target="_blank">📅 17:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">هم اکنون چندین انفجار کویت را لرزاند
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/19045" target="_blank">📅 17:01 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FTb14aMheRt0-9hJinpHXCLdQsVTQ41MGl4fTbxNe_PHSLuTXGzkw9kMiQEmeorN3qtzpIRg-g0GCY3ro0CdN76Uu3w9t4Pr-HV_PWwZXbITfcPsRVyus96fkgtKnpvwUuqox724na1bvRepgnW9M3fV4tfZMFiqB0c9KOO4O9xFtggndhG76liYECNrJkL04o1ODQC5gj2gWGdY3tVoLxDVywaa3SFLCtJF0YlSZV6iXpIVx1Z4vEHujmTvQnYJ_FhBUTCk_URJ4CZ0plRrlc8hRoo0zbRoWdws2h7wyg8iZnofEsxkhpJANnQhzlOMTrSz4Sesec5pjcWM-Ukr1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان دریانوردی بریتانیا: حمله موشکی ایران به یک نفتکش عربستان سعودی در تنگه هرمز ، الان @WarRoom</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/19044" target="_blank">📅 16:59 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">صدای‌انفجار بندر عباس‌ مربوط به نابود سازی مهمات جنگی بجا مانده است
@WarRoom</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/19043" target="_blank">📅 16:55 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تحلیلگر نزدیک به سپاه:
پیشنهادات اخیر آمریکا شباهت زیادی با الگوی پیش از دو جنگ 12 روزه و 40 روزه دارد،
اعزام گسترده جنگنده های آمریکایی به خاورمیانه در روز های اخیر از قصد آمریکا برای جنگ جدید خبر می‌دهد
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/19042" target="_blank">📅 16:52 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbgnoWAT-GDUQIDmhdw8k8jevSVuJDuxq_cxrP2sHDav3ODQ893ntjp5_mv9MKLfwEyYKbBxbwMtoUww1wovlq8nurh3YNChY7jiJrdap0Qpm7YieUj9b308jU6fMdrE1H62PXx2iEBbSMRLYPXG7XRE5eDghfJUPdcd4xbh1kkG-pRylAmih1BEV_gCHThR6NYz4fSk9Ei5B-2pGXgj4cmrIGT1DkIEjZI6RaQOHwe3rYlSO8qd0t-wmifcq2oULlu4YJ-wDrFrmxwUtzMnAAoSLxHA68dTTuDbdiyjbkVCUeljbUjl5bx4Zx8g1oGILxIUImwCxE5hGvw2faLMUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ توییت مسیح علینژاد درباره اعدام یک جوان ۱۹ ساله ایرانی در جریان اعتراضات دی ماه را بازنشر کرد.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19041" target="_blank">📅 16:47 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">درگیری‌های حوثی-عربستان سعودی:
حوثی‌ها اعلام کردند که محاصره دریایی عربستان سعودی را در تنگه باب‌المندب آغاز کرده‌اند.
@WarRoom</div>
<div class="tg-footer">👁️ 143K · <a href="https://t.me/withyashar/19040" target="_blank">📅 16:41 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">نیویورک تایمز: تهران و واشنگتن در آستانه یک «لحظه سرنوشت‌ساز»  بر سر جنگ قرار گرفته‌اند
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/19039" target="_blank">📅 16:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بحرین : ایران ساعتی پیش به سامانه‌های ناوبری هوایی ما حمله کرد
@WarRoom
🚨</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19038" target="_blank">📅 14:58 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">مقام آمریکایی به CBS:
تشدید تنش به زودی آغاز خواهد شد،
هواپیماهای ترابری و سوخت رسان آمریکایی به صورت پی در پی و بی سابقه در حال ورود به خاورمیانه می‌باشند
@WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19037" target="_blank">📅 14:51 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ممباقر بعد از چند ماه عضویت در اتاق جنگ با یاشار : آمریکایی‌ها مدام تجهیزات نظامی جدید به منطقه می‌آورند و می‌گویند دنبال توقف جنگند. روی هوش ما اندازهٔ آی کیوی مختصر خودشان حساب کرده‌اند.
ما در شناخت این آمریکایی‌بازی‌ها به مرحلهٔ استاد تمامی رسیده‌ایم و بر این اساس آماده شده‌ایم. اقدامات باید مؤید ادعاها باشد نه ناقض آن‌ها.
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/19036" target="_blank">📅 14:44 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXSPZxEhJnJ_IpjqSeSsrdbbITDJ4f1S9xB4J3PxDQzK98KE7L7YEqlQmm-l78mfIF6r-kykWUf_HlYaZI5rqJigQlAmHWdZgScLHyKq7l-HOSTEqvCQHUxQfMS-qnNbIrVES4vloIpbAAohX-IguSIJzDbu4rq_3TXBr2RtyvPTepRuPdRWgjN1dzNvbrgHwd01utx27BPWUltaB571AqI5XddqqOrHsJtUAoQySU3dTyeNoy4dY8ByVk3onKP2fVpciZKN_msEiZ9luAXSX9061vk1MI8s-Fx1wnvD83E_6p-mtcXpCYWSITJucS9W0g2PXJpDY04mxWYmKUIWvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ به دنیا آمدن پسر معاون خود جی دی ونس را تبریک گفت.
پسری به نام
Alec Neel Vance (الک نیل ونس)
. در بیانیه مشترکشان اعلام کردند که مادر و نوزاد هر دو در سلامت کامل هستند.
فرزندان جی‌دی و همسرش اوشا ونس(حقوقدان آمریکایی با ریشه هندی) (خانواده‌ای از مهاجران هندیِ تلوگو)
Ewan Vance (ایوان ونس)
– متولد
۲۰۱۷
(پسر)
Vivek Vance (ویوک ونس)
– متولد
۲۰۲۰
(پسر)
Mirabel Vance (میرابل ونس)
– متولد
۲۰۲۱
(دختر)
Alec Neel Vance (الک نیل ونس)
– متولد
۱۹ ژوئیه ۲۰۲۶
(پسر)
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/19035" target="_blank">📅 14:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KADcMrhepJ9yifK3WDqFBwHJZ8MrCf57wsg-gb23oDG0F-5XhL6ppWOk3WbgjI9gbeEjsLIHtWxbXSjmUsRkeRGtioNRgMH4NLlJHWd_yZE5cORnqMlajn2wruQYVUzuqRE20FRSVWMPBrcN4NNh2SUXdL1huj9FUnLH-LtOajtC-v9NdTNjbnFaZ0sMdo65j7lnWwV9uSvHoApGmaH55CzYtncRiYfHjXRTsZ-cecUY9e3Sh0PAPtJtagCnXcY2y28VTK6Z8PkBlNVsCorfClVsEbl1Y_0CLAiRmDqZmoGPExdbh7YJV2-Q4DLoVSbc3Ui2K4FEv8MlozBSFqxvsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواپیمای نتانیاهو  به مقصد نا معلومی بلند شده سپس چند دور زد تا جهت مقصد گم شود و بعد فرستنده خود را خاموش کرد!
@WarRoom</div>
<div class="tg-footer">👁️ 151K · <a href="https://t.me/withyashar/19034" target="_blank">📅 14:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">کیر استارمر
امروز،
۲۰ ژوئیه ۲۰۲۶
، در دیدار خصوصی با پادشاه، استعفایش پذیرفته شد. چند دقیقه بعد، جایگزین او
اندی برنهام
، رهبر جدید حزب کارگر مأمور تشکیل دولت شد و قدرت رسماً منتقل شد. این انتقال معمولاً در فاصله حدود ساعت
۱۱:۴۵ تا ۱۲:۰۰ به وقت لندن
انجام می‌شود(حدود ۳۰ دقیقه دیگر بهصورت رسمی)
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/19033" target="_blank">📅 13:57 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-19032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=SbHW-nL_ld7oBkVKPCYktrELx5a8Zhd73M8Xa9TwpWAD3Ehs-kePVl3mC1ntPBRvfarnGjjpoBMwiR1LWfClkoibdKr7ZzcfLNcc-sQjyDH4p7Dh7U5AjSH5LkImWz708iqzUA2UrH6d0vd9l4O2GP3qayd6Cqkm0HhXPSg1fpHDhsZhfdwKWRu1DE4TC1mq4GpFqVKQC2iM_Lj6lEptpWTu-3QXf0dLTrXnPysd7H-s6UkQmQuLQtNsNalowmMYl2sL4OHR9_1YCE12nhN-X3fv7m_m0ZgymvKOj-kKrCTJ6aoWyOL_5aJ7JKGsdGIO7Rd1GnLoFa5EHW5No488PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8bc26544.mp4?token=SbHW-nL_ld7oBkVKPCYktrELx5a8Zhd73M8Xa9TwpWAD3Ehs-kePVl3mC1ntPBRvfarnGjjpoBMwiR1LWfClkoibdKr7ZzcfLNcc-sQjyDH4p7Dh7U5AjSH5LkImWz708iqzUA2UrH6d0vd9l4O2GP3qayd6Cqkm0HhXPSg1fpHDhsZhfdwKWRu1DE4TC1mq4GpFqVKQC2iM_Lj6lEptpWTu-3QXf0dLTrXnPysd7H-s6UkQmQuLQtNsNalowmMYl2sL4OHR9_1YCE12nhN-X3fv7m_m0ZgymvKOj-kKrCTJ6aoWyOL_5aJ7JKGsdGIO7Rd1GnLoFa5EHW5No488PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روبیو به سی‌ان‌ان: از طریق کانال‌های متعدد، نشانه‌هایی مبنی بر تمایل ایران به مذاکره به دست ما رسیده است، اما شکاف فزاینده‌ای در درون نظام وجود دارد.  اگر ایرانیانِ خواهان مذاکره بر اوضاع مسلط شوند، این یک تحول مثبت خواهد بود، اما چنین چیزی رخ نداده است. @WarRoom</div>
<div class="tg-footer">👁️ 154K · <a href="https://t.me/withyashar/19032" target="_blank">📅 13:06 · 29 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
