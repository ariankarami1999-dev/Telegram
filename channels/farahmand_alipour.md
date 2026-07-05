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
<img src="https://cdn4.telesco.pe/file/R0ukF6YuJGfk6QR4W_kUt4LZoWXyR68nGhgAaGRupxOXfzeIIvxIVHchkX13f6nYxRluNLgGnGxRryGHZsg5Gz_bYJ0i_WlhCmKCKJJ3vOQlSM0MDEV0lJOJt3C33K0YPgOf8DjgSW0Qwjequ2px8d2oOXbHLewFGOSJcaWgxVRrYhHs3NKqBRcCQSQIg-hrRlTKxMyBFI-XM_qtbkJz_YQW6S-CCXRXBI0HZXM_YB6EDvYxY7Aihn-05mB4weml-2o_hemEB5_nXvP-KdD4adsn5uA6sEzs37Dc8ckoQlAy7yNLxeMx8afLKYpmYCGsFg8c6qLDawW0-MRi8cViJA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 62.7K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-14 11:56:41</div>
<hr>

<div class="tg-post" id="msg-5861">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">این کاروانِ عزا مسافت قزوین تا تبریز را پیاده  و در میان ضجه و شیون مردمِ شهرهای میان  راه طی کرد. در هر منزلی که کاروان توقف می‌کرد، علمای دین و صوفیان جمع می‌شدند  و بر جنازه خان مغول و حاکم ایران،   نماز می‌گزاردند و قرآن می‌خواندند (غازان خان چند سال قبلش…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/5861" target="_blank">📅 19:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5860">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">برای مراسم عزاداری غازان خان حاکم مغولی ایران،  یک مراسم بسیار عظیم حکومتی برپا شد!  که خواجه رشید‌الدین و …..مفصل در تاریخ ثبت کردن.  یال و دم اسب‌ها رو تراشیدن،  بر روی اونها پارچه‌های سیاه انداختن، پرچم‌های ارتش مغول را وارونه آویزان کردند، بر هر سر کوی…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5860" target="_blank">📅 19:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5859">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری  حاکمان ایران، مربوط به «غازان خان»  حاکم مغولی ایران بود.  پدربزرگش «هلاکو» نوه چنگیز خان،  وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،  برای او مراسمی به رسم مغولی گرفتند پنهانی و خصوصی،  حدود ۳۰  دختر  بسیار جوان…</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5859" target="_blank">📅 19:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5858">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfJcmnNIrdROT93jUDFe16HicYX-kbjTEaLzBUWy0R_QbLUNh4PJliyZ4kXErbfaW-VIqicmP0PHKHP6TE_n-1dccalJvzeBTt44asoXAA0sglWaxMwPvYqZQADAoFp_vcWiaDlsnNoIg62hiDFY0FaYAL9-ESZ3Mzi-cl_lWXJMjZNSdJ7lLY9-63GFakJM-7xIPFdMgf4f4sCUplmCe5hs3I2pBK9pzBBtqWHWFh7Hdhopa6Vqe28JYG4Vnn0tABb71hDEogzns-JqNQuheogk7yxSVCHcaOlzH0oyXL-LabxJnReayoynf1qlZV5kxlZIyv0h9gLKmCeXQkO9Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از بزرگ‌ترین مراسم‌های عزداری
حاکمان ایران، مربوط به «غازان خان»
حاکم مغولی ایران بود.
پدربزرگش «هلاکو» نوه چنگیز خان،
وقتی در ایران و به عنوان حاکم و سلطان ایران درگذشت،
برای او مراسمی به رسم مغولی گرفتند
پنهانی و خصوصی،
حدود ۳۰  دختر  بسیار جوان ایرانی را بهترین لباس‌ها پوشاندند، جواهرات به آنها آویختند
و آنها را در کنار جسد هلاکوخان، زنده به گور کردند تا در جهان دیگر، در خدمت هلاکو باشند.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/5858" target="_blank">📅 19:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5857">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccf07e73d8.mp4?token=Sus_ujqd4ki_ko8ue9jRSf_Zg9EGjIU4IwL8osyV04M9qQa40njge44ukGXPbYSMJssHNoBg-16z1zSOmdfyiSCNnzSJV8jDyf10355qHdYZX5krOAxkrrMkxIsw6Gu4O3DWLgha7Q_M_XoivS2FPLoFsNo5q-jtoumkSWHVHNoadCFKcqG5yjZUxZugG-OmCHoZi8ZKTWmwEttfuwgZmQOoi860qktuczpVXqlqQ8admBCwNPeusk9fRp3H9T2efQeJXFe4VLcHwU6p80schnJ6ckL9Nv6R3XPW0m8uqAZBAmxHsjB4PdSULN8Q60_vbXn6wfFT6XTXKDUt3ukE2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها رو!
آقامون چقدر قشنگ رفت :)
چقدر دنیا رو زیر و رو کرد :)
در نحوه رفتن آقاتون، چشاتون قشنگ می‌بینه، ولی انصافا کار خودش نبود،
کار اسرائیل بود!
ولی بله همون زیر و رو شدن دنیا بود که
باعث شد که یه مدل قشنگی بره!
برکات رفتنش هم خیلی زیاد بود!
طوری که رهبر جانشینش ۱۲۰ روزه
که معلوم نیست  اصلا هست! نیست!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5857" target="_blank">📅 16:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5856">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اینو یه هل بدید
😃
https://x.com/farahmandalipur/status/2073333637022449802?s=46</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/5856" target="_blank">📅 14:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5855">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a4cd9282.mp4?token=quTqKQAoO_INYIHsOPttKncwOyum_t4Ms_bwQr1Ao_9I3w1F2Uu2U2wulOGLpEzzPXuZIgFs9bvhR5NjSKqtJwAR_trN9XLu5lPSJYw0-bXSSaxs5rVK0cYofuONmMpRkZc1n3n1MeG0vl04U71VneZkH4SRaHEZ9FNgsqyMncyye5dH8HFr-DPnk_W7BJEtSfeRjXk0eRyWaMyx8dfVCTUQi4HERpdLpK6Z6ZNS2oBc8y0yxM2E0tXRc0ZiCY6m7RdwZryJ2ihK5FJnb6AdwQpDiHvW4gxq_bRoN7YxlMF964pN3LxmIVvGO88wug1ElZxpRaMOX8rd0eE12m9wFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏مقایسه وضعیت جسد علی خامنه‌ای (۱۲ تیر ۱۴۰۵) و برنامه «طنز» شبکه افق وابسته به سپاه پاسداران درباره اجساد کشته‌شدگان اعتراضات دی ۱۴۰۴ (۱۱ بهمن ۱۴۰۴)</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5855" target="_blank">📅 14:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5854">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NQHulXfRky7MAataJ4kesF-qp0E05VAm0c3xV6KoQ-KXW9CDcaUrMJ_vuAEa2hTO3MNhuQHIzcv0qkBsUrdB9eagzBNutOB3gXfSRlhjQQgSMqI6SehwDE79SlZXw2s3Ey2JhyRWWjtNrzHUHD_s62OvFtpLzvTnJB4C0n3R-cbjoWjf2eIEyftuau8JoOKLrEpi2TkeD1oLzCewOLNFTqPuG_7xfeaSd7X86ZLCb_s7OGKQ8b6pnNIxehzQaK3YDfUiEvcTnrJM594Sk9B84oqBv6BfU7z1UdNYuZeu66mZjeDtu_2TdsXkPoVy76bZVuHXA-se9U0HOtKdli7vaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگر در مراسم ولی امر مسلمین جهان  ۴ نفر از روسای دولت‌های جهان  (از جمله ۳ کشور اسلامی) مشارکت کرد،  در مراسم «اسحاق رابین»  رئیس دولت اسرائیل،  ۴۹ تن از رهبران جهان،  از جمله رهبران ۶ کشور اسلامی شرکت کردند.  (حسنی مبارک رییس جمهور مصر که توی تصویر هم دیده…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5854" target="_blank">📅 11:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5853">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL2EJtcpfihHSwKfkhy73HtBcPK32Ralh18laK-yxKheTIMIR-yTKOwW3uO-7JSTZYEkjdpZTdd0LjlR0sWTZBrQPsVVJze7e4qduT6RInNHFekdR0hSAuABqfIyD_1vbRJA3iLUmuDx5DxHlHuW8yOj2GXaMuLzw87mGJeC6WxDF0-Eh0F3A12VaOSNYACyh2r4hy0d0375mBTZCymBUtBSqosat2ej_o76HGvfOa45ZHKaGPYI3u0TwxT52Prvhkw6qjohqxZ8UTO0lCF4GTaNyAGCvEHLeMF3dH3L1NAuodINtTVQmPkU8K0NSsL1bNmge-PxnlTXhURocQ4Vug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر . که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/5853" target="_blank">📅 11:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5852">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYJRFQvhISI1GvZf9xKq5SrjG7wMbgQR5njcALOEFcufvNAZyMgPf7bQX-5DPVJc5fPWMh-MqzAr2kY3Wjo1_wkwlHvXjoYJ0NfvGIUVxob2HT4E9pSCPafP5YZse0stTFhK0F8cu6bD4wLIBWgt_BUTLTNqNebTxB_0rOFlZYLCOC4jXL2FiaCKM6gGqUYnWdXd_9ihWpv3XgcjKwC3blpO2B-Ra-oNkbGLiMA8jl5xhnSY_h5ysVM4ufC8OPQvfa2o6GiNnpEDPWDBrx72cbeO4Pu7c16DKZY_rWRMwyQfLP2yGOoXcFcWjpFPGfhqYySc115PoPUYiYmfAvDoyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در مراسم خامنه‌ای ۴ تا رئیس دولت مشارکت کردند، ۳ رئیس جمهور و یک نخست وزیر .
که از این ۴ رئیس دولت، ۳ تاشون اسلامی هستن (عراق، تاجیکستان ، پاکستان)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/5852" target="_blank">📅 11:18 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5851">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hU5FQmIvF1wom64UWca7ZKlfD3k7B-pAmTGzBM2FqD-QgEoBo5ERh0H97GkSRKsypX7w9_F0sUnhuzOMsK8DJk4ZwAr5FBm1qFtX03BsFGNOXC4UDRhxQPtBVbHE11Dt3Ky48awdGBbg6YEZTKjdEhbWbdVTkbRf7uoJQtIdv8W7fwwsMjyYznlf7iCsKBSK0uS-niMfX5184niHj86-1D46Oxp6IZVVOv5K5weK9gpt8lY9qzfanSg_FWebNrAFEo7M1AdMV7hbnv03J6gAUxu7Y9i_G5fBMEjy_r3KgFYLA70LN2oAhj1i7wxJ8t7hfjHRo2guYUK1T1YzJQmkJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فقط برای اینکه فریب اینها رو نخورید!
ظرفیت مصلی تهران، وقتی پر بشه  خیلی زیاد باشن حداکثر  به ۱۰۰ هزار نفر میرسه،
اندازه ورزشگاه آزادی!
یعنی اندازه «یک درصد»!
از جمعیت شهر تهران!
یک درصد!!
(ظرفیت نمازگزارانش ۶۵ هزار نفره)
حالا اینها رفتن از هر ده کوره‌ای و از عراق و افغانستان آدم وارد کردن، تا همین ظرفیت ۱٪ جمعیت شهر تهران رو پر کنن!</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5851" target="_blank">📅 11:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5849">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TFAKKtADXspnczadcDCULO632uV3rT8mVGpdjj6p4tdnPDgz6HhiFgL8Ow-ZfFk437V9BfRkkmKOaXv0GVYlpArZya6tuxkmnrBvIsSFSfVlnYZuKHYk-4TqkxD0YYUwCIZ7o6TghImmMdkYt_plAAX4rTIDMSdVLZuBT2WrEq-2jIGCPv0vNbPDl45z91rlZLuhKaMwk4o-a8ZGGASFClgVNXF-XsPDVPck-T4CbmZDjG95M11LcH1DrFyqKd7vCtb34jtHx8Iy45i4JCMK2neWAWCwsG8_U8xQnlPwSA8j09mKDLqjmSl1OYJfFRwrxR7lNMn_NSc7_DtMkLeFcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان «معاون وزیر خارجه» فرستاد
اندونزی سفیرش در تهران رو!
ترکیه معاون وزیر خارجه و معاون رییس جمهور
دولت لبنان «هیچ نماینده‌ای»
در هیچ سطحی نفرستاد!
تشکیلات خودگردان [دولت] فلسطین «هیچ»!
امارات «هیچ»!
سوریه «هیچ»!
مصر «هیچ»!
تونس «هیچ»
کویت «هیچ»!
بحرین «هیچ»!
مراکش «هیچ»
اردن «هیچ»
لیبی «هیچ»
جیبوتی «هیچ»
سودان «هیچ»
ولی امر مسلمین جهان :)</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/5849" target="_blank">📅 00:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5848">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UWK3YjDqeqzxH3Ej3bQHsf0aynQAz8V_pUfw0zUuRadJZ8fHzejokSynMVkLE-AaMnL4_0y4tleLP8d-c_JK9PQZdgTwluUmoLnTbeVujbMICREhNwuJe0EW6xhieWoguPycNjbh_oXT9G4VWOdbmNZtSnAMze5-MPaUX0B69KOJzRbUpLQD5TDNGrTe-6_GVYiFiLGS-zJsnEhc8Bu80R3zg2QCE1ZhK8AwassKtYwXikjVSP9UHSLFQpcAAGpvoQZLlxdpAljPRd5q-XLKEJJmM7nuL7UVF9uZKQOtlG27J4OtXW0ABRZQn3W0znzkKBdYA0R9wAXuF6hpooiGWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که برای شرکت در مراسم «اسحاق رابین» ، نخست وزیر اسرائیل، شخص رئیس دولت ترکیه (تانسیو چیلر)  به اورشلیم رفت،
برای مراسم ملک عبدالله در عربستان
رئیس دولت ترکیه (اردوغان) به ریاض رفت و‌حتی اعلام عزای عمومی در ترکیه شد،
و برای مراسم «شیخ زاید» در امارات
رئیس دولت (اردوغان) در راس هیئتی بلندپایه به امارات رفت،
برای مراسم «ولی امر مسلمین» در تهران،
معاون وزیر خارجه و معاون رئیس جمهور فرستادن :)</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5848" target="_blank">📅 17:41 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5847">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c5aece625.mp4?token=WQslslzo9WDMA2DkcajEDU7rtLwTmWAXcr_hhXSWYjeMR4mZvTJlESwl15N6zpeGM-c6P3NVyj66HBkD0SKa3BiA0t4MyKuFwclHNMW62VryU-RyRa9XOgr_dIVS5_71S3vGDl3291qdtu-nqut2xE3nWBhCJVnrfmBAEgcVPEm3fIz5yZu4HVNScXpjW636d97DoI5e1QpUNONIKJRfrIn5JTwCXRbStDHli2cS5SnfphLd44wzDx9wpYPQLlPiOBBBPwcKi55oOWjrs_1lYOsf4Putm4zpS_Nwo3ao5Ss132HE6F1MAgGJIcyEznB_GvPX4oZQYsdEUBngmJFOUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله
رهبر سابق گروه تروریستی حزب‌الله لبنان:
خامنه‌ای منافع ایران را فدای امت اسلام کرد.
به عنوان نمونه روشن در قضیه فلسطین.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5847" target="_blank">📅 15:56 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5846">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/926da5b0c7.mp4?token=MMG0BllQZBiM_JP_CWbdyZXFIG33aiIkGvrnv_Rmuy-vQq0TxPv08oAmG9ETFfwU8_M0zLBDS4C-NpkN7rOJAHk4V4YTaMc9tZQGveqv_OfD3fF3twEh9_qSX0Ptxpo_Gwu8VKmoPbt3gYqeWFQ7qtX-m_9rLr9z2uY6iWkHmQZtwHbNxOQH8L-fkwLxRc3t7LegyFIq-sOqyUgnhZ79-_mOwoJk10jPJeeBxsDYMmGsx6_NfL5ZKnd7CCOVAc2XOcyyRPrX8KbJbWdVUtOqAbF2ZLHQ7u7SkcyaoJ51rFXOlil029JUs4V7z9_bBzANnVun5tqYMwWdPerw0rbkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چقدر دنیا به گریه‌های ملت انقلابی
و مبارز کره شمالی در سوگ
رهبر خردمند و آزاده‌شون
اهمیت داد و اعتنا کرد،
به گریه‌های شما هم اعتنا میکنه!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5846" target="_blank">📅 15:32 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5845">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a9e91869e5.mp4?token=GqzkH6FKXLh-i3yJVAdsuqggsAXmK5HqP1SM9pF9LeA2r48LjaUx4uRZTacm37HFMioQ7EgggdF0yW4GiQKtIZOJciERVU8dw7GdNCcLzPvgt3Mc7c1GbvjnaV5z-6FsyAf3bOVbALkWF5dZkvcO3iodYsbIEMaNp09ZeP8Gl1N4XwIwO8oOGyv_QYhpDDgLBmMFgB2q6qZXaV1H32UTHGwJXabq9WrWtNpzh6LbDsqaJ8A9aInLXKHxhnkQ4-QmmTtT4_QUAI9ecD0TbVcaJsd6hRnt8_eXJMl4gRXbifFjQnozEHQMFkbEQROR3cigwSeucdl21L5ff7Pl0_e1bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا دیروز مراسم صیغه
و عروسی زیر سایه دوشکا و جیپ صورتی داشتن! تازه بهشون گفتن
سید علی‌شون رفته!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5845" target="_blank">📅 15:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5844">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbfd35ef.mp4?token=KWBbwK6y6rUmUAoxfRm0kBV-pz2Pq3MlRIpKi784OMJJwV3kgJiwkRlMo-iSQHpE4KurN0dr1KEAWtaa_WW3DpmeeMVilhhcHyBrwdZzEVV7lLf5h1cD3nReiYQRrEPB6MuV3b-1ldMywK63WVMg2PefEBZvT9fslrGClzZv4FyY7u-atkTmH5RUxYLzACQOXfpnEzg6724qGdxHAHmAk7XhI8xKtTAjajyEhtZGLPqRTI0HqYaN1l1S66IH-rWgXqR_0Tm8e3FHNdhgzLWLFJ3xObGiwRgWaaQRRBue5W03Z7NAg5JQEmDW2u7cjXfe2TVG7y4yU44IUTA6Eggu8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقای غریبم :))
کجا بود که غریب بود؟
توی بیت خودش و در حلقه فرماندهان نظامی‌ و محافظانش نشسته بود!
روضه‌خوان‌ها!</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/5844" target="_blank">📅 15:24 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5843">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4889807b7b.mp4?token=hLVQm0BHqiI2Tq7fGrDCFyKSffr8z1kXF1SJRdoaylvgwQZoZZxSua6maAY3gdR3I7Slp9cI_Ua1miJ47UvNS6E7MovRhngw6hWXfL4j_mQ4aixz-Iz7pwerQUUYGy35hHrCRjyMc8rRWkFyrLwkklr6eSg4TR1YhRp0qOoGbR9pxMt-cj-cSSr309-wZgEV65a-Go_rVTOcfOGGl_XboLIBNqzy26AxyPxSunzzyC99a1xeCXAsMFLc066lOr1XtEUpXeCM5PvyVxXnh5mvhMYVojFxJFPRLCKlgz_aHLLhGOENqdsXYu-aiDZ_lemUFi_ok3on9-6Hj7MDIDO8nQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟ با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟  چون مبارزه آنها برای “ایران” نیست! ایران اصلاً موضوع دعواشون نیست! آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5843" target="_blank">📅 14:28 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5842">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=k0qNLb6bxen9RMrDeJYQy64CP7MwXlrJX2dgDE4S2bPgbSjWajebcmqD1iNUlnfbd130LnotaxbPoltPWWfwbKpucQrUCDAuhz-cSy7hX7mDp9KlV0HkHgPv19s4r5hWDPgpT9_9nIR3f4c-_27dGZ6m8J3B1F9IsHdVh-dXiSUAYs5uBA-ViJrCTKNfijqXh1sWAk31MdnKEdxu3-vwbsXvosobWJdlvkBxLHc5hBA0myZA9Mg0sqVhO-dPLBd9UIn3NZPagcImj3q0uY6_Xmrlo08wsLTVXocaD_2A_uJnns3s1FhvaserHzfMB8HKL0KIncVaekR8Kp1qXqf_hQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc75f62c4.mp4?token=k0qNLb6bxen9RMrDeJYQy64CP7MwXlrJX2dgDE4S2bPgbSjWajebcmqD1iNUlnfbd130LnotaxbPoltPWWfwbKpucQrUCDAuhz-cSy7hX7mDp9KlV0HkHgPv19s4r5hWDPgpT9_9nIR3f4c-_27dGZ6m8J3B1F9IsHdVh-dXiSUAYs5uBA-ViJrCTKNfijqXh1sWAk31MdnKEdxu3-vwbsXvosobWJdlvkBxLHc5hBA0myZA9Mg0sqVhO-dPLBd9UIn3NZPagcImj3q0uY6_Xmrlo08wsLTVXocaD_2A_uJnns3s1FhvaserHzfMB8HKL0KIncVaekR8Kp1qXqf_hQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا کمونیست‌ها حامی جمهوری اسلامی هستند؟
با اینکه جمهوری اسلامی “هزاران نفر” از آنها را اعدام کرد، اما دست از حمایت از جمهوری اسلامی برنمی‌دارند؟
چون مبارزه آنها برای “ایران” نیست!
ایران اصلاً موضوع دعواشون نیست!
آنها یک مبارزه جهانی با آمریکا و اسرائیل دارند
(دشمنی‌شون با اسرائیل هم فقط به خاطر اینه که مورد حمایت آمریکاست، و الا سال‌های اول تأسیس اسرائیل، شیفته اسرائیل بودن، شوروی خیلی زودتر از آمریکا، اسرائیل رو به رسمیت شناخت.)
شاه به درستی به اینها گفته بود: بی‌وطن!
خودشون هم میگن که مبارزه‌شون “جهانیه”!
“انترناسیونالیسم” (که بنی‌صدر میشد، “انترش” ماییم!)
به همین دلیله بهترین دوستان جمهوری اسلامی در جهان یا کمونیست‌های سابق هستن (مثل پوتین و چین و ونزوئلا و…)
یا کمونیست‌های فعلی: کوبا، کره شمالی و …</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/5842" target="_blank">📅 12:00 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5841">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dziOjx5OoNhD_-9DwbyrRpH7HIIgqiQf-louNM7RwEiviwUiQj4ftplmKgHL7PqIjB22wtTte_F3nO004BDYShcipYIwYBp5Qvvab7eUtp7Fyc-KmgZHPvC42u29jlay76yMSC21BHMXP4_Uw84FmsqiqR7BvFJljsbyms6zfJGhVmssZcLpdbKWNyt1mGxy4QgLP7Q-ZYIXeJa8Wr8JVedkGEvnfTE5vHxO83Iwd-UT8K1FvV0rlkBbT-Bs8mfJygFLgEWJeAIRx80NYhtHNwhsGZcdsyt3Hkg03kpDYMGVLX90Ymfg90aD0DD8knkaN5PEB16YH5_jXTimDFrnlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت. الان تنهاش گذاشته و می‌گه: پیش کی بریم درد دل کنیم؟ اگر می‌خواهی من پیشت بمانم :) سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/5841" target="_blank">📅 23:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5840">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=SFgUHKE0qQedw6dz4Zojag3WOqkNNNkuL6Vn6pRpu7QaJT58mD116SG28o6V1NQun4lgaF7ZRBAhZLcsH0mnA66BS82IkmiIec4m8Og5Kpd81SFSfznDcF-Wk_afyB5gNvj2QUDsBTVt3ZWYbaD1YvAelCLxneM2b2VAuPCRRW7SQKvk86QJ-6KwjkAAYYv31peB4QkFF5qVW_kKdUnolhpzo_Em6sAOtKkLaNadbwqxR_e4I7PPZdkzyefQzlMLQjKCzoB4qS9FM9ncYz2y8CFQ22XpvI8FYo_NhZ6ZFNWKQwgAhG0Zjil6qMn4AgaMZ_dg43YIHx-O-IxlAt6rZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ed77bbc4.mp4?token=SFgUHKE0qQedw6dz4Zojag3WOqkNNNkuL6Vn6pRpu7QaJT58mD116SG28o6V1NQun4lgaF7ZRBAhZLcsH0mnA66BS82IkmiIec4m8Og5Kpd81SFSfznDcF-Wk_afyB5gNvj2QUDsBTVt3ZWYbaD1YvAelCLxneM2b2VAuPCRRW7SQKvk86QJ-6KwjkAAYYv31peB4QkFF5qVW_kKdUnolhpzo_Em6sAOtKkLaNadbwqxR_e4I7PPZdkzyefQzlMLQjKCzoB4qS9FM9ncYz2y8CFQ22XpvI8FYo_NhZ6ZFNWKQwgAhG0Zjil6qMn4AgaMZ_dg43YIHx-O-IxlAt6rZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تا پیش از این می‌رفت پیش خامنه‌ای، درد دل می‌کرد و غم‌هاش رو به خامنه‌ای می‌گفت.
الان تنهاش گذاشته و می‌گه:
پیش کی بریم درد دل کنیم؟
اگر می‌خواهی من پیشت بمانم :)
سنت و فرهنگ روضه‌خوانی :)</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/farahmand_alipour/5840" target="_blank">📅 23:52 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5839">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=BGjdtSnVRA1rmBBwNyt67IDloauhVSAYdHfUICUrYfO78h0MFU7GVQ9XiCAe1CUGqkNQJHutlP9ZCP7p_4ewwCEuwRkUozoSV5M0Xo9cmIVNyibF1Zsrhj9d0vCrVTfmL8B7eb_W56GhDfrknbGr3Aif3dtzVjQKLk3yFGHg95RpvdrZsAvPp-qKRUV44JiDGZ66sqqgIqX9zObjLUs64YRUwsII_2eFy_IGipIDx3ZtkSO1-6A7hkbUop6NFsnpKxW0vSujjD85h5n5HH_E0TzrGu40b2Tub0nEUHDv5stt9IgFeCdPPWr71Aj5UZxaPQE-FiQnIqw5F0DzGjYwrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abcd4ade2b.mp4?token=BGjdtSnVRA1rmBBwNyt67IDloauhVSAYdHfUICUrYfO78h0MFU7GVQ9XiCAe1CUGqkNQJHutlP9ZCP7p_4ewwCEuwRkUozoSV5M0Xo9cmIVNyibF1Zsrhj9d0vCrVTfmL8B7eb_W56GhDfrknbGr3Aif3dtzVjQKLk3yFGHg95RpvdrZsAvPp-qKRUV44JiDGZ66sqqgIqX9zObjLUs64YRUwsII_2eFy_IGipIDx3ZtkSO1-6A7hkbUop6NFsnpKxW0vSujjD85h5n5HH_E0TzrGu40b2Tub0nEUHDv5stt9IgFeCdPPWr71Aj5UZxaPQE-FiQnIqw5F0DzGjYwrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از ۷ اکتبر ۱۰۰۰ روز گذشت.
گروه تروریستی حماس در یک حمله غافلگیر کننده در عرض فقط ۳-۴ ساعت دست به کشتار بیش از ۱۲۰۰ نفر زد
از جمله در حمله به شرکت کنندگان در فستیوال موسیقی رعیم، ۳۶۴ نفر را کشت و تعداد زیادی را زخمی کرد.
این حمله در سحرگاه انجام شد، قبل از طلوع آفتاب و در حالی که جوانان حاضر در جشنواره موسیقی خواب بودند.
آنها همچنین ‌۲۵۱ نفر را ربودند و با خود به غزه بردند.
با آنکه بارها اعلام شد که در برابر آزادی گروگان‌ها، اسرائیل حملاتش را متوقف می‌کند، اما حماس با عدم آزادی گروگان ها به مدت دو سال باعث طولانی شدن جنگ و ویرانی سراسر غزه و کشته شدن بیش از ۷۳ هزار تن شد.
فردای ۷ اکتبر، حزب‌الله لبنان نیز دست به حمله به شمال اسراییل زد که سپس به یک جنگ گسترده بین اسرائیل و حزب‌الله و حذف حسن نصرالله انجامید.
اسرائیل در این مدت نه تنها رهبران ارشد حماس و حزب الله که شخص خامنه‌ای و اعضای خانواده اش و بیش از ۴۰ تن از ارشد ترین مقامات نظامی و سیاسی ‌ج‌ا را نیز به قتل رساند و گفته می‌شود ابراهیم رئیسی، رئیس جمهور وقت ج‌ا نیز ترور شده است.</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5839" target="_blank">📅 21:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5838">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ksuk1mjz3AQnW8v1BBeJ7SB4UhEPN57q-5TUpuzOc8ZRYcKF2GpycA5aFq-AgOn4KAiok2mgLvpzW1Tw7Zd9nK2ArZuT7r7jN6dmeUj-hwETUO7Bp_9y-eLqeCj33JKYdgZ8UGjixFB8mRYYdVr3_-OfTkPNgwHRXgRROLG_rJvT0vsZxD1Ll3vGjeQLG9DLU8Ur1wLG6Fc6oEsdYRunslhOx5z3j2yxw1R1ekJqrH85YQvpFg984aRS-c5fGO5Au757K--fzJo1lEy_MyywpPDbPWdD8004yfapdW_dPGeUddTqHCfrmd995JHf9RXS-BAUDdUbTQ74JGKotvcqTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها نوشته بودم بستن تنگه هرمز
علیه خودتون میشه و میشه تنگه احدتون!</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/farahmand_alipour/5838" target="_blank">📅 19:51 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5837">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl1IQSzyh5t4Kfzd8qw8Xn1vq1CclMF-gcjSVr-7cckqL88A0f4goDFjWWFGgbCJNrpabsz7q_eFrPXP6_CvRhhVofHBu8l_wluET52KBOVvEjdlFQf_x3QIbAgCKpSEI7eH7qvrPv7WUxte4tdAmbVB6PyTSD-lZ7nCftlvHiWkjfCGTUXEIpPs4nOG9uWcRdgKikA0GggupgSXbgezQjSLbfNu62D3bf4f42NNQ355BOM9Bg_k9_XoE2z8gcRZqlYe_N87RikvtTsnFLtsEnabWt9wDX4OkTCU3Ayu7dTPYBq9Gjp-Tgr73fMFJ1FP1-Dicrc45sQTgW5nKX6oxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند حتی حاضر نشدند «وزیر خارجه» شون رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5837" target="_blank">📅 19:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5836">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rrH6WK-cRd_VLFNY62SZWwCV2tBIhyqjPFyM6M9rnTh_qjx0ecbDn6SuvP4SKZ6zsPZ2uhZ66CaIGmA1Pm-AG2V3e6H3Z0d3GXVNQDvaFhzSbFTeramNZDPpldh7I4U4fQZZMoM4GGhfvjGse52XOQ1iG1_ZkD0lPXODe3Y31rmdb3PcN-W0JmqIlEhI3Vu032rK74b1R8_h7IRESBKow-4JdZLtnBLljZhhISLu5PMBDrTO242KgwBGP1XKtZ3Uc9ZIbYG0c3NaB5gYkmIze9PI4AgfS75vQ2oiNHL6jiiiXFUqxKcOPvQDUsFqkjQA7zzWjlv_1kB4dKz6C2_NXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روسیه، چین و هند
حتی حاضر نشدند «وزیر خارجه» شون
رو هم بفرستن برای مراسم ولی‌امر مسلمین.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5836" target="_blank">📅 19:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5835">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6prQ1uhG3vZfhyXmbRKr1iZTXe6_mjdOX2bH0Zx5GH-eAZNzvQwDBskrHAa5qZC5hwaQEI91xMDwN15nNRVEXBgrexW2PAebQtO3KdJnjj_wvFofnsVcs9s9I25UvnzR1pUzHzUFiXOiWCLumEznGVrtIJBHEWs1vzaBS9KDtMafNJytihzFwNAzvCPLjOpF6hGXzGjjPZEAhLB0Ds3YwR0P09wJGUgT8t_IDL-a1ncFfaaOEsqjzcnAHFcFqG3Dm_6w275p5HcH_Zr07Git6pb9hSVF0kHFOeXPh3aO-Yu8rhY8L3cCzbGDGjf75aLBRrODDRF4FUHd8Jt7fo3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">https://x.com/farahmandalipur/status/2072405978012844407?s=46</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/5835" target="_blank">📅 14:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5834">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDrbA0OttKZLExp-1p7FVzlUVzBSCIWKSxaeVe45OQOiiklwfG-7dxtgWI3_GZQLbPdW0VdvMDx1mqyL65IhucTUd9FY5zVBgQYG7ppy4JploFAb_c-mKtZLzL5Pr1npX7l7svgAbIlg-dorsqp8i6CNGs8cE6VHoPVVxfZSY55mtNv0QifEBCLOf-ObIL6nmznJBKV05nMzmkdUEL_XZUaY1aOEDD21HJgzhr8gWdfz26uuSzvG9ZspdOW2YKM8Jsb8XBHQc1K7tcpbm9uqMf8bPG_NTcGrmPzftghAbSP8e4EIqgAZE2ce1iYyV5qwIDjiVVwGgitaY_Bdw0y0Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/5834" target="_blank">📅 10:48 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5833">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iklufOKVouRa35O-vtoFro-F1XCmWr5lT53fPBQPMgdKvBVZkZnavpau-V4XPsK0Izi2xww7KsYa-FMQVDJP6gMg-xMN6FV1c0encOw2P6VbLdUXLezivJ8CEJ5qwBJN_FzhLuPEUOXzaPkNTgbkCjbdVx-efXD1aNu6cAJCRyt7E43Dki36CeFeWJWuleeyJpuSKTigIf9_q4kKvrLRRVEPk_QGlMRMD6ryXRGf6qUnMpVBeSLFuYeUGBZcDy6IazUmcm7bcNhU3h2l7oyWTKd-NxROeOysXaE8oBmMDFKPxrDm_d3SlwU0rBIyGQMTE0752n1TV8mWFwtOzFO6jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خود خامنه‌ای هم در اسفند ۸۴  یک سخنرانی در جمع روحانیون در آستانه محرم داشته و گفته که باید روی  «گریه» و «احساسات» و «عواطف» کار کرد!  و امر میکنه به «گریاندن»!  چون روی همین احساساته که به قول خامنه‌ای فضایی ایجاد میشه که بتوان خیلی از سیاست‌ها رو پیش برد!…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/5833" target="_blank">📅 10:42 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5831">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OXeGOoSAl6yK33mmmS1HqGu3EebRBybqpm1t5Itr8SLxW4kxNMfjpikmXAq3sPp89AbJ0AlQWQJ3RcDsgC3F_j7wpAE2EtduW06_FZS7uZ-d-gMj-I6YEhejnDOjRCWyj2VLL-ZSttfgW2DfS9WC1p30XftSFRZgLarIS2AR3vVJDbA_i3RuSVVwa3T64HFiTXggTI_7rVi-X6YX_jcm9wQVh53TQxc6xbl_A19z9vge7yq69k-GGwXdg5MSXxKH2piqB5DyKQcv8lXJjQf4uB3ZtdsFEbOjFZcz_CwQ52N7COOTQ3D3EHEHRqExjDoI0vxwiw_M2CnlioevwygwlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OKpd1neaoqsZLVBjd5UtikGwJxS8Ktjk5bg_QOA4sY_oS_swXapZ9wRHGYtMKvZGrwtRAu1dsdSDSkHoh2vbgDGKN7XCGHDmrurvrLunoNfgqfj7IoN8pFf7XSte6FZ6lPAfxJa8YoCzNrXhURdhklgCAuGVlDVMoMx667_kULpPauOpoEl-CUR5n5GQVzSl74O-F7Z4cidoNKNWOtdTjTt-MZH3mg3s43-k5n6W4YPfnw9-W5sE2wOVFS3uOHIO7ULeiqfTGlUbuMWwasJKVZPqtFDgRfD7Jxh6a_vvydOfkzpbOhy1IWe5hIXnR4uOXPdXnLPuKY-5uvKolPzjqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نکته دیگه اینکه خود صفویان،  از فرقه صوفیان خانقاه اردبیل بودن که در این فرقه یک «مرشد» داشتند که قزلباش‌ها، باید با «شور و احساسات بالا»  نسبت به مرشد حرف شنوی داشته باشن و اطاعت و‌ پیروی می‌کردن!   این کتاب «روضه الشهدا» برای صفویه خیلی خوب بود، چون شور…</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/5831" target="_blank">📅 10:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5830">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lX1451NGa_SnO8eca11iqqoSSF6kdPUQ_izcDtmQuMbFiAEDfSQnAo2K_bE4oo82bEjs4pc7Pn9Hjy7uoppMbUyxW8Y3MKyeF7yPKCbjidxS-_MIpjw27wMMZnjDFCNfd1Yz0FDRXapSwpnp4yltYjXLtP3ZKL4SNtHa0cDvw6KAeao8UiLyhZMzVWEfJeCiMsIg-zak-KKV079zoLPVPXcCbrN0LXB0SeR1jcu1mvx12Kmg9gfr0DXEbexuxqmsFeaPJHqpzttKKrpkEknnvFH8HrnJVh8TKJiVL-6bRqLplZZk_fqqFD_Ci0dJiW60iuLG1-C-E1Fba8nfeglbeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا صفویه به این کتاب «روضه الشهدا» اینقدر بها داد؟؟  ایران کشوری است که عمدتا در جغرافیای گرم و خشک واقع شده،  قحطی‌ها بسیار زیاد بود، فقر گسترده بود، جنگ و ناامنی بسیار! صفویه با گسترش شدید مناسک‌هایی مثل سوگواری  برای محرم و قمه‌زنی و گریه‌های شدید و…..…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5830" target="_blank">📅 10:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5829">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h9-BzgD2NJem7IaJvahv1_9OYdMWEhJKw2fIpkWeWsxZmBOIniFGjf8uJCBoyZhD5qxArGF_cIQ58BDsDwCKmsLqWkqTqX2yj9sdOgU-lKSDYsAtlnMSmUbWXrGrBksaQGT6A1OhSVBSdSBDNYTtvVMcbIG74EHOfES9QgEUzPXwPJLUn8pA7v_y1xdtX-zgRiZthjhgWlN5M_9qyCAb_665ulqSI9zH2pAw00aRgjG0Pw-KKB-ybue9ViKALXoNttreOBb0FxbNFBmperVXbD6kQcqtHEg00Y9_VZGQLqxoWNg3SJRDrmpUjMaU83pPgiBqZUbI8poVB2SCILPMhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با الگو گرفتن از صفویه و با پول نفت.  این خرافات رو تشدید هم کرد!  به «مداحی» و «مداحان» پر و بال داد!  بودجه‌های سنگین! تبلیغات گسترده از طریق رسانه‌ها از جمله صدا و سیما،  که این‌ مداحان با خوندن همین دروغ‌ها! احساسات رو به نفع حکومت مصادره کنن!…</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/5829" target="_blank">📅 10:06 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5828">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POqxfcaXFWJWIXohDeYkMf9lAX2NKh2eWbX42nus30bIafvyyvtO4OKMFYP3Bp6MpS3is3HAhbWsCue0lpZs1IvBfYWlaTYP1MqbKpDinY9vW3FEmqTF2qg6jNdYwkxCYUOogN5cvx4oPPKsPoUS7NXqYii4f-ywreKwSYLg5n83q8-qv5t8PR3hWnb2N8gXyWfoBrcYYTWWP4TCzbxRptZptM1gxOPGyX3IOIPHpabOeTnJBj8NVZWpGamTttJ1phWN0Akj5BCKHF7gvdrsqtYy9wZHE5mo4GKDS9ZQZ00Jwv8sbqMLtqdBFKjqUj_1QzoznA4rJ6kl_7DLgfBHQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرتضی مطهری در یک سخنرانی عمومی  کل این کتاب و داستان‌هاش رو «دروغ»  و افسانه خوند!  گفته از خودش نوشته شده!  کتابی که داستان‌هاش صدها ساله در ایران خونده میشه و براش گریه میکنن!!  کتابی که حکومت خرافه‌پرور صفوی عامدانه ترویجش کرد بین ایرانیان!  مرتضی مطهری…</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/5828" target="_blank">📅 09:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5827">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد  به نام «روضه الشهدا»  توسط «حسین واعظ کاشفی»  این کتاب عملا مبدا روضه خوانی  و ذکر مصیبت در ایران شد.  و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)  برگرفته از همین…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/5827" target="_blank">📅 09:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5826">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jkzxPOZr4fNXkwOeTZo8VFgI2ZeEL9zpSUCQ1oIazkSmtNYKFtE3SkZhSKPTlFxv3OtYcvP1L6YZ89gFI9Fd8Y4mLDcsAD9CdyJWrhBd0bhNYdRoNSNsvFYiwvbxPW5nLbh1b2CLHEWwEWMXCFOesrJTR4wB-rDX3GLwHwAUeccT8XWJCSDoDMvzhMPBI_I_OVAsANFyvQXrA_oXNIMhQjtL__fTqqvmAAGh0wvDT8qkE9GooNffBL4y4dUAGK-YYxnbIZhPQfRGk5m40AsWGMz3_GzZN2nzKSr4aOXpfGJwFVDFYY4XaB6Kc62sFvUG4o-reiBFKDV3hP_k9EIgcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در زمان صفویه کتابی منتشر شد
به نام «روضه الشهدا»
توسط «حسین واعظ کاشفی»
این کتاب عملا مبدا روضه خوانی
و ذکر مصیبت در ایران شد.
و اصطلاح «روضه» ، که امروزه برای ذکر مصیبت و گریه به کار میره (در حالی که اصل معنای واژه، به معنای بهشته)
برگرفته از همین کتابه!
حکومت صفویه خوندن این کتاب در همه مساجد و تکایا و….. گسترش داد.
بحث حدود ۴۰۰ سال پیشه.
(کتاب دو سال قبل از به قدرت رسیدن
شاه اسماعیل صفوی نوشته شده بود،
صفویه اون رو گسترش داد)</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/5826" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5825">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jUB2PhYkdXmhT2jH08KKTQ0Z6R2qlEmxi03TcD9YlbAH_9HX9j_DrF-NE61JTjYZwRcRvUXDzz9KD3NJp4bZa8Gh1bErCzmOzbH-9JL3VjDmiExwquNOP3hC02KrSaqs6AJMEnwjWmx2FQ8RVZFJo9KHpX14AQ4Lvo9C8-UCyEVqIHBXrRefXqRgTlvQr5Ghd4LXf_ihrdbpa_8UbaPHlARZ1_sbEsnGEWkzsLdQUJCtVyYZSEv9za8beBJFnp5VwsaqcRcZwoxiiBcDmMZP6e53-EJFeanMZPT3ORnbnMNr6TIlFaQwSec6fJOMKboO_5G7wrk6xx2f8XYKRqQhmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e54b01c817.mp4?token=jUB2PhYkdXmhT2jH08KKTQ0Z6R2qlEmxi03TcD9YlbAH_9HX9j_DrF-NE61JTjYZwRcRvUXDzz9KD3NJp4bZa8Gh1bErCzmOzbH-9JL3VjDmiExwquNOP3hC02KrSaqs6AJMEnwjWmx2FQ8RVZFJo9KHpX14AQ4Lvo9C8-UCyEVqIHBXrRefXqRgTlvQr5Ghd4LXf_ihrdbpa_8UbaPHlARZ1_sbEsnGEWkzsLdQUJCtVyYZSEv9za8beBJFnp5VwsaqcRcZwoxiiBcDmMZP6e53-EJFeanMZPT3ORnbnMNr6TIlFaQwSec6fJOMKboO_5G7wrk6xx2f8XYKRqQhmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روضه خوانی سحر امامی در شبکه خبر</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/5825" target="_blank">📅 09:09 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5824">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Yndq-nwgXUo86LMoUddGMA1qXENxpJoalAf2H0jYMRSsA5yxOnMrZJ--r7pyh-O_zbgAIrKre8Z3CO94_jxbZuoPeUY4yblM3fPNYYWja6jLbCyi0gPTVUmbDD506QKhPjhQfa7LyAR1kT7n403b6tVHvBJya9p491LQxd756wJnatpwY-KmdzjEZTAbVqYQhr-yqlSlGTNq78jd2wACWBOK7FL-YYbJwDPj0U0N5-3lc6lLpSJaW9cvQf35CoRotiFu6Rp64szQhcDuVH3C9zD4DnhQOxvuA4dtdE8lMSyQE_JmvPlKX5rJIzdnEmnqDU56W3CAH2KkwT0dgqR-cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43703b5179.mp4?token=Yndq-nwgXUo86LMoUddGMA1qXENxpJoalAf2H0jYMRSsA5yxOnMrZJ--r7pyh-O_zbgAIrKre8Z3CO94_jxbZuoPeUY4yblM3fPNYYWja6jLbCyi0gPTVUmbDD506QKhPjhQfa7LyAR1kT7n403b6tVHvBJya9p491LQxd756wJnatpwY-KmdzjEZTAbVqYQhr-yqlSlGTNq78jd2wACWBOK7FL-YYbJwDPj0U0N5-3lc6lLpSJaW9cvQf35CoRotiFu6Rp64szQhcDuVH3C9zD4DnhQOxvuA4dtdE8lMSyQE_JmvPlKX5rJIzdnEmnqDU56W3CAH2KkwT0dgqR-cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5824" target="_blank">📅 08:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5823">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d536abe797.mp4?token=XF_YC33u1oOY0FbQ0bQVUGxQqX64GYUJqS0_bvk5PQafwehn_DYhGGcas2MmItXiUZ0cJ0se2WgYPSHCxDdEzDbYrJ0zBN0e-JqvgX_pPtAkz0glX0ZvXQFfDM4nG7vlX2ofT2fzpENp8MeFkgIV75NzQyfG_pXnT7pMXLChy1vOKGhAUZo4L73G1UniV37C9kfM8hQDw-mMQYqBw8VIQNc0GrbHjTA9zz03a7E_nkURoGMYIQOaA26o2ZSWInrEe3Hx49IhYKSUgiPlxpjtiAh_ax4xwV6aPeQC176oI8BzxJHMAbX-kBQ3jlN3gXiemMNxRDcPFh_1ecHAQp4UJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d536abe797.mp4?token=XF_YC33u1oOY0FbQ0bQVUGxQqX64GYUJqS0_bvk5PQafwehn_DYhGGcas2MmItXiUZ0cJ0se2WgYPSHCxDdEzDbYrJ0zBN0e-JqvgX_pPtAkz0glX0ZvXQFfDM4nG7vlX2ofT2fzpENp8MeFkgIV75NzQyfG_pXnT7pMXLChy1vOKGhAUZo4L73G1UniV37C9kfM8hQDw-mMQYqBw8VIQNc0GrbHjTA9zz03a7E_nkURoGMYIQOaA26o2ZSWInrEe3Hx49IhYKSUgiPlxpjtiAh_ax4xwV6aPeQC176oI8BzxJHMAbX-kBQ3jlN3gXiemMNxRDcPFh_1ecHAQp4UJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم‌ سوال کننده، هم‌ این خانم مصری
برای مثال زدن از کشورهای افراطی
و عقب افتاده اسلامی از «ایران،
افغانستان و پاکستان» مثال میزنن.
حاصل هم دستی آخوندهای شیعه و چپ‌های ضد غرب برای ایران.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/5823" target="_blank">📅 22:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5822">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XaJyi6ItXTwKXzwh9Djb6kzePAPz-JIIHsNrpw9pP7ZsWhxJw_411faVEusNztWw2_Th3eootekUGp6kQhEATsc0_YiJWQCO_N-x4x10gh7W6ElIfVSb6_mO5P95pjdvWgK6vsRkB4CoAKTUQsrWTcXpYvpCW1UPe8gRWazwnCdpyWdoEJ-3xrj8VLOYmNZrhbsxIb4XKvNaRM5uDMGY6QrmWkHpmb9yLww32e0Kiw0T_SWouYRoQELFEhr0d0fFe4MpSs97rakhoxSGo6bgHTrUwVRDhIDe7SNLk8zg1kNmH_VtgqXkjv8-oB-llCyJJ0Tio9iyQRor19WwPXARew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad33cb95d6.mp4?token=XaJyi6ItXTwKXzwh9Djb6kzePAPz-JIIHsNrpw9pP7ZsWhxJw_411faVEusNztWw2_Th3eootekUGp6kQhEATsc0_YiJWQCO_N-x4x10gh7W6ElIfVSb6_mO5P95pjdvWgK6vsRkB4CoAKTUQsrWTcXpYvpCW1UPe8gRWazwnCdpyWdoEJ-3xrj8VLOYmNZrhbsxIb4XKvNaRM5uDMGY6QrmWkHpmb9yLww32e0Kiw0T_SWouYRoQELFEhr0d0fFe4MpSs97rakhoxSGo6bgHTrUwVRDhIDe7SNLk8zg1kNmH_VtgqXkjv8-oB-llCyJJ0Tio9iyQRor19WwPXARew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف راست رو از این خانم بشنوید که میگه بعد از انتشار خبر کشته شدن خامنه‌ای مردم در‌کوچه و خیابان‌های تهران کل میکشیدن و‌ دست می‌زدن.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/5822" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5821">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=MIMzJzUP5N4I2szBqd4bf7uDmaYiOen85msVPtC1554psmJLh62y0J9MA6CAW9B0VoANZ5-jbb5cnPSsfy8KXJyBDt6gwaopg1hWi13kAIsQK5zYe3m0Lkno3lqheZmOM0GwGfcMe2Z-90DQTPPN437cLkJwka0y2ugV2XiYIyQMXRa5tGRbZLJ2rnIdaN36gfF9OqJBFaLer26F50WqfJ1U3siLPSQrRBd9jRU982pMOunbmcwl1_OnuaYyOp9sGC04wRLyWKX8tf0bV6dSmqfD1uBpRcoNjPcLrK2PadAI3FuVNB-ipDLGRecpELD5wO5J06Bi1AVo30V7zPX-0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22e78d39b.mp4?token=MIMzJzUP5N4I2szBqd4bf7uDmaYiOen85msVPtC1554psmJLh62y0J9MA6CAW9B0VoANZ5-jbb5cnPSsfy8KXJyBDt6gwaopg1hWi13kAIsQK5zYe3m0Lkno3lqheZmOM0GwGfcMe2Z-90DQTPPN437cLkJwka0y2ugV2XiYIyQMXRa5tGRbZLJ2rnIdaN36gfF9OqJBFaLer26F50WqfJ1U3siLPSQrRBd9jRU982pMOunbmcwl1_OnuaYyOp9sGC04wRLyWKX8tf0bV6dSmqfD1uBpRcoNjPcLrK2PadAI3FuVNB-ipDLGRecpELD5wO5J06Bi1AVo30V7zPX-0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن  ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/5821" target="_blank">📅 21:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5820">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=cDabdSz7W4eydrnvB6aN6PnWQEh81XdHb51IFROwJsOtUmDX3_9wUWkWzRj2tMjjldVS8SXWLKXtOsiaROlNrC6Qk9uelAcjFt0D_-aFssgJRE1bdQKmq469trWyKFAkftbueo2n0PeoI5uu0tQSRC7Hb4ngQ8alcYbvfryAINjmqUNi6y2WQDe0fDqyOUvHObf4UWL0alcqxQ1aagLBSNjasingvwxrbTNisnwDN-GO_JTlMfBwgUgE7SUseTWTiMZhRQ3lnLB0qSJuUD5itkkr1-Vfz2jYKePU1Du-W6NsnZGEBJnHRzsMq73jl0VhPAvQavckMvpwpCFScIDOvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/256cc521e9.mp4?token=cDabdSz7W4eydrnvB6aN6PnWQEh81XdHb51IFROwJsOtUmDX3_9wUWkWzRj2tMjjldVS8SXWLKXtOsiaROlNrC6Qk9uelAcjFt0D_-aFssgJRE1bdQKmq469trWyKFAkftbueo2n0PeoI5uu0tQSRC7Hb4ngQ8alcYbvfryAINjmqUNi6y2WQDe0fDqyOUvHObf4UWL0alcqxQ1aagLBSNjasingvwxrbTNisnwDN-GO_JTlMfBwgUgE7SUseTWTiMZhRQ3lnLB0qSJuUD5itkkr1-Vfz2jYKePU1Du-W6NsnZGEBJnHRzsMq73jl0VhPAvQavckMvpwpCFScIDOvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میگه خامنه‌ای وقتی کشته شد امتش ریختن توی خیابون بر سر و صورت میزدن
ولی دروغ میگه :)</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5820" target="_blank">📅 21:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5819">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=m4k8qS20fZj8UQwSMf3j5Ahwid-Jk7a8xGYJVlig-a9Gb-Z7DkgFgrLCizAydWpq9Nq0ckqpexATaQLqgODlbMvwD3Apq3kIR4HaXN_K1-DMPf8vVLwwIpGVn5Aefy_S1g6athoRTsqdYTA5E5x-jZrtaPd13MQvG8AQP7QEDukCREtTzjZr2hGLICyfxMctMuQfxzF0oLitDoVo22jBZlMN93tCrGIZvZnQ7xtJb8xfm0JXPNXqtWP4ttAPeBhEf4LOccG7SDhcUVvm6qDfrzU7YeCFaZCbiocx5NbDLyLD29__W9PQ9ZKj87xEE3iM8_tUsDLj2QT0fcfnK0OfjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed6be978db.mp4?token=m4k8qS20fZj8UQwSMf3j5Ahwid-Jk7a8xGYJVlig-a9Gb-Z7DkgFgrLCizAydWpq9Nq0ckqpexATaQLqgODlbMvwD3Apq3kIR4HaXN_K1-DMPf8vVLwwIpGVn5Aefy_S1g6athoRTsqdYTA5E5x-jZrtaPd13MQvG8AQP7QEDukCREtTzjZr2hGLICyfxMctMuQfxzF0oLitDoVo22jBZlMN93tCrGIZvZnQ7xtJb8xfm0JXPNXqtWP4ttAPeBhEf4LOccG7SDhcUVvm6qDfrzU7YeCFaZCbiocx5NbDLyLD29__W9PQ9ZKj87xEE3iM8_tUsDLj2QT0fcfnK0OfjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به امید شکست و تحقیر یک به یکتون!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5819" target="_blank">📅 20:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5818">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iVD-uamCOfFMXcJP4OSbhr-J6wpwiX2W-Y0wwiM-djXi2tKKNL6Uq8OqLVcMB76YqRJZBGICyip6I6RLcJLyguQctSRXlATlKrUzRbnKrhIGsr4dNJCQXs3WEujAOp5-LkHEZx-Pi6knZQCD03IO4hLB8TshxhpMWQis-eI9oB-XILgHT13iqJQBULuTiMIz4kC3DASUfIhfQCLBm-ggSKg3g4SoX9t59x_bHLmSYOUuhk1vFJeQ2tJBA-SoFmsNnIHKIJtoe8t-DzLdFj8uJU8QfJ-zDADUbfZgRNos4GuHHWeI-CT7kl7Kwd5Cv8nXPfaV8bDJW4YbVUXEEtQCsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5818" target="_blank">📅 17:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5817">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7862dff401.mp4?token=HbefprtoDRyNd-Fo3uv1pJEqKtAsSHEIIgFC3kEXGeZ2rfmQ6DzN4DlcN2xvIwtUtdoCmwcUAVFC9OO-U3a65z0PjWOs2n5vESC6KiXrc1zJZf60Si5pY75vJ9K6nfpxPmdWCiVrLYR4EWuUu3VZ_mc6hE1HfQJ67tkTMrQpvyxN5A_lmL0FxyVEXtsUWu0NgDF9hgYK50EwjHdDVWffzgi44FscveVNxnjSOd5OnBYre7I6UW-FcHA3a3niwYEsT9SsXSM0UeWx3ErsRNahczStr7O3zhiwYmLX7uJn2sDQxdb0GwiC-A18nSwy9gHjbIhIudnoq-VK4gsmp1JIlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7862dff401.mp4?token=HbefprtoDRyNd-Fo3uv1pJEqKtAsSHEIIgFC3kEXGeZ2rfmQ6DzN4DlcN2xvIwtUtdoCmwcUAVFC9OO-U3a65z0PjWOs2n5vESC6KiXrc1zJZf60Si5pY75vJ9K6nfpxPmdWCiVrLYR4EWuUu3VZ_mc6hE1HfQJ67tkTMrQpvyxN5A_lmL0FxyVEXtsUWu0NgDF9hgYK50EwjHdDVWffzgi44FscveVNxnjSOd5OnBYre7I6UW-FcHA3a3niwYEsT9SsXSM0UeWx3ErsRNahczStr7O3zhiwYmLX7uJn2sDQxdb0GwiC-A18nSwy9gHjbIhIudnoq-VK4gsmp1JIlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،  بازارها و مخازن رو از نفت پر کنه،  و بازار سهام و اقتصاد رو درست کنه بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5817" target="_blank">📅 16:36 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5816">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=kj2syHY2eeccPzzxoCkrjq2XCUKaf4B68Wv0q9kMAyTGyhoPUir-JGJ2YZUGyEVYLXdKshpGv5CccpyCfMES8yUvT4p7RSK49daNTRt12QD-v4ff3tx_Ct2ZFivh85F_BV_HHwsXWCifIpk9fDw632AON9MF0yfFLUcxQ3ZU-RZR04SfWqoloJ2o4VCdpqUZccyHmmHxahQ6qRJN83SsKDgPR1IQ55bkJ4Xlw22ocNMMLifMAJylSZ7NCnof4zsJjtYpsst0KR_K9YpgVdV8vTn1mH8DjkpMmyYr91gT9p8_BY0hz3SCKnFzKOoiVuhYPLS__ao_b7hm39awuQsIjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f9a10fc62.mp4?token=kj2syHY2eeccPzzxoCkrjq2XCUKaf4B68Wv0q9kMAyTGyhoPUir-JGJ2YZUGyEVYLXdKshpGv5CccpyCfMES8yUvT4p7RSK49daNTRt12QD-v4ff3tx_Ct2ZFivh85F_BV_HHwsXWCifIpk9fDw632AON9MF0yfFLUcxQ3ZU-RZR04SfWqoloJ2o4VCdpqUZccyHmmHxahQ6qRJN83SsKDgPR1IQ55bkJ4Xlw22ocNMMLifMAJylSZ7NCnof4zsJjtYpsst0KR_K9YpgVdV8vTn1mH8DjkpMmyYr91gT9p8_BY0hz3SCKnFzKOoiVuhYPLS__ao_b7hm39awuQsIjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی‌دی‌ونس میگه ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی،
بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/5816" target="_blank">📅 16:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5815">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🚨
نتانیاهو : اگه نیاز باشه به تنهایی و برای سومین بار به جمهوری اسلامی حمله خواهیم کرد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/5815" target="_blank">📅 00:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5814">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=abIni7gXJhjqxRKO-rA5Fg7_FjsidowQCFlrYuc2GairsKL2pprp_nPNuT0LQLpW6U1mXg5LP5i64Cz8DGAuJvxfBJE4F01x_ky_6zmv05Mx7bDh_WLA2csfL7nHHXtQFyzoU-hLYPvxZuB784o3tLEmB1rpLdWKk_ISDTPMFbeWpiP7BIIcLT8yGcu2TG60oBhhEsI53hMefTBGXzvE0708ji_dMHd2EkuvIejiuKbSA-_BxRPDYI06oymJWpx798g8lkfLzPRkJKtXlt5kYOV4cctrMv8_mVZ0zDFxQbBq9mxyrioO1XgN66BV6XL86cn_Dov2yla9Ka-o9TQ-0pNQnFnL6W8KtKPuLpRnH42e7cUfSCnOFup444Dfx66vdEPTP-l2kkVvZ9fMwhY8humiqcL8okTLQjanm9IDM3aEZiVT11tF0Ply3rFFoFx8RU4xfkiFXb8HyvzDAOVTLPsoVCWqGnxO263gsz8UCOmuql9XTIE-Pwid87_D0yJoHnzzWMkSURMIXGRNT3AZF5g1Il3pe0ZJjoSf2VZyCDV1V7b2gatjQMakYs1TKdUj5Kz6SBOA-WPpv0UHzLFglby7EDgi71kA8XO5KwETWEo1ot_52fsy6zobaYe2DnbtekMPLUprYTVR682WBaaWp1XEKNhh3pV1gF7JoZLYDAs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c1fdbeee.mp4?token=abIni7gXJhjqxRKO-rA5Fg7_FjsidowQCFlrYuc2GairsKL2pprp_nPNuT0LQLpW6U1mXg5LP5i64Cz8DGAuJvxfBJE4F01x_ky_6zmv05Mx7bDh_WLA2csfL7nHHXtQFyzoU-hLYPvxZuB784o3tLEmB1rpLdWKk_ISDTPMFbeWpiP7BIIcLT8yGcu2TG60oBhhEsI53hMefTBGXzvE0708ji_dMHd2EkuvIejiuKbSA-_BxRPDYI06oymJWpx798g8lkfLzPRkJKtXlt5kYOV4cctrMv8_mVZ0zDFxQbBq9mxyrioO1XgN66BV6XL86cn_Dov2yla9Ka-o9TQ-0pNQnFnL6W8KtKPuLpRnH42e7cUfSCnOFup444Dfx66vdEPTP-l2kkVvZ9fMwhY8humiqcL8okTLQjanm9IDM3aEZiVT11tF0Ply3rFFoFx8RU4xfkiFXb8HyvzDAOVTLPsoVCWqGnxO263gsz8UCOmuql9XTIE-Pwid87_D0yJoHnzzWMkSURMIXGRNT3AZF5g1Il3pe0ZJjoSf2VZyCDV1V7b2gatjQMakYs1TKdUj5Kz6SBOA-WPpv0UHzLFglby7EDgi71kA8XO5KwETWEo1ot_52fsy6zobaYe2DnbtekMPLUprYTVR682WBaaWp1XEKNhh3pV1gF7JoZLYDAs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا جنوب لبنان سقوط کرده؟
چرا ۱۱ هزار ساختمان صاف شده؟
چون رفتن دنبال «خونخواهی خامنه‌ای»!
به قول خودتون چون «پای نظام» شما ایستادند! به خاطر افکار شما!
خواستید جنگ راه نندازید!
یک میلیون شیعه ۴ ماهه آواره شدن!
شکست‌هاتون بیشتر و سنگین‌تر!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/5814" target="_blank">📅 17:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5813">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=pU4Po_LBITtngmqHk8xvLrJ4qk4l9caiNrJHixjwXwEvQwhIYm4SlYDx0MYhTFnilJFiNebl6PPBsChjLrlc27vrgx7Uwib7gEVmHI8MOjhD9VYzg8Jw6cTNHQnyXBP_E3AHx8ppA2sacwfMpCFzWqBt-rahsaL8CkjeYX4egBIeLpNrupWACo-wgLEZ8a7_IXPYcIwfa9bNwrwN6lgmAf-S4j_lcpdvXXNSE9EytkQejlBPOzepDMg32uLcM32SyLrNoFowdzbpia6sJQitmHAK__zAo6fNnV4xQBiy5qy4xsEzqLwk2sc0vEJ6w_Tzq0bJdgQJvOf00uzweDKk_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a28a5f6ff.mp4?token=pU4Po_LBITtngmqHk8xvLrJ4qk4l9caiNrJHixjwXwEvQwhIYm4SlYDx0MYhTFnilJFiNebl6PPBsChjLrlc27vrgx7Uwib7gEVmHI8MOjhD9VYzg8Jw6cTNHQnyXBP_E3AHx8ppA2sacwfMpCFzWqBt-rahsaL8CkjeYX4egBIeLpNrupWACo-wgLEZ8a7_IXPYcIwfa9bNwrwN6lgmAf-S4j_lcpdvXXNSE9EytkQejlBPOzepDMg32uLcM32SyLrNoFowdzbpia6sJQitmHAK__zAo6fNnV4xQBiy5qy4xsEzqLwk2sc0vEJ6w_Tzq0bJdgQJvOf00uzweDKk_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه تروریستی حماس
در شهر رفح در نوار غزه یک تونل ساخته به طول ۱۶ کیلومتر!
تقریبا به طول خط دو متروی تهران!
که این تونل از طریق خونه‌ها و مدارس
به سطح زمین ارتباط دارند.
این یکی از تونل‌هاست!
خود گروه تروریستی حماس سال ۲۰۲۱ ادعا کرده بود که ۳۶۰ کیلومتر تونل ساخته!
این همه پول رو صرف ساخت تونل و موشک و
اسلحه و….. کردن که مثلا مبارزه کنن!
میارزه هم کردن و نابود شدن و ۷۰٪ خاکشون رو هم‌از دست دادن! می‌تونست صرف مدرسه و دانشگاه و بیمارستان و غذا بشه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5813" target="_blank">📅 17:53 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5812">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pGQYy6d8zwGjza-EMpCcC4VVeJR2JmlfNzn8SE1rWWJNtBPhOVRj0W40TInlKeHL9wyqng8ONbVyP7Pdfbz-uJKhSTMDCwHcWvEgSiZuDpPpjil1cr8Etkm64OyvJlcXm0vjMpgue-lE955ktpOYVh6KuRbgO70Wok1byD4vY0NdH5t6a3W3m6DYa18T38CHweASPqnXK27cva4akqwJm5DQ-XyK6FAt3MbUvJtT1bLkNGyX_a56Phh9fxSVfJJFteVQxQ9N91wgs0QIYJUCtUrW5PtY318lMaRK-KVHow-cthVNf79rHB8MyV09VaZc3DFRTFoZVS3iEjyl5q4o2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/085c31b1b8.mp4?token=pGQYy6d8zwGjza-EMpCcC4VVeJR2JmlfNzn8SE1rWWJNtBPhOVRj0W40TInlKeHL9wyqng8ONbVyP7Pdfbz-uJKhSTMDCwHcWvEgSiZuDpPpjil1cr8Etkm64OyvJlcXm0vjMpgue-lE955ktpOYVh6KuRbgO70Wok1byD4vY0NdH5t6a3W3m6DYa18T38CHweASPqnXK27cva4akqwJm5DQ-XyK6FAt3MbUvJtT1bLkNGyX_a56Phh9fxSVfJJFteVQxQ9N91wgs0QIYJUCtUrW5PtY318lMaRK-KVHow-cthVNf79rHB8MyV09VaZc3DFRTFoZVS3iEjyl5q4o2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد اکبرزاده،
‏ معاون سیاسی نیروی دریایی سپاه،
‏شب گذشته در یک سانحه رانندگی ساعاتی پیش کشته شد.
او در یکی از اجتماعات حکومتی به صراحت گفته بود حملات آمریکا «واکنش» بودند! یعنی ما حمله کردیم و آمریکا پاسخ داده.
جنگ‌هاشون در لبنان و فلسطین هم همینه! حمله می‌کنن، وقتی جوابشون رو میدن میگن ما در حال دفاع هستیم!
۴۷ سال گنده گویی کردند و سرمایه گذاری روی تروریست‌ها و وعده جنگ و… تا بهشون حمله کردن، گفتن ما مظلومینم و داشتیم ماست‌مون رو می‌خوردیم که مورد حمله قرار گرفتیم!</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5812" target="_blank">📅 14:57 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5810">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoNB4BdtkoQLqrWS3GXhA__HVQLGqkKpePzqxHPctD0h3gB4W309Vh9l-5ScTZNwb1Id-cBjDAbKHW79NQeHlbSq3EEqVKqqW-szizR68BjqMUV8otaMASPw3OwK_6COXJQf9sSal6r0CfPFCeYJk9W3iymyE3vtquseQIUF4jpOFUYcVmIw34E2WSLT3XBwxw3f4OqMgtgYuXKPvEl33WNxobt0sTeP_SJH_qNUBAq5rfF3x0zV-R7bYTFb__jWEURrqRY3emZEgELy8fCcrTTWdOppemKTn7gx4H73bGGbuCWNItA4OiDIxNM8CpiuzsZh8gGGJOxLZpZK8s-CKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J9_d17HMsi0CB_-8G5Qj2tdojqMn4ZWoGhveinZpRifKHnZpiPuVs1hzSY5uKdxSCGMdWEGX75xTemx1-0f-AMQ-QjclnKVIY3ynlX5Zhldu-1226AlD3goz6MzBEFGaYCnkpW4BBe9YN6sbHRoFJ_Ylj1tCutLSfqpgKUnlj94jGuHQZEr64pi4Bivt8DHw6fBsc7vowLIR1EdBymWKv3MQP0b9NxMYWEqGcG3N-_RFScyt0kjdrwmbBWRRfOvWjJj6GNKQaKU6WuN3imv4ika325ouMWbjjxcyMrDYv7g2OVOHAdGRpXXH2y3AnjC1gm8OMAvA5eepQiAvIfcJzg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ده‌ها تن‌ از‌ سران و مقامات عراقی بازداشت شدند. از خونه‌هاشون میلیاردها دلار پول نفت و طلا  پیدا شده!
خیلی هاشون از نزدیکان جمهوری اسلامی هستن.
با تصویر خامنه‌ای و سلیمانی و سیستانی در خونه‌هاشون و سوتین و شرت طلا!</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5810" target="_blank">📅 13:32 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5809">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=UKcX0inMKbljg6G0qoabqChhl18wkvI29KuZG6FvHE1NA24xYeieBsnm5lJFGavWPMr1MTLDvMcIF5kY45c31QMX58uGccCar6tO2GfibHykrt4bi1m4sMLQVwDq4YUTxLFQB6_vqKnr00b09rnx-632nGL_mTI1TWh3rCI2deYJtRsUSU7n455Gf_m6wGA6W9JrbNzD-kN2APmGmsfmmFRBuqGeLLksNwz16MIRoEToLVhIJwKmeJUkGT9pM0qA6dyoPcNkNaZTXLBlpYTYwdh9TTE4osI_4xpruJl8C95iqyJMSfQRusitmFMRXZN8a7KupfFRHIXLlv6orvVK3AlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee0be552a1.mp4?token=UKcX0inMKbljg6G0qoabqChhl18wkvI29KuZG6FvHE1NA24xYeieBsnm5lJFGavWPMr1MTLDvMcIF5kY45c31QMX58uGccCar6tO2GfibHykrt4bi1m4sMLQVwDq4YUTxLFQB6_vqKnr00b09rnx-632nGL_mTI1TWh3rCI2deYJtRsUSU7n455Gf_m6wGA6W9JrbNzD-kN2APmGmsfmmFRBuqGeLLksNwz16MIRoEToLVhIJwKmeJUkGT9pM0qA6dyoPcNkNaZTXLBlpYTYwdh9TTE4osI_4xpruJl8C95iqyJMSfQRusitmFMRXZN8a7KupfFRHIXLlv6orvVK3AlVU3kBH5by2wQGqoGijtfIqqzBZBESN2WyBEFuU8VoCd4xOXlVmcb7WsU1TQPG7RnJCpFeXzHPTuTSGhGZY9r69VIynfNPvuEBqlyKC25ynuPFdPenuE_Nz0IgwiK8nHH1UJukSzhmSfHXsUvB_t_MGUQWLTZHp64dOpcADtxLkxrFTBuOuc9E5XCnssc8_b8VBAxoi-68nIUB2Suvwd-H4Ag1K0uTykf7f5nOcT7Vz4vucxX_cristFYfLx9d4PuLgtHs9XIzr2BNeCXzxQthx6RmfxXpgiZ73E5TJUCnvP7mYOXri5vIKedDRt-XiXNkRSo6AAkFb_zdLDR9W1M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیش از این‌ها تحقیر بشید !
چه در ایران، چه  در لبنان، چه در فلسطین،
چه  در دریا ، چه  در آسمون!
در ضمن بهتون دینار و درهم نمیدن!
قراره یونجه بهتون بدن و پولش رو هم بگیرن!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/5809" target="_blank">📅 12:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5808">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cxl1cz1aX8y_TOiGiPLVG1Ck6GbWecilHSIJ7LTIrQs3V51iXPn6RxqZ10hFFXstgBvH9iFnyAxpYPWp5rxkxrCNj5XyR0fLKbsB7n8X_4Fwv2zejY9PybJg-76lOglWmnegxKcfY-IOXW_cIeS0zTvJKS3Nk5Yo7bKeESuZEH8PqIabwh7S0aSi5QSRkWk-d_PNWDkpX7VoKlry1xtgDJX1CQV9jxcD2dyHMIwFDJGU8ixsjeTvUD7NI8h5Us3VIK4PwolDNdEbiUfwmpBHraEcvopq0x-9BdoYmLEyfmyv6dYOe8IrymYwFpNonVc8LjjAbMScfZMwKngBhVTnfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مقبره رهبر مستضعفین! که در زمان حکومت خامنه‌ایِ ساده زیست! ساخته شد،  با مقبره فرعون‌های ظالم!  که به قیمت و نرخ امروزه، مقبره خمینی ۲ برابر مقبره‌های فرعون هزینه برده!  ولی عرزشی که نمی‌فهمه! بهش میگن رهبرت ساده زیسته خیار نمیخورده، خوشحال میشه! دیگه بقیه‌اش…</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/5808" target="_blank">📅 12:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5806">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mtctlL-jj0dzZwG-P76r_camnvlC8pRKEONVGi0-BtMJ2inDSOJTfLF_KWv4XAOd7rmXF-6r8pasWJ_fFfXqwQ1Dy9pNoPJS_v0_Co9u6M-0ztUXHudph960Kv-xBlqz_2ECnItjwqUJjVIkKMZsGpz18w0PEZ5uNbyXjMBV2K2zv82v69dazg14wHVvjfxW3RsNk28NyMcWpnFRGe7CUdTJeI9kNhGBTQ5Azks5xZp7-YN8gaK1gg1v8ldB7lUmUqwi-xRYHKE0okdWeMjXvHGMKB5eQgGkP2cw0QPm_6NGT-NkMA9OrrAPoHeBRHQzV9RqA0CNJz22fHHUQLdtFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e5a8VKOhxDCwErfz5q97tD9BpWMuFmFmegypwx0VogBzUN2Y-Mp5QsmHMglKNmlRqEWS5Po_Aq0TGd8O6eQmVZdvZdt3m4n6actJWsRkOUnxtd9G1sAWMBRt-0EHruVNfYmFcnBK9dc2mx280gNbo6xwCkkcE1V7CALUcEVwqTH-si-njD_I_Gvxrk7w677ybM8vdd6g-uHyFrZxOSjiOToQb1vnaqX7bNYzIOWfjFFsODupU3BEOAFmUjATviqRSr-1yvyVrmJo6X7rACfwrwxmF47-pAZIVOGBvShvrmH2cYMBZ5AU-bPCl-EcSKthcrIGSu4JbGzaxH2pH8mc7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،  ۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!  اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!  این فقط یک قلم از این هزینه هاست!!  ولی خب رهبرشون «ساده زیسته»!  خیار و هندونه…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5806" target="_blank">📅 12:35 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5805">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sm-0q3lrUbneXrHSiT-VXLSIm1eaNttRG-FzWfZwttgBpMtf0He8kYWqUCJzLIG9eFJA3MLi5lNbASk9hpmD9cZRhtjgS6EBQi2NY6ScueUeuEesY5xagQmmVRkH5o7OX4SfFjGA3WgwT39rHpy1cOuK2-bdYqmxFsOsO0seTL6oL90HvqdB102gtsIBnQ584vIlT1H-2QOg8W6YI69ppi8qCDeT7MLpCkNJFzL6BBQA8owqNHdHkVk3rQMuc7LFo9VShg1bupUrWBrOsi1HsMz4iwH0TDSIoL-bXJXGUROdyrUYpXj-byYLcPQOFC9l-xw-1z2ziH2Gnz0VCcFA9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه هر روز تعطیلی تهران،
۲۴۰۰ میلیارد تومن خسارت به اقتصاد کشوره!
اینها فقط ۳ روز برای خامنه‌ای تعطیلش کردن! یعنی فقط این تعطیلات ۷۲۰۰ میلیارد تومن خسارت به اقتصاد میزنه!
این فقط یک قلم از این هزینه هاست!!
ولی خب رهبرشون «ساده زیسته»!
خیار و هندونه نمیخورد!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/5805" target="_blank">📅 12:29 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5804">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=BVOT3NDo5qzRC76zwBSeefo1BCgJbQVJ8x9qE6lZOGR4ZgV6pvibdceGrMlSv-84OOuQPGWgnpRZRKGsO2DDm6-Zs_U2pi411AG3zOgEq0CTxy18ko2UIAXFTAVaXvBRVCEd7Ch-YODgLxQk4BQlUL9LQdhh7-00qR27Vi_UFSJy980uHd4H21U9nzZ1V7niMvBUyz_50mUukPuew_cppZywIJQFtcAIYchWLws265IaMh62nXjLmyiFu-8VGU5irsHHHn0IZzqZi9gUXhRwNtyG_zQMQ3h8M3bJ1HkuzmkaxH3i8L1OAJudhqCytGgP840bCNFEu37pbgbMjHC1yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b7a3755d2.mp4?token=BVOT3NDo5qzRC76zwBSeefo1BCgJbQVJ8x9qE6lZOGR4ZgV6pvibdceGrMlSv-84OOuQPGWgnpRZRKGsO2DDm6-Zs_U2pi411AG3zOgEq0CTxy18ko2UIAXFTAVaXvBRVCEd7Ch-YODgLxQk4BQlUL9LQdhh7-00qR27Vi_UFSJy980uHd4H21U9nzZ1V7niMvBUyz_50mUukPuew_cppZywIJQFtcAIYchWLws265IaMh62nXjLmyiFu-8VGU5irsHHHn0IZzqZi9gUXhRwNtyG_zQMQ3h8M3bJ1HkuzmkaxH3i8L1OAJudhqCytGgP840bCNFEu37pbgbMjHC1yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»  در شهر بلونیا در ایتالیا  که ۵۰ شب در طول تابستان برگزار می‌شود.   (در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5804" target="_blank">📅 11:16 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5800">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=UnSkCnLn6CjN8fdkI7K6W3QAf4K8o33yv5ffr5ISFEFf1G8XnyBELyyyJ-hV-dTDdiZpEdf2yKH4zMJZkh_Pv90a9peHV6-0FXJ2zwCZHiVtJanbXkFQttwNQoxmpdvrsmaGXu7mltNvX87twJ8J1dAZxm7tJaXQoM4zbz350-_-2VCg3cULFGejJW4mKHB8KyQNsHlLeuC-7wIjqhKHMgeWuU8_fMYuyH0P6x3e4inipjpYnw2fdqgzX-Vqu-J_vXWxmyyCcw-iJmVafjM3YYzde5JCrYkXEQw8ZLwH948mrqMQ8mLsbyafXji_RbB4H1U4umy4fgxNlY-ttTliYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf427145cc.mp4?token=UnSkCnLn6CjN8fdkI7K6W3QAf4K8o33yv5ffr5ISFEFf1G8XnyBELyyyJ-hV-dTDdiZpEdf2yKH4zMJZkh_Pv90a9peHV6-0FXJ2zwCZHiVtJanbXkFQttwNQoxmpdvrsmaGXu7mltNvX87twJ8J1dAZxm7tJaXQoM4zbz350-_-2VCg3cULFGejJW4mKHB8KyQNsHlLeuC-7wIjqhKHMgeWuU8_fMYuyH0P6x3e4inipjpYnw2fdqgzX-Vqu-J_vXWxmyyCcw-iJmVafjM3YYzde5JCrYkXEQw8ZLwH948mrqMQ8mLsbyafXji_RbB4H1U4umy4fgxNlY-ttTliYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه «زیر آسمان ستارگان سینما»
در شهر بلونیا در ایتالیا
که ۵۰ شب در طول تابستان برگزار می‌شود.
(در عنوان برنامه در استوری اشتباه کلمه سینما جا افتاده بود)</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5800" target="_blank">📅 10:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5799">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ti0ZhUO8CoQNQffwIPDwmowR5SAUKw40qoCf3nWfZbpK60S4yl700DC2qSw87-rOqOJ765vS3bQqDFVS6-1KnqW7e9lTyVYWcG_uUxoy9yGMqDx06VLp5ndGLD_K0UXP1YAhEQHt2BXReSf6mVTE79Vj1HwR2fmw0NLGnWvNM2qaFkpLpljpvCg6PCtx1esUa7LBuUHtzzjuCqLafjUseI9M9UgHrwF3F_0Y1dGba5Q8a0sta4_Jkjhu9pK09-gumN5Ji_jhiAS9qpFtOLvCbDQYcw9tljqunUWJnNpkCoE2XAlVHAsedsY2RG4kV4GHperWVkQr0lS_rVl2_f1VeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!  اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!  درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!  یادآوری : هزینه جشن‌های ۲۵۰۰ ساله،…</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5799" target="_blank">📅 09:26 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5798">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=F9o4tf11y5BDVKjdKRubBPs4mWI6RQYyxFtNynLEMFE9o4qXdswyaONWnyaHvu1Y5nqqQGZg3sxsiFG23GypDEbw_-wSDG_g9T4BOLXFr3BRSvCvypxc0j2fxls1iNluLubCkzEtK9Ru-1-1bjl27EGAjaWUpv_IHBYYTee2XVuouBF5DahdXkXs66su-VtcDrVlqq8wG8el9_C17s6Z2xzAXTnRasjpYs0cjAcOBvrIKJxEyPfxXAJG-hL_0lOC4iQizMCtBw3fHsZ-RtC1h9cWgBFMzKh0ligo0iIRjqZaroCDFo-iWkPiXjjDYvQOLIlCwwkQhSLE7ibIyihLhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc44e27bf.mp4?token=F9o4tf11y5BDVKjdKRubBPs4mWI6RQYyxFtNynLEMFE9o4qXdswyaONWnyaHvu1Y5nqqQGZg3sxsiFG23GypDEbw_-wSDG_g9T4BOLXFr3BRSvCvypxc0j2fxls1iNluLubCkzEtK9Ru-1-1bjl27EGAjaWUpv_IHBYYTee2XVuouBF5DahdXkXs66su-VtcDrVlqq8wG8el9_C17s6Z2xzAXTnRasjpYs0cjAcOBvrIKJxEyPfxXAJG-hL_0lOC4iQizMCtBw3fHsZ-RtC1h9cWgBFMzKh0ligo0iIRjqZaroCDFo-iWkPiXjjDYvQOLIlCwwkQhSLE7ibIyihLhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هرگز به مردم ایران نخواهند گفت!
اما کاملا قابل پیش بینیه که هزینه این مراسم بارها و بارها از هزینه جشن‌های ۲۵۰۰ ساله بیشتر خواهد بود! چندین برابر!
درست مثل راهپیمایی‌های هر ساله اربعینشون که باید از جیب ملت ایران مصرف بشه!
یادآوری : هزینه جشن‌های ۲۵۰۰ ساله، به ارز امروز، حدود ۱۲۰ میلیون دلار بود!
هزینه سالانه گروه تروریستی حزب الله لبنان
یک میلیارد دلاره! ۱۰ برابر!</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/5798" target="_blank">📅 09:21 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5797">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=TxyKN2fg1pD3KDD2C2aCnWweV9cOli9RLDqGRw8AHplq-NEOtdkNDBGymQi--advuEO-Mw6-wunHkrZTrF5zRfQ_OYNePo-NY5cxUyqCvyIP_8K8lKNDRjuRX6xJUuPgCIhsTmS8gVlUYTjDBXMLTa-Xj_UFqg9UaDTZ9X7XruMi5lafYT-f18r1l70z3HHFHJiAaZw2tDcwPXFTyrBcRz5YGSa-O3uQoPyKLi1P-J0xXDCC7RR1U9yx-UoHCzx041cwjuYRazdEyXvD5s4DAcDmKcDAu-s8s9oN1Hw1R5xFqN_ZgQ5z2ZOjq6e6W8lt-CPB7BcuVls6Y7y026RZLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3b713ac56.mp4?token=TxyKN2fg1pD3KDD2C2aCnWweV9cOli9RLDqGRw8AHplq-NEOtdkNDBGymQi--advuEO-Mw6-wunHkrZTrF5zRfQ_OYNePo-NY5cxUyqCvyIP_8K8lKNDRjuRX6xJUuPgCIhsTmS8gVlUYTjDBXMLTa-Xj_UFqg9UaDTZ9X7XruMi5lafYT-f18r1l70z3HHFHJiAaZw2tDcwPXFTyrBcRz5YGSa-O3uQoPyKLi1P-J0xXDCC7RR1U9yx-UoHCzx041cwjuYRazdEyXvD5s4DAcDmKcDAu-s8s9oN1Hw1R5xFqN_ZgQ5z2ZOjq6e6W8lt-CPB7BcuVls6Y7y026RZLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه‌ای که «سپهر بابا» ستاره رفیعی را دید.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5797" target="_blank">📅 22:28 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5796">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d3gVj5Mqr5LJ6zsKdYxWZYS3WnQCoqAjReF4fwO7pCZ3s9VNoesOZuPTTWXuKJkaYGCoCKWM2nqNnhvoWSVnilaZ2PwcRao5fmPROt7zmMeJuLHZF7xio2mvinHIwZ-OlwW1Vfx4PdgU8YN3KVsaRiLDS-POe3yDZWpHfuvqQWgpnY0hLJ9TlQAEU9pd310H9vi8QJ74yetoIACYT34NVJksAkMwSxWyWh48MvItBRakXXnHJ3GG_HAdLxv0BO3RqhsxfwVUmj1irCc1IO-K-PAShxYKx7QhGlJCsNFRYRkHq1D7-OBuBT57GrVgCisZrTQuRLwaWDH63luMuv9RLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e05c8825.mp4?token=d3gVj5Mqr5LJ6zsKdYxWZYS3WnQCoqAjReF4fwO7pCZ3s9VNoesOZuPTTWXuKJkaYGCoCKWM2nqNnhvoWSVnilaZ2PwcRao5fmPROt7zmMeJuLHZF7xio2mvinHIwZ-OlwW1Vfx4PdgU8YN3KVsaRiLDS-POe3yDZWpHfuvqQWgpnY0hLJ9TlQAEU9pd310H9vi8QJ74yetoIACYT34NVJksAkMwSxWyWh48MvItBRakXXnHJ3GG_HAdLxv0BO3RqhsxfwVUmj1irCc1IO-K-PAShxYKx7QhGlJCsNFRYRkHq1D7-OBuBT57GrVgCisZrTQuRLwaWDH63luMuv9RLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفاهم‌نامه ج‌ا و آمریکا رو به طور نمادین آتش زدند و گفتند که این قرارداد حقارت‌آمیزه که خب این بخش رو درست میگن!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5796" target="_blank">📅 18:49 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5795">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WoqIfq_zesm7aUOoFhzUHinXC3hl4R_wZJziiRjj1ipjgbEZEX6rU_jBxsR79JeoYIDOhIzXhs567n5D3C-JXYy6fX72NGM13AXOR9aCZZS_D4Q0v9CmVd-TjL5I-3uw3wH3cPqImdCSG6X2c_9_VvFiofOYyv5dzFt-D0J9djv50xn3HJyjGWydYKtASuUjzyRbmElSSkVWQ1_jPRu-0RmhkOzke_qD0Y9stXi1QauyLpTNeGipm5_6hcMtSRvKMIRHIwEfObFd5we8rwFvxWfO-EbTCn5kj80aWR2nZwxfxvhD5V9_0AIoW1fHwFD370dbZlMx0s-XD5gLPTYLJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امروز - دیدار فرمانده سنتکام با رئیس جمهور لبنان،
یادآوری : دولت لبنان چند ماه پیش
حکم اخراج سفیر جمهوری اسلامی رو صادر کرد
و ج‌ا را متهم به تحمیل جنگ علیه لبنان کرد.
مقامات لبنانی و اسرائیلی چند روز پیش هم مذاکراتی داشتن و گفتن مشکل مرزی و ارضی نداریم!
مشکل دولت لبنان و اسرائیل شده گروه تروریستی حزب‌الله لبنان که با پول مردم ایران تغذیه میشن برای جنگ افروزی!
در جنگی گه برای خون‌خواهی خامنه‌ای راه انداختن و فرار کردن، ۴ هزار لبنانی کشته شدند از جمله ۷۰۰ کودک، قالیباف هم به صراحت گفت لبنان ۴ هزار شهید تقدیم جمهوری اسلامی کرده!
لبنان ولی نمیخواد! جمهوری اسلامی به زور یک گروه مسلح رو راه انداخته اونجا!</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/farahmand_alipour/5795" target="_blank">📅 18:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5794">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=nCPLeLJa3-AbEKxwrO_EcqlvezA5KSoOsLs9hELCbNW737az3zaP7O-soxD_sjMSEy-fo48JeQrVKYIBbmDz5uQkes-WiT5Ftt9DN0I-8Gt--wHBFfT8UDwc89E9z7uetYPCEXrnI3v6eMDHQgjrG2pRmDae43IuQ9ASib4qExdT7wbbBeCXPcxqYuWNIx0DdKILbYsiWrrFnEwpFiaQ2TTod6aBGJab2m_tYj9Uogn1O_P-gg-xD5xEBh1LPWWKTBDX36lNLQHdfjEI86faYJHsl83ve5l0fojwORf9CocsnqVXvcCnFEXkfSmPEN_nSV1GC-dhC5XVpeZj0tmRwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e972609e9.mp4?token=nCPLeLJa3-AbEKxwrO_EcqlvezA5KSoOsLs9hELCbNW737az3zaP7O-soxD_sjMSEy-fo48JeQrVKYIBbmDz5uQkes-WiT5Ftt9DN0I-8Gt--wHBFfT8UDwc89E9z7uetYPCEXrnI3v6eMDHQgjrG2pRmDae43IuQ9ASib4qExdT7wbbBeCXPcxqYuWNIx0DdKILbYsiWrrFnEwpFiaQ2TTod6aBGJab2m_tYj9Uogn1O_P-gg-xD5xEBh1LPWWKTBDX36lNLQHdfjEI86faYJHsl83ve5l0fojwORf9CocsnqVXvcCnFEXkfSmPEN_nSV1GC-dhC5XVpeZj0tmRwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این شب‌ها، همین‌ها توی هیئت‌ها در حال عزاداری هستن
ده تا مرد مسلح افتادن به جون یک زن معترض ایرانی.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/5794" target="_blank">📅 18:39 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5793">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRiwj8vXzyn5qSCEhm9nfsYqvn_OprT8XKVR11LIW9_ResjB1rJxECO7gNs-M7ilDzw893hkIxG6Z1VGiAUsiWU8RcPKLptkzxiac_ql6O2QREP67UEcEZ0l-t2XMyoHbLtRcZNmcP8IvFR-_7_0pLOk7Dwf11FCCyll6r0lkDdmo_Q6_2Hu3IDXIiSAyUKuylfnujCOIrNE7JYzramj1iMhPjORVWkeYj1AODELyQNcKQoEtwITu7nGzsvZ_ROVxv8qyrxaiaOi0hX66vMElJnr4VYsz85u3eSfW6KGUAgaOb_q6nQ-Lk3w55V9QScJj9GZGQIHm83NqMtckHHe7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا در حد یونجه و ذرت ایراد نداره</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/5793" target="_blank">📅 18:33 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5790">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfkrkC8rICdaEbbw8leDyvHs2uP-KXwzYi_M_nTd5GYEveeV3Q4LHGvRnrknEepcEtsshay22K9hDolFdKhqyh2L5qdXmRk_Mz2kj31Bm5CMvOqgWufpawYfljb-Ps38DBCExQgcLwRFIkP0zGoJvX-wU_F19ufe8XSGFRnIKVKtu5Y-rGpUFb-fWVVrW9ZBVd-tcnLn_FcEf06t2EILThGG5R-exi11OoKCk5ptAJI66IwgyO_OkzkOhxa2jQZe34n8p_7M-SYtC6FOQc01z05upoSWDb_3VzUvjtQmhs6rSJVKOnZYQENVfn4iBLgNjBb4AEOVq44XvzrZH4HQWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UvvAHqsgrAjtfaHxuaonLX3dEIqE9JlHzVk4Y02Gi3oekspXkq070YM9Psh-70ouKCDGaUzxzyHcEeQwOj4lui18wA3_sxCKuG5NO_IaLsq26sD4LHCCNz_4pSWPgMivl1E0BFZM7GztqoSQagZKLk1huD30OvOCgG_VJAR_CcK1Tn5gzx4-u9vXin62iXRC0F6i_74TKOihZMLTdKbbCKYVCXYvwTudzgVfF8sPghkp7LT3iO81rUeYWb_KJ5sqaRxCitB4OgdwKjCagS98yBgNAIxvYka-b8p4woW6TJgGpMRy8QS-90kmVAmrPhSWpP29C2QBbgvgkybcV053gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/651901a9ca.mp4?token=UvvAHqsgrAjtfaHxuaonLX3dEIqE9JlHzVk4Y02Gi3oekspXkq070YM9Psh-70ouKCDGaUzxzyHcEeQwOj4lui18wA3_sxCKuG5NO_IaLsq26sD4LHCCNz_4pSWPgMivl1E0BFZM7GztqoSQagZKLk1huD30OvOCgG_VJAR_CcK1Tn5gzx4-u9vXin62iXRC0F6i_74TKOihZMLTdKbbCKYVCXYvwTudzgVfF8sPghkp7LT3iO81rUeYWb_KJ5sqaRxCitB4OgdwKjCagS98yBgNAIxvYka-b8p4woW6TJgGpMRy8QS-90kmVAmrPhSWpP29C2QBbgvgkybcV053gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«عالیه نصیف جاسم» نماینده پارلمان عراق،
عضو کمیسیون مبارزه با فساد، از نزدیکان جمهوری اسلامی، معروف به مواضع تند علیه فساد در عراق، چند روز پیش میوه نذر امام حسین کرده بود. دیشب در موج دستگیری چهره‌های فاسد اقتصادی توسط دولت عراق دستگیر شد، در خونه‌اش ۱۶ میلیون دلار نقد و مقدار بسیار زیادی طلا کشف شد!</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5790" target="_blank">📅 18:03 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5789">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">شعارها رو گوش بدید،  اینها اعضای سازمان مجاهدین خلق هستند. خوشحال هستند از صدور حکم اعدام برای «حبیب القانیان» ، توسط خلخالی بدنام!  جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن…</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5789" target="_blank">📅 17:05 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5788">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mQBDkMrx7SZ3TVNVlx154Chs61K8UphIF7RmMM1HvkivXHEvlLCM_Vl9oBCAX3013tjGJv6r60ATaCrPlaIoBRbpahZSCEhc31UuhYqUZWH0iRR3qLF44sikEnBjcC-GwHn-82hSVN1MDK-v9nQ2cj8ayfN-SQNn8CrfIYJfLTQ2-z19T_NL0RHfDV0zes7KNi4z5nlUco1Z8Af1VNlSytQ215g1cHkfGkL8KAnaCeM-TYMNkPnNenOomN6htuBRYpzruiry7uuNOziGU-QQWQ0iewLVk1lJhOcGnN0Sn7YjoGk4Vhza-g2YvcRWIhEiWEPCB9TDkvxIslQo6EhXfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/583cd57ba5.mp4?token=ZlA4FUq-X2sOP7DoSj0pHxLttQqF7tNStUiXN62RDg2NRznFgTe_nKJORQHxxk5uhJThvWHiauT42-3rqXI9nQ55Q2XJv3n_A-BVcl84Eqd6KfQbzFy5WjtpOi4GTDY6LIcXQ0nE_1AjFisXCqscXMr8xXubm7oquy7_oi8UvCRRnimuOZnJ0fmu8BEmbYAJ3cL8XwzXZ57zE7RlcKxdyMAx9NfUOSsHbN7IpMOPTCPpM6lxUDaMwBT0mmHDCpFUO2O7ZrwEN10_YeIFyz2dvaLUhQsN5AKtV6sNfJAAPphM2ujdNrRI_3ElVQHtPtoJQ7PZpZSAKsbtrSkJnaHz0mQBDkMrx7SZ3TVNVlx154Chs61K8UphIF7RmMM1HvkivXHEvlLCM_Vl9oBCAX3013tjGJv6r60ATaCrPlaIoBRbpahZSCEhc31UuhYqUZWH0iRR3qLF44sikEnBjcC-GwHn-82hSVN1MDK-v9nQ2cj8ayfN-SQNn8CrfIYJfLTQ2-z19T_NL0RHfDV0zes7KNi4z5nlUco1Z8Af1VNlSytQ215g1cHkfGkL8KAnaCeM-TYMNkPnNenOomN6htuBRYpzruiry7uuNOziGU-QQWQ0iewLVk1lJhOcGnN0Sn7YjoGk4Vhza-g2YvcRWIhEiWEPCB9TDkvxIslQo6EhXfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شعارها رو گوش بدید،
اینها اعضای سازمان مجاهدین خلق هستند.
خوشحال هستند از صدور حکم اعدام
برای «حبیب القانیان» ، توسط خلخالی بدنام!
جمهوری اسلامی اعدام می‌کرد، حذف می‌کرد، مصادره می‌کرد، بقیه  گروه‌های از جمله همین سازمان مجاهدین خلق هم تایید می‌کردن، میگفتن خیلی هم خوبه!
تا اینکه جمهوری اسلامی بعدش رفت سراغ
خودشون! و در ابعادی دست به قتل عامی در زندان‌ها در سال ۶۷ زد که در تاریخ ثبت شد.</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5788" target="_blank">📅 16:57 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5787">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/938419e982.mp4?token=aTeAQvuUZ3p1sQlok_anjF_WgZBr64HC6IDBOLRDbG1TAmzF9Fii_8D5WmhCed6yBtFfgSp69yt1J2tgEWvj-GWiNekBMVxifXRVxtCT_tvKuCr-LX1iR2NTqZ51N5ymqIUlTT9P_-GTovp8paRAGzta650ueYPpLTwQ1CjndkR3AXibZmHdhFRcJvHiFxXZNAYP9lZBT6QM4cg3cetDH16223sVY3wZ_V-RCdViwgv6LQ1_l-KJeyEi74J6MzraBPRVJkOj56OlaeLhAFYsZpRWxCcofbFHqmzwvA8gaAusp86lSK4bG1UA_R8BiyGHbh7y--VnXbRfhtocG0YjdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/938419e982.mp4?token=aTeAQvuUZ3p1sQlok_anjF_WgZBr64HC6IDBOLRDbG1TAmzF9Fii_8D5WmhCed6yBtFfgSp69yt1J2tgEWvj-GWiNekBMVxifXRVxtCT_tvKuCr-LX1iR2NTqZ51N5ymqIUlTT9P_-GTovp8paRAGzta650ueYPpLTwQ1CjndkR3AXibZmHdhFRcJvHiFxXZNAYP9lZBT6QM4cg3cetDH16223sVY3wZ_V-RCdViwgv6LQ1_l-KJeyEi74J6MzraBPRVJkOj56OlaeLhAFYsZpRWxCcofbFHqmzwvA8gaAusp86lSK4bG1UA_R8BiyGHbh7y--VnXbRfhtocG0YjdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قدرت حضرت عباس</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5787" target="_blank">📅 16:27 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5786">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgT5qLuCjeujKYtTL28TeSFqNqYAQiXMe1ohwWIiDkRKXZZyG3EZFpGzVAVndbRazJtUSiaDcgXdOH4ICO0H90JHnt9n8EFmitmBxhqZFd83R6bAAJBohaSbaKcC8iq5sOBqrfnmslQ1fl1oc_t9GNATF9C_ezzXFArRG58U8IQYgIrr3a-Swsg5ibrjew455S4lgeWrc-23ZFEsh3QbhsLmtfaMqhyBhFkLoGDbLkQ2C_f-FzXCW55rOk42Vfpl-5cPjjatcJZed1THO-vC7_jse0e6U8xEMZTDdHRvP0W7g8DHaKAjUtpArJhzrLqEmK7MS9YCCMC2WjaDbYGuhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای فروردین ۱۳۹۹  همکاری جن‌های دشمن با سرویس‌های اطلاعاتی علیه جمهوری اسلامی!  همین آخوندها وقتی اصفهان در محاصره ارتش محمود افغان بود به شاه سلطان حسین میگفتن اصلا نگران نباش که ارتشی از جن‌ها میاد به کمک حکومت شیعه!  ولی این جن‌های نامرد نه به امام‌حسین…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/farahmand_alipour/5786" target="_blank">📅 11:31 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5785">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=pnFP0APLxoIARxqyIyfUbyC2XKNTBbrZfWoq4QGhoZRwLOk1jcvN0ePBpqQ5J7nrr2MgWj_9pzsanjUU9vxUb2PN8Moz3X3EK8t4LsTnws7_jLnUiNmcjUm7BkD1zd44zP4PAMoqGFn3_WeOQFjvKgcFWGSX2sqBz5g0W8ITsOLyOhHfekMaZJVJLorrSvAIhZKEkIYz8uaWE-5sn8DRmLXeCN40mSU0OkUMBIr5q0b8Gh7OdZM33oyGlJO6nm7qACkrDtbmTVXuqkQiNaIYOpIrGm_6cIGHMHAwzfE1LG7S0EWvOEVtDQlG6VLOeau5Cw5Ka496zZePMV8gqSoQ1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b91e9581d.mp4?token=pnFP0APLxoIARxqyIyfUbyC2XKNTBbrZfWoq4QGhoZRwLOk1jcvN0ePBpqQ5J7nrr2MgWj_9pzsanjUU9vxUb2PN8Moz3X3EK8t4LsTnws7_jLnUiNmcjUm7BkD1zd44zP4PAMoqGFn3_WeOQFjvKgcFWGSX2sqBz5g0W8ITsOLyOhHfekMaZJVJLorrSvAIhZKEkIYz8uaWE-5sn8DRmLXeCN40mSU0OkUMBIr5q0b8Gh7OdZM33oyGlJO6nm7qACkrDtbmTVXuqkQiNaIYOpIrGm_6cIGHMHAwzfE1LG7S0EWvOEVtDQlG6VLOeau5Cw5Ka496zZePMV8gqSoQ1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/farahmand_alipour/5785" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5784">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=k0M65ZpQ5gWyU08AkRvuViU48vyzuDQu_Vr2yVThASLPJ__zNkLOb0oN2azGLsePG4wfs29syu0dmmQFH2jjJXRqUYJBn-lvrUgAo7oy7zQ8-mM_qcJbyINoUhj4KwELXvdZuNEgDZ_3skZOYg7ab7eBE8KsoagI3etoRnfYMII22MRi4uM7wqOYtAjGUfJY_RTOg-NQ4bGbdyH87TFP7RCWJiL_2zhwREtNNadq9fjcmUmR8x17krIt0X-HRV4PC1t-hPPSom1x474JBu4wgWFWG1lyjmfOavc2f5rTwgHMI39S4OZ2wwM9K3xQHc5Co9kWlDkT7OrvsaaooYU_cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb5c00112a.mp4?token=k0M65ZpQ5gWyU08AkRvuViU48vyzuDQu_Vr2yVThASLPJ__zNkLOb0oN2azGLsePG4wfs29syu0dmmQFH2jjJXRqUYJBn-lvrUgAo7oy7zQ8-mM_qcJbyINoUhj4KwELXvdZuNEgDZ_3skZOYg7ab7eBE8KsoagI3etoRnfYMII22MRi4uM7wqOYtAjGUfJY_RTOg-NQ4bGbdyH87TFP7RCWJiL_2zhwREtNNadq9fjcmUmR8x17krIt0X-HRV4PC1t-hPPSom1x474JBu4wgWFWG1lyjmfOavc2f5rTwgHMI39S4OZ2wwM9K3xQHc5Co9kWlDkT7OrvsaaooYU_cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زعفر جنی، پادشاه‌های جن‌های شیعه
😅
حامیان همین‌ها میان کامنت میگذارن که تاریخ مطالعه کنید! محتوای تاریخ‌هاشون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5784" target="_blank">📅 11:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5783">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=VoyT03cQ777Ghxbp-chEzMkM7aPe9jrrDHbvO4h2EOLWZJTHnQrCzsOjQlYNxFa2YcIEhfjhoELUFg4eWSFOS7-rX-DgMXj0tX6OIC1AjiQ3dMq2APX0KNQxWliWxP2abipARRQd1QShPIhgNSLcS2_7yDzxYMFNcgAY-ohkx4AJyEKNVqW1nwAJmBrgkIyDDEbadxqNfsze22YKXxvxkoQDglLFB4tqTj3TtmK-5XtL0EYtHBtM-TRSdlJEJikBcIZQZm9ihHihF9mQvgX6_qTFfpmJBxGM5BSNjqDx42QOZK9oRucHFJIM0wdUrRanMwL13-etB0FABpXuoJIa_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383f2c1b20.mp4?token=VoyT03cQ777Ghxbp-chEzMkM7aPe9jrrDHbvO4h2EOLWZJTHnQrCzsOjQlYNxFa2YcIEhfjhoELUFg4eWSFOS7-rX-DgMXj0tX6OIC1AjiQ3dMq2APX0KNQxWliWxP2abipARRQd1QShPIhgNSLcS2_7yDzxYMFNcgAY-ohkx4AJyEKNVqW1nwAJmBrgkIyDDEbadxqNfsze22YKXxvxkoQDglLFB4tqTj3TtmK-5XtL0EYtHBtM-TRSdlJEJikBcIZQZm9ihHihF9mQvgX6_qTFfpmJBxGM5BSNjqDx42QOZK9oRucHFJIM0wdUrRanMwL13-etB0FABpXuoJIa_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همش ثوابه :)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/5783" target="_blank">📅 11:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5782">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=WkwG9HtT0WNq8tLevNmhpwNP9ZoUKg-uHtRp7mNm_EcVsftC-ZLT0YSlUO0ONmF_c0O9xlDb1JmXPXG88lW52mDiLioAfKe4wYfIyDW0-OjF7WnDlWu_pnOb44HeVD-xHHMetPnEJvncOuv-t4jlCFo1L4jzloAqd75EbKSHkxwoq8jaIvEu-sxrymGAMOCIVYBt9W1KhAb_qPA8pnLRTVUJaOJf0EIpasz2VavIQTEFln3x6GFFRgoKLnlKV82nu1_AlfgkZ-6NeC7BqfmnobWFGGaBSCkx-6YXpcDZCdKIzkl8GDfhYU-jcXiuIfXJ-T7ElPShkDP8EjLUGLMHwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a9c5c701b.mp4?token=WkwG9HtT0WNq8tLevNmhpwNP9ZoUKg-uHtRp7mNm_EcVsftC-ZLT0YSlUO0ONmF_c0O9xlDb1JmXPXG88lW52mDiLioAfKe4wYfIyDW0-OjF7WnDlWu_pnOb44HeVD-xHHMetPnEJvncOuv-t4jlCFo1L4jzloAqd75EbKSHkxwoq8jaIvEu-sxrymGAMOCIVYBt9W1KhAb_qPA8pnLRTVUJaOJf0EIpasz2VavIQTEFln3x6GFFRgoKLnlKV82nu1_AlfgkZ-6NeC7BqfmnobWFGGaBSCkx-6YXpcDZCdKIzkl8GDfhYU-jcXiuIfXJ-T7ElPShkDP8EjLUGLMHwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آورده فرهنگی شیعه برای ایرانیان</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/5782" target="_blank">📅 09:32 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5781">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spknh8SanChfzYyJTzaM82VzRcWOALS6Gj1v9Mx9uyFlf2g7DlO9JWCKTeDrgPlcKuuDR4UQtAn85uKYSw72SEfMuRdxDilauM9liiAseq-JTR5UnvDyX3dsaRv9EQkLD6BTjqLHvosg0vH36yloG-O8sgwQzsyPHk8qxd907yC-JqJsUFMpieTxwzv8mI2B1Uh_v1I0aYlY99RoFqe_LVety8E5Bou5v7k5Tq3ZpiTLuOxVOS0gCXPGs5_nKBCuKTKGcyTCWXJM16aV_JjmvWUdx_q-nfRxdwEReymxTr9iuorsp_bvdXva-4hBl47pOmqBqPj9D4rrp78qxfqPRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«نبیه بری» دبیر کل حزب امله
همون حزبی است که «موسی صدر»
در لبنان راه اندازی کرده،
همون حزبی که جمهوری اسلامی رفت دو شقه‌‌‌اش کرد
و از دلش، گروه تروریستی حزب‌الله رو ایجاد کرد و باعث یک جنگ حدود دو ساله بین شیعیان لبنان شد.
یعنی روی هم اسلحه کشیدن!
سوریه در زمان حافظ اسد حامی شیعیان امل شد، و جمهوری اسلامی حامی حزب‌الله لبنان.
سایه یکدیگر رو هم با تیر میزدن! برای سال‌های طولانی!
حزب امل، از زمان سقوط رژیم اسد یتیم شده.
جمهوری اسلامی ماهانه حدود ۵۰۰ هزار دلار به نبیه بری پول میده. میشه سالی حدود ۶ میلیون دلار، مه در برابر حدود یک میلیارد دلاری که به حزب الله میده تقریبا هیچه! اما همین ۶ میلیون دلار امورات نبیه بری رو میگذرونه، که در چنین روزهایی دهان باز کنه و به سود جمهوری اسلامی حرف بزنه! بعد از ۳۰ سال دشمنی!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/5781" target="_blank">📅 09:29 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5780">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🚨
جمهوری اسلامی و آمریکا موافقت کرده‌اند که حملات را ادامه ندهد و سه‌شنبه در قطر دیدار کنند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/5780" target="_blank">📅 00:08 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5778">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=DzXE-YNOq-QsUGxaXlYrZGqAVNMw8H1qAU1lZqd3yrxhJRmJLcffFT8musHKbQTjXwvqM0MBVVsWJmSquu0pXYuKYykuYJb7XN3rlz9XJ1RmzfEJ25UDod1w9WbMJHTpPJpvUyevITPh8jaah1xml0MpZPbEH22yfjqZ-q9zuIQC72cUnwbSCZEsIi73Ij9uMIXBC_ejW423iC0viIO0kJZO6igJGeDCTYvRJo4J8t7-7_m5rKe_F6ju1Qa62cXiazlYEQUINDlkUgcGkw8cgL3rB6n_4Gb2IqRWpNsFDWNeY5qUGlF706LEiQDcmfx6NPya-hICEFuThmB4v22DUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/409f2a841d.mp4?token=DzXE-YNOq-QsUGxaXlYrZGqAVNMw8H1qAU1lZqd3yrxhJRmJLcffFT8musHKbQTjXwvqM0MBVVsWJmSquu0pXYuKYykuYJb7XN3rlz9XJ1RmzfEJ25UDod1w9WbMJHTpPJpvUyevITPh8jaah1xml0MpZPbEH22yfjqZ-q9zuIQC72cUnwbSCZEsIi73Ij9uMIXBC_ejW423iC0viIO0kJZO6igJGeDCTYvRJo4J8t7-7_m5rKe_F6ju1Qa62cXiazlYEQUINDlkUgcGkw8cgL3rB6n_4Gb2IqRWpNsFDWNeY5qUGlF706LEiQDcmfx6NPya-hICEFuThmB4v22DUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل از نابودی یک تونل
در روستای مجدل زون در جنوب لبنان خبر داد.
این تونل ۲۰۰ متر طول داشت و در عمق
۲۵ متری زیر زمین ساخته شده بود و در آن
سلاح نگهداری میشد و دارای چند دهانه
برای شلیک به مناطق شمال اسرائیل بود.
اسرائیل گفته که پیش از نابودی این تونل
آمریکا را در جریان قرار داده.</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/farahmand_alipour/5778" target="_blank">📅 23:57 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5777">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=uot7ik2BbLRyy3CfGgYBaOJQV_Ze0g03M8oZjTm1VRJg5MzAz73S1t4-pwsq46w6uDiVVHYsJuGzo5be1ylVFpMblcWqUZJ1igRrhieK7nimt7X4G8DAp1CbRBstB1md_gjO8d4nXl4FgzQ6Hjjquyrt3F2AHGJrO7r4w1RIR2ey0eqqvCVNJKLe_R0zz5ViWUkUHNdcIQlMZMJ-iIK0NM9OwTxwB0jxsenadGIsOialZ8omTgM_mhYKVhXNgUEhr9RZGeNuBTBBZLiH_r4_4fyIrZ-5p40lFoku8SJQzOArEcDRE2HrqXgdE07A-NVKiCucRjvpGnjWgXG_YBveAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06f2d554a0.mp4?token=uot7ik2BbLRyy3CfGgYBaOJQV_Ze0g03M8oZjTm1VRJg5MzAz73S1t4-pwsq46w6uDiVVHYsJuGzo5be1ylVFpMblcWqUZJ1igRrhieK7nimt7X4G8DAp1CbRBstB1md_gjO8d4nXl4FgzQ6Hjjquyrt3F2AHGJrO7r4w1RIR2ey0eqqvCVNJKLe_R0zz5ViWUkUHNdcIQlMZMJ-iIK0NM9OwTxwB0jxsenadGIsOialZ8omTgM_mhYKVhXNgUEhr9RZGeNuBTBBZLiH_r4_4fyIrZ-5p40lFoku8SJQzOArEcDRE2HrqXgdE07A-NVKiCucRjvpGnjWgXG_YBveAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منطق جمهوری اسلامی
و تعریف «امن» و «ناامن»
میگه اگه  یه کشتی بخواد از مسیر «ناامن» عبور کنه بهش شلیک میکنیم :)</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5777" target="_blank">📅 23:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5776">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPobaEPIMusUbTOLhIzJxX4ZMI1x1mpS74P_IkDXo3Gmi-Z0rdZQ0ANXvquSsIaAezfDsdSHUntzNtH-Td3AnOOSw6jpWrjznDDU6w2d5yRUe0H2OzYrZ60La09F7nMhmqSvizbo3_oOdNUk1KjTirrsEA_Zg1wOAWrnw_lQfHBzt8gpm0iSKc70RYklq4Ma2MQai4VaI_bBg6kRMQxTubTxD8f8ojZ8okgJE4p5nx9rS8eWKC_S_FXYRwunNMIn2QyPDRM4mKfT7oBsUCpWAlRySKh2pnuCUQtkRwAB0M91A3JQHvrHLdIXs-xI4Pjl0jjnwb5zqZ31qOZS0cjEmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس: چاره‌‌ای جز ساخت بمب اتم نیست.</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/farahmand_alipour/5776" target="_blank">📅 19:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5775">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=OesYLugUJK_RSEoXuZ4bb2QqaOA2lYX9y70REaIld8oYF9YLlDXHFUemmOXOMfTUyYvrYAzKlawpr7mBu0b86Qtd7Bp63IjBqwxW9nIJDNzTA-zpyF_D83F7FLL71M30w2GAzjB-LE_r12hYSYy4E5QuMmfnJGn2nCGRoniyDcIx_ZwlUuPK-25v2SlO6W7HHM1IgMvXCw-lnHqn5zm9arNq3mPzn6kYHSe8Dskc9t72L6sJc6O4vLHMIehYWF32_d4CFqfZhkFbr7KVzTx37yp-6PFj67m3y0D-RgXdsRhkHeppU4V4DjRmTDvPIVaKa52NTBh1i6mx_73VhuDbLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e4e9d7782.mp4?token=OesYLugUJK_RSEoXuZ4bb2QqaOA2lYX9y70REaIld8oYF9YLlDXHFUemmOXOMfTUyYvrYAzKlawpr7mBu0b86Qtd7Bp63IjBqwxW9nIJDNzTA-zpyF_D83F7FLL71M30w2GAzjB-LE_r12hYSYy4E5QuMmfnJGn2nCGRoniyDcIx_ZwlUuPK-25v2SlO6W7HHM1IgMvXCw-lnHqn5zm9arNq3mPzn6kYHSe8Dskc9t72L6sJc6O4vLHMIehYWF32_d4CFqfZhkFbr7KVzTx37yp-6PFj67m3y0D-RgXdsRhkHeppU4V4DjRmTDvPIVaKa52NTBh1i6mx_73VhuDbLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تیمی که با بدرقه قاتلان جوانان ایران راهی جام‌جهانی شده بود.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/5775" target="_blank">📅 17:23 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5774">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
شب گذشته یک عضو تیپ ‌گولانی ارتش اسرائیل در جنوب لبنان کشته شد.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5774" target="_blank">📅 13:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5773">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ولی ما می‌د‌ونیم چرا شانس با شما همراه نیست.</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/farahmand_alipour/5773" target="_blank">📅 10:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5772">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Ia3wZKK1iywwVWVSK1PX3HMSjn2wOrvTMmYFD5GPF1wR7fSFrFse9pQjw-AAVs6PG0uScsgs22wVhzA7fjjkgHbKa41XUsnY40zXUJjheWFwO1qppS-43KGKkMwZI68HD5qXnobjufrXso53aw07SH0ihFwXbZwhF7-gHA7EoSki2dU3OAs5uj6cCpezAJraY-vlGMavQnk9A2wGeqO_FW_T5bIDT0148spr_4how0TgXT0EJ4waxZXKhjhsxhNX-nytSOOENTFH_TQdEYeAx_aZ3HOD1hbgXlbV7wOpi2dSC-gagGwueV9haslTHbXtHJNDXSEpxVEt23bh7rXFKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1220ffd18e.mp4?token=Ia3wZKK1iywwVWVSK1PX3HMSjn2wOrvTMmYFD5GPF1wR7fSFrFse9pQjw-AAVs6PG0uScsgs22wVhzA7fjjkgHbKa41XUsnY40zXUJjheWFwO1qppS-43KGKkMwZI68HD5qXnobjufrXso53aw07SH0ihFwXbZwhF7-gHA7EoSki2dU3OAs5uj6cCpezAJraY-vlGMavQnk9A2wGeqO_FW_T5bIDT0148spr_4how0TgXT0EJ4waxZXKhjhsxhNX-nytSOOENTFH_TQdEYeAx_aZ3HOD1hbgXlbV7wOpi2dSC-gagGwueV9haslTHbXtHJNDXSEpxVEt23bh7rXFKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده میخواست گل بزنه و تقدیم رهبرش کنه!  ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/5772" target="_blank">📅 09:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5771">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=QqQycQe0MMBLP7UzDAYI3P5cmv6cuVnjmDZEIJ-QmrAPCNYb1ZPjqrGdMi2y3QlMKzTNARp2poQUKjVA6W69Vu66LoTbIc6BwxtzjxHDwkEbkdjasmXBWvO2qH_USvacz-QYkgvZsCneMJoGpVg-PworWdJu7U_7C98UtElgWU5DQsWVgBCOiw_6eP2uUoY4lzP_xZbcDXbqeCJts64JBcMZfZpn3ntYztT-VM7-uanQZycdlOMPCtct6vn90V1YK_BnPFFZui6-ESHA2TirV7NBYYuMz3HokWPUQwM65Z8cgtICSIYT3gC0W3JRyzEqu7qdgpaRGVwdJwaGe1_hEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d645372fb2.mp4?token=QqQycQe0MMBLP7UzDAYI3P5cmv6cuVnjmDZEIJ-QmrAPCNYb1ZPjqrGdMi2y3QlMKzTNARp2poQUKjVA6W69Vu66LoTbIc6BwxtzjxHDwkEbkdjasmXBWvO2qH_USvacz-QYkgvZsCneMJoGpVg-PworWdJu7U_7C98UtElgWU5DQsWVgBCOiw_6eP2uUoY4lzP_xZbcDXbqeCJts64JBcMZfZpn3ntYztT-VM7-uanQZycdlOMPCtct6vn90V1YK_BnPFFZui6-ESHA2TirV7NBYYuMz3HokWPUQwM65Z8cgtICSIYT3gC0W3JRyzEqu7qdgpaRGVwdJwaGe1_hEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شجاع خلیل زاده
میخواست گل بزنه و تقدیم رهبرش کنه!
ولی اراده خدا تحقیر اینها بود!</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/5771" target="_blank">📅 09:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5768">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cBuT3CJ8ixU9PBYXaww30d0WZflQXeRg1xkNJci2IRIxgBHFIzUvoCFADfjej19NSAwvkGQwaW_c7fo7P_r8NsCCWI6aozDqjsOJ3ecjnt00lgFnPzHhmWZeThFWfXepV7NPg9dliwU4E9ChFyFMa-IhS1aHuBEJ6febIhvmF_Qf-BymfmVjNFXtdS4NRSRqlamLuzP9nVlsH1jzmquPeKZobP2QPf3c2Urx-jdCaTEfP2qwE0zZ7HQqHrtTc0Y9NPEKaWJfgrtLM48gBIGwHqORYTgKWvrGAOXXjOyz0AJJAD1KNXXdI8zAjp5h3jGbvxkwXyPaLWM-myNqjEyD8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EyLjMX_wV_g3npS9Le182vfCRUJJkM_9AKidyaatupq7ZYpON06JDxYrVhlEUI7F2SKfyhOJ2-n7_v6Uh0lJtsJf6EI4klLgVG_kRDSUvhfDGWjlFiJs_WinTarZPrfAmn6BKxtA0Mx3kW60tYdmfaRSrGowegsEqBEwkoDpcIdX4xYVs7ILNRI-dJMfCy7EPdRMyBO_2jA2JyfXL3-1HLqyzpnq0F98krSyd3U7d5fs2f4Dzj3t9XtDHH_hAlJUJvk9tSTzamF8OwBy6zd-rKZFmet8YHbIylpAIxAVoKnx9semu1DKcehQU6DcW2L8w1-PUo3lTk35UmcoeN2SxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QkCuSlxY8jeSM85y4NiJel936BVpXzJsXZJJsOm4e8Ur2DY6kJmWbImihk8L6icUz1MuZGXHOOHZX9eYOf5in-uff7L1Mvn-g7Hm4tO6l9pV9qFscizcjJyakUHCy0KN-QWJLeaX2nbhOZqj2sJlgmUQbd-vmiGtpgL1oswkK5MLzHO3xPHadQbKVNHjSmXOKzyefikNGYT7c7BrgohDAI2zf2TkuinQkGgqiHZRsoIpNMMzHNRNKwAs5yb9387kVsykrmEWtxNyUrnL6HHbnPvWFCnGXxQMRsVlNtA6YTjKEec5d7hX1IR50nfINsa7yRpvA79z44ffprusaAAL_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در جاده فرودگاه بیروت، بیلبوردهای تصویر خامنه‌ای رو حذف کردن و به جاش تصاویری از «اول لبنان» زدند،
که البته دیشب برخی از اعضای گروه تروریستی حزب‌الله رفتن و تخریبشون کردن.
بالاخره زندگی و حیات‌شون در مزدوری رسمی و علنی برای جمهوری اسلامیه.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/5768" target="_blank">📅 09:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5767">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تیم ملا</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/5767" target="_blank">📅 08:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5766">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=m24aLhQcv--9RVfzqtDZNoEJlgKGoTcV5LnvJeV8aBvx1T6pCHmwXgNhZnEicjP0EdEMpdexiFFDxATO7S3juMX5vvyUWnXBEcqBtMKJSb1TafpAGMZSQDZvm97gDeUltjHct3MNRUyh_5m4_1sKnAuAaP6CHq-ua58b_ls3dvOBc7hJ165YrsTtZu2FsdstgL1cUulz4tMruQJ0j1brrsN6U16-zVR3rtCwWPLZczzNm-dIyWtrRcwhDe8TnUakJgIGUKOSj_RYBz6exAqa45LNVzZUrTaRljD6_povpCFuwbYrau_B2idpymMCXi5He92iGvgf3zootAAlyJvAdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10689e4ea8.mp4?token=m24aLhQcv--9RVfzqtDZNoEJlgKGoTcV5LnvJeV8aBvx1T6pCHmwXgNhZnEicjP0EdEMpdexiFFDxATO7S3juMX5vvyUWnXBEcqBtMKJSb1TafpAGMZSQDZvm97gDeUltjHct3MNRUyh_5m4_1sKnAuAaP6CHq-ua58b_ls3dvOBc7hJ165YrsTtZu2FsdstgL1cUulz4tMruQJ0j1brrsN6U16-zVR3rtCwWPLZczzNm-dIyWtrRcwhDe8TnUakJgIGUKOSj_RYBz6exAqa45LNVzZUrTaRljD6_povpCFuwbYrau_B2idpymMCXi5He92iGvgf3zootAAlyJvAdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط مدل گزارشگری فوتبال رو!!
یه کشور مسلمان [الجزایر] داره کاری میکنه که یه کشور مسلمان دیگه [تیم ج‌ا] تو دور بعدی باشه!
‏یهووو یه کشور مسیحی[اتریش] گل زد و اینها هم حذف شدن!!  :)</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5766" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5765">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaRrJadZXjIjBCCv3DIbmCxOnLwoIMu1noW64Na6Cn571gfzIOsx1J0YRT8aZVTZQxqKzu0UqWhFo1wkjok0qSGq2EDIIunHuRLJap0CkUgpT1-TJzAD4NARQHZxkSNS85MhIBStNCypodHFxYmeJ56eF6n7_1JE80icEawrjiBKvUsQnKlasyfzKM7fFMfKvj0KY9GZFy8aoqTmhkNVOwDjmzLInn7Foy6WKFYX1O1vaYEG73dI5Wro5ZpZkCGKgVFzNAhJnzriEjRi7JYXqwBWUeyyd3jhxVLUaJKUm-JRgI8s3MsNigDfYB7cyLFdN3RsKAWiuI7lcdezRvjKre1E" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17301f18ad.mp4?token=QULzo3rvzxGgtlWKbr09sAjSPdBNLTTD6v4ZnFO0pB-mF8HJbDAFMF1UVBRtzUIfdobam9wrfnicbWw69Sa9ne42x177tzGSmC5cVhwpisHBfiSUOOJNMRHklUGbL7FUhFewM8f9UTea7YYxWrIZVVwR2YwADLb4ZBaVviEU74dHdhA5HZyOfa0mViNiNFiufRGoxSt82afiYFnhqWJlfy8eqPPnJdmJuhT-Fatqf3-Dpm03dm2AfkLJwwDb-VDd3qa_cEgejAl-1W35A2EifYsy_-CMQC17meJSicJSEsXVftGuTO1-P5trXE66yUnnJF6QXMs7wjDqmRYuDLPLaRrJadZXjIjBCCv3DIbmCxOnLwoIMu1noW64Na6Cn571gfzIOsx1J0YRT8aZVTZQxqKzu0UqWhFo1wkjok0qSGq2EDIIunHuRLJap0CkUgpT1-TJzAD4NARQHZxkSNS85MhIBStNCypodHFxYmeJ56eF6n7_1JE80icEawrjiBKvUsQnKlasyfzKM7fFMfKvj0KY9GZFy8aoqTmhkNVOwDjmzLInn7Foy6WKFYX1O1vaYEG73dI5Wro5ZpZkCGKgVFzNAhJnzriEjRi7JYXqwBWUeyyd3jhxVLUaJKUm-JRgI8s3MsNigDfYB7cyLFdN3RsKAWiuI7lcdezRvjKre1E" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب خیابانی پیام عربی
به تیم الجزایر داد که ای مسلمین پیروز بشید بر تیم اتریش،
تا اینطوری تیم جمهوری اسلامی
هم بره مرحله بعد،
ولی اراده و برنامه خدا
ناکامی و شکست جمهوری اسلامی بود.</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/farahmand_alipour/5765" target="_blank">📅 08:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5764">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27a845337c.mp4?token=eBEyDdvn1eyafsHyK5sPHtHSDCvDJanhYwb_DH1dcplpVGZMhmvnOe3nRztHVTNQyouU4F_q66pEgMlK8Fl6Dg8CYaOLCJZ9uTlNCUgwhWgLG-4ekQ3OZaOqUuymxhi8p84_VuZqhGnpCrdTfWpr8mWBuVkrPH9zz9PTBI_Mma9ZoXv2GxlsWz1KacnxkVJbljLnAGXLecXrAxZ6nW1xzDzWMBc3fyaZX3iBSe0bvvPjfpsIsPxk1g_TgMIW4U8Xs8FvQR-1upnH_E2PK4iPxrTNAhLJTjshFrAhSZ8vuGStO2VTV4u1lnLqniG_MxE32bEoG3SUI1lj4jEBeuzqrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27a845337c.mp4?token=eBEyDdvn1eyafsHyK5sPHtHSDCvDJanhYwb_DH1dcplpVGZMhmvnOe3nRztHVTNQyouU4F_q66pEgMlK8Fl6Dg8CYaOLCJZ9uTlNCUgwhWgLG-4ekQ3OZaOqUuymxhi8p84_VuZqhGnpCrdTfWpr8mWBuVkrPH9zz9PTBI_Mma9ZoXv2GxlsWz1KacnxkVJbljLnAGXLecXrAxZ6nW1xzDzWMBc3fyaZX3iBSe0bvvPjfpsIsPxk1g_TgMIW4U8Xs8FvQR-1upnH_E2PK4iPxrTNAhLJTjshFrAhSZ8vuGStO2VTV4u1lnLqniG_MxE32bEoG3SUI1lj4jEBeuzqrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
تیم فوتبال جمهوری اسلامی رسما از ادامه رقابت‌های جام جهانی حذف شد!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5764" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5763">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🚨
حمله سپاه به بحرین و کویت
سپاه پاسداران اعلام کرده که در پی حملات شب گذشته ارتش آمریکا به تاسیسات نظامی جمهوری اسلامی در اطراف تنگه هرمز، به ۸ سایت نظامی آمریکا در بحرین و کویت حمله پهپادی و موشکی داشت.
🔺
سنتکام شب گذشته به ۱۰ هدف در اطراف تنگه هرمز حمله کرد.
فاکس نیوز این حملات را وسیع‌تر از حملات پریشب توصیف کرده.
🔺
سپاه گفته است که در روزهای آینده حملات بیشتری به پایگاه های آمریکا انجام خواهد داد و پایگاه‌های آمریکایی جهنم را تجربه خواهند کرد.
🔺
کویت و بحرین اعلام کردند که موشک‌‌ها و پهپادهای جمهوری اسلامی را رهگیری و منهدم کردند.
🔺
ترامپ در واکنشی به افزایش تنش‌ها گفت : شاید کار ایران را از طریق نظامی کامل کنیم و دیگر جمهوری اسلامی وجود نخواهد داشت.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/farahmand_alipour/5763" target="_blank">📅 08:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5762">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🚨
🚨
حمله به جزیره قشم
امشب، دومین شب حملات آمریکا به منطقه تنگه هرمز است.</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/farahmand_alipour/5762" target="_blank">📅 01:40 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5761">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ux2iqb4LFtcLrpeQa_CkkeBWWBGfaBz10we1NobaYylrgbcMlY9E2mTCyv7_PL0-u8L7JhattfgQ10LHpWAsG-88OdaClETFz09xf0V3DzY-v9QMPfT1sIE7LUI1Pt0Y2j3Kam3ZPGyzM4NqkUrJItGgH6HoM3YluQfkQVfv7CV4qf-YNxiPQ0OMUgQVxNwOmu8AU-dK5Q_0hSXsdjP8fP3yeQ13HLgyQ2o2fEv8whwjGE9puOSmEHk53VdxfImu_ze2q6o8P02Q9YU_-AxYheBpGo73F6S8Z3SZgl40E0maZty8JJWkVcsCZrK1n1BFpkni_rrQw9zR2q3pWorRKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه سنتکام : به سایت‌های ذخیره پهپاد و سیستم های ارتباطی جمهوری اسلامی حمله کردیم.
متن کامل :
نیروهای فرماندهی مرکزی ایالات متحده (سنتکام)، به دستور فرمانده کل قوا (رئیس‌جمهور آمریکا)، در تاریخ ۲۷ ژوئن حملات دیگری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا که در پاسخ به حمله ایران به کشتی
M/V Ever Lovely
صورت گرفته بود، به ایران فرصتی داده شد تا به توافق آتش‌بس پایبند بماند؛ اما ایران با پرتاب یک پهپاد انتحاری در بامداد امروز ساعت ۴:۳۰ (به وقت شرقی) که به نفت‌کش
M/T Kiku
اصابت کرد، نشان داد که این مسیر را انتخاب نکرده است. این نفت‌کش با پرچم پاناما و حامل بیش از دو میلیون بشکه نفت خام، در حال عبور از نزدیکی تنگه هرمز بود.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه اقدامات خصمانه ایران علیه کشتیرانی تجاری، دست به حملاتی زدند. هواپیماهای نظامی ایالات متحده زیرساخت‌های نظارتی و جاسوسی نظامی، سیستم‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات ذخیره‌سازی پهپاد و تجهیزات مین‌گذاری ایران را هدف قرار دادند.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/5761" target="_blank">📅 01:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5760">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
🚨
اکسیوس:
‏ارتش ایالات متحده در حال انجام حملاتی در منطقهٔ تنگه هرمز است.
این حملات در پاسخ به حمله جمهوری اسلامی به یک کشتی تجاری است.</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/farahmand_alipour/5760" target="_blank">📅 01:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5759">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏خبرنگار صداوسیما در سیریک:
‏دقایقی پیش صدای چند انفجار شنیده شد.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/5759" target="_blank">📅 00:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5758">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrOU-AKAfl1D99_pQx5c75N3OSItjYcVAgHSuLR8QP7MSWnAhHmT5m4OjnM8arPaXrdsH7ETXSIrw4gan0J4wo4eaWPyX0BsC1AUeIdDJiqKxtUhdJmWdbFgRZVF5i8bEiPn8T4GFJo68I8BV0iZwq6b72RqW-y3lGYcdUGAM9ecVH_uFaM_d0um0mLUm47HcrW0QIBkLw0-2hNZ7KZGUDzhwuxkhlv8c5szCXu-UE_AuvoeTbOykMKTiROxcv1GVw_M9Yzx_91vFVEfTYqipPySUxsUIq6cXwi8qrurIGC9zwv1hht9oz_I_bI-ZIBEp5-m90obd3WZpybdJbRvLIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cee64931e.mp4?token=kPbjLZ1DreRAqQfOeEm2Lp2vpSznEnqo1aRGZKBRaFtruIGJdEnR1RBbY_Q9DgRx2oXMaQ8zcfVU11VTwsZFO5BjXgIT2bFqxGIFkpLuUjc4KAoCcbZpp3WeyU5AgNQtzbhig2mvA1MmtFqtfcDf-wCb3s5jKmswlFACmtMKylHP6lXjbWA3y0BKSDZ42Kt30PqQ7e-gNVc3BYbF0jWjsf_zGecxtXe7mPvrSMj2RLgNFcP4TLso3NpvLwySgH5gRbZe2oHRkAxNLd5KDendL_vzAxNTdm5a5E6d1R9lBg-_ms_hwH72eIfERYvx6V-0zvj3yeahwJ8q67fR3rJuTrOU-AKAfl1D99_pQx5c75N3OSItjYcVAgHSuLR8QP7MSWnAhHmT5m4OjnM8arPaXrdsH7ETXSIrw4gan0J4wo4eaWPyX0BsC1AUeIdDJiqKxtUhdJmWdbFgRZVF5i8bEiPn8T4GFJo68I8BV0iZwq6b72RqW-y3lGYcdUGAM9ecVH_uFaM_d0um0mLUm47HcrW0QIBkLw0-2hNZ7KZGUDzhwuxkhlv8c5szCXu-UE_AuvoeTbOykMKTiROxcv1GVw_M9Yzx_91vFVEfTYqipPySUxsUIq6cXwi8qrurIGC9zwv1hht9oz_I_bI-ZIBEp5-m90obd3WZpybdJbRvLIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جاوید نام ۲ ساله
💔
‏فرزند ایران و جان فدای میهن، جاویدنام علی محمدصادقی، کودک ۲ ساله، روی شانه‌های پدرش بود که با شلیک گلوله جنگی کشته شد.
‏پیکرش را همان شب تا صبح در برف نگه داشتند و روز بعد به خاک سپردند.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5758" target="_blank">📅 22:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5757">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfdbWY08pYceyYlTD4NnRWO7GE84rNawP6XB_WEHRxbOnc1QmbM6kAuvcVBp2y3734MeyzM2jByphBY1ydmc7Fqg1K4qbJF2EweTfgROTljqA0UN6osApz-BwMFv4jQgrPgv4M6cRujaB43KPbcP85etuZXiOcES3OPGkz1Qnx08VzhLkycgE9N0PIHW5KF2e6UlRO0E4ro835Ws-hcn005DjlrL_nutSUd6SyXu6GOfC9InzF19ugPmPcbI1cIFHFexqGSNdvj6xbZ8Bwy4rQXsfrSbH6FwzM8MIfKH3P3DiIx0nSCtNREpoB7xQCprysLEYxpcfG7SRgAELYS7rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پنج حمله هوایی اسرائیل به نبطیه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/5757" target="_blank">📅 20:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5756">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">«ما و حزب‌الله لبنان تا ابد همسنگریم» !
خب ذوالفقارها!!
چرا آتش بس با اسرائیل رو گدایی میکنید؟
چرا «آتش‌بس» در لبنان رو به عنوان پیش شرط مذاکره با آمریکا اعلام می‌کنید! خب با اسرائیل مبارزه کنید! ببینیم این اسلحه‌ها رو کجاتون فرو میکنه!
در ایام جنگ قیافه مظلوم میگیرن  و کبوتران صلح میشن و دنبال آتش بس هستن! آی سازمان ملل کو! آی حقوق بشر کو!
و در ایام آتش بس یهو شروع میکنن به گنده گویی و شعار و تهدید!
همین جمع اسلحه به دست، همین‌ها! از جمله قاتلان فرزندان ایران در دیماه بودن، که حیدر حیدر کنان مردم ایران رو به خاک و خون کشیدن!
هم‌ایران و مردم ایران رو، هم‌ لبنان رو به گروگان گرفتن!
نتیجه سیاست‌هاشون در فلسطین و شعار اینکه مشت اونها رو موشک کردیم هم جز ویران کردن غزه و دادن ۷۰٪ خاک غزه به اسرائیل نبود! اصلا هم به روی خودشون نمیارن! کارکرد موشک‌هاشون در غزه چی بود؟ ثمره این سیاست‌ها چی بود؟ ثمره ۲۰ سال سیاست هسته‌ای در ایران چی بود؟؟
ثمره جنگ خونخواهی برای خامنه‌ای که در لبنان راه انداختن چی بود؟ جز کشته شدن ۴ هزار لبنانی و گدایی آتش بس؟؟</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/farahmand_alipour/5756" target="_blank">📅 18:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5755">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دبیرکل حزب‌الله لبنان، توافق میان‌ دولت لبنان و اسرائیل را که بر مبنای آن حزب‌الله باید خلع سلاح شود و سرزمین‌های لبنان تحویل ارتش لبنان داده شوند را رد کرد و بر ضرورت نگهداری اسلحه تاکید کرد.
حالا این اسکله براتون چی کار کرد؟ یه جنگی شروع کردید و یک پنجم خاک لبنان رو دادید و فرار کردید و از دنیا خواستید بیان آتش‌بس برقرار کنند.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/5755" target="_blank">📅 16:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5754">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=A0YB1gowt0-lRpRvnVN9MKCd06lz2g2wBt6tT6rJRICi_Lfr4nhoV9Absy1nXzfI-2a87hbzllOgSreWSQ7-8qwR0JHPrwuKqueXmgwEMhkjfmk8cAqt6YF5jKHCpfl9p0OqxFYkRwt95jU-trNtVUSWWn-KLbKXKNL-lkJhW8CZTMHgIh2jb84_HIRiJJSc_uVel0rla0sGYrulxcHNvR6CN4wAbqSzv2ISqZNOKz-tre2WBWTaKAd0ypONwX6wy9o15ORbUFsMkcNOPpO__XDnhNqCdyscZqo0OC6smtZhSjv1cVhREpYyzQOlUc5I4MdSlrMRdFnKFq-inGyaIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db5841aafe.mp4?token=A0YB1gowt0-lRpRvnVN9MKCd06lz2g2wBt6tT6rJRICi_Lfr4nhoV9Absy1nXzfI-2a87hbzllOgSreWSQ7-8qwR0JHPrwuKqueXmgwEMhkjfmk8cAqt6YF5jKHCpfl9p0OqxFYkRwt95jU-trNtVUSWWn-KLbKXKNL-lkJhW8CZTMHgIh2jb84_HIRiJJSc_uVel0rla0sGYrulxcHNvR6CN4wAbqSzv2ISqZNOKz-tre2WBWTaKAd0ypONwX6wy9o15ORbUFsMkcNOPpO__XDnhNqCdyscZqo0OC6smtZhSjv1cVhREpYyzQOlUc5I4MdSlrMRdFnKFq-inGyaIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/farahmand_alipour/5754" target="_blank">📅 16:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5753">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=jk9IEOPgM88zQ60oDBY-HhvF6KoJpoJVD3rdnBCjU6WnlLR1diahQNPZT4P02vLxQdEqZn7QTMyJFsTdfs0TX-5DEYQmyuzzBvFOckfU5i5Xchzf15NTMKEj25SCEKnTC6eB36d1Hxdok_QoEeLYdxkgbXdMiPQPXSmw2UMf58EX-BH68HwXhTEhBpuIQ39a_I31r5QHShDcrM2947i3qVlrwuaDwTSukTlRwFhW7gjmz2yXBC28NW7Yor9t9Ou03mD3lJv-hz75Po4y6X9YaSsMBFsFMVvSrDBASLo6N4YfXthnk0coplvPlsQOtX5X7E83OqGxoC0OD_yiIhk3_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f038d1dce.mp4?token=jk9IEOPgM88zQ60oDBY-HhvF6KoJpoJVD3rdnBCjU6WnlLR1diahQNPZT4P02vLxQdEqZn7QTMyJFsTdfs0TX-5DEYQmyuzzBvFOckfU5i5Xchzf15NTMKEj25SCEKnTC6eB36d1Hxdok_QoEeLYdxkgbXdMiPQPXSmw2UMf58EX-BH68HwXhTEhBpuIQ39a_I31r5QHShDcrM2947i3qVlrwuaDwTSukTlRwFhW7gjmz2yXBC28NW7Yor9t9Ou03mD3lJv-hz75Po4y6X9YaSsMBFsFMVvSrDBASLo6N4YfXthnk0coplvPlsQOtX5X7E83OqGxoC0OD_yiIhk3_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جشن و شادی در غزه
در پی‌ موفقیت تیم فوتبال مصر
در برابر تیم فوتبال جمهوری اسلامی</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/5753" target="_blank">📅 10:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5752">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=jR67A-5YBhYrxGrHyAdQVkypuiM95oIH0OAYMTUiAMpIbTmBW9lr0bQ2xNQDP9Xy2M3tsrPTmOJBEgmY3s9quSp3mU7Pf3ziuZPQzY7KHJbLqvSRCR8TbmhXnM2D_c1N95hRQWoGTrRJdG3eeWi_rFrjVn2cRv0hloFX7kkQEMZpqDJ5SYkqPOY34LObAFXrOnsOOAM6Jsy77TA64gKIl0Edjg0WbEbKOkD2_qnm6uvS31MpJXk4hu0wDuE211NRG9OOGuQiy3__z8aFhpoxi4pLJGYpNckdwU3YC56uyOakNDdJ4IbbErYYXJyFO0TYlgcfDnoOMmNJlyHN7MszNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b07e212ab.mp4?token=jR67A-5YBhYrxGrHyAdQVkypuiM95oIH0OAYMTUiAMpIbTmBW9lr0bQ2xNQDP9Xy2M3tsrPTmOJBEgmY3s9quSp3mU7Pf3ziuZPQzY7KHJbLqvSRCR8TbmhXnM2D_c1N95hRQWoGTrRJdG3eeWi_rFrjVn2cRv0hloFX7kkQEMZpqDJ5SYkqPOY34LObAFXrOnsOOAM6Jsy77TA64gKIl0Edjg0WbEbKOkD2_qnm6uvS31MpJXk4hu0wDuE211NRG9OOGuQiy3__z8aFhpoxi4pLJGYpNckdwU3YC56uyOakNDdJ4IbbErYYXJyFO0TYlgcfDnoOMmNJlyHN7MszNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش لبنان برای برخورد با حامیان گروه تروریستی حزب‌الله وارد خیابان‌های بیروت شد.</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/5752" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5751">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🚨
🚨
🚨
حمله ارتش آمریکا به اطراف تنگه هرمز  ‏فرماندهی مرکزی ایالات متحده (CENTCOM) اکنون تأیید کرده است که هواپیماها در اوایل امروز، 26 ژوئن، به تلافی حمله پهپادی دیروز ایران به یک کشتی تجاری در تنگه هرمز، حملاتی را علیه انبارهای موشک و پهپاد ایران و همچنین سایت‌های…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/5751" target="_blank">📅 01:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-5749">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UNGXU-qy4gZrYzimv4m4T0lgaSS895j60pQyvaUfRW2rxOk-6c2sQsjiNzx3Ea6grVugA0onowrM1xdPvokAQUW6Mv0N6VkdFZLAgzdPcFtgU3oabqyRpXoVc7pscri3fHNDxvjhuAAu2OqMwRCtSV2UOaui9fqN1z38Q4XJ3deeTjd6KmudWM3xZdk4jABV7Yt5wsGjbyFBrtfveH0nEvSgqy0sHjpm1ww88U9eNsE4Glauj2426qOEgezSwovm35YnniE4yKPDK7OgEB7pyEaPrTUYlH6bcANLRg07lR8SOcKBh3ErgcYhxLM8jlSA5Dj2uwkhj5GDV8ylj1AF1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29K · <a href="https://t.me/farahmand_alipour/5749" target="_blank">📅 01:02 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
