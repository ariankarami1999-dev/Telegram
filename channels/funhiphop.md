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
<img src="https://cdn4.telesco.pe/file/uHaQaZ6FegJ4UqJdkTCjuG93Fw4Y4pcxErLMJ6NeWfY8UJ-ad9ZyyDitgsnfLpyepw4ZnlslBdrWLlFvCyLy7AuCHo2oGPV6rxTHL6dOy4Jsxr2f82FNVxpMxvGwZTLX0s31Ie68ZRzYeoQguSCCkv891MFUBaQ_H854a71S4zjO4nr589hs_QPsXg_EIyp3gZiL3XBSbWQ-yh7fW3V3FRkrd6GfqVESksoL8_v-whFqgQWzMHlm5sMGA-g6PPdW2xQdtB_NjSge9ypsYcgCXOYbSl3ktuzj4aOQg3A0q88ksblakYm75H0DZZFXHqCz02ny0Wf5-PC8qkcvpKlFGA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-11 01:54:42</div>
<hr>

<div class="tg-post" id="msg-81660">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=ErOJJna_gkZxR0gp2i_Db0L-CKvUWp9PXrOW3uHWGh3S3FNLKj-1N6zUsb5U9kwAiEFGbFTakTVxnJIzYHD-0GwxNbNMr0Y9eiZ51bMyNGH_1DhAApOnAV8f1DtukLvN0iQyT7oAyIcxgO0Ts-E5rEvrNSadLFiIY2ENX_BTouVG7N9Du8Qq_xwbT2vWrKmlKb7DLpKHdzNeUMB-83TVmApg4yYLAz0pJWEHD0Pk7UqbhcKMJPvt8I6s6xz6fDyJybc0_kwmPjxG5Ub9CRmij8x57OBImnni-qnBTPq3HRRtVfBfafViMoO4xh5q5MsNqANEGbjzS-_kD0MIdA7BHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=ErOJJna_gkZxR0gp2i_Db0L-CKvUWp9PXrOW3uHWGh3S3FNLKj-1N6zUsb5U9kwAiEFGbFTakTVxnJIzYHD-0GwxNbNMr0Y9eiZ51bMyNGH_1DhAApOnAV8f1DtukLvN0iQyT7oAyIcxgO0Ts-E5rEvrNSadLFiIY2ENX_BTouVG7N9Du8Qq_xwbT2vWrKmlKb7DLpKHdzNeUMB-83TVmApg4yYLAz0pJWEHD0Pk7UqbhcKMJPvt8I6s6xz6fDyJybc0_kwmPjxG5Ub9CRmij8x57OBImnni-qnBTPq3HRRtVfBfafViMoO4xh5q5MsNqANEGbjzS-_kD0MIdA7BHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی حتی به لوله آبم رحم نکرد، وصلش کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 5.61K · <a href="https://t.me/funhiphop/81660" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dc4y2UgccIHJBDD5cTxaBAdySIcdVfwTwsKnB61x-OYwooigRMDiRdbmILhGRCBH6E8DGwD1b4h-ly3A8Pp6fDkXICa_UlHYtGshdB6zhU-MaaAKwagQpc0Ic6KPXmQ1tIyncyFIX4Ac-BylBNPtKJE59mXQMWHGSNB6LXTuDr8qRJU4VbSbQ6U1iSS6rEQNNYLU0Y9jNWJu5_86Z19tO00zJ2tPwDgd9z8mQDHOAGWjkIYuNVvXtUqZIbIzdc5ZLlmt4B4_UBG84bI_3OcCy8I0V6fsne4LtNHRqLJN0efCWsh643Rk7pxrpXXJyLfybNthNEzvw8el_qj6cHkXCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dc4y2UgccIHJBDD5cTxaBAdySIcdVfwTwsKnB61x-OYwooigRMDiRdbmILhGRCBH6E8DGwD1b4h-ly3A8Pp6fDkXICa_UlHYtGshdB6zhU-MaaAKwagQpc0Ic6KPXmQ1tIyncyFIX4Ac-BylBNPtKJE59mXQMWHGSNB6LXTuDr8qRJU4VbSbQ6U1iSS6rEQNNYLU0Y9jNWJu5_86Z19tO00zJ2tPwDgd9z8mQDHOAGWjkIYuNVvXtUqZIbIzdc5ZLlmt4B4_UBG84bI_3OcCy8I0V6fsne4LtNHRqLJN0efCWsh643Rk7pxrpXXJyLfybNthNEzvw8el_qj6cHkXCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویسای منتسب به اعضای ملتفت(تایید و تکذیب نمیشه)
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.73K · <a href="https://t.me/funhiphop/81658" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 7.67K · <a href="https://t.me/funhiphop/81657" target="_blank">📅 00:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه بیکاری اومده چند تا شات و ویدیو از چت اعضای ملتفت پخش کرده که نمیدونم واقعیه یا نه چند تاشو میزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8K · <a href="https://t.me/funhiphop/81656" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WLXMqGVvi6yjFHXwmPTe7j3c4NNoJnXLpvzYA-uARqxNS6SJ1K2AFD1RVQz1Lsua_zBlBrnBLU5dmWRpj6esEVnmXu_I_3vcMIH0Ypi5qgmKvddJYz2q4XJB8xvZOGdoSrjpg2UCmZNJw7viUeWEyeQeSKNhHSQgPZskTnczyJ5B9grz0GJgPKoZYdjXykABvtYNTd9KJb1i4gIDCUBlZ5T3xkrY8JvIPXLh2ylPGYeUwKQ07io6D1xcqiPmstzSaAuYz9U8ddRz4Wf_LY_4pv0CatYPm-f8w1GkDS-Un4lkKBj8-rRnOybWq65YMlZbfDdTdrOfzBBZTwvOEXae3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G5Sp_YUwDjxUk1ZQ1LSG2WVYTEMv15hUp7nPU2c9tNcKGQGmsmFriXKCKn48_8xa5rJY-4OGqIFmZ7q0riCUR1vSGf4n362ecDkvQuehmoMfN7dTsgs86tsgHQperguhzMFweSbSQkLQxdV4AhJpLQgbryWmKpX1VD5aIkpWaZSCqKDL29UslQN63H4Bvz5rvs3TrB7gus7AKaLgOo3-rXUm950Hc8jq-w-dnwFzZL42Hk10-YdvqBJt1kPXUPU9V9GrZtzcYIJrTV9rfmrOzhFuQM1foNDN1MH2Tdb9R7ENovmo3nZky4ExMVDjCcit3LT5_b_qyRPNAXqdlTizbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/81654" target="_blank">📅 00:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/funhiphop/81653" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/81652" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">زدن زیرساخت های نفتی و برقی برای امریکا و اسرائیل کار خاصی نداره
پس چرا عملیات رو شروع نمیکنن؟
چون منتظرن مقاماتی که هدف هستند در دسترس قرار بگیرند
اون موقع عملیات بزرگ شروع میشه
دقیقا عین ۹ اسفند‌ ۱۴۰۴
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81651" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r365DlzbjzLmilpx1DbPfFLB7iFjl1Kai6EsDGiMZpy0T_Oxdswv-8bc1vJKrNKUJ_r2UlX8qGAiA9ZWYdz4h85ZgqOvLVTLNqDNqi0uJKiCKBt8S7I0ULHXrXmtfcczoUpOMVsrExiI9U0exmlesd_KlwN5W6me-b68QSpPfWyC7DY4TL22CC_14ojaJtGTfvobSgPT8cOZHN13wqsO3JRulSn95W7YYxJ7XVYbZMx2302LqMRle6hX_IoBD8WwWped_dXTwW1V78084yadhTZiUG0WaWn6ZD8O-FLqpIgYSRegcbV7PyFvGoJGRwXPZZ86OS2Au54GGTHFG4TLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اکانت رسمی مرتبط با وزارت دفاع آمریکا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81650" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">چرا کسی از من درخواست نمیکنه خاورمیانه رو ترک کنم.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81649" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jbsEp8v_Q9QdmSV8IoiHJtuoihZsd0vWec6cgtgh7KeG5iCzsWgPwvbW43CzTvEhXPJCkI3NNeCp-lDAf-n63l4kiyBsVjFBksbS2odNFFV6fkpwE_T8nTzZJ51MLd3_cxClJIUOfPcn1TBuiZYOl7765IFdggZET-yqQp9Z9zenaflGEVEVUZ4jR8puuKnDoUCFIi7RaZVbzdnkXJe3h7Z0qPXQUYuJEiiOrfNgiIVp3ta-TlOEOF6v0OfwCo-GOyQhJZ5rT2WrhWx3hv_8GqpY7gta4OvjEtbN4WwcwK9obNUJaQOGxiFVvabC8dyAqJk9Gf53OSXBujdsz0h3tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tDmtg9MJFdPwtdiJka7kY_VuaoyVcfybWe1aPLT2tnPKQ91hdG7RwTV35JjFT-H2Py7-EdfNOWOoMV0UKbbmMz4oxRr9hlqKebHR8DCffjGQXMx6012uFBhq7fDeP231Frs8RN0s0kMeSMDS3tgvoUfars7XHi4PyfTeUtvvuAA0ubki_R8DWw0mAgVn1EyIrSYqf2wlQN-SZms5mOK7o5EWw4uPKHjH7E4dLPKG7Spimr18fcLZP7_0Neks5FF9dDvGBWWAtRSO_t9jwro-U0FeZ-HRQM8B7Ho14vaJYVa63rWI_9o4LDmvqyrBj2Wv-OW3Ye3xHrkKl9ohz95MXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iuE4fN4U6HOK6Qq_tReLrutcS5saEIEKr4ltftYGmAECTplq0GRvu90htwp-ch5lT5sTQnIBzsnRP6_ZGE9pbeI4y-P71-d867vmpAqaq6-JvxD0Ga4KQcbsrXZT4vvVcFhIDjEqxkg5AntTK3V4bWYuwE5GeWM-8iCvWYyrLlUi6ZxelMdgk2Trn4EQT1ktL2H6ly-gaNvyCiYE6WZp0TKYg9oEAWbJ2x9om4QIqmkPMifuyHNUgc1i5Ti9y6LgQsKQszPu7_rvop_320MicVDucTu1SeZqGnbCPWIH6Qq6a6r_XZTiZMFTwVnLTRVeSy6-qkH2NqNCO3R18aZVPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jaJ-Qeylylu_oWXYFeNtyp76-ZZWY3xqNbrJs8e_i7-bTkdZE6XZk4yFU8fLqy2jtr4YuPnMvx8xKuXMxD0P5juXFGPVwv3vr0CWHFrAuK_LuV74mgUIVFtLa8-lR0OXLYNTflLjTgNTWgaEai0fZ9OE6mWzjyVWZTmKhm7FAAZfnG2W2hf-tv3TYO2E1lsIrgzdQOATc1ZiP1lKv-Y1Qliv-4qnnrq_f_7jI_6ELBAai0_V7ofe42F1SdOvUymh1_Gh8LCptJGDwDwwShG8YdOmsAEdVtUchGxYeRHcJzXeAAzp6O3fgcqmDQbgpLG8LcvViFGTJQxAjMde5J6P-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NfKp1ltaItHJjktB9TK9KAHbfs7XarMClEcZ8DbGuZJF4ggdZJvzJftabM5DMKjKxURpKMKuJYhztJ8Q9L_nPYavDVPGSeoPQVP8v4aV1WFz5TzR_HyJ5LsgNwuWb6yM2wB8s4H1YxJZyWNRgG2AiTnR8zRxB-DnbDb3c5P1-LkGFiF-SXglYLeL9tPNa9oQTS6St2Rpx3SjZEWuEYFAc75m5dLjzFJmqPIKyXmA7wAwWLRXu8-e8hi5i8SYL2AP1c20erZi9iMm7rUdNilJsqtXzATQpaMcUbhJP4AlKGCEzZ_SaqAu0_LcqUEIbQZUirp3fiZyCgp2tcSniRNKbA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنها فرق شوهر عموی من با ترامپ اینه که شوهر عموم، بزرگترین اقتصاد دنیا و جهت حرکت تقریبا کل اتفاقات جهان زیر دستش نیست و بلد هم نیست تو نیم ساعت 37 تا کصشعر ai پست کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81643" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">#پست_دارای_محتوای_رپی
سپهر خلسه:
نیلو یعنی عشق؛ شایعه طلاق و خیانت درست نکنید.
✋🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/81642" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/81641" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81640" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">این سری، این سری دیگه قطعا میزنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81639" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81638" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81637">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">لیست اخباری که رسانه‌های رژیم غاصب صهیونیستی تو یکی دو ساعت اخیر روش مانوور دادن:
کانال 13 اسرائیل:
به گفته مقامات ارشد، انتظار می‌رود ترامپ دستوری برای از سرگیری درگیری‌ها صادر کند، و این، ساعات آینده را "بسیار حساس" می‌کند.
کانال ۱۲ اسرائیل:
یک مسئول اسرائیلی اعلام کرد که ایالات متحده از هر زمان دیگری به آغاز مجدد جنگ با ایران نزدیک‌تر است.
نیروی هوایی، سازمان‌های اطلاعاتی و بخش‌های مربوطه در ارتش اسرائیل در حالت آماده‌باش بسیار بالایی قرار دارند.
انتظار می‌رود که هرگونه حمله جدی به ایران، اسرائیل را وارد این درگیری کند.
مقامات اسرائیلی معتقدند که ایران ممکن است در واکنش به این حملات، موشک‌های بالستیک را به سمت اسرائیل شلیک کند.
یدیعوت آحرونوت:
نیروی هوایی، آمادگی سامانه‌های پدافند هوایی را افزایش می‌دهد؛ سطح آمادگی در نیروی هوایی، بخش اطلاعات نظامی و سایر بخش‌های مرتبط در ارتش اسرائیل به شدت افزایش یافته است.
خبرگزاری والا اسرائیل:
در ساعات اخیر، تمریناتی شبیه‌سازی کننده شرایط اضطراری با حضور یگان‌هایی از آمان (سازمان اطلاعات نظامی اسرائیل) و نیروی هوایی برگزار شد.
کانال 15 اسرائیل:
برآورد فعلی این است که اگر ایالات متحده به ایران حمله کند، "اسرائیل" مورد حمله ایران قرار خواهد گرفت و مجبور خواهد شد وارد جنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81637" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH_viWI_DfNpeHBjq9N4Bguf5Iikdg8kG6lSMTsRzRFfqfP7d6tNo_hi-si-HpVM9nJPoIn_f2PiG4EoIEOk8nBNr0YpazTJSpZdcnm96ca5Ufts-Ax2EfbtNb0EQ-b2d5RiegX_iD1rkDxJ1FhGWO0LoXK5q_UPKW32jX63gXaGX-l8HtFlTRb_i2q-NKchEg_L4N3nWwfRz3VBZlvI7EdbNuPHG3isfHisKvukvYKOKAMuUa6XS4uxvzzzNQgRtA2WcALT2pmd1lf8zTEB7ekgIhNX-cTw_sEVWBR1i4Echs8RRxXyCT65cS6VdkuS_HZhZ2CaCw6O2So4eMhGtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81636" target="_blank">📅 20:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HpTzmswMTXSXKU0QNWGeuWc9pttPRxhJb_vI8AdcRqxfscCZzh5g9jSyzG10NEhVaBKQSeu_QoYCvH0JazPsq9ptN2s_xDojMWxOYrrjUWu5Y35dSg-uyrra9e5t1YYVtABZtGED8oZ4gMOF43Y_BjYGWoqmc73ZlNgFhWHYkJjAyAnXco5j6w1hn-1RrdFfCH5fUhBcbpZ3JKsi6-bJokn6zv1FAgrv7UsY_6t13Oq6grK2D_lWRjS9lvzMe4PYsIzrLgbF42IsvEnK5hqcMw_-awMeSeURsuTNcQ027sNzLf1PuQ6l13goUqlNv_FExlUuMgfl0LtdvrxJY-oBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که باور کرده ایران ابرقدرته نویسنده های این سریالن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81635" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81633">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗽𝗲𝘅 𝗦𝘁𝗼𝗿𝗲</strong></div>
<div class="tg-text">🍃
به فروشگاه ما خوش اومدی
🍃
اینجا هر محصول مجازی‌ای که بخوای پیدا میشه
💰
〰️
محصولات فروشگاه
〰️
⏺
انواع آیتم و ارز بازی‌ها
Ⓜ️
😶
🎮
⏺
هاست, دامنه, سرور
💻
🐧
⏺
استارز و پریمیوم تلگرام
⭐️
✉️
⏺
اشتراک سرویس‌های پریمیوم
📹
🤖
🎵
⏺
فیلترشکن‌های پرسرعت و پایدار
🏳
📱
🏳️
🌳
قیمت مناسب و تخفیف‌های دوره‌ای
🥢
اعتماد شما ارزشمندترین سرمایه ماست و رضایت شما، مهم‌ترین هدف ما.
از همراهی شما سپاسگزاریم.
🌹
Channel
▫️
Apex Store
📣
Bot
▫️
Apex Store Bot
🤖</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81633" target="_blank">📅 20:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVsgxua6LElvKqHMSk7sm30360GOloOiSa4CIqUILIXw3pIsH9JRXtNeepyyowV3xNp-fpkiKwn7qwkQCaNF1Ujj_aSxX06kBDd7hI-JffxAgEuQxczI9fmDdsRXch11WqcKeGGz8cVg9cLtfv915T7VyzUU1e8xtVVz2rIYgsHAV8EOMKoduaLzd7PoWksvZsd-sylO0HfYBgiG4k7j-GkbmHtEksj88J6dzkonUgOx3Xnls7eOnO6NtOX2gg4JxEQnSuCTOzjMgLAWOSHAHzzt7iJ6YbdACvMrJgxEfV-HpyyP48MdQsr9xG0u_cDXr4R9dy27D7Y7eC1zd1uTxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که این بویان کصکش اومد بالا مسی خودش ۲۲.۳ سالش بود، بعد میگفتن جانشین مسیه، درحالی که کلا ۳.۴ سال فاصله سنی داشتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81632" target="_blank">📅 19:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gjbc1r7n4hw_wVCEr-ebN5J0VnOIhdf3brjgRs18AGERD9vl-APt9s9GYCDns4Hbctlp4r5i8pB2Vp6-ktQvXq1BorD6B47vEv_A7wZCEOCrLjLejWAnMOnlgRymBflzuBSfeDpOo6KL3Uopk-1TfZaLBYlzlHvUOwnIMdBlYgpSe3aE7l2VA_FGXvQwwGDR1lncqjnaLXS8eljIJCZqq0RzBon4xweXsUU6o4KpHHk_63nzd8mcfKwbcySK626Tf4aXC8eYT2Z9ozWN2z-9EKPlROaYnxmNbdkmYvXMRTvy7Kz6QD1czosRB3zjWkW12OOnhEyeQ3hTX_WpPK3yWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مرده که توی سریال کلید اسرار که قبلا از شبکه سه پخش میشد میومد پند میداد و همه میگفتن چه انسان شریفیه رو یادتونه؟ الان رفته پورن استار شده و بعدشم عضو یه گروه تروریستی به اسم FETO شده و تحت تعقیب پلیس ترکیه هم هست و برای بازداشتش ۵۰۰ هزار دلار جایزه گذاشتن‌.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81631" target="_blank">📅 19:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">رسانه های نزدیک به سپاه: اگه زیرساخت های ما رو بزنن؛ کابل های فیبر نوری در تنگه هرمز رو قطع میکنیم تا اینترنت کل جهان قطع شه.
پ‌ن: مشکلشون با اینترنت فقط داخلی نیست انگار، جهانیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81630" target="_blank">📅 17:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81628">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzH7mWXGopTIACOBGmb4qU5jr23xVh_AZ6NbdTAjYaJy3UT-TPYsfwKPSWs7RcPIkeyBacCODssdPqtOLp9076r7DUUUjQnZQeQWo8qXaPyo3ct4r9-kZu_Xpgu1yUsHumBw490V0KmqA0fHOXtpL_IodNbUOV5_eotrbYMwH_UQg7m7P88npgLUtvyK1FE7jeC3M8ZyK12bcNOacw7c-A_KGsi4RPGdykbLV33l8d3OomF3JnCGtmhPBgZvX9xObkuyFAIhdmV8P-Hy6vgZUtRk-iIZ5kdRpHy3XKXwSZo8SRSKR6NTUDAxzzc-LzbOw1goCK_LdHChxaABfBeJlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=ZO7HPjiJDiPEVD9McVkgLdEHS7jg4rMWw7s60_SV9qR9rtjlKDjTlBFmTNjHlIkJpVQZdHq7YUtNWEJAbVOP0jtsvopPRwNrettDE25f84mSrQcBsLHMilgh3-Q409TJyutO8wo3CBoWDN6GBGwGdlVvZfQJk3bGRomzvaerayPrUQOiLzhgWJmDaAywt7pZG3StBqlwX5ATwvXJjmNWukdg9sMtw_zqqLk0j_X0jgY42yjkcJw1jht8NwhGfLGjUXVTT5SlYN5lk8TTzKV1uT5z74mRhCwzWOa_D2tR69k8kNhDGn3_jtXjBkJnyfNsQCa0GjWYoNracAOwzy0KRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=ZO7HPjiJDiPEVD9McVkgLdEHS7jg4rMWw7s60_SV9qR9rtjlKDjTlBFmTNjHlIkJpVQZdHq7YUtNWEJAbVOP0jtsvopPRwNrettDE25f84mSrQcBsLHMilgh3-Q409TJyutO8wo3CBoWDN6GBGwGdlVvZfQJk3bGRomzvaerayPrUQOiLzhgWJmDaAywt7pZG3StBqlwX5ATwvXJjmNWukdg9sMtw_zqqLk0j_X0jgY42yjkcJw1jht8NwhGfLGjUXVTT5SlYN5lk8TTzKV1uT5z74mRhCwzWOa_D2tR69k8kNhDGn3_jtXjBkJnyfNsQCa0GjWYoNracAOwzy0KRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید سیدنی سوئینی برای برند لباس زیر خودش
.
پ‌ن: برا آخرین بار ببینید که نت قطع شه دیگه تا چندماه خبری ازش نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81628" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fanzkOde3zOTJF4X04M3g64p6ldwHSMlNN6QRSblWGmd0EuH8BJR9eluTfqbl_eGNTTOh1Ow0Co9iyIc_injfF3OQJalgvPLHnx2qzDXPWCrK8Ng2t4pD_zueVrCd_uXjoBy1iPivjvdE50boXgg0ZXLulyX0U0M-Ct_jqb6NXMZdG5NSy-v7k5Q_VK4Cv8uTJZ656qkiyYb30RYlnuF9DSh9oT4qPGa0QJOk4117WsNJI-3JLsVlo7PwpNoBjqs-iMBindRnusrJYMW6RCuNjZhmzmd90EEfx8cm-zxPTxVMjJcLwnY_Kb5x_HVNfQIddQWO_T4DXNutHJct2DCUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/81627" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81626">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">انتقال لجستیکی آمریکا به خاورمیانه تقریبا تکمیل شده، الان دیگه همچیز به ترامپ بستگی داره که دستور حمله رو بده یا نه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81626" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Drumiq-NW0PMBq0eqmzcDLRV1AvfRo_LDid24RL0psQTqi28E1bLVkNjfBSSnHJ8CD15g-VaA1nPt-fcpj3MtvcS-_bn3nwWPVrm20dmQOxPWVVkwpndoHQcrs2u6CI54_CgLKGhUZnMC_09fVXmcI0FnhVLVIshH15rh6qSTPedg1A8tNR7iHUxRwxuuHjtMsMpTG4qF3etxIB2JrxaiHfDE_ZpmeV8ebSywcmGo--fh-szWxz1KU9guqXfQP1c1ZQjGVBas9u3Kqndr4YTMlvW7TZeQDHATiGXzW9K9Lao2TbYCHmKSQmUAn7SOskAw-Ee3CnOcHn6nXLn-m3WIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تانک‌های T-72 لشکر زرهی ۹۲ ارتش جمهوری اسلامی در حال حرکت به سمت آبادان و مرز خوزستان با عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81625" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">امروز صبح آروین خیرخواه یک زندانی دیگر اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81624" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81623">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اول جنگ ارتش یه سوخو 24 فرستاد العدید قطر رو بزنه که منهدمش کردن و تازگیا جسد یکی از خلبانا پیدا شد و برگردوندن کشور.
ارتش گفته این ماموریت 4 نفره بوده و همچنان اون 3 خلبان دیگه مفقودن و دنبالشونیم
منبعشم نمیدونم کپی پیست کردم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81623" target="_blank">📅 17:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR7ee0QGrtfiqfqOEhdqaIrJ0Gh3oDAbeeUHPaPBX1RZBNk1d22SPmXgyQdm24XH7WQunWy00sL4VVCXe_Jojm5ti7ksvp929PC4RRIUVDg6M6X-ueFG5dQmyzKvGHc6KtSL49-AyLaoJMxQoKcaLrEojjH8mA51FgTEyuhJnotFXd3bZ0GcZewu-NdG0FEZgEJPz7xYqp5K0-8jZ3wooxzQt53Iv7pvvKxUwhNFLzh9grkaNWQ6QfDA8zZffiXkobP1xN0PdoqKFdfEvK1FUAz_UYJs3uCDi5CgS_xgX-LbwvZfnymyku5UFWejF5YmvwQI1TFDQICXHskzCwWVqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کمتر پورن نگاه کنید، مغزتون گاییده شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81622" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">سی‌بی‌اس :
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81621" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bfo9DboGhFeE8P_TfRyOP7u1V29xwlRW_LpbDFn47ztlpdo8D5pCmhrwgtPIdaGl0JahWbzxmbPAjrRCSJPzNm7N4pAXIznBrvonkedVIjSnTVwenTdUlK9PA7pE4lmyB8qpT5il3JplkkCO7eKQj70uh8LArQ60fvOB9WHajNU060J0Ji5vSJKS6N5dDH_ZaJnKXW7HvabsMI9BmBFYVkLthKvCB04DaB6fFZRn3wOfU59GwvAF5fZ1kwW6yK6nzbIy_1MjG8O-hGFM0MUNBQd6G7H31KRDRlBkMUPuzb0I1BSKzASTybRuhftrkblTFf43jfWpeCaIWqxlI8pfvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش چارتا چیز که ندیدیم پیشنهاد بده
اینو بابابزرگ خدابیامرز منم تمومش کرده</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81620" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RHH8RPavMNqVdcuc-dg0BCv8XwSLcalNoJFewXZT4O9tA0JOFD2BWKbyoFLJ_pqIlUZw_-WPooCOeaRwcpVfpnrHvBHYMlRx68AvzRBGHHdDhmN7X3inrDcQM-_Ea6uxJiKoku-_emapOiBzs7BD_m3JQ50ekokh2S9w0S9Yp58yNvfR7Ea4ATTdctTMIuQ9PhdSWnlXbmPKm2aY2qufpKVFf3N-enSWusy4Jn8nYT0iSyDQjx2dAeooOmeAXn3kcUkOA_Vva4BBvapByTBBqWcxq8MGGz5wYU8SGP5oMONdugWOmedKrQltLN15XUpRcdO-iXszDCZr5c-s1cU2yg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81619" target="_blank">📅 16:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJ4FleRgfsyQqS8l7r5_A4aruR6c8IrBAx1RK-ro90Uc_SbPriyavH2BXTePTN6LencOlkDRDXRyIey9TSL97dLJ8iDkEiQkTtiSO2XxXVZJuO5RNWGj68cIrwmRTZJD59rD2MJxiWUHUGAumaKaU5UtcpIfCWSMdWiuj8EiBzYYbVJv3-LDkwbvBYT3dnMptzDmOk9gtowRejCF7BnhvAxNGBNaPZg0_hS9bmGwXqi-GUSxAaiWKNoNIbvF0YQoQlx7R7ALgortt78tssFOHfu8GyATOGUdV-qZkfKIcY6n4HqVs3QmOdRnTJwLgb7yuT_6b1MT9N7gRREICUXEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگار جواهریان جدی معتاد شد فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81618" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81617">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07811532ee.mp4?token=Q3ZQz1k_ZMbTEg_7dDcBe04B_iLwuBBk5IUquUrFOiyINUf_UcujLOYcZ9eVSXyzg21OySeIFcV4AI_DyELxtTeB69gTWtG08RkP4HC-zVujO7plJfPLTp5LkplYsU2_jWU739G6nQ6nrfEbOvdkrxG-pQPIek6k1LtZRX2hZ0ICLIjUsyoi8DomfS5lnrKUC6RjHP6QJqB0LScM4NbkwHB-1D1dJ0spaqegG4XviG2xLsAA-gMAGdwBLk2Dx-5mV59KN3YnrnWAjzYXeiIp9r8bx1ByKswRQwoLZVUyVO7Xx2LnJX9LLlxk0e10UxDOJu9VF6-DZnGSGa1eZ9QpeA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07811532ee.mp4?token=Q3ZQz1k_ZMbTEg_7dDcBe04B_iLwuBBk5IUquUrFOiyINUf_UcujLOYcZ9eVSXyzg21OySeIFcV4AI_DyELxtTeB69gTWtG08RkP4HC-zVujO7plJfPLTp5LkplYsU2_jWU739G6nQ6nrfEbOvdkrxG-pQPIek6k1LtZRX2hZ0ICLIjUsyoi8DomfS5lnrKUC6RjHP6QJqB0LScM4NbkwHB-1D1dJ0spaqegG4XviG2xLsAA-gMAGdwBLk2Dx-5mV59KN3YnrnWAjzYXeiIp9r8bx1ByKswRQwoLZVUyVO7Xx2LnJX9LLlxk0e10UxDOJu9VF6-DZnGSGa1eZ9QpeA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید به مناسبت ۶۰ میلیونی‌شدن یوتوبش داشت با بادکنک پرواز می‌کرد تا انیمیشن محبوبش یعنی Up 2009 رو بازسازی کنه ولی یهو بادکنکا ترکیدن و با کون سقوط کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81617" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81616">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81616" target="_blank">📅 14:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81615">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81615" target="_blank">📅 13:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=EW6YAMb6b3Ry_rN0UMIcVcqK7azPGrT8uiBy2Cu8aqEpg1PFjXIJr3zzlNy1jB9bU5TnUp9x26AHBEsWuN5UlTFaMXD6WYAGlAaX6_M8Tw1wqZ4OQSQ-0gplW7-qtH4jwElOPBgziQRDSvAnGZE5xXW3cpiaenmKjTD0r0kuKhhHOHjJm-j4opM2gbuVLSOZqqSndtKt0M8qxU4GKl1kM-PrOZrediSdK7nRUJvwa3T3Jd0FOy8sv1MoOKW5O2dmxUzqZ66I_7kWTkcw4cWqXh_3SviTUB1Es0VeHwQdOhV65w3qVSM0Utczek82bIH00zBPM2bTSM03BuYCbT1Qeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=EW6YAMb6b3Ry_rN0UMIcVcqK7azPGrT8uiBy2Cu8aqEpg1PFjXIJr3zzlNy1jB9bU5TnUp9x26AHBEsWuN5UlTFaMXD6WYAGlAaX6_M8Tw1wqZ4OQSQ-0gplW7-qtH4jwElOPBgziQRDSvAnGZE5xXW3cpiaenmKjTD0r0kuKhhHOHjJm-j4opM2gbuVLSOZqqSndtKt0M8qxU4GKl1kM-PrOZrediSdK7nRUJvwa3T3Jd0FOy8sv1MoOKW5O2dmxUzqZ66I_7kWTkcw4cWqXh_3SviTUB1Es0VeHwQdOhV65w3qVSM0Utczek82bIH00zBPM2bTSM03BuYCbT1Qeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با ورس شاهین نجفی دابسمش میرن، پس عرفان بدبخت چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81614" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81613">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnY_If6rQoYGnlUOkStwjAh4pwtO6W2zBAKiY-cVl75M8QzfuPQlCha5L0_9UU67_OQ_R5VKhFeGBOT352_Z5MPfk2ppba_12A5tzIfbazENgX-kXK-VkvLoxdDCgai5YTTc5B_R7yxgyndcotS6TzPwhj55mM62O9u43fs3-8XVqUXZ7a_abOgbj3TQ3JlArmq-Wri03cvF38OwMqHDCv3RgrroZa_sH-aPw1vgBF8venDIB9V8lwq0ZnfLECQK4yK-h-90SwP0bV_bmoWLKC5Uwtg001tuGJltsI0_xRQNsoJgzOJl_q-h1NmQHXNdeTfwitjWTVfLieSDjNLvWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81613" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81612">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پدرو سانچز، نخست وزیر اسپانیا رسما به گوه خوردن افتاده و خواستار یک جلسه اضطراری با کشور های اتحادیه اروپا در خصوص بحران به وجود اومده توسط مسلمون های غیر قانونی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81612" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VRtMW0RTg7t6M0TlB1xYT1Rp9WZ7779xbaww18GBuO1rm_89LUl8uUIsI6pQ3H2GFDiw2nclJt21ntLlHUmVo7Z8hNR0uSJ6dZFZeVmKVFrgSWwKXzEYFKYWpIzvg-zEuJpOziqICV7tXiSTL6oC8lybx70bel8vtrXbom5en5p0kW5Fpnk1EkG5fpRemZP-IC9WuNPlzT2eVUUBfhSn245mbooshkouOU2UdeWzbjWhoSafk0o0SxA7XQV9u40LTfoduOfuCyQynQN5hzR_lrwJkpgFE0gaqdMyTgfDhLSbkxuionRgjtKnk6nV3HHkPBBNGUqda2VyR-xSYek81Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا به این بی ظرفیت چیزی نگید از این به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81611" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امتحاناتون بالاخره تموم شد، چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81610" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=QWOUBrLFlsx4DE6S39AUQk5UIkdBmoBQEHGhLils52G1SkE8lSoFUtePD7quzotlV5u5NC6faJiV7xlCgHKEeTZ9g7luP36I1A27z1oA_qn-4moznLMw0O2pXW500vO5mf2_Z6BVVYI4XfXcIKvoul5Kb6HFoEFcx3f0GZ0UIOFC6k7IJXUn3_cv_RYrPEhUhaGB3RlEhe6FUIZ69IqsZKiuN7uiiCA_jk3CO6MkZh2k3cvKVFVDW9YkZjrn54ZLCoNV60zLbzTufdVDcH0ovm8Rp3YnOnCfq0iwXbhsPr8nnCHzG2MKaqBeKl4rQXvNoI_a3snM1fXQzDA5-EMbxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=QWOUBrLFlsx4DE6S39AUQk5UIkdBmoBQEHGhLils52G1SkE8lSoFUtePD7quzotlV5u5NC6faJiV7xlCgHKEeTZ9g7luP36I1A27z1oA_qn-4moznLMw0O2pXW500vO5mf2_Z6BVVYI4XfXcIKvoul5Kb6HFoEFcx3f0GZ0UIOFC6k7IJXUn3_cv_RYrPEhUhaGB3RlEhe6FUIZ69IqsZKiuN7uiiCA_jk3CO6MkZh2k3cvKVFVDW9YkZjrn54ZLCoNV60zLbzTufdVDcH0ovm8Rp3YnOnCfq0iwXbhsPr8nnCHzG2MKaqBeKl4rQXvNoI_a3snM1fXQzDA5-EMbxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NTQ4jS2BI4JHEpSUYELq86p_JF2sPR_IEK565nNpIzpS5pLVO_g7Qzlgb6JUg49J1KrdMCn6XpwMdWfD39dSSD9neCiZbFdzUkHRrsW2a9yXwM11faO5wn6Gtcn0OjhZ9yO0Cp0RKAWOh-pk7e4VmG9tqh8bu1A4Z-DfvUYEuOENEWGGn50odjm3ZDUOwyYofXoXeNix5U1ev6UZ2YodbgZ7sSUGzFKYIciGJfse7UA0KpNww_cyv-BeK7SHlOvtXCAj2EA0A59yxBfT3t6UZmGy-5oQtkA0_UlNmMlmAdV1e20qaPrKfkOBxpY-bDt8PTqqioQmgP2ydwJ1iK1eJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwIN1gwjR7i6vVKNVXXeXBApb76JGdyGNXOFn4CjHcsI-fPDtpEtXW-O3tzEperoCr_FVjF5MAe9KlCg2EDIbW18uVJA8D-oPZZ68I_J_1T-H_ikKy_901nh8Y4LB_YyCCHZoNmdPUc0pTlmSFXYxN4h6H64dflFdkaBoFfnk-Vkt_8iaSyYYro_SC-plLrSiwG36XZMn-Md5R9n2ETvBKaMzifguchpnXzeTuUM07X_gpcvyUVb12hq02CkEWmgEF1c6vVXgI9mg-9O33QoDthgi9ew-uEkcjhFev5-XlTzD7GDVlI-Dk1LLHJCS2iczkW6vU-QA1G3DoNfG0mGwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=NqBYRyXv-T5tkv0n7PP42XCTFB_CpXWKSmELoBNodHzq8boP0OoPkgfb49w96cz5aFVocpm2cGXISxQ18cZ5WE_BcqNM4-1RZzKpyoeye9QmNRW7zEDhs7aKEZ1pOpheEXTiIaB29fnaIfNli-v3HRr5pIMu-6P8qujN5OhuK8iCLoBwfCuqRY1Fb5WADlxR_ACLXoOHC-vGSdrukcfpW0jcASM0HFgp-Ns2DQycW1NZAzKQU62LZL8Qk1GLDgqlgL_1a9mrmBJss3WaT2uCIVbrfvHSzMHuoPUxyphJyXuN68WYR9BFOGso8w-8Uv_b7zqbqMenZuu79CWqV6l96A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=NqBYRyXv-T5tkv0n7PP42XCTFB_CpXWKSmELoBNodHzq8boP0OoPkgfb49w96cz5aFVocpm2cGXISxQ18cZ5WE_BcqNM4-1RZzKpyoeye9QmNRW7zEDhs7aKEZ1pOpheEXTiIaB29fnaIfNli-v3HRr5pIMu-6P8qujN5OhuK8iCLoBwfCuqRY1Fb5WADlxR_ACLXoOHC-vGSdrukcfpW0jcASM0HFgp-Ns2DQycW1NZAzKQU62LZL8Qk1GLDgqlgL_1a9mrmBJss3WaT2uCIVbrfvHSzMHuoPUxyphJyXuN68WYR9BFOGso8w-8Uv_b7zqbqMenZuu79CWqV6l96A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7mf2kHcCXu1fCcesw2mDnM59jH68ASzIqruT92OR6mU8_iRwG-uYr1IiRxxhBMpXiKZY7_QcFZ3G5dAZ5J_-whTp_MCkek90xOjWTFS5-Chud6vufZ8YQOrdJJCI4iEzBuXRMZp-3vJe4p6gTGQDlQ6yv0DSPt_SCWWAvnUJwbgU2yu8ghnv6JqviD097Ij3bICNhZXL2XCGKdshF_qFRq0Cm8RATrFPaxIPJTgKT58M7SQv5Bz0E0Oa0HiJPeQJSrwm1_sFMrAVDDZtkU-lTn8KmUM9JmaVDP7DjJxfDPVh0DqTuxkPhhwhhmJiSNy00GC-7uNITaf6Rjn-27Gww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwoo1fVrIv92uTFkK94hL8adisxHh91uroe0Q0x2A3LTvSNVaeE47tJivzpSHWAK3pDlaqPojJ3Cd1Cu1k2JPYsh0LIzE8eD29V1irJuBvp6HVTZts7kGixOebEkbIcobYBlq03Gd3CjFdQ867XqKVrMVFG-ekU-ZsiaKvOG7sSQ24nYkKcJmFu98XMJy1MWpHCeK0vDfawwCLYmF_tEKvm-U-pf07QZMRFq6GRLec6XLffezhqM7Q0CEFjD-MKEGb20KH-ARRW0RpahPZxbWpi2IarwLWC64kb4z2Qp2iKsbl1R-ulI7h0885GCJktGuSRBewCUKGKrwdCr02MGQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MybAvruhJhDtsU4WcZoHjetT4jwKHHypexAKvH_Cspxjr-1S1Mb5HTWjOk0vcWSC14c1KTvTyDKdblAsRPSzASRmXbWYm15UYv_q_wUyHhlV767wypJ-O0Mkwjim4h2x8gGUtvdbKeDHcPhrx5ZyQx1VgqeZvCb8J2QnM_RjGOsmTLM_IneGqTcV_LIY0RO2GtVBuV6GhP1p4QOQXJtJUj4MCcZ-s7KwT7ozHGOFCR6zrmaxl0cTSEjGaMo9jYBLytIOEH701S9xtUkP08mimw33JZfWr3LEO1xjpjbkbey6Wnw3O9HNS385cR7prhdRYR_rBMcEjAAeeJ4NrZJPzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=na8jr_eFhIiEv1tqPHNvwB2BpHaoLQzlPd6egJ4goesm8LGFHQyo-wXhcSJ12ZWFsSD8ej6t8IIiWh_w-2HltYnUoevkr83Kg8nj1toQ9JVZ6jjuMqzKrwqEy6P1KZsOjr_TY7LAY50kthdsSdIx8kYxW3d7obE01CXNriH1QgEpTkY6EiBb9NTWlLpArVYwBrJJDUy9RbDzx4sBQ_AGJ15_jYd9Iakt69aCndNfhfLInagMnCj24bBelTSacGiWmKS1CqRKcKJVQZ6_-MVZpQcB8p9_E6dHL9u48xNRdamLgBD3l2orfu9FzA5XdricXBOz2L-ebsMunldTt8U-7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=na8jr_eFhIiEv1tqPHNvwB2BpHaoLQzlPd6egJ4goesm8LGFHQyo-wXhcSJ12ZWFsSD8ej6t8IIiWh_w-2HltYnUoevkr83Kg8nj1toQ9JVZ6jjuMqzKrwqEy6P1KZsOjr_TY7LAY50kthdsSdIx8kYxW3d7obE01CXNriH1QgEpTkY6EiBb9NTWlLpArVYwBrJJDUy9RbDzx4sBQ_AGJ15_jYd9Iakt69aCndNfhfLInagMnCj24bBelTSacGiWmKS1CqRKcKJVQZ6_-MVZpQcB8p9_E6dHL9u48xNRdamLgBD3l2orfu9FzA5XdricXBOz2L-ebsMunldTt8U-7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zs4E07B4fp5LGerUPmDYs3gchOe4lCd3gXXj8FInvjOSxexuh9ukjVIZ1j0MTJ5zXdRHq1fcrni8Xc9UozM9yOJJX1kM6djKgioDNHUQTUS8xAVXtyHvHnWbIBCravXTRvuMF1eAXO_GEIrwvhg8O5dTQcE5MEHrjviABQyDFgtclr6xCipjPxw5BH4GUl6MzbRerUcvHNZd2EdJ8zBQZ05BH7hwGVbeht-7VHdaRXfIP6xLY9QONrQGCmBgdvdwFXYRWRiv3LRz9RGnsHICFNUQfNdE33DQHTx8I9qcaNOyo4BHUikRuo0A6jHbtc6pMMBD-Tk7sY4AhlpsdXrp6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/va3ThcdlGJdWWppWXrVh40idLvetbHPaVR051k58Clo5eUzbnqD2MNj7ydV8vDiVg7JN_Q7ttlVZ2gjpRErQ4kfhYbDZZErrq4X3qRSs-NaU6EaOu8CgRX7dsD6RPNcu3ny3n-jRuWPzIv-wqnnBnwyk2fIKEseN2TZbr_wsrEi7_2KZMylJIzHRNoKGWnvdm_r7Lk9nFvbFkjhUTWwjml8aPwjoacKZRWdys3UWia4JBzjT7sgdTD6qr3uKbsLr7peEggjOqcn--DB1QJoTxVK59H5_N6cwTXdip7io5hhBQq1vRrVcOWrzdInRd3pKQVw-u-Fv5uWUmuKQTgiM9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T6FwRwFPCprqsVAVTbDzcKYi2Zmu5i8ivQU-KZM9bgbhKNSxarBHvsO7VJRmMl3Pf5Z1srQWO0v6lNDb8ZjWzlbL05R5fve9pfHiDtySXf5Y4jzDtKKarYwMhiAxOa2I05NaMbkmS_Z9lmoLO8_ruhl5dqo5G7FQMz546Mz7JVElf5ensG2AZYriIrBATgzoLZEXXT3fi0h9BpUgbiOC3cA1D0EPwXgguVtzo_ZrycBKL384gYk4eDVUVaSHKaNoiXcrF86Fs4eoPvzdBRErsfc-lqZBAO8CmlVOTZlvI7o3rapFOUgBIiO53-Qd6ahyqIpVsRIZ_O_AzwIjoRCyLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81592">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj0kE4b3WN8qeVkDpP7VxUVEA-e65O0lE9g5ymQ5LmfqeV1rDqSQJmCRwN4JMCcoh1d_m59KgS94w3UrPN-CjQty30TjybtdKTHsUjzM6X39tI3I2rhCtLZLOROKVcdSOxvaY7QwZXJnIp7dX38UdmoyKXoHY678MaGYFAODP7-4a_VLeJesm3sMhNX7PsFR2iEdi6idl4l7yWQsO-0w1VNl1N8vowpEBppghkVhcR9ybpKJFxgZm3c7EFMuyHqRtpP-1OU4MyltPh2pNsObiT10FtmzwAr3kqjU3g9gSS1qJqow1WKJSuElBduw-dVUvtfC1TImfvkXWPHgh4kwCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#شرمنده_بابت_پست_رپی
ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81592" target="_blank">📅 20:51 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81590">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VU3QACddeGYwy8YKH8XtO9slbk7cExLcWBgpmLFQQqydhDmYKaYXrtQX0vnvEnWqLfEvbU7Vdvbltws5tkcWaB50w48U8hcxW-2jUJ4XP4vovYbu9Atqn3s2UFZK74B-sn0KMZU49mHfWSK_GQ7QFAE_DKrRO4B3mGmXqvfQR4N3SxnWbj1BXQ81_N-eAiXheSfUYnDdBWNWI8YWICbzDYSBAjiTMtqgaNUCrG8Vi5uRN1YqNoqz37h3MCernJcgb6GVHZacPVPVvP5DtExxrwtit8mcfaQq-wF3-5CsJBs9xZkTPPFFXND6D9qJ32Bg_4dP7uMl132brHA4KYSsUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد
آقا تو کربلا رویت شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81590" target="_blank">📅 19:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81589">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMcgjdUh0X35PJAioMIgt3uWD_0s2VcKRyzxsV44aBvmZGd6WYhssE6LLU3zH1yP8xyLtRQJeztaZsaSy2Bk3OZJYsGg38BToeG2-KYrOrgdiP6U79b2ZlgF0tjd3SFp6Bi6o6UxbCO2IKsrsVqICGDiotCQp9qw-vIezUlp043-EYid88RpIgchZm631QzVR0i8jHcg321_MBOsd7_3Jlv7s-kV4MZIBc-qSOGJwtbHRrrkG27uS7msx3X7vSAOuaOJNFBdU5UMqo5KVy8Bo8C0qjVn17PrnOZvEItW7_a1zR29VCgLIZAnZTvuqoZIQpPECbkrER2gWd17eKmWBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیپهاپولوژیست هم لایک کرده بود
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81589" target="_blank">📅 18:37 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81588">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NopJLpbcEpvin3Fyfv_N5itb-u44usjRcyMJiPpnkuf6pURHp7qclk37_F1kClCZYmPtQl-gnxrPsAT8ocZWfqmDtxTjruF5ZWMpMXK6drUutY-cidYykrsFaBsu_KVEMqbKhmDnl6nQoLnlZ_BDsCKpF8yzhvNOIEcl3yPOaabl4kO1h0r3WeFd3GoCV9NmXI1OjQl6B2uKQFk4FrI9AOxn2F9IdlHMeKSJ9t2ifglMoKLHIlzxdYp5ljPDws6f4BjKLPO9x5P4pD93Sx1gezeJYytAsWm7NM_wN7pJ0h4hx2K2RknsujGRSYdKhbKDL8Dh_OE_Ff_ZXXJTB1wAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81588" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81587">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6dRilaGsa3G6V_D5AxYuQwzDgSYJl52aOSQDux-k99Z_8O2uPCrddA_pTJpywbyqMk7lBZc1CEJBaOF8Lv4eeSE4FmKc0egeWKtJI6fNTwkFP1GdxjKMXKg2P2G-cPYtZqaw7RLvPlrCEu5ySs6usAnEZfDBRkOQaMKp5vOhUieEYsTpyobq3TDnYGoTEmtzdpHu9iz0D4o8WvdNlFgPJlWRQV_zmgybd-bq91FSlOOTL-YtSQ8jkJrrHE0I6bcfd7LE1Php64D2BAtZUvWINAJr6F6JsW4HpUTZfa0yQ9t1D9iWnXpYP6PwF-sPxAnJoUVmv89TtEqhNJ3X1nArg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81587" target="_blank">📅 18:16 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81586">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗥𝗮𝗽𝗶𝗪𝗮𝗿</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=oSXt36_Mns26xUAfyALArOqOhpAr3R6VLVsOA4dTPuzB-DUFZP3Loo7HrftHB-HQx6zkFE4bEdzQzh4Hp1-h1zT3N51GQCtFJR59g7BGiSKjezx2Ke8C2Rjw-EfBMCdVhG_vNV0BKppFMTH8uRduguD6di0HI-tUihX2aSHK5h3lUKP4jSw-bEHvw8QbCIQ0AqnO2aRDsjrScokFGzYzNvo2gnfnJdIe4dgVNIqabfEgnkgpA4SiuxkwRvJfy5whWlGDuC35JJXJJPA9QJVWqhgTwyi_5AfIyy8YhSv6KqfVsnodTaELKmvcDJka8w2pje8-ar_jIPtAhZ3jzCn5Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f78835d85.mp4?token=oSXt36_Mns26xUAfyALArOqOhpAr3R6VLVsOA4dTPuzB-DUFZP3Loo7HrftHB-HQx6zkFE4bEdzQzh4Hp1-h1zT3N51GQCtFJR59g7BGiSKjezx2Ke8C2Rjw-EfBMCdVhG_vNV0BKppFMTH8uRduguD6di0HI-tUihX2aSHK5h3lUKP4jSw-bEHvw8QbCIQ0AqnO2aRDsjrScokFGzYzNvo2gnfnJdIe4dgVNIqabfEgnkgpA4SiuxkwRvJfy5whWlGDuC35JJXJJPA9QJVWqhgTwyi_5AfIyy8YhSv6KqfVsnodTaELKmvcDJka8w2pje8-ar_jIPtAhZ3jzCn5Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینجام جلوی خود خلسه دست میزنه به اندام خصوصی جی جی
@RapiWar</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81586" target="_blank">📅 17:22 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81585">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a90b7fcb9.mp4?token=rrkrzXnM16W357fdasn4bAlvxeiC09aaTlomhwcWrOKrRimE1dzj1lkq0tHYU6zxJiT_R-P6uei0ZN8Ax0m4Iml7I-P0PeMPIq2cQ_e6f2E_d2Po1u54Jvod44QtF-4lct4QotNaNXY96-SfV2B5Esd-H5b5u6VVDZHLOJPOrXM8VO1fzqTC7s7n02iy0bd3PPinbE01OAlll02nYYadC9NACwawKCK_K8LjYu8mULcsN5kTLF4tOtgD4syWWK9FzmMAIeyPK7BjcIBZAoeMMn090XkEqijtVGPvW9nVffeaBWDiB0UXJ2-2nnvw6x2xntIRdngSHCw1QrcAXT56DA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله دسته جمعی مسلمانان به خانه های مردم در اسپانیا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81585" target="_blank">📅 16:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81584">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjiqgZEcQ9IjfL_JvoATboLYi6Co1zHmbuAdAt6RBFbonBeYENv-ZoGazPzdcLGElTkNTpxbivXcdCG06Un2TMG-a93LqNCXZJhhTcHaaau5PY7343yuMXUvHqLhkJ8s5I611WVLwD4bomdKhNwbU2xOj2QMHiXr41v7SRahFNGBPRJO89UUP_Yyh57oTCUZVFgAeUd7C2h0qrh1RticIrFEyS0vbhWN5sTr3cPMnmyVC2P0BW-W9IqAoSx6t0Bl_n7BaN1F0mljAoHbXcl30NVfyyZiLAkRhCEs2cpSpd1vBMjV6nNr1tHD-SD5zI89zuRJxgP2tbc1uaSfFkw4Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینترنت استارلینک از دیروز در کشور عراق فعال شده.
۹ میلیون برای سرعت ۱۰۰ مگابیتی و دانلود نامحدود.
۱۵ میلیون برای سرعت ۴۰۰ مگابیتی و دانلود نامحدود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81584" target="_blank">📅 16:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81582">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cX88ZnMjOwy-8XbFl2BvVoBRMu4j2t546ET1IAD7PzxnzeY2_-dI8P-K5wSwWw8jw9XsRlaNh0suXa2ObbX5G2OhxrJSpaMDqhThznoDR7MO4HWE9CxRxhg1Pa8cedLIP3rgxei7OyBANGIr0ROSXCsVGMVXyeRu6bMm4X1mPIlFzWT25BHP5WRMcA-Dx7wnyTsU3BWuGh2WWNXoSiPzTL93dHr1Wxyl5WIbQtj51sbDsBs69ExZ1nh7hM0sNQmABECXDvzuCakqgcLCxCqn4ngwAxLuIy5S6VV1tRkCPL7wkh-suRdV9CIXDdVSVIUWbDKRSRSPrxBXSp-tg3KWhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSBbXrgHjlurxiFRmqaLXhDy5zSSLiMG7oezHusQeQEV4tGsdljnVYfk61vzcglTH-OC9kDnoXisGbFK8TR3YHlIkDaotN3V9Q6pNvnxaUMDeuIqQPVdQ0OqhkPCeG0M5xBYNzBjRBJmanDDjnphF8gmjUmDNwC-HHM0k7mUP5JfclJDDllTgrIgTk7-19FtfgqYP8Epyv_49ZvEQtoPHkdL49NLG3Jtv_rzzoAGx2M6Rn-FZQq44VcYRLZP7yR6PmHWWjEh9rnrybJqJRqqHQU1Dsj65b5yPx3cO1coWWJWogLwv9BusVgEX4vVBHKhHdB-i6Dhut5YE4CJAbh-ww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اصلا حواستون هست داریم چه بلایی سر اسطوره‌های ایرانمون میاریم یا نه؟؟؟
🥲
💔
#free_toomj
#تتلو
# اکسپلور
#پرامپت
پروکسی
پروکسی
پروکسی
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81582" target="_blank">📅 15:33 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81580">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aEqqTp85taJUHx80wLOu98rww9HYJDkUrT-wg3PbvMDZNHAnyiyRWPGkw7Vofs9p4R4UnL61-2XlnBB23lCGgVgJkm7KeZeYLyVMp_VH65a-k8IisiSVnYbPPtH6PmtETUwXkj1DcY-294RwPeRl3xAO5O-Ynb9bSlVKisZkHE_UevJAhdGCuny0CTPPhTIxuMro7Ea5-KHuCgxlHEVghDOrVinuyC1jr3YVpRAy71CYWazUUqIeHpXWA8O4R0R1Z2qJPytWY91nzts4XU6LwMXUf6LoYvTZrLNtJGtSB8N7c7Z9r1GGEGiNnUXhjBnzljwi8VvXAvz-nMR5ArWdSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I4fwZOZdvCG6NEuAu0MTtMEA9XgaeLMQFV1mLAFecxM2hSJikNCyn0BK7DjXG-03emdv3BBV-jbj8_sTZ9mvRtFqBoAqXG_opu4dsJzyMFv7dN4p2jewoTJeTHwsoeS-J_F4BtAnJLv0aHL_7-297W7_rhcNFKjVibFhfgP3mH-rwiylxdk7-XHnsxuXH6V32xOYLZmHOGx7CmOgKGlWRhWc19OajTjSy3uDdZJ9AsQRw1HXk9SoqmBZ_aX0mERarT5EQ4TqfooWCS4_88bTEzSWQOBysU5QQjyyljyyw4FaLO_pbE-V0y20tNlG0A1Bqzo6sFVNSCUWLaK2UiYYuQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عاقبت استروئید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81580" target="_blank">📅 15:08 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81579">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qMHplFOQGU6CLKZiYMq8q_kcHUNTxW2iSprmgxKwdDgRXhhEa9PyewBsvEsvnCMA6ZhMH5Cz6jINsJFltzExwIIM43ZQ3peiUYfMDLhZn5ih-CgBRXAfDjvAq4R1jKrjdMJEnzOfO934G62P-9GvZ6hrsSD9cjQtpNEIhVj4lvhR6s_aIBJ6qxBvXLHsjHRF7hNogLLQrgORqdplGOBCHqWEJZFG77-A0q2fk8YsrxrPN0rsVCMF0pA9bn2VPG9eLHW6BR9fLoivab_kPOgx2oo4gX0CxyO59bHPWGKThgwvdnu2wl4h4rNHqSLJCfO2C9i37uWeA9t-KhIDY2KhPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81579" target="_blank">📅 14:49 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81578">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ امروز با کابینه امنیتی خود در مورد ایران جلسه می‌گذارد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/81578" target="_blank">📅 14:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81576">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دوتا کشتی تو تنگه هرمز زدیم، امشب آتیش بازی داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81576" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81575">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">آقا تبریک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81575" target="_blank">📅 14:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81573">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k4ocuGOyiJA2BvwPLLLXWPgJekTdBYa7bxkr3lhUj5H7pMRVJ_WDYGbibU5wZT25fAz7ny3XseC54_XXAJ-jmPqoAvTG9Ai_1PAjQbszvYtXRcT9poYSVXRznWKD003gFszoJN5bgUpiFoHC9ISRmfiRTUkzWoMPiyYunArgA_-E9DotPlNJmk-ltETgumm4GerZIAdCPpNyudSTiAMoNSODfRM5Guuj_KSynip14k8wu6AkC6cJ1F5TtX5cUbYrvo_tk-pCtp5sX8glKXMNS7NoDIacBJlDKHmqt4hR7bqpSXmpcuaX7VGeKxbcFBruW2-XoZyiJCCDdpnXH0nacA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم میگم تایماز چرا انلاین نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81573" target="_blank">📅 13:54 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81572">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gKTBi5RMn62LvGDKeY6ZhK3XVvS_9H9rQXaZubyf7KtNU9XjBAn3cOy2WRDVqxxybgxNKBt4vSiNrt0TBPz3ovX9PsPg5efZIrOY3uHsglZi82M6vHGYduEWb3SeOcT60sqPhF6YOOcuFxJEDZXtOQA9zQs__Vrd7lNj-ljJGzR81KUdSegiiPz0QqndugM7bmJ74V5OPSt1TS2mxdLGMKa6BA1CCrCZne2XW7c1skNRCmdCWmwQqlY7DGYBb5g4WDT_CMpYYxHICgKOtqpDgj5Os1xii8BAyX64VYaSb2yQDbIYfoLNxi8NMVEjZ_kLp67Eyn5-ygsyPEP1OI8dIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر وینی چقدر شبیهشه
(پسر دوست دخترشه، پسر خودش نیست)
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81572" target="_blank">📅 13:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81571">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DWZDFOZV7Ao2jKbiIzKFDZUTYCfAFGb2-Awi6qbP53cNXb_1h__DC4QG3H331-1gYA9M64kzO4x-ZujGQ6xqrThSmN6cuxcpysCJDP79aiXasJqQA-7NoQrv41VCk_Gc6PKMAj1mFRLLnYmcuzKZtDV_X7ADW51eT3uBbXVIwsApCVnLBMQBxVKY-vrW8tVbM_SNl90uVX70NqhXMmixhtQce3PItQjASmEhx5cIrPZNzYU7-ABge5WxDrjKiMnMmeFsxIl_064HTh0LQC8B70fWYjKS6eoOXL0zm6gtosKDoyCIK0iBbJhH83sexjtpTOG6rvNXYzVJu93pqX0mag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81571" target="_blank">📅 13:12 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81570">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uj4VYHo1A6Bs9-VPbW2uOi-nc4jz1u0u7p5Si7swZdzbrdfxSKWhN3rd5MklMNIZRKmSMTflRnmxMiJHN6GhVI4KdSiYK9paoRHSoP6vntGH62tnOvjFaMuKSmo_y2vEnlxZ8tCMdlOQhslArShiHKGosAx_P7UzBASziWSwqU9uaRER_RPn_lgwdDbhzkbT-e5bwWkwcflmwvx37HINIyQEpdRuvkV_dmEX37BRHYGh6gFiCOfKOyzxdclfUsmEunoOzoLryggjFxiSqcMMzqUwgHEwonxv9aJBhCmkRJTks9jiysBZW6Z73t3e20iB807tKMV59Yta9vlZDEQzpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیبایی ببینید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81570" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81569">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FejKB5hRDEpqPQb3hwy3Yy4Ol0Qz_B9wqmeeGwlAwZoK0HQ72EkrYsryg0o3MLOVehC7glEPnV6j4iKcbgvlFoYiFjKVXsukaC37Cqpi-uIBXhEbZE0c2oPxEf0L816bvWzGwGN5H9LdZzg-IjVZVpHKgTDqx1mOGZeJAYYP_z9wnf4Zkd1O2HhORz7MJGce50lAlpl0In_X6YFhFvAwPWSuY_l0D3NQNaNd39BRdzhoPwSdOr7b6Vfjmi8OWcYpXqiaT9dknISi-pUEQtTAvuGRDCptiIluuj_S_qxwFrDkkCub9vXguU8hwMJccuLgzisovR3B0fgMnPppDhT0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
بیرمنگام سیتی
🏴󠁧󠁢󠁥󠁮󠁧󠁿
-
🇪🇸
بارسلونا
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
جمعه ساعت ۲۲:۱۵
🏟
ورزشگاه سنت اندروز
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
بیرمنگام در ۹ بازی اخیر خود شکست نخورده است.
✅
بارسلونا در ۱۵ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر بارسلونا ۳ گل در هر بازی بوده است.
🧠
مسیر حرفه‌ای از نظم شروع می‌شود، نه از شانس.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r9
💻
@BetForward</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81569" target="_blank">📅 12:43 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81568">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eVVXK3LnaQiKJ2GI8L4G-Cq1bYIGeFlNfMAPkEEnp9Wc2mLEB7KP_MdVTw0XEWSApePTxCGkfTL9-jh3R9wXvkHx87vJiI4VAYtHizZOM5d9Jaz9dHzhGfoyXI9khlP3ZrlLbaAFyIAq0AgspYo2bUE1XYAGzDK2wD3ayshb6VMnfW_nvG9vciQn7geGP4GxLpBbhV2XfSRDsrTmKZIxSFu4beo-z948igZ2cbfNpyDTdAutzrzsJ9GEkorqqsSwpEpq9geAhv5HD3v_-wMs_L1YNB3iL-vgksOpvri827wVTNavy1wM1_4Xwqsou_z52xGIHCSgNGzZ7AvE9koagg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81568" target="_blank">📅 11:31 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81567">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81567" target="_blank">📅 11:20 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81566">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf580585ef.mp4?token=GQDtq2ufkMyHO_xUI6pHjL090P7EyvulaM-u8UJ6q_L6R1fpOm0HiM6-BDIvg7hqlMt6XvgNYaYPKYjCDc58n4aNV75EiCxBcuZzrYpq7lri16oWtvaW1MmpJR1UiH_w8oZdUmfiPlmv76fLdpiurERnzlR-9s7WQptCx7_IFW0KiJQFIZxP0bMIKSyURBRbfXW1cbH27kBg4GtOkmqvjKBm6yRi_xQmQs8SvhCRExqoMbEuzuaucsfnwJf1AUECtnJmeORqJ6l2YIJjrCWFfLseQ6vRhUvsWycWzXsYHXeyOhdPszEr7s-vPDwX0nFuR7VPHrAzJPwl2AeHdt2gsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81566" target="_blank">📅 10:23 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81565">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCiamZx_W-FXUGqD6ko_NP08MEy9zL-q15kEjV5V3AN-Rb2HZnWqAA-Sz4KZKXMPvTdddYKfcxTste148wVmHT4Uo8l0Sph9414w8ijKvNfCV8PMTgmIK8Ictpjn73kZGROigvXA-Hl_NoLcf45qESVAlBzqXxE08Zpyy9HhC6oDGt-PjSsSDNVl9orusAbGP09rbNebk_mTfFTZ1UIR0m3nCPhkesphFUIh-mXyrDF7j1BnTcNcAwZpv8PdyK8y4G8ZnV-qVdX5QhLBN-dvKgvGxPqxSQ7p_dJkI26gSSN9M5-RY84iD8_E8nk8_P3gyY8xxAYbbidkcKJD0nf1Tw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از این تحلیل کارشناسی شده‌ی رائفی‌پور، خبر اومده که عربستان داره برای حمله زمینی به یمن آماده میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81565" target="_blank">📅 09:47 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81564">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76336c1936.mp4?token=nGu6Ns0sB62yE0mrbdk_oPZDxzxClOXAyhJ4-LeTkUDa0QvyRk4cqulKZZrtFKfRHqgIVhNj3sguKf8Wbph_LycJtMbr9aC66NxutbsluiZMISApFrxch1b9gFi5hr8qXJHtalO60qs11oOgMgzaDPmBolHthbe65jxggcMrmahSu8kG6meJNGtFJRLrLUnjEtgP10Tr0fXXf5V9v6eoxxrun4q97-YBdoPdxd6Bs2KChL6ki9rvZtdFKVCdkUkuA-0DkFxw98Q0eseSS79zuHjYKLqymm3L6xjx9_dFGvyDvn3f9MZ8P_ka2zM0SwG1sSw2hDkZInaoOn_cJ7t2BQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون سر شوخیو باز می‌کنن بعد تا ما چیزی می‌گیم میان می‌برنمون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81564" target="_blank">📅 06:02 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81563">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81563" target="_blank">📅 03:29 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81562">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسپانیا داره شبیه سوریه میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81562" target="_blank">📅 03:15 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81561">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">حماس خلع سلاح می شود   ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/81561" target="_blank">📅 02:19 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81560">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">حماس خلع سلاح می شود
ترامپ: شورای صلح امروز به توافقی تاریخی برای خلع سلاح کامل حماس و سایر گروه‌های مسلح در غزه دست یافت. این گامی عظیم به سوی صلح و امنیت پایدار است.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81560" target="_blank">📅 01:59 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81559">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/81559" target="_blank">📅 01:39 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81558">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06fc3e48dc.mp4?token=hYSmHAh4CHTjZ4oS_bvw3AKBpZVYGnXysp80qvi33n5Pj8NZwfVUrN_UWppfL3poxrUoNZbS0UVbYK21Vrg-Ls_hl9d_vJTzCTokwITusdXA-9ry9BoVujFkMbgMZ9wKoneXvZGGa7isJxZgQYT6w-fNEHdOm_A9pHZOCoUG1YXbdURkonwsbVmLiAsOMWOWqNB-nx1m3x2z4Mz0DUztMWlAFN7PTw1k3-297GjB37tMaKRr4c6EeZzW_uEjWZ805RI81poG-MvU5FC-Ij5lC6hnY9sq7U9R5DGsDSvIgMUu2d0-vmzFoEoFYrnEzZ5gVpYBPPA9ZdPi6-TpPbRn9YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های جالب پژمان جمشیدی درمورد شایعه‌ی جنجالی
بوسیدن دست وزیر ارشاد توسط ایشان:
آقا حالا ما نشسته بودیم یهو رندوم خیلی اتفاقی وزیر ارشاد اومد کنار ما نشست منم یکم چیز شده بودم با هم گرم گرفتیم و داشتیم می‌خندیدیم درحالی که دستم تو دست ایشون بود یه ذره خسته هم بودم یهو سرم خم شد ایشونم تیک عصبی داشتن دستشون یه ذره تکون خورد یهو دیدم رسانه‌ها دارن تیتر می‌زنن من دست این بزرگوار رو بوسیدم.
😐
این تیترای زرد و سخیف و مشمئز کننده چیه می‌زنید.
😐
چجوری می‌تونید نبینید من همیشه در کنار مردم بودم و برا همینه یک هفته‌ست باید با فیلترشکن وارد سایتم بشید دیگه مشکلتون چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/81558" target="_blank">📅 01:14 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81557">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">این پست مربوط به رپ فارسی است  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/funhiphop/81557" target="_blank">📅 00:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81556">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sctq85JXrOhfCaa7vyLUl61GhGcgz4yVSmj420XeGkUyb9XrkIY7_oox6iVZdDnXDjCsAPNv6FfavBz_eaBbdD31Qt-9NMOVbbqw8QtmvTEezAP08tTQap7jZh7WjltRcB6I-JbUWkqkdxSobY90e9eD_2qfJDe78pXOWN9hIECru9jWeGvsRipI7raX7AQDlttnym9zhbpxoddhMoNRwv19EvtY4JJQ9T_irL9KXix1qwt9ceXdRUeTe54dexOpcU7U0_ax_DPTcBA33PB50BuRUep5aLmRuPEmurLhB2UCDS7eNaMpyVHpMGLmBFZLCWcPiiuEmaTm8RRc7QTiJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پست مربوط به رپ فارسی است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81556" target="_blank">📅 00:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81555">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دادستانی تهران علیه افراد حامی محکومین اعدام دی‌ ۱۴۰۴ اعلام جرم کرد.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/81555" target="_blank">📅 23:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81554">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LYxRhAAti3mq7P7rImpr1gkhHtRlswNz95V5wvc9S-l3Yp5p2UHm-Gqy6UMtEMknS1U5x_a1_xVRyHlCMeJieNad55bbWS3PCF237OaUa7XRFuLK18TlaQXDyyI1Jyut1brC38A_jPFIyHUKPI9aRfowow37S2xE4clJFrJlzOzVwzT5ZqZ7E8T72DSX5v5uMhon8ljRuQbTIJ6qJRyyoC15w1XusEp0KoMBi_j50al0Ni02oIh906xxolwn4_ATFgptBzvztvDXbvdP8LcJuod7sQG_R25Rpnb9okTYnsuBfihrg8kEvZtRx_VuVqAfcFvNk5RbBQjb0nME1hTlpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه ها ده سال تحمل کنید تمومه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/81554" target="_blank">📅 23:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81553">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37370edf56.mp4?token=eNzNQlQu7q8FoRzu9ltN6A8AA6i3kaIeOqNd2fh6tnV122335sqWg8xe5T7bDrq9OQMyv06FgJd8Xb1ktLz3UEjCCPljOeaAjwhtQ1YVv-Dxb2EitGAHCiCPztSVpAzFA4XQMg5OaTYX3LkNRBBMnEDpaIEjttNmYdZQ-payZ6h53SLGNgqDrIs__nh7JxfGPPWFTzvqqS9XgXZDm2GN-f9kJ-wzHikwztbHimaMjngbEJv99JYhkfkwkLnfLR1HE-EmmAYC28NbT-_632DeZnRNxt-0RDEcmHpWAN-S5k6yUl4Vi5kJH2CgWZYlK4xkXqRxb4WGPrfAr2isCD-q1TAk82rzbK8n9ZuJNqEgd-MAp_v1M2Sk6A48Orp45kaNbi8Nym9zxuLcQ8Ao5ar7b6IU8GAOnfPzBsAazvDjoB39jQdLTmaQ_Zgr82fLC-v70FUmD6lo28QGcIu31sNnUcPnjwhU5xGHnWWOLIDNkGXONi4AhAxtclxhktPe1UHA7xByI0c3a-N5Ia5VhgQHdBtm9GONwMpRH-qavdSeRFpnJQuSEyrYUTRFqvuu1GNkQkhLZ_XVdDfjDppRlS8IthcJX1MF4po0TFzaaddoDiJzEpvcBspfIQVmcGTYNtnADPO6AKmZB6AICPIFyA4PX4bGkx3I4xekOXIrT1Smgg8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37370edf56.mp4?token=eNzNQlQu7q8FoRzu9ltN6A8AA6i3kaIeOqNd2fh6tnV122335sqWg8xe5T7bDrq9OQMyv06FgJd8Xb1ktLz3UEjCCPljOeaAjwhtQ1YVv-Dxb2EitGAHCiCPztSVpAzFA4XQMg5OaTYX3LkNRBBMnEDpaIEjttNmYdZQ-payZ6h53SLGNgqDrIs__nh7JxfGPPWFTzvqqS9XgXZDm2GN-f9kJ-wzHikwztbHimaMjngbEJv99JYhkfkwkLnfLR1HE-EmmAYC28NbT-_632DeZnRNxt-0RDEcmHpWAN-S5k6yUl4Vi5kJH2CgWZYlK4xkXqRxb4WGPrfAr2isCD-q1TAk82rzbK8n9ZuJNqEgd-MAp_v1M2Sk6A48Orp45kaNbi8Nym9zxuLcQ8Ao5ar7b6IU8GAOnfPzBsAazvDjoB39jQdLTmaQ_Zgr82fLC-v70FUmD6lo28QGcIu31sNnUcPnjwhU5xGHnWWOLIDNkGXONi4AhAxtclxhktPe1UHA7xByI0c3a-N5Ia5VhgQHdBtm9GONwMpRH-qavdSeRFpnJQuSEyrYUTRFqvuu1GNkQkhLZ_XVdDfjDppRlS8IthcJX1MF4po0TFzaaddoDiJzEpvcBspfIQVmcGTYNtnADPO6AKmZB6AICPIFyA4PX4bGkx3I4xekOXIrT1Smgg8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعار مسلمانان مراکشی بعد از نفوذ غیرقانونی و حمله به اسپانیا: الله و اکبر، ما اروپا را اشغال خواهیم کرد، زنان و کودکانتان مال ما خواهد شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/funhiphop/81553" target="_blank">📅 22:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81552">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/OCuT_l0kSMDC9-V-MCJGIEwo3kY1sW5VoQNLiJPIJPVoCW3lc0ruF_-6bF974SaIlkuq8U8EiMxp_APDdnV-lsxNCpJZOUrOK02PzjNxLPmEIr9iunjsOz0Zy-DKm12wBcHUEvZGn5biiWoSOj6kja-wKTxUpSDSnGs_G4OntR8bA4qr23hmg_c-hrjDlQiPoF8bIiAyzJr3Dhd2qmDMr9vAUsjwa4fSPsXEKL_hmwZZldAhfW49Cnrvhax5LpP-sq_apRmYOzdP4kHmv0XsY9NkQr0A8sdbi4ZVaVJNelPTkEaWM9gvDEDJJZQOzNfEjj4XNpkxle3Um-UzqPcRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
😐
پشمامممممممممممم
نیکی نیکول دوست دختر سابق لامین یامال پورن استار بوده ، فک کنم یامال وقتی فهمیده ازش جدا شده 4 تا از فیلم هاشو پیدا کردم براتون گذاشتم ربات چه
کصی
هم میده لامصب
چه ناز و خوشگلهههه این دختر
😍
مشاهده فیلم:
https://t.me/Footballi_Dark_bot?start=get_tbcbmlqhfqdjyaew</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/81552" target="_blank">📅 22:27 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81551">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترک جدید مهیاد به اسم چشات میگاد ۲  ریلیز شد    SoundCloud  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81551" target="_blank">📅 22:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81550">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dyu-duWTUsxpTasm9apEXJYf7Apa15OL9Zz2nkuxxZTod-HoqW7igsAyTMPDNEWzd6wCXsBIeHWAqzcl6d6vGIq0uSR67ZYx6GSiztCgBochkCwhKhmaMA7IHwwiolZEEU1cozbw3lu0ZQq_5wJpdhplXf-cDYD9PYDuLh2o1ESsQfLLwIncC8-67oRWZTAkdUAkHqFfoBzaQN80l5TuBgHigelrBJwwj8NDC8cVpH8iLjikelw74JniIlIbHjQ-CrqmzadZ_AKC_A8VHq5qNAlRwCxMP03u4Gj_xAVi9Vmtd17gxgdmg1UOIKOj7BsWn29uTU791uEdEEVQaoxI4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
مهیاد
به اسم
چشات میگاد ۲
ریلیز شد
SoundCloud
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81550" target="_blank">📅 22:13 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81549">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c2Zogy1ZDPJIEIfxGyHoY1zfxZxhwzZ_v_DOYB0hY6wXAzeKk9c8UDNfKKtdyRUF0xnr8fNyI7BYAj6J7l9ybSk8LyqkxR9QrhMFmfDSaxvtVR8Jy0xqXGpxo47t7Kiv-juyRl2PVilT8FYtsdVhrEQcROVpD43Em8aCvGyxSTT3TT9IdMH-1HnoIc8r_cBPxG8FkZuBTbUg8-I3CFbUFS3zSzdn32h_7m_Xma3yb50NsgH3iyzmEB1tsrntnJvT0Hg8sdOq-QuLZu5ffSatcG8MIaznKZmIHWE09fjso4r-WoMhydrRvpu1iH_yNJfkJjPzlC1GwrZ_VnebxGKQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یتیم گیر اوردن کصکشا  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81549" target="_blank">📅 20:59 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81548">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پیج اصلی سروش ولی زاده برگشت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81548" target="_blank">📅 20:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81547">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FqMdocKZ_Gz8WGViOr5cRoByrhgNvmLjfzPXgXSc5gjpNT1-R-omGjkkcCvO4mWbIMgRPGQh8_C8CgYzOYr_6_CKLA1GBFn_M2UGS9XwpVVUPecY1iU5wK1_iyCWc40XwAEvcL2Ysr14LPIaZGAKIco95V2A3IYKfEqdoOsOHRl2u6yrfbVco1GdWvpJUzyN0N0p1rAR2FG7DCvbcYtbOYAFktv2_4OqsRiliTZnAHrpdNKkj1Ckm4mji8jlaTREfbvmKow33uOrvT8PYuFqli2YKT6zGffsy8H3YrDm1njzug2E0uffxTOEuaAPbiNiM4B3pOO144qfZyYITf3rdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81547" target="_blank">📅 19:57 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81546">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NVBGzqt5MGXjJqcrzP_KFFvedJku4KgiJx5b9bvHAC8gIhAFSxEAVf6CwMWPdteNaz4pcDh2kXf5lF0-Qowq0dUqGh8lZtzsWRr1RhdczLiWWlCVgUdlt6xE6lg2YeeBdF8KKeHQXbc3kv_z0KsXo1EeK7n3HDUai_Bt9QeWqPxnuibUrsXEqBoD-NkIxmJ_vq8FNez-nu6S9IUMogIdVKYvhYE7huqiZIcPOUpcF0nyPwVwIFELKd9taXcNTAalBVgLFfnLTB9OBMj3mUAcQMEwmjyo1cOk86vngptCovF7csWntD3SVuMvMtJ-XB9xHmxQJ81EgWj2tC4siRvYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/81546" target="_blank">📅 19:52 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81545">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkqItVliTPGEKfDBMCXFHaHVFsSAuKzsTgzSjkGtYZKw5OSbtkyukWkXCXKLfQURkog0c7Z4InA-MA74LWmbsN6rMLc2DbTgwgd60HcGEdCTuaZlRmHtk4M_7vkFcpTyBa8NfIsfwI1F-qWy6mwUkNn9GOItsOKZKTAxT0afa5O4jwj5kXK_OtVL9sDz7dSQzmiYK4W6LU_ae8EF5yjEtPiCfNAdg3Kl75FcUY-hr4LedRp3hw-4h98nT-k8evlYOpBDPc3nbMLPTbblQTHm18i2U5fZ4vUCK24uc7OWrHM1f6N90TXjhusKOa6GxkBvQjssUYSCJpndbPvth4215A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بازی شاهکار رو از دست ندید‌
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81545" target="_blank">📅 19:45 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81543">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qBnAhY_21kdThY4qaex5aCmEQyhmE4J5A0pgVjpT4RMe4_ITE2oGbAB21MSQ2gGdmp0rpPQ8wnclsnpmKXrFdPn5jVsIsAZBsVzJpBf4KpNoqp4C7D2zdnFK2yBdrbw4K9xZBuyrZW11l4r2vb7zKw0FOiQY70_3u_Q7Fua5kt0CdCP-sGZOHyLR69Dr4J9r3hqIWZjuGAP5Mv_cqPdJgAlzsIg6d6b9wj8WFN_EYkcEu2AtEZEiVu3MhCZ-A4JXPvdK2haa1zUgMDpxl9Ol915DbMCopM3El6NSoi_XMNCveYWjA30sdR8RJIvRPV3Cdpg_TWx-Zgj0P4T9SUIRpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران:
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/81543" target="_blank">📅 19:06 · 08 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
