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
<img src="https://cdn4.telesco.pe/file/OFbmYhHh9HamxCIBwieuc4OvK-9MRtbaT8u24o0sLXBZeVl7fcFAkxbY-lZHLVti4kQ_6SLRhm1fNk5F9jezHTsPU71KDoisVP3guItdxZ_2gsnJwhPA9cmGQsVRVuNBV6sU1FC4AtmxlKMl2oDABqY4NJgxo4DwWLKwu-af3n6fyaDTodNabZodYMoGID_ixeTdToyO5_UPhD5sQ2TpMWrEDnS0UUHpDNJaIKyCa_VoDhvyZuiFB8bONn5XC6JI-TH7Gik4N9SRPiGOedbGoNRpq-XAI9tW-pjuDizTadMgtxXAiR7pfF-Mda039x3WLxGG4m6uMnBSuw2mR_RJ6Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 174K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-17 16:26:06</div>
<hr>

<div class="tg-post" id="msg-77058">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
حمله به بیروت از قبل با آمریکا هماهنگ شده بوده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 918 · <a href="https://t.me/funhiphop/77058" target="_blank">📅 16:23 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77057">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m_Gfn39MBpbSahUSPCHnQQQaV5jhOT9iWOhAY5PTZ2zAs0525n_a8cu9bwvCyWXPciDtuRiicJgIZn6E_1pqhf-667H7PmfrEqb1emJ-bXFCulRysDSyhvw_Wp8KFfKHdjxc7Il0mWdladujFk4_BMeR2OXYk5OtEqmo0LiJnhZ0m62mW31mt-cfuHkOjT0LhAneyps6hVnV6ks9O-eVanQu2GpHpfPyKRvQejdjB-yecbrz9oqYUyMwBwtuk4L5xMbdV0GLMq2wJw7yI2jsDCA7M4yQxL4JcfpmRKTKE8H4qFFizg6_8shK7620bW0L-ASiuJN8OmpzBVjx4edryw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنیامین نتانیاهو
مردی که یک تنه داره سرنوشت خاورمیانه رو عوض میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/funhiphop/77057" target="_blank">📅 16:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77056">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الان ترامپ عصبی میشه خودش اسرائیلو میزنه</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/77056" target="_blank">📅 15:57 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77055">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سپاه گفته بود اگه بیروت بمباران بشه به اسرائیل حمله میکنیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/77055" target="_blank">📅 15:56 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77054">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">پشماااام اسرائیل بیروت رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/77054" target="_blank">📅 15:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77053">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">کالابرگ افزایش پیدا کرد، دیگه میتونید روغن بخرید با کالا برگتون
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/77053" target="_blank">📅 15:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77052">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مردم مادرید در صف رای  پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.33K · <a href="https://t.me/funhiphop/77052" target="_blank">📅 15:18 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77051">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OPEPKnJlXgp8GFLcYU6MV4cLFelZ_kZxQzH_asYKcpcdatznhAum7Saeg6fPcrCilt7-RZ2RRo-HwSD4YioeZv_CwjjARy0WJtL9vxCyf5u8AF5k_JpkpvjAHozsgvYtYwEOXkeDSm73I89A1o3EZXzioEJ3KfPbka6JVlHjiASCcprRtH14pTXcpBt-GEXn3bwvxGsidogjpMbSUIBx0QFeS9qKaRIqiS1WJ_liFrU_nRCXJ10-toiN7jGgP7bYN2VakeTYdFhKUizyLDrr-JW-iia90Mh7RD0eAzCEjY7CsM525ElJTEIXOqF-sjW0oCKLBTgVBkdi7TZLZlb02Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مردم مادرید در صف رای
پ.ن: حاجی منم با سیاست های پرز مخالفم ولی الان بحث، بحث رئاله
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.94K · <a href="https://t.me/funhiphop/77051" target="_blank">📅 15:11 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77050">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJPdCxc24lHRVcXw_F-60Ep69Z-8egP9smzoFVekGWwKRinOdoop4ZcfZDRUfz2MIl10lkEEHNLpET-jENqrKnIzLi5XuTTJeeEqPYjYmQrgVEVSoDbyGgJvq0hL5FH2rgRKMNpnSlZH4PJIkzq3NZi4X5wQLc7hc8LT4GzB6A2VBFncSbYR9fPA5ihkbbCu0GYPb_EAXyGcTl45W0eA6eku7Dpz5mnokbstZOcq1P-FTZKvDbbcGYVI4K6eXJE6VC7KMBmceWd_MGMFnmjfJstStRl9uvlC7nmIguzA8i1PSkha1mXmpnvGUNjvmf2Z2f3sdHgWsSCIp-cX7ocSUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیموتی کصکش زیدت کایلی جنره بعد هر شب میری بسکتبال میبینی؟ کونی تو اصلا نباید از خونه بیرون بری  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.69K · <a href="https://t.me/funhiphop/77050" target="_blank">📅 15:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77049">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وکیل تتلو: امیر تتلو واسه ماه محرم درخواست مرخصی کرده تا بیاد مداحی کنه.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/77049" target="_blank">📅 14:27 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77048">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yk8BvYrD8WzJyiJlk0nHSm6f9czBSTSwwqjNeOtEJtfO9sgiSR084Zq747a3NGd5H1emhXWbbmabVXCYOKHZoPNdctJt791DoZ7SJ0CMuousMZyz2HD7KIkcjiGRuvmfSNgKWa9C49fvAEzh00E132iG6Slwyp4U-PV-G5Juq6tJGdEEjFufXp8H3ky1jCrxxtWMom0H77pMX5eVUcRnxYVoLAO4ofBn-W0skvsJU9vk_hirBpQJL4LraVUDiuM-z6tm0rKvaDceIT-sxTjCQwB7YRShEbGQAI0VOCwE3Px1udUBumREpEvRDVUCwAklchAHRSGI1b3o-IEjNXepcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
آیت الله جوادی آملی :
ترامپ و نتانیاهو باید فورا کشته بشن و همه باید یه کاری بکنیم تا کشته بشن چون این خواسته و دستور امام زمانه !
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/funhiphop/77048" target="_blank">📅 14:05 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77047">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHunter Vpn | هانتر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F__wdScpi3cWb-tf6oWu9hNEyDkjBzU0kMzwva1haO3ppzaGp6gOsEkQo2bOdKMXXkP5hhy9o0_6QZ_YwcUAtRVt_IgTnCUVRAuQCWqwI8rlXm6iZpiAN_Jf6A57n_OQbA6yO2uXPPD1AD3qABAMaj97CC8SXO7U7NC2lKHZ3KY9JLCUtIsUIMVdUZYYwyAHG1fUrdKH8m4tWj8In0wz9pBK6wzso7AUdVuZejoNM25OHZWMLkflzwV_WhYicfeVnIN0etVIruz6ZuOGqr0_cxrKHkQ-p938DgMD25Mv6NJ1md7Lv-JTOLCkJHPeMEiyWkhzuv-rHhuJ-GjZYRhnyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فروش محدود فقط گیگی 2/800 تومان
💥
💥
💥
به مدت محدود، ارزان ترین قیمت
❤️
☄️
10 گیگ = 60/000 تومان
💵
20 گیگ = 99/000 تومان
💵
50 گیگ = 180/000 تومان
💵
100 گیگ = 299/000 تومان
💵
200 گیگ = 560/000 تومان
💵
بدون ضریب، همراه با لینک ساب
🛡
کیفیت مطلوب، قیمت عالی
🛡
پشتیبانی تا پایان سرویس
🛡
⚡️
جهت خرید از ربات اقدام کنید.
🕶
@Hunter_VpnRobot</div>
<div class="tg-footer">👁️ 5.49K · <a href="https://t.me/funhiphop/77047" target="_blank">📅 14:00 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77046">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اینهمه ناشکری نکنید، درسته قیمتا نسبت به سه ماه پیش سه برابر شده ولی نسبت به سه ماه آینده یک سومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/funhiphop/77046" target="_blank">📅 13:29 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77045">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/77045" target="_blank">📅 13:02 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77044">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCSuTJCoJhll6yeAO-DyPWJJ9nhTwUIO5N0-4KTirEE0ykcrY-uojTkfASqpiQn96sjzyKuBACPsOiVQ1wHRHAb7Ms_ErzN1Z45JEq0o6sSz6bLsccdnLHPK580j-j83mEtvfjCPTQm3q3TT8_VBtu05fS8r8CCXvPobbsqEFHASQMvSUfawEA1jKunFjvr6TPLmaF6YGUtIovJ6DEbLOpxiT0t95OX1AiN1Dd49PLeZWoaWnB6U45gjDiNd_-H3q7o-8fUlJu4ztu8938uIw7iNzQAEvmBmT2OcLHGN1XhPV8LYHKcHdNsj351R42qbBnpHGk7T-46OkE2dX4aXSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز جام جهانی شروع نشده قلعه نویی حامله شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.93K · <a href="https://t.me/funhiphop/77044" target="_blank">📅 12:54 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77043">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lz3agGh7jbY1VsIPJAsUW2bk4b8i1HTZM0culb9lsDYC3bPEHLaZROsEJzeFvu7NyBHlM8o9nw6xhWaAvyZ_SCUfbOTE67U89TAbFc4-9WLyTenGkXew8ptUgQmSop737xaiHtZqOs_SYm27jajz0N5LEavYVc3JU7PXWiv6vDbHA_dysWfAT0dHFnfKqAMcCj6Uv8ow_omCk44Aanep6LOrKRqSvE5iv-_LBpiUQDIj_3KglTGTPg2GsuSfaznSI5txlUARkfRQZd51OJVHg3VovSAiDE9tXpmoGA6ZxIks0_A8J5xbkW-pZi3IMKjftn1ejCm4XB8lvAhGhzi61w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.42K · <a href="https://t.me/funhiphop/77043" target="_blank">📅 12:49 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77042">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مراد ویسی:
نام جانباختگان مدرسه میناب را جزو "جان‌فدایان وطن" مینامیم؛ زیرا آن ها نیز قربانی سیاست های نادرست شدند.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77042" target="_blank">📅 11:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77040">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VD7R5zdKE-uglCeXJAq4_BtVchoS-Bdkm5rJHmHHZUDGHStVqtxb1EnMLWEFu-Q989L8fuznBQyw_d-9BUc6ew5ZRpIwB-O9455MFoc3YPQWFziae81_nlYaR1IKgpxsdC2zFYWSHqsSDAGs-lKSdbHETfqEiRFUQmzfgXqARwA_daMK104QkYy5FIpJ5YpMkSi3Q_GeUz0qO3bqi4YhMyiLYGleO0hmmW_JU9KAe03b21r2tRmds3Yfrmi4Y3blsbxvp7d0ncrrvUNy8u5Sy5jmKfJVGM4fMPNKowiQN-mHZfb_XIuohaR8xGjqhmXdMY-1aHkNQ9qUhdg8l-CMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77040" target="_blank">📅 11:48 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77039">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oeIo1KATJ_fnHSdQ4mkDA2Jn9XU4xY8oI2s2Q4FqpFCoMgUya2pY_cEWX0ThpG-Tbdwtjz8Y2xhJkYfnm9V8mkC-YKQQxh8wbAjqCmHTP7-PBgCBktrdVcWXWVQTRl5q0wTkgJMRp8Yu6OXv4a3zPRoiEwO_9_I1Duu5yBRQA9SXes0hKlIRJ7E0Dk9n9chncPLQThgUN1AMvJyqBvlPex4NxeXVxQC5Vr1n-oCWNHEl95aA23AQszQDJCsAkbEMQvR0bqS9RoGheX6ty0LNJ9BnFKi8thT1oN2ggl47IitiJK1vufit46lAnaepYJ1w4KWfDWqkF6yxHpNPIUwCAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو میگه رای بیارم امباپه رو میارم فنرباغچه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77039" target="_blank">📅 11:38 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77038">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lP-ex9SjUUjDJ59Uv-SFwsbZfe6JMTH-xXO_S1QE5diwwU9dJEZ6_06Pa7cCDRfzw7UJsqeZRc5Mm2lfYcdDTaiBz-gB30wApaRJSHTQwwmwg2LEwRxTk_bFVI4eqGva5GLwD9Yp1yoZJXYAU3Mq82dY5kDz7EVTMYXAoWX2o2b0eEEZROC08lbijDAPAjFvr82y2Gd1LaCvH3d8bPKtafVzl2sjKQzR15O592dJ-XMn-OmQ_rYBJiDavb64MIuopL0VRvact4VfSSUDfGXTA0SlNLeN8sNH1C7C8jnkVy4UdMrqZilsW1103fKfJl3LM-Kl8OL0VjjM66Aj28mGJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الهی آمین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77038" target="_blank">📅 10:59 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77037">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oqoul19XJqYO0xSrM7GLWkS7T4REw3F9-A2yC4vNxqmF6bHNi11_XavhZNRg-CmHRygVA5lG-_FmoJL37cqlNPtwOLtKdVybROEWqoMO9FX7By8jilKLLZ39XKTmB57Q0e6UfMjbg-h9HZAjhpoPH2L2uh8pt1LpX092TF0SGinCR3_-61ZmIrc94xzNB4GgTQOgx54jAskwDX9EYxaRdtRa_HBVqHG6gUPN2Fa2QRW5Jt9pmYkNsZb4NkGTqLQUzziLCWMQF3yHJlwQI6OdglCEN05LWu9hKbMzvdWDR6x6KM8pQFIzlPBvf5yR6Dn7lg5T-aJeSUSvI2d_ueMKvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیگه حتی به اینا فحش دادنمم نمیاد وقتی این ضریب هوشی رو میبینم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77037" target="_blank">📅 10:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77036">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JrteetpukhtglCf6gSH4YkVnPm0P33fLMV-glyYWP848p5MTDOEgOknhxtn_-aK_0LIqokGGNjd2H_TerWV8yVn5HbpidhA0HzZxUfoeZmiYZPT0wcmEDBqDuHFKsTxoV1Rk1Ogs_VSoiY5lJDKKtd8mP2rxNaQ31gSsbPBlZvYzh0I7S4NdtKZCVlZh9zNRudb7QLcVvxnndF664rDZOsVadkTEZl-zRTEsUnNvZI3Z2GbFkuUzGQ2r_uFtbeQsHyS18ZU20U7viEX_Umu7kgdYM5WZMs7BfrHaGhhv55-cRMOpx2rhC5kfZ7jO-Rxw4QhUVwto8vnbmzqfGtS9mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
مراکش
🇲🇦
-
🇳🇴
نروژ
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
یکشنبه ساعت ۲۲:۳۰
🏟
ورزشگاه ردبول آرنا
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
مراکش در
۱۰
دیدار اخیر خود،
هفت
برد و
سه
تساوی کسب کرده است.
✅
نروژ در
۱۰
دیدار اخیر خود،
هفت
برد و
دو
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر مراکش
۲.۵
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نروژ
۳
.
۸
گل در هر بازی بوده است.
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب:
۱.۲۷
🧠
وقتی از بازی لذت نمی‌برید، متوقف شوید.
R17
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77036" target="_blank">📅 10:50 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سنتکام:
دو پهپاد انتحاری ایرانی را که تهدیدی برای ترافیک دریایی بین‌المللی در تنگه هرمز بودند، سرنگون کرده ایم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/77034" target="_blank">📅 09:53 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77028">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntGETX5y2MoLtf8gP1UCmr9yGA4VeXEJvrImngakp6THxZTJHnr0wUssjo2XexggmZplG1hOK5JTmWZHCUMi7X0iQ0nl49dHOeqO913Ly_n_9Gvgv-rC-cXzaePttwqp7TidkrxdljGHw7NEgmK5Yf0dmBts3IwRmpogcvPvLGWPNIiab9EizDdSSBOpuKvWf7yh2FvJdMugHdKznmWrFGYvePu5o2uva8jr7DQHqmMv6-wKDg-2q6SFqXfmJseuunp_b6oxjjJN5_ZrcS9LAzJhR1ss2FvosFLk_KE7KHx5_styfsDQon-LM-ru_Sy7zkR6FTSSL_8rJY6rKTkxiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش CNN حکومت کوبا شروع به پخش سلاح گرم به شهروندان کوبا کرده و از آنها درخواست کرده برای یک حمله نظامی از سمت آمریکا آماده بشن، حکومت نظامی در پایتخت کوبا برقرار شده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/77028" target="_blank">📅 09:04 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77027">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFR5ix3yzHjp44206KgfO56zGZlXqRGIVG6hDzHmfh10JS4cvHyyEKYV5AYYltLcw5-Goc5W7Ya6_RyIgBwDCq4H-REXas7Eb6tjAXGrTPaeZ_yw9rbNFuJHlC7JQHkOpq-RKV8N8FFKO6z_foBzl_NDI-trY0wLbCw040H2R1kfKN_DZTT8N4dg_vNDhowJnZlpmet23zosZ2suUOHrCZIiReB_CkOLI3byyi9QkJlUiT72_KcCHM26PHqT2Ct6ReM68iirLKoTIPSw9R8zqDgg_VuJ1R4rP6sxvvuqpnShdxEMJd1Dbn6jN68JCTch9K-Xuq5pMZn4hSg4p7em6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب قهرمان جام جهانی هم مشخص شد
از سال ۲۰۱۰ به این ور ea هرچی پیشبینی کرده درست در اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/77027" target="_blank">📅 02:52 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77025">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">درحالی که مذاکره کننده‌های ایرانی می‌گن تا پول بلوکه شده ما رو ندید مذاکره نمی‌کنیم؛
رویترز گزارش داده وزیر خزانه‌داری آمریکا می‌خواد با اون پولا خسارتی که کشورهای منطقه از حملات سپاه دیدن رو براشون جبران کنه و داره طرحش رو بررسی و تدوین می‌کنه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/77025" target="_blank">📅 00:40 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77020">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5uV5XkOYgCH60g51cElI_cPoWStucdUg61MSdFIgl99UwRe2Vk3icRvundPl2w5jLde2bGLewAG13Jqy63vuXqhrmJHIlDD0OlZlxjr39QvS0yRszR9HRAuQu9P6ehmNqskmMFkigg3cxkG6J3dkAsjWIyR85X7vxjMw122mTLzSTmS6JwINtrl3k1AERJvlTovPL9UO3yq9GK7MKMjNjLh3adteIeWTovIR7MuKl5Bhw4LyxGt45IqR3Cureud4gs2VIgA_s9uxBJJCZfuI2tyviYAgB74mP_y3B3pDX1kM18ynz9NvW_bQFX5FnJKr3mGrxQvaTCKisCc2bKwuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر به من بود قانون فضای مجازی استرالیا رو تو ایران اجرا میکردم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77020" target="_blank">📅 00:14 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77018">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p-wwo4kYrwzASI729PdMFCoPcwuPeVbM2EshW3FqR3OpgvEF2Sjwl9-Mk0bHUoD4qn32Lfjd2nKRwxy4gdctFMijFoNKo3YepT5BE9uTPfcBdZc7dPIBLNnkZBeVAHpbvqGe9Z8_VloUAjoWUW6xqIUplEdCreZBhA5KOlLUynPUx3UPr6YFzW31-OdV3La19PE161nwy6CmKpeL-Gv4JlVfSE0STq9CFwZhU1tP7JeR203vwfG9SVz3Wj-pgy0iupxB31fB79KhysewFJ-hvIier5KX8QtxWOnfr0f3x4JCaJERnbFouyIEL57yEfT6FoQxDufQHx3vlB5Rsn6nMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمب جدید از CNN
اسرائیل تعدادی از نیروهای آموزش دیده خودش رو در کشور آذربایجان و در نزدیکی شهرهای شمال غربی ایران مستقر کرده و از سمت دیگه در مناطقی از ایران عملیات مسلح سازی مردم و تغییر رژیم رو در فکر داره
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/77018" target="_blank">📅 00:06 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77017">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">محمدجواد لاریجانی (برادر علی لاریجانی) در صداوسیما:
رفتن قالیباف به اسلام‌آباد غلط و یک هزینه بزرگ بود. ترور رو با ترور متوقف خواهیم کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77017" target="_blank">📅 00:01 · 17 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77016">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJIH1Z23uB4OCTG5Kgntle0DSKAC5xvKB8uXTf9KY2GHa21pmaosqwRLWUVYoKAtK5UWHTqiVnEDOsKOnbnky3aJEKJM-3utE7872ezCWehxex-6Ma3tGFOWn0bmwN3_B6h246sC8aHs6A4XlKp37c6PoKIAa0uQSpQ7_1zDZ7qbd-IrgbnjXpKDNab7f5EsB54uypcQKkBhScgNCvNt9WotKGnvIN_3Py9WK541Rl7bb33bX4n_aUuBF963s_pydl4a8C2O1FMYos7_L7qKw1KMN1zfg7iUcczJ4aQ_u5PKSF0diXLy6pzp5UfslQZ_ylZsww0lXva_JCjyERecxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک عده هم هستن مثل تصویر که تو جریده بهشون میگیم "ملا به ماتحت"
و به وضوح خایه مالانی که وسط باز نیستن
از دسته ی اول بهتر و قابل احترام ترن
درکل چه جاوید نام های دیماه، چه کودکان میناب بچه های همین خاکن که فقط دخترای میناب سپر شدن واسه یک عده، همین.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/77016" target="_blank">📅 23:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77014">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElaxWMjY7aJ33nB98pywHeiI3MNuC_kjjVfEetMig1MJVQ9JQy204plPnDCH7zX90VerWJPaDQAN3NW30Gyo5O97Tx12jIwjIsiwL1n-Sm6SZ2yFQvkFlWvWIPmgnSFfsFlvsaVOChgJydRU2A_2ke1BXVgnG99cj8ivcft9-LlRBup-IWVMrQYq1KKl6vvCM1vggWiOrW00neZVwDpRurI2UqsuYSfH5O7L3wKbguLa7gNOK_HwaUvrVhl2Wh9jvfxwNZt9umdFjlsrR8MFNsbSOPVtpbHIWYa9ssIuei9GJzLLSUc4gJBoI0QBLoVPm-DVNoYEp8rxordOq4wsTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا ایران بوده گرفتنش
یا دیماه اتفاقی واسش افتاده
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77014" target="_blank">📅 23:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77013">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OVhZrxvoS9auRUW699cJAQKxkfjGNjwScs2xlmKlIhrox8QIXtAxSbbL8KJk2crBGCY3Z7h7ofdh8fA7UME_KnlFK4qmvIy8IPjyW1VCSYy_R1TneFOE2z2XZtmixiVxdTk_41ka8JpHPXh0-UDyINwm2RtJ4BTIjOnfKTorh0_sM1JnfQUOutkMvpc3sDb-lRpRRCb3iP8QPQ65eHQ43EXSb24ANF8w_oopD6y2athX_quIZPj-GCPheKWmRq9kq0HFjXZcSdY17enSgz_n9A6-S8rNsNyEirP8IGiYMNp8LGkvMMjN4p90I8PvGhGxxMz5V_ukZohsVDfyrNo2bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست به هیچ عنوان این عکسو باز نکنه.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77013" target="_blank">📅 23:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77012">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IXfnlnoKcRUepbdm5CdpicTmdvIkUOs3ifgrRQiiURqPTbLp_xr0gaz3K8Mh1kr4FdY4x7vtJQP1APUH-ZKdBRnxeXh5CpJjlG4iWZc-JSYzrYZktwmFblWT2P0eSTg9HRpgy7dJQIsXDaltUUpjd9v92SXk8N-QmQRrIntJFGLOo0LOVjbAYHYkyrJ91sanXWOspQdi07zdiUFZwxRtnsZksj_zquwXrc9v1sHcpgjSGn2uF0TfJvce7XqjAipWJkXuy0Z3OCsd_8eRbP8BlK6ya08AP6UseKsbtOGnEYtzUQI4ZFReAvfSGsxaYlwN9nFgFi47owwIjn3UjOmPpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مادرقحبه ها چرا دارن اینجوری تبلیغ میکنن.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77012" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77011">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">app.apk</div>
  <div class="tg-doc-extra">51.3 MB</div>
