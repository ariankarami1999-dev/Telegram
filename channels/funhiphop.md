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
<img src="https://cdn4.telesco.pe/file/krBPw61ew_PFULRIPrGTKWXpJLL8Evj049T7u27wr83IlK_F-a1Z6xU-duDDJzLhLMnC4d1QN6PJXc7oA3A__MTaNwHJM6EwI9nLrXksWjQxSz5Ier5VHebf8ndT7Qk10SFp_FwVv7WgT6NOcxZZOgAKpk9TWGvPT7Dug7X8Bvt8tffxK1A1LiO81Ggup9J96-QDu1wRwSsV-5wxy_181hpt8s1V8KUoCDrQEQYVUmLHI6z__gIWOMo-qvWHDNxF9VjDOeJTk3VudOCPR78xXA_kZitHoaIur_D0deqH1R7B50k7FqMDDGo4YjAFD2kHC_Eng6FesKxKrkof9qNFpg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 265K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-17 18:54:21</div>
<hr>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">دولت آمریکا در حال رایزنی با پاکستان و ترکیه برای بستن تمام مسیرهای زمینی ورود و خروج از ایرانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.04K · <a href="https://t.me/funhiphop/84637" target="_blank">📅 17:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">خدابنده‌لو چقد شبیه رودری بازی میکنه</div>
<div class="tg-footer">👁️ 5.55K · <a href="https://t.me/funhiphop/84636" target="_blank">📅 17:42 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">گزارش‌های اولیه از کشته‌شدن معاون اجتماعی انتظامی استان در پی انفجار مین کنار جاده‌ای علیه خودروی نیروهای انتظامی در منطقه چشمه‌زیارت زاهدان حکایت دارد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.93K · <a href="https://t.me/funhiphop/84635" target="_blank">📅 16:59 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">میرسلیم، عضو مجمع تشخیص مصلحت نظام : تیبا در سطح ماشینای معروف خارجیه و به راحتی می‌تونه باهاشون رقابت کنه.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/84634" target="_blank">📅 16:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/84633" target="_blank">📅 15:45 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/84632" target="_blank">📅 14:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tcOpXALEgHs99FJ_Y1ySmXiYWNDDW6XUJOY-dHRz3qnlFjuWYvPkcVy9nLiTPdCBebrFWJaMaMB6sS99kQrnYbMULXjvm5Vw9l86ZVAWZEht5CjTNeYhY7Nm9UX31EaxfqX_3rCmNOVZnE6zps3tVpWPxaOKCQW3VXChMz7qK9BELng0G6_26__BhiKN1bm_AYfOadIUfwfndx1zCuDWGgVLwW2m6w7GArv_XK1WognT2iXoNlJb7Vjpf5FHw3crcXMUY8cWc5cY-qNHMW_boH5mX820T2ymNCo_ftIMuO39VMzi3llc5BO9BZEbieGHGNIHVvEW9Skl38W-4Wi-oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشالا حاج اقا
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84631" target="_blank">📅 13:17 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84630" target="_blank">📅 12:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">سر همین اصلا به مشکل خوردن، پیشرو زنگ زده بود به هیچکس گفته بود داداش مالزی کنسرت دارم، هیچکس گفته بود خوش بگذره داداش</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84629" target="_blank">📅 12:39 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/84628" target="_blank">📅 12:36 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromᴀᴍɪɴ.</strong></div>
<div class="tg-text">من اینو صب دیدم سریع رد کردم گفتم ای آیه</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84627" target="_blank">📅 12:35 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WA82f1gYdI_pbnu0uRe3ddPxJ7S4QSZ9J3p2jZGmRMgL6lb8XIwyjMbMPRpsEG91-tHwqjldBl3usmE9M_hpc0NxHL1qqMnlvpnqisrPmhNfHFWPptxPmXM_5o1igZjNhn5eKIBzEqoYXxMzx5LkJsN9To8EMzCyyel7KemBA10UOwNFWPvq4xchnaoDPtX5yuQp3tz5s9A-qfq2Pt07kkjRRd7VXpj_ngSLJICHQJ8mQRs8zwBpIQ-GCj90NKDs9LTGxJ1lGcbu-hK_onzfimdXKm8Wyy1SKYrrYMdV533Ty7k-e935VCaaMkYEC4PFwtAAynXYSOLV6p3XsMY6DA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا فک کن فیت بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84626" target="_blank">📅 12:29 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">هالند و امباپه تعویض بشن بین سیتی و رئال جفتشون بهترین تیمای جهان میشن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84625" target="_blank">📅 11:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VP8aXjeM-xsRO4exImFRHW20LeI7wFUHi7ZgxK1BKj6_ItGySkkzoTR1nKqQypU3dJrfEsSMYfjEujenFT-KwhlpdkoT9fHBJ8HbKQivXZoVt7_sYZvLnrKnaP5znWUYbzbK8Sfg4yhlh7VPwGuAM9ThoUUiYCkTOtObKfXlrnAL-mr2u_TOvsLvd_HsYToOkog7UiiXm4OjqgSgdh-Q6ZrSP_DzWIdDkigUnU_2s0ZPi1-TBJxk7G1IADMEu-uCm12ltXwA7apax3BZCs5qrm1-vOcOfPmCqNP6tRZlRO9YxShUCXd5caILLzH0ohXIMi9eI6zqERistawcblD2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس داستانای کیلیان دیکتاتور حقیقت داره پسر
آاس :
امباپه توی رئال هیچ رفیق صمیمی‌ای نداره و اون توی رختکن رئال احساس غریبه بودن میکنه. با بلینگهام بینشون یه جور تنش و سردی وجود داره، با وینیسیوس هم رفیق نیست و با بقیه بازیکنا هم رابطه‌شون بیشتر در حد کار و فوتبال حرفه‌ایه. حتی از بازیکنایی که قبلاً باهاشون صمیمی بود هم کم‌کم داره فاصله میگیره، کلا تو تیم کسی با امباپه حال نمیکنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84624" target="_blank">📅 11:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gv_v5HBHOEOfVWV8PLZKLhv-Yy5jq1uJKND5ouqgPb4Obd-qKk4wr6xgH2IzGP1ONtVL9I7Udsgy9dYvTP79tMQzmbasWQiY3H7QBnp2mJyH5RAQae4HZ54hHRaKS_caCEYMhdKaVlhN3gHCpTEa7h-d87PQ94HRe_pTZYg8-Zmd23lKmm-UuzPTz4ETZquU0ZYpRnK1TlumFHkoihL0CRN3tq1bfaBe81U6z_PUIyNdcPVvIGuVM2UZaUhzkYHJbvkqbh3aNJBTtXOhFNYKAKOx8JjMzIjrsmaxekgh5jbjJS4FK9GYwPThVTNJv06z05XKAKOZJ06lg9N5hPMDxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مستند تک قسمته ۲ دقیقه ای(یک دقیقش تبلیغاته)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84623" target="_blank">📅 11:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">عراقچی پالس های مثبت از مذاکره با آمریکا داده، شیشه هاتونو ضربدری چسب بزنید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84622" target="_blank">📅 10:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ویچرت؛ تحلیلگر معروف آمریکا در توییترش: اسرائیل دقیقا قبل از‌ انتخابات آمریکا به ایران حمله میکند. این پست رو‌ ذخیره کنید.
پ.ن: این یه بارم گفته بود آمریکا لحظات آخر جنگ ۴۰ روزه میخواسته به ایران بمب اتم بزنه که ایران میفهمه و مذاکره کردن رو میپذیره، قبل از شروع جنگ ۱۲ روزه ام میگفت دیر یا زود یه جنگی بین ایران و اسرائیل اتفاق میوفته
پ.ن۲: آیزنکوت رقیب نتانیاهو در انتخابات اسرائیل هم دقیقا همچین حرفی زده دیشب
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84621" target="_blank">📅 10:20 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">من جای تهی بودم دیسای قدیمی پیشرو و هیچکس به هم دیگه رو جلوشون پلی میکردم و از واکنشاشون فیلم میگرفتم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84620" target="_blank">📅 09:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NdnI0OIHBI8UpH1-Y5zycyGsEW-dWdII0J7ebhxOoXgsU9C8VtzH1n51pEtn47UVo-QHU75Sev43p0uWr0lA595X3rjlYwlAdm6SiX97xEE83lAR0L3YG5anTQ6NP8zmsNyXME2lHvGPgsgmYEiT0R0yQ5SJS8eVQTusTWztNdhaouPBZjH0Ld4Wz4PSdR3kAlspYu4SjqAYbuZZIbTc5kFuZb-Pi7MCjixEFV8b2IYWLR6-kkpDaK17wUnaT2DTLpMONXuMw0OHM7iuG16HhTI3ByWdgGEvxkO1MAqhdM8MiBqIxiLG--e1I9t0R2fVK9f8romO60OtthyNLHVkvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی کیر تو روزی که با این تصویر شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84619" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84618" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XhkjmO6zOxVqq0aydU-vVvkJyUQ4GKZmp5utzDQ4xF-BfuWK9acjscaIWl4v6k9NRA5zGiscCcRkHEktu1pUqwiZmuyxR7uXt18Swvmyr6URjO8uyIgZ5z4-RQWrMM8UIfkUNWNk3CJSyYbgufTOzja2VqU6HYGOz7U0R3VVugmXy1Pi4NV80VSGArQnhWGvX4Ch2ioBSjO9mn_rF5sMV2P_0YlDsvxS1nO4K86nR1rEciUwbteeG5VNVlQVDlPPvW8CIMiv5lVzFlkSSy_YZtHdYXFU-e399HIuwd8dZ9eygoMLROVK-3wKclh156czlf7xIDM5vCkRsha4V1mwVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
پرسپولیس - صنعت نفت ابادان
🌎
ساعت 17:00
⚽️
چادرملو اردکان  - خیبر خرم‌آباد
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r17
🔗
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84617" target="_blank">📅 09:48 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a66d8a6ead.mp4?token=IGfg7_tiaUeP87fVUgp7jguPkrgyfZhZvUjBn7KWMOjZFUTWYf87C8g6JIt6FqqSktvFcmNocPbJYKJyVfZ31x1SCEAtjtu_3mZY3TksdHhgDWGtjvWi8Zz3Rgcdfc6q9CY9sD0bIId01AqOJsqABvD6OHYNlRxXxpDG4Jmj9k-4HVLyqjjmuX8kbAUVboQDNZWJt6om0fOU3mfRj3fa9gAGtn9VjNlnvhw3cJ4cFPhIdng_CnBONQQ8ni_bmtshEb6TqoH8pyFG5r2RBzrT-HmebKNBxOqbb4zCRgRDByFfnXCQ_7p77_4763wFcv5XqIbl3WpQHfa1s0jUkfEFdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و تهی رفتن لندن که سروش هیچکس رو از نزدیک زیارت کنن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84616" target="_blank">📅 02:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84615">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aTk2kT5msKJfjH_DtoQuoRHHRx0KU9pQTfYt6KeuXnr4gJCQqwxWrDgBIeQCmPZlk7f903cKTK40EsQe417OMPbCnAXDR4p6NGFFA8HS5KoVBPUWwXp4Go_N_oJ5iNY-j14OS067KPI-1qQZenaQzhzDvNyA9ctGgYFisQ0lWXvKPDwDxtqaNYz9mEc6oTEvyKeY2rMK5jbFvg6aMdZD0blmyQg5thic8F_7zo5s2PPXRtYBq22LjX3aa-3ZlPhqztdKdx6tXn5yn4UatvpKgUkaDoh3zoOve4lP_XrqHxm3RUc-1cJRrq0QEBTgURZB3awbpZS8DTc-A4qkni4mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هنوز شیوع طاعون تایید نشده؛ تو ایران شروع کردن ماسکش رو میفروشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84615" target="_blank">📅 00:40 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84614">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سپاه به اربیل عراق حمله کرد، احتمالا هدف مقر کرد ها بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84614" target="_blank">📅 23:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">اجرای جدید هیپهاپولوژیست
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/84613" target="_blank">📅 22:53 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=jejYIefj2M0umNekX-g2M8EOoZFmcwM3oirBG5cwSUE_1-1pvvwGgzxK3uSF8SVfyGxJqYatF9fKvFNAGZfk-LGLm9xfS8BmDiopMDlZQczb6WZNdmtmhNMh0oDYHrQU0rmSQKX09wCaGhYJHHfYERvbm8Q213YjVB1qDpFdwIAGkOxaVxwp34petsq5BNL3-uvwy7uibD29hCUPir0FGABplgBCSH99bPjwp_oZ7QL9KkJEyYzxHz2FdQH-0eZy6VUqBGc3klvHGph1Ls07YGUUB8ScQzkAn6ibgIlUk4grHliIm2WExxsU-wdieY4MThIG1nRt33EwBchvmtqbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d16fa565c7.mp4?token=jejYIefj2M0umNekX-g2M8EOoZFmcwM3oirBG5cwSUE_1-1pvvwGgzxK3uSF8SVfyGxJqYatF9fKvFNAGZfk-LGLm9xfS8BmDiopMDlZQczb6WZNdmtmhNMh0oDYHrQU0rmSQKX09wCaGhYJHHfYERvbm8Q213YjVB1qDpFdwIAGkOxaVxwp34petsq5BNL3-uvwy7uibD29hCUPir0FGABplgBCSH99bPjwp_oZ7QL9KkJEyYzxHz2FdQH-0eZy6VUqBGc3klvHGph1Ls07YGUUB8ScQzkAn6ibgIlUk4grHliIm2WExxsU-wdieY4MThIG1nRt33EwBchvmtqbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوجی انانوبی بازیکن بسکتبال+۲۱۰ سانتی نیویورک نیکس رفته دایرکت یه دختر ۱۲۰ سانتی و میگه بیا ببرمت نیویورک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84612" target="_blank">📅 22:14 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=kYEZ34SvwKkr9QnoSDH_YqPct0E0i99I1wlxFih5991F-5O4-vYwydUvItxvOA0myLr6ChS2jCP2B_gCGVl9qRC7KkF0Aij9RJUt37HVIxpypBzPEPghgd5qUYMsmvo9InmMkX2OdRq9hA19OWHtqvQc-DjZCO7REjKp_0mOalL8mDWBe9jo4JpVtg1xOcZ933APTWOBuFwTkwFZ0QOV2ygVtGHsfAbzR9MfMWBPhPpbCzAyzR95gHiH5djZCRuV1paFBZ9OsyMsh8Mbc4EvihReM87hBzHGV_bRWsSqTZhN9xX6gyybFV9HGv63xmrM4FGjh_FffDnEn3q59vo0pQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49025c86d2.mp4?token=kYEZ34SvwKkr9QnoSDH_YqPct0E0i99I1wlxFih5991F-5O4-vYwydUvItxvOA0myLr6ChS2jCP2B_gCGVl9qRC7KkF0Aij9RJUt37HVIxpypBzPEPghgd5qUYMsmvo9InmMkX2OdRq9hA19OWHtqvQc-DjZCO7REjKp_0mOalL8mDWBe9jo4JpVtg1xOcZ933APTWOBuFwTkwFZ0QOV2ygVtGHsfAbzR9MfMWBPhPpbCzAyzR95gHiH5djZCRuV1paFBZ9OsyMsh8Mbc4EvihReM87hBzHGV_bRWsSqTZhN9xX6gyybFV9HGv63xmrM4FGjh_FffDnEn3q59vo0pQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سرقت غذا تو یکی از فست فودی های کشور:
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84611" target="_blank">📅 21:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=F8OrgrsL8RWYQhwl7F3gq-Bc5w5Oy7SyEWHyP9WLk_E00YSRqnKxf3asV5LAdIOiPPEML-bnQYrotjyA2fugm4IM8m8XLZYXyUbLiEMDGQM4UDmh40e_Y_P1w5_hSrYPu8wIM1lwvpbw86N2AG4e21N7Xx4j-hGWPm0qT21AWoIj9QPzQ20FZFiynf_pJJaJGqoUiA5UAPplH0KQGytNrMjIXN6pvbBSts0GFWjSh9hJR9NR9-xFuIAQ9GnpK9Fx1mn9OqcXNr6PzHBORzVZ3jUTfxQXWbrHdrfjyl1SEm1HTUitXHJCQ048XQoq6Y3KVIl3NEPQ0qdycUlnsqPBDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f08a78a31e.mp4?token=F8OrgrsL8RWYQhwl7F3gq-Bc5w5Oy7SyEWHyP9WLk_E00YSRqnKxf3asV5LAdIOiPPEML-bnQYrotjyA2fugm4IM8m8XLZYXyUbLiEMDGQM4UDmh40e_Y_P1w5_hSrYPu8wIM1lwvpbw86N2AG4e21N7Xx4j-hGWPm0qT21AWoIj9QPzQ20FZFiynf_pJJaJGqoUiA5UAPplH0KQGytNrMjIXN6pvbBSts0GFWjSh9hJR9NR9-xFuIAQ9GnpK9Fx1mn9OqcXNr6PzHBORzVZ3jUTfxQXWbrHdrfjyl1SEm1HTUitXHJCQ048XQoq6Y3KVIl3NEPQ0qdycUlnsqPBDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من هیچ کاری به این که رئیس بانک مرکزی ایران به وزیر خزانه داری آمریکا سه روز وقت میده و این که دقیقا برای چی وقت میده ندارم.
ولی چرا میگه ۳ روز بعد با دست ۴ نشون میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84610" target="_blank">📅 21:36 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=JdBJ916dgpGRmzgO8J7qj43r1lEoE-t8O2MTywWvOxjm3Zaq3olZ0SE9HFUEU5eIAGxl8ZvTlTCXBZZKdon4YLQiwRL063Y-PvMwFKHvZR209e-1AjyG9om5ngQktj88E1GlBpG_JmxjoNcX4XLKko55jikkDJqVXgQj8fA8Kt7uGl663JmWf03-LSZDPnUQtCeLRdFCEYGEF340JP1FyR0_9ZQ80zK7SGeAnbk3pYquCB3S8FS0exCmI3ouFt3eB4-ppWH4xofKdtm7xsKrGyQaqaF87ixQw2lTuUlsFIiMov4BOH0ihemgHQ9Geiwe3ZhJXohR2D4UnI7C8s3fTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23d8dc7bfe.mp4?token=JdBJ916dgpGRmzgO8J7qj43r1lEoE-t8O2MTywWvOxjm3Zaq3olZ0SE9HFUEU5eIAGxl8ZvTlTCXBZZKdon4YLQiwRL063Y-PvMwFKHvZR209e-1AjyG9om5ngQktj88E1GlBpG_JmxjoNcX4XLKko55jikkDJqVXgQj8fA8Kt7uGl663JmWf03-LSZDPnUQtCeLRdFCEYGEF340JP1FyR0_9ZQ80zK7SGeAnbk3pYquCB3S8FS0exCmI3ouFt3eB4-ppWH4xofKdtm7xsKrGyQaqaF87ixQw2lTuUlsFIiMov4BOH0ihemgHQ9Geiwe3ZhJXohR2D4UnI7C8s3fTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد.
از این به بعد در سراسر کشور، با خانم‌های بی‌حجاب برخورد و براشون جرم ثبت میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84609" target="_blank">📅 20:52 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBa7yb-eidrbqcjlFDotr1DvHV8VreplPo0e5kucyudUJJun7fHWWgau2EG1cKKBjjkQxtG7iLWPQCDXhbEFsj3zBVXUJ1f3iVcOZo34mVv0H5JRaWOmC8k56DR844DpcmnrsbAi80suK1w4jRKBTFArGbRYhRgBF1fc5qW7qh--mKQbE1AliorhV9AzHfLAppGs5N6ElP_hfTWist-KtQTF8uB_4pDmFfJ14OuClKPAHbw9kgyXlGpgQYglSU5etZWgXsamYxYTvH6-m52OjvbLQBR8IKb16PjaekKEzfb5wYscyIv-2rJ8jtafvv7s2tYsgLtDSUjQW41O-qH36w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین الان پاشید یه جوری شیشه‌هاتون رو چسب بزنید که ذخایر چسب کشور تموم شه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84607" target="_blank">📅 20:27 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cROmw-aciwy-ePFYYoWjgqNWN2a3dDvA1GENVC09M6y8ggQpOESaerRB8wSU5OPcHmMPSHVwWf7SPLYYnWi8o9j1-fIdpkjuspRE4dgehrSlNRAfdk81Sk6P491E2Fki8Jf1C317CW-qqa3ES9I9CPhMOYZ0iL_GRmHZ-DHhfu0IPuhAKqSFU7enlrt7LIPu5PHJZawFU_nDYzQvEiNMJmMfj4s9TRhn_qHmWJZzCgNcoJHBcyVOi6hevtcXL_q5zAOVu3xCeIs5ihoSgI8iPrB42AWX-zkFIeJ5GcN3cAsQFNw1wqrI3hWdaqwQAW-VE9F8IOmX78ZaHVRdnErx6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خخخ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84606" target="_blank">📅 20:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V194LHTEz7q-rf_nSEJ-CjsqR2EtFRIdQaZmQL00x3RsIB3bC2sxqvKdBTFm4r2bZ4GnPTp755Lmie5Ml7Zg-44sD2h6oSya4jqXBMs1SD0DH3-se-QEWjh7voZ8rFLk3BdMHuMCERTAkHzHxZ5soqOLamKcFnVJ42MXrxdvYg-8Pfs6EeeR7z7axaqTVKqJXxBuK0GA8KdailWzSqXml8kJD_ew4dZmw89dwcUzI0X0A5xy_PwUCm8tDaf-4eRfMGQ0_ZMzYswivnvXbJCI9C1uVqcDSaZbZP1x10qd_hq5E2voPpcew7XVQPvh6a8TWIaOMLUiplzSmfRnf6wECA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توماج صالحی با رپر بسیجی‌ای که شبا تو تجمعات اجرا می‌کنه درگیر شده.
(به نظرم رپره داره حق پسر ایرانمون رو می‌خوره
💔
)
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84604" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=UE7rZbQcMHYCnZND4eU2vPHesbrfm1dhN7eAdpLNi4ns3EHS7mN7B7A5hth2IbZpfvV2Va3lgjraltzXkZIGdHRHwlGrn6z4wvQ6DqUQkV4OzGFUt6k7sGDnHpzY2v_iACjwCKyFxP8-XkgEGmIKRcWHP-nR6C2cgboHO5BW1m0qRtw5GSxvZEXGyPIyyxeFVwd8mGeldjbIe23WK1KwQYTHTbS2S3h7OzwxI6IMGy_vdBvpd9__B2a6K1T9ia-EGoAmzFL-_Xvvw1YTvDR6VOP2tbkvGqFfUw0plkxPznM5aMdzW25sAl0kII0mVAz6pXFn5NDMTGIo_z_1QEkQ1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://yewirkxojf.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g16
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84603" target="_blank">📅 19:44 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=AnmjVZQns0p7SfAmfbwPd4-sOOIc3qHQxTCMDRFk-F5UyffV-89T-_udk7nTu7MgWE1aeyzU9v8rIWqJhpgqe8zIMcij7FbTu-OtfDvy2ZtZpE_A7LNCPJ1pdD4-HkuzlV0rGj3_R-vdiUQmTLs2s68bNRCDkvDTeeo48Mcn8WXTVfAsOQUqdW7b9fWhues0bujlwN-w9FBFvZDztLOcCsiR3MJN-R_0D4Z4Ad5ogqqGs3c6cOVAvIJujpDp0aqC0_e-h5MfxQWAhGjw5RuGOAbDGYkGBPsUrHdGjf2ulCWUqWs6uaVPHj6U5R41HnNJ8z9h76RF1SD5gFb-oYYMtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50ebbea01a.mp4?token=AnmjVZQns0p7SfAmfbwPd4-sOOIc3qHQxTCMDRFk-F5UyffV-89T-_udk7nTu7MgWE1aeyzU9v8rIWqJhpgqe8zIMcij7FbTu-OtfDvy2ZtZpE_A7LNCPJ1pdD4-HkuzlV0rGj3_R-vdiUQmTLs2s68bNRCDkvDTeeo48Mcn8WXTVfAsOQUqdW7b9fWhues0bujlwN-w9FBFvZDztLOcCsiR3MJN-R_0D4Z4Ad5ogqqGs3c6cOVAvIJujpDp0aqC0_e-h5MfxQWAhGjw5RuGOAbDGYkGBPsUrHdGjf2ulCWUqWs6uaVPHj6U5R41HnNJ8z9h76RF1SD5gFb-oYYMtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی رشت رعد و برق جوری میخوره به دکل برق فشار قوی انگار که زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84602" target="_blank">📅 19:28 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">با اعلام رسمی سخنگوی قوه قضائیه، بی‌حجابی رسما جرم اعلام شد!
از این به بعد در سراسر کشور، با خانمای بی‌حجاب برخورد و براشون جرم ثبت میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84601" target="_blank">📅 18:59 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">هوا الان یجوریه که همه تو خیابون فکر میکنن شخصیت اصلی داستانن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84600" target="_blank">📅 17:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">حالا من که میگم استقلال یکی زده به تراکتور، ولی ناموسا فوتبال ایران دیدن نداره</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84599" target="_blank">📅 17:37 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84597" target="_blank">📅 16:46 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">محسن زنگنه: قراره 110 هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84596" target="_blank">📅 16:43 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c055QUKmKMVSBmgEEaf7rYsApZf76gCi2if5N8rRx8u_OzWRy6A-2wU5xW1YoRTXyb-PO9Kr3v3eC6Z3Cs6cirjaBjAId20y-Q68975aC7JmnoKRREsDUqPSZS3wWgVbPLfWrd-iv8YvfMBBhwNDLszcb_W_fLXG10VEmvWdDCHBLeFP0A-Lpu6W8oIP9_BiPnZfLXQZbU7ANvD2aSsikqfWqO-wXrD6Z3owHYUHYLZVhVmQcgvxc99YyUP9TlS5uiacz8woT_Inq1hm9V4hZGQd1cnR7kgjC7NAk349xZGKATkzscSJgRbMqjZ1WvaAWqByAy_Ztl7y8iK30u_X3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر دلو فوت کرده
خدابیامرزه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84595" target="_blank">📅 15:29 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DFDUwgPMpfh-wrCPcled7o88aA9Wv1b6eigpeHkJ_ZDiBngNU-ELU09ttmJtVYySyTAVpGiu_trim_W8rXpxCIczBIzTy3yMqOBwTMbeu1YeQ1E2po9aalJcg5CN4BOEXZII82axtgp8-JrKYFnv7rblWD791zFYeLSuqG1zIf8x1lyT5oc6v41xUENdHDAniaw0hyFluoM4Gibq2Tp1vx309SchusQvUfy3OCztEk2EfAG1DRn587NfDekX3w6ATyULCx_wFiCerM6PUClyRy2YnyxsOnFjySYSCS_cVwuZAf37VvphAk5TzAilW-A8yDWkXeC8HdZd4FW7EJ983Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ps88fi6nOBJnCbaSL0vo8R6Py375yMSKs8H8tzeQn0lv-WiojGVn3b6FYb3Dl509-NhyIdh6tuQDDS_jw49DAnBo-7jJNVUxUNxvwIUiJxE5y-_DTQyze-UETQ1cjWcOgRXDUq0XagkB3RA-vobgMYz5vfC9-6isCPGronzqyxyrFnsLG2m0gaYBkn2J3K3AAfIwcO18HsriryU-7GM54TibG1vqDNJcxRrHnQt5I5Z1p8l9uVltbbvCEd2lhImKWARpoJq1Sa2WKyDVNt2kh07cuhAx4KG34ZDVBTEiR4w9IyhQoQCPU3z4qdPulL8nzuYkV9wHIuYUEfmtaLeaSA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشتی ریدی که
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84593" target="_blank">📅 15:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مجری صداوسیما:
گاو که دلار نمی‌خورد، پس چرا شیر گران می‌شود؟
کارشناس:
اتفاقاً گاوها هم دلار می‌خورند
عالیه پسر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84592" target="_blank">📅 15:10 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=EEFS9JZRylHMRMsV8XFGdgpE-PbxbXYDguLm0-5nndZWlfzGUDKyXsWRT2cRDrVPv62pi_KFGbBRtTd4BZoDkYufZmKEo-eH68rdYSvJcBkC3zM9B4AEnI26kq-Uvo9YTsVewjbeU9DiuSRkoFPze_-zH33IQNhvYqZB-DlgyYEa3PRmQwyBD8VMctqccbrxvqqDb-Brj1GwxuOmtZtKKi6tYG8gjcmRSpzKznSuJO88t9vJC3AztB4qFtPu0u1a-rqj9dEVl8bGEA1ChriBHNXSSfStwLry0IhtnqoplSY-DvChC6LnL-jVDEuuB0gNLTq0dw4uhCEDREsgcn0MXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/cac1e3571f.mp4?token=EEFS9JZRylHMRMsV8XFGdgpE-PbxbXYDguLm0-5nndZWlfzGUDKyXsWRT2cRDrVPv62pi_KFGbBRtTd4BZoDkYufZmKEo-eH68rdYSvJcBkC3zM9B4AEnI26kq-Uvo9YTsVewjbeU9DiuSRkoFPze_-zH33IQNhvYqZB-DlgyYEa3PRmQwyBD8VMctqccbrxvqqDb-Brj1GwxuOmtZtKKi6tYG8gjcmRSpzKznSuJO88t9vJC3AztB4qFtPu0u1a-rqj9dEVl8bGEA1ChriBHNXSSfStwLry0IhtnqoplSY-DvChC6LnL-jVDEuuB0gNLTq0dw4uhCEDREsgcn0MXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امروز، ۱۶ مهر؛ روز بزرگداشت داریوش بزرگ، شاهنشاهی که نامش با شکوه و اقتدار ایران هخامنشی گره خورده
👑
داریوش بزرگ در سال ۵۲۲ پیش از میلاد به تخت نشست؛ در حالی که شاهنشاهی هخامنشی درگیر شورش‌های گسترده‌ای از ماد و بابل تا پارس، ایلام و ارمنستان بود. او طبق کتیبه بیستون، طی ۱۹ نبرد مدعیان سلطنت و شورشیان رو شکست داد و دوباره یکپارچگی شاهنشاهی رو برقرار کرد.
در دوران داریوش بزرگ، قلمرو هخامنشی از شرق تا حوالی دره سند و از غرب تا تراکیه و بخش‌هایی از بالکان گسترش پیدا کرد. او همچنین فرمان ساخت تخت‌جمشید رو صادر کرد؛ یکی از ماندگارترین نمادهای تمدن ایران باستان.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84591" target="_blank">📅 14:30 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیویورک تایمز:
پاکستان به کمپین نظامی عربستان سعودی علیه حوثی‌ها در یمن پیوسته است.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84590" target="_blank">📅 13:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خیلی دوس دارم صبحتونو با درو دافایی که تو اینستا دابسمش میگیرن شروع کنم ولی اکسپلورم کلا شده کچالویی که باباش داره مسافرت و بهش پول داده تا ۲ سال دیگه برگرده ببینه با پول چیکار کرده</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84589" target="_blank">📅 12:31 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JRbq2eYTJ2DbZ3HeMyI0tD5zfT8GGiER-erUnQPjLSCJad7HwbBrnl1nHae4hmeWZXovs6wOaaGbX_8G62VFBK_SCfB2Y74pEeLoi6Kpy1tV36NyJnKk7tDdrY31CUAsz1R5YSOISxZ1GcopBnYi0CU4fqW2qmJNV9W7zx6ockTzrVMwZEiBieSi9sPBDoLr5Z9UENld8HuFR9ucnC_ZqFJX1MQsmfukbMIS74FKcZUskt8j1boquAuyt_kP8ofMdGtOVEgOy9dfgW2rLefLotQwdgYPL-OA4pBeYSnoSH3rNrcJmlNIBuj4QZTUqFGnZwv_jRjroHl3wpX9G10bQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84588" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">همین حالا ثبت‌ نام کنید و از بونوس های جدید ما لذت ببرید
💵
🛍
👆</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/84587" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AC_Dy4TGeZE8-ntwpjm_z3LTPsInuGDTJt9G4D--M-81V79MKf6wPgnuBhDxbKgtyDEu7ufRq3DebaRaXGM2d4-F4cliRaZ3KWfxnxwor3EmnVMAdldkj25o_5P7YujmNm9AfHpVHKLsV0Bm4pfUG-584ccP04hG_JQK96L5IoafkmWIVheCaP7WKc1DQK8idWpbMRDVTaBwgqHI89y0-aHep0ku9mPuiUdHNhb9oEJoGdc4e262DVC5NrQ-6svHrGhEGsHI3fOKX1m5il07FXI169N28AwKknIXzvSA2jwSqqMKVeWyE8xQdbm5tq1NiWrRPeJTfSqOZCj8MgaOZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
آلومینیوم اراک  - ملوان
🌎
ساعت 16:00
⚽️
گل گهر سیرجان  - استقلال خوزستان
🌎
ساعت 16:45
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:r16
🅰
🔗
https://bhdyfhicoas.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84586" target="_blank">📅 12:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84585">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">خیلیا تو بندر صدای انفجار شنیدن حالا معلوم نیست چی ترکیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84585" target="_blank">📅 09:22 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84584">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">وحید جان بیدار شو، زدن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84584" target="_blank">📅 09:21 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84583">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4894c49154.mp4?token=uLQzyYw56anYZPOHHqo8MkZhQLJdaSYo-I8ryORM0gNjrsPQOylxRNe71xtiPonyWy2kNpGSI0w7YuDK4tKEkd0kBxFqgMTo6yXMMjCq_ulyR-81JccJDFu9t5HLWvk3jnZpA3GcOAJVFwMNhWHBkQHWV9zfaT4AvH6W9iOhjkZIkrCarx1dg3iQyJDIL7FtW0fUS6gFoBmMr5nze20_ikG4tRVLPPn7C2nv4SDkDj3bPLRwJjsICsr_H_juUAQ1ynWhpie81EqwRfZv0V_6HVHq9gZ2w7V5G6hWT26YLrnSrJHpEftwNzlm_3kCBrf-c5DUn03WHXEvzeMX43e5fA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4894c49154.mp4?token=uLQzyYw56anYZPOHHqo8MkZhQLJdaSYo-I8ryORM0gNjrsPQOylxRNe71xtiPonyWy2kNpGSI0w7YuDK4tKEkd0kBxFqgMTo6yXMMjCq_ulyR-81JccJDFu9t5HLWvk3jnZpA3GcOAJVFwMNhWHBkQHWV9zfaT4AvH6W9iOhjkZIkrCarx1dg3iQyJDIL7FtW0fUS6gFoBmMr5nze20_ikG4tRVLPPn7C2nv4SDkDj3bPLRwJjsICsr_H_juUAQ1ynWhpie81EqwRfZv0V_6HVHq9gZ2w7V5G6hWT26YLrnSrJHpEftwNzlm_3kCBrf-c5DUn03WHXEvzeMX43e5fA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">+ آقای زنوزی پولاشو از کجا اورده؟
- آذربایجان ستار خان و باقرخان داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84583" target="_blank">📅 09:18 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84582">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jSTQu5AlbDZgvqoDkptfLoL6c5hQ1MPaGWxi1q7bUGWK0T7N4tuzQ-ZF6YaMSZRTSGGQcWOEMqfMmQjSThnBSRrSyY_-2fMkyUh9QORbo0EMurJEsBYUDe4PRV0ctsA1fCoZeQ7cLS2Q2XjYmmf1UK24VsjYMO96z19QBy_Dhk7i2rsxG-HLUplcvVxh-aZ2I-309SKhzvuFn__AtUxCUM6GcEYdWLZJbqnZlnR0-AAOd4WI366z8Xk3swV_37vG1HDOSTQabOysZZEy4s3pNL-j2ZGJB5xFtiT8pN1-mTTAc2JVxfKn96fQAIYz3MVlFgWl8GYkRvSQSQWzMEGcIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاوه گویی رسانه‌ی جعلی آکسیوس:
مقامات جنایتکار پنتاگون به سنت‌کام دستور دادن تا آماده بشن برای حمله‌ی مجدد به خاک مقدس جمهوری اسلامی ایران قبل از انتخابات میان‌دوره‌ای آمریکا.
همچنین دو مقام اسرائیلی گفتند که احتمال حمله‌ی پیش‌دستانه‌ی سپاه بسیار بالاست، زیرا آنها دوبار دچار غافلگیری شده‌اند و دوست ندارند این غافلگیر شدن برای بار سوم هم اتفاق بیافتد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84582" target="_blank">📅 03:09 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84581">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید  Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84581" target="_blank">📅 01:51 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84580">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">یه ۶ تا ترک کنسلی و انریلیز از تیجی لیک شده، اگه علاقه به گوش دادنش دارید چنل آرشیو گذاشتم برید گوش بدید
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84580" target="_blank">📅 00:50 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84579">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دوستان زیاد دنبال موضوع فعالیت این چنل نباشید، هرچیزی جالب باشه یا حتی جالب نباشه رو میزاریم ما
هدف ما راحتی شماست که مجبور نباشید چندتا چنل جوین باشید</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84579" target="_blank">📅 00:15 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84578">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">رسما جنگ زمینیه
افراد مسلح ناشناس با شلیک راکت آرپی‌جی و تیراندازی با سلاح‌های سبک و نیمه‌سنگین، مقر فرماندهی انتظامی جالق در شهرستان گلشن را هدف قرار دادند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84578" target="_blank">📅 00:00 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84576">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=JKj0TWXlV1ielIEVVEUrRCn8KIPex2N8xSLGkdj0QrKZSo3WAKGyaKnyL32e90wRk59Vj2G8guynSc_HPA5Kt9yIJkYap-gwIbJ2lT5bDJyuJuJq2Q5A8HNa-J1ZlawDgtGQRH0pxvawWOiIAijcl8k6D47Qor_OBqAegAIVT6zLr08t2BcBCj0AmyiKHiML-4hCTCrTJFkHn6YO26FOLbvWPiy_wD4YbAmJv0b-jhhcfBXKLZ_pCMw9Zk6TX13Fmwt40hB3KeykcW3XyMkmmO8Qrpl-qT7MVcIj9J5yCYjL6xY23VfrWxndN9xDEPld3-3I8W1NlRWb6gHxdVqRqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/015c4e30e6.mp4?token=JKj0TWXlV1ielIEVVEUrRCn8KIPex2N8xSLGkdj0QrKZSo3WAKGyaKnyL32e90wRk59Vj2G8guynSc_HPA5Kt9yIJkYap-gwIbJ2lT5bDJyuJuJq2Q5A8HNa-J1ZlawDgtGQRH0pxvawWOiIAijcl8k6D47Qor_OBqAegAIVT6zLr08t2BcBCj0AmyiKHiML-4hCTCrTJFkHn6YO26FOLbvWPiy_wD4YbAmJv0b-jhhcfBXKLZ_pCMw9Zk6TX13Fmwt40hB3KeykcW3XyMkmmO8Qrpl-qT7MVcIj9J5yCYjL6xY23VfrWxndN9xDEPld3-3I8W1NlRWb6gHxdVqRqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی قیاسی رو با تیر متوقف کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/84576" target="_blank">📅 23:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XLRA7jMjd35RlRp0_WR1vacZN7JFj-pyRfUNn5CeAcJuhAHIsuCGf0_FqZxIpeU__LixFO7xlnwXKwwwfHCgIrNGl3xhvm9r1JMk3-KZdR64M2LGuWTLrADbAgJJlNB9A1sWq3Pmxgntcs7100i4nlDJY15epBVXOS7DGfEMnXj0DPXN9bBVR_vKQ6VYUT5n69jCNUTbLHu92HHdK_ETSD5vuocI_G6JE0ggVel2hQtsQOiymNeJXRSwnGGxMTISRj1cNtV2HYjnQdUkKCdFFtgn4mPvsxW0UXOsBc0ZZyDyAT3t8jugKgxJ1S5PgE2ZtfpWdJcc2cnsqYyqn5r6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYXGaxPA-Xzc-sC3l4xbUlL5Ky-OuugwHgv6kYUEm4yV1qDg5CB7FOBWAEYW9fxTuIQfk3miZadB74Lszt75vOOqTxIcf5bZEHDiQZAI87SEhLKdku0AzBtnV2TfvcKOTFJISsWGt9e-tfMPo-6n01GVft04rzzP3EKViC3tiyJz-JxvrzC7JUHS7rFPfqFZzpU4OZwl0bnrNw18n6NX1TpwIhJugr-FrfoDE0XQ-y-bnWY8KZJmfuHnzj2SFMBSlycveD_AcJBp06uYpjNOFF_5GQDXgFqpBjOdk2ttUUn3GjD_SxD-n0ieg5kYCbx86MNmTCLhn_JfK5y91w99Zg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاگان و ادرویت دوباره افتادن به جون هم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84574" target="_blank">📅 23:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝐒𝐡𝐚𝐲𝐚𝐧</strong></div>
<div class="tg-text">بلندگو هاشون خوب نبوده</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84573" target="_blank">📅 23:06 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=LzR0kTuYdhtDSJJlO6jQq6M4I2kbK0j1gXrRH53ZtX6MTsBMDLLyAU0n6iwMlSqpUh6MsJrOxaYGh_6mkhCyZwEUn1iM7_9-cLVjdONcaqfP872BQHB5QrfnqpNhvxNlujwAN1hqWpPMB0QSHohJbBjdRn0_EqrmMFohiEMlreYjAQP8EMoUpPx85-325nrbAQX29IW9E1jLObMA4jxkfAIt38dkiLaM82gLcN7XekF9o59S5txHNvIgUSBBoSRSNDzI4GLQxbHJsKWUS4_By4jEBRJnegtk1c19rcE5W1CpnU2ipgXZ1jFIZfmZpZJm_XowJRn60uPPKBi8IL377w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af3a994e34.mp4?token=LzR0kTuYdhtDSJJlO6jQq6M4I2kbK0j1gXrRH53ZtX6MTsBMDLLyAU0n6iwMlSqpUh6MsJrOxaYGh_6mkhCyZwEUn1iM7_9-cLVjdONcaqfP872BQHB5QrfnqpNhvxNlujwAN1hqWpPMB0QSHohJbBjdRn0_EqrmMFohiEMlreYjAQP8EMoUpPx85-325nrbAQX29IW9E1jLObMA4jxkfAIt38dkiLaM82gLcN7XekF9o59S5txHNvIgUSBBoSRSNDzI4GLQxbHJsKWUS4_By4jEBRJnegtk1c19rcE5W1CpnU2ipgXZ1jFIZfmZpZJm_XowJRn60uPPKBi8IL377w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84572" target="_blank">📅 23:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d35a289765.mp4?token=L1yOw2OOGBGanY49KeRY1rIkcgOdWwsayailPtx876iEI748RkE8A8Lsh_8x-8k1bunyFoL7-nY6Zh3Laqc0hYdsB91WUJ7P7pSQ2NqlbTbNfyw3qZATpVYTfMd4hW6UkndZf9P743vbpA2bLHrI_UHBHJHr6J8PIaK3b6nsk5ePEoK9S8x4iu2VgYn0o75WE2uDL7ue5-KIKnlhvSxlNDf_dOoulgxQDJGeJeRYi8yKmVkL8jShvhXZIvxO-wXRDtcBUfNUUSOG6JrvGM6Nc4VdwlqEG-6S-YDDzLg29mbz-1nB1sFtXCNQ7RkyDG669IX2GtbBBrTYohN-x3KTgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d35a289765.mp4?token=L1yOw2OOGBGanY49KeRY1rIkcgOdWwsayailPtx876iEI748RkE8A8Lsh_8x-8k1bunyFoL7-nY6Zh3Laqc0hYdsB91WUJ7P7pSQ2NqlbTbNfyw3qZATpVYTfMd4hW6UkndZf9P743vbpA2bLHrI_UHBHJHr6J8PIaK3b6nsk5ePEoK9S8x4iu2VgYn0o75WE2uDL7ue5-KIKnlhvSxlNDf_dOoulgxQDJGeJeRYi8yKmVkL8jShvhXZIvxO-wXRDtcBUfNUUSOG6JrvGM6Nc4VdwlqEG-6S-YDDzLg29mbz-1nB1sFtXCNQ7RkyDG669IX2GtbBBrTYohN-x3KTgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خلوت کنید آقای سامان ویلسونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84571" target="_blank">📅 22:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84568">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dkYc3stzI4MpkfsKFd96fm47fR8zQsOBykys5U4pLDALjJLS7UgrZ24UzF1H06MjAhrssLWDmtB1OUtIjUiG8iWQuoX8qJisluiQ8KLKV-mSjdJTo-hPxG39PWHy6H08Z6MGG9ZPpr4X2Ln5B2rWfJBldTRLX8842hONrbLsxW_j6_nuZgmKzF7x2j8mofN_FQjnBgk6SzqAh_EP1-8SytGmSaSp9xxgjUPcUJs2gYzK1Oc-xbjrSkbRx0jd6SS1jo3OMtdzpeZC6S_BaE0yeKtoLT0fyI6HIVMhgj5Q7VsWEN4_VOZG7x2IbAlW5gIrW2mSYOojrGx2S7hMcVbIEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامنت رونالدو برای مسی: لئو، سال‌های زیادی از کشورت دفاع کردی و تاریخی ساختی که برای همیشه ماندگار خواهد بود. بابت تمام چیزهایی که با آرژانتین به دست آوردی، نهایت احترام رو برات قائلم. یه بغل گرم...
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84568" target="_blank">📅 21:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84567">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کیانا عظیمیان خودش یکی حرومزاده تر از مهدیاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84567" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84566">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amdu5V4yNmLcElPollUWVBFm7xiwNLMx2VjFmYVOmKl3TNeaOzTBmMGznN72XNDTFP91poUyUevp8FjlBD_MWRGfEdU1WjVJDEN42N3-mxAyY4GYtaK6ToqL9aRgnMudiX_ETQHm1F7k7VZUjPuIPU9XS5CYCUyS7BtVZxhCOJ7fDuu378xv1th-0gJ4bFeXJkXBt6pJVABb6WgkvdbFxatrnh8MdG8Ko1JWU-0KoiFcMRJwUu15ewYdnC9U-XcYHPvForseocqklOW14bolBc75zN097uEawXucLoeehVtYxR2FZnjoAlfr9uDV5y_RVCyDStVOtZZUs2MwzBQIIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری های صاحب صفحه‌ی ۱۵۰۰ تصویر خطاب به مهدیار و ملتفت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84566" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84565">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">مسی کصکش جام جهانی خداحافظی کرده بودی دیگه بازی خداحافظی چی بود پولامونو بگا دادی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84565" target="_blank">📅 20:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84564">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">پاییز نیومده ثابت کرد بهترین فصل ساله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84564" target="_blank">📅 20:41 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84561">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">HEJAB</div>
  <div class="tg-doc-extra">The Creator & Lickel</div>
