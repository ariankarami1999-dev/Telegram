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
<img src="https://cdn4.telesco.pe/file/tVvIYb0uPmhtpZQZhA0TuxHkrFuvq7hnLdweN6Y09tPv3bhlMKFxozD_mUTr1CzBCGPE6zf_kEM8v80eaD8VC2ZDwYa1mzQlIlMyfm_tCc6HKplrFIcvNe80l-5X1K3PyWnXXbs_aehWhuwtuYxNJG1xfj6yt1k_dttLpV8lCZMnJDrFULdW1CYo1AjXvRkyLXBUv-59NNR5xj4-6n5cwfEF54b6Qs9ySdvMokDO3G-dzZdi9SsafEDh_GiaC3Jo2A509Yi0o_RcpI89VvwIp4kl_Br9RiALw09OslR3I9ZnxvFc6aeypthor2lf5FdWL7sAKjWzVFJL2zKw7FaJIw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 207K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 18:14:17</div>
<hr>

<div class="tg-post" id="msg-81250">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خبرگزاری وای‌نت اسرائیل درمورد اینکه چرا دیشب نزدن و چه خواهد شد:
ترامپج می‌خواست خیلی عظیم و گسترده بزنه ها، ولی گفت یه فرصت دیگه به ایران میدم شاید دکتر عراقچی یه کاری کرد، پاکستان و قطر هم دارن تمام تلاششون رو می‌کنن.
ولی برای اسرائیل، این یک فرصت موقت برای ایران است که تغییری در ارزیابی کلی ایجاد نمی‌کند: توافق‌نامه آمریکا و ایران از بین رفته است و
احتمال دستیابی به یک توافق نهایی که در آن ایران تسلیم شود، صفر است
.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.29K · <a href="https://t.me/funhiphop/81250" target="_blank">📅 16:59 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1pxHqmJD6MwwhJ8j7Xj2G8QKtmL5QzF5KcC0FWFvkHt1jLcH2s8o4tfFpBhtmE-HCHRKVMsQjsOdfSQUcmGf0-ZBwXXnftN6pqCHnvJ9QSA3Y5XvGqoS7Jj5yNZLRfVxE-75MaCM3-AWj5CvFeH3y7jA1eAZcky2H_H_2f7ssTigSZU7qqz54AAyqJUx2Q-4G1ikeoIAD7Sa3RaqO5DXGwXPQ9Sog3ko9ot9DiPXpYv7atEyYqyT0YWCmQlQlMLr_96zIRe6BVV1KQ4Yttx52plLnv20zOIloJexX_QK4opNuvbni4_ICs2tI4sLDYssW5Xgzc9aj0v_TIpzriV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx2b06JK4b94jNvCnWQKAmJIG5wymvQZoSaJgfT59cYwqxzojnFsy3kATsY0r7ewEbqJopGiO5Y8vflJajFNs53bmATTTUk47-uwgNIfnM9CAccXMjvIeVSy7OOc32yPfcF-QH_ZTstJBd7WEbqAk_yip1EV1AvT-tgXDYddbysGjBxVEFyojwe93vD3-GFL-8_zslSOFZjQL_tP394WR74opc6mbGOZHuYu76l6N168WRgDZyX5zcD9J_b2g1zUUs0DpI2xSDxYJ521aySDH5D73QhX2ed568urUT9K70MZ4gSZHh902_cqx8RblNI0Px-4syfbIY8Twa0eibhM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llGCb2siPXW3fah_ghbYT4Ty7rdaAFFNsqcYu_60FPFr7GNWJi6R4kuWFxrmxPcofGUpXX1qzxoDyqf05qylgI0G7Rfakdc8hvmaVuuGzWcpO944HYb0tB9QzVcHxMJxmHh2JZYzyl1qCaqky2BJIddEfAqBnmTQZbYYcMhOEiAQG3XaHhO1fDZNewfafNa86HbIEdknccv6Wi92vQJBZ8swguNrJjlqOA1sP2hFZxRgiUwyK8Kfmgb7SyNQCLUd1KXpPZa5Uc8MMCH2J8KsOMwZLBPpTXnJ9WgqeHm9XmX5uyDTuF7Fq4XO9LvvXX3dqENCFdhF9q1NR9-ZyslH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/81240" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوکراین چنتا کشتی روسی که محموله های نظامی ایران رو حمل میکردن تو دریای خزر زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81239" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شهریاری، گوینده جمله مگه تنگه ارث مامانته:
متوهم ها باید قبول کنن‌ که آمریکا ابرقدرته و حریفش نمیشیم.
پ.ن: نه مشتی صبر کن رستاخیز بزنیم آمریکا این سری دیگه از خاورمیانه میره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81238" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81236">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D8ASZatpyJAaBPIYUFspnkjNz31mMLKMGox6vh6ramkZysLmyAivS5ZJNNr89YMGGigi-bn_lzkigEKyLJT0CND-wf0jlRVw9b17pOJSZHXoOCLLj4uSjsAo6hqkgqKze1BfnkxVgNmpw0V1UUhl22Kpf-BcS2WPWoVsFAL2qznX23diYa5YrEaKrJ2Dz45_k319ECyTFWg40IrID-PJnicQXeLPlYeINx0ktPgcpXDyzrPrK8SSiPAAfl2rALFw1_0in49kcYOFdGdm4HwLTphpbRffpi4Mdpdm7tUFdlccfVh-JjZXkppHLuRRmkATk_t2bRcPOUlnYhQGtP6_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdAse9oaBoLgpyh3F4HJchAyuodCTFaUHuOEAfMt3OCyqjtNkHg5JICFZROtKsGfyn5K_fciWWJzo6KwX-NHIWP2eyIxsMlHiipk_sI2UuO2arruhRhii9YKSVwvRcHKBcGeQb5f9gH8ef88AZZUDD9Hn2vZ34u5SW9Hn2LdKpp-womjO5f9MtKFrQ69xPFTWGDbb9mXzN0cp3GOA--ob7UqszdIJTTVXzpW3V11WHRalvgaW80NcLSdLU6q5FYsxk2IEZJ4FSyjQ_C7XWsS-gdfgax4zB7WUbCZslMXSukD9NM-U5zpmV_QnnJP2EOn8Ri3VvTi1Gl8BJV92IJlIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این اسب که فقط ۵۶ سانت قدشه رکورد کوچیک ترین اسب دنیارو زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81236" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هوا گرمه کصشر نگید</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81235" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ترامپ: رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81234" target="_blank">📅 11:38 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=TQzt8V7lp67gMNhOziCphPn22H-QOsiLzGo7XggXgcs5Lys83b6-lt2H6PpBMY3mVTO-UHHQUs5lusva73kSOtwY3oY_6A1_fzlWYOnYyjIkK8iPl0q8dqEAWXUKXP4Rd5K4e1uizt63qXx5pYqLY_tQKmwRkiNJWjHIJdLYngD39lCuM5f50qZLUa5bH6063ZncfCeGvPBlWQagsAvRnbQ6dyCklrj5G3XfCg4fH60MA0OKNinL9m0Gq-7n49z4yCrtmWSa-JyV_9EfsjfpAZOTSCVa6Ag1sRzgYE4G8EMC9VTXxmEhCsyducJtiwgKpVa0cGV41TYLzpjne-Fo1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c1e370de3.mp4?token=TQzt8V7lp67gMNhOziCphPn22H-QOsiLzGo7XggXgcs5Lys83b6-lt2H6PpBMY3mVTO-UHHQUs5lusva73kSOtwY3oY_6A1_fzlWYOnYyjIkK8iPl0q8dqEAWXUKXP4Rd5K4e1uizt63qXx5pYqLY_tQKmwRkiNJWjHIJdLYngD39lCuM5f50qZLUa5bH6063ZncfCeGvPBlWQagsAvRnbQ6dyCklrj5G3XfCg4fH60MA0OKNinL9m0Gq-7n49z4yCrtmWSa-JyV_9EfsjfpAZOTSCVa6Ag1sRzgYE4G8EMC9VTXxmEhCsyducJtiwgKpVa0cGV41TYLzpjne-Fo1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
ترامپ:
رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81231" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_cdde_jU7ONfCr1PrRAWKITpSk1eN84ZF-aqonFsqSkzbul767MmoSeAWUkRt9ucREBUv21el5dkl3M37Yw0_BDWQmrYBV_K2C3wHqFVG6KYhTdRaAO8e_xsC9CWEprSeibhREr00rmaAkr6qJJQcy07fOHKVpSG_HB4mDjX2C3tjOa7fdvEFW8y8PC6RYyxHdHk9erY8kFpAKQhaPUuP2sJHIPYulFkUiZa9338KLWxfsdyO6gObSmZ84AoH1MLxTD1K4r6Y5owTKyl9ndMzBHwKYsWEob-AbmoT1XHC-1hnTzX-BkY0PaGVVY_5_fJI_qLB-y3WGXtgt_5_RxHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پورتو
🇵🇹
-
🏴
استون ویلا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
شنبه ساعت ۲۲:۳۰
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پورتو در ۵ بازی اخیر خود مساوی نکرده است.
✅
استون ویلا ۴ بازی اخیر خود را برده است.
📈
میانگین گل در ۱۰ دیدار اخیر استون ویلا ۳.۷ گل در هر بازی بوده است.
🧠
پیش‌بینی آگاهانه، تمرینی برای نظم ذهن است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r3
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81230" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/81229" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw0ORU2o-gvHwTA_bQfu-LnIy7ScuyoDfdOcoEZcz2-DHQmqTGayqJ-pnjsl4ho-21hJUuaaUeGeSjEt_VaonCJC6fIFOmt6rOsuorltGXWTd0OoEKzDb9Zjt0UYZtX5QCkQBtab0I8nHl8iqhKS-UzabgHhcdIs6OsbXSrbJqEHTk755KXINxuAGppnZ8mG9rMWpkw5J17T9G7oBp1GW5Gtj-BKBN6AG3JatPPho5gXNPtj0cc8kt_Btf42z7mb24E4WfefRnD2c0fweyL7jTUY0ONWf1n8M5L6gFW89gDJGxDvZ0DDP8XrC56adD78gi3BVmJm5KY1pxZh6TQMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81228" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قدرت اول منطقه برق ما دو ساعتش تموم شده ۲۰ دقیقه تاخیر دادین چرا نمیاد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/81227" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چین حجم تسلیحاتی که آمریکا تو خاورمیانه مستقر کرده رو دید و رید، حالا خودش دست به کار شده و قراره کنار پاکستان میانجی‌گری کنه تا قبل از اینکه آمریکا حملاتش به ایران رو دوباره شروع کنه توافق رو نهایی کنن
علت چصه دامپ تتر و نفت در روز گذشته هم همین خبره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81226" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81225" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81224" target="_blank">📅 10:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0j9l6_otFjp1imVzkaObfEDTIqWA_dLEz_qfba9tFy21zc4-Oa_KuqRF86AFOdls3OKI7w3fVtK3JHAsH4o7Q3wDR6_rk8jLiGwAlttk5y-8eyho_4EWWtnZjJ8bx81VI-f0rilHzPt4oFu5XpfXYLeQjCmQ-vx4D7Ck8b-1jOEATlO97zYfVexKCz8JO5s_ExmPsUft2ojz3XgBQkGsMOsk3Krw8BxLSOgVxaWVcdGLKhzEp0q41ATBvFs1XAsGlbD-ArGkd95t-xI5Wf3XoD7YlyDCVuH4qeaJqfD_DuqAoLa0sDZyz2bGjhiqOraNDvOXgeVdR1MWA2LOfogKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#بالاخره_یه_پست_رپی
پست جدید ایلاکه که احتمال منظورش اینه که "پوری خارت گاییدس فقط صبر کن" ولی روش نمیشه مستقیم بنویسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81223" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHm88q0-PKmlxWMgR79cHG6xcSnRO47WJ8YQXSgpXoJ8zCyMSXsy3u7bPsf_HAJp_JfCeey8-VOIpZ7btrjAZrzDfkxnkkDJ-pxBWIgYB-Jru-bV3GiCH4bpPRQX3MNxqXpSr_hSv2oYDfHlMnj8-DOZJEartUOqe1fE4WHpN0LLVTOjxK4qAsEwwpxOK4LXSwpuGUM7WDhmzGbHsfqoJB6tlJGNrJq812ZQEskAoNZKY_imnadlKRcw3A_7ovb1A-Kk0jCLV1aoNhLsRMkwZY5Tw65e9Kp16q9sc49eGqfI8akTbEqMz2pZGwA_A9xO2gHy8F5xW4fqW56Bc7n9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور کنید اینا با آمریکا تبانی کردن خار عربارو بگان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81222" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این وینگری که رئال داره میخره از قیافش معلومه فقط برا کار تو مزرعه ساخته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81221" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لبران جیمز بعد از ۸سال از ال‌ای لیکرز جدا شده و رفته فیلادلفیا سیکسرز
تینیجرای ایرانیِ همیشه در صحنه، آماده شید جرزی این تیمو بخرید و مدعی بشید که از ۵ سالگی طرفدار این تیم بودید و بخاطر لبران نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81218" target="_blank">📅 08:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علل حساب اگه جلسه سرانی چیزی صبح هست لغو کنید که اوضاع مشکوکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81217" target="_blank">📅 04:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رفتم قسمت آخر برنامه ابوطالبو دیدم، بلافاصله رفتم هایلایت لوکاکو جلو سیتی تو فینال سی ال رو نگا کردم</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81215" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را تا اطلاع ثانوی لغو کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81214" target="_blank">📅 02:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امشب آمریکا نزد، من زدم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81213" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب آمریکا نزد، من زدم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81212" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عربستان و یمن همچنان دارن کون هم میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81211" target="_blank">📅 00:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgy_1S48lFgCP-fPwzNl0NMrNkwHJjjvnJxDnoCaDjIwT8FH59FHPf1uShZcBMKTq0ZH7dAeDRR7KyeVmKwVKWEssnhXgenXukwhac3yPL47JcQDaJpW2jYDjV0NJ27uJA2ZWC9I8qr1lVeslqWJ1TuIQ_bR6UbAG2Na4cFxfEEyLO8Wq0j5xi_narZsnBk5kVDNbLru3VdxJ-uxxug1o_qVCzlnuCfzo-uRLGumS5eJ5JMZNgusd7A0sgGsSIEfbnoFXZTP8aOJ4-enmFsvczvZL7z1PuaNzawRHnJQG4ULdBT6h1JERI82eJ9oCkq_Npi67oLnaJJMFuwLkcqHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81210" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81208" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0Ykl6WWV7FtPRAVuJr3AWozaXKw-B7G-jJK7kvAYl-oBzntkDkB0JOkgQt8JtqvnTgKGDioNw8qk14nBoXUU2nR6vqVzC0lMZcv42tTfAg484IA9XYPuvo8oSaOjJB7DHIMwSOxuzkpC3xaJXGZOKtPhJs2yzsZZXOqafn-UtCuO8X8eq7j-uR2eU_l_-eQka7FtNWhNkDtADivpwnVJE4echWlcOMFn7UNeT_MDrkJYWJBY-8IdcnGZ0yvZOWDGkcL7bl-jb2wFMb0wU7EQeSQoy3OStn0Ki7-ImgXsgviFba4IcoHD6tsaBEOVtPjZkNP-IRlyHrUPj2EzJRB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81207" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:  مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81206" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عباسدرمن: تو عراق بهم میگن عباس بَطَل، یعنی قهرمان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81205" target="_blank">📅 23:04 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81204">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=lWLiia7Yfag-pFHTSvEXgNWpqlB8moWWgVY0e8Gglq34uCWLA9EmOsm5kjl9oboxgYj_PzqsSdIF2appmBVBWhWzJqIRNaXmEFsBeL6JkWP6Sh1jirpfZvM2I6fP54w6W3kLglIJIJDdeG7lIQHoXeLWFZDrdxE2ovkP_xtyKL3XbIftCMEx9o-JVxWVRU4dEjJndWzFIRfLr8dvuNYEbeM0cgOlnBV6Whrn-AfQXQnak2WZwmmV7nToilZkMpxx6gO7Ekc9nkhTAXPXYv8ligsN0nVVx9HAwU29aUjMWWOg4UMVV0gzQG4OZWzVG5yYmC_pyADfi58gV12pV4Sabg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/842d3e3bd5.mp4?token=lWLiia7Yfag-pFHTSvEXgNWpqlB8moWWgVY0e8Gglq34uCWLA9EmOsm5kjl9oboxgYj_PzqsSdIF2appmBVBWhWzJqIRNaXmEFsBeL6JkWP6Sh1jirpfZvM2I6fP54w6W3kLglIJIJDdeG7lIQHoXeLWFZDrdxE2ovkP_xtyKL3XbIftCMEx9o-JVxWVRU4dEjJndWzFIRfLr8dvuNYEbeM0cgOlnBV6Whrn-AfQXQnak2WZwmmV7nToilZkMpxx6gO7Ekc9nkhTAXPXYv8ligsN0nVVx9HAwU29aUjMWWOg4UMVV0gzQG4OZWzVG5yYmC_pyADfi58gV12pV4Sabg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین صحبت های مرحوم در مورد وضعیت مملکت هم ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81204" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81203">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=sER7dlJF2HMAiRCGV-VsAM0pLrh1FU56bPEIIO0-uW0K-pr_ULZETfIUFeUDvqcqs52ouPRzam6UJQEstfcnJiLTr3Rv6m14GBYKKme-uoC3qCllyoD5WTSW-TdmK34KWtKXP1Ka42aFo6xK9aadB7x5Wb4VdSR0l4vNiiybnCuvu-3z6_JMtsk6R7Cih5CGfbpVy6cJKMCAZOe02P4NJOgYr0_gZVRDGCGr2EsKl9ngktrh8z_qEu5pL2rmSkPISHMSRPBx_13lCKm1mf10OVxhS35f6zszW_r6vdEG1zQrAA9j3zLa2MPtz6gr4DgasDRkffd7n-0jc6t5MVPYfaF5zOAzZLskq6YMfAnJsAWtzv9Le3Pnos9nEl4x0EPmDfJdZDPfk8zs4_IKN-WAbSeKxKChRHqqNHKWc9DSqVXcbQ-4PP8_IlREpOoTQf5rwQgqyhJSqG_goVRNXM2-vGwJa9FKVdt1vCQ08SstyCeoc0fbp8Kwr1R98TP0k5YfXqUEV5bSAl6uQyX4i_l_QbTAuKOyIDCtKLqLJDh8txZf1J7svRv8cGpX2PW7_n4GzyOfu5R70PwPvIM0lJLtpbsAE4xMQgyzTxeVfe6fKvF3312pXCRIE9ClezW0MHurwmrk1R5GAw-tAK6J5zWAF-8jjLjzV1mFevewTiKbD6A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb669ee556.mp4?token=sER7dlJF2HMAiRCGV-VsAM0pLrh1FU56bPEIIO0-uW0K-pr_ULZETfIUFeUDvqcqs52ouPRzam6UJQEstfcnJiLTr3Rv6m14GBYKKme-uoC3qCllyoD5WTSW-TdmK34KWtKXP1Ka42aFo6xK9aadB7x5Wb4VdSR0l4vNiiybnCuvu-3z6_JMtsk6R7Cih5CGfbpVy6cJKMCAZOe02P4NJOgYr0_gZVRDGCGr2EsKl9ngktrh8z_qEu5pL2rmSkPISHMSRPBx_13lCKm1mf10OVxhS35f6zszW_r6vdEG1zQrAA9j3zLa2MPtz6gr4DgasDRkffd7n-0jc6t5MVPYfaF5zOAzZLskq6YMfAnJsAWtzv9Le3Pnos9nEl4x0EPmDfJdZDPfk8zs4_IKN-WAbSeKxKChRHqqNHKWc9DSqVXcbQ-4PP8_IlREpOoTQf5rwQgqyhJSqG_goVRNXM2-vGwJa9FKVdt1vCQ08SstyCeoc0fbp8Kwr1R98TP0k5YfXqUEV5bSAl6uQyX4i_l_QbTAuKOyIDCtKLqLJDh8txZf1J7svRv8cGpX2PW7_n4GzyOfu5R70PwPvIM0lJLtpbsAE4xMQgyzTxeVfe6fKvF3312pXCRIE9ClezW0MHurwmrk1R5GAw-tAK6J5zWAF-8jjLjzV1mFevewTiKbD6A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنده خدا حتی وقتی اعصابش خورد بود هم ملت رو میخندوند
روحش شاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81203" target="_blank">📅 21:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اکبر عبدی درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81202" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDo4LJkZmghLTMMJ3DJChum_HjP8WSsRdCr0rT6INvEZIkA_0TZiRlBEL-OdcQmCRUEWSyvYqatF95urOsrhsuCWM5naAvyNiltub4bigWv4YJigcTBxAqQ0an8QIlcfkNQjZrI30wy1QQRldTVksGt5IPTTzj8fhW8vf08m5Vm1CclYELTkTirMwW_QV5CohYKuw5G4vStiSzD1Py56OaHTFv19CkoV2snwWbfgLkPioNscvUD0G60rT6-nRucI4hSz1-PvW3XZuYaUhoPQJ39O-tKGiXuGMkTJjzWX0w8zBKGLvK_lkXeUmBqjvn7ejbrytXe8q2apmNLLCe4qSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم این چه سمیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81201" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81200">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">تنگه رو مفت بدیم بررررره؟
مال ننته بدیم بررررره؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81200" target="_blank">📅 20:16 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81199">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZZ2Fp9aZJC9IMec1TdkLriaukv5gpcdcE1gOleMyCB7xpu8P2lqiisHBIt6gEtThrIKFVeROs9rKz009VMsMPq-My-7hWoKpoNLa_NXJ0_ep766gy2kWirlfgToW_2dVuxF8uwX83rxpEfz1rb0NXr4pt07mvlCShTX3TpB3yxdm6SQa87OPzMmWrDv1K2UOKwzpRsV3r_ssNKFT37k3z7yTcYsXqMh34x8z20k5oxYcXCRmt2DopTx3pmsvJ6o05JWdR69S0mMsqU27uR43GXRtJrh3yVo5ufSkhrBTRm_tePVPwHeM5NfwHofMzL_nnNPVUfqEhEPbProPjzM3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این مقایسه ها که خیلی دوست دارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81199" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pfIAqerd7f-jKfAH8GXggmBA7R4bp5bJlYxUJi-PXZdeTYD8SCH8Rg1ulpbmKPWtmEH5imSqAF4W9EBefb--2OMRSk4_8--eWDJcRUdix2BXU9X-si1V4hQSxgzOJ1RnwChaKqvBpJtwwTI4-KveoM_KJZju8eOUwT7o8oEhEuXtHErWGIT68Z3WgwasxCclLaEijDbvniAy-cxrDadvzhK3BGSweAQ08CjdfpdhKH3eDOTsjJ01-xoaIxJgpb7mH_aMkTztAAwBGeY0d2TvGN_y-mDUmnf8Tpu1w9rY9rEWGAT6uxA0YrWOyPCY-DRbTho7ujM896NuvpRe5fNRww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از مقایسه رونالدو و مسی توی جام‌جهانی که خیلی درخواست کرده بودید.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81197" target="_blank">📅 18:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/USFbPKfjsQKlATZtdeFjJCNwRsZAEPD700iR_agxNUeo_CpkHKkOBZLn4MS6YEyE_cPXqcFoWD46Vduv4BVuTtD2hB8JoZWU05-cCVc_eZsOa7vg5c6bM3F5hrmlIU4k2P06a7T7FxRVVzeiW4JI3-7NuOo40IFqpQLc6SPEEgpefqkPXCPRec7D9oEowAY0R4kYFTnXLz80mOmIY7wc5oLFWM9hrAH4HdoxtOv7InzXrjk8FEi998J5bgI_qpxOSdbEOCa25NotOap42k8k4NiEBcXMQl8wKyfHP7W_G9MghXF4MJBwY-R3jOeWRMJKgmzSRJ5PBbSOHJvZl6I9bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGkC-_M4i8ClB1ISfHePyp0jW6Smi_hrZckQEQuUUqXz-KoIwYnMapEUgdzGIKP93ngU5SYHDebEjJJpduqN0u8t9f-aDLdLhCXL2qWIiGL2akRR_4PqEbrXdUJOBAm2Wz-5q45jhIHsbNNPN_mahr1NOnd34vFFPxnfmJE_itqJVuKYHyrdffxVBZ-DQIt3Xulg1nf-Y9NJ6MFkA_GiqUIKB_j2gkhTNdQMVTMnNLJukseq4csuyhsHy8O2OnjaWkVOfuRHHE4wG8hP_ItK8JPajgC0vh0Psog-erlWlkYn3N1RKcw8AYr1xkxwxMJnoi91PTkKR0Z8lTciEK1d3Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مورد علاقه رامین رضاییان
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81195" target="_blank">📅 18:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">۰۲۱کید داداش بخدا ما بخوایم یو‌کی گوش بدیم انتخاب های خیلی فراوونی داریم، چه اصراری داری انگلیسی دریل میخونی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81193" target="_blank">📅 17:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dp4wV0EdmmPuCqcdTaA-7U22SC3B-eEcz4LhzJVwTT77bSba0jP6dp4t7MBVisvWXRAzUajwgxCBiwO1xeXXbeUhTLf61F4NW2HYUZe9EhXawpzriKATGkeyDVbpuUpY2LnVo2KnPYFUsWRegWD38mxG53ccK5aiOGPy8ptdoaTKEAnvYjAqQwBuorWpkC4HuEhgTN5an6aFBS0Oq6GoGBr_muHBssMRMCCMxMTxpDRChqjr2H2nBmNxv2dVzG0BvNe7BwQb8Q8LRr8EhJxQtLSaGe5QoE77tqhDpa6s5iENikmUCfCY8W8Fy_rvmsgsl2TeVZS_75WOuf8dZ87avw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81192" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJA6zMxcRwBqNQ0WzAFhsi93XQ-2Wu08Z2p6an57X7JBAnX244wQ-udLIKraJa92AmScKj0NpCgz66koIvwc5OoTLDs6AiGT5FEBQAJwf1Ss_S2pPlL7o_4PftElaN5FOABalqXupozsRsVM1ALYSB_QVdJfv5ypGc-2Gufr-ch7uMYd4DrVE8BugkR0K57dYVFt4bVnxFobYRTpGdvXm1lWpXF-3VhuxJA0x7MSUJLUH_FMWLYCVIDrmJ6VfwKlJ0de12oypQIxfPbNHGx64q97ualNpiytDeOweNSYKWRgm9bZk_KYgwfVpqU-xey6GUhn4EILjCDbal9X_wodCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین عکس جام جهانی 2026 از نگاه هواداران فان هیپ هاپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81191" target="_blank">📅 17:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meX49jVBd50010i1pikZU-3yDFTUNRS1yxDAepjTHwGGd7icVtCHpCgVF1UmyBCZpnA51DSRqDzzV_HdCr85L4THyrbmixydoFE5iPCvydG__k_0OP5Rtxp0U4Ic3W_2ymEYyoHAlzw2EhFmKh5-xJfwNsTkQB3wBG0EiCiB9ueGbaxTVXsf1HFiI04pZITEVx26cwVoc27EO5pYBlhba72A1IQx4KZvwQBIAHfT18MgqxkY-Xil4QTpF1CjAS2eYcdhnx36uWbSY9uMWWBOSl1JNYTxDHqbqlBcaiFSYcx6KY-n3F3psMiR47y_x_QKTrTHU2u0GqNOsRpmXJeTOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81190" target="_blank">📅 17:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tp8kXi6tXUr4AnkhBbZp5LO2IHF1zjjFUTUkbbUcl2Pgni-fWKkw-sysawNhlTS8VY1S9HKSvVq-R4UaChQcCRr4QMQlQuZh-VeVy1YBXvxTwB619gNl-vEfWDJ0Y7bz87SSOrzsPIa3jQbW0ZWZU0WCXI3uTBNuQtUDaGU20n9Sc1ODNauuUV_Hjqi-VUO3p1vhhtRbKEs5YgTNzUFPJQiQ8b1T8Nmr21LnrEdDb6kHQT6vgDl0xunWzIG8pmrMmRFLRYug-pSz9q4tlRROSEVgCs2IMTaad1U9phDzdSj7o3mI2qaNxiEpH_MUDOgFVwWGxTzr9b7F6SdyuJg9lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81189" target="_blank">📅 16:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsE8zOcK_yiZknJ645odXXB1p7V47YYl96mivRleuScQ34ZUBsBkkKu3WjlpJryRUpM4YYn1WFYLJxFN7o54KliyYPA1ckNv2W33tULigeEH1H_U-iMosmqtWbkU8b1VIsWzI4U0_wq0FD9RinlodBumtuRtfA43OAG6felmEUv6P05pz2yBdZODbUOy1c9XV-e2XeZUcCIsnyE2kJyKBz9OaXJXQxgPhQct-x_LAtoWKfDpVmsRFcWnA0nSq8nb9KKPBugGXqY4eaOzvK4a7eQpoXb-LKt1i3GnjJoSa1hitqBmNaNEHLQ8mPk52LmZ-nMP1Tt2S2WFMJPmCUuU9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس آمریکا تقریبا مثل قبل از شروع جنگ ۴۰ روزه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81188" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pQ-8c3s_jREDtd0PGrnrCAU19kgwdkjBd_NQXCeDrZA7m0f7KzHK5xECqhq_60z9LF7YCGtbNTTvW6V1q9DKlh_s0UF3JynH5b1JPdLEXNcYZqoKyDoRsk3IuGYjxmEdC0Lb0lmvTdsDfAIuO8UYRckwzKcQfXRxUxq6qqB8VS_z445GArWstFzG8h6dj86Q3Wpl_dGkCimOZeY5rwKlYD6DJVrC9ueEe-r6C1pUBX8szNiC27gd_f3cJS0uomkDsU2eueaDg5owP5r0p1QCrox38EtlUqEyCdKtTY8neF23CPIm3svHHKfnfiOIBK3QGyWzLrX71orww4-bfhcPeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81187" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اختلال تنگه هرمز قیمت نوشابه رژیمی تو کشور هند و بالا برده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81186" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دقایقی پیش ادامین فان هیپ هاپ از من خواستند فورا فان هیپ هاپ را ترک کنم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81185" target="_blank">📅 15:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81183">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81182">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت خارجه آلمان از شهروندان خود خواست فوراً ایران را ترک کنند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81182" target="_blank">📅 14:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81181">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUs_Zy4XmUxexW_BSd0eZWvXx0C8F8aa6LEAih4oC87nk7bKcoUyLOiYfPQc-no5XJoB9PaAl5QI4ArQXFDSlYckzNGRT2rlUqrjsjn-8TvO0hj68kj8VSBeL3nfbu4by8Hc2gV_drGQ67p6avCB8k8YBZFy_3iPy_XgWfWAARs4e2sA2zIciPpMsR1_KdTTRAa77oYnoe9vZmbdRSlLTUwuNj1dOj7TDZOJ1zmYX5aKRY9rTAWdke7MnG-fXKOM-OI73nY4nExV4AkUvk_c9h6RRoyC02KSm5q9BTlRhYTjId1QWHs6-0zr_Zcq0vYcaWE4Zh1ilGwFiG9aTQApVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81181" target="_blank">📅 14:09 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=WBAuMv-wXTO4_mZqe0uwL1CRgL8P0DTf-jg5f-6vqZ4hIKyuf2tuSv8wDVOkpx_6VBtqK0cgksgRvl0FcQodQjAG5s1jYdv1YjaFuRooRfiQ539GO7mEQ0Ln2AqpkqkUo6h7ZZVERe0X7PWhB6tmYYKEK5SLcU9yXsNTpcCaas8ujjgYaSQhpa-lnuvpZdDHTonArHY18ODZMuO0D8a4dBkDcRTvzMGG7nKVAaZ1kPY5naXE5MQ6ROR1rfmi3nQHuHE_QOt3_aRqmFRu5z_OAC4IgUjn5YbxSqKVWMu_caJpjG0vamJcE03fYFNh9RPtUZ4rb4UsewyhsGrv0U0i2A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=WBAuMv-wXTO4_mZqe0uwL1CRgL8P0DTf-jg5f-6vqZ4hIKyuf2tuSv8wDVOkpx_6VBtqK0cgksgRvl0FcQodQjAG5s1jYdv1YjaFuRooRfiQ539GO7mEQ0Ln2AqpkqkUo6h7ZZVERe0X7PWhB6tmYYKEK5SLcU9yXsNTpcCaas8ujjgYaSQhpa-lnuvpZdDHTonArHY18ODZMuO0D8a4dBkDcRTvzMGG7nKVAaZ1kPY5naXE5MQ6ROR1rfmi3nQHuHE_QOt3_aRqmFRu5z_OAC4IgUjn5YbxSqKVWMu_caJpjG0vamJcE03fYFNh9RPtUZ4rb4UsewyhsGrv0U0i2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خداوند زمین و آسمان را شکر که زبان فارسی را به من آموخت و اجازه داد آنقدر عمر کنم تا بتوانم این محتوا را با چشمان خودم لمس کنم.
🙏
🙏
🙏
(
معرفی بازی رومیزی نجات کودکان از جزیره‌ی اپستین و رساندنشان به بیمارستان خاتم الانبیا سپاه با طرح جلد کیف صورتی معروف دانش‌آموزان میناب در صدا و سیما.
)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81180" target="_blank">📅 13:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">یک مقام ارشد در کاخ سفید گفت که ایالات متحده یک برنامه دقیق برای سرنگونی رژیم ایران دارد.
«اطلاعاتی به دست من رسیده که بسیاری از افراد از آن بی‌خبرند، و من می‌توانم با اطمینان بگویم که ایالات متحده برنامه‌ای برای شکست دادن رژیم در ایران دارد. کارشناسان بسیار متعجب خواهند شد و سپس خواهند گفت که همیشه این را می‌دانستند. به سادگی، به آنچه اتفاق می‌افتد، توجه کنید.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81179" target="_blank">📅 12:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meAiLRxJeQkLjiXm5RQIsYjrH2_I1jOuq1In6JiEtSOa_Uk8HEzyozoAt61HSqYReKIei1pmqM1O1W0xbU1wBHZ7sr-ghBvsTEwX0zsdHTA-krUKrZN8n9YqicPuZJ42YE1Uj572Ys5X5sxdiHDeseKvOhmokpKLBnd2-kbuv1jf52A900PWiWDWBcimZU31zkGndi9LyUhWlrK6BAbt8X6bwjqVaOu28NCknosUs972NIXN4qOMZUPCT5JnbmYZ4rYbbxbIJlwfJq1ZXQ_ACvlwX1LazuNxzAE8XvH04sPFswY4D6rYMtn2j3ciH1Heb9i61n_qnpXhT9LaUdgrXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FM5ULDckID7MT4eORbP4Mnrz2WDr1dnnGnp7dgKPHtW7Cj5QzPtAKd0jxlQcn5ktQg5gEPNbGhxAShnr66hhN4Qi9D_V3soZq2omoH-aLuTmNMKG7G-ykkKUWmf1nnYV7fossH0h4Fo54R-8vqnIEgCLl0wmGiP5VAxTdOQliPLMBOhxK2ungvh9iUWBOuVVhCfqfJRvYvGEe8wByd450XTI_f5-GxCyjrL7NMaun4iEWGM0NTNB8M7SYSYnH8XjlRsIZQTUAKQdd36RbmsVygQfzUUjvdhAT2UAR0DKn7sUhl6mpoOUbsoOozOFOwoAWvtSh9D-92QPER-dddXZ6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حملات امشب آمریکا هم تموم شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81175" target="_blank">📅 05:20 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فیروز آباد فارس صدای انفجار شنیده شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">وای
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81170" target="_blank">📅 02:46 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بندرعباسم زدن</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81169" target="_blank">📅 02:43 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اهواز جر خورد</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81168" target="_blank">📅 02:42 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81167" target="_blank">📅 02:31 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81166" target="_blank">📅 02:30 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اهوازو زدن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81165" target="_blank">📅 02:29 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=O5bqsIJ0WZnE01-wLHlqO93tB_QnaH71Asfq5sIpbYuOjn9UHDBAm-ga1UxLlSjYNt6POCdcsJnqXP-IRTP824sLgjbQBFFBvHCxwebETCsbGZRDbJVKRBBem2FmoUjDnglg46_Iu0haLLiylr_2lt1_a0vYKZ6LjsmYLMzcktAM1eMUnku6njvO-YvryYUbaykWtwKK1NI98xJ5VShfM3LTISiCxupwcGVQdogNoAFimHqbLeibu_J21WN9MXeZfxo0Rlg9hEE6ysukUUk0TALPQsnt5JwDGoA-851EpfrCEJLTULoJyD6h4zIx_hB_E1J4C1ceHiRrZQoQOKR8dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=O5bqsIJ0WZnE01-wLHlqO93tB_QnaH71Asfq5sIpbYuOjn9UHDBAm-ga1UxLlSjYNt6POCdcsJnqXP-IRTP824sLgjbQBFFBvHCxwebETCsbGZRDbJVKRBBem2FmoUjDnglg46_Iu0haLLiylr_2lt1_a0vYKZ6LjsmYLMzcktAM1eMUnku6njvO-YvryYUbaykWtwKK1NI98xJ5VShfM3LTISiCxupwcGVQdogNoAFimHqbLeibu_J21WN9MXeZfxo0Rlg9hEE6ysukUUk0TALPQsnt5JwDGoA-851EpfrCEJLTULoJyD6h4zIx_hB_E1J4C1ceHiRrZQoQOKR8dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس: یک پرندۀ ناشناس پس از اصابت در آسمان جزیرۀ قشم، در حال سقوط است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81164" target="_blank">📅 02:21 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بمولا این یکی یعنی تعویق.
ترامپ به آکسیوس: جنگ جدید با ایران می‌تواند از عملیات خشم حماسی که 40 روز طول کشید نیز بزرگ تر باشد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81163" target="_blank">📅 02:11 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">ترامپ گفته ایران از این به بعد هر کشتی که تو تنگه هرمز بترکونه، خسارتشو از پولای بلوکه شده اش ورمیداریم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81162" target="_blank">📅 02:06 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">باورم نمیشه ایرانیا دارن از فلایت رادار مسیر حرکت B1 آنالیز میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiUXnwzGK3wDI0HmcwTx45xjMN3qjtFc7aOGFOu1NlvmG0o0qirkzlcBr3gcetLzZmEvHL7Lgg1LLzHH9AaWaQM2mAjMjmALJYUS0hLuEDSYF9567ciUh0DhAHHj_H_cFd5wuMELhEuJ9czS6Fdz90V5NTPS7LKZgb_e1yjzCWOl_72hbMWldp81nNkNnwPXRL2P1z7ZCj8Q-IXQy0eC4DbHJWrIxLpsCoULgP_eI3x7-C5ifJY6u6c8bs_gxuVrSeMbYLRrvOGGQ-sP9jlfyH_s0PO5Kmfo29TnQU4rwSLZpZUI1RMRKVwKuV8dY8O9YgdU0w9AyeE8oxDtoWuguA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA2f98PiGiPHCq1TRri0J1pmUeS_9cAb7-CLcEN9hQpb8OtaUxxra8VnjgCYWb9Ll5mIKSZCMXfUyRftbdioGPXfriJ_TU0ykXkrgZflkQ8NFwqfd9kcsvnVInE5kpp3csLXunoNwzIrqKE6ZkdzUinraNwJDHLdguKKeWA63-ubLVmd-9YvkEnNuAOrnZSMm6x5qwVc0wHvj5t0RBXBYo-nRegaSv5NkbWj8cS8EFZuuTV5h4cXE3Il_ewHBa6ScqZFUhrfh9zIlWSCFU6g76LPKY3VTRR12343pZBidXEt3AnPT3McvEUVAvUPae3lTnax0HIgkeUCDHevkUhIEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">سپاه چند دقیقه پیش حمله کرد به کویت و مدعیه تونسته یکی از رادار های تاد رو بزنه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81154" target="_blank">📅 23:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">امروز تولد 33 سالگی نوید افکاری بود، تولدش تو آسمونا مبارک، روحش شاد و یادش جاویدان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترامپ: ایران میخواهد از طریق مسیر دیپلماتیک به کار ادامه دهد اما به نظرم هنوز آماده نیستند و باید بیشتر تحت فشار قرار بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81151" target="_blank">📅 22:25 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">یارو اومد گفت هر کشتی بزنید یه زیرساخت جنوب میزنم گوش نکردید نتیجه اش رو دارید میبینید، الانم گفته هر کشتی یه زیرساخت تهران بازم دارید کار خودتونو میکنید، وطن پرستای زیرساختی نظری ندارن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81149" target="_blank">📅 21:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی به کشتی های توی هرمز موشک شلیک کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81148" target="_blank">📅 21:08 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81147">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه چن ساعت پیش یه نیروگاه برق تو کویت زده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81147" target="_blank">📅 20:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivMx_3bg3a07ehLZegX5sYWCnNaFj7yNhGrT0zGs2dh7-lVjw53hz3qFvsEoTtJxZn28K5JvpATQeA3p0ubKDNdr4nMXmjNvr_ppWzhv9VgBYly3yD69rbT6Ahh3Xj9pdeJKNlWlJ4V529qZ3MkENM2Nbv-JrX1a_Wk3kngdvidW09pIxhkLM99BFlFe4EEYTgKyvw0J2dlbyL3qYWuUzCym9_j0TyKcPTUlHTrfBC9ylV6ZIZhIrbTJJdr-_dXiFFA9Hw1ibzrnmbQ4BA44PjvQ0RwfEZfCS60se1-X4HnAPJsmxSAxj8R7nnrlOLlEWoOBfTo_kXvU568dwe7G2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال جقی قبل از معروف شدن :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B86A3PSChd45fh2-rmScGhn5Xf9YMRD9T4HVNvSRpwGaWKDi70iuun2Olpfypzrl-SajuWiNAObLBY6qaS59xVPzCAarsCeZW7sZjM-idHjxcDrTt66GzVPMKwB3LSZVoTXDVigs_f6liQyL_intGAUjUWS9UND-HZqEeEKoJ-MSDQlmN7g0ddq7O10YPLpYFYnqLYd3nbiXQktJzb_UyyOJd941AsiTM0whTk_LEIpe0z5FUg5ccoF3KCUPfeW-20RkZwtAx8wbaQd_DcfOLUN-3HxBpBSPLQby4BEvWCtKA21vqtgZNMJDGc-AbrNWE3O4cvKApVpMfI8Meb3CcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fWAt47fACHZAEZ9qtWBWbWVuh3wkkSUJjpQsDZaXk14DIDTbmQafPf8CiV3G6DV3_4WN_rRoF9_TuQFdeyPltHn9QXYEjsAXuBPdNJCoIZbqlYrKM3t8e3OKp9rrBaJbvbvaGqW1P0DJjz07rooxSIKMyqdDlntTWyLtcrO2Rv5vnv_63wWl7ieIqq1356T94Yqt2VejYfdS2CNPf8fj4LmN6CtWCVFshoSSVa6ue3UPcIPWm9k6tovsnjGatQegehzpK1WO8Kn_0-bt7NPWdgWTVaP1YDTTIn62KgYQW6hz9yBa6WmLCjYRG0h_6HYwHA9eEgX6CEEmVKJ8vP9Igg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzh0ucQaIRuZbKzZU-OzHL8t4YR-WntaNftOk6EWbNQuPVL1ONKV_qnozjAI1HLbvi9dc5GkL_mHvxdHS6sS35Eef_G4Qb-WUWA7-slBWDMgqDLuD5DDsm06YC8stCC_Og7lByD8Hvl-kt7BrdEWEhJOw8bBgrcXjV5PQ1NPAG93bZQWnWdoSSjXd2X83u835ibPuJ3IttrT7JDNuI3p9snvQXNtFcUxBBw3ESVTDUNuojueU0URzRzovsroA7_eRcLl4EiS8WF7dWIDjQ-XXDygj7jLmDlb9n8BMYKAMYqEyW2KUbAuptRmIOloVattFfPXA_uiP7_FpwckxvQKMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ایسین به اسم دارک منتشر شد.
📷
YouTube
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81143" target="_blank">📅 20:31 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وضعیت خزانه کشور.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81142" target="_blank">📅 19:38 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pkQ9OMHShmEnRE3ISaBLntcnMHaYVGDLLfvgOA7c2I-76daVq_vlqV94YR_vuSERKkybXC_7MFmeR7egEgPLnHvjpFSM1mVhUCxITE-fereSdy9OaFkv1nCTel8kyg4KaD86TQKXhv4fwL4wH9hdnYp04BpJjZVDMGoLtr2dKEyNR6x9imWBDaFQntNINqB6zOaHGyhIOBHFFr88LgqIstpJNUHj6QWSvP8da45b2409iRuZYx8JbvM8U8W4oIQQA-06iMfNwdZBvMjZ1Qg3ogfnbkJ8hzC4bsjLpfeNml7-xduDmC-P3YEOcTNnHmZfKwCh_krXk4EcybVuQqCf_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eA5jfOO4ylYXq4b0PBA5oGbI0FAxZHYAT124PiW9ZwUC5aCsv_h_WVf0fjxc4Fy4xzj4l0GKpNos5nY6ihWKYIPdN08AMnhuGelWtFUNhE82LP8BcPnK_BFI0iNZBOzIXwGjXZN8iCCKU3dn7y_s6UpkC-1XR9xTtIOeRSxLwvNRFTG6dK7GbSJavHzgfZpuj6frOhlg9-vBf6QG5RaOjTjYK9jEBZ3BAeDDJKZhn9XoH-JvNIE8XwQFGBwNWJv6cT9SqrxmwPH5Y0QMMj6Hcb0zGCEGlv2sZ9Ba6VgTksq5eTd-FDau9pFy8q1h-ZSvZBj0Kjru9kgbiLJLwzx24A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید کنار بیناموسا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81140" target="_blank">📅 19:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81138">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">آکسیوس:
ایران آخرین پیشنهاد صلح ارائه شده توسط میانجی‌ها را رد کرده است.
میانجیگران تمام تلاش خود را برای همکاری با طرفین ایرانی به کار می‌گیرند، اما ایرانی‌ها همکاری لازم را نشان نمی‌دهند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81138" target="_blank">📅 19:19 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=WLIngWDSwmV5O_NWoPI3gvWTj-A2OYuFJ8fk_x9z--_Mvrhwv0xmfP6ZqaUQStdS2WpaHUDDpqFgw0RZYuqLW-m1V_zHfohqmTYPR-468VizZTzKzgbfN-UxDUpwyiMhEoH5dGHoLx0S2-mY-boBafmDBV5QkshZruMIANW_jsDJ0UCNPgXhWkKTorZWN22N8uEHZS5ZghU3b9GpezL_4qa9_12gq7nT5-7Pg9FZoTvJb8ESgXZOvRCOQuM64bWIgaEeaQdO9lWBeudb1NLnmtzfyYbccwMjVajDi83VqFNUfkPc8ie0qOtjJfXzxK0ZOfFZr_fyKu7Z458f6deAAA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=WLIngWDSwmV5O_NWoPI3gvWTj-A2OYuFJ8fk_x9z--_Mvrhwv0xmfP6ZqaUQStdS2WpaHUDDpqFgw0RZYuqLW-m1V_zHfohqmTYPR-468VizZTzKzgbfN-UxDUpwyiMhEoH5dGHoLx0S2-mY-boBafmDBV5QkshZruMIANW_jsDJ0UCNPgXhWkKTorZWN22N8uEHZS5ZghU3b9GpezL_4qa9_12gq7nT5-7Pg9FZoTvJb8ESgXZOvRCOQuM64bWIgaEeaQdO9lWBeudb1NLnmtzfyYbccwMjVajDi83VqFNUfkPc8ie0qOtjJfXzxK0ZOfFZr_fyKu7Z458f6deAAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماینده کنست اسرائیل و عضو حزب حاکم لیکود جوری که انگار از دهنش در رفت گفت:
ما در حال نزدیک شدن به یک حمله علیه ایران هستیم، شاید حتی این آخر هفته.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81137" target="_blank">📅 19:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رسما و شرعا توافق شد آقا
ترام به کانال 12 اسرائیل:
من در حال بررسی یک حمله گسترده هستم.
حمله‌ای بزرگ‌تر از هر چیزی که قبلاً رخ داده است.
من نزدیک به اتخاذ یک تصمیم بزرگ هستم، آنها هنوز به اندازه کافی درد نکشیده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81136" target="_blank">📅 18:59 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXSPeNnrtOqJicBRdVkHkT_KS1R-J3e9It1mhu4s6JQGYccnD7lZsOLz3OieRk7oLkKmSDp69_F9a5n_p0RYjJt5-ktNnnUeCcwHPXXw-z8htSi5ce5OP4aTV_ojedQw9St67XxanewOc-GXbwfDrlyPUSQmQX1SLq5oiNpwkBkvfBxNyQpgVDtcZosXbcE9gdWj_GqF6vEFN1vrinR1MNuaYxhYNMeDEZoHbiV5nQ1i191YbCXgTqBDeNcGNJFC1eHefAY6xW4s0_0cStu9Htn4PxdORwDUQImGVMgq22KMUxMb8SqyMlDyThPiJfDXZRbX08_Lft3lJuUwY3FfwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nr69RGxSRZZJAHpeZSBtiORf6xXo50R4M_RVbe8SGriw1ruliRCzLtmpenDvLn-71TV12X2EYhfw8YTTPMNREn16paMoMcSoJXcwcunPHUHIUopi2XDMxxbw0CXg89Fp_-nI9bP-eAnfokMdDYR5_XZywhfvS7KDiUTBpyaFrMyign8uVYvrKXK2dkfBWNgt6UYXX1mz5t9eQ8h3qmO0MU9g0lkoi8xuzsxmVqm1m97Lgpl-cVaw7bt_3htjn-u3Sfa7HOHVLaGwMaJ_6FBpfSxUsgE_P7GCMgaz9uLrlJz2c6URtdXQh0mv8EUCn5N4CI2L4aVYE9uEuAhg1LI8xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادعای روزنامه صهیونیستی جروزالم پست:
موساد گفته این افراد زیر نظر وزارت اطلاعات ایران و با همکاری سپاه پاسداران انقلاب اسلامی قصد ورود به اسرائیل برای کشتن مقامات ارشد اسرائیلی و انتقام گرفتن رو داشتن که دستگیر شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81133" target="_blank">📅 18:43 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=fNNUkZa_YOF9AQ7JAKulN_eXPMCq34Yg6H4Wrei3OB0R77C14TLSxEak0avDVesSJGosFw4NFN9xugDVDknMza8l7V1Zzgd4gGmob_jWNX0t4NU6O1ZDb8UK1VnldPc72AMXKhrqYQht7zp_4HRTFrRlkafjjIePC_XN3ObfSOHfaxM2WXRoVJ2lhudLt2_V73z1xPc1Q3VmPfIdjRLSrDZaUMLVJKMCXtMgoQY0spwoJKaUJcvHr_TjyiTHsGl6JHDl28WnIUyM7Cgux3TS_XJt97jmlkbCfN4jdOHXU5juobCPBj_U5J73BGb3AljnGHrsnLnSc0-unaJCnyNXHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=fNNUkZa_YOF9AQ7JAKulN_eXPMCq34Yg6H4Wrei3OB0R77C14TLSxEak0avDVesSJGosFw4NFN9xugDVDknMza8l7V1Zzgd4gGmob_jWNX0t4NU6O1ZDb8UK1VnldPc72AMXKhrqYQht7zp_4HRTFrRlkafjjIePC_XN3ObfSOHfaxM2WXRoVJ2lhudLt2_V73z1xPc1Q3VmPfIdjRLSrDZaUMLVJKMCXtMgoQY0spwoJKaUJcvHr_TjyiTHsGl6JHDl28WnIUyM7Cgux3TS_XJt97jmlkbCfN4jdOHXU5juobCPBj_U5J73BGb3AljnGHrsnLnSc0-unaJCnyNXHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KBB3yG2qi1f0NYwQygXD5LXNCFFE3c4ZhLBOHUDubWfzxupclMleT9J-knz_jWoSD08ZYDFlP9j2DSii1rLKTJPCG03F8Vx0jdqtXB-V1MlUtlsG0CNZlEwJed-A7y4ZgTyYtJB8EOeHuLCIbdCc867xNLzq5rwNxyv5jGGDc6VTVR0nNyi_tsFWkYNPgqqZMQ2A3cXGt9mVBKiJZMmVIaYivqal-ajsxYu2yXmkTxDwAMFxCsC5Pv1-Poe9OcB-L2EMklsVYS4U44xUIXOLn5OJ515rNzF8EhbmIU0PvjFvVg9z4GamLVYepweQ_h4PNSx9KbH_56juqOQnshg2Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید ولی برا خنده‌م گزینه‌ی تحویل هوایی با B2 رو انتخاب کردم هروقت دراپ شد قول می‌دم بخندم.
🙏
🌹
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81131" target="_blank">📅 18:23 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/81129" target="_blank">📅 18:09 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=q8uk5Txcw9L2Pevjz16kN7OLWXcdwzKcYnmxuiwDZs1V5tpogznSCcHZrNrOzJ3smZQEHzC__MNrA--tUPjBs79JaZm_Y4kxT-i9KVGab5lI72N9dxG8h2tVvP0nr4V5iGOLAOI9GKvmrR_iXGdyAAQo-Pw_uytUXF6IWhVuoRfODuoQqoXOnhgdOCS7QrFIl8Zb7uHnJiF_tE722NQL5EnYDBnYDKyYSWFYSgZrmUHOYlDeMx0ojEmbnIpYYHDt6xJywHmA5itxOpRJJaqMMXWL3GXRBfHVHNZ7REfIDlTRskSysQS5mi4W6rQTegqUVm8r2WgJiffVKeY0UTae4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=q8uk5Txcw9L2Pevjz16kN7OLWXcdwzKcYnmxuiwDZs1V5tpogznSCcHZrNrOzJ3smZQEHzC__MNrA--tUPjBs79JaZm_Y4kxT-i9KVGab5lI72N9dxG8h2tVvP0nr4V5iGOLAOI9GKvmrR_iXGdyAAQo-Pw_uytUXF6IWhVuoRfODuoQqoXOnhgdOCS7QrFIl8Zb7uHnJiF_tE722NQL5EnYDBnYDKyYSWFYSgZrmUHOYlDeMx0ojEmbnIpYYHDt6xJywHmA5itxOpRJJaqMMXWL3GXRBfHVHNZ7REfIDlTRskSysQS5mi4W6rQTegqUVm8r2WgJiffVKeY0UTae4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین مونده بود نسخه مناطق محروم اسپید به قاف بگه کیری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81128" target="_blank">📅 17:56 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81127">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=pAmICIJsvznhxSHM-2fC3bAqCSNLjNaPi7ACuzGXEl2zoW2lQXxIrG3nqUCUQtYts65cINQ_Nt2EQTotF7CUBCy2EpV5p_z_O7fKlprY8mitLRGEC_xXVVAAbsIQbdujonXx4DAk0s3f1FLuQY937wbd3gG77jkS8C-uUiBojcX66ooWXr7Mo8mY3BA5OpZd8rmgukfYTs8pSdDWlD_zPjk0rhaAcPduxcEAnuYk-NLqpd1-BZ9MvsKyUaQZPegJCP01ZGIF1FpMP78nxkhQWHeMtuha9-0JcOwa-wCPKGIpj5ZlG3pIrDPPclrHcJhERpy5_sLkmapSiZZW5Tsfyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=pAmICIJsvznhxSHM-2fC3bAqCSNLjNaPi7ACuzGXEl2zoW2lQXxIrG3nqUCUQtYts65cINQ_Nt2EQTotF7CUBCy2EpV5p_z_O7fKlprY8mitLRGEC_xXVVAAbsIQbdujonXx4DAk0s3f1FLuQY937wbd3gG77jkS8C-uUiBojcX66ooWXr7Mo8mY3BA5OpZd8rmgukfYTs8pSdDWlD_zPjk0rhaAcPduxcEAnuYk-NLqpd1-BZ9MvsKyUaQZPegJCP01ZGIF1FpMP78nxkhQWHeMtuha9-0JcOwa-wCPKGIpj5ZlG3pIrDPPclrHcJhERpy5_sLkmapSiZZW5Tsfyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای شهریاری
❤️
💋
💘
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81127" target="_blank">📅 16:30 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">ترک جدید ممد به نام فول فورس منتشر شد.  SoundCloud  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81126" target="_blank">📅 16:07 · 01 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
