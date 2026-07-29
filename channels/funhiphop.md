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
<img src="https://cdn4.telesco.pe/file/fNSKPssqGp-J022MFKOn5rqRsVxQHl1yuOtd7MXhLLqKrMZSt1y1C5rHiigsUaoh7ju0inEvlGOTLPwvkWfKTJGMw7YaKuCzQcpiFRqNQKW_58wj3b2kZ0H5vC6JkkSCsL-wHa-tvJJqxUZXuKLRhN4JQKVcwM3Nwze4HWh1I7as4e4EZFZl_oTvdZQEsMyZFEcaURr77igvhKkOg393_1d6Gf7VCHzkQsxSGuviq3Ar19EdS95pFgcexWsjAPfLCuHE-_E4ng1yPFxL0uTfIrlCqYdZX0idBW2I7PdRar2MZD5SHT-dPU2IJ889UIwJZYJucetctHuUnskSu06AZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 02:22:41</div>
<hr>

<div class="tg-post" id="msg-81510">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/funhiphop/81510" target="_blank">📅 02:14 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81509">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">کصخل سوخت رسانا بلند نشدن که باهم بندازن، بالاخره میزنه دیگه</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/funhiphop/81509" target="_blank">📅 02:10 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81508">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/funhiphop/81508" target="_blank">📅 02:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81507">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">ترامپ مادرجنده ساعت دو شد چیشد پس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.27K · <a href="https://t.me/funhiphop/81507" target="_blank">📅 02:07 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81506">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">فعلا چیزی جز صدای پدافند شنیده نشده به فیک نیوزا توجه نکنید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.01K · <a href="https://t.me/funhiphop/81506" target="_blank">📅 01:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81505">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">پست آدرویت تو چنلش: این روزا انقدر اتفاقای بد و عجیب میوفته تو ایران آدم نمید‌ونه از کدوم ناراحت باشه
🤧
🤐
🫤
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/funhiphop/81505" target="_blank">📅 01:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81504">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">تلگرام کانال روابط عمومی سپاهو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/81504" target="_blank">📅 00:43 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81503">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تنها اپی که سپاه و نیروهای نیابتیش میتونن آزادانه توش کار کنن تلگرامه</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81503" target="_blank">📅 00:03 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81502">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ این جواب سخت ما چیشد خوابمون میاد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81502" target="_blank">📅 22:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81501">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nx8MewuZDBF_4T5mfCWilRAyYWoOWj39JnP0Vp85KPKXSwwraZcJNS5gc9MrkjQpDGT5KQATw9DY8yMe7BJmKd58mVv8qFtWiX081a612W_LSEwjzJyKcp4bS7nkfcbW4D8M4TQVGrNBY3qhkeO6HMi7NDVOkQQtwoc6GQn-dMh7boCdvANXUgect7pu2dMFQowsRT1yxmmpqIv7zmy1XSIL9_EYKakNFCnkVlEs5ifq6RJuszuL5_k2FQ7IzgYgkhZfdJw4gXZ37w0BZ8QQ8g-ymgPkbr7V55eiAx0rIkutDuC1U5Ix8P8a6YLi2dkuxF1lzb-HYGErEQ3wGIxQyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برا دزد شدنم ۲۵۰ میلیون سرمایه اولیه نیازه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81501" target="_blank">📅 22:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81500">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنر</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDu1ClSU5X9XKf2C0jDbX5_s6Wyzf5dN1s_qNm5icLisMwZ5eer1uj-qhiM0ya07k8_SKgLXjZFzIkLMFdMgN783MrBuDed-tQcVf3mvTL64kvI8F5yvqbbpQejwnC1fmzAzrcfWEXNUNnJ9mTW4eC0faRffMjfen7Nq3LvIhXZEbnug7ii-nRrwMNVB6Bn8kW29lRPazSY0ezLBHEceZgImWNithohzHwRi61g17aPngor4_CsjwbzYQcuegq3145H8DhA7mSLI4LkExwkOqnpv3QlwQo4FqjIsXAqnxtJ0HFzBu9SvAw4BkgowBkjIW8HPfYQQ8_KLzpxSsz0udg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎬
با نایت موویز، دیگه سینما همیشه تو جیبته!
😍
دیگه نیازی نیست اشتراک بخری برای تماشا و دانلود فیلم و سریال!
🤖
تازه نایت موویز یه دستیار هوشمند هم داره که بهت فیلم و سریال معرفی میکنه :)
💵
با خرید اشتراک خداحافظی کن و به نایت موویز سلام کن
👇
❤️
🍿
@NightMoviezBot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81500" target="_blank">📅 22:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81499">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">نتانیاهو امروز با رضا پهلوی دیدار داشته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/81499" target="_blank">📅 21:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81497">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2_ZkDiMQ_j3KUkSEzuQLyzqSqpwAhTbZFpfwJMCHvzFT4jMBjBcTVP8ms8PihipT4eHWRgMgF9xt_tER_CiX8MzUjILi5TV2Ww-VYui3rhdg9T_QPpG9Hw6mpjwExSqtCwiU49keYNGdV6NNfyC1vXbOADRCghg2OI9Iy90cV1SHfXp208QyecQJ-e_QQc8-hA3kKAvm9jFXU_akWM42_hK5djRr3wSo5ZiTRTbdZGYYURAbxR2lqNNMag3CLbCkGFDmowcizrBUJq4Z9ebm6a0CihUEM7OEFbYhGg09ZaKv2TAlh32HnCRRB96xJxBcr1bbPp62K24fEIkvUc-jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام چه بامزس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81497" target="_blank">📅 20:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81495">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nEiJurjCarpjIjGPFh85TjSCsnYoX5zQv1ECIEKNS63eVJcIfOocC9qnnYNjRVaLPj-92-qijK9zXHVuFjRkq9SJHKf_L92VXvZCt3OvufDoJHoU1XFUvkCXVUuBan88I9N6l4Cw3GXrqyO4-jRDdBmSkSEuBzK4WH8JE5MsXkfJyByzP7TY5j7M0k4mlv8yEggrPrMiD0ak_3FTP2V7AkSL2wCQ8i7hOfFzQaVHg7YlfUQ3ie1wPeVsL8bA6Dj548dq9oODFqP1bY7UHvFs2eP3Xu_KNA-8DHgC0wuHjJ7WkLhFmyzgPFWjoPPZtj809ZaYUVjBh6wKjeR1KQAEDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی بچه اش رو دوماه زودتر بدنیا اورده با عمل که فقط تاریخ تولدش روز رند بخوره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/81495" target="_blank">📅 20:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81494">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZirjrNRBwij_I9Leez9jvsR68t2_UkUoCKbyQ_UE0qMKfE2J75L1lpQJP_51qei6lWOkiV0C8HObXDicG4gH4isDhz8LR-aoMJPF3dgNTEC_uK0hDlGVZu_FZLG2DhNYi4DGqnBnwaYl2AP5-XowL5txi_NMZUoHuzv1ib7eDOo5D15wqm0cXDB8DIrzjrqiuAaUhdkM-qz3rJ-Xsn5osFU74JZTNZbwskUkCFUGPCI3DaSIujNER9OF0eCd4uC5GbceRPaMqxkbCnw81SiXtQmeF7srt4fX7No3HWMr1zBxowyWkl1BtNly_XtS78q1WkQ_fxl6nl38D8OtHhZ8-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوتیسم پسر کوکوریا عود کرده، بخاطر همین دیکه موی بلند جواب نیست و باید ببافه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81494" target="_blank">📅 20:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81493">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">پرایم هیچ بازیکنی اندازه رافینیا ۲۰۲۴ بهم نچسبید</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/81493" target="_blank">📅 20:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81491">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">از وقتی تلاش نکردم برا باز کردن پیچ خوردگیا هندزفری سیمی کیر رفت تو زندگیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81491" target="_blank">📅 20:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81490">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">پول ایرپاد نداره؟</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81490" target="_blank">📅 20:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81488">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjLtVA0r1YvS8V3ZyUFmguDUvpmqvl5mZRdyJA_mc42cdIabliE9xl5jEN7QOP-AG1yiFyc2eky0-ZXm19dgesVid04hwJDGBes35HCt-SkhYyVrN3KRf113tjA5nmWyzWIjx-83afN6HaDcP7eyAOXo2hFMn4rZAa9inETAtxAZ9RqqpBMqRw7Kp24icM1rvfrRN_s9DcSFp7cyyJIEwwSg-NDv_9kyk3doxdiKOArTp254zLTm2d1PApgRS4EbPG7WdIf2WiSaxAdUhaS0npdQqs2NzmSDsC_4pBzu8DJcAMm2lWYU4k9TN9_MQSIdYEU9w3nr00ehcVkL-tY_-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uuedw_L47y4-XQaAia1f0zUJ6E7913LDV1uZOjE_hg3PqrMIjQW0WIkSt9Sa9CDTewbOa_B6vsY6sPfIxtoUCCOpyqZ0coFnzXiJrGc6y6uZ3MasVDaP1P3ZNsit5DeBK4xbbGA6NbPDBk8-LLG4PZOzjwkbQDjAfkzH1vI53MAMmmIRT7nABg5zjCr-08Uso8orBbZzhYBXO0uKQZx38MMn27ldNditvHCwk4KlgHjcL6dbkIhQd9VxWtLqg2y2D1lkHTm8IW9qzyZq-eTdpMK8B4XHiFIc06UbFYaLlqpxy4mmj1Tj5l__YRECofUCvzlUpx_xWaprYE6pEsESOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رافینیا شبیه زن جنده ها شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81488" target="_blank">📅 19:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81486">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k1srxx4ZJ12yyKMgTUBbXk9h9KZkh_XekLH9Zubj2C2pUOlRR_tI70XvwPE8zl6LGoASR9InUM_WGV4lkk-q7rgwgT7C3RFn8pX1NJE9sSIQYKakXE7Fbd_UqUD5AuK8rwWbrqq-8MgkTRqjYvOwZhMS7hQriNSSyXIMi6dQ7vgsI-zPvPXzncHcVIxvfimzEjtkaI6Gza-IBIVZ4MsnZrubkvVzgr5Kk5mrQL42VItAlV8EMoeR6BpZS-erkdlkips1cMii6wdy3oDkgVFO5foBip0tvKgRsavU6wTha_FOz9MzYlGfEnW_dY4cFV3f1fgSubQQuC2ZfxVDTDHqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MJnWTgqBWQ9HXtxO6I-A1JwZXT6THjb8nDpVPxhDn7S30jfIjDyTTZ6b0hctusVpiQGpeaxyeRjAHtXSoxKmrXyEgi3Vc7_HBpQ3B3luOg0sACOeC5pLa9LLCNbid2QeZM-4V-x4DypRcOAd_6kcfy-bGdTDanoDSdbiG5It-tJJbk0r510OCLaF2fNwWeZ_pICpDw3wqnfDIqCqMM0aX3fbhI2623B2DQFlcdGZHQkoM7djzczK2km3EnVTFOiHmMnuUck3XbPNX9p013HS1RkYtJGCF3NLeHDOnm_47Eg-4zY0tiBuOsJmwLfZSmrnpeBKzpnRXvStqF18R8uuHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هرکاری میکنم نمیتونم با قیافه جدید وینیسیوس کنار بیام.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81486" target="_blank">📅 19:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81485">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EK4eACXRJAuLMqR99FVjuiS6Tr55HySDU3PsyOi_UNdc8AZCPGsLwQV7K1znszGiv5VUX0aFuFJT-mCy-d_vUSnvmeAq5ebiAPmCqHx89_GgQS3n39jKgysz6mwPOcNwWdAG35SJa-QjqBY2E9DVhpNYlntWjyqTVqr0CVV3dFy3lmVKH0EEiO68RCTrr7pvM_6Oqn0mJStVe0PU3yQVfLxdtjaC4sXt6XWzfOyU-_W7Q3kRprfk6msVRe41z1dXLxlDgZtsJmduDA3qvYO7yZa3Ce6xbIQkZw6J1U8XAfaFnZLAHRDkcA5Bot4HvObvCbGhkTAmvRRH8TxtszC4Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چی بگم والا.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81485" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81484">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uVA8E51gftDj28A6TFo4Bfl17FCXzM94PDw_xBAf3tMMb7CbiBpIJUCMUQafj_bARr69TcluzJ_1Je2wZ-Sl8C0oUFm9DdXQ5-0XyV10h9ItIr41LVj7FF1BybTfovkyoXclBKDyvZq6bM-I70yup9Axponlsxm1yqlVIZo2kKb1arsFpCt69aalXRq4UD6mF2Whp2AYkCtRSKQcyvR3MH4WcLy3q3lf_hz1k3wMJW1DOEnMcJfC_2rfPx7JYSZE52COyvZzbtSUzCRsGZ4YNkOJC8gr93GVV0R0nSXRGvpNLinXOSSdMtdcnHshknQD2lo80S6DiOQsKnJoTc_kGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81484" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81483">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFnS6qHNL7hZIq_yvH-5veGK9KCb145R8OaOa7NTB3h8akqFZPBxaG_pELVkoQicikjE-vEiB_EWjNtUbsA0Sm06lld8G1GiazpbSdO6Pj5GBQk1CJgIayufBgQDZGfM9PBBsR7_ETsouG0SUvjvTNJYxK8hnXnT_R-k5RFLjmDrItqcyljP_b2hvExQM2S3kjt6fcjY8rxp1AMjWBXI4Lz-NgZU6gDMvYRyXLPFWC-5iFgIzP0kJ6CJh74P3ci5K3vwVXJPnFfJmmvhmn2-Eht-Ufz-mHaHU8e4qdp4EekYcw33657jd_2CD-T0hZzAC6RHnZ2dXqHCRcSEmXkGjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس جدید صابر‌ ابر و دوست پسرش.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81483" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81482">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5tFmQrabPwRcsxQ3oHcxLJOai7MjKMHGMZhJDTc6RQbHPEJsVkMyF6hkjVHD_Yjup71YgxBbGLkQhHFJCvC1eb2n87IP51-dOzX6TVcP_CiSdOw9GdTO6aw_aEUKNj2hwBgsjuEuK8Fj7LMP8sUR5AvcvozQBHWERFEMC_oW_UDGO4_7mlFNsyAMLHPeAiXYTZbEQVWxuyGlg9xCbPsgalXzri77M0C5--VQUIWDsUEfRoTegErgy75Q6kNMr45mQfXEWjIMLEA44DY-QyqIIyQW84wXdsydmrS0j7iw3YYEjRbSL-rLWMgE-AqILpOt18oKV423XxjEka_TeZW_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفایل پاول تو تلگرام:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/81482" target="_blank">📅 18:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81481">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkO-gqEBmYBqPDWSnEq5WEkf6KD14Kie9ISkIhkYzly6gM8NxW1swhQqGqgHt5Vtxqqjc8oDm5z-cxH8uln3wKosPwrkNTOXveVWQl-OcxaJ4LF0uNEJPIjZW1N9Yap5_MiCrE0OJD8frJuC-wIA36A59e7pcveQNboy9hTHChmeK3UBnnOX4LDAigaRlpR_9gAVwapp_z3BYYQ0MxfH1qlI5WKzLiK3creQvXBFMMDqq7T5oJzRwUvyl1isS5vAUoeshG4GQfIx_2DpCYGjdSugfliwUg_hVJQAmNKnzaoQTmXetdXXLUX5EyggH1kZxWpz0UjSzE3zhNHRpXHhzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش دورف:  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81481" target="_blank">📅 17:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81480">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/81480" target="_blank">📅 17:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81479">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAzgoY4YLB0TfGhDKYaaC3iMvmfzY7dNqxr9WRsXwPq6CDTlNnmQnZwdQMK5bxSJR1wd7z_a_ZiW4kphk1QIj7erPGjp8i-LJVzpegB3S5hveGytfJ-SB_gk91JtyNxl9aT7wyGTBCvX_gSfo3-_qGNIPA-dZ0DefRk8GNp7TCwrAORXY7USlUsxck-VJS_wCo9obKRAJeauI2bmSStYiiHofG3CO05Xz3vm7HhcCVn0O0neu23zm2btlB332lnuZlLDlKnxR-888_s19O-7fA1ETeIaGeMIRskix6lCT--qLN4UNHf1so5kQKtHMmDg3sgr4GhHyS1js8CvlMsm7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عاشقانه‌ی جدید عرفان پایدار و شاهین نجفی به نام "داشی" ریلیز شد.
🎵
Spatifay
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81479" target="_blank">📅 17:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81478">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IZk1Hb0oj8sJO_Mx-VUKTX_sXnIIKjERU12iK9mpcRmMSrd-GlOPXep8rY5ExfrBYw06wqox1rbag9BEtQZ0jkYHaOT4IU8AOqDwDGV7G77UDoel24Up1_5RyYvAr8HddwTxkGz1CKDiriVFY1h-cPd5XQmDOlwxMCXqRRSFFXxhj-eJqaoqwogGhKeUMtTLty86gJNGGiTr_bKQo4z9i2OG1mYqxfVpwnktANUe6KrrvYImGCJ_a6jFgkkZpNKAWME4l8214AP1X4z0fmCZFv8O73DTh49mUcgRHyADxWlLY87GOegWVItSXUNmNaeq1L8hyfe32ppzedR4cI4_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81478" target="_blank">📅 16:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81477">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: ضربه سختی به ایران خواهیم زد‌‌.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81477" target="_blank">📅 16:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81476">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">منابع نزدیک به سپاه میگن در نتیجه حملات دیشب عربستان و آمریکا در عراق، تا این لحظه دست کم ۵نیروی ارشد حفاظت اطلاعات سپاه کشته شدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81476" target="_blank">📅 15:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81475">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81475" target="_blank">📅 15:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81474">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اسپانیا با پخش اذان از مساجد تو بخش هایی از کشورش موافقت کرده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81474" target="_blank">📅 15:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81472">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7nvxbgR4b_2uspZDuS5W6abnffEpZ5jASV0e5wwcTdvbGAJS6IaM_y5JDncCFLynxNg7UOxHQVj4zxiI1Z33Qex5Na9BL3IaXp6OkY6GKOvHK7Czisc5XoNtz_fTiTrEETthPR3IbUj8r4whPgm2sdYaDM3ez6SXSQ80MVbZKdc6GAKgGsbM3CQYXlM-2DApDeRB99U8ICwCT1tFN9myEpJ8mZweLA4DGVL_Lpk0JiK7v8gZC7ygkZ0ABjBj_WQMf6CgUJLYCeueeIidK6N_eh5n8GnWXwnqC26u3uh5fDzXnchKGjOcG9bsuVMJGaKbJfZW8xacHkMMr7bD9-JIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81472" target="_blank">📅 14:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81470">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wCAT_jnBZsfUGNF0xNieHC4aXCljoSsZ5vGico1tpXhSTRbZ74ErjGeveD1LI41_3afijog8iohXN8F3AO836znX-Vf-eM0NGj6XIjAargBSlXFxAwYZ8ylqc1-RdqMVAZJAl0OCu2RF5HBAIoNyoWPp6pdnj93TZjcmcc7HSL4KcGSonYpvVKlkUYrVVkaA7Mfv0aJ4uMpX2JrdvAeY0JJ_cuUmN4xgYqLXbHEVci4nEf9dqq7j5Ft1ICjZF8bBCk3IkWgxApIGsqVjpnNVOzLqSzOwfk3RoeegwMCURdbCNA-oh1Aj7d1WC0TCMsUCMmMbff9QV07Qv32ku9YXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pLKQqx8C7eQe790u_Bf1g4AJ16E4GYpbWs5XaGfHcUTZsC56Yb6R8UGYfdktduV53yOORk4OXLvOULrdiuqvDeH6lm1l8xnZGoVv3XqImBD4GbgoHQNpUwbPid0wIYj9bYTNmSv7xHXxdV9QC4jaD3694QUqgFuf_-eTN_ucGThPvSusrXTYHu7fnzuAcQklPqoZUjXLgBOIBNM87MInHzSFi96ryiERR9wQXwrJURdnHfPKIDheovfDQxJa6ZbqnHBDtB6cAOQL7XxvBrotD9SasVgHM-Vcm0onRf7KGHuEj7H1ByiizovN3dheJeaM5Z9FXGv3bQFf4F57Jwl5cw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81470" target="_blank">📅 14:35 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81465">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">اگه این با سپاه همکاری میکرد که الان همه تو صف اعدام بودیم</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81465" target="_blank">📅 13:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81464">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">پاول دورف داداشم، به اتهام تسهیل فعالیت‌های تروریستی، از طرف سرویس امنیت روسیه تحت تعقیب بین المللی قرار گرفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81464" target="_blank">📅 13:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81463">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دلار 193
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81463" target="_blank">📅 13:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81462">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JH9z0x3PysQENZkpeLtF9baom0ajBQxQ6VUGsQ_fIG60SYbTRXStSVv2YIJXF020B6hHoppkf_NuxR5sdN8zuLC--WT9Ht6d6-Wt1iRHLDH3oDhCuQOeDifKoewL-W8-IOr1C-9FxBEPMHYtOpmJB_cO349dWvz3cZjEOYN544rdRJSJbWUFzzL-ThsPFQB5oRS5BDT6pxSQdITCTTSkGZ8GS6jTEvB6-FPl65qx11kQkg1AXGKwKtlqYbP88DyZKA8RcSuODbbEiu_O9A181pviNtO8d3oPHV3MWjRdx7xccY-KVCwHzgxy5p69QpoYK3LHrgYD1vJ6gWYV5S7ifA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری پیشرو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81462" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81461">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bMbq4zfALVvqVyIzpnTsEOQesP625hgq5wZvrWccyKDmhmXlSNkax66xcPRGCKcDZHR3R_NsYVm0NV6PqnpvJzhqW_is4V0TdfJ6gbj21aS65-gPQhAapWfZUGA9DoSz5STEMHfmQ62DcG-1Qn8ZvcaQ8t0ckYOj8XBdfJtjNBZh73apFBkErzeUtqst-sQ1HTLIiZ9Yr_BeX8RR7uc4_2qmPU9OpZgXM-_ZzTJSaib5h_3VcBI1Ld4PClIkL1KeqqIIJ6s_3--2VIAXDU1IDhpDAIPswsPhDTIlwlmAYuq-zeq9zkVC7gm87hNfKewXtvZ6cootoBDkGhqNSwmA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
اتلتیکو مادرید
🇪🇸
-
🇪🇸
ختافه
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
چهارشنبه ساعت ۱۹:۰۰
🏟
ورزشگاه سرو دل اسپینو
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
اتلتیکو مادرید در ۶ بازی اخیر خود مساوی نکرده است.
✅
ختافه در ۴ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر اتلتیکو مادرید ۳ گل در هر بازی بوده است.
🧠
تحلیل خوب، آغاز خوش‌شانسی است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r7
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81461" target="_blank">📅 12:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81460">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">از الان تا ۶ سال آینده هر اتفاقی بیوفته ربطش میدیم به جلد مجله اکونومیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81460" target="_blank">📅 12:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81458">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">هدف یدونه پایگاه آمریکا تو اردن بود فقط
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/funhiphop/81458" target="_blank">📅 01:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81457">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">تروخدا اسرائیل باشه تروخدا این یهودا خیلی راحت نابود می‌‌شن بوم بوم تلاویو اسرائیلی‌ها مجبور می‌شن از دریا فرار کنن تروخدا پدافنداشون ته کشیده ۸۵۸۷۴۳۹۹۴۴ نفر ازشون مفقود می‌شه کلا اندازه یه استان ایرانن ۹ میلیون جمعیت دارن کلا تروخدا تروخدا اسرائیلو بزن سردار
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/81457" target="_blank">📅 01:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81456">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ببینیم از لپ لپ اسم کدوم کشور درمیاد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/funhiphop/81456" target="_blank">📅 01:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81454">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcYZQh9mNbrgrm7pEAOmuW6Viamk8vHaN5cFbzZMyrIz0hIIj1fxqWeJpy46JH9fTKEtKodMUDX-xkg0jCbwT6SJZmWbtaSOFI8ekN7T-YPKIiurnvmqLsf3hBkkp2HC8KP4OF8LzjmdXd2sPIQlzfB3gL4YJ781ToCfYWQe5ohA3RLAeagsgkcC6xAYxU43u4CnTBxNqQk3WysE9uF_vqqcjFBvs-3k6YKjS4Hd2zTnGGG_-EQNZkpwRqaqvQlad9PYJrT_xBjaS0SjzbqEIc8QECYXftDNxFyvT8d83Tp8cEct1-pOhaSLIGXHxhPejNpXkMcunegnK8WThJBV1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/funhiphop/81454" target="_blank">📅 00:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81453">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r0rgNcHcA6iIdu5rh5R3w9UfjQhTZeHAXB0Qnq5lFdaNGlY6AUO-8FGNgoM0GQapTuLFv24r7d92YI-aXKUXzhDbCkR8aC6CSRiFtk_GItl03hEcnKg9U0anqYshN67e5iGs8BJtqIBeDc7rux886cJmudbsARdXJdmFpRJs2VGYEkj1xRCX5s6KMHqi0yRaa01-te32ATpTP9gNN9t-rnrksQUWJ-1m214hvM2E9M7Q4S60ckLsg8T_MRsYiCuxmeSzgQK50a7TpdexIRPswnPRJHzy1SW8JzRcNXSJnL96DYetZrap5WFQlYPcTPL7FSogh-TBDS_5HG6FcKONLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم" تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81453" target="_blank">📅 00:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81452">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3ZbBY_znryoXdseWkYy2wQ7wZtH9XM2damN66HQo9zxaezfPg2icCD-Bb3QL8w8CrHlYyYZbuvy7NNwXObPRZ0bMerlLcBV49kq_kc0JxxdL64RVO5j5wiXGm3pyl51rFeAlLZi61p70fJSnW2D4NN9dNfRXONESKC3Ax4lJJ9jPl3P6-IVfSIXr-h2uiTzS2fcIyKdZtkUu3by10mMvIk7mW0Z12s0cUi9-QKlhUNkFvzIpfxY__Nw7tJYtcuT80fPqDv2Rn86j4hKQBW7R9tAGIkXueiCddupESOyjFrAVrsUicymMX7JxB7n4wxMWVu5qkkKnbJShJJ3Qt_Bbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچیزی برای تعریف ساده کلمه نیاز به یک توصیف ساده و فراگیرتر داره، مثلا خارجیا وقتی میخوان بگن بی طرفن میگن "من سوئیسم"
تو ایرانم هرکی میخواد به یکی بگه "جنده" دیگه این کلمه زشتو استفاده نمیکنه، میگه "شیما کاتوزیان"
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/funhiphop/81452" target="_blank">📅 00:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81451">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">#رسمی
داریوش ترک کردهههه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81451" target="_blank">📅 00:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81450">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR6mysSIHQPh467EEQYi7S5I5_jbkgYgTKwFzcyL6rLZfxEZkTTkau7TkcHS_s1khHA8c0VXJ1eqbxduxhZoC67XRXmZEQZLwFW4tEFxU-lLSJpTpBTih5lvcTnMiE6U_zuRVUtZMvrW7RruWSPHcAqv6vwtRB1OD0IjXvZ1WSB5IjYfYjMZR7p7CkmeFTG4RamHSU48FS0_IX74oXlIONYOSJZ9Lq6qBgAT1_WEcXTCKKnM1Je_KDyoIDmO4Z7UUgOFq2TX9utW4u-nKLmCynp1pb7s20v_QDNKcfCyS6XCEyRpdkUCOpUtmhFxaADuGTYXBqde_4s81sBnsHXzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حضور شاهزاده رضا پهلوی در مراسم یادبود لیندزی گراهام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81450" target="_blank">📅 00:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81449">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یعنی جدی عملکرد ترامپ رو تو اوردن نفت از ۱۲۰ دلار به ۷۵ دلار تو دوماه ببینی و باز از گرونی نفت بعنوان یه موفقیت حرف بزنی نیازمند خیلی کصخل بودنه  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81449" target="_blank">📅 23:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81448">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EuZM79PAoN5iZWkrI6MFnI2jas51MLnWse3pBSfzPCOT9XivgCSHpvfjUCpRmvMY_yDYZ9jxy_IH4bjXJnQnXAaP0lWbw0uGm9MJ3iTtfLvW_nUWMdYQB4hqe3XhrMzSegeVeuxi5Kyb3Pi8bRlVsHTKR5mtMvjkp5ijeVs_zVNcon1NuypYe2MlQxNIQtctozwGRQEX4CLeMCoyAYXBl2_LE4RxyyBEInT5EDxmvsAhxHORSg1NVRpZ_k7z8i0DsXjQvgXtFVnIgpmA7QQyTI_kcVLMGGVAbPAskfmC6Z01-1wjy9F2cmGgUFuX6tYNzMTzQ3XKy0SoP2qYUuUheQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاپورتا سکته کرده، اما اعلام کرده که حالش خوبه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81448" target="_blank">📅 23:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81447">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">قالیباف: دنبال بهتر کردن
زندگی
مردم هستیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81447" target="_blank">📅 22:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81446">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1i2qovGLj7jkpzHNWpR1l0MmLsdzk4OgWSEfZQpQpXtDUOmDbZwnkIeAYiF2c841mey8aa3C1Jyt2yTJLleXvzqcJIAYCQ4pxPw3Zoqs5Z2Om4gKsCAFMLx0BMY08HyTlMDVYcGOeVL7xyFjmIxOyhhDGIyWXIznwKuRB__GqdBPkG1o1jA6KoNAqpZwzod4noJaC_aZbQo-kE3EZeHqdKxudBrPBTY7SyI0ReBbYzs7sjI9S9Yt4CyEMXwhdhqCR0dT4wQ2nPg1EUHTeahu5uUFdC7bDBb6CluAOipFz960SgjxLq-EvVOYi3riNxLGXCX6pyyO8iy3uoKHp31WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جعفری دوباره منیجر حصین شده، هم پرایم حصین هم شایع با جعفری بود، با هر کدوم قطع همکاری کرد بگا رفتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81446" target="_blank">📅 22:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81445">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن ویتوری موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر نامحدود 90 روزه - 45000 تومان
🟡
سرور 20g - کاربر نامحدود 90 روزه - 95000 تومان
🟡
سرور 30g - کاربر نامحدود 90 روزه - 135000 تومان
🟡
سرور 50g - کاربر نامحدود 90 روزه - 225000 تومان
🟡
سرور 80g - کاربر نامحدود 90 روزه - 360000 تومان
🟡
سرور 100g - کاربر نامحدود 90 روزه - 430000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81445" target="_blank">📅 22:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81443">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SYbI5LosjE292-IbOIDrCwi-fH06bLfyRPzMZJlqhXhzhtvWsGG-TL2TiMs51GImtF2Nn-TJlX-qlBhwonUAEARmcb5FbG1LIC-fxSQg1JZ6z8VweVb8fyC6YMgdzu0ENNDt5FG85M3jRWTQJ_1gp64tQqYxV4zy6m9u8_9A8aTZYZ4glMqf2I20pG2Yq5uMbd1pzBcW1ZrD7sBwLPMtnFalIr6rpBLun6WMaAz6Azfvq6u8kiONXEaX-RMwkB1dOXesX4MDsOh65Yddvjt7b_TOGG5KYW4LNYXNt_NH8ICXU1q_GBvL7TFBQrxLZo85LvEFCCJUNlJLA0DF14aUEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Bt_8cUaLLeogVK9fg6g3LPZL6pFlBcFZlQN_HP3DFKDm0VhhKcGnT4a8sd21-3s-efFJEw6mA0gJVuPYrHmrcd-ZZTSNwLFZS0o75J6wlB6WKln1xWAgOIKIZHEImyAbHe2ygzLcLhLKwvNmOWzOtjwS56bjHgG-hhtT_aKnhzI8mSCfs9h8QGFL-NdJxzf5maB_Wl3dl0Mr8iPbdlZZUBWTZ9qodR-wSP1gJLuccmWdLMODVhDbh7VATOS7A7LrkwGx7DImt9qxplFcZsaV3Pab5thnAfe_y0PkawhHj47zRgsB_l4DkmaAkEXesSRAqf9pa0eB2soZ0WZQjwVooA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری های نوید و بامداد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81443" target="_blank">📅 22:04 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81442">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=Lx4QjZFoRqTJJm0jOGwCbnE_uJvVb0HXPVbYIWMK8HBNebcfykn4g66Em06-kHP9ZFZiSFgSesAYxUYFpgN0VynqjPx7zkyXLeCgh6T2hJPDCrP3S_4z6DAkMXMxisVVeHWJjSDbJuy2BH4E_Tm7jIKc7YnGlIZSArWczMpUwJj-aIpr1RdtHB-Haa_8hQcubNFcpBcHaP5Vx0EauhLywRdsbflyZP41jkmSMMbZY-TcX5JSWeKhLDt95CXuhXCZ2eB3yViPdDetyZkS-sU40cUMOixjOwPd8Vo0mMwwr-YzKFcFgr5ymbXVNLtT91D5RaWiobiatDLAXCEN4D2S-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5beb4b7c70.mp4?token=Lx4QjZFoRqTJJm0jOGwCbnE_uJvVb0HXPVbYIWMK8HBNebcfykn4g66Em06-kHP9ZFZiSFgSesAYxUYFpgN0VynqjPx7zkyXLeCgh6T2hJPDCrP3S_4z6DAkMXMxisVVeHWJjSDbJuy2BH4E_Tm7jIKc7YnGlIZSArWczMpUwJj-aIpr1RdtHB-Haa_8hQcubNFcpBcHaP5Vx0EauhLywRdsbflyZP41jkmSMMbZY-TcX5JSWeKhLDt95CXuhXCZ2eB3yViPdDetyZkS-sU40cUMOixjOwPd8Vo0mMwwr-YzKFcFgr5ymbXVNLtT91D5RaWiobiatDLAXCEN4D2S-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار کودک‌کش تروریست صهیون:
آقا جلسه‌ی خیلی خفنی با ترامپ داشتیم، وقتی می‌گم خیلی خفن یعنی خیلی خفن دیگه، ما تقریبا سر همه برنامه‌ها و اهدافمون به اشتراک رسیدیم، از جمله همینکه ترامپ مارو پاره کرده که ایران سلاح هسته‌ای نخواهد داشت و یه سری چیزای دیگه که من گفتم و جاش نیست اینجا بگم زشته جلو جمع.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81442" target="_blank">📅 21:46 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81440">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KhcUTqwly6tw-thx3_USaEZvvhTysnYshshJTH6Ym8uWZ8-BtqUqjV63Szjh8vqkWXHI9wxKB6Juz53JiHw5oZp2u2HU4Y4fDy_55v2cRUom28BiUxKTGajvkM-kTp7FxJBnZ_90f2_q6JZ5p8wXR1xPZW2_glELiy0_h2yyfOKiqujBWBRA7dMLwjNZ6DjLVp-4sB9aVPJmIS55iunw4qPXxSF_Hzx3vWetYfaKXOl8bs5d6fXaUEu9pehJ0CDheMpVCXLdLVF7G-VYMuJ9C6CkDg_UX4KI2GnmxOUH4dAAEx1bM1an5--9macIzXV93KJ74j_E_IbRXrOnBCcdqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FE8C-BXiWzNzYTlNiSwMfUy5HoA3v3nypgC8WL-jLk81GQna7z2x8VSFw8enVwS4KaFYKnS-IolLKmv5-VDETytOWASBRU5KPjqKWX89dyvuf-EggUggrYCooFeQ7r8nQPgpyzZ24UAt7Iw1kGhRHUFOt4ooA7zPos8SV9PBrSjN4CEqHHRTaEtM8r6KdTP70nnB3Ql_4d2ZEYMCqwnFMQmvlwFTJpcUkf7NiT5jbiDyF7OcBM5sP5UGTcDyt8envgD52TuWvsp5zh4QO9X_CR9e_ir-lDhOvHcBO4FOp_FPbrnfG-ITMNAHMFOtaDu9GSLsjhXCwLGzXfybp3lFAg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کوکوریا قیافه دلافوئنته رو تتو کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81440" target="_blank">📅 21:14 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81439">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ce57fZSBlFftny6Cd-eVw_6KGs4VPVsXfa0Q8IwaaIrvmlvFX1ORT6zclOlJYvm-JVV9dYD40N0kw6MjAmdhFzItv0Ab2osdnsxxd5x94k6UdLKAI6yV9n3GULEnMDEnuk3C1DIDBeywnUKEwX3DfkFK6vnzPkoKV_yDIBiHdAoA-KObOqiASbx5XMjN68h9Nhcuvc879pCYHwlTpV4hv3BSiBeo3l56gQowaHvAKJXSSLgTYH3ZLaeIRoKIm68kAhmpp1vj0ypxoOtXonfMoeYLHKjmP7lmUNgge-jxL-_ci0QHTLmj_DrBw02vpCPQ4V-Hj7giuNX20U5K6Hw6mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشماممممممممم
😂
🤣
🤣
با هوش مصنوعی فیلم سوپر زن رونالدو رو  درست  کردن  اصلا ببینید پشماتون‌میریزه
🔞
یجوری داره میده انگار  ۲۰ ساله توی پورن هاب داره کار میکنه دهن سرویس
😂
😂
ویدئوش رو اپلود کردیم بات برید ببینید بدردتون میخوره اخر شبی
تماشای  ویدئو کامل
https://t.me/CONFINGMeliShkn_bot?start=3126b54d70f9</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81439" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81438">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بعد از اتفاقات دیشب شماره مادر سام صابری رو گیر اوردن براش فیلم سر بریدن فرستادن گفتن سر سام رو داریم میبریم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81438" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81437">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شاهزاده قراره با بی‌بی نتانیاهو در مراسم ختم سناتور لیندسی گراهام دیدار داشته باشه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81437" target="_blank">📅 20:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81436">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDBL9aS490O_ddzosWzVgYo2NBfahPSnNKbGoayW8BDQoh9P9q4tDUZ0ygp_w_f3uMB_Ll0MfvCRCNNEIHquj-4WQgu1jfyNRqWmY7V4uRA4Zo5pC6gtCLWU3XX_LjXKGxjgudNItC-lj9IxFIXBGEbpJv2JNp4nAO7jQGy24en2gj0JbgtJxjgyRDawKJinwKijRD70Eu22nN2vAX9sqWbJ3z3o5XUouXm63vTW9UireU7N2YfCxFABBdy3yKeGolY1NlxVZnbxKhVLHt2KHQejFqPmDCiuzo6OzHk3-8_dh5JrlPfRYTtu-T5_HWSWdUK1ux12n2r6PrRT8VHlLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک ماه گذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81436" target="_blank">📅 20:32 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81435">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Numb 1 - Madoro</div>
  <div class="tg-doc-extra">numb</div>