</div>
<a href="https://t.me/funhiphop/84561" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84561" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84560">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcuL-NvE6EVRQ0rPFYhyrv3fYBOOa8ckgXBNQIEhLZ3EcFcrfIUIVosJ6kvVjO5_gCKpKAp7iKrb140bvvO0dJaoBRgqrHH67F2JE6_g4bb-YZkQ6nVNz-rgtFpbJjDgXqRC62CDB8p_pGji47yjHVmXTn6Ik8_xum72bsxncbxyagXAF7Kvzyth3cLonNPrlp-d_g6uu8NHD_onuSOl-G1y0YlYe1HeWYCBakcumUy_uhLeiepjNUt_BVGRrKSZby1AunIaeUGWPQCncl19egca8IcsmmeLd_u1K4xzgcqrFCSgO1HmtsPjxEqrRh4_8NSV2slxmiJCHS0Cfna1vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator و Lickel بنام حجاب منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84560" target="_blank">📅 20:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84559">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=jwSg9vI2NtiR_2hgFZKh2Pvi2GwZ5iJITW1grQoYxQDsqxL4IzYq7_SuztJssPavgMJjZHHZ_mTh9GNXXWZcOKqqxPSaJDe1LkrhEWXYoK7OB9OGZp9JqcLKWrHiyMnEQAU2WPIlS1qLXsn5cODmjOtiHhTL-gRQFftX6S3b2B0CXXN1ugvMAkWBWe3PmMI7qYAToGU6bimttCmpjtxvxpZqfj0C8XB-GYF3X5az6GS7N8ZSVv5JF_UZYAAZ0KCeInVUGrBShxQgzKDTu5U9ypLbqaS7QtSclAYgSObbrp_qw3C8RyF7bJuOz5bUIn8KIeEKaK72c_3LbXPIlFN6Yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b1e1871fe.mp4?token=jwSg9vI2NtiR_2hgFZKh2Pvi2GwZ5iJITW1grQoYxQDsqxL4IzYq7_SuztJssPavgMJjZHHZ_mTh9GNXXWZcOKqqxPSaJDe1LkrhEWXYoK7OB9OGZp9JqcLKWrHiyMnEQAU2WPIlS1qLXsn5cODmjOtiHhTL-gRQFftX6S3b2B0CXXN1ugvMAkWBWe3PmMI7qYAToGU6bimttCmpjtxvxpZqfj0C8XB-GYF3X5az6GS7N8ZSVv5JF_UZYAAZ0KCeInVUGrBShxQgzKDTu5U9ypLbqaS7QtSclAYgSObbrp_qw3C8RyF7bJuOz5bUIn8KIeEKaK72c_3LbXPIlFN6Yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسسخوش با ۵ تا سرعت پراید چپ شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84559" target="_blank">📅 19:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84558">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hysbn-3lUUzX413dZJAwd446iec3ZSkTOvB1D9Xxipf0lwiM3vB-Wmze9Hmrek7wWryWmK4x-L7JkkM4ys3dike01gVsgJ-7fgA5JwQqU2nxWQ-YZ005xOW-_0WB2ROBwL9RsROTwg6aCCH0kvCdhkoA4djK43aH_dCYjmeS3_2t40G25rfN1ZDmk9ab1HMb2-duCFiE2tRt4iJybTwp3aoP8Alxkd-f5hnT_bFWTrG9UJKeYvjiJssHe_VbcGu1CkqhSpAg0Nh3NUxQtfobEY9mitN679IJ0NnE7i6g1oB9gIoioOOzj8GRKa7i_Nx9Zm-QMaAMjc2zLpi-Da-kgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخاطر این کامنت ادمین دومینو بسیجیا دارن دهن شرکت دومینو رو‌ میگان و هر روز جلوش تجمع میکنن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84558" target="_blank">📅 19:20 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84557">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B8R_zDfafv-ItYByBfqvpWKYH5xfXUDkohSWck5EpKELT4JNH2T1jfQdxGiyweN2SrEBhQ17kUkELtNjP7A4BwPDK6lLt_mU6h6poI6qsOEdP3479tbNHps4MT5nG1HnKt-d_2tOrg15ZNJ5hoseQpipbKp9TgNXBBWMb1mDqvrbKz_CrfMseCtL0U7PdC3ztRCWTSikdBamJSLCQy6jLCUs6UON0A3Vs9kdCaAdFcVLlmPPrQmzNfcaWD9G4rOMzJvx-F_9TPaR0_i0aQVkPz0X3xKC1iwG4toGktg-FtP8XevBir9jx4rZkB6b-S0wzzfCewxAZJh-Wqn0th5j_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیم‌کارت با قابلیت درآمد زایی؟ اونم تو؟ بیا برو مادرج
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84557" target="_blank">📅 18:00 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84556">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=Pz6fpMVPbg1Cor3lMFEKCx1phpW9WLp3272_yGT0eTOnNfiV2M4s9ZC3mdrvtF31Fw_4_B3SyjlzrcmbcdYDf-bWcg3kdrU25hi0lv71N-kIeYUeLWKlGwsmnA7MHQaDaGia3GXblxzP1h1h2GEUKOa76xLzE1Brg3bcrws0rY804JxK_r6caCPZTtIlXGVFsV2UNuVzzT3mmGEIYyR2Oj8mOGIYVBzoHddurrdX718VBDhu6HAeTIoNDzYT36ImmWJ536LuQzHW-dz6NtxTnD_-iJmDDTp0YOtmjjkjHvQZWKtefA4UJ2S_9q3HXd_BpuIddmVdH1zzqPCsZbt3Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/546bf4e186.mp4?token=Pz6fpMVPbg1Cor3lMFEKCx1phpW9WLp3272_yGT0eTOnNfiV2M4s9ZC3mdrvtF31Fw_4_B3SyjlzrcmbcdYDf-bWcg3kdrU25hi0lv71N-kIeYUeLWKlGwsmnA7MHQaDaGia3GXblxzP1h1h2GEUKOa76xLzE1Brg3bcrws0rY804JxK_r6caCPZTtIlXGVFsV2UNuVzzT3mmGEIYyR2Oj8mOGIYVBzoHddurrdX718VBDhu6HAeTIoNDzYT36ImmWJ536LuQzHW-dz6NtxTnD_-iJmDDTp0YOtmjjkjHvQZWKtefA4UJ2S_9q3HXd_BpuIddmVdH1zzqPCsZbt3Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمااااام تتلو همه تتو هاشو لیزر کرده و از زندان آزاد شده
😐
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84556" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84553">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSBss32yvNhD6E2aDCA7Z4qE9x36wYCEgjmqaKW5QByFYjH0GWtng9iYvABrdrrckzMUmksNqrofk3yiWQr-UqzzOHogD1DireahnAzEsVIvlVLaT7iNeSz7uC85Md2SlfPZZ0AlUO1ww57V2JsxdYzILUfULLVUsNugSP70etq83vN0DYbXp4QQcPyJXEzMdeYp3bxq5iCHQAS8hsplW2Qqz1tNhQFSDxIz8ggPpz7Pp-6cfExhf8FhrnKcLLj2YFGiSUfOVEnTZZwWr-WAtkhJL5SvLERHfwUG3tdoTgjo9nalJnxaLYbh1WygCBrK9bf9UjPtJuDH-_gF1vW5pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84553" target="_blank">📅 17:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84552">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teVPSfN89l4sq_xnrM0cbFbr7oZzlapwCB3Xae9c6G_pezsVcMjZPqxiHykbIF0RRWG-N94VjNU1tsqK9GjJ_VUPOcvMyuN7O9WORaoeG0MaLHW3r11fbAEIcFSA9moh8LqJqljRTs2auaOopO8ZMw4mitmE7DRZ3ZyyEk-l7VWbZL9Mh8NX2vpFdulm__7qnjGW5aRlYNGretyVJ0NU7h8YOa6bkMCidCbft0YZ2_irieyM4Xw1i-YNxYL9MhYcGjMLsiPspylXotJWWrsIDStRbJoTZK74JCNlEcMnJOTTttnq5Yc1QJ_uqIxbOC9ql4xTyxmfmQt9kFy0xEAhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من اینجا واس دوستام تعریف میکردم تو مدارس ایران همو انگشت میکنن خایه کرده بودن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84552" target="_blank">📅 16:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84551">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">من اکسپلورمو به کچالو و مردی که عدد روی پیشونیش رو قایم میکنه سوخت دادم، هر کاری میکنم هم درست نمیشه</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84551" target="_blank">📅 16:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84550">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohPZ3v3z9uFSsGhunTrXHwikyKQv0nhsjAolXcKQ1URF1AXcV2Hg9uM-y32o54eFrVM7YmIj0zA1eKIyss-HItWFF17A0PisscRTLz7S5K1LsmXUBK0gUzWeC680oeOxuAnHPRomQa8KNwq9u2kYN9Uv8fLD5sTyzqU507FrzbVC6epoD7YMnGAQ-uQWiPHnCjY9GIzvNoB515wKBfTznpy9Bp8fkDenKIvlgbVVVQy1X2fc5cE-PY8RHxYVsvoR_fNpPlCLaN7BW4Wt5vp8KF-DDt1baJiITte9M48Xj9XPgULIcQkrMhVaH8bjtJK6me-4cHQYijo-Uz9ytnqwFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه نالوتی یه ویدیو با هوش مصنوعی ساخته سلطان ازاد شده کل کسایی که تو توییتر هستن باور کردن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84550" target="_blank">📅 15:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84549">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=eSIdyU9woYpCP0aDt4pvyNV_F6bbhWV3oBHjcDDROwBbK60nIih95bOv75RNQH47rw-Py9_8t-esz7dmytl6WrKxPxWXtAQ0f7oNeIwNDfjZAeYNlIoWYzAt6__vNc9BMKZGbKtww-nmwH4ENZ85NI8m2SXhAH7TqPozLH8XbrOg_AReYeO0IQ4X1aLPRevBtkL3gXlBqYcYpPJzANMTVB9iqWuURyKVSlv42TFTF-KSGJ4lBgw6kuu5TZB5krQnebe1jjYGAchopNOR43FVwV_tDrtZ4aSg7LSX9nql80KwMns86VCE8ERyRRGTnnk6CNnemY1g7d3px-vbXoEHcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=eSIdyU9woYpCP0aDt4pvyNV_F6bbhWV3oBHjcDDROwBbK60nIih95bOv75RNQH47rw-Py9_8t-esz7dmytl6WrKxPxWXtAQ0f7oNeIwNDfjZAeYNlIoWYzAt6__vNc9BMKZGbKtww-nmwH4ENZ85NI8m2SXhAH7TqPozLH8XbrOg_AReYeO0IQ4X1aLPRevBtkL3gXlBqYcYpPJzANMTVB9iqWuURyKVSlv42TFTF-KSGJ4lBgw6kuu5TZB5krQnebe1jjYGAchopNOR43FVwV_tDrtZ4aSg7LSX9nql80KwMns86VCE8ERyRRGTnnk6CNnemY1g7d3px-vbXoEHcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بانک مرکزی افغانستان در گزارشی خبر از شکست دلار توسط پول ملی این کشور را داد
در این گزارش آمده است که:
سال ۲۰۲۲ 1 دلار = 90 افغانی
سال ۲۰۲۶ 1 دلار = 65 افغانی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84549" target="_blank">📅 13:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84548">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبرنگار حوادث: تو کارخانه شیرخشک سازی،کارگر با کارفرما دعواش میشه،برای انتقام مخفیانه ۲۰ لیتر اسید توی مخزن شیر میریزه و لحظه‌ی آخری آزمایشگاه کارخانه متوجه این قضیه میشه و از یک بگایی بزرگ جلوگیری میشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/84548" target="_blank">📅 13:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84547">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">رایتل یه خبرایی از واگذاریش بخاطر ورشکستگی پخش شد، ولی به دلایل کاملا نامعلوم مدیر عاملش اومد گفت کیری سودیم واگذاری در کار نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84547" target="_blank">📅 13:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84546">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=iXNwdsAspSmSpzqahgddJp4dGfUL6GyBQqfY1lY1uq2_6sePvacKpCIc-rtjD99gkzTYyuvOIxDA6kmn36b9MyzjwWlbC0ljx13amtzx_LhdHUUBGzvuBlwXkHwUxl0ld91bM08cFLTlhIXfUOqQV9Aou3vVuTieGQSY8ARnpAbv9daXv-Z2TRKjhuqIgOCe_QtEzA-Txqsz4Fk0QI-u2pQHrZjVsARZsNGlDeUFim6BNGluBsAPvHr_J08gWm9h3gP2TaTATZtb0dsNYADN-yADYil2-uWWsjfW9GrK0pEcGnE1xZRN8G4qxs__9IMfnbQNFDPjQstsxtQBNcklsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5582bd1932.mp4?token=iXNwdsAspSmSpzqahgddJp4dGfUL6GyBQqfY1lY1uq2_6sePvacKpCIc-rtjD99gkzTYyuvOIxDA6kmn36b9MyzjwWlbC0ljx13amtzx_LhdHUUBGzvuBlwXkHwUxl0ld91bM08cFLTlhIXfUOqQV9Aou3vVuTieGQSY8ARnpAbv9daXv-Z2TRKjhuqIgOCe_QtEzA-Txqsz4Fk0QI-u2pQHrZjVsARZsNGlDeUFim6BNGluBsAPvHr_J08gWm9h3gP2TaTATZtb0dsNYADN-yADYil2-uWWsjfW9GrK0pEcGnE1xZRN8G4qxs__9IMfnbQNFDPjQstsxtQBNcklsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خلاصه دستاوردهای همتی در بانک مرکزی.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84546" target="_blank">📅 12:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84544">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dSRHYy7OOllTDflFjSo1VmQz67wSM9l8Q3iHiYi9r0dMZsblt-N02URYxkVylYDREiQq4mr8JgRA-qclcvPhDdeSrzdrLTcULiOatA9lsipmjDZRNaK8dqjAjYHHcHTqIBRidV4k4vQzKGgqNOfYEdV-iV5GidLKTfdFmWtAAn2gjJKcadkx8NOUQlOoESVxOKkQdgty8Vv7Gk51wH9igijIuFVNHON7PxgjoQSAKNY1yXEBMrywk_lX-SuJM3pDwgzlYtZgvv-1K2hLrCl1Z56_oZYainmGegtOchcP2hKbL9cB5g_UjBsfEPVrYL7mCJhbPUVyg_KY7Rloxplxag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86ab280716.mp4?token=vJmT7g44IKioDYCojTWKzcWrOguSPEjSUCVcWT2H3sga22kbClHQWSi3pOAjTEXxBpudN-wl6EDg22lKbzu_2K2Cn6din47tb3mRzxfsXyAgjbAEGc0ZdrpVc0SVHM0YHPAV-ZViU30BOlciGt6cZ9OnATxtJhwrOGxZISnZsACKyPRg5ZuTLW2VTOpiKHzKf01Lg0GIjoaVnjmFv1l9hUQwJXSbC4_Xh1oZpR29CKWLcJ2TvmsVFA9qSrmh90q4-ENPexRslhWGO2J2AOMzhAStvwPvwHoruCN7dxH66pwROtAjjWMekL2libSQHb1C_mWUqFPCwpxUVaEX-9kSFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86ab280716.mp4?token=vJmT7g44IKioDYCojTWKzcWrOguSPEjSUCVcWT2H3sga22kbClHQWSi3pOAjTEXxBpudN-wl6EDg22lKbzu_2K2Cn6din47tb3mRzxfsXyAgjbAEGc0ZdrpVc0SVHM0YHPAV-ZViU30BOlciGt6cZ9OnATxtJhwrOGxZISnZsACKyPRg5ZuTLW2VTOpiKHzKf01Lg0GIjoaVnjmFv1l9hUQwJXSbC4_Xh1oZpR29CKWLcJ2TvmsVFA9qSrmh90q4-ENPexRslhWGO2J2AOMzhAStvwPvwHoruCN7dxH66pwROtAjjWMekL2libSQHb1C_mWUqFPCwpxUVaEX-9kSFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
نسیم مقصودلو؛ خواهر امیرتتلو :
خبرهایی که در مورد آزادی امیر پخش شده فیکه و هیچ تغییر در پروندش ایجاد نشده. اون فیلم هم که گفتم شرط عفو شدنش پاک کردن تتوهاشه مال پارساله که اونم دروغ بود.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84544" target="_blank">📅 12:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84543">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrWjgGsgrLc0lxSK8sJi0jgEwGBamct3sdAzpfXNmldfLADy4t6PsYyYn9HInzv0UjlKgrobS24PuJmrH_MyO6ra47AFqLuRjdrxynBRkLE45RC8zlEgaoanOFxCkgx1014m7G0wchEe66PrzTHdc_h7qPSiqnlkLME7bcJcYnVR_rLWWrnTCzYA3GDG5Yy8YPM0Tnr56iOfC01zgTU2DNXFZDkXhJPo9XtMhSSgH5iwcszIafPP0m5kOsGsEk5mcQR_j8wZ5qc9VfhZPzfjPNCa7PscaxQntsGlVg5pdkZtHy_3pmdRQb7oqiYz1N4a8Z79nfdoaBH-LGJn7Yi66g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
شوخی شوخی جدی شد، سفارت آمریکا تو مسکو درباره احتمال ابتلا به طاعون ریوی هشدار داد و همچنین
هشدار سطح چهارم «سفر نکنید»
رو صادر کرده و از شهروندان آمریکایی حاضر تو روسیه خواسته فوراً روسیه رو‌ ترک کنن.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84543" target="_blank">📅 11:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84537">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qchGEuH7vqzXKBqG7ADU_9cOPZhgLd9jdAUbxWcy-RdmAR8I8judtQU_fNC6p2pI3cimxRyQjLXqWyd6bXVrqf98SfYZzlFJ2H5F2zptPgJT-jabZALM5Pv1cusKnuS_4LGhNRUvyeYXkEVafU9PQvChMsWSMzpvXm1aeRBhH6nbTzY0_sqczZ5aINtZxreLZlNI6rFxwNxs7kMO4pvpbrJ2SHxgilyqMo7NjYkNJQ7Ihu2DbxYq_K8yHzUuBwlltz0GD47DdTlw7Oxi2PKwUlHRIP7i0bArH9lN7N6cm6IQoxZIWVFcNjuGlt5r_dzdsC0CC-SrEa3EogQbaclLQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدجور دارید تو طبقات بالا ویولن می‌زنید ها
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84537" target="_blank">📅 11:34 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84536">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YAeEvi_evua93Q8hv-dqOtvxZ1wsoJUXpZbwrRVBXqWuQl4e38CuGRc8aUAmQJtr-RqostJ8HwoBs5DYhQUbQRnJWJ2VAoMD_5bjenpDScWOvlEvi60rCXQ69eeyqT-pf8QKxCTvclZfNqoQm8DVS9cTiWH4eJHogk7iGyJha-n2Dz4avZbAgD9DH9aMARAabt4QRj9vW6MfbESicvjCnei1kcQoH16ATEtAduHZjTRYTYvs9yHsDviCFlbV-k8WiYNKpGG4HJY9g4qgfuc-jDNfOAaeb76Ewfsm_kn9QiPtsUD3wwXYt94F3hVLqFzx37G1BXnGWJlxxk6tGF0tPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام امروز هفتم اکتبره.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84536" target="_blank">📅 10:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84535">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d26406817b.mp4?token=FJar7Pr-jpOvaNAZH6GJ_dgNdhzU2T7CjhRQt46_OVnpqsQ_Yz8Hhn-qiY8vQ0fwOa7UcrbKhozJXI_4u8bMFwjCl4FKAZ_ZS-GVnFJO8BV-zO2_J_8vB7fNsppqjsVI6iLJfzeDTTNpEVGHmqW752CGISK5qO3gQo2dPTeB5QeekODrsy7LsAtb3AZjOCR2ZK-kmmN2SBLTNmcc-v0ADGW0zAU4mNipKT0O7_BJ88XN0_vBNQQFwnQooog-vKRqwfFWYyrgx7Fd52KIShrdQezDjgd3-xUs_3FMObcbb_faw6mvtnvTyr9WK_VvKlcBttK6JdOHMFl8KlG6cn2gpw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d26406817b.mp4?token=FJar7Pr-jpOvaNAZH6GJ_dgNdhzU2T7CjhRQt46_OVnpqsQ_Yz8Hhn-qiY8vQ0fwOa7UcrbKhozJXI_4u8bMFwjCl4FKAZ_ZS-GVnFJO8BV-zO2_J_8vB7fNsppqjsVI6iLJfzeDTTNpEVGHmqW752CGISK5qO3gQo2dPTeB5QeekODrsy7LsAtb3AZjOCR2ZK-kmmN2SBLTNmcc-v0ADGW0zAU4mNipKT0O7_BJ88XN0_vBNQQFwnQooog-vKRqwfFWYyrgx7Fd52KIShrdQezDjgd3-xUs_3FMObcbb_faw6mvtnvTyr9WK_VvKlcBttK6JdOHMFl8KlG6cn2gpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام من از آینده میام
حدس بزن چی شد؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84535" target="_blank">📅 09:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84534">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLrKPkFzy6YS2yxiMha7Vmn-0a0LkhTzq7vkjeydwM0x-7h2w0FqZqLJs8_YmfB0ihrt270FoxXPKCHiqcgJds4LAhDhKg7oRDg-6KHlng1Bugxl9j-gqCcx6QtZYaGuxHk8uIqJ0RczscYUx8wvIJJrgxbCveTBG2AEnq96acEcV5uilkoR5B0xiwDbF9bDEKRi-VJwi-Ej92IePx8EmNBtw5XKdQiQy_mI1P85A7z2iEnZEFH6Yp9cJgK0jGKK3RqTXn1gcWFkGNTjwZDHNok_V1P-btGYprL5ffD5sHbowgdLkYaccZ9WFIQhHgSqJWUYNqgYLo58VY7xXmRUpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم ملی بنین در بازی امشب.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84534" target="_blank">📅 03:50 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84533">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">یکی بره اینارو بین نیمه توجیه کنه بازی اخره یه ۱۰ تایی بخورید</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84533" target="_blank">📅 03:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84532">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کسکشا این دیگ چیه اوردین جلو ارژانتین بازی کنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84532" target="_blank">📅 03:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84530">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJBMLhn7zVDKnefJwFoeEHlTI3cH6tX9OswpaEWl2G4X_y3Xk6otmhiKB9KKPBRXvLED4wh-jB576BsZ4JLDmOIUuj54cMRykO1dSSWmSXUwu6o4TMz9xy6KqplJkawtTl3YEWH89fC04YzGmvSl5NfcpN5ysVshF2GAk4xVBChNKKwLvugn92uE9qyYrw2Lx39nypsAm--ncjuKZYQR0MiK-tKQxifb9MV7xGs1aF8vfmTgTIqpTj6Ot9thx3zLXwYsJCRMf4RUX3HhdDbSQ4txYT5p9ZbJihbhTBHCxW1mHvW9QQdxOzjnK0npc0CzAKqu1wnmFvc35QN2zzsR3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیرون ورزشگاه به بز واقعی شماره ده چسبوندن اوردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/84530" target="_blank">📅 02:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84529">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G9MsPBptP65ohgOe-4YVIMXgzUl2LhDJOMDFnegCFUzISBgqhRKpDQkqVTU6FR_-LrvL2AuQKKQkE7au-zJtcmfyGCZnnEGh0jELJe2FyPzdK5WGpMlYViyWbri5Y2h49PxvFKj2KS6lo-C-Tj5nLsUbMt-LbA0OVcHMeEDNZLle3GNLY55gJ8wPNcObuNPQX67TivEA_7tPLg6w0_c5C4EOumJq9_f3nt6qpOFDrth5xp6eKeLQImErsQrl8j70xKCna7r6bDj0a7BIcu1F7CarD2CkciiB2mJ-0vr1oV0GuN7BdmpDqyskggnLpzNxPNFUimZVJ0SFEgBDJdGDig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو دشمنی هواداری چی ای</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84529" target="_blank">📅 02:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84527">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PV-obYzMywzsmuQch-CBX1d69zvl3B89JVoAL9oBCK8pzbMg3bDKeSl-UxYkZqkZpk7FnZ1HwnpDSs4_RYZWECB3sr0X5_R3ubKNrFzeCnfgV2KkEBwmKeM3HtW5YURRY-NMp5P-YJphP5TfeuIb4D3Tn1lPbCJvsgVx0KaTlns-5RPpph8JplB5q0RjJ39anNNHVJHZsbVUERxCh_nacxvOCCS5Xk83L7Y9S7G8jlnNF41zW5ReYH3Rgk49OJMvYLrGeMfmRaJYFh-Jr5L_RTE5huH-dowfZZrf6z9ckk6PXIVk3h8ZuKHgLAvUBi-9Aqd8xyb3B1Lpnx11f6lm3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحنه رو پسر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84527" target="_blank">📅 02:36 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84526">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اگه خداحافظی مسی هم مثل آخرین کنسرت ابی بشه چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84526" target="_blank">📅 02:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84525">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شوخی بسه دیگه حاجی، وقتشه بیایید بگید مسی تازه ۲۵ سالش شده و نیم فصل برمیگرده بارسا</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/84525" target="_blank">📅 01:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84524">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZWSKnnn4mSXpnV1xwVffhbBMjFdMpVu94dYI-9hIiIvLkt8sXyBiDGZc-z2TlTeP--dr-8Wd5q8bJj_8iUXWqQWAKfe4Gz_BI3Sogdcx7QC-rjAJduFsGOyVHlThOWsyeC9IgYI46Bk7Yoiutul2DV6iciVMKd0KqGqxM5G2ZgwsVDmfA8LPC5Pq6iqvdITK2FUgjEPC0p-nXHVqQx59R824ihUPnx5jIOGoZQytX_sXuuNJk1nnFTr6rdSL-S-LVlz6Vs42UULvgyqYBs1GaUuEn9WLs__haoW9Ph6MF_XRgDxOPQClIyLBRdYVCmJ8EhU-qJomh3jVR0FZFTYIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزشگاهی که امشب آرژانتین توش بازی میکنه یک ساعد قبل بازی:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84524" target="_blank">📅 01:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84522">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84522" target="_blank">📅 00:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84521">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gdy3e54ljxA1RMAqXNqmP4xuLvOfpVx3Xlz3Qatk7OKF0yAUid1rIq2U9PnUnR8bsrDnf90AhC57FHWcFumhTUM-7nkva3X7aLP0kaDMoTwoofz7_3bwDuAo6sWr_hliT8PXsuAT_2rrzq3jHGoPbr3fj2jcm0-kgJc1jR36dnOWVyU_dDa5oby8k413wzQCauyz8y62HnCeVO_BdltXYvaj6SgOWAw96FTYRPlrPIU_kjZz074VrHX-6I6fVnNHWrO_Yuqrsnhu-Dp43hjOtUr9eUfTCONz3IKI1bc5CcWJFMqrKhCiwOIDkRZA6FFUlVcR3VK9qyROmqhipo1b7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر این یارو خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/84521" target="_blank">📅 00:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84520">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">شما براتون مهمه که تتلو عفو خورده و برای ازادیش باید تتو هاشو پاک کنه؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84520" target="_blank">📅 23:49 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84519">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ قاتل :
باید کار را تمام کنیم و تنها مسئله این است که تصمیم بگیریم با روش خوب این کار را انجام دهیم یا روش نه‌چندان خوب. به‌زودی متوجه خواهید شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84519" target="_blank">📅 23:45 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84518">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وال استریت‌‌ ژورنال: ⁦CIA⁩ یک لیست از ۵ الی ۱٠ نفری مسئولان ایرانی رو به اسرائیل داده گفته اینارو نباید ترور کرد چون بعدا قراره حکومت رو به دست بگیرن تا ایران کشوری نرمال بشه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84518" target="_blank">📅 23:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84517">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">همتی: بسنت گفت تا دو هفته دیگه ایران فروپاشی اقتصادی می شود‌. ده روز گذشت و چیزی نشد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/funhiphop/84517" target="_blank">📅 22:30 · 14 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
