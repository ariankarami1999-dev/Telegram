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
<img src="https://cdn4.telesco.pe/file/sld_673kh4cqwRQ_Uzy2UAs81Pb5pRvql94KTohnG722AylwY5UnsKifTmoMmd-L8VdBEWrtI9ONXOByhjciG3EsXC9Muv2DXHA_kNJWbDpcbRa41k7B-PNWRfZHYWpbE_f-Yq5Wqq1vfnJ94ZU695b6OF-OZ9q1tYDzdQckzq5l-hOAXh_pc6i0E8IIa7QUZ7L1-zIY68houllLR9VXRZX_VTAFNeal70Nj4fMbjO40QDHuWdbl8aqO0XhHHZPh_bcjqvcGj5NRRXbwqNilHA7quNHLBh45JhnPsz2FHPW8nQsHVK_NbKR11do3IPZnT4-o1SmtneFOClhlWThQZQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 198K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-20 02:22:22</div>
<hr>

<div class="tg-post" id="msg-79974">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رژیم ورودی های سایت طالقان و پارچینو باز کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.85K · <a href="https://t.me/funhiphop/79974" target="_blank">📅 02:12 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79973">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrogxpVbzxRXtzXbO9Yb3t3ksWa9W5mBR4U2nnA4re64fNTFsBzLPy2lKkM5e61drUp2f5L2ts9yfk5iJ5dSEmounr3_6uIvMyrkMVYh9su0nsu7sPcpyZMPa8yOi1WMMjVjqQyYYDOYhB2FYXAQMd2ThUM-TL30nECQXrdZYnKUjWmBuoDKFwCsFog7jkh9O4k4QqWr36NW4HsAbQCKzkOIFRhz25qVIlbb0AOLlNazmmea8-jz8_NIYys8yF0wUPUk7pyUwOjVzh_miyAxc7MR2l-IXu5NhHQNRegIr8_JSN661_81krez078jHap4HJje-Hm7-892MKEXhumMiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس نمیدونه چرا این پست انقدر ری اکشن "
🤣
" میگیره.  @FuunHipHop | Constantine</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/funhiphop/79973" target="_blank">📅 01:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79972">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">یادش بخیر ی زمانی دنبال کننده های رپفارسی فکر میکردن ویناک همون آرتاست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/79972" target="_blank">📅 01:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79971">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کانر میزنه یا مکس</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/79971" target="_blank">📅 01:25 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79969">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uGYufaFmf8ei37Pm5QCqsNeSLYF-MNWAg9lclLxXN0x7Xtvh8WQVtMeWzigFtsbevdEPdIucUlgx5S_oQQHJEY0692y-DigO5hTeoRTxuDTIlyGL1H_hpljnMxp2k1NmGmotFCKligXATyHMCvalUsjSziAyS2ECJrL3ij9f7AG45OyUbwgMMNZwMAe-vRkZPCJDReYHf0mdWRG0CVyUydLenn7a6uyrzIykpsPUS20KVUrUYEP7_LtfUN8JLeha59iSRLoGIUNWBgHswLUtCippzFHAVESSMOJK5Osq9m2m2-H25_kxJvV-NSRNQs9IIUXc8wPCfDdKoztGsf2MpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YlAda7j-uTt1nf_gqdRF1F_hX8Pun7aW_qmUzPRSaDaVZk1VbnqedGdsogXPSgCggTALRReMrrdTxGOJoSbeGjzVo5nwuFDVIpCES36iw7Sp3KL9MRkNgkCgPSKrDo0TuMvv_GHnAeQI1VnnaNrkOXw7cGBiqCHM70wNClWmzoGD0evoSEq5b3xGnT-9vYT_T9GkeSvSfpoPyzo_yJvNi_w3k4XhmB2cPjsZenmNT5o0le9JOhVlnMoO5K8hvRZ__vMRc-FzryeCVn1yCng8Fy9GgaJ_UTQFByQAldtxQYQ_dnbfEsuyqdQvp7HDN6IM6wr8ngw8MxpzRa4G_ATO4A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داداش یامال خداست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.65K · <a href="https://t.me/funhiphop/79969" target="_blank">📅 01:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79966">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/funhiphop/79966" target="_blank">📅 00:46 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79965">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/79965" target="_blank">📅 00:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79964">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">توضیحات کاگان راجب بیف دکی و ویناک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/funhiphop/79964" target="_blank">📅 00:40 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAshkan Kagan</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd4c7da62a.mp4?token=v7toSf-mljfeonMn6NuyZI4-84YW43qRdw-pIw8roYb2QtaDikrPvOAT-wk0WvyORrajVkYGDdlQqitL8Wf48VvvKbnCEeNnWWX8Hevq0e7FbIwwFr__ofaNVFHEHKrRG4VOxpx7X03YV7tjDxYbmg_wekOc-HgrK_yUlpgDF1PChoR8cNfHhr1Npgf9VjGFc6-ITENc5ktk4rUspQQ3bkJQF1xBElEvxg26VAuV49GxIpV3Pty0PmW8ppbTjoR0NF5PxIf58sTbNb4XeMy1CBfNoVpf1nicc8dlkTLQOtHWGPl4tCmmTFD3T8pDFdEhgUJzKU7VS6teF4sOhtHnfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd4c7da62a.mp4?token=v7toSf-mljfeonMn6NuyZI4-84YW43qRdw-pIw8roYb2QtaDikrPvOAT-wk0WvyORrajVkYGDdlQqitL8Wf48VvvKbnCEeNnWWX8Hevq0e7FbIwwFr__ofaNVFHEHKrRG4VOxpx7X03YV7tjDxYbmg_wekOc-HgrK_yUlpgDF1PChoR8cNfHhr1Npgf9VjGFc6-ITENc5ktk4rUspQQ3bkJQF1xBElEvxg26VAuV49GxIpV3Pty0PmW8ppbTjoR0NF5PxIf58sTbNb4XeMy1CBfNoVpf1nicc8dlkTLQOtHWGPl4tCmmTFD3T8pDFdEhgUJzKU7VS6teF4sOhtHnfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 8.26K · <a href="https://t.me/funhiphop/79963" target="_blank">📅 00:37 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">دخترارو چمن و مهدی بردن، فمبویای گوگولی مگولی من بیاید چنلم.
https://t.me/+cPimg8CRJ19iOGE8</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/79962" target="_blank">📅 00:35 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">مرینو عجب کصکشیه
😂
😂</div>
<div class="tg-footer">👁️ 9.52K · <a href="https://t.me/funhiphop/79961" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این بازی اسپانیا خیلی دراماتیک صعود میکنه مطمئن باشید  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/79960" target="_blank">📅 00:20 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79957">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79957" target="_blank">📅 23:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79956">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">این بازی اسپانیا خیلی دراماتیک صعود میکنه مطمئن باشید
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79956" target="_blank">📅 23:21 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79955">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بلژیک به پرتغال زدددد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79955" target="_blank">📅 23:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79954">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">داور به حدی به ضرر اسپانیاست که خیلی واضح به اولمو تنه میزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79954" target="_blank">📅 23:07 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79953">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دلیل اصلی بازی ندادن پدری اینه که دلافوئنته احتمال میده که بازی میره وقت اضافه و از اونجا که پدری قدرت بدنی کمی داره و بازیکن ۹۰ دقیقه نیست نبودش در وقت های اضافه ضربه جدی به اسپانیا میزنه
برا همین ترجیح داده تعویضی بیارتش به بازی که ضربه نهایی رو تو وقت های اضافه به بلژیک بزنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79953" target="_blank">📅 22:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79952">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">دکی بیا پیوی چارتا ویس بگیرم به ویناک فحش بدم فور بده چنلت فک کنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79952" target="_blank">📅 22:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79950">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کاگان اون ۳۳۰ تومنو بگیر بده تتو رو سینتو لیزر کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79950" target="_blank">📅 21:58 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79949">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">این وسط که اینا دارن به هم میپرن من فقط به این فکر میکنم که اینا اون تتوی کیری رو میخوان چیکار کنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79949" target="_blank">📅 21:57 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79948">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سکوت تونی وان کید این وسط خیلی عجیبه، کصکش بیا دخالت کن دیگه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79948" target="_blank">📅 21:51 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79947">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">کاگان: لطفا نگو من اینارو بهت گفتم
ویناک: حله خیالت راحت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/79947" target="_blank">📅 21:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79946">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بقیه ویسایی که کاگان به ویناک داده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79946" target="_blank">📅 21:47 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79945">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79945" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79944">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/79944" target="_blank">📅 21:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79943">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">قطعه گم شده پازل کاگانه، شاهد هردوشون برا پانچایی که میزنن کاگانه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79943" target="_blank">📅 21:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79942">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قشنگ معلومه چند وقته آماده بوده، موزیک ویدیو اینا داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79942" target="_blank">📅 21:38 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79941">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">این بک دکی منو یاد دوتا بک کصشری انداخت که اول داد به پوری و بعدش بادپولی رو داد  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79941" target="_blank">📅 21:37 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79940">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بابای صدف سپاهیه انگار، فک کنم دکی چون رو زنش کراش زده از ایران فرار کرده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79940" target="_blank">📅 21:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79939">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79939" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79938">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromVinak</strong></div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79938" target="_blank">📅 21:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79937">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">خلاصه اش اینه که دکی میگه ویناک کاگان و دکی رو فروخته بعدش فرار کرده ترکیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79937" target="_blank">📅 21:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79936">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دکی راجب بدهیش: چاقال تر از اونی بکنی اخاذی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79936" target="_blank">📅 21:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79935">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یه نشونه هایی از دکی قدیم رو دیدم تو این ترکش</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/79935" target="_blank">📅 21:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79934">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/79934" target="_blank">📅 21:27 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79933">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/79933" target="_blank">📅 21:25 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79932">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/79932" target="_blank">📅 21:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79931">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oXyA66pBEtXB_34_rGTqYJxZqYBHtA0HD7NoVMSHPfDkIbWoH992WqvsV-YIGfer6CRDUEcwrMMBBMgnefFyXCtGRkPe0b61BsN92F2z8JLbFuxRCejM0uua4WE8E9cZqw-LxNX7m0HLXCZ43abPHGwme39KjOUjAsQiSjl72gCvHe1AchhPXw_hPucZMU2LUTPiOoXl5cfX1ZXZpQRrY0gEvR-7bT7_s-VOaGtaDBDwZJpIkuPJwBwUvd4JkkXlzOFg9mbgSkNv-gxharRd5eFW4TfwBLp5Y56VpCVGiC6g9ycGRo6UAU9CwgxYpQ6UWBguDgYm4DRuaXucB1QBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید دکی به نام Plea deal  منتشر شد.
Youtube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79931" target="_blank">📅 21:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79930">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">همون بلایی پوری رو سرش اورد، این دیس جدیدش بیت به بیت پانچه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/79930" target="_blank">📅 21:22 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79929">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دکی دیس داد باز</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/79929" target="_blank">📅 21:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79928">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLKGOiDbs9e4Yvkq0m6RMHLSTWutdCpC4vJQnp4M7-CFF2401lb6En4O_HOeibuTseZrfjNgvHg9wzh_3mbUia0X5Sp2bO4lqfsW-eSKzOGmglrcpmTu-0OPUMYgeh4vTkUCj9HWaO2DKSFr92pmREBCHX3vtX9IBnjKiThyXPd0AIHZLfH_0F0BTm8LjIsBD_Tg4obYDaogRwSMzFWA1XzvheyHa6kB0SnWWVAafWdB_M-wGWtcqqfl6Vwd7JLGwIsjPM3fbpNit6NplWUfrlJx7Rnyfsw-3lYMf9YYjjD5Pl-86QhRNOv6f6rZumpubIbUiVohhCuAJdvBkPZh7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدری نیمکته امشب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/79928" target="_blank">📅 21:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79927">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromKhode Khalse</strong></div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/79927" target="_blank">📅 20:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79926">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gGYYnRHrRQO44wPPduUMGkogWIMpHGdTwwcWzceY5-x7aJsyrYVnt5-lFnGmlyyYU5HagZmsNAI4Si9n0waN2tA3MDaFALLvwG5gpsJZdvXie4PAsjQ39R0t4ik9QcB7_pB5CNULfgnqreSSEwSX16wb_mIoDnFTUV0OyoDrO4YnH0k-03fEDz_L49-ukgx_T-MzV4l-9yZCH-9jh8UCjSDLDYROcd0w2KG6PaBxJnzqWNWy8lGS-RUl1PZ6TuDi8w_lZ5jlRu35Qkg7A-N3wForPolqs7jg1FCByfXkDUjjbJxCpY4nZmTV58jlWMVWS0IVBWXXUuVSscXkk_YsOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمیدونم شاهین فلاکتو یادتونه یا نه ولی گفتم بزارم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/79926" target="_blank">📅 20:18 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79924">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsWVfOz-mRwC1kVl21p2hjLwft2xic6xe4UzF_TRlwSPvgBP3lu47jOU43ipDo3jwrZz_dey1iVADawwNp6Zgi1a_WeqqS-St7UwrMLXDZ6bnrg91bAto8vp90slJawt-5uPVpUKnPCiPXHO0MXjGjfpCh1KpEySntUiqgu6_aPXJwkGszEcNeRr8-kriBm8oOl-2b0JNJd0DMcbyY4It3J9izzreV5w1SaYiQPsQgIHlv9TnzYEgQsbnQxfWt4bBoiNfiNZEPWK8oNTe41efFwhQCV109uOlgDcjPIqb5gN9HQxIrTpWXXVr1gi0AWa1MmZ6nXRHreL5VddlEWFoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارسا عجب دزدی ای کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79924" target="_blank">📅 19:49 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79922">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برای یبارم شده چیپس لیمویی(ترجیحا مزمز) رو امتحان کنید دوستان، مزه بهشت میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79922" target="_blank">📅 19:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79921">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79921" target="_blank">📅 19:17 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79920">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">این کصکشو تروخدا
جمله پایانی ترامپ در مصاحبه با نیویورک پست درمورد ترور شدنش توسط سپاه:
به هر حال واقعیت را نمی‌توان تغییر داد؛ امیدوارم دلتان برایم تنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79920" target="_blank">📅 19:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79919">
<div class="tg-post-header">📌 پیام #53</div>
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
😂</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79919" target="_blank">📅 18:50 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79918">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGavNKFElSSC4p5CKFbhRJ_JzVtEEbjjn22HD53bNAIY17tLEojAsfbtfyLBfUvMgIINfaltLEKPE28Q-xcoDAE6uRxnNSlKuMT3T0NSCDrXHC0UlhQko4PATWNrRf6FdstqpW8MAwEB_RQ836lf-phC5vcPdClMMUWpMuP4Ww7FUkofg5Toye9FHPfsq7e5AkEDwPvB3gwkHx5gobxr2zc-mETa-qTYrg21Mhxp_MrZvTHtP2R9ESSFhuGNRb_FojbvJu524CUn-xyGmh2Imk_G0FCc5LatwdK5158E-eaFGDob9YJQHNqi0PeNundjSrUXEzrw6AA-_y8Vz_ysjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک چرا دندوناش انقد بزرگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/79918" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79917">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tf2d4hIhBbCP_NKNuIrBL8d6kYsVP2qzgJ3t7RWQfTlEydeEmoO2IKhK0Md7dZk_uuYaW6aCWGBmC06BQRlr9eI0mC3V-2lO-nXLkoqFP7ktelyaq74K5Nqhz4mfixLXvA1jtlZI-tlFvfrrMsusWDXbgirk4CeiqppNlF04stFyoBlhmv16UikaBiV77PfeOw0Vi3Z_hg50NTeCNW6K6IRXWWLOvWFZYd1-rTRPvns1kGGEOd_oBntWjR4fVb1ZTztHRpPo6ygwvPD_yapLvBs1jFd3RokGkHus9DPW6MqplI7_I-vsGcrLSCrYxENb8oPmDUvxzEbzjgRtcK8YUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79917" target="_blank">📅 18:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79916">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/79916" target="_blank">📅 18:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79914">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ryEQk6ZStOD-sYT9bJvragiVKNp2oSYTHjp5fzYZq8KiCVzuIzrZluTUPo8XAE6FZrqefcd_3xstmaWOUD2BjC7LXYFNJTkIR8-ltYsFYiimKfuTw1P9I9m3mSTXVLe-7ehzU8V9y-Ghxh8VCb0xZdPjsorOZv5nYlGk7XhjQgK2DCpeP1aKdcmNNXvcGjvPG3MNlBWM1J6JryvgXhE3_d9H_J0HqFsKMKt7SPBaoXSKMUBLgP8YZXxVwUHc4dgNLnmh8I-yCe4AnXi6lsvmR-ejL5usdF53JIxJvqVrw_1mtASlSymv3QVMY-8LZkfsptEwr7Ncumfw0df2pbBNuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/twgbAWrvHK8eommxu_jqZjyokIOlfnC8izrFp9RInQuzuHTHDM8iixBWtnyfONTsCIXnbHnEmxf9HIQU75pYchP8LDQH9l6Ihe4AlS79Hb7JDEaVkBCOwwlfWzCteZggjmQsSny6k7Lxj3LUTbSxyniGoQT9HlVieuUnhBTlESEdanFt8RCn4VQOhrvYKHhOU0dZFfl6DHqT_6RwEFMSBRA8Y7_KcMOr9cHwjJHQppt_lqu__P3uIZaJoT2RqkjvmzV2oQG8I31jr6lkqqEWd0tN8dxwOZY39IvExhbNZrpQUxuq0u9fIt0G2_u_4ihhYiM7JdrdLdzNgdmc1gYGMA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترامپ درمورد احتمال ترور شدنش به نیویورک پست:
من دستوراتی به ارتش داده‌ام – اگر اتفاقی برای من بیفتد، به سادگی آن‌ها را با شدت و شدتی بمباران خواهد کرد که قبلاً هرگز ندیده‌اند.
من مدت‌هاست در رتبه اول لیست ترورشان قرار دارم و این بخشی از زندگی من است و چیز جدیدی نیست.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79914" target="_blank">📅 18:28 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79913">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">هه  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/79913" target="_blank">📅 18:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79912">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ریدم کنارک همین الان صدای انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79912" target="_blank">📅 18:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79911">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qpFxLEJtGL0K-uO5LkE5QEzmW1uytqFslABCq0yjA17KNnOr7ODPGkkMw7Sutx2FReQHUBLiZjFfeMODJlpfFuV4fDAbSZy6l8jb7zPBNSwKrQcUEP6IiQVBPbdz5in3IkwRafW05QFb2WPWSLtyaRFwLEimSkpy_TQHF3cq28vU60wXecwZ4fYGVm-k5uoJAN8EkTcb5f74hpVMbrtifaZLm4ydp9eFBNdN-M2xI5Ntx6MFrWxwW2EZT-0zq1kvGo6n8TQWsYwIbPa_g_q9y2d7un9brzyt9aUsIXgSae9W5UxBOzBGx080LrQ4I-pqizgoKpYYK7cZJ-EK71nsYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هه
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/79911" target="_blank">📅 18:15 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79910">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVlTUlhIPUkrkcK-n1ZPdYonpwIFShGRzrpPnM5i0sz_Fs0E5P8Z4irgPvmkQrD75lgT-8QcIwJCPjCmE45IJnCkiiEGjhr0kA6Y0mQ5vql-RAXY_Qc8k7ow1AqJGM9ljMCovFFdlh6ocHqloQB_-C6IvzafecQn9OXG071IDrvSkR6WZXkNI7HvYRcsFHUGSxDi_phr3ct2ZZlLicxDZn7tMcvHdwsgwsN641mQTiDSyS909DB_SumsoxmJ1EBKGqZIau8u-U94D3L1e1MkHwJA_hKKTOr-WzKkLu75tgVh0SquTwjNVlSgztSfbnF72yGnqkbZFVtIquane5mQzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه با همین ترکیب هافبک و خط حمله اش پارسال به اسپانیا باخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79910" target="_blank">📅 18:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79908">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N0rJGZSaTcZPXO4fvXPsX4LpYl6GTt_fn2hyXHdnVA19ku2zv8-Zq_VO-g54fU1gde269nLIMS28AHLbkto078gtb4Srpv3ZFkbLMvb7eR1kvp5xAqA5YNrMKhOwhuqfVNp7sewYPICXLC52jGL4XcwmG9U1uLvrtM1M9PsCf80bGad3FVQugGLcopMcSDZ3P4yar2w-m5fTtnEx4IYwPd4xOYAFvGt9G49cqtMHX8wWKQyGk2IifKPT0qHzfDHYHFjayZ15Tk4mHEvZlsoSW7O9BWB-wE313Hk5mb9thxQQDAylRv_sKC6TDsBpGTQBLzMC3ox_OKxnO66ZcwXnBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dX3mtONa6Bgbd5NHTq6Coxa1-EvMU95qSoPh5OycipYD4JO9z94oLdNUOidvBs8NHa5ORssUvVfWxs_Z5PrQnF1R9cSGJtKATpUui8gLqqr0tOXViUBDms_gA_Yo6dnPaGrS-c0lsH3AGPkjJb9rvAmzujN0eax5jAHqKBpQEFHhVj6ilheqw1IdUkYGxhIaZnNBgPVWi0bVCubfqNoUnsvLrmV2ownvWXlOlj3J_Hh_TsgFnqLhR2MxHezESm45jcOLP0f1lgj-O9T8veM8Sjc3bCe7dUxhDGX3pR4Hr_lOq9YCLIvxz0D6oON1SFrRqY22jDmJ1Rgv55FQkaa2-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">داره بامزه میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79908" target="_blank">📅 18:02 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79907">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">پلی بوی کارتیمون کم بود فقط تو رپفارس</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79907" target="_blank">📅 17:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79906">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اینو کجای دلم بزارم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79906" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79905">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTijay</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/79905" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/79905" target="_blank">📅 17:42 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79904">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WvsGZsKkff2RqQ3QFy1Ge20pigfWh3xkS36V2GkCYK9azhhqr3EHDOSrTuE1-c4JJSpbR1STs6Hr9qAcbJAPbTIF8dFj6dwEH-3zGSVKVtYt6TsiqzYBt3IIoyLaw6MmsfW0McjCAMaJDQxJxJwZ45wbGC3t_eAL1MMFfL8TzDXbNtw364UZ7tOg0jZwdzEtKocRatZ1lnVrsxGZbNOhHAhjwMuT-T7jNQ8zk59HYzt1N1dmRoIn1Lx7LQYvEMb02EzCItqZjsfQSV2C8Dsc7MGu8F5gxCsb-LPqXrByflu6RySziApNd6OrufTqjNBsKTjnLMkX9hO9Q7J4v8K2eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کار به هیچی ندارم ولی ناموسا چه تحولاتی تو مغز انسان رخ میده که عکس امام حسین رو میگیره دستش باهاش عکس میگیره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/79904" target="_blank">📅 17:40 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79902">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxlqPGOpwddQVgBj5IS0HdVXNYPX1ObKs5WhIv9skF57WmZicqGWuNfkAaR3PQF8WdbmVokFHeorZcuI6UEtGZBoqWHRKP7A5Lv5vw3_iVixnxAdu-S0AkzkIpShy1u_21_T7S2M6d-_z5Ztyp5vVQtBA_wxTGJaTEIhP1wnW_JXHd1koU-zC435XuaWYYtEnoTM0vc4zQK2fqa2aJokMZ-JDH28umIXETm8mwLbosbjcc-RLX1LACs4366OgvCfd4izEJn9HIEmz6ezZdSFT2QkPPtgwzVRMDNpkEGHxmt985QEN7iiFthn6mZAjGgDO5cx_gijQ_yGZcuLz8oXhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0434cdafe2.mp4?token=aHFr8QQVLzK1cBfXLyePzjW3phgToCrYHt-gWI7JIDiow8vrRmRoaIOz-uCleknAtdWZcUZ2HWuE1nXvyd__wzhuHdUZ-rf58yMMzC-_tm8zVgOaqy07yOEEVEydqlUKXm58OYQwd_2aL8EInfuf62jqmyqQgV87k9DSOX3LkvWcovq1CVqxjGSD5M5hkOLT1y68ZIscMPeCaJA0MATTf_B3CrKRDrgNDJcK4bUSvFD7SAQ84WXUa1kUi0mZpeatqR4tUXLiGDtYqk1cn0Xse3Jil8El6YRJB5rVbHSXsxqnjTxMBM17npk2HDCMcxVG-6FH2D6bpfqL-ZN4WjbkBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دکی هم اینارو پخش کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/79902" target="_blank">📅 17:34 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79901">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBZpwAsINOJ_DvVD1wh_1YMYxFoFarGCy4E6R9V-DJPGLrGYVDnLHW1F6yi7gREEH7YN9jbeakxNv1zGanyquqbjVmwVdCzjuTmywXZQlVnHBT7kh_y-vMgbHiJJhymUvs78gVFkZnacVwvFeo-1sl4mhsG2oFO_AuSUzbo3x4tGJpbWfMrczhjYbfH9BMEw-HJcOsTWmAUfhf-8GszWnfYFJDpEEyz1yCIcOs2eWi4o8Gd4ZKzYwt2Y2ngxSWrtZWQZaXUN8YQaDKVnNSZxShPqeRxffr-A_i3OrSlnDSfEBFPkxEw1bEKuJhgpH3kJOTuPUhTtZ88oVymbzwirgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسی که ویناک از دکی پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/79901" target="_blank">📅 17:30 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79900">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkIA0EVJWPANxYp10Ks_Hr7tZ8xvcZEQ5wn5-IV2XNFDyxqMeL_UJbkAAToYwqSNA-1XmsOwEyHE-G7XWIrvKy7eEQWd0PDj_SkzGnli-F1iFNn_3eMSvFKcsIpDhIkGFNadH4R84zMlMi0WcxAgd5LDcGp6TJg0ejNRiI49O_poY8UAUpDZV9XOdy_G2S-T1bZPCJQLUyxfBJz55keY2gsYbOlJ6GA3JusaTv4i8fDnzfQaeSlyx9kzBfBOiCRC8AFOd7E_IyWDhkDU0Kb15fJx1onznjUZeu9ocrOUmNSbp85vbgN19Oc6zPQbrQQPTXrjA1cinV1tfCKlDfPMGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلاد
👌
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/79900" target="_blank">📅 17:26 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79899">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">کباب کوبیده با گوشت گوسفندی نود درصد تخفیف به همراه ارسال رایگان برای گیاهخواران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79899" target="_blank">📅 15:29 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79898">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79898" target="_blank">📅 15:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79897">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kmuhE8MPaGrXQPBzFgRmC_UWIsH-9cvl8LqdufW35KyrSqARMlZSozosp7z2UGhatTs472klR0PoQHzW7V0Hw7fzHiS46mBeFjGXDqOAMGThVo6Pqu8ERfEY0-mjeRji7RuCL7HWHslcQ0v7ia-vSp9A8EVmFx9qMu-Bm47_EcrEtw9N1x2z2pHRqXiY38dnmzImb6phEKAipwd4mt7VrmYwCoIOPNY5Iak8dhu7XrS4717UiqIqrOpsOFN2tfb2MwrZWBIuRWbwD7PnQT3zIh-SbaICblHvolu3biQNCYaOsoq8cqrJBvDLu20DK-EkVPIwmU6TIKaXY8JFRR3BIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79897" target="_blank">📅 15:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79896">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده کلا دوساعت وقتش مونده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79896" target="_blank">📅 15:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79895">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwlOk1HuzXQ_d9ocwZfC0BCl5uSvSGN-pX8wWgK4j_EXq1ZKr9UtJCkBBsg7_U_MpUXKg6-iE6DNxUGrHXwXHi7WvEQ5XVr2M7_yyzdJWsxZCN8rg9sWXIJmPktbkyuEPDOAdeFrpoFiki2AccUZEIqoFROrdQ345SbYTY1iGOqXI84PcR9bA4Grq7zcGwUmZ-wLLJkMbn4AbcDfrNoN9iakBUrwpsa_7h1AseMSPwcE0ivupTTZXyGOgVjgZ5eNRZBDNwEonuo4ldozaGTpHDD5p275dsrOaIhJFktNIxgiea5cOTfLpd24KebPDFbLyqjTpGPA5dlmWRTVC4l3qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریع برید اسنپ فود یچی سفارش بدید که رو غذا هاش ۹۰ درصد تخفیف زده
کلا دوساعت وقتش مونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79895" target="_blank">📅 14:59 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79894">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79894" target="_blank">📅 14:45 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79893">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">رنگ شورتشم بگید دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79893" target="_blank">📅 14:36 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79892">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">یادآوری بدهی هیپهاپولوژیست به ویناک تا زمانی که تسویه کنه، روز اول.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79892" target="_blank">📅 14:16 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79891">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ولی خداروشکر لا این همه بگایی و دغدغه، نهایی و کنکور ندارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79891" target="_blank">📅 14:00 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79890">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بیاید بگید ببینم وضع زندگی و حال روحیتون چطوریه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79890" target="_blank">📅 13:43 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79889">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">واقعا بیف شاهکاریه، هم دکی صدفو دیس میکنه هم ویناک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79889" target="_blank">📅 12:33 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79887">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rWMbzC7RS4i1bhmDnhO35Aw5CetNszunZyimoyx4SvHprLTQQ5Tuxw8imJRKtzwPBy0yMbTe-J-LNI9o9DLlnc9cr8IoB0MwdytWwFb9XY0eKNxJQ4FHaFpeTfFZTncP0KHzlgEGvmxCsoAp210aHZ0goDE0ZH7DATQ8NuTcNPbQ_TPlS-CdhZTvwbALMWrHPzxsxsSosqcGCBsb6AZ_2B4S2cXph2I9Rop55rE1ho8E22NjSwPdtxyE1aT0to86N5oSbwC1iz11EngrUuuqMHKZaZ94ty3aH15p8dnALpoDmC9uC_IgTR10qpC6izNCPmndeAfDdlv4Gq-BdADRvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=TCMPtbOJOy86CyMbqUhvWRhMguO-kfXXXwRrsCCLcDEK6U0y1Ujsn1DRYFbcAFxWrX09ehXWID3CV8scqZ9r5FlF7lqu14NhUWvYBtMytQrJY_HoERkV9Vjnsd3wlGOWnzMLBNTJv_P0Ncgq34aFJ75j3uPGaZdh5gMyQicfoUgedKkFoy1L4eh6KRPh7MYAjmMTArVGtdBAZ9xwHxsyCS0u1TRhChgvjbsLn3mnujDNBn802PM2mgV8I30vC5LjsSknzXWoWJYtrTYs59V8OHDQXYr0kqBj9_M9tVsh5YI0NFfMAfHkB5rbr3nZyiYIGzk43ngBPQmfWt6VkDeVBq4MAT5RpVrEHEPTKCGJ8vpeWf1GuHxji9z9mZ_3bnDyp9Qj9Bn4WyF5n_n-cmnbQM6WDmzDynn-K8zvEEjVryVR6X3DaRSUdnUMIKqbRPnrJKNvrHLi4DI2YJFwHrQsyOKXAI9tRgqxRI61fZ-woicIIJMYuMBGs991Y_ZFGFnvpw_J9LSZWsYLOfVwf5OXyap2aQp1iRycylCr_9StClmZSGxo10s-P0KVTQ6rjlmkwnYMhcBPJpjop37-OAqwq2poeao20R0_iYOoFBgcKwppEfrsVGqhhb2xJpgwcdMlgjVilQwAs8N7gJD7xldXnFRIkXHuR_WP2xekVfvxwd0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5748e213fa.mp4?token=TCMPtbOJOy86CyMbqUhvWRhMguO-kfXXXwRrsCCLcDEK6U0y1Ujsn1DRYFbcAFxWrX09ehXWID3CV8scqZ9r5FlF7lqu14NhUWvYBtMytQrJY_HoERkV9Vjnsd3wlGOWnzMLBNTJv_P0Ncgq34aFJ75j3uPGaZdh5gMyQicfoUgedKkFoy1L4eh6KRPh7MYAjmMTArVGtdBAZ9xwHxsyCS0u1TRhChgvjbsLn3mnujDNBn802PM2mgV8I30vC5LjsSknzXWoWJYtrTYs59V8OHDQXYr0kqBj9_M9tVsh5YI0NFfMAfHkB5rbr3nZyiYIGzk43ngBPQmfWt6VkDeVBq4MAT5RpVrEHEPTKCGJ8vpeWf1GuHxji9z9mZ_3bnDyp9Qj9Bn4WyF5n_n-cmnbQM6WDmzDynn-K8zvEEjVryVR6X3DaRSUdnUMIKqbRPnrJKNvrHLi4DI2YJFwHrQsyOKXAI9tRgqxRI61fZ-woicIIJMYuMBGs991Y_ZFGFnvpw_J9LSZWsYLOfVwf5OXyap2aQp1iRycylCr_9StClmZSGxo10s-P0KVTQ6rjlmkwnYMhcBPJpjop37-OAqwq2poeao20R0_iYOoFBgcKwppEfrsVGqhhb2xJpgwcdMlgjVilQwAs8N7gJD7xldXnFRIkXHuR_WP2xekVfvxwd0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من یه سری سوال دارم جدی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79887" target="_blank">📅 12:23 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79886">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79886" target="_blank">📅 12:13 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79885">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">خبر بد برای دبیرستانی ها: آزمون‌های نهایی بدون تغییر و براساس برنامه ابلاغی از ۲۱ تیر آغاز می‌شود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79885" target="_blank">📅 12:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79884">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">یزید این چه کاریه آخه.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79884" target="_blank">📅 11:55 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79883">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=k_2xlPOqRnxoobXM4eI4JHe99P_3x_MS6Y83KW5NiYgdu_hjI10Wte6Hyke7dbKUxjVcEimB_IyYdyAqWVctTdR7-bEEsC9mbQApd4pjWADvSiwP9Oic8OCBxhu6-qcDrtowHGGwM_zM6WIQo_t4S9_4oR7x2m7KgESvOnN6VoQ5vhoBdddaavPvRtqjbE4t9GnSeCIzGrmITNlH-eMmsVtkQXDn1eMxWSiJpuyRcIXuM_e0Rom0U54J6OdGw2UBxqMniYYMrBXz-Slze4sHkH8V9dp3yW8MZwQ9hHfderKTkseZXvHEyOnus6eTfW4c3B4dQrxKQOKfyIbtNF3LPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5db00a79d2.mp4?token=k_2xlPOqRnxoobXM4eI4JHe99P_3x_MS6Y83KW5NiYgdu_hjI10Wte6Hyke7dbKUxjVcEimB_IyYdyAqWVctTdR7-bEEsC9mbQApd4pjWADvSiwP9Oic8OCBxhu6-qcDrtowHGGwM_zM6WIQo_t4S9_4oR7x2m7KgESvOnN6VoQ5vhoBdddaavPvRtqjbE4t9GnSeCIzGrmITNlH-eMmsVtkQXDn1eMxWSiJpuyRcIXuM_e0Rom0U54J6OdGw2UBxqMniYYMrBXz-Slze4sHkH8V9dp3yW8MZwQ9hHfderKTkseZXvHEyOnus6eTfW4c3B4dQrxKQOKfyIbtNF3LPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یزید این چه کاریه آخه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79883" target="_blank">📅 11:41 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79882">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">امروز 18 تیر سالگرد اعتراضات سال 78 کوی دانشگاه و ماه‌گرد قیام 18 دی ماه هست روح تمام جاویدنامان هر دو اتفاق شاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79882" target="_blank">📅 11:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79881">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گنده گوز اعظم بعد پنج سال برگشته که مکس کونش بزاره.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79881" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79880">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IHQYvdlM_NzUDPSmnTKM3NMu536b12ZXjhQTEBk7_1DjXdJFBQzAFYMYFTc8vuoW9HjZs2Qp8sllvBLFWwebju4ijIN71RH3TbkAY0JILb60PkOGvvUEhl7ziZO53Mg_DCcfmvMhdxW8tRS4DN9S-kpjZJv7mBrp2TqWJfD7ffmtqJhH55Fv2pbOJtithJLVrttRHhBJDbot2K6Q98Oo9nHSXaVHllERWnx0fhmMbI5kUiuQBe4k6412PggjsmEbsyJBtkHqTBvP1L_aF0Wnvv_xi98x38imWSSszEkGxp67IpW3EI6u1Vv7-04XggafTnSNYyPjB6wEg7-6NbaRyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
اسپانیا
🇪🇸
-
🇧🇪
بلژیک
🏆
یک‌چهارم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
جمعه ساعت ۲۲:۳۰
📍
ورزشگاه اینگلوود (سوفای)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- اسپانیا در دور قبل در یک دیدار دراماتیک با نتیجه یک بر صفر پرتغال را شکست داد.
- بلژیک نیز در مرحله قبل آمریکا میزبان را با نتیجه چهار بر یک درهم کوبید.
- برنده این دیدار باید در مرحله نیمه‌نهایی به مصاف برنده بازی فرانسه و مراکش برود.
- با توجه به قدرت هجومی لاروخا و هافبک‌های خلاق این تیم، برد اسپانیا گزینه‌ای مناسب برای پیش‌بینی است.
🧠
هدف سرگرمی است، اگر تغییر کرد، مسیر را عوض کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r19
🟢
دریافت سرورفیلترشکن رایگان
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79880" target="_blank">📅 11:12 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79879">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=KiLLYXhvdGvtkTqPS_pdfiLVDEoU0fuTz9ly-C_gRLTRUcc4VHjEUc5p3V5p0soDx5INn7eKhaatoia75TxHfqEPAMpeHyEYAGMJc2_eg-gZPbDR74R4cpdn_YKFr3WohRt0WqaNyWp40YTJL_5adGu8ifiKJKsLLar6DAUV3RCN7Y6Ie2K-7_scy7OJp6726Y2JsCDN9GeKsme2AlDw8p44Q7wIuKecYU_V1XZfWVx2sU7Bxv-ravGKR6QE-oWwhFiwEVUgTNbwMKweZ8GVvg9vjC_u0FuirK9KHpWubGYjJKuDS7yuxRXzCiz1r3w_GKkxAZhYEiAPOnlpCwe6sA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7d7f15171e.mp4?token=KiLLYXhvdGvtkTqPS_pdfiLVDEoU0fuTz9ly-C_gRLTRUcc4VHjEUc5p3V5p0soDx5INn7eKhaatoia75TxHfqEPAMpeHyEYAGMJc2_eg-gZPbDR74R4cpdn_YKFr3WohRt0WqaNyWp40YTJL_5adGu8ifiKJKsLLar6DAUV3RCN7Y6Ie2K-7_scy7OJp6726Y2JsCDN9GeKsme2AlDw8p44Q7wIuKecYU_V1XZfWVx2sU7Bxv-ravGKR6QE-oWwhFiwEVUgTNbwMKweZ8GVvg9vjC_u0FuirK9KHpWubGYjJKuDS7yuxRXzCiz1r3w_GKkxAZhYEiAPOnlpCwe6sA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 5
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79879" target="_blank">📅 08:48 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79878">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بعد مرد مومن به صدف چیکار داشتی اینو خود هیپهاپولوژیست تو دو تا ترک دیسش کرده بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79878" target="_blank">📅 03:24 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79877">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اما اگه بخوام خلاصه دیس ترک رو براتون بنویسم: زنت جنده اس، بدهی داری، فائزه جنده اس، پولمو بده، زنت برام میپیچه، بدهی داری، حصین زنتو گایید، به علی ضیام بدهی داری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79877" target="_blank">📅 03:19 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79876">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79876" target="_blank">📅 03:14 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79875">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.  YouTube  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79875" target="_blank">📅 03:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79874">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aQray0u1MXl5fVTR0DC7qSLz3Pvg2Dsn-RHdLqjsJuNruYJeMqsFumLMrByWMiu3QuXqIXFHgHIaqhG9JdOU44MNWHS9E1Yls106k0SuERsOa-vAg-bNw8yIRv2X4Z1WP573ChTSs4Gx6O9egRyPjpCPu2iLdH8e2ZqlYIp1efAP6XE5FrtfYkeSTuZrLmjrjbIv3CjDWEBjwU9-zkGlKT-gQHpbN7C0v1pY_4EG_nrQ2T3yvIsx_IszOTq0pX0qzgg2eBQta7strpex3xBLQNSMo5AABtpADkitj2nMR5o0aj30CIpiEpRUn-VDZVRYNJwlu1-IlyiBIVsiUIx8fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک ویناک به نام قمر در عقرب منتشر شد.
YouTube
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79874" target="_blank">📅 03:06 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79873">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">دیس بک ویناک امشب میاد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79873" target="_blank">📅 02:01 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79872">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">فارس اعلام کرد که خامنه ای بعد ۱۳۱ روز و یک تور ایران گردی بالاخره دفن شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79872" target="_blank">📅 01:31 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79871">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">البته دمبله زد یجا که یه ذره غم و ناراحتی وجود داشت ولی خب تقریبا از یه سوراخ زدن</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/79871" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79870">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/79870" target="_blank">📅 01:05 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79869">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">کصکش یجوری زد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/79869" target="_blank">📅 00:56 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79868">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">امباپه میزنه
سوپر گل هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/79868" target="_blank">📅 00:54 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79867">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیس ترک جدید دکی به‌نام "تا دیدی سروش" منتشر شد.  Soundcloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/79867" target="_blank">📅 00:39 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79866">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/79866" target="_blank">📅 00:35 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79865">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محمد سامتینگ رفته برا تشیع جنازه تو حرم امام رضا، چند نفر ریختن تو سن با شعار مرگ بر سازشگر بزننش که مامورا باهاشون درگیر شدن، صدا سیما هم چند دقیقه پخش زندشو قطع کرد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/79865" target="_blank">📅 00:32 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مراکش عملا زورش نمیرسه طبیعی هم هست ولی فوتباله و هزار و یک اتفاق غیر منتظره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79864" target="_blank">📅 00:08 · 19 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79863">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">یاسین بونو
🔥
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/79863" target="_blank">📅 23:59 · 18 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
