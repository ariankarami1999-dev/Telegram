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
<img src="https://cdn5.telesco.pe/file/llK7IPcic6konEPbVGFxlEjg5XxBRTDtANNjc6nAKnpw1qBD3rJLmwSkSzBL2Fimt7EzXMHkFsnJXfZ1HBDDHHTT_vo6S8de0DXo0RpXETArp5Viz_5_Sbjmn41zy4rUV5-BdG73iXAjDIOI8paJvoEyvbqtGbjNVOZ4KiqKGsz_RGS0XZCuTyjTG-2oyiGkoBtApPEygPkYLwDfEzNhtHDxKbzyktig0B8iE8Xd-JbxkKcscWo4U9Ueua8d0-fZhzW65gIBxZ9vLu7w30nf6YeaWXAuechbYkDyqPwU1Itk-NdvvBLuhBhBsVrwp8QXgzrVbg21dIu4Cw7K0PqPYw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 300K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-19 19:46:14</div>
<hr>

<div class="tg-post" id="msg-91718">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNTy1o1gKSap6KOtIkDkYWpstzSgY_w_bAhZbvJWuyyLceBR3Euv0LgkNf7YXvdJOUkaa2aiwZGRfZsNBgnQNVRPAEdyQbQQ3eCXfQLuxGL35ugTdbxers2hax0IE4Z7C6KVjUYMoPjUiUTFpMhzCJjbXMJSOKNQo2NVE-55zmXjb2MSFGvdFyth2_4DToA-1w5sDko_EO0P9_0jZw-kZ0tJ74DZAu6lniJ4H4ZpVWirJQMcUVMP8APfnATnuaPLIC9VlhJ3dhk9gIzPQjSsEeZuUhvfZbm9KnWa_JNv24B8afyUVYqsouwXhTjYaXFPA6qMBvB6--ZhXtXcSJKngQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اورانیوم غنی شده که تو پات نداری داش دیبروینه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/91718" target="_blank">📅 19:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91717">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🚨
🚨
فوریییی
❤️
🇪🇸
یه خبرنگار نزدیک به اتلتیکو خبر زده آلمانی مدیر ورزشی اتلتیکو به دکو گفته از جذب سیلوا کنار بکشید تا ما آلوارز رو با ۱۲۰ میلیون بهتون بفروشیم!!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/Futball180TV/91717" target="_blank">📅 19:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91715">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PenFtPvUyRB6rlI48eTpIFURySt2LPbsz1eWQPxwBIhchx5K1pU1OclPzOSO7Vkr5_rDdcSuHXsotsD13cD_3suFAU9aPLKapLlYxmuslfhg0LqITBP4PB42E15QGach-cK7OWBsQXVAm2S_pYR-Wq9GOltvqLg_UCs8Kl6qbdPP7PPRL_uu_n-XhZpIypIn13fAyKK7BHWQJu71A4Mz228RJJ3FsKZYDPPC6VHVeKmFItGmq1lJgmikj_UDRY2eaUrQW6rKNks32vzfL-QlwLro4ACxdFKrWcxEEHx1A-D1MySuyHUjVO57UMVjzl_PNM6LJV7AGtMhr7gQiLZ5Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qgUxyv85noRDZEZ1hB0XZp-GB2XL9x-MBUxWu9Mp0B6Fn_-NXaSUST9cWAefj2PYqkgfdFtp-rx7FIdQZQEHgux1lAs_MEEY5PJ1dZLGMMm-Tykb4oqbk19BObbrZA5W8x54EcH16Tc3YA9CNSmiPNJ9H5d0TOVe2VFKpWv2oru5E8rTDbwYVa932WQnmqclZMXAx4-AWwRkbcthGezFiPtPdCo6tr4GpwGCqpl18reD5vf3gZ50l9k4m2jCOQuVl1nGl_SFNLUKx4A75cLKLiGKVywCm0a68O48VuUUcXRob3jgzNlCohN728RajF6SqmL7TkYrt5Fu2U9WcbMcjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😀
🏆
- ورزشگاه مونتری (Monterrey Stadium):
مکان: مونتری، ایالت نوئوو لئون
افتتاح: 2015
ظرفیت: حدود 53.500 هزار نفر
🗣
با منظره کوه‌ها پشت جایگاه‌ها، به‌ویژه کوه Cerro de la Silla، که یکی از برجسته‌ترین طراحی‌های بصری در مسابقات است، شناخته می‌شود.
🗣
استادیومی بسیار مدرن در مقایسه با سایر استادیوم‌های جام جهانی (کمتر از ۱۵ سال پیش ساخته شده).
🔺
چهار بازی در جام جهانی میزبانی خواهد کرد (۳ بازی در مرحله گروهی و یک بازی در مرحله یک شانزدهم‌نهایی).
🔹
مهم‌ترین بازی‌هایی که در این ورزشگاه برگزار خواهد شد:
🇸🇪
سوئد × تونس
🇹🇳
🇹🇳
تونس × ژاپن
🇯🇵
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/Futball180TV/91715" target="_blank">📅 19:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91714">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">حالا فکر کنید روی بازوبند مشکی حاج‌صفی اگه به فرض محال که اجازه بدن، قرار باشه بازوبند رنگین کمونی ببندن. چه شبی بشه اون شب
😂
😴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/Futball180TV/91714" target="_blank">📅 19:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91713">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JQL_BFuiCXPo5sBLbXd5g-xld3stCG9OjnyK0p7fbQsbZkwdETp2zsZTkwPkkpXJLDNuvtApQoFznXK9-ukn_cw485e7HoJVfUquPH2Yab-qBJKMby_bS5sJ0VpjcWkQiTpfq93KohoNFarEpXxJGsf6Smb_5dfVW9yEmaUwxgJfx6vslIoicmQMeYxu2Pvk_hG7IxdkTGkxGz2Nq-G2shcMf3bR4XKkB9yVu7EVZ2smihPI4yjEqPdTat9TxMPEDeRiftWKd7zvnaz7L7C4mBmjRoFZZqm2dPooOAQFbOqGtqQkParE_QJVHDC-HIkPM0hDpZ5U8o53SeY7a2DFIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
مسابقات افتتاحیه جام جهانی:
◉ بزرگترین پیروزی در بازی افتتاحیه:
🇷🇺
روسیه ۵-۰ عربستان
🇸🇦
(۲۰۱۸)
◉ بیشترین گل زده شده در بازی افتتاحیه:
🇩🇪
آلمان ۴-۲ کاستاریکا
🇨🇷
— ۶ گل(۲۰۰۶)
◉ معروف‌ترین شگفتی افتتاحیه:
🇨🇲
کامرون ۱-۰ آرژانتین
🇦🇷
(۱۹۹۰).
◉ از جام جهانی ۲۰۰۶ به بعد، کشور میزبان به طور رسمی بازی افتتاحیه را برگزار می‌کند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/Futball180TV/91713" target="_blank">📅 19:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91712">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcYCMDuMQmimkEUKiNFWHEGzLHYc9Kvo12oKwhWfmtsIfUGFC33a3J93clY57AL2BY2KEkRorPAo9Vn5F3JzE93Rv8eQFH9yxPWEbHxtqBM-aKnKO4cQAedeS7ThqadofAJOfwH7WZxTYAg2PaAD8fJTiDsMV34RX5Ib8OYiLg5RWuYTOXFMWEHXKD8FBcZAzQFE0K3Dl6WVackEBLwyFlJs-vYat_dE2i1yWGN6QE99nH38zj3mWqZBGH0OJP4YZmlaOvK9DClq7YisJC1vzQuXk2Z7DSmzoNwywWbpd-GpVdNn5cdZER6jpk1MC03cap9hnat8U-KqZkJK1KKO5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
| آیا می‌دانید؟
👀
از جام جهانی ۱۹۳۸ تا جام جهانی ۲۰۲۲، تیمی که برزیل را حذف می‌کند، در سه تیم برتر مسابقات قرار می‌گیرد.
🤯
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/Futball180TV/91712" target="_blank">📅 18:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91711">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qYzOPOvYFX1Kx9nwhcTh2l_q2Zd1H4z2LLOYyoGj8alNQeSjukbO0OoVg9UC6NmD3q0MvOvQC4WEJiOlQFTi-x_tzDq5a21mcSm2N0-mSjZ3B0CLdDHfqfZ8nZlpFmO4Ki4PcAd7n5qhyuy-e_2A-yBtGqfAOyaJa1cXXJUrQ4c7JBSJmgQcd3SXRmdncl1l2kktzijeFeD97MIZXRl2oONl-XxWHjFXzhVH3j2kxonwFxvLm4obBSR8kKaILeUpS2RHFFzCzZqfjYFRWiWmkP5ZNdNUSCKGejJMxmIeNNZ_HaibG7OTKjDkqMlZWsiDmxYc_i9yndwDaHF9bOq82w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
رونمایی رسمی فیفا از جایزه بهترین بازیکن زمین جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/Futball180TV/91711" target="_blank">📅 18:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91710">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqcMINlpeOOpkby8v_O9cdCe7qaxTL_oFs4of08ExyQOkBQt2RIR9bMjHtcDd9QWVv5tP5UC24CRPUyjeoLlUOcsQpqC60cVNZXFyfcbK7l48L5c0Vj5vUmAyB-gANt7C9FGKXxkW0wst5FaVsVseTY2M0ALJ5OIhPfBl1buW_m-M6v6KB7UOdy-5Y9XfBsFbaKTE5qRCqR_rupLBp1TrHts0pI0RHUbx9NxkJvy8y3o5U0FPZ1DORKxlfSOXnECBjy6DjnYycGcRyzUSxEs2gHnhhGlJ3h4-9nY98O5zVUhLxmJL5k8CFAZCCGE2piQJQ217phh_RIbKHSA7w82mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو :
🇪🇸
🇮🇹
یوونتوس خواهان جذب براهیم دیازه اما تمرکز بازیکن روی رئال مادرید مگه اینکه نظر باشگاه دربارش عوض بشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91710" target="_blank">📅 18:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91709">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-poll">
<h4>📊 استقلالی های عزیز با توجه به اخبار مربوط به سرمربی آینده استقلال شما به عنوان طرفدار کدام سرمربی رو ترجیح میدید؟</h4>
<ul>
<li>✓ بختیاری زاده</li>
<li>✓ فرهاد مجیدی</li>
<li>✓ نکونام</li>
<li>✓ رحمتی</li>
<li>✓ اسکوچیچ</li>
<li>✓ قلعه نویی</li>
<li>✓ مربی خارجی</li>
<li>✓ سایر مربی های ایرانی</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91709" target="_blank">📅 18:27 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91704">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dJE5UmgIdCbBOXlbaRR0tuP8GCtEH_spAOMRVJavsRYy5jc1p3XMkNDnZrP9ouU-yuXr-1v-dkMNXPYyJKpd-gezQEVd3j-HfFQ6zI5Qt8JNRYiCN9m8JJa0hP-oa2TX3cIdOtftj4YI4AjPAp3PGz_ZdT2k_eIPY-F_jopoxKsRmjVXK2OZRx2fH8LiAE3XJcn4DeCVDp3Z8hPUnK4oipfu2gS-89E42BWFhjdVmTs1wPCb2Y8F-JbubNGGtPg-Fm3yXPo-LIPMTCXPI4BiM-6yC5SMK3Dw6DIWvDh31rXScJPsGw0p6glhTMAK2vAoDnKb_6NUbltwUFG8CGUd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6vuGVqjnt2GrcPyFSpF_1wIXc9ITXC-Z9ArZ8xuU_pzPn3G9rox_iJVAQ3kmqMRF-VmiE8L54BofSc-SlIpFIPeQuIjK3QHAVrBxp44lkN2q5JYFocDMiRsAK1POgDxKFoEgx95HBHPufJ6aasr-p6X-_gucocXEcV3lCMQBf8ca5oqkyyfDubJ3ZTK6GEcTZSBluNKNruPg-epyF8Ul2CvyiMohH3lMqfShdx8FOXfls2hziIhFQ7Kv8oH4_OPa6o-SIj3E7jIhPH2PIr-uYXXba5MkIKu5X0Ikk1uZq9vlm_6U39vfYCq-KK2CZMi2veN8nEZfyZRZGXWWNc4Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/An_2pUkQeRblHAyI5adBc9ABOZEssIbt8pzbU4huOdyz-tYMLLXO2qIXUdan7KfDHdQjCVhoOYg3KoRrKno91zqpN315x0db4H7cr2GGnx97FSofxocFEabdzwIo_6___kPbNXOVeoi-OAswMxPNxaOe6DdQ-DbbLqXw7_s03UgC4MBQxYGVFFSDKplWslpmeKky4pKu8TV1mr0DBg4bSV3oFnw7iwi1QRfIeGQR4Mj3yDWehhmIV3gv5vSJQ7zEZ6tnz4WqAcDTOHAGpZj69hhCllR2nOObRKyc0-ekXqDts0L090UV9CFgq2EIQM2b4J1Tu8LOc4rbxaCRJM814g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این دختره توی اونلی فنز فیلمای لختیشو میذاره بعد یه پسر برای قدردانی و تشکر از اینکه دختره باعث شده خود ارضاییش لذت بخش باشه یه BMW آخرین مدل براش خریده!
🫣
🫣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/91704" target="_blank">📅 18:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91703">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=icKzd1mSdipLtWzrmvGqQ-5c0cjGskuj5qCbdM5wofkDpdo0oaO72vHjHNTOSdZLGok9pHL0Qq_Vgp47pvX0KWDR4F_Pel4nPDqm0y6XzJYnDqevSwanGL9K867P9yOaZUYbaCtpiFo7xmx976Ij-bldCCsI_Vsvyz9YbxwbkF8X4wbYsfxLhgcPobzIyeMqOnI9RhbPPDzEwJpVmiqBnkaZp_sOkB1_6wb_TMjjG4oSRe8rfNlZeBORHCVFvpstYa1VzEnSNEADaMMCLJ3zmaaVuaZ6fJeJXozOwIxOtvyqeOAbrJmNjzv2G0wrFmPQSvXrTbEztFR6LsbDjI1zoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b69522e0ec.mp4?token=icKzd1mSdipLtWzrmvGqQ-5c0cjGskuj5qCbdM5wofkDpdo0oaO72vHjHNTOSdZLGok9pHL0Qq_Vgp47pvX0KWDR4F_Pel4nPDqm0y6XzJYnDqevSwanGL9K867P9yOaZUYbaCtpiFo7xmx976Ij-bldCCsI_Vsvyz9YbxwbkF8X4wbYsfxLhgcPobzIyeMqOnI9RhbPPDzEwJpVmiqBnkaZp_sOkB1_6wb_TMjjG4oSRe8rfNlZeBORHCVFvpstYa1VzEnSNEADaMMCLJ3zmaaVuaZ6fJeJXozOwIxOtvyqeOAbrJmNjzv2G0wrFmPQSvXrTbEztFR6LsbDjI1zoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
۸ سال گذر زمان و تفاوت از زمین‌تا آسمان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/91703" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91702">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWcO_6XhbNfbVokkXUP9dnsXnlMDC4WRP72h7uDJHvpshUsqGkikTHKxbGJe_aOmNWIivg-BBzXsS6kxUYAdwO4wloPFlalghgIkPQt-HbMLcmY8nY4gNkvJqZbapJ4c2qulEd-K-q7zJhrpbmULwyKwAzYU6tHEJ3O4n1rxS_N9U9sxnbzzxJvxtZ5zgUvNTHFm9-qLLloTQOsP0sg1lspxGj9Z0AVY1llmM_kJ8efnP56_bupNaFbtu3TkSNEUJ3QKHb8IHiJzsCSHF4Ih4FBNkFj0PnIxreo6xfOgpBFPC-VPox3DrXf1BxHyyPSn-fhAxY3JwKlWXJCSU8vVzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوریییی
از رومانو:
⚪️
🔵
نیکو پاز ترجیح میده به جای اینکه الان به رئال برگرده یک فصل دیگه هم در کومو بمونه!
تصمیم نهایی با ژوزه مورینیو است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91702" target="_blank">📅 18:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91701">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGhMWR27ExtypUUi_XyIswpDlFHP4hkvKd9biscXAErr6EkqEKgG9ECvsq5G5s5QKDOrcgDxDsDBCsl8J5rocawOadh0KjB6Ew0Sdw7-65VjAPFOTyCqxDXWJGMX2rvbGV96gJBdHCcHri0vM6ulpb7uGJvs88ir4h0SofVTh1XZUwK-jmnHAXysDYHNk0LaPPxDMA9z6zfoNsoztyHVTYZIW4RRVZkGWtsy8Lah3Ezj992i_H5bajzMP1oGbKquvNibcRi6pTGpzbcEGmS3Dp5wxXmCnsoQGlGFwY2cJtcxNFDcPyt1rEuiARK3M_hwvBhgaEB-DyleKaXkTqODcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتواسپورت:
پاریسن ژرمن طی چند روز گذشته افتاده دنبال جذب لامین یامال و میخواد شانس خودش رو برای جذب وینگر بارسا امتحان کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91701" target="_blank">📅 17:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91700">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUhBBKXcXNK-903q1eluScstDSuSaNB9CyQV5jaBjU4oE7z0mo6dS3sqV-nwc46k8BVJb2R_4g5tFo4SzENkNV-rA3GPsUoVrfh6vgBoArmeZiaMsXOqhxwJfhMFQJBpHYApEuxFMWtyErMBrv-cWSxe1i0ejWw6sbXHxA5PhYFTfezb4GJg1ZzgvWuda_ojWeeF3UBToMjshIqMwn-AD7fXPwvU7ssXj91GOBXpF4rfxW9DVfRtpFp2EPdWc9y8Q8wbpfiXYb5mSgtsrJYPrOe1n1DTyMQR_RslDFTtrAhBmohfX8tdn7mK39dbi8MWdwQeSjEd9UbVyD91TEhyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91700" target="_blank">📅 17:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91699">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=gQye3WSxSWCTnzNOU4VTCwh-OZRnw3Box0VsOOcclFPRAo8SpBEYcNQIL9mKMsP3HK5LpEa_KZKuW6fLQ2mgLq-m99anv4MpS902r5QqnqF-ZD98mKLu8MvY0rrcRCsSSyX7wYe-IbAUGU1qlf2YA3AYhQQzVyhuiI6vWpZf7aBx_9zcowAyxiCKbSEAoDGgWegOcHPQNSWbdXQezk3xd8_gmOSX4f-oWfi7WxEob3SeOsNiDWwSq9xw21zAE4WXU4RVeYJGeNk442DhGmst8Tc7JrfGFAj_dn-r6TRMbJeWMGae7_cs5XSVgETBQv7KiaAZFHyO1BNWZBkwf-Hukg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5fba6ae20.mp4?token=gQye3WSxSWCTnzNOU4VTCwh-OZRnw3Box0VsOOcclFPRAo8SpBEYcNQIL9mKMsP3HK5LpEa_KZKuW6fLQ2mgLq-m99anv4MpS902r5QqnqF-ZD98mKLu8MvY0rrcRCsSSyX7wYe-IbAUGU1qlf2YA3AYhQQzVyhuiI6vWpZf7aBx_9zcowAyxiCKbSEAoDGgWegOcHPQNSWbdXQezk3xd8_gmOSX4f-oWfi7WxEob3SeOsNiDWwSq9xw21zAE4WXU4RVeYJGeNk442DhGmst8Tc7JrfGFAj_dn-r6TRMbJeWMGae7_cs5XSVgETBQv7KiaAZFHyO1BNWZBkwf-Hukg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو تیم ملی نروژ برای جام جهانی به سبک وایکینگ‌ها
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/91699" target="_blank">📅 17:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91697">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pvBVH7OgosdUF6QoqRIrrl-D7kAHxn2jd6Cmx8jS0rYtwMa3r8mGj0Y5PwQ5BXNXxXPKFs2MwTtmD0VnK2faDsiR6y5DUfVWO3RDasf2T3AgTD6rGpVv_OHGWZEEdRVIGwrqu5T3cYqeoSgODINj0WQoHgmXL_vFXN34Jn-d4kMlXFX9os2nYJrcyhHlJUgW0TSrIhnwGg1OkhZB--l3Ic6wjrHv3C_JEpxg_VNEJV8BGTJRxao7_JhejBVczhq86iES2IsfkjCfDv0sIQ3T_AfBWNPiZFFWL3s9sbNxLKIbgsvNgBOf9vumQxEpFbU4GpcvKZJgVIa1-5GkJ11l_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AgVFP4fqujq_epa72sWQt0IowgOs_c7uguqdpTsw2o9quAv3RrM-aKdj6dsrPqJfQTG58qPj9eXoHoRY_9s2l2zAq8edo212YKqmIgpdvj3R0ux8TgDtDAhAO_ZVce_OlQ9OukxItaqMR64QNFXcFZA_0wEw6RWhRKUgH2y7JUAAoH1uPWW3PvZWv7nNGWskC0401PAfA-EAtLGTU7W4nU9hxDU_8Zi_9JwvNJSs71XFNTpQNoW2-AQEDUJH_6CdJ_6iOV3QNca3vpC6qI4JZkafNiBfUCZxHAJiqJ6cwVX_KAuI12ByjHhFvRXRJ2lGz2sYfOWU6namJ39dhKoWlw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Newcastle
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91697" target="_blank">📅 17:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91696">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8Vdt3J2M6ATTCGcNDN84iUKqSj6r4VOVO_IO5nf4pa6AOtbZ6WjlanTWEctALrAg_QNbJzNWmuPTftgYeL5igxE3RXJAjJtbfZOtRJea3AOjP9Et22DwCc1b3bx2l-4_gQDcFNBMZZHEzEBZmVnHPiClnzngrl6F1cEGQf9SIgj8ZBNynhL9FVVOXHfDqhPURX-11zltSvxhvZ1tNtRfUv3TMmE0Xgm_F-RlnN_ZpDsZD0RdksrWSEF7FPaJhzmk1-6wOq34B9wW3ICN5BxMb-p42ASJgoMCjeD4gkcCUsTRd65fPKDdRMm-rGeJWqy6vVL1AX_HlrYtD5OH8VJhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
گلوبو: نیمار ممکن است مقابل مراکش به میدان برود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/91696" target="_blank">📅 17:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91695">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IrN-VdvS-XDHGSdFvbp32o4LbgK2n4XwNtZGOgU4nAyR_DhmZAq-IZ-vaYhAy0RrCUVuao9m1UUTfoX2aQhn76aaG7aPd3Fh2ppxUmIbl4S2pghvKZmHFZIUGve69jq7xB6S2thuzr83o75ioE_IFcoVV2xd-1xNf1HG1AJRuMn_Xonuz1nKAqqIvrBCldkuP9wH03X84X_ty7_MLAhVKx-3yGhOdCmrv0xz85C78eYJYMvGqb1-OHDdUzLcovdyWq-81BWaoY-oeu32rsyAScyu_Oqr126_YbZEJQG9VN-Jkx4rtaoh2kJg5qaeDpUfrA23dpjK71jeWn8tzSgxqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
رومانو: منچستریونایتد درحال مذاکره فشرده با وستهام برای جذب متئوس فرناندز هست. رقم درخواست وستهام ۸۵ میلیون یورو هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91695" target="_blank">📅 17:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91694">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/VqM0i662xW1FKRfKGyzOj-E67uKWOZM1H-w81DPQaH64PApf1EngPXpLB3X_mtGklLvycXFwCnbhjje3Ql5JXEVh847TvroS9NxovOCvRdNG9uMavKuQh55YIqVCl1UTJoPXi7HvUF4rbe98_59uU9lYzxkD_1odUJVjQO5sowwAAYb3XiJebpKSu_JFn724Xgbzq37PJnpEjWnA-YkfRAm5Z9LYeYUP1_MPQ0njmAPLovU865Sk1fOjLf_zeX_dMDeofrIDqIWrS5S-hyXF1tEskYvkaQVZhhsIcR251BG8TQtZlBen8a95o3CKIjwQZxv1-TgmKyXGd8_c1EJKEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
رومانو:
براهیم دیاز میخواهد در رئال مادرید بماند و برای جایگاهش سخت بجنگد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/91694" target="_blank">📅 17:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91692">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WTTEpr19roIJngD-vaP7V4m4CWhHvaapMAg7DPKtSzmEDgTpFW8f6mXxFyKzEdFwq3gz5OmPmJkltmBJWAGiRZ_ZcwyC0r7ykGF-DiJvsQmA0nU98hanBhfl4pIAgJhLky9VY8DSxKkQfsTOH6jW0h_2bgOtxYDBmqi5KbJOYcm1rGuI5wfyXftOeSoVjJX0b_wAD0B2r9ghBHpb8QcrpwjNiC0ZwvdtM3LlCxPHP-mGTbxKAZshWcJ4YltKcCO1UaezEYqKMffJMUi1uG_qVFuDUvG8yAV6HILd9Na8S7L9-8MIOnw43sfmby6l6N9piq1AWjWittjfFdQzBupg0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DgV5CQ4dAoilV2W2I-goxi6Kd3Tv16NANO076bZ-iwxztTPyAQz8z8IQmmE6UEUrQaGNJDlwWAQpFM0kMfrirzdmfv1Uxktb7wjkZT5pwGHNDunsXkuz6t07_y3zP1GGxBS5Ls_vChZLeRW1h2oGsQGVrFCqhgfQOyurh0mobbiAvrmbJaIkMisDOTXzGwIWJqKqdBeOrmIleNFhozbVJrd5ux95PiSUsRcr9-hq9L-bssFweZ920j6fb0zyQLauJ66HZ3p4dLo1bJamZv_SLxlcwJWshonLnbSOvcXZ0Qr-9abMB2L9PDl0GozvLpRls_uUIfoI2e7UaT6BKgh2pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">معاینات پزشکی رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/Futball180TV/91692" target="_blank">📅 17:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91691">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
#
فوری
؛ پس از اعتراضات اخیر دانش‌آموزان، تاثیر معدل سال یازدهم در کنکور مثبت شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91691" target="_blank">📅 16:47 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91690">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78f1cc690c.mp4?token=tKPTJHPFfsmtTv2fE2A_NGYGWS-4y1JgotNHwwMsFHlbzEj1wn4mkM2p1YGhstne3fa8D9i0MEnEXQabedBK9ZwLTyqX93rxlLAmVn3EGoxCefTuV-1hQS6VQdyfrX0aLJgwfUvegQLCuD83TuVisNVuSWy8OfIS3fD2oqXukr12aY7MPZ1A6hzGhAUai3cTks4mmBRnPRwABddbA0ZPHd9WcVdrzPKV0sS08PDEbVcCVbwJZ7yOYF64fYi0nTsotfTQtBO5uhHr6rIbWPFzmxczvAZB2uZKowWmpiU77kxwpSrQCAJ808UJ3O7pP1uQ5wsONijOjyTbbLaqK9n1zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دیروز وسط‌تمرین یوگا‌ کف تهرون و صدای پدافند؛ چه ترکیب متناقض و عجیبی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91690" target="_blank">📅 16:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91689">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/871f3caa0a.mp4?token=c0oa4eQDsnmCBiu2qvGwpGwDHBqgD0MjfPzso4fpEXlcFGA9vC-t-zzXySsr81SzEIY5bmPHGYp2jExf8twxi1kh0gYxjnt6bdXW-t5WqLkO9rSBLrBEYMkd7t1epMVgG8US3ozjMBUrnsWKptDoU4SUWjSG6fN1y3orv0OkRtHtV8Amo45uXzVHlITIh7sphZ9_aFs-AntJFthCOtsYnXbaPJta6QoatTCIGMJDdiShKN3GSBmrX6LULQkKhQeaPG3NTzWU0M2WoH-jWUUNBcdp-_KTXqxhBlnrF3EArkpY7WW17miOFLdkwpAeNH8j48YzQvnZxhIyAmT2dbEIOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تو ازبکستان روی سکوهای استادیوم یه‌ پسره اومد اینجوری از زیدش خاستگاری کرد که دختره کاسه کوزشو شکوند و جواب رد داد
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91689" target="_blank">📅 16:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91688">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa9aa48bcb.mp4?token=XOhH28LXskNzg1nnyTUslpV1_Qzgu6l2XSV2n_LPp3nwUPqRunqx3xmmYTQV7FtTmkQ2Jj6xplO04AbiBCM0_Fiq-hk5m1yPKTrXYQcvHVXT7o-TuppNWkXfOVjsrJPmZ9yoefZYzwQMZiaKJC35u3J0rI39fHPamI5R2UA_NOVQtu6dERY5OcHyhe19r_0IdgfKvfQUrU8Z6VIMfgB5EsY7q2q2yA9uRBFNIuO4o0LbH-Ww4BE60k5ryKUKnFlFJCbYODH4BBB0VRB9TOvZyVczLTXvUWnNrKRfsVZevsteKZ1igH7uUxdcpgkc1l3Quvx8S0fRUJG2-qoft6k1dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکم رونالدینیو افسانه ای ببینیم
❤️‍🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91688" target="_blank">📅 16:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91687">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/813a70ddec.mp4?token=LE1rw-0Rz4EdBgPfvi5mjgbKLzePJm1GGDX4Q4E5HffTShEPN22kx5sdzwqOdC2_pFITYmY1T09ziBBA45tgTKVGb9vMcPqPj5Brt1-KBLvsivN68udzVhDLMZw9z_OifL1moa_0QsoqRv-GE4LQfiupVYYFAxjLcX0UY0_bkLBkmYGKSoyTJuFt39WfUNazFcjpufXOoXrgcbH6oyxv7Vj2b8XBXOnjBi7b6166GZhIYshWReBNvw1d_ECoOFXLzmcLlz4J0lQYeWino4tExnZmaczAsoJznPfNBCyMABw39BdXIrcUw3dej-sN_FHXXJaA8LcdJYWxrXitpBjyuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
الهه منصوریان بعد زد و خورد شدید و فدراسیون ووشو: من در برابر بی عدالتی سکوت نخواهم کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91687" target="_blank">📅 16:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91686">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ea15ec78.mp4?token=j7YLHWyzPl0MN45pCmEwOXHa9vBawr5dweme1bfc2VwNbvmV6CgXBwtu1GEJMkOLqxEDkUvjExrNeZDJMRF9EQ48NzTx-wZhA1LatKHhdXzY4EYoKkTQBp2H0IIPltZFY7DTdpT1YI-zmXiu-zfge6CZI6IQ18JdhAlkiqyCYbO9zVziApeax9y9yKxdNA4lFC6jLPOjOI-vkprpf7rBQO5dTTKBSVQpHSAz4xRAxIwdf7VjJ0wXxzYMyy5Heq4uMSPhDLRnXKPpLyvbhWa2gWp-ASqJXSUrijjFADmoo-XBhBdF0k3HNDdhY-FOizIVvXystR1tknoWKS3z3DsODw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی بازیکنای برزیل یه دروازه خالی گل میکنن:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/91686" target="_blank">📅 15:50 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91685">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qfdTEEQ1z0SxFlJZu6_fus4wzp7ikHpvu_QckU4NhECW8djBcxfk-8RoC1no0_M3HEaCxGoJ0Q2Wf8ss-53jXh-jCwMKLdRzcCTtLkkyAWhD7tUsQGnLnMi82iHZd4KbA-_gz9khfw2yOL3i5qb_jj0nfMggl5TGRhSdMNKVMGCHkv1umJNsVhvSsvPvUSkkvqdlPEL8vGAT4oQn7BNQXjlzFOaQicNnRVdMtg55zyWMUG6GpadEd28jsqXv_DVwDryVQSlHVGCtB06MdacjystJVZ8F4i_iLK5gf9zFucOpJxHIAFLQgaaUv2ewVZSMTDr_Ch-UHNhqM22sV4L5KA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مورینیو وارد مادرید شد
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91685" target="_blank">📅 15:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91684">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd169632cc.mp4?token=Z6iVhDlumtaKWb6TiTjs7fgQaeDaNBN3kWvTVxWodlWU3GtxCOzP2Ltg-uUmNxFodcoK5Pmjkv-U7RYW2JVcSvMJa1TylVg_bP8QCf9ViKtdpOBNZdU6OJNUIASMPmjXgA3ESZxClOEZT7fbPLcEx85WEM54XJFl7XDGyhlZxc1AvKXMlVT97VuwyN5SQsWE_2err-WxXzgJPwKD4PhCGK8skqyFeQ4KB15AoJwt03tIPd9tRgkTblfGKLNZ1bIg-4FgDx6UF6wNYOfyFT6RzVvN2HMzj_J_2wdMxgiQXnkUw_JyAhDhxAlNY5WwQs8WaoqDFV6SHxi0kvuvZkhQRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گاوی اینو با این افکت صدا توی تیک تاک آپلود کرده:
صبح بخیر عوضی فوق العاده؛چه حسی داره به عنوان خفن ترین
مادرجنده
دنیا بیدار بشی؟
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91684" target="_blank">📅 15:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91683">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J0ie8OM9GQ23vUsxxU73IqEJyC_vev0c89Bu0KufxutDh8rj4UwRw55Z6A2yxfWnGCN2rV64CEgdP8Aye-TR3hC6T1vbYHYuoJ48HNYd2EXYMJs-5iW3KF6TAiZ1SNXrYl_cEIDW3Zco5x30nJZe-clAnrh5X8PExN7Uikgfq3IUUZ8Trg2oL_BBSI-YGVmmoNxH5npx8bBKCXAfhK_plA6VA8GAxR_IYjLHJQvE6drfkgv4FVEb9HrNS3SVadZCNpt2bbBjSudUkbra_giBVIlyy9a65I4-tqI-uMgcWGFn4ruVUO-_anZ_KtUawGAI58_GnVrmHb9zzshVtIaBXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🔻
خوزه آلوارز خیلی نزدیک به لاپورتا:
🔻
بارسلونا همچنان روند جذب آلوارز رو دنبال‌ می‌کنه. ۱۲۰ میلیون دلار حداکثر پیشنهاد بارسلونا برای آلوارز خواهد بود. مذاکرات در روزهای آینده انجام خواهد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/Futball180TV/91683" target="_blank">📅 15:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91682">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sAyMpZnL_zpYfjlJ6A_7SnSJBLrTOX67u1IuhBwJmHeTo20HIK1qmbQxmZSN5t_bI5Yt3rGDm8loNWwiCSKAognq1hzJqTHjAImrJ2vrO855kXHPG9znCAs-HoVEIULvbqGyC5GlV7L2r_rYxluPpOKMv-Gj11woXvkoOB6bPLWX9fwm4Ipg4iYn6vS6CQbO7lBxgBJUjCMrOWgfqkhStSate1_0Wh4D_NdV01Tzg21ZA_GR8p7YqW6HGr2aQGn92SFlK99GxiCg_orNQA2nLM4VyG4Gg6VHE18yhTerSIOen1UPXbxMHtlG5II62Bw92KcAX9xqLxKQogb6x_CyFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💥
خدای جام جهانی؛ زاگالو با ۴قهرمانی جهان با برزیل
🥇
۱۹۵۸(به عنوان بازیکن قهرمان)
🥇
۱۹۶۲(به عنوان بازیکن قهرمان)
🥇
۱۹۷۰(به عنوان سرمربی قهرمان)
🥇
۱۹۹۴(به عنوان مربی و مدیر فنی قهرمان)
🥈
۱۹۹۸(به عنوان سرمربی نایب قهرمان)
🏆
اوبه عنوان بازیکن، سرمربی،مربی، مدیر فنی قهرمان جام جهانی شده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/Futball180TV/91682" target="_blank">📅 15:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91681">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15a705f7b.mp4?token=QZgxDYbP-ZkipTiOm2rOnoSlFtzoEAkrzPrnjXEA6BjbMqdfUlcDHFALQlK4AjW_VE71xhdKmpZJwVkeGYOnt65WqjeUpEtkhTTmJzUiypxxxS_riuAWAsrjX6r4l3LFCUINbBGKyDaFRXZqjhxLFkFoFhzJVDEGQcic2jI1tLAvI8PUfC_FIPm7rYT6OUZ6AZ6_iFbAT6G3RdpCqZj7g4IFJLON1HmXwg1p4_0S2EaovyyUDjLhhP-5WuU9xkOXL0X0Ebvu4zo8rX8I2kz_olkV4LwSKTPu8Ewyh4l2fjKSYLi6PK-ZRstHjMXIOlraCafuIHFmSYCKfP3QjMVYRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مکزیکی‌ها این ویدیو رو‌ از اعضای تیم قلعه‌نویی منتشر کردن و‌ نوشتن که تمرینات فوق پیشرفته ایران در اطراف استخر برگزار میشه و اینقدر امکانات اونجا درخشانه که رو دست نداره
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91681" target="_blank">📅 15:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91680">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=OJPqIFn8GxDVrCn4jcTqYxpTPNNt-yF2YaiJZE1Thd8F4JghBp113I6wzIVxA3k-1NdB_f1BX6WGr4kEwhvyUBpMI-qB-n9tsI5zFzoyIljT7hMoYB21IjwhhFWw8gOn-2rRrDYT0j59S4wiTafaj_hsGL5Cd3hwo46_Tk8ZWDMDQ2BaGfngfhEs_9vp3D1pwx2r54rTSseygeyc6HZffLpMO006r1FCi79LGnurt5hKTbT_bXkOrMU0ZN-nM115McZSzo2kZpQ7VVs1sKsXXkRCJZYMNgbtGL3LROjexRKfTj_g1H9iI0aLyQDwUi0-jyda0TEm9ONXhhLbduoz-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a39f457cd6.mp4?token=OJPqIFn8GxDVrCn4jcTqYxpTPNNt-yF2YaiJZE1Thd8F4JghBp113I6wzIVxA3k-1NdB_f1BX6WGr4kEwhvyUBpMI-qB-n9tsI5zFzoyIljT7hMoYB21IjwhhFWw8gOn-2rRrDYT0j59S4wiTafaj_hsGL5Cd3hwo46_Tk8ZWDMDQ2BaGfngfhEs_9vp3D1pwx2r54rTSseygeyc6HZffLpMO006r1FCi79LGnurt5hKTbT_bXkOrMU0ZN-nM115McZSzo2kZpQ7VVs1sKsXXkRCJZYMNgbtGL3LROjexRKfTj_g1H9iI0aLyQDwUi0-jyda0TEm9ONXhhLbduoz-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ دیشب رفته بوده فینال NBA ببینه که باز انگار تو حالت چرت زدن سوژه شده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91680" target="_blank">📅 15:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91679">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YrJ9Eqjvf19C8yxXxnGtU79gWUkA1U3q_nzEvtKkfnLbEofavlHB9F5soT8zTgFcaQsxS-LFEFcDGtErTeYQFP3wNEk-mGT6e2AnkRUrNiOS7JC81BtT_JYdcOGNlQWI6EDBMjPQ-QkyLuBAXxb5UjRwrxPNKxpyQyjCkw1pnN_vwWCgJpolRQT9nO9BjrdSuJij4NUKQ7UlnYlLSi4qVnbuJ2lUguwL6M4rHVUmLHeysmywOOQwALBgfnCCJKwUICa-GuarGs8-nM6aXXiRNCOQrQyOYmJ8SVCAli8LOHud2WdrfAP7z3smVIgpoIaKU2TkKyKvH9px71k7XNqwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
دوست دختر رودریگو دی‌پائول:
«بعد از جشن قهرمانی آرژانتین در جام جهانی، رودریگو مست به خانه آمد. من مجبور شدم مثل یک بچه از او مراقبت کنم چون نمی‌توانست جشن گرفتن را متوقف کند. به او گفتم که دوستش دارم تا آرام شود. سپس او پاسخ داد: «من هم تو را دوست دارم مسی.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91679" target="_blank">📅 14:45 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91678">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🏆
اینفانتینو رئیس فیفا درحال خط‌کشی استادیوم نیوجرسی آمریکا در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/Futball180TV/91678" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91677">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rbf-g6wucchLW3Y89XDYZEkr00CG3Cuie2Tn9jFsb1QOqB0UXT6b1Si1CJpbsUgfbds6prJ810eW-H2bui6_M5T-MamiEjkGjfcggNUMzitK6WhMlPXoXqw_9s6HCR84whmD4ggzVFChwxyZiHB5_jOFgWErdurNGTUTTLD9c-I_LGA__xj3xYs28vAnWHyNzXjgVwxpH7mI1fUxgDrHTfgpvASXHX7son_Xji04lF9sxgy7KBqsTASAuggwllsjrnAQ4HkF9apb_B2fqq41E7zXDogHcDs18V-vPnQolagDivgqWLL93ti_jA_5utZKmbq6c-y6dpgJt5n-Z0-xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همسر نیمار به همراه بچه‌هاش یه ویلای خیلی لوکس و خفن تو آمریکا اجاره کردن که تو این یه ماه کنار نیمار باشن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/91677" target="_blank">📅 14:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91676">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">📰
⚪️
اسکای اسپورت: هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/91676" target="_blank">📅 14:39 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91675">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJJkSn36yijw7Yg9TBTWATdWGSxh7GI90jdVmgU7l-KdskFZ5GB40iqUMQTOU3JokGPPUDWRabXqmgs2a6m_-TpbIUL1Ix9tN5Gzs8pzzGDew5mqM7VgZ9Wf_9werJXFC_17bYavOFdehQMttVB1KQd4YZk95MgKAFpek1dbOZnjT_KHzxc0pDqpWSjN4ozi3-lFBQ--GBac7Xv414f_SRBOILVbHrjK9gXiUJulEOQD8sbPyfGZor1ep9eT7YVb3NOB-lnjFheJKU4J1UUSHByEQ2GQr_naGTrNkDWygnybL9izvISW86BRMwT-w-R_ng-Nw05yWqKpmHq7ENhPow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
⚪️
اسکای اسپورت:
هدف رئال مادرید اکنون قرارداد با ریکاردو کالافیوری است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91675" target="_blank">📅 14:32 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91671">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qx-ZOtRTbUydYNYIJjPvJpJjI4DNWkZ7jpACOy7Ncz1fwrGnHmZ1X78l2uiBO6hHi1fWd5zeR-RoC7I62dxbUXmMkuUBFj-Ydc0qTwXCwL9znp5WBy9boPRuzvmDFxwzMQtOtHdsgTYMwlNDkx0k6gS6zVf3HExIyzdBpFf3Ji064ES2C7z2ZO-G_BS-6MyNnUxegXVWqV8tMXfEA3qv7y5VWqFHuzMtXrBXcQqHh05MJjikzBrXra_NUMft46wTvsTk8F5T4DEql2yuHMXOB1rJHIMsxLazUs7-TWkhBED4uK6cA-YqoHJpV34t96M8gb27giGExr2-B3-QFqAfPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJQXFpHX2fkmhp9XMGhLPvBF2SjJI9YdLv--z5MBXdTSiZ6V8IFKr_iVPMLRDbaW5FblVbi5TOtyK7XaCE5bQ3of1MJ6ofPID56_-ZuW2H2QxtIpvnXqE7S6ybtnZWs_0Ct8JRj9vMMILY8FXtZhWeb_b0y_v4cJu10BjHkya8KGiE_zCTrA-024n0gHSUqTQmOKMM7TQhn5e7-5aiasQzKWr7HneElkCkHzDAoXctaHPJHOMsyi7BqOooxnf3JJmhAHVBYOMptT4kUnDeKpwmrYksOc-7Z6yYh2vx9Y9fAcYotOCGyoM6iCV8Xaauuv00iWqHnI__ZkHrCljpSS7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u5mzdCf1ZSF3kW5Ykovu_qiiGDpvvhlYX-M7AsYUmxoibdiYlHPguCgdz7fbgwMQqhMSjPuFdVRJ8L1gM5Hx-UrnIlUFxFwUhlahMgaR0IiYjZEP1jpQYwkLlXxpODIEtA3ioj-BFIuiScxSt9cAsEvKrLxbyKn2JoR9Xj0_xefUWEDHOMV8ty_aa-POYXb594om4T3rUIhaYbqj_lqs0E5GUh1JOvH3D8sUDpIyITYupuhHze-xgGdqPfx1WUUOcLGQ4uodOBqp42H3bAdcQMqa2YuIibCksQLPzo7MQeOlrkoYeHbePdjl9VCC6aG4ZefqdX7FgxnBg2-18mVU_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h5xj9y41_EjbbdpStZIv2sSnz-pVzui-lpWuY-apbIgs8ahyvnxS-OoMNQj6eAkKKb3eHyqhyb_LxAVSSw8F6P0bUPvti2KK-CYP6NND6NR3KUTPdFNhjgvJnyMVAgQ-sntoAzEd5KWhR0HUoNvnH729Q2AJyeXGTZrqys8nVPa_qIG_uOdDTmf870VsZEkXYFRyW7L3achE6qVuStgvG2cpCfSuNZuwzMvFJY7F9ri9N6-nPRfgXHRQHtClYB3EoSdBT9ZnwW10Z6FS-Bf0cRjLCGTiDS2n6kB1Li_UG_TqtTsjuVxZ4TtaP6XIacTepz05F5qx3o4hf_VEXQWe1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مجری داف و جذاب شاختار هستن.
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/91671" target="_blank">📅 14:30 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91670">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f43f043a30.mp4?token=XViQWDVAwDbK-J8sBXu3fJav4MXCoU_bSoWwOAmUpMmvNsWnshBNSYez0weKTG9441e0ACl0D2F7zfB9BInQO37d7j_-0SGA5W0xA21zbQ7ps0IOCUJOI_u47nrbd2dTLVq5PO8_qh1s3xpSKVPHCEklQbLnS60S9VrHHBiQsAa_AAZhxdyzl6Wy9BlSCUBCNKe7asGpnfNsZ01bL7-CUDMDyOxM_QujbCtwJWokzp57-SgaPtrTjkRJ63JjzTdfdSRBT1EJkwc9b2mYfqulyrbke8AaPcNx-_HZbyQOzO9_rSAlWr3-bBqdz1legkVyDpRVnX_lLhX2zLrgY7qUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
صحبت‌های عجیب و کنایه آمیز شهربانو منصوریان: من راه میرم روزی ۵۰ میـ‌لیون درمیارم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91670" target="_blank">📅 14:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91669">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🚨
🇯🇵
تیم‌ملی ژاپن کمپ تمرینی خودشو که داخل مکزیک بود بخاطر شرایط بد و‌ امکانات ضعیف به آمریکا تغییر داد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/91669" target="_blank">📅 14:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91667">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bhWwJCqpsK0zG0fEINWB0ofNSpEKjQgO_-OPEcErjTWocYiz5LgLlk9jPAWrIhlON9GOmL_gj4PEEn4gOjphJgzKxOD00lmgBKxp4fiywNo3nXE_e2jh2Ko0TLvWlqgsRoRF9rvP0JGLKMu5RG8NTLZBOzIfZUa2uSHsKU4vNh0yvvWrF6a3Z5KnNgrc3FKwoK5CvNMMYsZoU_qz0RDbzJxIlyEGIBpyrW8QHR85_paEgQ_qRLzHMRIOyfjTw0Kgi7mISQ78wjZQEGZKmtQvSLYvPyC8M0ifHzr0NsWJ_ln-ygxPxKVtKxrFmkJcM8IpPyxS-KQnyiCthkI4Dt-qgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t6B2HXFADRVingecOvX7i6NefGwFFAjCjLeiUsh-FA49eBk9YjPBMSg9gyWlCFawsSK1UiY0HYPQE3PukUeGyNvLCuZ0vocgx6AEvAp1mVhFzvRZHqSyg0BRTOKS3cvD99wo9h7MMzdUjDGGfC6nbLxtZatTgIJePHH5pOFLSnvxDRqOHM55qxKcN4pMFGl0OK5k7BC6wc1YMkSrLaukx1OV4u-lCIVBQ1FCQNEX8h2PpO4IGFAJAUkq3pGh93-WBNgCHPvIt7quWx-ZSwip2J1rvPjIjS_6I2RPv_Yf4Vcm5tXf2hQJqSc1tpmK8gkrEuBTx8pPtMlPrlMBYZcAjw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇦🇷
مسی قلب‌ها تو تمرینات آرژانتین.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91667" target="_blank">📅 14:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91666">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7LrFZux3HAFkw6VAZk-6mgnygmgkyz9QzmKiQKdn_gMMrGERPmB0P6nT00p6S6IzxsPCbu_sbRtTOjtCp1Uv52Izc00UbcQ5EnoupU6S1Ib4ifNtQC6PSoEWP6zLp7AnUM7Ul13u4hqWJFJbEC-LzH1QmirN-gKMPccqet0XThkPJSoZ_8QVLSCFNG1n5i5keicVPF2WLqonYtqCW-7lijBDLM6G9GlhqYdPTmwxHcNB310JMmtHuNcwsZfhnDkXUYMliWEE1xnc45tnxWWuh1CebuzYtCYhp9TlqkjCzvJteZCv4G5DE4OOBSnkgWR5NQuxzmFRLl5utMF9WHH8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین بازیکنان تاریخ جام جهانی از نظر امباپه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91666" target="_blank">📅 13:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91665">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=JfWBwnBiRvYX1QkHb54T01_KykWBqEijK7YKflY2OwKG1Ao-hKWAGpQi3iWlbDhaPkULufe1J6NzZg7-LaVMDVzjC4pHsCS-UFS_fnZXwaICb5bAgN9gtQQz3wpcGEz1EY6nnhDaIdQlWoRjQLUT76JSXOI0F35O02gNaFX-BnzBw3VSwbqFsoxpncgEaqSUIwxi6_TkpMkJH4yHZZMlRjWFfDwTJdqbT5pJUoQu5E6sL7m1gBC_izv6Ohy10ZQnx7oLkM1txstphOjAoKmDg7Z-k2A5kRyg_mTnTWkv1mSnuSWPCRDRw9IrwUFMhHQ9fKRM_oRquBVCxDnHR-Tjlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57c3ac63bd.mp4?token=JfWBwnBiRvYX1QkHb54T01_KykWBqEijK7YKflY2OwKG1Ao-hKWAGpQi3iWlbDhaPkULufe1J6NzZg7-LaVMDVzjC4pHsCS-UFS_fnZXwaICb5bAgN9gtQQz3wpcGEz1EY6nnhDaIdQlWoRjQLUT76JSXOI0F35O02gNaFX-BnzBw3VSwbqFsoxpncgEaqSUIwxi6_TkpMkJH4yHZZMlRjWFfDwTJdqbT5pJUoQu5E6sL7m1gBC_izv6Ohy10ZQnx7oLkM1txstphOjAoKmDg7Z-k2A5kRyg_mTnTWkv1mSnuSWPCRDRw9IrwUFMhHQ9fKRM_oRquBVCxDnHR-Tjlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
💥
بعد شکیرا، اسپید و شیدا مقصودلو، حالا نورا فتحی هم موزیک‌ویدیو جام‌جهانی منتشر کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/91665" target="_blank">📅 13:53 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91664">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520253fcb9.mp4?token=O4TCLBgNrmDreT2Tf-4NhFNUSIplOv8GIFwJKyXAvKayYGr-ReyvzkXT1t3NtiRoAjZqS-zM-2_aNUlY7a_pDWmA61Sj7InG6e9JFJ1trzBT8zvEWYd6r3ASvEyvKZi7efiDjaHpSZEJcFVcSQEuaszooxJXLCoX67Xvm5ihjKjLDvCPY8BEBCP9yi9QKjWsI3ljvK7mFKnxqfJ-5xmrsEEMjmCzWgfD6siTDCjMbPXFL_ITObBvTG2kobkFHiZ5XZ1oM3SqAIww-lCHWa04dURpv8qqIWCWB-5DLkAOqdd-VJeuSDN2FO-tJUI0oVMYX66aWBBN46Cg3yVTfO26cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
آموزش رقص در ایران با موزیک دای‌دای شکیرا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/91664" target="_blank">📅 13:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91663">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIikM8wV3crsQJQQg_H3p0ycIkBdSqPKehnx_TVsLquPFbPxZG-5KUy1o286w4JhFBryixPg3sEyV0ERQM_Ta_EPZsMux0MwSdBXi4ppBSeswy4EfZGz9JetZOxlauyi2Rs-AmwE0pydMf3WBhtfvZTP4lrpSTf2NFqKxhUlBrBxw9nV5d05iosuyghPT5F_SONrWbIbI4ykQWvk1IlIUYakDE2E1-nrBDMEB2B4VMSu2cCunaNe6Mx_hOuolRSmrBPHF3P7k-LWbz94A8STaH7ZsrvaKAifSod8DfOOUbCymhfPde1drAwb-3YMWft_wyMl7KfrSX9YLaIh3lD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
✔️
پسران رگنار و عکس رسمی برای جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/91663" target="_blank">📅 13:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91661">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d43531369.mp4?token=Q8K2RSoWOOClZsxrOWcRvUjNazzrmNq-KDPQC1sGn4PlFmbSF53MWO2N8BlQ13LVg1Xdy6ysThiDE7B-9v1RBVGEFIGVRlCtcxLKaGExHoLt9BE0OLdGZjkZAJKRE2iUrSTra3q1upmsZuODAp4CPNLUZtt6W7Sd98xv0FcHa7t4jaSbOzSbDGayKRkODs43qOBdm9ggBoxrXkWbmzqS4IyS7vGLmCO8EX7bHtgpDtW-23dQk7OcxT5mh25GVPdfUTZKH9cYvQ9ujGlLPpgeTustZwVGQkzIouVlQSYgGtpKaRUwCp_hc3KIXPukU2T2NVK5P0JMkvqqE6xV2ahrSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d43531369.mp4?token=Q8K2RSoWOOClZsxrOWcRvUjNazzrmNq-KDPQC1sGn4PlFmbSF53MWO2N8BlQ13LVg1Xdy6ysThiDE7B-9v1RBVGEFIGVRlCtcxLKaGExHoLt9BE0OLdGZjkZAJKRE2iUrSTra3q1upmsZuODAp4CPNLUZtt6W7Sd98xv0FcHa7t4jaSbOzSbDGayKRkODs43qOBdm9ggBoxrXkWbmzqS4IyS7vGLmCO8EX7bHtgpDtW-23dQk7OcxT5mh25GVPdfUTZKH9cYvQ9ujGlLPpgeTustZwVGQkzIouVlQSYgGtpKaRUwCp_hc3KIXPukU2T2NVK5P0JMkvqqE6xV2ahrSzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
صحبت‌های یه خانوم دهه شصتی که ده تا شکم زاییده و میگه هنوز این تعداد بچه کمه
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91661" target="_blank">📅 13:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91657">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/puL_7Mxpqz2gwYhqylysx6vxOEsDOB4BUx1nXYnuqgC3C1pwVCXKfuq_B7h2JyoFd_f4f_zV3Ta1GGXxfqwM9gI0qorgKXLIdxdM57k-PcMBd0wJeiEPiTg0PuHStd9vkZN5aKej-rt1AeFoctwdZ5njFxIIUh4dHMawVmpTjrOQkz-laJx7DQul-Zpm1FkZYzb49Zsy0OU70aRCfbahSqMoQg4aq44LMh1fFSWsB75hfPTyBBePB9uQzoyUhLym3YMCTAtxMzUDdu-Rvfk2ZNwtDcGHREGuzqybu_lawWvIoBfEBKkSc80yMqRqbwTVbIkn2kTgVV0UqMctudnGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TYcgObDMwFcEgRP3vVjoW4yDt3ABHLKxInzrSlwjXGsghPP6JvaN8NzOGJgbn68h-3qb1ixfYT1EJfgERADPu36UdtSKnDzqRRkxXfV9PXFUSMuh3nf8T4sRTZTID3-A5V6z6LAQTJYRR_-F3Ulh2jaLBYfSvITzJvvndj2jM_vxYVOWgzB-44oO7rxCiVUwKF3OS5swp9fhm_27D9os4dHfwYzH3R_T1wJv2jm9eh9P6EL_wYMABwrfKIPJvSogelFdDjNFTNmF9wNScCuoUdskwRGZo9IjNjzZ7b43f23zJb-Aglu63-O-b8fQSwdfK8scHgeKMxKtKvisSxoOiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dxZnRcGNTVtPeH5f2R8dt1HOjNl0hqtEXdX6hfOp6k0kfuqnJqHaehdhFHvthhVa48XsxrNsisiGJJfPAPYs5D0Y5NipBmI_siwXgtkgDtlTPtOMuwgdQVLboqASGCeuOpk-ey2TIt2TgXSTe-XWcM4mAaJf_zr8mggJBz9D5zuGjO0IPy9LX0Se4tuBM-bf30RqJ4AMYy_PPHBH-A-FSpRZNUOqLzSwfAtaTQ-_RCpE8EeprKyUrwdTXHWGLFOQ5uXcJ-Z9ubi_5eqtkEdO-aAFvlWiOdvs9Zta4ul7NvhjB4yu8hDeklbtuqg7A7NoK2ekMOAvFSDbqFItwWbV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oEq1ImJjp73g5-qaHcbfsbR-Ox_x6e66pAI1jNjETDvwQDF1PprZmFt3ENNz-Ep2BOYM2ZvKjbi137_Dt02TWeNkVqeGfA8bIR6phqBs5VT1tapHOpRhQ-8hnvrKTeZCYQ7syDDAvSLaIsTX52kD51_t_X7pWwm34hKkLQgRcdPjg6QdkLPb56_TDaCj-QeAzrZzxsC3VBA2NDfEPzXaIesPAy_IQP4kE56EUaXqVaFQ9vELa3sjkLkicD7gGeQa-r1N1TnpngdnHwsAysbbwuJvgwqwVhLdjmpNnoQe6ODRyTL-J2zkVvnUcAJS9C191M6eS42Sfc1bKf4gQ1QY5w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
داوران چهار بازی اول جام جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/91657" target="_blank">📅 13:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91656">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=VUX_D6fUmnAVDJDmh_NwVr1ZM2ZkqztD9HH3y-LxkmuZLsnTmg4ggWV0Dn4JVa3uYPb2L-7RDLIhjuwZ9ycMP8PTnyULvw9cdP4AVBM0ryXiCeSxpgIj2S16JEgR3a7GRQupsAb1tnridoeItoGdhYQthbpTNNfs3-9qln5dcX5YhVWNXO9fWlKpwL6X3khB7wVEcToU86NN8Er-SM2OzIfrArd96UvO8dBaSfYMF0maB6iYhnYSIuPPZuJARkaA0rOBBlMpJ-nxHeHDAIwTXs4j8zJPvYd-6Qj_d-q7wWJVgM1jQRatH5h82X_DHlGonOmS3zYqry7FuK4tMNkbxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3909e54d84.mp4?token=VUX_D6fUmnAVDJDmh_NwVr1ZM2ZkqztD9HH3y-LxkmuZLsnTmg4ggWV0Dn4JVa3uYPb2L-7RDLIhjuwZ9ycMP8PTnyULvw9cdP4AVBM0ryXiCeSxpgIj2S16JEgR3a7GRQupsAb1tnridoeItoGdhYQthbpTNNfs3-9qln5dcX5YhVWNXO9fWlKpwL6X3khB7wVEcToU86NN8Er-SM2OzIfrArd96UvO8dBaSfYMF0maB6iYhnYSIuPPZuJARkaA0rOBBlMpJ-nxHeHDAIwTXs4j8zJPvYd-6Qj_d-q7wWJVgM1jQRatH5h82X_DHlGonOmS3zYqry7FuK4tMNkbxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار حمید سحری راجب وضعیت اولیسه و ری‌اکشن پرز
❤️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/Futball180TV/91656" target="_blank">📅 13:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91655">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🚨
ادعای
مصطفی پوردهقان، نماینده مجلس: رفع فیلتر واتساپ و یوتیوب در دستور کار قرار گرفته و بزودی این دو اپ بدون فیلتر در دسترس مردم قرار میگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/91655" target="_blank">📅 12:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91654">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e68f156545.mp4?token=P0m2489kkdRzanggozQc6KIZVClC8FcVbpreqRWcedS5ZivvQ1jRSoHhVXwT3-Wz5NfIsCyf7dmNDHuo0jag6MjeVThwvi_nm7Xdl5yHG7v7HLJ6OSjwgUekyzxUuj7YrbvoIwRZPk1knCCtU-H2T_6rvxivUpjzu5_Mmve9SLL-SrIkc2QrYbIpM_R_OPOl2qdKtACQmp9R2KdmHW-Mbg6GFkrPMGV4yXYEunC-Oo5LfhKedv4XNg32sF2v_RFmk4VilwFM_ghzE7ohsM4AJyMbYdOL-iqoar2scEfsnL5iR7gDqyclmg_g_118sP3kyVf6KcHbQKGVBB57YRMWaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e68f156545.mp4?token=P0m2489kkdRzanggozQc6KIZVClC8FcVbpreqRWcedS5ZivvQ1jRSoHhVXwT3-Wz5NfIsCyf7dmNDHuo0jag6MjeVThwvi_nm7Xdl5yHG7v7HLJ6OSjwgUekyzxUuj7YrbvoIwRZPk1knCCtU-H2T_6rvxivUpjzu5_Mmve9SLL-SrIkc2QrYbIpM_R_OPOl2qdKtACQmp9R2KdmHW-Mbg6GFkrPMGV4yXYEunC-Oo5LfhKedv4XNg32sF2v_RFmk4VilwFM_ghzE7ohsM4AJyMbYdOL-iqoar2scEfsnL5iR7gDqyclmg_g_118sP3kyVf6KcHbQKGVBB57YRMWaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
لیونل مسی: «از نظر اهمیت، بهترین گل دوران حرفه‌ای من در وقت اضافه فینال جام جهانی مقابل فرانسه بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/Futball180TV/91654" target="_blank">📅 12:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91652">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L4bB0kIcJrxYcnwQ4ZOrdSfoe58o7-9IBnQ_JdMmOg-fSa342MftQXgpQGx-9XkypvBYScSOPSDt41qF9Q4HqEO_Npo-PLT6Yxfm83MxQ_qBqMWYuw1k7UABrFsVlFooFaboKNlLqvNAHZOQjvkn2EwRiQMhizPDpSvACZGL3CxoPjYQ6nI59oaSMq78PtIyqzSWWFPGoAVDgiMuC2o1FLz9I-DecoPE4wlDv4aIHLwh37_9Mzycm0Q1GWQyy408z0AHlHtyjNX0GmduCbE4OYLtd3VpCzWG_bOLxHeragONMIt4jfvqKK8pcSBQ5fimmVcw607fTEbrZKpmJj-jCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔙
هواداری که به خاطر نوشیدن ۳۲ بطری آبجو از کشورهای حاضر در جام جهانی مشهور شد، دوباره برگشته است…
🔺
این بار او ۴۸ بطری از هر کشور حاضر در جام جهانی ۲۰۲۶ دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/91652" target="_blank">📅 12:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91651">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d6zxFPCvq8M3gXfmQmsajs6ddK4e2ufDDdLkCqTa3r4Zo0Ba1y5nxehY1P2i-a7eebdpt1UXXUqgjGbAl49oIaKRbWbMyJ7WhNNn4ckBIoNpgBv0WhD3Nzv8Ga4prLlS5avdFKfomkSI3HMIAXq2NKy7_1wkx1uXAgJ-dU0mncSd2A7i3sxkMWBbqiWQM34elW8hOs75XokfS2QgC947QnqPI5IlWbgr6ZaCgt-3qCaP1IzgwWXE6CGTGfMcotGZ9vWjbMCo1FHM8tTiGajDfdq0vRJ05-T0fSQ9-P_xBJ6HlR6VcxA5q7loIXN-wBsg7L4ci2OR_SrawRfGpgvwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ژوزه‌مورینیو دقایقی‌پیش وارد مادرید شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/91651" target="_blank">📅 12:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91650">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U4RSri3jAxED26WfO2VUPaGG8eNurHqMlInimvi4jVKrYEBWKmYLitbz8-KmlDu8iwk7suCyNa-Vrz_nDK1uWhoPHs7fG7KckZc-7w-pjd_1UYr-7YE1VJwN1HNUmnqZvwno8kY3M8UIUK3YsxVgLif7kf5_XJ_WWXEqwHtjlagfhaHPC9Ayi8amLBHvQw8Nhb5o53op2Ma5qFR_cHrT-Cplhd_PQOhy7S9gekFyeph0gQ9-t2XtK24C3shXbHk8TkSVamXATT6VEL0jCYHG0SOi6IOxP5BnJkLX1RxYb_Hk8L2-ZU3qk_NMkje36YsYwme6v1xmLSR--O49s7ywMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی فرانسه در گذر زمان..
انگار دو تا کشور جدان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/91650" target="_blank">📅 12:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91649">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fSVSEexb03bgUXWpLmpKhqBgcIgpHL1lSr2BJRBF3kC7r-yJqk2nJbsavgPbeshzqdoquKlCtT9WvW2VAfF8Ub56lVbWswlMlA2juRN1oM2AyxKZGp0gzWrrzyaIWiUq_UsDstIn4TjoKRP4FSIW-U4ZyJppLB4n66NrD-GS8SwuwhJGNPBX5QS5BXHZ2nZVwjLbx48AMqPuN09Pq_8_ujQjFPboo1wLeY9kwMFfuBM-1KEKOoaE2-nbmcG4zqYlqQe3XfV3k4C1zphfvm9kOSzNDiQALlXbmiWZYoz4tvk2-IU6FE9iNqNHeC9jMn__cVgLhux1hJ4VFKUzzrPiGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
🇺🇸
ترامپ دیشب سر زده بلند شده رفته فینال NBA رو ببینه که باعث شوکه شدن افراد حاضر در سالن شده و از نکات جالب اینکه تمام ستاره‌های دو تیم فینالیست توسط ماموران مخفی آمریکا بازرسی و تفتیش بدنی شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91649" target="_blank">📅 12:06 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91648">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=GisWupMCIiulyjas1zLZNZbAs6IuuJdFTVN45jo2iVkQTaUWTJzneeOo80axUi8uDbRQZw4oJMHCWLG-gO2V7p7Um3f4r7YtATTxia06FqGtk_6hm9vGboyS8ALt3-U_PZGEBes6_PRqEp7ZRN539cbo957O3Dd-SAt_2g6Rv8xZ9M3QHPnq-WuiWhJI5RuafJvNIYJhshx3IDI_uAtuMCNPjtHTQXXcpI2eQyit-_nX9pByQ1z5acu_4MTH9P2w7gwI0O6Nx6wCkogC031Nr89XK_ZXRgB5_Le5oz3icCqJQRfbG5L5hMjOBZDj9vn21Xto3qS2gxrzfubn1p6sjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b81ccf3378.mp4?token=GisWupMCIiulyjas1zLZNZbAs6IuuJdFTVN45jo2iVkQTaUWTJzneeOo80axUi8uDbRQZw4oJMHCWLG-gO2V7p7Um3f4r7YtATTxia06FqGtk_6hm9vGboyS8ALt3-U_PZGEBes6_PRqEp7ZRN539cbo957O3Dd-SAt_2g6Rv8xZ9M3QHPnq-WuiWhJI5RuafJvNIYJhshx3IDI_uAtuMCNPjtHTQXXcpI2eQyit-_nX9pByQ1z5acu_4MTH9P2w7gwI0O6Nx6wCkogC031Nr89XK_ZXRgB5_Le5oz3icCqJQRfbG5L5hMjOBZDj9vn21Xto3qS2gxrzfubn1p6sjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
حمایت و تشویق کیم‌کارداشیان برای لوئیز همیلتون دوس‌پسرش بعد نایب‌قهرمان در رالی موناکو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91648" target="_blank">📅 11:54 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91647">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔥
🏆
برخی از درخشان‌ترین سیوهای تاریخ جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/91647" target="_blank">📅 11:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91646">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/91646" target="_blank">📅 11:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91644">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cIFOnNFqNkCIedtFtlEF3WuXbGtgtrmeM7VTy7ygP4m-Fap_F5ZuBu9F80aYFZoMUoJ8WxMGbHcwyGaXxEH5Q1xVFbGBQw5YRyQeyVen0ybMBmWNtnvDLO4TX_v7YtjbRCzd-gGW27VRBqrT6HWura91ricv6BfV8jtmRa-Gh4xWlryULNuiaYrBsoBPzkOFCm9iIUmi6xb75XRT_icpTW42DJ8z4RATv8jIKZu5N9MhuqsZLWeaQZykHrWFafbB-posR6fdycEQF_scASrn0ZdaaFFuFsh_dKqazBAAvRju_cLHJkmzmXeaQAXGzVWlyR70iHLcPh7NQZXWhDzmaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇩🇪
فوری از اتلتیک؛
بایرن مونیخ هم به جمع مشتریان یوشکو گواردیول مدافع کروات منچسترسیتی پیوسته و قصد داره برای جذبش تلاش کنه!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91644" target="_blank">📅 11:24 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91643">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SDXFKyNNw0RwbszSE5J1yGs0fFdeZNCrrsPBw_0-m74S0Y0PQYQ2xfOuM6gUNRNBoWSKWZJcOuuMXr35HIlfcSzndYFJntZTr5lxd2L2kBNuv4SMBYcpsIFwNwOcHRftaEUZ1vT83bW25ZRgnZtLMDHFfO6XRvbz7s_75GaBi9mK8UWrKsj_e7pf3syokU0W_RIGUISzmOloqOhK6lgnwMGXudBKblUdiiAxnXHWWNh7gKK3_FvcB0z-0aBD5L10w5yLUc33Rfqs2iEYuMaR1Qd073rL0dlmitVoxVxQaoC57KR06miY8XzHwMZz6mkmDmWWHJtx6lKwKtMI7pspUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
🔥
لامین یامال از زمان جام جهانی قبلی ۱۰ سانتی‌متر قد کشیده است. یامال که برای اولین بار در ترکیب جام جهانی حضور دارد، با قد ۱۸۱ سانتی‌متری خود جلب توجه می‌کند.
✔️
در سال ۲۰۲۳ که به تمرینات تیم اصلی بارسلونا پیوست، قد او ۱.۷۱ متر بود، اما با برنامه تمرینی حرفه‌ای و رژیم غذایی مناسب به سرعت رشد کرد و به ۱.۸۱ متر رسید. یامال که هنوز ۱۸ سال دارد، پیش‌بینی می‌شود تا ۲۱ سالگی قدش همچنان افزایش یابد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91643" target="_blank">📅 11:04 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91642">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🚨
🚨
تیم ملی جمهوری اسلامی به فیفا درخواست داده تو بازی با مصر به خاطر عاشورا بازوبند مشکی ببندن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91642" target="_blank">📅 10:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91641">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🙂
دیوث بازی مرحوم مارادونا در جام‌جهانی ۸۶
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91641" target="_blank">📅 10:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91640">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">❌
ویلای ۳ طبقه علی کریمی به متراژ ۱۱۵۰ متر مربع در شهرستان لاهیجان توسط قوه قضاییه مصادره شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/91640" target="_blank">📅 10:21 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91639">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=OLV34l9aSKTzdKVl3N00G9VTCwAlaRQQXfgf7NscAT3Lh4mHVOdbxRplTSVLdnQFKq6-SjXnOeA0FZL9BFOq_KkwfnrsLsXW5O1WlgQ1Pu12eFgKasu3H7BY52IQHAzh9iD80Jm6V5KRj_2r7QX-z-zQzh-NFpS51HrDHxs5y57Zc7UcljAbQ6YfR-rySHxst3tGiudrZF9D84A8iPv8fA6nTQM0vjJlK3UASlszLWxv8_Sgc7zzIIQY5pXz9SSUaiSLZgkxPBd6jst_lcIX8UsY_6ta_rhxEwyWvoKsYarTsRhYCZeX2SlNKIWUevjubq1k-NvWeWO4A8JXKCrGDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/14ade73f00.mp4?token=OLV34l9aSKTzdKVl3N00G9VTCwAlaRQQXfgf7NscAT3Lh4mHVOdbxRplTSVLdnQFKq6-SjXnOeA0FZL9BFOq_KkwfnrsLsXW5O1WlgQ1Pu12eFgKasu3H7BY52IQHAzh9iD80Jm6V5KRj_2r7QX-z-zQzh-NFpS51HrDHxs5y57Zc7UcljAbQ6YfR-rySHxst3tGiudrZF9D84A8iPv8fA6nTQM0vjJlK3UASlszLWxv8_Sgc7zzIIQY5pXz9SSUaiSLZgkxPBd6jst_lcIX8UsY_6ta_rhxEwyWvoKsYarTsRhYCZeX2SlNKIWUevjubq1k-NvWeWO4A8JXKCrGDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🙂
سوال روز مخاطبان فوتبال: یعنی آنتونی گوردون با ۸۵ میلیون دلار رفته تو پاچه بارسلونا؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/91639" target="_blank">📅 10:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91638">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران میخواسته یه بازی دوستانه با کشور گرنادا که کلا ۱۲۰ هزار تا جمعیت داره برگزار کنه که لغو شد
😐
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91638" target="_blank">📅 10:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91637">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUZU7trq5dzo9MT6vXS7xouboSUNDP6ZXKytL2chEy3CfTqDpV81fCUcmRes8_AtGTfqy0k36P6ca7UQQ4ZqQGeuuPG8jRCu-5SVkb7sWcEcnzUVfCH15xAqoCdC9HNvLGNOZKFECc6IFsGgka_eg4SPTc3RdNtLrfEG2Gm58xJJcC_ygS__jaPWK5CHBqwnJdCv1L_ShrymfVxfIvtozUQjLxFGlSiEOQFZJEibXETsIf2hmXpp2otGvqj6mFJHTwDBxlL2j7X-nAHyr0MlCVfLwOm8ACsZBidF3ufFu5-3pFF60f3Fc8GocSB-gVFXo_-TyVJv0NIOR8WQEbfc5rYY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15d23ccc5d.mp4?token=noYH1wDWXoO5QgEws9_xAubaNg9zP962p8aP6O5M7vHDwnRcYlFD03iMsxLl60tAOyCT8Yq6q9NRvwmMX-ZA0a1C1euhUKm5f_wf0Pyyq_nhWH1MJ_s3pP9pPcANs_4wizaxd0Dl_AAlxKgtaZMFZUPjeOBWBTDY1h4ajGbWwR1WtlfTqmCswGWAZqy4oL_YQ5uWl16sFwsd-Cd9FqBlA_gb76B-OCcSAqyo4YUvIv0MEAJimaRsb3eH4Pkn05oW-0d30w2mwQzmAVNxsCTcYKQOmsy7ETRaVU5AZTt7DjwIRmFKORnQSdZIwa4iomKKnj4Xy0twe0EMaCP3LzeAUZU7trq5dzo9MT6vXS7xouboSUNDP6ZXKytL2chEy3CfTqDpV81fCUcmRes8_AtGTfqy0k36P6ca7UQQ4ZqQGeuuPG8jRCu-5SVkb7sWcEcnzUVfCH15xAqoCdC9HNvLGNOZKFECc6IFsGgka_eg4SPTc3RdNtLrfEG2Gm58xJJcC_ygS__jaPWK5CHBqwnJdCv1L_ShrymfVxfIvtozUQjLxFGlSiEOQFZJEibXETsIf2hmXpp2otGvqj6mFJHTwDBxlL2j7X-nAHyr0MlCVfLwOm8ACsZBidF3ufFu5-3pFF60f3Fc8GocSB-gVFXo_-TyVJv0NIOR8WQEbfc5rYY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از هواداران ایرانی بانو شکیرا هستند
🐸
😊
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91637" target="_blank">📅 10:02 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91636">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🏆
🇺🇸
🇮🇷
کشور آمریکا خبر داد که تمام بلیت‌فروشی هواداران ایران که از طریق سایت فدراسیون تهیه کرده‌اند برای جام‌جهانی مصادره شده و حق حضور در خاک آمریکا رو ندارند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/Futball180TV/91636" target="_blank">📅 09:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91635">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/devSPgum0p5Yud8HTX3f1NhT1w7BZawmLBtPun5-HGd8ANq5N-xAfVjvoAI-ahtKUhGGEdwo7tzZCwthpY-CNY4RXu21rpD3wK7aZ6zoj66LuKMRNiieO9WF3V4l_1jKM_qMHDuQOCu_Q6QVN_x8sIddaRr2eaqJOGO0X3RQiiozivUkkKM6ZDfuQ-guQIwMijlE8Be9v-1j2CylU3G-eyqEo5LWAcTujE45gfTOjSp_qwEgdp6eQzC6sFcBpYYgUxbnEbZQoMkcotry6VxLfGYQpxTrYoyMGO7OTXiw_NI7QLyiruRrhTH4PDfmEAFDmbqhBW8DmLWo-aHmPpUsuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همه مدل موهای نیمار در یک قاب.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/91635" target="_blank">📅 09:52 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91634">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=JAsNOjUxIjzngWrm-z94_ZWqf5d_zShEPpZOJ0tfoznWTgg2SydGXnMBQPPv1LhOSuG9uWinKRX9WNlo8jr5tGWGSlx3uwmyldDfqSqGCpR6L4Ag0UTS1aeScDCJ3BMPTNZ5YCvP1J45QoMBB3699Hl9MfCi5LMSvEHHrffMG9FVFICV4Cfy4n-lRjOn04vk36RbcUk1_Q6uNWmt_wW4eIlZsPSpO6OK2BrWJpynES_2mp32lt-fiRVxETmDj5vt3HubO16DQfZHVNk-SD3o_W79n9MeKMqIXrSeb6K7HCvv-jl0UcmIKLpuvZPNogduyaq18isQWm0ZHQyudI4qgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/584eabaeab.mp4?token=JAsNOjUxIjzngWrm-z94_ZWqf5d_zShEPpZOJ0tfoznWTgg2SydGXnMBQPPv1LhOSuG9uWinKRX9WNlo8jr5tGWGSlx3uwmyldDfqSqGCpR6L4Ag0UTS1aeScDCJ3BMPTNZ5YCvP1J45QoMBB3699Hl9MfCi5LMSvEHHrffMG9FVFICV4Cfy4n-lRjOn04vk36RbcUk1_Q6uNWmt_wW4eIlZsPSpO6OK2BrWJpynES_2mp32lt-fiRVxETmDj5vt3HubO16DQfZHVNk-SD3o_W79n9MeKMqIXrSeb6K7HCvv-jl0UcmIKLpuvZPNogduyaq18isQWm0ZHQyudI4qgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های جالب و عجیب لامین یامال ستاره بارسلونا درباره دلیل بستن باند روی دستش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/Futball180TV/91634" target="_blank">📅 09:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91633">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=aJd1keCdtfLxBLIoUe6nYR-5865XXa-zsu1ArrMzzYa4KAhSJLl5hzzcRtCKmZ_FpdH5oXxlAUkkxMAAoh_fgN1XL8ml-YzKIV15PKA6yQMrHpKqNiW0jCqH1GQUFxMc-Wi0hK0-gvfA8-aWhwBkX2MozG2UnJgKc_a-8vxJrg832wqSqdDq5mMN9J3pLK3sqVo7NjTtyM1mEMkGcF_FUShb_l4MsYVfJH-cude-rf7FHzlalppZ5WWX7F5s_WZsrKJtBNVDlTYCNy24Sec_tETV_A69jlqoT-3BAuizow7RmnyJPwgvO0V3SletfgEpc78kqpVbWvJNnq1ocyMzJbgfeopNyjX7xAdc65_oVaRl6Z5ZW6A6_TQf20nyA8u3bQd0BK0qRrtzeI1Mp8vGDQ6Z3c1RTu_wVqPKr_g2DnYAbRvXHt7oaEfC_E7iGVLrAZcAXsbo_w0Dx2mgFth2uRyR60jq6FzA3Vf_QzJxc-mB9gGObJr_V0T3T_DMRgFvBQjkeD5WjOQaeFtuC35HeOx3sjbdm96aP0sx10xGTq8qKXEOPN7Hd8LFpYwEBwh0Qy6ekN2-5Ckwz7QdFjoIJMY7sUn7wGUc_inCtpTI2_C86_twb3DBA1XNAGGmrljA4ewEWrRYBSlOPYc-Rpe2gn4x2dDiBynwRaaVc6yg1MM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37b5e13b24.mp4?token=aJd1keCdtfLxBLIoUe6nYR-5865XXa-zsu1ArrMzzYa4KAhSJLl5hzzcRtCKmZ_FpdH5oXxlAUkkxMAAoh_fgN1XL8ml-YzKIV15PKA6yQMrHpKqNiW0jCqH1GQUFxMc-Wi0hK0-gvfA8-aWhwBkX2MozG2UnJgKc_a-8vxJrg832wqSqdDq5mMN9J3pLK3sqVo7NjTtyM1mEMkGcF_FUShb_l4MsYVfJH-cude-rf7FHzlalppZ5WWX7F5s_WZsrKJtBNVDlTYCNy24Sec_tETV_A69jlqoT-3BAuizow7RmnyJPwgvO0V3SletfgEpc78kqpVbWvJNnq1ocyMzJbgfeopNyjX7xAdc65_oVaRl6Z5ZW6A6_TQf20nyA8u3bQd0BK0qRrtzeI1Mp8vGDQ6Z3c1RTu_wVqPKr_g2DnYAbRvXHt7oaEfC_E7iGVLrAZcAXsbo_w0Dx2mgFth2uRyR60jq6FzA3Vf_QzJxc-mB9gGObJr_V0T3T_DMRgFvBQjkeD5WjOQaeFtuC35HeOx3sjbdm96aP0sx10xGTq8qKXEOPN7Hd8LFpYwEBwh0Qy6ekN2-5Ckwz7QdFjoIJMY7sUn7wGUc_inCtpTI2_C86_twb3DBA1XNAGGmrljA4ewEWrRYBSlOPYc-Rpe2gn4x2dDiBynwRaaVc6yg1MM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇮🇷
مستند کوتاه و دیدنی تلویزیون اسکاتلند از تیم‌ملی فوتبال ایران در اولین دوره جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/91633" target="_blank">📅 09:20 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91632">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/237827913f.mp4?token=LC_KPgca8k3RAtjY1fY6w5AD8ZHcW9JQz_i1ZTTAQBKcGHICEomzyQhNXXvlwSF3FBjIQ3nco1uuGNvlrun2TerOH8Sg829cnCe5ZFdrzr0-3nJEJXSSPZ_59iaLff8zCuMYd8T3Qg6ub_XNY5mkowqHMNxsvZsjs2hiEbzVM0swc4t1R-LeFfBK8yxvIPYsrG0sGXvQ7HfGKrwevYt0CeSMr74WbseQv4ds-Ay_Lf2oyZZC5Zju7zycyuBOU6PzCi5iPbQFlQ1EQFHfylP53DT3CIjStZ7S_BR3dHlfUj7gmXa7O7h7Y_c54i7CWrjlbVhNGumIEP5GTQeuP_HZKGXtorhDaKl8ZiAcQeNuqwGyScert1qOpZy2xsm3aeIVv5Hl6Ux0DF1LUGH-HjeALN_MWZTbWnNg_yPTe1JBi2fIn9nDy5yO0NPUmYKsTA2RhnOxJzjJZS9F5bb8WiktBDkJwe3ki3ehrznlQ1kHNE-g8gaWu7BtkMwctymb_a5q-QyuKade6ZeXkmYUUL7q2v4G8a3uF2g9ilrpZDDUG2S2Ebl8cMIGZyLfMtbLm6d8QKV2ZmT7GOupNHxuhFhhZAi47KRSQf904VHxmo1BTLRzzZ1IvRq--DQpBSLtiD6UTomYl_WrY46_34pkUJbAwM7lGFoB8-lyvci9ue2pL80" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/237827913f.mp4?token=LC_KPgca8k3RAtjY1fY6w5AD8ZHcW9JQz_i1ZTTAQBKcGHICEomzyQhNXXvlwSF3FBjIQ3nco1uuGNvlrun2TerOH8Sg829cnCe5ZFdrzr0-3nJEJXSSPZ_59iaLff8zCuMYd8T3Qg6ub_XNY5mkowqHMNxsvZsjs2hiEbzVM0swc4t1R-LeFfBK8yxvIPYsrG0sGXvQ7HfGKrwevYt0CeSMr74WbseQv4ds-Ay_Lf2oyZZC5Zju7zycyuBOU6PzCi5iPbQFlQ1EQFHfylP53DT3CIjStZ7S_BR3dHlfUj7gmXa7O7h7Y_c54i7CWrjlbVhNGumIEP5GTQeuP_HZKGXtorhDaKl8ZiAcQeNuqwGyScert1qOpZy2xsm3aeIVv5Hl6Ux0DF1LUGH-HjeALN_MWZTbWnNg_yPTe1JBi2fIn9nDy5yO0NPUmYKsTA2RhnOxJzjJZS9F5bb8WiktBDkJwe3ki3ehrznlQ1kHNE-g8gaWu7BtkMwctymb_a5q-QyuKade6ZeXkmYUUL7q2v4G8a3uF2g9ilrpZDDUG2S2Ebl8cMIGZyLfMtbLm6d8QKV2ZmT7GOupNHxuhFhhZAi47KRSQf904VHxmo1BTLRzzZ1IvRq--DQpBSLtiD6UTomYl_WrY46_34pkUJbAwM7lGFoB8-lyvci9ue2pL80" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👍
رفیق خوبه اینجوری پایه باشه. حتی وقتی موهات سفید میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/91632" target="_blank">📅 09:05 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91631">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Fifa World Cup 2010 (Playing Football Games)-[www.Patoghu.com]</div>
  <div class="tg-doc-extra">[www.Patoghu.com]</div>
