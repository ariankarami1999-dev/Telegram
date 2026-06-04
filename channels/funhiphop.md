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
<img src="https://cdn4.telesco.pe/file/X_-e6lMsEVsGECStl2MxiYm7fD5NtfG667xkgdFURD5mblanx61_mvDNFT9CHpF3cB-0FOLg9ebGqwSypLaBxUod352XvDqI3NL7SQMl6P5fHLujekxhCn2JeZ_DOtXkhTfSFid1dGKXZGcCy8YG_lPZWnuZ5qH9auzhJXZ-q8sQ15AVg6ZlxoFiwQ6g8xgWzZcyywBagCuggXckN-KxulGg8lEXbvUJPdnn7kkl6_yRYzyjpz-UL6z50cGhlFAL9IgYaqXxr9GVB_w0LUNbHLYa1VTxz-RQ921WUYqBeee4XdsHJmnGfmweOci7pJgVe0A5yedV9cnJfHaNp9z1lA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 176K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 17:08:24</div>
<hr>

<div class="tg-post" id="msg-76839">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8fa7807d08.mp4?token=gMq8UoWynsKdiwTsQdr-9qs3ABmp14WhP8Lhf0Dh6zBCDmAxp3_6d31zkaemSMtnxkTGrbUzTt5Iivi096_eXFRsU424_RzLQ1FseqKTmq4o3RmFhjKXmo_PZpTS6JcY3VFBi2VwL8UGfxwI0e_mWeYIRZVuUIpyRhOqXNxVtgEEC_y1-QUeFZ8cfE7DO7KrHrx6vvSKN6diELd45_kfHB10fWrEK5g6P4owxZey7IUTSVZ7FRuUkv_GCZ-gRXlxjVLJhewitgsMRXmOjmI5WL9k_c9q81ENm-I9kxbj1fj7gM1zgdBWhVtf3ti5FLVqZe6AaG0LChQqrUF3Ht7s-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرایدی که پرچم حزب الله داشت با موتوری که پرچم جمهوری اسلامی داشت تصادف کردن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 1.84K · <a href="https://t.me/funhiphop/76839" target="_blank">📅 17:01 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76838">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">گروه هکری حنظله، وابسته به سپاه پاسداران انقلاب اسلامی:
امروز صبح یکی از مدیران ارشد موساد مرتبط با ایران رو با بمب تو ماشینش کشتیم ولی احتمال می‌دیم دشمن مثل همیشه جرئت بیان واقعیت رو نداشته باشه و تکذیبش کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/funhiphop/76838" target="_blank">📅 16:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76837">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اسپاتیفای تست کنید بدون فیلترشکن میاد بالا</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/funhiphop/76837" target="_blank">📅 16:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76835">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPTFunUHtoHcovF318j51xl5aWK63mSi33dZfNOy08M9ESFL5VfjO5FpguqPMKEAwBlRaevup2IKuTx3trgY5MXDQ1l26VTxi3GrKUCuI37buDqX4BOvdp3DrUksUDC7SpH3JR9nm8Svihaao1R43DkL6GSelMR-P_wS-CeT3fOj_aUtNyEqI7xrM7cNqCfiVwzQLQhK8cWt6-wS_8H8PS23w_m6EFPSKIojCfE3_6pBD64WFnn1prD-660npPAw98fTN5ojnllVSvvBuLHxFFv2CncmRperp9iMKOS4QpS9fjgXZ8dGgNnp_BdBQutLuKUNsFacV499iotyriU3Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتی داشت مینوشت سپاهیاوووو یه همچین حسی داشته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/76835" target="_blank">📅 15:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76833">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">https://t.me/+nm4DbCzoFJVkOGRh
https://t.me/+nm4DbCzoFJVkOGRh
ی جغ مهمون ما
💋
دیگه لازم نیست برای جغ ب سایت های پورن و فیلم های مورده و قدیمی بری
🫦
تو این گپ با تصویر کار و زنده ارضا میشی
🥰</div>
<div class="tg-footer">👁️ 7.35K · <a href="https://t.me/funhiphop/76833" target="_blank">📅 15:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76832">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">یاااوووو</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/76832" target="_blank">📅 15:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76831">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">پروفسور سید عباس عراقچی در مصاحبه با المیادین:
در لحظه شهادت رهبری، من نیز در دفتر ایشان بودم که مورد حمله قرار گرفت اما به صورت معجزه آسایی قسمتی که من در آن بودم مورد حمله قرار نگرفت و سالم ماند.
من آنجا بودم تا در جلسه به ایشان اطلاع بدهم که با توجه به مذاکرات روز قبل از آن، احتمال جنگ بسیار بالا رفته که متاسفانه این توفیق نصیبم نشد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 7.59K · <a href="https://t.me/funhiphop/76831" target="_blank">📅 15:15 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76830">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امین منیجر داره هد میزنه میگه میووو</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/76830" target="_blank">📅 14:54 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76829">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ی دور از کص خوند ی دور از موش خوند، ی دور از سپاه خوند، ی دور از بسیجیای محلشون خوند
آخرشم گفت گذشته ی هرکس به خودش مربوطه.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/76829" target="_blank">📅 14:45 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76828">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدونالد ترامپ</strong></div>
<div class="tg-text">ویناک بهم گفت نابغه</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/funhiphop/76828" target="_blank">📅 14:41 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76826">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.  YouTube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/76826" target="_blank">📅 14:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76824">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">رضا پیشرو نسل جدید</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/76824" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76823">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">عجب سمیه
😂
😂</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/funhiphop/76823" target="_blank">📅 14:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76822">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T1Xf9cLy19eiFf1OFx-fTVtxBMOr5cqf0R7MGYvCvdpnJYj6SKBrWsv0ckGze3mY8IVzZIjxXXpVsJLWWCQ-4W5E27hEnDiB9FQHSnUuJyart19SAngrX46kUjk5EPBNEd8Bq9cem37JoY-OYYydZpuTWZikfkTSEOGjZDJYcrEHcEh8zv1dJNEV5KT1qX1JbhfAkTJWE_-OQVrYBDUzefZRfWDdbTxpzHl97DHOHaNCRs9m2jJHJc_TwP16Ab-Mmu1gy4FPHy7beZo7A6Ui-wC619ZbXlhKEwQpE8fqak26vrK157McCxMKifEPnR4s9Q8rfE7Jvm4gmZlEJ59g5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید ویناک به نام "HANTA" ریلیز شد.
YouTube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/76822" target="_blank">📅 14:32 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76821">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ODODr8wZNL7nJnqRWYkVfKSc-FmsL2MOP0EX6jBAwGOKFmo8rvoAvdawkYeryfK_tTM_W43OXTAOwqsQZaddPq50sqKVPNuN7K2YtLBDfXp99n2Q7NNFXDAW9FSNOXFOtjRjoTSaFI0dBfz0HIckNeiKdtz5yzPyNdLZOYBJXNXZVlpuqwL0T8uxblp2aGcYEQNqr_OV8Jck-mxyUWaIjaHk2fXa5U5KiBKRpCfCFX6jwlQPDUIUPRk6S6bGqiQhrAE6aEpSkkDip4G_m1D-RXTbvm2q3nYVViJNnH2QJiBf-ggO94ZH3vzUR2ztS6E0Hk37FKs2m84N8xXWah5tdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید دالکوس اعظم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76821" target="_blank">📅 13:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76820">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">مجتبی جان ،بخدا نیاز نیست برای هر مناسبتی یه پی دی اف ده صفحه ای بدی بیرون، ما خودمون میدونیم در صحت وسلامت کاملی  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/funhiphop/76820" target="_blank">📅 13:14 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76819">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">متن_کامل_پیام_حضرت_آیت‌الله_سیدمجتبی_خامنه‌ای_رهبر_انقلاب_اسلامی.pdf</div>
  <div class="tg-doc-extra">785.8 KB</div>