</div>
<a href="https://t.me/funhiphop/77011" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🆕
اپلیکیشن حرفه ای لنزبت
🤩
۱۰۰٪ بونوس اولین واریز
👏
اپلیکیشن را روی موبایل اندروید خود نصب کنید و بدون نیاز به vpn وارد سایت شوید</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77011" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77010">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIKJ32ckMx8hZ6MMFVTxYCWGx2RCvPEtEjY3fyGriIlH0tTd8uVFNcwJuT827Ev3NuFCpYGxNvERR5iOMYEJJIlRMhBXg6tK5D0fndVr71Vaxmg68Dvl7CmqFlYgp0Jduu_OrbnIIK4981ELuji_KVrRNgtgJuPUHPnBvvd5qVP1brttGrgSFsl9tiP_S56NoZQH2eHTquPiE0PKqEo9QV9yTOMhJexcYRpqrKPmltCEfI1ZLwd-kvjyHq1pJFPSxt4bQYQMPjoDlxlRV6jfwI5HfzSXRlpVHwRr4LsYoRYcJftVsGve9-IVYl2fAEDgK8-AtsmG3xktVb3cRQY4tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
لنزبت بهترین و حرفه ای‌ترین سایت پیشبینی
🔥
🏆
↗️
بالاترین ضرایب و متنوع ترین آپشنهای پیشبینی درلنز بت
↗️
🔣
0️⃣
0️⃣
1️⃣
بونوس برای هر واریز
💳
شارژ کارت به کارت آنلاین و درگاه
🔠
🔠
🔠
🔣
0️⃣
3️⃣
کش بک هفتگی
🧑‍💻
با انواع دیلرهای فارسی زبان
🪙
واریز و برداشت انواع رمز ارزها
💵
💻
همین الان وارد لنزبت شو و از جوایز ویژه ما لذت ببر
g16
🅰
🔠
🔠
🔠
🔠
🔠
🔠
🔠
📱
http://Lenzbet.cloud
📱
https://t.me/lenzbet_official
📱
https://instagram.com/lenzbet_official</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77010" target="_blank">📅 23:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77009">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tbUA5eRZ4rRJvIJHSpaD8ZDN2PXb3BQtb9Pv12ES0d8SkqqH8k5bHACGgEUTr0RkZesHryR-12haGBO1Z4y4S0NoGXZdIaoW98foDH0ddTDMdPSyaJTznxYoxDlPdQvnJtAxhAq8BVTawvMBoa2FpepNxeb3d2GWYgXz5Dg3vOYH3eU05cPt4G2BrLbqc1YMI_wfN0oZBlidm_nEQYYXQZ1MjKlQPu5BIMKALx1IlKu0fGAZHN76JaodsLaXLABoQhPSn8iFURrZx5aQIAjIl5nc7R3oIrnews5HYjHBOSDORC_E04CivsAsKp2lj0jVjHc8a3eC5RXvy1Rs2-4rqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسهال خالص
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/77009" target="_blank">📅 22:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77006">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">خواستم این رو برسونم که اتفاقات خوبی قرار نیست بیوفته
هرچی جک و جنده که تو خارج بودن دارن برمیگردن ایران و طرفدار حکومت میشن
جدای اینا بعضی افراد هم که حکم های سنگینی هم داشتن دارن به بهونه برگشت به آغوش باز ج.ا دارن برمیگردن به ایران
بنظر من همه این داستانا یه تله هست برای کشوندن افراد بزرگتری به ایران برای محاکمشون
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77006" target="_blank">📅 20:28 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77004">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nePZ0Pp1u47V9CVQJ3FSDhMHeUSL4PjRe4Bp_5MOSR_PffrU-OExtsuAvOLs0_wBIiLOMn6MqGGz0DtHpaEotJgqNL-T3aMXM-Hw1y_A4JDbGZRqnkgL4nwBDpoN_m2Jm7PGhYQYNUkXgBlbdYx1CiyznogOiWNrF3DAMstMjzYRDTV_Jot5gTl496-C9lpcR0CAPCLWXovEpEJ3SkkDKX8_JCxRg_VYziHK7o5URWCyJPYX08KswWAPnGFuWDehplLiWNtMm5PMNpC68EyNXIx-T16nhM4IHzm4G3wUVgAnQ_l2hu4E7lMN3CijcS24X6TVXza3fgCNVaE7B3MLTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور میکنید comatozze سالم تر از نیکا فلاحیه؟
ایشون هم اکنون در ایران حضور دارن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77004" target="_blank">📅 20:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77002">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IquPkXqnxeThmd387WwOZ7Unnl3jTh8LT6-Xcr56F1u0KX7licK4onftAfe_mC7nr2ol0j9w93FBPNZ0x14OGmhGT0y-P2I8gm7fxv6KGwGcQyHEte9r4u1CBBSGVA8G4tYDOh3JqS2Zye26EEN6mCPy9gNdUJ_jZR1gSEWegxNKscVA8EZrFgsOc9JOrE_ponltqR_68v7Cf7Kh6k_jXp-wSIUJOv-bd-sJQ3vls6oYJpfO6-bL-UpiQzYDBw9K93yIf-2QaHYE8995QfRNt3astJnWr2YaOcQIVH8hSB1x4hgg_OLxM4843V8sVI3sSYA5v1jBNmNzq2AML1bC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز فرداست دنیا جهانبخت هم برگرده ایران
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/77002" target="_blank">📅 20:20 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77001">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">من بین ویلسون و خلسه "و" رو انتخاب میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77001" target="_blank">📅 20:14 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77000">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی، حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249 تومن
🔥
❤️
لینک ربات
👈
…</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77000" target="_blank">📅 20:10 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76999">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyCMiz67bQOrEvnjixflaaeghcoITrdn9npGqGdRAqmflO7A18hbkSLqcS-odw6CnjCbhcLD03Mtzoe-NKCIbL1hAbM79RjJDYNxt9JlXYTt-G1gOJl95Rcscdwu-glMdvetDePJNuI9SOP-ALqBj9rjbULpBAaY9iH6gYaDUu0TgRadIPy32ADXlX4rjGbfzMfSEX_ccrOT73jN2izaA14eCSlq6PVV43IJPtW-xuTPTS25BqTOjfN2MBzPR73gVP2-cdLJ_7iq7dLEEMjSE9g2Z8Zh0Cacsen6zrp3lw1BjBYBJwJyq-c33i1URZ9WgGWC46SwOrTwCzegaYfIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ارزان شد
🔥
هنوز بابت VPN هزینه‌های نجومی پرداخت می‌کنی؟
🤯
ما اینجاییم تو این شرایط سخت اقتصادی،
حداقل سهم خودمونو انجام بدیم و با قیمت منصفانه
سرویسی پایدار و باکیفیت ارائه بدیم
🇮🇷
❤️
💸
پلن 1 ماهه نامحدود
⚡️
(
✌️
دو ‌کاربره فقط )
❤️
🔥
249
تومن
🔥
❤️
لینک ربات
👈
@Window_VPN_bot
💻
به همرا پشتیبانی قدرتمند WINDOW VPN  تا یک لحظه هم قطع نشی
😉
@window_community
:کانال تلگرام
🛫
پشتیبانی:
@WINDOW_SUPPORT</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76999" target="_blank">📅 20:02 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76998">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=rfdChJC-gVUUVlmnMHiJhdHYG3S033n9lg-CAi4_5AtdRgoTCi7gSF587gbi_anWR-7p0XLcgQXrM9w_ppqvsGuZrX6VvmviwEWdFj083bzvmZOhD7M-Nmz_Qxb5aiU0tJlu0UY-HIkKvNgVtF8kPJnQ7f65kzK7MHrdNl-Uvs4k56hZ0Pu21Oaelqzs_Tw2Y2bEwCCu5uzrRDFfoY7cTVcYCoraLyAcf9zWZH8m6sLSbTYYL_aWiTIfge14d7PvOYAd2cc-eC_9sCkIcHMSvYXb3PDSC4XDSZC5aNx0kyTo_3UklLIoBTHUFqI-WjPrfI-HCf03nOdQkb74DANadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652823ca5.mp4?token=rfdChJC-gVUUVlmnMHiJhdHYG3S033n9lg-CAi4_5AtdRgoTCi7gSF587gbi_anWR-7p0XLcgQXrM9w_ppqvsGuZrX6VvmviwEWdFj083bzvmZOhD7M-Nmz_Qxb5aiU0tJlu0UY-HIkKvNgVtF8kPJnQ7f65kzK7MHrdNl-Uvs4k56hZ0Pu21Oaelqzs_Tw2Y2bEwCCu5uzrRDFfoY7cTVcYCoraLyAcf9zWZH8m6sLSbTYYL_aWiTIfge14d7PvOYAd2cc-eC_9sCkIcHMSvYXb3PDSC4XDSZC5aNx0kyTo_3UklLIoBTHUFqI-WjPrfI-HCf03nOdQkb74DANadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو کامنتا بنویسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76998" target="_blank">📅 19:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76993">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PfQLWu30CK0cZOpenmlCKs8VZv_Q2MdxuioUnLBzkgyankf6kBcF2pKXYCCtXaAB3rA65ouGEQZorpHOb7NlGjHaVUVwJZdWbO0hGlUV33Dm63o1zBmS-zkVmH2egqItW47CBEClcHf9FltCtBo_cQC7glUvUj6P9FEP2SjvSUqB9NYj7KXbVa47V-eVeWnQHiQYXFzTomoqIjbYQsYP4r2z5eijtB9Jaacz7EZmMLdor60TncD5CF0EeaODx6oF3vytfT667byGiBaLmAuIEQv5rZtE3_K70WcljvaPJieVC0Ivu8p_osZWaZWf53FKymBybk38g033lOtJk0NtRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/txl2FoaZUfHcYfuZh8SIYALVLgn1TnO1i_cIw6_oY3j5wf6l5fUgSt7ogNqluaRq7e-fRrJ63AMK3SWjXQRAzFGzrAVE8cf5rKWSuDQIBySPe599_LnZypCiX3sjzLFttEsJKg2FbVAzt1F1hqKtv2HW-9wIfBkc2Sds0geq3Hi1z5mgljWP1fsB9YwTr1QpglW0bh029wLrg0VRPB81Beusz1FpkJyjjeDoNecDJnhTiiEG9zzs_Ehl02eVMNdbZpQsZSho9WhJr05pNIqphpxpn_L4Y0WDa9xjLWu6bssf0TF4F1FUtW-1lUzy84_yWQXIFcKI2OITGSdLQvl-Sw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F836nqfCyqpPP3KiVTzwbZ5vCGomxulwVkZHsJBreoT6EE6sXvbVkLCHf6mSRUB8ecir190XL22F4qOo70Aak2FQv9TbAcs8kR_a1FVn3niegP7S38MRW1fQPTVIH4A3ttxDlAI3uGAgJ3fOP98OpSrcBc-eTA2GBzqgiTLGDNLdKYudaZd9abdJrVl-jVpgHdfsZdsnXCJV0GAYsmPIzj2axA8-Nq0ReWnf2wQJTKNpFOzCcoXVjzl3Z13DisgyIRwVVs24BqYEBJWkscYnlBNIbgZeahWrmzgwYo0rU_siUkVzzBNr_7w6go80GtBmKSnFbYjqsKkXnF79Qakomg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FIxlIgSsIN0680CCI2IlHKegad8StQKdqMTcR0UqmuWnSDmzb3FVAb9sCam_EjTQJUHAzaTV9mT94wJinq4pcCfWQBqdgpJLeqz6WwwMj4eLZCjNc_QASEAOPupMPEwplSIObUKhYpbY5UK9JLiqj0eSdbReQZAGKOIQOJuooeyOwvzXsKgvlYCwPPQBSJbRylswLzUaPlM8Q50HS7MnRsoUf8d8Om42E_SuIl7H-T9efzy0ngsB3frJJoTtR2aGYiy3O6Rf_JqWMhFiZgCAe2q7FpZmcHByVEQt6dVNAqKVzcoDqQ2r2jevakaJ8CZIl3MZjosiBkipJUCdQc2uLg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو آنا د آرماس ببینید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76993" target="_blank">📅 17:56 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76992">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djbjv1kAQ4lVnno_yeKv1KCB2c5WBnc1FTiXQEvu3WadU53u8vNLKuYcMMCTZ4pN73CzhXdXQPjnTleTCsG1QD_n1gPb2MyEFqUcIv1ZXIZBrZ4_71W2CJc1YnY8O4cKy98TDvKDTnY6FDMYsNpo7E_FcpngM4bb3BCXDGDKejpfc1sLdq97CgZ8_ZSxy54FQ2UQ9g04OWKsIxb-w8kiPKUT0THqsC4AdyIpobluSKxGtmecMkosyuZtbLdqDD4EkDv_1LE-1fFYoccsDX1UjC0kLuFXiAcLK9aVEnTiTMd80zY4oYD1ulFe8Z39OvO4bVV189BU8GUw5zqLAJk4Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر خوب برای ممبرای ۱۵ سالمون؛ اسکین وینیسیوس جونیور به بازی فورتنایت اضافه شد، برید عشق کنید
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76992" target="_blank">📅 17:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=BN2VPndrSmM-uEvMK1JA7ikkvCq3_6HftGmlzJ6pZYZv4tplW8JbwS2Kqw8PtZTAK7tMFqAinr18ewfdcuvAsMmvvbjDMkDLcen5ScwLtcEp9quhj1T2bWSW7TtIBM0dsXWvVAkZ7TSH5MgFH4TQsUQ61m-_nkhaXXa6VnVURO-3vk8AnQmq-Np4l1NYe-6Ju6YxSZ_lsm0PWCGLIccJ6bwtLFqAZjqdLxn6tfizP2nqVI2gMb2GTJOTBdCyLqHZPd92iFOR1nAuR0qTZ8ywD1kPjTqK69mx_dhocybzBD6eJptM_ahrPaHDPp4lvM1Aw0YZ_xhgDyR1XkA4VX9EzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/771a0a778a.mp4?token=BN2VPndrSmM-uEvMK1JA7ikkvCq3_6HftGmlzJ6pZYZv4tplW8JbwS2Kqw8PtZTAK7tMFqAinr18ewfdcuvAsMmvvbjDMkDLcen5ScwLtcEp9quhj1T2bWSW7TtIBM0dsXWvVAkZ7TSH5MgFH4TQsUQ61m-_nkhaXXa6VnVURO-3vk8AnQmq-Np4l1NYe-6Ju6YxSZ_lsm0PWCGLIccJ6bwtLFqAZjqdLxn6tfizP2nqVI2gMb2GTJOTBdCyLqHZPd92iFOR1nAuR0qTZ8ywD1kPjTqK69mx_dhocybzBD6eJptM_ahrPaHDPp4lvM1Aw0YZ_xhgDyR1XkA4VX9EzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگ داخلی پارت 2
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76989" target="_blank">📅 17:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خلسه هم آدم جالبیه، به ویلسون میرینه میگه وصلی، بعد همزمان با جی‌جی هنوز رفیقه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76988" target="_blank">📅 17:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">جمهوری اسلامی پاکستان ۲۰ هزار نیروی سرکوبگر به مناطق آزاد جامو و کشمیر جهت سرکوب معترضین ارسال کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76987" target="_blank">📅 16:57 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jtT1HK3Nb-AmGIjR7lXab3dln5EGWpmukToiFNd5uv9n7SoqOCYvO5CejwW878H1FvqmY7YXXQvZkm4qn-5cU6nF9VV5Tvn0Gyjr3sV5f8BDvu_Nxp4bcAzn4Eft34kPoSnapD1jBMPw4OB6BzKUT6D0ic-F7aH8T1CPVozKpu_yXu3jq6cLzSaI4844vmYiQIMnkTS5OzZPD6ghJlMNNqv9vCNEEZw-quVdTZKU989VnAB8EppBIEP0h9hD-2gc0D64snfYT5f2UfcN-DuFZ7tkwAknjmX6QWeE8I8Phf2fgcENiL-BkNFUMTADLdfcuKk-ullaSKxvRhAQFiZm_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز سلام و عرض ادب میخوام یه ذره بی ادب شم تو این ویدیو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76986" target="_blank">📅 16:50 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">او اینقدر بزرگ و قهرمان بود که حتی دشمن خونی او یعنی دونالد ترامپ
اورا "سان آف اِ بیچ" یعنی خورشید ساحل به معنی بینهایت و قدرتمند خطاب میکرد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76985" target="_blank">📅 16:23 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Do8EcIgreMk-KI5dDZbkUZWhsBRS-rdr7roVYP4ShmUTmDv5Ha8rkdCt5LjyBIUYu1TvZ8Zk0nbOc3XEFGKe3LKKDPW-5w5DH21JECrHNK18Jn8oS0EUi1rc3KcR_3A7Zw2dkzLGakr2oXBtg_j8N9tyUo5v9zK2il42xmH712Srxc-CgcyEeHkTxqGv2tlML8fmQegK5o--SHKSmp1c9huMbkmguJJJm6SfyxMOzwjtkHjcq_EU1WizJZTxOXztdkW2s-E8s0MgWZdC0DrJzc6OdeY6idAzPkP4ll_EnE7bEh0K9e9uiiN_GKg2q0yuTLvnNSrorBaXH1IpMQH_uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه زوج اندونزیایی اسم بچه تازه متولد شده‌شون رو "علی خامنه‌ای" گذاشتن.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76984" target="_blank">📅 16:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت از جایی سرویس تهیه کنید که تو نت ملی شدید هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر…</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76983" target="_blank">📅 16:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7sxsTVfC420BXWAshA5ebDdmIZ4xGPk1-6edQ1lKavmFUh7cDdsZ8VnY7Z78xh483Vt6aO34dMlR14e82HqO5C23m7Yt2b9UM54Ym8vYRjdH9uJJ4JrPTmOITsxVZQpfR5CSExsIjZksTspmUhjBthuGE5riERASMF0Lz0fCv3BqnHMfuZEKkYqWc86D1bhrZGigY8Nb0XIX_lGmIMiXrV422Vk0iLiJZLZmsI9ZY_wweGfJwbeWE0acYfIJvOlt06t0rDsHS3RgOtbWG2MapmTVcLBzFKGrdYE0y4RKczQihTVBeLgQivMBUooSHAOacbSQYmqvdr3O4rME2rfSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣
تجربه‌ای متفاوت از اینترنت پرسرعت
از جایی سرویس تهیه کنید که تو نت ملی شدید
هم باشن
🛡
🔺
سرعت بالا و پایدار
🔺
پینگ پایین و ثابت بدون پکت لاس
🔺
مناسب برای استفاده روزمره و حرفه‌ای
🔺
پشتیبانی سریع و همیشگی
🔺
ساب‌لینک برای مدیریت مصرف
⏱
اعتبار یک‌ماهه
🧑‍💻
کاربر نامحدود
🚀
با زرین بدون محدودیت وصل باش
🤖
بات هوشمند
💎
رضایت مشتری
👤
پشتیبانی
📣
کانال
🔸
زرین وی پی ان
🎤
Zarin VPN</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76982" target="_blank">📅 16:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76980">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جام جهانی رقابت بین هافبکا اسپانیا با هافبکا پرتغاله</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76980" target="_blank">📅 15:41 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76979">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">به مناسبت نزدیک بودن جام جهانی خاطره انگیز ترین بازی که تو جام جهانی دیدید و یادتون مونده رو این زیر بگید.
- خودم هفت یک آلمان برزیل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76979" target="_blank">📅 15:31 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76976">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NKncBsgow6ss8Rr-XXI3Gt9xyK_vdBQTkRQW_McaZO9RXnF2c3SPV5-_MlBKvh7th5veWXq999TmZRqqUYGby-XNxrvHSmlU5ffYrTRNcXXfJcQSYMMRW9tAjwt7pEZNXGdPILH-fa9vIZUwpuKtehEkCXo9cNL2xsltPQu6U9Sl0gX3Cr_WOvSfK036wR1qRd3ISt4510j287Bn0-7ts1-aymOaWzxjbUlM9lygcMK51bJv49y1TJyhGS2C-pGncQQ26IQwoSiuZOrF0LIh7znoDnujSxvnqRSBc9mxuPmAA1tBGt-TCqLwfEf8zGgfe5HunF6EIGG4g1lNlh8wOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری جدید امیرحسین قیاسی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76976" target="_blank">📅 14:34 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76975">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76975" target="_blank">📅 14:06 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76974">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بهترین خبر امروز هم اینه که وزیر خارجه پاکستان یه بار دیگه داره میاد تهران قلب بذار بنویس خدایا شکرت
😍
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76974" target="_blank">📅 14:01 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76971">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76971" target="_blank">📅 13:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76967">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WyUOoX4CekKbkhqe_2hedXq0SUkXaOAMl-C3LhoKRJNdWlwPg-A8fYZjusqWfgH9AUZjtCZyOkS2LNwZPP2OxxPVL6BSmLPIOkESAiaRqKPXB9aVFEsOGoz4cEzJjoadzqJxQ7TjFTtd4c0JfxENjTK6-WGfpANfZiz7Fvx4EAyru7S-zrxfVEi2OWXOsgU28e_XD0eLcj0m_r-uJITDNlWqsyRwxOJcCUZn4XyPwSo_gv6pkW4MqV5jIO3HdcU5Wtq6B_2DOe9_VlJYcdyTXNNOUzfZkFNaZKmtmJLGmb6wYJ1i8mF1Ir9WuSkQYH-6So466ymVg6wyK2aFKRjjKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QYCDU3Bz_aaVtK-RQ5BI-laK8MyjjXpdudYCY_QGil-XP2o0xaLK3yKOBaJ2GkhZn8bgadAtQQouENNdHunDVROWynoG9IH9Q_C3hBBN2BGg1BKGl1VTrrW6J2UcPy8kXLbJLMOHbBDr2cL9WMPTd4C2-eEWXLYMINlNJpVESBtDMXo8mENOFWuxRta28qvbT1STISEZogFIvkCL7aOXyVv8g84A01KhWNw1uc8x5bs1Dgz9OMdCNcrpxlDRd7M79f3J4BfSulModR20TXuyXHZHlMFupAtrMp2ezp6lBkXO2U-si6hzYwtnD8jaEy20i59VVC13KPcht6IOq-Y1gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t96Q9F5QuhcJ8U2MZ65UNMRhLPnbJMlsawQ57H93vB0cF9IrHSFv_AUG4a2x7nQOekAclvA5r7wDE1OA9PlqEsCG7UG_A6SuwOw-CugjJwVPOP3G_yTw99iIv6qQGvi2TIjQpryTQbLbD2UTD1w0awmwxWWsEH2GJYH6Xbe0Ks-ma7L4eI5ObfMGr4b9kOKlmTRVL4CDjIoVJ-xIdcIx468l5Fdn4mQ32JM0KJO_FnJNzCgg_ZSzy1u5hHRhNTFtqhspz8QYaFkkCVUKpqb_KsKgzHy2Li6Qqco5KJ2ynuvIDVU5gCxZ4rRUYd5FtHqsaoiFLjXOdWbNA7wk5m14EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G22jstvl889Ilygrh4jPAoWqUzZuj998j4492a1rXmpP2ZjSV5sxdkf_ZxxWylI2mjFTHR33f_Vfkqifws8IP762LPjpxMu-DI6Gly6Be8wMbo94mJnfKGZhhfvse5a6g0O-GxlVgMGWYb4fGw0tpoBB9WpM3bGQ_LVP5iZ0A5PRBpGNBixJZoXz3humo_q-d0eF212UCh_ua9q3ahu3O0fa_HRvceZeLw7kRwDxqAKsEhPVv85VL6CzNZtQMPXekWxIU-qAU6xv_nGXiiUa6DL4ywv8ELx6tcpDU5WJJRMmWAwacWnhSHkzHcYDlab93zX-y2gp3fbgB4EQvRttWw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ادامه در پست بعد.  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76967" target="_blank">📅 13:22 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76966">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZPIpdrRAa0A5z9U03DsA6K8LY-c-8VW9NREu103PY5Vf_NFWf2d5rXAQJ4VRxcec-HkPgs8_Dh_-kgLZr48evHjBI1UfsrX_OD3jR-MuMEF2jgfH18n9O_0NTxxQp0nbJTy-mLUS89S7TlqBFCYgPflU4HliCVKialX98YUB8wNTXd1PFPvRlFF-ZEFbM6WHOQveeJGaF7Jv7TqHmNnpl76VDKUgM58RL81r7jJ7YvTRyQWzVA051Ksxw10m7vNaOy4al9VsfM5a_fWqdNAzJX-Tg7IumEIoqBKH7BLXU1ytr-SImIheXg7Svvft0TPMdjT9sojwV3dUGqfvGWasg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه در پست بعد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76966" target="_blank">📅 13:21 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76965">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAeAgo-YAHTxDbwmnlyblW4PlYbSQSdY35hA8qJLklG2KmoRp6YolGK_t3qXaffHDQlmZLzb2COhlWJOlJtmm1eINeIcIzcP3I-TZPbBy97embUU5mpF3-opqjVVwSayQeoeaPtCWlSmMamg1HluJzZzUBGv3Az76Jt3ZuLEhusji1-yh8GDbcFoUAM4zAQTkRMbNoyEUaewQkbzTTuF-Bk1K_OKqzUg8rQJYKBDDLLIaZXKarKHLAqHjCRH2fbcXbSQTmMGdfvc5Hca710qJIFI8ivP1PHJCZIVcRs1E_S-Ksk80hRdK4bLwSQ8LbFA0_1Lhg-BK3PR_H3EvwVhNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چجوری بیاد تهدید کنه مثل جیسون استاتهام
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76965" target="_blank">📅 13:11 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76964">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76964" target="_blank">📅 12:26 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76959">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">یادش بخیر امتحان شیمی نهایی ما افتاد به قضیه خرس و شهید رئیسی، ۲۰ روز به تعویق افتاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76959" target="_blank">📅 12:19 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76958">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KXyMcOk_Vj3aI4f74ndoWKVXtg8h3RiP8k4McCvT501HuaY5cW51nl9ahyyjk0h5fAA6RcP_Utcx4MikTERzwLcm01oS-bn4-_o4WSKuM7RmetenNg_aMD8Zok_lcWaU-HGje2zxk6h7eUbCAeqG6imOdEhiOGlSRsGaGNI539R9y8bDo4-BjdEGbPSus75rxm5meGlaW1lkHCH9AaMYelxxLGZZQKT5XsymmeJNOzZEdFb88Af5ZTcCHLqH2Mc0U4CvuZyHxgWZ71KYWZkelsS0EftAuc2VPf5JkZBSLAbtajBfVa9nB9MNCirW2spq0UVpgHYTbe33vjuW97qVBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگم وسط این اعتراضات مسالمت آمیزتون چرا کِل عروسی میکشید  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76958" target="_blank">📅 12:16 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76957">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=Z-sVO8FDbC8gnfGsSSD9PoXakXwrbM3gZZ2kUEf71-9ZhMIGCBOmTl3OriLW4FmCpRqndxbHb0OyDGHAsFsWNeApbUIh2WGUNTXn4nF5qGDldlP7hAl1SyJ64BwkKCta_PvK7eTOGTqIOYbzaG6qt-Q1LXdfNAv6npT1aBl3V8yhnYIyLIvGbAZXV1u3mgb1qa7M_hRpY9EeG1l1OcC9t13ISdfSzNfAcYJ84nns_lrd0HzQmfO7xuv7Ogsm8JiUeGPvuLQK0O1umBSSE-obn44Ufe-P96Kwx4BVUNdw0dBN0AcjtEPQGzEtJCT02Z9hOGme5H_7AamE0Zi3LATTpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69ce83d7ab.mp4?token=Z-sVO8FDbC8gnfGsSSD9PoXakXwrbM3gZZ2kUEf71-9ZhMIGCBOmTl3OriLW4FmCpRqndxbHb0OyDGHAsFsWNeApbUIh2WGUNTXn4nF5qGDldlP7hAl1SyJ64BwkKCta_PvK7eTOGTqIOYbzaG6qt-Q1LXdfNAv6npT1aBl3V8yhnYIyLIvGbAZXV1u3mgb1qa7M_hRpY9EeG1l1OcC9t13ISdfSzNfAcYJ84nns_lrd0HzQmfO7xuv7Ogsm8JiUeGPvuLQK0O1umBSSE-obn44Ufe-P96Kwx4BVUNdw0dBN0AcjtEPQGzEtJCT02Z9hOGme5H_7AamE0Zi3LATTpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم نصف پسرا برا دختر بازی رفتن  @FuunHipHop | ALI</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76957" target="_blank">📅 12:13 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76954">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">فنای اسپرز بیایید بالا میخوام بخندم بهتون</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76954" target="_blank">📅 11:43 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76953">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نت بلاکس: اینترنت پاکستان داره قطع میشه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76953" target="_blank">📅 11:12 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76952">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVrqSQ1OEHIx6zdEpInD2YNbLz5QbuRYyxmhhlzM2eNb8iy9f8yA9tnSQ0d7TQ0qn4inu5hVPUzS6F8DXhtSy_RA8mlGNJC9v3vKGSylJQklwdVS7jYT8AodJts3Ro-sFjhEAhVWqgCoxaH_soaol2d2CPJuLBq6sodN1DYh4zQ4HM9FEc-lCf67uGIiqABB_tijAxEZwtf_rLeQPUyv5Gk4dcsiB7wb8iB7E2qkpmUo7TV5ctsi3MA_c7gvyzaBORlWU3Yw-T9_ZqHzbAGlxyRMNAai4cQK5B5fyhwjGj2APwhblhi5NfA_N2wSEPpKo7E99wJ7Il6UPivmJJQh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیشنهاد میکنم سریال جدید اسپایدر نوآر با بازی نیکولاس کیج رو حتما ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76952" target="_blank">📅 10:32 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76951">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شایعه شده که خولیان آلوارز رباط داده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76951" target="_blank">📅 10:08 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76950">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NO0Zi9b1ypFk8ipjClfUgj8Oy0nOudtlib8-jFx6-2QkMYe9J88W9mTUO7ZL17RtQVoTMVRoJuGbnnxvM5e7o68A_a_C6bIgKnZ5LrdZClkUqIVIfmVZImdKBPiXIvNcFp_grKwy6kW6XhMPUNpMqNypOClJkFAsW4hKMTWe1aPkqL2AbZDaxsVi7wmQ0dCzk65Krnqc89vdeFAxvCF3qd-msjFsBfs5Ocn9Lz9x1rnWN1S0S9slbRBPVeTk61MWP4Oc-7H-crdo6mEHu1epzu6l-bv9qUF6gUZYKsVSYk2MeAN_o8niXb093OLRH7sZTgqdWOTv24a5mo6c7u9ZSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانو : رک و پوست کنده بهتون بگم، ناصر کیرشم دست پرز نمیده چه برسه به ویتینیا و نوس، پرز رفته دنبال جذب اولیسه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76950" target="_blank">📅 09:15 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76948">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DsXr1bzN_DIV9Ah58eqJK0G14BOEZK5UGY58zJO7FhCVMgv-yrWK6fmMYYrPTEd1exhjQZDzpeD5rIousUlcvsaLqJt9oIQcG7ZChOGfLcuXCfE_txb5kXJg_rXftvDU7ycVpD1s-w-GSc0FyDnkPcpBUaodrM7DDthDwKiR-aGGBjV9qRyJxqlT_BFGjDz_i9QBxAwuP_xbOP_LcUzDPI2v9UeVb0QcCoNPaPJtZIa-PUemooKi1FMxnN2s-sTndpzl6w2sY6oKqDRGWid_J--pnotJ5JSpy5OMc2XPqSgq-weBA8BZxjaijATpjzKEZQMHrOe7IWsSKKvnD-cvOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hj9a5OzRw8JQHFIuzDSz0s123ZX5D4dYXc3w2K0o-l1x7RM0QSRm9U3EE0fobv8ahKdtJN8YXwkDrpgIVXKy4YAJGRbE41gR56B3F39cM4qj3-ds3dyyxGUiHqTJ0qMiTDO5bb60FaPk8ep3sitDYQy40Yz1JgJhJNsXAiXMoOvRFNGgYqTuUelHQtd7BkYQuWHjeVaeju8Qt-m_4VyXHa0AWuE5C2hYbX4x3f3dNOMr4tLkwgymPhfgFMNP0DzESfWLhtZg9n4YFODb3-8s-nBnVM3e6CRmXGA-g17qu_LpX9oIbynKHorAAMO8wuw5iST3l8tXEsicIbMLDD0ing.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76948" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76947">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esmkalCp4IjzExUAPULI_WrL5txVu_PwHJsfZeabvxbdkZhUazECTa3llrPD45-LcHEFfsfZV6w6jWwaRXJp6oRtqUUulCphepdMDbn7Ekda7UUsXu8S2HlRRFbwRvhqO8a6SGy_cAYcZdms8HBYfVOQQf6tUePNClPfV8iFxrcWxPTsz39E9adhlMXfBScjdRYiHBBC06VRj-odaBC-lDsVWp56VwdDHQ9d54zz_MEv-bX5fALK24noNIOnlPoLYlR0-fWK5aG1gfu-HNFufiig845e1WV8ZakIR1zEp7EM9Mc1JdUJW3f2xQTc2YMQMQI5lh0kKhol72MT3mWz-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
برزیل
🇧🇷
-
🇪🇬
مصر
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
بامداد یکشنبه ساعت ۰۱:۳۰
🏟
ورزشگاه کلیولند براونز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
برزیل در
۱۰
دیدار اخیر خود،
شش
برد و
یک
تساوی کسب کرده و در
سه
بازی شکست خورده است.
✅
مصر در
۱۰
دیدار اخیر خود،
پنج
برد و
چهار
تساوی کسب کرده و در
یک
بازی شکست خورده است.
📈
میانگین گل در
۱۰
دیدار اخیر برزیل
۳.۴
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر مصر
۱
.
۹
گل در هر بازی بوده
🎯
پیشنهاد پیش‌بینی: مجموع گل‌ها: بیشتر از
۱.۵
- ضریب :
۱.۱۹
🧠
اگر مجبور به پنهان‌کاری شدید، مسیر اشتباه است.
R16
🅰
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76947" target="_blank">📅 09:00 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76946">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">روابط عمومی کل سپاه :
بسم الله القاصم الجبارین
فمن اعتدا علیکم فاعتدوا علیه بمثل معتدی علیکم
ساعت ۰۱.۳۰ بامداد امروز چهار فروند نفتکش متخلف با تحریک و هدایت ارتش متجاوز آمریکا بدون هماهنگی و بدون توجه به اخطارهای مقرر نیروی دریایی سپاه، قصد خروج غیر قانونی از تنگه هرمز را داشتند که پس از اخطار، یکی از نفتکش ها مورد هدف واقع شده و متوقف شد و دیگر شناورها متخلف به عقب برگشتند.
به دنبال این واقعه ساعت دو، پهپادهای آمریکایی یک دکل مخابراتی در قشم و یک دکل را در سیریک مورد اصابت دو پرتابه قرار دادند. در پاسخ به تجاوز ارتش کودک کش آمریکا بلافاصله دو پایگاه هوایی آمریکا در کویت به نامهای علی‌السالم و تاسیسات مهم باقی مانده در ناوگان پنجم نیروی دریایی آمریکا در بحرین هدف آتش موشک‌های بالستیک نیروی هوافضای سپاه واقع شدند.
به دشمن متجاوز و کودک‌کش اخطار می‌کنیم در صورت تکرار این شرارت‌ها به پاسخ محدود اکتفا نخواهد شد. مسئول عواقب بسته شدن کامل تنگه هرمز به روی خروج نفت و گاز شما خواهید بود.
و ما النصر الا من عند الله العزیز الحکیم
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76946" target="_blank">📅 07:07 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76945">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76945" target="_blank">📅 03:59 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76944">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/76944" target="_blank">📅 01:52 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76943">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">باز شب شد آمریکا جزایر رو تصرف کرد سپاه هم آبراهام لینکلن رو غرق کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/76943" target="_blank">📅 01:05 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76941">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الجزیره:
15 نفر از اعضای تیم رژیم جمهوری اسلامی واسه جام جهانی ویزا نگرفتند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76941" target="_blank">📅 00:38 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76939">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DojJvHqk_LHpnWAZqP0gLKyQ5_hjOjpE_e0Z3dsvEhw_odTHGzLaHcH9JZjSrKFW1jH6q8S4vBOgxbQsWZ4sZ1s7Abe4rzf9GlYwjDTrjttqxIwhIp2gUHlDMRcIEYNVY-rM1KmcZyapY_VQ4idue8l_lBWqZqjivw6V6IJL9B1AIdF-LR2DbbgWmpndFm5BxMLXzHc8fOISB5JdxuGO6lvrgwzWhQVAxaTTapY6urn0qFKIuY949E3d2txcy8Bc7MY15vCveJtqIpQjfZ9ZZFvU_IeJ61EOyTexxlx4Z_gh0VOrgqEMOvpOhz9oz1LdCjaGW74VXuT9pNN5RVzDlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6dzAghvympOXqjWnPsohay7ajuOGYNRIOnRnH7S64IIgXiFMhCI5C5PdU50q4c4nH9sSi4pg0wGg-As5MrNOUI-01wxDwOERQ8IJPgsBdNBpDKprSMka6WEd1u0rWd0KWBTswo0q-Zj-tE6AqMzes7RZlQ3zA7ptUui7W_TkRsk1BUjRD0QMchjuTQvIPm4KL84ZEQn7cHX5eDV9peEckVl5B_ul_OPZaYMBTdIzPTN6Fc9V6HQ4VLcyC75Rhw3_WqF2SydJDqqOK7o-_pslmF5jmIdNesxH2gza-FBBFMxGJ_3oQSekkrfED7YcjpdzBnYvc2dcoTMN6r_YeuFtg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ناو هواپیمابر نیروی دریایی آمریکا(لینکلن یا بوش) دیروز در خلیج عمان و در فاصله حدود 280 کیلومتری از سواحل ایران دیده شده.
در مقایسه با موقعیت مکانی این ناو در چندروز گذشته
این ناو 50 کیلومتر به سواحل ایران نزدیک تر شده
!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76939" target="_blank">📅 00:18 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76937">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=Ik8vz-w2zt9eLWn6HMq5oiKGFPSu_9BnslKxPQCe6GilBBinS0La-VwtTgQimS1p8WuD-GVHuzmPH-a_KxTnnWZeBre0Qi-I0nnldbT27xZz3Z6Szji736DpPgwkkE-LSkDOMyPVIkQcoxw_CPrewh-umqnZvLuvX7_blX_B5bnOKsazXPZ28WNxyh7hybKve64Z78eXOnNqZIjoyc-UrQRzNjxTgyBTF2aBRSa_ctqNd9mT20labR-AwPK8YR_2vGVbE3YKh5UuLeBt5qvxOTppMCO2_hiDXFGaAo6XriagMfBP2ZfooTNeFHEmVxzWFOh5sJtlxRowmblUT-88WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4adf695bc9.mp4?token=Ik8vz-w2zt9eLWn6HMq5oiKGFPSu_9BnslKxPQCe6GilBBinS0La-VwtTgQimS1p8WuD-GVHuzmPH-a_KxTnnWZeBre0Qi-I0nnldbT27xZz3Z6Szji736DpPgwkkE-LSkDOMyPVIkQcoxw_CPrewh-umqnZvLuvX7_blX_B5bnOKsazXPZ28WNxyh7hybKve64Z78eXOnNqZIjoyc-UrQRzNjxTgyBTF2aBRSa_ctqNd9mT20labR-AwPK8YR_2vGVbE3YKh5UuLeBt5qvxOTppMCO2_hiDXFGaAo6XriagMfBP2ZfooTNeFHEmVxzWFOh5sJtlxRowmblUT-88WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنظرم جی دی ونس  گزینه بهتریه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76937" target="_blank">📅 00:09 · 16 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76935">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ی سریا میگن یوتیوب رو نت مخابرات بدون وی پی ان بالا میاد، تست کنید ببینید واقعیه یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76935" target="_blank">📅 23:56 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76934">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3980333f44.mp4?token=h4XeXJBnIkuIexkUv_jtbq4rBih3sLrENyVUvyOW2qfa1CNj0WaNxGCBTWbY3yKlMRaLqub-1RsM-dmAPq5WEdLM5rw-9wCFLAwseJrLEGNsVEqRFR_uFIJCPUNBP4xeoTSqsCSZC-8fPiu9XqqoSmJxtXVMIKNib43fqa8sH45h79D7xmeP2FogaQrhQMvcRH6btJJPdJAqpSxXZ2ebhKb6MEwM0nlMz7nKm9u3E2A_N46KxE7Lx7NlzbNNxFLWsACYtU6jfQHwepXIfZF__8SbcnNUICLbNtFUEudA0mx9xVpyoSn9uxOdpoxaUE9VvztylTWD4v6Q6pDcGtdHxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3980333f44.mp4?token=h4XeXJBnIkuIexkUv_jtbq4rBih3sLrENyVUvyOW2qfa1CNj0WaNxGCBTWbY3yKlMRaLqub-1RsM-dmAPq5WEdLM5rw-9wCFLAwseJrLEGNsVEqRFR_uFIJCPUNBP4xeoTSqsCSZC-8fPiu9XqqoSmJxtXVMIKNib43fqa8sH45h79D7xmeP2FogaQrhQMvcRH6btJJPdJAqpSxXZ2ebhKb6MEwM0nlMz7nKm9u3E2A_N46KxE7Lx7NlzbNNxFLWsACYtU6jfQHwepXIfZF__8SbcnNUICLbNtFUEudA0mx9xVpyoSn9uxOdpoxaUE9VvztylTWD4v6Q6pDcGtdHxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موزیک ویدیوی شکیرای مناطق محروم (زن مورایس) برای جام جهانی هم منتشر شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76934" target="_blank">📅 23:08 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76933">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مهدی ترابی بگا رفته و احتمالا جام جهانی رو از دست بده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76933" target="_blank">📅 23:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76932">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">آکسیوس:
به حضرت عباس قسم مذاکرات یه جوری خفن داره پیش می‌ره که پشمام پسر.
نشونه‌های عجیب و غریب مثبتی از ایران دریافت کردیم و مذاکرات به شدت سازنده شده.
ویتکاف امروز رفته بود با کارشناسای هسته‌ای آمریکا صحبت کرده بود تا ببینه شرایط نگه‌داری اورانیوم ایران تو آمریکا قراره چه شکلی باشه و آمریکا یه تیم خفن ۱۰۰ نفره از کارشناسا هم تشکیل داده که این کار رو بکنن.
ما به شدت به توافق نزدیکیم جوری که اختلافای الان رو می‌شه تو نصف روز حل کرد مثلا آمریکا می‌گه بعد از توافق باید تو ۶۰ روز مذاکرات بعدی رو جمع کنیم ولی ایران می‌گه نه ما ۹۰ روز وقت می‌خوایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76932" target="_blank">📅 22:37 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76931">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خبرنگار:
فینال NBA که قراره بری تماشا کنی، ارزون‌ترین بلیت اون حدود ۸ هزار دلاره. خیلی از مردم عادی آمریکا توان خرید چنین بلیت‌هایی رو ندارن.
ترامپ:
خب، می‌تونن از تلویزیون نگاه کنن. دیدنش از تلویزیون مجانیه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76931" target="_blank">📅 22:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76928">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه  عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76928" target="_blank">📅 21:54 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76927">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">لطفا اسراییل رو با هسته ای بزنید دهن این قمار باز رو ببندید
ترامپ:
ما در برابر ایران موفقیت‌های بزرگی کسب کرده‌ایم. آنها در موقعیتی نیستند که سلاح هسته‌ای داشته باشند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76927" target="_blank">📅 21:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76926">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">واقعا فاز اینایی که میگن جنگ بخاطر جام جهانی متوقف شده رو نمیفهمم انتظار ندارید ترامپ بخاطر تیم ملی ایران که ویزای ساعتی بهشون داده بیاد جنگ رو توی خاورمیانه که تموم بازیکناش کصخلن , متوقف کنه
عملیات اگه انجام بدن تو خاورمیانه قراره رخ بده نه وسط زمین فوتبال جام جهانی تو آمریکا
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76926" target="_blank">📅 21:48 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76925">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/76925" target="_blank">📅 20:39 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76923">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">برنامه سیاست با علی و تحلیل اتفاقات منطقه در طی 24 ساعت اخیر
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/76923" target="_blank">📅 20:30 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76922">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">طی 24 ساعت آینده جنگ میشه اگه نشد هفته بعد این پیام رو دوباره بخونید
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/76922" target="_blank">📅 20:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76918">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">این از دکترمون
اون از دلو که فتیش زیر بغل دختر داره
اون از داریوش فتیش عرق پا و بدن دخترو داره
اون از حصین که فتیش بی غیرتی داره
من کیرم تو حوزه ی فعالیتمون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/76918" target="_blank">📅 20:15 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76917">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmirhaz</strong></div>
<div class="tg-text">بیاین بهم پس بدین وطنمو
چهار ماهه آزگاره نخوردم پای همسرمو</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/76917" target="_blank">📅 20:04 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76916">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">مامان شام درست نکن نمیایم خونه
ما عادت داریم شصت همو بخوریم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76916" target="_blank">📅 20:01 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76914">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره. پیدا کنید پرتقال فروش را  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76914" target="_blank">📅 19:52 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76913">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gC7WqESz1ma_8g6MP80AsnBbMI2GOmzQeUFlssgNN5_Ubn9PXHCFdaznoE88x-RBzFuG6OGN-OB5JdsBWk2pbFfzPKb2yareJ1B9P7-4N7kStMvxuPRu_m6q6utEaqw5wHqlJ4Eln1z8uK2OczQWpBIxrhEjRmJcFIgMbzTBLsnMvR-0fsKD0LEZzHBnSFsXZdSdY33SobCNnXMXEZquUZ4PLkX_KyGAbCWRhMRrIcMKlxy8xCrazccDfbBdpWuAtLe6avUM70jVSPVlcC0vXgSkloYleSq6PffLn099NWnXXX5LWqNM_VWSIlXMB6wYp3ZTNOpEEwRPuHkZ2RPNow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از روی عشق و حال پا میخوره، یکی مثل توماج توی زندان نیروهای جمهوری اسلامی مجبورش میکنن که بخوره.
پیدا کنید پرتقال فروش را
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76913" target="_blank">📅 19:50 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76912">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دکی: برید پیج گوچی مین محتوای خوبی برا پا دوستا میزاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76912" target="_blank">📅 19:41 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76911">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=U0pdSna71NANMfy7MJ4trFoR9voFfcXpKj24dYJ7YEy3aVPrz8lHEFAY7d28ZLQ70uOkSoG9ktPPt_rJBtS5FkMn6jtoI5ZTekZPuCGp49LfXPhqemFyJ-ECsG5uhjmMrfj3GkpVCFhBqKpfnCUPy59cuYHRN-1MXQb7tkklo0qx2t5aPdp9ydM2DeDBV9yzn_2ufdTEbMJYnnVjNYSjlnwqWwKSi38WFtRgNOPLe4i3bw3OPxys51NqNF45VPzVtrvmKLtGNrHkqoDaLC0I0yf_3_aBqlnpX4PrUm96A-5Ueipa1z3ydOzAZzMwG0VqOnKgpj57WZsIMh1cTEpVHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bb569f0ca.mp4?token=U0pdSna71NANMfy7MJ4trFoR9voFfcXpKj24dYJ7YEy3aVPrz8lHEFAY7d28ZLQ70uOkSoG9ktPPt_rJBtS5FkMn6jtoI5ZTekZPuCGp49LfXPhqemFyJ-ECsG5uhjmMrfj3GkpVCFhBqKpfnCUPy59cuYHRN-1MXQb7tkklo0qx2t5aPdp9ydM2DeDBV9yzn_2ufdTEbMJYnnVjNYSjlnwqWwKSi38WFtRgNOPLe4i3bw3OPxys51NqNF45VPzVtrvmKLtGNrHkqoDaLC0I0yf_3_aBqlnpX4PrUm96A-5Ueipa1z3ydOzAZzMwG0VqOnKgpj57WZsIMh1cTEpVHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop | AmooFirooz</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76911" target="_blank">📅 19:40 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76910">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kIS12FnPlT-pPLfnCLaqIXBQb3BD7zxAKRr7D7chQwVnAApU90ZvqXkvOnfsaebndyIzfhHtoRsliMvLYEwJs9A3NtfJSfsHsfa_dUDEODF1UjI_XOlQSfRh063imLV4piLY42iyXOmqfqDqqiMzHohkbHNTCt6uqh6pPkGYe98CHC1-hVjI5eM8oyXBeG1D-ri8NCx4sBc4hXhIq5bhoeJexEdJuRABYpukjetziAka5G22bdZWOgnEeCIi8haZbPSc6xcnm5yfsJ1QWjcCTFRHMBk0QZ0qxo4aFGokpeDocVqiEuv6K8cCj4EgPWnxFNDCP-MRcSEHe1TmfGtw0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بمیرم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76910" target="_blank">📅 19:25 · 15 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76909">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGjy68hTebEjTUA6GavsH3HCoCcVGSp5XgZ3U-tc0l6brJaIQzQvdRB2QbYWflFAqP1BYCaBLqPZOHkv-6JlZw0l2xZ66lQpmv2YaAmA1bosoZ2wirWpbzwjQa9gQoXobYYjnfF4oUx9J_0n8LQLnru1780Wpqfza-pWdOzskxv7d6KOy6BnfUk-TCSf-vKe8btGUAfEgHlxYA0DNp1zEc-YKHHRbcKIlqJYZJ0N8BNFnzjxLjnKtyyoroTPT-2fFqNcQKukaVNTHdD88Juo7fQqOi3iWjAA0KDNVUctazpdEVVqRbHsOUDCmmPCRaxPBV8FIwLWNXO-JJM5GrX9XA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی واسطه بخر
۱۰ گیگ ۱۸۰
🚨
۲۰ گیگ ۲۸۰
🚨
۳۰ گیگ ۳۸۰
🚨
۴۰ گیگ ۴۸۰
🚨
۵۰ گیگ ۵۸۰
🚨
با ارائه کد تخفیف hiphop  تخفیف ۱۰٪ بگیرید
سرعت بالا و لینک ساب اختصاصی
📩
همین الان پیام بده
🔤
@wevpn_admin
🦄</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76909" target="_blank">📅 19:11 · 15 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