</div>
<a href="https://t.me/funhiphop/81435" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81435" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81434">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rXI5PDtqHYnwSMi1gkjet2AlzSkQehPtbUtu-fLHULDe7TFogkpUFBukpWuccCV6jZdfzKrtyB71jVDLBxd630sXvj7pwer3Wngwml99FrpF4O5rEFgpuf19Gk-8rLqavdCVEvJSbahxZ_fiCY6OUrnui_AEtfssP0t3z0n25rzYYYPZR-lDe01QkaDxwv2uTbdIdta-nER0hI7qH4kXRzR0eizWOJ23c1N73e7Ly3cIOvF2tOnelXq3rf6aiv3jwN91eVrK6h5u0UqGv5Als9ihVZ_b0JOQTEAgNujiPkw0eRiHlPqHePWwVJjl5ifPygSFZj4Q6QyRM3Wq4RiHPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آهنگ جدید numb به نام مادورو منتشر شد
📺
Telegram</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81434" target="_blank">📅 20:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81433">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">این که ترامپ دوساعت قبل جلسه با نتانیاهو میاد میرینه به نتانیاهو یعنی یه کاسه ای زیر نیم کاسس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81433" target="_blank">📅 20:10 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81432">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t07LfgwdayMdJE76F23ZfFCQHD2ERQUg9uKcA9qjZwzlhDQImGNendXi4rXMVpgtrDUOxeZ4UW_mNChl0Z7TAESeDdF_ohziPqqbpmOnDh5SegFoTkZzLatwkRE4nEgm-COGP9yMFTGOIEvTjtqsVnaoktVuJrgEYn3oaa3dN--EQSsRpqRg9tAiVDptcBsLw7GQx_dX2HNTxmQYTayLgIvqvDIcyv9EpfhnO8sPpJd8W5zATUXQoFMm8tXCV89sGYBCeWAHIiEX9OeA4VEK3pOhWS4GmWRTUHu7mdkQr6QijlZoLYONWZCYVkuYiOewms9yQXKVgWwjTs7ugpq7oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این یارو تو فصل یک عشق ابدی رفته صداسیما
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81432" target="_blank">📅 20:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81431">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGpr2toYukPMY6FeNtGOcps3stEPFG_N-fcQxKU6e782JNJ5F4LpsrVoJynxz13NHhRcqbKqOZXXHxjX-n2XImtEE5oJq0haNJACB2itAKfto4FF2zYr987Ege9ZKGNcRXBkY0tdrZiXJejiT-H_vdlR7DBYAB7SmconhHJNKE64H3fzXRjLxLT4oGDoyJM32ea4BXoEx3Vv_-q4TLMotR2FPefxuEtaTYSqqHbSk5Sl60ii2mxCSRUZe2r97ALMb-GNtKc9squi4ySPhQ5d8RLz0rKoXMhHWn_FsWJAzzbT-enBeYaeswV3t7NP9SI6_mORqma-2FCHdc5PZizRmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو و دو تا از طرفداراش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/81431" target="_blank">📅 19:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81430">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYjb3dQuRgXTM1TA9nVpnQXkFevEk2P69DnL40OjirMhZ4nJc0T6ZYaCd-b5c2qwpsj6-YSEY_GgMXOt1IHhK0wbvLLncmXNWO3vf1ifeE7lFtxNrkL1j8c9ed3VZ6asj0fOWQ51mGpeD5ym7m57sAqbYigYwnbR8Gx9LJ4QD2o42W_9wB_W3f1wJ2ZahPLyTv7hyz5IZ8oW3jVaSttmALNzLP3zwqQOnlttN-_5-pi60Rw6iKtwAzgpozp5xxYrqIY-7CLctJy1M2L14GqcWeIjHNLECKDFJBJGX3Z7NZ3uf_pH69CSB7PYaDEB1X0JpftQtY3zvX2vvoL_z0dFQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توپ فصل جدید لیگ جزیره
🔥
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81430" target="_blank">📅 19:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81429">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDDUqxYz3naTXvpLSGfr1dxnlrqOMQnx0P5-6G-8awtuClvjdCast9mDTYWG30Z_SRGD1v3Tf3k6sVXWZYNsvmNTzEqxFK_hozyGHA7Y8WHWiVo-Duj8SczPlk_5qQnyf_K_tvlHJ_6srMwpJt4m6mG_XVeaXAbAKCBSoMMnibSAA83F5PLklyJk4c8zoxIuZrh5naeQeal6jnG1s0AabpjZUmLI-4E8jFbOuiUJ2zVDUIp66NHlZ_lV68Fo6u9Jqv0C4tWSMSnT2fvHNafZRAx7d_jenVlAnc0ffb7StP3Jy9DK7Rfex0tDmVDijfIsazZtDV66Qkxb_GJVjq1Gmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرچی بگم از طنز ماجرا کم میشه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81429" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81428">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvfGLUc84gqzK-MEPfZCFhb9P4EN7ZF_YNDjfMquwWd3vMYRnE8gb0IjXh7pXWDtrBWgsMr9CaFwmE0kus_-X-ViDmQnyuxcj8iNru4_hILZvpl9O4yZz5C_WkN7KXsHh2XWezgKEj4q2v5QzErupalCsjfuNHRpIydp8ujej0EMiNF6cuXi8_WDOOGcCPmH2EOzP3cZCaHmtYr2CuRlJFe0ZvR2uZqQQHMN49RnS2lruvcGamZ6bKBRmsd3zYWxeb48qIBdDfnErZU4LNG4A06p4tdd_aoy3J8Ii1ChVxGhQzP8_nGfJq2bzg43IGPT8ukvBlcc8aOVS5A4-IRQdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81428" target="_blank">📅 18:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81427">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/81427" target="_blank">📅 17:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81426">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">به گفته ایران اینترنشنال,
قائم حسینی ، امیرحسین ملکی
و
علی دشتی
از معترضان پرونده‌ی میدان علیخانی اصفهان، به زودی قراره اعدام بشند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81426" target="_blank">📅 17:41 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81425">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">احتمالا امروز یا فردا سپاه به اوکراین حمله میکنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81425" target="_blank">📅 17:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81424">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jv2t5FiIchHDcUR0mjVdh2cb5HxXan87cC0HeEi5egnKT3fzxhywBc3hrAvZHzawMo2VjXmaeggZMMUeR7flvHoVGN22_I-m8ifyVBWgtudsqcX7LQcQEceokcWbIKZ6_AUlNg5aEdX7ZdLqZZNz6I3Hnd92xiWTNUsni3dsXA6Lp2V62fOFRrEIGCR-QPQatnhUo3zs0ZVgCk4YRzgavsWRPn4EJqKdCNiIJJevPHAhkSDS7lHYoATZeY5id6nn_mNIOEDEdXF-cR57VbQ3UwCC0jyFAXxrivuA8JAXz6Aje9nAqpe_9293qWaimemF26GaKrk4-BoLvMjharK92A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو خود سایت کارزار، کارزار را انداختن برا بسته شدن کارزار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81424" target="_blank">📅 15:26 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اینطوری که روز به روز اطلاعات جدید تری نسبت به زیرساختایی که از ایران زدن و زیرساختایی که از عربا خورده میاد، فکر کنم آمریکا رو فقط در جبهه کری خونی با AI شکست دادیم که اونم ترامپ اشتراک طلایی گرفته داره همونم ازمون میگیره</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81423" target="_blank">📅 14:23 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سخنگوی دولت: در طول جنگ ۴۰ روزه ۲۳۰ میلیون متر مکعب از ظرفیت تولید گاز خود را از دست دادیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81422" target="_blank">📅 13:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81421">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">از سر شب تا صبح ۱۰ ها موشک میخوره تو خاک کشور
اما به اندازه ۵ دقیقه اذان صبح کشته نمیده
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81421" target="_blank">📅 13:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFBv8Z2RfWaR8Y6EmsqNbTS-oILnj5btCKh2SK67zqZohu6RBkdMkVElT2j1FsIK8cbMGXz3T6YIQ2gS7UsJx2UKoHvXhQz2FKrtuazPXEjYxUOZTRc3RN55AUv48uEA7c0pCHK02jkGBsOxF_L6MSUtfCVEXjlKPKOLiP9Y0CiwqSEG5FuZlnJP10_pYiocAeekypDbUdz6ZMh6V2x4XAGOyUvJZCocmIIJXBO7KWvWH3xN7qUMGpX1D5N29LqTWY1l7qWLvGB5DxEH2vI2ZEAcJg3vQDUrHIFacfXmnXuXDY2THqTaGdyCqmyDjrR9squuCgJ5u8mrXxOCxcWnEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OI62XiRKzU6IH0Rc_0k7-c_Sj5FV7EK_-RLB70fFjSFqFoKrS17DSTPtBMD0NXNDPj8vGUERo7S0CRVPhbpKeAbkbRPG1WzjaWKE-qCZcmDP-cKwSsmYgE_1aIZ8C51dskuH3AEkj5gmBd_cLImeCOlKDXi8sjqM4iwGPiqtMI1QxJC0fb_DAIOaB0bOSDNDM2KwWpha7_j_oQBir3FBbEBxRz1oSt7cYqXiKjnatiKWmkZKwE5RQXr2r6xlcFk-VEIPATOPbS2O48TSGjwQsKoE8xG-ZpCE9GrQ7LFkj29PjwDCPO-BMEXBfTlDr_hYXvlzYp2fVah36Bt2vGSPHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی دیگه از پیش بینی های اکونومیست درست از اب دراومد.
زلنسکی با دوربین کنار یک کشتی ایرانی که داره کالا حمل میکنه، و یک پهپاد هم بالاسرشه
چند روز قبل اوکراین با پهپاد یک کشتی ایرانی حمله کرد.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81419" target="_blank">📅 13:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81417">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LwREszABPVKB6UNMgSrYTnhthQ59XCbDs7mjmTtqXXg3JtMn6zRIzDHTvRChvT8wTlIP57yxQcXeRNWKQhTXox1adSHHMOYgGupsGMC6UyVC_vqD06ph5b_iR2y7WsAPGmgCa-LIWWLFwiG3ovbY_iMUSjb9aV7HK4uZALYNs5kFDsLFKarQUmlvgn3cSWIz8Z6hjIsDs7XXmRotOhz6Ack1q_t56vxdKZIcOWeeqUmUs-SJRwezt_-zrNZ_neYCut6EhulqPet5ifYkgaXiXlS_wN9Pb1oZW5UhghnOue2TF0Djmzvc53gMZm-FN6Nm8maKLEOgPou_YoVcDGoeBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eZeBhtkX_W99c_IWqfL-ieF3TjtZdcX962CplzGMcK7waZa3f1FZdnKf2D5Gfd1Iu0F0nIJ42L10WH3eSK5ZnwbmabPjSwNpu06RT3IkNe9xeyiqTPKto5b4fTPCuZtWyRrCHLzW1DuHSkCmwrrwx_78NZ7tSnARP_dX4tq1-BhqEaNMXSLdLVKzxfaGSW8E2YFBk5cFHP__j6vjURsn4rgMYH4PEjHfqTyZpMoUbxZei91mXYy73EWtbKZ-Rhu7YyFEAgjylf9oBbz7ayROT51Xe-8KjPxJ3aYAyLlDKm7DGoh7yqSIo6LkQomyZuek0T_UcmkRkHNtVlW1aFYsqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f171036de.mp4?token=eZeBhtkX_W99c_IWqfL-ieF3TjtZdcX962CplzGMcK7waZa3f1FZdnKf2D5Gfd1Iu0F0nIJ42L10WH3eSK5ZnwbmabPjSwNpu06RT3IkNe9xeyiqTPKto5b4fTPCuZtWyRrCHLzW1DuHSkCmwrrwx_78NZ7tSnARP_dX4tq1-BhqEaNMXSLdLVKzxfaGSW8E2YFBk5cFHP__j6vjURsn4rgMYH4PEjHfqTyZpMoUbxZei91mXYy73EWtbKZ-Rhu7YyFEAgjylf9oBbz7ayROT51Xe-8KjPxJ3aYAyLlDKm7DGoh7yqSIo6LkQomyZuek0T_UcmkRkHNtVlW1aFYsqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طقه پوبون رو زدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81417" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81416">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XkHHXF-ZZpk5jajO2fU4Rs-eR8pNO1w32hoXiQiSaAtxEoil-EOvp5nAmYmJ0NWcYvALlu-JgTaRMDdFl3KCWaJPWt--DCFYJ4yKN2LKP2bOjBFJPOaFNWdFV6dmL5Q8HJubhEx2i1_Plk-luysUcexAOjtDZ2jok0kiQbjk731yypQR3Qe5KAWZZSu8vzdfM5n4zaZCjSpyLwnvG8wfNXymF7dut895634S5hcRB7XPQYSujyKfmEgyu2iCAerDYLJwxO8MVbAxyJoYS1gErYg2LxCGpuUUvgK1xsw-E023bNy30fVe053UeMNBkVqBK4q3U8x6teJStm9IcBUPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رئال مادرید
🇪🇸
-
🇪🇸
لگانس
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
سه‌شنبه ساعت ۱۹:۳۰
🏟
کمپ تمرینی رئال مادرید
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
رئال مادرید ۳ بازی اخیر خود را برده است.
✅
لگانس در ۳ بازی اخیر خود شکست نخورده است.
📈
میانگین گل در ۱۰ دیدار اخیر رئال مادرید ۳ گل در هر بازی بوده است.
🧠
برد، همیشه عدد نیست، گاهی آرامش است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r6
💻
@BetForward</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81416" target="_blank">📅 13:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81414">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=ZvFkhpfFPsHDpuky3dS2Y_tEBYRbt9QDVb0H-9dkJs2nNdXVU20JLTjunb4jwfNZvLdtKeMmWlPo_Gt4YzXA0_C3shl7SjvDbOKYy4jJCAby4uY5EpTS66BKpBy290zK0ZmkWPAPBni5-dmphU4sjhy5tWkt8qSX3PiJhap52j8Zs0Qp8seIYRdDQG8ceF_ML56qOLLkBzVZ9OBh4I09WhBYwV7oOTqUKlE0iKHJCmeCCb4HLJ9rwtvSzlCxBd6RgoBX99npST06Hd4nBkKShcDjx9VtyMuF0BI2tH_K0Yd2FW8GCoBVX6McVkiCXxyLcrc-1A2cHHlgkEbGD0MC0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce9ff43bec.mp4?token=ZvFkhpfFPsHDpuky3dS2Y_tEBYRbt9QDVb0H-9dkJs2nNdXVU20JLTjunb4jwfNZvLdtKeMmWlPo_Gt4YzXA0_C3shl7SjvDbOKYy4jJCAby4uY5EpTS66BKpBy290zK0ZmkWPAPBni5-dmphU4sjhy5tWkt8qSX3PiJhap52j8Zs0Qp8seIYRdDQG8ceF_ML56qOLLkBzVZ9OBh4I09WhBYwV7oOTqUKlE0iKHJCmeCCb4HLJ9rwtvSzlCxBd6RgoBX99npST06Hd4nBkKShcDjx9VtyMuF0BI2tH_K0Yd2FW8GCoBVX6McVkiCXxyLcrc-1A2cHHlgkEbGD0MC0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی گرامی کار قبلیت چی بوده؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81414" target="_blank">📅 11:11 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81413">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">مگه نمیگفتن هر زمستونی یه بهاری داره هر شبی یه روزی، خارتو گاییدم چرا تموم نمیشی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81413" target="_blank">📅 10:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81412">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE6ItjYrSfV14hkGf_6v5UnElAPnG8eg5QUW-oLKcIIzDuVu0_-ZI0_bIvKsHHpXOV_7Ty5rGAcXWze1QuLHR3ZfwdTVj-1wVQuQCBQcugpDf7cA38MXz2JXk23OBSWVg96TWH1ApaWD5wjzjvhS-Ms3pLCrLouTSeRgvGV3hceKGvCIa6eye7V_SzTw2y_2odg5jf-bnOe73NGBQAVWAKeQuC34HQEMVkx8Ym3r3Cfczx8sxjDGDbko-Xq2b8w9jpJkvivNVPLj_vMkv__Iv6EMv1OFraAojaxsmsdKeYWCCAaWz59AbpAOaNwn4RgeZL6OxPGKK7Y7JMI-VbS5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81412" target="_blank">📅 10:05 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81411">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">تروخدا فرزاد قدیمی رو قاطی زیرزمینیا نکنید، فرزاد اونقدرا هم کیری نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81411" target="_blank">📅 08:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81410">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">خبرگزاری فارس:  هر سه نفر اعدام شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81410" target="_blank">📅 05:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81409">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">خبرگزاری فارس:
هر سه نفر اعدام شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/funhiphop/81409" target="_blank">📅 05:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81407">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">از میدون صدای الله اکبر میاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/funhiphop/81407" target="_blank">📅 05:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81401">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">درگیری گسترش پیدا کرده میگن با ساچمه چن نفرو زخمی کردن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/funhiphop/81401" target="_blank">📅 04:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81400">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اقا یسری گزارشایی رسیده که مثکه مردم و نیروها درگیر شدن و فعلا بچه ها اعدام نشدن
تایید و تکذیب نمیشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/funhiphop/81400" target="_blank">📅 04:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81399">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مخم کار نمیکنه نمیدونم چی بنویسم
فقط میتونم بگم تسلیت به خونواده داغدار و ایران عزیز
شبتون خوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81399" target="_blank">📅 03:58 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81398">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nZTYtepZEP8g_id58PgRZYZljhXxbSNGKvLYDeH5bfL9ykkkRq2ybGkWEm1Hx40bHTzkMBlDbEfmq4UcTPIC6hfankkbpRh739au_2zHt_brl3bWfc0UYzD2axoebfb5YIns9JTJCPNF09kOvSK3tApTVNLJcynczUYHYkwSLET4htX0qmitsAP4FKB_Cl0V5DZcCYHSU9aVaY1HAPGi3THAeXvBpaCuF2Pp91H3FVfU4ytxcO1oO_pdNMzOTizPG5t8kfxoKFVoP2dRUvh4FvIkV1hRou22UDCQbDVlzkeWHPSPnlccELMI8sjDF7qLR0BOVKo7LvEiRHOBYDE9Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کپشنی به ذهنم نرسید کسمادرت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81398" target="_blank">📅 03:53 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81397">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اذانو زدن
🖤
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81397" target="_blank">📅 03:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81396">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAryk0C7tium3g3RKYcrVVltL8s1s_3O5G02YBLg-pqJKkPAcTu5WsO8xdAnRTTX0Ze5Xb-y0jf0RSMgvUIJSWPEhjrOY_hWrgzkhAToKOxUF0SmxEkh4f4qvN9kqTE_Ih4qKANWdBO6eIkFQSYXMovalNRxyFVSbv8RdwBcvgNljsZnYHiFWwwicfUBlnuqKeNeck_7qwPmLFNdC8PHogTTvGh1U5FNM-AM_uU3TqyuOJu7NPJwoBaSifsO9OzsUPbeO-CmrIEKd5zscRAA66zrkcjIOTYcuvKUZvQ754-BF-YZP_wJevVQVyVBZCoY0oRi57myn9pkVN2VHzWF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81396" target="_blank">📅 03:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81395">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اذان صبح امروز اصفهان ساعت ۰۳:۴۲ به افق محلی است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81395" target="_blank">📅 03:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81392">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e358934688.mp4?token=mlBPg1I7S2Srd1ZjW6p--kW52Z3VngPYfEpj-XjBwwVPbM4fvvZg-ddyfr5r3EnDdc1oFpHv34JD7YG9bryiIyNZzn-rxG0FiicFfJ97pXdCOzQgkEg9MyaxvR6cPGvzkhgeBLaoUaaFS9ea_MzrjYiGTnBPKjI1nEpre8ghOOWe8WojvIPipT9t76GLbye0KZlwljpjb-XOcWp9oirmO5Zep5MXYxpoLsWEZW-TsnhxO-M4mhy8c6RrLbSaX6evhIcrsuy6TfKfApttog3pMJMvClQCZ1_-PiEMiQ5pQyikcxvC-fQ0Jssqk9vkcq1aMTpH45o6JjQK5asUVGPm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e358934688.mp4?token=mlBPg1I7S2Srd1ZjW6p--kW52Z3VngPYfEpj-XjBwwVPbM4fvvZg-ddyfr5r3EnDdc1oFpHv34JD7YG9bryiIyNZzn-rxG0FiicFfJ97pXdCOzQgkEg9MyaxvR6cPGvzkhgeBLaoUaaFS9ea_MzrjYiGTnBPKjI1nEpre8ghOOWe8WojvIPipT9t76GLbye0KZlwljpjb-XOcWp9oirmO5Zep5MXYxpoLsWEZW-TsnhxO-M4mhy8c6RrLbSaX6evhIcrsuy6TfKfApttog3pMJMvClQCZ1_-PiEMiQ5pQyikcxvC-fQ0Jssqk9vkcq1aMTpH45o6JjQK5asUVGPm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81392" target="_blank">📅 03:08 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81390">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">معترضین بازداشت شده با اسکورت شدید مامورین برای اجرای حکم وارد میدان علیخانی شدند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81390" target="_blank">📅 02:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81389">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64626deb37.mp4?token=alSjh3vKfmb-0IQQ3viXat9-mgQSOSpecRgGd8qRQtlbv19a0Yl16xmaM4wnCqqNs0_iNeeLMfCJkULilJA6JXWmDZ_rcCTx7R-B-Rfnrljf0crtbR-8Us6y7q3SH4p3cLKAphMBK3Q2_rc3hOPxdw_Tka96rZZ9-EdL39bojAabNrDQN-v9FUGnJSOKfg_r0UH2g0ZYyp1XEPbpfLoM1M5D6cl54XMICho_T6dQSXs5VLGfJb05gvaWhQC-Sinjd_qbo6Ivx0TuFPqYTMq-QuaECdsPfKFJLzrpCMjmnKAgur0U0nHXZ_AUosuGTcMt7fPDyk7LURR9b2_SX3tOAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64626deb37.mp4?token=alSjh3vKfmb-0IQQ3viXat9-mgQSOSpecRgGd8qRQtlbv19a0Yl16xmaM4wnCqqNs0_iNeeLMfCJkULilJA6JXWmDZ_rcCTx7R-B-Rfnrljf0crtbR-8Us6y7q3SH4p3cLKAphMBK3Q2_rc3hOPxdw_Tka96rZZ9-EdL39bojAabNrDQN-v9FUGnJSOKfg_r0UH2g0ZYyp1XEPbpfLoM1M5D6cl54XMICho_T6dQSXs5VLGfJb05gvaWhQC-Sinjd_qbo6Ivx0TuFPqYTMq-QuaECdsPfKFJLzrpCMjmnKAgur0U0nHXZ_AUosuGTcMt7fPDyk7LURR9b2_SX3tOAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس‌از اطلاع رسانی کاربران توی فضای مجازی، جمعیت میدان علیخانی اصفهان هر لحظه در حال افزایشه.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81389" target="_blank">📅 02:31 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81388">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YP_mxLHj_lHtscRnnpTvI6-q53kThsBBPtU_v8_1lm7kCKy_trAfNLgNZRT7sCK-aMKG6oimWcF83V87ZOXHlDwEJRHfq7nr-uaovyIiVtTkHPgiOtrQatGQYDKWoqt4aHcoMatTOA9DOBynAk69njxnsMm8wVADRzvTZaxaFdZpOpSWPyX1fu_a4uj8FI0SX3ODV4Lr_3izkKEVk5B1N-jNcr4KlulcMKESCSKxwlwPqeBDErHCzqMfxkuydMc-rYzNaEKXMR5UIXfkrxv6JKmC-ttNl-ObAjvAJ4oREBA90SGH6upCq6q5AUwZXMW_aGy2AKIBWBmDdn-WYwOoXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این لیست کامل ۱۲ نفر از بچه های معترض اصفهان هست که ۳ نفرشون قراره در ملأ عام اعدام بشند
۲ نفرشون هم در تاریخ ۲۸ تیر اعدام شدند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81388" target="_blank">📅 01:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81387">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eHu6Y4cFJTa5yjVzO9yyHAfghKhVO3GUxlvIY_xLdeEJGSkxtJ3B4nU9SZz6e1JR2msn9ANS_sFlFkQtf9i7j8AL0I-6sVdoM3Dax5U7nT52MLExGxHG2S-724sonAPmhBtNu5Hm_0ooMPMGiUV-6ZIrYa_3DhfJEyThacmoqhIjctXx5sgUqf3kLW-yNGWqxxuRIJ0ev79INMqkL2sROvPWNOnjzHvMajlaDvrHNqsMxkt0kAVHnYbx3OsCxVhnAnNTAaH5yYw3hKGYduVQDQGhatB9MIYeFoR9xCOa3eu49B-wwY6Am6IMIA-Iu99hsBpUvw_l8YWGLdQIsDvPqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این بنرو تو میدون گذاشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81387" target="_blank">📅 01:34 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81386">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81386" target="_blank">📅 01:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81385">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jD_MKXVbwKoZjLHg-6xBhF9pNAoAKoTyg3Lqm_bwLBM_D8H_cc5djmTmUOFhqTAu0JJs3MFQ-Y6UdWJpwoPvyR5jVfRAmAS1ENIOXUdB6yE7_LI-LWiUdVse0cXJsTVscPBKYylE0ViXZod-P-OiEpBBpiRKq3iVCuWwwcbKzWKsnXRN5h8qwKLgRxOoF2QZtpF8nHLM2mg4matLVAwzv4d6Vnq01INvfZTkQRmdWp4grdNZnsk3OoQHcx9vK59JIzX42Zdi4MEV9p80zBy-ppA_fzdSteY5ApMz1MBtrVgtT84YXqxJBICiZ64rTugoSbdRRwxXHeBwrwu-gzkXcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروهای امنیتی رژیم تو میدان علیخانی اصفهان جمع شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81385" target="_blank">📅 01:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81384">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از این ادمینمون فریب که شاتای پستاش تو جنگ ۱۲ روزه تو کامنتاس از ۱۸ دی خبر نداریم  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81384" target="_blank">📅 00:53 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
