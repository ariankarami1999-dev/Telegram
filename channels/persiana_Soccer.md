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
<img src="https://cdn4.telesco.pe/file/gP7Gih_e1TfWC7ws5IrNMdfbarMNY8CbuOJ2deizAjVUQR_Xjf1bv-PDumnegGfyZ4VMQj20Qatd-PPyMjymY4vmltHDziOOEiW3KbcbA8KPW-WKt8Ap9Akx7pKOo6f6lB_mt2IQLg5l8Whn9ZoW8O1Ya4IPzwAyr4PVD_80QG2uKe8-JQ6OWjO3buC9-nZ3C7XV45n-8uxVnLv_Z5UzwwhjoSue5B9uhlrSZbQTDbXx-k-4f0N6mim2Hjkwlfy7BpywY9FseToecF6-KMEM9abKQaYGCcQVtj5ASh2TQVO_gNGOvA2Crj2PafftzmqAygWB-4eglPuCgBHCCe3_bA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 606K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-09 14:51:53</div>
<hr>

<div class="tg-post" id="msg-26874">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HzESNnSo9XWyeJxAMsPfHHJfBJHbAt1OE4I8lTPF8ndQ_0IQC37gw3h5GMw90TeEuPTEyR9ImD_MHD8-3XeSRIcLqMb9FdFboDl-nQJwoXgIAZrXIEcRR8NGwYRNvzd4U4HaPpmtlJXzN8e8at5duLei2Uhhr1nuatljG0gJKPWigGal1t4Y9rOjs6ZkE67J-iqm0aJFPlsKLqbE80HvqmAoY44MtlG6WNsbCZeEi_H6j04cwvHPOJsKYcJgr55zHsYC36qy34UfPw_5Oc-39SuDz8dSYcPtQhy1meJPCun2JfVP6TVfHwsn4JgmrSVthuet7_R44rHKtUQZinAUMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استارلینک توکشورعراق‌فعال‌شده. قیمت‌ها هم با دلار ۱۹۳۰۰۰ تومانی: ۹ میلیون‌برای‌سرعت ۱۰۰ مگابیتی و دانلودنامحدود.۱۵ میلیون‌برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود. میانگین درآمد ماهانه مردم عراق: حدود ۵۰۰ دلار که میشه تقریبا ۹۵ میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/26874" target="_blank">📅 14:24 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26873">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0molnG4jUPPGvf481j3SMYcg3D5BpYoPPtYu2_eUYhy1ojzPhW875Lxhu-E7Wm994kl8u9hE77Ev_AzppxgDmcdkFVZGFbRs-aGNbJb_lrinjFOrqHDjW4eR694OlbcaOaeLwq-h0Z9cJOjpAs_0otICIbwwPJn_okadG9xjVCuCpQ8kXhKhrTAJTsuQkqojLBVJnB_l1RdKK-jR9jyPjEp_fuI0SXp75WNJzwS9GID0njRzzNpOXd9-h--bkSVEOi_Ui04KxnE1TGTla1M9LOJQLs8kOjQr-DQSiPxxsnBY7LkctRmLZqT0aV43NR9UTRQyR9CtHOypJ6v3f4mkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇧🇷
باشگاه آرسنال بزودی بندفسخ قرارداد برونو گیمارش روفعال‌میکنه و از خرید جدید خود به شکل رسمی رونمایی میکنه. تمام توافقات‌انجام‌شده‌است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/26873" target="_blank">📅 14:09 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26872">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a91beb718e.mp4?token=iY5NcvczBePxJ7_8x4kbmtqReYJA-f2i2eIyPrjidL1vIPPv1_u59sQ9ai2iY7CqJaVRW5KMKHx8szCW0YI-OZwcYkZl_lwT-VyLjJla7G30o234WKAM9CFCoaQ1LvRfQQm7BbB3QYH66GA2gDehZ7vWguMzVXRwbRynvvJcsov3MudjjbGrmzIkl5YC-_-7DBaD524Ygxkjit9zw2K3K5HuC_8ZLhDK0SBdHZ1YL5hO_lZM47FtjgOIssas5Ma9vOn1o48BeukCV9lOlw6tgtHCRNt6K7tZxNE5qwJbTQTvN8JliT-nmFlh5CcYzGxXWWNBJ4pvHnVczQ4kTDjNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
برنامه دیدارهای هفته اول و دوم لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/26872" target="_blank">📅 13:41 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26871">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u9k9j7dI6Xr1X-K4DlWcTPF02avDCMl5h3BRaAVPkoeWy6_Yn83KjcVayEP3hkCKL6s78gGDhGoKpmJ1QFwhVc9UbArWqgQhmkcTvnpnA-6njd7wRqSYGRJxeipkccypn6SF2PLWYqtUcJ-Po26aOnIDE9_e5-ut6j9fhcgVpL2Q1ZvoFYd3teboQY53L2U8e_Bz5xJsCh_rAx78UTBtURZP5zsiYPZFL1yHMa4tst8YITcsbdX0rlCybdGuuXsqui2OW-euVcJkKr-2DO_9ylaWXVFQbqdZDyNWkmKoZFmHPb9eqOgZzHH6kR-LisqZrS2as52hOPMS1SRDmJCqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مایکل اولیسه که علاقه زیادی به پیوستن به رئال مادرید دراین‌پنجره داشت تو تعطیلات در حال خوش گذرونیه. ویدیو مثبت 18 بود تو کانال دوم گذاشتیم. بزنید روی پست ریپلای‌شده کانال‌دومم‌داشته باشید.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/26871" target="_blank">📅 13:10 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26870">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f2b1c64c36.mp4?token=r_KcXMcOl2rB5CgEwNBvTmrkKZd_-C1ldWBImZlbZ30plCPkTNTghHhrLLSHHGc3yQAcPcsWKDxyCBkYCw5wbdZf0yFtiKMpugDzRqIYf6WHuM7h2XyUseeTY4aWLQZsiXlw1_pwmXJsluwV2M57zqim7IcIy-s_4rgqX63kH324PsbqpvXpsazWgQhrhVJ8RoQsnlIg5IMB-wQ_bcQ2hTjMBdYft4KqyigY0moezYw45xmPI8NgbiVqCfXh_eGicmoccerVO69pmxghCxOgmc6l0jWTDwRQaklChC8DDdQ9CeuxcUihaLTmZk_BqzwX-k-zlL36vqdWizs0UNOrrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
توضیحات و عذرخواهی میلاد کرمی ملقب به وضعتان چونه درباره تبلیغ مرز ایران اربعین:
‼️
یک بلاگر معروف در فیلمش گفته بود در مهران ماشینش دزدیدن از این مرز بد گفته بود خیلی هم وایرال شده بود خیلیا دیگه برای رفتن به کربلا مرز مهران انتخاب‌نمیکردن؛خیلی از مردم ایلام…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/persiana_Soccer/26870" target="_blank">📅 12:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26869">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFygl9nbpfW4LYY1SGGnIzGpnzZBNQ7lJG1o20GVJQ8pcVuGUwy44hfLsfiwn9d53tY6huk0oxnSdTZ9cwV1_7uXpTkipPoQAPFNolPO7Vlxy2YMWhREKCMLGJg0NNCZ76LpNMxrR0O13lMmIXEY6FBvDDzrjOvEg6XRoGheOZBWvNXwzr6ZY2RsUFK3lWxjXe0oSjJcl72KM3aDbGy8zvNtE-sUCpFRvAWt35Bo-DigEKQJJILIlK5ZAWt6dDzMa2gDNS4THztWh7l2qt2ExcKGfddDeMMiVzPONbe9wr2xYaaX_f_tj3_Un5saz_QHjjWKr5gPIVqRunFxqjxMiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/26869" target="_blank">📅 12:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26868">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1C-xEwKIcGOCadr_r5wWKttIryor2CDyx_F_PCNB1e-mopaNzQ-Y3WRymA6GYD0-A9Q7FzYwsj6o-s_eEln0wnLYFvJfr60-Q_GNQNvopT0eRPhopRVckGPdRz549CzojZaAsySyi97uhsX7nm_cfxNUR_iwYRbkdP8MkpkdBia24mC3ThgznhhCbtO8Fwo3eiOsM0VFAH7uYYX74dNFh7LWdMo_CgHRbV_HteQsr_yhRR4VIJ3UGnUM91lNwI5HajUJ9BnjAaDRlBPaRi7mTdSiCPKk8MmT5afr_ocwKqe8BiPqNvmH1vmTXxGeXkxr6NYN3PNtqfTp7GWIaSxEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شکیرا خواننده کلمبیایی: جدایی من از جرارد پیکه بهترین تصمیم زندگیم بود. اون با خیانت‌ هاش بارها به من‌ ثابت‌ کرد که لیاقتش رو هم نداره حتی باهاش هم صحبت بشم چه برسه به زندگی کردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/persiana_Soccer/26868" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26867">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLcR2tJxq4mOEyLGgDcj_hb_MMgQrbQzdqn52nxxA1Ni3G_uxBgJlXpmla61MqtDOLIa3LWvomjRZ_RKcAvChZ9bzqUMdLL1Eur39UtswWKaW74s26fgP80TYfT-cLdHDyRwer1SzYZDrnmbVb47LdopTp0QtX4f-FLWN8EFpeD9R9IgCHtnEIjTBiA0qVA-4H75Y-WLiDL9xySjHa9Eau6W53KpWV1GIgGVJknacTuNRP7qDbquRZOoS5WLyugCPKFzw5jkyaGHD6YHpvmT_lmsQ2yBgyhC-0X5wViXo5cNb_1Hgqisy2Kmx9bGTatQ7jm9N1nDtY2mJxhD7fwV8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیمار داخل یه ویدیو به محله‌ای که توش بزرگ شده‌بود برگشت. یه پسربچه بهش گفت: «من پادشاه این محله‌ام» نیمارم‌گفت: «یه زمانی منم همین‌جا به همین اسم صدام می‌کردند بیا باهم عکس بگیریم.»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.6K · <a href="https://t.me/persiana_Soccer/26867" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26866">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rJHwWzH4qkSPQX4AvKsuo19eKghdv3g4ntJ1qWqFowMlgyJ3ST9GgCuqodUQpVk2jUbe95OUkzNGdfkWbxYSIomK9P5Hjqk3d01he1pZf4VAI-59MFIf7Fmu2VLiQOOT170FPuIbMVZ7jqYKyjKPZCh4LpYMxlm40HXum7r-Rr6A_MvSN3G_skPUrXJwtonJRNOp53hlJUfAU226vaVKqlP9uCkbJJbTXKL3NePtor7leYsse2MerFab5CMgHy-MBqOtV8hr9HEMOwL4pw7CXq9KdusRwRp413PdnMbB0uULl4aANAQvJab9gkuWyoQSlBKGBLaW8xCrjcLplvtZAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/persiana_Soccer/26866" target="_blank">📅 12:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26864">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VWBPoERA5RHWCmZ5KRHLDzEjgAvie0vWTca_FYAjC6bexW8TEF0gL6vb19LpnOCvUaoak8vjM9jiw2aP5m8-gzzcirBF3dMIl-DJs68nKQo7-zd-tuoAn8Pv1OASrZTv08cwQEsb4XGE4zGDIx0VmcNMrFhQ_dPAGMbfecxE_Lxj5yon9NAU-Gcis3G-59LZgrhYWCsm9s_86DdapHrdnAykb172em40fPrX_WPyrpMVRmlyog_5yagCwyj5XcT0E5CC6Vodn5lw0UEBar7eWADo7DpImQ2F8DUOfELAxBBK_T7qEtsRdk9RKpTe2JlMZIDOqaPPfinR5H5qEl03_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NMN3cQF4m3-4YETe41V1cWgskZ4yrNvZleefe3tL1E31olNGYao9I6YhIewYuOrdIKAlrIdG3xtrcheJBRKjnSpAzt2h1JB_gkIi1zqwySL-de-j0Skol-KdFUkZ_nm1rerjXm8kgz1n9Xw4mjMOSKlapVlzi4oFxRlXoLPZfrN9sHEsfZk0O-oRhl2aFXbGp6YsGjBlfNXI5VcobhMgK78rxutHqYhIQMqleVles80Nv5xaIAICD2d3-_V0kmQRsrTleE14Uq-AnQbPiDofx5AQf7cDNtAV1lL5WT_Q3hN9EQt6OqWe7WZbKGGUoWFxIenUCYh3k7dZvKiYaFKDNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رنکینگ بندی جدید فیفا برای تیم‌های ملی و باشگاهی؛ لاروخا و PSG در صدر قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/26864" target="_blank">📅 11:56 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26863">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PpMBGldqEShvZ9vLaXcFOZliyouRRFdi77YgIRuorxgmvn5ca9fixuzZCdWWeuZlpfipN8AsOupjBbOTWSipxzCaRSSR2V8phtFZutnsF7xB_KAMsQ20oIj2rXUXdGnBU6WLIYB1f4h1N__eRp5DSvylUS6CN4MJkA6Bb2Nj9wEhEgU0Skb6emql5_VVDJUIPCH_pW19nhGeZiwmKHZTa-AndajpSdldIw7QTmNrhrREyxqXTE6w-V5YK_9uMPgJLs1oV99NgwulIfR1PhWoXYlkOF6NE9zWZCLFFHh0auwcs3t_HYvFe2xQfYiBjWuQMK-TkDYJ2IRuq0-wHTEV7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
سعیدمهری هافبک‌میانی‌سابق‌تراکتور، استقلال و پرسپولیس با مدیریت باشگاه پیکان برای پیوستن به این تیم به توافق رسیده است. رقم قرارداد مهری در پیکان برای دو فصل 25 میلیارد تومان توافق شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/26863" target="_blank">📅 11:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26862">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q4UZka2AF3bEJVIseKfllpqgHVgh_mLvOxLk8MbHgZqjpvKKqWcpBzWMScvfOj3JiIYXC0cAlhYRKlAiZ3kYMn4M8uAX0HNuflXf5PBLQi5h_6pVwi9xTsQSg__4olUozkmD00RR0UWSkuq-ITrRAjwAKkiyS3H9F9n-N43V7CDg5K73_IJWTuj2h2f3Mxg14q70vEfq-YaiSOOKyWAH1-7SrX4OoNRHBjCg79ADavEs0y1JGX3q20wcR9Sbm-fgz1chcBlXNXLfQM1ubrZhT9aTc27Owh3RYK-SEoRFYjtwBYb4TRHaRaJ1SdXKqzC0W8MpspzzMeKHhl63Nr37dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عیسی آلکثیر: به خاطر دلخوری از بعضی مدیران و بازیکنان در پرسپولیس، به استقلال رفتم. با خسرو حیدری و ریکاردوساپینتو مستقیما صحبت‌کردم‌ و هر دو هم موافق اومدن من به باشگاه استقلال بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/26862" target="_blank">📅 11:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26861">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c5b33a46ab.mp4?token=R_ENGyQ9TAJAbFJQo9-kLWoJepHfPdPv_or1v1Wf3nA3MTx6efxiLs7xqgyy8t9u-mn0UGqNNu-sGWYTt0-6RMtpk30_eEUQhSGCBfIKl_FCrMEc82kcWmtHl3Nlg5dsSrnotVHgO3pLJ92sCUmN_48MA8sPugJ64CZFahDp_v2kQgy_Vz-ybo0hhorQ7eE4T4-k1NTcxmVX1A4bkPZRqkZow1tAXAkCF5dQMyvjeaex_m7StfGmd3CdfPapuNrerVSSC3Kk1fgZXZjnTH8YVnwlgwqhIXbQwFW7gBo95wNFzk_1nrBXLssIoNd0RnNWHnCpIo7mP_JjWdG4_AJPbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/26861" target="_blank">📅 11:07 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26860">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mir4HqA8BqUqAAaEaDLE4omq_Vsc8aWueg5UE_GH9snTBO4QQp00VfNvY4MpV62XdO03awFw312DF9LfTFr9sFfm6utJ2gFBNIxlqI-pFZkyY_sdPuahyINC3UpE3nIdB8rPS3z9cZhFL8TaTFzi4uyba6B8Q7FMGIrTzyzqpsizy6jOfW4Ai_F9aGPUbUzoXc2K1_XSn6tmAny-1KBF4_hFH5W-GL7UqLkOG5BtBg40r-6JVZE6epxUcwknX7q4rl75aFw941AdhgZRlXz9KU4WifR_GVCZdo-ank-tRn9xSNyX8Eg0rQ8vOky3pXD2uwXGWWou_1Z-Hav-PZ7yaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه خیبر خرم‌آباد رقم نهایی رضایت نامه و فروش مهدی‌گودرزی و مسعود محبی دوستاره 22 ساله خود را 150 میلیارد تومان اعلام کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/26860" target="_blank">📅 10:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26859">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SBJdqzV9UI9PUSFCnEQf3wh9RHkhwJR9YP_j4DOwe1KV2aUhwDrLAUkc5BPydZpVrTruR6dSMRd3mRxXs21ZggRU2YSeGGAFgJMI_FGunmxlbVLtjd8GLdZNtx8QoDJvHEm5e1fYafy0VRkrU92C0cHXN2uvumeJ7UciC5IoKL_qKSrEoMXTThpm9_uJBrc5sqkER30tkkpAgpRfiSpUEcLlBWizGbM71RiTt66H_jlzdfQI_L3iiN7FI9Pm1LZ2TjAEnZW7YOA6PH_s2YJlVYjHiCYi8WuJ-u6yFcrvEocnuu0rPUS-cAmvam11bdm2217H2akedOT4M17_3gDdbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ عثمان اندونگ مدافع‌سنگالی 26 ساله سابق گل گهر از طریق ایجنت ایرانی نزدیک به خود آمادگی‌اش روبرای‌پیوستن‌به پرسپولیس اعلام کرده است. تارتار به‌مدیریت سرخ‌هااعلام‌کرده که قرارداد دنیل گرا رو فسخ کنند و اندونگ رو جایگزین کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/26859" target="_blank">📅 10:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26858">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAsSy1IG2Hj0Q5YJ8GyEUUTaBllSncQdAePH6dXxRPoz0TPRaxdAfm28x9IMUSS7-jbTp2N-uKP7OMMi8eJ3NdvhVpTqiV2FwWt9G6HPkp05X0TW5DyeiBh0uWgefsNPuqcTJEkkDjttk1ypwxE9yVdjkaOaNHo9ZyvpoJG2YH6TROuynLC71FyM0XYHHQ6zq9QS2Jww3YxUZ3isj9iLVSJVZOJPpxHV28O3VLbaCJ86juWLG66Q6eVc38DSU5x44LmCA7wlg1cTOwRvR9iEdrnr2Gn_vN5Im3UALwEUZMJ61M14tH2b33vs7ZZlVtTen5nQggffFkHzLIxkeSk49w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
بااعلام‌فابریزیو رومانو؛ باشگاه رئال مادرید 25 میلیون‌یورو به لوانته پرداخت و باعقدقراردادی پنج ساله کارلوس اسپی ستاره تیم لوانته رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26858" target="_blank">📅 10:01 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26857">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWbnaP1ACiXAKBxe5MaJEFIN0x2PkY-n-ppTlpHXNK34GihwgIFxZOBeV39AWk6kdjsbW_NPGYX8vuhaV_o4fMYVdXicEeUvGdCSFKcXztqGWuTc_2Np6VahfKVQD7u1LOfqbLQn1bzQcTaaEEX8lUKOBplXk6hnO_Za870PrRhMnlLONPj4pYFOMNP5GrGL2Up1PkCRI3yU9gvzGUX9_SwdN6wNJLj2AUiKbJr9btH0uXawHb9Ho6IBUe_H7dH3lv08w1oJF19Cknfx1yPat1GlKEFRRi0Vul5ZfCFthoUMAZxQFLDamcYWrFZXdjJFIHYNWAuBX-XsUHx5klssXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
بااعلام‌‌باشگاه‌‌آث‌میلان؛
فرانکو بارسی اسطوره و کاپیتان‌سابق‌روسونری‌صبح‌امروز درسن ۶۶ سالگی درگذشت. این در شرایطی است که در روزهای پیش خبر فوت این اسطوره منتشر و رد شده بود.
📊
بارزسی افسانه‌ ای ۷۱۶ بازی رسمی برای باشگاه میلان انجام‌داد و ۳۳گل و ۲۴پاس‌گل به ثبت رساند. سه قهرمانی لیگ قهرمانان اروپا، شش قهرمانی سری آ، دو جام‌بین‌قاره‌ای،سه سوپرجام‌اروپا و ۴ سوپرجام ایتالیا از افتخارات این اسطوره محسوب می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/26857" target="_blank">📅 09:53 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26856">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TmnGHnr7PbmQ1wVrNn809iH_X2zLXW2LWxEi8wL8nK5_d-2XEA2vNahnyiOl9n-atrauq2IqhjDURjMffwY62TXXpKhCmz26KlP62Ho7V4_qqVKuuy0au0mHcqmZAz1hDj44CXUjUyoGOz-E61LFY7L_cAOwv0n1jK8jdczaSMgzyxYO2xFZPPqdLkXP4GA6gyPRWoMTa3BbgNhKNcnIsw8GKm47-9-msu48IhNRtGWYp3DMXCQ_dVhJJU5mb65x1x0PUphHzMZBzEiBMRKkRficIDqO2mD3beM2tJVZiIVOPV_LzYukWuHadqPIFdtuwLoAlXDPUEVN0LuWi4lB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ریکاردو ساپینتو سرمربی‌سابق‌استقلال‌که در روز های اخیر با عقد قراردادی به پافوس قبرس پیوست با این باشگاه قهرمان‌جام‌حدفی شد. از معروف ترین بازیکنان این تیم میتوان به داوید لوئیز مدافع سابق چلسی و آرسنال با اون موهای خوشکلش یاد کرد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26856" target="_blank">📅 01:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26854">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLbnlz72t8ZjFqZUgCMwjYmEeggfC5xnvGDDXeMVBcdxx3QxZMWR_I8GORrLrfZm7EAm8SBWOOAAqP_9Y3M2fLy7CsHZsOWH2h7BrKK-4qR4i8edGes_7k20ac9Ut1nIwtQ0NuAHlIeMJmrgQS98EbvkFNcSM5To5OCNNXtHJuC_6iHmDXgec5xcAQk8HmUnj6iLImsZvLEcqxqTHwyqZDTELJFn5IPynna9jgoX1AwPpUTd1iNARBPDsANbs76TMlKhQzMByNNCUbBtWhAba9qiZkz_f0j5ADOv_mlIKnI-QSkwVhIFz3CIYbguY-NaqbpiV1NgSDhtTogwQYySbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RpG5N-ZLDcL1B_PR7KwjAT-z4dil1syubaox35gB_s6lkKYofpjHAj1c1GVtIM2Vsav1iAIn79s7hW1up20iB4GQse0SKCMvcSXgnwi1ObrNl5vzDrBDtR7BOo-UQu_g4uJ6OM4fsawrSWAMEN7scdXHkb79Te6OnfywS0ntvp3-5X9H8jeSx-Pde4ZV7ZxeJDZjwh7NvPBrpO3MvoY4mtHoinTXp7QWB_Z3-JLpu8sxsN0kZPNg2vefSzu1swTjFFkdQcZNrYeZEkpKcR81r3c_SNaR--JSgcPXHd_6V0Ues8F356j_RQAXZrXc_VbVYnqocQnKe2lCeKXc2bCweQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌وتاریخ‌برگزاری‌دیدارهای‌ سه‌ هفته ابتدایی فصل جدید رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26854" target="_blank">📅 01:34 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26853">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NBO-_Kwd4Xgzz9gj-f_SbV_bCITtVJuyDps2v4mF58J8gpPxUmAOWsKni0yv_LCFae5WL5XIwVECmSWceRVh3FtfPZ468U0pmhFKHqmuQ4e_OYfMEDWLLCkcC3OWb8zWDaOZxG7_vXlDqOat_fsFQD93oqTtnGHupcGvPti_HwDRVDOCxaqykd8TwfGiDulAfS0tIfl0aNJ4fXwuQzHkmrhALryF2KdH3Lnss3SE01HFJ1jTuEOfUeynPJDzm4EKAQ0oZzY2r-hspihrIefNNADOpY4N_WwMrBrnDkwRNBv434wAU76HrZ5_09pyKoBeG7pTcV6M0pSsv_t1gUfn0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه‌استقلال امروز پیشنهادمالی جدیدی به رامین‌ رضاییان داده‌که 15 میلیارد بالاتر قراردادیه که درنیم‌فصل امضا شده‌است. باشگاه به رضاییان گفته ظرف 48 ساعت آینده پاسخ نهایی خود را بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/26853" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26852">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YiUS8OyBfucTHzgiQRIkm_rZ8mcBxAq4A6t9aEIeEcAFKAbsPIk0wlcSuarMJwIm5PQyIJ2KCBKo7aI9Ur5_-JBPoyLjOPyV4Sx1-BlWmBNRlatkzn59Mwm-zY9nJGYpy2jgTRFix-hekjtMJ0EH7xahxMJnv3SV-jcBpI9yFFVEBmSEwm66eP3qAvlujvJu6wjHz1e1aJ4NLVYGGFNyDzxhzlm6YID9jj2SBxZmCJsisvsThX7gxDipUa7OwhAFLhGRYdio9ZWA5vNF2XxuA0LBLFaAYoIyslCsJbR94hIPmhhYC6fnuvQgw-fGrkHuhlwNYJeKIbGdyoqaSAIVjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/26852" target="_blank">📅 01:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26850">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eItsiETGpFimlN2r9aNEVPjGItr59ZaOEJ7cZScfNZ8zerC2H6PERjwdLsdWMRDSMSG1eeiHVpd-By0P2rsIvukCMPxUW82ubMObPEB_8JEtMeMK2V7IXfXb0nX41X-H-2rX9YE3Wuq3JV7k42CpPdc7QJuMoHlMWrEDxT0IsVIzYJ5cOp8xOUeDjx6rd81Z-13KJPvW4trtbYhlfx7ebYfBrtZ9C9Tqywz0yhy0IBZQxX-7ywYRoAlzltxZYzGckY-HU4RlKJjwd24Y-4qOfckuoJ0vQh5SGz4LHEhNO-kruBnKcKLWu02UZpgaKbyp0imr5XrbOQ61_T5XMig2Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
#اختصاصی_پرشیانا #فوری؛ مهدی تارتار سرمربی پرسپولیس درتماس با مدیریت باشگاه پرسپولیس‌خواستارجذب عثمان اندونگ مدافع میانی 26 ساله‌باشگاه‌اخمت گروژنی‌روسیه شد. مهدی تارتار از بین ایری و اندونگ یکی رو حتما میخواد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/26850" target="_blank">📅 00:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26849">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWV8e_tcJETGGJmHgD6KcAShOJOq-cTxalJz-eNUex9Sh3kADuqpHns1RrPfE7JtpSs-tqwbmKEiGkOqoHDNH0-h94mpYNSbeWuafni0SNGTn5tWAIfedbXrFM2ahaje4lpo_BnL38HbhpkAmqyOo-YDglyH65mf8FEzDoKwtEmnlB7IiIw1CKXQq2oUQmTHqU83ozPm5OjJd2DQL06zuDMq5ub_g-JqJ-RsRZxV2pnwRLJoIwGKldomktp2Mslo8hGaO_aTTI9FyLqxGJzqZVKjxGWzhUIex48aFRnHNL6p5S5kKOjWGbuJVxYC-X0E19whEDwFy51kDWAiQ_O-kV1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1f1e56c6a.mp4?token=aKQXajZAZqCw-7m1wX_a2TCSWQHTlxBlahjpwWrCv-nLSqz35AYBpjVCi1wn85d-ZrwRGx6Lpp1agP2PGwMbJYCGCmUrsUiHihtWq0P4jEgtNYWnZmEPfOL7HZuekMfTWFkCQr7a8E2xFwnkQ1XvPXS6QA5m9NZClQpcsqDH4yFpaNCpn18E0_1xz1YoHL6LTGqf4AhfrsKW_6dDecsUNIi_H4He8pQ-r9BqC8qdkI2fiG6zijWIGqqkDSsddO2EYOLi2b-KbndmWCeZELzwY3SH1IAyfT8qafjTn58YKHWwzlpLcgTHAw2qUZDXlf7ouJhJjc43_CYWW5xpzaHHWV8e_tcJETGGJmHgD6KcAShOJOq-cTxalJz-eNUex9Sh3kADuqpHns1RrPfE7JtpSs-tqwbmKEiGkOqoHDNH0-h94mpYNSbeWuafni0SNGTn5tWAIfedbXrFM2ahaje4lpo_BnL38HbhpkAmqyOo-YDglyH65mf8FEzDoKwtEmnlB7IiIw1CKXQq2oUQmTHqU83ozPm5OjJd2DQL06zuDMq5ub_g-JqJ-RsRZxV2pnwRLJoIwGKldomktp2Mslo8hGaO_aTTI9FyLqxGJzqZVKjxGWzhUIex48aFRnHNL6p5S5kKOjWGbuJVxYC-X0E19whEDwFy51kDWAiQ_O-kV1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
عادل فردوسی‌پور:
🔴
اگه قرار بود که من چاپلوس و دست‌ بوس باشم الان‌صداوسیمابودم‌و نود روداشتم. چراباید دست یه مسئول رو درمقابل‌جمعیت ببوسم؟ چراچنین چیزی روباید باور کنید؟ دست کسی رو نمیبوسم. هجمه عجیبی علیه اومده. همیشه کنار مردم هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26849" target="_blank">📅 00:44 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26847">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TwexBoXhtka_ipKVKopRBrEPwsuEvHAaB9282H-8a3uMD8kujJHZ2TWvSi2t7F1sKHEZop2my_sDgOoRQ9M4bldRrnE2NzOAsyDDeWtGcjZdQNWQa9tUzD3ECzvXQB0OfIJ5ttF_iRExOwvgzrf9OGOIBjbBl6I_ryffMGPR0BrhuEJknmnhFq5ln4iuVWpjqebLsHYHE02ssHKvxoDcEgaDeXGnAPhhhbSiLzzswvj98bnnaxmCDMh2mCNVdI7a4lAOUrG11BVXR3ibAD2QRfpOiZueqeFZRu-fC4KHN7hmN9l4xjwR8EWBXW4dJmbemeUBhmfacSxrbpKh2hUsbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
بازی دوستانه آبی‌اناری‌ ها برابر تیم سابق جود بلینگهام در لیگ برتر انگلیس
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26847" target="_blank">📅 00:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26846">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mP4lzvFHn8POlgc-mTJ2_aYetcKeDbgGeY2rsWQ8qJYLZ14tZwkwHnrCzyBcUy5OuynKRBGyZN1yQedGAcCA2OQtmV3UmUoOrzJ8diIy0Ye15jMiUJSNxufdo5BtfBdzgwYTosJ60gLv-DrBYneKzv21IrKkubFuKrAkoccQZFhre_8XMOg7JX1irpagDkkafvIWONwqkirFmbi6s_Era5EYqTTZ7hrAtxSejH8PPdcPIOGKiegW3e73dqj6uWmbvm9IenbypbyaASw5NXXOnyJLPvl49bIVuNb1BJ73vkx9QOK6iApPm6SMGzJwPi2mpld5VQc_Rz2AZFshd6vM3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#تکمیلی؛ کارلوس اسپی مهاجم 21 ساله لوانته بزودی با قراردادی 4 ساله به رئال خواهد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26846" target="_blank">📅 00:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26845">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ND_3VJCLeWdwvl3AJ3h6t9Brwt2euedKH82p-PkY856B6vT8xhz5HKoJodDN2ARNzw9RIVVAHbJ_N2oeZxaRq7p7DMLLWjtRE6iA5WRFKbuXdvJuAKXSpbtT80ph2OP_l9t3V0GC04LxbENQS438vbXeGukMikbFpqeNvRXhP238t-UJ36KYdF5bKm1VOA-NYHKdZ3CY6BQRRBlWHi6lggS5-D8nG4EnX074N4w9sKdFQsH4GFawoS6b1Yq0_eNVc1-BHsUwO4hCfDS4DtAAowmtNFc10hBPrS1Yfc4n8MrQ1icAMeTE5G9gi7xABKgnQ3ch2wD3oqK6fpYkyf8XWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دو گزینه نهایی تیم‌پرسپولیس برای جانشینی میلاد محمدی؛ اولویت مهدی تاتار مدافع جوان گل گهری‌ها شد.
🔴
باشگاه پرسپولیس بعد از توافق شخصی با امیر جعفری مدافع چپ 25 ساله گل گهر سیرجان؛ امروز صبح با ارسال نامه‌ ای به این باشگاه خواستار…</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26845" target="_blank">📅 23:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26844">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npLRAEP0RaCestX3TaO8iPw8VW63FUR1aYVJF1g82E8QPVuxxIQAbBaOHuiGZXd_tzVgSoovA5_OpwYQ32N06BrYkkSVw83U7Lw1TRCcXTNKq9Uqr0jxt4eOdRRzv2Kye1N2bs5dZv3kjMczm8X6Htu8NwmxsKBh1OrlcSoDdJsxdI7PR7uAJfwLEnUKOCmJsIwdeyqtDtqMlYog-VEqZDjB6VzAvdtP3w3XpAnuRT6qiLAVmGv755Adw32-gdt-gyRR1cvV1Ar-WH0DFW75eiZy9HafzNx90Nx9S1d2HNAM7dNuQj1mUuhb-Fn3UyJ3GzZR1-8FGtAD-i-QcCD0ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل…</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26844" target="_blank">📅 23:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26843">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aiHaP1wBYQ0JXHXds86ID2yo9pu_qVGJCHT7RCfVFJ39NkXcSptmwjI0HhaK2UohJleM2AngeCkl6BrT4U7cgkVR9Tk-OmH-T-1ElSdZyTtxETroJ58QyQez86i6K1srRhU7rmxNwlJrNAq48AKVVZxL_xM01wG0MrsB1zT4-ROL-BKTz9uLSeSxw7ZULkqFZXufstqpk1Drtjrr6bmyDgDCUqkQDJNKrPxOlJzc-UCUXCGgJXd9Ij5BhbRCzmM2-d1L5qXYXktxFTJHwQzJtEXsCED5glbl4X37nU-oUtrC4RjNZ94GKv4IM9hyR1tlUD1ov9_GYictYCdi49JSBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
طبق اخبار دریافتی رسانه پرشیانا؛
سعید دقیقی سرمربی جوان سابق پیکان مذاکرات مثبتی با باشگاه‌صنعت‌نفت‌آبادان داشته و احتمال اینکه بزودی قرارداد دو ساله‌ای با این تیم امضا کند زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26843" target="_blank">📅 22:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26841">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPIZ22TyxfKgQiPTy2qGO_o1zp39tv98bZa33wAUS_dWKP4yr9AOJ-ilFHkozSCiaxrw4zqcfE3RloBV696VD8io00G5dASvwLiQ6hT-hStsnGZNLQV9L2B2SxauxxYnviygtm0agvxix2qoSIwv51rCNpDf5_cW4lkbOWhloGUxyfjRiSFU60GWJFfa6Z87QA-xQOCSsixUIn08msim99kjdfsAGmDUbNc-GAMPTU8SnYpufKnL7sLj5Xi202daDWzv_0Zh0glvGnH3c7uWJ14jok0Lrvu354ApK8u8M24dlkKZkE4pMF5OPOC6-wPc8fyT9VOexERGsXi0io2vig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین‌گل‌زده درسن 35 سالگی یا بالاتر در 5 لیگ معتبر اروپا؛ کریس رونالدو درفصل 2020/21 توانست 29 گل‌برای‌یوونتوس به‌ثمر برساند. او یکی ازتنها 6 بازیکنیست‌که پس‌از 35سالگی، موفق شده بالای 20 گل در یک فصل از پنج لیگ معتبر اروپایی بزند! روبرت لواندوفسکی با27گل در یک فصل برای بارسلونا در رده دوم این جدول قرار دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26841" target="_blank">📅 22:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26840">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjupyPt1pcGAlq8iz0Erbv8JwRkE3fAK1G2X4jt1Qho0AZEo8-Bf_NJaJwekmJJ-yrAhvuV8D6WGzJvnbqyQxnxuthu-b0-ji4Z-fKA9PUvclSjRJfWAw9J1mjlUuoh6J2W9Ez5S-l5V2_R1A9Nxld0Xdg7JwtqhpW9SREuyuUM8nBOYyyIQDVBNS3zNN_1gzXO5hII3jAsehGFAb8kVHXhLkZfcAtxHznudRjq_-iOT8uhG34Wm22rMlWrvkm5eWxdnTlL_8Nx7STOjxKUzSR1305PxKH6KOXhk-4CZxtWjhmkBpi9TS1Ti4qIUkkEFFMTbTIJlu9MYy5AE_P95dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇸
نشریه‌کوپه: باشگاه‌فولام به‌درخواست آلوارو آربلوا سرمربی‌جدید خود؛ باپرداخت 70 میلیون یورو به‌ رئال مادرید گونزالو گارسیا مهاجم جوان کهکشانی ها رو با قراردادی سه ساله به خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26840" target="_blank">📅 22:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26839">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mHuQ1yS4bVy7Tm1rY7IX71pmbLoNKRTRTL-ZXNPZ8ivbpCuZJmPzYYCS9usqNC6Rqc8UM2zZAZ_YchLlDWvTrAs9-jacxlXPYjlyVmfClfcj5y0XLyXb2CwzMaSn7XYYWfmkd3pGKTPNxUuTNqgMAcp0vdCp4yZi1eQDS23x2Z3m4rvlWextCMyYp8N3VgG8zp6vOqkte2Mlb-1xN7lSDglntsKY4373r370HB-pAEagYJbnrmaokPKmDRyXcpUXlqw1M58RfPPd2h9Yec3CkvC1dr00_FWYjAr40y06IfmJF0miZpTsFYBrfwgVgmDdTD5-yOE_OYjY9Rd4F1AG-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26839" target="_blank">📅 21:54 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26838">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s4isEYp0s-xZLLlzq2Di7I2THPTywQ-Hb7i9wF45J4TGZOzoeVWSHWi2j3XW8Bc-f5llxw4nSbz5FKxW8gNryA2D4Dv4Et3c701QQ0ucVzmbGNqextyyPY_3V8MjWNu5enulXAPTSaEB1Vj08z0CvkvuveFphgGjoBEXUZPcKG9SYP8wL137q3EkbjbysWZjKKJi0gy_hG2KvVSntn88VHKVGaSWVDUpmXyTNYD0B3RDI7nCB9kjaw8ffGHPkr_7Bddn5E_E8PeJIdnZr78-FsvSaEN68ara5-Pc-jqJX0sApovSAhSmogRYDcuvWdX850MNjry4p3VqlxJuHnedhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26838" target="_blank">📅 21:25 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26837">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WDUgBM_Q7R3msA2bC4s6pSnH7AMSLQxM0zEj2SR5yp3IqjyKRacI1DuM0S9t2y70uX9eCdUw26S7Z9o8dNuY-POYaoEl3OAvs_XTdtqerSK6VoDhpo95ShrZrIzBo-ykPNGfHgv1n4uSSmySffIlIkFSfXA4LKhmr1Cro-SibI6MiMlCZZKhuKCI8jARWHyerL5yNKGJMnSuJOINgTiFCqyO1a-h_FijRQAdmj6Po72H8WVtQjEKiqelZPuOpqjjw1wHdBH1jf6C_sBwXoNJlwoRiMihyj6SZzCFvIceUK7iEXTFcenBuhmPwuGvA_XnuQYETQWIId-wkGafrWgxPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پرسپولیس آلن‌هلیلوویچ‌هافبک‌کروات سابق بارسا رو به‌ اردوی‌سرخپوشان‌پایتخت در ترکیه دعوت کرده و قراره‌ظرف 48 ساعت آینده هلیلوویچ بعنوان‌بازیکن تستی در اردوی شاگردان مهدی تارتار حاضر شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26837" target="_blank">📅 21:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26836">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uhc5VxldOqbK9NCB3XlphwZGwT0_3iYWGHRu9XEjHqsloawgsEYVzfVAc0mq8_9OU4sGxmAiQJIQJew45RPWwTtC79WcPp39TdxKRCEk37lzLryeeXPE2ZxlDMaEMNvGE74byKYQv5dmlnaWl7xKNB2W-9xXiURefsCGwq7yj1oeEqRqtPbm3V7h7A8CJOlSoFuuuSzpKiRGbjyUtzZYrxJb_XCf2A105MAfggKr908ZuJIZxiR2utMYA4DckHkGKH2zCVOWyEcW_riizTWLYEEHHm9AcMmqZl3OG8qG_Xq3ovGILIj6oFRskPLsMpoiVNWpxyC3Z4kWkSbWzujC6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی‌رسانه پرشیانا؛ روزبه‌چشمی‌کاپیتان‌اول‌استقلال شب‌گذشته با رامین رضاییان تماس‌گرفته و ازاو خواسته‌دراستقلال بماند.
❌
پ.ن: دربین‌تمام‌آفرهای رضاییان رقم تیم استقلال بااختلاف خیلی‌زیاد از بقیه بیشتره. تاجرنیا گفته رقم مابالاترینه…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26836" target="_blank">📅 20:33 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26835">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=RQW0iNIJgAZofrNUpt9mmbM4ZP3Kle0bXuayo2N7eo-2AYFRGtSsJQ4YtJFjUXMmz0dvqIxH_Xje1egtponiFsTEXPThECnKp-8j7-KRBboiJBFbbKNF45lqv0J2PHJmqIVtEX8bERSQLt6ID5nmH4mKDBws_bWY0AA269s2mFtpMnguv_VkaMN5p44hnO0I4fiyqg6ji_S_-LYv7beWD1cMjSUN_cqec1Sq_Rfy7BXnVWLKfXuBprMSmnaIQZvFtMizLCLSsP8TCKL8EQSPmxjz5GyI0QDUD7QuxskXBjxQ6u6vxLJXxLJkSU03n4RC-K8Ey7P4QcmWr_dqYVo4bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/391acb06fd.mp4?token=RQW0iNIJgAZofrNUpt9mmbM4ZP3Kle0bXuayo2N7eo-2AYFRGtSsJQ4YtJFjUXMmz0dvqIxH_Xje1egtponiFsTEXPThECnKp-8j7-KRBboiJBFbbKNF45lqv0J2PHJmqIVtEX8bERSQLt6ID5nmH4mKDBws_bWY0AA269s2mFtpMnguv_VkaMN5p44hnO0I4fiyqg6ji_S_-LYv7beWD1cMjSUN_cqec1Sq_Rfy7BXnVWLKfXuBprMSmnaIQZvFtMizLCLSsP8TCKL8EQSPmxjz5GyI0QDUD7QuxskXBjxQ6u6vxLJXxLJkSU03n4RC-K8Ey7P4QcmWr_dqYVo4bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇵🇹
کریستیانو رونالدو:
در باشگاه رئال مادرید اگرموقعیت یا پنالتی خراب میکردم، در اتاقم رو میبستم و توی تاریکی با خودم حرف میزدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26835" target="_blank">📅 20:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26834">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LKdElVOfTgpmtEHrhWA6_-71VWgJGLnBQrdywx4yAJUqWdAoEXOLMv8JA8PdoEcy-QHEE4BhY7VrNWXblkgL7QZqiSRj3JJmgW827mqMQMPygHflFRZF-pV3j2ND2rfiv8ksP4T_wQcNdAriviVadTTevGzs4o_8U-zIfnXY7fG_w7fpVXFWQ7NPvJhEuQs4NEz9lH7OnXzw8K42kyc4jHfVZu8W_9cUa8wbzpL2Ah30FQEL1O_fj8PTt_-sHqAXI3iyODJ13jy8grmQ6q_cvsMLMDFzlDck2nfqVP3_ccz1t6dZV-apnT3VAMw6kEX9o1p6vlRylfPZcJ4q3X123w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26834" target="_blank">📅 19:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26833">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vR3KraQgi9AOntv5YMYSaAdyPUxs7mEH7CNQ1Ni8p_osKrQzOTI1NWfOHQQm50knwyx3ytjb24Xo03tUpHQKv-GllpIIYA_aZAOMefpFPnf6jNcbmrm_TedRyelGSfwdFgMsLXWrvXMtGxZc1go6Mius6MlApO4mG7iAOBtD-eNIMG2c3D0tAe2RNoBxtWhXHbzKNTl_eFdOcMX3kyflRVq4rdSA2pGowWZOZePTp_q5yzY26f4seq308VQwobZ6xJzvHSANcYj3GCzaKQFv4EyXC7aavENi-tCswoEO2gmKKoT4gDQezZmr_sK5StUXjbrBjuo4mK0f8bud5iIR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌شنیده‌های‌رسانه‌پرشیانا؛محمد رجائیان مدیرعامل‌سابق‌آلومینیوم‌اراک یکی دیگر از گزینه‌های علی تاجرنیا و هلدینگ خلیج فارس برای مدیر عاملی باشگاه استقلال به شمار می‌ آید. علی فتح الله زاده، سعید آذری و محمد رجائیان سه گزینه فعلی هلدینگ برای سمت مدیرعاملی…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26833" target="_blank">📅 19:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26832">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iukcHtoj-Lg3tPS2kWzR1iPJdvdrxJ356QEF3DtaLnEjqehnUIveI9fQy3qhQA4A6VPPhZiW_ezyncXePPiPSyxyG9gOHZRwCWRnzdjmiMfO3mxjSKxwTzFbpw62GytgQkwsVTdrP5lhHj9qR9kMQFlogPGFzQPmir-KODEoAFOHJEAQaif_nj7BbARDIXiUYHvJwHK6hoeQz2r0SAjOAZAMK0-itrcZHczNSAcV1URP6ToQdewayEau3SEI0Jv18rX_ACWR-PQWhG-gxC5AFJNyJEKJmVKC4sKWTF5QsqkhEDDVpYNapA09kVNoNywsSE_7OY5FS5L0zN9twooWVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام مالک باشگاه خیبر خرم آباد؛ پیوستن مسعود محبی مدافع‌میانی22ساله این تیم به باشگاه روسی منتفی شده‌است و بزودی به تمرینات خیبر باز خواهد گشت. رضایت نامه محبی 70 میلیارد تومانه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26832" target="_blank">📅 18:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26831">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Y_5UVKrECumq3trU5fg1mWEXyf86Vu-bNDVfdXmwWwDpaxtIgF6PXC5yBPDeAcYZB0q8UwXsjS4Hd00yfkG2eItehzc9zDkbsXB01GAZdxZ6ULJ1v-fYp5uSvQTHPn1KZ31kBfChlkiDZ-P8VP3VfuqAEiFPCXJG029t_bU1rBizTFdf8_BZt4cZLOf0Iqtf0w37p0hSs8Ip0ym3I-9CKhdF7CQF6y7asB6wrfHoeWkQeG3_6ACLURwJB4LdOgtya9N8St7QpqYEzfVMme4ZWyucEP_3H_XDS2tkVYV3xU9EB8-jYwN15xmS3seviZ-8gOQashRXWradK1wk4gRgRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2c2e717da.mp4?token=Y_5UVKrECumq3trU5fg1mWEXyf86Vu-bNDVfdXmwWwDpaxtIgF6PXC5yBPDeAcYZB0q8UwXsjS4Hd00yfkG2eItehzc9zDkbsXB01GAZdxZ6ULJ1v-fYp5uSvQTHPn1KZ31kBfChlkiDZ-P8VP3VfuqAEiFPCXJG029t_bU1rBizTFdf8_BZt4cZLOf0Iqtf0w37p0hSs8Ip0ym3I-9CKhdF7CQF6y7asB6wrfHoeWkQeG3_6ACLURwJB4LdOgtya9N8St7QpqYEzfVMme4ZWyucEP_3H_XDS2tkVYV3xU9EB8-jYwN15xmS3seviZ-8gOQashRXWradK1wk4gRgRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
نصحیت‌جالب‌کریس‌رونالدواسطوره پرتغالی فوتبال جهان به کیلیان امباپه ستاره رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26831" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26830">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_kaQJ-Ydej4asR69z9UQEzCX0m7iCxtZXXbIab7q_Lg7-VptcJHa6ifsCVys7gGDfxm3K4gHuBIsTT8QEFmRoWhamxj8riEYcfN-EED0yRIzbbBd9YMm8AsUKGzgmnz_azO84YJpBH6f9hpdgblOp2StDKNqPzaDRQGjyDGaRw_W8lYacriwpiZRIITYxmcY3gey1A1a7mnzDRlhQIitZpxhrGPVvvJTv3n_QvbGKiXNBpD8ZSiFDvXz3soqm2auefgYy9rx-WH9I65YgY2EU7y_o2Jl2h09l0SpBEwVwQxKGghY3aDqIIgCiqMhTDrOFNmnOWGAIxWCyP9P9YncA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
کادناسر: تمام‌توافقات‌بین‌دوباشگاه منچستر سیتی و رئال مادرید انجام شده و باشگاه اسپانیایی تاساعات آینده پوستر رودری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26830" target="_blank">📅 18:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26828">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AxjAW9flvgfwAbsDUeuZarLHEn8e-zAzOUBsI_8uYSuMKtHtqTVNprRwBzHA6IDD_ZOyLI1SjrnnnJLWpHoO8YrmFOqtbBpLvOBBqmRkEeq_FfdL_ReCtkdx9Q2JzeZw3fzcmAHlgGT0_X6ZZGsLF0z2BWADE_c1NgW5wb9xA3KS1wS65LS4KNB8iJrB2nq0BXOZ5kX2stucDprT0rAtQtM60k3R4zdsw0PEoPwn-JXAKV7gghS2d89GQB6LSnYKZ6DJ_1icFCUMMDNfXSeISZpXsRj1TFtrDEh5ECEUqhHD7vOHDX-t6o4cT7f2QNuNz6aLmWU4p64bs_vMh5lI5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
مصاحبه‌احساسی همسر انزو فرناندز ستاره چلسی:
تو 16 سالگی باانزو آشنا شدم و بعد یکی دو سال قرارگذاشتن باهمو شروع کردیم، وقتی که دیگه باهم بودیم.تویه‌خونه کوچیک که ایجنتش کرایه مارو میداد زندگی می‌کردیم؛ وقتی دخترمون به دنیا اومد ماهنوز اونقدردرآمد نداشتیم و براش‌ لباس‌های دست دوم میخریدیم صبحامیرفتیم‌ایستگاه اتوبوس و اون میرفت تمرینش منم گاهی وقتا پیاده تا سرکار خودم میرفتم. ماخیلی‌تو اون‌دوران سختی کشیدیم و گاهی وقتاغذاواسه‌خوردن کم‌می‌آوردیم ولی تلاش هممون بود که به اینجا رسیدیم‌. روزی که انزو خواست مارو ترک کنه بهش گفتم به یاد بیار چقدر سختی کشیدیم باهم الان‌که‌وضعمون خوب شدع زندگیمون رو خراب نکن که خوشبختانه‌خرابش‌نکرد و باهم‌زندگی میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26828" target="_blank">📅 18:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26827">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPWi75dMI3BZdaEG6gF7v2zqkAgd2ylPeGxuF30Bn60sD6ngZ4tJ1MY6cyLXgITVkrg1AncD6tER0SFWdt1IcpjA6hhfdnzFXGojyBNsPUAniRLl_5_yF4G4-v00-fIgWhdr7kMSFmZH0fejTUm2JdfH_bcYC445T42DEFJhQ-_pASW-YlfJviXh31-e0BiGtOLKccY4zlMK14buTBfkbozy833ueF0Faa__ja_wE5sotsqbtLGcor4HQGz0LPoSWaWc8qKVjuNsn5gToQ05MEEKyy9nltsI1jf8JrfYSHHy-Gu3yhdzSglObY0i9A44g6MumFdMBJjajEX35DaHBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ترکیب‌تیم‌پرسپولیس برای دیدار دوستانه امروز مقابل آلانیا اسپور با حضور بازیکنان جدید این تیم؛ مسابقه دو تیم از ساعت 17:30 شروع شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26827" target="_blank">📅 17:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26826">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=lbWEGrVtmy5GeZWCh7x63IshPykTTN9VMHGwx_QX-CN9J2-06Ym_7DWIXIf5VtGvlz9wxyv-4LuBF0wDfcvVJlNaWfUd0nvoPmBMiIQ82csxTl96zS4SaUDs3I8ZA1LBHineHMXYRAcJU27bo1e7bEvXGRXf47JxytLpF28fF6se_7XKEBVUjkMM0SDVcYErDAvrwwGaZrSmuiVHcY_5077WH0SI0JSdT2NlaQa5YEsDC_vY063cmd3jdXy_Dp7W0JPXloslAF_AouFMAtGm0e_aQdRIbh8OhFYu5saNNz4Dor2xcrzNAefgi6Jcl3EHiPfN1fdZPPAw0v3U0zRweA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/337c4609b0.mp4?token=lbWEGrVtmy5GeZWCh7x63IshPykTTN9VMHGwx_QX-CN9J2-06Ym_7DWIXIf5VtGvlz9wxyv-4LuBF0wDfcvVJlNaWfUd0nvoPmBMiIQ82csxTl96zS4SaUDs3I8ZA1LBHineHMXYRAcJU27bo1e7bEvXGRXf47JxytLpF28fF6se_7XKEBVUjkMM0SDVcYErDAvrwwGaZrSmuiVHcY_5077WH0SI0JSdT2NlaQa5YEsDC_vY063cmd3jdXy_Dp7W0JPXloslAF_AouFMAtGm0e_aQdRIbh8OhFYu5saNNz4Dor2xcrzNAefgi6Jcl3EHiPfN1fdZPPAw0v3U0zRweA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های حامد حدادی اسطوره‌بسکتبال ایران درباره علی آقا دایی بهترین ورزشکار تاریخ ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26826" target="_blank">📅 17:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26825">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lexij0HqojI-Crky8S3se1zgoruMR5OgrgNN3Ad_tl6hnMneEDWc8Yk2_iF3-08mVtwhCgMTAUMzfp4G5IMw0MFmTXnucf59eULjgnWe1BY0Ni_BGTxlhzaIgC6wBnqmHf_zihtr7JmPc1-DICIXH8KnOEZGv-KPdS_lcB9M6ZbbLWpDkalB5HZxT4ceTZ-GZfAwJkYmK51oZqnIQcHmabtFP59VEWx5BmlXIvF_iGSnw8PSG6dq2Y-66bI3EKqZj4lfC_fECVCyes-T_rGZJ8wu7zMb0-6jp_wZE-G6xby0bbqrLHUxzjex7JxMspoVRX7QnuQiVu8-zqsQWaikTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26825" target="_blank">📅 16:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=jBzEFRjHEU695l7wC0Oy_mkXdHS0wkjWdswpmFQftBcdqGXJ9mexxGIM285BOv-67byb7pFRmjv4V4LeaN9EEdfDzWfTzUtKEkqr5tpc-_SuzaG7QraDP6ezmG5cCowHbOQZ4vZhEZ5Yyn4tMc6Dnv3R3DlVsP-gsraO2flQ4IMQf9LMbRl6UlfwnzY5l8oKljDKe8AdFVTbjfPyPpTtLlZHyEu0gPNegk-vJyGC0LhUqzHi4illmvc1KbgOaiu_bqi7bIX2oZ4cDk-ed5SpQ7nz8OChrbbdQltwAnGDIUeeBY9GcPKvjOXV8DUlhCCNjbrg0UZqArmkFLS3vcweMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f949cdb55.mp4?token=jBzEFRjHEU695l7wC0Oy_mkXdHS0wkjWdswpmFQftBcdqGXJ9mexxGIM285BOv-67byb7pFRmjv4V4LeaN9EEdfDzWfTzUtKEkqr5tpc-_SuzaG7QraDP6ezmG5cCowHbOQZ4vZhEZ5Yyn4tMc6Dnv3R3DlVsP-gsraO2flQ4IMQf9LMbRl6UlfwnzY5l8oKljDKe8AdFVTbjfPyPpTtLlZHyEu0gPNegk-vJyGC0LhUqzHi4illmvc1KbgOaiu_bqi7bIX2oZ4cDk-ed5SpQ7nz8OChrbbdQltwAnGDIUeeBY9GcPKvjOXV8DUlhCCNjbrg0UZqArmkFLS3vcweMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26824" target="_blank">📅 16:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/diEChv3HdX92DKHg8bTRwMgKmwqpAdWqb5U8UpcQTz2ov4T4bWBNswL8MuM3r2SMt6A1SUna9oJm6tQSFdjAD1SD7w1AG-vm-Bi9992xDzPWX-pXGnKI6UoOo8Y25BJvwMah8A3exoJhsOai3xOUwKMk6MEM1HIbR8nl24ms0TImxrMuF07yQ8xTBjuohebqxCxsLexKIv5nZrSI13EtyRoXpkNDO_iwJ6BBt74Tloen9vEocghUijTBFG54fUcEQ7ADkbV6W42098kH3bIZg52lc4gtvT6xfOMuYyuyJL5-f3cyIDpRPz5_70aLX-rEwNfvlfYNCMpWSXaxM1wHhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدئوی جدید یامال و دوست دخترش؛ یامال: اگه یه دختر جذاب‌تر و خوشگل‌تر از این پیدا کردید من ابروهامو میزنم. پارتنر من از همه خوشکل تره:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26823" target="_blank">📅 16:22 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GJmIiCc0YhxNT4Bysrxi92NLxkUUer62fnPJ-QWq_qTqLDJvq3SboAsw0y5_b9SObSFNT-vAlgpd13X83bk7tNg9vQhsoiniUbG5KcD0k2IDVmC4Mza0ikz8kFkzwqRouO0hLWAhToo1Q6_cMkjxd9jo3SjroKyJDMNB-0EUk4xFdgi_BD2wjxAvuedgo7mRIWJJuqYT6ManRjQzVcEBZgjPYYneRFePazRF1z8FjcLI5clN3ctikAu6e9gv6pcHcbwMV_vp1gWEcvuIJVNZh5q5oXztUkRowXsYhiNgcfmU8Ux8tRfpleBJuCeLSpbNIiZYLeYzC98GxTH5iLFYFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نشریه‌مارکا: بارسا تصمیم‌گرفته‌که‌بند فسخ قرار داد30میلیون‌یورویی‌مارکوس‌رشفورد رو فعال نکنه. بارسلونا به سران منچستر یونایتد اطلاع داده برای خرید رشفورد نهایتا 15 میلیون یورو هزینه میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26822" target="_blank">📅 16:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=nhNdBmAtAo6EvhcL1Pj9tZZxEqLvy-oVBOGC6GXD4t5o17LHWMPURu57hWhgDY737VdQjbXFbXetQN2ecMEQb1XIFcXEdHztEJGsGTLR6iRgEcdEkPw6nFxafoENtGwVHRGY0vaKiByhgTyQp_lvDqpNIxH9XGf5NlX3_Y3RVUMAbeXz5AsgvXXIbb0nHy0BO3YZEP-4ANWB6molZAJHrj77DkyGl6oBamb2DAVhzEBLT_kDksoBEgaGr4ABYznwAX1u4CkfWbFdtmwk32hJU7ZlfVYBRb3SnpLgsLCcaPskaQeGmkxwIPnWnP4Onq0AeFgIGGlyO_ROcrU1tyxzjjuvEc6N6B57Kk5kyzblrgDSGGT3CWQK121mvC0-I7CaLJQoUns-o7WQtTtwoyCK5YN2nPR78JgyAkLWPYdEUkIep74quWsQCSfU0O4wbyCjVpdavet4Os-gZ7y5XJFWi4npFja2qko9JzEjK-fIsIzWf1fJNBujr6TmdG5QJh9RqcGeRkeYbe_gSSEJcR3yoM9DxTGXLNSnBahexnB6nM61wBfxCQh2Xu4yYHsGcyYoNDZWyOpEgVRpdaF2Aa8suUMbu36mnJ4D4l33w1ZyGlCRtz6qby2puMRCTG4AIhZSlJd19wp4IQsyA2af5sHZ-FF6Mt0cVJgyo8Ro3t1p3TQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1d53ae06d.mp4?token=nhNdBmAtAo6EvhcL1Pj9tZZxEqLvy-oVBOGC6GXD4t5o17LHWMPURu57hWhgDY737VdQjbXFbXetQN2ecMEQb1XIFcXEdHztEJGsGTLR6iRgEcdEkPw6nFxafoENtGwVHRGY0vaKiByhgTyQp_lvDqpNIxH9XGf5NlX3_Y3RVUMAbeXz5AsgvXXIbb0nHy0BO3YZEP-4ANWB6molZAJHrj77DkyGl6oBamb2DAVhzEBLT_kDksoBEgaGr4ABYznwAX1u4CkfWbFdtmwk32hJU7ZlfVYBRb3SnpLgsLCcaPskaQeGmkxwIPnWnP4Onq0AeFgIGGlyO_ROcrU1tyxzjjuvEc6N6B57Kk5kyzblrgDSGGT3CWQK121mvC0-I7CaLJQoUns-o7WQtTtwoyCK5YN2nPR78JgyAkLWPYdEUkIep74quWsQCSfU0O4wbyCjVpdavet4Os-gZ7y5XJFWi4npFja2qko9JzEjK-fIsIzWf1fJNBujr6TmdG5QJh9RqcGeRkeYbe_gSSEJcR3yoM9DxTGXLNSnBahexnB6nM61wBfxCQh2Xu4yYHsGcyYoNDZWyOpEgVRpdaF2Aa8suUMbu36mnJ4D4l33w1ZyGlCRtz6qby2puMRCTG4AIhZSlJd19wp4IQsyA2af5sHZ-FF6Mt0cVJgyo8Ro3t1p3TQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی نوستالژی از درخشش فوق العاده ایسکو ستاره تیم ملی اسپانیا در فصل 2012/13 با پیراهن مالاگا که باعث شد رئال مادرید او رو بخره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26821" target="_blank">📅 15:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=A9T06mhlDvWTqMcB5rsF5iMlm26sdo8sY4_pJhs3NmknOLqemMWwQDLQaz9DD3FAsfBiLGGa0QJQgEw3oljbxlOWjtoTQG9L70J5yQhm-FS9FHX4Q_rR_pybhDnxGmJ7M8BZxU9bMGVGxu8nqu4uIe0ZUPAjEzGAMFw_TIkOKAnyIaz9_4RrIxu1zKH9qDCy-2MD6-jJP-gH_WdAwEeLTLJxA1scJsTTtb0wJaS0YHH0YmbWjDuyjN1l36866ZTPj3q-n1k2QGz_3YAUq-XgwU5Mzm9PIG8AhayeEbro_Iq5vEAHlJSfPyX7t89Dz-YUtoP2bG2t5AFB0PgyDBykSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2998bd2af.mp4?token=A9T06mhlDvWTqMcB5rsF5iMlm26sdo8sY4_pJhs3NmknOLqemMWwQDLQaz9DD3FAsfBiLGGa0QJQgEw3oljbxlOWjtoTQG9L70J5yQhm-FS9FHX4Q_rR_pybhDnxGmJ7M8BZxU9bMGVGxu8nqu4uIe0ZUPAjEzGAMFw_TIkOKAnyIaz9_4RrIxu1zKH9qDCy-2MD6-jJP-gH_WdAwEeLTLJxA1scJsTTtb0wJaS0YHH0YmbWjDuyjN1l36866ZTPj3q-n1k2QGz_3YAUq-XgwU5Mzm9PIG8AhayeEbro_Iq5vEAHlJSfPyX7t89Dz-YUtoP2bG2t5AFB0PgyDBykSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارگردانیکه‌سال‌هابهمون‌رکب زد؛
ویدیویی که از گواردیولا درمجازی‌وایرال شده بود، طوری تدوین شده‌بود که انگاراوروی‌نیمکت برای یک صندلی خالی در حال توضیح دادن تاکتیک‌هاست و همین موضوع سوژه کاربران شد. اما تصاویر کامل نشان داد ماجرا کاملاً متفاوت بوده؛ پپ در واقع مشغول صحبت با اعضای کادر فنی تیم خود بوده و کات دوربین باعث شده چنین برداشت اشتباهی شکل بگیرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26820" target="_blank">📅 15:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cECzsJPv9LkqqZai1gBZgtvclwsubTOhQKkKhwl5fwOJYnuvL9hxRcCGNofkCZbIqyciX1qGf5CCjpTA3rmRjzXxykhrBZJCVwC5tO1v50dBMk-yD9FOv_TnRhntYNX7LIZ0R0k_6jtAObe6k3F5U0FPrCeT1XoiX8sDzrXrhJ7TQdu_0extd7krPpK8_zWRUz6c4jZLNn_DnyyZGX2bnp9bOkWrQeWCIhxv8HqMraiaHxwAfyjGIURblcVhjLcHtLJ6OGtoPnFzCVswVW7SQhk3cpuDG54Ejnpcv1mcbCe8OcKCPMpyzMtz5sGXue3YKKEntl3hkM8IREtOuAfaeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26819" target="_blank">📅 15:05 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jdhsIHBzNQB0aBp20Gp_omgj-5L_1tZ6DIisOuhHtEM7DBUANUKAtA39HXVRQKLX_e_MGKe-U9tOTERDXJW4kjnT6_V1eSrUkjOgHojPieWEn8UdoqMk9qC_WK5C1vgjv_omL-qQIV2G-8VvixDOqbwdTQoy7dCka_dd3GXcUCs20AAzrAwNoAe0wpIM2uKJ3EOVWmZN406dq5cvaiNTmDuuwaOWKNa9bfC2k7L9a6w5BTs80vNhaSLBRf_-cCKEGvcdsLDYV8n37U8KuQ064KjBc8CZzGepM6TWjoF9qgh48m5iL4bnrdb4oergLCBIkor9lZCsGlfTVioaiP5GCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
شرط‌اصلی‌باشگاه پرسپولیس برای قرارداد با ستاره‌سابق‌بارسا؛مدیریت‌ پرسپولیس با آلن هلیلوویچ گفته که‌مامشکلی‌برای‌عقد قرارداد باهات نداریم منتها قبل‌قرارداد دراردوی ترکیه بیا چندجلسه با تیم تمرین کن و اگه کادر فنی تیم اوکی داد قرارداد میبندیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/26818" target="_blank">📅 14:36 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GZk3rdOltzNgeNnd5EGNdZsl1b5weu94Ev-yaOaQhmqgk0ZD0kKZgQgs0_lFVXWNXPHR4mJcPjrIg2bM_uCOhWHd6znO_VZeND84GvBSX-ZbDM-S5o386liDjl8_vfroX--vRW5d9wVpAJcqbvJIzRUjfxxyhNVY4HicC84NRaDz9wGp56oAoRQSivzSI5MgISfR60tHT3_1DHC0B8GX-grbafpyZZ8-8ZI9LXk4LoTYCp1kjGq_IaDXfhBwERsIYS3s2Z5ZLAtTmbDK3U3s7VinqIQJ-RY-z-6li898SSddr5Vyc7ViGk-BdYnAb0N2ayAv4F_YIhQcWDZ2EMYkFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یه نفر راموس و پارادس روبه‌مبارزه دعوت کرده راموس انگار بدش نیومده و پست رو لایک کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26817" target="_blank">📅 14:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RORG26gItcwyl17wZTr5MbSMUUEiAyTjQMMp6CK64R6sr4mR0AcHbhVZ3cxpve91omqVDp52v8EvGkdOiEqrXAtD29Pdw2s6vGBbJL9jBBSHn5rO7LOnQ5VrCz4Ypw5nmhDpoJCwp7Crfoib95v0J-fBjU61P1E7M8nuk1jUu3fxio52LYZ62yxsLB81F9y2XTSkNsEtoTIliNFPcImMB1PYA-egpA-O6u-_TiTsQnukfUl0aDmf8YiU-mQTLU1orj5O-rXqGurhUDzO4SQOH2xoSSZfFuTzp9DyqUsh5LimuHJHNrjSB16AiVEGEsbUoyeu14-C--AED_AuOItryg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
بریز بپاش‌های چلسی طبق معمول ادامه داره؛ بعداز جذب مورگان راجرز بارقم 137 میلیون یورو؛ حالا سران چلسی باپرداخت 60 میلیون‌یورو با عقد قراردادی‌تاسال2032 ماکسنس لاکروا مدافع میانی 26ساله باشگاه کریستال پالاس رو خدمت گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26816" target="_blank">📅 13:50 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/By8vbNT6kp7MkebJbkKxEinDkzFF0_PiX9m8nUOPY7iLidtuSmC3az-EzlRVDl60k6i3d-By-7OjwhB50YAnozuWHWBRY8P6M5Aiwic-1wYdDUmj-akVVr4Mi2vX09K-sZhZWOpWlaPIQLQEhPhIvDuC2k-F5_jlbi7ESCqaJBLYM6cFcQ4Ni8ZsSt9I4Iz_kCDxlrHOzrkqECjPy9-E34Xk3wy5ZJVpSltWEc64kH7Ab-5bjukQ4X8dhRe4IvfW6oybHhd85-UNXnIUuSobhsi8aTW2Xb45YPeryUhE0H3X-utRSsNWQaX-xxdC6U294nPZx6YGy0_lVbOwRREPRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛روزبه‌چشمی‌کاپیتان‌استقلال ساعتی قبل قرارداد خود را به‌مدت‌یک فصل دیگر تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26815" target="_blank">📅 13:38 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26814">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBfhFZjx9B6V8DaGNqf_o6JHVWI_QH1SgdyGdkC4EjazKmXCAld8Qso4mrmiEqYqLqzJRaiKRriDKEKGE7Lw6MwVqRGn4WWpqEdCoNgBbP22tTr0iknYhkjJbPbgu_hJ5oRhCKeNAzhV6fJeo6fHM36JtYKZMcCrkGlXrdwKlB7ctWAgF52UFCF_XPZwIAXSX1TM8yPHgrerwcQpJSUAHol-nBheSjCKm_Z-NswLJyEU_4XCMu4w89xbVwjlcLbQChvRC5uoPPxDofCyxNQJQIHWfyOp9ESG52YzY9YsXimwHln1PrTQPkpPxtd7Al9zAe1_84HT_pn2Srzi83nduw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26814" target="_blank">📅 13:35 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mrNPNkLEem7an8qEV7Lk0bhCcQXsfpkKoqI9BT-qa72ZssVGmOLYXyEmbghSEmF4i7eUVYtFzBHjZlZBw38jToj4g2EIIyYawmq0gMOBo9n-Ew2g7lKcCI1nxuyxQyiUUNmfSiZQnrYj7JuIZBpA64Fi0p9E93Qz2BDPQwKhRkHzgQPfX7eJTa2cXShD09_wEhpADZe7t266K9DIleD9OHZ21djjqPuNseM6XgMvmnJh1EGqg0kHqCTN8aZmFUXr3kubyDUv0AR8C96C7G3QjBHgdfH_O1Vc6ArpDz_3P5hOF48zs4C_tcCzSuMA09FOP21J5ap8GLhWoyfv3C73Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkfFp7-e8W_v6D_SU8AK7kme8ip7hyaMwFBaKPFd8jnxT04ab3HKR5eNxeXPoiT0EXyxSM72Jbnj5y3EGGc3hnOp91Ztqm_BzDnFE06_-k2xyk4rpybsr2QgghK-7pFt7lZmuaO4logMYqqI5kzVkH-U9RhuGrE9MA-yb0jeVkB1um4JwadLO4LLuqFWvSJi0s22raIFW2JJS02l0tyeZz-CVg6M-nez_Wkmsta_ftxh4ub1yWiC0MPtqZ-GgZwzJnSgfc3kC87_NGtplG4MfoejDs8_8vE9x9bUZF5SeWoPg6TojehlQ_h62FWG0ENADxMbP6mc5UKw7Ov8fkr6xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RK0ES0I0KvT1h0lHgkVShZS9yHHqnTwGOfu--sXeBSG0Y4NXD_w9Y9y7ZjRoPY293akwpGfkAKy0YlNcjZJlRYkfwfcTJ52sytJOQCmfF2TLGGaJ4KrMi6gXuQ7KJrCZEffd4KzpV6TfyHM8WfvOrNJe45AlThpYWGfquj00gWW5iypLWE-tubOjoCdNqr1zuxC34Lhks9pMyjw97T3TCqwOV03IwqsF4HdwNX6WtNBoG6TKbQwTTQuAtAQGVrhHH78GZxZF0cM6qaZMqbucGGpYcmS1WQv6RTdJ1DvBqCN2LHHh6z5ntaX-YRNDxa8LA7t5svFqV-_L27_CfBH4Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ll0aEiPTErsFJvthK-4Q8dZ1TSAuOpkZf6ppzt1KUT7IsfDDVi4LKqm0_MYPmnZkaMVWIvqNE5iwXWa1M3ijR66s4H-whY1LZ3unUUHpA7ZLKVmSXdJogkI2wTZgypIaN0AlqEa7GevN2KXn_kQYLMVz90IAk_J8CNnjPIAzY3BMeZ5xCcawHNOWoIQChDiezgWHcZCNmM4xXJPcuQEJ2aVugWWc4sGC6vcAfaADRQ0Y3TEZpb2W0elo2lXXEiC0Xan5Hc0jKfiPh2KqNAbwVwib_Wgq5IKuSfR2lTxMxasvxV4hIyB4WxrJtB3792F19wlmLeIgi4DiJIefMMtX6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Po-9YdECqL3UUlqpoWaFpZe0tsLsQj2i1WX5dGZWyoaKt7fUEK5sHXQtX0IrkOnGolYoaMUuH32e6nOJvLV1_nm9GajDL5sqq9jaJTvkWDOtZ76PP8B4vrNAN6hmS2Z77x99JbVra9d1aKxpCl7SlqcaKBvvUus_c0KGCZ3tiWaw8BW4Ti8WjwJelT7zd0mCFuXuHp1f0SFv7cmlz2Z-_wA5kKRwSMpN2AHBRUDg-0sCY1aOjBDjPbaoDpZHxBVqW_fC52dcI482GIA0hFASiX_lC638mIX8DvZnT478hruuy6L0TPJoyeiUYUWCQrFJA84bN8qDuHijdcDMXtZTUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=nQL4eaVppGm1zbnqzuOx2c0lSNgAQiBmpiN8fvOOHqQ1IaHpHckOA83q6oglyJaZI64wM2nsMWUxbM8R_WUFFcEbxw-gXbO1P2XsRPc9_LqmCBGiueh1K82cXDNP1iy5vnNdXMkuUFJxL2Cnpqhcx4HLQ6WX51QgzossZqhA40nJoVhl2yhLLdAFJBFXdtMG16ilduZ2lAB2bSos8waellm0tvRb1y3cHf7yNNSa261IN0qKZ4gWd_oDL1mfraZfEF5_MifUbJsJz71dwpx-jVo-7Dh5EYHFUY_GWEukLLXHbpeJ6oKSdk7DDpbYMZFl3IKrNphbh-0BV5_071NvuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=nQL4eaVppGm1zbnqzuOx2c0lSNgAQiBmpiN8fvOOHqQ1IaHpHckOA83q6oglyJaZI64wM2nsMWUxbM8R_WUFFcEbxw-gXbO1P2XsRPc9_LqmCBGiueh1K82cXDNP1iy5vnNdXMkuUFJxL2Cnpqhcx4HLQ6WX51QgzossZqhA40nJoVhl2yhLLdAFJBFXdtMG16ilduZ2lAB2bSos8waellm0tvRb1y3cHf7yNNSa261IN0qKZ4gWd_oDL1mfraZfEF5_MifUbJsJz71dwpx-jVo-7Dh5EYHFUY_GWEukLLXHbpeJ6oKSdk7DDpbYMZFl3IKrNphbh-0BV5_071NvuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRJKaQ0Zx6T1wWI5H1smQ-AlBoW2TFWSP_r3TIhXrPkF6WlQ4bdTaySNX7AvUe2V3x9IIp-zW_DjdWPYyHBCoqymop-FqXeVNNNKN1zMhZ3ptykf1G9EnHep0gSDRm6i1CAqnGSuf47tXPbJItLsL2cgkW_-vU0N20lowDU46TBIb4vL568iPrw2f1YYAfd_0yFqlmTKrcNis4TL35XjeV3Va0ftUscdTKFozXrSTKyrSm0SPV8ReFTWZ-IUsqFO04QIKAeaGtVLHti646JtAt9GAZwJ77G87V860YAJiXWuwO8KbixadHRJdG9kDu4kEccBxMWePBYs6OCxF-EIuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUmIm8vWHaN15ukO7ist1GsWqQJou3OjC5Pr3IU932z9uAS1K8dJVs9qnHWnFnV9rCR9CNsdGkePF6GVx0geAj4erRYTKViXjCatXQrq2mg0IEMUSQDV3U_t6yjLvOhc8isCrpzNoFmoDjNj0t-hvCyLVgIWLRyYNoPCJkkl3k2O_UpzQELiY8eMwNDEJUKwDzhnfgZFJvMP_-GFncPY7f-7E-JYvCUdio2g9q2Sf2Er9q-MLVmKZ0J09CklU-koQfjR0oif1Bdab0OyVa419IH_TWG5V4Jdj2MpWEG7Nwqi4x3Ck76I6pe18XoQbqakHDU6pf-IvJSCtLUqgd1y3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IiSIBdwxOxd1jLZbAyjOhlrnXENrBfnWdekYnd4ewZ0l4WsVfaW4xxOu1pZ8zaTAcFxUF6IydLN9XVHqsIfa0qh3w1b3VkR0EsVP4TFJNVkwWregIs-2A0rTUQMQ58vAcm2d68yIfhaGwJFAIO0E4STLSNddgTHie9cyE3Oz9X7RO1ajdrhqhwIZ_plxR3VfWA0eyDvOQpHJ4saotrlIDQtQMuQxT_RotqvOCS2UZAFAbmykfM2k1J8vDf0dx8EXnmNqDFPW-HdG-r8-Dw9NzjvOx0Qk0npgtzNuYJmr2Rl5jIySynAYgN8MLHvD3sMStSdtvlVluWr2_WXs7iXNZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=J_3HOxSma914tQiZVzz2cANuhrVHwe8qV-HGUyP4I84Iu1DcrZNmhJTzz9wkzUm7_YEZbYn8QO4VPe5Fr0TVfBZMXZ17Zem4xGpGRGj0PMyB_aN0VW2ka14w5ku4R6qUBnnIJL1oH5dEKfCyRZART3m0DJ_EU6M_I2ySTTcGQaSSuqjcUyFeiLS1mGu_H7ScwM8p3uA3WjFJAZjEBnQsWJUqeGuuxkJQS8Eg0xH9e0u65vjw6OIn4WS4nOU7IbJs-P5t5kcrqfWl0mq7QDVP-MmeepFf9pcpRXCBI4M7D-UZnUnPeW1X6S_sg_-NGuUTqkwAbQn1ZRef0vXMbaB_yQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=J_3HOxSma914tQiZVzz2cANuhrVHwe8qV-HGUyP4I84Iu1DcrZNmhJTzz9wkzUm7_YEZbYn8QO4VPe5Fr0TVfBZMXZ17Zem4xGpGRGj0PMyB_aN0VW2ka14w5ku4R6qUBnnIJL1oH5dEKfCyRZART3m0DJ_EU6M_I2ySTTcGQaSSuqjcUyFeiLS1mGu_H7ScwM8p3uA3WjFJAZjEBnQsWJUqeGuuxkJQS8Eg0xH9e0u65vjw6OIn4WS4nOU7IbJs-P5t5kcrqfWl0mq7QDVP-MmeepFf9pcpRXCBI4M7D-UZnUnPeW1X6S_sg_-NGuUTqkwAbQn1ZRef0vXMbaB_yQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xp6wnU5A7mOWo4paTRfK0KGXRkTQ64HKrJfPC0nxyz5g9Z_TQDAU7lam2ejV_l_64QB9zFKhILRS_92uE7TGP67_p0KbGI02AABNCyS-OiYZ8XcAsP3f3nCWVDf6Bb0A28g0XHbTMi1fV7wqBRSjxnyALPAfTEhgTIaC4_2_mDSw1QXDjE2s1mWFCTCdmXwv8SQrBh3gX-XowLul4soAiwBB3_28duNnpGjY4AlWEHh01OOvjANZG_4Ho_QVqmiyU36Vf_L8tVh3f8Cap6Q5U6c3m_jF8FZl97Yf7xPU_Lqa0gOtmVaA6mCvFloV6zpfr6fx1ofaO2pJd8kLTIEZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/foyJC8GvazwNoh2mcd1QROhIadezSO-06tIr9muo81wP3-eqKuCjIRdPwslzcGmMIbSKl8P-Jd_B_mQPHmj_nFdouxmM7cBQaE6tij7elIV-Sfe_vnF52eni6eIYoFfDffnDY_RBB1Xm6gWkMbfi2mDFVZKlIkMEph-MCvMzZjPKFZNQnPJV-7vSAMjgtZfEmxoCmV1aSBd6sL1DKfs7Pg-Nf2Yf91ZLaT6c7JlMQSX_jFm9FBO5Zs4sxYtGqwX3fT9Rh9CHhL5yJgzRdTDNWxO14asu9ytv0HA5ntJaDjXnOYASrYim-KTU2XyOo0b1E04TX_qLWJ6x6ggJy_k4wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pWQShuM_siMWkyV8AJjkOnl7lqBDfkbLk5htsif3eeeo5_p_HwVIHEQKDBRBpXbpTUXyvDIjrNuB9nieloBlJSodzChOo8AY6bLmjYLYmid3EaxjbPzW29b5kzg1pGQ9sZJGkiXPaCuspiRI4S8BfA7w7nvdGhWYT_XVmPDxR0oBcgxL_-J1P-TyImRrhni4yuSwMmJaPV_GwRyRve8hzD0rbrnxOILEEWfH3e-vWvRmh6NhnqnERkytIcxNBDz-IwytOb1JHqlpWqrMBj_03xFKuIhkNDZ28hSgoh6QePz5FhoGmHwnVKrvBQ5eTeBEyRg-6og70Me-ufMq-QiIhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tjls9Gh0RkIoVP9UislTeHS-P9RH4tV9q3Wau6Q-Qii-AbGWkUs1k1kFPzdRh3MKuy3yCzu8QqvN5rYwhjtxg1qSpAWd634h18SwmiGb5n9KU2dopMDn2drvPX_AM_d8ymLufgkmGe1pEITK39AY4vK8nWtAYx4_Gh5cz66feafipeNlBBrIUBZ_yskNcI2V-wX3QMTrXzYPUTcP5O-Nsx1ByD3seWTZY75S7natysaCN8rS5BMTeuAqsbRhfbHFE1Tz1WXfS5FgPT5JpSFl9r6WQEzMG-ysaGW1XdEEoU1227lYtS-6cCYfwm7jrywcAaDDVfbb93308ZaEIn6Uow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=tjls9Gh0RkIoVP9UislTeHS-P9RH4tV9q3Wau6Q-Qii-AbGWkUs1k1kFPzdRh3MKuy3yCzu8QqvN5rYwhjtxg1qSpAWd634h18SwmiGb5n9KU2dopMDn2drvPX_AM_d8ymLufgkmGe1pEITK39AY4vK8nWtAYx4_Gh5cz66feafipeNlBBrIUBZ_yskNcI2V-wX3QMTrXzYPUTcP5O-Nsx1ByD3seWTZY75S7natysaCN8rS5BMTeuAqsbRhfbHFE1Tz1WXfS5FgPT5JpSFl9r6WQEzMG-ysaGW1XdEEoU1227lYtS-6cCYfwm7jrywcAaDDVfbb93308ZaEIn6Uow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h7nLaEdQaaUHJsfrl1E-jbYdZKgiPnGBEqF6vu0rNp3xPxshs3xkVXEopmACmqeRM-00yeVdn9ByPSfqEuDE9j32-VUBhDV3BE3duQJJ8ZTmlZXwg110aZHHC9btMtEjV7JtiYDu6r54hcxdNlzMd2WVL1Ar-9Cs-18e8NkS21Xx-A11iNmL3cABU8j0f0OYOtlt3_kmDGnzoWjFZgPMbf_4ODCBiduB-emjk7U_0ZKIxVEHL51qXoaDJslQHBVFIQWOvqaLKbpnB2CGJA06jx40XJTHTEk5MAIrCbxcfSmQhCUaZSZKs-d0g89Jyr4iAy2TGAW5T6aWXkffdMptlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJXa2Jm9RAhzXaDDHEmLv8M3JZWsJWD6J24ZS4PgZkWBkAKGqvrgG7vZbXm_VkcwcYHgzmPXKZj8l7w96-GWFJjJ-KL5whQ5QSpyibeeylyww4epcUd2Xq0qA6SwjtUOzVOs25cTJnMXVqmVm52ETFfvRYLdO7gbybzMFRtEdEvpOveQqORdmwAUdnv8cZU1nPSAkR5y7wZCQrLQVe4ZQgrvcF478KwlajnP0PIv33pQXiRDljR2EDlIQ6IgDy--wUihtWpwIppZzmqnWcjVFY2F_1o1r60E5ReFBX0IbbHXsSMIw7hizlg6mNgdtqcBiu0QQHXYnoalUygxHlff-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WtjX5J8rAYOaGX9kDK5ndWgxaKGNK1VxmabvQFFlTmP9zii1pW4pYrFXvJA6q1fwncW9VSI1sddsFtD6xKCiA-svMfEJsPsAdT5CS68e4lTcP0qxAEk6DRPH2rD0DOP7IP0sL1xj0_3Y_PWCCib2sGyOSZIiWX97u31rONRu_B5rqQSVDtGE-_Zm3vsSHCX1ZJalZm_vGw76L5NkCL7w5TYCFDS9JnYKKcnmEJxVA5WpMkOsYgGdf-8XjZ_nrUHtEntVnJ64gJGFydHDuI75UfpNPTktSdvuSWr94jhq-Oa8qM9jBsTiET27msWwwmaZ145Ny0v6qgSbydbBWqfZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oc7p7jIOgxX8CqWiRcru5lXiFfKKG2cuBBxKbqXzgQ2nXh5bAd84XH0LWZvCjsiWk6BFW84NMXVAwBPMikXXnaOZWJES9lEQaXX1be0b1BJQ31tVnsxbLBR3U2XS1IqaTi63Mdt2D_TUBhe5yeacU5CkQHkmIyDvimmRT4h0PHRPhAi3NmLWQ9CHafhFVMxWw8Mv7bhZ0_X83g9hAbydZvaKO8Zbuz3grMROHEE2kNT06rhyPxKZG-fvfX-dnCG0C48cqmqUmSxaxZMHRYdCycQqcnZsdJZDO49XHwe7aszgz-4B1skSQRZitn6W6v6EErF3e9n28QRefRooWnBLoA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=N3albE_nVuyKG3OZV5o04SKDkkVvJW6e1DyaZeTRgaLcVjap1whK2Zs6F6g7WaX1YiAm7y1lFrejshKKsB1O5LR1_Y2XrCanOMscVxZ25KohZZXPBq_PZD2Kv_EfGunGgalnMjEaQxXwmDC0wvyAemQjyLNXQKfbIRZrJKk5a64_mbpDyLbC9Rz-vX9GpeQGq0u8vNvPqGCFivYscv_Cj99AXjXgiDnAQOnfUUcSWNHM_F5EtKQPMxsM9LMLDuCdLFDsBnWBx4tfS_i0CUmXJLVB7rUtfXvpmf7T3TQbAp08GP44iWl8ijO2dzbM4iuTffVAxpHDlwwV7YnXCz0mPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=N3albE_nVuyKG3OZV5o04SKDkkVvJW6e1DyaZeTRgaLcVjap1whK2Zs6F6g7WaX1YiAm7y1lFrejshKKsB1O5LR1_Y2XrCanOMscVxZ25KohZZXPBq_PZD2Kv_EfGunGgalnMjEaQxXwmDC0wvyAemQjyLNXQKfbIRZrJKk5a64_mbpDyLbC9Rz-vX9GpeQGq0u8vNvPqGCFivYscv_Cj99AXjXgiDnAQOnfUUcSWNHM_F5EtKQPMxsM9LMLDuCdLFDsBnWBx4tfS_i0CUmXJLVB7rUtfXvpmf7T3TQbAp08GP44iWl8ijO2dzbM4iuTffVAxpHDlwwV7YnXCz0mPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=AHzXGEmByp6VAMXElccHcfBUL7D4kFfxydlIFX_wD2umIsKTCUubq3l4SFu0MNyMX2M9tLRhg5ucLOthGM_1mbP-r9Vce3DK1nnN1N0z_tywSvoHBppNxN65sde5XEdY8PcVRrZEvaZtw6VaaJVt5225rp69Mg6Hqk3rZAO-5PHGSLh3nMZQ-cSyS3FDdtQ6WM0lbUPTVRRhYxS_qaa0Ddf8W-ElKWNegiuz6N8Iv72kf09Q6FIB7E_FP6nBUFSclb-Oj0ABJkB2ZhRq2RuK8cZBWrxTswHbU0hbWcKz4suGVH7-1MSSHDmlcWxUQbgxD2oIb2fmPveZPq0MwvMKNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=AHzXGEmByp6VAMXElccHcfBUL7D4kFfxydlIFX_wD2umIsKTCUubq3l4SFu0MNyMX2M9tLRhg5ucLOthGM_1mbP-r9Vce3DK1nnN1N0z_tywSvoHBppNxN65sde5XEdY8PcVRrZEvaZtw6VaaJVt5225rp69Mg6Hqk3rZAO-5PHGSLh3nMZQ-cSyS3FDdtQ6WM0lbUPTVRRhYxS_qaa0Ddf8W-ElKWNegiuz6N8Iv72kf09Q6FIB7E_FP6nBUFSclb-Oj0ABJkB2ZhRq2RuK8cZBWrxTswHbU0hbWcKz4suGVH7-1MSSHDmlcWxUQbgxD2oIb2fmPveZPq0MwvMKNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHd5UBttZWaW9B89oRUmFms7Yg0tCeye9gS7RoJQzaW3-o1PJYd6wQ5DmZhNhXUAoYoS2GxDIBFiqbK6Cq5yNB-WiQunkrQd4MqXG32Ruw2WVN7y-T9ZGgEvl-cB6725JToK-xFM-R3PIU5kaewGSixWqq_aC0OUz500HRmFImSRP0HUGmHQ9u6zPyTDLok1ivJt1qwrNkqOInSSRlH4DfpJq7SIO-Vi0eieh1lVEazlcVqdltserWNYTuRpdn-5GPoqbdTtU9sBi1Bx8ZQHNCtiwy0JPRHEScfMegWiXzlqCoWyEcRdWjWPXULLhNLKpIAPgQLjUQ1BJJQCt_Vyzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cM3zpJB50hFwDYF6hc17_yxLtIZzi8LhQI3xQyqa-1LtHNJA3PTmapaYWHSKBeiFt3SxRxKMQCDL2StFZq7VFlcogp3xj6AAXIXVq11cMhn3wyr1haF_glGPT1xBS4AZqvXAR8S-L1f6D6Qiw-dgVDlU6OEwfQA2LSGQhFGI6Q-Jt1Pbm4RZmiuMNaZwdkPmk8DlOP4krLJD2Bl81TsBdBrNYJ4pVIeQAUpyHD709uFjgQ_FjFHuC7o3xmdm0O67MBJGMSxogcJo6oT1Q5SksqaVZAWJ8VbYRhMNhfJ33nijXvxji1s7GXLF5AgpUhiLbsABX5Ki4mNxe-BrXnPpfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VOw1WsPcAmdxMcqGIxRgZVvkyAlvEHm_yP9H0R5xF3MXrAkn-JY-4SnMJEN39xRJzhGcmAyQAJNoY7LGsNDuI6kFKCvZu4z2docp_XOTCAE64oK9qoNk-mBo-YZN5_CDlo3mQt3I1TO-dKdF8oBuuHU0uOUNZwbwtej8oxfGVeDkLcOz297UGUTJVu0LAi2tR1uRFIhLjHMVtiSoz-T__r9N2QAFX9BRN-VI2N0Q6sqAvcx87tisNptWADJd3iJgG9w2D5XwB8wD9LP3s-FoW86JdtpK_WvV5mu4Gow_dUMIbetMqIka_MJ4ZfpdWExOmtlI_MXl93jPYxsx1JjMQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=VOw1WsPcAmdxMcqGIxRgZVvkyAlvEHm_yP9H0R5xF3MXrAkn-JY-4SnMJEN39xRJzhGcmAyQAJNoY7LGsNDuI6kFKCvZu4z2docp_XOTCAE64oK9qoNk-mBo-YZN5_CDlo3mQt3I1TO-dKdF8oBuuHU0uOUNZwbwtej8oxfGVeDkLcOz297UGUTJVu0LAi2tR1uRFIhLjHMVtiSoz-T__r9N2QAFX9BRN-VI2N0Q6sqAvcx87tisNptWADJd3iJgG9w2D5XwB8wD9LP3s-FoW86JdtpK_WvV5mu4Gow_dUMIbetMqIka_MJ4ZfpdWExOmtlI_MXl93jPYxsx1JjMQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=T03pwJtWq6xPsFd3W3NoAERNjm_J2LHuQ5eA2SPAHLmQg1RHks2CSe5czMWfwbnBzeGDaZ00kQA5oKcCW28SGdcN84jMbsrTIKRLdFoSOocpBOk1tTUEZPJ5VLeRigKZ9Gje702MOeZBKFAOgsHnhsAj817O9Z6fluLfr7oz1GvI_0yLbYcsFyJ25Ll6Xb7G0dW0fO36_6K6pqPCOauVghxywMT_WzNtpv2t2XwDSbzsijaxZCg8d7SmZ4SQxQ5JD2h4eixdnx4rRoQcj12Vwy5XZdThYmqbaf800aXEEFb-rzq4rQRy2jbrBk4FBRcyLj2YhiTbMtNk7FdCOQW7arZ0axCUKAxj17yDnamVYkwBqf3fgX9I9WuX82xrdYun54273iQ6lzRO0rsuMjMeI5xFWr8FhxmjPswwmiIZSE6HANFbNp4D--PSxihaW6fb2JZDsf5165wuFBiKft4x1y8Vk6q5-C9LFNagQGgPxad8yAkYzjlNB--RPSegyMKlNxwZBzcMH_qwAPZiSpJzLP-VBRz0-pk9HAkTZGg7SUW6PvXSjQxGgpLq-I9YIoW3iZfDLR4R5ccd7TzbvFzdfVS_pvA1eBF8JXei5hEkaYvsntmihTFfbwFxUwj2Cx9O0lMKsa0vr4WpIXjmEcxZMGMI4Qg_iNOZpfsua-NQc04" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=T03pwJtWq6xPsFd3W3NoAERNjm_J2LHuQ5eA2SPAHLmQg1RHks2CSe5czMWfwbnBzeGDaZ00kQA5oKcCW28SGdcN84jMbsrTIKRLdFoSOocpBOk1tTUEZPJ5VLeRigKZ9Gje702MOeZBKFAOgsHnhsAj817O9Z6fluLfr7oz1GvI_0yLbYcsFyJ25Ll6Xb7G0dW0fO36_6K6pqPCOauVghxywMT_WzNtpv2t2XwDSbzsijaxZCg8d7SmZ4SQxQ5JD2h4eixdnx4rRoQcj12Vwy5XZdThYmqbaf800aXEEFb-rzq4rQRy2jbrBk4FBRcyLj2YhiTbMtNk7FdCOQW7arZ0axCUKAxj17yDnamVYkwBqf3fgX9I9WuX82xrdYun54273iQ6lzRO0rsuMjMeI5xFWr8FhxmjPswwmiIZSE6HANFbNp4D--PSxihaW6fb2JZDsf5165wuFBiKft4x1y8Vk6q5-C9LFNagQGgPxad8yAkYzjlNB--RPSegyMKlNxwZBzcMH_qwAPZiSpJzLP-VBRz0-pk9HAkTZGg7SUW6PvXSjQxGgpLq-I9YIoW3iZfDLR4R5ccd7TzbvFzdfVS_pvA1eBF8JXei5hEkaYvsntmihTFfbwFxUwj2Cx9O0lMKsa0vr4WpIXjmEcxZMGMI4Qg_iNOZpfsua-NQc04" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nAX-k2YGgF43zJx83dt-MtcnXRCstZNXE2u0qOF8TQG3xPJJcCPW1ejmj2fyD511V78GUEKATRelEniGD--pZnqGkX-cW6lvILxJcQHylK2aZvdaxprYhQ9nUyBt6mfRn5bhA7TWx66j1pEuwRzJ3Ne3nqEyzDPmr5GrQFjgQoow9zZvZ0odqv0WyS_EVSds59YIVagZUC9seiOTdhWfGp4M3fkX6xC8xKTEDfSoqKnGpyod7b0NdmHb4r9hWlfTZwk_1S-_XO4eOoKt1kTMTNLblKzZ0Q2M7orTo44awmnV91_Z7p0H409G4GhUsWRooiZw0F8w9cQeDwlrsMBZ8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ho_645kegW95AUII0sXSXEUjk_DkmDNARxZS7WYjxmhD8CubLyIWL0_-ewsxvY8oiJJXU4hQBFzAoVnszexqArbhxY8g6TwlYSrtUlsmKopEhKDKc2ev-wcoCIn3V5AZVk-VFeiNZWr5FA3dHYzbOPlWecGMnK5daG8OBcZfadd4iG5nPGDExbCS9Vvwc_jApYvp1Bxd9dTlp7f3Ai907XNV7D89NvntyXXbkuVtSeB3pvYk2eqxRPTfzGUBPLC1XhIB1oR2ZPO_fQlcHKCS-zsZjHgw9WIV8tsJ7DfL901qYe4vGwhTBqJB3xZS2zlc6vlZ_9Gkl0wC2sLef5Gbyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KncLKgjRvxTzjPL_Ca5pAaabA1RLs_QDw9XxIOaFAcYwsBZGSd8I_Xf40KkdaTy4fyRVJRYD3TfITGaVa0EG9lRqw4ZgOkpq2qJ0bGgWyW9bgnrgCPDumBbxpqAknaqsihEh9qndVS7FMCCYYhdiNjUTctB6m2hST3KKNgpBKFznECJzwEkbrU1DhpNwjlApo5mr-C7wbfGSJPG8dklSLZAMzzlMjKaI3v0PP_OWvUdBs1pd8fOzYAmOGsGkIevmwLC-4kdiawTteHgxyX3dNsczkcyVMR1TLypLM2A26GqacolWTbiTljdUTlAo8Tdo5mCdp2d2HT7J2QpFhyTw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pDAU3ftlmfnLRoQX-Iy09sE6734panu3XIufpnrs4DcAwCYh0b7vhS8gq7MPEObRN5b8VrbaHCISfRStqlLYd4kgUfTTn8jhJjBA0FK5juvxv4PyypQlEHv11OYV-U2sV_suRpOHPnXMF6SZqgd1CiMKOQUWr_wgQwwwj8zvCpiim3OKIl3pqh43O6yzKTUMBVc5GMQhM0u7VaU1zdDfWD5xRNpax4dCzNDnRuXKZ6X9r2ymI_9_cIa7lgIkbsJolvYcsJohmy8zAZIwPk7TCeMr3qQE_fCsZwYhy6RRYL6QUebJlkgXs4B5HeXV9dODkWAtkOCYWpoAebKH8PAvLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujEb8ZoJKLuqtvLrMu4En-TqGIlA9g3DPYWUVZJ_6UcVL338ItAH2JnaZCJZ76w9UXfgREUaYX4iq5L2dMpKI5bXFedVLugLV6mbCNXZW25MVhgobDdatkkIL9NVwg38mEdGD9Sq4f40XqTUPz8JklyeXUUfnA4M7KYRJ47vrbTS-OFqD1RMRM9LQbLpavKOaLkwsO4bBKEO5RcaJUOtd98RzbV6x6xLgHE3Q4b7fFVAjgWz-wAq3EdR70xA-OeUvWEW5ki8FQQl6X7pFzcLjrAAxaIpp8jP31x4Ts3qheN0ZEMW7oHue0xJiB0pWjJTXaH-d-QgWDRWDHeJXWl5lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yo81PPNk2k26Rpe9VBPaG42di-pvH9kWlX7ei_TSHRPH8LuIBWz5PVGN1SllEXA8kH1ncc9rPN4x8yShXbDAD7oYoyJ30DQ4lzrj55QLCodDopf8EudljyN5ei4lb0vimsJlDGQ15xXfzxqjv4S_c6MhAvFwY1em452NqdCRe4bD3fsbZq8ibBIf2yllyOLTLqcdmUjSM6zQZyxWA6vZvhzC9vdPd9FYzchANIl9l1-hrf4VVqpTHkJjwn5X4WG1EzgRvxZ6vr44lAmQevwYxjsnehgh5cB9mzHT7RCBgb9no_lkk0Uqz0RV1wtX5RJ0QkFyB4noi_ptG0Xif3i3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=omSWoy0jWfHjsRAWe_oZGorCUxL7co8Drb98p61UxGK_W5hiYdIPw5iJqUMplSQA8i-8bs425pcnGBAF30cFIFoXj6AAKFendUT3gsgTehtK3wdj3EdYmSpa7o3n0kIzxAuAPkd3Oe9lUCxV_stjYieF3u-8kY8_5MoJFkWu8BKquFJzeImAyr6v0ykL2FLFWy2e1LzyAid59JLZj9f2V4_zZlQcU2Biwo4dq3LhOymyVZ7gPWSHWyX7OjqphnBpkCphkFEkBDU5aFlTzo_a7PwnDuk9RxZp_8QX8IixwfSNP-zoUb0aByYR-QA_1zzbJJlpdbKoiyRJIWo--HIM6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=omSWoy0jWfHjsRAWe_oZGorCUxL7co8Drb98p61UxGK_W5hiYdIPw5iJqUMplSQA8i-8bs425pcnGBAF30cFIFoXj6AAKFendUT3gsgTehtK3wdj3EdYmSpa7o3n0kIzxAuAPkd3Oe9lUCxV_stjYieF3u-8kY8_5MoJFkWu8BKquFJzeImAyr6v0ykL2FLFWy2e1LzyAid59JLZj9f2V4_zZlQcU2Biwo4dq3LhOymyVZ7gPWSHWyX7OjqphnBpkCphkFEkBDU5aFlTzo_a7PwnDuk9RxZp_8QX8IixwfSNP-zoUb0aByYR-QA_1zzbJJlpdbKoiyRJIWo--HIM6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=FntiJzpZp3OleXtCKJqPKKthltV0dKPaNKVMse_w0-0yFRwuy-KKos1p-42AQs1PeEgaAcVN5adZg7zaEwrOO2rSi0ZjSijaQc3_Wv3EcAX24EYuCKJrNJkU6y474-skycKbn1J6uYkekwZj7mjOYcV5hIRIYNATCxGQhbuPaP3gPx82wWb2OkuwvbHiLsikl3mGW8n4EHa_9L4dmnFn6dwHkYcPtqlcCXPW3hN7BZn5kzo9EGs4CgQOWNAvTEyfZsJITJk7D781fnFCvuuHTgf61W7PUtNDi3QETP5F4BqpuISoV9JQsZMJyZJ9bXfCqrwAWY0MvJ0fOVpa7cs9Ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=FntiJzpZp3OleXtCKJqPKKthltV0dKPaNKVMse_w0-0yFRwuy-KKos1p-42AQs1PeEgaAcVN5adZg7zaEwrOO2rSi0ZjSijaQc3_Wv3EcAX24EYuCKJrNJkU6y474-skycKbn1J6uYkekwZj7mjOYcV5hIRIYNATCxGQhbuPaP3gPx82wWb2OkuwvbHiLsikl3mGW8n4EHa_9L4dmnFn6dwHkYcPtqlcCXPW3hN7BZn5kzo9EGs4CgQOWNAvTEyfZsJITJk7D781fnFCvuuHTgf61W7PUtNDi3QETP5F4BqpuISoV9JQsZMJyZJ9bXfCqrwAWY0MvJ0fOVpa7cs9Ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZD_PgkqrY_DRR2FoNm2qIfFK4BmjfA4rSzrrvMypdXk2lYVSz5Z2zb3wpNwTiGd1lHBiNDR7ZFRDHUh_BdgNrQfdUOD0bgsJRrM0C2CQPUPjn_rQEtFCKzyqQyOx0gBjpVKw0qTiod_SN4XhzbmXMbY9adNfuLu4Shljt_ybZq4LjlGEoNZ_zM-JWxW22-ZLTEHXAIEG6_xA0oeLvJutR2Mh6BAJkE9bKgqUgdtSrkwdwG-WZhQ_l7oky0-fhctHpW024clwFDgFXNv45K5lUgl_4tktO8eCeYH4GjNK5iUf-Wn9YhpLNM_99ThcJgSb3w_2xX3OSQevvRsU-4WyhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fjPzj4zRGaRugt92CEDDeqs3HkzVyiwQecCZxrFoFef42Dvl0HS_6a35mQPvXUu-4TvT7DKONw7a2IXBCQ81YKMIZEwY3Zw8OsEigatMGntKwKGDK7VK8Ijdxz_T6arkiplcN9itweeeeCqKY-NgH97qAJkHeQlYWG9lClLBde5MsbA68FWr2eo35Az7Ny38ERhz5WZB0rqbXfmgKnOKdl1u8QjeaEmGm_GflCXZOWQrKd4zO6JEN3WMi3qjJVtiZN7lPrk5orhDzHRyiMmn-t2w8C5z374mfpJwYWO8HNHwG_y5htBmkrscsK7Xdli2yCqHt6BAmRs9flccCTjy1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=J12BYBwCmF5Fks4KHnrriU_6BbHrVSHRd8aOnPQW2xpIqgxEgOFnZkrZfvfI-6a3bqNm-Fko2tqja0Oj_xc51JgYfkf1UkZoH_jdlnNsroEiUK7J-Y2DhggKCXuSgEWEq1v3thJBE28ESMbfM8ZSfUta8ruwnKszMrayxBS7cAezU8cm9ac7BXi_uVPx0ULeiQgo_RcxoXjehg10zx63cT47Km0YuZmSlehaqqj_SwS7wkYFNDMKhhBBH_Lm5efE7Xt1XHjP6QsFqXypFD7to002NQA8kfxlQ0PqjQxR6uILX6INemTqDMyxHqHK13egVUnc0gRfAqHDjRqaPOHH2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=J12BYBwCmF5Fks4KHnrriU_6BbHrVSHRd8aOnPQW2xpIqgxEgOFnZkrZfvfI-6a3bqNm-Fko2tqja0Oj_xc51JgYfkf1UkZoH_jdlnNsroEiUK7J-Y2DhggKCXuSgEWEq1v3thJBE28ESMbfM8ZSfUta8ruwnKszMrayxBS7cAezU8cm9ac7BXi_uVPx0ULeiQgo_RcxoXjehg10zx63cT47Km0YuZmSlehaqqj_SwS7wkYFNDMKhhBBH_Lm5efE7Xt1XHjP6QsFqXypFD7to002NQA8kfxlQ0PqjQxR6uILX6INemTqDMyxHqHK13egVUnc0gRfAqHDjRqaPOHH2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_DKNYp4u27sD2dbdqwgjX1zura2_LUqUrHhcS65_lqay6kRlhcR_VPzWkH3WszyGlG0-1RcTV5t5tAFM5sNNfaaN4su9MkJ35HS3ZBT5VNyFbR-o_wEtYrJAVcaZcwkjE0ppU5-R5_CDZT5z5ClfObZtsSME0c85Ix4HFAy63oJqVIc2Rteg8qWyK_8ma-YsbKrYVBB8ctOFSwFPX2avHN5VbNG61cMGRGaMwEp9J7PZ6Ojgsiaox9Fbujnt-dXlNPq0qP_LE3LsE8rsJL3xl8JZCxd35HdITgICFGccqADGILpmVUfAbFfLSNb2fT4g4XJ3XZokiNRGMMzmxagBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aG6kRiTR3lJp3D0HczkSLRjvThAEidyOUv-s07oua3MfoUQMnxMOw9SO5Zs8TR4BFCof2eaK6_RP1pZhMYsAXTufjyzBzPwcD48gQiBaE5k4iONSGyQe17i78wbE3UbD3pGF5lYFd3guyjUlXnpdd9A7MpoJhyNZ7ZgCapGUwP4rb1tQk536L9v_66b6D0aCyjYk6KNjSJWUq68H5eKd1wJevq4pPBnUxDHGQo52BPVuJPKngUo5Z3L0dvqBCH5bxnLG-3kFkck57jZe9a8aceK67LaFJjrEP6GuhQOLTtl-hI3ZPD4Q53Bo7oP3wKLHss1vAEbWFQkjqxgc_DCF1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=S_mvG2v34TFDrC9e8T26Bb7Maho0_Pi8rRda7QrtIby1HKooAgLzR_4JX1-o8O_GVvAfroGhiH4BvXdcP1d0t69NG1FZRVThgfsq-fOHNejfOO68gIihUK1IKfjZsD1KM2gyC9UseFR5AHZN0xnRGY45vN2YqSq3u6VcxUy0-RvmTwO0Og1b-eDtYecJYLFos4Wt1ybharfR5Gq39s87E3hM8OeaFkg4kL6agqqYe2FEF6GerI2KJ41p33pqZzTrDGBsCdYPisAEiyB_GMVPqot9Xvt3TiqOwoeHSWshP-YcurBpUoyr0lQXOMIyU8NSqsdPysQbrxCKoLKDXEv0gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=S_mvG2v34TFDrC9e8T26Bb7Maho0_Pi8rRda7QrtIby1HKooAgLzR_4JX1-o8O_GVvAfroGhiH4BvXdcP1d0t69NG1FZRVThgfsq-fOHNejfOO68gIihUK1IKfjZsD1KM2gyC9UseFR5AHZN0xnRGY45vN2YqSq3u6VcxUy0-RvmTwO0Og1b-eDtYecJYLFos4Wt1ybharfR5Gq39s87E3hM8OeaFkg4kL6agqqYe2FEF6GerI2KJ41p33pqZzTrDGBsCdYPisAEiyB_GMVPqot9Xvt3TiqOwoeHSWshP-YcurBpUoyr0lQXOMIyU8NSqsdPysQbrxCKoLKDXEv0gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l32Zcm9iroIsWqyXiWf18F9wbuL6ipOHW2uKTD3MlKS0hPdVmPf6JiIJUjRJbJjphDFFfl14zpBP3KCpDwd9Abnr9xqdP2xtPcgnZKi0UC3W55eE0Ue1xkwD8Y4bL4JY_GrxKS-HE_Hb7vpxAf_eIcd6OO3lWWesYRhkRTyj-aacghdCADcQ9JfQijLUX-Up_MlYinfmz-wSAYvqZliZLkvCJXBUlWR4Lxi2Tq2s6UJ5lgllSLPhEfNAHVKDknKmQYDvJbBDG_JwlzIlpSAwvOvmx8-FQeC1VRwJQzMhya77RESJMAsI2Qxihm71BcxJyCu4AESnZ7MMEGbt8NHZKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_6PKsr8OnK_JlJBP41XwRqPkUAObyleVg8yK0SnwW77yZAHkAHNxTTMW3-8hpMziCfm71g9T28--8Ev5z1x9cuHcvVQRZr94FvqrRqXzTzh8MuToJ8WZffOHwJFRmuRrTgZ6E2Z0dGILiQMaRzsthh1WAWjMzMlA-jMHaF5pzyiy8yD9tuXxBsuGZ3AYycW3eBJRlToPst-5fgSoGmLpyiPlMJH9XbsTFTPSYVxGCVnGpK-yPYRfTIakboglWZnKsbOgz9dOb9zbEMhn5szlz0v9O7FP9R5VW1wIBUF_HAh_ICbD_B1Rd2UOTz0WlZHuw1UAXQUUDcU5la5MICMXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Vyja-k7Xwho43mxrfrAj_nNKYG3s6KUrfjKfTqkpRONV_Z_jyDn0zyckKO6Ny4IRTG5SyT5jD91jHfIlj2x4ETBD_Hc4GSzGhqjPeSlkR-Pdq8bcqN2xsmWcGLPcgqsBL4g1Py1kUOrHuGE-yS36poll25H7m5bR9iPrH2NL2SNcUIsSTRCkC7qaFrKNVCtvPVRhuqWZxquKuXoQpySUgbOUeSJ_hIYiWTdjYf_gW2ItsrWNDq-qaKj-DTsLrEJulgLmCBeWeTUL8fDli2XBUp6xoMy-rJ6_rnRqeWN4qa0HJdB3EY1ZKY7fwd7BPneGf0LJq5rNewUJ0mq6cBvFUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=Vyja-k7Xwho43mxrfrAj_nNKYG3s6KUrfjKfTqkpRONV_Z_jyDn0zyckKO6Ny4IRTG5SyT5jD91jHfIlj2x4ETBD_Hc4GSzGhqjPeSlkR-Pdq8bcqN2xsmWcGLPcgqsBL4g1Py1kUOrHuGE-yS36poll25H7m5bR9iPrH2NL2SNcUIsSTRCkC7qaFrKNVCtvPVRhuqWZxquKuXoQpySUgbOUeSJ_hIYiWTdjYf_gW2ItsrWNDq-qaKj-DTsLrEJulgLmCBeWeTUL8fDli2XBUp6xoMy-rJ6_rnRqeWN4qa0HJdB3EY1ZKY7fwd7BPneGf0LJq5rNewUJ0mq6cBvFUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EP6iTATmoQin8DH4bkJWn4vJyftnU5kAqoqVm5GI6IwN4iS_LRZIC-AcQJhuykCq0iAFNsEVLbRNnniS9-aYk7G1fwF4RjkGt6Rvw8iCGlsNIYOBn05KMURi8YT2hjya85aG_s_gisBPcfRhp5FjngXu9xFyEV-TkXzT40EwgpG8boe7w4iIAWnIdkuF_mMwF0OnVGdKKHX961eWIILdwkWo-5FlQTa-_uBs9DyasE-nrTzg0t2oosYnzjNOH5gbQf30TZk9Zm6LNlVdZb0-eZbqKo12727x6GObWC_UsSGJ34rgMgfT0jaxdG6kXFqyR991UfJLPGf9yryRcOJMGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ey6QCM_cPKl1fMdjqAzmRnsra0Y-yV2-0FJz032ZHNcGxpgUy4CT_dDzBwb4rvODoI4Svoz0ci4O1gRhrlk2lks0s3xoImzGosZNWF_L9RL_-qHwsu9s1GLcUxTOa7xB_sYIN9S1on0FY_bJHxud_OSryYopKZYG4tRjk1wTKoZHfZ8RR3TprJHjKrJLuN_Kni0chf_Q0Qa3SyabdCekN1DDwi8j8s6lJD56qZmfdT265bTV3JIP_5Tx9HHRFEfsV8ZJijPp9O4sjfJX8HioXOaezxtjB2929ShwNwTEfVI6MxRO86gs_SEXoszlpAzasfRAuESjeIvr-MFpwhoivQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQf4FCL50PvX5gLLOL4PfC-Jw7bmO_qflrDFehMIo4ezKPWZY6Gf6oI9ycDYAJfxdv_x94c68Dl93TzgMaJRhMmYuCJQmc2CXvy3GaJcH5-zo71znSMhS5lXaeL2K1nXCrC9FSlex1v4DmFrdhWjdG4UJITUi507HORst1qSh-9I4JDMuxjv50kmMyqwxNEmM8BV-JfILmCTX13ZgqINhDT2gjYueCLFZY3hv1m2_QywEUayNY_W-aN3_x67gtLQQj2aTZVG8Ya4arlWL5Jepp36TEYbLj3qBElB6A88hCm5k5MRUXZdIZpJ0iINc_1djA-Xo7CHSWGP4pzbcSF2iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FOY1FtaQ4TJgrsGXku1atLmhter2cpKSLeQDb6ZjxrW04522g00UP6YBaXnTmLbme9N1HIneQk8Jy1CJGKCEQfpEDGin4_5888ymEKhnAEF5omP3GJ3flAZnH0_sVYyBWVncL8ZtBStpmrLxEJUc4K9sv3np17Znawnvt6cK011EPzyCFVuxN381iTnFW70HiXrdOfLlWMMXx9yiFg5fEBSBUoOyXt6ltMLDoGjBfJHbYGHFuZqQMTGnx1eILxrDueNhKjbbyIxJcGtY7VeovTuIX29cvS5igFNUcEdc-sfRP15DWlW9czbqvoYqNBKxX-U_wM32dXXdvKc5BjHm-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NeFGf5nGL-wV1RZoJ_utst4fWc4O1HOsXyDMBdgS-28jyerFRpz64KKNOS7s5gu5NHeicfPyf9DMHOT8s5fD8TwfpxWlHohUK2ITT9nAh6hgYJPZJg6TX2XZuomLJQPXuqe9P--0JuvW8r3fB1oPdiyvDNRv-kWn1sfAwqxdRD5WkfI3s8gCMmS5cLtQsMZS2gj0V4j_HO-2H8OwjzSoqCGQ6cqZ-Tq2kO7PTcOWUtFIIIKEWv6sp4H1D8YP4xPUHYBIZj6g39aHFxm0G5xtI3Bleulox7ousn58Zv1TqLITewst5Z8l8AfHQNLGW3dv45BZatpz7RkvZXtYseW4rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TJ2cOdN4YlmupDlQVHrfrIlm2_mmMwi9ANCDroH3fKhA-xvQpoTOLT9MWmLB1RWMpsy5espZNqU903WFcytLW4kSubg_X2tzLiUNarzqU-jl0ffVi-gIvgf9RLx9IWWyazPi0rEgWeyiw9vdJqKUngGvmMK4ygMTVbZCkpRk3ubIdovXf9PZ6zAHgDT7S4znjBKhcYxUvv7nvYkrRbsyR1xgTcs9I-GnpWOZ6ifS0fgbpb0_7Oip3dVR_cMzPD1iwRHNHt-knfvy98XMPK2ExeB1TQUpxbht_DmtVEEXzqI7O4X8cQen7s9kYTVLKBquIkJEt1KUAHnyZ533GzXJjA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
