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
<img src="https://cdn4.telesco.pe/file/fiUtkfufKVOKcdNwJMsdSaiB0cUDSvUdrM8aoWmrB03xOR3HJXFTHCOQfR570KL518j_ZiB6T7GtfHZuv_3aAwgkhIFvYqgyvsFHtYBFv3fvTwUWzfaUZUrxFwXWWeSsB4AQX0lUSTzrlX-e3D8_itnokSjTa4rRvzBSMoaySVbNS7A3bwMw_VsR7PrEuKT9rCoi1A-4p3pbf40I3ws_0kKlkA4As4vZLJckj_uHus7ws09HKu1yzS8SSSwlSxg8scS6CH_sE-g7yJ4g8oynmHZzDDaQadj6_H1sfXGdRNPxEHc_5MArJP1Byojiuw-K_P6b_GF0eYzPXS1ixz61zw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-24 00:15:23</div>
<hr>

<div class="tg-post" id="msg-77808">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یک مقام ارشد اسرائیلی به ynet:
هدف این توافق این است که زمان و فرصت برای تمام رویدادهای مهمی که اکنون در آمریکا در حال وقوع است، خریداری شود.
این توافق واقعاً چیزی نیست که دوام بیاورد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/77808" target="_blank">📅 00:16 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77807">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LkFGJREW8x4uAu3toQ600jBRLMO99F6wUZ74Vu93-UaNHp0tkL9fINsnoB3ugWQAE1KfcTVGCvdXJB0IC-HFawxEgHy3dZZADkFkb8fzqLFgb0D04ifxCmiPZZ88ZInXSqy_1CzF_X__f0GLMJz5Z1juRoZ4l34WsLRTCxx1yjCbE1cKTVyYYgqsqv-jQG0W1qcyVaIwUWlvS7FBIlZn9tV4TkR4TcKKCwYS6UbmQdOyaektO4xIKRPTtJ8_EO4Op3-jGKMIz9GZqM0GW85AcYkiyuAufAqWNAFLRuKGgGehSxyeRABTQGqr04MPbb4QfTvNfklDlAoYyktYqI_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه ی جدید رهبری در رابطه با مقابله با معترضین اغتشاشگر که دوباره ری پوست شد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/funhiphop/77807" target="_blank">📅 00:06 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77806">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ریدم از اون دنیا بیانیه اومد</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/funhiphop/77806" target="_blank">📅 00:04 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77805">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">من خودم خرداد ماه کف خیابون بودم</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/funhiphop/77805" target="_blank">📅 00:03 · 24 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77803">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqglqCGALIYYZkqdBbGmeZFXW-snSqrP96g1Kb1uxHj0Zt3Y9XsxkyFgG5xdogwJcZxpAu2BEvNcLiO621UpiBa13l2ydyrvzB1pZTPPtcazGW3QID2RHN4ZcR7_H6zdILJlrNDHmjIwJlSoG0mnHHreu0OVw20qUYoFavuEl9O6-R_mfSRJlLhx4Q-wjWZdWV8_UgCAm6PaojoFAymJEWzwvdmvR3vgwawSX3YKgmLeYiO7kKmyGsOs6oYRNAz6rSzA3SngJKcYVCmZJK-iW7_H4zloZ10jgPi6-ceAxiQu-EGIFdqxJhXAKEF6LUsyFAyl2SfeKxzfxNTHMjqezw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زنده یاد تا آخرین نفس پای رهبرش ایستاد
💔
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/77803" target="_blank">📅 23:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77802">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">#سوینا_رضایی جوان معترض ۲۱ ساله در خیابان ستاری تهران  کشته شده به دست نیرو های زحمت کش سپاه پاسداران صدای او باشیم</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/funhiphop/77802" target="_blank">📅 23:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77801">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sz0VEGNcWvXoqNKjY8dw4LPQ4aGcOCXg3q4AeAoGpLoOeKOn-XzfWNwIhFITG7kxPUIBSAPsgv9m6QkLb_uI3End7Lf5Ge78uK2SCN7yV92CLheReNhbqUfesI7Ypba22SjL07UrtOST0KCN2dYYahYl6UYecahA5lxGewfOEikvBQwYMynRdr9IBvpiLN-p3YHPqrY2YmlcP5fez7tXFvhPiaYLx9prU87SoKY-J-SJLB_U3mBvsg7RpCNyXIpAro9hNHCN2QmaxcziUHXiirmqbQawy0mdBWmsiCn5qtM3rf5mT3fMWaA9HQB3AWTuuA4auAvvRuCC8ZBucNYOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#سوینا_رضایی
جوان معترض ۲۱ ساله در خیابان ستاری تهران
کشته شده به دست نیرو های زحمت کش سپاه پاسداران
صدای او باشیم</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/77801" target="_blank">📅 23:52 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77800">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ:
کمک در راه است
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/77800" target="_blank">📅 23:50 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77799">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آقا کجا باید عضو نیروی سرکوب بشم</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/77799" target="_blank">📅 23:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77798">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">از نیروی زحمت کش سپاه و بسیج و پایگاه های سرکوب خواستار شلیک مستقیم هستیم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/77798" target="_blank">📅 23:47 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77797">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">منم به این اقتصاد اعتراض دارم
ولی به این نوع اغتشاش هم انتقاد دارم</div>
<div class="tg-footer">👁️ 7.08K · <a href="https://t.me/funhiphop/77797" target="_blank">📅 23:46 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77796">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">حجت‌السلام نبویان:
طبق متن توافق، ما مستعمره آمریکا میشیم. آقای عراقچی هرچی آمریکا گفته رو گفته چشم، رد نکرده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.39K · <a href="https://t.me/funhiphop/77796" target="_blank">📅 23:42 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77795">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">این آخرین نبرده، جلیلی برمیگرده</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/77795" target="_blank">📅 23:38 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77794">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هنوز توافق امضا نشده اوضاع اینطوریه، امضا بشه چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/funhiphop/77794" target="_blank">📅 23:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77793">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">پسر تروریست ها باز ریختن خیابون که
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/funhiphop/77793" target="_blank">📅 23:19 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77792">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">الاناس عوامل موساد به مردم شلیک کنن</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/77792" target="_blank">📅 23:15 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77790">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نیروی انتظامی، حمایت حمایت</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77790" target="_blank">📅 23:10 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77789">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">نیرو های سرکوب وارد خیابونا شدن و اونایی که علیه مذاکرات و قالیباف شعار میدونو سرکوب میکنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77789" target="_blank">📅 23:06 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77788">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اغتژاژگر را باید بر سر جای خود نژاند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77788" target="_blank">📅 23:04 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77787">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=NMysA4mepKtB6I3ytvNvUlG05HyDnvzhIe9z59Uls5iTCKKkRIoBNmvpVXbrrLXE4sIgPFdByRDuP_KunaDwOhMvFKYI3OndYQnQp3RHqDJAyScyx0NBtHWOj7MyZasf0bAZfe4ztWypgThWELkLQSH85pz7Q5LopTifMVWF8ThGLS3BPjAoq1kY9PFfFBxQBZTzI3Qh20IQQfuvmq9ZdFe9qCCqU263t-WHVVJwT4U_ejLYUoPNAUyzPFNp-EXq6eqpTsaPLIvxKlRb2rt5dSsiZ8QuKJWGnLoeNRu2FMCRmIzP6L5UQU1QAz5224EXkPxgN_2HYCuijkR2EoQ-6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bc96beb56.mp4?token=NMysA4mepKtB6I3ytvNvUlG05HyDnvzhIe9z59Uls5iTCKKkRIoBNmvpVXbrrLXE4sIgPFdByRDuP_KunaDwOhMvFKYI3OndYQnQp3RHqDJAyScyx0NBtHWOj7MyZasf0bAZfe4ztWypgThWELkLQSH85pz7Q5LopTifMVWF8ThGLS3BPjAoq1kY9PFfFBxQBZTzI3Qh20IQQfuvmq9ZdFe9qCCqU263t-WHVVJwT4U_ejLYUoPNAUyzPFNp-EXq6eqpTsaPLIvxKlRb2rt5dSsiZ8QuKJWGnLoeNRu2FMCRmIzP6L5UQU1QAz5224EXkPxgN_2HYCuijkR2EoQ-6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">باقر شاه در اسفند ۱۴۰۳:
صحبت‌های ترامپ از مذاکره با ایران فریب است و هدف او که آن را امضا کرده خلع سلاح و تسلیم ایران است.
مذاکره با ترامپ به رفع تحریم نخواهد انجامید و نتیجه‌ای جز تحقیر ملت ایران ندارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/77787" target="_blank">📅 22:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77786">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=HmNhQyQpocHwnGa7WI39s7vX94-sPYe1NGA8tZsGSsip8xq0hKfocFon6TrXxyDfbREVYD8h3FauXqJotuP3i8dTBQHDfXK_UP5MDyMb2vv8uxVN5MIbbRk3oZ1Un__DfzEVOYAMRK1-gUdw9SSh4OCfLTFRNJgjEnHr1ksGwMUb49XbtaFNHjexviytp_zuy-NmZJRuULy1sbk777swDLRhVU-G8UyowcHHv2hlpNaS4dLFmP71xb6jYRRsoZL4roMJOJOD7XTmWmGHA3ljC1T5fMRwQ5JGv0BcAkd0ZiBlECcJZUaJpZ5VnzCrxEWf2PtkF7HtiKB7n0WbkVpH5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63e89cbdbf.mp4?token=HmNhQyQpocHwnGa7WI39s7vX94-sPYe1NGA8tZsGSsip8xq0hKfocFon6TrXxyDfbREVYD8h3FauXqJotuP3i8dTBQHDfXK_UP5MDyMb2vv8uxVN5MIbbRk3oZ1Un__DfzEVOYAMRK1-gUdw9SSh4OCfLTFRNJgjEnHr1ksGwMUb49XbtaFNHjexviytp_zuy-NmZJRuULy1sbk777swDLRhVU-G8UyowcHHv2hlpNaS4dLFmP71xb6jYRRsoZL4roMJOJOD7XTmWmGHA3ljC1T5fMRwQ5JGv0BcAkd0ZiBlECcJZUaJpZ5VnzCrxEWf2PtkF7HtiKB7n0WbkVpH5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ وقتی جام جهانی تموم بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77786" target="_blank">📅 22:09 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77785">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3780248517.mp4?token=gB0nC3drRIO3y0n4DhUbxBCqInkMyqKl-N4lykIh1CGQVhMzGMrYTOnwt49JXOJ3HGIiyeEomR8h5R8uPDvWE_zx9KoiR-FDgkcfOaJ1lEX8wjq2_taikHisBd-PILLiqobdJanXlSc2dFvmCyKadqbCdV0gITzT9rHgtjAiv2rT293eQzFUJLVXkJ0hgcI3YkYYyPv4B9IEp-rivUWS85Am_CFfiEV_UM4ZjHHQDAzZ_l3tQJvbxXDxuYk340INmmfnktr5m2u7NmcXWF5fhAn6QK-_ScPoV4Nf8AaDcwSJNqdvkHF8NTrjC13onxnH6cCX4tONVnrAEaaxhjmimA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3780248517.mp4?token=gB0nC3drRIO3y0n4DhUbxBCqInkMyqKl-N4lykIh1CGQVhMzGMrYTOnwt49JXOJ3HGIiyeEomR8h5R8uPDvWE_zx9KoiR-FDgkcfOaJ1lEX8wjq2_taikHisBd-PILLiqobdJanXlSc2dFvmCyKadqbCdV0gITzT9rHgtjAiv2rT293eQzFUJLVXkJ0hgcI3YkYYyPv4B9IEp-rivUWS85Am_CFfiEV_UM4ZjHHQDAzZ_l3tQJvbxXDxuYk340INmmfnktr5m2u7NmcXWF5fhAn6QK-_ScPoV4Nf8AaDcwSJNqdvkHF8NTrjC13onxnH6cCX4tONVnrAEaaxhjmimA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار طرفداران جمهوری اسلامی:
مرگ بر عراقچی بیشرف نفوذی
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77785" target="_blank">📅 21:48 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77784">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77784" target="_blank">📅 21:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77783">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تو تجمعات شبانه از یکی میپرسن کارتون مورد علاقت چیه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77783" target="_blank">📅 21:43 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77782">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اگه توافق امضا شد من کونیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77782" target="_blank">📅 21:37 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77781">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e7na8vGEao8O2Z3CM8luaPnAJReNdmZSLTTLph44S0ooH6NekTrBY-WN7GIPTgyaNmcpBH-9c_TcwBEoKaNaETjhYqVPmPvoPG9LZObxIxsoKpfqZJXfr2-XHEmilvDNIE2hTIbSJpMKPMhgP0VaJKrMXQcpyDwMdQRf-DlinNaJ0GAVRgcNOxtVHsYKTQTOCemaS_qqEA4bqIJDIQQGsE5LltFWQKLta4RW4yOy0pr4DpdOk8BxCmZISUEflZuGoqzgmYLTtZ22_iuPk74xh4C99gDV2p2e9ZXgWtI7Txt3uQBjkYoL-dgQJigAIKkf1QpMc_a1s4oAVpOZ_OH9RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Joji
📌
Piss In The Wind (Deluxe
)
📌
Piss In The Wind
📌
Smithereens
📌
Nectar
📌
Ballads 1
📌
In Tongues
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77781" target="_blank">📅 21:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77780">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">یک سری جاها ظاهرا طرفداران جمهوری اسلامی با نیروی انتظامی درگیر شدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77780" target="_blank">📅 21:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترام: فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای…</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77779" target="_blank">📅 20:36 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fWDFKUMEhiYCiuTuvV--cW6E_Tou98fU0oEFyW-k9czaAySSBKtmAlazflebpbnudFoZCILhAZYy4lPKURLNFfwb784kSq0GfWuzsjubAyInx70Yk3fJT6ZKoRbZG18FQPxTivPWJfEaqRSt6aOqVBSky0I7ytERjmrS6uAIzNzpTetLm07-nQXAdbMpOAVijkKSYFRLsmhW8UXp5IGINL3C9AkJbPdlowbGSBPIwsl1gmRFx6p3GeKDzY-9zqEjWmdfsjtodFcxD4JeNUKBGQpZ29Fy3VOc25B0VEgGi6uSmSc4UJAjdY7G5D_PxWS1OXDsElgWbVM6p2IVuWdPTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترام:
فردا تفاهم نامه رو باهاشون امضا می‌کنم تنگه هم بلافاصله بعدش باز می‌شه، امیدوارم توافق نامه نهایی به سرعت پیش بره وگرنه خواهیم دید چه خواهد شد، بر خلاف اوباما (ع) هیچ پولی بهشون نمی‌دم، به زودی هم وقتی اوضاع آروم تر شد می‌ریم باقی مونده مواد هسته‌ای رو از ایران جمع می‌کنیم میایم مادر گرامی بنده هم جند
توافق باراک حسین اوباما با ایران، برجام، راهی آسان، زیبا و هموار به سمت سلاح هسته‌ای بود که ایران شش سال پیش می‌توانست داشته باشد و خیلی پیش‌تر از حالا از آن استفاده می‌کرد.
توافق من با ایران کاملاً برعکس است، یک دیوار برای نداشتن سلاح هسته‌ای! در واقع، آنها دیگر خواهان سلاح هسته‌ای نیستند و نه از طریق خرید، توسعه یا هر شکل دیگری از تأمین، چنین سلاحی خواهند داشت.
قرار است این توافق فردا امضا شود و بلافاصله پس از امضا، تنگه هرمز برای همه باز خواهد بود.
روابط ما با ایران بسیار متفاوت و بهتر از دولت‌های قبلی است. برخلاف صدها میلیارد دلار پرداختی اوباما به آنها، از جمله ۱.۷ میلیارد دلار پول نقد سبز و سرد، هیچ پولی رد و بدل نخواهد شد.
در زمان مناسب، وقتی همه چیز آرام باشد، وارد عمل خواهیم شد و گرد و غبار هسته‌ای را که عمیقاً زیر کوه‌های گرانیتی غرق شده و قدرتمند دفن شده است، با کمک بمب‌افکن‌های زیبا و خلبانان درخشان B-2 خود، جمع‌آوری و آن را در ایران یا ایالات متحده پایین‌رده‌بندی و نابود خواهیم کرد.
ما مشتاقانه منتظر همکاری با ایران و کل خاورمیانه در آینده‌ای دور هستیم. امیدواریم این روند به سرعت، آسانی و روانی پیش برود. اگر چنین نشد، ما جایگزین نهایی را داریم که امیدواریم هرگز دوباره استفاده نشود! از توجه شما به این موضوع بسیار سپاسگزاریم!!!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77778" target="_blank">📅 20:22 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nYRgr02m3IzbNZYZmnNtOpf-FPCpriOo9A8ggeubMlqoVUTKIpodYhdsVOnPamlDJsLS-osHlPfi88WqZ2ig49Sk4NCDvxx3bfTiBuxX8gZFHspCBE8Jz4gMntxmZtMqkm_MEOkC-SG9hsHAHG-a0U5bRtZTsf-Q3rFqPfdOcWbaiI8kOR_Bdf4VlXbK5UCzsHUsOI02JG6JAQeO_lVgoMzXfz2mW9q_EJs5220W74GKqFlQGxmUvMorFDfrC4cVijPkfUvMNABqljCDsAw7LbNSNBnKQ3L4MFVb-Q1lcG393GsQKXOErryfQRB3IgB6kOtXMIo5tOPzJnmSsdoBqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب کاستومی پسر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77777" target="_blank">📅 19:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/n-XAYk4cHvAPMWkF3NvGoTvl3SW0Z0tzi6_UCfXI5eMZDIZAxzuCeeY1N6FmVV9UYJJNtdlufWPaCjtS3wHel6BgYoLG7jwb5ZyebK4HQSGc2K3_eh75jDyoTj66T3DDxSLFTDwIYQH34D4CefI6GWdpnwLNOs-bSNqHeTgaLevqu_pAHYh7CPx7GdtTh2Mgg8Q8kGUo1ZCKh25jYnVY-KY5XVKGf294ikflBrEDHfYgS00POMkI09oiWwpyZY9VMfU-jPPT4gwgEFoUJtvcQP0XWcSrvTh3HZajHluxB8iTF6Wav0B4M1kflDOpyFV0_4FV8X6MtgZdGVGjLO8CtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع برخی از طرفداران حکومتی تبریز در اعتراض به توافق با قاتل رهبر شهید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77776" target="_blank">📅 18:18 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77775" target="_blank">📅 18:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">آکسیوس : فردا توافق بین ایران و آمریکا امضا میشه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77774" target="_blank">📅 18:00 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77773">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbPfzMWH0OBSfWvsFa_kttAriGWAHLpUgLUYePEeU1rPo7UlmMkzIq-1NyB8QkX8c5wkqFCtHfO-YWJhonqeqxV3f_QWPFAaVMmW96y12GilVBNrYUaaEcX6czC_heDVxOe8aIdV2aXSDS6dt8wIea9QGonCeChoPJkcJ2hMVHJwvZTIOthwOjXvgGlqpJrjabe-uLPtMT9-LdvPbvKM4qi_zSCbZYiSUGp177L4hQviqotQYuVHqlG75OgFXRO8ynfVDNCARvZRqMQeJ9rtY8hIUaiACzwPFgo-7HmFM-Vw_rMu0IgroBoS_Qw7uGnPvWYblarOOj6d0vJM1uBMgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی آمریکا پاراگوئه عجب بازی خوبی بود پسر.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77773" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77772">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/77772" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77771">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD_ZOMOGVIWhyBSz1KuZPyMDiKcLAJ5ePjGjgMjBtfUSJDg05CnAMIvkvOFQT1i8GGhV-PQrsE3L6Yk3c_ENiVIWg1sveY_FLFJoYUNx5ekQYCn_H2NFKvJ7MIhr72Rso6HBt7KJ4STZU3lG7SXmG62H_z_xi-zr9xcxaBPvYy6joH_M5da65y4VJ8-eP3rws3GQTl1a5YFmz01C9GJ0fHzmTggAvVuWsDAZGV-hhchYcetZqKdMM-MccMLG7cjzSFAJv-GwFoNkcycFYjC3YpAa7u8H5YluogUfTtUhBTrHnpDb218W8GhCnKyog0zB0glQiVOCg5oCxV34H9BunA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g23
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77771" target="_blank">📅 17:56 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77770">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJ6FAFGZb5Y5CIg3XoZVauAfoyogmA9L99a1T0INWzK-vz09ZVHLhvqOQ2z6q4_mmebO6rWqM1fpkK2OcHJLwegodCFK8YUxrMBoJHN4RX3F_ajtQQe7VKhEBqKfNGkkh8RrtZto2nFHIUCoNnHs0WdtH9qbGehXwh90HV2xX4RngI4-nInXzSJewiv1Rx1yFTNNH5j6TwJwQaOuRJUvwRnrVBqDq7g62kCrdJPMvDqvTvRonwtdLRUKV4s0_tHwwvMI8Vf6uWVDnfQ-zqnX5vNEi08suONnuEfh91HniHfkG6fT_41Hm-h0tzQJZMd0C9AuJ7L8OGLIYvQeuiWz_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رامین رضاییان داره حرمسرا جمع میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/77770" target="_blank">📅 17:53 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77769">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سازمان UKMTO گزارشی از وقوع یک حادثه در فاصله ۶ مایل دریایی (6NM) در شرق عمان دریافت کرده است.
گزارش شده است که یک کشتی نفت‌کش در بخش جلو و سمت چپ بدنه (Port Bow) مورد اصابت پرتابه ناشناس قرار گرفته است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77769" target="_blank">📅 14:59 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77768">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFP4uQWKbrLkWMyS7iSr5YPXhjUGexkGxaudRiiQ1zB0sB4xS0ciB7vzpERxnbyEkyYUXsoPQiniJze8KkTRamF2ZLRW-0hh0a0jkTIS13eQDdJJaRnaERjnVw6Bb9_T-UtTlavpZspTbu-UmGpFjhqs7qxRkC7KvNXy-_XMrGnarV443X4X1Y-Wo9axht9NmqJwRZ3fbQ2XRFjlHrNufjYqc2cUvPg5BqFZ5B_h-vRBWeEd_HptJwtdoo9rCVmE4xREelemyJkJuWf-z5XBqATiBE4E30fshQlPCiTDruTiHGwTFNJbNRZxRrht8kbQut1wB2vP_eCdSx-TkMFbGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ای بابا
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77768" target="_blank">📅 14:57 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77767">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Owzi2hdnXjf2xleB8GCupAWMniEfqFsmfXgnQkGjXc9NyC4PfhvSr-pbsNLnuT4lLf8XP5bdHLFbIzOjt_Nk19y9jc944rbZjcp0EEy7mO0CpnTWV5sQTz3xJkq3EWerSqMCNF2RT1fZFQssqqicZQa6ZorddO5lEG8SuACRzlyPpYn4u_3xG-ceMNc3cTM7YWlwb6DVmxsoJj_cr6ZlLGHzDFNl3XJXhGN-Qtq0JshdF62DSM-BABv4WkqcsQySwf3636Jb70kTgwv4pfi0J-Q1VCIYioNcWG2Zn-Qg1_MbS5M6lvFdHozIq8rAMvEE72TavPPqwNROvEefkeSGRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهباز شریف:
متن توافق به دست اومده و ما انتظار داریم تفاهم نامه تا ۲۴ ساعت آینده امضا شه و بعد از اون هم یه مذاکرات در سطح فنی برا هفته‌ی آینده داشته باشیم
و ممنون از همه‌ی طرف‌ها که به پاکستان فرصت میانجیگری دادن و به امید صلح پایدار.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77767" target="_blank">📅 14:44 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77766">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">چرسی داداش چی تو خودت دیدی سولو آلبوم دادی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77766" target="_blank">📅 14:24 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77765">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WmcsG3Oaankc6t4jpoA-Q3E_wBP7lyLz_N1cCQbPyYliKZHy_3WGZNFWjaeuMuXMagDktp_vokARrJa6iC3zJnrTWaFULYJXFstceezUFGed3_MJHwfe2gN7XDWfMQdnADYSko4Kc7k5q98P8ED696hJPnNyMAoxnSkEo4lLG0pqv84azApCsRPovFngzBmV5c8FWN32PJm0UlS2R0fQz6lAZVPsiwbEokSfEu5BZfAJXWtS0EtmqEukUmDb5fYxEhRdkxcJmICP8I_qa9s9h4yJ_zi_WnQsyLfdCjKNvTMu4WykGcmgqoTXlOoYRRaXqwd9OBbRzWIX--5VMrR4ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Drake
📌
Ice Man
📌
Habibti
📌
Made Of Honour
📌
$
ome $exy $ongs 4 U
📌
For All The Dogs Scary Hours Edition
📌
For All The Dogs
📌
Her Loss
📌
Honestly Nevermind
📌
Certified Lover Boy
📌
Dark Lane Demo Tapes
📌
Care Package
📌
Scorpion
📌
More Life
📌
Views
📌
What A Time To Be Alive
📌
If You’re Reading This It’s Too Late
📌
Nothing Was The Same
📌
Nothing Was The Same (Deluxe)
📌
Take Care (Deluxe)
📌
Thank Me Later
📌
So Far Gone
Enjoy
🩶
@DiscographyTship</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77765" target="_blank">📅 13:16 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77764">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چخبر از توافق؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77764" target="_blank">📅 12:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77763">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیمار بازیای گروهی جام جهانی رو از دست داد
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77763" target="_blank">📅 11:25 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77762">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCr5IRmrBZVz3jceNAM_9A_2sKdtKz0LMkq3eRpxYmB1St1pJXEEqR8Kc_lO95YLqCyrk6WfE3Y_xqT8Vjc-XJ4ZCh714u6RhC1b0-ShLLrbL3zNq9RV3BqLBBTiV0cI3wFzm6k9H48D60QDi8w5-D_oxbNpKXxCJ5Lx6kEXgdz3u7kwktJgfpjHMssckRNPW1k-AicMi0uLAoL_g0ezybTTvIdvd-ju84oPk3FzslfV1h1BTGrZ8mWMmW8ZYMw0Np8xEkEMNQtH9VYQqnUkA38V2SmIRxa5vxMr3HHhL20G-M1-5lCxu9FaTwiPQSwnXvv9Y7FASKhmmGC_Y25zLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو نگاه اول آدم میگه طرف یه عقب مونده اس که اومده برا دیدن فوتبال، ولی یارو جزو تاپ ۵ بهترین بسکتبالیست های تاریخه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77762" target="_blank">📅 11:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77761">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آمریکا کی انقد فوتبالش خوب شد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77761" target="_blank">📅 10:33 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77760">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odNEFBJdhVO9bgOm1jYs4U8GiOTMySLerilsZlD-KvCo8tyuQuzmVh6Ixp4qE4KbcutbiN-Y9yR48QIQi2u8vgMrVUuojr5jbykyDJAOK31KdqEaUuNKjw6l7OBcV834fSis8rw_g2Y32BqJmgDMNXMpAIQMLv7ON4mf6znodyU7cBY9KR4pFOyWUzVkTb2SrWo4X43wCRTty1IGk-6Pd-a9MNA5uflCF1hBabqL9d66J5fLHcXhgVZj3MRnpm_X2wrz0uXnfpY_rRJQWsGJKRIzelem4v7EO4xQKzatKP5tDG6pWTUYmNjGqhl4vrqit7p_MMt9RX5Yefa429AIag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت قهرمان بازیه پسر، شهر به کمک کن نیاز داره.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77760" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77759">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/77759" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77759" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77758">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zo8Q-gnsr3OX3k5vn6B3vo7Zo3NGeVAYCDBMrC0_pp4BdZG2_dqLQxxExanNr3m-3dLMRKCmkNbaPfDktCM4oLoKtl4XN0Qxg6Gh8L7GZMC-su2GUhP_ke3TegkA_4RTRdiDLGOHDA4pry_PPP2qzEQKNoDX1F2RUvyjwMDifkEsARVJ5LHK3qgOLOt2NYe7Dvs_s96tZlQdKHHQ5f7uaw14eE7YPaQl0fLcjBc4069HpIQI4RObFe50_8beuBLkPDVW__l8T9fn-B67e82MUVBmbQoQ5d8WXHMGTNyWsv5sf_aNcim8pKKUnApZs1lgkatzALdn5tYzLPDK6CJ2yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r23
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77758" target="_blank">📅 10:23 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77757">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه) کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)  هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77757" target="_blank">📅 10:03 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77756">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رویترز:
ارتش آمریکا امشب چندین پهپاد انتحاری سپاه که قصد حمله به کشتی‌های عبوری از تنگه هرمز داشتند را منهدم کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77756" target="_blank">📅 04:01 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77755">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LFu_h-Vm2N3oet8BHSB4jCB1_qwnKX9Kd3YTyEG99N0hXtum82RhufEQYmHBUYcC270zTA7-Zk7JUy-Jue4m99j80vwgkOazZ6PJDtQonZBa6iv8AJw1xBO4ZfmgN-BYrBhL1tWArPtsSdiCEsEjiVPPZYYseT3GuC7ELcp94SPbfc2RWgBWt3qSedOYHcfyvSL3XioZjfaw-X6_SCU8JHYycaF_cnGBNNIi4wbEfRQWcWG393p4pcHJ75xc9A7EiyhzFCBKFwQbK9zSGtgDGf1F6x7lHvfqJY-v2GKhE_cO2uTw7cR35PfcGUL_g0Vhq7Pdg2frt22_DUGXyIUYew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار باقری هم در اتاق جنگ بود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/77755" target="_blank">📅 02:20 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77754">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یک سال پیش در چنین روزی جنگ ۱۲ روزه شروع شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77754" target="_blank">📅 02:14 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77753">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امارات آزاد کردن پول های بلوکه شده جمهوری اسلامی رو تکذیب کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77753" target="_blank">📅 01:51 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77752">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">زیر این پست قهرمان جام جهانی رو پیش بینی کنید، هر کی درست حدس بزنه صد تومن میزنه به کارتم.
@FunHipHop
|  محمد رضا ناصری آزاد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/77752" target="_blank">📅 01:02 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77751">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=nTM9evO7BXxxx63eXjGAMAeLvPSpsR3NWq7LGfNkew4FPf4TZcKOswNnPOug_UPScQVM9UQNSbBxNdn-yX2nUcelpWjbSgkgmVRGfk4zKOH4fnF63ist8rXQd4jBiM-wpIsl1_SsUcmdqeZ-ybZobL72HIPab25PEC0S6rAXlwNAU3FOY4l79Aild6JzeDr7hagRzNju1b2DYhycKKE7lQC6SRWmdr1r6Au345sAc4zLXOGMlTOcJhLaTCrJfK733uc0XszpPVnrAQwLCTD-uXRGAQ8Ug-ENlcTUnPtI8x5lguGww03-itLEqujf4XpTRZg8OTpfOu4Ss4n2BU5CSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e3c0e5144.mp4?token=nTM9evO7BXxxx63eXjGAMAeLvPSpsR3NWq7LGfNkew4FPf4TZcKOswNnPOug_UPScQVM9UQNSbBxNdn-yX2nUcelpWjbSgkgmVRGfk4zKOH4fnF63ist8rXQd4jBiM-wpIsl1_SsUcmdqeZ-ybZobL72HIPab25PEC0S6rAXlwNAU3FOY4l79Aild6JzeDr7hagRzNju1b2DYhycKKE7lQC6SRWmdr1r6Au345sAc4zLXOGMlTOcJhLaTCrJfK733uc0XszpPVnrAQwLCTD-uXRGAQ8Ug-ENlcTUnPtI8x5lguGww03-itLEqujf4XpTRZg8OTpfOu4Ss4n2BU5CSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میساقی تو آنتن زنده خطاب به کسایی که مخالف تیم ملین: آدم مفت بر از خاله کسکش تره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/77751" target="_blank">📅 00:34 · 23 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77750">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سیریک صدای انفجار
😂
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/77750" target="_blank">📅 23:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77748">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">عراقچی:
دو تا موضوع مهم هنوز مونده برای توافق نهایی؛ یکی بحث تحریم‌ها، یکی هم مواد غنی‌شده. راه‌حلی که داریم اینه که غنی‌سازی ۶۰ درصد رو رقیق کنیم. در مورد تحریم‌ها هم، ما مشخص می‌کنیم که دقیقاً کدوم تحریم‌ها باید برداشته بشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77748" target="_blank">📅 23:25 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77747">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">عراقچی:
برای خدمات در تنگه هرمز هزینه دریافت خواهد شد و این خدمات دیگر رایگان نخواهد بود. این موضوع مهم تأیید شده است: پرداخت هزینه‌ها الزامی است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77747" target="_blank">📅 23:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77746">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">عراقچی:
اگر در ۶۰ روز به توافق نهایی نرسیم اما دو طرف از روند راضی باشند ممکن است تمدید شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77746" target="_blank">📅 23:21 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77745">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">عراقچی:
محاصره دریایی آمریکا اولین چیزی است که در این توافق به آن اشاره و تاکید شده است که باید رفع شود.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77745" target="_blank">📅 23:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77744">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عراقچی:
به‌زودی ایران و عمان بیانیهٔ مشترکی در مورد ادارهٔ تنگهٔ هرمز منتشر خواهند کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/77744" target="_blank">📅 23:18 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77743">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">عراقچی:
دشمن تعهد میده که دیگه آغازگر جنگ نباشه و از تهدید و زور استفاده نکنه و دوطرف به حاکمیت یکدیگر احترام بذارن و در امور داخلی یک‌دیگر دخالت نکنن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77743" target="_blank">📅 23:16 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77742">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">عراقچی:
توافق شامل دو مرحله است و موضوع هسته‌ای را به مرحله دوم انتقال دادیم و هر وقت همه چیز قطعی شد به همتون اطلاع میدم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77742" target="_blank">📅 23:13 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77740">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_wbzcx7f2SJoEH-bUOVegQHPMgMSbtfCFFh-mv3CBpZUoEyihR76P3u9TUfGf6EC-BIR0wvnpsqHeHiszritLgR4cKqszhVVclwUUoPpZOsgNAPQYsTdl5dMlyLQr_GOnWa9h-19wnJ63R_WBPfLX3TqhKDHECZr-jPU3r-PESY1XPDfwrW3jqtX8tJiXXmfsKPT99OTJIie6lNbYeMd4IpKyN-vL3-92weGF5XECT066OtTh4ZlZxnT4zCRa71tNJxXsfXvouxm9IO4l6vnIY-uAjf48IemZvTR0OFjfmAqOutqr9VWvVOZz9IV25ZO4UUEgLat5MdF89UsRB1_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
YËAT
📌
ADL
📌
Lifestyle
📌
2093
📌
AftërLyfe
📌
Lyfë
📌
2 Alivë (Gëëk pack
)
📌
2 Alivë
📌
Up 2 Më
📌
4L
📌
Alivë
📌
Wake Up Call
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77740" target="_blank">📅 22:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77739">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-cyO6ob-aHHQEBGhqL7nWccvCoG9EzItSkON9pQIhUNcHontp76dXcnBIP4YQm6-vH4n-HOmu3tPWkQE_JW-4P48GDD41ag8AX6Jzoyplm2YbjTz_K4J7BMkuuT7AM_MDG_ycnMvtm1lEN5VJq3wvLWdJqqm2LoNiDHu3hYoPI0MuI1W_mdmFB_lyxmR2mXSPFuZ8R1Fo28a3xd0xliaDVcwYOUYBynoTmkqkDw8aLtvM6cEpF_f1ERGMbnnZtqL80Xr0d0lBdoM_q9sVKIlP2vNz6qLZAalrMxh2_FcVaxuwkR4fcwyJkkog0C1NS_QhbK32c76gQZLIquAba1Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف خدایا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77739" target="_blank">📅 22:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77738">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hO5dapp5UON_FtSJ5MzIsAN1XCOBTsxTuM4k5zELvo7lWIK1mDhgNb_o7EaCRgFnu26jzPat1CkKxjYZl0gMPQxH7ns_inHIh_JoGpyZF612n9_p_WQaoF6QsY0fz-X4bfgzFIVD9IrsSDjXzRm8Fwd1mHIoSIbrlkLONHKeCCWQ70zpOs7g1UrktfgQyfprZKB6avA1qcpAmjEQOKriozwpbmls38Pu0mj6jqaWpTcEXuu6pcjQh4aoZQcslRGso8Eyjg-s4UHq4R9dsEZLeoo2RVh9JhhMrkYdy2OpJBrHraPycVXxKe7HEXUVUoLMEPiGNODYQ0O9xxMUpL02mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">درود دوستان شبتون بخیر
💤
امیدوارم حالتون خوب باشه
❤️
کانفیگ داریم سرعت جت
🚀
(جتی که حرکت نمیکنه)
کاربر نامحدود
♾️
اتصال پایدار
✅
قطعی ام نداره
❌
(چون اصن وصل نمیشه که بخواد قطع بشه)
هر گیگ کمتر از 7,500 تومن
🔥
لیست قیمتا توی عکس هست
👆🏼
ایشالا که گول حرفامونو میخورید و قید پولتونو میزنید
🫶🏼
Channel ID:
@RezoraVPN
Robot ID:
@RezoraVPN_bot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77738" target="_blank">📅 22:00 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77737">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید میخوام فلش بک بزنم به حدود ۲ ماه پیش  عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد نتیجه توئیت عراقچی چیشد؟ رفتار خودسرانه یکی از باند های قدرتمند…</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/77737" target="_blank">📅 21:30 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77736">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/benltUHZZn22L8Dk6bY4kVq4X_Q_-iOau0DpWrmJbfPFJy7YtoSTgOklchYx2HRlcwjZUBPTI7yitWzxz3k-4yA2wYxZ0M0Lr9hy0bBj-0kf3gNGBrB9XLPkizuqfn221zoIoGCEgeCm-W5IPEO6CKj_-Eoe_R6P25EAQe0BjkcEvbVZk3jc1Cqc1tANuNQIxFAVvVPGOlYD2_7d6Jy0uD0ohWkgdUwwx-kw_n85iVOAZ1cVTx-_RgdgqZWAPbGyxyOWJgdPtosMPiZlw8QFFOaEGo_3Az3rlpNMkkLSWDMLxQIctpsxYysaPrDGKoW3E3ephAZclzWyRDVKzvCvuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Kendrick Lamar
📌
GNX
📌
Mr.Morale & The Big Steppers
📌
Black Panther The Album Music From And Inspired By
📌
Damn. Collectors Edition
📌
Damn
.
📌
Untitled Unmastered
📌
To Pimp A Butterfly
📌
Good Kid m.A.A.d City (Deluxe
)
📌
Good Kid m.A.A.d City
📌
Section.80
📌
Overly Dedicated
@DiscographyTship
🇺🇸</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/77736" target="_blank">📅 21:20 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77735">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXuPQtUyenPzwn15JwDxbDSnScw356GxLwQpuhpj5VOs0NqWf7gY52TGO9-WZt4LbH8nJWIDxNw3oaVmm_hPa9iZP9zw_2r15DW1E66JlrsqR83OkRufdZFzCeqtWGoWsoPyypzDIkw3K2i8eACRU0G6E6Vg3BwAYSHsV1YPXTPRV595mn22dfz5IKx_t14tk4dlIRWxiWfEjubhOEdE_4W6R0X5YU4ncAaeozUFEW-IAdimgVRMJ09s2IKd5Rh0gFFySw_9YKmQGRP7Nt_2qVq6b41vspsPAtGEOBNZ6IXNj7mEAket42WlEn6Un-GiCxA9p2XQmx8ToDjQZjuFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم افغانستان میخوان قیام کنن، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/77735" target="_blank">📅 20:46 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77734">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">مردم افغانستان برای امشب علیه طالبان فراخوان دادن و قراره به خیابون بیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77734" target="_blank">📅 20:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77733">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه دیگه از سیاست با فرید
میخوام فلش بک بزنم به حدود ۲ ماه پیش
عباس عراقچی در یک توئیت اعلام کرد که تنگه هرمز باز شده و ترامپ هم در مورد این اتفاق بیانیه داد
نتیجه توئیت عراقچی چیشد؟
رفتار خودسرانه یکی از باند های قدرتمند سپاه و بسته موندن تنگه هرمز، ایجاد جنگ داخلی، حمله خبرگزاری فارس و تسنیم به عباس عراقچی و …
الان هم به احتمال خیلی زیاد توافقی که ترامپ ازش صحبت میکنه با باند قالیباف و عراقچی بدست اومده و این میتونه تنش رو در بین مقامات باقیمانده به حداکثر برسونه
باید کمی صبر کنیم که ببینیم واکنش باند مخالف توافق به این توئیت چیه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77733" target="_blank">📅 19:31 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77732">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میشه بگید ژنرال یه عکس دیگه بزاره؟ من نتونستم ساعتشو ببینم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77732" target="_blank">📅 19:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77730">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dpg4ebBr6Er0xHo5VFLVWg3ZkBXVTzIXOO_PFl5htmsZ9xJ8_U6bOjqtrJIafL97Ux0r_qRZODN5d5tDpe-JzDNdm22ET7yvS7docp4ER2JmiU8J1rzH6Ewg46M8B15hExVU8iqIUAmaKmsXxlHyB3-7E8299cTWmcpolSW8aiHOprp_6LSXIG3DpIN0pEmUoz1mklhITU_3bT8nmuzbOKJkbzEOzEaE9B4K0PnvKZZaEpKr1QxOoCopg5-3fDO3PdelkxRMARLX0Au-0kEemTA0AR9FI1PkMmw5uuKdgDTNU9r0JKdnjrzUh6Cjs641LrvDjEkAkJqidSsuNyQIXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دالگخیز توییت عباسو ریتوییت کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77730" target="_blank">📅 19:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77729">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVRHYt3q63g4yEOAR-aMEfp8toi4e0e3Uw6QmIsyVHW3-RtECOmpQCWappkEmB-Wbd0TqsdgPRGpfm70FdxdUmfvhJpgXhqwbVlIiwueF0qaFro6wbUePUnxWkmIOF--fE6NdMuA88eoH9DXonwb0Sgq-TCj6MvtEa8Yo4l_8CIi5KcI9Fx7XkuPTEpVdrc2eey0kj32mAF7fpx709s50VHvx9HvTcjkNjug-OTdFVN6lGeEasCvUpQGdddmn47dd4QshNzKJZIjV9TPdUsG53oWs4AA4vceYK3wVsJtl-SkH8bslSLtnxTl9hWYjY3N6HN6iP0s7Uzw476Hsq48Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سری آخری که عراقچی گفت به توافق خیلی نزدیکیم هفته بعدش آمریکا و اسرائیل حمله کردن پس تا یک هفته دیگه جنگ میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77729" target="_blank">📅 18:39 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77727">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">عراقچی:
توافق با آمریکا هیچوقت انقد نزدیک نبوده و مذاکرات به جدی ترین حدش رسیده، بزودی جزئیات رو با مردم به اشتراک میذاریم.
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77727" target="_blank">📅 18:38 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77726">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">شاهکار ترین عکس روز  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77726" target="_blank">📅 18:10 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77725">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZTHhWfLAsToS1Hg6aOSQinDDb4Z43W97PJm9ZR_R6QE8-IKL6Wzgr3pBFdOjvHFxgEcWZPGteQ-8rSGCNjJQB-5d-Cjdi91fPa16hdk0Vp-YeQAbmUYFykDfAg6e3dJFYKX8dt6fpApR-1rc5_yK9U-IlUdq2TZaZcswrp2dTFroQs-2fHhZOWIeLL9fSy8jrwTXXNDVXSYtIUvp9u0wvCc8T4M32ZD9xzBaTBT8fu2J2Fyb_4W4wwkWjxxpRo70ovrK-NbV7yL_1BnnP8vzXRqJAW7XMamNIWY0wBEXyhsRR87rpuOw4CYFg5UHfDel3BtsHEiQQ5zZKbvVXJDoMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار ترین عکس روز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77725" target="_blank">📅 18:09 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77724">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/anc7ctCcbUFAdc8ILMYpTXTn8CPfRac8fkcVWJ3ojtD0fYRFXJ2ymjppwKXxoZOdLKC80F_935hiK1JbEzixWVnTjWklNZYuIvRCO0eB5QIpBtww_9P_X0KJqghELFFFRYfjL4l5XoTEllaZRxwQt0pJFILl5ZCPQ6KIdVLZZwbhwI8cjT3JrVeTC_xy_g57M_UnVvUExObclP4Io4DtOFgisJCEuuf-fMShWEj23lql9NcgffYTmah38_PubUuAnTDdKmB8ucRcqCkkgRpgeEnnYQwZbJodA9AJjoAzY1bgHDz9S5PJo1ZUs7GUEIv9vLir05f9XC7KzuzyC8OOYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این کره جنوبی هم خوبه ها، حالا در حد تیم ژنرال نه ولی خوبه
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/77724" target="_blank">📅 17:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77723">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qgns9WVm8ShEHE6h27qb8x3SUjJi6p-bere4dJ06iO4u9G2N8KHsC602yzaqYdnzueUVGhRS3s3gXbfWoEBphn3hXmHG9dUTQZhlm8_6jSB7nRo8wdHQVz7RedUkUpScexAxT4UUU3IwMQFozH6TcZp_okMLCLcTYEsX8PGdt-J8_8KUVsGzB14quDzrO2diKEjsGbsDuAzxBGl4WGnUjBUlprBXjKusqUaV1xvq67NXrgUMSbrLQa-S042D3Qx1siTfatOtUvSjyV-3s1rtwvCFWsAfAYU0s25ajaoT1tm9sFRLkxbTbJQqGK0vUCeoMG-mGq4FnQ1J3i7p5jBhlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو روزی که همه ویژه برنامه جام‌جهانی رو با رامبد و دیبالا و... شروع کردن ابوطالب رفته «علی پروین، مادرقحبهههه برو دیگه» رو دعوت کرده باهاش برنامه ساخته.
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77723" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77722">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77722" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77721">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEC6SRLvMXNe8NtGiUHNrJEe-AzVaS2_N3sgZW3Dv1TLn_QV5DzaRFT_HXbPfOfVclb8ipqi6Jy9sBqPtUhSsSu0Qh-_iAwcRT9VuPP0TKaURTtiZlB9D-gTL0NDxS7ks1LYpbD-0Sjjfrs8eusM0579jhHiiQCrzeblLdW7J2baAPt1Yn-l7agFG6JFoXN9jH98-wwuAMnCosPea81KBVkabysWxtTKZm9821Nr4j7SA7YGt3qxNFrfsqu647XeaIl0DlAi_O3OG8EpnHljOr1EaW5HsfgLgUVAjk_HCYMP4fdLK8YkKzq1mwAIct955zC0_xVl61aZA0zMcbbaKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g22
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77721" target="_blank">📅 17:49 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77720">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رویترز دیروز: لشکر 82 هوابرد آمریکا خارک را تصرف خواهد کرد.
رویترز امروز: جی‌دی ونس و مم‌باقر قالیباف توافق امضا میکنند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/77720" target="_blank">📅 17:42 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77719">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">فاکس نیوز درمورد مفاد توافق احتمالی:
مواد هسته‌ای ایران نابود و خارج خواهد شد، برنامه هسته‌ای آن متلاشی می‌شود و هیچ پولی آزاد نخواهد شد تا زمانی که تعهدات خود را انجام دهد.
یک مقام کاخ سفید گفت که تنگه هرمز به طور کامل باز خواهد شد و ایران موافقت خواهد کرد که از حمایت «گروه‌های تروریستی» دست بردارد. (دقیقا کی موافقت خواهد کرد آخه حرامز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77719" target="_blank">📅 17:33 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77718">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=epKcLhcxHDEDMdpldImt6wmStMszPEVJYMQMZQOec7ZswbWJqkHNwRNq17sIxhXRo9srAE7cTwe54ss3_rDKC-KAmO-e1V7Xio9auOt3S9Z8BnfV8xkdhze5L5YES7kWjM-zUcqGGotIGlyR5kEEi-Ww5hsvRiBBJ4AQmUr47KLixtV68Q9Qz8Q4kaPDc3FHORLl431SRL_KqUyTiHHKgbPzca9KSNkaE5QzGskg5sI6OpcItqYiXG44Zz_9m9Km8L2_lJSPA2qJYGKx4W0_FkGKvKA-IZfyw4Nv7Rr4EMux-_ku6BNSrtX8WmUF05uEBR3wukr7BkTRdvxso5trFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c4a7984e.mp4?token=epKcLhcxHDEDMdpldImt6wmStMszPEVJYMQMZQOec7ZswbWJqkHNwRNq17sIxhXRo9srAE7cTwe54ss3_rDKC-KAmO-e1V7Xio9auOt3S9Z8BnfV8xkdhze5L5YES7kWjM-zUcqGGotIGlyR5kEEi-Ww5hsvRiBBJ4AQmUr47KLixtV68Q9Qz8Q4kaPDc3FHORLl431SRL_KqUyTiHHKgbPzca9KSNkaE5QzGskg5sI6OpcItqYiXG44Zz_9m9Km8L2_lJSPA2qJYGKx4W0_FkGKvKA-IZfyw4Nv7Rr4EMux-_ku6BNSrtX8WmUF05uEBR3wukr7BkTRdvxso5trFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77718" target="_blank">📅 17:28 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77717">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ یهو ریج بیت مودش فعال شد گرفت رو مذاکرات و رسانه‌های ایرانی:
شرایطی که ایران به اخبار جعلی فاش کرده است، هیچ ارتباطی با شرایطی که به صورت کتبی توافق شده بود ندارد.
آنچه گفتند، از جمله بیانیه ضعیف و ناامیدکننده‌شان درباره داشتن یک توافق، هیچ ربطی به حقیقت ندارد.
افرادی بسیار بی‌شرف برای معامله کردن.
با آنها، چیزی به نام معامله با حسن نیت وجود ندارد.
شگفت‌انگیز! همچنین، حمله پهپادی کاملاً دفع شده آنها دیشب علیه کشتی‌های هندی که از تنگه هرمز خارج می‌شدند، کاملاً غیرقابل قبول است.
بهتر است هر چه سریع‌تر خودشان را جمع و جور کنند!
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77717" target="_blank">📅 17:12 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77716">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dnNPxBhCl5WtsUTOYV8CNiB6spNQ0X51SJuElNeUMZ23ya3ACK0FwZyrJph__AgvTcn7jSGZwyGWrNpw3WYztXTKK-oliqkq4Gfsz8zNOb-mEo-pPHihiB1FnOBmYvxt4blEdUp4rkVyK1xNM7t5QPDqAa0SrhGqT5uVfvR0D-4vyHLj7PwbAuTsDt5-DbwOK4biP5wVMOyTWhfkPzpkBPVvgVD8QVUZ6KMezTpJj99zUM4XGNto9IHtwfpmpEyE56Zt7Kc0KSjg8LtlA06F-jFK_8kvg3RhQTjQ1wqJoZLSZ-AnyF1pVAxQo3Osri3r91tO0rN9bQh8sUJK-96ICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ارباب سعی میکنیم درست بشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77716" target="_blank">📅 16:50 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77714">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77714" target="_blank">📅 16:23 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77713">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">من تازه فهمیدم چرا علیرضا منصوریان کچل بود، خواهراش کنده بودنش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77713" target="_blank">📅 15:59 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77712">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cq9KX-6D2c2vncvNM1jpZlIW3aLC8sdl6908iq_AeYwPpq4XOqx0SxVLaGp7c1NhEyZb6Y_rU6HcANsqoCeeVsu8t2ZNWtYs4hysTAQRjx_U2gJ0_NUussmxWRJ4xb1l_IHxzkbebPg2cgEwEg7Qj40pUl_5-DxODDAxF6duIwz6IagddPPiPXsMLPs3M7MipdnlCoze5A39DJRTV6GiMUZlcv2nVZ_iluDTScZ0bOshDR35WJmN-1otwcs5F-cr20_z8swZCS8G0rRT1tBYN7LOla3VcHvUzK3_uLHQIHeKST6bpq-zqXjLaN_Easjw1fGda30wd2Jd9y5tVJxuUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام:
کشتی‌های جنگی و تجهیزات هوایی نیروی دریایی ایالات متحده همچنان به گشت‌زنی در آب‌های منطقه‌ای ادامه می‌دهند و محاصره علیه ایران را اجرا می‌کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77712" target="_blank">📅 15:51 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77711">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=SXhc1YKVLK2sJzi_SSG2kmRsqftd7SnuWBQ_xp7Eu_AWEjox9UhyjO1MI_Z_TKoF7ZdFJt0YfBIUv_XQxX0zoiteTcq1aoTtjGU_ffTQkVtdF6phyaCzxMOHqbAResZPKiYcrgBak15GAKwT_5Gogt6F8SiHN5YhXT66BY_kMQ0cene-uHuepVdCuKpRwQ1w1H0euQxCXZWJogTdOBOyjxo8jh_f_e2LTXyFDFReC63jbaOo3hys7CVR1b4MKtc9KLG9_73cQvDFv7WrJQibTHIxOMk4Gn3D1O9m8V4N022j4P0N6IAg-d2zcu4ULwuv2BdUZyt0Q3UjHtyTM2-5og" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1716c7017.mp4?token=SXhc1YKVLK2sJzi_SSG2kmRsqftd7SnuWBQ_xp7Eu_AWEjox9UhyjO1MI_Z_TKoF7ZdFJt0YfBIUv_XQxX0zoiteTcq1aoTtjGU_ffTQkVtdF6phyaCzxMOHqbAResZPKiYcrgBak15GAKwT_5Gogt6F8SiHN5YhXT66BY_kMQ0cene-uHuepVdCuKpRwQ1w1H0euQxCXZWJogTdOBOyjxo8jh_f_e2LTXyFDFReC63jbaOo3hys7CVR1b4MKtc9KLG9_73cQvDFv7WrJQibTHIxOMk4Gn3D1O9m8V4N022j4P0N6IAg-d2zcu4ULwuv2BdUZyt0Q3UjHtyTM2-5og" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
توهین بسیار زشت صهیونیست‌ها به رهبر معظم انقلاب.
🔹
صهیونیست‌های ساکن سرزمین‌های اشغالی که فهمیده‌اند کار جز کودک‌کشی بلد نیستند، اینبار در اقدامی توهین‌آمیز یک مقوا با سیمای زیبای آیت الله سید مجتبی خامنه‌ای به همراه رنگ‌های مختلف را در رژه روز همجنس‌گرایان نمایش دادند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77711" target="_blank">📅 15:36 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyL2ukzzbfywooTn9yCg-cD94SrYXEE2oVxyr8zrwWabXbXDUeeWV5pJkz_-cydjleK3L9g9U_cvD3NdMbYqQwY-L21WeQgIt0zWuc-B7XNNdVqaeWSub-xmPILg5TTz8v8uE_YEKMrsPfqptYHAyt5joXuyTTz0B64YkarBji2e87NUjgYtGVi97x2bXSOEQcc5BubEHotjz5ugC8lv63BH3MWqTbbHZBhHU3uCDQwY4yCA8g7WcHYaHnXExd9JmU86sDwQylG2BcHkE_Rcq7qKMjq2E_uZGTXAtPuNMnsaC1p-Ah6IpgbOho0rZExKGcaHTAJmmXm1X4m1nHa92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#رشید_مظاهری
را فراموش نکنیم
رشید مظاهری دروازه‌بان سابق استقلال و تیم ملی پس از حمایت از مردم بازداشت شده و ازش هنوز هم خبری نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77709" target="_blank">📅 14:48 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dlMGWCOwQY0OMXjpz5IN0L32LNie5hQiDrOKLARjBsCtzWpMuJJtNTshCBvMiVTP5HF6EUb4lP6osXeoZAihHJGFZflVDjnuDaCSahiSi2tjg5u-5oEBjZFAvWl-0M9Ah7NtZ79tgqB4PrrX4K43DKL_Y94LxzIGqbQd4WDicKJQ6RjVnh5zwe92T0Qn3Nc2c-rTZ_mGxyPKs2wwl0_jTiF12v0DiO3YmGXIaew2a1mK2XMZdd81HWx4S9CNMNfL2jnJDDqPdMDSYGT52z9xJugsA7k3jm_Uhc05iO-CVglOLsH7uuqG_Rv2UrqrMPHnovF1k7rmWN2G97RNma9bFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیر دیگه کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77708" target="_blank">📅 14:26 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bltDss-a8FhccUxsmJPD9OM52gnM3Rv5ldxqEksRonVkOA35-zmw6UQzD1eKxsPb_feOGgTHPWDQBiwW2MmHdsaRRtLTg383AwSYrl6nz5Jzyi-2EKaBUtjEcLkrrvqzU6it216yavpbNwJ5LsczX9wtZTz8mcspHDFJnKhIhIRPdgjxIIWAxFBrgebnKfntXwwxptgP3eH59h19-Lp5negmlKwk40iVB7_zZQPTkL1yPWzliTl0LqirEh5Tzbse-G6myzUpzi7ppezLpo5Bn1Rferusb4fNNZgkgKWp3nybN2qE8p0stOSCSLdytWqx5vPR8Y4yZMCqdCJU8aE20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیسو
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77707" target="_blank">📅 14:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77699">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد: ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی…</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77699" target="_blank">📅 13:17 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسرائیل هیوم تقریبا توافق احتمالی رو کامل تشریح کرد:
ایران اصولاً موافقت کرده است که اورانیوم غنی‌شده بالای ۳.۷۵٪ را منتقل کند، از غنی‌سازی بلندمدت صرف‌نظر کند و از به‌دست آوردن سلاح هسته‌ای، از جمله از طریق خرید، خودداری نماید، به عنوان بخشی از یادداشت تفاهمی که منجر به لغو حملات آمریکا به ایران شد.
تنگه هرمز پس از امضا به طور کامل بدون محدودیت یا عوارض باز خواهد شد.
هر دو طرف متعهد می‌شوند که در این ۶۰ روز علیه یکدیگر یا هر کشور منطقه‌ای دیگر اقدام نظامی نکنند.
این پیشرفت در مذاکرات پس از تمایل آمریکا به آزادسازی ۱۲ تا ۱۵ میلیارد دلار تحت نظارت قطر
برای خرید وسایل بشردوستانه
ناشی شده است.
یک مقام ارشد آمریکایی گفت هدف استراتژیک تغییر رژیم «فعلاً» کنار گذاشته نشده است.
انتظار می‌رود امضا اوایل هفته آینده، احتمالاً در ژنو انجام شود.
بند آتش‌بس لبنان همچنان باز است: آمریکا مایل است به اسرائیل اجازه دهد به تهدیدات نوظهور پاسخ دهد، در حالی که ایران خواستار آتش‌بس کامل است.
مذاکرات آینده ظرف دو هفته (مطالبه آمریکا) یا ۶۰ روز (مطالبه ایران) به محدودیت‌های موشکی، حمایت ایران از نیابتی‌ها، خروج آمریکا از خلیج و تضمین‌های بین‌المللی خواهد پرداخت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/77698" target="_blank">📅 13:11 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری
پیت هگست 44 تا پرس سینه رفت و ویدیو شو منتشر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77697" target="_blank">📅 13:01 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسرائیل بمباران جنوب لبنانو از سر گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77696" target="_blank">📅 12:52 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eIcNxxkKbncieXJQAMbTJB5z1l7N1qJubPYCxMQ-BC9tMnfOTAjH_-7rdeoBXo8nOVAOmcunc9zkeUM178eVNGGgnKN9QymSMUMHRR1IFKsKKUBvhx9yDZ14ZRh6m_Pdg8iVsnfMYsRMNVxFAZRp-U6gUCC4B_QBeurWa3_DHIwKoF-vuJDqUOQtfa08qdlnZZJMHV8Lw7zXL8085qD2kV548_08iL5HUafLWAz3FUSPRW77ITK4xCYv7rTdbP4KxM58pk2ceWLHNthkzz1PR4FyJaqgUyu2OXp7VdlVGnM2zuSPBrAcDTFEpqxAEjhUMRAbkaywUJuNUH956QlM-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوشش اسلامی سال 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/77695" target="_blank">📅 12:19 · 22 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">فقط چرا اون پایین زده ۲۰۲۲  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77694" target="_blank">📅 12:10 · 22 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
