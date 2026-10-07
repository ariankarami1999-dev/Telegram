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
<img src="https://cdn4.telesco.pe/file/LQgPBxoFaJQUZNJESKBeODd94U90dEuPeW4PTTVv44_uC2VQVRJrZjny49ZKP-KNnNqtjU_d53Z0RJ1PKInc5UQuFBM9FUOIJ8tujCaUWnClMa4BI_jZtVlFuU0H7_-AQq83OGPmjPq7xZ9gjgNWY_lqaM0xk45LtfHcKGiM_GZ3plxj--Ia8nsPJ91vwZxUxPRZ1wGzDJGOcy_xI_X0lQI8D1z1Mh05E8qNY9gM3HEUghgbkP7yB15Z0JDP3J1LJjyqW127ReqPQW8s9VLZKuSAdxOg-JmpdY8gI7_4SqAIBbbbDwFJZKyK1KyxITTFVXTEFzcGAW6Mj-7Cd5zZww.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 1.01M عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-16 01:37:44</div>
<hr>

<div class="tg-post" id="msg-151547">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👈
آکسیوس به نقل از 3 مقام ارشد آمریکایی:
چندین لشکر ارتش سوریه به تعداد 20 هزار نیروی نظامی در حال آماده سازی برای اعزام فوری به یمن و جبهه های جنگ با حوثی ها می‌باشند
🔴
دولت سوریه در ازای این حمایت نظامی تمام عیار ده ها میلیارد دلار سرمایه گذاری عربستان سعودی در این کشور را دریافت خواهد کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/151547" target="_blank">📅 01:16 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151546">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVpF9u7Lsmi52HXUR3ftwZSp2qqMyJ6NKPR2xbKEGsUg4PbuifQl5W1XzJ4xFdBwg6iCu-cKwNL2_wwm7l2cOYnYjoWntk9IWs9VWArV_lGnBZu_k9KRu7VDicP7-kuuZQh5rfsh6LvG6DYUgbUukIzcfWeyceR4OfFxIzKxw1lQAYWB8sPJN7haKVftNwtbDe33o_q3F1HnOgBAFzNw0d1MMzMcfGMD0hGg9Um2BxAS0_IMCxR790jNWTjpWXWIddVYUqIePt9wkbuYnCXoOJbKSpfS95McmubjNzZ1sN75Yj5FWB3jI69ZoaJodyPCVcuy9g_jZKgwTF2WfEES6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری منتشر شده که در آن خلبان یک فروند میگ-۲۹ اوکراینی پس از سرنگونی یک پهپاد تهاجمی روسیه، در مقابل لاشه در حال انفجار آن انگشت فاک نشان داده
✅
@AloNews</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/alonews/151546" target="_blank">📅 01:12 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151545">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgauW1MM4Nhqcrd-Byb4QkUqqOs8tMOF1UNzwYfKnMPqkS2Gh7smc1SRR6h8wU_IOxiW-uAEfLplSpDIVpHwvlGMu3pAL5J1bnt9zIF3cllWzqcFBRy4fdel6nU1zERjP7E4bl1sSJ6FTAgj5fxjysBCM3iLzXx8gTVadghmqdIIj3lf-i0uhqBk_VNxFz3nfzfUcbAil4RK0vjPUHb_B2Rxiias_FqQrD46wr52Eta864IRw0Gf3Mvs9LlRjKOaZWbZCqyLeIEI2J17GdQ29KMGLNUCFs023tocplCHyYtyJeuJRKS-qZGdVJbLosRwuqU7I2DMet0uiKuAuptGIkk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05c961e8d3.mp4?token=j5r0dLBFaXSAzOBoikzV5IfddY-SB9ZvNVEeToYwqRLAKqBkBfd5qo1vYSnBFEy11OYyDEYffztd9pnCv7K45YrMw2oLhN2C2-YF9yiCko_wgyfk-XSC8z_6Hv0RnqZMhbD1lNAcAjtNZzCkj9PznaY9IEnKNT2U55N03W7IOUhbs3ixGofwKJIQIFPq7PqN4z3TCHjzl7V2oTuHd0erMJYxv_QHZCNEESjv4rmePKq0NGX77GbvyxAOLN6SFP8I_Xx6BhkvUK66mg4FCrgHLfEoyaFa6q1AqhPptpz6tHwCkjdOKKlUXsyBGTnXWxfAgSUN-QYZykD4qgYeMH9uMgauW1MM4Nhqcrd-Byb4QkUqqOs8tMOF1UNzwYfKnMPqkS2Gh7smc1SRR6h8wU_IOxiW-uAEfLplSpDIVpHwvlGMu3pAL5J1bnt9zIF3cllWzqcFBRy4fdel6nU1zERjP7E4bl1sSJ6FTAgj5fxjysBCM3iLzXx8gTVadghmqdIIj3lf-i0uhqBk_VNxFz3nfzfUcbAil4RK0vjPUHb_B2Rxiias_FqQrD46wr52Eta864IRw0Gf3Mvs9LlRjKOaZWbZCqyLeIEI2J17GdQ29KMGLNUCFs023tocplCHyYtyJeuJRKS-qZGdVJbLosRwuqU7I2DMet0uiKuAuptGIkk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دیروز عده‌ای الاف تو تهران ساعت ۹ صبح کفن‌پوشیده به سمت قوه قضاییه رفتن و به پسر پزشکیان لعنت فرستادن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/151545" target="_blank">📅 00:54 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151544">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🔴
نشریه آتلانتیک : کاخ سفید از پنتاگون خواسته تا برنامه حمله به اهدافی در ایران برای پیش از انتخابات (۱۲ آبان) رو آماده کنه. ترامپ قصد داره قبل از‌ انتخابات حملاتی رو به ایران انجام بده.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/151544" target="_blank">📅 00:49 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151543">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">👈
کارشناس مذهبی تلوزیون: افرادی که ناخن‌هایشان را تا ته می‌گیرند، جن‌ها شب‌ها به سراغشان می‌آیند و ناخن‌هایشان را لیس می‌زنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/151543" target="_blank">📅 00:41 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151542">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نتانیاهو: اگر ما علیه ج.ا اقدام نمی‌کردیم، بمب‌های اتمی ۱۰ میلیون اسرائیلی را نابود می‌کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/151542" target="_blank">📅 00:32 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151541">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c552576b68.mp4?token=XzXsZlVyDxMBM-09yVokm8cVYkME1HzYL_obm_C8g8lz4m1EImp-pE7dFQzQC5CYvRDYhO4tlGJc3JbAHwCczFz7FA8DuqfdIV30eOCOaj-yzKCw0zOziOzpWOYKKPODN_68kyHfvDHcyiyorFJBvltYNAE3OaAhUimcTwccAhl0r8jUSwFkUDEJ2RtogRbQW1KfFiSzCCSl6GlUjAqOJPVBSZ-DBSAm_WjMtZXGpkB4oXE_U_oOYI_yKfwTfostHoAOiDfg_AkVdEY_EG7D3R4oqbbCPKhhNggdYpysdzlCXwCGFKikwbsAotj3DTkavHylw6sso8cHjK10-Fi4QA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c552576b68.mp4?token=XzXsZlVyDxMBM-09yVokm8cVYkME1HzYL_obm_C8g8lz4m1EImp-pE7dFQzQC5CYvRDYhO4tlGJc3JbAHwCczFz7FA8DuqfdIV30eOCOaj-yzKCw0zOziOzpWOYKKPODN_68kyHfvDHcyiyorFJBvltYNAE3OaAhUimcTwccAhl0r8jUSwFkUDEJ2RtogRbQW1KfFiSzCCSl6GlUjAqOJPVBSZ-DBSAm_WjMtZXGpkB4oXE_U_oOYI_yKfwTfostHoAOiDfg_AkVdEY_EG7D3R4oqbbCPKhhNggdYpysdzlCXwCGFKikwbsAotj3DTkavHylw6sso8cHjK10-Fi4QA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاید باورتون نشه ولی این آهنگ تو صدا و سیما ممنوع الپخش شده
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/alonews/151541" target="_blank">📅 00:25 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151540">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
خدا باعث و بانیش رو لعنت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/151540" target="_blank">📅 00:19 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151539">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
سخنگوی وزارت خارجه:
تبادل پیام (میان ایران و آمریکا) از طریق میانجی‌ها انجام می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/alonews/151539" target="_blank">📅 00:07 · 16 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151538">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lmnrnZ-Kso3GGSkR1FKtR2aX9lRYNGTdxfT8z0JXA6iE9DryY8bQN0_AOi9zA60dwW7XOj4LCTATf97riT3490uQ0uE7fcf3-JRCKj5aO4LaTy05A8EvgYtNteNfCGBRGnwQCqmlB7_g5qqUXtZLm7cssZfv0aW-dSzH85mfbGOrDbA5oeTjsokGQYQ_XHgeNEi3AclMZ_Pa2Fz1vO4ggFCQVNiVCVvKNLkoLPi-EUFM-Ca8PO76nM5fUKow9X2R-Rc9tPpR6Vst8_boXodeL9AZ-qTe4Q92OphZqYG3z3NC8_2Cxcjqtl1Da15QK9R_2G-E7Rdgxc_VJXuO5sQwFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد خوش چشم: یه موشک داریم که پنتاگون و غرب تو کف موندن چی هست
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/alonews/151538" target="_blank">📅 23:59 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151537">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
پلن ویژه افزایش ممبر برای کانالهای تحلیلی و اقتصادی داریم جهت اطلاع از شرایط به دایرکت پیام دهید
دایرکت</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/151537" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151535">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
کانال 15 اسرائیل: ایران در روزهای اخیر شلیک به سمت کشتی‌ها در تنگه هرمز را از سر گرفته است
🔴
‏ ارزیابی این است که حمله‌ای از سوی آمریکا انجام خواهد شد و بنابراین ممکن است آنها بخواهند ابتدا حمله کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/151535" target="_blank">📅 23:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151534">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
پزشکیان : من یک دانش‌ آموز شلوغ و بازیگوش بودم و درس هم نمی‌خواندم اما وقتی وارد جامعه و نامردی‌ها را دیدم تصمیم گرفتم درس بخوانم
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/alonews/151534" target="_blank">📅 23:52 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151533">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a58a5239b.mp4?token=R-rkd3VsZOlaH6X-_3t8JYjWZcwlsumcHGN6JFM9XKZFUV96OKSMV9Mn2slLp3V68wWiBl9xUnUF06V62COkoA6djnH-kIuRqvwdi7d1dA2Z6X-exmmCu4MVylXPnwLDdgWfkCKl6YhiYh1BXwlLrNHXFIJlIhO2cva2UYiPRmTNc_7A8a8K8eaAavw5dMLFlUgQCe0v4lqWRl5aeJvj5I2oE6Fx7pG6gSu96P5xFhagiGQdkAvGoIgLa7tI8aKk05hU3tQxicEiMSM13dLP-6UdLvooeEuge3Lv9bNK18qpNbrBdIAievvsa_Vs4kKSThZA5NazXLa06St7Vu1d_W1LEZKXqbHioG9eJ4wTEEBbS8fCBBXRlYt2GWG9VZwrCIZoUIfgyWMzzFUQiztl0tNWWfg4c-PpZlA5DqvPbUCi7uQkWAmj5kStLGQ-WhkGsQ-iJGxFqH408Hplhq2qpNMuWkMEQ0w8HWMb9orsrCBHyoBVX1v-WeIhUG0cDWjs0u1z-UlrIBmZYLEK1FWG20AU8COUrFTLKLwmWs2-YhKGYmQdUpF0eSjLcQbOvY3kZpv27vy0vnD5UPOmJA2eYLd2_9QIOWXUAs6_ju-a6AVr8FB8JCASPMSlZXa3swz3lUdBUi_PFBwjI1nqHYMeWDbHExGWGvNAeEw0Pb8hPUs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a58a5239b.mp4?token=R-rkd3VsZOlaH6X-_3t8JYjWZcwlsumcHGN6JFM9XKZFUV96OKSMV9Mn2slLp3V68wWiBl9xUnUF06V62COkoA6djnH-kIuRqvwdi7d1dA2Z6X-exmmCu4MVylXPnwLDdgWfkCKl6YhiYh1BXwlLrNHXFIJlIhO2cva2UYiPRmTNc_7A8a8K8eaAavw5dMLFlUgQCe0v4lqWRl5aeJvj5I2oE6Fx7pG6gSu96P5xFhagiGQdkAvGoIgLa7tI8aKk05hU3tQxicEiMSM13dLP-6UdLvooeEuge3Lv9bNK18qpNbrBdIAievvsa_Vs4kKSThZA5NazXLa06St7Vu1d_W1LEZKXqbHioG9eJ4wTEEBbS8fCBBXRlYt2GWG9VZwrCIZoUIfgyWMzzFUQiztl0tNWWfg4c-PpZlA5DqvPbUCi7uQkWAmj5kStLGQ-WhkGsQ-iJGxFqH408Hplhq2qpNMuWkMEQ0w8HWMb9orsrCBHyoBVX1v-WeIhUG0cDWjs0u1z-UlrIBmZYLEK1FWG20AU8COUrFTLKLwmWs2-YhKGYmQdUpF0eSjLcQbOvY3kZpv27vy0vnD5UPOmJA2eYLd2_9QIOWXUAs6_ju-a6AVr8FB8JCASPMSlZXa3swz3lUdBUi_PFBwjI1nqHYMeWDbHExGWGvNAeEw0Pb8hPUs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری: گاو که دلار نمیخوره پس چرا قیمت شیر دلاری زیاد میشه؟
🔴
مدیرعامل اتحادیه تعاونی‌های لبنی: اتفاقا دلار میخورن
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/151533" target="_blank">📅 23:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151532">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
ارتش پاکستان: سربازان پاکستانی در «ظرفیت‌ها و حوزه‌های متعدد» در عربستان حضور دارند
🔴
نیرو‌های نظامی ما تحت ائتلاف دفاعی مکه در عربستان مستقر شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/151532" target="_blank">📅 23:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151531">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
سازمان عملیات تجارت دریایی بریتانیا:
گزارشی از وقوع یک حادثه در فاصله ۵۱ مایلی دریایی از شهر الشمال قطر دریافت کردیم
🔴
در پی حمله به یک نفتکش با چندین پرتابه در آب‌های نزدیک قطر، شماری از افراد زخمی شده‌اند
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/151531" target="_blank">📅 23:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151530">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ درباره لهستان: مردم لهستان را دوست دارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/151530" target="_blank">📅 23:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151529">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/unanZ8VnpA1vN7ZYCcb54X9FF2_GgA-3JUn7ajp2YrLfbd7_-RQGMXcjRLJrZi6pI2hZlA2XnkVrQFJMf7dEKe44NnNf7yJ_LTwa_cP7F-BwYHAMnhOnV1N2pdwnDWviq2YcX4Vws7aN2PBzElhn1c4DmICupAYoa0b9iFWlx1wImyzXystbO-OA6atfmNg0OpdJjujWSa55BoYV6Gn2P-EHwNVKnltvCB7t3c5QJdDuOuj7RkA8GbL2g4Fdlj6JwdphruN2L7pEuaFF4yKWdkAvnzjeJpEOht4wGDqDP-x3mqntMsybfMwkfSuMhDcm7nxzCIYs7Ddcd6tl9t188Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آتلانتیک: ترامپ پیش از انتخابات میان‌دوره‌ای دستور حمله گسترده دیگری به ایران را صادر می‌کند
🔴
کاخ سفید از پنتاگون خواست گزینه‌هایی برای حمله به ایران قبل از انتخابات میان‌دوره‌ای آمریکا آماده کند. تصمیم نهایی هنوز گرفته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151529" target="_blank">📅 22:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151528">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ درباره ایران:
فکر می‌کنم داریم خیلی خوب پیش می‌ریم. داریم ایران رو خیلی بد می‌زنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/151528" target="_blank">📅 22:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151527">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: ایران در شرایط سختی قرار دارد و هرگز به سلاح هسته‌ای دست نخواهد یافت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/151527" target="_blank">📅 22:43 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151526">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
گزارش ها شنیده شدن صدای ۴ انفجار در تنگه هرمز
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151526" target="_blank">📅 22:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151525">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🔴
فوری / ترامپ: من با نتانیاهو صحبت کردم و طرف مقابل بهای سنگینی برای کاری که در هفتم اکتبر انجام داد، پرداخت.
🔴
درگیری با ایران به زودی، به هر نحوی، پایان خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151525" target="_blank">📅 22:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151524">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZ4Wpz0BSOdzcAVQBkv2hJN_MGnI8PCX06ZiwoHPBg2XohM2s0uvy4mb-HQJpIImxjsnye6AePzh2cu5sWfBUKJTFcZVEJ-dadtHB9z__sotDJdGuVBFbfP2LO8PKFmw5NwA-9SYHNEurSMVGNSo9-qQdcz4pPtc15TmMbRAUiwm5esUdjydDirTXDBlc7GA9cLHoWC52mWbpjvnGNtU3rPLwNOY-hkHPTGGtVayJAzA5CJSiTneEtHXVrWS0ALPal9CrGWe5ix2tKVvbPzKnDbi0O-CKEnbon40CIK58y8n18FqCNtz8MP9Is6Ke0HKdhpFYNeBlx8E-mege5IPDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت ترامپ: استیو ویتکوف چراغ را روشن نگه می‌دارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/151524" target="_blank">📅 22:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151523">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
فوری / ترامپ: درگیری با ایران به زودی، به هر نحوی، پایان خواهد یافت
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151523" target="_blank">📅 22:19 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151522">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
دو منبع دیپلماتیک منطقه‌ای به i24 نیوز: احتمال دارد تهران یک حمله پیش‌دستی را آغاز کند - به دلیل نگرانی از یک حمله آمریکایی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/151522" target="_blank">📅 22:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151521">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fbc004919.mp4?token=LNwcGLjX3-N1up14c_FNFDyVI-uZ1opKBGVgvolBlIFr4YDW32i_k8pOvkxyaXv-lu6vhyq3wz9rJ8snSTb7nE81XgZJXLHkxtlAf9ZpNF9q44P83ib53fHe8Av1ssTvQhXs27ha5hEID5SKmmJYl_snHb28NmZhlrrE7d0eh_xPxwNoMU-lP1cWYgQtwkg2e88kFqfdeKTGdU3wMypx7ZwUh5yMVmdV26a8MoTt9YbE9WtFx8OY8SYYC9nSe8Cn7KRgUcVUJTEsi_9D5w3x2-8yQ64ZUePl_jNKoKzPF74QNWXlpj3zeQ_rozRLccTQnrko61IkvKVKW1mAKVrT9bZtvlya78dGaypiOfbOX3UK08xyAKx3ZAWX6Yr5nLeJziY9ywVeN558St6jGBH0qUdQlR_d70U86EXCZQqU8_GoreRYFZ0L8pRNpEd8vWa82-ZFoltvgEJz1qsv3TKU8GXXS3idr0CFqT1Q_Qt8G068fznDqQPF1P1ZwPh81XUHoE8tjKV9to-bXjAj1fUurBedibtha9AYPjWJdzlmZcQWiLFz8LPJOY9cvOjPjhbge8LTjiTeQKh4Ber3IvpJltLRXBvPpuaMWik3N86J_FZ9KJn8A7X7f2ATaR0gnpxYGXVi8Qp48bOY-cOyk-1erjT2oCIKkHd97RMGfBRwDcE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fbc004919.mp4?token=LNwcGLjX3-N1up14c_FNFDyVI-uZ1opKBGVgvolBlIFr4YDW32i_k8pOvkxyaXv-lu6vhyq3wz9rJ8snSTb7nE81XgZJXLHkxtlAf9ZpNF9q44P83ib53fHe8Av1ssTvQhXs27ha5hEID5SKmmJYl_snHb28NmZhlrrE7d0eh_xPxwNoMU-lP1cWYgQtwkg2e88kFqfdeKTGdU3wMypx7ZwUh5yMVmdV26a8MoTt9YbE9WtFx8OY8SYYC9nSe8Cn7KRgUcVUJTEsi_9D5w3x2-8yQ64ZUePl_jNKoKzPF74QNWXlpj3zeQ_rozRLccTQnrko61IkvKVKW1mAKVrT9bZtvlya78dGaypiOfbOX3UK08xyAKx3ZAWX6Yr5nLeJziY9ywVeN558St6jGBH0qUdQlR_d70U86EXCZQqU8_GoreRYFZ0L8pRNpEd8vWa82-ZFoltvgEJz1qsv3TKU8GXXS3idr0CFqT1Q_Qt8G068fznDqQPF1P1ZwPh81XUHoE8tjKV9to-bXjAj1fUurBedibtha9AYPjWJdzlmZcQWiLFz8LPJOY9cvOjPjhbge8LTjiTeQKh4Ber3IvpJltLRXBvPpuaMWik3N86J_FZ9KJn8A7X7f2ATaR0gnpxYGXVi8Qp48bOY-cOyk-1erjT2oCIKkHd97RMGfBRwDcE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، پس از اینکه متوجه شد دریانوردان کشتی جنگی یواس‌اس آبراهام لینکلن در طول جنگ با جمهوری اسلامی ایران عملکرد بهتری نسبت به آنچه او در ابتدا تصور می‌کردند داشته‌اند، دو بار شنا انجام داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/151521" target="_blank">📅 22:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151520">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DkCL5R5SvUgVoLQf6E6rZWWyHl2nBTaaY00fuiPKHC4dKjS7E7Hn5I0F4AYOjVHBgNxK6mY-6kXYeyLF2kh0mucc9Mhrs2_nbwDJf8wQqZTgjbc2yF9lT1IKBfxHl5y4ebInMyL8UjjvRFlCvaTSxUtU_zccq-LX4B3X1syCIu9o12-vemmLTSiWMwdy3e1fexMjNycKZ2PsbO6I3wYjE1taCpvAtDhYhvZFpWniVYj4L8WnuPto5f3tK64xkZdtpGz4cno7zySj00UbkP5lM0ncD_MXqpsCDit4PY03YMqhprzItGaqAfFdFudQ09NhbrPK2tj4Wn9mCS_oWuo3rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
این وسط گروه هکری عدل علی تصاویر برهنه و منشوری مسیح علینژاد رو منتشر کرد
😐
😐
😐
😐
😐
🚨
مشاهده فوری عکس‌ها</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/151520" target="_blank">📅 22:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151519">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، پس از اینکه متوجه شد دریانوردان کشتی جنگی یواس‌اس آبراهام لینکلن در طول جنگ با  ایران عملکرد بهتری نسبت به آنچه او در ابتدا تصور می‌کردند داشته‌اند، دو بار شنا انجام داد.
🔴
ما با نیروی دریایی ایران توافق کردیم. تصمیم گرفتیم اقیانوس را با آن‌ها تقسیم کنیم.
🔴
نصف پایین را آن‌ها گرفتند.
🔴
چند نفر در رسانه‌ها سعی کردند ناو آبراهام لینکلن را به نمادی از بی‌نظمی، روحیه پایین یا مأموریت ناموفق تبدیل کنند.
🔴
وقتی به شما نگاه می‌کنم و با رهبران شما صحبت می‌کنم، می‌دانم که دقیقاً برعکس این است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151519" target="_blank">📅 22:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151518">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
سفارت آمریکا در عربستان به حالت هشدار درآمد
🔴
در پی تشدید محاصره یمن علیه حریم هوایی عربستان، هیئت دیپلماتیک آمریکا در ریاض با صدور یک اطلاعیه فوری، سطح تدابیر امنیتی برای اتباع و کارکنان خود را افزایش داد.
🔴
به دلیل احتمال بالای تشدید درگیری‌ها و حملات به فرودگاه‌ها، سفارت آمریکا نسبت به لغو گسترده پروازها و انسداد حریم هوایی عربستان هشدار جدی داد.
🔴
تردد کارکنان دولت آمریکا در شعاع ۲۰ مایلی مرز یمن ممنوع اعلام شد؛ همچنین سفر به استان‌های جیزان، عسیر، نجران و شهرهای قطیف، ینبع و طائف نیازمند مجوز ویژه امنیتی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151518" target="_blank">📅 21:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151517">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
حمله مسلحانه به مقر انتظامی در گلشن
🔴
بنا بر اعلام منابع آگاه دقایقی قبل یکی از مقرهای انتظامی در شهرستان گلشن مورد حمله مسلحانه قرار گرفت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151517" target="_blank">📅 21:57 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151516">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
کانال ۱۴ اسرائیل: سازمان سیا به اسرائیل فهرستی از حدود ده مقام ارشد ایرانی که نباید هدف ترور قرار گیرند، تحویل داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/151516" target="_blank">📅 21:51 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151515">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
ترامپ : به محض اینکه جنگ با ایران تمام شود قیمت نفت مثل موشک سقوط خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151515" target="_blank">📅 21:30 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151514">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e69a46df1.mp4?token=AKrN6YSPIzzvnxOIQYazbPH5AxrDnTBDjnMwV3EgJB6-u5LWd8ShYztQUB1sbS8hV1yPvGIVaQZf0fa0sjX4m9B1w2DV6hSsdnOsbn6JAPMVMIp-XX7LeJN-nwBMyPAfEjG2qtB5ngAoWcxgvEMo_8bDa8qBD5cFOgm8I4H2VB1XEib7erTDa98nD8MxpIix6hjq899YltGPSXtk6TmTpqg3R6LiQxs4NqLfB15LEYaU_FqvhTizDSB4SzMIWxUfgc_3p_qGzLw7Gq7S2xjwQr2hKq38gN2B4crnHgB8nibPQkT5yJDaTy7jc28qtsi3xMjBBhZkWBJFjmi7pkiEcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e69a46df1.mp4?token=AKrN6YSPIzzvnxOIQYazbPH5AxrDnTBDjnMwV3EgJB6-u5LWd8ShYztQUB1sbS8hV1yPvGIVaQZf0fa0sjX4m9B1w2DV6hSsdnOsbn6JAPMVMIp-XX7LeJN-nwBMyPAfEjG2qtB5ngAoWcxgvEMo_8bDa8qBD5cFOgm8I4H2VB1XEib7erTDa98nD8MxpIix6hjq899YltGPSXtk6TmTpqg3R6LiQxs4NqLfB15LEYaU_FqvhTizDSB4SzMIWxUfgc_3p_qGzLw7Gq7S2xjwQr2hKq38gN2B4crnHgB8nibPQkT5yJDaTy7jc28qtsi3xMjBBhZkWBJFjmi7pkiEcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: آیا روسیه اطلاعات کافی در مورد وضعیت طاعون در سیبری ارائه کرده است، و آیا ایالات متحده درخواست اطلاعات بیشتری کرده است؟
🔴
ترامپ: آن‌ها مقداری از این اطلاعات را با کارشناسان ما در میان گذاشته‌اند. ما انتظار داریم که آن‌ها اطلاعات بیشتری را با کارشناسان ما به اشتراک بگذارند.
🔴
من همین الان با کارشناسان خود ملاقات کردم. ما متخصصان بسیار باهوشی داریم. آن‌ها از تمام جزئیات آنچه در حال وقوع است، آگاه هستند، و تمام این اطلاعات از طریق آن‌ها منتقل می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/151514" target="_blank">📅 21:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151513">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b1e7109c3.mp4?token=NZi_EsNB8Ti19vNAY-tiaZNyeq62BZSUJCZqAQAKYhofS7Wm3aisawJvmgQ4EaX_fRF2WeYdJz8Kc5jIG9cbkQ8-cU_D5n1iU0uV8C5jKVYbyNJAe_CIBd56QePdgP2s8FOnBYVhnf-5Y-mXXAUm_F6Wpa8sJWwSG1gtDsbicRIJSGMWPYmGAmXDy07VixL3UiqGWPdx93l4nbrD-ckZjRzV8M-aSXkGfAmscb0yk3f28iTmgxz1qiY-kOcMWA3Nrw0MYcdbFijVVMBj4HMXQu1nyZXL1VN9cpba_rsTMyj0_HQM8VAUhkkpZS_wH85r949HBs_Kb5ftuGjiT_KzIgy1P4y7EetwyzCm5b4gWU3eb88Ea3KF7A1vrUYByH6P1qOkA-mZiq0TZraksj5GTlueUe5VsSocyCyqW6MhQDrQVnPgBtm0OwSaGCbnqbstoT6xWOR9oY075C4WLGM2iug-ZeLTfGESkuNsR0R7NivlnK0FQUimWouFnEUeOwh96uGYYh4qboWUfQDkZxhrEwuoaHrxJXD2CysH8SKlaaR18Q-bdIwajcEzlxqPTmx7ro896u8AcPioY20DWcpY5P768rmDk5Gqd630LctAIn3vWLdbP7geMwM56zgT4_f5SXDJfADn-f1fb0SjserchawVX_iH7l4lMzlk9_j2nUI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b1e7109c3.mp4?token=NZi_EsNB8Ti19vNAY-tiaZNyeq62BZSUJCZqAQAKYhofS7Wm3aisawJvmgQ4EaX_fRF2WeYdJz8Kc5jIG9cbkQ8-cU_D5n1iU0uV8C5jKVYbyNJAe_CIBd56QePdgP2s8FOnBYVhnf-5Y-mXXAUm_F6Wpa8sJWwSG1gtDsbicRIJSGMWPYmGAmXDy07VixL3UiqGWPdx93l4nbrD-ckZjRzV8M-aSXkGfAmscb0yk3f28iTmgxz1qiY-kOcMWA3Nrw0MYcdbFijVVMBj4HMXQu1nyZXL1VN9cpba_rsTMyj0_HQM8VAUhkkpZS_wH85r949HBs_Kb5ftuGjiT_KzIgy1P4y7EetwyzCm5b4gWU3eb88Ea3KF7A1vrUYByH6P1qOkA-mZiq0TZraksj5GTlueUe5VsSocyCyqW6MhQDrQVnPgBtm0OwSaGCbnqbstoT6xWOR9oY075C4WLGM2iug-ZeLTfGESkuNsR0R7NivlnK0FQUimWouFnEUeOwh96uGYYh4qboWUfQDkZxhrEwuoaHrxJXD2CysH8SKlaaR18Q-bdIwajcEzlxqPTmx7ro896u8AcPioY20DWcpY5P768rmDk5Gqd630LctAIn3vWLdbP7geMwM56zgT4_f5SXDJfADn-f1fb0SjserchawVX_iH7l4lMzlk9_j2nUI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: به کسانی که این نظر را مطرح می‌کنند که شما صرفاً قبل از انتخابات، پول به مردم می‌دهید تا برای جمهوری‌خواهان رای دهند، چه می‌گویید؟
🔴
ترامپ: خب، کاری که ما انجام می‌دهیم این است که رشد اقتصادی فوق‌العاده‌ای داریم. شما همین حالا هم شاهد آن هستید، اما اعداد رشد اقتصادی را خواهید دید که هیچ‌کس قبلاً ندیده است.
🔴
ما می‌توانیم کارهایی را انجام دهیم که دموکرات‌ها نمی‌توانند، زیرا آن‌ها نمی‌توانستند مانند ما، از تعرفه‌ها به این شکل هوشمندانه استفاده کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/151513" target="_blank">📅 21:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151512">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2920ff853.mp4?token=qtJ9ab14bUcEXJm-szjjWfBMr2iX4GRRA6f7eS2SwNnRkERRadDMHJboIuLEniPyTh_4n5b9sIzSk_frScMM3jX4WzdgzXtOEVbS2WzO4CIeIbSQozzghDa0SPkcXW1tRuqPkaP-bdiNy6NJ2YQ1OK-tlw4GeurkEGRnbKrpZNSYOPcQsrSuRylbV0IQ617MZVcWugQhHUgUQNnEx3u131RGc4jQdsHnxTFWmfMeu4jMebIy6DMp6WLMNIpud_ZPAu4pFXJniFb-9vk5SpoWiFAzamLymi1Znc9jzlYe8TwP-sTwK1Ns-fAUjEO9CkoIuhVjK6vTj1x4gbL3d6gjeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2920ff853.mp4?token=qtJ9ab14bUcEXJm-szjjWfBMr2iX4GRRA6f7eS2SwNnRkERRadDMHJboIuLEniPyTh_4n5b9sIzSk_frScMM3jX4WzdgzXtOEVbS2WzO4CIeIbSQozzghDa0SPkcXW1tRuqPkaP-bdiNy6NJ2YQ1OK-tlw4GeurkEGRnbKrpZNSYOPcQsrSuRylbV0IQ617MZVcWugQhHUgUQNnEx3u131RGc4jQdsHnxTFWmfMeu4jMebIy6DMp6WLMNIpud_ZPAu4pFXJniFb-9vk5SpoWiFAzamLymi1Znc9jzlYe8TwP-sTwK1Ns-fAUjEO9CkoIuhVjK6vTj1x4gbL3d6gjeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : ما باید کمترین نرخ بهره را در جهان پرداخت کنیم
🔴
کشورهایی وجود دارند که اگر به خاطر ایالات متحده نبودند، متحمل زیان‌های هنگفتی می‌شدند، و آن‌ها را کشورهای پیشرفته می‌دانند، در حالی که آن‌ها نرخ بهره‌ای بسیار پایین‌تر از ما پرداخت می‌کنند
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151512" target="_blank">📅 21:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151511">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d789c09213.mp4?token=hPJcpAaF7gRuH20es6OZ1_O9jTTIrrxCtHjj6Sz5PxyhN9PQOhJywI2UEC1xoRTcc1uzD_0OeS8WKdCVH7Y-pdT6DE3Isp7uCLeas1EfLkIY1He9VOuyKY4iPF_K6h6ySZyl9Y3ga3nu9edzlsyOoMWTUZv2JXNPb-J1eWN5BWvSGn9Ej-_oK3Zg7dmn9ut_lm1pmUjjw-S3OBsLUJcvp_Eumhlf96K6WFOTLFa3YmJwO9PHvkQnU8Ul6_GQiOBC8vie5ZF1Fw4gfIBAZnNb6_Ife8-hBRjdmNU6UD6yi7ujp686FTH47q1YvnFetxI7ny-8FR41suwde2I_vYwh9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d789c09213.mp4?token=hPJcpAaF7gRuH20es6OZ1_O9jTTIrrxCtHjj6Sz5PxyhN9PQOhJywI2UEC1xoRTcc1uzD_0OeS8WKdCVH7Y-pdT6DE3Isp7uCLeas1EfLkIY1He9VOuyKY4iPF_K6h6ySZyl9Y3ga3nu9edzlsyOoMWTUZv2JXNPb-J1eWN5BWvSGn9Ej-_oK3Zg7dmn9ut_lm1pmUjjw-S3OBsLUJcvp_Eumhlf96K6WFOTLFa3YmJwO9PHvkQnU8Ul6_GQiOBC8vie5ZF1Fw4gfIBAZnNb6_Ife8-hBRjdmNU6UD6yi7ujp686FTH47q1YvnFetxI7ny-8FR41suwde2I_vYwh9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره سوئیس:
اگر به سوئیس نگاه کنید، کشوری بزرگ، بسیار بزرگ و زیبا با کسری بودجه قابل توجه. با این حال، آن‌ها را از نخبگان می‌دانند.
🔴
خب، اگر تصمیم می‌گرفتیم ساعت از سوئیس نخریم، دیگر نخبگان محسوب نمی‌شدند و ما حدود 40 میلیارد دلار صرفه‌جویی می‌کردیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151511" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151510">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ : نمی‌توانید با ریاست‌جمهوری با بی‌احترامی رفتار کنید.
🔴
من فرصت‌های زیادی برای انتقاد از بایدن، هیلاری کلینتون و باراک هوسین اوباما داشته‌ام و همچنان هم دارم
🔴
و افراد زیادی به من گفته‌اند: "بیا بریم و آن‌ها را شکست دهیم." من گفتم: "نه، شما نمی‌توانید این کار را در حق ریاست‌جمهوری انجام دهید.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/151510" target="_blank">📅 21:27 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151509">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
ترامپ : من می‌توانم هر کاری که بخواهم انجام دهم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151509" target="_blank">📅 21:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151508">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b33175d5d.mp4?token=mHRmfw_OixODhwqY__2Gz-IjtLsQaoDjTyzRZNH7qcG3Y6nV6KyTUwv_bjhmaXe-ERjy7i5rG9Fz3K81lf60YdTqM-yGguNOc2BoeGrtGKt7G1zZpZP824hF87CGqr_j0vU5TFAjN3GAiSfTSMXMWdLzg7E8BoNZ2ZZ_8Sw-KD17AN2x2HojDHhUhVYYH7HY5N78A30aL0XYuEkguQQ8Dj9IGtOx0c-UWdEAyBLiGzLbjsZJMWN_rn9ABOwCgCa_sDpBQGLi4vv7FBXsbX61TfslL1vmbGHhIKikfJ_1hQb64eRAWg11LkFDPXZOJZnT0XFb0vbtex6ClkJHNCTesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b33175d5d.mp4?token=mHRmfw_OixODhwqY__2Gz-IjtLsQaoDjTyzRZNH7qcG3Y6nV6KyTUwv_bjhmaXe-ERjy7i5rG9Fz3K81lf60YdTqM-yGguNOc2BoeGrtGKt7G1zZpZP824hF87CGqr_j0vU5TFAjN3GAiSfTSMXMWdLzg7E8BoNZ2ZZ_8Sw-KD17AN2x2HojDHhUhVYYH7HY5N78A30aL0XYuEkguQQ8Dj9IGtOx0c-UWdEAyBLiGzLbjsZJMWN_rn9ABOwCgCa_sDpBQGLi4vv7FBXsbX61TfslL1vmbGHhIKikfJ_1hQb64eRAWg11LkFDPXZOJZnT0XFb0vbtex6ClkJHNCTesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : من می‌توانستم کارهای بسیار بدی علیه هیلاری کلینتون انجام دهم. می‌توانستم کارهای بسیار، بسیار بدی علیه جو بایدن انجام دهم. می‌توانستم کارهای بسیار بدی علیه باراک اوباما انجام دهم.
🔴
من فکر می‌کردم که انجام این کارها نامناسب است، زیرا باید با مقام ریاست‌جمهوری با احترام رفتار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151508" target="_blank">📅 21:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151507">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d2922b16b.mp4?token=SSRudYsNPTxGxeskUUuQfaKKrBUuUvT63WJdXRbYdD5DA6BGINYfET3SdBUyU1h4m3iSmJydeWtk_b1nvCyYTCygxPaEnrW5KvUAj7v3EnoDcW2B1f387mkSHs0Qnbmg5CXfNJW_Qt90Ad7BJGP3mvtHG1u-QqMK3dMwtLUXyUpfivzoTWZMdpM9icAVZPvOy3b3YEwFiIlDTCEqcOW9KKahfnkxfLIpuUQdJq_p_54zFhHoI9QtEsGkjMtIm_u7vdNeb-jxEmRFUIt7znCn573Tg9QESue38Vjbp-TJ7dOvXV99NKa6CwNwGn9aCCwX5h7lhTP3mVaEX7kuoPFnTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d2922b16b.mp4?token=SSRudYsNPTxGxeskUUuQfaKKrBUuUvT63WJdXRbYdD5DA6BGINYfET3SdBUyU1h4m3iSmJydeWtk_b1nvCyYTCygxPaEnrW5KvUAj7v3EnoDcW2B1f387mkSHs0Qnbmg5CXfNJW_Qt90Ad7BJGP3mvtHG1u-QqMK3dMwtLUXyUpfivzoTWZMdpM9icAVZPvOy3b3YEwFiIlDTCEqcOW9KKahfnkxfLIpuUQdJq_p_54zFhHoI9QtEsGkjMtIm_u7vdNeb-jxEmRFUIt7znCn573Tg9QESue38Vjbp-TJ7dOvXV99NKa6CwNwGn9aCCwX5h7lhTP3mVaEX7kuoPFnTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره جایزه صلح نوبل: صرف نظر از اینکه من این جایزه را دریافت کنم یا نه، من کارهای بسیار بیشتری انجام داده‌ام، و فکر می‌کنم این موضوع باعث تضییع اعتبار آن‌ها خواهد شد.
🔴
[باراک] اوباما آن را دریافت کرد، اما هیچ کاری انجام نداد. او هنوز نمی‌داند چرا آن را دریافت کرده است. او آن را زمانی دریافت کرد که انتخاب شد، درست در ابتدای کارش. و او هیچ ایده‌ای نداشت که چرا آن را دریافت کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/151507" target="_blank">📅 21:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151506">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پیتر دوکی از شبکه فاکس: شما می‌گویید که دموکرات‌ها شما را استیضاح خواهند کرد. به چه دلیلی؟
🔴
ترامپ: آن‌ها نمی‌دانند
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/151506" target="_blank">📅 21:25 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151505">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8ed562e7.mp4?token=vmp-emckdZG-p4ZJNLYG6buOkELBMWjqgSv_gvW-NeMjvN-6tYHGGNZqK8IriYff5z6RMKTwWFAo4Q8_Svp1qA71pXnDF8Iocffd7BPe3azuUq-j4v1Z4ibTxqAsH3qMYU7fM_-iUAwOgjDvfHD8oiNXSC2uqsbmFJuS7oEb8rRzMXVkxKYj2RWVrRtGkOTP6Ev8kXba2ezo2vwUeHirS8qVKni1xD8N4Dhpt-paFBlQgfafdAThAy_1HZDduhbvVVc7vaOsauxIejhXsvSBiY3mKeIyVr1RLuOQwlDu7SCuLWD0WEZISRvDizgfH1f78Brg2k7s3_vLMAi-DzTaag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8ed562e7.mp4?token=vmp-emckdZG-p4ZJNLYG6buOkELBMWjqgSv_gvW-NeMjvN-6tYHGGNZqK8IriYff5z6RMKTwWFAo4Q8_Svp1qA71pXnDF8Iocffd7BPe3azuUq-j4v1Z4ibTxqAsH3qMYU7fM_-iUAwOgjDvfHD8oiNXSC2uqsbmFJuS7oEb8rRzMXVkxKYj2RWVrRtGkOTP6Ev8kXba2ezo2vwUeHirS8qVKni1xD8N4Dhpt-paFBlQgfafdAThAy_1HZDduhbvVVc7vaOsauxIejhXsvSBiY3mKeIyVr1RLuOQwlDu7SCuLWD0WEZISRvDizgfH1f78Brg2k7s3_vLMAi-DzTaag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خبرنگار: آیا تا الآن با ولادیمیر پوتین صحبت کرده‌اید؟
🔴
ترامپ: امروز یک تماس هماهنگ کرده‌ام. امروز تولد ولادیمیر پوتین است. مطمئنم که شما تولدش را جشن می‌گیرید
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151505" target="_blank">📅 21:24 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151504">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=uw8SCOzvfYFfRPRGg8mQchrfZx6eEvucgAQuvBRSDWvw19wTEeGXoP9u5sY_BT0vLTk_z2XnzNQjU5BN6dgM15GtIbNS5YqTJbN-0uF31hnatRkaJ_ECZ92CQdLKogEoHysjWAjoNcVkJw-F2Ca-6x5nQYOTrZnGhK1MAlzAR0BjfP9RmlGNZE9t3EGsQPdte9CWVMQW7zIzMxLhlJqIfrDJnj6fGaVexzaAnm7wp_q_jJmb8LNuZWcCoeMTHSOejGcca0Foby3mVGqTcLJ4s1huDpYzS5x59_QSkEJffKwMUtAy4aRRbUDlvdwzkIA6AQf3Y3kpJK7e0uA_8vlkGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b310f181e.mp4?token=uw8SCOzvfYFfRPRGg8mQchrfZx6eEvucgAQuvBRSDWvw19wTEeGXoP9u5sY_BT0vLTk_z2XnzNQjU5BN6dgM15GtIbNS5YqTJbN-0uF31hnatRkaJ_ECZ92CQdLKogEoHysjWAjoNcVkJw-F2Ca-6x5nQYOTrZnGhK1MAlzAR0BjfP9RmlGNZE9t3EGsQPdte9CWVMQW7zIzMxLhlJqIfrDJnj6fGaVexzaAnm7wp_q_jJmb8LNuZWcCoeMTHSOejGcca0Foby3mVGqTcLJ4s1huDpYzS5x59_QSkEJffKwMUtAy4aRRbUDlvdwzkIA6AQf3Y3kpJK7e0uA_8vlkGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ درباره ایران: من، شاید، از نابودی کامل جهان جلوگیری کرده‌ام، زیرا ایران هرگز سلاح هسته‌ای نخواهد داشت. و این یک اتفاق بسیار مثبت است
🔴
رؤسای جمهور دیگر باید این کار را قبل از من انجام می‌دادند، یا کسی باید این کار را انجام می‌داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/alonews/151504" target="_blank">📅 21:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151503">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ترامپ : من هشت جنگ را خاتمه دادم. یک جنگ دیگر هم در راه است. من تمام گروگان‌ها را آزاد کردم.
🔴
من کارهایی را انجام دادم که هیچ کس دیگری هرگز انجام نداده است. من در حال تفاخر نیستم، فقط حقایق را به شما می‌گویم.
🔴
احتمالاً هیچ رئیس‌جمهور دیگری جنگی را خاتمه…</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/151503" target="_blank">📅 21:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151502">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
ترامپ : من هشت جنگ را خاتمه دادم. یک جنگ دیگر هم در راه است. من تمام گروگان‌ها را آزاد کردم.
🔴
من کارهایی را انجام دادم که هیچ کس دیگری هرگز انجام نداده است. من در حال تفاخر نیستم، فقط حقایق را به شما می‌گویم.
🔴
احتمالاً هیچ رئیس‌جمهور دیگری جنگی را خاتمه نداده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/alonews/151502" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151501">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b240a5223.mp4?token=PC-wyxuhWj3OOWdnJoyLsd3e4H5EnTLEvr7sLso3TC3I4sFE-ed6iTWZoPm95P2Yy5i8s17JB7ote1u8_CNbTlSYSXG6ePwTSbzRXisdtKRUuVF8u94mktlkf7Ab8pFj2tPcqGTEqHM9-bnq6GEtMaWU76mblZGvhSaBHr51IV6moeMpkbaE_80VE7JHqJq79s7tLNC2X6cEFieIuhFx39zW3P0Agik6smTnVCsv8AYHCygbjfxvkWKZUXlk1qZxacrHCOUXv2tIUDZLLZmHCojfLbYwfnTLvLV-8ShBPcir0g_e9NqkX7zba4BvKA_J2EarUx24qn6BJTyXIGgm6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b240a5223.mp4?token=PC-wyxuhWj3OOWdnJoyLsd3e4H5EnTLEvr7sLso3TC3I4sFE-ed6iTWZoPm95P2Yy5i8s17JB7ote1u8_CNbTlSYSXG6ePwTSbzRXisdtKRUuVF8u94mktlkf7Ab8pFj2tPcqGTEqHM9-bnq6GEtMaWU76mblZGvhSaBHr51IV6moeMpkbaE_80VE7JHqJq79s7tLNC2X6cEFieIuhFx39zW3P0Agik6smTnVCsv8AYHCygbjfxvkWKZUXlk1qZxacrHCOUXv2tIUDZLLZmHCojfLbYwfnTLvLV-8ShBPcir0g_e9NqkX7zba4BvKA_J2EarUx24qn6BJTyXIGgm6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
گزارشگر: ما شاهد آشوب‌هایی در فرانسه بوده‌ایم. شما این پیام را منتشر کردید: «آنچه در فرانسه اتفاق می‌افتد، از کنترل خارج است. مهاجرت گسترده.» آیا این می‌تواند در ایالات متحده نیز رخ دهد؟
🔴
ترامپ: ما جلوی آن را گرفتیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151501" target="_blank">📅 21:12 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151500">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZjkzfP3L7b992YqME1lvEaQOQ6ZpTK43KMFEuE_d28HN5yVe0kWKO-WoOnVbQb41qEE_0PjRN6v_MndkrzG4C6oF1qxIJmvFAc69DIGRYDPMvgFIhVFvkplq5OH2fFgXA9T4wrNETINBlb66rCyIap3dh3e81lIBaqOIJVsK1sroKrmEgXMtoJPKcRjO37KaSLF01eR-Sm0z27u2NimyD2cBnlfRnxrNXKBxIFNU_2demU_dsFT_YU3RQ-lIWTQ0GGDCIXSl84AQw2dxGm2mgVc1WD-AzHfiNPTQHM4UYnruQGqPP8IK2RC2Mlv1FJqd3Adw0ea7WE43LLROaj5yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بیت‌کوین در حالی که بازدهی اوراق ۳۰ ساله آمریکا به بالاترین سطح خود از سال ۲۰۰۲ رسید، به زیر ۸۳,۰۰۰ دلار سقوط کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/alonews/151500" target="_blank">📅 21:11 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151499">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d02a2eddf.mp4?token=PpV3bVJkZFVuFqktgoM9xcMmkWwiYmuGctT5u-YqhLeo9QQaKXZzRAlHPpemJAqcDxhgrBpGoghLSg-wqY3Ujr1yVJbBGb5-Rd9JQeJxdZ3Pd-exLChR4-Euu3umRahcAMbvNf9w1HffxHB5dkuqizdKcCiPMRAmJ9XxQMq11q8J5wg6Ls8_0qfvBuIg2EYpH86QJfIHCu8LII-2CQ-0TjqNm1NH93StnhFlf5eIwSa_ZgmdRbpLtY3YpUbzfvhOMY-wj34PfBP5-rIFwsWPDgV1ptMU28yz9w7T2ZHAaKC3t855ewJ22y1x19hAuEA8Frf5ZA0-AF2eaYeOf3ra8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d02a2eddf.mp4?token=PpV3bVJkZFVuFqktgoM9xcMmkWwiYmuGctT5u-YqhLeo9QQaKXZzRAlHPpemJAqcDxhgrBpGoghLSg-wqY3Ujr1yVJbBGb5-Rd9JQeJxdZ3Pd-exLChR4-Euu3umRahcAMbvNf9w1HffxHB5dkuqizdKcCiPMRAmJ9XxQMq11q8J5wg6Ls8_0qfvBuIg2EYpH86QJfIHCu8LII-2CQ-0TjqNm1NH93StnhFlf5eIwSa_ZgmdRbpLtY3YpUbzfvhOMY-wj34PfBP5-rIFwsWPDgV1ptMU28yz9w7T2ZHAaKC3t855ewJ22y1x19hAuEA8Frf5ZA0-AF2eaYeOf3ra8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ : این کودکان خردسال... فکر می‌کنم می‌توانم از این اصطلاح استفاده کنم. باید مراقب باشید
🔴
گاهی اوقات، شما کسی را کودک می‌نامید که حدود شش ماه از سنی که باید کودک نامیده شود، بزرگتر است، و در نتیجه، خشم رسانه‌ها را برمی‌انگیزید
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/151499" target="_blank">📅 21:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151498">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
🔴
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
🔴
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/151498" target="_blank">📅 21:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151497">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/578f2076e4.mp4?token=IgRtPLUwrmGH7WLxc5KKC51l2N6gpvAt_ZjWU-UinTuieNbj031Jac6wFHjnUiHuOgei2EqOx1YzcjS4p0qB6nGhrRVhDiAzWKTE-3qkhlqf2VyO5tyvgvN2yO3ejmyptPx0os1DQ5Ip0vkv4QbxrBR3ABuBjlAysM81yKu6pH5LFnKwjlOnA4bn5AN_2X0I8VhwNnWYWO2xZR_nA9C5n6PTltf4Sbwxq4oHOaaQec_KwQxQa0A-vvGvAwxP9-IukMMq-2fv7o7wS8U5RVfru30uLWRFCI2Yv92jO8mpgkRgHlps9fc5eJTuLKoQfrzT_4u96e4w2iKSA1-d0GRwLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/578f2076e4.mp4?token=IgRtPLUwrmGH7WLxc5KKC51l2N6gpvAt_ZjWU-UinTuieNbj031Jac6wFHjnUiHuOgei2EqOx1YzcjS4p0qB6nGhrRVhDiAzWKTE-3qkhlqf2VyO5tyvgvN2yO3ejmyptPx0os1DQ5Ip0vkv4QbxrBR3ABuBjlAysM81yKu6pH5LFnKwjlOnA4bn5AN_2X0I8VhwNnWYWO2xZR_nA9C5n6PTltf4Sbwxq4oHOaaQec_KwQxQa0A-vvGvAwxP9-IukMMq-2fv7o7wS8U5RVfru30uLWRFCI2Yv92jO8mpgkRgHlps9fc5eJTuLKoQfrzT_4u96e4w2iKSA1-d0GRwLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پیتر دوسی از فاکس نیوز: آیا طاعون در روسیه یک سلاح بیولوژیکی است؟
🔴
ترامپ: ما اینطور فکر نمی‌کنیم. به‌زودی متوجه خواهیم شد، اما فکر نمی‌کنیم که اینطور باشد
🔴
روس‌ها می‌گویند که این موضوع کاملاً تحت کنترل است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/alonews/151497" target="_blank">📅 21:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151496">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LpLho3SiYRDce-hSHH-x64uq9fGQaeXRphlnfViEOohD2gFj8llEb6QHt2YJrHx9VS3eBMAQsfcPsgpgowWyYAXpsEYQ-4gkC_pypx_RjAc9j8HLAxiYx5GPF522j3KzhZSB18ZMaMyz4qqGJVcBuOxuDzqjvQcF7UCUnd6PAGes1GefOuiJMGRtkmUbJFoX1W_4dd6h0VQzuO1jsZa_gfnfX_-2aquwOIkpIrt5EF1tAOXoj8JYPcwsDhw-gqZ65JyE4GUFEGXxCDkLympIQY0w7Wvuh5B5YFgR5JZr7tw7LZ2NvZtYfoxzxccpp7OFh6x9OIP9TLFrLDWQnJEQtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نماینده تهران خطاب به پلیس فرانسه:
باتوم بر سر دانش‌آموزان؟ مگر پاسخ مطالبات نوجوانان و جوانان از راه چماق و سرکوب و زندانی کردن ۵۰۰۰ دانش آموز است؟ چرا به‌جای سرکوب، بستر گفت‌وگوی مدنی و شنیدن صدای معترضان را فراهم نمی‌کنید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/151496" target="_blank">📅 20:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151495">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
عبدالله سرحدی، یکی از مقامات جبهه پایداری افغانستان (طالبان): "زنان بی فکر هستند، عقلشان کم است، چیزی نمی دانند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/151495" target="_blank">📅 20:49 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151494">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/daXNmZrrClTtZm9wb6QUQhkTxyTKMTNEZNeIGBDGq0SG36njYdAzmj9TDqUjLxtlOAcds-ciLGH9nDtfdXCO6NwXc0akJiQYVnNeSHIx_yq2kLmlHBuSTNVGMiOj1PdibRL5ZzoMZeeTiz-sY-PayU1PdP523xUsJHbRrGSlNSZUXzyzJBt1iSYEIemnNYG89qnhLuJxlZNoU02y0DiNb8uvWNG4JJqwPhsMbdETE1xN96PMOuqghX_09FsLlMyzEEVsMQq_XNd1PUDnmoZbHNX2XofcIki9okUUjlcE6h9bPhiXBx1M2jdGKpw_vrpCg1X_NFbQR5-NrtP1kl0mzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک پهپاد بدون سرنشین مدل "گرن-4" با موتور جت، امروز بر فراز کی‌یف پرواز کرد و تصویری از ولادیمیر پوتین بر روی قسمت زیرین آن نقاشی شده بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/151494" target="_blank">📅 20:44 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151493">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
حدود ۱۰روز از اعتراضات فرانسه گذشته و در کمال تعجب تاکنون کسی کشته نشده
✅
@AloNews</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151493" target="_blank">📅 20:39 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151492">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXinHSJcs968qkcgIDBdBSPnff65OC3C6ahpzzj5K5aoZe7xgZ9Eh8KZw3uU8jn6b6qEb8jYrGjdWOeWjXwfHhzvzrzc_S50HaV012gTLem3AtU_NHZ44JPF4Q3E4TK1JROg10yzq82ep81sxOXtypq53jLXwSR_zZ76HQoWQC2oQbhOUHaZjISXSSSUlRP1foBuJ07wB-A1V6fkhEqOLGnVj1VcTx6Ff3HIZ23BpitJpEvNflY2HMhl2jqLDWsUZx42I_47wAtq6wUiYy7LFPx8a9l621xnNWLmyQzVkO_qOnsECNIO5_VYZ5Qx5Ie0NBdVIk9obsmShjOoSYPi3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ پرواز پهپاد های آمریکایی در آسمان عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151492" target="_blank">📅 20:35 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151491">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🔴
طلا به زودی گرمی 30 میلیون
‼️
🔴
سکه  به زودی 300 میلیون
‼️
🔴
دلار به زودی 300 هزار تومان
‼️
🤍
اگه میخوای بدونی کی وقت خرید طلاست
کی وقت فروشش، تو این کانال بهت میگن
@Tala v dolar
👈</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/alonews/151491" target="_blank">📅 20:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151489">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
رویترز: بر اساس آمار منابع امنیت دریانوردی، حملات به نفتکش‌های عبوری از تنگه هرمز در به بالاترین میزان هفتگی خود از زمان آغاز جنگ ضد ایران رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/151489" target="_blank">📅 20:32 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151488">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qK9H5aXtRYdSdfO5N97DR3NIELpmK4qHabGIAa9C9zUzodF-KT-1PiYKi9SMwUGTMkWU5DgZLNu_1fSaJPBVSwyAqWWpWJffzoqwbIPnTBaR-zRbSNhUuXK0JcEuUWH_O-xeIGGqlK211wWV2GtCIwVL4v1OqcnpnRsVCT3G-D5fpYB8ybjO1edpznTAf1lYBedjwqaMSTQFDZQCjWzeLMPSVfYFUAgn3eUUYcCrnhMoc5NEgRn8Oyni-o79PPALxhGvGqBXUS8DZZnvm9taNEtAuAsFreNvoOTskPxCRcZ7dXmY5piTdp8MnIzE0JdeXaj0wtJaXLzEcYCkPROsVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فرودگاه بن گوریون و فرودگاه رامون: بر اساس گزارش ها امروز چندین هواپیمای سوخت رسان در این دو فرودگاه فرود آمدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/151488" target="_blank">📅 20:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151487">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a37aac2aad.mp4?token=fB9dKeTL5QSo7AsoDXV3xGpvvLnqYD6j9PpWVdQgBdTu-rw3NM0fBCm_ZZQcEUnumOsNjjeA7hbCg1Rt1hQpvTpWg1FTC2wV2IZulijx2xUsAeVaNXe4aqy1ffCkbkg8mMgX0dKEcvPoZU8b9LyzJwKPxjsvkAWjvzCggZjFZmMPknQji3p19xRfh83jjXKA3CpzENP-MmVPIWtdwwwHDbFzH7FowANH0liklFxgeEjfJMnhJ4W3Jm4AbndiR_a3pyojWH8hHjWxRK7atnV-GlUoo9E1WcNzAQJjIWXZrh5MXslUPXuE1DrCBrIQpWSfCLpNMjDy0AqTgYyu2Wm7iw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a37aac2aad.mp4?token=fB9dKeTL5QSo7AsoDXV3xGpvvLnqYD6j9PpWVdQgBdTu-rw3NM0fBCm_ZZQcEUnumOsNjjeA7hbCg1Rt1hQpvTpWg1FTC2wV2IZulijx2xUsAeVaNXe4aqy1ffCkbkg8mMgX0dKEcvPoZU8b9LyzJwKPxjsvkAWjvzCggZjFZmMPknQji3p19xRfh83jjXKA3CpzENP-MmVPIWtdwwwHDbFzH7FowANH0liklFxgeEjfJMnhJ4W3Jm4AbndiR_a3pyojWH8hHjWxRK7atnV-GlUoo9E1WcNzAQJjIWXZrh5MXslUPXuE1DrCBrIQpWSfCLpNMjDy0AqTgYyu2Wm7iw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: تو تگزاس یکی هی میگفت من گیاه‌خوارم، گیاه‌خوار یعنی فقط کاهو دوست داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151487" target="_blank">📅 20:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151486">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🔴
فوووووری / منابع عبری از شنیده شدن صدای انفجار شدید در حیفا خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/151486" target="_blank">📅 20:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151485">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
روبیو، هرچند ممکن است گاه احساسات، پیوندهای محبت میان ایالات متحده و اروپا را تحت فشار قرار داده باشد، اما نباید اجازه شکستن آن‌ها را داد.
🔴
ما باید با هم، متحدی را تقویت کنیم که قادر به مقابله با تهدیدات دوران خود باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151485" target="_blank">📅 20:02 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151484">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
العربیه به نقل از یک منبع ارشد: تلاش‌های میانجی‌گری میان واشنگتن و تهران با بن‌بست مواجه شده است.
🔴
تنگه هرمز دیگر اولویت واشنگتن نیست.
🔴
پیشرفت مذاکرات به پاسخ ایران به مطالبات ترامپ درباره توانمندی‌های هسته‌ای این کشور بستگی دارد
🔴
واشنگتن از ایران می‌خواهد بپذیرد که به توسعه توانمندی‌های هسته‌ای خود ادامه نخواهد داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151484" target="_blank">📅 19:54 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151483">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a2371df48.mp4?token=K4E5ph6jA3J8irbFEgRAP7ygZS0K7s3ovCCKtA3tOUjXJir67dtx7EFAe3gUQ-wE0yOGgvxoYnISs0jHQ32eNk0thM5qwx-WLLIj8jBzdOC37yj_dZu7ffuRs9E6u5om3KhXslEsCoSDS1qMJBb_5Ewd6gZxrQWA-wAl7oMcnCKprrzZKzLRhiVg2KPYj40SyWO-upagKOs24OBEFxa2I8DLtkNFdVnSbBGPHFiihpYQO9q6yt8T19_seNNkeJ8BDBwufDZF6Xum8X_LiJR8pGo1CFrAwEFFSb9X5DPe6a1Am2jgHoQypGxFokEERo8oJHqjn7hQ6zq-9han6CrLCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a2371df48.mp4?token=K4E5ph6jA3J8irbFEgRAP7ygZS0K7s3ovCCKtA3tOUjXJir67dtx7EFAe3gUQ-wE0yOGgvxoYnISs0jHQ32eNk0thM5qwx-WLLIj8jBzdOC37yj_dZu7ffuRs9E6u5om3KhXslEsCoSDS1qMJBb_5Ewd6gZxrQWA-wAl7oMcnCKprrzZKzLRhiVg2KPYj40SyWO-upagKOs24OBEFxa2I8DLtkNFdVnSbBGPHFiihpYQO9q6yt8T19_seNNkeJ8BDBwufDZF6Xum8X_LiJR8pGo1CFrAwEFFSb9X5DPe6a1Am2jgHoQypGxFokEERo8oJHqjn7hQ6zq-9han6CrLCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
خوشحالی ساکنان غزه دقایقی بعد از عملیات طوفان الاقصی در ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/151483" target="_blank">📅 19:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151482">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فرانسه سفیر ایران را احضار کرد
🔴
سخنگوی وزارت خارجه فرانسه اعلام کرد سفیر ایران را دربارۀ آنچه کارزار انتشار اطلاعات گمراه‌کننده دربارۀ اعتراضات دانش‌آموزان خوانده، احضار کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/151482" target="_blank">📅 19:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151481">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31254ec41c.mp4?token=uT9eUfOUQpMXP2Wd3_M90uWL4FWllP2RxzJocyspNoz-j67Ag7rMHz83RKt6XOuTy-kITU_t-VsJPyQOh5qrzOWkz8jeGTj-jtYFnP2vGvcfI2FeyXEBPdhhL8xzw8dwOgEl8loGRhIklTFEK2aJLykNS7ixUcGyT_fgky0a-P0ft3R9cHNUwM2KQu7zOk0qv_wFo61YkJVY6fRrm8V0iOcKGjm1w6_Z13641zHpIvngugj4DE9P7ua8R4fad3oQ733AIeFwH8F3yDCJDJkNX4LdOdVmxiyKcbEX3kT9GL-CIacZ2poIPxXOeQQ4sd0scM4L6gITWGwLQt0O_8LX8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31254ec41c.mp4?token=uT9eUfOUQpMXP2Wd3_M90uWL4FWllP2RxzJocyspNoz-j67Ag7rMHz83RKt6XOuTy-kITU_t-VsJPyQOh5qrzOWkz8jeGTj-jtYFnP2vGvcfI2FeyXEBPdhhL8xzw8dwOgEl8loGRhIklTFEK2aJLykNS7ixUcGyT_fgky0a-P0ft3R9cHNUwM2KQu7zOk0qv_wFo61YkJVY6fRrm8V0iOcKGjm1w6_Z13641zHpIvngugj4DE9P7ua8R4fad3oQ733AIeFwH8F3yDCJDJkNX4LdOdVmxiyKcbEX3kT9GL-CIacZ2poIPxXOeQQ4sd0scM4L6gITWGwLQt0O_8LX8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو، وزیر امور خارجه ایالات متحده آمریکا: ملاهای افراطیِ جمهوری اسلامی ایران و این فرقه‌ی مرگ، کودکانِ بمب‌گذار انتحاری را همچون قهرمانان ملی می‌ستایند و شهادت را به خودیِ خود یک هدف می‌دانند.
🔴
قهرمانان ما ممکن است حاضر باشند برای آرمانشان جان بدهند، اما قهرمانان ما مرگ را نمی‌پرستند.
🔴
دقیقاً به این دلیل که ما برای زندگی ارزش قائلیم، می‌توانیم قهرمانیِ کسانی را درک کنیم که حاضرند جان خود را فدای آن کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151481" target="_blank">📅 19:42 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151479">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V5yuSDdTgnnMNqlOH9KPwfBpOSkIjw6tV_Jwr7SrE-YHXdZUY2rFrJtqKUFYeqiUswZy4nMmeOmbZhN1Ns2WHCK_XhOBOPmZ9kH-wC-sGIOzAIn_cvdgR_Eih6fUUk-Uky4bX4ciu6Ar5r9tvQ5teZ4WNilQyckcPEfO5egweAU-g7LxB7gBRwL2IUCCDMvdgy72AGPJppa1986R6lVYqHgA_QBS0SJouKslZJt7blMsK3dZxRWMSnVWlSnX76XAIebxk1PUCFa9rWOaCUrEmbDNJ7D_aDi7Cc4gOJQDWZZI_2stVrbzKamxEOhFLs5YP9CnQhB-7eW8nozLwgv9og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba0cc8e697.mp4?token=Nw-ES3aXodbDvx-8nti4H1_jDHSQALoc2sqByWoE6qHweVGF-Y4JKYVc7hdEsi-bhW8IQ1yUXtxk_kAmVDvtEdLF2MGnKh9ysPIznOzrSfzA2qhxx43XDWaPzbONAnNtDuwY_y4b92nOOkFEsT_DOA8i58q7b0DEJKloWEyBrlrlIzIdkM4nVCJvzwl9NdRnRWtJF17kEIURqMwyqLOCj2VoiOEnYp7WgCJF25BhDsjb77P1aZAXaAmQMPIwiH2yxSrnxrXWWz9in_3fODRvrRe3Y_lj_DNM9jpUuRM5OkZ7wJMo5HrnPa6TwRTGY7MuB3qruwTJmoYLYZlxtO-Bag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba0cc8e697.mp4?token=Nw-ES3aXodbDvx-8nti4H1_jDHSQALoc2sqByWoE6qHweVGF-Y4JKYVc7hdEsi-bhW8IQ1yUXtxk_kAmVDvtEdLF2MGnKh9ysPIznOzrSfzA2qhxx43XDWaPzbONAnNtDuwY_y4b92nOOkFEsT_DOA8i58q7b0DEJKloWEyBrlrlIzIdkM4nVCJvzwl9NdRnRWtJF17kEIURqMwyqLOCj2VoiOEnYp7WgCJF25BhDsjb77P1aZAXaAmQMPIwiH2yxSrnxrXWWz9in_3fODRvrRe3Y_lj_DNM9jpUuRM5OkZ7wJMo5HrnPa6TwRTGY7MuB3qruwTJmoYLYZlxtO-Bag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پلمب تالار غدیر بخاطر حجاب همسر علی دایی
🔴
دیروز علی دایی و همسرش رفته بودن قم برای همایش یه شرکت خصوصی. امروز دادستان قم به خاطر نداشتن حجاب همسر علی دایی، کل تالار رو پلمب کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151479" target="_blank">📅 19:38 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151478">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔴
مقام ایرانی به رویترز:احتمالاً ایالات متحده حملات خود علیه ایران را بین انتخابات میان‌دوره‌ای آمریکا و انتخابات سراسری اسرائیل که 5 و 12 آبان برگزار می‌شوند، از سر خواهد گرفت.
💹
@shahab_gold_trading</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/151478" target="_blank">📅 19:33 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151477">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bRX3_RGL4IPRr7sfB3_nCsobC1mCHRWwl6zyTNHFj74s_loHrvsjJ79doEY2i-zAO34ZXu1g9UilAB8_cGNIgQSMeAPH74tv_RjE4nyqasjcO0bHxCfOyunsUj58RnLlpzYYowrnTsipHld2YOA6mXBQYuwFLUSd_EpEgpCq6nt3Bd9cw0Chq8iIeYUF-o-esyUc10DoudyCFs87A3pt4Bu5YAz4feHhQlMPUrku1pXUXVfp02a3j2jlX5AfYpbX3lBs4QqgHHP3pZXRSnIkngrnRjMvt-R0LFV9e4yy2CK4jqTtrta2tuYX4gcZr2-7y1jbsXaWnfJIUg-uhv3xNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تصویری از غزه قبل و بعد پیروزی ۷ اکتبر
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151477" target="_blank">📅 19:28 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151476">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
پیت هگستث، وزیر جنگ، به همراه تفنگداران دریایی از گروه سوم هواپیماهای نیروی دریایی، در تمرینات بدنی صبحگاهی در سان دیگو شرکت کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/151476" target="_blank">📅 19:18 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151475">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4x4gtcS1uoLYMXGG4pxh9XNlA4KSYFwe-d0NLA3w5lW5yVb2QTBrFuYnDH0hlYCuj_n6caxfQxrO3VOdkHZ8VT58fQBd6ViXO2Fs7mAnjR4jVYnsyqiQxjBVllavR6pB3aVSXZuI2vPaQzdFg8FsOLaXWEYPKsxhXiuWTgujx73V_SjNP_sUuGtw8mp4xoL7Uj8p32R1fU6g8IbhUeNqRIR2O5VyQFvyHIhcSHFry90ypE9E93pba2c5PWrBDLd19SCLad1Pr350H_evFnyOswssvEVSaxUpyOJpb9PM-TlaCJnqv48Afoqf7zAkxOw4jlPur6e_VRtt1PDwwgfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرگزاری رویترز:  یک ماه پیش، ایران 200 میلیون دلار به حزب الله کمک کرده.این پول خرج مردم آواره میشه، حزب‌الله قصد داره تو مرحله اول به هر خانواده‌ آواره، 3 هزار دلار پرداخت کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151475" target="_blank">📅 19:09 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151474">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EyOZBtoeaTp9AUXki6Tibkt-nX1eVDSvRXjN92VGF-8ni7x57f_RbpevQgxewr0AMEDXjQE9dtoda_V8UBG00BpObHl_Z7_cS-6taodWEc6VgBAFxX-dbjC4NFxj_lH59dzN3uOVRmfmv55fVfP-x1_k4H6giYrtnAUfFqc3T3dHKDTP9ESidSfQoy327rIotuj3lgD3LehKFHJx7dB1g5o4GvLTWqqe08BMDgObdg9QlRNR0zq1zogl9wY43OBy2o4L-u_Kju2PTAxnqjLSYDZ8fnYXrGvRBr942ycwQEDesg8vNkvqs3sPp5VYg4mK9Ir7L4WI5LjLaAprBLPCxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اعدام بخاطر یک استوری
‼️
🔴
نجمه امینی دانشجوی ۲۳ ساله مشهدی به اتهام استوری که در آن به پیامبر توهین شده شعبه ششم دادگاه خراسان رضوی به حکم اعدام محکوم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151474" target="_blank">📅 19:03 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151473">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mi4iDNb21qZ1MxrlrVr9CloAU0qIwKtNc-OdqI5DUb_d1TD6y0fTEAB0_aE06PjvVrZIzLDKgvcYGMT4GYkMyAjf_BnrFPGcVeD8iHeXrw5ToXj5QNDzberB_3nZOIWAv2Ji5zVtTzlFEK56BePxqOOuGr_uvOnQfMJ7geousyi4UbTLHYjUgwcMHf_z-fsISkmH4_YX9W4F5LBAfjyxgNmWtqh7d7Z1ygbivn9VifHf0t9F04Mnd39yI_d-AUuf6ITZzNDMdJoJkcuxOFNNChXWPsV3m314Ahj2jSNrmWO-Nl-6LmLU6bT7rSwLKBalMGireaqCJmUa9xjLO_gdiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عوستاد رائفی پور:
تنگه هرمز برای همه بازه جز خودمون
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151473" target="_blank">📅 18:55 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151472">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4f7cee201.mp4?token=O9xV-TLplKJdeG0IlZ48Da-IpqIp2XxM7s1UvlR3Vyu-c-ZCyxR6wfrGxy8kwsJRc_3D6vTtOF3cRUUdHFi8YcaKjgyHuxG19OPuvQ7ezBBa_zhhWJQZziF22x93p51mCP2ZhXPzmGGQynSVDD9we_K1bqonAW0AoNwcl2WrJi6Q5xkNKqWD3H2_ETZ4z2dfkaMCtWGo7xdZw07XeDLSGTkmK3JjrIm1pHdlVnSpLA9sJQYDEKvgivXkqzDQNL-ziMUzBGtIzkxx_LJu-dFQj1RLMrzCSXgfLegY8FoRV1a77Bd4EPC1ImpmOV_J0MMeGxhBQVlv7IBTW-t6qjZpHpDiXHOSFAxCk6yNn4MK4-33EnXNCgyJ2YEJA8yCHenEY5lgYM-SDQwBOoge3E4yrizS-DuCVQJrXU_PINv8mIOVJLVS8PZHy4kQ9YajkjnGbyC0HrR5-KuSxxCnmjYIqhIB-xDvTt15ze5KkjaG9hElLU07kGGWPW_q7sXorjvJYBf8TSw9xMRwISB1F0VaOscYX_XwWQkezrJiMh46amWW4Svu92yauDBW18w-C3c0BpicuTqE0ifugip8NaF5k595ymrSWBWUDD-QKTe6z_y38tLi_I9Q-TXU6iG4p9r6ZUyxKz7wJ4PROVYAbzjS9_Xt0eq7baMi9IzQsnEPgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4f7cee201.mp4?token=O9xV-TLplKJdeG0IlZ48Da-IpqIp2XxM7s1UvlR3Vyu-c-ZCyxR6wfrGxy8kwsJRc_3D6vTtOF3cRUUdHFi8YcaKjgyHuxG19OPuvQ7ezBBa_zhhWJQZziF22x93p51mCP2ZhXPzmGGQynSVDD9we_K1bqonAW0AoNwcl2WrJi6Q5xkNKqWD3H2_ETZ4z2dfkaMCtWGo7xdZw07XeDLSGTkmK3JjrIm1pHdlVnSpLA9sJQYDEKvgivXkqzDQNL-ziMUzBGtIzkxx_LJu-dFQj1RLMrzCSXgfLegY8FoRV1a77Bd4EPC1ImpmOV_J0MMeGxhBQVlv7IBTW-t6qjZpHpDiXHOSFAxCk6yNn4MK4-33EnXNCgyJ2YEJA8yCHenEY5lgYM-SDQwBOoge3E4yrizS-DuCVQJrXU_PINv8mIOVJLVS8PZHy4kQ9YajkjnGbyC0HrR5-KuSxxCnmjYIqhIB-xDvTt15ze5KkjaG9hElLU07kGGWPW_q7sXorjvJYBf8TSw9xMRwISB1F0VaOscYX_XwWQkezrJiMh46amWW4Svu92yauDBW18w-C3c0BpicuTqE0ifugip8NaF5k595ymrSWBWUDD-QKTe6z_y38tLi_I9Q-TXU6iG4p9r6ZUyxKz7wJ4PROVYAbzjS9_Xt0eq7baMi9IzQsnEPgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فرانسیس فوکویاما: جمهوری‌ خواهان در انتخابات پیش‌رو شکست می‌خورند
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/151472" target="_blank">📅 18:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151471">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
حسام الدین آشنا: کاش می‌شد حالا که آقایان رسایی و تاج زاده هر دو گرفتارند؛ مدتی با یکدیگر هم سخن شوند.
🔴
حتی شاید پس از چندی اشتراکات میان خود را در موضوعات مختلف بیابند
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151471" target="_blank">📅 18:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151470">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
معاون وزیر بهداشت: هنوز ابتلا به طاعون قطعی نشده و تاکنون نشانه‌ای از انتقال پایدار انسان‌به‌انسان یا خطر شیوع منطقه‌ای و پاندمی گزارش نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151470" target="_blank">📅 18:37 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151469">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نتانیاهو:
مطمئن باشید جمهوری اسلامی سرنگون میشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/151469" target="_blank">📅 18:31 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151468">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
نتانیاهو: ما مأموریت را تکمیل خواهیم کرد و همه کسانی را که در حملات ۷ اکتبر شرکت داشتند، پاسخگو خواهیم کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151468" target="_blank">📅 18:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151467">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
امارات استفاده کشتی‌های ایرانی از بنادر خود را ممنوع کرد
🔴
اداره دریانوردی وزارت انرژی و زیرساخت امارات اعلام کرد: ۴۷۲ شناور حق استفاده از خدمات بندری امارات را ندارند
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151467" target="_blank">📅 18:23 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151466">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
بلومبرگ: سوریه قرار است به یک مسیر جدید برای صادرات نفت خام عراق تبدیل شود، که این امر امکان ارسال محموله‌ها را بدون عبور از تنگه هرمز فراهم می‌کند
🔴
عراق از سوریه درخواست کرده است تا در زمینه صادرات نفت خام با انتقال آن از طریق جاده به یک بندر در دریای مدیترانه، کمک کند.
🔴
این اقدام، یک مسیر موجود را گسترش می‌دهد که قبلاً برای ارسال سوخت عراق استفاده می‌شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151466" target="_blank">📅 18:17 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151465">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sqPy8oxGIEvgNrXGAGeIbSNNVGXVLjsVxFlxIFLjNoTxfwmh1acZkv8Jcm-HMn3bM5YoLeq0yu9FDGWXstvmq0R0yNMs2qCjVLPWGJUreJk-dkPGETAR9BNLYje_YFI7HUaDjfopnK85KJzKViXE37foYBcQU6L-LmnMGBmIwADxsZHjoCIjWnXx9UB1K5dleJ-NoS93PyOCA_I2pI2CeY1ZVMBjE6NULYAk-F_ezFEmR0EEpagRCheUpptXsnmRGN5Acr92_C32ougJtNl6I65vnDEUos4Y43qp8PcUyJ1RoGFP-1N38j_GVS4emE0O-Ulu_nSXLaH2GBy0Hnz0UA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نادر قاضی پور: رسایی تو زندان هم موبایل داره هم تو یه بند مخصوصه، یجورایی هتل
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/151465" target="_blank">📅 18:16 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151464">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DZ4NPEhi8SBQfz87IuRqKO0RRsY8QtBaGX1PPkj0HizSq4sc_dXnHaqmubtVZamRvaOG30q_Zy9L4vrizV6cGoUn3W8U-e1F5EvKcGVcOLlCgtkzBiMs0tlrZVWh4E3ay1HyHXbrjUGN-WVaL1DIREaT2br0lDSsjIwpI7E22kPJ5m3be1AZlf0DZRqABJ36WvJd90HwP-c8YYzcOQcO53BTn_9X4eAZLGFR5Pd-wsMMvxMn2azHOPW_Fh2lV0sRBK6dDnmIoYw2A9BXhzpcF3PDUiSkUgnFzNPk4CGDIpedexDsWDzPiueVVyHxivBIF_QeHDGuBlm0tVQ4FcL0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شعارهای سیاسی ملت معکوس شده در حرم امام رضا، صدای مذهبی‌ها رو درآورده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151464" target="_blank">📅 18:07 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151463">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نگرانی ام آی سیکس (MI6) از افشای اطلاعات پس از دستگیری رئیس جاسوسان آلمان
🔴
سازمان‌های بریتانیایی در حال ارزیابی هستند که آیا پس از دستگیری آگوست هانینگ، رئیس سابق جاسوسان آلمان، به اتهام جاسوسی و خیانت، مواد محرمانه یا منابع انسانی افشا شده‌اند یا خیر.
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/151463" target="_blank">📅 18:01 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151462">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3922c39860.mp4?token=B9AvNw5GTkCOnlqL96xqGHG2JFr-nJnKlpz04b0SUkzfs0lJHFqFEWsr_FiT35Q7a8PP_ZUbK4FRMBdz6leGWJ_6FFw5uQXSUCCkv2OkN7ZJavsprklByQsBtCLQ5bvx7ByVL7k_3ebLWtu8ZmmE75sH5MIpjWsz82Z_fJDRdHFzEvOXb63j6cmnR3KNaHpItpeAR75zviaaH0iXktVLW_u4lTb-7QlbtF8oQ2yBvEH_DZVkofUMAWgynRy2lBc-Vy1kjZe6IiEPXzoJLHvhXPp1COXA4Xb2W2ErjnLETB_jYjcRZEAtMTB0xYlN7cSfhv7e45ZIJ7GhkuANznMnWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3922c39860.mp4?token=B9AvNw5GTkCOnlqL96xqGHG2JFr-nJnKlpz04b0SUkzfs0lJHFqFEWsr_FiT35Q7a8PP_ZUbK4FRMBdz6leGWJ_6FFw5uQXSUCCkv2OkN7ZJavsprklByQsBtCLQ5bvx7ByVL7k_3ebLWtu8ZmmE75sH5MIpjWsz82Z_fJDRdHFzEvOXb63j6cmnR3KNaHpItpeAR75zviaaH0iXktVLW_u4lTb-7QlbtF8oQ2yBvEH_DZVkofUMAWgynRy2lBc-Vy1kjZe6IiEPXzoJLHvhXPp1COXA4Xb2W2ErjnLETB_jYjcRZEAtMTB0xYlN7cSfhv7e45ZIJ7GhkuANznMnWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
دریاچه ارومیه پس از نخستین باران پاییزی
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/151462" target="_blank">📅 17:53 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151461">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Nf8OLd3S8CUHQLhS4tAwfcoOjvKaqxVf0rjt0dWqyf0JuxjwewGdm75z1kGzxuqarkCkP75-vxJgi0PxSEkj4D1MOkxm8_rqFUjwdn5_BUjMDlN5N_GeWeaxXRE5VJO4OceJ5A3MOh0d76BTcdAA9xXjOKrJjkP4wYXYKsNp4dTXXcZlxfU4lmwc1XqF4x5ZrW5acQh3_b-Dhn1_HcDZ3SjU1C5eQeuJ0UAvT-7BIRNBl2KXyl-I-INapGnbrTg7eNmGij94Q6Zp9_7Y5mgPxw9EEQrwIMuarKp_jxODdHX1sEgUPsQEBud145hbdjTBPOYYgu0tnqG51riNmR-Ywg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=Nf8OLd3S8CUHQLhS4tAwfcoOjvKaqxVf0rjt0dWqyf0JuxjwewGdm75z1kGzxuqarkCkP75-vxJgi0PxSEkj4D1MOkxm8_rqFUjwdn5_BUjMDlN5N_GeWeaxXRE5VJO4OceJ5A3MOh0d76BTcdAA9xXjOKrJjkP4wYXYKsNp4dTXXcZlxfU4lmwc1XqF4x5ZrW5acQh3_b-Dhn1_HcDZ3SjU1C5eQeuJ0UAvT-7BIRNBl2KXyl-I-INapGnbrTg7eNmGij94Q6Zp9_7Y5mgPxw9EEQrwIMuarKp_jxODdHX1sEgUPsQEBud145hbdjTBPOYYgu0tnqG51riNmR-Ywg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یکی از حامیان حکومت میگه چون این مدت جلوی مجلس توی تجمعات حضور داشتم(شعار علیه قالیباف)، اطلاعات سپاه بهم زنگ زده و احضارم کرده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151461" target="_blank">📅 17:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151460">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
عارف: امسال حداقل ۱۰۰ تا ۲۵۰ میلیون مترمکعب کمبود گاز داریم، دشمن ۲۵۰ میلیون متر مکعب از گاز عسلویه را از مدار خارج کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/151460" target="_blank">📅 17:40 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151458">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iu42EWVOooM577T-kgtpcsI0HtqX0rCaQvsHcbYmsPm0euufH4ZxUi99Fk89ZwibZYCj1NLGRV6q88wo4wDxKdfZVWfdx4AJV00t7yKexMcHb8bxAgzoTmMTIOfZhni2qDSZq0ZdqBBquqNQxE5M9x6Eouy_My5FLpzs3nrrsXQvPRSZNGFDFewIAX4uKWOXbXZSEbJAxqF4HXSSH2nUZe6_9MQhCb65zpjhP8YIM3QLkGZMx6svps5SgmRHORIsRFVoBj18p0z-tUAdmhD7Og9tEEDO26zx15am4y-srXDk0Tz4eK_2CUjp2iU6Z79pPRgJjinsV_Mh4yz1I1ZxmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی از مجلس بیرون انداخته شد
🔴
رسایی طبق قانون، با ۱۰۰ ساعت غیبت از مجلس، مستعفی شناخته می‌شود
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/151458" target="_blank">📅 17:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151457">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AmT8b0Q2Dx3uAVBLpS9Vwd6bLcrAzGHZn0PYbMIg80a4mtlbqLnTBkIT589n1YQcOI975qvO5tHA7GzMKOZLI0mg3vsgl2ZGdB0GX1nU0mOMlVS7auDcVbGgZ7HrG1fXwLyenTMpF-N7ZFoW4kKx8lAm2vwhMn2ST6DJBOZ0dsnaj9zNx-gi5GEak375OuhCzKZLPeUvHJ2euRpfHsNPcuflaCXw3KeKVcgRzTpB8rsMvEVaj49MwgzyisWFCV0dS8ZCAxNqQ9-wWjP1TQSxKK5I3yw7Awx_RXQ9A3q0ErjbUr8G5Q8aUiw1l8fw2sY-yMILJShiQn9OdRgoKw8mGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عکس یادگاری فرماندهان فراجا با باقرخان
🔴
شبیه تابلوی شام آخر
🤣
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/151457" target="_blank">📅 17:15 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151456">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
واکنش لارنس نورمن، خبرنگار ارشد وال‌استریت ژورنال به سخنان ونس در مورد کاهش ظرفیت غنی‌سازی ایران:
🔴
مشخص نیست این موضوع تحت چه شرایطی خواهد بود، اما چیزی که مشخص است این است که غنی‌سازی صفر در کار نخواهد بود
🔴
لارنس نورمن، خبرنگار ارشد وال‌استریت ژورنال در واکنش به سخنان جی‌دی‌ ونس در مورد کاهش ظرفیت غنی‌سازی ایران نوشت: یک تغییر موضع قابل‌توجه دیگر در اینجا دیده می‌شود. ظرفیت غنی‌سازی ایران در حال حاضر صفر یا نزدیک به صفر است. اما ونس می‌گوید ایران می‌تواند در ظرفیت غنی‌سازی خود کاهش ایجاد کند. این به معنای بازسازی نوعی ظرفیت غنی‌سازی برای تولید اورانیوم با غنای پایین (LEU) خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/151456" target="_blank">📅 17:13 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151455">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCdH-ZRjXHcwyzR12iZiDtX-I-3opigLlCtiRps9lzc1idMRvqOPJ5Om_yMe7zXnhvRRZzfIcwt_WAOlUogR2_JI-8h7xMBPBsT07Dx2S2Y_WHYwQNfpjHNR7nzFeSsBgZX6HEGUpWWZEHvVUH8kvMgVpgyxm8vw2JsJLvTm5bAahaNf0ty-IAtWmvAMaWJXWQTThMpWQDPDmejYmkLMbi25tNC4I5pv5mE0EBmwCmZNwU0anTXr9evLNi61tpwFf3gNTGJc0eyEErKd71MZuLX6Db5FnnUnyP8XNVeF-RbcPn5jh_EuUNi1UypsiyOtPSnCbU60im-rBTZ5kzZPOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
👈
برادر
بیلی آیلیش، خواننده آمریکایی: نگرانم ترامپ کالیفرنیا را بمباران کند و طوری وانمود کند که کار ایران بوده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151455" target="_blank">📅 17:08 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151454">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">✔️
عملکرد حساب کپی ترید وسود ۲۰۰۰ دلاری معادل ۵۲۰ میلیون در ۳ روز گذشته
👆
👆
👆</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/151454" target="_blank">📅 17:05 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151453">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e4842f342.mp4?token=ColcOlVEpH5dmkAwtkK06GUu5c_vOnJJF_dt3eKzIoC8n9LVpJnAh3hKVKyJsgmPI268jQFz6dstOq2NXeWzl77cB-MOUp98J6ndFwvGJtv0KevC_sdmZVICSvWGv6n0NrwLKw4J-6JWxtFjhuDbs4f2HD6yXIMphfwXroxx_bqcpTPSm_ND63Fkp8YrJdFf2JsG_en6Hxsyre-yCsmXmRGdbdm718ew0WMBGvdAYaHSvYD5wnGBO6YGfyH_0PeQUqnt5v-Z2W2wCZ-F4BfREqDWqj-P3TkBbXwluso-XAzByR5vb06EF8wXPbTNIMuhsA6o5Mc9cadUekFx6_sFgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e4842f342.mp4?token=ColcOlVEpH5dmkAwtkK06GUu5c_vOnJJF_dt3eKzIoC8n9LVpJnAh3hKVKyJsgmPI268jQFz6dstOq2NXeWzl77cB-MOUp98J6ndFwvGJtv0KevC_sdmZVICSvWGv6n0NrwLKw4J-6JWxtFjhuDbs4f2HD6yXIMphfwXroxx_bqcpTPSm_ND63Fkp8YrJdFf2JsG_en6Hxsyre-yCsmXmRGdbdm718ew0WMBGvdAYaHSvYD5wnGBO6YGfyH_0PeQUqnt5v-Z2W2wCZ-F4BfREqDWqj-P3TkBbXwluso-XAzByR5vb06EF8wXPbTNIMuhsA6o5Mc9cadUekFx6_sFgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مارکو روبیو میگه تنگه هرمز بازه و صادرات نفت از اون به اندازه قبل از شروع درگیری‌هاست. به گفته او ایران دیگه کنترل کامل تنگه رو نداره.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151453" target="_blank">📅 16:45 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151452">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTUrxUBXFO7DDkpDE2jdm0UAb2_fa-ZDxD5QOkSktVo6kbXaAKCO52Odyd6AtPY-dBJqVkf3ed_6pmAmJ9kj2OnZZoSZnie49As9eCwnSS8xtx-WIVPlfdeWb9_ZfqXQr7obZVuipJ9KQZ1dEjMR4IYm1thJOv1HcKSwr79aJR5tDWwB7z54w9t2Qcjz55yuz91G1wNW78Po-6WKAPPn2F5nWx_lGMyfiW9v8N1d4LwPDTsNLAx8Zo1OWz9tdnSorvaS69amHaBr394RdZh5Tu1pbNOsUOBwa6G6sCY2vedUayS4zJTI3jZe6hwBiohVx8M2rUkK1W74pPavxgr9Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه خبر حال خوب کن
🔴
نارین خانم دختر ۱۵ ساله سنندجی که تا سر حد مرگ توسط پدر و نامادریش شکنجه میشد زیر نظر پزشک تحت درمان قرار گرفت و بالاخره حال روحی و جسمیش بهبود یافته.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/151452" target="_blank">📅 16:29 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151451">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">‏
👈
معاون نظام وظیفه: اگه لازم باشه برا جذب سربازای ۶۰ ساله هم فراخوان میدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/151451" target="_blank">📅 16:21 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151450">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eeToJwWpoekqc1qe_McdtMcAqvms8wFZMBqjWJOr5Ta9pYggTU_EpjgjeoPTwVI6sbWwvYkCsy0z-qjOnwnGjeaPuCBLbyBIySovJqsWj0I0VDJSs3MJ4YeGL7kl_98Y88Yit0a-CNvrv-xEcyb9KyhBQalaKuhtR5P2EXq3oBZSF9nwu9c4IyVpOOJtOLTdqt4cz5C5uUdHTxP2IsgKWqKyo-ww2Eeugq6ZrPuHBzteNMzHu2bFZkZZQRQueCOIbgk6lxskxMUVYKjOpaYweuHrpalvYB0P8C-czKPyQTFd362s1u_Adr-FIy2BZ4nQD9kIRsyWl5g4eCqHVsXO0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قوه قضائیه: رسایی اصلا بخشیده نمیشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151450" target="_blank">📅 16:04 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151449">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">⚠️
هشدار جدی در مورد صرافی‌های داخلی</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151449" target="_blank">📅 15:58 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151448">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
افزایش اعتبار کالابرگ به روزهای آینده موکول شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/151448" target="_blank">📅 15:47 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151447">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
پزشکیان در تماس تلفنی با ولادیمیر پوتین، رئیس‌جمهور روسیه ضمن تبریک زادروز وی، برای دولت و ملت این کشور سربلندی، رشد و شکوفایی آرزو کرد؛ دو طرف همچنین بر تداوم و تقویت همکاری‌های دوجانبه و راهبردی تهران و مسکو تأکید کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.4K · <a href="https://t.me/alonews/151447" target="_blank">📅 15:26 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151446">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bb0297a66.mp4?token=bTga3EUhViExzWk6y8n_wW0y9GpxFEkDS9TCs1WBf5yyj6DREWs1DSraQtZRVVm34DgI7eG4guq4rOSSuSwTNg0hQVhGw1hFxvZqbsPpKq6EpB3fP2JOC4ArmD8dj7Ws3E0U4OvPs_sCfrS6c6ZLtgVAqrF-0_mHFerb6SJLM7vE1mzTrztck3GzB0hiWx6SKzQUNAZD1Hm8lH8C5Jkn4Yc-wQoMgf2_BwHivb132tg5iCppCBPjzEWcHglBLp7f2pCtkWPnp0nHJ5W0_Cqb3k1Jvs4-U6YLGlDp_FuLQ6xNQwV6azPxpc7xHkGwONgdab6Ldl_qDWD-As2_WJ_75g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bb0297a66.mp4?token=bTga3EUhViExzWk6y8n_wW0y9GpxFEkDS9TCs1WBf5yyj6DREWs1DSraQtZRVVm34DgI7eG4guq4rOSSuSwTNg0hQVhGw1hFxvZqbsPpKq6EpB3fP2JOC4ArmD8dj7Ws3E0U4OvPs_sCfrS6c6ZLtgVAqrF-0_mHFerb6SJLM7vE1mzTrztck3GzB0hiWx6SKzQUNAZD1Hm8lH8C5Jkn4Yc-wQoMgf2_BwHivb132tg5iCppCBPjzEWcHglBLp7f2pCtkWPnp0nHJ5W0_Cqb3k1Jvs4-U6YLGlDp_FuLQ6xNQwV6azPxpc7xHkGwONgdab6Ldl_qDWD-As2_WJ_75g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تاسیسات آرامکو عربستان بعد از چندین روز همچنان درحال سوختنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/151446" target="_blank">📅 15:22 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151445">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
مقام ارشد ایرانی به رویترز:‌ دیدگاه‌های ایالات متحده درباره برنامه هسته‌ای ایران با خواسته‌های ایران در تضاد است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/151445" target="_blank">📅 15:14 · 15 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-151444">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjRg4Fe9EwPluOhIAytxzi9QAr6d84VG6kc7KnKHMpSCaInivCXczJZ4ASjGaOl-EFEQEEftB7mFshibSHNaoiqFRTWNERUBuS44PrR4Cej4vDOYfzL6aWTxWvtNkDfsAkSgf0YK4aqwgbcYxztUwHm-g7wW623lpcK0qfcqM0Hniw4Av_V2j6tPIdmDwILt48iMzGO5kQiJQPEzExwz2rpBGdbOfT0byRWVsMECG07prvef3WUCqbXfQIxSkk3FBFLSnSgWtY-yv0tZSX9YpbtsLfaGeYhn8cmL48reKnXujI4Lx3vtsJPQ8CqdvFo2ZEUTXjp5ua36Zzv9ummMPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پارک‌ جنگلی چیتگر که درسال ۱۳۴۷ احداث شده بود در دوره شهرداری زاکانی به طور کامل نابود شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.3K · <a href="https://t.me/alonews/151444" target="_blank">📅 15:09 · 15 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
