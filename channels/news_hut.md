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
<img src="https://cdn4.telesco.pe/file/IrqY-hBrIozaRRJ_awMicG7B3J-DiSl20Kq-jgaV_nQGen9fYzsdQsiLiA3uMF2cruf_RjZWeY82fgpYbSfmc5_oNiVWmlPLXjc3dLU35ZTPy1MD78LygHDPf-eMcPK17Ap8ZYq3xyJ414dkTE16DQd-S7oQofuh9idjssbdCwkFLGcsQu1JF0eD9EyVinwW6urUcckXnZnIYqsxnlM82UmaIrFnV0pX-0N67zBw6D5DXFGGP8NVfBVTBJ0n4UZhf6dfOGO7uSgH9Drrj3k5Mqi4ZnKsb1TCl4gjsfYgzEckYS9CJgVoQunBCKjAwreFOJoCzeAgIgrRWIuE0zxG1Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 117K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-04 19:40:24</div>
<hr>

<div class="tg-post" id="msg-70631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ℹ️
صحبتای امیرمحمدزند بازیگر صداوسیما:
حرفم با مسئولین اون وره چون این ور اگه حرف بزنیم احضار میکنن و تعهد میگیرن اخرشم‌ممنوع الکار میشی
قبلا حدقل زنگ میزدن میگفتن ممنوع الکار شدی ولی الان زنگ هم نمیزنن خودت باید بفهمی جلوی نون تورو گرفتن
ما ایرانیا با دلار ۲۰۰ تومنی و طلای بیست چند میلیونی و مرغ و گوشت و .... خیلی مردم شاکری بودیم
هرچقدر هم اقتصاد بد باشه گرونی باشه جنگ باشه میگن باز شکر کن سالمی حدقل
بعد که مریض میشی میری بیمارستان با هزینه هنگفت میگن شکر کن حداقل زنده ای
طرف میمیره بهش میگیم خدارو شکر بابا مرد و راحت شد
ما ملت ایران انقدر شاکریم خدایا یه امتیاز ویژه برامون قائل شو
@News_Hut</div>
<div class="tg-footer">👁️ 1.48K · <a href="https://t.me/news_hut/70631" target="_blank">📅 19:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
مهاجرانی سخنگوی دولت: در میدان ولی‌عصر یک خانمی به من گفت الهی بمیری!
رسایی سرباز نظام نیست؛ ظریف سرباز نظام است
رسایی منافع ملی کشور را نمی‌فهمد!
جریان پایداری خلاف منافع ملی حرکت می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/news_hut/70630" target="_blank">📅 19:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=l7CSWDDg1rB3gQiT706Cvv1EQqr7NkTHVxg3PJ-faHzDo7-KntlhQDmFJsc5U5emLfTh83_VzeHPQA4pchc0FAJTAPThY8mVTSEQ_u_yTIwWVMMw71MEewTtaaSz19NmUNsdZRhLiZs1Uzo0o0eW6lkGiHwrbYSNttUoYSXID43llqB4UMX7TEcQwzu-wLDuyIujKF6OX9j3nWWBrBwOWvd4vLeIMdzZysLn7YPNrb310t20_Q8UeO5PKlUWYywveOWT9FzEosylzhXmGEsT6SKBRJrMbCLrlwueacMSij4onJ5uAdKeicHjf2TE-ORcMD2fSUwG_orf7Jw4DbzE8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90d9d9f6e5.mp4?token=l7CSWDDg1rB3gQiT706Cvv1EQqr7NkTHVxg3PJ-faHzDo7-KntlhQDmFJsc5U5emLfTh83_VzeHPQA4pchc0FAJTAPThY8mVTSEQ_u_yTIwWVMMw71MEewTtaaSz19NmUNsdZRhLiZs1Uzo0o0eW6lkGiHwrbYSNttUoYSXID43llqB4UMX7TEcQwzu-wLDuyIujKF6OX9j3nWWBrBwOWvd4vLeIMdzZysLn7YPNrb310t20_Q8UeO5PKlUWYywveOWT9FzEosylzhXmGEsT6SKBRJrMbCLrlwueacMSij4onJ5uAdKeicHjf2TE-ORcMD2fSUwG_orf7Jw4DbzE8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبتای این دختر در مورد اینکه تو این جامعه، سخت‌ترین کار پسر بودنه، به سرعت در حال وایرال شدنه.
@News_Hut</div>
<div class="tg-footer">👁️ 3.89K · <a href="https://t.me/news_hut/70629" target="_blank">📅 19:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/news_hut/70628" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kQjqoqkym4Pym46wq5zfKV9sJmEDhya-4nm9VWsj3aw7rXyBQGY-1SrOpnmFRfcSun9NA7q69l6SxlWhEyoWsni8pnyrKb3uGRzsmbmy7fYCcG91bWnJwG9x52Wze__wNNkPPHD-E22Whv9XqgMrC8mF7_pMmp79tEgsnHgePh5J5ZrKcZrh-eaqzn9XTCSIEooH47_ET1aRAaIkGBJ_OKJ3Dw_n8Ys2c5zSkUxGv8wcc6zag0ygxhpAEtKNrfZZCys-VBB611XU94QLr_QMm7S9Eznh2dFhCBdSWND_6TJRmTGJGQAEKCGOIIgWv6sBt2de5WdWkvvSdevk-hfsgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=EucFOnxGJj-64n9HmbADd3B8ey78Adq5IVoIq63fSv5lMu-Rb2Jaeu36VrEzbX19RTUHQQ_F39pDgj19V2qqSJA8psa0AvTZ1hCqT7tv4r7Dl29xDhF7ah9_XTLbHFHtD9ZKFZmwHnCGPGRE2S-m-27cGdxbTaQaLnV1ZReKhpYnAs5ptQkXzF_FuIQsb5IGtnHqk4KXlgXQMolFWUYoCl099t7BMoC1NJ4mgvkVGGS6052EXHrtC3h-8-90SeYUVmuLbaaUVMQu-e9SK9OoBJGFCy_6AGLQJRlVPBV4YDt39FyL6dguNXq_t2dXgWRCv838cPElrwSJ6NHIJi2e6kQjqoqkym4Pym46wq5zfKV9sJmEDhya-4nm9VWsj3aw7rXyBQGY-1SrOpnmFRfcSun9NA7q69l6SxlWhEyoWsni8pnyrKb3uGRzsmbmy7fYCcG91bWnJwG9x52Wze__wNNkPPHD-E22Whv9XqgMrC8mF7_pMmp79tEgsnHgePh5J5ZrKcZrh-eaqzn9XTCSIEooH47_ET1aRAaIkGBJ_OKJ3Dw_n8Ys2c5zSkUxGv8wcc6zag0ygxhpAEtKNrfZZCys-VBB611XU94QLr_QMm7S9Eznh2dFhCBdSWND_6TJRmTGJGQAEKCGOIIgWv6sBt2de5WdWkvvSdevk-hfsgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g4
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/news_hut/70627" target="_blank">📅 18:59 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70622">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIubK21h41b2v76wqcm6oeA6Y5KC4UQ94iaCfTsQAZ8MtpHS0LfmbNDRu7U0OS0-AX-vML4eEzujqWz2G5gPKccGCfnxJ4GhyOlSEU9XmzCfXpk441Hk-fLokIZVWm2C1YJRGnuzJlX5GSwtcJq7879EkLg4bUKeCLGy_vx1VeqIcaquFOZXcgjopaBG9LsymHJ8ciwSEjc-hwXCDGvQsDrVziuArayLiVRXNFdGAI00Njm50taaXcM5MPFe7MOYt-knYEVZgIdEwxwDQ1NLD4wBm-XpN7qI6J0b7HCOEbSdQtuTBDpJPp_Cyhr1wHGfBWgT8_LNcM0-s6IDrVQnRHND8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1a8b5c63c.mp4?token=GrSjJj0E1gDB9YDJKAD8Mo7xEQsOnQkbIrjKGe16E2BX1xSQzb69-31asohfg0jfpsb4h83ILbyWD4gnBy51TAjIggbYvBdgINyGAjYlyUIYY1hjrwYfJx6Jpu6b8rqdoopy3Xincm0jUoCeYAe4VElXBTjkHz6TVqefLKuOfQ10Aeki2-no4WfU3btMVwDn-YPqkL5UvFQ7tOgqzfXN-fSdxxKhuULfd3X8eylELdcc0hy0wNTEMvWC7F-d0Rhq6EdA4tHq_2QNkE8BwnYA6snRDJfwyvWjlT5lArVrEMvx2ykJFnBIF5dIsVi_ciVsY5n8WrQgpdF2ppQ-sAUIubK21h41b2v76wqcm6oeA6Y5KC4UQ94iaCfTsQAZ8MtpHS0LfmbNDRu7U0OS0-AX-vML4eEzujqWz2G5gPKccGCfnxJ4GhyOlSEU9XmzCfXpk441Hk-fLokIZVWm2C1YJRGnuzJlX5GSwtcJq7879EkLg4bUKeCLGy_vx1VeqIcaquFOZXcgjopaBG9LsymHJ8ciwSEjc-hwXCDGvQsDrVziuArayLiVRXNFdGAI00Njm50taaXcM5MPFe7MOYt-knYEVZgIdEwxwDQ1NLD4wBm-XpN7qI6J0b7HCOEbSdQtuTBDpJPp_Cyhr1wHGfBWgT8_LNcM0-s6IDrVQnRHND8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇵
🇨🇳
وقوع یک سیل ناگهانی و شدید در منطقه مرزی میان نپال و منطقه تبتِ چین، خسارات سنگینی به بار آورد.
گزارش‌ها حاکی از آن است که در پی این فاجعه، تاکنون صدها نفر از غیرنظامیان و نیروهای نظامی و پلیس مفقود شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 6.04K · <a href="https://t.me/news_hut/70622" target="_blank">📅 18:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70621">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🇺🇸
ترامپ:
فکر می‌کنم ۳۰۰ [درصد] باشد. شنیده بودم ۹۰ درصد؛ اما به نظرم تورم ۳۰۰ درصد است.
@News_Hut</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/news_hut/70621" target="_blank">📅 17:16 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70620">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=TCEbeqvXVU0cj8tUdhx-CSVIwK42zs4w6SolS9hB-JmBSg788r-AKGLnw8Hz4WWRRuxc_LrEQFE1SOPQ1tI1hIZVR3BxIc3O7NrYXbatmuEU5pi1RdyzfRh44GT6cDx_BvRpFm_SaNRtRm0rRpSAvIecb12O1o25YAmv4uDHi2yiKYcW09vht0hZ9R5pesfyA9PbTAdJnSQeIQzm2dEUD3LuW_OTMyMRTisZaqDCg0g7_9DoOs-cWMaJuRnrSWgHFqyygBrV2Jd-yESCzvoTarsRW9LWF4wFNWllyyEVh71xYrR8dA6O6A00s-eaorT50w6rkDFwgG8kYJOHUlj3Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07afc966eb.mp4?token=TCEbeqvXVU0cj8tUdhx-CSVIwK42zs4w6SolS9hB-JmBSg788r-AKGLnw8Hz4WWRRuxc_LrEQFE1SOPQ1tI1hIZVR3BxIc3O7NrYXbatmuEU5pi1RdyzfRh44GT6cDx_BvRpFm_SaNRtRm0rRpSAvIecb12O1o25YAmv4uDHi2yiKYcW09vht0hZ9R5pesfyA9PbTAdJnSQeIQzm2dEUD3LuW_OTMyMRTisZaqDCg0g7_9DoOs-cWMaJuRnrSWgHFqyygBrV2Jd-yESCzvoTarsRW9LWF4wFNWllyyEVh71xYrR8dA6O6A00s-eaorT50w6rkDFwgG8kYJOHUlj3Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
وقتی کسانی هستند که حاضرند شما را بکشند، اعتراض کردن در ایران بسیار دشوار است؛ به همین دلیل است که آن‌ها اعتراض نمی‌کنند.
و البته احتمالی هم وجود دارد، چرا که آن‌ها بسیار تضعیف شده‌اند... به بسیاری از سربازانشان حقوق پرداخت نمی‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/news_hut/70620" target="_blank">📅 17:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70619">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=es5FcT7xeCfRxAy3W9cfYYOUtSTO3MmqSWSs3C6x0rSToSJUJOr25eAnjRYEhQrlJK4pskxvZNTqP4M3bX436Hxd2gpwvIFO18di8QK_SJmCX8La3y2UiT-7pb1GcdBwONskq5nFJJnxblffe-5xfKNWI7RPmBvOfqZtEyIrjfHeQE7m0CmmURTX0jZdB2fUbjXD87PKuc8XrSEOmeA3aJje8AHrG-I33IUBjufkCLro2uUqJe1v_E056jCx8CfKOrgIUGqC4RQaTXmY_pszq4hnW_xeHwt3o6t-ZvveZ2KaJFC5SaxV_CEWDDDh0EO0aYWW2qcRqoUWlGEnlomb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7effdb513d.mp4?token=es5FcT7xeCfRxAy3W9cfYYOUtSTO3MmqSWSs3C6x0rSToSJUJOr25eAnjRYEhQrlJK4pskxvZNTqP4M3bX436Hxd2gpwvIFO18di8QK_SJmCX8La3y2UiT-7pb1GcdBwONskq5nFJJnxblffe-5xfKNWI7RPmBvOfqZtEyIrjfHeQE7m0CmmURTX0jZdB2fUbjXD87PKuc8XrSEOmeA3aJje8AHrG-I33IUBjufkCLro2uUqJe1v_E056jCx8CfKOrgIUGqC4RQaTXmY_pszq4hnW_xeHwt3o6t-ZvveZ2KaJFC5SaxV_CEWDDDh0EO0aYWW2qcRqoUWlGEnlomb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
ما از شر مین‌ها خلاص شدیم. اما تنگه هرمز... تنگه فعال است؛ یک تنگه فعال.
بله، هر از گاهی پهپاد یا راکتی یا چیزی شلیک می‌شود، اما این تنگه کاملاً فعال است.
مقدار زیادی نفت از آنجا جریان دارد.
دیروز ۱۰ میلیون بشکه.
@News_Hut</div>
<div class="tg-footer">👁️ 8.86K · <a href="https://t.me/news_hut/70619" target="_blank">📅 17:09 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70618">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OOkqqFF7XcCW-tjlfLFIePeIt_rtKyBDzF1LA-5cWtHlBInJvMMzmP0igblsKaW4-AQ4Mi1RPqKizPbkYMU11f-lIi4bGvj2p-n0-OZgi_wvL8nFBuUwVklV-AVzQVgNyCVTbbAZvw-tuJdjJ3zjV74pxLhfuGEDiv5ySrSy1FBIhBEZFMhw4oy48JZES-VgaDEs7DTP7dvClJP3nOd8_ox2zVyC_2TN7fbI1znRMOfdZVw4IFiCIxErEIaBuauh2vX4DGog9T-zmyuapShtelHIeK8D1AoFsWdkNGvZyezFh7hvlVfCvxRM32MJC7gRg6gOAU_3T91FdYtnHVp7SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/62ce2d5dc6.mp4?token=OOkqqFF7XcCW-tjlfLFIePeIt_rtKyBDzF1LA-5cWtHlBInJvMMzmP0igblsKaW4-AQ4Mi1RPqKizPbkYMU11f-lIi4bGvj2p-n0-OZgi_wvL8nFBuUwVklV-AVzQVgNyCVTbbAZvw-tuJdjJ3zjV74pxLhfuGEDiv5ySrSy1FBIhBEZFMhw4oy48JZES-VgaDEs7DTP7dvClJP3nOd8_ox2zVyC_2TN7fbI1znRMOfdZVw4IFiCIxErEIaBuauh2vX4DGog9T-zmyuapShtelHIeK8D1AoFsWdkNGvZyezFh7hvlVfCvxRM32MJC7gRg6gOAU_3T91FdYtnHVp7SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره ایران:
«باید بگویم که آن‌ها اصلاً گروه شرافتمندی نیستند. و می‌دانید، ما کاملاً قاطع عمل می‌کنیم؛
دیشب ۲۲ فروند از قایق‌هایشان را نابود کردیم.
آن‌ها سعی دارند محاصره را بشکنند و وارد شوند.
نیروی دریایی و ارتش ما عملکردی فوق‌العاده داشته‌اند.»
@News_Hut</div>
<div class="tg-footer">👁️ 8.51K · <a href="https://t.me/news_hut/70618" target="_blank">📅 17:07 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70617">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=liF51rtqgLNWp2RHIHmPnz86YY42kwP5S_BuM6ZXgc_O9ah_DKD1tkUJn6S_WhcOYhHae8N0wSomeYjmPbaR0QnQHs2AWboC7PfK0v4P9iISTRNFWGK2sNoKLOFwGGz9kcabIZ7OjhWZAOyAdw8Zh7zUvzclcF5FYCobKqWxQdiNB7vuNaOB3uY_oWjOR1UByyxqf7vrk4q_ScoTv3xJdfrXtY2Pz6HYEMBVDVVU0hWnRp_-4E993pVCyLFvGBvgm5RJZ8Yl7dqPzgzkXfMkqPxx2yH2MEkDgRs8iBtP4sbA3SbrsfLfcDxw73s4k-YipseEXb1RfvvEcOV0Rk7CUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ecc2b192.mp4?token=liF51rtqgLNWp2RHIHmPnz86YY42kwP5S_BuM6ZXgc_O9ah_DKD1tkUJn6S_WhcOYhHae8N0wSomeYjmPbaR0QnQHs2AWboC7PfK0v4P9iISTRNFWGK2sNoKLOFwGGz9kcabIZ7OjhWZAOyAdw8Zh7zUvzclcF5FYCobKqWxQdiNB7vuNaOB3uY_oWjOR1UByyxqf7vrk4q_ScoTv3xJdfrXtY2Pz6HYEMBVDVVU0hWnRp_-4E993pVCyLFvGBvgm5RJZ8Yl7dqPzgzkXfMkqPxx2yH2MEkDgRs8iBtP4sbA3SbrsfLfcDxw73s4k-YipseEXb1RfvvEcOV0Rk7CUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
ترامپ درباره مجتبی خامنه‌ای:
فکر نمی‌کنم مجتبی خامنه‌ای مرده باشد.
او به‌شدت مجروح شده بود؛ سمت چپ بدنش، دست و پایش، و تمام آن ناحیه آسیب جدی دیده بود.
اما گمان نمی‌کنم که مرده باشد.
اگر هم مرده باشد، دارند نمایش خیلی خوبی اجرا می‌کنند؛ چون مدام صحبت از این است که باید برای گرفتن تأیید نهایی‌اش با او گفتگو کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/news_hut/70617" target="_blank">📅 17:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70616">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=OUi0E-P5WVYwHCG1I7uBKTXYc53vNcsNjFWVILPCIBsH5zWstiOs-W-e9o6y26khffvD0XOSkML7XyTtuTGLNmJhGz6ohjCFvKeEM64jttUl_7u34_ziiedsjamavrMXzyRhD-O-AUE0Eyz38DRik4nQvlJJawTUC5zDFyqJtQLaiKThEL_jtmwqvc8l4d49sFL1phOWp__3wCQCAzYPfVnc4LVBHtJeXosus7O8lY4qTu4UOzjlzaNh5Q2BjZGRneej54zMjTN48OnNkoUYA2cefph5wLslBK6UcmNTuTyOuynj3PfrXfT1w5b2eIugkvc6zEeTJoqkp3uVqGf5tg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/852e6e635a.mp4?token=OUi0E-P5WVYwHCG1I7uBKTXYc53vNcsNjFWVILPCIBsH5zWstiOs-W-e9o6y26khffvD0XOSkML7XyTtuTGLNmJhGz6ohjCFvKeEM64jttUl_7u34_ziiedsjamavrMXzyRhD-O-AUE0Eyz38DRik4nQvlJJawTUC5zDFyqJtQLaiKThEL_jtmwqvc8l4d49sFL1phOWp__3wCQCAzYPfVnc4LVBHtJeXosus7O8lY4qTu4UOzjlzaNh5Q2BjZGRneej54zMjTN48OnNkoUYA2cefph5wLslBK6UcmNTuTyOuynj3PfrXfT1w5b2eIugkvc6zEeTJoqkp3uVqGf5tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
🤴
امروز 4 شهریور ماه، زادروز شاهِ شاهان؛ کوروش بزرگه
.
@News_Hut</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/news_hut/70616" target="_blank">📅 16:57 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70615">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/79b4425472.mp4?token=hj8PJ3j6zbgpUzIC2RSPHifJxVMRpJW68GD2UYNB3iDBwBuyNOeW4z-j-RlbQzHeJw-epwiKLf7L_rvw-ugIT15E-K9Uo2PsB0a6y2w4Oxi3Y2W3sTBAe-oTzNuHPOP9_CfL36jbJHDqoljCTA32cJfU7M5evIu_fPr1NMCteGcikh5aN0ygY_pG7cBWYjTzE402Qt2yxD2PvjEOZNc2h88NoTWol09pMPRHwK56nre_XmaDx1BBWdojf6t3OkiWy7sOa6lUneMs646q6uCEkn1KlAkDzZ_Sj8rrLs5ttnanza1tJ4q8X_onTUkd1gnPky_xizCN_1W24qdR5nF5dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/79b4425472.mp4?token=hj8PJ3j6zbgpUzIC2RSPHifJxVMRpJW68GD2UYNB3iDBwBuyNOeW4z-j-RlbQzHeJw-epwiKLf7L_rvw-ugIT15E-K9Uo2PsB0a6y2w4Oxi3Y2W3sTBAe-oTzNuHPOP9_CfL36jbJHDqoljCTA32cJfU7M5evIu_fPr1NMCteGcikh5aN0ygY_pG7cBWYjTzE402Qt2yxD2PvjEOZNc2h88NoTWol09pMPRHwK56nre_XmaDx1BBWdojf6t3OkiWy7sOa6lUneMs646q6uCEkn1KlAkDzZ_Sj8rrLs5ttnanza1tJ4q8X_onTUkd1gnPky_xizCN_1W24qdR5nF5dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کوهنوردای ایرانی موقع صعود تو کوه های آرارات، آیفون17 این دختر آرژانتینی رو پیدا کردن و بهش تحویل دادن.
@News_Hut</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/news_hut/70615" target="_blank">📅 16:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70614">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=m6IwxS9ZcB9Dr62oUl56WUxvyDy2AZY_ekvRZM2MtwFiq-94SSkr84LPrTqdaUez3NrIZepRP0xxSGvf9aI46Qn-cqP9463lwIglt7cf--qtGT9wzkbQoEAXPlYoSsyhCkn3CGNTJY_AlcKeAI96eM8MIIV7DOXnByC1Iqh5BUsq0njLxJ939HTHO_s1lBtGYzSEIU1b9wgCt6u4tWAqVW5vm5J8pROASGuVWgR30Y-jqANYoh-4Tt6NjEFiBpRhFjYbu3RDX3HBTI2PtTCqYCyHKiZNW4D9zUaomDsXnmjHo4lCcfA6sEX1ZyFaEhgtjOYWBzkGNnsCAQe0ktO4Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/662dd7f509.mp4?token=m6IwxS9ZcB9Dr62oUl56WUxvyDy2AZY_ekvRZM2MtwFiq-94SSkr84LPrTqdaUez3NrIZepRP0xxSGvf9aI46Qn-cqP9463lwIglt7cf--qtGT9wzkbQoEAXPlYoSsyhCkn3CGNTJY_AlcKeAI96eM8MIIV7DOXnByC1Iqh5BUsq0njLxJ939HTHO_s1lBtGYzSEIU1b9wgCt6u4tWAqVW5vm5J8pROASGuVWgR30Y-jqANYoh-4Tt6NjEFiBpRhFjYbu3RDX3HBTI2PtTCqYCyHKiZNW4D9zUaomDsXnmjHo4lCcfA6sEX1ZyFaEhgtjOYWBzkGNnsCAQe0ktO4Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ویدیوی وایرال شده از نوجوونِ 18 ساله‌ای که با موتور کار می‌کنه:
من روزانه 8 الی 10 ساعت کار میکنم!
امروز یکی ازم پرسید چِتی میزنی یا نعشه بازی؟ گفتم هیچکدوم.
با خودم گفتم من باشگاه‌ام رو میرم، خرجی خونه رو کمک میکنم، اهل دود و دَم و دختربازی هم نيستم.
به خودم اومدم دیدم از خیلی از هم‌سن‌هام جلوترم واقعا
تویی که از این روتین خوشت میاد و سالم زندگی میکنی، به خودت افتخار کن، چون مثل تو خیلی کم شده..
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/70614" target="_blank">📅 16:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70613">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=mC6r4UY9Yog_5Q3Vg9pfHyqpEWO5LYjANro8_0xEei16TlOK5sXp6Ei-RoGZG9pZ0WD3o9G5ZGnJmeSga6bLj_uUHo_eONQH42prA1N4miYmmnwM1sW99AQnkRScD479k-FasnliZbhLMsj3PawuJOedNJbAwYc2il1qvw8pR-uYy683L_dmEL8G0itakGGHFBOVR-RJicSwaUrLpbjZvuoQo7ChXbfStEPjbOv72VHiVCzYIh7pt0Q1mdeyYkRpr5rUaP6yKxBfEyh3KHB9GLFOnoo2wzCJQv9sLihBHRU7QIY-8nB98nJz-Q0po1TyEpzBWlA9mLrVb0e_TC_eYA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/91fcce4d61.mp4?token=mC6r4UY9Yog_5Q3Vg9pfHyqpEWO5LYjANro8_0xEei16TlOK5sXp6Ei-RoGZG9pZ0WD3o9G5ZGnJmeSga6bLj_uUHo_eONQH42prA1N4miYmmnwM1sW99AQnkRScD479k-FasnliZbhLMsj3PawuJOedNJbAwYc2il1qvw8pR-uYy683L_dmEL8G0itakGGHFBOVR-RJicSwaUrLpbjZvuoQo7ChXbfStEPjbOv72VHiVCzYIh7pt0Q1mdeyYkRpr5rUaP6yKxBfEyh3KHB9GLFOnoo2wzCJQv9sLihBHRU7QIY-8nB98nJz-Q0po1TyEpzBWlA9mLrVb0e_TC_eYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این کلیپ هر ثانیه بیشتر سورپرایزت میکنه.
@News_Hut</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/news_hut/70613" target="_blank">📅 15:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70612">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=lyWtm8z83Uu2zOon0zv18xa8O5Y1U944dMYbRrlmvnHu2B8ehGCAxA-31dgrx_pVOo3Q8nSBkfhmyd_j-9LknaOSKwLLjFnmiHaOXK_0180LlB7q4a4xtbRH7y0dphy5tciHShM9xurEMK0TzZga4myXg9bjV9jGAbVu6DudhjZhLiD5r33AS5DmsaiVizNt5Bwu3QJL_7b5vN1Fd-fi51IC802DR3kU6iywmKw19IHQjhRhP2f9b_TnGD1iOjB5q5x2TSLtocgvMOtlkRWbPD7adg-9S5pVZZwF6QC3hPO3mAD77aEalsuACat3RzzZ-AT6sWuFRYFwEQD6AC2z8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ee1652504.mp4?token=lyWtm8z83Uu2zOon0zv18xa8O5Y1U944dMYbRrlmvnHu2B8ehGCAxA-31dgrx_pVOo3Q8nSBkfhmyd_j-9LknaOSKwLLjFnmiHaOXK_0180LlB7q4a4xtbRH7y0dphy5tciHShM9xurEMK0TzZga4myXg9bjV9jGAbVu6DudhjZhLiD5r33AS5DmsaiVizNt5Bwu3QJL_7b5vN1Fd-fi51IC802DR3kU6iywmKw19IHQjhRhP2f9b_TnGD1iOjB5q5x2TSLtocgvMOtlkRWbPD7adg-9S5pVZZwF6QC3hPO3mAD77aEalsuACat3RzzZ-AT6sWuFRYFwEQD6AC2z8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
لحظه شلیک RPG توسط سرباز روسی که جلوی پاش میزنه
😳
@News_Hut</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/news_hut/70612" target="_blank">📅 15:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70610">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=lRvcVJ6k4rO-IRhlL0OzjPspLbY5KWIfuPHYsFH5vuBJLh09LIsibOHHfowKInVjg_OUUmMj-awYt6fhz-KoP2FoBBgVFz109-qJldqaHFfglC26WVEoS-x6DRogDSYVKWhq8O9RPc_ElHHyABtEVp0XWxwGjdkFzGB3JkYKqRoofgYWO3xxUP3LRGzxDvq_JNzs0axIswJY2H7VBGXSvfKMT6a783n5e88jLc7fXoa5A-9TDzEfkBQmDUcfMw7G42GEsqC8UE5z7ma0Qf4p7sI7GdZd8jwnyjwfTaAyDcgPMWkY8YUaJlz-nOn4TfJmdmXbh7Gp_By4WIbzWcI0GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/378122b9f3.mp4?token=lRvcVJ6k4rO-IRhlL0OzjPspLbY5KWIfuPHYsFH5vuBJLh09LIsibOHHfowKInVjg_OUUmMj-awYt6fhz-KoP2FoBBgVFz109-qJldqaHFfglC26WVEoS-x6DRogDSYVKWhq8O9RPc_ElHHyABtEVp0XWxwGjdkFzGB3JkYKqRoofgYWO3xxUP3LRGzxDvq_JNzs0axIswJY2H7VBGXSvfKMT6a783n5e88jLc7fXoa5A-9TDzEfkBQmDUcfMw7G42GEsqC8UE5z7ma0Qf4p7sI7GdZd8jwnyjwfTaAyDcgPMWkY8YUaJlz-nOn4TfJmdmXbh7Gp_By4WIbzWcI0GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این زوج به اسم مینا و رضا بعد از پنجاه سال هنوزم عاشقانه همدیگرو دوست دارن و پنجاهمین سالگرد ازدواجشون رو به زیباترین شکل جشن گرفتن و رقصیدن.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/70610" target="_blank">📅 14:32 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70609">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/SJgQKNZp42lPrkkj4hNK-3eauC4r6EFmwf0z0h6v3pk_eQ1VuTjouAHSdHdTM7e7ExA1andi5IeFCqneg5bgFveoUm5gAq9Br8pFdlLwfSWyUWZ35Qxxgry8rXn17eO3M1tj2jsPyfTA8gZ3L2ilw3K69_OOhS4LHzVYwM0bdEdsWBdPaCYhohL5cyNPGIkMcWHZK-dLRlBku_LyV2wPMqldr-1ZS0fSC_aslvDtoW0gZ5WDNY-D8M9JfzB58pBM7kJR1jn1qcNUvZP4ZCwvzssh0HiUiy8MtLbxEEvWtUmfpxTPaQireJC_ayfQjIMAcaQgeDMOxLu_Y3slxNMDhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زمان شاه هر اسکناس هزار تومنی، معادل ۱۴۲ دلار بود!
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/70609" target="_blank">📅 13:52 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70608">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c49c82616.mp4?token=DQv9IOswWGSCcbPG-xB6n7D3WOB1mfdgtiR9LtOTfZYaiOub6H7NWTX-s7GNjQOfOxGturTwB5iWLLl_kA8EcptcKvm1vLGl9q1EHMAcu78ZEETNDvqmBPpcV97NWRbgh--ud6LSfgMJUdF8vdHfKzXLjUnQzBW6kXAWbiJ75ObE7rJ9BUfgxEysYk26LUyuqATxHIYAlwhRTA2xEqusCioi_teNeoYPuPLFCPV12UFhu-VHtxBcBKDenSRBk6zyIIqLCQiwGdLyCoxe3CKd6AKfyipYDdwzMQPejxH4708WtPMmQqyECTfHExPxUK0mV73HYuNRf4tYLHlc1yc4kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
سخنگوی دولت:
تا آخر شهریور هیچگونه تغییری در بنزین 1500 و 3000 تومانی نخواهیم داشت
‏مهاجرانی: تولید داخل و ذخائر استراتژیک بنزین مناسبی داریم و جای نگرانی نیست
@News_Hut</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/news_hut/70608" target="_blank">📅 13:10 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70607">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c8a784e93.mp4?token=QaPZasNMp2aH90awUqrSXwzObk2m1vARq8ms-UI6o5GGMaWttZmEr6GNbG2gE6BXP6lYnS-MSAyaiRC4XdJUHgYifbn2fNxaw7ii_3KNBiv1EaTSIwPaE7MEWk8MG1Vw5rpftn4OYvuv3upXq1ScxoOF3dpp5QoaNGvZ9wQW7XlmViLKCh6AZsGzK6Fll3By8C7iCuqbOjh0YbbrmspJbRkJYLQuRzsEO0eYqeZumhi1YGyzTwz2eBmJnrTKRozFQMAtORwKBpBWLBBRF02DFNv2UrujTzScGwtpDx2X0InL5P2vzXlSIkOGW3jk7UJPZPJdWClNDyOGHenDkzxckg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
می‌خواهم به شما بگویم: ما همچنان با چالش‌هایی روبرو هستیم.
چالش ایران پایان نیافته است.
ما همچنین باید کار را در غزه، لبنان و سایر عرصه‌ها به سرانجام برسانیم و برای انجام آن مصمم هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70607" target="_blank">📅 12:20 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70606">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8feb89091e.mp4?token=e2e7ML4kAvgTmBRIT47lldtpcBY5ATdfMAwdGb29I-4ehumgY0kjM0_PFmxRzyEjsqL_9A4F7ZuiQXFjRK3WDfWQ6i5Odn0islh3jLeehU_dAx9XDAIBOMW1Ar1DK9hwcCiYG5Xxp_2bH-JEvg42-G0FQkq1nAqrWGjjC0ICpOhBdgpHn221VgX5neEGwhNiy_iek2JxUcI9z0G1Xpo75lf6Lt1FSe1iSc5grcmmp6YXGEjdDSmOwRiTMfRRxyf2gFnlQogJUqj4-JuaUsmSG_y5cd5peWpGf88ANzornwGcQn58p7wffSYA93zZL3w9xamc9-mduZ_Wo_2KU08YfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نتانیاهو درباره ایران:
⏺
و من به ترامپ گفتم که احتمال سومی هم وجود دارد: تشدید محاصره.
او دیروز آن تصمیم را به شیوه‌ای بسیار بسیار قاطع تأیید کرد.
اقدام دیروز رئیس‌جمهور ترامپ، تشدید محاصره ایران بود؛ نه از طریق تنگ‌تر کردن حلقه محاصره خودِ ایران، بلکه با تشدید فشار و محاصره بر کسانی که به این رژیم — این دیکتاتوری هولناک — کمک می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70606" target="_blank">📅 12:18 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70605">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c258982c.mp4?token=LgpU1NWs-SPE3c0ffUCITxpb2_ayaxE033B307bM2BdWMUok0lIQ1k22dPn0s4hYKZmMbeKtLYMAYwP51LGQ2ikDR-NizVAiPvNMhaMxVU3IqYwmiXcS_sNts9UJ98R4nvk1WEj9uotCk-FyHngTod8sOYG9fJqki6znB8lv5dH7eflT7fBrfGm1nfz7OArfQYrDDWRlRKxBpZG4YuHl2Rlho61-kHM7n2PubrWLfVlRGLTxnFFi4F_Plb_3KFBrta8XivtbMI5nsol7T6StkUJpbzcaugC-og98B3vZ0oRnlIutrmQh_OUz9z5RkeVtK5CzG5JfMn5HwyK6qXG-Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
نخست‌وزیر نتانیاهو درباره ایران:
⏺
به ترامپ گفتم:
البته یک احتمال این است که شما با ایران به توافق برسید؛ یک توافق خوب. ما هیچ مخالفتی با آن نداریم.
اما تردید دارم که بتوانید با آن گروهی که آنجا هستند — با آن وحشی‌ها — به توافق برسید.
🔴
به شما می‌گویم: نمی‌توانید با آن‌ها توافق کنید.
@News_Hut</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/news_hut/70605" target="_blank">📅 12:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70604">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa0f2625db.mp4?token=uQifEj-KVP9oNyLwxUBXvIU584p3Cu4Kdfg8hvbvZMCrskMQ7RBgU5UbKuUXq1rqQWyruClghHHOb3AdSuwNj2oW8oFE_MHmMPCR6RrjbOVQ6N1Ynep1TWpOAbWOis9v3MvdtlQc_nnPEzYDvo8z52UhphdO-VrQchsMRRV6oB_b1OgMDIaYSkLLn4cAuBA1nNsXKRI7OVfERcJ6EcaKM-0hAE1TZRhHCevwyzAyX3zJZsiCnbsZq2k3wl4mkOA6zJg7W4Jg3dxYXzA90rkywDS-cBFIlFr5fRptMGwqFAi3IK9IDFafryl22S7sDjADqAO3D_bz76LPe4-UiDdogQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رفسنجانی سال ۱۳۶۰:
پهلوی همه همت و دغدغه ش این بود که مردم خونه و ماشین خوب داشته باشن؛ زندگی خوبی داشته باشن و ارتباط ایران با کشورهای جهان خوب باشه ولی الان دیگه اینا ارزش نیست و برای کسی مهم نیست .
الان دیگه مردم دنبال معنویاتن.
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/70604" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70602">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b90ae8ead9.mp4?token=a_eYgzkJHrOkh1I6LT27XBioEMB-YnqYBlIqXwySGEiRzSZNxIOsIVNrsZivNu_AMbloodnAauMOgY5uNezjC_fK7H9jvbhgX4pD7pipjKxqTDc5cIdJSuYCEMob6W39mI0g1-3tXuf3SlFUKLiFJI-cDlMVLFDvfKmshOE8mR4rgUGdtN5V0iamYfcHaCL82OburL4Wfxube3Zs6SDxwYXpy09XDrkL12eQmaR9xDPkITlLnyTaJRvnuhck0n8MFeIuO4QgK7f6K7ibP0KAsdV4NjT6vbdNjuaQTkr6060h46PQiVnlbW5glSPFzWc89dI_GHA3P5gITwcd-1BOIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
مدیر شرکت «فردا موتور» داشت واسه ثبت نام کنندگان خودرو توضیح میداد که ماشین نداریم. دو سال و نیم صبر کردید؛ باید چند ماه دیگه‌ هم صبر کنید که مردم گفتن «سیشتیر بابا همتون همینو میگید» و ریختن سرش.
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70602" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70601">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70601" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/news_hut/70601" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70600">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g_YINNULRupLL0mIi_IbjL33VtZprRnNXHiLmoaxQY3gisjo0Ob6eTS0fay-V1skEPFQPMmtZlsIzL2fhdFRAW1CE9hyGUlGB0A8gQXfFYhEXbFHJNGGs05GqGW0YuI_ruvPUFKL4pEkhETTAaZKc3F-IQlCycRavKvOAh_YS6Z9Kp4dCEnKZy-xqpAxOqgMow08UxnD7tnnBeVt_Ca0exEDd6boWiJQvjQh8y4JbH74FqGzBPTkWAy71ixG5OxoYE5_WmOZXOsFRL_fVYrbxHOLeZzW_ZTTYQHL0FWp6Zsei-_VF_Y0A0tpk0MZiGcldfcyYPh1JfDFifx4QIMEGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r4
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/70600" target="_blank">📅 11:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70599">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/106022ab0d.mp4?token=pFPipaB6P9uhSNKgT1K_w5NEfz1maSjuHiPhq8ytYDQq_JmhLOs__78_nB3QCOKULkrQia-Ky6VPDtXiaX98W4RVQS1xenk555PUZkCzsjK3wih7vJZslGrEGXbdgyTGA0NcljwuOLrg0MCNJwpZoGy_JinmjSFe28pdffNnmpxWC2Y0e-BDe0T8JCD-JR9ElThTJqzr8P3m7OZof1M-S0AwrJIh4Fq0qCaNrkme9jPWllrLRqluwlo4NF95-gjOQBKqdudlTi__noxer_vOiqQjBpyIsizr1mPKmO47uPffyDCuwzZoLLihZMTCo0NvGvr3_mwuymajl6XJAVHz5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبتای یه آخوند طرفدار حکومت راجب حجاب
:
اگه شما آزادی پوشش داری، ما هم آزادی تجاوز به شما رو داریم
چرا اون کسی که میخواد به زن ها تجاوز کنه آزادی بهش نمیدید؟ آزادی باید بهش بدیم دیگه خودش انتخاب کرده که مزاحم همه بشه
اگه مردم آزاد باشن که هرجور دلشون خواست بیان بیرون پس باید متجاوز ها هم آزاد باشن
چطور میگی قانون باید جلوی متجاوز رو بگیره اما قانونی که باعث بشه لخت و پتی نیای بیرون نباید جلوتو بگیره؟
چطور تو آزاد باشی اون آزاد نباشه
هرکی لخت بیاد بیرون حقش اینه که سرش بیاد
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/70599" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70598">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c5b717c94.mp4?token=I7Nm5bSRmj0ZsGFaAXRGGKqK7rqb-YstUpFisWKX05zJToqLh9UkmXJOjiTfXEmMBsJ1upBJEZrFxe0PepJFFb_qHBTDsK0BiPAUPQe5rXXwlIu2NtzjZr1EbW2_oZkTi-HZS0ZGW7xUfGHcT273OrppX8V9wFDgCp1Ca2EO301gAQ--WTLxJbuNdV-tSA_IWLf2wBA6nD3MN-Ox-f31yEqScNtDPmnj17ZL5ZGCV39kcvVU1MwbCByYp7gVCWCYJadVtlsZE3QiGh2h1VqzoSXfwJOY0ShX1Yn0WnS-pN9Y_qZYn6jFnoAl8ZcS7-_Y5DifUO9VnWurB_Wc-poYrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این خانمه داره مشاوره میده یک فرد چطوری با رابطه تریسام کنار بیاد
😐
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/70598" target="_blank">📅 10:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70597">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bdd3ca324.mp4?token=rabd8qor8MVV9E01oPhetU8kxrwRCMBmCBO0ZC4i3cvrXXCHY8Tdpvudynwjig4dpZPeTN1IRfb8O0WfqfptoX6Jn-_rJoy0hlDHpBqaxXQJuPsw74Rz_zQo1M27FcIuHlKaid4KrzcocVwfC-CbosEWiIb-a-raeOhOrPBREsrcm7q4hKz9jPggvl9J2ulE-YFRNn82LaVX7PAY8fjy40evtt5D8NmX1L32TXwmd4iPFlDHTPuNf9rRaPws0fep-xnEOLvmkW4raftqqtGqh9YDG9xHwmHchk2O1id2upGyFGJXlNF-rZrS1Mnp0ljmTnVydEFOsFfl8jLmBhmnOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
همتی رئیس بانک مرکزی :
علت بالا رفتن قیمت دلار طبیعیه و نوسان های خاص خودشه
ما نمیتونیم بخاطر یک نوسان بیایم مسیرمون عوض کنیم
مسیر ما درسته و خوب جلو میره
اگه این مسیر ما طوری باشه که میان مدت دیدیم درست نشد اصلاحش میکنیم
ولی من معتقدم که این شوک هایی که ایجاد شده جوسازی امریکا هست و شرایط مطمئنن درست میشه و رفع میشه
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/70597" target="_blank">📅 10:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70596">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">❌
ویدیو وایرال شده از یه جوون ایرانی خطاب به مسئولین جمهوری اسلامی
تراپی خالص :
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/70596" target="_blank">📅 09:31 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70595">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=aVD8z77z6EryafkbYfMkv8Q7Eq_eyC2DFNU6IoNEFkM_c2yWM_KafWi3tfx-xHJZboxFzW0ZFchGdEb2HYlnuTYJbSX_Xm1OiI6wjcOKFjoab8lGhoM3cRiBVske3QPTEfCjEdegu8aMCHq6pGvId2pjGBkkIdP23LXavpcnTFQcHvURYTOzuuhvU9m29My0OYWv-tQ5z0hRlIRl946R5M0zigylmEAVV-B1asWAzF4frDIOQ4e6R0RwR4X1lQKvO3GzRPbsEDh-l24gzO67cfxTo2adMrx9S_RUOPWkn1wCGrg0ywYSglWtvuJ7ufeIhC40cGkw6VhfvoPdAcuoFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0e780a212.mp4?token=aVD8z77z6EryafkbYfMkv8Q7Eq_eyC2DFNU6IoNEFkM_c2yWM_KafWi3tfx-xHJZboxFzW0ZFchGdEb2HYlnuTYJbSX_Xm1OiI6wjcOKFjoab8lGhoM3cRiBVske3QPTEfCjEdegu8aMCHq6pGvId2pjGBkkIdP23LXavpcnTFQcHvURYTOzuuhvU9m29My0OYWv-tQ5z0hRlIRl946R5M0zigylmEAVV-B1asWAzF4frDIOQ4e6R0RwR4X1lQKvO3GzRPbsEDh-l24gzO67cfxTo2adMrx9S_RUOPWkn1wCGrg0ywYSglWtvuJ7ufeIhC40cGkw6VhfvoPdAcuoFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
غریب‌آبادی، معاون وزیر خارجه جمهوری اسلامی:
چرا باید همیشه منتظر حمله آمریکا باشیم؟ ما میتونیم پیش‌دستانه اقدام کنیم
بازگشایی تنگه هرمز فقط در صورتی انجام میشه که جنگ در همه جبهه‌ها تموم بشه، محاصره برداشته بشه و وضعیت یمن حل‌وفصل بشه
به فرمانده ارتش پاکستان گفتیم ما توافق رو نقض نکردیم
اگه آمریکا میخواد تنگه هرمز دوباره باز بشه، باید همه شرط‌هایی که ایران توی توافق گذاشته رو قبول و اجرا کنه
ما هنوز در وضعیت جنگی هستیم و تا وقتی این شرایط ادامه داشته باشه، تنگه هرمز هم بسته می‌مونه.
اگه آمریکا به اقداماتش ادامه بده، ممکنه قابلیت‌های نظامی جدیدمون رو هم رو کنیم.
تنگه هرمز تنها ابزاری نیست که ما در برابر آمریکا داریم. آمریکا نباید فکر کنه فقط خودش می‌تونه به اقتصاد طرف مقابل ضربه بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/news_hut/70595" target="_blank">📅 09:00 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70594">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👑
فقط کافیه مرغ از خیابون رد کنی و‌ پولت چند برابر کنی راحت
💵
👌</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70594" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70593">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=RfdGncfEvqMSR8bG7VUB9xdJD4eWfP8aGvQx6Cb82Ny1-OjM7OwR3iDzVsZ30tApfiWQO0Sdnq0E02wl4Yb76b3SboSh0YnDJ22RaEAOsAkycl8S3wfU6Ub6evbYhzCgJftDeXvwuHkjI8PwTeHjFY6uZicnix4uJYBJr79xoFU5drzEzEW3iUPtE936aPofm3FYrOyl1NxPvEt8oq9UUeoRvUSHerBmhM4hMxLaNlQqX5t6oqP6ENzm3CzTVUvexkXcX8AlSALEKyOdVR32yla2skOcRKv0cQk5hhLehtIEG8wHYkSMsfxzw0gKAs11zgtLvDo5aAm0rNmcxvm63w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17cffccbc4.mp4?token=RfdGncfEvqMSR8bG7VUB9xdJD4eWfP8aGvQx6Cb82Ny1-OjM7OwR3iDzVsZ30tApfiWQO0Sdnq0E02wl4Yb76b3SboSh0YnDJ22RaEAOsAkycl8S3wfU6Ub6evbYhzCgJftDeXvwuHkjI8PwTeHjFY6uZicnix4uJYBJr79xoFU5drzEzEW3iUPtE936aPofm3FYrOyl1NxPvEt8oq9UUeoRvUSHerBmhM4hMxLaNlQqX5t6oqP6ENzm3CzTVUvexkXcX8AlSALEKyOdVR32yla2skOcRKv0cQk5hhLehtIEG8wHYkSMsfxzw0gKAs11zgtLvDo5aAm0rNmcxvm63w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
بچه ها اسم این بازی عبور مرغ از خیابون  هست ویدئو نگاه کنید خیلی راحت 8 میلیون ازش سود گرفتیم
😍
😤
اگ توم دوس داری خیلی راحت از بازی های انلاین پول در بیاری حتما عضو کازینو شبانه شو
✅
توی کازینو شبانه بهت اموزش میدیم از بازی های انلاین پول دربیاری
👌
🔔
کانال کازینو شبانه راهی برای چند برابر کردن سرمایت
🤷‍♂
➕
کسب درامد انلاین با یه ادم حرفه ای یاد بگیر و‌ پول دربیار
💵
a3
🎯
همین حالا عضو شو و شروع کن
👇
https://t.me/+FaoDjhEVG34wMWFk
https://t.me/+FaoDjhEVG34wMWFk</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70593" target="_blank">📅 02:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70592">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKnsJwWi_X94QsM6tSpHIPjlvwewU5x6FLwMaYVr8c4pSK993uPZwxybOfAHs-gMXdRn6ckPj89M5aFKt_zSz70XvXQnEA8UILGRF5VUolPwomTlo9TvO41bUCnfZ9RcVId0RzANhdTJE74_2iIC7ywSyON904Pq4Btqxf32Vv-1eS03xObrQgZkkJJ_wslfLJPi90mBtqHeu7-Hhlj2R4fRNVvUqLYw_aHTqGSp3BDEpVKKXIgxMIH6JLKU7mAc03ukEb2psvZtRqqjTGhB7tslUBozqW-LJogOVx7tnZ7oMPvFeNQHnKoA09LTci-QIDtR3na0pEYuzM7nJH5OqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
وام ازدواج برای یک زوج ۶۰۰میلیون
⏺
یخچال ساید ۵۰۰میلیون
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70592" target="_blank">📅 01:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70591">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZPOYan_Hz9rLMr1X_u0gJR6RkGUnifmnBxi_3cFf9l4d7aZDjcI_wwU-Nsq0-mzmSqFVgxg-0xj0jgCbqOfQ128UDWJktJC6uhfRUFQi6zkKg2A35PmSuEpMJAaCPkB5WR9jV3FHNB3mYEBd2rsAlfk2j9xW7Y62iakawHhIRWUg3W96Wo5bNUnEZrXT5asLiHeGok3ORz6WJgxatFL_8-wmieTrcMQ4H789fPJxQjtfiCvEcVqCqFgbDSVv1YKyu3bDPNG_zBnTzAKjvsubgO758pdxy76llkhegvVJ77lswG8pJUmRIbP65ZHKEmDj-jwIOnWCIrD6QTWSesbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📰
🇺🇸
🇮🇷
اکسیوس:مارکو روبیو، وزیر امور خارجه، به چندین تن از همتایان خارجی خود گفته است که ایالات متحده «در حال حاضر» برنامه‌ای برای انجام حملات جدید علیه ایران ندارد.
در عوض، دولت ترامپ بر اشکال دیگر فشار، از جمله محاصره دریایی و کارزار تحریم‌های تازه اعلام‌شده، تمرکز کرده است.
روبیو اظهار داشت که اگرچه واشنگتن برای بازگشت به عملیات‌های رزمی گسترده آماده نمی‌شود، اما در صورت حمله نخستِ ایران، همچنان امکان انجام حملات متقابل وجود دارد.
انتظار می‌رود این سیاست دست‌کم تا پس از انتخابات میان‌دوره‌ای حفظ شود؛ زمانی که ممکن است انجام یک عملیات نظامی دیگر مورد بررسی قرار گیرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70591" target="_blank">📅 01:17 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70590">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpjKFYp3wJXhLOXRBgWWnD3acZFh5gU9GoS_IvLRtMC_N-sl1ZnZm_NNfJ4cVXns6fXFJQtrMaSVBXbFvPr8fxTSwQqr6qGm-HBQjeuld01jhLbr0OzDnTCrEi3cjbzDvJJW67xeziUY4Xjl19BHH2x5oFamXe0l_xJ0IQmC4AUa7UlEIo5PzfCfzVUKOPyF7irc_GX17B2y1XA4prWkmtF3Xf6mUWdui5SPS4LvWTMuhbyJOWoCySiYFR2GcI9BOfKzlB6fP75Wdkmkjz4hkHdP808ebJFmrrYUfYXhqzvwZ02EhPVMQg5B1oX1rb0pnCgcfM91nkW5ZuNUmYH7Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
خروج یک هواپیما از باند فرودگاه مشهد
روابط عمومی فرودگاه مشهد: پرواز تهران به مشهد هواپیمایی سپهران هنگام فرود از باند خارج شد اما مسافران و خدمه در سلامت کامل هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70590" target="_blank">📅 00:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70589">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">⏺
🎙
وزیر نیرو :
تا دو هفته دیگه شرایط آب هوایی به حالت عادی برمیگرده و خاموشی ها تموم میشه
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70589" target="_blank">📅 23:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70588">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJZzmBDCvVFkm3VIM3GpUIp_ydJy4yilsex2ab9lxLimoMFpavR8TCGwYclt-TyNPUikKQZiclxr04bFS8NQCj1eQ3JXK9gLeOaJDfz7skNyxWPMBc63v9el-D3OS1du-xkClxSikDEnCo-0WPqneuYQoBUuhjK40hc4YUPjc583Hky7TwhetJlL190jHg_lkW41YeP_Jl-ucLxPnDiLnWnT-c_VazkyrOWy_L8OAYbblOGI6LmeTfuA1wBqoYy2uTwHrGJrwNyAvffddoNORXCIT0bz20bIouHrXasUOsWH08R1ixrHSkmPG_nVImSc37faFDF_T-JQAS5YPfB1dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇴🇲
بیانیه مشترک ایران و عمان: دربارۀ چهارچوب ادارۀ تنگه هرمز گفت‌وگو کردیم
رایزنی وزرای امورخارجۀ ۲ کشور بر ازسرگیری دریانوردی ایمن در تنگۀ هرمز با حفظ حاکمیت خود متمرکز بود.
🗣️
چهارچوب پیشنهادی شامل این موارد بود:
ایجاد یک کریدور مشترک از طریق تنگۀ هرمز
اجرای پروژۀ مشترک برای مین‌زدایی از تنگه
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70588" target="_blank">📅 23:15 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70585">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/da205f9cc0.mp4?token=EHrELH1e-9bb4h7MNfWdlsEitbw2G6GtKjt1n6JkkkGY_frQrTySEiebfh3LtPUcGgpKtcPZqM1UOkNSvpZD3YCaiM1fJMWbOJYR8ou-9EZLD6pKmgEohDGTFOu8cleZWzjaxdcddc-5aysxWZfm-g2HaevKKJPbGQ25LAm6hM68U5yTa98-fKIGD9IpJY1efn0WmWzgJjLncgSfFcme9TOMHILnERA5YEahWWX3tOf2WDQ8pEl_AB3xJySqJkcEtpoodjyagNA9369Pi7UGDGpik9mEIjZSqRuLjnMPqN9U7S8AWgFeoKiywB0MDRp48u49hcf7uAUlnLXhsheSlg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی به پالایشگاه نفت آفپسکی در منطقه کراسنودار روسیه حمله کردند.
در پی این حمله، آتش‌سوزی در پالایشگاه مشاهده شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70585" target="_blank">📅 22:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70584">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49911fbc7e.mp4?token=gnlMYgw3RRcRWs9SzIULv0Fpc8FVjrlvUpVi62sN4ZYmrxvxXUTvSPLicIEXyv9nZoetrJjmCRpJNAciCTkIExQ6EEV7T9aFuPX-zu6vRDF-b3ZDYzY3d0jkT70_VaFezu5uJlsJVzHOCZ4q12yO9ppUjhaPybni2rV7DMnYW1hOgETllqlQhXIZQYYiGnF-tVlpVT9ZpA7swws9zhVnNAT7qXz-TPq5x0FczmGHMx0NFUWFY_VwLLxLO9wyOFLxMqybktXN6EwK670xLzxeoGDVRonG_rtgJzS0-MU9SBIlL1_StApvFRGMUUbkqdXacZcuo2g3urtEMrEbH-v1IQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مستر‌بیست(یوتیوبر معروف) یه چالش خفن اجرا کرده که باید خودش و دوستاش از دست 100 تا نیروی پلیس به مدت 12 ساعت فرار میکردن؛
برای اجرای این چالش ماه‌ها زمان صرف آماده‌سازی تله‌ها، دوربینا و مسیرهای مخفی شد و حتی یک شهر رو به‌صورت کامل اجاره کردن.
خود جیمی (مستر بیست) و دوستاش به مدت چندماه تو یه شهرک نظامی، آموزش‌های نظامی و امدادی دیدن و جالبی این موضوع اینه که مستر بیست برای خودش 50 تا بدل درست کرده بود تا پلیس‌هارو کصخل کنه.
این ویدیو یکی از پرهزینه‌ترین و پرچالش‌ترین ویدئوهای یوتیوب مستر بیست بود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/70584" target="_blank">📅 21:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70583">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9b72e753c.mp4?token=bZrwU0vT6zP2cIj-yJdFZ3tyxC-NuX4-sfXWKMjnWeiBwhWbdBc9gqLQT0ezOsk_dutkpmoM3tPv3bHXHo68EatuFmHxhMe92JoKwliqq-crXB1wJjx6VXRDoQPIf_y0R7-FNz2ijOnkgpbONv3EPGQCr5owfthPqHCwWOw_SAKPNEetxh8Dj-S1N4kJ-g1YNFUVVDT4U6YLmzkn1cRL3P8mZN1i9FcDK_Zl4gT4Ya-dCDqYsgI1rUUXrzIjTjckQnYpmxemETq9GD5vXepXGfuCZCj3wCgclrE-f34XqP8zHq1IQG36yTIfVx0wNM0Bq3OoL1P7RxqJudyVm5KHfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
سوال خبرنگار از شاهنشاه آریامهر:
فکر می‌کنید در کشور شما کدام‌یک تاثیر بیشتری روی زندگی مردم داره؟مذهب یا پادشاهی؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70583" target="_blank">📅 21:14 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70580">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RMVe-Cxo_ELVkxVdXGJnPrruYKHZzh7EehwXE9vdKSI33K3oBGtOmj1m2cd8wQGw8uDcF9HVx7mDTUIWMESEeBuTC-O8t4pKQdSlML6aa5tZ50Nty5ppz_EyJiYVo8Blyv4zoaymwuIMWLJzV8jcKHph38Vp0f2D4otXn-unH-i4Y0X0gh6xIlpjGruQ_bAokqVPjOT2MVLfZ7sfvMiD8kHBMa6AY45Imu4RfFGr6tCygADNxwu15VnT9NyVEZyCkMo78d0oMtQEEh_SaoS411rjD7Z5gqm9ZUEl_IM59rArTwHii5vx0ef6synLHq39n554SdmzfJcnsyuLiZR3TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VndmRhUbRQPf7KdVm-Z3J9ar3X_qGD1jooVmgvLiU-RY2SMzMbMAmV1noV59kyKECUJ0_Z5OF0RAwhz_7embX2But3ypb2cEMrKXrPWX0bAsr83i8bV5TlQSzo98qciDkStiwTfeV1hUMxzGeLJTfT4zvlOXFSMmklSYRYV8TACtnYC9zRSU_2YRLsB27JqTzgO2GhXT0YFGt-v1CR2J8PGt1sIm77uYKzivN2ltoZ0KYhHWxBjMJwzf54kWLNL3GNmmki--ICB8memgGWTCfAVqZf-EwGupQGQB1sTybA16h0oCYuRjHJ0xrrPZqC4XXsMqGC8yyqRyF5itz-UwOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dAbPSAyE6wCIivBPbRIWplB_xdWuKg5M5aEluYX_kIKFla7gdGAV9L_qr_nbTvEiLETVEa4qMCjrIylZsqFNM4t_ezLTqPnM1GuOklr_UmYVe85bmOLkJE-got6UJEhcNQtbWwn-VsfT8-kl-0qsGcXBRernIFVn37wnR9cTxR8AeunpuH5AuV-PFk_enD-t5U_eknPFVhVHEMV2gB435WM4E5-CXWIWrxxkO0gSR99oZ99v-ww70oj2vZnBik9WTUC2BbQeOD9gIbkymasIrRRGOtlTcrlVUJK7YyywQB5pcKhed-VNf_APcW0NVdmjpha-8aQhNzwrRrf1CtY9rA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
〰️
🇺🇸
🇮🇷
اسکات بسنت وزیر خزانه‌داری آمریکا:
🔴
رهبری ایران به واقعیتی اذعان می‌کند که اکنون برای جهانیان آشکار است:
فشارها کارساز واقع شده‌اند.
🇮🇷
مسعود پزشکیان، رئیس‌جمهور ایران، ضمن اذعان به کمبودهای اقتصادی کشور، اظهار داشت: «جنگ باید بالاخره روزی به پایان برسد.»
🇮🇷
محمدباقر قالیباف، رئیس مجلس ایران، حتی صریح‌تر سخن گفت: «هر چقدر هم که قدرت نظامی داشته باشیم، اگر مردم گرسنه باشند و خبری از گردش مالی، رشد اقتصادی و تولید داخلی نباشد، دوام نخواهیم آورد.»
در دوران ریاست‌جمهوری ترامپ، وزارت خزانه‌داری همچنان به قطع تمامی شریان‌های حیاتی اقتصادی که این رژیم را سرپا نگه داشته‌اند، ادامه خواهد داد تا زمانی که تهران کاملاً منزوی شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/70580" target="_blank">📅 20:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70579">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/JfomaLXFewvRnBn-L2yNFknKbAmQeRJ0bPWxlEBNkemoF5LUrXO4eHlpYh7rJNsjGRi1oI7dmmr74pc5Nf5Xf9vnS4sTjkcDlR_v5AZF4f52H_7a1gaiQHMdmkHo3s2bortazUNoUefQ45qTzPcGsz0e_IqabPdq-aBEFNvSwq2HPlMHnfn8HRbLW5Ptgk_agzLjGMmAIkdRZf7y3GmkM1-_r0yHbyuTn5pWU8SUz6Vdj9uClvIkHtWrqL5xKNr4_7zN18mNJVEJrOD10yNpfg3nB9ANoWSlPpR90h--K14ypOXeyd-rOoPMmxxwexSUsy5lY6UeFUprOhcyysbZDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
💬
اکانت رسمی تلگرام در پلتفرم ایکس :
امروز به کراشت پیام بده.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/70579" target="_blank">📅 20:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70577">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=EKCoUxgCPWtQZx8stN4Ja_4BJViw8KJ1btlqCeAnw9qSIPKFQPcRwzlnDgmJzkmufVFV5H-zw-Y12GjMW4wUDW3mWlzE7uzoKxVfhTRDSeXUDIyfjQ6qX-JIqhk210NVk-Z1aERJtf0GBtLxIKShhsE9KsqszDx44V_xf1-wWzOcLO3AU7bbqGrmJ9PbRoAdLH8_HNkjMlJ5AoXUJzcGNkolkI9XMOZvBcOeS1zFO2SF19n0e2yLPwepxJch4D0JfcEDwXbBAiNxZYP03EkfNxLJDkQouTfXvGw9bBeZMcEHj2vlEcnAPbB9klefJDNa3mfnsLqfZHSkwKfnGJ_eLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/370e63e8ae.mp4?token=EKCoUxgCPWtQZx8stN4Ja_4BJViw8KJ1btlqCeAnw9qSIPKFQPcRwzlnDgmJzkmufVFV5H-zw-Y12GjMW4wUDW3mWlzE7uzoKxVfhTRDSeXUDIyfjQ6qX-JIqhk210NVk-Z1aERJtf0GBtLxIKShhsE9KsqszDx44V_xf1-wWzOcLO3AU7bbqGrmJ9PbRoAdLH8_HNkjMlJ5AoXUJzcGNkolkI9XMOZvBcOeS1zFO2SF19n0e2yLPwepxJch4D0JfcEDwXbBAiNxZYP03EkfNxLJDkQouTfXvGw9bBeZMcEHj2vlEcnAPbB9klefJDNa3mfnsLqfZHSkwKfnGJ_eLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پسر ۱۶ ساله رونالدو و دوست دختر خوشگلش:
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70577" target="_blank">📅 19:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70576">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=KiaJ7b7rPHrYd412gtU2AOuPvT9h1Eek1foG11rZQTEYJWiiKRKWMCkFPCU2W1MMKGhBl0yJqG-TEubqe6Bxm1B0C4jBJ3y4u23MrX7GL48MzyC_EwC_M_2CVyRedheVG3xUodI0LynXTQiLrhdWqMf9_RKgNWIcQ5ejRIhEuzaViGBXqshObpZ296bNb95HWabxXQ2ptn8YQfeQtZ-SdazpKRXIoGiRSJaMne7n_p2_wMMF41hMZbDiNvtpBMs4obTMW4eBgIj3mBJ_zXzdPXGghDffnQNnTjyDYDqfN0B50egC40ylW9HAXFv0NvJmMvNL3yWHQqDIJT-2oOJnvIMWuNvjoIaGQeiCzBPQbLB8iK903YsWj4FlZ6YE_FTK4FZzgxBI5w6n6ECXB8ShCtsCKD1kyI7OCrIRgy4hbuYW6Jt-QuPueuY0TupYhrh5VClayQmtIxhNJPPW08LcjyUMeppP3iqptoJ45AqKnquuT8L_efELy2ffTXOcdgPWt_MCpCCRngoV3KYr8DbASgSSo9TOkLiN09YqpSsfTYxtEihbGxS6qNlyoThdFvbagScmZoquCCg5EfXZE0cBER74Qu7Bc3PP4KKEWQH5BHNWGlyoHDnIH7c9zQWc6J9aIp7vLmiN_chb0kezZQdQLwyRcS7m1rz49SXHOhCA7x0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/070dff64b7.mp4?token=KiaJ7b7rPHrYd412gtU2AOuPvT9h1Eek1foG11rZQTEYJWiiKRKWMCkFPCU2W1MMKGhBl0yJqG-TEubqe6Bxm1B0C4jBJ3y4u23MrX7GL48MzyC_EwC_M_2CVyRedheVG3xUodI0LynXTQiLrhdWqMf9_RKgNWIcQ5ejRIhEuzaViGBXqshObpZ296bNb95HWabxXQ2ptn8YQfeQtZ-SdazpKRXIoGiRSJaMne7n_p2_wMMF41hMZbDiNvtpBMs4obTMW4eBgIj3mBJ_zXzdPXGghDffnQNnTjyDYDqfN0B50egC40ylW9HAXFv0NvJmMvNL3yWHQqDIJT-2oOJnvIMWuNvjoIaGQeiCzBPQbLB8iK903YsWj4FlZ6YE_FTK4FZzgxBI5w6n6ECXB8ShCtsCKD1kyI7OCrIRgy4hbuYW6Jt-QuPueuY0TupYhrh5VClayQmtIxhNJPPW08LcjyUMeppP3iqptoJ45AqKnquuT8L_efELy2ffTXOcdgPWt_MCpCCRngoV3KYr8DbASgSSo9TOkLiN09YqpSsfTYxtEihbGxS6qNlyoThdFvbagScmZoquCCg5EfXZE0cBER74Qu7Bc3PP4KKEWQH5BHNWGlyoHDnIH7c9zQWc6J9aIp7vLmiN_chb0kezZQdQLwyRcS7m1rz49SXHOhCA7x0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صادق خرازی:
به آمریکا در افغانستان کمک کردم و حتی فرودگاه در اختیارشان گذاشتیم اما جرج بوش ایران را محور شرارت نامید!
بیشترین خدمات را به آمریکایی ها دادیم و حتی خون دادیم
این نشان میدهد یک جایی در پشت پرده محاسبات دو کشور نمیخواهد رابطه ایران و آمریکا به جایی برسد
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70576" target="_blank">📅 18:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70575">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=GQGP78_0-vpkviPCtDxLETKcxeyPJkjp2zDApswqEj9WHWF_Mij9mMCIt76NA2L9WbU0w__vrACUrKLDkjXBeD4JiQnJrIhls3snVxJqBVex27fwCk2WhoYcpJ2V0qyeb29L34oUGBsQX5Hk1O2CESEgTSd2yfWD6_gDjf6IuhAZxQWwB2tDLix26DlaxCXVpy_su2yU_bV1eanSDx4JyezE_5meP7AnugFN1BQ1QryTXquWYWlUjDCjDdWCPOjyDxML7LWgh_By0zng5WHe4Prv2aFf-OhmvfnKKhIas_HPMalwiEtZIt-ha1IUAPnkHWJMsqxy2gd5GQbQbHuQ5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b7fd64d7.mp4?token=GQGP78_0-vpkviPCtDxLETKcxeyPJkjp2zDApswqEj9WHWF_Mij9mMCIt76NA2L9WbU0w__vrACUrKLDkjXBeD4JiQnJrIhls3snVxJqBVex27fwCk2WhoYcpJ2V0qyeb29L34oUGBsQX5Hk1O2CESEgTSd2yfWD6_gDjf6IuhAZxQWwB2tDLix26DlaxCXVpy_su2yU_bV1eanSDx4JyezE_5meP7AnugFN1BQ1QryTXquWYWlUjDCjDdWCPOjyDxML7LWgh_By0zng5WHe4Prv2aFf-OhmvfnKKhIas_HPMalwiEtZIt-ha1IUAPnkHWJMsqxy2gd5GQbQbHuQ5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👑
نگاه هویدا به یکی از بی‌شعورترین و بی‌سوادترین مخلوقات زمین
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70575" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70574">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/70574" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70573">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAqsW0Xh1oXyS27KFcoeLI3VOG689v3zUihtrTjsTv30Fqk4nAZs3Zj3Ya_bJG55mesgWIdf9RMhYX_JTiuJW_kaPaHGHWQrwq2Mr6MmQr5aiLR1k3tO1JbpooZMg6WgCFFi5j1stb45JPzZRmFkTBCEwMha7X894FleLqyvgypLeQ8itTNoqAZSBNOuglrYPtYFRCSIJ1J_eTvYhcfw_a5VuJAegl4wPRUcqiniQWZRqA_rlnKs5Y8RYyW4DeT-1O9b7Ehl11gGKbWAVTVkOeaDMdsFR4LnqtzKd9hsOjfnWOKo_GAHYAGGzVMQmPsL_w8ytWsigNHAEhcYRhFkKrW4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAqsW0Xh1oXyS27KFcoeLI3VOG689v3zUihtrTjsTv30Fqk4nAZs3Zj3Ya_bJG55mesgWIdf9RMhYX_JTiuJW_kaPaHGHWQrwq2Mr6MmQr5aiLR1k3tO1JbpooZMg6WgCFFi5j1stb45JPzZRmFkTBCEwMha7X894FleLqyvgypLeQ8itTNoqAZSBNOuglrYPtYFRCSIJ1J_eTvYhcfw_a5VuJAegl4wPRUcqiniQWZRqA_rlnKs5Y8RYyW4DeT-1O9b7Ehl11gGKbWAVTVkOeaDMdsFR4LnqtzKd9hsOjfnWOKo_GAHYAGGzVMQmPsL_w8ytWsigNHAEhcYRhFkKrW4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
g3
⭐
کانال اطلاع رسانی سایت:
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70573" target="_blank">📅 18:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70572">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mITXxcPTCJTocsywO1554IVonGeBipJc8cIa7ZrNJ_Ore2ZLTPgJ8fIdXUBCeKG4GxkrBhyqSA-N379u8san7OwX0Suqw7FRcWDXOpzRB9PTTGMg1J8qwGSiGpFDBgHdufVJ_wrHuFcEwk_O9pm4SwpplQHaLAGCcthLuJU3yOUvY48nFXOGqdECXXczOBqZaAcbUKr8m6JE2N91EB-L5fmi-rw4Hl-RpUS-1rAnM2zEEA3ecuhAnLHKIRfLs3bIg9_tYG3Tu6C882T_5De37uTm5Y6r27A5oy5b4N2hvm7MZk76dqN5tJNUM_X6oI5Udb8QDkGPRrLdKj1xz1nEYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇺🇸
پرزیدنت ترامپ:
نیروی دریایی ایالات متحده به من اطلاع داده است که تمام مین‌ها از داخل آب‌های بین‌المللی تنگه هرمز جمع‌آوری و/یا منفجر شده‌اند.
به ایران اطلاع داده شده است که هر کشتی یا قایقی که مین‌های جدیدی را در آن کار بگذارد، فوراً و به طور سیستماتیک منهدم خواهد شد.
ما از طریق نیروی فضایی، هر اینچ مربع از تنگه را زیر نظر داریم، همانطور که در مورد کوه پیکاکس و سه سایت هسته‌ای دیگر که قبلاً نابود شده‌اند نیز همین کار را می‌کنیم.
سیاست عدم تحمل در مورد مین‌گذاری با تمام قوا و به طور مؤثر وجود دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/70572" target="_blank">📅 18:08 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70571">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=Gf0sXCozMaos05o_wTrhdgrE1DHLlS7AD_ST9rOQ3o30zWWEYSKVstVdrGFqlzcwBFFaCCdFQpc3z58SR6zKNd2kyBJroQSyFwhenz_O5Fm6rBm8r3Wdy3ycp1FMIAQdUS9SajLaEFvIZdY88NiBPQTvUuutQNos-M6-IaP4wcL8v8cYdydZvo2caxxqwk-_a-rjha7VOph4X1EKjgtWs3M-FANqxhb9L0c7fn6o13IsgMQ6U1vCQhMNJO5fULwy-HcTdWIPsAQi2IizrbT7y9K2dV6uxZe-E3Pe3TcXAIh34ncAi7BWNkrNKKF5cwDXf6cD9LUb9W0bn5g54Ziadg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8133b3536e.mp4?token=Gf0sXCozMaos05o_wTrhdgrE1DHLlS7AD_ST9rOQ3o30zWWEYSKVstVdrGFqlzcwBFFaCCdFQpc3z58SR6zKNd2kyBJroQSyFwhenz_O5Fm6rBm8r3Wdy3ycp1FMIAQdUS9SajLaEFvIZdY88NiBPQTvUuutQNos-M6-IaP4wcL8v8cYdydZvo2caxxqwk-_a-rjha7VOph4X1EKjgtWs3M-FANqxhb9L0c7fn6o13IsgMQ6U1vCQhMNJO5fULwy-HcTdWIPsAQi2IizrbT7y9K2dV6uxZe-E3Pe3TcXAIh34ncAi7BWNkrNKKF5cwDXf6cD9LUb9W0bn5g54Ziadg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
شاید باورتون نشه ولی ایشون بخاطر اینکه آلت تناسلی بزرگی که داره، گریه میکنه! میگه تا میخوام با دخترا رابطه برقرار کنم، جیغ میزنن وای هیولا، چه مار بزرگی و فرار میکنن
😢
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70571" target="_blank">📅 17:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70570">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=blywSb0Oz2UVU9_t200wJzoe17l0JyMGIu4nuIvPMBnc1UmdDnXtFguudDAL0bgEU9-UHqRJf6RYu2vTCOhXdTKfuMKlIVkkhtIrIBrJCXfmD0EZwNTjoLSn9C9wWMgEQFUpCRtzWVdjV28WDOiryuYPIm8r60Qp_Rahrgocam4qyCDUL4HvlLaDhfx4P6fRtfEMRoOAe69ZT3enPlwWeyk8Th8W6IYxF3JDUDqbLp2wEoIQ3shMypaktjIqsaQHAv8csMtWi2HigTUyUt1I2MbDP44qjthDg1SDW2oDXLeOKXyglo_7XOaLEGIhg3P_WjfJYd16VzwIZpRiaAhwkL4mmjhU3BFnHALUQdMcMmXfsF0J1hqJn8xq0xaIs6lR4c5-W8Hw7OvEgPPfgvdbrBxBXAjqPy3__09lOOt2XE46NbwdT8hft0EbezWDkV79-374jPcrn4EStIrSxl49oIzyyt1wLFMmjwZSdtaGR2BI18U2739rOIunVU242jTQDxS_rJabFHGJ55f5RW_MnfQ-dFKHSm9Vmm7K8ur4NBH6WEcTdAT6jWhBRDXmetTIAelBnPAm0dsCrdcRF7TqI4SD1rHj6AcbDZ6gV_5zBfsErYHEzC-KHTWxubBLoJiOl_p_pLugrhBQQG_ukGQKFXRRfAdu9el1KmYPQYv77qc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bb0dbc493.mp4?token=blywSb0Oz2UVU9_t200wJzoe17l0JyMGIu4nuIvPMBnc1UmdDnXtFguudDAL0bgEU9-UHqRJf6RYu2vTCOhXdTKfuMKlIVkkhtIrIBrJCXfmD0EZwNTjoLSn9C9wWMgEQFUpCRtzWVdjV28WDOiryuYPIm8r60Qp_Rahrgocam4qyCDUL4HvlLaDhfx4P6fRtfEMRoOAe69ZT3enPlwWeyk8Th8W6IYxF3JDUDqbLp2wEoIQ3shMypaktjIqsaQHAv8csMtWi2HigTUyUt1I2MbDP44qjthDg1SDW2oDXLeOKXyglo_7XOaLEGIhg3P_WjfJYd16VzwIZpRiaAhwkL4mmjhU3BFnHALUQdMcMmXfsF0J1hqJn8xq0xaIs6lR4c5-W8Hw7OvEgPPfgvdbrBxBXAjqPy3__09lOOt2XE46NbwdT8hft0EbezWDkV79-374jPcrn4EStIrSxl49oIzyyt1wLFMmjwZSdtaGR2BI18U2739rOIunVU242jTQDxS_rJabFHGJ55f5RW_MnfQ-dFKHSm9Vmm7K8ur4NBH6WEcTdAT6jWhBRDXmetTIAelBnPAm0dsCrdcRF7TqI4SD1rHj6AcbDZ6gV_5zBfsErYHEzC-KHTWxubBLoJiOl_p_pLugrhBQQG_ukGQKFXRRfAdu9el1KmYPQYv77qc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ارزش پول مملکت رقابت شدیدی با گوه داره؛
یه مادربزرگی گوشی نوه‌ش خراب میشه و میاد این پولارو میده به طرف که گوشی جدید واسه نوه خودش بخره.
به گفته‌ی خودش این پولا حاصل 6,7 سال پس‌اندازه. از دو هزاری بگیر تا ده هزاری جمع کرده که تا موقع نیاز ازشون استفاده کنه.
حالا طرف اومده پولا شمرده و مبلغی که به دست اومده خیلی جالبه‌:
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70570" target="_blank">📅 17:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70569">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/439a914edd.mp4?token=adhdUjrjIMGWOUMXJVFgl4MZYlLLUxRdytvUJmOZbBbCcoHB5QwF47O8G3cqQSmV-_g_q2yo4xl3dbrZpN4B19bpjeNfSewVrSKc3L6fU7xACk9wae-FBH2tEHLwt8yzEgVn0F5atyvHJ6QowqoQ-PgkRJEQxCZMAwar8-5afF6uo-5s3mzZgFxgwbnnTs52gffAZpZv64vqy2PByWJzOPp0f0cIICl5BY5v7u4ZjDRsfCewbTyLRWgWmlQBx6FAI33wBRHEAOrnbtRWlvGasfNQN_-uQpzx-7wd37oNsvM3NqJ2Z-TP2lQ0CIg6SyFEOMlp2H8JUe5HFdj92tz-VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/439a914edd.mp4?token=adhdUjrjIMGWOUMXJVFgl4MZYlLLUxRdytvUJmOZbBbCcoHB5QwF47O8G3cqQSmV-_g_q2yo4xl3dbrZpN4B19bpjeNfSewVrSKc3L6fU7xACk9wae-FBH2tEHLwt8yzEgVn0F5atyvHJ6QowqoQ-PgkRJEQxCZMAwar8-5afF6uo-5s3mzZgFxgwbnnTs52gffAZpZv64vqy2PByWJzOPp0f0cIICl5BY5v7u4ZjDRsfCewbTyLRWgWmlQBx6FAI33wBRHEAOrnbtRWlvGasfNQN_-uQpzx-7wd37oNsvM3NqJ2Z-TP2lQ0CIg6SyFEOMlp2H8JUe5HFdj92tz-VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حملات ارتش اسرائیل به شهر المنصوری در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70569" target="_blank">📅 16:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70566">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aPIZsaGnfJRs3lhLGC9gOguyrphSARybSjbdV7w_lQNahJ0DcrtbfdHxezfBGgnK6-_CvdIL_J7dKX9ZIMdr4UhJakNENUcs0wm_kjWlQgcBcoVP7_oISW4P7uR1um6boaRjsK0aNYXKocsywlgUt_0ywramZeb3kdnV0plnSeuSoUwzcWpdRfV9herwWDJjVxdS2B_I_WauQwjFkEdomWWf82PfbOlpCqhqRC36wz07rCXSaYhoxdwylkUGEpx0ekPzGOqgNbbdPf6bVy38rZfCqVN_NBygNifKNOOwBMxnc_4UcjEjMDQxZA-oANMnI4fLmbnWfa1MQdO4yR0N7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k6efEGhthCYDUY2Ou2-6IVr3g5EyE93Qm2L6BqyuHloZWs9vutOAbVH-oKfxjz0GTOIn6MT_a_hQRwESQdFCAsm0c0A-123g50TP_OxpENEWqFn-owe3qIfgDgY5pr9n0HM6LrzDJdj6GF9IHcB3HDdjPEKNqICnNsrGF3F_uDr_VuA5dThiko52NbYhq6aRZPlEPUxsMoqekZwwjFnykXcpDWFZjR0qwzDoN__GfMlGXVsCrBDiYSCd2z8NepCzKcSLXnPrPihHc31W6PRBluykYAKP22VkEuU7MzzFTDd03ht8aBe2f2R_IP1MzR-5ZgNeJiPMxGcA9L5TPQV4gA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eishmDx9MT4rBrKutPfVCEP0uCtkq--N-cJaFVzFGhN4ggxfAKAkXDX6Vvvifx1xkhDY7B_wCJ0buHeutTGTd1dpj6NniIMYsb7zVENmeaI4iKaRnvsCqOjdFNwrZJS3eLcpvzbzzMp37wBaaxFQ8Imt9kb0a9VoislY6zpU67okY_BQ9oUZh7sLlUD1VFggivPnhOd98jxFc6belzcq945AY_CUtfi66-2Efr10kP6HOwZTy-NIzo5xFWpaVEmzfS2SZq8czAw0spLoEFU2kRLhOCJuP8FSBtx2f_ZvmkPCt0U8FAL6ebeIPLxXpV7Vpb9DofhEOky-qe1_ODAVPQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇴🇲
🇮🇷
وزیر امور خارجه عمان، بدر البوسعیدی، با عباس عراقچی در تهران دیدار و گفتگو کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70566" target="_blank">📅 15:59 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70565">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rKYR7v5M_ZFu4dPaz-FWuqKPhXZ-iqBXkdazYLA_Vrsq3J0O_jYxQtGZ9YYn8eD6wQdIEZpSzVM--8fNbNIXQMKP4F5DrQn_g-GDdjUrleM8kuJcZ8KveAvd3Jw-rjeBbdUl906DOoEx-ngi59_IhhVgu45aKtY093auytq1YdWdXBhJnrnis56aTrb7BBDgAeffpdli1G7i3-sKAf9A19rSNQ4MohIAEfHL_rcS3havS-ScYEO03tF5s6Fp5GICqyBdEf2vlhcqCcxzoeI6tPBxqDXyzhRJkiO7n_WNQros65StvOQrnwSlJGDYeU9GAzAlWTiClvwcV1-eLRlIRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
❌
🇮🇷
بانک ملی ایران در سال ۲۰۱۸ به دلیل حمایت از تروریسم توسط وزارت خزانه‌داری آمریکا تحریم شد، با این حال همچنان در سراسر جهان شعبه دارد. اسکات بسنت (SecScottBessent) وزیر خزانه‌داری آمریکا به‌تازگی اعلام کرد که تمامی این شعب باید تعطیل شوند.
🚫
مکان شعب بانک ملی به شرح زیر است:
۱. امارات متحده عربی — ۷ شعبه (دبی [۲ شعبه]، شارجه، رأس‌الخیمه، فجیره، ابوظبی، العین)
۲. عراق — ۳ شعبه (بغداد، نجف، بصره)
۳. عمان — ۱ شعبه (مسقط)
۴. آذربایجان — ۱ شعبه (باکو)
۵. آلمان — ۱ شعبه (هامبورگ)
۶. فرانسه — ۱ شعبه (پاریس)
🚫
بانک‌های تابعه / سرمایه‌گذاری مشترک (در ۴ حوزه قضایی)
۷. بریتانیا — بانک ملی پی‌ال‌سی (لندن)
۸. هنگ‌کنگ — شعبه بانک ملی پی‌ال‌سی
۹. روسیه — بانک میر بیزینس (مسکو، کازان، آستراخان)
۱۰. افغانستان — بانک آرین (کابل؛ سرمایه‌گذاری مشترک با بانک صادرات؛ وضعیت تأییدنشده)
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/70565" target="_blank">📅 15:34 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70564">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DzpDYyvvS_o60uf9xqUS5AlhMTpCLwNIOx-KabdnPftXqNwB5wAOlfJxBt6AmMFKPP2HQNipzzWmLe2DkbXKNGw2HUuW3CaLIorDuYt5oYVCBDWd7DtlV44w4tvOATZBXFB6HqPqjdajd7Iu3PuBcGQ4jLNkhc5kaYIGjwxs9ucXcC58hz4tQkngU_ddi2olqp0LhTQ8EXb2Dwj_FuWpMGv04i_CBviSuOydxyvvG2ZpkZWe5cUO9t9L2I3sA8EjmlF6B4YGU-tqZTtbcmhI38DXU5kj9_SUB-Ye1JxGhKepUYssDXnUvdINzRGiUNdi_NkOkQuD_xE5jNlCus_TQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
جمهوری اسلامی ایران که در حال فروپاشی است، حقوق بخش‌های بزرگی از نیروهای نظامی خود را نمی‌پردازد و هم‌زمان، معترضان را — حتی زمانی که مشغول اعتراض نیستند — با شدتی بی‌سابقه به قتل می‌رساند. این یک بحران انسانی با ابعادی عظیم است و باید همین حالا متوقف شود. رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/70564" target="_blank">📅 14:43 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70563">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=RxGzaAJwKaeg_k8-8tpWWHI4n7wL9PMCS75f1aPHlRS-4XHGTKWbrJ3_u79ByNQDUERqKHFRZH1hXI6QOGs9fQRlMN-kBWEtPGNw2JgxyggqUIUnpr6SKQ-YNoU1I0bPcKd2hObgF4IfdHzZykzq5lo-V1NsGhK_uOTN8m5Fn7f8VwabTppWZb3nCGJCtjf2VIUyUqBEYuVvbmFhDIbA19LQWhZa7NG32it2_QbQ1LwCFv-HMsibopSL1-aIGrXdEx2cph4XDOoQmQpDFP2-HnFArW6EoaxOIjmnboJbsGr-g7jXAFaLuSh1wIxXnlfJ9KP2Vo4n9ogN_tYqRupJbRdCEs4n-UuxgpyErdD74DIsZsmtUkQW2LZzUL3QP73Pjw4BeSZ6QR4qDxC7LYHuO5Vm6rvXSLuhATuf4qN6SUNejI6_BcqCEdaK6g1irudDN3WtXL8Q-t2Yym9Dmn9fEw1uH9MNRATMW3L3zbUS7RuEWWJoRjuIrX3uUPT6-PYvGLdaz7QwTnOqUDDkXCBV6SJZtqcEZr5xkkU5ZLzRRNsV9G0JjCKJAly_9RtVMYXcs7gYBKhgfYuhbcWWADvhtOtG1J068tJwr__xOtq0iK1zbEpWOOATT9TtbbSjfK3X7muBFj354O7URNIUrZIGirzdvu2-B8wo3Y-gTMs08q4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0811e8964d.mp4?token=RxGzaAJwKaeg_k8-8tpWWHI4n7wL9PMCS75f1aPHlRS-4XHGTKWbrJ3_u79ByNQDUERqKHFRZH1hXI6QOGs9fQRlMN-kBWEtPGNw2JgxyggqUIUnpr6SKQ-YNoU1I0bPcKd2hObgF4IfdHzZykzq5lo-V1NsGhK_uOTN8m5Fn7f8VwabTppWZb3nCGJCtjf2VIUyUqBEYuVvbmFhDIbA19LQWhZa7NG32it2_QbQ1LwCFv-HMsibopSL1-aIGrXdEx2cph4XDOoQmQpDFP2-HnFArW6EoaxOIjmnboJbsGr-g7jXAFaLuSh1wIxXnlfJ9KP2Vo4n9ogN_tYqRupJbRdCEs4n-UuxgpyErdD74DIsZsmtUkQW2LZzUL3QP73Pjw4BeSZ6QR4qDxC7LYHuO5Vm6rvXSLuhATuf4qN6SUNejI6_BcqCEdaK6g1irudDN3WtXL8Q-t2Yym9Dmn9fEw1uH9MNRATMW3L3zbUS7RuEWWJoRjuIrX3uUPT6-PYvGLdaz7QwTnOqUDDkXCBV6SJZtqcEZr5xkkU5ZLzRRNsV9G0JjCKJAly_9RtVMYXcs7gYBKhgfYuhbcWWADvhtOtG1J068tJwr__xOtq0iK1zbEpWOOATT9TtbbSjfK3X7muBFj354O7URNIUrZIGirzdvu2-B8wo3Y-gTMs08q4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
وزیر اقتصاد:
تفاهم‌نامۀ اسلام‌آباد روی کاغذ نکات مثبتی برای ما داشت اما اسرائیل و تندروهای آمریکا نتوانستند آن را تحمل کنند
امید داریم همان تفاهم‌نامه یا بهتر از آن احیا شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/70563" target="_blank">📅 14:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70562">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUARblfSQzlmRCnJvqRY6zbCPvreaAoOobXX8MqoWxl_hH7XB-nResnPswozTg6RcEup_tbuKJOF2hjNmf6bljminj0tyTuN3nEjwMkrL40YeEkJJIS08NGXbkvz9-fmN7-AuqQEexzvqB8mBbJJqgGpcZ3_H9clVg1ho2qgvj6MJk6l_0VJpCtpSllgEzt33UxpNM6b4s1W8wAQGzEq5RC0f4d3p_LKhgJOnlLjk839ymU1ApOOGMWSIMkXiDAjsHHiR1mZNMNsugMjJrbJ4BIP2O7ExDeaeWIli_JoGKZ_whUea5VyvBWc8ersqjyyBPRwQtxtyP262lG2gJslUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">〰️
حساب اسرائیل به فارسی:
درباره ماجرای دایناسور خراسان، احتمالا فردا امام جمعه مشهد می‌گوید: «این دایناسور از برکات نظام و نشانه پایداری ما از عصر تیرانوزاروس تا کنون است!»
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70562" target="_blank">📅 13:51 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70561">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🔴
📰
اکسیوس:۵ نشونه فروپاشی اقتصاد ایران زیر فشارهای ترامپ:
⚪️
سقوط ریال؛ دلار به حدود ۲۰۲ هزار تومن رسیده
⚪️
تورم شدید؛ پیش‌بینی تورم ۲۰۲۶ به حدود ۶۹٪ رسیده.
⚪️
فشار معیشتی؛ گرونی و افت ارزش پول، خرید مایحتاج روزمره رو برای مردم سخت‌تر کرده.
⚪️
سقوط صادرات نفت؛ محاصره و فشار آمریکا درآمد نفتی ایران رو به‌شدت کاهش داده.
⚪️
رکود و بیکاری؛ فعالیت اقتصادی و اشتغال افت کرده و پیش‌بینی میشه اقتصاد ایران امسال حدود ۵.۴٪ کوچک‌تر بشه.
با این حال تهران قصد تسلیم شدن نداره و ممکنه دست به اقدام نظامی بزنه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70561" target="_blank">📅 13:16 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70560">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=qneq-ByVOrVUDiJML1bYQarBRX37jsrg3aMfQcwWoLJhXHjtswJJqB_ps6KrgJupm8W9a_6l8vPi1kniUQw_uMh0yMl_IVyFZlQn0EUrWW5vN2-J7LXBx5jdg1_nwZUx6ELsKbvD4TzhfjGgmSQ9SHmdbSLEVbraZEXLWPGwtkc-LytoXTZ1mreStOmd7fktNE95sBARWBDZsP_UnU_goBnrydKvuOHj_die_5fZW5MFyplfT0egdrXw8QFgU5Y3SVIcXyM00hJe2ryxgoVXctxzAs_qfBRirlQu769IsP29LnuminyJwysW1-i8abFVdRXgkRYtV--1QSF9xZpfzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a518ac30e.mp4?token=qneq-ByVOrVUDiJML1bYQarBRX37jsrg3aMfQcwWoLJhXHjtswJJqB_ps6KrgJupm8W9a_6l8vPi1kniUQw_uMh0yMl_IVyFZlQn0EUrWW5vN2-J7LXBx5jdg1_nwZUx6ELsKbvD4TzhfjGgmSQ9SHmdbSLEVbraZEXLWPGwtkc-LytoXTZ1mreStOmd7fktNE95sBARWBDZsP_UnU_goBnrydKvuOHj_die_5fZW5MFyplfT0egdrXw8QFgU5Y3SVIcXyM00hJe2ryxgoVXctxzAs_qfBRirlQu769IsP29LnuminyJwysW1-i8abFVdRXgkRYtV--1QSF9xZpfzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
صداوسیما یه ویدیوی جدید با هوش مصنوعی درباره پسر ترامپ ساخته و اونو تهدید به ترور کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/70560" target="_blank">📅 12:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70559">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/377055b126.mp4?token=hLny5bLzbkdoP8ojVBD_fsvudBOiyJUrbk9wpSgSTKGeh4xYg820GU-FqR0DmrVP7N-10ZXJT9CzUcBHPzthh1Iam7vpIDUtNAMGvK8GSNMPWMEN6hVh-tyAlSLfMAC5L-M4mvT7c4F1vRj7SaG5RAiqGidXegpR38fDy78SQcdrnqqyKBMA5X7hGthQesAmi2aQDlMDtJ_lJir-EK5xoLtDsNpFDBLz6Ll3PNWdxE4bZT6I7ZCeLyJug4j9W2NIBCLZDS5bkIl895LWDHg9I-tMJ8ckrl4faT6EMYahiMQuVuqgWj0hnXwZE02_yuidxelyO6ZmnEdsYRrEp7jpZg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/377055b126.mp4?token=hLny5bLzbkdoP8ojVBD_fsvudBOiyJUrbk9wpSgSTKGeh4xYg820GU-FqR0DmrVP7N-10ZXJT9CzUcBHPzthh1Iam7vpIDUtNAMGvK8GSNMPWMEN6hVh-tyAlSLfMAC5L-M4mvT7c4F1vRj7SaG5RAiqGidXegpR38fDy78SQcdrnqqyKBMA5X7hGthQesAmi2aQDlMDtJ_lJir-EK5xoLtDsNpFDBLz6Ll3PNWdxE4bZT6I7ZCeLyJug4j9W2NIBCLZDS5bkIl895LWDHg9I-tMJ8ckrl4faT6EMYahiMQuVuqgWj0hnXwZE02_yuidxelyO6ZmnEdsYRrEp7jpZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این شما و این برج زنبق واقع در منطقه ۱ تهران:
۲۸۰۰ متر پارک و فضای سبز اختصاصی.
هلیپد برای هلیکوپترِ اختصاصی شما.
بیلیارد، سینما، سالن اسکواش، باشگاه، مجموعه آبی، کنسول PS5 و سالن ماساژ.
اتاق بازی کودکان، فضای اختصاصی برای جلسات کاری، غذاخوری و...
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70559" target="_blank">📅 12:02 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70558">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=vuAV7Q3Oybt41rO88MlRlyTMW5_fJAk_P4iMMHwFU2KFPB0DI3qU67bH5aWPhsI4Bz6kG5qwUc7mv0dqam1C9PVMP2SrGkWXkWfdOGV9XJK_KiDyQCGmdI_W08NPoJKoc_SKDwDhKTU7P2jtgDRV2EJu3Z7_80ryYVGckSeBOdFocJLUSzYzp7w15x88g_LnVZRxV-CIXiA2ylQwGbZzqeRXaQFmCFajLyfxtqkhWSajde5EQ32Wx_twHxKfNUw3lEiZEONRSE2xH1-M_MPeckLzTpJlT6bHu7XWuE9kFRJJGhpoSkbHzRzGZsrep11vxjvnxIT0pTGXqXvGL3kuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e23f896bb9.mp4?token=vuAV7Q3Oybt41rO88MlRlyTMW5_fJAk_P4iMMHwFU2KFPB0DI3qU67bH5aWPhsI4Bz6kG5qwUc7mv0dqam1C9PVMP2SrGkWXkWfdOGV9XJK_KiDyQCGmdI_W08NPoJKoc_SKDwDhKTU7P2jtgDRV2EJu3Z7_80ryYVGckSeBOdFocJLUSzYzp7w15x88g_LnVZRxV-CIXiA2ylQwGbZzqeRXaQFmCFajLyfxtqkhWSajde5EQ32Wx_twHxKfNUw3lEiZEONRSE2xH1-M_MPeckLzTpJlT6bHu7XWuE9kFRJJGhpoSkbHzRzGZsrep11vxjvnxIT0pTGXqXvGL3kuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه دختر برای پارتنرش شرط گذاشته که هر بار دعوا کردیم، برای اینکه باهات آشتی کنم، باید برام طلا و سکه بخری و پول بدی.
بعد از یه مدت رابطه، این صحنه خلق شده
😳
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70558" target="_blank">📅 11:31 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70557">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BHczLovlK-8Kq9pAt_CFIinY4QuBra3RT6NpZaOrSGnCES7lbuFxyHWDf3ZWPqNtqUUNZABxwVtzmj5Ckt4N0Sn2Qy85eq26O7Dv3G_YG6iD-e5AI1iZ2JRi2uCSxLyBG8hHIpuqxNk44LUz5jdQ1_ZswmAUWE5uXE4aFdD9M6ZwA3migHa2u0qeeo8BufOGrVQNNxX7n-ozqSnj4fOG72Uc5AENIp5G9o6oj06An8T9ZL0pkgVwhBGqDF4hlsBfHLs4WIUj-XD36wvtFLDXwaaie-tzcur30OPw3X_ZhD450QrWC7EsiJqVcLN5CdrnTN0kC6Nl6BINgm57gSH_0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همتی از زمان دلار ۳٠ تومن تا امروز که هر دلار بیش از ۲٠٠ تومن رد کرده به آینده اقتصاد خوشیبینه
🤡
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70557" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70554">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=kylBem14u6E9AyS7jjRwlRb_P3XBbdbXKQ53tpbwaOIgoEO2VIYZ1PM5pYqJ8NovBDD5rCvxMkyuDzk6gw4toVm3Q4hbH8DLtr_CfGpW8lWAFcMpkYqe27yq9MpzEu8onumb4sbCUhNA3FI5swLO9nxfWKUen9uqeCBlrjj8Roff-kDlNqC_SD2J7EnBxfdAEmrziNFYYGemmtntic6fxHTu17q1CN0gKOBpeRf4e7JsWEUlr-Px0MpLIDIb6dh4y7nBHtYkoiDhwEGbh5nYoRiMfV6vMay6j6jD8ts3uArkDA3sLIJZPQn3whnzfDfRLPFHa_6NutjuTK_g0nqFaw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99d1804edf.mp4?token=kylBem14u6E9AyS7jjRwlRb_P3XBbdbXKQ53tpbwaOIgoEO2VIYZ1PM5pYqJ8NovBDD5rCvxMkyuDzk6gw4toVm3Q4hbH8DLtr_CfGpW8lWAFcMpkYqe27yq9MpzEu8onumb4sbCUhNA3FI5swLO9nxfWKUen9uqeCBlrjj8Roff-kDlNqC_SD2J7EnBxfdAEmrziNFYYGemmtntic6fxHTu17q1CN0gKOBpeRf4e7JsWEUlr-Px0MpLIDIb6dh4y7nBHtYkoiDhwEGbh5nYoRiMfV6vMay6j6jD8ts3uArkDA3sLIJZPQn3whnzfDfRLPFHa_6NutjuTK_g0nqFaw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
پهپادهای اوکراینی در طول شب سه مرکز لجستیکی اوزون را در سراسر روسیه هدف قرار دادند و تأسیساتی در آدیجیا، استان استاوروپل و داغستان تحت تأثیر قرار گرفتند.
این حملات در میان مجموعه‌ای گسترده‌تر از حملات به مراکز توزیع بزرگ روسیه، از جمله سایت‌هایی که توسط اوزون و رقیب آن، ویلدربری‌ز، اداره می‌شوند، رخ داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/70554" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70553">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">53.7 MB</div>
</div>
<a href="https://t.me/news_hut/70553" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
👑
امکان شارژ و برداشت با کارت بانکی
⚠️
برای ورود فیلترشکن روشن کرده روی کانادا یا سنگاپور یا آلمان و ....
📢
😀
Telegram Channel
👇
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/70553" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70552">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCTgJRhnm8RtxozBrW-Iuu6fnTizKR3D3nwx-8K6trwgbe8ddNp7Pw7_HKKggS_1gFIA0iOI6bEooKzarWNeEtehP9W0fnNElPNN4kLU54pqE71S2fZniqMTvZevOcxyXRpla-_CvxvT3SyYMFdfjGLaK37wtAuojdBX_1Wpa1KvMC5aGFCvFw6CEsPfRokWewBHIRv-Hyq5kT6SPXgi2lhHRHKgvKwanq3TRpxa34JCdkvo55ErXAECOmsCgzBhjo9KiDv0oqhSXqGNVl9kwZ-3ZlFIv5FrowTKWxGUlygvs2nfrSa-NZUOBRZir9AiCWzqhrAcuPqXaDKO4R2NBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
میخوای مسابقات فوتبال پیش بینی کنی؟!
🥇
پس نیاز داری به یه سایت بین المللی و معتبر
🥇
⛔
دربی بت
همون انتخاب  100%
💎
ویژگی های سایت جهانی Derby Bet:
⬅️
امکان شارژ امن با
کارت بانکی
⬅️
واریز اول دوبل شارژ می شوید(بونوس۱۰۰٪)
⬅️
پر اپشن ترین سایت فعال در ایران
⬅️
تسویه حساب کمتر از 5 دقیقه
⬅️
برگشت بخشی از باخت به صورت هفتگی
⭐
دارای لایسنس و مجوز anjuan
🚨
کد هدیه ثبت نام:
GG007
⚠
️برای دانلود اپلکیشن کلیک کنید
👉
r3
🔔
کانال دربی بت :
👇
✅
https://t.me/+c5jwC3lt9z45NTE0</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70552" target="_blank">📅 10:57 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70551">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇵🇰
وزیر کشور پاکستان: پیشرفت قابل توجهی در گفتگوها با ایران حاصل شد
⏺
📰
خبرگزاری رویترز به نقل از وزیر کشور پاکستان:
پیشرفت قابل توجهی در گفتگوها با رهبری ایران حاصل شده است.
ما در حال گفتگو با ایران برای فعال‌سازی مجدد «تفاهم‌نامه اسلام‌آباد» جهت حل و فصل اختلافات هستیم.
محور گفتگوها با ایران، تمرکز بر تنش‌های منطقه خاورمیانه(غرب آسیا) و یافتن راه‌هایی برای گشودن مسیر صلح است.
دیدار با رئیس‌جمهور ایران با نتایج بسیار مثبت به پایان رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/70551" target="_blank">📅 10:25 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70550">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=HtyDJTOt4d3sCOzBkb-y7h5sL1jCU76ScCpzWMFlyFWKpYpidzZjpfw-uuFYghuuX6b-RSCtkF4dSg5ullRJWtNtDBge8NdmRToMbnI-JI_ixCg-bMbfpVX8jU06zsuzVi0NX2bI3G_e0OM3DJNv3BbuwBmq5Y5V48wBTT4BHrekqkNTB6teX-o1Z8ieNSY819ZdrmGaHPmR3i7dQzuuO70SM3Fno2UYucGGPO56DllyMbxirWCbPhxG2vcIs16mxLtiCc-JswtNl8aUkjj167H3AuOR8H5o5YqPD7ZlZhqw0mtTvxaq2dWqZ9tTAf_j4ggBvis6YUQ_XECvyiQU6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b422bdb1ee.mp4?token=HtyDJTOt4d3sCOzBkb-y7h5sL1jCU76ScCpzWMFlyFWKpYpidzZjpfw-uuFYghuuX6b-RSCtkF4dSg5ullRJWtNtDBge8NdmRToMbnI-JI_ixCg-bMbfpVX8jU06zsuzVi0NX2bI3G_e0OM3DJNv3BbuwBmq5Y5V48wBTT4BHrekqkNTB6teX-o1Z8ieNSY819ZdrmGaHPmR3i7dQzuuO70SM3Fno2UYucGGPO56DllyMbxirWCbPhxG2vcIs16mxLtiCc-JswtNl8aUkjj167H3AuOR8H5o5YqPD7ZlZhqw0mtTvxaq2dWqZ9tTAf_j4ggBvis6YUQ_XECvyiQU6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این ویدیو به تازگی وایرال شده از یک گروهی که رفتن کرمان و در مکانی بنام قلعه دختر مثلا جن احضار کردن
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70550" target="_blank">📅 10:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70549">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=FMuh78GkfkEnPzLn9blCF9APVEfj9VCVyfWkVHjGIA3r5Z82uWMSFRQCT1wLLXI0hAUKb-h_cHdgQsYKzUGEnNqglawp2Eb98CORxhG4RCYaUqbYyd7LX7jvumGAypThVJctAnsCskqPeRxyEfWQEoopB0cQARNQvOKhWn1mRt6LDXPvEMYoWujN29MvN80Ezq29UG6POyPumB0shKQjdGnHnxq2WZUpe1MKxKQWMLIdtMt1h8se8Fb366DgP1EZAvQlLPhhjkbALyn2t0hPC0OQaYSRxs5zKWe_ZucqAuinHgemw7btkM7zXoUR4BCu31p3gaUtkLwm4tNISG7JzVX_UWR_kKFoOUNzIplCj2nbiKcbJC5fQatYkfxX859koberthYUKzpZV4u2pvgJ4BqF1iq3SGOJ0xjceenq61hSUcdLJ4z0gS9rcnpBvXGZXSfxWEN3yvfOOf2369D_YQsct8QM6melS_HUngUGTX9A_1ZCGoDJqJ-1XR925yFXXaltRFlhIrXzNyBnuRu43xcQ5cI4oO2Q-UjeDeHHWRWh-2z__G6zJiQUshMwOiRdk_SkRDFu-PrtUB4OaSRftJZhUogTjPB6meakMOM_WADqQXytJJnAGK9R7APw8nZsIpHtPl3Ak16KopjAu9mc3y6TN0amcwnSShffjDRHOCs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a52e52e69f.mp4?token=FMuh78GkfkEnPzLn9blCF9APVEfj9VCVyfWkVHjGIA3r5Z82uWMSFRQCT1wLLXI0hAUKb-h_cHdgQsYKzUGEnNqglawp2Eb98CORxhG4RCYaUqbYyd7LX7jvumGAypThVJctAnsCskqPeRxyEfWQEoopB0cQARNQvOKhWn1mRt6LDXPvEMYoWujN29MvN80Ezq29UG6POyPumB0shKQjdGnHnxq2WZUpe1MKxKQWMLIdtMt1h8se8Fb366DgP1EZAvQlLPhhjkbALyn2t0hPC0OQaYSRxs5zKWe_ZucqAuinHgemw7btkM7zXoUR4BCu31p3gaUtkLwm4tNISG7JzVX_UWR_kKFoOUNzIplCj2nbiKcbJC5fQatYkfxX859koberthYUKzpZV4u2pvgJ4BqF1iq3SGOJ0xjceenq61hSUcdLJ4z0gS9rcnpBvXGZXSfxWEN3yvfOOf2369D_YQsct8QM6melS_HUngUGTX9A_1ZCGoDJqJ-1XR925yFXXaltRFlhIrXzNyBnuRu43xcQ5cI4oO2Q-UjeDeHHWRWh-2z__G6zJiQUshMwOiRdk_SkRDFu-PrtUB4OaSRftJZhUogTjPB6meakMOM_WADqQXytJJnAGK9R7APw8nZsIpHtPl3Ak16KopjAu9mc3y6TN0amcwnSShffjDRHOCs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیوی جدید از حمله هوایی و پشم ریزون آمریکا و اسراییل به خرم آباد در جنگ ۴۰ روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70549" target="_blank">📅 09:30 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70548">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=jqsBjo8ZkfxGTizWhqRORtAN-kY9PzF91DnA9916SsEpmZGaLWeWHK_lXPOYcw5GnmWvtAYatrbHet_gnTFcVumz_UfPHwxUsbqNDujR4-gngWLgMqKQ1vlH8dFW9MP5F_axwzFE53oacs3WdakXQmKGJCyD93QFwGIk9Rp29BPKKP5nYXGF0YkIO_Zt_NP-gwWMtuSqnuUE8wjAJJeSZXrSBxEJrfruXoL1Y_OR6un4O5IF5-GoH8gxaBBy1pt3P2ygOl0xjLFJDB2QlaQZhgHOgtmwgT1CSv6BtCqiNDIl8YnQCchdYWNb9chaLzmJ1UwVWT0UczHval7sYHi1vBi3IwZQiOTRFUbO_rjsWBuyl0T-nyqfCEwUP7DZa_LzPDVw4tB7y_mZzngALI-aTV2EcUFAZLwgiVyezEPUFZ0EH_4BK2E-BAyKN84Ta358HbPiWQEcW52TeWir_CfoJzJ9G7YhpuxzT191kQ1lqLidnhlG3YbvLxZyIK8de9Z8HEhnX8JYnUJxhfaEsqz5p44Orx1ItwyKzAyfVdigl5KwZsX48JLY9GS10plSV6j1hN_cVqUn8TTceL3TaHRxSMCIrvHge_jcbYkBbRgPnS1__OdfBkPnN3G9FfMhyaNhnZfCTZriSwApHDN915yRSx4wDh68GhsCojbwXnaNiis" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b10dcd43f2.mp4?token=jqsBjo8ZkfxGTizWhqRORtAN-kY9PzF91DnA9916SsEpmZGaLWeWHK_lXPOYcw5GnmWvtAYatrbHet_gnTFcVumz_UfPHwxUsbqNDujR4-gngWLgMqKQ1vlH8dFW9MP5F_axwzFE53oacs3WdakXQmKGJCyD93QFwGIk9Rp29BPKKP5nYXGF0YkIO_Zt_NP-gwWMtuSqnuUE8wjAJJeSZXrSBxEJrfruXoL1Y_OR6un4O5IF5-GoH8gxaBBy1pt3P2ygOl0xjLFJDB2QlaQZhgHOgtmwgT1CSv6BtCqiNDIl8YnQCchdYWNb9chaLzmJ1UwVWT0UczHval7sYHi1vBi3IwZQiOTRFUbO_rjsWBuyl0T-nyqfCEwUP7DZa_LzPDVw4tB7y_mZzngALI-aTV2EcUFAZLwgiVyezEPUFZ0EH_4BK2E-BAyKN84Ta358HbPiWQEcW52TeWir_CfoJzJ9G7YhpuxzT191kQ1lqLidnhlG3YbvLxZyIK8de9Z8HEhnX8JYnUJxhfaEsqz5p44Orx1ItwyKzAyfVdigl5KwZsX48JLY9GS10plSV6j1hN_cVqUn8TTceL3TaHRxSMCIrvHge_jcbYkBbRgPnS1__OdfBkPnN3G9FfMhyaNhnZfCTZriSwApHDN915yRSx4wDh68GhsCojbwXnaNiis" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
زنده یاد مانوک خدابخشیان تحلیل‌گر ارشد سیاسی در مورد فشار اقتصادی آمریکا؛
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/70548" target="_blank">📅 09:00 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70547">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بازی شکار مرغ این روزا خیلی پرطرفدار
😍
توم میتونی بازی کنی و پولت چند برابر کنی
👌
از دستش نده
✅
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70547" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70546">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAmxYoJeZMzw8gdGk71NAqD8bhkHxPA3c79NR1OaANHLugv60QMV81EBDR9X_vWlnuVUVuxoYOpJK_Ec6GvoO1c_JPIEGlDZKu9DzdaPlSYmcvwiGtqO9202QM2JJmmKoUzGBQS4WKc8GrcseX3b3zjVMfASBVdw4umtgPCPsjBVO_Nu-3wPTfPIbBfCNAY4bQQGof3ff3RrdJ7P8n9cyuBTLtFSGlHmanJB94oqJ4EzaV4OZoTQxkaDI9LL0ilBmxuR0JtfJs6eqpWAAH_puFEAdb9XzgO5bg-ufnjLUeqhlIuaeTpplcrsfjOw8Z-bZ2QRGDSYJUU9XOnn-dINd_QQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7abc39cb8f.mp4?token=X9D-LTJJV9HdNqKIQF3bkFg00XCmIBoIj7Aw5E-AaCqRlCq8zud7gn-mUhRL-QB7J7uibKf1JZ7efKUzERA2i2yMuvSuLLB-IjNMP09lO6WO1kBbC9PWTAM9vpnfVMTTbI0Ga1m1oqucxu50m7s1ENaFPQ3dwAQYUFRE1yHPf7hkLZ_FVZ1LyRW5bDspTm0hHzDn25jcySyUo_ACeJOX3tmCHtanf60c_A71e9k8-N_Dz8VDL_itrmgVAq9z6nVd9b8GNnbyBGERNewQEbZ7Lm8ctm-JtwXf6Irzqi42zPHgU2JiYfQbDo6ogt4-TO5FFqHbDVKUIffwBQ8EaFTOAmxYoJeZMzw8gdGk71NAqD8bhkHxPA3c79NR1OaANHLugv60QMV81EBDR9X_vWlnuVUVuxoYOpJK_Ec6GvoO1c_JPIEGlDZKu9DzdaPlSYmcvwiGtqO9202QM2JJmmKoUzGBQS4WKc8GrcseX3b3zjVMfASBVdw4umtgPCPsjBVO_Nu-3wPTfPIbBfCNAY4bQQGof3ff3RrdJ7P8n9cyuBTLtFSGlHmanJB94oqJ4EzaV4OZoTQxkaDI9LL0ilBmxuR0JtfJs6eqpWAAH_puFEAdb9XzgO5bg-ufnjLUeqhlIuaeTpplcrsfjOw8Z-bZ2QRGDSYJUU9XOnn-dINd_QQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙋
ویدئو بازی پرطرفدار Chicken shot
🙋
فقط کافیه شکارچی خوبی باشی و مرغ هارو شکار کنی و پولت چند برابر کنی
😍
💵
💖
توی سایت بت اینجا بازی کن و پیش بینی کن و پول در بیار
😍
⬅️
امکان شارژ با کارت بانکی راحت و امن
⬅️
تسویه حساب سریع بدون احراز
🎁
هربار شارژ کنی 12% بیشتر شارژ میشی
✅
🎁
اگ باختی هم 10% باختت سایت بهت برگشت میده
✅
🚨
ادرس ورود به سایت:
💠
http://betinja.bet/affiliates/?btag=2760677
💖
فیلترشکن خود را روشن کنید و روی کشور مناسب قرار دهید مانند المان،کانادا،امریکا،ترکیه،سنگاپور،فنلاند و...
⭐
کانال اطلاع رسانی سایت:a2
👇
💠
https://t.me/+x83BW_KQnT01ZGE0</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/70546" target="_blank">📅 02:58 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70544">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bk_bwNWPnIAnnR4NDI2DaQWAV-Rx-0CBYegzTNgFfXvesnlLK54KRd2-aJcSN2LHGSAubQE4lZnfZ2lw084rZI-p8yqlxpurXNEc5G2AvgKZE7eLYJeeJr8F4o21yznTULa_lMikl7Yg6pfUyII1r2Ex8JlrM4utwQAFRLVR8B-VK3AEPh2FkmYGbZrmxzrzh3x1nr0UtAtvKlb-4cV_PqHzQt-Icd6uNQWqOYdsFMhn1krWQktRJ3KotZ__skXBG0A7HBkh4BZja8LzHE6BZV07DWbKNHklfNWPAwSvzPF1V6v-cbOz-WVKay4u-8n-_emZqYKzSGwkONCiJuGZPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MF0FlQHq-lI46pRCy_cCWtP3zTBM0h0Yi93-2cNI0n5Z-BFi_g54a4GOHyOsF4Wz9xpAzGD43-m1CLnGqulJOU6Nf5mL2h8Ir5jt_wiDUTMNQPOkKsOfQVrye3unutjBoltklYlWutPYoifJKP6IaAhH6r0WlYCGxtEH64MFBPE7_AhGW4wuF4lGctYKCrxX-jHI_GPwKEKpkLpt4LrqpNjRt41JfZQSBF4q75PMD8IN0n96C3bI1ftvicW9KSpf4CcROD0bp8iD87CYOBmWdZF0MtwesbJRFxgUra9Unt9qGkew9JiIpWNc1jT38z613YL_Op-RTkXmtPNzk7dY5A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
⭕️
🇮🇷
#فوری
؛وزارت امور خارجه ایالات متحده:ده میلیون دلار برای کسی که اطلاعاتی درباره رهبران سپاه پاسداران انقلاب اسلامی ایران ارائه می دهد
احمد وحیدی/ فرمانده سپاه پاسداران
علی عبدالله/ فرمانده نیروهای مسلح (خاتم‌الانبیاء)
سعید آقاجانی/ فرمانده واحد پهپادها در ستاد هوافضای سپاه پاسداران
حامد لشگریان/ فرمانده واحد سایبری در سپاه پاسداران
مجید خادمی/ فرمانده اطلاعات سپاه پاسداران
⭕️
خبر واقعاً دوباره در ۲۴ اوت ۲۰۲۶ در حساب (Rewards for Justice)منتشر شده است اما تصویر قدیمی است و بروز نشده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70544" target="_blank">📅 02:53 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70541">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=diLYV4aYPW9oF50mqKmFFPWhYfOplQT633rF7jcvhVFmQQWH5yLO55ATli-fpfn0KYl9iqaXBggbZZnIFvcf1ACVSn_gwH_ErWJIb4yeVMf4vUjuuXaBTVNVERB_zyGg6QHrBmZ1xeFdls_cFAspHjGCX4b9pVxYxuTZPorKYwWaZrlxtYDbm_HwSEQ2RKbZKT4YWnVUfw2E80_5CqwUrqJ5Ai-zgwt4L5vh8lU9sGyVfGvDXJJdkjwwI9Yn4K_aCcTRvxPHZeXivX0bIZKrMezN44KRk5HPCbkcSy8A9TgmZWbUo7v287YnsWISWOK8aNXmib-imBe_tEfWPYJb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4748f1f410.mp4?token=diLYV4aYPW9oF50mqKmFFPWhYfOplQT633rF7jcvhVFmQQWH5yLO55ATli-fpfn0KYl9iqaXBggbZZnIFvcf1ACVSn_gwH_ErWJIb4yeVMf4vUjuuXaBTVNVERB_zyGg6QHrBmZ1xeFdls_cFAspHjGCX4b9pVxYxuTZPorKYwWaZrlxtYDbm_HwSEQ2RKbZKT4YWnVUfw2E80_5CqwUrqJ5Ai-zgwt4L5vh8lU9sGyVfGvDXJJdkjwwI9Yn4K_aCcTRvxPHZeXivX0bIZKrMezN44KRk5HPCbkcSy8A9TgmZWbUo7v287YnsWISWOK8aNXmib-imBe_tEfWPYJb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرچم تکون دادن ترامپ در رویداد «Freedom 250 Grand Prix» در واشنگتن دی‌سی، برای آغاز مسابقه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/70541" target="_blank">📅 02:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70540">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xsr1ZB05nZ1JLJcXk8RLURm12EZIPLhDk-MXGcPv7ugPtyw-M0CuaBijR3swyJpxte7sGd2nlxUX_xe_nW70lPgkfvi_NUMf9f2U8t5GaYbQDmJrbkB5JNEu5YF_vVKXXhvUgdHI-baA206dFI-BU4ul3I_BCfq4_IK42FvEHPqcCs1LjW2hI2_RMcNzh4KGtDMexi8om8dVlwFDVylfWDtaaR1gwP5DUDfE4rPb68gm2bt9tn4lHi7VeItEdTKmhRWlETRY1fGbXgoeO5Ro4BCjLgmQV7zcRQ37e_i0qaT3efgF4oqnQfCSNKwmk9TaO1wfsFyZ4E3O9-mea5zmaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
سازمان عملیات تجارت دریایی بریتانیا:
ما گزارشی درباره وقوع یک حادثه در فاصله ۹ مایل دریایی شمال‌شرق منطقه الشیشه در عمان دریافت کرده‌ایم.
یک نفتکش مورد اصابت پرتابه ای ناشناس قرار گرفته، بخش موتور آسیب دیده و کشتی از کار افتاده.
خدمه سالم هستند و تاکنون میزان تاثیرات زیست محیطی این اتفاق مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/70540" target="_blank">📅 02:36 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70538">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6611759db.mp4?token=FuC2ry9r76OZr5JdABEkj8mWOsbYSiw1_b2CZaTr_slSJmvKdyv7DsVQU9uXDhGyY41f1ehwQLaL8tkYhr51xBlmw2r5Q99GDHJNiT_1p0tswEEJGDrhSQlIqCpWDVjiKN1txXMTTTB8kLjufvNLjmSLHkeBC0lKF3qTKf8oHSods73rN2GQDnXxq3gMjSgyjB3k6EBldGe6Bxc6lPOZSUUiZko1hrstOnDs4d0zNvo1Kuqf53tO44LYY-phdSTnsBFTeEy3MBXGmeYkKudabk3Mgc3vmNo9-CeTQBs9TU8yTEZiDI-Kf6MOftcMdkc8HN6NRNuEo3faDVy0URPPig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6611759db.mp4?token=FuC2ry9r76OZr5JdABEkj8mWOsbYSiw1_b2CZaTr_slSJmvKdyv7DsVQU9uXDhGyY41f1ehwQLaL8tkYhr51xBlmw2r5Q99GDHJNiT_1p0tswEEJGDrhSQlIqCpWDVjiKN1txXMTTTB8kLjufvNLjmSLHkeBC0lKF3qTKf8oHSods73rN2GQDnXxq3gMjSgyjB3k6EBldGe6Bxc6lPOZSUUiZko1hrstOnDs4d0zNvo1Kuqf53tO44LYY-phdSTnsBFTeEy3MBXGmeYkKudabk3Mgc3vmNo9-CeTQBs9TU8yTEZiDI-Kf6MOftcMdkc8HN6NRNuEo3faDVy0URPPig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
برخی از کاربران فضای مجازی مدعی شدن امروز برای اولین‌ بار جایگاه های بنزین تهران با کمبود بنزین مواجه شدن:
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70538" target="_blank">📅 00:50 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70534">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jsF9oOW4go6hE0jXbbvtOtsA16e7LIJ0tWsKMTKaTQZqJw_Jgk7jsH3eKzWA326-Rg37jg2xMRi7UKZ3vBxx3EHJm7cqoF2WosKcyBW8F37r_SvoCIq_2wKOCyLVyiuKz5g5KJ5LzgWbnhAzCUNWh0yeOoinVtykFWrhKZdHHtexrlOuSSiWcdgrOWihAJNaq7_2snAs7lxUkEXZH6H80x4JnuuCM7bNP11scIjbAgoaBNRbGnnsksHCTP1ZpOEJKru50-LQndGlD_xlc7-rZc1R2YYX81lDEe5YTsNN8_sZd8g1anycSksJLMT3KLOEYP6UkBNVKBXEGUsIN9R2Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=l502aQh3cy8yNkDExIVmqPLHjb-pxeNKLBk-NPvDZmFrMrXiF81TaPUFW1jtHZ_XdsvBayn1K2XvblQp4b25P1u63TKPMmRws-W8U2aNDuXfFDVdHYWqWdl0p_3MB5hXKCjFYuUkI7xWYztdiGhwNSK9PmZTIPwiQ1z8sqEd6xxTAO2owqFYrp_NNDdnhw7N4V6_vehUtB2cGayfzo791YZ5KhnBGJH56LcBg-kr-imkFeG920Hcif_IC4yM_yQtePy1iZ3igKyI_UWQWE5p0GEyvuN_Mw0ZkquHMhJWGDq7jPVbidsLi-jAvggKbn7MoRnLSn9xGJRiXBp9CBjegA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d54a3f2ccf.mp4?token=l502aQh3cy8yNkDExIVmqPLHjb-pxeNKLBk-NPvDZmFrMrXiF81TaPUFW1jtHZ_XdsvBayn1K2XvblQp4b25P1u63TKPMmRws-W8U2aNDuXfFDVdHYWqWdl0p_3MB5hXKCjFYuUkI7xWYztdiGhwNSK9PmZTIPwiQ1z8sqEd6xxTAO2owqFYrp_NNDdnhw7N4V6_vehUtB2cGayfzo791YZ5KhnBGJH56LcBg-kr-imkFeG920Hcif_IC4yM_yQtePy1iZ3igKyI_UWQWE5p0GEyvuN_Mw0ZkquHMhJWGDq7jPVbidsLi-jAvggKbn7MoRnLSn9xGJRiXBp9CBjegA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این خرسی که وایرال شده بود مهمون سفره کوهنوردا میشه
متاسفانه رئیس محیط زیست مشکین‌شهر از شکار شدن این خرس خبر داد
💔
شکارچی هم همراه ۴ لاشه از حیوانات کوهی دیگه دستیگر شده
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/70534" target="_blank">📅 23:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70533">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTX9EJn1KqgiMd4r5FWKwycrxd-JBgN9-BxQiBKxiWZHm-i29QJj32fmGzC3bU7l6sNzWWkWdIw4VuL0nsMDxGb6cGSI50VfsQOwzgEI-H-Wz-J6GsdNUdyuldmu2eOjtpff2TJ1w5YmcpteVR2lViJmbeXQ7y4LW1fmXrba26kQE_vqHc5kQORLVf1T73N-LSH-XE54vwdAdp9C3Cj-2Ntk9ii5aXswo2YIKc7lNlR1smS08AcwhZni3d9LVyiYH-fN6zUpgcN7hQmlNMW6xsQ1eFXPemFo4zeH8CSFbhI2NVQ2YSlMaEj8reElP2UUp8wresJtxQ_Z-xuC1x6Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
به دونالد ترامپ، رئیس‌جمهور آمریکا، و اسکات بسنت، وزیر خزانه‌داری آمریکا، بابت تحریم‌های جدید علیه جمهوری اسلامی تبریک میگم.
شما کاملاً حق دارید از این دیکتاتوری سرکوبگر و کسانی که به ادامه اقدامات تهاجمی اون کمک می‌کنن، هزینه سنگینی بگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70533" target="_blank">📅 23:13 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70532">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3bcc93470.mp4?token=SyzfBPnTuoFt7bcbrvbrduhUQy9e_5-Gtbbim4dLKUS2239YnZ4Kmg32NlLyUD9tx5zW6U1WEvBmJXSncieTlujjZogq7dIADtmihS_8PCwXfrlAaUk_7c7C62Q-rMMkKOwUcR_7vfgJuGbsmhhgJhXSIYNcyyk8cKCx5LtWxxhU04JX-NPfj8mrhvZdke-roUcKKSJCl-pD09Ajrkqjwg3W8c8nMCoIQLsCCMlEliKvvkgxX_y1kFUyP4CHQ2BBk862jekgkfbtqsNXvH5y7PEiuJ_qeIBzBRuLB2lGWNKqqs_wFFKrUQuUMnkP1Qr4RqhNvJH8TmDBHEeu7SNfdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
اوستاد خوش‌چشم :
جنگ بعدی تو آبان و آذر با بمب باران شدید آمریکا شروع می‌شود
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/70532" target="_blank">📅 22:32 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70531">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با این کیر شق شده‌ای که من از اسکات بسنت و ترامپ می‌بینم، مطمئنم خیلی زود دلمون برا دلار 200 هزار تومنی هم تنگ می‌شه
#hjAly‌</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/70531" target="_blank">📅 22:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70530">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=alEAk3wumMHPfWd45QZHKJHKuXgkuLaarXpZ4uz2WrK4Gfi6Fox8zYG7gEx3lH1Ln8giz6uGivOzuB2lJWio_X9Scek6IdGJGrtkYzj-wIdEPA1HRLCI4d6SXucmUVpUNgQYM-RKJMgsU5fQ-Fh7Vyaw18fThmS9_Dn5Wn9KZui_EqaemElhtMc2F6uffQXCV3xdU3qpoJM7zwohHP8xSFSKS_vjpCxsJip-MoeiiqxAw8NizfyBoM4nuPWf5C9XLqw8N9ZWMPb0Et3a92ein6JcytRkNqFL7zS7gQup2ZtZOLE_EBbZvsLVorDKyDAAmrQUfb0Z7vVtLFhGkvRMqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4eaa4f9b6.mp4?token=alEAk3wumMHPfWd45QZHKJHKuXgkuLaarXpZ4uz2WrK4Gfi6Fox8zYG7gEx3lH1Ln8giz6uGivOzuB2lJWio_X9Scek6IdGJGrtkYzj-wIdEPA1HRLCI4d6SXucmUVpUNgQYM-RKJMgsU5fQ-Fh7Vyaw18fThmS9_Dn5Wn9KZui_EqaemElhtMc2F6uffQXCV3xdU3qpoJM7zwohHP8xSFSKS_vjpCxsJip-MoeiiqxAw8NizfyBoM4nuPWf5C9XLqw8N9ZWMPb0Et3a92ein6JcytRkNqFL7zS7gQup2ZtZOLE_EBbZvsLVorDKyDAAmrQUfb0Z7vVtLFhGkvRMqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
ویدیوی وایرال شده از یه پیرمردِ حامی حکومت که به طرز سنگین و عجیبی داره پرچم تکون میده:
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/70530" target="_blank">📅 21:53 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70529">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9839729319.mp4?token=owRLGUwQC4wggMmuk35MtxzNzXdCLDJF8c9JHOSwQfEHlJKdmLk6Octft5_wM93Mitiwz_uOIoYuozWrdFt5heTL7X2O0luRO1-4L8WbS3ZkTdJm6AVLsGnVJutDjVibGpXueFYerGgR54kJG4MmuPh6-L2qWJC-ELcXHFwW9seR_ya67zYCScXZ693uKglVEvw-SgvumodT0mZaNR6OEEtv0uo8jsL50AQm5_W0kh2voHZeXt-Sn4Zu0hNlidCIrdKi5HyWpEK3fUU4pwAKfNrKtvHbHPn6oJ-raPSm6BOpczuDr-5LvEE_Az4V-9-JZBcXQdu5qNMaqone2ZAbJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
«بِسِنت» درباره ایران:
کشورهای حوزه خلیج فارس در طول سال‌ها از سیاست مماشات با ایران چه چیزی به دست آورده‌اند؟
زمانی که ما ایران را بمباران می‌کردیم، ایران کشورهای حوزه خلیج فارس را بمباران می‌کرد.
سیاست مماشات در قبال این رژیم کارساز نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70529" target="_blank">📅 21:09 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70528">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fd4a88095.mp4?token=GgkC9dej4eP5sN69jTMJIkgUt6kvKJjDEk_Lpv970v7ZZICCWayafqOYnHz5QnW8lrGFQmPbHJYF1a2v9Iqn5lEgOn6QsmO7tyLf0ebtYYAcPEsya_QFzIAUVKuGzeHSBJybWwEhr_32yfEuf1WUYXhE-dQI4YpQ-WS-ntLdR_zRLasZWdLWilcI0f6Cspv51FOjLo5uNYlxufZWChwMSqPVcZFKJWjxgunVZIZAAfINnNqmD_6VYt2Mdwefbjk3ljsYyclFEivZKPvbaJ_iFtzCSwkYVLiaJafcBzQSCrg6GvRnUoeqt0J6d7MVrPfhVc0MaGAvZpDYaSmHWxlOCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
بِسِنت درباره ایران:
کسانی که در کنار ایالات متحده می‌ایستند، از مزایای شراکت ما بهره‌مند خواهند شد.
تمام شعبه‌های بانک ملی(ایران) باید تعطیل شوند.
🎙
خبرنگار:
گفتید ترامپ با رهبران جهان تماس می‌گیرد. او با چه کسانی تماس می‌گیرد؟
🇺🇸
بِسِنت:
ما نامی از افراد نخواهیم برد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70528" target="_blank">📅 21:06 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70527">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7d89159ae.mp4?token=vGYqnXMLm3XJuf1DuRajFOFPAeqkQKgkN6Pv8_5eWe1GiXW5BNoV_ZXuCt9T_1MTTcW3URK65cqa1Qz2nseAzrnjX8BJ9fgIckqSmK2N6jJnVHRlU1BebTdQbSoLcvtyUwGCqMDAHBrinssz0Iira_BJg322thIbtRNUnA-mCRPNCaXnCmmcU7FGhZrCIeBJHYzCwhWdbMQnOBy0hpvPnZlifFU6huAYx4Svex5QQUdbFR3WzH9AYJXhqxZ5WehC8voyJv-CCaGN8akA-8uzDX4v6ew1JZ3zJ_HlTjkU3U0mlDDX2FyTKeaGMI66-LOLI7YrQ8RPbdMqq44jbPm8RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات «بِسِنت» درباره چین و ایران:
امروز می‌خواهیم به صراحت اعلام کنیم که هیچ‌کس از دسترس تحریم‌های ایالات متحده مصون نیست.
اگر آن‌ها تراکنش‌هایی را تسهیل کنند و بخشی از آن چرخه‌ای باشند که نفت ایران را به پول و ابزار سرکوب تبدیل می‌کند، هدف تحریم‌ها قرار خواهند گرفت.
⭕️
اکنون زمان آن فرا رسیده است که رهبران جهان میان آمریکا و ایران تصمیم بگیرند.
انتظار دارم تا پایان همین هفته شاهد اعلام خبر مهمی مبنی بر اعمال تحریم علیه یک مؤسسه مالی باشید.
🎙
خبرنگار:
شما این وضعیت را یک «روز دی» (D-Day) اقتصادی توصیف می‌کنید، اما «روز دی» صرفاً تهدید به تهاجم نبود و ایالات متحده هم برای آلمان ضرب‌الاجل تعیین نکرد. چرا تحریم‌ها همین امروز اعمال نمی‌شوند؟
🇺🇸
بِسِنت:
چرا باید بخواهم نظام مالی جهانی را منفجر کنم؟
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/70527" target="_blank">📅 21:01 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70526">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/155ae6e1ec.mp4?token=OSlSMChp0AEHnrqammOVsoaWZI-fJs_uxPI-ZiHDK2PktBc9sPjEpHewqsjudA88j7tSJwG2U-Bze6IYwEt9QdWNSmXotcPEuEbs2YNcRJCZ5POtCMbstPdDxTVwWym_1NWAnDX2wn9GQIvgvPNdi06QqbSTjgSlGHiLJxXkky6SBuAFR4cmExaxsaS_XHAyJuzPo2RINdLpfo7yxAyKSsdiu095AOZGtu_6xzWW7sACvOlDdaN_B4YFD761TXwvI72kY1WgV6MDSYJvkJWW4A0QW6hu7qP4P8NQJEj1gjkrtj0DmYyUYCIj9Q6noayHTFVAh2J88-gixewr0KtnDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🇺🇸
«بِسِنت» درباره ایران:
⭕️
خطاب به سربازان عادی حامی این رژیم:
در شرایطی که پرداخت حقوق‌هایتان بیش از پیش متوقف شده یا به بهانه تأخیر به تعویق می‌افتد، از خود بپرسید که آیا فرماندهانتان کشور را به سوی پیروزی می‌برند یا نابودی؛ و به یاد داشته باشید که دیوار برلین زمانی فرو ریخت که سربازان عادی تصمیم گرفتند به سوی مردم خود شلیک نکنند.
⭕️
و خطاب به کسانی که راه را برای تهران هموار کردند:
بهای آزمودن عزم و اراده واشنگتن را دست‌کم نگیرید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70526" target="_blank">📅 20:55 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70525">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b91fbf3e30.mp4?token=Zobqe673AHLdBkI691QYRPNw1RlblKm1KDKpFlYuRvB9QGNc_WOoJDNyA6gxhf96AOjR2OKkv-xNcgrx4uNkTOpI3vtBFeTgMun7XV2fnZLMwa7YTLb_bY_BvMaGqOmlykyETrwOrK4SKvLs7EMqxHmo_q5bpob-dTjA90g5He_-WCHsKxiH-8DD4RE2LDUIyBMeoR-u-nwp6wWqbl0QAFomrcsAYGEgw0c66KQOpFhuCovvLea0rT6-YxOs--tAMIip_X6tP0y-c2vVc33YN50lt8nr027ZKtYRSYiUiP8dkRXJl45ioaEjSvig84uhemMmPEQ6RSb1qdWnOs5hQg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اظهارات بسنت درباره ایران:
از امروز، حلقه محاصره را تنگ‌تر خواهیم کرد و تمامی منابع درآمدی احتمالی را که بودجه سپاه پاسداران و رژیم ایران را تأمین می‌کنند، مسدود خواهیم ساخت.
ما رویکردی را با هدف جلوگیری از هرگونه نشت (دور زدن تحریم‌ها) به اجرا می‌گذاریم.
ترامپ با رهبران جهان تماس می‌گیرد و مشخصاً از آن‌ها می‌خواهد که تعاملات خود را با رژیم ایران متوقف کنند.
هر نهادی که به نمایندگی از ایران پولشویی را تسهیل کند، از سیستم دلار آمریکا حذف خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/70525" target="_blank">📅 20:52 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70524">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75070defdc.mp4?token=Kci_MmMmxUbKNGPie34aw-Y1tmwrGJhu4PxrT4lLDK4RoEz-zX95iF0HNyfV0cxahfk2jKA-BJVx610VkWdqTIikTnpJo0i8HOG7mWgTyHpIGJAW3HpVOM4kzVCcShY4zTXjkgAF88WyKx4yTfA7c3pqGSdfMCRmTaUpfiesmeu3qmlf9EPLPIHInCtXJaoVOV4OccireDzbTr9QfGmQlQNgMP4jtYkOMfUOJChSzUdiISJEx9M9aqn16BCd0HZ-w-xTrjZWDzA8A84qAFPcbOaXjVEirNeC_WGRn8_iayQ6hk9818F6y0DUVSLFV23AIJ4jXy6VtA_dVXaQKvt5aQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
اسکات بِسِنت:
ما در حال آغاز یورش اقتصادی علیه پیوندهای مالی ایران در سراسر جهان هستیم.
هدف ما قطع تمامی شریان‌های حیاتی اقتصادی است که این رژیم ستمگر را سرپا نگه داشته‌اند؛ تا زمانی که تهران کاملاً تنها بماند.
🔴
در دوران ترامپ، آمریکا دیگر صرفاً تهدید ایران را مدیریت نمی‌کند.
ما در حال پایان دادن به آن هستیم.
ایران دو مسیر پیش رو دارد: انزوای کامل جهانی یا مسیری به سوی بازگشت به وضعیت عادی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70524" target="_blank">📅 20:49 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70523">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b43c7e4e6.mp4?token=WnVq8hD2cs8SR5eKhd-XMF3xtXeURlea8FerYyDkMh8iaV4uCRXF1UhMC6PMsqcxFX8kf4X3DfiD6Om3NQ6lSX8-gy3jTP7WfwXrbP1YV7zaPnQ0CVmjyEAHDYRI0ziyUVakp6OF1M7gXtEzn2jyLuQtMUUzLrN8uxYs8Y_3t31MuPp59WSE3kGCyO1Wew7eAYbpp-Pijj87gHaWHyY_9E7mSEDcDGkhzWMJQeNSiflDkuW408v6UTjFn3am6OA2x7mDrcU8cFmX8U8QOPOzQsI_jAx7R1bVnscfK5U9Kr11zx6UvvlBS3w9OWh6dJgUBY49_wSmqQcK0lQETNwW_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
اسکات بِسِنت وزیر خزانه‌داری آمریکا:
امروز، وزارت خزانه‌داری ایالات متحده «عملیات طرد اقتصادی» را آغاز کرد؛ کارزاری بی‌سابقه علیه جمهوری اسلامی ایران.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/70523" target="_blank">📅 20:41 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70522">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YhgBs3Oh7QLI4D_yTmrA-kljnc0JJjQ8fgPaEkrpdzho2WV6aAR53Tv-aQSmuoHiJrUULbAQ_y_UF6jfuD2t7V6hSKP_VtbIa9g7hEcJ6K7GUSeaxuSarm5DGGqILqqj4Le19xZuLSrd4KUFKfylA_PjFGTXvQ3qmjFjddBMxH_3NZ_AnDyrjlFfLlhmmcfiE_qqrBWY9FbbKLs6zm_OpSqO_7keegINA9Zi1p2C16QOh--ueIMk3riqe1ZFLN0BcJe4F1GwRMzIfgzID75G9iyJNm1BVLgL3L8xysyO4D9ILYCePfUvga8CN8034DnLuiKFGOoIi7wuGrSm7oHvug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو:
ایران تلاش کرد یکی از پسرانم را ترور کند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/70522" target="_blank">📅 20:28 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70521">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C8ajnqVOT_DERhRlJP0KeMsGL6y6mABoZAAcQiXl10S82sQjhF9Hqft5wYGjnllXDPZ2JeavWHHjPDxjRzhUj-Oyvkg_p6zPoK9NRH3kdI_oS-k6lcITph5T_aEOA5o4qrvvvWB7sTSxHJopE1G_jnQA6GHKPoisxgg6rzWkjn_takgb0SGMrrcemwVJtEuRbwD9G0i6gflUX4mbscF6_zpxASP8CqAyDD_XbJJzmM6M0be4pYST_DbMporbO_XMWGeHAZL9jFC0wieHCA3qC7wGBc-foz1SxtZLMzJs1GaEilbtDPOjHO_Vu1Ycn1ayKN6B7NjAKQC5wknoy0gtZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دموکرات‌های چپ‌گرای افراطی با انتشار نظرسنجی‌های ساختگی، دیوانه‌وار عمل می‌کنند. آن‌ها این نظرسنجی‌ها را در سطحی بی‌سابقه منتشر می‌سازند. این اقدامات «عملیات تضعیف روحیه» نامیده می‌شوند؛ تلاشی برای دلسرد کردن جمهوری‌خواهان تا پای صندوق‌های رأی نروند.
اما واقعیت نظرسنجی‌ها عالی است و روحیه مردم کشورمان در بالاترین سطح خود قرار دارد.
⏺
ما در حال پیروزی بر همگان هستیم، از جمله ایران؛ کشوری که در گرداب مرگبار اقتصادی و نظامی گرفتار شده است.
از توجه شما به این موضوع سپاسگزارم! رئیس‌جمهور دونالد جی. ترامپ
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/70521" target="_blank">📅 19:48 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70520">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw46rK8WWMzOPhgqoPCdojDgJOqYdEUtWwO-YHH_IEcXBgeBls-rhyysSxJZ8Eqbuv1mBzE4CdJ8-5m5cCdk5YzXnXbq9GnMtTrtoj4FWlfKneYMsFDwPaxU_MAxHIHh4uVjZaam2Cs6ZvuYTYKztQ3UlkIthaII0IeagpQu12d8O5mOi9R7ZQuwcvHcSGIT9AKJmK3c5Pr_kKBvEEVCPp9lfNwZXgN0Utn6Tu0kP6XsBbsmLDHz3KpqfrkxqaOEcUpyz2OFsCaXBH1Nfc5SmJhlzavqPFxY8_k9O4C-6_3YDTmWtMLKDag7Pabk8cscwP1rNNCiK0PUbeV9QlW8ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
قالیباف در دیدار با عاصم منیر:
تعهدات طرفین در یادداشت تفاهم روشن است و این آمریکا بود که با بدعهدی مانع برقراری ثبات در منطقه شد و دلیل دیگری برای بی اعتمادی به این کشور ایجاد کرد
رئیس هیات مذاکره کننده ایرانی، ضمن رد تاثیر پذیری جمهوری اسلامی از فشارها، تاکید کرد: ما پیگیر اجرای شروط یادداشت تفاهم هستیم و این امریکاست که باید به تعهدات اش بر اساس تفاهم نامه پایبند باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/70520" target="_blank">📅 19:44 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70519">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=YP5Kae6IkRE7gr7Vgi5jlHfGwts1fix4jFNXHcuKJg48f4Yde-y9E1YMok9erA43OQXKFPV2M0DEL4UoYMH4DOJYhdEVimsd9xek20fuCSG69f9hBXcKJcHsG7ZVbDzbj8GvGl8UIMGxdpZCcHPB9vfyRyJiuh5KkCLHUYH8AYwe-yldPTepfDMmCrz1J5_NSz4qqvkohMsjlKUBoJWTuV036nFWcM7XnXrrprS1ISAYE0zhv8R6hlvrcq0SeTJqT3NNjF33RIRyIoMyrNyFeR28IIHN-OcHvKgDqeROjiXQqdi88HwP5w6MJoPGi5gieJ06BzRWhY-VYzURJbrMgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/235f69fa4b.mp4?token=YP5Kae6IkRE7gr7Vgi5jlHfGwts1fix4jFNXHcuKJg48f4Yde-y9E1YMok9erA43OQXKFPV2M0DEL4UoYMH4DOJYhdEVimsd9xek20fuCSG69f9hBXcKJcHsG7ZVbDzbj8GvGl8UIMGxdpZCcHPB9vfyRyJiuh5KkCLHUYH8AYwe-yldPTepfDMmCrz1J5_NSz4qqvkohMsjlKUBoJWTuV036nFWcM7XnXrrprS1ISAYE0zhv8R6hlvrcq0SeTJqT3NNjF33RIRyIoMyrNyFeR28IIHN-OcHvKgDqeROjiXQqdi88HwP5w6MJoPGi5gieJ06BzRWhY-VYzURJbrMgzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🟥
فاکس‌نیوز:
در حالی که ارزش پول ملی ایران به پایین‌ترین حد تاریخی خود رسیده و تورم همچنان رو به افزایش است، کاخ سفید آماده می‌شود تا آنچه اسکات بسنت، وزیر خزانه‌داری، «سخت‌ترین تحریم‌های تاریخ علیه ایران» می‌نامد را رونمایی کند.
ایران تهدید کرده است که علیه کشورهای حامی تحریم‌های آمریکا دست به اقدام تلافی‌جویانه خواهد زد؛ این در حالی است که فرمانده ارتش پاکستان برای تلاش در جهت احیای گفتگوها و میانجی‌گری برای دستیابی به توافق صلح، عازم تهران است.
همچنین انتظار می‌رود وزیر امور خارجه عمان برای انجام گفتگوهایی با هدف کاهش تنش‌ها پیرامون تنگه هرمز، به ایران سفر کند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/70519" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70518">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بزرگترین کانال پیشبینی فوتبال در ایران
🔥
g2
فرم های ما رو از دست ندید...
⚽
@Tabanii_Mafia
@Tabanii_Mafia
⚽
@Tabanii_Mafia
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/70518" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70517">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p7sUiLiWdj8rPDV0z8DwtXREwavzm1JfFkeNs2gM8-nkLfO6RaUWSCOGgv9mhOws_P8zok6ExiVM17DKbpWnYERuNlQixMcEg4h_nIKeWMEooK0gIZHKw4zSpNzyRiWLmwYX9KyHd7ejrFtT4_19MR363kQnIl9Umd7TTpU0OD5eSte4ogYRZByZPax42QdEHQKqyjLFQ2zPYJ458aZkaM57x5x2S7wy57XDBd1p2Gvtu_BKCndKPkxd_Vdlv0PS7bZYge2cr0pEiqMei4vfJvh9IbkaYy_jZh88edlZFte6zCzpeeKS6iLU93jqpFARj1rJ6kHmTilS7gLJEUorYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میکسمون عالی برد شد
❤️
✅
✈️
@Tabanii_Mafia</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70517" target="_blank">📅 19:19 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70516">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=D7-Dt3Pdn-IlBeqh71Ha8j9SiiBCymBkE-ahzhUN-3xoTGWNTyvd5D6uq2pBF5u8N4UIunyub6z7VZqGDoVEk0nNczb9AHd90m2oq_hy5qF6XD5YVeHUfLaHzRUi-lLdwMZaM-xyOT01lJ6XCDNHa7O70-zOgntLbMcFsu8PqnANFMnzJkZ8siQ2cH2zrVLhThH1HaN-uAQmM3qBTMjYYsLhWxUx7WbYRaSjTlwumw1x4gCfwD_-ui8rQi-UkrOXPjFrTRcWrGRFPhxPK6xUa5EZ4FiQixzfW_BJYXzfKH_yFuE50Lk8-zwapoTYgIyprVIp-m1eCdkHyVTsCfcH7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384afb6ff9.mp4?token=D7-Dt3Pdn-IlBeqh71Ha8j9SiiBCymBkE-ahzhUN-3xoTGWNTyvd5D6uq2pBF5u8N4UIunyub6z7VZqGDoVEk0nNczb9AHd90m2oq_hy5qF6XD5YVeHUfLaHzRUi-lLdwMZaM-xyOT01lJ6XCDNHa7O70-zOgntLbMcFsu8PqnANFMnzJkZ8siQ2cH2zrVLhThH1HaN-uAQmM3qBTMjYYsLhWxUx7WbYRaSjTlwumw1x4gCfwD_-ui8rQi-UkrOXPjFrTRcWrGRFPhxPK6xUa5EZ4FiQixzfW_BJYXzfKH_yFuE50Lk8-zwapoTYgIyprVIp-m1eCdkHyVTsCfcH7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
محسن حاجی‌میرزایی، رییس دفتر مسعود پزشکیان رییس دولت جمهوری اسلامی، از قطعی بودن کاهش سهمیه‌های بنزین خبر داد و گفت: «افرادی که بیش از سهمیه تعیین‌شده بنزین بخواهند، باید آن را با قیمت بالاتری خریداری کنند.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/70516" target="_blank">📅 18:50 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70515">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a8609222.mp4?token=PjrhXnN8avCUWCiCmKitpaTEjJvTS0ajcnWUdJfLdouYJKnF-Rln51O-irni3hcAeIWINjYiJYgFfBn0pSzJT9ncz7YAJBvabU2Cuq1WGEbNvCcWsdKQPdiZQ3bABVO-Yfd6pxakXKAtX7n3mJ--0DDiykgtZjuHubmAJ9UKHAafpAth0i5cEnxmbJmaKvOKxJRDD2EzD3C3ZpUCb9dpLMiy7c2ksdR7Ct-whGJl2xt6el2ERHAQi2CEj4CJfM32KtTMtednUQhdjLPKWQev6Jf9mYAjWpcGFaaJaBQbOb4Nt2ShGVV9OXTIEUgqGPhb8cvCod8hNtAQkQ5LDHkDMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a8609222.mp4?token=PjrhXnN8avCUWCiCmKitpaTEjJvTS0ajcnWUdJfLdouYJKnF-Rln51O-irni3hcAeIWINjYiJYgFfBn0pSzJT9ncz7YAJBvabU2Cuq1WGEbNvCcWsdKQPdiZQ3bABVO-Yfd6pxakXKAtX7n3mJ--0DDiykgtZjuHubmAJ9UKHAafpAth0i5cEnxmbJmaKvOKxJRDD2EzD3C3ZpUCb9dpLMiy7c2ksdR7Ct-whGJl2xt6el2ERHAQi2CEj4CJfM32KtTMtednUQhdjLPKWQev6Jf9mYAjWpcGFaaJaBQbOb4Nt2ShGVV9OXTIEUgqGPhb8cvCod8hNtAQkQ5LDHkDMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دو ماهیگیر جنوبی موتور قایق‌شون خراب شده بود و چندین روز بود که وسط دریا گیر کرده بودن و دیگه جونای آخرشون بود
که ماهیگیرای عمانی دیروز دیدنشون و جونشون رو نجات دادن
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/70515" target="_blank">📅 18:15 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70514">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=iPoYwmfZELiwHzVHnRIIaSq21--gulB27pzjst_SocWjNFgIhLNqQAgK84kEc2M1DWUDNVOjscHsuHdigKPvQuDOzlOGwcyX09xflTddaKLBVZwx4l-dpMPFHurTfxBjnsDRJUuu6sMw9yforL1ZfT75tP_nAyCNUAAWDW9IsUNm8DpBX07SPcCOq51cYHOoE8niCs6uMXLpiFJKfwBEv9CfigpeACPTEniDUsk0I00fOFXoFVv86hs4H3TtuzvCYMtLb1akwzMwSd9kVXl2cnxI8wMgWMjblhzOIdo4zeBp7RwyG8tkIOr0kG3h6KlXkgDDg7YTRML03uTl4Ni7mg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/16a65d9f01.mp4?token=iPoYwmfZELiwHzVHnRIIaSq21--gulB27pzjst_SocWjNFgIhLNqQAgK84kEc2M1DWUDNVOjscHsuHdigKPvQuDOzlOGwcyX09xflTddaKLBVZwx4l-dpMPFHurTfxBjnsDRJUuu6sMw9yforL1ZfT75tP_nAyCNUAAWDW9IsUNm8DpBX07SPcCOq51cYHOoE8niCs6uMXLpiFJKfwBEv9CfigpeACPTEniDUsk0I00fOFXoFVv86hs4H3TtuzvCYMtLb1akwzMwSd9kVXl2cnxI8wMgWMjblhzOIdo4zeBp7RwyG8tkIOr0kG3h6KlXkgDDg7YTRML03uTl4Ni7mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
به تازگی توی بالاشهر تهران، یه رستوران ساختن مخصوص شوگر مامیا.
خانمای میانسال جا افتاده و پولدار اینجا جمع میشن و پسرای جوون و خوشتیپ هم میرن اینجا، تا برا خودشون شوگرمامی پیدا کنن
😳
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/70514" target="_blank">📅 17:31 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70513">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TUD2TcH6pdWzNZwdEzQyo1ZYA8WSrTuACrjf1_yfIbiqM3DRKH8Zviaf2BnwJ-p7w5fW2A96-b7drgtH_LUhFD623Lo_di4onJfwv61v5NKHj3DxZDiE3oPevbGKPhbPSiwjGGD_nXyUGsj3ST9JL7-lFXwIpE3Vx6QWt8mxp_nvZUT697mOjWWDhYwX_lLTShAo87GQ7WLOWcbUD1Zm2HjYZQ69MMATh2ZZaB7BCCXKqIvwKtpYia31xpTSWjVx7C-LdjeMbyus95es5PrBCnih5_M7MHU_r1DHSZAeEM-cwfpyIIvU2UwfZYwm411XVjKtOyxxdWzWE0r1IeqfIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
قطع برق کمیسیون انرژی مجلس،هنگام بررسی علل خاموشی‌های اخیر.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/70513" target="_blank">📅 17:04 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70512">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tNIL7j3GcWjzrvLO30J7XwQ1X36j3CftlClWA6umW8JhFY9C0eovsyP_zhjJtCO6fztbh5Q1ECAMsqkl44MT1WWqaApSJkpTSEa1C6I0fHhF4SHkz3Uwl0iwUe79DvUYAXRdnooe0G5VyHugcsHDCXL5M95JQrTivWIxj2TEyQmPaqYI_XRhYPbiVzFtA_9bKHXTf4L3uwJucKv0XVSWAHlVwN9yHkvB-Jj3BMChKOsB2q5qJ40rBgKgBkiDNc35m8ywF6JthkQHe-opSdr2VaK7HEV4Q7AoQRMSCp0htj_WgRE57Rc5ZaHZQ22mwcjmn98omjfV63DquVoMlShHMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ
:
ایران به طور کامل در حال فروپاشی است!!!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/70512" target="_blank">📅 16:21 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70511">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=vkE-htekdBOCHSk-5qg2X_sCce1JgpEPpHNSsCsqGcl6rf9nAdyhZwmf6r57dQ5W6k22AcKgP_MN4GC0E7eXHiZ9owYf7N2kGZBXZk1HCUoE1Rww1TdPin71IkAd3JXn2JNF0Ubk2ffL5j0M5dSJpP9k6n1JdJEQdVXWeFnEz2u91GGSWJjIL54yAXJO195S9oC4olcQkE6viKoYEO0iYmAlajosPD0OoRHEDQKq55xCo83ZiBAG3FJfnNRlzaxdzEd6GA-XJMH2lrEmDJKjcYJEMbply0mqLhjNX8U8Kftvr8Wpqn7w8g5_paCp-U-2KkM955wCSUyJBYPhNBXOiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98f13e516e.mp4?token=vkE-htekdBOCHSk-5qg2X_sCce1JgpEPpHNSsCsqGcl6rf9nAdyhZwmf6r57dQ5W6k22AcKgP_MN4GC0E7eXHiZ9owYf7N2kGZBXZk1HCUoE1Rww1TdPin71IkAd3JXn2JNF0Ubk2ffL5j0M5dSJpP9k6n1JdJEQdVXWeFnEz2u91GGSWJjIL54yAXJO195S9oC4olcQkE6viKoYEO0iYmAlajosPD0OoRHEDQKq55xCo83ZiBAG3FJfnNRlzaxdzEd6GA-XJMH2lrEmDJKjcYJEMbply0mqLhjNX8U8Kftvr8Wpqn7w8g5_paCp-U-2KkM955wCSUyJBYPhNBXOiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
یه واحد 131 متری تو ولنجکِ تهران :
131 میلیارد تومن
🇫🇷
یه خونه ویلایی استخردار 1080 متری تو فرانسه :
130 میلیارد تومن
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/70511" target="_blank">📅 16:03 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-70510">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=N3MIUQtGcEzcz2yoG2asOu_4XvTgauILLrLxDYChyQ5mbe7W3B2-kPxBtMEjHb0j2ca8Z1lW8kI_68NxjO7QsmaW7k5GAqv_ifYitPu55yatC2sFcItWb8n1PK4LYUdLr58YIc5fQHEmUBAm9tOwiS96mzBgLZ2mZCkjR2BZ2ZEN6RfaLEjPXs6lVJEqxz51OIIzEQwARftmfvo7ZmgszkZo6pXJqicjIVZm7zE4NcHb19AkuozqU3I4qd0cHAtUFpAEkjyPzE6hlF-TTuayz1hmwBSbMe5N_8AJM_gPP1rSW03bNuVPBnpMFaCXEg-CleSIPwKWhS4bzBJpB8KQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/685fbb8085.mp4?token=N3MIUQtGcEzcz2yoG2asOu_4XvTgauILLrLxDYChyQ5mbe7W3B2-kPxBtMEjHb0j2ca8Z1lW8kI_68NxjO7QsmaW7k5GAqv_ifYitPu55yatC2sFcItWb8n1PK4LYUdLr58YIc5fQHEmUBAm9tOwiS96mzBgLZ2mZCkjR2BZ2ZEN6RfaLEjPXs6lVJEqxz51OIIzEQwARftmfvo7ZmgszkZo6pXJqicjIVZm7zE4NcHb19AkuozqU3I4qd0cHAtUFpAEkjyPzE6hlF-TTuayz1hmwBSbMe5N_8AJM_gPP1rSW03bNuVPBnpMFaCXEg-CleSIPwKWhS4bzBJpB8KQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بقایی سخنگوی وزارت خارجه:
ما از قدیم شطرنج باز بوده‌ایم، در سال‌های اخیر پوکر باز هم شده‌ایم.
الان هم مدتی‌ است که ترکیبی بازی می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/70510" target="_blank">📅 15:33 · 02 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
