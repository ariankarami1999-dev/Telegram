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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-03 16:44:49</div>
<hr>

<div class="tg-post" id="msg-81247">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQuIjSF5S_8MjaLcnk8N30T8QX-HFjZgQv48uX28Ilf8DPdU13AwQGhP4VAuY3tmTfE402LHog4CC9LiHsQVV5qODaNGRMOejm9h73K-MSvb6aTVu62DWNZyvX3itqu3XniHdOaLaIYLfOw28SmE8nUDTVbKUONTCWgztb4q62vCkfDY88czKyElM8TVYtZ0e7W5kNitck22Qv4afUXaKSV_Drw3xZmHbqu9qD2L4cRMCuzII64_x_bvj7RVASwc9WXBuLKl_oNy22uP2PoO6PunHfhu-KMtbEuMsanXP-kAbeSvQ4vVb0a4vDdLXCkvNeM93vQ-k2j3zItkZEObBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فایلای این سریالو کسی میتونه بفرسته بگه</div>
<div class="tg-footer">👁️ 369 · <a href="https://t.me/funhiphop/81247" target="_blank">📅 16:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81246">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1pxHqmJD6MwwhJ8j7Xj2G8QKtmL5QzF5KcC0FWFvkHt1jLcH2s8o4tfFpBhtmE-HCHRKVMsQjsOdfSQUcmGf0-ZBwXXnftN6pqCHnvJ9QSA3Y5XvGqoS7Jj5yNZLRfVxE-75MaCM3-AWj5CvFeH3y7jA1eAZcky2H_H_2f7ssTigSZU7qqz54AAyqJUx2Q-4G1ikeoIAD7Sa3RaqO5DXGwXPQ9Sog3ko9ot9DiPXpYv7atEyYqyT0YWCmQlQlMLr_96zIRe6BVV1KQ4Yttx52plLnv20zOIloJexX_QK4opNuvbni4_ICs2tI4sLDYssW5Xgzc9aj0v_TIpzriV3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدبخت مهدی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/funhiphop/81246" target="_blank">📅 16:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81244">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">نیویورک پست:
آمریکا در حال بررسی طرحی برای خارج کردن اورانیوم غنی‌شده از تأسیسات هسته‌ای ایرانه؛ «پیچیده‌ترین عملیات نظامی تاریخ»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.66K · <a href="https://t.me/funhiphop/81244" target="_blank">📅 15:43 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81243">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">عباسدرمن: اگه وزیر نبودم میرفتم پشت لانچر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.32K · <a href="https://t.me/funhiphop/81243" target="_blank">📅 15:08 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81241">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx2b06JK4b94jNvCnWQKAmJIG5wymvQZoSaJgfT59cYwqxzojnFsy3kATsY0r7ewEbqJopGiO5Y8vflJajFNs53bmATTTUk47-uwgNIfnM9CAccXMjvIeVSy7OOc32yPfcF-QH_ZTstJBd7WEbqAk_yip1EV1AvT-tgXDYddbysGjBxVEFyojwe93vD3-GFL-8_zslSOFZjQL_tP394WR74opc6mbGOZHuYu76l6N168WRgDZyX5zcD9J_b2g1zUUs0DpI2xSDxYJ521aySDH5D73QhX2ed568urUT9K70MZ4gSZHh902_cqx8RblNI0Px-4syfbIY8Twa0eibhM-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا ما بزرگ شدیم علاقه به کودک ترند شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/81241" target="_blank">📅 14:39 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81240">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/llGCb2siPXW3fah_ghbYT4Ty7rdaAFFNsqcYu_60FPFr7GNWJi6R4kuWFxrmxPcofGUpXX1qzxoDyqf05qylgI0G7Rfakdc8hvmaVuuGzWcpO944HYb0tB9QzVcHxMJxmHh2JZYzyl1qCaqky2BJIddEfAqBnmTQZbYYcMhOEiAQG3XaHhO1fDZNewfafNa86HbIEdknccv6Wi92vQJBZ8swguNrJjlqOA1sP2hFZxRgiUwyK8Kfmgb7SyNQCLUd1KXpPZa5Uc8MMCH2J8KsOMwZLBPpTXnJ9WgqeHm9XmX5uyDTuF7Fq4XO9LvvXX3dqENCFdhF9q1NR9-ZyslH4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/81240" target="_blank">📅 14:10 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81239">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اوکراین چنتا کشتی روسی که محموله های نظامی ایران رو حمل میکردن تو دریای خزر زده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/81239" target="_blank">📅 13:53 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81238">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">شهریاری، گوینده جمله مگه تنگه ارث مامانته:
متوهم ها باید قبول کنن‌ که آمریکا ابرقدرته و حریفش نمیشیم.
پ.ن: نه مشتی صبر کن رستاخیز بزنیم آمریکا این سری دیگه از خاورمیانه میره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/81238" target="_blank">📅 13:40 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81236" target="_blank">📅 13:00 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81235">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هوا گرمه کصشر نگید</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/81235" target="_blank">📅 12:01 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81234">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🔴
ترامپ: رسانه ها به دستاوردهای فوق العاده من توجه نمیکنن. من رهبر ایران که یه آدم قدرتمند بود و همه ازش میترسیدن رو کشتم و الان یه دیکتاتور همـجنسگرا شده رهبرشون. اینکه یه قوی رو کشتم و جاش یه همجـنسگرا گذاشتم دستاورد نیست؟!  @FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81234" target="_blank">📅 11:38 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81231" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81230" target="_blank">📅 11:33 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop | Menot</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/81229" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nw0ORU2o-gvHwTA_bQfu-LnIy7ScuyoDfdOcoEZcz2-DHQmqTGayqJ-pnjsl4ho-21hJUuaaUeGeSjEt_VaonCJC6fIFOmt6rOsuorltGXWTd0OoEKzDb9Zjt0UYZtX5QCkQBtab0I8nHl8iqhKS-UzabgHhcdIs6OsbXSrbJqEHTk755KXINxuAGppnZ8mG9rMWpkw5J17T9G7oBp1GW5Gtj-BKBN6AG3JatPPho5gXNPtj0cc8kt_Btf42z7mb24E4WfefRnD2c0fweyL7jTUY0ONWf1n8M5L6gFW89gDJGxDvZ0DDP8XrC56adD78gi3BVmJm5KY1pxZh6TQMlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانیه وست
😂
@FuunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81228" target="_blank">📅 11:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قدرت اول منطقه برق ما دو ساعتش تموم شده ۲۰ دقیقه تاخیر دادین چرا نمیاد</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/81227" target="_blank">📅 11:24 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">چین حجم تسلیحاتی که آمریکا تو خاورمیانه مستقر کرده رو دید و رید، حالا خودش دست به کار شده و قراره کنار پاکستان میانجی‌گری کنه تا قبل از اینکه آمریکا حملاتش به ایران رو دوباره شروع کنه توافق رو نهایی کنن
علت چصه دامپ تتر و نفت در روز گذشته هم همین خبره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/81226" target="_blank">📅 11:13 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81225" target="_blank">📅 10:07 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یمن همینجوری حملاتش به عربستانو ادامه بده واقعا برمیگردن دوران ملخ خوری</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81224" target="_blank">📅 10:05 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0j9l6_otFjp1imVzkaObfEDTIqWA_dLEz_qfba9tFy21zc4-Oa_KuqRF86AFOdls3OKI7w3fVtK3JHAsH4o7Q3wDR6_rk8jLiGwAlttk5y-8eyho_4EWWtnZjJ8bx81VI-f0rilHzPt4oFu5XpfXYLeQjCmQ-vx4D7Ck8b-1jOEATlO97zYfVexKCz8JO5s_ExmPsUft2ojz3XgBQkGsMOsk3Krw8BxLSOgVxaWVcdGLKhzEp0q41ATBvFs1XAsGlbD-ArGkd95t-xI5Wf3XoD7YlyDCVuH4qeaJqfD_DuqAoLa0sDZyz2bGjhiqOraNDvOXgeVdR1MWA2LOfogKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#بالاخره_یه_پست_رپی
پست جدید ایلاکه که احتمال منظورش اینه که "پوری خارت گاییدس فقط صبر کن" ولی روش نمیشه مستقیم بنویسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81223" target="_blank">📅 09:45 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHm88q0-PKmlxWMgR79cHG6xcSnRO47WJ8YQXSgpXoJ8zCyMSXsy3u7bPsf_HAJp_JfCeey8-VOIpZ7btrjAZrzDfkxnkkDJ-pxBWIgYB-Jru-bV3GiCH4bpPRQX3MNxqXpSr_hSv2oYDfHlMnj8-DOZJEartUOqe1fE4WHpN0LLVTOjxK4qAsEwwpxOK4LXSwpuGUM7WDhmzGbHsfqoJB6tlJGNrJq812ZQEskAoNZKY_imnadlKRcw3A_7ovb1A-Kk0jCLV1aoNhLsRMkwZY5Tw65e9Kp16q9sc49eGqfI8akTbEqMz2pZGwA_A9xO2gHy8F5xW4fqW56Bc7n9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باور کنید اینا با آمریکا تبانی کردن خار عربارو بگان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81222" target="_blank">📅 09:31 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این وینگری که رئال داره میخره از قیافش معلومه فقط برا کار تو مزرعه ساخته شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81221" target="_blank">📅 09:19 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">لبران جیمز بعد از ۸سال از ال‌ای لیکرز جدا شده و رفته فیلادلفیا سیکسرز
تینیجرای ایرانیِ همیشه در صحنه، آماده شید جرزی این تیمو بخرید و مدعی بشید که از ۵ سالگی طرفدار این تیم بودید و بخاطر لبران نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81218" target="_blank">📅 08:44 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">علل حساب اگه جلسه سرانی چیزی صبح هست لغو کنید که اوضاع مشکوکه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81217" target="_blank">📅 04:36 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">رفتم قسمت آخر برنامه ابوطالبو دیدم، بلافاصله رفتم هایلایت لوکاکو جلو سیتی تو فینال سی ال رو نگا کردم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81215" target="_blank">📅 03:30 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">شرکت هواپیمایی اتریش، تمام پروازهای خود به تل‌آویو را تا اطلاع ثانوی لغو کرد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81214" target="_blank">📅 02:47 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">امشب آمریکا نزد، من زدم  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81213" target="_blank">📅 01:06 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امشب آمریکا نزد، من زدم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81212" target="_blank">📅 00:51 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">عربستان و یمن همچنان دارن کون هم میزارن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81211" target="_blank">📅 00:41 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgy_1S48lFgCP-fPwzNl0NMrNkwHJjjvnJxDnoCaDjIwT8FH59FHPf1uShZcBMKTq0ZH7dAeDRR7KyeVmKwVKWEssnhXgenXukwhac3yPL47JcQDaJpW2jYDjV0NJ27uJA2ZWC9I8qr1lVeslqWJ1TuIQ_bR6UbAG2Na4cFxfEEyLO8Wq0j5xi_narZsnBk5kVDNbLru3VdxJ-uxxug1o_qVCzlnuCfzo-uRLGumS5eJ5JMZNgusd7A0sgGsSIEfbnoFXZTP8aOJ4-enmFsvczvZL7z1PuaNzawRHnJQG4ULdBT6h1JERI82eJ9oCkq_Npi67oLnaJJMFuwLkcqHXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81210" target="_blank">📅 00:15 · 03 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81208" target="_blank">📅 23:55 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0Ykl6WWV7FtPRAVuJr3AWozaXKw-B7G-jJK7kvAYl-oBzntkDkB0JOkgQt8JtqvnTgKGDioNw8qk14nBoXUU2nR6vqVzC0lMZcv42tTfAg484IA9XYPuvo8oSaOjJB7DHIMwSOxuzkpC3xaJXGZOKtPhJs2yzsZZXOqafn-UtCuO8X8eq7j-uR2eU_l_-eQka7FtNWhNkDtADivpwnVJE4echWlcOMFn7UNeT_MDrkJYWJBY-8IdcnGZ0yvZOWDGkcL7bl-jb2wFMb0wU7EQeSQoy3OStn0Ki7-ImgXsgviFba4IcoHD6tsaBEOVtPjZkNP-IRlyHrUPj2EzJRB4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوسه و زیدی درحال لذت بردن بعد از قهرمانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81207" target="_blank">📅 23:26 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81206">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ترامپ:  مهمات برای یک حمله بزرگ علیه ایران آماده است. ایرانی‌ها باید این موضوع را جدی‌تر بگیرند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81206" target="_blank">📅 23:14 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81205">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">عباسدرمن: تو عراق بهم میگن عباس بَطَل، یعنی قهرمان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81205" target="_blank">📅 23:04 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81204" target="_blank">📅 21:41 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81203" target="_blank">📅 21:34 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81202">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اکبر عبدی درگذشت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81202" target="_blank">📅 20:57 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81201">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDo4LJkZmghLTMMJ3DJChum_HjP8WSsRdCr0rT6INvEZIkA_0TZiRlBEL-OdcQmCRUEWSyvYqatF95urOsrhsuCWM5naAvyNiltub4bigWv4YJigcTBxAqQ0an8QIlcfkNQjZrI30wy1QQRldTVksGt5IPTTzj8fhW8vf08m5Vm1CclYELTkTirMwW_QV5CohYKuw5G4vStiSzD1Py56OaHTFv19CkoV2snwWbfgLkPioNscvUD0G60rT6-nRucI4hSz1-PvW3XZuYaUhoPQJ39O-tKGiXuGMkTJjzWX0w8zBKGLvK_lkXeUmBqjvn7ejbrytXe8q2apmNLLCe4qSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم این چه سمیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81201" target="_blank">📅 20:52 · 02 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoJ6uqUQ74p7h9IhOxbrrZQssSb1KvaCylcnRBlPNUeYKK_zw_p0Koht79wgrbbye6sGE_-RYAbti8A5KwmFMuwD4Jmey6AIhIoucwHwHQBffMN2dem5vhI-Q_TwzqjSXlp9rc3m6DuBE4l6mR8-J9v3pL9pssyundpZCo7PFg_ZwNL_yY0D9qPYHhh6y2Ago4twJUe4fAxI3lgsm3r5-saoWqkK0GxCirsEqyIwYIYwjsyGPIJOUXvTHyHiRdpaFfueczK_7SqBRSXlkupNPCYHdthQ2nF0XGc2BPbOszjKT8nR-4FcOPIrUDqQ38kOOh5ssqgE9cn1fhOejol0xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از این مقایسه ها که خیلی دوست دارید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81199" target="_blank">📅 19:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEoieOia8Hl3Kk4hHakC-qL0nDz-zGNFxJAUWMIRkhrZNrvUJUUWN4uGWicNvORe7hCYz90gKy3fYQiJJI9IhDHGBBf4PxaaNvtwOooLvAh7NN7vVilfEvEKoicRmSLZpimp4uAhXLhe8zHCiJMRSS-4rrChlfp7YoO5RiX2U9De_Y6zOYUBIkbqmMnlNqROD_-dZw_mRLVDIv9MVZAtfeRdBg-tt4W-fVgKDVk_fcX3UYjmR_lgRmJIeXPtxxJNlB6wGFHj3Tbg4CkhEvgtfM2N_8GtYVrMbAYMfWra8Z2xCao9-s0qvhBoa4nlPo9ADb1P_O4YyLHZemTjrFXXiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم از مقایسه رونالدو و مسی توی جام‌جهانی که خیلی درخواست کرده بودید.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81197" target="_blank">📅 18:28 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WGdKFh1TdIbr9XosifJ5WLH4146CeqhzRF25wkr8UHhfYRIInSoBKQA4XX1ArosdjG1yrnDkYfCyZQcQ1nzJmr1Nd3D_eBaNNSG1pSBWdw9qrZkAIMOpu63BgnmD0k_JVMumsbdOEx2ZEbaKOaE4S7LsipMD-g5YY42OuF8EtSdi6_WOzjQzQ84xQuEf45gGH1b_MIYI6dN4uYN9QkGMcwMOZy9ja1kJeUUreBMutGzxKygOHm1-Wjcifz4-ik5Fbao4hPHHxARAQ0yuzmp6_9mlIEjh0_a_230IwrtFc-HK5xJhSNKsCkTU3Iki1ADuvwBFr1dsOOcwUN9kEnlv1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gRHJsZUU-U-ZWY2RFgx6XxDEMywiA4FAZpoz4745AvkrVbJj4qZDp-ufHdtP00oe2bOyjyUki1yCcHbxe-gcSASMOERF1W3X8ApOETb-W_hdX3ipwLby0IoeaU_cv2JkTpMccl44_DT3Ok3Al6RITK0uFsnKcomkkX7J9NKEcBdCIHE6D1VAUT5BgpXJGheR3dWX4u6UOcLZ3IKM9OkkPFEdJ5Nfiw-lCP8HtQiegJNbnEXE_cTvb6hpZ-dqpSaGS3zw80nYf2lDvARDMrdpMfot0HmofJ0Pwd3EBGxxU_g5TFYsxPfOq6tbxt4M8NHgyiClI9Y8Di8i43AMArD76g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8VCiAZk333r37-4L_11Sv49oSEoBic2zF6NQO3jWBwFTOPmZ5td-kQ57dqzU6JgJK-9sZboecXeGa7E5qhZeqBSNwAK9QM7bPXyntIVBYGH8ADs5lh9ybW4cshr91TGjcnm6fUXFmXMlgnHqXbSPIyCfzKF_UKHoI1PVw9KKM0TtleVbI0OtY_QqVn19hiEAdBLP-9Mb_Dp-mVHfQZBcPwHTx90mry24DHdIWg69jQrhgGjqtTVTKJLU2otX4xfp7dNt0U08fvbxEvN7N4JlV8gcFAQt6r1uDNmQ-BBLLnQXtwN4Numv3kBS74sKp_cDhj0z4Un1WiSZuSif0OEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81192" target="_blank">📅 17:27 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81191">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r8nTBEAKUtm7cKkxvpLpdvzl4YFO4caXF-0u1bC3qrQRMXRSHZpdEaDSLOBvJZ1zYADPI3PaBBkYJqYQyeNicTjEhpa3YElPRpbRNAkfXClySPLVMfLRp2tJRf8xjfl52Hxevq74HEC_S5G1GCCFYnoujohR7rDItlGePDnylQxPJbxzcrmou3xbBEvzgD099i7p2ADSpJrh3BsB6hh-93QbDPwysLiZovgvtTYCNeJpPReOaIVGl_VBSz91mmbYFGHhzOPdA8MbkJZaYXpectw3PKUe6RWwnuNULUi0ruXpXkbGI4p_OzKevJmVG413smXeqUmbAjyljj2-9ZqRQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین عکس جام جهانی 2026 از نگاه هواداران فان هیپ هاپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81191" target="_blank">📅 17:07 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81190">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t9FgMdKHFykvlDh8sjc-af_cG0EquxC5HGlZADUOE10qLmTlxR0nkvDAhqiOUdRxUhtoXm7ImJJnLLJpme81EgmX-gSVT5oQfrycb7lxvyLrqismRLP_FwxWYZGrITKugkli0G34QYqQYU0ZRAcwnsQQSmZssOx0sknibE_-Su64D_30WkKNn6W4p-hMxWNqhgSmxwdHo1pdv5_9UmzbJpYG1SMYgh8zj-579Srm85nhkQcZVIKMSHThgIQkrUgeMFlW-V9KCKGGJL-bu5-W0eTIBJxInk2fokrkjdu_JQgEaicrYImxNs5rGrt8qgvUqTBuyja5f9mO-qtqwAPUcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81190" target="_blank">📅 17:00 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81189">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pACXfhAChMDC-TmvxnylSmacSj8_HgLin4A-qVshshCLMern1uTGCoodfRAfaS2nyvb6DSEVoKqgkMj9uaOElFy6xPWSBufwPuVRxEfOjsWjfz3L3D44xEbhrxQ5_Fx5oN4xFPiy98N0TmB-ENoODh3i24_ipMFQChzmZ0mp1sQSNh9TPW_F_TRf79-rJtnZ3Z0G3cmMoKd0PYPsQvvoHmxpW4IdhG86aCopAEzgIbNQ4nR_5QK-bwaONNVmR6SlNV_bJg1UajHnLoak8HkIQUolx1Fa4EWqrzcnSDiK3uNsjH-v5YGP9p06o2vrRdUcwDYygdUnxVyhvjM03hxMug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این عکس مسی بهترین عکس جام جهانی ۲۰۲۶ از دیدگاه هواداران شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81189" target="_blank">📅 16:53 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tu5PsQLUI0yGVZUltUcTiterWZ6RRpL98eSYwxyC-fkT1gw06rKdw9wsjZd3AuVKQWgAPkNccJB3Bs5e89KUy15nR3xob0uSqZsv3JY2BeK1RPCuafpIg6zEp5xck5iIeNhnMcMRnY4mXe6JxeCgDx9kf4YS5YUOFArw0TZvTw_ElNW4dePOEcpVYiZruvgp4ejNKht-_zvwtOrsTQilHwF9oH1JGwjKXELbpZN1HGthclbTogXE7ieDZXcqTno8TIDmWQeWNMe7oBsAJVHfrZoG46a-K5S2CUeugecJC04lJge9Fjd55zrX1Pm91J3zjCbxmT4WMz9RFL5pKn9WWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت بورس آمریکا تقریبا مثل قبل از شروع جنگ ۴۰ روزه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81188" target="_blank">📅 16:33 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J_rUK1H1Pgke8-R6cUC3rphRGQwmJKYcp5JHds5ndBVFpViylcDGiswe3uMHGcYeZq2soQtJGMgVt5JzQlprb2GHUiV0f0_tLtvmYec2CUAblLMGVM_mQ4swlEcIRsx_6tMic_jV_WxjIla4ggC311unVJGmXEEgq3HX0FLp5UFSg6ELQDC5UrE6I9t3QlbuuPT7gSx37TIGzkBvmMQg4ZvCqGd6nKM286DaRy7NNNH0NdK1t3bJMdzeGNqjhBkiRBjfHOubtSm0VmgF0dov4BGKSUbPxO7-HYjwn0-FnT_CuLm79EbOH8x2l-faR0kiAbw337KUi0_tFqGF-PrCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81187" target="_blank">📅 15:58 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">اختلال تنگه هرمز قیمت نوشابه رژیمی تو کشور هند و بالا برده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81186" target="_blank">📅 15:43 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81183" target="_blank">📅 14:45 · 02 Mordad 1405</a></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mJ1puvq5mZYbbSrAZZcHnAJNbMBSwxcV0UIXhO9SPmWb7d7YKriOtlUb7NbRjhL7VYLybGQ7yCotQoOFq9ntQcF0sZhWwYe-ROJ7PT_vArO7RUXuRpIfprs3X2wlPhGJzclRUfmyHDD7TRE1_ZtNahBCu9HxqtdArUhC9m3Lh9L15mWLbMABbX4uUAt4j5SZ_oITpxuXnSwOWOSM08NQqhr0C-ZvANAWCiibStX1nNW4neQt6Koe1q8_XII6mHJNFJfDt8sgwH041HDeew51aOmjjlKy2vuaUYcer2ZYzQTbn2qHLLcs6ss8KBQVDRMNuNzKNx_-8ERAFgh3yJDZKw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=ubbJI-zrUfIXMjGOKG9SxNDrd_lHJ-Wlv7RQcja9GeXnF24DCKGQPRYSr4-OxULfyhS6HV1SnVdRyYkZglKlnHJ_qAOGXWFEwnyB5hVffrowo-F9dbBvuTpjMx9amoA4zvRmNr4gfXf3Zmf6ayPbvsMbCXyUlAcR_lQJ-dHY8_t9_ZKcDYz-4B-uWR0EH9Dagd3Xxd-V7Wd9hEzqmdHKEtYp5WguV6Gcc7Jx-8TMvvss9gOaU5Awjn_d6GBnODLN4LPP_1ou4zNsvSVecwV48qGGwStVQKKJvcw2VXtwCpqHLo6FKSisnRWYiBhF4EukljNC_BuZ1qn3tdujbG60PQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bcddf257b.mp4?token=ubbJI-zrUfIXMjGOKG9SxNDrd_lHJ-Wlv7RQcja9GeXnF24DCKGQPRYSr4-OxULfyhS6HV1SnVdRyYkZglKlnHJ_qAOGXWFEwnyB5hVffrowo-F9dbBvuTpjMx9amoA4zvRmNr4gfXf3Zmf6ayPbvsMbCXyUlAcR_lQJ-dHY8_t9_ZKcDYz-4B-uWR0EH9Dagd3Xxd-V7Wd9hEzqmdHKEtYp5WguV6Gcc7Jx-8TMvvss9gOaU5Awjn_d6GBnODLN4LPP_1ou4zNsvSVecwV48qGGwStVQKKJvcw2VXtwCpqHLo6FKSisnRWYiBhF4EukljNC_BuZ1qn3tdujbG60PQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uNmTTWcb4PeMgoxj3fitTU-d21Tt8HlK8mCO10eeZdOZ5DXS_EMN3rLSiqywbqlYWepYlgq-oGn_GRFAcPWYSjZ8FG2zj5C0Q8XqN_KcymDLmuJnZ04gSjgX9moEmEGTH6COg2EvEhVQKS7b1eBDq403c9C10hThgzvKv2YcFX89CEJ_3SglsT3jrytFKXcDOUHIDlBZFiCkkRF3c6-XxQwEstU1tDvAieKY2qcP2RyhfQcK0DdX8mL6xVKEB_yU9nKbelZ1-PbNGrIeWyPk6mFKVxARF4kWki7b6iKvO7yPkuOWFwBmORGwBO1-sOh-68vVRGA7qEeuphzdK9Z29w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه اهل وسط زاگرس نمیشیم یه نفس بکشیم با اجازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81178" target="_blank">📅 12:03 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cDwvV9tiVjzmRdzN5YKTdYNrQ06CyrlcwBztMAdw6iPaR1hyRHM1XT0sStsrlyGJmzNSkQ8kQP9HIXGmx7MNcKB2aHN8DQisPPFcomd4CJvElxjMOxVRH_PflkgnKguZPHcBlw8xwrZFCkjFFC5wkg7pjyaEaaI9kJMOlbc2T-zghsKCl8yVnuPUPBNPpsI_IQRHiC7GjpMz102dsqepKyM-xtPSjoUlYzZBLP-zrCmADOKgL3MLMLmLj8jN-Sg8Y-fhhjgEkaTIpW8WuRI76nQPyIJ0TFi0mcEpKQo8iV89393Dq2Q_t0ZeOKbzxEdDHUME3er5rFaPOCPY55Ux1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان کوکوریا زمانی که بارسا بودم موهاش همین شکلی بود، پسرشم نهایت ۴.۵ سالش باشه
این که میگن بخاطر بیماری پسرش موهاشو بلند کرده از بیخ و بن کصشره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81176" target="_blank">📅 10:36 · 02 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81173" target="_blank">📅 04:30 · 02 Mordad 1405</a></div>
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
  <source src="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=K6Dxwq_CtYxirZn2bjLK68yM7u6WPRs5h4Di14bvfXsVRL8UBq3dLTQ_g9DfLAjYOfbFwYrtwWAS-lN_E4pdt3l1fVK2KMlx_6LzQAM_e2eSlgWrf0Ttuum9v1o1T6NsP1zBvM2ZwNbMSpibMV12nPJvWwgQWfeweISHespvGdZR0r2Sy3EYshF8S_i6kzYqI-cUP0IticdLVE6_fBoiUDiY-EnDLjmEe_SZleUeDEs1NdrGab8pwjsx-H-AkwpmqpVWnAjkrxExrOrvHT1nDdnvw3ziraFVvA1SLudMmhYi7cAwF7KoVDe0oI2i_Oqlon4F81TUGhHcXzWGKOHDqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47a5b222b2.mp4?token=K6Dxwq_CtYxirZn2bjLK68yM7u6WPRs5h4Di14bvfXsVRL8UBq3dLTQ_g9DfLAjYOfbFwYrtwWAS-lN_E4pdt3l1fVK2KMlx_6LzQAM_e2eSlgWrf0Ttuum9v1o1T6NsP1zBvM2ZwNbMSpibMV12nPJvWwgQWfeweISHespvGdZR0r2Sy3EYshF8S_i6kzYqI-cUP0IticdLVE6_fBoiUDiY-EnDLjmEe_SZleUeDEs1NdrGab8pwjsx-H-AkwpmqpVWnAjkrxExrOrvHT1nDdnvw3ziraFVvA1SLudMmhYi7cAwF7KoVDe0oI2i_Oqlon4F81TUGhHcXzWGKOHDqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81161" target="_blank">📅 01:51 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انگار قسمت نی اونموقع بمیریم، قبل اون میخوان بکشنمون.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81159" target="_blank">📅 01:18 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mk3VEvkwTjF6jhKchb4BwIDj6IPmIykbmfG3IYtvTKs3i4B7neXvDGtfg86UPC4zZE5JEYRvW313W3OmcfVvk9VRLAPKAzGbcajXCdLdBZSi4rbCR0-Jlz8xC_EqKXjECcmnB6vNfaWtrq5QL97h3U4A3J5YEqGmajaDXRaDzoTgk_jlr4Dd7cCHqTAxllAAZb6yN2DHn1_TeMuf2gAz7p7QUd1Oi3JxvXl3_6WRd_7DKEnrQrdZQp0vcslQFkJD8HrYPNPZ1RmgmBoHiTuwmnIwlY9nnGT40G3ITzqsUNEXSqJgJQRMgCISvHuKIWP69VxRXpXMX2Z2lkF0rKmMLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81158" target="_blank">📅 01:08 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81157">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">5/5/5 نزدیکه، تا دیر نشده پلن بچینید برای خودکشی که دیگه از این فرصتا پا نمیده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81157" target="_blank">📅 00:48 · 02 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81156">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-6uL4SjWFZkgfQCfzhnNY2BEzyLvADZTvxtWZ-qMCAKNjYBrydhvWFOwhbKQ6M8q5m9DWYcPtTEx-SjJLytsfftCTVu0aB6fCuhUd2hJ0XujMBYOB3SCblqSFAiA2uknpBAWzRujR7o0cGRMfPV0PV6XOz3ADrwO2fGBDJI-CyOJJf6_eGUX_YdONAyAv8iaI8gT6D7IsVwiVhmw5z8DdX8wRZr6Zu9tgC2X0331QyFQFaoEFHR6R99LcigwhaK8qFygvQvLR5XyDsA4-jYLg_S5nJ-CNwLbMIALND0kuUZM85VXfVpL2k18EZg5QYoCo0Gtr1c5Z1HI-JHrAj7xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر متکی نماینده مجلس: احضاریه پرونده قصاص ترامپ به کاخ سفید ارسال شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81156" target="_blank">📅 23:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">دخترا جنگ نزدیکه، لطفا مراقب خودتون باشید قربونتون برم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81155" target="_blank">📅 23:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81153" target="_blank">📅 23:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">کان: از لحظاتی پیش تمام بیمارستان ها در اسرائیل دستورالعمل‌هایی را دریافت کرده‌اند تا برای فعالیت در مناطق زیرزمینی و محافظت‌شده آماده شوند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81152" target="_blank">📅 22:46 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81150" target="_blank">📅 21:45 · 01 Mordad 1405</a></div>
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
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81146" target="_blank">📅 20:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFB9v2LRuXqtfFrz0fkqTPjc0SFE-eI39--G9fEkjq1NjUO9JYIEz7O8EL_uTDwxKfFrhZOnXzg3BETbpV9iSYKjLP3F8Hw0-U8OZo6SqXpRt-gwoiiA3fEcvEhZxIznB1ln1PGPaZ6zivIJY3DgPLwLxe1pF_h8W1-0hbEoY2UfuonoV-8MEIc1q8o-Qk1JVsSSAqGDQzrYKQ2pkOEVvBFZVpyY_1BbOQgytvEmdZosswTLB41XycQfSW6GjUIG0mSvLlo9p_sLXn4hGnPjgJIFfBTP-PSJuVcWeJqA5CfDTU1s0kvDT3x2LeTKoYQLOxP8Of2uQJF7D6d5ai55Yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keZwG1eii4ZmLhlmvBCAlB1Hvx4Q1UEqMxJKNApStbNbUvGuTz899oxBVvy7DF9c8KuC8jYh0q2VCbb6q5aQcmsHveHKSEAwE3KosyP_JiLEfH2rmH38zf6PmK-D1-K9v2rbswxsQrTZ-2lpEx1NuBxQcR72ccd4O-4rY9Qhz2JXhcg_s3HbS9Ap3pPAJ4WjuaMcMYpIZ8O0_UYFi0uMLqi2fFc33XIQSWgvfxngZN0Cf9_wg1b-8M9xcmusxdLWAlwzpN6TNB5Ob1t8_6II6-d6_oqejTMDCHPMZvpxyHfrHrG7XFzygzLOJcACBMnZGQkkt_4ppTeiitNRPJZAYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شات های جدید جورجینا :
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81144" target="_blank">📅 20:34 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81143">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxN4TQwGOeZgzmRv2gWJ_wZkxrHgJqUVdu7Ky-pBoArxPqxNZOglAxHKJtO0NkT_ZybCw4hVsAAzCFvPRniBgTBERz8Bjo5bZueTFSTZwOB55hpGWMRGO7kkxOSPWdYqf4f413wYHJzoSgf0lUSrslYpi7dUSoQ5yn8Tn12HGw5xfNc7X5zqIWyXHkqqGsMEtn6hIuA6coed_jdH3vqZWxz9_vicixG8aCqaJJKTqboR1286tQECfCpgCt0heVrNFBeVqBPl3Kkve6eoFP_YgT_plZZS46se5QqLHSHjw4CT-moe5SwASt2xLv92GJw4ikDdZ-lDYbQR4_srrAsFAw.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpP3NVrkO0lId-v8pnSPj7LajqyBt1Gq_Kb8Lb51w3UyDZlCYZfTFC0vihWfkOV69HUhN8GBl_cA5eqFw45lbzy-W40SMI7OZA3kWcnW1YrrZZ0KGWtlJduFjzooLfzNnbcBO0HsBYxjvCE3fei_aXD9VdIfrLRKPbjFsMWxM-FJsNKidl3xUdf1U_htB_5FFLM_5JIsUAYyqzKocswFKkI-nIU98JgjRbVE6RWJECaLAuxgUypIW6A5eEuqBIw9PMgf1G2w7CDXNomu8gzbDoVY7AuR6Kq76dgQCmQKxWXxLZnYeCfygT1GLS_iXW_k2RB9PQlnVG3_jzgeQjnHaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت خزانه کشور.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81141" target="_blank">📅 19:35 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/skyYIInJHXRs7Vdsiqx1Zz-taPItdGwJk88GHhEZMeKX3cB_-qPAa09xmc-2_cwwaH62CPWQDqm66v_2U29tzucJFEPaJ5FF4gFs5q9l_9gFkykiJMdUdi5U1B2oY4WP-baP2C09ENjMCWJ678IEMWBN6Ah-BlE717Eg5PsnnbeaT8PADeewIH1ihepDRaF0wRy1_3NxB-MypbHqaZJPc0yRG3WF043CdfgEM9gLmhehRO-63RliZ2QEmB5Gqkek6Glv-nZthgo1n-PBEKODDLVZFW9eCSiaGenewBC6yyjKnnBwe-GCLRO6QCclfKrT-L74TpplqxqNrPZ0Bin1uA.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=YF-yJT30wXIWFs5Ckx22FKPRiokNjWPwzrFNHUTXc-eljv2iT-7taJU7V2VMKFANMYovBvazdU8-37P4sDtMVAehEjPhTSRJvZtJ_R1BYwnzbfbcbF7Pz9txWLRImIstd8cW93FROakb9ewqFG8whsJjfn4eJRhezJt1ppEeWwu3qohUeOJ5FHUpX4GKqH8UhWGrto2FXJswglj0rEr4GRYHW2v2z7XJ_Loc2o2besjhdeX3Zi7CsjUxRTLxFZcBjhfIvI-_zGMH5IKFfU8aCitf_qd7hKYSrjdppeDwei3xEVrQdRk0VLmK9FWiHIluikkUb-xlQSG3INBBxjHHMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b2a53fe9f8.mp4?token=YF-yJT30wXIWFs5Ckx22FKPRiokNjWPwzrFNHUTXc-eljv2iT-7taJU7V2VMKFANMYovBvazdU8-37P4sDtMVAehEjPhTSRJvZtJ_R1BYwnzbfbcbF7Pz9txWLRImIstd8cW93FROakb9ewqFG8whsJjfn4eJRhezJt1ppEeWwu3qohUeOJ5FHUpX4GKqH8UhWGrto2FXJswglj0rEr4GRYHW2v2z7XJ_Loc2o2besjhdeX3Zi7CsjUxRTLxFZcBjhfIvI-_zGMH5IKFfU8aCitf_qd7hKYSrjdppeDwei3xEVrQdRk0VLmK9FWiHIluikkUb-xlQSG3INBBxjHHMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ESH_a-OszyDRN6HOl7m9hRcBHYn-36ikHPNmgLrQkmzPSM8gP4LbvldHkz7KovCakrFMaajUOmEIP26ZZjU-Od7dNiG8TcRR58SpK7M41crauH92Ies1JEuq-4RZ-MZMnajnJCOyTdUvuexgn9pUX8776wfS1kYuka7i2rITKuK-sr74ntldux7WkcZs3erO1T_39F6P0DojOqW0FvCjyvgDEdJG7ZXsdiG-ElAh5diqCHUuekisir6kP7jprG-m152pwm8Oxe-RLFlLJRPtBR4juSrZcURXhwqLl5tMLXNHgbzon-3Whk37qkIfCmn03URbyjZnzP3pMPymlP9LFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمالا d4vd بخاطر قتل و تکه تکه کردن بدن دوست دخترش با حکم اعدام روبرو میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81134" target="_blank">📅 18:48 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZm_GSxBxxXREYQ0axIY1Ayv2LaEVjDQjL-pH2AC0SHnfgVNb2FtzFH9rXezVP_bF1ndjRoUxNESspTtV5d4yZueghZpXkFyzcu2WN2RmKlwyuXWNvpqmiUHsz4daDPnW1Aw7eeRnuZcu74nh6BNY3K1usLBjf1O1-JnpZRolsv5CrLrtrL_hx6RSv569Us01fJrZ-NTb8wFx2McEHRAbdmrwyQQKM5XiNC_kFPTcxNIiWvM6fuNLvw4CVgU3-cX_Sd63RDk2h4wHgDvcu9hefM4tZwhLUmckD6Uw7VixmnUnpDZefbfXXgK6JppwCbSsE_f2FnUU7-FRA6dvTIxpw.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=ISs_5flJRcVOkjJrs2h2sZWWdZ8iQ2MAZwdFFShgt5fh0VwFnuOLQWDb94lFM-bkZ1XkMNygUeD6h3aSbtbLTbvMQc0oDxtXjjOwp5Z8cjHloEW-nbRPMM3QzszUSBPrFNtxtuJ55miGMzJJFYDtuL0Mh91QkJBtWibSKhNTAuj0LbvOAWmJnd-siBNfY49SxkA-aHN1s4S4rBgPvy_Lgxrbo7aRc5s52-smLIZzZq0dHHfCmdtZtAwBejOhCw0OhL4Wh2pnm1DLCIArD8OANbKMEDPsa_3fS-rK_yY38FGSvWQxhTs0Xw2eaucJZo36zw2TTySNTs_5fBfvcQ5lIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c71b69ee2.mp4?token=ISs_5flJRcVOkjJrs2h2sZWWdZ8iQ2MAZwdFFShgt5fh0VwFnuOLQWDb94lFM-bkZ1XkMNygUeD6h3aSbtbLTbvMQc0oDxtXjjOwp5Z8cjHloEW-nbRPMM3QzszUSBPrFNtxtuJ55miGMzJJFYDtuL0Mh91QkJBtWibSKhNTAuj0LbvOAWmJnd-siBNfY49SxkA-aHN1s4S4rBgPvy_Lgxrbo7aRc5s52-smLIZzZq0dHHfCmdtZtAwBejOhCw0OhL4Wh2pnm1DLCIArD8OANbKMEDPsa_3fS-rK_yY38FGSvWQxhTs0Xw2eaucJZo36zw2TTySNTs_5fBfvcQ5lIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش:
به نظر من بهترین بازیکن فودبال تاریخ پله‌ست؛ ولی اگه بخوایم این زمان خودمون رو بگیم به نظر من مسی بهترین بازیکن فوتبال جهانه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81132" target="_blank">📅 18:33 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V8TvKhKKTIBc1rCyXiHShMJuH1Wy3stxNV9tzK3pv0B64VlAMBclj-1rGOJN33hvpbCEbnbU94vatjqof_Vq46fXmaBHG3AVAw9ly3T79QQLIcEyKAeM6vzytbW2sJRO9BM7AmdVx-3rdEQF6sOdzW8gGaRPqHfJDpBfsodh-X_VlMmtqqU0RqFO_W14s-D_N9aigu5kQreNOFd7sbcnE3-b6rbtXHOPw2C1Vb9aZ0FcqtRo8QDVuTulfKoI6CPwWMQUwRFDRl6bmLB3ZipSxxE3fZyE6YM2PU5imhLf_JeTJOoj0v2LnIEJb397_cw6gdWkPhZ9AxriBQizG81epQ.jpg" alt="photo" loading="lazy"/></div>
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
  <source src="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=canoJX9IZYIXLErJEqPnO0nWYXSzAzIQEcGek5gW2c00PRjKlK-LT5pPF0FIYyj5-z6r8igE4GrxWi-Buwu1Pp09MuHKDI5IRPGvjVXEscLTlvWgvrKcld0UkV4zq00p6tUHjEvZjt4BavEonTa36uPjrOPlraqLhHy8pnY_-8Q5gPvj_RVnsnOiqLAVzVJnVelx2R_Sceq6xwy6fpnoVchSnR1gwGJl_JV34O7-MG4ZdIhn2Ct6aRI3VWnR8p-1fpkDm9xfZRgI7DAo5GlbY9cziiXb_8DFC8jrdy2RtVfEYIDAUOBrVEBbM8t4r-QiijzU5_UimHpU83543FrsDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72878dd77c.mp4?token=canoJX9IZYIXLErJEqPnO0nWYXSzAzIQEcGek5gW2c00PRjKlK-LT5pPF0FIYyj5-z6r8igE4GrxWi-Buwu1Pp09MuHKDI5IRPGvjVXEscLTlvWgvrKcld0UkV4zq00p6tUHjEvZjt4BavEonTa36uPjrOPlraqLhHy8pnY_-8Q5gPvj_RVnsnOiqLAVzVJnVelx2R_Sceq6xwy6fpnoVchSnR1gwGJl_JV34O7-MG4ZdIhn2Ct6aRI3VWnR8p-1fpkDm9xfZRgI7DAo5GlbY9cziiXb_8DFC8jrdy2RtVfEYIDAUOBrVEBbM8t4r-QiijzU5_UimHpU83543FrsDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
  <source src="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=hAG-LHKknBNgHEqjJNSgdHFcIMfYhDcSmf01MbnSAH4ICrFAjdLrkX6FCTu6QroE_GMrKhPBMm0JnV_RPdfufC7AfGRXyAfWuJPvUqFUQDVyhacaRUBxIZ4d7kIiXyU7aPnMH4yfzPUKCtJgk0cXhRXTAWRoDNeQ-B4nMu7LrKedwnt3KZaJZv4XChbagUZ1QCsPDP8SnGBZK7xYPkOz0aLLfvoMpo-PIY4zeqSofBeIfCN9fE0bB5kRBg8qN-asodcE3IUq-rF0kP2kGFoJpLn4z8F4rKXMd1fgrFDkQ2cKJuCynuciCbhEp6Fn99VyEfkG-wE86yNxvYW8yiu8wQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0183a12a61.mp4?token=hAG-LHKknBNgHEqjJNSgdHFcIMfYhDcSmf01MbnSAH4ICrFAjdLrkX6FCTu6QroE_GMrKhPBMm0JnV_RPdfufC7AfGRXyAfWuJPvUqFUQDVyhacaRUBxIZ4d7kIiXyU7aPnMH4yfzPUKCtJgk0cXhRXTAWRoDNeQ-B4nMu7LrKedwnt3KZaJZv4XChbagUZ1QCsPDP8SnGBZK7xYPkOz0aLLfvoMpo-PIY4zeqSofBeIfCN9fE0bB5kRBg8qN-asodcE3IUq-rF0kP2kGFoJpLn4z8F4rKXMd1fgrFDkQ2cKJuCynuciCbhEp6Fn99VyEfkG-wE86yNxvYW8yiu8wQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