</div>
<a href="https://t.me/funhiphop/76819" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/76819" target="_blank">📅 13:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76816">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hz4ZB4Zsp14g1iLQ4aNyh8DGrNaoHwHK01HM6kyl6EgwKOXegXUiowv4RV3NeLxHH2OvbvdnU8w5uP6AK5A_enmn9XodehIKBTONfFU7Oua1RWl4DxHkbDzeqHjWtR-55R_7pMm_NVaqX324KXcoL48B5kpR0SFFc1JmMQSfZ1ZSRFoQO7D9bH46E6vnKPi-SXRb_cpjUwuXhQk7QWGFXbsPoucS3WF98uxSiI29gO8evvCBdkQYxvwEG1GEINVFcs6Qm6pVt_6xVa-lII4fCT30DuTCEJ5igFhFsycXtIjA_DjCUbVUrmYT3UVw-PhP4k-jM9UD11jwL5cjwz8gHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تجمع دانش آموزا فردا برای مثبت شدن تاثیر معدل یازدهم تو کنکور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76816" target="_blank">📅 12:29 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76815">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76815" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76814">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">رسانه داخلی: دسترسی به اسپاتیفای بدون vpn ممکن شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76814" target="_blank">📅 12:25 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76813">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تون مادرجنده از ترامپ غیرقابل پیشبینی تره  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76813" target="_blank">📅 12:19 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76812">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">این مدگل چیشد حاجی زندس؟</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/76812" target="_blank">📅 12:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76811">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X9HvSSJgq5xv4_08gy67bB1oIUBluXs-aHjP8MqVcJu5dEux1E2eWL91lF6IrpzayNo4BmdFcC3ifNX_VFeETE4zONS-Zu6UCkfNX9SgC8MyECIKKBm79fIk5J5YSb3agJUMqYvxqv630U2hOk4tLFJSWAhvXgK9Ggo9XGveQLaNQdTRBwRemePZMu50nBG5r6gWMh6Wf5k71Df13nMhtPSjfaf3_wayP3r88K9OpW5_PRSH96NkRwHX38zRB9Jegft8BQLMhq0PI00UrC7TYCymjerRuABY420yBkqEH6_-LQ-QritMY-Nl6LLmgj_HkuRApdrSUCWr0cln42g2RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاه رپفارسی با دمبل 5 کیلویی داره بدنو میسازه؟
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76811" target="_blank">📅 11:49 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76810">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=scWxXZR5nhF_ttJmx0VO3GSTbO8PByzd31Sd4FMsyj7TaQdb7-pwlNbYLelYxIjvtJIYAvuZBJNdbducvlcLvAv2O-x1GvHLbujeE8tDm-aTKKuJjowEHufpMW7r06WtbbiYwB6Ao-_6Gl8Zb3pd39_WCX--76r0Rq0qtXRKnawINF0PSSlHxo_y6l4TuK8_0ijzI6sdFmKe4S_jFg31aZT_aoJYs9k02vC90SxgTmxdqpUcChvjVkCDE9mkVN18vCw-INEvbNcXgxcJGjPGYhbF2D_ovKYbvqP6h5UNjrUwzMtyMUlGI3KVnI0hxW3VDVzCc4wNn1KFpl5CcSW0YA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0a7027cb1.mp4?token=scWxXZR5nhF_ttJmx0VO3GSTbO8PByzd31Sd4FMsyj7TaQdb7-pwlNbYLelYxIjvtJIYAvuZBJNdbducvlcLvAv2O-x1GvHLbujeE8tDm-aTKKuJjowEHufpMW7r06WtbbiYwB6Ao-_6Gl8Zb3pd39_WCX--76r0Rq0qtXRKnawINF0PSSlHxo_y6l4TuK8_0ijzI6sdFmKe4S_jFg31aZT_aoJYs9k02vC90SxgTmxdqpUcChvjVkCDE9mkVN18vCw-INEvbNcXgxcJGjPGYhbF2D_ovKYbvqP6h5UNjrUwzMtyMUlGI3KVnI0hxW3VDVzCc4wNn1KFpl5CcSW0YA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فقط 7 روز تا شروع جام‌جهانی مونده.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76810" target="_blank">📅 10:33 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76809">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sw7bVnJ6lFdoBxAYBOkXdChQ6B3LovLinuiqw3HWtYo_K401DUdGiOekdsJcUe7ey2ruaEEO2ghg_cJt54b3LN_w5LrWe79pXsKxs_9zQPo0vOIFJp2e8TtDRhRFKY8s5--niwrrcoxs7jBaQRyqJvn604vI0yLd0oqTGMF3qeV_FM-SCoRcKnJT03CN-X17NoyCo83Ve-3mLRKCo-wnpV2EktMfC6oMeLoUtACuUfY8zhffsryW5w8a-Oh4oA5ZFZ_CCsqLyIk9I9YeiL1vv1R1sWh2_vIBHLpWppy_C7agOAT3x1DOAT3nLDHHCGPeedl8aT-X5UWbUmgWLilWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیبیلاتو نزنیا آقایی، عصبی میشم
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76809" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76808">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76808" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✅
اپلیکیشن حرفه ای اندروید سایت بین المللی دربی بت
✅
اسپانسر لیگ انگلستان
💰
اولین سایت جهانی با امکان شارژ و برداشت با کارت بانکی
🔹
برای ورود فیلترشکن خاموش کنید
😀
Telegram Channel
👇
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76808" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76807">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ll2TtrjZpEAL-bPJNsDar9DQz4u7CaTdU01sH7oMLU3r7xOtpq4eDo2pzPCrfpCamIaabHPujEayzUhJvl-fVeWj9nBelY3tjHgSZ77Fg0OyfTkru8mIVV_XoPYArBVmxlKUNeGfVpPQP9l8fFsMlEyZzFbSdhcaZQytVXxGu2-v7kCApZPiy9izTeppxaZ7hBlgKRfzbIGvs-IZpdKvBSIn8XuL3KbQ48-f-aFLkadnpZ3RZF3-aFpzxkPjPiYq49PV_FeAyaYWlzIoG3NYMuanpNMQdzR-K-K9CAKFYJ_5e6wI-iXt5WKtitt__DuedZZJw4Lx7mTqIL7pkUDneQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😤
دنبال یه سایت شرط بندی بین المللی بودی که به ایرانیا خدمات بده؟!
⛔
👍
دربی بت همون انتخاب  100%
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
⚠️
برای دانلود اپلکیشن کلیک کنید
👉
🔔
کانال دربی بت :
👇
r14
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/76807" target="_blank">📅 10:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76806">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">وال استریت ژورنال:
ترامپ به طور خصوصی به دستیارانش گفته است که در صورت
کشته شدن
سربازان آمریکایی توسط سپاه، «
ممکن است
» آتش‌بس با ایران را پایان دهد
.
بی‌میلی ترامپ به شروع مجدد جنگ نشان می‌دهد که ممکن است حاضر باشد برای جلوگیری از یک درگیری گسترده‌تر در خاورمیانه، درگیری‌های کوچک‌تر را برای هفته‌ها یا حتی ماه‌ها تحمل کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76806" target="_blank">📅 05:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76805">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آمریکا و اسرائیل و لبنان امشب یه توافق کردن که توش هیچ حرفی از عقب نشینی ارتش اسرائیل از خاک لبنان زده نشده و اسرائیل گفته اگر حزب الله حمله یا خطر ایجاد کنه ما هم براش می‌کنیم.
در عوض لبنان قبول کرد که حزب الله رو به عنوان دشمن متخاصم بشناسه و خلع سلاحش کنه و اعلام کنه که دولت لبنان هیچ مشکلی با اسرائیل نداره.
آمریکا هم قبول کرد تو خلع سلاح کردن حزب الله به ارتش لبنان کمک کنه و ارتشش رو تقویت کنه.
خلاصه که سه طرف به توافق رسیدن بریزن سر حزب الله، اگه محمد باقر شاه هم قبول کنه میشه شروع پایان حزب الله رو اعلام کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76805" target="_blank">📅 02:53 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76804">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e41fcdbb86.mp4?token=MBn-1Mboq1GZYsYz9N5iLT_m0gRllqe9jyatuum3Gz9Loywcy4jsN57hpPKBg7j0J9g_03d_nRNlh68aUwTvaSaTCYJaXD2ynn9ZR5p0F_4zvdzC7aTzTMgmpYEhTxrhcvQKtgbnWeZlWJyvlPW7m6iatlCNIfn-pRjyVh6q1pFx8AqVLyqQYIvbI842XHWxQ5VK1K_dNrc_YabetZXluBaVhdzAIF-G63Cmox_Q9Hh4uifBqpgQI6NQm9kiIhOUnuNxVaNfK236Yzng7TpcGO6F-ZfS4WCGSdstD8Egs_Xi5hUQPpGIWXiJCIC_-ZyXWRR4e6eFYu_GqE1tguJnEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دستیار ترامپ و معاون رئیس دفتر کاخ سفید یه گیف ساعت شنی توییت کرده.
رئیس کمیسیون امنیت ملی مجلس ایران هم زیر ۲۴ ساعت بک داده و یه فیلم از یه موشک ایرانی توییت کرده و نوشته:
خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76804" target="_blank">📅 01:18 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76803">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.  رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76803" target="_blank">📅 01:08 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76802">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">مجلس نمایندگان آمریکا قطعنامه اختیارات جنگی را تصویب کرد که به رئیس جمهور ترامپ دستور می‌دهد نیروهای آمریکایی را از خصومت‌ها با ایران خارج کند.
رأی‌گیری با نتیجه ۲۱۸ به ۲۰۵ بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76802" target="_blank">📅 01:07 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76801">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انریکه ریکلمه رقیب انتخاباتی پرز گفته اگه پیروز بشه در انتخابات هالند و رودری رو میاره رئال و حتی کیت این فصل رئال هم آورد که پشتش نوشته بود هالند و میگفت همه چی آمادست.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76801" target="_blank">📅 00:58 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76800">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=YVgRZYjg2B7oltvoqk2t5w5mZSg8BR3koAennoiOE4EHTCglXncVqK_Yzp_Xq3XNHCnjcJgchOn81eTLT0vAqP5CKv2SyTMsjZrmCbyW01Bc-rOWYDxx07S2Co8AsZi8DsWXZO8KrMi34Nd0BtJvmhGWKVDUoHKEfwq-ty6hmkXM7p5ckmyNyTWtpRlHgW-Wx42zxTmQ92PvhV5otFrsfyQBRRRSdNUxYFrdWsfyKYm_YaicaCCbnpd4fdv-oQQJnw17UOlPX5RUJAKsirWGgc4oaYlhuZI_iU47UcuWIrIhY8nLUE2VaXMcPKU2xQ8IypWFkPbv6S-cppMlH0vE8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/668e86dc1f.mp4?token=YVgRZYjg2B7oltvoqk2t5w5mZSg8BR3koAennoiOE4EHTCglXncVqK_Yzp_Xq3XNHCnjcJgchOn81eTLT0vAqP5CKv2SyTMsjZrmCbyW01Bc-rOWYDxx07S2Co8AsZi8DsWXZO8KrMi34Nd0BtJvmhGWKVDUoHKEfwq-ty6hmkXM7p5ckmyNyTWtpRlHgW-Wx42zxTmQ92PvhV5otFrsfyQBRRRSdNUxYFrdWsfyKYm_YaicaCCbnpd4fdv-oQQJnw17UOlPX5RUJAKsirWGgc4oaYlhuZI_iU47UcuWIrIhY8nLUE2VaXMcPKU2xQ8IypWFkPbv6S-cppMlH0vE8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل اینکه خوشش اومده  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76800" target="_blank">📅 00:38 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76799">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3LJ8EHoDWQ_9ZkYYJfe6qsByClLg5_W19PU138ExwZHm6ovzOOPElrj5Qxhf6qSqLxEtFQ246g7jWHNUBI7S7xkbEzH8_yAqrA3soBdYt0R34ltvaUs2WWyTnO_umi2nhRCAOM4feEVOSO4Kk-tQqEYES0ZAx16gZs8Mwb_9uvroWDPmtU4XdCeq0br-0bDr7F6lWLoZmEG6lwhXFToMPrPaEP5HTgk8L3QeNPsfJWVgxpIDASDYti4Vx2SxNjcFoic9UXxj5NSWDNr5UA7DicgZkKfECC_al1WZ74d-9CtemWcHxeIzyNoiOKrEHl7-BM979TshV03KteAib_O3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه خوشش اومده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76799" target="_blank">📅 00:20 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76798">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ
چند روز پیش اولین بار بود که با حزب‌الله صحبت کردیم.
قبل از آن اصلا تصور نمی‌کردیم آن‌ها توانایی صحبت کردن هم داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76798" target="_blank">📅 00:13 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76797">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ب‍  غ‍     درباره حملات دیشب سپاه به کشورهای منطقه: خب، می‌دانید، برای هر چیزی دلیلی وجود دارد، و ما قبل از آن به شدت به آنها ضربه زده بودیم و آنها کمی تحریک شده بودند، بنابراین آنها کمی پاسخ دادند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76797" target="_blank">📅 00:11 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76796">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ درمورد خاورمیانه: در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76796" target="_blank">📅 00:02 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76795">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درمورد خاورمیانه:
در آن بخش از جهان، آتش‌بس به معنای توقف درگیری نیست، به این معناست که شما به شکلی معتدل‌تر و کنترل شده‌تر به یکدیگر شلیک کنید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76795" target="_blank">📅 23:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76794">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JjsR8W6v5Uz4ZKPrQNtqKw3Dvfo1zUI0ktyugSdA1MIyjTrSSx0wlYEIfmpHSeY1_o5QhTlwdKRjgnnTpPQb9S0M69JbbMAmP9x098ppmIG27Ay1smKoH_dkneJbBwnr4YAk4NhaQXlWcgQ-cSiXY5AMrYp3Ig85zFXtqAowJlcuf1PDSekjC2h-7GSb_xGK9h86naSS7NPFN1AX9ifNVxrGEWWKV_oS1Zpomu4YysU8HYk3upc3bSb19KfiHMMZoYgzVj853XvyNzsQpuppWooHnQEFRzxqaaYJgVhMy9H5XPBTRIaG3NKyEFN0SqRrn6y0H2RRZSyeEhAUf8q7aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادر گادپوری نه نه چیز فاز و نولو درست بزنی هیچی نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76794" target="_blank">📅 23:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76793">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pen14Yy1qO23Cl3lDkbd_y087d4iyN0EajShT1IVj8BKjpVa1l-dlsVjBQHZCbh-P8TIhK3gdUugWtCdn8HuNB0Sy_vH6-cJK6EM9vw7_VoC-HgBH8RvIsJXxf1MrSaYlUAf9GKzGyw5B6xFSYJdwhKDlg2Nwbq3lOUx_xYdTX7fT2FClWh5vS1wvZ0pG6KdL9jN6eerznYCMvikTn3a5B_uyAD3KfJGs8aKiKNfJE24enFb5HD1dMyNZdqYSIItg_WpH81ZehOVULVUnSg9Jm0Knpy9EvFY8_8ZqkWF0YW3MjpErM21sVaxUNS85KwWq15pWz_AR5XpIWooh1S0XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚀
اینترنت بدون دردسر با RAYA
🚀
📣
توجه 10%تخفیف تا پایان امروز
📣
⚡
سرعت فوق‌العاده
🔒
امنیت و پایداری بالا
🌍
سرورهای پرسرعت و بدون قطعی
📱
مناسب بازی، استریم و استفاده روزمره
لیست قیمتی سرور ویژه
RAYA
👑
بدون محدودیت کاربر
👑
پشتیبانی تا روز آخر اشتراک
👑
دارای لینک ساب برای مدیریت حجم
⚡️
لیست قیمت RAYA
⚡️
🔹
10GB — 150 تومان
🔹
20GB — 300 تومان
🔹
30GB — 450 تومان
🔹
50GB — 750 تومان
🔹
نامحدود ماهانه — توافقی / ویژه
━━━━━━━━━━━━━━━
📢
مزایای عضویت در کانال RAYA:
✅
دریافت کانفیگ‌های بروز
✅
پشتیبانی سریع
✅
اطلاع‌رسانی لحظه‌ای
✅
آموزش و ترفندهای کاربردی
✅
امکان تست رایگان
🎁
همین الان عضو شو و آنلاین بمون!
📲
لینک کانال در بیو / دایرکت / کامنت‌ها
#RAYA
#فیلترشکن
#VPN
#پرسرعت
#اینترنت
#تلگرام
@RayaVPNChannel</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/76793" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76792">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=dK7L1dQ0uJvmxkgAgAdNwimTDD4ryNOYuYYO_xzpz6N68aPZizwlO2zegh_2nYg_nbSr3a1Xp7ykwK97njE_nxsIVyVU0HNzbh0kgY8wzeSJolHQRvtdnQKXTE6rRraFoTDT49EuJxJQNJsheDwmT2BwmoyVasZn1fMiKIYPB0AiMth4taX46_dan7m-_61TicHEXXApwFGzG8S3zXcPXHVNyhowRXXMcXgpSQ9Mu6-PKN7WTAyVksQ0eATM0AzBr10MeleXfS2fkhMMPppGGsxEnmWptolkhDRIlLHB56PbzJLXsw_Cr_c6Jh5lyTEp96Bq1t8KnCbONbg3vexd7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=dK7L1dQ0uJvmxkgAgAdNwimTDD4ryNOYuYYO_xzpz6N68aPZizwlO2zegh_2nYg_nbSr3a1Xp7ykwK97njE_nxsIVyVU0HNzbh0kgY8wzeSJolHQRvtdnQKXTE6rRraFoTDT49EuJxJQNJsheDwmT2BwmoyVasZn1fMiKIYPB0AiMth4taX46_dan7m-_61TicHEXXApwFGzG8S3zXcPXHVNyhowRXXMcXgpSQ9Mu6-PKN7WTAyVksQ0eATM0AzBr10MeleXfS2fkhMMPppGGsxEnmWptolkhDRIlLHB56PbzJLXsw_Cr_c6Jh5lyTEp96Bq1t8KnCbONbg3vexd7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فارس:
ساعاتی پیش،
نیروی دریایی ارتش، مرکز فرماندهی و کنترل عملیات‌های ارتش آمریکا علیه کشورمان را به صورت مستقیم هدف قرار داد.
ساعاتی قبل و درپی اقدامات تجاوزکارانه، نقض مقررات تنگهٔ هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به‌محض کشف و شناسایی، «مرکز فرماندهی و کنترل» این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک‌شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت، هدف قرار داد.
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی-صهیونیستی را رصد می‌کند و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76792" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76790">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76790" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76789">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76789" target="_blank">📅 21:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76788">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">مقامات اسرائیلی:
«برآورد می‌شود که اسرائیل در روزهای آینده به بیروت حمله کند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76788" target="_blank">📅 21:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76787">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یکی مامان روبیکا رو پیدا کنه بیاره فردا ببریم تحویل بدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76787" target="_blank">📅 21:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76786">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">خبرگزاری فارس اطلاعیه تشییع جنازه سید علی خامنه ای رو تکذیب کرد و گفت فعلا خبری از مراسم نیست
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76786" target="_blank">📅 20:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76785">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مارکو روبیو: ما دیگه عملیات گسترده و مداوم نظامی تو ایران انجام نمی‌دیم و عملیات خشم حماسی بصورت کامل به پایان رسیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76785" target="_blank">📅 20:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76784">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fOIroVZ3916JtirOc4l25pGRlUjOAse9B5uStfbY3tHvP-uM1PB89RuUGs21DgDYs3Bo_CXn3UZKtzyAcGDqMIRwdfeGEKgmNcQ_5uk0TBxty94DlFWk15d4qpjCkOCOX_TFCEJH_wV1oAcJIUwYetBuHSvADR5epkBVqyT-L4YCPxRP__L_NqiqaLQFVckfFtzEnlCP3lVef3F1PHwmqHf-yffaCVdfn2WK1eE0qQthTQGXWrQUkMRXx-_aW_mYMgdpuRXBRSZlZNrJ4TabZtCr9Umb6uzQhmK2J0bAvyftCJXRueuQXS4lgguzFQ5IYg48ulciI3QOOv1j4Rnx_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76784" target="_blank">📅 20:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76783">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ترک فردا ویناک احتمالا فیت آرتا عه</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/76783" target="_blank">📅 20:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76782">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده! هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76782" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76778">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76778" target="_blank">📅 19:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76777">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این‌ دکی و ویناک با آدمای واحد مشکل دارن، بعد جای این که باهم برینن بهشون با‌خودشونم درگیر شدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76777" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76776">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تقریبا تمام رپرایی که ضیا برد تو برنامش و گفت
اینه خانواده‌ی رپفارسی
فید شدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76776" target="_blank">📅 19:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76775">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">نهایت ترک‌ها گسترش خواهند یافت</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76775" target="_blank">📅 19:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76774">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1894538736.mp4?token=rdYnLPSAsKwAPJrBuAjLsDWRikyF80KWOmBZOmoTJ4za9tPEoPLykl1g66BjB6bqevVBK6gk_oq_pylf3aFzDySEuZir-WJa-kID8UYO53GofQFzrOmmy2IDcUV6a6Uy09iAKoFi40el_n6Vot0v-EcSt3pbkPQ51rvLTRkI_xJNuhZhUndYWE82bKCMsz1GJdWwJNjz1FzK6wn94rLyKTB2UmNlNOhfkeg2BDU14UBFEXCAai6TnQ9veoM_OnVOLdakABt9-ciPJUyq9iTJX4vxPnz1GpcXOxr_IF9IsqrP9NLBZUMVfGoy7bDIfNujjUBDU7bqVqBy86asmaJmuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1894538736.mp4?token=rdYnLPSAsKwAPJrBuAjLsDWRikyF80KWOmBZOmoTJ4za9tPEoPLykl1g66BjB6bqevVBK6gk_oq_pylf3aFzDySEuZir-WJa-kID8UYO53GofQFzrOmmy2IDcUV6a6Uy09iAKoFi40el_n6Vot0v-EcSt3pbkPQ51rvLTRkI_xJNuhZhUndYWE82bKCMsz1GJdWwJNjz1FzK6wn94rLyKTB2UmNlNOhfkeg2BDU14UBFEXCAai6TnQ9veoM_OnVOLdakABt9-ciPJUyq9iTJX4vxPnz1GpcXOxr_IF9IsqrP9NLBZUMVfGoy7bDIfNujjUBDU7bqVqBy86asmaJmuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نتانیاهوی جنایتکار
😡
:
من معتقدم که در نهایت ترک‌ها گسترش خواهند یافت و رژیم سقوط خواهد کرد، و ما تمام تلاش خود را برای کمک به این امر خواهیم کرد.
فکر می‌کنم که باید به مردم ایران کمک کنیم تا این رژیم را سرنگون کنند، و این تصمیم تغییر نکرده است.
مردم ایران خواهان دموکراسی، روابط خوب با آمریکا و روابط خوب با اسرائیل هستند.
این می‌تواند اتفاق بیفتد.
من هر روز با ترامپ درمورد ایران حرف می‌زنم، اما خب منطقی نیست به شما بگویم چه می‌گوییم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76774" target="_blank">📅 19:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76773">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">مجری:
شما راجع به رژیم چنج صحبت می‌کردید. چرا الان هیچ‌کس درباره آن صحبت نمی‌کند؟
نتانیاهو:
چرا می‌گویید ما درباره آن صحبت نمی‌کنیم؟
مجری:
به نظر می‌رسد ترامپ آماده است با این رژیم فعلی معامله کند.
نتانیاهو:
این به این معنا نیست که او می‌خواهد این رژیم فعلی باقی بماند
اما نمی‌توان دقیق پیش‌بینی کرد که چنین رژیمی چه زمانی سقوط می‌کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76773" target="_blank">📅 18:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76770">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=D5hQVzCr8258desYzSqZjbPpO-0qvSSdTsmfLqacObeHE4OYzwsX8VhhLqHhGHywrFKWnnqHPWS7fcGoCg138RiHC_UpvbKhfm0KmnymHsVntxR_YlXMz9hYfaPmjt-iduoRZw1VEbJD_lhYubyWS02koYW-oWQNAHedl3PIZNyyD9X8LmmwsFs1z-Z2KR35XcwLgnzP-XGIcRRv-of5ePK50Njs5w81XaCIGwFvy9_x-EIPzAZn3yjzGgKGOppcIdO8vx1aaKrLucTLPt9AwfVce_c9ZNhoTayYdyg2zGUMFdmh8-_esp9l4VfKG7-8erkndFzm7ai7MV4lQ52T4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=D5hQVzCr8258desYzSqZjbPpO-0qvSSdTsmfLqacObeHE4OYzwsX8VhhLqHhGHywrFKWnnqHPWS7fcGoCg138RiHC_UpvbKhfm0KmnymHsVntxR_YlXMz9hYfaPmjt-iduoRZw1VEbJD_lhYubyWS02koYW-oWQNAHedl3PIZNyyD9X8LmmwsFs1z-Z2KR35XcwLgnzP-XGIcRRv-of5ePK50Njs5w81XaCIGwFvy9_x-EIPzAZn3yjzGgKGOppcIdO8vx1aaKrLucTLPt9AwfVce_c9ZNhoTayYdyg2zGUMFdmh8-_esp9l4VfKG7-8erkndFzm7ai7MV4lQ52T4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76770" target="_blank">📅 18:42 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76769">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">امین منیجر فقط ثابت کرد حرفای فدایی و شاپور واقعیت داشت
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76769" target="_blank">📅 18:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76768">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">یجور‌ میگید انگار 88 ترک داد حصین</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76768" target="_blank">📅 18:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76767">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">یجور میگید انگار 98 ترک داد حصین</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76767" target="_blank">📅 18:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76766">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بعد حالا فرض کنید حصین حتی تو ۱۴۰۱ هم لال بود مادرجنده  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76766" target="_blank">📅 18:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76765">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کی میخواید بفهمید "زن زندگی آزادی" شعار مورد علاقه‌ی اصلاح طلبا و امثال عادل فردوسی پوره؟!</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76765" target="_blank">📅 18:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76764">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">با خایه ترین سعل چگینی بود که تو دوران مهسا سیاسی داد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76764" target="_blank">📅 18:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76763">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">با خایه ی اینا دانیاله تو ایران
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76763" target="_blank">📅 18:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76762">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">تنها چیزی که بینمون بهم میخوره شات الکله</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76762" target="_blank">📅 17:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76761">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aU19GBX9WeDsOpV79ZqRw2e_fXIRacUpWA1c33EZQywiux45la1QZ20tWDkv2wBXNsPGBzQUKamQ981LL82D9Jyzrsa6EVM6KK5LIAJrkniITg4cIMnciaGxdnSK9zp5D9gKS-rsFgcli4zgZT0BVtgfuVWXhFJReQfIEbUU4m2TMoZwdVjRpan3G32TXJ4zlQmti2VVjTvZ_h31P7_gx-ioWALklLbhgLcVpWM9PwADgG4IPNL0Zr3aVuUk_dy4LKfYDNOk9zrGt4WGYlHQWZzVQ4PV3u_lksHobV-FNVxjEQvmztktvqDH0LopeHpQuHqbr0JQm6uS7YNvhVLzQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدممممم ویناک عکس پا خوری دکی رو پخش کرد
😂
😂
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76761" target="_blank">📅 17:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76759">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76759" target="_blank">📅 17:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76758">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نخست‌وزیر عراق از تشکیل یک کمیته مشترک برای تدوین سازوکارهای قطع ارتباط با گروه الحشد الشعبی و انحصار سلاح در دست دولت خبر داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76758" target="_blank">📅 16:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76757">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=WQbis1XKYZckRgN-LYkiEiLSTEJE70W-jITvxVblZ-31p8OtubMhORfQaUlbnPwefeGMsdYHVARh0_ylIYkf42XkCHFvv0sGXteCaEr2dH3VusKMaHA1ZLrC-ax72Qbf5I0KJJGBwTF8Xg2ncaSL4Fl9OG2Sg0R3vkmjU81HOSB3xPZCfMfQLtRKS4TZ7pxLd_qBl4LKIHi_R3kNBq4m7tprH9d9FQRp9tj7-5Mw8P9VlPqd8NMMmrCH4eBA9YOizw3F9eUjHxVNFUjUwVmmAYJA8VjGaC2Tx8YMdsTcMpUdShxt0e7A3v8Js8nvqFyq6akjLJ5CbwSGbmXk5x60Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d22d94095.mp4?token=WQbis1XKYZckRgN-LYkiEiLSTEJE70W-jITvxVblZ-31p8OtubMhORfQaUlbnPwefeGMsdYHVARh0_ylIYkf42XkCHFvv0sGXteCaEr2dH3VusKMaHA1ZLrC-ax72Qbf5I0KJJGBwTF8Xg2ncaSL4Fl9OG2Sg0R3vkmjU81HOSB3xPZCfMfQLtRKS4TZ7pxLd_qBl4LKIHi_R3kNBq4m7tprH9d9FQRp9tj7-5Mw8P9VlPqd8NMMmrCH4eBA9YOizw3F9eUjHxVNFUjUwVmmAYJA8VjGaC2Tx8YMdsTcMpUdShxt0e7A3v8Js8nvqFyq6akjLJ5CbwSGbmXk5x60Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76757" target="_blank">📅 16:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76756">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=u8RMfYJAyq5MRYMn2MytxO-eFT27RHCoe_22VHLdOnR_QhjjCVFgVBv5-33CTMpVVuesX6_QjQ_UubiWTmyiASNXt2tVBcC3yjne6zz6CDW7ciLwNkzyCpoMtJQYKzN_rA-wG0GeHKhpuEwUFY4XcEwGwn-oYlpujw2-tZQVaBaQRc-Q_yLc0yg236QysEgh9fNfVrWWNr2yes2oUsSs1Qlcjo15Gy-OfNRyxaw_w4QM9_bOz90NQfCEmKIkSsbd5GRgLWilxd_mVNsS3gpAQChBZnfKMx-RbD1kao_QLU2WYPUPgYAnXWdR3fWnfWKTM0TnpGcSaIZO4zzOwyK0KA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c69b8022d2.mp4?token=u8RMfYJAyq5MRYMn2MytxO-eFT27RHCoe_22VHLdOnR_QhjjCVFgVBv5-33CTMpVVuesX6_QjQ_UubiWTmyiASNXt2tVBcC3yjne6zz6CDW7ciLwNkzyCpoMtJQYKzN_rA-wG0GeHKhpuEwUFY4XcEwGwn-oYlpujw2-tZQVaBaQRc-Q_yLc0yg236QysEgh9fNfVrWWNr2yes2oUsSs1Qlcjo15Gy-OfNRyxaw_w4QM9_bOz90NQfCEmKIkSsbd5GRgLWilxd_mVNsS3gpAQChBZnfKMx-RbD1kao_QLU2WYPUPgYAnXWdR3fWnfWKTM0TnpGcSaIZO4zzOwyK0KA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حداقل یه فیری استایل برید کصکشا، این‌کونی بازیا چیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76756" target="_blank">📅 16:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76755">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2wcfklNYfGqXir6lPFPCecUTQAtyHLypg682ZsHmp8qZU24NAD8Q7E5UWPEyFxS0k7XnDg9EAqsGzGMs1XSIe1f5nHeqhYF8m5EiAu98nG1N6ZYYrGp4M70VfmTGpfhx1xlmm3MdkF5H39w6cPZBT_hFoNTOy2PDgNxjUf5hM_amMZ8W7nuBA3Bpcd7mVPvXMVFsBCnoYjuXvcOH97-7Utq4ovVI0C6Kq0w2qfbctIXiAhRPJwdlYygmUnB4FKz41TNEp5e6TBBKYEzzPClCkvBJ2RVLpZnvvgLDDMjfmt_HVeZM7pq5PrARa7ozMzHR8ZObG-mHvV5DBxg0iswdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه آمریکا تا ۱۵ میلیون دلار برای لو دادن شبکه‌ی مالی سپاه پاسداران جایزه گذاشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76755" target="_blank">📅 15:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76754">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">شورای عالی اسلامی عراق خواستار تشییع جنازه علی خامنه ای تو عراق شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76754" target="_blank">📅 15:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76753">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">رییس جمهور لبنان حمله به کویت و محکوم کرد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76753" target="_blank">📅 15:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76749">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLRfPZqBIte8BNqYn75OaQYY1WXbs9dpAcnt_9pF3isq0TcqrLMt-5RcIx84NmiFcnAFPVI5ZTU6LcOfekBzzMvwvKAD1IQqM3TpECtEW5Lb5-LBDb2WFDXwfRtGA_6grGXeZ8oSXufRfwMrPjHAOn3ICdkuoTERxOVYIdGnHt3lDnu1doz99KFb36CMEfkI95Hg315c9tpYwTBwxtHAXOy1IVph5XOShoGulT5GnPxcG2PVWlM6T6cl_vqzBbT7lhHHJgluq-nRvBfRtWrtn6WoJJrrre424QGwydnsRPeFwOAN0NrvpGqbURPtHi_lfEzpw9lUa5OCDLC019x7Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UdgFjQkaCQ2_6KsjYcPhvBv1OSyc5AP_wx3EXTp1vkAssKGSENA7nx9p77FxXtrMODPxYM4iN0VBKxgF3fq-uixGVQ2_IxZdNiW_O0lsv0KaZIdGgonETUU0B4uEt6Rw15FPgfQcSwmHLLCyzQ3Wk_ky_JfH6uqzluCR2Qmnx2lhsl8xSfyjF6vWKTSq9o8QXDWy6NH8uVIYzexezVIMs5VxnCxaiisvIPq3I-btKKVqS-rd8SwgMV5ABkwLvkakKrzFXj019MoDFiUI27MXCeTZY2PokIaLNs-xI_WxoELeW2-6bTHnJn9hlbagT-fUlI9qFLQVDn0qkO1oWHKdZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rLv_mP6XsjzS04_kDszw17V8_TjKvzfkrEIcJ8LfVQ5hOcUBQevHYzDBAx4Nmre8FIDBrCK0oVaWMr_p4g71-y_wWN5uAdHDnDJiwdH0Ime7FK_tN4QP9bw4WvK68t7_2_cmmpOFIDnL4kq-FO5ZJMIVG4QGPqMIMJDuY9wFJy0Od2-e9ovC9VeXi-gmc65NzEQkX3WpIvVQ2JswfgfiEn_oobzElEd0FqDOCJm8D16854kYFXIoG2HXLF6wrSY9QuX41IJ24dLSX0s1QavOBj6nhFARrhZxTyFJyIxdZG3KZMiFa-qKBp-70MRSI0kYeWQFnoKlK1qDnpPx5gHuTw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=sQr7ohWxVZLJh_AlYXep_mEdH16MHef8zkDryJPt_8h5bsvxl5eIN2K7mqeJ2jP7j0o3Eae_p1imyjqzMTlnhXQKdZ2_AmKwyjhRifWTAAFxtSIwJ5J0GiupFxyrm8iyNgDalcoSurQA9BM0DcmiijA8z6yefWJThIgHJF7Py9cOZQGhsyG-Ff9VasbX8G92qWUSp9GDheJHsF46bb0EwLf0kucd-4PwZJZSJlMfMIqKhd1fSj4VXYvzhibH-rd4yAFb-DjHpO1QnNYH0qQG9Zgo7vskyAdp9GEvDoHzX4qBx3cuEZv1E7IkfnB2y3D66t6dIKNyAr-tG8KJMzSvrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c69019e0b.mp4?token=sQr7ohWxVZLJh_AlYXep_mEdH16MHef8zkDryJPt_8h5bsvxl5eIN2K7mqeJ2jP7j0o3Eae_p1imyjqzMTlnhXQKdZ2_AmKwyjhRifWTAAFxtSIwJ5J0GiupFxyrm8iyNgDalcoSurQA9BM0DcmiijA8z6yefWJThIgHJF7Py9cOZQGhsyG-Ff9VasbX8G92qWUSp9GDheJHsF46bb0EwLf0kucd-4PwZJZSJlMfMIqKhd1fSj4VXYvzhibH-rd4yAFb-DjHpO1QnNYH0qQG9Zgo7vskyAdp9GEvDoHzX4qBx3cuEZv1E7IkfnB2y3D66t6dIKNyAr-tG8KJMzSvrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرگزاری های کویت دیروز یک گزارشی پخش کردن که بازسازی فرودگاه کویت به دلیل حملات ایران در جنگ۴۰ روزه تازه تموم شده
ایران دیشب مجددا بهش حمله زده و همچین صحنه هایی رو رقم زده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/76749" target="_blank">📅 15:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76748">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoXJigX1rmNPct3V19tlurreFB4sVuW_NN1fy2Tta91NcdFTQxhAxy5ZDdm5YicS9E8k88GM2tc0YUSiyd7lMkepFC3Mwb9gnAJdFVkSXvi4c7Ep4LMLhNpp74ccUdcpxyqBI1aoFQ4TQGGGG2z5cikDmQbEyz2DrcU-4Za1ja2mm3LYtgxMudapie_zmEo4yzuzI73PxuQLcre-jpAT2DlT8VxtCjqCLu6LaajZ-qGh1MjWtMZxzHWXE_jU5ob2MZtlE2TzV7-94ZT_mDw2f9eg8AzF-e3UbKAUQbu-A5H9IbfAlTnIFGxZJIJotnmmG34hCldFJFU-dTMd_jXExg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید حسین تی‌ام به نام "پیستول" منتشر شد.
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76748" target="_blank">📅 15:03 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76747">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=R6sUFSP-8zkoquyl30qpUZcq_f8fjtt97GgKOOaQIBJ-YrLbWncIyhjwxrXAtrfQFsFqdQG5L5u0fVwCt-85XhZ1TlCg-hx5Nyzr-1z0owoLPO5-_Ir9b70P1pgpFKrZhprbjMwj8DB6RbnlTik_xWuWpNNK99Xozpd46KTNeIfdjmFyU-QCBXcNnn-t6P-7Ou-_-T8R3zLPPYyZPuZLE8FcNo1GJnp7MZkgOXmM8iqTP2kGjf-ZqtlFXls8RVIChnAgtdgNRt31P68_gktIGrxg2xVa7q0l5lTw_fsVg5Ij7qpalbbUE0ZfhZb8EH2jAiyCNAXrkEXpkSEBa5hofg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2bd935e81.mp4?token=R6sUFSP-8zkoquyl30qpUZcq_f8fjtt97GgKOOaQIBJ-YrLbWncIyhjwxrXAtrfQFsFqdQG5L5u0fVwCt-85XhZ1TlCg-hx5Nyzr-1z0owoLPO5-_Ir9b70P1pgpFKrZhprbjMwj8DB6RbnlTik_xWuWpNNK99Xozpd46KTNeIfdjmFyU-QCBXcNnn-t6P-7Ou-_-T8R3zLPPYyZPuZLE8FcNo1GJnp7MZkgOXmM8iqTP2kGjf-ZqtlFXls8RVIChnAgtdgNRt31P68_gktIGrxg2xVa7q0l5lTw_fsVg5Ij7qpalbbUE0ZfhZb8EH2jAiyCNAXrkEXpkSEBa5hofg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76747" target="_blank">📅 14:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">اوه اوه بندرعباس و قشم صدای آتش بس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76746" target="_blank">📅 14:40 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بنظرم این نه دیگه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76745" target="_blank">📅 14:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76744">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">هرچند دکی تو ۵ سال کریر بهتری از حصین تو ۲۵ سال ساخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76744" target="_blank">📅 14:37 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76743" target="_blank">📅 14:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76742">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">MIGA: Make Islam Great Again.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76742" target="_blank">📅 14:24 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMVuZApyvyFEptC45_mj7Smn8RJehGoERrNJ6tT3VMOS0df19N6U2ToR7Fc3Y5HzfySaYTJfHl9GDvmOT6OAGeuyxBtp6pkFZoTHzmqXZmbOYQkO0p3SPVmfQZHDKteeQ3Dgh30caIfQDWTZSRUxd8AuGhZqkVazqTPT3kFCXFMRNiTVTXN_gKNNddGlFfEE9kJITR9CY3xmGg-wU8t7IqUGMzXq6DFXs1XEelM2CspekyD9HYWbgYMnSHhdIst6vUcNDQS4pZEPBsyuiy753_dNrGyMXlaXbDTNgm_2nHcyIAuyi6H9wpgeKxLFu8SIWpQorJdVJjhrM7NJn61T1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76741" target="_blank">📅 14:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c517113be7.mp4?token=f9zApCHVGBL7Q66WRk9-v824exc3IKB9L-W4tY9ArPMkHv34MXy6hIj-BxfGvBtAtjNW4HKfPkIbNnRmlopI6TxLh-tKyleB8M3N33H7vL-fh462y-mM7TtMl9nDq932Zlbtob3Az_jEPbNNtqZ_fFc8Ypo3miMGHQDRX_Gg_oQ5BI2wBOBJnXXUGReTS_CYcJ1O4z_M07m89LVm2yVT85arXqdicg3UoCkocKVINsUOyARhHrCRQXKrenKpMnpGaMysCQpFinLfFIKnSaD1NXizSpGSUdfZBvNez0Gsjm8r5OtSM15TI2Ej6VJVwA6t8SqYkbZXcxfNz9r5MdipFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c517113be7.mp4?token=f9zApCHVGBL7Q66WRk9-v824exc3IKB9L-W4tY9ArPMkHv34MXy6hIj-BxfGvBtAtjNW4HKfPkIbNnRmlopI6TxLh-tKyleB8M3N33H7vL-fh462y-mM7TtMl9nDq932Zlbtob3Az_jEPbNNtqZ_fFc8Ypo3miMGHQDRX_Gg_oQ5BI2wBOBJnXXUGReTS_CYcJ1O4z_M07m89LVm2yVT85arXqdicg3UoCkocKVINsUOyARhHrCRQXKrenKpMnpGaMysCQpFinLfFIKnSaD1NXizSpGSUdfZBvNez0Gsjm8r5OtSM15TI2Ej6VJVwA6t8SqYkbZXcxfNz9r5MdipFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حصین در جواب به ویدیوی دکی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76740" target="_blank">📅 14:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76738">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">بمب جدید از ترامپ: ما همین الان با مجتبی خامنه ای بصورت تلفنی حرف زدیم ما کاملا به توافق رسیده ایم ! بزودی حملات ما علیه اسراییل و متحدان اسراییل اغاز خواهد شد .اسراییل 15 سال آینده را نخواهد دید  از توجه شما به این موضوع سپاسگزارم .پرزیدنت دونالد جی ترامپ…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/76738" target="_blank">📅 14:04 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: احتمالا در مقطعی با آیت الله ایران دیدار خواهم داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76734" target="_blank">📅 13:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTMMl0QcDxwq1ZrH9qrICQtp--rYUxrGexV-1kYr7VvfuPFI7j_JMo8lMuf5QA5J7931ZmjOkCj--L9lTjEhE1HvQ_-Qezt3vAydmFAmnYp3RpnGdN2JRJoWSAQMu9j-0l-yuwa_itvhWribaKAnDtjMwhyKP3DkR0NwAAZ5KzJzt-QdDBinFPKG93JO7-aKB9TkxIklDnZK-87oIPdr1Hq_IAPoI4Fdo1LwfsmYTdWDTaE5U6HdGfaH3q7zfu20IZkdesFsvRMdozUJYlvEfmObcP7dQOEbtLM8ZF71jATqNL2Aet1Z17--0YpNtH02fdpzwhW5akyj2WaQXeVeKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خط دفاع رئال مادرید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76733" target="_blank">📅 13:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76732">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شما نتونستید بچه ها، شما منو حامله نکردید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/76732" target="_blank">📅 12:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">دیشب در قم، دو بسیجی در عملیات خنثی سازی بمب های عمل نکرده کشته شدند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/76730" target="_blank">📅 12:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jG7Ir_lMm_AdmkpsPMdiVkhmKH7REk0e947DFXe7vF1rsRqd98bBAQtsZYWqveYG3-To24SZ6w-k8vASSg1Z63gxAmt6FsQGXm7SVYhVev9OdNDJ5J18JK4ufRrqB8dCO4Nc-KwSkyn2ihcsc6dq2MGdPcD12nUumRv3ExdSmDWjcVg1bW85O2Z9DJFNVXxavIQpx4ULTL7C57orxyDwLoiw6dV0AZqZTDR-1f95P3HGIna2cZbDOUz-G71lVIEIhV0Zx4RT1IcpnIKMdV8ku6uEtT5qkF8cbxfL39eXHOVZkBidNOLaIurZhjr0tTsPRjNHrcOvapxCVUo_t8nuZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استایل جدید کراش العالمین
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/76729" target="_blank">📅 11:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OIcdZ4e0FW-AfhCH6zX4DN_nLSwpDsWD31zGYFZziqotdrjmgqWaqiYqXTEp8ZomLSeYxfJ9X65OJf67CPx2lPJVlIL3S-R8UXXtGUVmt7ff7o_Z-MqDvfGokEryIOkiZ0z1oxIsWeesdliRV45I-upSFUSAX8VcLJAQMcNhfmpOGcXHC41-Ww1Jr4JwiTjdNs-76EBM8Gh1ycuVJMJJAh3i8lB0s2oLoY673vRAWsiSW8auqYpof3bENiGLcmAHOIYbwmDA366hBLcTFL4eu-fJdNjXvVusRX7JyR8kDNotIhbv8vFVS_u4s_sHc-ed_oURy9xutViaXjwEYK1nTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادی کنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/76728" target="_blank">📅 11:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sy_sACZ1iIB424CZudfCr-p2PNMLANhSR6hHh-SRdboW72ImE1wg8XlB9--Nsr_kOf7_EH1Zwgam8hhecKAUHwGtOVXXmdCUxrCjXYIBzeWt2F96cDkULqjQXUzcnSZJkflAXsMqAb_uEYC6fPOPK79STb9sF3crv_WXubzBH6IPAllDLWNIOc_1q5b6ia_w53sJ-6ruG9cOfCqJ8mLLyKDlcKv1sz5pbQQeqvTpLrLFI6HhI_658lWZ2gHQbMjLm2HQI-w27Bn8Gsb8LKost0lL45p8Zk6nvhYvmKNawISL_WNDRWtuBhlfdt6GLkHVleBgcYKHUTTZ9keNsEgvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nB2VWXvF8iGCh1RlOwh4YHH73AmC8ocQ4cdR77NxYoY1Xam1zbKS76-UGRSNai3-nD0Mp2Ix99oYW4PjTfHCdmxs5wBp3EPYJ-f1cGltWBWAV3HSyiHCakziouEMpaXSPi0RRT-TABq8ze1IifwILKvFcYLHBoG7A-w8X-lUWaf-NKXWvkcfOGzaX5cgKPWMLmD95CdL_aFuvWADJtVpwLQpOtCUwNS66L_De1qJh_a63Gx5xPe-IZD_7JcxqafcWBVPA3oWqsrlZgKx254LHdBnIEg3anhU11M2nWBl2OrqD7Q3pTtMTY5LF03yP2IMoHsglSmPVn4RU6zRrza6LA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">زن مراد ویسی (
لادن سلامی
) دختر عموی فرمانده سابق کل سپاه حسین سلامی هست
حاجی سیاست حاجی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/76723" target="_blank">📅 10:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ItaEhIAvbmJ09ssjCvf-9oLtCDxTAJ7LiT4RuMgQVE_rGyH3ZrVnROpJd4xUgnFkHiZa8014inzjQvwB1DV1HZJ4-rdlQA0vGEqCmhn6pecFgcBVXCIrCos4CQ5wPBK5ObQ5iOoyeeTvVzn4KAbCrCP89FvNOAGIoyHa0W16RvKNJXmudcCFo6yxing7lOepO5I3HWnPCaMGc03tL-mlc7iNIcMSeec2kgZ8A5SoONmXdEgWffKJ2LLqYNozJ9gx2BH33KTad39Zxy8iqwityCYsWue48ndTn7J8e4qqnp_TgSPlrVyPG7kvN8pRSHsmdqMBZoE8TMHpytuu6K_4WA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فوری: گزارش هایی منتشر شده که محمدرضا شهبازی، مجری برنامه پاورقی دیشب مورد تجاوزِ ۳ نفر قرار گرفته و برنامه پاورقی فعلا به طور موقت متوقف شده!
هنوز جزئیات دقیقی بیرون نیومده و پلیس در حال بررسیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/76722" target="_blank">📅 10:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76720">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76720" target="_blank">📅 10:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r5PwrGH4AQcfwfv1VdKoIFpM0GyxalWgLd9fdogAMDcW7Nt7xldnrm_p5PZOj6BeX7ccdgsDf59FHmBUZXSogklK-4gdC1dChW3tFTfVO4WfK5WjRTg_SX7AzeUHkzDPRWNpn9EW4y0GazrkYjhj7t_m9yW_lHwrsOd59yWaMe0GynX0GpLFqNiaJ1y7HKZfp2zgn9UWbAyrq6P7wYlWcCMxEVqTMnF6tZCE1tTiDGWVrM-evapi27b25LFzvam_862Hi5ITokDvcB-sGeFDAmNEGqEXTF396YSgtUvz3vmtc9K544ySh4WwuQTKuvrVvdES0hnkihm89cWrxalY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب تو با آیفونت توییت میزاری نمیگی من اندرویدم؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76719" target="_blank">📅 10:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">این آتش بس با بمب اتم هم نقض نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76715" target="_blank">📅 10:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76714">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">زدن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/76714" target="_blank">📅 09:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای یک تک انفجار مذاکرات در تهران
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/76713" target="_blank">📅 07:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقتی میگید، کصمادرت ترامپ "🫪" اینو بزارید کنارش خیلی بهش میاد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/76712" target="_blank">📅 03:34 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بخوابید ترامپ خایه حمله کردن رو نداره</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/76711" target="_blank">📅 03:10 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
