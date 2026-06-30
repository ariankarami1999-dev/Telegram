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
<img src="https://cdn4.telesco.pe/file/FkoP_aIeIL4_-_inYPZro2KkX3opEAg21gfjMIaaHHMqWBonI0wH0NP7B1zMp9_tXARGNQLpQBLhpn8-vBOAwLZ1aGwwmFjStYdT7Ojt1pJias0tSQmw3qUZHuM6ax2iPaGj01C9cAX-3EdnCWYbkSH3AAoyKdgWRKdxJca61ijaFJtRyCvS83xET_e0hk0Jt_s4HmLIW99JH6RzpIrlJoF5KQM6TdfnzHjoUX5u7GqxpP8_E_ifu9k_w-Zv66zlX49xblAQJnVD_BxIABhHXMaUAvSxqSs77j0CHIjzii52kUIcOBZvE002_HJgdbEh8RIlT-NkM6M5WcmYOWfjEQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 217K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-09 13:56:39</div>
<hr>

<div class="tg-post" id="msg-67078">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EQOova1yluilZtP9JY-O4NIQ72SJek6f4QopdbXFLcHKl7vTeCNo5R_yKWQHytgGDEPjhnWj3MYlBPcZgyB-J0z6Oto5Yl4IKa0kEnONUkebDfJiPpX1_wipnf_ytad3Swo8RZTAG-NM36QI8NbS1lRu7mNIRPSiA-zw_IJrM8JwAW0UT01BSoaiUMaCt3BMW1fXnhuf25ApzJg5s69yXJsLVlnBUKmRY2Zv69ubnV626UoxCgcO6mL580T5TStS8Egk4CurMnTuW-08vJmIy5HyJh24v3VC-0lt8sHTM-pIeF8u7aY-a9Eph_9Kc3yLluzy6qmWQpUPSKAxcjqzmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افت رتبه همه دانشگاه‌ های ایران در رتبه‌بندی کیواس ۲۰۲۶.
این فقط یک خبر آموزشی نیست؛ گزارشی از هزینه انزوای علمی کشور است.
رشد دانشگاه‌ها را با قطع اینترنت ، فیلترینگ، دیوارکشی دیجیتال و انزوای دانشجویان متوقف کردید.
@News_Hut</div>
<div class="tg-footer">👁️ 2.81K · <a href="https://t.me/news_hut/67078" target="_blank">📅 13:40 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67077">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fXykCPw51hgwYEx2VgnxXUjbBS2fMflF1QSsFLmVNh9IQmrAGg_zed9V__jc3gjM36Aor1QtTmzjt0qnpquEzR8faujxxiXQJHQoideh8DJz269Lolwp6VOBJJnsoQVf1NM3K_otZ2eDE2wJVr_AVBff_apqWf8aRwxtqTM205IRjmqswTs5KbHFEiMnSTMXeElXOytND4MGKr_Zpn1LIOfNau_Lidr9BDL9UiJ12sc4vNsm5DmZs9mOIUfp96qqZIQPZZdQ4_ogzRpyaeN_HyLFrOUyo1whMENkgjGIOtNoafX08mRbSBkXUd9ara1B2y2TymGCmKQ5wattIkOp4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
💢
فرماندهی حمله جهانی نیروی هوایی ایالات متحده برای اولین بار تایید کرد که یک بمب‌افکن پنهان‌کار B-2 یک موشک ضد کشتی برد بلند (LRASM) را بر فراز اقیانوس آرام شلیک کرده است. ادغام جدیدترین موشک ضد کشتی آمریکا در این بمب‌افکن تاکنون برای عموم ناشناخته بوده است.
💢
نیروی هوایی ایالات متحده اکنون توانایی انجام حملات اشباعی ضد کشتی را مستقیماً از قاره اصلی ایالات متحده دارد، در حالی که پروفایل پنهان‌کاری خود را حفظ می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/news_hut/67077" target="_blank">📅 13:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67074">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpC6vG6ECtlsHXyZtZ1Yd9kg49Uv4WQxPX6DC2zxW1qYZZV1TnE2prqJRYFU-hOVS_2q-2QdLjMlIbr1SJKj_6pGHU48lsCcqFx3vTO0fNZXfw6qIsMfK9AzLsq_qMsK_ZkFSOdcsBIUe1mCYUy0r2cmwxojGDgdHb9VyOyzqJa7j_xv_eV-o_b4IhbNuTK5gMIxlFlhqu41cLIBTKz8kUmcxfktl-XBvLbyPvjYsZRvuZOidD94s5hbaon0oL74CCVHXt8QxFz3zHbreA4FrVdpTqb1SMu3PqU9gbh3_RCs59cInc2X6YQZ_0KtgIgCjoDoNfNxJ2gbzTL85lEikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚠️
🇺🇸
مولین، وزیر امنیت داخلی آمریکا: خیلی خوشحال شدم ایران از جام جهانی حذف شد. انقدر خوشحال شدم که رقصیدم. نصف اعضای تیمشون سپاهی بودن و هربار برای ورود و خروجشون کلی اذیت میشدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/news_hut/67074" target="_blank">📅 12:06 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67071">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TlW_1A2pNQxcHJAzkIXQKlzSpMRv0beXQ9k3a0hrdmX6mODchd_zX982uzXskU6z7x5ONRgUDjtYzvZutg1ss1eCU7Fj5AZtb-53FhW122CII6mcqX6yFnA6Tjx2JGorenGec0fwKIx9dvbLnvaMjVG9vVaWZTlWEhU1xc-PAhK3hO784O_nDA8KmpAzxDojasXMSFl7H84VJuiO01atHqA2Z1eIR1Sn35oy1CsIxGEkbpD3AWWP8_tEtA1nkNDHRNKje2WSikT0CwT3vz2vfIQLxB3vaiACmV3jJOfZyzBE7mjwm-3WHSwaTHNWQjNJ_m5d3E2tkM8kvjG2X0MTWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uiYwciNxEnvqhgRat9x1JCKgf_XytWE9n5IxIHC5EN2pVNq7x9Kw0C9GKCcfzK56J6wVd2k1h-ufAOqbNXvrDEFRHoeuplm0F3wSVOa3SUeOCOZZkih3POAttIci40eTBtd-sJ0ZyaYCqkxP1WG1v7csu-JFRvxGv-ArZxhOtJLNpfw_dtxz_8nbl16bfJHN26zv85xlhjLsaSStr0isXom00ZM3t_IsMshhP0bOP7Yt2oEmrqmqhw_uBrI5gGE6lZHlW7KhYQWRNGCOTU7XUf4vlMFVhfff4YrEtQ-UR5kH-Y-87qYvBJSJT0GPovkHGOok3Zm6PU81vxO2kt2WHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BdXdpjBe8nwlQx7z3F_EGy1Jz6O_Z_NJWy6FhCho2NUm-1dFFkDjDqwo4hQSoYIQts_sphVZJkB3FALTTTg4GqKmsQfHB4ayH9FtqGMxrPDGQzCWTWBH1ZLInVu8PEEt7QpIFBKXbqlsihFaO1euW5y5fkKyaaJlN-n5IoIy7Dh65BfzObApCMCPns8v2cVjl9kdQDcpZFRtrHyolewcRt9Fml0QOf7tzpzjedNSl2t4NmujHfcGNXA0127QRIcZWa_cwHEorJ5XFPyyzZU5f3pOalmmS2toe3NlUQF139cIJEAZoShNt7n2BDE8A1rBs5_hApmAz6kD5Sum1i875A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
اشتباه نکنید، این زیرزمین خونه والتر وایت نیست، این بخشی از دلارها و طلاهای کشف‌شده در منزل یکی از نمایندگان پارلمان عراقه. حالا شما به این فکر کن توی جمهوری اسلامی از دون‌پایه‌ترین عضو  تا کله‌گنده‌ترین فرد چه اموال و میراثی از مملکت رو چپاول کرده!
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/67071" target="_blank">📅 11:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67070">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qmVIBmwq8cpCtRZWy2ZFfn9s6xAMjAWA51BioJ-Z5fNLgC1WBm1PXgIfB4IQwoKILPEjtGG5Vf38rC9J5CWnE5ql4CCQ8Uf8r-Y-oAXj2EDwIKmdNi3vwh_uaSezs1Q_XBpdemrzNEoykdQlTnKTZ6Xgvz9Rwj0atQQmEmUjCY8N5P0W1yKMgT1mlqBLHlwpXaMvPRUr0vE7F56YpCEzVBI4QXDES9CUaMSeIbWv1625BSFN_n_Ihrw_mI3txT3Avoh4Gtyb0H94tQPsKH7UN5wg3L3w1UWUPD9wdQWoD4axk9Z8Rqf-o8KMtccvoMFQSU3a63qjjXCsw0XPXpey_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
اموال کشف شده تو خونه یکی از نماینده های مجلس عراق
@News_Hut</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/news_hut/67070" target="_blank">📅 10:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67069">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f285f9f0de.mp4?token=ptW60INbDxoPMQga3UFIKrQgbgO_YrXt6wo3f-Zxp1BrM5e2LKOpO_KAzxR9CdWnqUfBoncVcLYZ7A0lV7h9BWr-Rbso10rJgvkUekOHd873Lr-bFciApRJqRXCMO8BO5vI_E-WxG4Wt8fsTdEPjXmHj9D_Shnn4r6GGml-5yxrPF43bQa7V-JrOnECko58ORHEHDXd2Mg2CElx_sDTJLCS8j5Fm8zi0bUY1DXVWe5UB4Ji7QcBLG6VykbjOiSur-GBW7Zb6DkEMm9mLfYnMVfOGbAm9S0z_sy7jVwav4NO08TLlwpsmIlSfCjJLqc0jNCiu8wRwxeY2T62ARo70OA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یک مداح:
رو هلیکوپترشون غیرت داشتن بهتون حمله کردن و علی خامنه‌ای رو هنوز دفن نکردید.
۱۰۰ میلیارد دلار پولتون دست اوناست، و میخوان ۶ میلیاردشو بهتون سویا و ذرت بدن.
@News_Hut</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/news_hut/67069" target="_blank">📅 10:30 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67068">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad39cf71f2.mp4?token=jgR65WWOJ9qzeBC24slhDzfjZGIxliCAIqBVrYJWkvASLr49PxC5dqTkWlL2gq-92VnI96QdgcN4Jk4cP3ByW1SFCQP1-RT62MUGNhfdCZKtVdTUtuQERmimRaRkdG5bljiRTH-2B2BiIk1DllEYy2PDjLgQjdCac-xLLACB3a0ykT87aAZNsMYK2K17XmRC-D3wY84TiVOnjuA0BTrpijZzbz1na9laVGHO55OOYJS0a4H1SeRGYbwTp7Lg6MspQXHgcuOzF9gwkn-_BsP0gzHghjjouCiYLnDZ1cNy_khgjOhSSQzZhMAmXGCiPe91vtUsCelbIXfk144BhWQxzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از سخنگوی‌زن‌قرارگاه خاتم‌الانبیا هم‌رونمایی‌شد
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/news_hut/67068" target="_blank">📅 10:02 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67067">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97a96b4393.mp4?token=mgr64ty_WDCOi_JpVQRdPorvKkS7AZtdHYB5p8UFhqM4p8HAaqcTwDrvqJXZdqFtKxsI-5TDgribocmM3J04cxtDgSFH3hTDAKFuMJ_o3uScNmrsMDEd64UDfi0hKBTBHjKb1O4_4nrcdaqNF94QqG21bGalb0sXhuwHrygbwj9Xu1DsmCYC1ydO0eg7Crn66lNvtmX3J45wm-pSyEzjn0HOJMZxm1_wFpGD6aPgTyU1AlKvYfOD8wpa37tX6jaMDqZpKlurFdswlVftljxAYJB2h3dbr72VHvpqtws-kheHi7rKj3jD8JqIMKDrFTAk--imKT73Ajhzd7Z2NPy6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس تلویزیون:
جنگ تمام نشده در وقت استراحت بین دو نیمه هستیم
@News_Hut</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/67067" target="_blank">📅 09:34 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67066">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81a3f09336.mp4?token=rVpaYKRm49M60F6Q5ECyJQCkdX94tuVzJ89yPWEt1ieS8MrRnLrde-SuGogRdOELUa2cj3bHc4aEm6YO2V8pYhk_8cyASyTGwTqOrod-tYkbzXwi5p9zva4olIEAhfhYCeQVus9TrRTzpmOK2Q3frGcSyTgZbJ6315qdm2DBNIqIZ-SY6rmxlospZsZ4ITHycSuvYcoSLm9Bx63bEMz5dgNfgW_YfsLw472r4CCwu8STLDOPIF_-zifIv0aGhiov4LlU5z_J3VC9Hv2AYBsMfkJfYHIezjPYAzwBoDw7JbwyUYXQAkb7QetiuN3VU0jB-nhR8FRUu4rNQhpaTBi3bA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مسعود پزشکیان در جریان مناظره‌های انتخابات ریاست‌جمهوری ۱۴۰۳ با مقایسه وضعیت امروز و دوران قبل از انقلاب گفت:
@News_Hut</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/67066" target="_blank">📅 09:03 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67065">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/67065" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67064">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nwE5adGO0A2e4t-WOKYdZvMgzGnpuhb6JSU6yE6EbzMcOIbuiHDYbDh4P1HSmt-P_yabtcpdAvCvzf_AXUkF0hfXj3yI23mBCpoHkX3eOS-AG4TQELepD8DDOa8eGy27rX4wGWmuDfhVarp6ctp7_bbL6THhXZVUyqoMILakcBkRrC9qTgIOP_-7s66Y-GiyFmNXF9neHRNw9FrguFAYHxRPnDgJLFidVrFA8_RxOuHHVA_t41IKOY-wBDXRJLbKbOhfb34hZ_icHJQLq-0XsJhQ6HSr7ScC9ReOMMUVK3nxXplCUJzMZBvkBPulagKP4oJC2leA1-xy-9CeatnHpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67064" target="_blank">📅 03:04 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67063">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
یسرائیل کاتز، وزیر جنگ اسرائیل:
احتمال دارد جنگ مجدد با ایران طی دو روز رخ دهد.
وی اعلام کرد که نیروهای دفاعی اسرائیل آماده عملیات و هدف قراردادن ایران در صورت استفاده ایران از موشک‌های بالستیک خود در راستای دفاع از لبنان هستند.
او از آماده‌باش کامل نیروهای اسرائیل خبر داد  اما خاطرنشان کرد در مذاکره و اقدامات آمریکا در راستای ایرانی‌ها دخالت نخواهند کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67063" target="_blank">📅 02:38 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuPm5O56Hc8vFKDluvi7WZbpUa-HQsqw5K6C_hAH90F9XRGhBA-QSaDf0Q4H4mwnZMuHWAQRmF5ntuM_wD4Kc3UIfbuYzjvF4mSnYEF31gHmYNWb93gLB9RRDJi3-IWd3eOTqdKS0xGdY_DbGXpsMQqvg0Xidv20WkcPckBW_feplOrjbUrLK5zmlkFp3owXs3fkQqyo2fJBVkpFsNPjcIGLIWoqEAVf7sen7ExulsDnOvSA3FcFo5LTCCcbw64OEGb8IYV5Tcd8EoSiAc0uHfQe0AfrlDtA_Y66ghWNlo55RgM28lDv--5ccc2mvqvgIEQ6O_OF76EQGgYGHRNHUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
تصویری از بیمارستان پاوه و هجوم خانواده های نیرو های امنیتی به این بیمارستان،به نظر تلفات و زخمی ها بالاست.
«کشته شدن سه پاسدار تا کنون تایید شده است.
سیروس درویشی،خالد خالدی،برهان کریسانی»
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67061" target="_blank">📅 01:58 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
🚨
🚨
⭕️
⭕️
گزارش‌ها از درگیری و حادثه امنیتی بین نیروهای کرد و نیروهای نظامی در شهر پاوه ارسال شده
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67060" target="_blank">📅 01:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1VvbRhQieyeylbv5sAEnvXBPih27tSE-OT3hZFZmfKSR3ZQ0GBdDBEa_ProVn2yPJuvuU6xRoY3j3YbVnQO-OlTdYTDVZY4DyQzK8ZOZDSG0Y6MjIiYkLakeeJ7E9_RMEWv8y9cc73me_BdhECmnZY-ue10qp0ZG-IxGGgGyVDjZyGqtnuxeqXW-SowGBquYH9gAEICMUgxfXeWTzSuQqOcDjUsgH1SAxWp77KFROsOLWCAqPY2LoBe35YwVoYCkd_OwLlR4GVDAPfnxqAPsfYQI-aletr0DSykihRxe0ctPToeU9vEBJTL28jPMmvChiWxbvGqEHBiDLS4VVqBKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
تفاهم امری طرفینی است. اگر طرف آمریکایی به تفاهم نامه پایبند باشد ما هم به تعهداتمان عمل می‌کنیم.
رویکرد ما در مقابل رجزخوانی‌های نامعقول و تهدیدهای بی‌پشتوانه، تکیه بر عقلانیت و کرامت انسانی در تصمیم‌گیری‌ها و دفاع قاطع و بی‌پروا به هنگام عمل است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67059" target="_blank">📅 01:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
🚨
🇺🇸
ترامپ درباره ایران:
این نشست در دوحه شاید مهم باشد، شاید هم نه.
خواهیم دید.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67058" target="_blank">📅 01:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15a452960e.mp4?token=YmYANDidpyWG7Ybuo9dO1W8mmaBojoO5jSnx5Cxlyvr-2kZefkygjMfJ6wgQrQX4wr18CKGEGLJc0ZtoRq_CoZhdO6TytkrwGSoHtOMoVsvsdWz_kIOomcY6kVIThDCAaLAiHnf8otrFo3U1RBweChf7aELN_FvbzoHl1QeLaUwLg6A60U4JOexF2h2SvsX-3Nmss3cq4QozTRIJPqFT7TN7nON675qqjDSlmCKikC36kqyivbxovWUnzyvtuFq4wBRcJRFjT5bEwKXZipFQj8vXnMmZZXbHbUqJ1lUFeCp4jxRxQC0okSDhaQonRYljNsq4v2LM62dCmMN-QQyIZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
ترامپ درباره کمونیسم:
این سوسیالیسم نیست؛ در واقع کمونیسم است. آن‌ها از واژه “سوسیال دموکرات” استفاده می‌کنند چون خیلی خوش‌آهنگ به نظر می‌رسد، اما در واقع درباره کمونیسم صحبت می‌کنید.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست، شاید از زمان تأسیس آن. این شامل جنگ جهانی اول، جنگ جهانی دوم، حملات ۱۱ سپتامبر و حمله پرل هاربر هم می‌شود.
من فکر می‌کنم این بزرگ‌ترین تهدید برای کشور ماست. بعضی‌ها وقتی این را می‌گویم می‌خندند، اما افراد آگاه خواهند گفت: “می‌دانید، احتمالاً حق با اوست.”
این در واقع وارد کردن کمونیسم به ایالات متحده آمریکا است. هیچ‌چیز تا این حد خطرناک نبوده است.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67057" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UYG04gGyiWt-iW27UiwRwGZ8eXhndbw6-hGop29vfaQhl4hIT-FMTnC27_9ZQlsjeJGJtf9VXtHkWp5meHUp6uw8yuM2QZQ-j9dZKmKp0jdYLJ_Ymt_CqIGFXwMxjtVdJEqvdXhVFYbBVqbUmuyJ_WskIH05DHxYFiBAvXdcEjnOQ-yRZOiHVg5Ap1buIMTNF8YegOsoAnkIbK4oFatNbtB5JXTpNpPZAjy_KBrAxPk21tXTzgbWb3Te2pesqi5ctcu4PK0Pez07fpMBmZtYZnRkyoJ3Xs_H9fSa8O-ZXIQ4XuOOwQge6QIgldrtUrgpMOwCPJ6hpl2KwIzYL-pozA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/67056" target="_blank">📅 01:14 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9c7afb034.mp4?token=ao3Q96S8gPg6ZLJqZrhvlMVBt8oWWFs9RkY017XfhAv5gzvo3ZLP18KrsQbI_LvI5VKi-WJi0Y8ZHoycjWYnZbLPB6ioMmSiiIBW45-uX68Z2s8-6fROqTV7eVOcxuV9wmXRuHZp9Xcn56p9ezdbIqURyJg9-Y5gIXkryJL1YMgqzcmHD82d_QoN1uzkQM8_y16751px-jU8WqmErKAlVSN8EFmK85lxhc8LJck41382o0buP5ok0SnMsfZFLC7PscpaDZEXDOpN7qHMZfA1LDfNIiUmFUj2AF2n5JHmNaPkhJYRJ-bETh0Uku3hk_yRQJPyvOzioT5_bjJzYl2rrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67055" target="_blank">📅 00:01 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1336110317.mp4?token=JKzAjanDdNl2xJcvfvXyjFLMPYYukr9HY3FPW3eWiCEfiW8wmXORPAOm-sSn8QiKYSO8Z-S65RGagixxD8kdTwRBzfWdfrc6qEA28sh4IkA7jclpEUFzw8orCYW7_odXcrZzbNb6YAr7gBQSafxICeWJEs_eMRSv_pssDwZtDi-NkPB76EarRj7e7_1KGmzXXaz-zGkGNPbsVt0IWfHVRexOQnZM382tGelFwFoUIHToh-aflzVTxIhCr5dE1ehHQo3KJ8wXzLFe3eUjwSSWIFHiz_cO9OiOgMqMaCsEe8DxwhO-tIu1ahvEQdR2-vt7hQ9pZ9dohNuYFVjpQNKtSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادگاه محاکمه ترامپ و نتانیاهو
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67054" target="_blank">📅 23:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e959102c72.mp4?token=A7nDCwr6ovAxonhwRjQ3-PhFiH_GgkSSXhq6ZT6f_0Z5FpBTDL4KcsKjhexaJsvtQNUnXRb94BksN03kNRpfpBylAZcExbBtEt7t2axdJikGJnLnRdW3wk5MsAAbFJOzvBFiFm_cR_SJNysXM9Z2t5iWie21XpizWFVnKD_LDNwkTreZLiSSJFovJQIC3iuWQr64zXO-n08Xmg6V8TI--dcOv3X8nAv-9Hnzi6yr4ByA0X95hl7ScLd6g0BFp6Kw2-j6kTmqPuS2zKdJANtcreyxZsia4Qi9ALvI7kwN2mbDpbpEu2F3PuOgrxWyUx7H86Wrz2Kcu6k5o_lWQnYMKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e959102c72.mp4?token=A7nDCwr6ovAxonhwRjQ3-PhFiH_GgkSSXhq6ZT6f_0Z5FpBTDL4KcsKjhexaJsvtQNUnXRb94BksN03kNRpfpBylAZcExbBtEt7t2axdJikGJnLnRdW3wk5MsAAbFJOzvBFiFm_cR_SJNysXM9Z2t5iWie21XpizWFVnKD_LDNwkTreZLiSSJFovJQIC3iuWQr64zXO-n08Xmg6V8TI--dcOv3X8nAv-9Hnzi6yr4ByA0X95hl7ScLd6g0BFp6Kw2-j6kTmqPuS2zKdJANtcreyxZsia4Qi9ALvI7kwN2mbDpbpEu2F3PuOgrxWyUx7H86Wrz2Kcu6k5o_lWQnYMKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
عزاداری پدر جاوید‌نام داوود عباسی بر سر مزار فرزندش.
جاوید‌نام داوود عباسی یکی دیگر از کشته شدگان اعتراضات ۱۸و۱۹ دی ماه ۱۴۰۴ ایران بود.
داوود عباسی روحت شاد
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67053" target="_blank">📅 23:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKP7sKgugcA_vIDz5wc0Zmf81oqxNd_ZJhs-fEZUPg_pScAGgZQ1XXnkzJ7OxxssYwu6kZaVjVttDljET7S3P5Br0srkrLxazaXqSXoac6rqcIkfoVpY1gl72H9ATsxQoBhFa6dSwPQrVuKD1BBopsfym5u7iSoQ2EQ3sfEZ-OiQtntbKoVm-wZssf412zl8wfZ1KpoXVz69kBcgZuNwJzBZT5evWQyyG-jcpFbfsGoyoQL_jmX2v3bA2hSvpB80fba8-SgYf5wVinov8dplffacZy44_PEunxmZkLitRwUu8CNl8psk7JPfPp04G6zcVMIo8uwGhzBCRszK8mEblA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرگزاری فارس
:
معاون سیاسی نیروی دریایی سپاه طی سانحه کشته شد
.
دریادار دوم محمد اکبرزاده، معاون سیاسی دفتر نمایندگی ولی فقیه در نیروی دریایی سپاه، ساعاتی پیش در یک سانحۀ رانندگی بر اثر واژگونی خودرو در یکی از جاده‌های استان کرمان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67052" target="_blank">📅 22:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">‼️
اسماعیل بقائی: هیئت کارشناسی ایران برای پیگیری اجرای تفاهمات عازم دوحه می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به وضعیت اجرای بندهای مختلف یادداشت تفاهم از جمله در رابطه با موضوع فروش نفت و دسترسی آزاد به دارائی‌های مسدودشده ایران گفت: در رابطه با تعهد آمریکا طبق بند ۱۰ (فروش نفت) مجوزهای لازم از سوی آمریکا صادر شده و پیگیر روند اجرای آن هستیم. در رابطه با بند ۱۱ (آزادشدن دارایی‌های مسدودشده ایران) نیز فرآیند اجرایی شدن آن در حال پیگیری است. در این چارچوب، همین هفته هیاتی کارشناسی از جمهوری اسلامی ایران به دوحه اعزام می‌شود.
​
🔴
بقائی در پاسخ به سوالی راجع به شروع مذاکرات برای توافق نهایی در چارچوب گروه‌های کاری تعیین شده، گفت: هنوز وارد مرحله مذاکره برای توافق نهایی نشده‌ایم؛ طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات توافق نهایی، منوط به شروع اجرای بندهای ۱، ۴، ۵، ۱۰ و ۱۱ و تداوم اجرای آنها است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67051" target="_blank">📅 21:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">‼️
بقائی سخنگوی وزارت خارجه: هیچ‌گونه مذاکره‌ای با طرف آمریکایی طی روزهای آینده در دستور کار نیست
🔴
طی روزهای آتی هیچ نشست مذاکراتی در هیچ سطحی با طرف آمریکایی نداریم و اینکه نمایندگان آمریکا به قطر سفر می‌کنند، ارتباطی با سفر هیات ایرانی که برای پیگیری اجرای مفاد یادداشت تفاهم از جمله بند ۱۱ انجام می‌شود ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67050" target="_blank">📅 21:19 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=D-8AnW7Q14ydrJt6VdGI6miPg3tnqdzLenPs_Sn8c8MgnOogMArRCwK-QIf0Lk5nUKDlD0gH_6W1RfGrsmfU3DBmTyBxNMjLT1bdVNScCdv6LL6bLva7tG2rQHgjinXJu02XIVJ-VZWixLRKdS3eUuV_DQ-D3isZ2fxZSh6sowshCLCyeTZhFic3Ti300JIDBqFxBeWmTqSI_ek9MSGEXJN-HgIEWv_B-HJGpHfBP_g_wUolTdbLEY7Si0YzF_bXFLC5QkZ9X68JVDCyKnbN8FEShP8FFXdLvEan1uqKAyuCDCiljZNQCo8Yp20gtB_CQNnAdKxUg1eueBKPYkH5oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5249169d4b.mp4?token=D-8AnW7Q14ydrJt6VdGI6miPg3tnqdzLenPs_Sn8c8MgnOogMArRCwK-QIf0Lk5nUKDlD0gH_6W1RfGrsmfU3DBmTyBxNMjLT1bdVNScCdv6LL6bLva7tG2rQHgjinXJu02XIVJ-VZWixLRKdS3eUuV_DQ-D3isZ2fxZSh6sowshCLCyeTZhFic3Ti300JIDBqFxBeWmTqSI_ek9MSGEXJN-HgIEWv_B-HJGpHfBP_g_wUolTdbLEY7Si0YzF_bXFLC5QkZ9X68JVDCyKnbN8FEShP8FFXdLvEan1uqKAyuCDCiljZNQCo8Yp20gtB_CQNnAdKxUg1eueBKPYkH5oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ناو آبراهام لینکن امریکا توسط سپاه غرق شد
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67049" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=bun8Hrp60ciYvkIh5wD_HQOtyp8xGovtQs9QBS9bQ_YPl4ojFeJRpqc2Y3SEBAizi5Ze8B53XF476Haz2TKaC_K0xRszkh1XqiveacdHr1EDLUAQg3LMbO8nyP8kJiDyYLCQi55bIVa2AHuXvUxd-msRffbqG55MsaIjElYXe3CkSVOZzCpLaMBlJPICMXUxUSiWikFUnAmwPRH1h8xEGs3raoAk2pW_Q09kMUUk3-bUFN4-XPkNuLRIegohMZUBtefLMGO3xcNNzEKwgDYPOgSgYGiEaYqmFloU2DBhglZM19iI-MUeD_mmlMsF27d6nSWOvBxEkDX0_MpCq5z8CYheH93feFObTnUQsWrUTV1r9FjmjmkP0aASnJd04bL6NEa4OgEbKBghlKtT9OifpfAmlwlskVix_09Vi14GRBwf3jWrEPOHS8xXVf8YqufqSbhBDNIT8QQSYCNu3mvpWlkfj5KREOPwuTuI9nQF9iGLFknpzw4qXec6a0BvBuSOuFQHDbPDuNlhifKIxBssuM8GEPBdpw6rRux0qVUhR6t8GdjwGxEPPUg919dZCM2iXH2YZp72TZ-SHguIpVz-YAa9EHvD8DC7AJfyG4B2doJDpvekQNxD3QkPzTlT7d7M3RtEpzXJggmx1rm8zavyPGq7wr-5pbEEMfAE5IUu5ss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15026d52cf.mp4?token=bun8Hrp60ciYvkIh5wD_HQOtyp8xGovtQs9QBS9bQ_YPl4ojFeJRpqc2Y3SEBAizi5Ze8B53XF476Haz2TKaC_K0xRszkh1XqiveacdHr1EDLUAQg3LMbO8nyP8kJiDyYLCQi55bIVa2AHuXvUxd-msRffbqG55MsaIjElYXe3CkSVOZzCpLaMBlJPICMXUxUSiWikFUnAmwPRH1h8xEGs3raoAk2pW_Q09kMUUk3-bUFN4-XPkNuLRIegohMZUBtefLMGO3xcNNzEKwgDYPOgSgYGiEaYqmFloU2DBhglZM19iI-MUeD_mmlMsF27d6nSWOvBxEkDX0_MpCq5z8CYheH93feFObTnUQsWrUTV1r9FjmjmkP0aASnJd04bL6NEa4OgEbKBghlKtT9OifpfAmlwlskVix_09Vi14GRBwf3jWrEPOHS8xXVf8YqufqSbhBDNIT8QQSYCNu3mvpWlkfj5KREOPwuTuI9nQF9iGLFknpzw4qXec6a0BvBuSOuFQHDbPDuNlhifKIxBssuM8GEPBdpw6rRux0qVUhR6t8GdjwGxEPPUg919dZCM2iXH2YZp72TZ-SHguIpVz-YAa9EHvD8DC7AJfyG4B2doJDpvekQNxD3QkPzTlT7d7M3RtEpzXJggmx1rm8zavyPGq7wr-5pbEEMfAE5IUu5ss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وقتی کارشناس برنامه خط انرژی به غیرقابل شکست بودن ناوهای آمریکایی اعتراف میکند:
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/67048" target="_blank">📅 20:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗱𝗺𝗶𝗻 VPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJaPB8b2dzs4BxI6QGbkVK3f54QnMEjXXxvfUmbWNzgL0uLgmecqeLlB8ut2NfLkgLnqjv90BqadFYo0zUdjBiIxOjzhG4NI46aR1veQcu_tmKpuf1FNa79l7n9yctkxaWio7n7te0UmydEeaWRk4-NrLBP7QsDBOBuTNUW4ug4wf-_NkiTeR0uj9w91UoY4_cPeWY2v-8OY3qI-0LwVrvDXlSksiaOLeUQoH5WCxUKklUEcISyzLNKbz8ZUUPvohuSsEuRtxYqoOPcVifjxabfb9pC-6IUkRyWDYnowkgxEH37hh1I4CIzk0Lvpy_MjVnMsBpjaNefDdbfOx2DfLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆓
رفقا
توجه توجه
✅
درآمد تضمینی روزانه 35 میلیون در منزل
🌟
تمامی ضرر هایی که این چند وقت بخاطر جنگ دادی  رو جبران کن
✔️
🚨
⚡
⚡
⚡
⚡
⚡
⚡
https://t.me/+ArmBt6ZWMF84ZDlk
https://t.me/+ArmBt6ZWMF84ZDlk</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67047" target="_blank">📅 20:56 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🚨
🚨
نیویورک پست به نقل از یک مقام آمریکایی:
ما به ایران روشن کردیم که تا زمانی که پیشرفتی در پرونده هسته‌ای حاصل نشود، دارایی‌های مسدود شده این کشور را آزاد نخواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/67046" target="_blank">📅 20:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=FpJFEcQ0NyJc0-VExZIpu9LSXaKJXaSbPwv7L-k9FZ-J92pQYhVQjKNRcFP-VU4l9Yex5UHok-MvEcTycb8dpv1mhFlIpFAg949hkCAm0SX8F3DXgJIRQDT15GJtmM0m5sLcfWZdvfKKUcU5agB_1vAvgoiTWlgJOQ9BwKNCwiwh6Woim2vBC_OCFU4-_v2uk3D4J52_PjD8GhAmkcPRJYrhiZUQ_5s0RXAJQI6K7-aSa6o3ChkcMtuVtgoSun0fbsytVhq93FWwUSgbGk0p-5KN8scb_JBMbu0b_xsbdGkSPfb72F857HT5IcsQjqig4yZ3kceJF-BXaR2BiRM1PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a60a7af63.mp4?token=FpJFEcQ0NyJc0-VExZIpu9LSXaKJXaSbPwv7L-k9FZ-J92pQYhVQjKNRcFP-VU4l9Yex5UHok-MvEcTycb8dpv1mhFlIpFAg949hkCAm0SX8F3DXgJIRQDT15GJtmM0m5sLcfWZdvfKKUcU5agB_1vAvgoiTWlgJOQ9BwKNCwiwh6Woim2vBC_OCFU4-_v2uk3D4J52_PjD8GhAmkcPRJYrhiZUQ_5s0RXAJQI6K7-aSa6o3ChkcMtuVtgoSun0fbsytVhq93FWwUSgbGk0p-5KN8scb_JBMbu0b_xsbdGkSPfb72F857HT5IcsQjqig4yZ3kceJF-BXaR2BiRM1PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زنده یاد مانوک خدابخشیان این تحلیل رو سال ۱۳۹۸ مطرح کرده بود؛ تحلیلی که از سال‌ها مطالعه و شناختش از روابط بین‌الملل میومد. حالا بعد از گذشت حدود ۷ سال،
با دیدن اتفاقات امروز حرف‌هایی که اون زمان میزد، داره عیناً جلوی چشممون اتفاق میفته.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/67045" target="_blank">📅 20:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J8I8Bi-pTQYbHOP4w1CbUhvSdFNaV4MjnWCCk8dghKGZ39NN2tvs1bpElAjxMb6o_sk3IYZHmoyS4kL4fs0FePNmhNJN9D6bm3WnBadWQvT9aNuBCkC2zhSVqWzdUrK3AeBYWZGBY9cJ3kJpEt7_bEn3BJM9HcmcPMoQ82WsrqoFriGTPc7mfno9GawA46HcHlmbMkcv0DPzEQceIf1TV20xQQAtykVPxuEBTPkvFZki7WokmDVDwXiFXit1OXHJGJAyalQZG2excFdc9ZJfvdsZYzyewbghZ_3tmm3GbC6XaHL34Sla9trY-zlL-7tIYW-Cj9uKgcggwHgysAqTSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
حمله ارتش اسرائیل به دیر میماس در استان نبطیه در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67044" target="_blank">📅 19:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🚨
🚨
🇮🇱
یسرائیل کاتز:
اگر ترامپ تصمیم بگیرد که مذاکرات به نتیجه نرسیده است یا اگر ایران به اسرائیل حمله کند، جنگ با ایران می‌تواند دوباره آغاز شود.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67043" target="_blank">📅 19:41 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=ro1XDoWQrai7x2AxkSKiIKi1xX1pWnedF6YUkl-dYt8qGXyng5y09t6lwTP0ySJTu32QdmobZU7LYhcYXR2eC8hD3Sz1qZh3CMYBdLprM8UrfbH6VEACW-Oh5xDvztibJz4MfK-ouLcBF-2Yr5QKTHHHKrnWjJvTMARQQKTCtp7GoyylMQD9S7tdQ_TP77m-Gi1ND-h4dCm2pfkpOQQVQYYaJ34Q_0GhM4hpaNKKDegOn51RCl__y8EjrT_3uQMTyKG-mSbUU-F4P605Sqy5h1j_EVfzlZQOC4izuE3ZgFFrRIljEYrVCw2STjwuGSWch4EEr5Z7RNbtigDBaOLgKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ea6a79f9a8.mp4?token=ro1XDoWQrai7x2AxkSKiIKi1xX1pWnedF6YUkl-dYt8qGXyng5y09t6lwTP0ySJTu32QdmobZU7LYhcYXR2eC8hD3Sz1qZh3CMYBdLprM8UrfbH6VEACW-Oh5xDvztibJz4MfK-ouLcBF-2Yr5QKTHHHKrnWjJvTMARQQKTCtp7GoyylMQD9S7tdQ_TP77m-Gi1ND-h4dCm2pfkpOQQVQYYaJ34Q_0GhM4hpaNKKDegOn51RCl__y8EjrT_3uQMTyKG-mSbUU-F4P605Sqy5h1j_EVfzlZQOC4izuE3ZgFFrRIljEYrVCw2STjwuGSWch4EEr5Z7RNbtigDBaOLgKTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تردد در تنگه هرمز در دو روز اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67042" target="_blank">📅 19:02 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=WHh-9qTXcH6u8dtTgGtToDQC5lNm-bfIHMuFU-fhC9cKXZCO4mt3i_Fr35-zq37ZmqLwL5Vk_WxYWF0cr1yojiJsCS34Tgc5TAlFqxZG0Jl2foDIJBPBmGJ6Lcfw6QRMfFGx6TcTYF-cYjHkLDANOlHYx4QB54Wu8oCpLbjvdmvwikZQtIjb5yjCkYZnOLXFHFhdldwdvL8seaw9lfmnCAZ5lVnADG2_doLb0WgckJUDyaXOPmTHT9IpxHLP1EvNBtlFqSODGKP7nMAANzsMeFHn3ESuG71N0R6EzxcsjPDussX_sltjk89JyVoXkMjmf6i0DMhmvcsd7pqUFEj7Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f9b7cb450.mp4?token=WHh-9qTXcH6u8dtTgGtToDQC5lNm-bfIHMuFU-fhC9cKXZCO4mt3i_Fr35-zq37ZmqLwL5Vk_WxYWF0cr1yojiJsCS34Tgc5TAlFqxZG0Jl2foDIJBPBmGJ6Lcfw6QRMfFGx6TcTYF-cYjHkLDANOlHYx4QB54Wu8oCpLbjvdmvwikZQtIjb5yjCkYZnOLXFHFhdldwdvL8seaw9lfmnCAZ5lVnADG2_doLb0WgckJUDyaXOPmTHT9IpxHLP1EvNBtlFqSODGKP7nMAANzsMeFHn3ESuG71N0R6EzxcsjPDussX_sltjk89JyVoXkMjmf6i0DMhmvcsd7pqUFEj7Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وزیر امور خارجه قطر:
ایران یک کشور همسایه است. باید بین ما و آن تفاهم وجود داشته باشد.
آنچه اتفاق افتاد غیرقابل قبول است - هم علیه ما و هم علیه بقیه برادران ما در کشورهای خلیج فارس.
اما در نهایت، همه ما بخشی از یک منطقه هستیم و راه حل باید دیپلماتیک باشد.
ما می‌خواهیم یک منطقه مرفه ببینیم.
ما می‌خواهیم یک خلیج مرفه و یک ایران مرفه ببینیم که به طور سازنده با کشورهای خلیج فارس، با سطح بالایی از اعتماد و همکاری - به جای آنچه این جنگ‌ها به جا گذاشته‌اند - همکاری می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67041" target="_blank">📅 18:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=BmDnI0VRvWBxhzIre-XA7FnQsW5aiA6rqhgG8MQl2s1unvEuCjDP9XWg5oj6J808n8Bt6dBJmKjRZ0hSafvaYoFTFl2C1pGlfJ53HMgCPaBzqu7YwP35hxy2kwr-aiTOM1e2JhRTX7bd3MuqNvsNAoVkX8_9KDJ-ECfq7mJbx3hbbzvj9gRrrfKCrMx2Ezz4OG9D-FsQEfMXI03igGm4b6tLKronUtwYx0Z5YAxLKuWUHYuVBSnSmP5SSudsu8j0zNpNtR9BTUIrCdIVuY9Jwsi7fpO8GHvbnz_Lb1Mrdz_gV3EL7-gsQKqUl6Z_lFg-0yRpW9v0v7V1-E4tVVt3fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4f066d85d.mp4?token=BmDnI0VRvWBxhzIre-XA7FnQsW5aiA6rqhgG8MQl2s1unvEuCjDP9XWg5oj6J808n8Bt6dBJmKjRZ0hSafvaYoFTFl2C1pGlfJ53HMgCPaBzqu7YwP35hxy2kwr-aiTOM1e2JhRTX7bd3MuqNvsNAoVkX8_9KDJ-ECfq7mJbx3hbbzvj9gRrrfKCrMx2Ezz4OG9D-FsQEfMXI03igGm4b6tLKronUtwYx0Z5YAxLKuWUHYuVBSnSmP5SSudsu8j0zNpNtR9BTUIrCdIVuY9Jwsi7fpO8GHvbnz_Lb1Mrdz_gV3EL7-gsQKqUl6Z_lFg-0yRpW9v0v7V1-E4tVVt3fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
جزئیات اسکان و تغذیه در استان تهران در مراسم تشییع رهبر شهید
اطلاع‌رسانی رسمی جزئیات مراسم تشییع در کانال پرچمدار
👇🏼
t.me/Parchamdar_tv</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/67040" target="_blank">📅 17:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=Is8JUgGK7S3pzYLsWhY1kshV0UQKf6M-OvUrNQ3exI0jRpB83s13DNMKfKwvEpC91jV5AOZcO1WYefnBTSDwRlU74B0m66ZOIkgYcQoBXzOGL2YVTYeb2UUTDHHiZ1-qECi7kBvyhBoEJ3V9XzS6WiKimAXmF-16ZQtmDxvafD6p9vVBNEcQYlng6HGrce9p8Y2RfYVuXnAYM8BBMQwzlwuQWw0wpMiIqrdnrf3UkfEhxbXLwl2re08c4LUSDq7Fr_16DEGhzisq9TJYNgzCI8yTs8VS4Zrp0afNgB6ta7yWq1ZXA_ill0INlNK8zH4LF9ZZ-1LNDJ8Q0cat6YwgYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78917b25d9.mp4?token=Is8JUgGK7S3pzYLsWhY1kshV0UQKf6M-OvUrNQ3exI0jRpB83s13DNMKfKwvEpC91jV5AOZcO1WYefnBTSDwRlU74B0m66ZOIkgYcQoBXzOGL2YVTYeb2UUTDHHiZ1-qECi7kBvyhBoEJ3V9XzS6WiKimAXmF-16ZQtmDxvafD6p9vVBNEcQYlng6HGrce9p8Y2RfYVuXnAYM8BBMQwzlwuQWw0wpMiIqrdnrf3UkfEhxbXLwl2re08c4LUSDq7Fr_16DEGhzisq9TJYNgzCI8yTs8VS4Zrp0afNgB6ta7yWq1ZXA_ill0INlNK8zH4LF9ZZ-1LNDJ8Q0cat6YwgYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه داماد، وسط مراسم عروسی تازه متوجه میشه عروس 11 نفر از دوستای پسرش رو هم به جشن عروسی دعوت کرده؛
گفته میشه داماد اول فکر می‌کرد اونایی که دور عروس حلقه زدن، فامیلش هستن؛ اما بعد از پرس‌وجو می‌فهمه همشون دوستای صمیمی عروسن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67039" target="_blank">📅 17:40 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=C96lNuXLcfRLxLC1OB-vo6dCzRCmzbU_jU8Z9Z9F8LNfAm1132-rjzkmoeQmGRuz-4KI7RLgiBM68G7rhLATJurWyD0psWw63etyxOKB4xHQe371qTjdk9L8Mmur2Sqluj48rXRnsRqy0vMyIozD5IOhdQ874ezeTsCUZCB3JUGNgCkMQWtoW8jF7Vem2UGY4uTlX_GBVEsbmkRzvyuNPBrySSusf8dHY-m8kwZh7QWLMkdvLfJvEwXm-wbbt0k8DzGMfwvyQsZxMVp5my5Age0777q3Qo2pjmDNOLCCR-Oezn0M4pbfemVDKFG0NJvQehfSVjXhNZ-4gw_Ev7_FYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de1b4e3a38.mp4?token=C96lNuXLcfRLxLC1OB-vo6dCzRCmzbU_jU8Z9Z9F8LNfAm1132-rjzkmoeQmGRuz-4KI7RLgiBM68G7rhLATJurWyD0psWw63etyxOKB4xHQe371qTjdk9L8Mmur2Sqluj48rXRnsRqy0vMyIozD5IOhdQ874ezeTsCUZCB3JUGNgCkMQWtoW8jF7Vem2UGY4uTlX_GBVEsbmkRzvyuNPBrySSusf8dHY-m8kwZh7QWLMkdvLfJvEwXm-wbbt0k8DzGMfwvyQsZxMVp5my5Age0777q3Qo2pjmDNOLCCR-Oezn0M4pbfemVDKFG0NJvQehfSVjXhNZ-4gw_Ev7_FYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جان کری، وزیر امور خارجه پیشین آمریکا، درباره ایران:
اوباما تحت فشار و اصرار نتانیاهو قرار گرفت تا در بمباران ایران مشارکت کند.
و از اوباما درخواست شد که اجازه (چراغ سبز) بدهد تا این اقدام انجام شود.
اما اوباما گفت نه و از مشارکت در آن خودداری کرد، و آن را یک اشتباه بسیار بزرگ می‌دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/67038" target="_blank">📅 17:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=iTo5JhEF1ChEgehnxOcEdt1fDcsnLXRC4AZCavHayQmC8wCMezvyBGu1ubDHDoC21Ot_PX9PEvoP1qEmi0jMk1FNvPBOWS38G-YIOibUsTdgW73ovVxlvE4518wCKmE7TaBeyr-2dgbXmqJ17ZK_kmFD00q_gpAEiET0vxwmg4mvjxR_oSzEqrLk5Nz18U-_LJ_ZOYIsoulolsuh1Fu5skqsK4UMOm9SUybgHw86ZEBt0tWBrZLWj0fB1q8oh9wZ9_qxpuxSY_Mj9i2M4wMV32e_TQZscKeCSA3ZxZfhr2ED6aMNFXzjeUSoL7gwstO0ZRHfbUcC9CbyUDaDJAye-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f6a02f29.mp4?token=iTo5JhEF1ChEgehnxOcEdt1fDcsnLXRC4AZCavHayQmC8wCMezvyBGu1ubDHDoC21Ot_PX9PEvoP1qEmi0jMk1FNvPBOWS38G-YIOibUsTdgW73ovVxlvE4518wCKmE7TaBeyr-2dgbXmqJ17ZK_kmFD00q_gpAEiET0vxwmg4mvjxR_oSzEqrLk5Nz18U-_LJ_ZOYIsoulolsuh1Fu5skqsK4UMOm9SUybgHw86ZEBt0tWBrZLWj0fB1q8oh9wZ9_qxpuxSY_Mj9i2M4wMV32e_TQZscKeCSA3ZxZfhr2ED6aMNFXzjeUSoL7gwstO0ZRHfbUcC9CbyUDaDJAye-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
ویدیو ای دردناک از لحظه وقوع زلزله در ونزوئلا
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/67037" target="_blank">📅 16:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=GEhsiK9zLlK1bjaTnOZLd-1tN4P-lYCbJye-w5cLMc5-p-uj0NsNsgQBxG5zbEeN9iOwGjFqh4oaDRnDSbCPpRkrLjvComJ7L2dzYsA-5nEyczjaxH-bJgHZJhba0xXBCJjC2UIxlIEw2g0s34wSQ1ZveuxmW6eU1oOsal7MfJ0cUWBy9n4RWQu_735dbSDQs7Zud08xbxGvw25TKV74B2aYajP-miY1Yv2JZUxoiyBw45IjVbNmTewdPWFp0KkDBUX7gOsYCEe38dLah4TiiBubo1MTFzmzghY1G_G1diAexDX9NgJbF2Rat8dRAbwfnLKNtIziPfViDINiZ3IcNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e63aa7bc7.mp4?token=GEhsiK9zLlK1bjaTnOZLd-1tN4P-lYCbJye-w5cLMc5-p-uj0NsNsgQBxG5zbEeN9iOwGjFqh4oaDRnDSbCPpRkrLjvComJ7L2dzYsA-5nEyczjaxH-bJgHZJhba0xXBCJjC2UIxlIEw2g0s34wSQ1ZveuxmW6eU1oOsal7MfJ0cUWBy9n4RWQu_735dbSDQs7Zud08xbxGvw25TKV74B2aYajP-miY1Yv2JZUxoiyBw45IjVbNmTewdPWFp0KkDBUX7gOsYCEe38dLah4TiiBubo1MTFzmzghY1G_G1diAexDX9NgJbF2Rat8dRAbwfnLKNtIziPfViDINiZ3IcNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حصیر آباد اهواز؛لحظه ساییدن سیم‌های برق شهری با «برج میلاد»:
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67036" target="_blank">📅 16:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🚨
🚨
سخنگوی کاخ سفید:
استیو ویتکاف و جرد کوشنر، در نشست روز سه‌شنبه در دوحه با جمهوری اسلامی شرکت خواهند کرد.
همزمان با نشست‌های مقام‌های ارشد، گفت‌وگوهای فنی نیز برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67035" target="_blank">📅 15:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67034">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6e2Pwd0CwFdr2vCJBRa0Haxcp0vqFgidnze8SJgqOFSekW166Z_GwXeri3aX4eCVonejCR9CLl0Rrwt4WmwMg3-sAuceIHIJvf-Ajqj-z6NwGvDY1Bv2mss9o6ACbTPzr2vfP2qyp4TAX1uO3kFPEpQCewZvhMG-25NjtAHfCppcUwSzXWBwnfnRWV39VvNQNQa_-cL7b9O_Wo1Iuiemnr7ren00rmsXk_NKW5HfmfhoGrIFk7GQ8u_VGWGhapJSsmvcywSkfSg71KMuHMAeiCxw0nrtNCi4FqcixpXYEY0cV6oa7xMS2XdKfypJA3233Eygv3d2fzaecDCUAtFmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
ایران درخواست ملاقات داده است. این دیدار فردا در دوحه برگزار خواهد شد!
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67034" target="_blank">📅 15:09 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nGvUs4mgI_MvAun9fRJUTPkfkyDpFLcoKxx8iUOI2nGnNGsaSj5TazcX0HMWPUyZCYok_pbjmiMfKOGdBKpUN24NRPmWJegG0Dz76uyP-0tmbHAV4kkXrr48rKsbUnzY8XWLgSB_xLQ75QFo5lP3nA8C1VZjd92jke8wsYRsSGQIkjcuzesiZCuMOrINxUouwN1HTa3YtMSKm9_LZh-JUedvwj4UsbWTM94r1upa90wFOwJDu7WLx1xCFJ5Uj3SteLgLN-fAMv9HBRjW_N2OxXMAJQI_iB4hn_nak2ZR6JJZ_Nq_TtgNxH2fpCBTpwd2T4P1zc3Wb1vqDPPVBkIjBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
ترامپ در تروث سوشال:
محبوبیتم تو نظرسنجی‌ها از همیشه بالاتره
حتی از روز انتخابات ۵ نوامبر هم بیشتره؛ با این حال ایران نباید سلاح هسته‌ای داشته باشه
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67032" target="_blank">📅 14:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DJHTPv5HWKO-WDN1mREGeT5mp9IunGstalSx9ilmGwSRvIIh38D-s3nO7t8fsKb_O2To3M1BnrJyl0X7kbPssF0vUdmp4mF9xNBpjpWCCoTl1B1rg0zODsoyhpqn62gC__Vq-BYhZQp-ezhgFal8IEJWSp_40q1y3LEs2GlRJ02uuxyH6Kb3Paxiz2qHyuOUWXszZVbChaTJIvtmNAA6Qch0hqtkXug0OIJWnLo6jtPReVt0wBf_HVkZ1iku_blIfGxSK5aAMK_UPfYzFMz6-5TFoAFF4u9nzaEgqQKJXd3M7h9WqVMLtghpH7_f5fdRr-GZ_kdKlnNRwH9Ty4cPhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حسین شریعتمداری (کیهان) :
گام اول تحقق خواسته‌های رهبری در مذاکرات، تاکید بر تحویل ترامپ به جمهوری اسلامی برای محاکمه در مراجع قضایی ج ا است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67031" target="_blank">📅 14:04 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=hjoRKSF0SNvP3_AMSFwp7jAJXM6PwvpsUZNeCx2Lxc2R0CSCYQxL0PX5PlvNY_B5rGrP3GTvP0Pt3f3xHa0ktggCKrwPOLj-YmyG0LIc6gyU8MRH22maDkNQW2M1HmCbDbGcYCLuSEs-vwJzyL4jiM9h-A_8CHc1dRgRav6Vz7XQnzeFzEXvZgYKojoaqL6Hpggg8J9rCnL_mLdt8UiGupU53PnyO1twGoLjYQcHl9oU0hAd_NLiPVAqnr0ibebL-4P4tfPrJ5k0a7h8i69N5S7S-xXV7z9KOp-aZPp2EJyP2_Tbq_dFM8jvII53tI-RIPoaDjb4LS4yhT9HDXr-qFN--6yjJf9CQOVS7JZN3h9zBAPBFaH6DXrWNNZogLzPEuTN3HvmspnotjTwqsvZrUbXV281ewDfhoS49rkvnSzQjGb1WLd2QH5hTLIG0rIgESykgYM_uIpdNlZfp1vS0ZRE5yx5Kko_aigyjFzRuWl5wqrP9BXnudBhOxUh-Kvr0QAg1U9ty5qOlyZg-CcrKLmsTILTZLxMnRFicB_803CCV2S1PR0v70IUfgGBXUTXPIMz9MukCQV76Gfvjo22aT_d5Dn37nzSDwgCjDypuPscE5FL8_nhIG7d8zgcmLQ-3d9IXX5caIdzC-JB-fIZ-9ZIIrIRUfaE4D--gDvBDAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/311b818b7b.mp4?token=hjoRKSF0SNvP3_AMSFwp7jAJXM6PwvpsUZNeCx2Lxc2R0CSCYQxL0PX5PlvNY_B5rGrP3GTvP0Pt3f3xHa0ktggCKrwPOLj-YmyG0LIc6gyU8MRH22maDkNQW2M1HmCbDbGcYCLuSEs-vwJzyL4jiM9h-A_8CHc1dRgRav6Vz7XQnzeFzEXvZgYKojoaqL6Hpggg8J9rCnL_mLdt8UiGupU53PnyO1twGoLjYQcHl9oU0hAd_NLiPVAqnr0ibebL-4P4tfPrJ5k0a7h8i69N5S7S-xXV7z9KOp-aZPp2EJyP2_Tbq_dFM8jvII53tI-RIPoaDjb4LS4yhT9HDXr-qFN--6yjJf9CQOVS7JZN3h9zBAPBFaH6DXrWNNZogLzPEuTN3HvmspnotjTwqsvZrUbXV281ewDfhoS49rkvnSzQjGb1WLd2QH5hTLIG0rIgESykgYM_uIpdNlZfp1vS0ZRE5yx5Kko_aigyjFzRuWl5wqrP9BXnudBhOxUh-Kvr0QAg1U9ty5qOlyZg-CcrKLmsTILTZLxMnRFicB_803CCV2S1PR0v70IUfgGBXUTXPIMz9MukCQV76Gfvjo22aT_d5Dn37nzSDwgCjDypuPscE5FL8_nhIG7d8zgcmLQ-3d9IXX5caIdzC-JB-fIZ-9ZIIrIRUfaE4D--gDvBDAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوش چشم کارشناس صداوسیما:
آمریکا فقط به دنبال باز نگه داشتن تنگه هرمز است.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67030" target="_blank">📅 13:20 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX39e6GmpAfDPi0K2Fgawot8m1LBGwufkVGko7XAibCdvexaxWMlMdEAWCARKGQEhWZFzUI8pdUF6q94xdi0aCMOEV07ngHozaivE4MIHwinLj6N5SDEGWYfstOxUzzmiCmwvcxuYMQwQ-wV-Up3c7YR1-_A9nbhNfAjf34cJ8GuXuqlmNWqQ7Y_h6B2PjbRE-kpoqrMsdkFKx2T6WYvDjdYZg-lpT-a1hjmKkMRbAYUmWGcRJttuJhBJqEFthe6rkoEeDQNhjz3o62J2YBs6QoRG6X9HcYsjEsOSZ9nJrtLsu1HbodCV1a1NLg-a0ukQy0oiPiHYdo-fSbNpGdxpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرزشی : قالیباف ٬ عراقچی پس خون رهبرم چی؟!
واکنش صادقانه ممباقر و عباس اقا:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67029" target="_blank">📅 12:45 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Un_bu-RmaEm6-7rtP2Op6Cf9_7kNSUz-NaVH8KTGPbT48FK7Xzi_NVIGUhVbhrYYZ0kaOd0OcCuPguRbIskOZBT6lnkWwQjapn9Bto_IDF2XIdH7gaB_Y7hBNAQrcbvgYjX0Mls3UjNfzhpWylSKs9xuubCCBgcbybQJlw1WA4qVbFWE0fjZniLMhF-rcCvztabZwBqzOHGP31VUHzRmIJNhu8SKHSjzU-MYZ3xSjN8h1h7hTdStxY56gYNxOQJJIjqE6u12MXUfHHsIi_fLUNGNgDVTgQS7ZLXVup42zjdlzb7Wy03JF-1VMB_p2SxgrM3BLI_N1pN2vDPy_NkL0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706d335e17.mp4?token=Un_bu-RmaEm6-7rtP2Op6Cf9_7kNSUz-NaVH8KTGPbT48FK7Xzi_NVIGUhVbhrYYZ0kaOd0OcCuPguRbIskOZBT6lnkWwQjapn9Bto_IDF2XIdH7gaB_Y7hBNAQrcbvgYjX0Mls3UjNfzhpWylSKs9xuubCCBgcbybQJlw1WA4qVbFWE0fjZniLMhF-rcCvztabZwBqzOHGP31VUHzRmIJNhu8SKHSjzU-MYZ3xSjN8h1h7hTdStxY56gYNxOQJJIjqE6u12MXUfHHsIi_fLUNGNgDVTgQS7ZLXVup42zjdlzb7Wy03JF-1VMB_p2SxgrM3BLI_N1pN2vDPy_NkL0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
آتش‌سوزی گسترده در پالایشگاه اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67028" target="_blank">📅 12:15 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
پزشکیان:
بر اساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع در قطر، آزاد و به کشور بازگردانده خواهد شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67027" target="_blank">📅 11:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67026">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Z11XmrGXuqXYnpP-1C-DI7gefGU4eOUBqUcGYeRGjyb_WqCPCTLZnHKJN_oF__THbYnTTJIpnO_msZMtAroEnnXpySfhXoS0wHCq7jfWAkBKDAD-R_kQZlAPGV4JypMFFCRhIPQ5tmP53M87NtFEQuAtp_RV5Xk63bDpgVY-fRaM_5u6IsbvuT6uYYr5taKF7mqxMTIhc-9DmUfQ1XKse6Auf51iiWFgLDCH4_LH847s7tNMV76YyyPnuggvi3nH9oQOtdhyqdeXOSxpuLYICWCs626rDjaQMXBfwg8MdvDjaU-a3QQeFvQQpfl4p9BsJ-PNJINfhkFrGIk0zcv1Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23c44657f9.mp4?token=Z11XmrGXuqXYnpP-1C-DI7gefGU4eOUBqUcGYeRGjyb_WqCPCTLZnHKJN_oF__THbYnTTJIpnO_msZMtAroEnnXpySfhXoS0wHCq7jfWAkBKDAD-R_kQZlAPGV4JypMFFCRhIPQ5tmP53M87NtFEQuAtp_RV5Xk63bDpgVY-fRaM_5u6IsbvuT6uYYr5taKF7mqxMTIhc-9DmUfQ1XKse6Auf51iiWFgLDCH4_LH847s7tNMV76YyyPnuggvi3nH9oQOtdhyqdeXOSxpuLYICWCs626rDjaQMXBfwg8MdvDjaU-a3QQeFvQQpfl4p9BsJ-PNJINfhkFrGIk0zcv1Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حملات سنگین به جنوب کشور در جنگ اخیر
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67026" target="_blank">📅 11:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67025">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">این کلیپ داره مثل بمب وایرال میشه، الجزایر گل سوم رو زده اتریشیا دعوا کردن که چرا طبق توافق پیش نرفتین‌...اونوقت بازیکن الجزایر اینجور با دست نشون داده که مساوی میشه نگران نباشید و ارومشون کرده  @sammfoott | پروکسی متصل</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67025" target="_blank">📅 11:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67024">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=PJRbhDwq8OSOzac7IOn2qMUZqSDIiv-owU8lI0ElVaqnw6f9KfHnkb3kefTRn_a26uYph9MRmxO6USQDSE1PsItvoqQSCvOZKbCia08Butdc_wAqtFnM6pzeZaVHxkQWL_7rB2HBx7m0qZEirf34YQjMmUyna4peihO0g8kVo9Bw7iLN-jKEi65xZZopxQE1D82fZQLkhKSOAAtrKqA4_O5bMrl2VySTKkP3Y7H6XEtcIiD0_eDhqZQH_2ZbltfktFv_kspnGQYtJ5I931QdlCD4TNRaoFQE9ntfdCwZtE30Es5Eb45oqNeqd-LNYddAowN6GL-x0kirEkFhY3nhaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1a1a05c8c.mp4?token=PJRbhDwq8OSOzac7IOn2qMUZqSDIiv-owU8lI0ElVaqnw6f9KfHnkb3kefTRn_a26uYph9MRmxO6USQDSE1PsItvoqQSCvOZKbCia08Butdc_wAqtFnM6pzeZaVHxkQWL_7rB2HBx7m0qZEirf34YQjMmUyna4peihO0g8kVo9Bw7iLN-jKEi65xZZopxQE1D82fZQLkhKSOAAtrKqA4_O5bMrl2VySTKkP3Y7H6XEtcIiD0_eDhqZQH_2ZbltfktFv_kspnGQYtJ5I931QdlCD4TNRaoFQE9ntfdCwZtE30Es5Eb45oqNeqd-LNYddAowN6GL-x0kirEkFhY3nhaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/67024" target="_blank">📅 10:30 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67023">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91138929a8.mp4?token=BdQHgsYzUqRmtuBC3unwBpkVSkol63iIIqoUW-ygoa1ipo1pZmrQcEXcs9l2bNqprERY2KuiwzxZflwONAJT6ayT2P15XDpyDyK4l0zNcaclMLvlNCUPzHO61BUgvRY7-SBrc16wLRM7IvGNrAMbMXLMZZhduHTaZszelsjrpcNU2HVlielLhIB7Fxc1DVxz5i-tjbirAIYIPfOaTIIG5eIswzITybMs_NTNvexDLGpgdx7iHeehIyKBeqLLYYd3UaXlqK2i67BmqHdq8ru0lWMI9VE8FGpcm56aiuokI7AgGiQmEcjei5UjfiIa7mQlEbhoUALe_5oTI5Key8T_dYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91138929a8.mp4?token=BdQHgsYzUqRmtuBC3unwBpkVSkol63iIIqoUW-ygoa1ipo1pZmrQcEXcs9l2bNqprERY2KuiwzxZflwONAJT6ayT2P15XDpyDyK4l0zNcaclMLvlNCUPzHO61BUgvRY7-SBrc16wLRM7IvGNrAMbMXLMZZhduHTaZszelsjrpcNU2HVlielLhIB7Fxc1DVxz5i-tjbirAIYIPfOaTIIG5eIswzITybMs_NTNvexDLGpgdx7iHeehIyKBeqLLYYd3UaXlqK2i67BmqHdq8ru0lWMI9VE8FGpcm56aiuokI7AgGiQmEcjei5UjfiIa7mQlEbhoUALe_5oTI5Key8T_dYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
🇮🇱
بنیامین نتانیاهو، و یسرائیل کاتس، وزیر دفاع اسرائیل با انتشار بیانیه‌ای مشترک از کشف و انهدام یک شبکه زیرزمینی در منطقه «مجدل زون» واقع در جنوب لبنان خبر دادند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67023" target="_blank">📅 10:01 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67022">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FS-XQBvAwJaOiP1EPEUSqfRmKdIG9UKVXD33I3jGggxfyKjvtsd6D5uePlWR06YsEdTURDbE6Lx6bWAmHjw9BWbDyVa3lswYx_Qr6Fz6R6d7qfnposJMLb4rOBFr2peAdr4tAvIkf1eQaJHWzLONxIBxC_PMqr6UzCbEyxjcENloqKAnn0Epnj3cmxZFmiDOk4bqeg4QhFlZJ9uN-sLVTV9KPBFs5cajeOS1kmtVI-_PEvgFzj-UYxdq8yoHZucxrQvLFVhJNoQUjZ90LRiWrQrKPhzXMgGtZrVlRFFI5oi92IczDHxUVnumbQDLPsmLWAnAd2fnGTzK09qhRhvF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شاهزاده رضا پهلوی:
🔴
‏از ۴ تا ۹ ژوئیه (١٣ تا ١٨ تیر)، هم‌زمان با برنامه‌های تبلیغاتی و فریبکارانه رژیم برای دفن بقایای جنایاتکار اعظم، علی خامنه‌ای، و در ششمین ماه خیزش ملی شجاعانه ۱۸ و ۱۹ دی، ایرانیان مهین‌پرست و آزادیخواه در قالب هفته جهانی اقدام برای آزادی ایران، به خیابان‌های سراسر جهان می‌آیند، تا واقعیت ایران را به گوش جهانیان برسانند، و هم‌زمان یاد جاویدنامان انقلاب شیروخورشید ایران را در ششمین ماه کشتارشان گرامی بدارند.
🔴
این کارزار ملی با گردهمایی‌های روز ۴ ژوئیه (۱۳ تیر) در برابر سفارتخانه‌های ایالات متحده در پایتخت‌های جهان آغاز خواهد شد.
🔴
پیام ما به ملت و دولت آمریکا در سالروز استقلال این کشور مشخص است: با تروریست‌ها معامله نکنید! مردم ایران را انتخاب کنید.
🔴
۲۵۰ سال پیش، آمریکا آزادی را برگزید. امروز نیز مردم ایران برای آزادی مبارزه می‌کنند.
🔴
معامله با رژیم جنایتکار جمهوری اسلامی در تضاد با آرمان‌ها و ارزش‌های ایالات متحده و جهان آزاد است.
🔴
هم‌میهنان در داخل کشور نیز می‌توانند با حفظ امنیت و پنهان نگه داشتن هویت خود، از طریق ضبط ویدئو بر مزار جاویدنامان، دیوارنویسی و دیگر روش‌های خلاقانه، پیام‌های مشابهی را خطاب به ملت و دولت آمریکا منتشر کنند.
🔴
برنامه‌های دیگر هفته جهانی اقدام برای آزادی ایران به مرور به اطلاع خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67022" target="_blank">📅 09:34 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67021">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">‼️
آتش زدن متن تفاهم‌نامه توسط یک مداح تندرو
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67021" target="_blank">📅 09:00 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67020">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67020" target="_blank">📅 04:21 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67018">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/udg5okIUOJ6DEogXYCWTLT8BdTZKGomUR7zY_m6MzBvTrLbyyFx7DJFQJmrooMX80uuLTvL_RQHjVX-_usSKReBvbrHawT3Dty8mK3pdAFYqDAbVbIgtkJbIsURaJ46TGSmSqYC5-Fz4KlglUHx-Ejz6AzufaWDz8LxByRGqn6qrJU69cQzQIXfs-pm6BAJGD2nfVyZX65-6udQUhqlKLlB9pZga5ypa1dyhvgxb2L0pczEdPIKqHWiGpnXKEJbCOZ-bNJ7H3Y_lxFVF-mWZbr630GiBpr8b_1ny_GozidypQhzsNiC0AE2K_d-mHyzlpNukfV36D5IT3C8ZkfP8HA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67018" target="_blank">📅 02:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67017">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=SA_z1VmFAwlbbAwWMZiTq2mrbnGsadeE1Oz3zs6R8tR_MPkY3fQt73GuPI_YGFSb38wq8dXTwSudjzWtGdVDyJrJYn4Oog5u7RU1uWHytnkh9M0JdSAugccjnThoOsGN9m8TONrsWPRPfEtQtCeOU4_gA-CeMzd7RNAoJX8rf5T61uIBDeUT_LFPGHXw5lTpRBlxlOgFard8fRyGRuyN9q6HOS4NQD14uoGHK3V0BnGMfkR8UUd3HtS20QJsJGcLzbmwAytRGx-wO0aQ4qD36oP0uoJXwda3x9hhsUpHLxyAGCJIzl8InwnPcF5-y9HVC_EC1NMnbC0s5hPxSqJe3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b55b34728.mp4?token=SA_z1VmFAwlbbAwWMZiTq2mrbnGsadeE1Oz3zs6R8tR_MPkY3fQt73GuPI_YGFSb38wq8dXTwSudjzWtGdVDyJrJYn4Oog5u7RU1uWHytnkh9M0JdSAugccjnThoOsGN9m8TONrsWPRPfEtQtCeOU4_gA-CeMzd7RNAoJX8rf5T61uIBDeUT_LFPGHXw5lTpRBlxlOgFard8fRyGRuyN9q6HOS4NQD14uoGHK3V0BnGMfkR8UUd3HtS20QJsJGcLzbmwAytRGx-wO0aQ4qD36oP0uoJXwda3x9hhsUpHLxyAGCJIzl8InwnPcF5-y9HVC_EC1NMnbC0s5hPxSqJe3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
حملات هوایی پاکستان به ۳ نقطه در خاک افغانستان
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67017" target="_blank">📅 01:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67016">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=afSOrrhtmmf53YxQrqshoi41lWpBB7SyHtHC5kp5J6UELrqDIERyWULI2whuwgOJldffoaXvbfI0mp5dge8GbRWhSkb41iPjc6-bBgO9w5gE1oh6mk-QOah4YdzZ6IXE5MJj9m3nc9ltVC4jV6ckRJNRLH1pUFoTOeT_dHPljuFHlaqbq909NIsj-3iM6Cczulfh6ZW9CdLOvdVJpX3PTO6RnyTQs02GieQyJ0Ex6cg1O6X-e54qFBS_e8uL-bOUfDBm5Y6kwOjw78JC6S7EcUN9Wlv9Nk0FG6h6C3yGnqggQWkLuSg7Av1qRNPO4TkYszrZToz4DkuwjhtSRRP-WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18d3b4a51.mp4?token=afSOrrhtmmf53YxQrqshoi41lWpBB7SyHtHC5kp5J6UELrqDIERyWULI2whuwgOJldffoaXvbfI0mp5dge8GbRWhSkb41iPjc6-bBgO9w5gE1oh6mk-QOah4YdzZ6IXE5MJj9m3nc9ltVC4jV6ckRJNRLH1pUFoTOeT_dHPljuFHlaqbq909NIsj-3iM6Cczulfh6ZW9CdLOvdVJpX3PTO6RnyTQs02GieQyJ0Ex6cg1O6X-e54qFBS_e8uL-bOUfDBm5Y6kwOjw78JC6S7EcUN9Wlv9Nk0FG6h6C3yGnqggQWkLuSg7Av1qRNPO4TkYszrZToz4DkuwjhtSRRP-WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
فعالیت ۲۴ساعته و سنگین ترابری هوایی آمریکا طی ۷ روز اخیر در منطقه
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67016" target="_blank">📅 00:55 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67015">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxhKmbJfEBNSBYl26R5h5TPzn92p0SK4L-cwyZ6UzTGyO3NFYLCCx1eWzn9fFVN28JHZXb3UfQq0JdKtUapJpxjKixcQOVcsVzhWp-3frmzUHHAmkCV1K7A07BzVBdH45ZuYzYvKs80G3lcdMe8b6e0JaOnqRaUz8occFTwl4IdVcErrHqXquDXRfV24dEk_7frC5A-aVEnbUvg2p5A5JynOtjTOKBzLbUjjWCDtvpqJBzr-ETKcZHthY4e4zYN_3HP5l0VZSQNuffzaGW1U2-eQC7Uaom18G1IK0ii8S0dWVNicWOw02nBJa072lus825mlMcMK3v74VN6zP_LThA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آکسیوس:
به گفته یک مقام ارشد آمریکایی، ایالات متحده و ایران توافق کردند که حمله به یکدیگر را متوقف کنند، در حالی که دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر برای حل اختلاف خود بر سر تنگه هرمز دیدار کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/news_hut/67015" target="_blank">📅 00:18 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67014">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=LrTOb_50Hh0c8WEYgrQIqWfgiMqssYKTfVlz5lXmegoljdDHcKSN7gVAtLbU6V87WGYM04qYFhKU7stl73zBcelMaT034NlxneuKaYbXKiPCOK2MEdHncP1TiFYn7CmhcCw-EL5LYCwYESZ-uFehme8j0LwjXAjoVBSJp_8Vg7GpKgwY8L53qanNpNrrHzJvTXLcRjQkwDhzeOUCeI_K7Ejv_Gd4xhaOn5gi5QEfALy4wLdzmiCkfl63GEAuBU3z-VyMdXUg-BEVVRKnpopMjsJOetRKvFVitAMqFZEmD0Odg-I2NiHZU47osivTrzDvSSdAx3WursjD-rJY-38FGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e66d65d2e0.mp4?token=LrTOb_50Hh0c8WEYgrQIqWfgiMqssYKTfVlz5lXmegoljdDHcKSN7gVAtLbU6V87WGYM04qYFhKU7stl73zBcelMaT034NlxneuKaYbXKiPCOK2MEdHncP1TiFYn7CmhcCw-EL5LYCwYESZ-uFehme8j0LwjXAjoVBSJp_8Vg7GpKgwY8L53qanNpNrrHzJvTXLcRjQkwDhzeOUCeI_K7Ejv_Gd4xhaOn5gi5QEfALy4wLdzmiCkfl63GEAuBU3z-VyMdXUg-BEVVRKnpopMjsJOetRKvFVitAMqFZEmD0Odg-I2NiHZU47osivTrzDvSSdAx3WursjD-rJY-38FGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
دختره رفته پیش دکتر، یه تیکه نبات تو واژنش گیر کرده! دکتره میگه این چیه؟؟
میگه ما یه رسمی داریم، بعدِ عقد نبات میذاریم داخل واژن‌مون، بعدش میندازیم تو چایی که داماد بخوره. چون با اینکار زندگی شیرین میشه!
😢
😢
@News_Hut</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/news_hut/67014" target="_blank">📅 00:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67013">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=ZIE5RIodiyp7g97DQMY-2L-byw7dKyTSrwbGuNffuzjxD_A35EZwr4tpBQSEWB-2U5R2d7BsUpfJsmg0cvrmS5ak6Wh8a2t7pVErucdooL9WP0N2SJ5VHVEMX0X2IQdJrYJzDTAIgwSMFGyCqeL-z2zGzFI3AffDPcNql8wLkIPsJ9tlv7n4KKhmLfy8h8cwXBeIQfLIHcfVomMdxC2Fq1iVxA945JKBjIicG3D0w5Fg1OzaX9PfEG3aAAWQ3s08kZO2UXtoFiF4QvdhJrlzzzNEMOshTMilKa_ini4RMUVZxC81zFCEDjSpAfjFHs7onPG45XWvw5FUsdiTDzXsNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de8a95a6c6.mp4?token=ZIE5RIodiyp7g97DQMY-2L-byw7dKyTSrwbGuNffuzjxD_A35EZwr4tpBQSEWB-2U5R2d7BsUpfJsmg0cvrmS5ak6Wh8a2t7pVErucdooL9WP0N2SJ5VHVEMX0X2IQdJrYJzDTAIgwSMFGyCqeL-z2zGzFI3AffDPcNql8wLkIPsJ9tlv7n4KKhmLfy8h8cwXBeIQfLIHcfVomMdxC2Fq1iVxA945JKBjIicG3D0w5Fg1OzaX9PfEG3aAAWQ3s08kZO2UXtoFiF4QvdhJrlzzzNEMOshTMilKa_ini4RMUVZxC81zFCEDjSpAfjFHs7onPG45XWvw5FUsdiTDzXsNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله آخرالزمانی اوکراین به پالایشگاه نفت اسلاویانسک روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67013" target="_blank">📅 23:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67012">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar0wrLnvExWNVFVY4Fhm7u_w7pdQLlRCQHaJxq1UGwFZYUtFafLX_m-wnXtLNuBFGUlulim9nyAAsgoW07nox35d5pz2clREmersFtgPtJkLH_nd9JtD6Sbv_bpDMdCFgU0FhrWQKd7PViiEErG8g2Z25_3QxO2ObAT8TMewa_bSsqwlhHMiL9CzE4KGvaJJz7mtCKCPmv1bRfW7-SkLd_bL7V_yFp9pP2uLcPCHA6Op1rzPE52f0NbF7heqKq1iTTJgYnbW8yM5FdwgidXcYtEoi9f7o7Qmkr5iizCu_SS1U-1urYKYbctDxBMSZZmxXrW_hKx6sMhATxFHt57y-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
اسرائیل به شهرک‌های مفدون و نبطیه الفوقاء در جنوب لبنان حمله کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/news_hut/67012" target="_blank">📅 23:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67011">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MI6bdr3v1ZNsHOaU_85nl5NctZsJcXRfCsemKHKevmj-RtI2YimrGhK137_yJXCaN-slAh3KSDNYhzy1saJ1D1JjH1SN8KhpL5XcdrjM4ohsNyCQ22JDjjYAnu-aClUlNz-WLCjv77rxQ1pz_g9HIA1ofXEw7sAG_lwwggH2-mUOwdYvEydVlEI9quPHmARHrgCr_uhXWHvxTY2lcrZNEX2U_WTULjIBbR4ef9jLTRFcnH2Rl4YteY3b_6X18R7WvtARITAZxyVIpiI0sbgKfnEH30nBx-MvRAvVwaZiQ237DHoNNKuWgC9UcRh1axet7aK73DM_fEAr7MRQUrgeeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/news_hut/67011" target="_blank">📅 22:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67009">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qfTTXFeJQq-jIPxf4A1ulfgbOFgh0PdsObFcytUk_C0ujm_yzzelHbBnVDWhnAF0Rn2wdWTHKgq3RcNpZOHa3RPTQAlorpiJtsXlKyMcVK6RsPtUsVwrIqLG46-poUSEqZ1ERqA6vTuK5nMcHdYQb82bQQsSTRoBt9adYF1yR-LXWKUZu5ExpkTYRJjv80HdTEdfoL40ER8sHT_Feu1jlgbz4Ar13rJJ24hz4wa1ZoV8EQB7BMo9bWVy4q9-Pj9-6Jr6ww-vUO73_3ADgqEDX4fiNQyEpZhtYTKXEYjRSnBmGxfMCcUQSli5xoY7MHfMtjT_nL7ih5BLlTxchk7nIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=cqnfebo7whExDxvfPCEfUME843fF8SPiGPZWReZC0iialMswprawxnxuTPAj6SkRtMOogvbzIhUJmh0i9eIMLipXTDk6BcPbAYf3eHyow4MdDTwXgCi05HUfOpPkTtC0OQ6VJtxP1NRRuFFdkxDdBnKXCGg_YswS4qIpLRSXnCAgJYdNsno_8-xTlkjfpDhL1-jDMWnCYISR1KAWZDPx-XW9X__KTJvoti8m_uBam-LTO0lIl9qB_9LH2B2YXZ5eFsZOzyW10pw9kG58yqeG1fNWerMRXBIDHAk_cdu71SOy9XZDeRyNsMHZCuyDl9IvYLXdr7a7Eap7D8804u50rg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d35ea35af.mp4?token=cqnfebo7whExDxvfPCEfUME843fF8SPiGPZWReZC0iialMswprawxnxuTPAj6SkRtMOogvbzIhUJmh0i9eIMLipXTDk6BcPbAYf3eHyow4MdDTwXgCi05HUfOpPkTtC0OQ6VJtxP1NRRuFFdkxDdBnKXCGg_YswS4qIpLRSXnCAgJYdNsno_8-xTlkjfpDhL1-jDMWnCYISR1KAWZDPx-XW9X__KTJvoti8m_uBam-LTO0lIl9qB_9LH2B2YXZ5eFsZOzyW10pw9kG58yqeG1fNWerMRXBIDHAk_cdu71SOy9XZDeRyNsMHZCuyDl9IvYLXdr7a7Eap7D8804u50rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کاری ندارم که حیوون خونگی این آقا مار کبراست! مشتی چطوری مار کبرارو قانع کردی چایی بخوره؟!
@News_Hut</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/news_hut/67009" target="_blank">📅 22:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67008">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🚨
🇺🇸
یک مقام امریکایی:
هر شب رژیم ایران حداقل ۶ پهپاد را به سمت کشتی‌ها در تنگه هرمز شلیک می‌کند که برخی از آنها توسط ارتش ایالات متحده رهگیری می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67008" target="_blank">📅 21:11 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67007">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hYf0hRBEjEclKnoJ55GGO66_NfQcphYz5NrMsIj0p74I9GRzelwS0e21mfUNA6_u8x2AOK4w885HNGHEX_miEr5qx2aLqzGsfg98Tn2ZNbTsggp4zD-323rX4nc2_ux-f1UQazr_myYAx_6KSApYKVrtGY3xMoNhCVaOgqqc0HiyzLUEzRmPuVBdQChDgLhwQyulZVmiG2aItbXWqGemXk75tDFSYTLw6CjKxrR_k_nKw0unXSoGQZO5UFp3pMZmkj5Rij4fnPF5NiBAQSoM_O5_I-sHvnuD2ajEXIibCu1ykUnVcaRfTu4nfayhEo3sTVMbOVIAkIvcZQmma7hzoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو درباره ترکیه:
تقریباً هیچ روزی نمی‌گذرد که اردوغان خواستار نابودی دولت اسرائیل نشود.
ما این سخنان را بسیار جدی می‌گیریم، زیرا اگر یک چیز را از تاریخ مردم خود آموخته باشیم این است که وقتی کسی می‌گوید قصد نابودی شما را دارد، باید او را جدی گرفت.
ما این اظهارات را جدی می‌گیریم و آن‌ها را به اطلاع دوستان آمریکایی خود نیز خواهیم رساند. ما آن‌ها را نادیده نمی‌گیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/news_hut/67007" target="_blank">📅 20:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67006">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fVd_9dmmzk-6us9IiAbDr0RuPJlZhmPtsTGuRNTlyOv9UH6CFKH9L8-NHa53OYIcB-Sv4WeTjLAvVw5amypps3WHKZsMUX3O7viazY2LZ7c5BR17REo4ERC7CvPyXUxWPaqGR0W6r8St-By3pwwmRDT2h_qxUa9CbCfHC86oYV9CnK4CPhAgDBecp_n1XB4Sy_PJugVAtyKrDaZAJbrgZ_Fl2B_Yfb37-vfFo7kjATbFfYE8nqMqVlI5k0J3nw-xY0tncA2txcYGc_iVwaJpvVpcsl_G8kuOcJ__7ydbnsF6Un1xuTNVeawMjkHPDtwEbOfNsIBBPezypzy5xpjQXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:
آتش بس ایران و آمریکا در شکننده ترین حالت خودش. چون مذاکرات به شدت ضعیف شده و برگزاری دوربعدی بعید بنظر میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/news_hut/67006" target="_blank">📅 20:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67005">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
وال استریت ژورنال به نقل از منابع:
مذاکرات برنامه‌ریزی شده برای این هفته بین واشنگتن و تهران در سوئیس به دلیل تشدید درگیری‌ها متوقف شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67005" target="_blank">📅 20:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67004">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=rHPOwbk8ig9vtm-vNBPFIX-XHaDSDoqY6Ds_0DNBf0aTalZFX-A8Uw8UbRtKa3R03yf8cFQy6RIgoulPVhauF2YlK1FlyKlwOQPOS8xfet-32aSZSSKe-tbijt40R5kDPzFOfqn0z8fh4zbqa1VX-sAIeizweqNVA7bTaKkw48hv_3G6OyxMUBsIu7IHpQBkIhzwh5X9xhyZaJk5-h5AzqtgUvAcJyC7wus4Pj17Lc8C2d_gVpLW-VDaFFW9ILgiZZTg235RdSTOoNteeh64OwO77XV0Oi9uu29o4zbYHj0jbHkQY5EK6bqGFiQ2I2jFwhzKh-INu1e3N9Od1OT02Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b64ee519f2.mp4?token=rHPOwbk8ig9vtm-vNBPFIX-XHaDSDoqY6Ds_0DNBf0aTalZFX-A8Uw8UbRtKa3R03yf8cFQy6RIgoulPVhauF2YlK1FlyKlwOQPOS8xfet-32aSZSSKe-tbijt40R5kDPzFOfqn0z8fh4zbqa1VX-sAIeizweqNVA7bTaKkw48hv_3G6OyxMUBsIu7IHpQBkIhzwh5X9xhyZaJk5-h5AzqtgUvAcJyC7wus4Pj17Lc8C2d_gVpLW-VDaFFW9ILgiZZTg235RdSTOoNteeh64OwO77XV0Oi9uu29o4zbYHj0jbHkQY5EK6bqGFiQ2I2jFwhzKh-INu1e3N9Od1OT02Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئو سپاه از حمله موشکی دیشب
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/67004" target="_blank">📅 19:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67003">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=EKvF1LVgjBuHe6DzRxx-gGziXc4RZBl-95UfXNd2N5amE6krpvFW1XwQExifstrCf1e2AmDIH7Z1yeGqxzcBwK4kuxEkxtp47myj_qgFxmrHaCnNlb9yaI9v1a-XS9_U5L0Lu6WHTNVSTsM7QiOg4n5mKdnEfoaN6h7JA6ZY1B3SnetCIYzAKWFCcBqn_lrk53wq3-6mHBiuBeguTuYRX9JHhsNw9yUu0ZJIAWXUX3NxfZz7QBbm9x452oCfM2954lZQO3ME2iDRrAd0_EkeMnuN_29zLsA7TqK4DSbfyupfZQYi3LzS0MLZfxLitLLhx041icLIiiY-E1Bl62btUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72a36c0ade.mp4?token=EKvF1LVgjBuHe6DzRxx-gGziXc4RZBl-95UfXNd2N5amE6krpvFW1XwQExifstrCf1e2AmDIH7Z1yeGqxzcBwK4kuxEkxtp47myj_qgFxmrHaCnNlb9yaI9v1a-XS9_U5L0Lu6WHTNVSTsM7QiOg4n5mKdnEfoaN6h7JA6ZY1B3SnetCIYzAKWFCcBqn_lrk53wq3-6mHBiuBeguTuYRX9JHhsNw9yUu0ZJIAWXUX3NxfZz7QBbm9x452oCfM2954lZQO3ME2iDRrAd0_EkeMnuN_29zLsA7TqK4DSbfyupfZQYi3LzS0MLZfxLitLLhx041icLIiiY-E1Bl62btUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سنتکام:
ملوانان آمریکایی سوار بر ناو هواپیمابر یواس‌اس جورج اچ. دبلیو. بوش در حال انجام عملیات پروازی در حین عبور از دریای عرب هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/news_hut/67003" target="_blank">📅 19:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67002">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=O1gNK0pkX_e0-7HVtjrzxFTHjCjzi7G4meTXBeTJh1edn6fnQPfs-bm38zJfRa7WSxYmcJ737HRYrNxViMBhj-bWEINuY4URgrY83qwiNw9splvI6i75YADt1oYbueuDNm1azs46dIrlAKaagUSpPIWrygx5-2mBHL2FVRjHB7B-VPfR0I-BzlUmrpD9NQRBTptuhJmMrJpYalCzEuLiB9taymlRt3r-68hF2cxlLZxIUdHwKqQp0ESu-qbMPdWzhPFnCjdljoLt4hLXF1g5jzIL0IbE3sO-zLkmuBPl9Enxa3mOR_s0lvJfNSQ9uFDqlcj2plr5iDHbKjBJLOShag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dcd7fa042.mp4?token=O1gNK0pkX_e0-7HVtjrzxFTHjCjzi7G4meTXBeTJh1edn6fnQPfs-bm38zJfRa7WSxYmcJ737HRYrNxViMBhj-bWEINuY4URgrY83qwiNw9splvI6i75YADt1oYbueuDNm1azs46dIrlAKaagUSpPIWrygx5-2mBHL2FVRjHB7B-VPfR0I-BzlUmrpD9NQRBTptuhJmMrJpYalCzEuLiB9taymlRt3r-68hF2cxlLZxIUdHwKqQp0ESu-qbMPdWzhPFnCjdljoLt4hLXF1g5jzIL0IbE3sO-zLkmuBPl9Enxa3mOR_s0lvJfNSQ9uFDqlcj2plr5iDHbKjBJLOShag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67002" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67001">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=RqYu-1pvP_6J0tEU3OuPfBZbWKPZ8RXszn3M9jG5H0qUhubEGKa1iKWrFEraYyGE6ydFCOCEjF7LdZemdDsW-t-_ArEfw9fEXRzLi15rsMtq0AwyRzUtaqe0ld15zUjqMKqI2J72136qmDzTa9g7OyIYFZAZeDqJ2O7G4U1wlRwdibBANSDEtNv5cs8Y9TsWd87UFP1M7xZtZ55YAr-2B4NzS0wj-5sLk1au_aEHMFnRFp5QzXVTtJ9iA-4u6wJdbS4Rv1hpKXx0LQ6EKT_QQxPVLrVrXHFajtLa_KIuEBdYbOENBjnR8mgSxT-iDh230b-iJ5w9ZVJdDq5jLto_hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6bc1a83a1.mp4?token=RqYu-1pvP_6J0tEU3OuPfBZbWKPZ8RXszn3M9jG5H0qUhubEGKa1iKWrFEraYyGE6ydFCOCEjF7LdZemdDsW-t-_ArEfw9fEXRzLi15rsMtq0AwyRzUtaqe0ld15zUjqMKqI2J72136qmDzTa9g7OyIYFZAZeDqJ2O7G4U1wlRwdibBANSDEtNv5cs8Y9TsWd87UFP1M7xZtZ55YAr-2B4NzS0wj-5sLk1au_aEHMFnRFp5QzXVTtJ9iA-4u6wJdbS4Rv1hpKXx0LQ6EKT_QQxPVLrVrXHFajtLa_KIuEBdYbOENBjnR8mgSxT-iDh230b-iJ5w9ZVJdDq5jLto_hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67001" target="_blank">📅 18:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67000">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eB8utvjdDvhwYzPu-gYlhULNrWhJO5Hkg9ydv3RHDX2AaC2pnVORVyB9n4PofmlybVHt3XsV2W1H7MoJttuycbf0VHIlOv3_b6boVszOX9OjTnzlsMJIjzGmQTbC74vRbuNXXaAu1u-WIVxaHfvVfMd-j_7_SptiUv09sA7fKQQezIUyOBT9Bs9PLNVxTJShP9TKNl2dBJlVnvfe0uvwLfZKYvWsdIInNfvy5OjzXDQZexNMsd5-xhxwDen2KIPQmyuCmGBHqaMqDjk-VbT2lFkccUeImpHmNRGcLvOeTKbADGtjFKdAjZsD5yfdvB5TE1ARTbrd3o9qPGVwpWr8pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سخنگوی کمیسیون امنیت ملی مجلس:
پول‌های مسدودشده مردم در بانک‌های داخلی را آزاد کنید، خارجی پیشکش.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67000" target="_blank">📅 17:34 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66999">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=hsL9o7hDvebjwRhttEpZRMV0xk-D9guskBbAG7vGYJLfOtMp1loDe2DyWHkTi_S9kvpDQS23IM_ScZbxKGePkiCGLAJZMfYWM2il6gxLtd_wxPugOCg194LPW79rypO5ga93recygD7aRdX81iHUaNdhF7cLN8r4AyVH5ji-b1TP59L50Zh5w6z5VQ0wydhhRRvFvWi2fb8_ksgCp2jMpE9QqnC-XBwKtmecQ8pQH8gnTDWRCKk0eBSJlFeBvBbe9_ZZV-s8uFFI42jaRV-Pl4NkvmG-M-GGtyvtRJRPy7xnCAY7soTCFH-JLngNb1kayI0qdrL895jemDlbhDS_oQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c972b464a.mp4?token=hsL9o7hDvebjwRhttEpZRMV0xk-D9guskBbAG7vGYJLfOtMp1loDe2DyWHkTi_S9kvpDQS23IM_ScZbxKGePkiCGLAJZMfYWM2il6gxLtd_wxPugOCg194LPW79rypO5ga93recygD7aRdX81iHUaNdhF7cLN8r4AyVH5ji-b1TP59L50Zh5w6z5VQ0wydhhRRvFvWi2fb8_ksgCp2jMpE9QqnC-XBwKtmecQ8pQH8gnTDWRCKk0eBSJlFeBvBbe9_ZZV-s8uFFI42jaRV-Pl4NkvmG-M-GGtyvtRJRPy7xnCAY7soTCFH-JLngNb1kayI0qdrL895jemDlbhDS_oQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عراقچی:«بر اساس تفاهم‌نامه، تنگه هرمز ظرف ۳۰ روز و تحت سازوکار مدیریتی مورد تصویب ایران، پس از رفع موانع از سوی جمهوری اسلامی ایران، به ظرفیت عملیاتی پیش از جنگ بازخواهد گشت.
🔴
این ترتیبات هم‌اکنون در حال اجراست و مسئولیت کامل آن صرفاً بر عهده جمهوری اسلامی ایران است. هیچ نهاد یا کشور دیگری در این زمینه مسئولیتی ندارد.
🔴
مطابق تفاهم‌نامه امضاشده میان ایران و ایالات متحده، هرگونه مداخله در این موضوع یا هرگونه تلاش برای ایجاد سازوکارهای جدید یا جداگانه، غیر از ترتیباتی که اکنون از سوی جمهوری اسلامی ایران در حال اجراست، تنها موجب پیچیده‌تر شدن وضعیت، به تأخیر افتادن بازگشایی تنگه هرمز و افزایش تنش‌ها خواهد شد.
🔴
همان‌گونه که طی دو شب گذشته شاهد بودیم، رخدادهای تنگه هرمز از پیش به افزایش تنش‌ها و رویارویی‌ها دامن زده است.
🔴
از همه طرف‌ها می‌خواهم در مدیریت تنگه هرمز یا در ترتیباتی که جمهوری اسلامی ایران برای بازگشایی آن در حال اجرا دارد، مداخله نکنند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66999" target="_blank">📅 17:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66998">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=VA6rqqql-e1U8V1mR8J0L3s6mtpAgxEmbwede-1XD2nv7DFCJJwLpaEumrH1nzW9VgTT23VhNKTzM-qCBGb725ybKBCEIv6pKiy5VwUboVkG9hNE_Ar8uQj4s8G90A9BEfQT2v3m1mue7igVXFljmNMJlTNf2SVHyY0Q9vaSWmmCL1vidfuzuoQUKG8xgvSU2FPR3Yh1Rua80-T15J6175Luiy6Pywkil4DEGYJ9phcajFBa36T26R_urTdx9oOF-8xLqqZz9c9sdQgQfMxYDwZbuE9cbFlXCK4TjNN-Mo1bLtUxZn2JK_sC8dfqVa6ypifHsd2cyJHVB0Kusw838Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96542aaa83.mp4?token=VA6rqqql-e1U8V1mR8J0L3s6mtpAgxEmbwede-1XD2nv7DFCJJwLpaEumrH1nzW9VgTT23VhNKTzM-qCBGb725ybKBCEIv6pKiy5VwUboVkG9hNE_Ar8uQj4s8G90A9BEfQT2v3m1mue7igVXFljmNMJlTNf2SVHyY0Q9vaSWmmCL1vidfuzuoQUKG8xgvSU2FPR3Yh1Rua80-T15J6175Luiy6Pywkil4DEGYJ9phcajFBa36T26R_urTdx9oOF-8xLqqZz9c9sdQgQfMxYDwZbuE9cbFlXCK4TjNN-Mo1bLtUxZn2JK_sC8dfqVa6ypifHsd2cyJHVB0Kusw838Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇱
نتانیاهو:
می‌خواهم به شما یادآوری کنم که در لبنان چه بود. حزب‌الله ۱۵۰٬۰۰۰ موشک و راکت داشت. و ما حدود ۹۰٪ از این انبار عظیم را از بین بردیم.
ما آنها را با بیپرها شوکه کردیم، نصرالله را از بین بردیم، فرماندهان نیروی رضوان را کشتیم.
فقط در دو هفته گذشته بیش از ۲۰۰ تروریست را کشتیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66998" target="_blank">📅 16:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66993">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ 𝐇𝐨𝐭𝐍𝐞𝐰𝐬➕]</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vIA7R3aOvnQgjdhDH0wI-cobOMDubZ3Om62o3g9jYzWtk0Rml-3rQjW3LVe71g2cjfEcjc_aTEkNH4bJVar17f5YJI9GZPjOCyu6yTyROyWILzLQ8ZeuKo3fYpKKINuE92B3NZ7XXNCDXPGJAEKySh_olbV_g3YD7h3202zNZ56dIJD4ta-BPnjcRDYUp85UiybdKqREWMKxKCd_6ctsjXXJqSPz9JjbJgLqCD04wdF7Qm1kDjigYt31VJH4GC98oMU663Nl7myRBgPuvK__7qBctJoRCKyglrs_4lilzqzikfC66tdXxn2fl7ckLabBAkD3t4lPCdOvsA5vKoSPFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kVyvRJAkRqag5prXm09VnICIs4VMTDJ6IPTgufDnPtvUkGtnUOXwmWc2Li1kCvVzOKgIGbq2kK-J6No_oNOg0ql2zJe4zkJJLfsiq36k5mF45qVkbuO7cORTtGsm5zRS4yce8p7wbJtcyrDC7K8kxtYIV2C2xECh47c0wNYs64R6mWvnzXttLAQttXaZ6U2BeiqiXx2fckTIJ1HecSCCvQgJoPlhgiga9UxXAQsHxQHRwpsHvlSnEbmkAGu1jIoBZ9ysN9y3AYEKEJ_tBSxlbmb_-KspHNPLy9D08PD1zrQCiq6wJmah22oA9h-Jw79-osiHo5z9MJd5z-1Kfc5fHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JcvWyAvIqtbJy5FH4wFSuCPHsjMzsa61tMBuCI_mUdx1Ll0DbJkCdrJMgW0NYMTbEek_8WneA4-ga568AHpGs0F-kYl186oPWwEBNA4BRJUla92Pt27PLz52W44tVUQpDYSnat6rdcSKkNWJoYkwu82w86TO2AcwGjBA1bp2vcLiwe18hkqnF-omvRX80FlNHMVDtDxsrNaQU1BVXGL6HSPM0PT9bd6B3TXffIqupa4GE7lya8mNToX6gPZLBwnQchpX01X9XcksNv-F494J56MIIIleYBjJbj0dn2cP7SAzQvd0LKlxk8YwCswjIVkCLEes1qLHI_FnMzioErTqVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=uaJeRdgw3HezX5jFSr6pEKXzV5kXSaQS5bBLmU3u4CMNkPYm6w0qQnWnudzxju-2dbU3GWA4mFBHvGjXWkcFoZimMk2F6cKW56k8eP-IEkO39-LCEeIclHSjt8bFSmWoIGcB5x6wU6m9Wxf91ObIGDIx2skKryCZU6Jj5H4y80yEIlg2y8VFl1KkGXQriQCbrYjzNEJpPbpHGhWGcRzMyFFhDdF1XfH67mqG_KwAV4dIpUggTP5By77HPQCmrgyHoCsB43hyo7CBQn3LdRSjlAiBRFejVdsSAPi_3SosAdD5IXz6qjrGE1jQncZ1PUNML_6OMTqPdXFlChRV6vKO2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2d278e2c9.mp4?token=uaJeRdgw3HezX5jFSr6pEKXzV5kXSaQS5bBLmU3u4CMNkPYm6w0qQnWnudzxju-2dbU3GWA4mFBHvGjXWkcFoZimMk2F6cKW56k8eP-IEkO39-LCEeIclHSjt8bFSmWoIGcB5x6wU6m9Wxf91ObIGDIx2skKryCZU6Jj5H4y80yEIlg2y8VFl1KkGXQriQCbrYjzNEJpPbpHGhWGcRzMyFFhDdF1XfH67mqG_KwAV4dIpUggTP5By77HPQCmrgyHoCsB43hyo7CBQn3LdRSjlAiBRFejVdsSAPi_3SosAdD5IXz6qjrGE1jQncZ1PUNML_6OMTqPdXFlChRV6vKO2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیاین یه نگاهی بندازیم ببینیم چه بلایی سر تیم به‌ظاهر ملی اومد؛ قبلش بریم سراغ مصاحبه های بازیکنان این تیم تو تجمعات شبانه حکومتی‌ها:
شجاع خلیل زاده :
حسم نسبت به رهبر شهید ؟ افتخار ایران ؛ گل اگه زدم به رهبر و شهدا تقدیم میکنم
رهبر عزیزمون شهید شد همون چیزی که خودش میخواست بهش رسید
گل بزنم به  رهبر شهیدم تقدیم میکنم و ما فوتبالیست ها همه دوستش داشتیم ، افتخار نداشتم با رهبر دیدار داشته باشم و دوستش دارم
حسین کنعانی :
حسم نسبت به سید مجید نقطه زن ؟ بزن که خوب میزنی ،حسم نسبت به رهبر ؟ بزرگی
رامین رضاییان :
شهادت رهبر انقلاب رو تسلیت میگم تو تیم ملی به عنوان سرباز برای کشورم می جنگم
اتفاقات داخل ایران { دی ماه } به خودمون ربط داره و به خارجیا ربطی نداره
علیرضا بیرانوند:
چه بهتر که تو آمریکا بازی کنیم می‌تونیم تو اون کشور برای اولین بار در تاریخ فوتبال کشورمون به دور بعد جام  جهانی صعود کنیم
روزبه چشمی :
حسم به رهبر شهید ؟ بزرگ همه مردم ایران !
سعادت دیدار با رهبر عزیزمون نداشتیم ولی بزرگ همه مردم بودن و این راهی که مردم دارن میرن ادامه راه ایشونه
و بعد از این اظهار نظر ها بریم سراغ دیدن نتایج، تو بازی اول از ضعیف ترین تیم جام یعنی نیوزیلند دوبار عقب افتادن و در نهایت با سختی یک امتیاز کسب کردند، تو بازی دوم فقط چند سانتی‌متر از باسن مهدی طارمی تو آفساید بود و گلش مقابل بلژیک مردود شد، تو بازی سوم بازم همون طارمی پنالتی رو خراب کرد و در دقیقه ۹۳ شجاع خلیل‌زاده گل زد و خوشحالی‌ای کرد که در تمام جهان سوژه شد، ولی بعد از چند ثانیه کل دنیا روی سرش خراب شد چون فقط دستش ۵ سانتی‌متر تو آفساید بود، نکته جالب اینه که شجاع گفته بود گلم رو تقدیم به رهبر جمهوری اسلامی خواهم کرد
دقت کنید برای اولین بار در تاریخ این جام جهانی ۴۸ تیمی بود و ۳۲ تیم صعود می‌کنند، یعنی در واقع به اندازه‌ی همه‌ی تیم های حاضر در جام های جهانی قبلی، این بار تیم‌ها به دور بعد صعود می‌کردند (علاوه بر تیم های اول و دوم، هشت تیم سوم هم صعود می‌کنه) و بعد از مساوی با مصر، سه شرط برای صعود تیم به‌ظاهر ملی وجود داشت:
۱.بردغنا
۲.نباختن ازبکستان
۳.مساوی نشدن بازی الجزایر و اتریش
ولی در کمال تعجب یک معجزه رخ داد، غنا نبرد، ازبکستان باخت، و در دقیقه ۹۴ بازی الجزایر، ج.ا صعود کرد و در دقیقه ۹۵ با گل اتریش، ج.ا حذف شد، این واقعا یکی از بزرگترین تحقیر های تاریخ بود
...
می‌بینم یک سری افراد با توجیه های احمقانه می‌گن اینا مجبورن و فلان، نه عزیزان دارین اشباه می‌کنید، میانگین سنی این بازیکنا بالای سی ساله و عملا فوتبالشون تموم شده و رسیدن به آخر خط، اینا فقط دنبال باج حکومتی‌ان و حکومت به عنوان حق‌السکوت بهشون مجوز واردات خودروی لوکس می‌ده که می‌تونن ۱۰۰ میلیارد ازش سود کنن، یعنی عملا یک رانت ۵۷۰ هزار دلاری هر شخص بابت حق‌السکوت دریافت می‌کنه، جالبه که تیم های بزرگ جهان مثل آلمان و اسپانیا حتی اگه تیمشون قهرمان هم بشه مبلغ کمتری رو می‌دن به بازیکنا (۴۳۰ هزار دلار)، خلاصه که جام جهانی بزرگترین رویداد برای شنیدن صدای مردم مظلومه، همونطور که تو سال ۱۹۷۸ کاراسکوسا کاپیتان آرژانتین بخاطر جنایت های حکومتش از تیم ملی استعفا داد و...
ودرآخر، از اون ضربه‌ی تیر دقیقه ی ۱۲۰ جهانبخش تو جام ملت ها، تا پنالتی‌ای که طارمی خراب، تا پنج سانتی که شجاع تو آفساید بود، از پنج سانتی که بازیکن کنگو جلو ازبکستان تو آفساید نبود، از پرچم کرنر تو بازی الجزایر، از گل دقیقه ۹۴ الجزایر تا گل دقیقه ۹۵ اتریش، هیچکدوم اتفاقی نبود و همشون کارما بود، کارمای حرفایی که نباید می‌زدین و زدین، کارمای کارایی که نباید می‌کردین و کردین، اینا همه صداهای مردم و آه‌ناله هاشون تو گوشتونه، مردمی که دلشون باهاتون صاف نیست، حالا هی بیاین بگید تبانی بود، نه تبانی نبود، اون بالاسری خواست تا شما به عنوان بی‌غیرت ترین و بی‌شرف ترین نسل تاریخ ایران با حقارت‌آمیز ترین نحوه‌ی تاریخ از جام جهانی حذف بشید :)
#hjAly‌
@HutNewsPlus
|
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/66993" target="_blank">📅 16:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66992">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKam76W6kuwDNzRIw-I9ie9vD704me7aWntvBmmVVsXV1r63RHNU8Jfz8c6_RLjKdhWsveLtDyKTF6crboq7zSP72MXr818UJUskkANefo0r4Dfk_H8UYAJuDoWmp9ThHtneA2GnHkaOx5hazqsJYlR1gLqeWaM13lqb74CcotqWxbGnBQjJBmwEVtSOsrqJK40-ZJXqEUWRra6q9FtmEmv5aau_WQrabiHIXsmgT7HTeSwjXI3oITjR4B6Krf__1Jjj7ii9UiMVoX6qr7zRHSgho5xDS8VARwmp7Akw_hm0g1poazkiM012xUjB7v6hivVlFQSeKYANoIyENzUqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هواداران حزب‌الله دیشب تابلوهای «لبنان اول» را در جاده منتهی به فرودگاه بیروت به آتش کشیدند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/66992" target="_blank">📅 16:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66991">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromHossein ️</strong></div>
<div class="tg-text">🇨🇭
ایران - سوئیس
🇮🇷
مرحله حذفی یک شانزدهم جام جهانی
سشنبه ساعت ۲۰:۳۰
محل بازی : گیم نت محلمون در بازی اف سی۲۶</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66991" target="_blank">📅 15:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66990">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‼️
هنوز تیم جمهوری اسلامی صد در صد حذف نشده
:
تیم های اتریش و الجزیره الان تو امریکا هستند و باید برن کانادا. طبق براورد، احتمال سقوط یک هواپیما 0.00004 درصده که اگر اتفاق بی افته ایران جایگزین می‌شه. یعنی همین درصد ایران شانس صعود داره
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/news_hut/66990" target="_blank">📅 15:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66989">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/572c331047.mp4?token=nb9j-wFABVWX7mJfpFj6nGA1Z0hZRqSuYRU_7IXxzFwIyRHTfe2kgKkicXJ26UggLKb3lSWvDqs-6GuBkxQRll90hDv5tHrJCx09ovJgIJhgzVHzWPJNzflhKWZw1K4vHxKx1jDVhckSui3LRtlKrEFHuEecW1Q4kpvtLzljMY_z0yOJEywwrQrFh7w2Fp-nKHLfidBRrzB9kZqeWjkDhaPJ2bCNErbnzb7yR0JHkamEAGoJwNo8MbyhPtffccHOsYBGGbjYVHIAi0fspxd35gLFPoQsJ9r4PxctAEiEyM8SeqdtYxZSwEsLuTxXTrQYuwJAip0VpcilRcDDrPbpRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/572c331047.mp4?token=nb9j-wFABVWX7mJfpFj6nGA1Z0hZRqSuYRU_7IXxzFwIyRHTfe2kgKkicXJ26UggLKb3lSWvDqs-6GuBkxQRll90hDv5tHrJCx09ovJgIJhgzVHzWPJNzflhKWZw1K4vHxKx1jDVhckSui3LRtlKrEFHuEecW1Q4kpvtLzljMY_z0yOJEywwrQrFh7w2Fp-nKHLfidBRrzB9kZqeWjkDhaPJ2bCNErbnzb7yR0JHkamEAGoJwNo8MbyhPtffccHOsYBGGbjYVHIAi0fspxd35gLFPoQsJ9r4PxctAEiEyM8SeqdtYxZSwEsLuTxXTrQYuwJAip0VpcilRcDDrPbpRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
😂
😂
😂
😂
😂
😂
😂
😂
#hjAly‌
@News_Hut</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/news_hut/66989" target="_blank">📅 14:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66988">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=lE8-ajoY9FZE5bv5vjo-fcNcApW-xaqkREvPupoTW_bsbq8XxkFIuXqOgbhzC3SIMdG9JaLzqMB1ZqL_Pu7X0eQjE7atCaDVCnk49KQyzcFMP5p_RJ7cdGaB8p1MnjKTmRgSV_fWLcjf1EkgU99lY2UGg2MWrRQ1zRwx0P_Am0qsWKnJY6b93KsziaqpZDB0mQ9bj741sXjd-yPGHwe4AjYhCccL1gTKFRJDQX_S5qmwiRcftXbejr3-Qqa_vq_fzxBVdzqHz4iGbMpXRuaAK_OTmNmejh2XkYs6ZDzd72BtzD0n3KhCBEUbQxGrYFTrY88cL1C9cNfJrNCi0CGNfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74845b1c1.mp4?token=lE8-ajoY9FZE5bv5vjo-fcNcApW-xaqkREvPupoTW_bsbq8XxkFIuXqOgbhzC3SIMdG9JaLzqMB1ZqL_Pu7X0eQjE7atCaDVCnk49KQyzcFMP5p_RJ7cdGaB8p1MnjKTmRgSV_fWLcjf1EkgU99lY2UGg2MWrRQ1zRwx0P_Am0qsWKnJY6b93KsziaqpZDB0mQ9bj741sXjd-yPGHwe4AjYhCccL1gTKFRJDQX_S5qmwiRcftXbejr3-Qqa_vq_fzxBVdzqHz4iGbMpXRuaAK_OTmNmejh2XkYs6ZDzd72BtzD0n3KhCBEUbQxGrYFTrY88cL1C9cNfJrNCi0CGNfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی دیشب:
ایران با این احتمالات قطعا صعود میکنه اگه هر ۳ تا بازی طوری رقم بخوره که ایران حذف بشه؛
فقط معنیش اینه که خدا خواسته این تیمو بزنه و تنبیه کنه
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66988" target="_blank">📅 14:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66987">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=dt6Mw93zWEQzamEg6osG5QEvrdmmN8JQF1MJZhiZ5LDZgvNGT9f4JXOC_QBrUirZXmgCxMAUHbFFScdg33ks7xJHakCavQTvcfKlNPplhUXiKaXNczNla8sOHD-hLgKPzYvgS0S9ZsIzl8bFTg_uZuYxOSgAAkbTGH_Yd8WyUIXPqnwrTPWBpkugzzKq4BYsLjvRA9QhSIx3ZJD5ZCeYaCJtMYTBAidi5pHZtGUK1DDEZ12UdUKHtkt-xmgbjURukfuNXIDDYf2KQJbv3B0a1UQS5bEHTgznX_KKLgMeZF0-bCS7qLCAUeKJmtt2wBCuJetaR3U8gnvmMpDZQTKOSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f10176bb5b.mp4?token=dt6Mw93zWEQzamEg6osG5QEvrdmmN8JQF1MJZhiZ5LDZgvNGT9f4JXOC_QBrUirZXmgCxMAUHbFFScdg33ks7xJHakCavQTvcfKlNPplhUXiKaXNczNla8sOHD-hLgKPzYvgS0S9ZsIzl8bFTg_uZuYxOSgAAkbTGH_Yd8WyUIXPqnwrTPWBpkugzzKq4BYsLjvRA9QhSIx3ZJD5ZCeYaCJtMYTBAidi5pHZtGUK1DDEZ12UdUKHtkt-xmgbjURukfuNXIDDYf2KQJbv3B0a1UQS5bEHTgznX_KKLgMeZF0-bCS7qLCAUeKJmtt2wBCuJetaR3U8gnvmMpDZQTKOSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سخنگوی سپاه پاسداران:
«از اینکه دولت به سپاه نفت داده باشد، اطلاعی ندارم و بعید می دانم چنین موضوعی صحت داشته باشد.» او اضافه کرد: «سپاه برای تجهیز و پشتیبانی از یگان های مختلف خود به بودجه نیاز دارد و دولت موظف است این بودجه را تامین کند.»
مسعود پزشکیان، اخیرا در یک سخنرانی گفت: «اگر ما پشتیبانی نمی کردیم، رزمندگان نمی توانستند بجنگند و ما 20 میلیون بشکه نفتی که به دولت تعلق داشت، به هوافضای سپاه دادیم».
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66987" target="_blank">📅 13:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66986">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=tcEQtsECE9vNmesY6fLT6XMLjt-YDUUEEWCIanXCNMBo-RnZHUwaGQvq_GAlykFw4dD1e69j7i7ibko5vfok6nNHnMRBHkP6Gcw2BftMQYO06PK0q4IGoRh2_qboSebNDpyooOU8vFPCjZ-dMGh9c8aJrPQrcyXefF1rbquXSQ1_9qpUu_5GTAwR_Vxl-l3Q9mmo5jm6OjEeSJhOQ1Jik3PhtcsJ2cbaDikm5cDzpQUqlJ1UttCKeiOGiw_blp2G71WRUQoP9v3d_tYFnej1QdnpSAx06hwTisuoT3tBpGUSIr5Pzgrv-h8TKdgKcsX5zK5pDMLbbq1ZvFjDnMudEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/00001b2a3d.mp4?token=tcEQtsECE9vNmesY6fLT6XMLjt-YDUUEEWCIanXCNMBo-RnZHUwaGQvq_GAlykFw4dD1e69j7i7ibko5vfok6nNHnMRBHkP6Gcw2BftMQYO06PK0q4IGoRh2_qboSebNDpyooOU8vFPCjZ-dMGh9c8aJrPQrcyXefF1rbquXSQ1_9qpUu_5GTAwR_Vxl-l3Q9mmo5jm6OjEeSJhOQ1Jik3PhtcsJ2cbaDikm5cDzpQUqlJ1UttCKeiOGiw_blp2G71WRUQoP9v3d_tYFnej1QdnpSAx06hwTisuoT3tBpGUSIr5Pzgrv-h8TKdgKcsX5zK5pDMLbbq1ZvFjDnMudEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویری از حملات اوکراین به پالایشگاه یاروسلاول در روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66986" target="_blank">📅 12:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66985">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivmvayIkflX7zTMwZXRJKNnMoyjzIr_WrEAFeeVUB52haJP-Q4L1CO6ifTuuQvVt9_OqcVzo-1JqRMyFTDeSotnUL2ph_iAGcefxReRgv5ZE2GiPvpIJWuwIluGHKL6o92qJSLoUmogcQamjWZ0Aq4soLZ569ifKdM6yI05CgiG-_xwtN7p-Bodj65OMQOYtZwaXUCvvheY5212U-5B7d5vl9u6O9PxxvDjRCoh7sXpm-qQLKr6LGzaHWYbURDXT6RuJjr50hO8JV82q7zjorwZ-VwfgAudzr5uYmr_WPRcwjQb676gUUQ2dqLJAMYXmyGXgIlfBXgbOJ94g7NT-mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
وزارت خارجه جمهوری اسلامی در بیانیه ای حملات هوایی آمریکا به مناطقی در سواحل جنوبی ایران را به شدت محکوم کرد و آن را نقض آشکار منشور سازمان ملل و نقض صریح بند اول یادداشت تفاهم با آمریکا دانست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66985" target="_blank">📅 12:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66984">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">‼️
کارشناس برنامه دیالوگ:
این جنگ به مسئولین نظامی و سیاسی نشون داد که توانایی نابودی اسرائیل رو ندارند و چشمشون به واقعیت های میدان بیشتر باز شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/66984" target="_blank">📅 12:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66983">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fzSAb5EJw0PO5iIgfsbH72ABOdeEXyIevWJcJmo7tKJkLJBuivvGYq6_109afBX46amoRAigfKmteMnXHNGZFc46RtHmRpBztTdGL1wKW0XswFlLLD-eTWDCvdL-CUcC4HWPiS3vjUOUFsdJ7yv2SVtG5ZIKR-d7AbcY5W9_8jSol5uSKTidn3Zm3k7O2AQrmGN1YLYGYjYt0CLBNfYzGP_u00oxZMifPpGud9X2zliQE3Ac83iNhcFqRRJy5hgIPinjruaB6CdOZd3bWfjPOmHLiuptNmv_7twpyWXKw6aZ1tsbkucMA8Otpt6PsqLho4cRaKskmuhvLDxoh7LMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚠️
۶۸,۹۰۰ نفر در ونزوئلا سه روز پس از دو زلزله کم‌عمق پشت سر هم (با بزرگای ۷.۲ و ۷.۵) که کشور را ویران کردند، به‌ویژه ایالت ساحلی لا گوارا، گم‌شده گزارش شدند.
۱,۴۳۰ کشته، تلفات در حال افزایش است.
نجات‌دهندگان با ماشین‌آلات و دست‌های برهنه در میان آوار جستجو می‌کنند؛ پنجره بقای ۴۸ تا ۷۲ ساعته در حال بسته شدن است.
گرما تجزیه را تسریع کرده است؛ شرایط بسیار وخیم است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/66983" target="_blank">📅 11:45 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66982">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=klIO2aScwuYbl8JGP7-DfMar5hCp2lmsKis1r87B72NSVvP3zR0jkvf7H-uNWictMbzOMYBHqtbs7rA2slsdgfIOXh6EeRw9GDuWoHG7vLZqONb1kIk416L80g7dMEIgyCWfefKeETrvBczAcQ8NwrEGNzPBS65BvvmgQKTgv1lJ7Wnc5303yLXfPWOQApNxojss9xK3fohc3Qsn5-zdYctWExdpnBNy3htGkywf9x4a2ezh_oVKtCq3ldLFm-yRXZdqn9UgevKS5glQDpnmVKrbPBlBOxyXXrrLGFVJlBYD_al9GJcH3Jk1LJRT7QG-eCli4qbuJg3lUJFLhRfm8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c0f8ca35e.mp4?token=klIO2aScwuYbl8JGP7-DfMar5hCp2lmsKis1r87B72NSVvP3zR0jkvf7H-uNWictMbzOMYBHqtbs7rA2slsdgfIOXh6EeRw9GDuWoHG7vLZqONb1kIk416L80g7dMEIgyCWfefKeETrvBczAcQ8NwrEGNzPBS65BvvmgQKTgv1lJ7Wnc5303yLXfPWOQApNxojss9xK3fohc3Qsn5-zdYctWExdpnBNy3htGkywf9x4a2ezh_oVKtCq3ldLFm-yRXZdqn9UgevKS5glQDpnmVKrbPBlBOxyXXrrLGFVJlBYD_al9GJcH3Jk1LJRT7QG-eCli4qbuJg3lUJFLhRfm8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
سعید لیلاز: فکر می‌کنم آمریکا در بهمن یا اسفند دوباره به ایران حمله می‌کند، تفاهم‌نامه یک وقفه است
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66982" target="_blank">📅 11:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66981">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">‼️
گزارشگر صداوسیما وقتی گل سوم الجزایر زد
خدا صدای مردم ایران شنید
😂
خدا دقیقه ۹۵ و حتی یک دقیقه از بازی گذشته بود گل مساوی زد
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66981" target="_blank">📅 10:49 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66980">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">‼️
مجلس خبرگان بیانیه‌ای در حمایت از مجتبی خامنه‌ای صادر کرد:
🔴
1. مذاکره‌کننده‌ها باید حواسشون جمع باشه و تحت هیچ شرایطی از خطوط قرمز رهبر عبور نکنن.
🔴
2. تأکید میکنیم که انتقام خون رهبر گرفته بشه و ترامپ و نتانیاهو به مجازات برسن.
🔴
3. اگر طرف مقابل توافق رو نقض کرد، باید سریع جواب داده بشه؛ همچنین باز کردن تنگه هرمز در شرایط فعلی اشتباه راهبردیه.
🔴
4. موضوع برنامه هسته‌ای ایران اصلاً نباید وارد مذاکرات بشه.
🔴
5. کنترل تنگه هرمز، گرفتن غرامت جنگ، آزاد شدن پول‌های بلوکه‌شده، لغو کامل تحریم‌ها و خروج آمریکا از منطقه باید حتماً دنبال بشه.
🔴
6. مسئولان نباید حرفی بزنن که دشمن احساس کنه ایران ضعیف شده.
🔴
7. در نهایت، حرف آخر با رهبره و هیچ مسئولی نباید برخلاف نظر ایشون عمل کنه.
🔴
8. گفته شده دشمن فقط دنبال خریدن زمانه و احتمال حمله دوباره وجود داره؛ برای همین نباید مذاکرات طولانی بشه.
🔴
9. از مردم میخوایم حضورشون رو در صحنه حفظ کنن، اتحادشون رو به هم نزنن و به حرف‌های تفرقه‌انگیز توجه نکنن.
🔴
10.  کنار رهبر و مردم می‌مونیم و در صورت نیاز به وظیفه خودمون عمل می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/66980" target="_blank">📅 10:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66979">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=jZXxt1lhY-ETBjIiksbRUFmv1cUpV3h6e2Icz8vTSOWI-bLZ5hJcYwZP008Xef0h1ukm8FPd6nAAlH4ITMCqdbWiGs6KcCfwyXSgmgWp6IhZsVQw30nip6TXSitPnb5gg0KPojmbAeoEQAVJVTk9HxZkcl5LDADHuWxlX2MgQ4pUKonpevyBbVX8JRPusKT4mAmSSnc4CuRSYgYrEMrUcP4CijzxPO1nQNDjfShNfJONMKRpv3m25pkXVGWoFCMPishBkh_RMdOd6iat5FKD0Aox_8uzD3RwVuJh-1PCtvwDoOzMy39bJUzIuXGwCgb1uKRYXkOE10IXbJvxZdCbAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0478c4d3f1.mp4?token=jZXxt1lhY-ETBjIiksbRUFmv1cUpV3h6e2Icz8vTSOWI-bLZ5hJcYwZP008Xef0h1ukm8FPd6nAAlH4ITMCqdbWiGs6KcCfwyXSgmgWp6IhZsVQw30nip6TXSitPnb5gg0KPojmbAeoEQAVJVTk9HxZkcl5LDADHuWxlX2MgQ4pUKonpevyBbVX8JRPusKT4mAmSSnc4CuRSYgYrEMrUcP4CijzxPO1nQNDjfShNfJONMKRpv3m25pkXVGWoFCMPishBkh_RMdOd6iat5FKD0Aox_8uzD3RwVuJh-1PCtvwDoOzMy39bJUzIuXGwCgb1uKRYXkOE10IXbJvxZdCbAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
سنتکام:
جت‌های جنگنده نیروی دریایی و هوایی ایالات متحده امشب به دنبال حمله پهپادی ایران به کشتی ام/تی کیکو، به ۱۰ هدف نظامی ایران در چندین مکان در داخل و نزدیکی تنگه هرمز حمله کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/66979" target="_blank">📅 10:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66978">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🚨
🚨
🇮🇷
روابط عمومی سپاه پاسداران
:
فرزندان شجاع شما در نیروهای دریایی و هوافضای سپاه پاسداران انقلاب اسلامی، در یک عملیات مشترک موشکی و پهپادی در ساعت ۰۲:۰۰ تا ۰۳:۰۰ بامداد، هشت هدف مهم آمریکایی از جمله پایگاه هوایی علی السالم در کویت و مقر ناوگان پنجم نیروی دریایی آمریکا در بحرین را هدف قرار دادند.
دشمن متجاوز که خیانت و نقض معاهدات بخشی از ذات اوست، بامداد امروز تحت عنوان مقابله با نیروی دریایی سپاه، پنج نقطه ساحلی در ایران را مورد حمله قرار داد.
بر اساس تفاهم‌نامه اسلام‌آباد درباره تنظیم تردد در تنگه هرمز با جمهوری اسلامی، از این پس با کشتی‌های متخلف با قدرت بیشتری برخورد خواهد شد و هرگونه تجاوز احتمالی دشمن به هر بهانه‌ای، حتی مشابه حملات دیشب به اهداف کم‌اهمیت، با پاسخی ویرانگر مواجه خواهد شد.
دشمن باید بداند که نقض آتش‌بس برخلاف بند ۱ تفاهم‌نامه اسلام‌آباد است و منجر به توقف کامل مذاکرات خواهد شد.»
@News_Hut</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/news_hut/66978" target="_blank">📅 09:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66977">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PhxdwqKmil0jgHe6jNxmV8RshVy0bes-oTjDj5CZt8tB87kmLWCS0XPkPaESXkNGl27UrN8aw5XO6woKQMg4mulOUvGJFezOyibUqhL--vnkZbVku0tHxM1HrD5TmTQYNGm0ZaPRoD-jVctNX8q0IM0EmwyrjnKXBA0mGzWB4FTkfJwJzKZXMv1kx0c6h9seHsljPN9vxXK0XKrgxTb13ILApk_fureAXEQ9Cr-agPffoeCjhUVYcJt5WS6GSnQTdzXxQ7pKZUn3LwEHnAbEyAE_yTkgONvOJi1pvANylMAxGu-gapr6APbuDkoLam7CJtVzUCWvXo5UkagqEyBqSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
هواپیماهای ایالات متحده به تازگی به دلیل نقض توافق آتش بس، به انبارهای موشک و پهپاد ایران و سایت‌های رادار ساحلی حمله کردند! بسیار محتمل است که آنها هرگز درس نگیرند! ممکن است زمانی فرا برسد که دیگر نتوانیم منطقی باشیم و مجبور شویم کاری را که با موفقیت آغاز کرده‌ایم، به صورت نظامی تکمیل کنیم. اگر این اتفاق بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/66977" target="_blank">📅 09:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66976">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حداقل تا اونجا رفتید صد کیلو از اون ذرتای ترامپو بیارید الکی نرفته باشید.
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/66976" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66975">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=eI6YNCK96ln77BdDk2Hr3j0LXOs9s_5f8hvdbgGdOes9GQIpGA6k6rXQc-DC3E1OPj4Nu5q8-r7pbdtLFKvkVnWwa4goXvdjz8wQMJXBBkjRD6Ff1cTbT2R6PAiXf9Lf7QRXnG0tVJEKzkR91d5Fh_eAuVzBYWRujZJN4WHhoatmhn-7YAg-rbAowCWTFbarppQTrcca4em_DS5msf6zNaJDT4qYxrt3p_w6AsawCgHxBgm3y0gVgcl-aUgJ2fWqboCs5NZyRd6QldipsOk_8N4_xZUSjYv-NS9R21REW8ZoKeURsym74lp5VKnqmwU8FvveEEqndhTuuKwpaZFJCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df26bad47c.mp4?token=eI6YNCK96ln77BdDk2Hr3j0LXOs9s_5f8hvdbgGdOes9GQIpGA6k6rXQc-DC3E1OPj4Nu5q8-r7pbdtLFKvkVnWwa4goXvdjz8wQMJXBBkjRD6Ff1cTbT2R6PAiXf9Lf7QRXnG0tVJEKzkR91d5Fh_eAuVzBYWRujZJN4WHhoatmhn-7YAg-rbAowCWTFbarppQTrcca4em_DS5msf6zNaJDT4qYxrt3p_w6AsawCgHxBgm3y0gVgcl-aUgJ2fWqboCs5NZyRd6QldipsOk_8N4_xZUSjYv-NS9R21REW8ZoKeURsym74lp5VKnqmwU8FvveEEqndhTuuKwpaZFJCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من دور خونه بعد از گل سوم اتریش:
#haa4m
@News_Hut</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/news_hut/66975" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66974">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/66974" target="_blank">📅 08:37 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66973">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ngUELUltmOiOVjjysugU2i5wMbTUrWDuZ5-aBywJmMM7DvFCG23SFA-9Oq8Ec5MyCkXjJN6Zi5nJQXnotZFzETRN7TbERG5YYbji9h8hgs53QasgPucuZL24qtlQNJdBhhHC9ThSO_xxjBHjval8fkOAiqHdHni60s967qjTUSlkxP4Lg9DuYZnLgQVzgjp_hjsn3H_S9ijgF1bBAfXawifyNUPbFE8dLQfuW32ElLEJZDbO_bY-xBnqPSqxssBKY8zb9DNvFqQFPHOJsdXP1HdOc7cJmzmmLfWLg3ch5-BIaUx_vbXkXBvfRGuSC_U4zp8pXMR1bHpnF8iyUxJtNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a4cb5436.mp4?token=ngUELUltmOiOVjjysugU2i5wMbTUrWDuZ5-aBywJmMM7DvFCG23SFA-9Oq8Ec5MyCkXjJN6Zi5nJQXnotZFzETRN7TbERG5YYbji9h8hgs53QasgPucuZL24qtlQNJdBhhHC9ThSO_xxjBHjval8fkOAiqHdHni60s967qjTUSlkxP4Lg9DuYZnLgQVzgjp_hjsn3H_S9ijgF1bBAfXawifyNUPbFE8dLQfuW32ElLEJZDbO_bY-xBnqPSqxssBKY8zb9DNvFqQFPHOJsdXP1HdOc7cJmzmmLfWLg3ch5-BIaUx_vbXkXBvfRGuSC_U4zp8pXMR1bHpnF8iyUxJtNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا ابد موندگار شد این سکانس
😂
😂
😂
😂
😂
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/news_hut/66973" target="_blank">📅 08:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66972">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=lucprJrB5GKnQEMaADVZh3Qyvo2UlbJ4imHdy6NUsWwL-ZnBMG79QI82Fv75hXjWWZhZekBrqDZiHYLSzeosotyKhG0JY1bMtbnEfzXnidK1ekEqGOtQZ2ZCT6NLMFqnYa49MaKi1XdWtL1yJNWn2NBkdH-LWzy9m--G5aenv8eDJ-4MKd0_zrX12QErA2o43f5c5yrvt-SxyAGeEWXuO46s8KGuQYYqpDxUUk-D1ozvobPtgBwr5InPGEIsGV7CNns_CPKHFlQyGAieO0FKQmJkZlIwP9D6HYbkDHTsc5-_o5-ckIR4Vc8ErR4wOIEFN9sU89sm2XxHqs4GbockZg" type="video/mp4">
</video>
<br>
<a href="https://cdn5.telesco.pe/file/b5b527c33c.mp4?token=lucprJrB5GKnQEMaADVZh3Qyvo2UlbJ4imHdy6NUsWwL-ZnBMG79QI82Fv75hXjWWZhZekBrqDZiHYLSzeosotyKhG0JY1bMtbnEfzXnidK1ekEqGOtQZ2ZCT6NLMFqnYa49MaKi1XdWtL1yJNWn2NBkdH-LWzy9m--G5aenv8eDJ-4MKd0_zrX12QErA2o43f5c5yrvt-SxyAGeEWXuO46s8KGuQYYqpDxUUk-D1ozvobPtgBwr5InPGEIsGV7CNns_CPKHFlQyGAieO0FKQmJkZlIwP9D6HYbkDHTsc5-_o5-ckIR4Vc8ErR4wOIEFN9sU89sm2XxHqs4GbockZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/66972" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66971">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fSWho2Y_oO52_sJRvJjA4XX2xfwnOUzrN0hatyXlVtorzD3Dv9MFXiXLT_XG8e0wY04_nOxOXi-ZNKt46UFsNAoE0_Akn8XZPLMn1BdYwT1Gnnbr7Oy7AuLOgbU0KUH1kzf1_V_cRWzwkZ7p5Aujvo0zw-NbokXNi0QL44wEvK_0egdgNfwyYt5uoReXixGwFyHBhRnaUSz-ML-1Ygli2XjOheM9qKHzi-poW83lYyVk7k-KUeq_4a4skbOZCjwvlji9o4jCTcs2S6TS0thYr5AcB-OfcXHHE_cnf2iwjRMcCRr3Qar3n7BXyS1uqrqAVIG92Ie3VBwu-g7EXP-lQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خانواده ۴۰ هزار جاوید‌نام امروز خوشحال شدند، میلیون ها ایرانی باشرف امروز رو می‌رقصند، روحت شاد مهران عزیز، امروز رو خوشحال باشید، بزنید و برقصید که عزیزای ما تو آسمونا خوشحالن، تا می‌تونید این بیناموسارو ترول کنید، خوب و بد ندارن همشون یه گوهن، نفرین میلیون…</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/66971" target="_blank">📅 08:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66970">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‼️
🇮🇷
خبرگزاری سپاه پاسداران(فارس): بازی اتریش و الجزایر تبانی بود!!!!  @News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/66970" target="_blank">📅 08:12 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66969">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UhdyAcyLX4-CGn-06Cm6NE0IxGYLKD0gjxv6XjKPRo4jhjoRH06qC-KQYsdRxBJv0WhO6XeQQt0Do6nrY8UuKgiBx5N4_ZahlEbIyZF_PY6pcrPMAeGoSAl6oCZBXShXzg-sPnO8C4q9kl7tggs-c4s-nhAnH_JRccpVnazo77vEaNNeD3jwzhSInYYe0PQ_r0W1hfqZK_qONuYfPgpZImzLePCi_fZpRiwX-KLFqqhbM1_Lq5p0l7rjDs2oJZkuCXqGlK556JORPc6ttnGI9yI-RGGBJkv-8hTG7WyxGX1k1BBD0M-le-NGCZZ2PnEQsniBJ5Q7BPio5kUf-VDM5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای
😂
😂
😂
😂
یکک دقیقه مونده بود
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
اتریش
😂
😂
😂
😂
😂
دقیققققه ۹۴
😂
😂
😂
زدددددد
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
#hjAly‌</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/66969" target="_blank">📅 08:05 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66968">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vag4WYyKlCEbVxe3T40GazkNiqtefwnOfooo3hEmZ56IeURMK4EfG1yFLx2E2KCuDIq8HDiq1RUR1h-95YZrxmN9sZWqLg6CWJhZxzY0rxbc8LiJyHapRYMXyOa3caUjQ8VEugFTVSpMNQoyaFsPpXSIrpoHsMthl9T_CYcAeUSfyJIRTTos3NRtuYuvRzyHwlxndbjbXLGvq_XJa1TVSkEFB1CDJWRcQRcMPYzcGUCVn-L7JlKf3iQ_rx14vpLBDOW6yPdebKCGwzbdEae14DpzBk_iSIahNCW-nQWe4A3PW-vdBimYaO93p920g63HxCp1bObVtifAHHALUGeTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/66968" target="_blank">📅 07:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-66967">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MIGjTmKYTWwMdWqEX3uAZXGQDE5b_gzX_uXLWN612alqoqwUIBTd6Ccs9M585DX5dUQcQ8dTq2iHBfvrZl9pQ3i-HSLqA9rb5TNFgO88z7DS9W_N2rjbdwsWNSX3cbjJp1CpOv3MOzNowhatILpR0oli6oy3OQx_Mvi_4ujnsUyWQUOZYve6JSlkXTSjP-HF1FsMgTOTkAII6SDUZUAkGogDdvgZ0F_67gAjUzF0V4HytVLFxEQBn6wzTRUztJkilEa1urrD8ZTSp-heSDurlSaOI5m80Q9mvS3DXDA5Ag-x98-jvOSLyPx4qvklIJaF2s-kgKKCSjLFxmY6G9uqpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برادران دست به‌یکی کنید نتیجه همین بمونه، درود خدا بر شما شیرمردان مساوی‌خواه
😂
#hjAly‌</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/66967" target="_blank">📅 07:38 · 07 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