</div>
<a href="https://t.me/Futball180TV/91631" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🏆
بریم به حال و هوای جام جهانی 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/91631" target="_blank">📅 05:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91630">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AWyeQltKfXvK-zACS201p_j8JbqViuG2wQ3C8EEy8gxOhTQzFi_Ce6awm9iVG57v-5PMO2735Su5QqvlCmoGxLgZNn6So4bVJF3VcB14IuWz_8r6IRkdwKofRbPca9gRYYKlUHjR2nna1wEHunOhajAcjPUzcwQFPb1JX90x55_V0KtijT_hmlICaoHIrj3A9TSRdxTK_MIJ-3g7wlib-VX3Rm3UQ1PJIBvX87p6LAcFZKrgKj7djjS4ua_8H8Gddv6Nb49XbubDgmeJ92gzJzS3xoRGW-1dcgHjD2mB1mS_N7skeo_8R26TR2wXCrBSFvCOzZNl0harvsu7N7ImQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
#فورییییی
از موندو:
🟡
🔵
الهلال و النصر پیشنهادی به ارزش ۸۰ میلیون یورو برای جذب رافینیا ارائه داده‌اند؛
با حقوقی چهار برابر حقوق فعلی‌اش!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/Futball180TV/91630" target="_blank">📅 01:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91629">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qr_Jlf6uHgLLaOhzTmrLjWnAykwc7-U2kZ7zkgEinqYasIBeQktZeuBEXR0fybNF0YiwX7qgT7QXa0wH5XzIWGYWpfi_WEuuBij7xrAk8InecRDgIn2gRoPIlAhOP7Bh42Ta7w8Kt4FWwzGwWworRv5UmusF8vwLlfgapdHRh1j5lbUPZFNz1Dv5r8Zr7T3Eblbgxj-_HQ9VuREQvTi4-hiNlfOyGdismSg_f0rD2vFzog8tsBPNUMq78q17pktOESoOnYEV1KAMJgABUkrCa06K0Ko_cLuatMc-EWcNIp26raskqmu7ykluZgrGz0Ygpc9SBXeEk0WxNjRiDwd0Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
⚪️
رامون آلوارز: بنظرم بازیکنی که پرز قراره براش 150 میلیون دلار هزینه کنه خولیان آلوارزه
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/Futball180TV/91629" target="_blank">📅 01:29 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91628">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezw6g-z0cWIYykrExTPYTTOWV03Zyk26oJh01pwxViABfsMmz2E6AsKNTAjP-8V04-diCcYPiwsbdm_tfL1FzGSM9yizwJg8v4xZgynv1OSFy7jcdhG2PrVRzF7kDZJARzi0718QHsCTPmdbDNXsb-V5U5BHuwjklzP7hDgQOuxXh4AlI7qXu7IfSpmmDbrxdsfk1HVe50v8rhPV2fJ3sUarGZdHpY-Fs6aYLqQeyecd9Tax27ktvOzpRdDTHhcstKM7aAb-iRQkcddOMZdcQ1JgJXcFUMscI4J3KV399vwJkLZRU2RWBHYcwRIyDUrxnchERNeq9iSQbNoWBodY3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو در کنار رئیس جمهور پرتغال قبل از سفر به آمریکا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.8K · <a href="https://t.me/Futball180TV/91628" target="_blank">📅 01:03 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91627">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.  او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/Futball180TV/91627" target="_blank">📅 00:59 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91626">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrRhe9DiFBWuzRsuOipl9wIGbDOOSts6pGri6FvCasCMD2IyRfTl_ag_sIZCRoXxOaII2ii3gAboGLbfUEZqMWLXtxj0OaC_Mcu8kcadEHRMQ6aq4ZIU_toZmCIysakUrd61TFxjdagRbYuM27AyzRFQwPt0oq1rQbo5AkwxPaShcFssVEmXxLS92CpBoPhe3hsPw7eiJuMGMsUrbzPSKa8YEN7-AYKhBxNmSF1C-BiD2sdHDLxPG8nLVKnFviitvjslt-t4luuLASDu8V2sLhdBm09V-XVa6WmMyfpBflNLY6_RJ4Et_2Patc03BRuxk6cUo8mk0HKLbaRjKn9UaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📣
🏆
ویلتون سامبایو برزیلی داور بازی افتتاحیه جام‌جهانی میان مکزیک و آفریقای جنوبی شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/91626" target="_blank">📅 00:51 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91625">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROzMZRLffXUJdf-mt36FGu3Ci6Zvz8sHxztmtP2R9zxs6aC16oa_zqx_GxpDAuwywamaY07q1SASFtRXwj5fruvf_WYS8ARbn9SBDcAE-jbZ_eqOxZoHGdKwMxpeFDHk8uaTl3maHLfQzPjIT1MzW_l3MzPjKl9qLtBm-6QC1McSbMERY3IbZoRYpa6Q1H4kS2MVaN5eqhtMhPMcbMZTlQljOlg0v4rMOlS7JBHnHh9fDrh8xk22QfuI630juqbdGW3ACd_Hu5QajOnnaH_MpLAhrUwTgtuksmMN6-3XHYNU9QEl0yc81g0vlYK5qEQgI8ORSfUo4OiNZCFXL1sv_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">POV: Bitcoin in 2010
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91625" target="_blank">📅 00:40 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91624">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vqJWLzg7XHTYof549ME0Enz0nl6SsJVTtdjQx6Uq0Mu8LfOuln1sKhYt_Z17WQQswiCgy04inNbeUV11l95QoK0dcuzd0znVmcRqcvdlfIx_VCEqqcM_ED8XDL9b4Cn6XobRAjb7u9O9l21YtmS1-Q33JTt9fgGsCU6w8x0XRgHbFxSGeyiClsAgwOJO9q73uGWq2jURXzzouiH8lcGZym7wxous0yJdkNyyJ0VcfVbA2VAcN64p3ziyYgXGWzRaJaGptYTGcgcRR7UD2WA02qoyo_MgrnyerOr9dFaAFXHjYtLGMV8g0V_gid34ZSWX7z19eUoAwDg4OboDocWkpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب: 3 گل 3 دریبل موفق  4 شوت تو چارچوب  4 لمس توپ تو محوطه جریمه 5 شوت   نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/91624" target="_blank">📅 00:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91623">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/ppkR42J1CI97SZn3YZ7Ht1ETKmuEuGJilBSElaVumotDm7P5TXAuNM6CS3Rhwoj5W1ivZf7e7DWi9jywmzkYkm0m3pbdsWVaT51ZatnVF2QAjiUfIHMXf5O7SI6aAjpzYxScc_Ko6-qVUbd7Sg8BqJWC0Kv2xlzLLXEl1_FXogOE3I1xBQlvmQotde60CerNLd9UyVwpmSvADPDgAsawtmyaaHHq0kZaHXxHZHeqjf-4qPAsJj6VwgIxiCCqW342L6QLPhcYyR2T231O-wbwJgptrGZXX5oUPeaz-VWW__E4GOlkQjJwsvYqY8kdwpz29mKlyuhdyd6yzV9rwaVgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
آمار پشم ریزون  مایکل اولیسه تو بازی امشب:
3 گل
3 دریبل موفق
4 شوت تو چارچوب
4 لمس توپ تو محوطه جریمه
5 شوت
نمره 10 از سوفااسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91623" target="_blank">📅 00:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91622">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=LNSwi15oEUD7PICISGRWwalg1DaD0o3IrMK5S0eresteu4vuG0m3Wj3BJcn7m-MtXtvq-T_GF3ppH3aXn8LtTyr52S_Wz0LUI0cTaYEtdxPZ-lmUN7YdmP3epbXnk2dCQSybT95yLwFlSPAz1RAuecz0GgEN1NBLNm0vR0e_7BQCK2VVGf7tYDaaUIY4mIP46O0x6DdYjKMQBsmFDPgGQWVtgkacuLpda2j4LV6kCCOXM-9UzGjwJGL60RFbgEVPd-_0a0nqGmBLtnbc_taKq8nu5OmIvK88q9mFGve_1gUwXJIgLHlLEmnb_JodHb8oSui9P1KWfWlx9vMFQgd0Zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaea310c51.mp4?token=LNSwi15oEUD7PICISGRWwalg1DaD0o3IrMK5S0eresteu4vuG0m3Wj3BJcn7m-MtXtvq-T_GF3ppH3aXn8LtTyr52S_Wz0LUI0cTaYEtdxPZ-lmUN7YdmP3epbXnk2dCQSybT95yLwFlSPAz1RAuecz0GgEN1NBLNm0vR0e_7BQCK2VVGf7tYDaaUIY4mIP46O0x6DdYjKMQBsmFDPgGQWVtgkacuLpda2j4LV6kCCOXM-9UzGjwJGL60RFbgEVPd-_0a0nqGmBLtnbc_taKq8nu5OmIvK88q9mFGve_1gUwXJIgLHlLEmnb_JodHb8oSui9P1KWfWlx9vMFQgd0Zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر گل اولیسه و هتریکش تو بازی امشب
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/91622" target="_blank">📅 00:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91621">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eRHVwkkOARwDT3PqV7WmVpmwegS9JXX4dBE6iKdLS3krMlh1QOb6ls7cJxKapQ0H0BCp83Kx_GfsLjAsey2MAqnWz-rtM-A891mYFuVe4asfIQdOhH4IJULOH7OBOxFC-BsxzW0eNkGh9H9ita93QIxIPsokCvSwWxRmLsck4wYUmkD-mW0xArCQKDTK8QK6ivNurkKZxIzacBLS3Rb-Uo_1mN-hfOjFCU8NcEM22jYzUGc3KUVAfW2ULNACkD-gI2WxWX4wRz2tv_yBB_I-WwnNkJ9cZtyhoRROKyVNZht7YDCMTRg6_bpYCTqzIvrPytyODx_Ljj3pxlfLxFXGzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مایکل اولیسه توی ۱۷ بازی اولش برای تیم ملی فرانسه ۶ گل زده و اولین بازیکنیه که بعد از داوید ترزگه این آمار رو ثبت کرده. ترزگه آخرین بار تو سال ۲۰۰۰ تونسته بود تو ۱۷ بازی اول ملیش ۶ گل بزنه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/91621" target="_blank">📅 00:17 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91620">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/91620" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91619">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=oCr-f0oJaekuOOwZZFllfDyJ2M1HCcdEQRvXXmv7H2ffKUk_3lARw2FhTGkIDYu554B6hJdAeQDszo3AFbUl1invBmn1f-R2mBwr6r4gNYYuJD9AZm4MtK5AQ43M2jubFFkfDKPKzYTuR552mx3hcavrgpo3mIEzv9ONhvYigEn5oLRvpBNrnglgAkL0g-fY4uBSEyqHxOLg4hjG8hODWzT61rRKnhr38hVvcb7lGStOC3Edo5wzCfepK70mzr-s4uB93OxFL4fi34lMkJHMmWIt1phkQjpj9C-oGFFRErk1v2v2YPjA0ZBDfaDHWHGSXJpecLdsENv_QYVFK2my3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb905f6488.mp4?token=oCr-f0oJaekuOOwZZFllfDyJ2M1HCcdEQRvXXmv7H2ffKUk_3lARw2FhTGkIDYu554B6hJdAeQDszo3AFbUl1invBmn1f-R2mBwr6r4gNYYuJD9AZm4MtK5AQ43M2jubFFkfDKPKzYTuR552mx3hcavrgpo3mIEzv9ONhvYigEn5oLRvpBNrnglgAkL0g-fY4uBSEyqHxOLg4hjG8hODWzT61rRKnhr38hVvcb7lGStOC3Edo5wzCfepK70mzr-s4uB93OxFL4fi34lMkJHMmWIt1phkQjpj9C-oGFFRErk1v2v2YPjA0ZBDfaDHWHGSXJpecLdsENv_QYVFK2my3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
گل سرگیِف بازیکن پرسپولیس به تیم ملی هلند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91619" target="_blank">📅 00:16 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91618">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پشماممممم اولیسسسسسه چقد خوبببببه
🔥
🔥
🔥
🔥
حیف این پسر بره زیر سایه امباپه تو رئال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/91618" target="_blank">📅 00:15 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91617">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnRx61SIo37L86KhMFv_6feHwkCJbxvH3g8WXAYG4Epne-cu1sudKLRfGVZZU8jmC0lscV-_xxYZtvDtU-N47xIIiO_rYA9_eHxZBTzkZB_2pqBI4ipl3zU8-F7XQRrT3CLSxaBr6w_rWzYiLwkHXT9GnLFnfXh11DH1PkjKj4K-TMmA7HO0SIJeq7idsYer1KfBrw90OhG5OUdgFouHh5aWQBLRBAGbGQ5yG795uZ0bNCSDODtBvEmnmRrz9pXXuB5sUFOV56gdCxQeOzL-BEVCUf1fEtxaPxd1hRBVfWD7DWjJA8JxlQZdkirBKx7-dgkOBUXB-kwjuiv58MaZ6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمر آرتان، داور سومالیایی منتخب فیفا، از ورود به آمریکا منع شد.
او قرار بود اولین داور کشورش در جام جهانی باشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91617" target="_blank">📅 00:14 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91616">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtdgcBCSPSZ0rFOnALX1v1NgkiE4ODSIadVRhtbc_8liBjDhXCmLQI7srqsbd3K8NRDfTXpcY1L8bleOVhDdfjnAxFWcwTgL74fuErQ4eSjN9Ko3dgMjO2tEDXa65G9tHSGCMs9NdbXL9a-QvvHJ7gaCVRC6cbqYbxovh6RMk--Nwt8ZEjdA6yDAyleJUQyBHrd_aVBKFMprlT5yScUWl4VEIOiR0gqZyftV1eBCRdDDxihM_yLYe8kB4OdEXC8oiZGc04yqKwjQmzq92-OdH8GvS68_3Zp7s4TAU4jK0tDFn4JhFCPpu9Ti8V6Mvl8-fc4BHaHb37vtoanO6-AARQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فووووری؛ یونایتد، psg، آرسنال و لیورپول بدنبال جذب ماتئوس فرناندز ستاره وستهام. تیم لندنی خواستار دریافت ۸۰ میلیون یورو برای فروش این بازیکن شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/Futball180TV/91616" target="_blank">📅 00:07 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91615">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLz1WVdMh3VEqIlsQwMDPjoSA8VTZedQUpWLS-ejSKeM-C8B_LQ1PanAdzLUbZFd3oJ_BEa5t66UNmMCDTIAfYbRSMZ8bxCmsNkWwhv5iRRx3UrJzE0yqZuEggICb6iRcFN5wVivEwLo3Yhspygo4kjf8Emw4h0VNHpsO35Mu-lTJ7ofwBru0HcLlzUdI4vQYKCFPbFohNZRrZS93u3RoG3P5QSl3PulWZYjQJavhxkUtyslOsc7GIsyc3MRB5Cfh2KCNgn1-3BkGDhpmQLfwr9UokAoPx-nrvHasaw_LUEgaL_pwEaZSoa0HAawTfrkGtN1PazZhzIHjSEvEEamWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووووری
؛ گستون آیدول خبرنگار مطرح آرژانتینی: منچستریونایتد درحال آماده سازی اولین پیشنهاد برای جذب رومرو ستاره خط دفاعی آرژانتین و تاتنهامه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/91615" target="_blank">📅 23:59 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91614">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=GIcucHgLIj8reavPgPczUi2THJtQsvOBhhcIJe7omL5Sy_4bO3i0-EvfH4QMUJseNYmxjBjzqNwVgTZyDJv2SENT4yx2JWaHkjUhhlLYLFiOn8B9eDhO6IndSb5SedgxidoGHdVaP8QWmJGDqdkIlhmgAqlfw8fYG15rJdKIPc1HKelpGYssgt5XftUxwgceqAwQcn7SfPTvKWKSLyFCqZa3HZ0ZaPgvuqjusLndAKjfLJuKJHmBENWUNTWheI8PcrVCQgvZzXB0FCcjhwUbbD8d5qgNcPLjnywvg6Mv9-tJYiB356GeZkYPB4ISW3Rfcc_5b-J_qQAgEdef_G3pvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c9b54af6.mp4?token=GIcucHgLIj8reavPgPczUi2THJtQsvOBhhcIJe7omL5Sy_4bO3i0-EvfH4QMUJseNYmxjBjzqNwVgTZyDJv2SENT4yx2JWaHkjUhhlLYLFiOn8B9eDhO6IndSb5SedgxidoGHdVaP8QWmJGDqdkIlhmgAqlfw8fYG15rJdKIPc1HKelpGYssgt5XftUxwgceqAwQcn7SfPTvKWKSLyFCqZa3HZ0ZaPgvuqjusLndAKjfLJuKJHmBENWUNTWheI8PcrVCQgvZzXB0FCcjhwUbbD8d5qgNcPLjnywvg6Mv9-tJYiB356GeZkYPB4ISW3Rfcc_5b-J_qQAgEdef_G3pvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چی زد اولیسه
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/91614" target="_blank">📅 23:58 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91613">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🔥
چالش جذاب و ترسناک‌نیمار در آستانه جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/91613" target="_blank">📅 23:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91612">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QkaN6DDpNYLuEop6HDX3MEG-y95aagoTuSDFwGfhmRd4oLblQzE6guH6NKkvUgB-DECg-vrD5JZWCkp0SN653bLLNYXcP_0OgCzkOIgi7x0-quZOsNQny3EX5Rfm9I_9j2Olnlztk6t9ZDgoMv4SDkKwIuj-cbNJJS3laVlPgx2v8yKwtz4JhUPe7H5wponVyiC78AwRIVfaZl1jmiokpDySXqN-HUCyQSNbwjKdWnjA2zMg9_RhjZHBpOYIbbnGgNb9zT4MH0K4QeJo7S89DSCc4N54A9Ip_Gfw0fFrCbD9Kzn7ZyhHNxZouruyMiV4DDpbZ-rZVMf_5A71j6ZkPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/91612" target="_blank">📅 23:44 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91611">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vuyCO32yzNUk6ZwAzp6B9jXB3_tSTRUFPFsVJeKL-cQtubSyesw50DXg8d3GVg8Ssti1fTdRqVFg_SEnQCpZOTc07MGHUKZHsbjW5oewPY2xhqlLyUYeKAW_Ipg_Y5WhML4rXcAttGGN4RiPwgNwEQ7uQ2yJbd2q4zFZJuODlaupym-OQDsdJPI8_QAKTh93TJkYZbShLwNDwJWlbjZ1FmeoSy_waYUqYc0c1T_cVtHhi8mar3f5qM3UvbOGh3qbcI8jrkh-o09JU3DXZ3KVhIv8k0sefBs7txdbiKxDUKOukHjm0sz7IhKCJVaXRuHXcQSqeC4aKLs8FexUEtDugA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇱
دی یونگ: میخواهیم همه را در جام‌جهانی شگفت زده کنیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/91611" target="_blank">📅 23:42 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91610">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZfD7R-V8Y75-T0kT2a82bURrEN3PWhnglbRAtxFp0Yqti-Mum1xMnI64LCAijSLhwZCh0CWxoqSqQC09Ko_VGNZHBp7JRm8gJqLKskt0FrVt6ns8Ug-bO6sLzTxql9ummfylc8Kk7LH9KoVPxMEd1BMIaBJBKi20W6QJzGWiKsezA_TkAe_wNzdLq7d9IklwSEs0sKuRo24ykG1cxJCLWTttE1P5UmU1B7xfOJ3evmq5_FQEfUNfjW8h85gXq9jN1d6o3RXSFAEmphmX5fAB4ce6-NBycZn6PUKyAOCW0e9JzckX524M1zzBt_Tt5gjvdDC5ZqkAOxbH06oc_hUV0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اولین خاطره‌ای که از جام جهانی داری ؟
🎙
یامال : بازی آلمان و برزیل و فینال 2014
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91610" target="_blank">📅 23:30 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91609">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S5nlqVJQpJXXDGDCjDg7vrH28G0RAEYd1OQBb9yXTmR6_DdFhnoBvbqEE7XRCrpq0eumaKky0AK7IfJmvBeOTW2a1PAnHlfhTE7JoIXmXCx17tXd3CPKrzpnGnrDxcrJBKKwAdYgDp6WhJK-Qe4OlKDUOoXtRl6m-EgyU5UP3j0BOHaETVG3IeaX2Wwj_gx0DvwATgpEest8cZkN27-fJwK-Dy4Fia-lXTKIb04HZ4X4OZqKoi6rZnCPfZNrg86nKjyISRyxGuonyHglUWPI_HzehQFtLS1imHkkLqzfW09Fix5tcDCHq9STS7_4IgSJk8rlWLTf1NoIaQCec2X20Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
| کیلیان امباپه دهمین بازیکن با بیشترین بازی برای تیم ملی فرانسه با ۹۸ بازی ملی شد و از لوران بلان، وینسنتی لیزارازو و کریم بنزما پیشی گرفت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/91609" target="_blank">📅 23:19 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91608">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d43547db82.mp4?token=t8vbkTKX9xO6ge7jZJEl0c_FexKOn5VSan6wXgMOCwTnNa9-iLbEJszwq-nVec264yRBt1jFzmhS6jIlcwQFXxsYcnLMYHPoLkxCFaqemr7hn_9KAUWDvgxaDGJSlTmeD0cNaouuzUzhRT538TlJ-rjFULMWJ1GjaUvlVXgngMpLFYn7THL1yP9J2Cwap92bD2Weh3tCNYpteVWyfWEDsIXNQ483u8WcCs0zXuWB3hLDWnXLJIrnEsS2iX1-TFsTyrGIYZBCkPV6bvMVJGalZ2njZ5Fm30JL--a2-bZUikTEgQmt3Silw1hoK5qoaaRBNvmBkZlwquZl4UPULqmvcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d43547db82.mp4?token=t8vbkTKX9xO6ge7jZJEl0c_FexKOn5VSan6wXgMOCwTnNa9-iLbEJszwq-nVec264yRBt1jFzmhS6jIlcwQFXxsYcnLMYHPoLkxCFaqemr7hn_9KAUWDvgxaDGJSlTmeD0cNaouuzUzhRT538TlJ-rjFULMWJ1GjaUvlVXgngMpLFYn7THL1yP9J2Cwap92bD2Weh3tCNYpteVWyfWEDsIXNQ483u8WcCs0zXuWB3hLDWnXLJIrnEsS2iX1-TFsTyrGIYZBCkPV6bvMVJGalZ2njZ5Fm30JL--a2-bZUikTEgQmt3Silw1hoK5qoaaRBNvmBkZlwquZl4UPULqmvcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازم اینترنتا وصل شد گیر این فن پیجا افتادیم.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/91608" target="_blank">📅 23:14 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91607">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Y6D_JfV8G1ROxde1TQnO6O30gDfOCLfFGU90ESzVPrmZD5En19AjEGOZN0ulrvIZu_y9VLSuKC1-zlA-vRAkc8Kp62DxJIV7RLMGL3xzIa0aR7ICucDD-oRSr2diXOI-55ICPYJBgyE_sfmmmqirpVoKaKHF3f5MfjsCoU7VBFd5yK3jn-xFROSLW3ZFeg9xBdt1EOKv8iCXNFArJDi4dZVm7-pIxj23D-XvuXXfnAlcHt27ztpLurHHShzea8ATEkDDbN7Ehq-sMTmYQAJ24HenktaMFOL05eOjyA_nDk3trD2X8dNCo8MqfknYKy1BD22oWC84deckDjliCIwjKcg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f21c49fb96.mp4?token=CwyZJSjMEgqjtAtv9WmZ4UTz4RRy5yg8AP2b-uJQoiGMuy9dWKD9uqj3Br0XfOHJ0Xe9ELwZee1HVWEVXLj2TjPh5di2anWbVspkV_itJgtfIWp8EY8EzYICTAWxuvk4voYTr68aHdia6zw9L0b3TbPoLPl44QNzvdTFpQ5uLY9ng-XimQG_2N2nWYxwlNkjXQ3ezDVmHRcaGj9gnLCcj6xpzGYVjckDW3kbBa0hwVjf--C326YMpVdjPoAIQAV4acbPeT_WhveUHUvpvSSikOQ5EOeftCkp8RoNWFxSWUlsZDPPuAv6izS7KUN4D0Pzw9J_oQsSqk8GFoM28km8Y6D_JfV8G1ROxde1TQnO6O30gDfOCLfFGU90ESzVPrmZD5En19AjEGOZN0ulrvIZu_y9VLSuKC1-zlA-vRAkc8Kp62DxJIV7RLMGL3xzIa0aR7ICucDD-oRSr2diXOI-55ICPYJBgyE_sfmmmqirpVoKaKHF3f5MfjsCoU7VBFd5yK3jn-xFROSLW3ZFeg9xBdt1EOKv8iCXNFArJDi4dZVm7-pIxj23D-XvuXXfnAlcHt27ztpLurHHShzea8ATEkDDbN7Ehq-sMTmYQAJ24HenktaMFOL05eOjyA_nDk3trD2X8dNCo8MqfknYKy1BD22oWC84deckDjliCIwjKcg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این طرف تو جام جهانیم ول کن گورتزکا نیست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91607" target="_blank">📅 23:10 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91606">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=Mny7_8XWWO3GoHj-9t38gwdwcaeKGOf9IalXwaMZnv7545UFJHPvGu_jKiasZQFmoLm4Cc2R1tJNE272QZaT18SUqP5nU1CWMGVAe8SIH9QGcGRkg2SxexQSVgj3iesZb-Y6l0DXkgbFBZX4EBsmy18NRBspCeKCkZw79JAcmJslV1zRdQqM4KWt1K5WtC349CNJ0-SASNdQiwasF1-ntbxvwDH2VInZerkHub_OVV-WsRUKYI0Nt_g--mVBaDbU2bLwU1fwpR19v4aT0VtsBZwTSbDGrK83M4paQ2I9yBDRw4YDmAiJ4O6FR9PPcB5qp0VKnXHgy0dXqUUTTGMySw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92d1d72e16.mp4?token=Mny7_8XWWO3GoHj-9t38gwdwcaeKGOf9IalXwaMZnv7545UFJHPvGu_jKiasZQFmoLm4Cc2R1tJNE272QZaT18SUqP5nU1CWMGVAe8SIH9QGcGRkg2SxexQSVgj3iesZb-Y6l0DXkgbFBZX4EBsmy18NRBspCeKCkZw79JAcmJslV1zRdQqM4KWt1K5WtC349CNJ0-SASNdQiwasF1-ntbxvwDH2VInZerkHub_OVV-WsRUKYI0Nt_g--mVBaDbU2bLwU1fwpR19v4aT0VtsBZwTSbDGrK83M4paQ2I9yBDRw4YDmAiJ4O6FR9PPcB5qp0VKnXHgy0dXqUUTTGMySw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهکار ریدمانی امشب امباپه
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/91606" target="_blank">📅 23:03 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91605">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AwT9uPEcauH0i-BZAX_zIdtDv9ineW42EWWq2AoYMyxQXL25NVl-xyoNr-hc0jtGWUCJ5nTdGGX1XLnup-XwTU-6pdd63kE9Nt2Sf7tyERMwlT730qMqlGi_jril5ABF1Gxs2-e6pWt006RiyNcb_7ke20rUHk3yv-k-ZfbaRJsa7ErFvqjkIR9cOD2i46MP-1kBQeem6cStqhQQYOsEv-ZsI82qRHR1dFuxB1orOnOr3yLy0HBN0dy0LXbHVgu-yhuFFmifipYsyCRYeBe-wkyp6c0_vVez4AZ3YALwhFZLSUxQwEPly3a5fisVRBnG3XQMNkKjF0VGdb_GQaP5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فورییییی
؛ در نزدیکی کمپ تمرینی تیم ملی سوئیس در سن دیگو آتش‌سوزی رخ داده
❗️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/91605" target="_blank">📅 23:02 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91604">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=uqFXZzSvvFLjTiVGC6VSC3qne5APRwUU-bT4mSNw9T2Hn-sDgW-sa4xxbWgBsjcgduufoYo-4aQS1k-gEZrxfzUKx9eDlrSF4wo464lMQQeIZeXqYxgkCwJbtV9MCarDp04dSbPb35TIs8U_Qd9sWJrRYplWm1V_h7S8sCmGc9-SqFaPppB1mkZVYDj3r8dLgSbHoAjw8v6AgQcJ8TEj5z6qzuXL0gMzfh3soeq_pxnx2R_dvOXkNZYhFCrZd05NtqXY8UBRit_BW3iqx5wMzNDLkAWZ2WTDUPWf22FPJvNaGZwnKuB4tBolFxSsYlk_SRJKK16LAAErCP8DMQSyUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37db48d9f1.mp4?token=uqFXZzSvvFLjTiVGC6VSC3qne5APRwUU-bT4mSNw9T2Hn-sDgW-sa4xxbWgBsjcgduufoYo-4aQS1k-gEZrxfzUKx9eDlrSF4wo464lMQQeIZeXqYxgkCwJbtV9MCarDp04dSbPb35TIs8U_Qd9sWJrRYplWm1V_h7S8sCmGc9-SqFaPppB1mkZVYDj3r8dLgSbHoAjw8v6AgQcJ8TEj5z6qzuXL0gMzfh3soeq_pxnx2R_dvOXkNZYhFCrZd05NtqXY8UBRit_BW3iqx5wMzNDLkAWZ2WTDUPWf22FPJvNaGZwnKuB4tBolFxSsYlk_SRJKK16LAAErCP8DMQSyUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
زلزله 7/8 ریشتری‌ فیلیپین اینجوری باعث شد این 3 ساختمان متصل به هم از هم جدا شن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/91604" target="_blank">📅 23:00 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91603">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=P9PJ-7Qa3VA4OTTqsc7B8lRrJbdeLlyx95dUpokn-wz3JINtWSnWMAL0LNxtxPo8OzkVfq7BCU6FtRfbBjb0GnSBBq1Wp5WWMaPV8fhGyfPjjSBy7eFhU11OFev_7vnjmfUoNpsqIb3MbALBzBjqU7kCN9KZwabFdy36hCxZ1HMN_EgbkYPBNG0PUupCxbLeoD0hvvkRi-TPYftj1OfLzf51Gv-m0xbm_FeqSgzq8Ams-_gyPtRY2huE2oO6HHsrPgQjRV1ReNJtXGJfte_RkkyGL4LaYwrqVYyf626qYSucE5IHNYZZ-t_dXjX2dCwNE0z8KZJDH0w6A-FQSHp4eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45f87b14f6.mp4?token=P9PJ-7Qa3VA4OTTqsc7B8lRrJbdeLlyx95dUpokn-wz3JINtWSnWMAL0LNxtxPo8OzkVfq7BCU6FtRfbBjb0GnSBBq1Wp5WWMaPV8fhGyfPjjSBy7eFhU11OFev_7vnjmfUoNpsqIb3MbALBzBjqU7kCN9KZwabFdy36hCxZ1HMN_EgbkYPBNG0PUupCxbLeoD0hvvkRi-TPYftj1OfLzf51Gv-m0xbm_FeqSgzq8Ams-_gyPtRY2huE2oO6HHsrPgQjRV1ReNJtXGJfte_RkkyGL4LaYwrqVYyf626qYSucE5IHNYZZ-t_dXjX2dCwNE0z8KZJDH0w6A-FQSHp4eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
👀
ایکر کاسیاس در مصاحبه با روماریو: «مسی خواب و خوراک رو ازم گرفته بود.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/Futball180TV/91603" target="_blank">📅 22:49 · 18 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-91602">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiZ63OLlt7GrM-iIqbgwEQYYHsD2IMzZhuI6Kmhv5EOyJp_uf2mTkfxuzw4SefqZgbaAiIvldoBUlJidCJSivw4FO7TfhfHQYHL7DltcLq5-BmefUMpnHQpSN76woGIXvNImSCBvLUI4RUCAho3OuCDi4bhxxGi77Ln-DPw5j9k81fDU0R7uqCyuCTonezOUluMZd1yCHIaeP1drUArBVwmV1TClNVEkkEVbm3QPMH_BedGyeLKLLOmtS7Frc4RIErUu1JyouRDlOi9YTrnJzioyRRGvTyYaDD6Vf0aotXxwid2LLzhPwXHpQULpAtjMCmXcxm0Pq3LCqFzGc79hGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برونو گیمارش:
«برزیل هر تورنمنتی بره مدعی قهرمانیه. پنج‌تا قهرمانی جام جهانی داریم و این اتفاقی نیست. فقط باید تمرکزمون رو روی هر بازی بذاریم؛ اگه همه‌چی خوب پیش بره، دوباره قهرمان جهان میشیم.»
🇧🇷
🏆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/91602" target="_blank">📅 22:34 · 18 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
