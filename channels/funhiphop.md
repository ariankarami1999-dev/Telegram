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
<img src="https://cdn4.telesco.pe/file/IK3PEpKuPD_xoIrT5MgbNFxjDQxU7HwvbnzhUJRqqlNJgZJaEHUox6T5MO1-s3WMeVc3PQ_9yIV1Vk-DJNORsodssZt_WlnaTg8wsKq0slQHrVAClAh5RKV3DKLzIqccbGdMTLsQSg3eQO5YdqKEORJ0mqaADJ8PvB0ROAKNYJ1TNL45N-h_zny7_mupqOCWr682jSEkx90Z2LVjHejUPHPLjkUEa7Gmbz4v6qz1PxjCc7DnCvP--oGVEQ4rEEqIr0pItaIh_OG1LdEFbzJMdPjpHcn22xsP6ryVxSnUa-7-EkJzKmKAFjI7vix2uHDs1Mn31m0t8lfimf99Fyep_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 223K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-20 13:53:21</div>
<hr>

<div class="tg-post" id="msg-82072">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/funhiphop/82072" target="_blank">📅 13:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82071">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا:  گزارش از وقوع یک حادثه میان یک نفتکش و نیروهای نظامی در خلیج عمان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/funhiphop/82071" target="_blank">📅 13:09 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82070">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oaey3u6TD_FbBj8DHVdYCgk6IrPDUJDaIdgF1tI2k4xf2N2H0CUL-so36YsjCserj_NWBrrC_9PtVTr-8lXsokHPbU0p5Hf0MRJDMIsIAqOj4zfTvi_22f0qkt2iau92Srsenxle1IgpKPWQBgvhFONZ2pqqxa_A524JuKCCXAWKJcJ-2UA_9PQ40WNKtKzPBwKMXWVaAa9QY_Bdbkk2-B1_rNCjeW2Lq3Yd-mLa2j00WH-t7xObX1UgxIaT_CDU9EUmSSNF7IkSvt0wNhHxSEcO4mS3bafjda3CkltYpkSyhAvggpxdShD9fr70SJSZFq-R7aEzrtvecVaxKOctgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک پولات به گا رفت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.09K · <a href="https://t.me/funhiphop/82070" target="_blank">📅 12:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82069">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IEWwLRJ2WIhXyAyN84UO-en-yQ5FqwtatWyGIFDqVefuBIKQUiKArchIqB8ginbRAwhlUCtD3C9gqEbqAbq4MPvPYDLST5bUTrBHquWIuTMxjEBEH5gG8_akLG31f2tmrDOjoUj4-Rj3OnFzqw2JoB0efj9-iUz2U7bREYFwml7evNPAkW1TyzveGoaUOXL-QKeZ8R9S-KuseB5DCRXvKniiJDOFOzmJCqrKSHhYm_vCFha5GuD__2jC7n2g9dTUUR6hH8F6o0WWIAYW1lCYeT7tYw07yLn9lnVxldedkRHo03D31VyDgMNwYkwZO4IB55rBFYVTcYcPh4Nef13fLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/82069" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82068">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIks-Uden1rQEJmUZqWUNwnO-WPgEpIBvI4Rzzf62gOmI3vdx-OovOL5dwDmFgbZq_JH4SfLxUJ4Bn3ZF9XJ5nS0PdcIIkxARWOU7CRckJqJ94CwYqiNYDXnXFKmNV2l7onzFCF6IJky0g_ay9ZmUo5FWljrbZtyyhcy7Dw7-97i2jeH67x5jyZZhQle3VJKQrpOF31_a7xEmMoHHeyBAphGk3BbvxJIKNA1sD0FHHc0Q0Ff4uH-h4xAsL1KkccZr9WphSp_GVzWz7CdUe5zsGFH6rQ8_yoHgPGfgPN2Wvg3mnvmTpmyfaQqdRf00x2dwrHuLtzqAzTCVELxfn3RtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
رقابت‌های مرحله مقدماتی
🏆
لیگ قهرمانان اروپا‌
🇪🇺
⏰
سه‌شنبه از ساعت ۱۸:۳۰
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r20
💻
@BetForward</div>
<div class="tg-footer">👁️ 6.77K · <a href="https://t.me/funhiphop/82068" target="_blank">📅 12:21 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82067">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hnu1ml4k4KPRcstNnU8_vfg8arsF-FlQ7eUmkyQVXuWp2Is5MOlhGxJB4Kgsw4vq4TYpGw0q0y-ii9Re40586c662qPntDpQy_q0k2ypzf7uAqwSrhzPaufKIrQ5CEs4N6Z-A0PXayvCyFPTDboSDkCNxcflp7SgYvBoIIfZXgs_sjRLBZxxwXRCLyTge6eCJcNeHV-VjoQGJZqH-j059hyPoqGf_Q9nYEm-vlEYI0UInN_4HKCqq8XHQZCPYHxQJxYQVgBhqKVEXchkY3VbLjMRfP4CmhyJXIScB0KwH9tf4JYDmN3vuakxX45djVkNs_R9-s3elynbN7WclnwD_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری احمد خدایی همسر جاویدنام صالحه اکبری از پیامی مجاهدین خلق بهش داده شدن که در ازای پول علیه خاندان پهلوی استوری بذاره و اعلام برائت کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/82067" target="_blank">📅 10:49 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82065">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">داشت یادم میرفتا
کصمادر جی جی و دانیال ددان
کوروش
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/82065" target="_blank">📅 02:14 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82064">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKkVCyldFRKPsts910ClSAMsJ5u5zWfMxz_iRwxbDIXoKMmzXpSWFYMwt7Obp0ojeqvt60ePV8UquXsw89d9rjLBCvKax2wKcPJgNXmxRW7RO7OGGVerOpHYIOO3DFZq2SMNDbsGmBFd9ZgSSKPdWy7EO8DZCFzZWp61_tDd8-SWscaEjCq1XE7zXvZuNFAM4yRyi-ri2aanSmOa_j1gxM_XluDttG4kURehjAdWVFqPogCZKGm7IJQrnraTmzPqWpR8vndxjOMM6294nXrIRXDZlOLzbupQrGtLuLHOnHWSogtYNGmcQsGLeUKjaJ-bhbwUB_wHyNNYvSi8UvkFaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فریک پنج ستاره از ایران داره تکنیک های مارکتینگ یکی از موفق ترین آرتیست های تاریخ تو این زمینه رو زیر سوال میبره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82064" target="_blank">📅 01:17 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82063">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دیگه حتی دکل سیریکو هم نمیزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82063" target="_blank">📅 00:50 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82062">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N_f4Dma7OlVcvgBgeYNFAnRoSllLM5Glr-W4cUxbq7Kg-5neYFZQ1YxXE5O6hXRtxoPVshkw8P8z5Lln5isc3v1lvpzjrgZ8OPK_kH2pUDle7lro2apL66Jb4Y0xe2Xl9NGkgmuFUVB04ObWKpAVIVtW6OIWveiZn5IB-TX0XU4Cs7KnnqOl0xD2iGtBb_zqleoQNfZ7AJMOLUOOaIwJ5mnKdycYSrZ5SuxwTrFwu2MPdI1ygJPTE_3iMPRLMinWj2iHfViWAXB9YB2L7mXbuQujDZA7tGfTs2cLtKocDSPJrjVrAnEHcFAFXYoJnYevgDLD0SNdiJ9JscP5ujhExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سطح امیدم به زندگی :
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/82062" target="_blank">📅 00:10 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82061">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید. _چمن در خاک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82061" target="_blank">📅 23:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82060">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/litlMH_6BOmtkGrYXVQ0TyApZ3fXD4fNV5Ydh7sCsgIpbKkG6q1xTG-EYG0dtLItqGzZDLXyjAeRZdjg_TpswImClSKlG6GNsEtjV1vITOP9vAA6R_enN_cEG_jpzmnO__tsNLOaiGS91ncShBXwHeepxpaNBpLPojAagmHelqqGO-O4exH0y5cortp-SkKKLOnEUQKgWfpNNZERVEZbSIN-I4ODvULtVd9-DIqe3RFjplrJDmfFofDFLcOgiEEzId4fC7XWSWTAkVhhgoJecZuPXxcD595f1AhUZfsAmSdSUWEcJx1_76t-y0gQNdxvwD55RIGcKBzDOaFeJs3wpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید بی‌بال به نام آزادم زمان منتشر شد
YouTube
@FuunHipHop
| فان‌هیپ‌هاپ</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82060" target="_blank">📅 23:45 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82058">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tIcRiIok0pfMbbFZc1vQ_TqDnSJY5vmT06GkL5kME1jpfscy53zSxFCSJy0nWIocMGVkGd7OO_6ic-cuPrTV9CRsmTQFLhN8wTVRn_RI7_FGB8yaTWtwRx4UNzylZiYgVFetc7CzjhKsUMmazgtZi984jlZ1KJWDS7GddHj19V5zj2VCo2he3OD12k5PEvMV5XZPss6-QCmCpcuu0Bw6FAqp-3Tv7udffba_v6X1OeoAXnXxdJ0e_QmSpz0PFJ8UVFh4Q6AsY3fVxETUf7NepDsFoLAx9KZhyY0x8a45JdTs2mVwtA-aeH7yxNrpYzsCo35-xfP2wa6eSN_wM65cQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پینترست چرا تبدیل به کرج شده  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/82058" target="_blank">📅 23:30 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82057">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ عالیه
گفتن خب تنگه رو میبندیم فشار بیاریم، پاشد رفت یکم اونور تر محاصره دریایی گذاشت گفت اصلا خودم میبندم
گفتن خسارت بده، اومد گفت خب من که خسارت نمیدم هیچ شما باید به ۵ تا کشور خسارت بدید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82057" target="_blank">📅 22:35 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82056">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هنگامی که با یک املاکی مذاکره میکنید، بیش از حد چونه نزنید.
_چمن در خاک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/82056" target="_blank">📅 21:59 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82055">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/82055" target="_blank">📅 21:42 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82054">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=KpLfnNf3dYUV0p6cZxLgqQ--BWeUr77pfCtRRqMe0g9hM2zkEajp6Fe0cZajaNmN867T9D21ir0NFbmeN65tWYWBEBWTnqtYygSzOUThYSPCka6A612Wk3fIl2mz88sHXU0JzJJlB7Quh6o6iKKJMUG0_6DmqIsQyV1gXOm1h3UwnIha1xYD0VB4HRCKay2z8x9LYL9X9RzibZZjV66jlHlTY7wqDqNNLN55QzdJ9c5Z2QiKSPwWblnPwhRT1GRgGfaGqThyz90m-1OaLoSqVBAHHxGGHoHfC5QCnK2E9FIC9lVzDH95_evebeXlard8NQqnRcofz1QpCIMzosbGAw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bf0cb6c78a.mp4?token=KpLfnNf3dYUV0p6cZxLgqQ--BWeUr77pfCtRRqMe0g9hM2zkEajp6Fe0cZajaNmN867T9D21ir0NFbmeN65tWYWBEBWTnqtYygSzOUThYSPCka6A612Wk3fIl2mz88sHXU0JzJJlB7Quh6o6iKKJMUG0_6DmqIsQyV1gXOm1h3UwnIha1xYD0VB4HRCKay2z8x9LYL9X9RzibZZjV66jlHlTY7wqDqNNLN55QzdJ9c5Z2QiKSPwWblnPwhRT1GRgGfaGqThyz90m-1OaLoSqVBAHHxGGHoHfC5QCnK2E9FIC9lVzDH95_evebeXlard8NQqnRcofz1QpCIMzosbGAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دختره انتقام رجب زاده رو از قاتلش گرفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/82054" target="_blank">📅 21:40 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82053">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">ترامپ:
-
من می‌بینم که نمایندگان جمهوری اسلامی ایران درخواست غرامت برای خساراتی که در طول درگیری نظامی پنج ماهه گذشته به آنها وارد شده است (آغاز شده است زیرا آنها سلاح هسته‌ای نخواهند داشت)، حتی اگر هرگز در هیچ یک از مذاکرات یا جلسات ما ذکر نشده باشد! اما این ایده جالبی است زیرا اکنون من نیز از ایران برای همه افرادی که با بمب‌های کنار جاده‌ای و بسیاری از درگیری‌هایی که به خاطر آنها مشهور هستند، کشته و به شدت زخمی کرده‌اند، از جمله خانواده‌های کشته‌شدگان در ناو یو اس اس کول و هزاران نفر دیگر که در جنگ کشته شده‌اند، غرامت می‌خواهم. علاوه بر این، باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است، غرامت پرداخت شود، و ۵۲۰۰۰ نفری که در پنج ماه گذشته کشته شده‌اند را هم نباید فراموش کرد. من به نمایندگان خود دستور داده‌ام که این موضوع را به طور جدی در هر مذاکره و تمام مذاکرات آینده قرار دهند.
-همچنین، در رابطه با مذاکرات ایران، ایران باید مسئول خسارات و مرگ‌ومیر ایجاد شده برای مردم لبنان، سوریه، یمن و غزه باشد! رئیس‌جمهور دونالد جی. ترامپ.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/82053" target="_blank">📅 21:20 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82052">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0wCg4DgKPK8tbjkyQLHy6qv1Yagy_HhjZPinLY-CNfaMrvnXB46-JjgKjD07Y_hVnXhlYXVqOmWIW8EvtNm9Vv2bAcTbqe2QngqxfUENGJ1Hguv5tgx7Sf1DtJJrIlEaUPDsFpk5a8ufFUYapJFN6Fai3osZs3gwNFPObIgRNZ32HiV4OjBB4UgwUQ48we9YTXK_ifZ8y-6n_suWAgmHza3KdQ1LpYoa7NkKbN_5OO4k2N4niJLxzJFVDZYuJhQ4F1uvj5f6BWHlFqVJZ0GZCpg-QgpcMIOYx_Mt8oOjqfkhIlovwhObpFKdwWbuKRP3xtxUlHdFhI_eS4QdtOaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برید امضا کنید لطفا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/82052" target="_blank">📅 20:16 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82051">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8xnXTOjwbzs97rF6ku2G8HxOcFA4xnLL-ZGnx0agj4989nE6gdTXuuN0WO4lWV3hyE0yedAdoIiK7iDTCtcCLlzpPe1YaKZa_q9H3b0VcMvka5HhVhDE70SNMn52HJFY5OZ_dRuWDdMUrUtB66qlOrRhI4g3wcZp2ZMRTlpXymX9QD1yC7XC_E6Wm3-PyVInXzdiZkT417lm4kAqn4_mjN9WBPM_eGo_qVlHkfkQzNxMzxh-8uickcX5NbFYKe7y-XsqJ-OnDuxWsJhU_Iqg1FyylUenqIYiC2DQum5zgtTyKrW4JmLh1TJR0h_xVmzwNkJEuE6mWNoRHKSWt_33A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ورزش سه تیتر زده جهانبخش رفته تیم صدرنشین لیگ هلند، حالا چند هفته از لیگ گذشته؟ یک هفته، و تیمه پارسال ۱۳ ام شده بوده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/82051" target="_blank">📅 19:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82050">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKBK9HfOQ-vsbwBnHFgng2j7g0l3uKxTKDDsBCak9JfFjXpP_rFTSi_VnlbzD88uo7A3sre8N8gVup-fb3ENcdZcDKwhGNmz-h7kGgBd-KRH7l79RazwanRzvd8zLITY8FwuSJiD-18pqdy-GWhzKI9dav4bGNYqmIEy66Bss7I2-W2ZX8c3CknPaCp2Lurw0BslF87M7KcGTTcxdfoukhVFZPIGdRelTsUZo8yRJxWoHtxJy73F4grAFu7m7RSY7Wz0l45yoAo5lgARGdUWSgNILFeyTUX9GQFCPpZe7Ltp-JcDe11_WQBWpGO745fJPRoEsoJauI-TpcJPlTqc9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرومزاده
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/82050" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82049">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l_WAY4le-qs3U6lcFiXRrVQ13SMYCSthg5qMGXBvi7_ClYoberuza-bjcfy7SED5IFD1zm9qiMPctls_R-AqAAcsiRmtJziWa03v5h3XQ2pptEopIl_h7GX7jwi1y7S9QlfqTr6L8odNh1PDLYTm0lq8Fdjav-SpTnM5B7BVOpGt409bms2CumRnKnmBjAa5iSp8p3_768UFKR-z3QoClF0PRgOq7_6RUdljSm0rqvQdcQdCHN6X6ID6Gc408uZXoAF8g1DyfRW766dxpia_unGA0d_q9KWZKQM2x2G5Upqww5P5bk3mH-TCU5YboXaas8gp6XtTFQaeBNZOuvjDSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r19
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82049" target="_blank">📅 19:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82048">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WxW01M2YQFAEbYlKpAT1HkCKFrc1m9sbpnGf9E7j0O4EGBsz9rFWjtaY4F9B0j28ier6ilYKX-uPBBA69ydJ94lzacFN3ql8pmyPFAXmnNBWXNN4qNOq9yOz3aJcp3SK_412YxaqYGjJpUD01h3XhzOfuk7vplzpAEMdaOFU4SFm7GmLWU-dQ6OquOKUu-74HWjKnFF3gbcuYYdk9cQQpUXDw18xJTiJNB91mPcokAcXw2N1MX82tqFZ-U4xTqICA6fotHogik2fuxjOf9tCl9T_A0_52BccGcxDdvN9G_ydzgeIWp021W_0cj0Hml5jOeuaOdFygrTV4fN01uvhmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید بانو لنا
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82048" target="_blank">📅 19:13 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82047">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ss1_gpckE_ITcLgrB_c8RUtQDDnVYiNTXRnwtIKWghqgfpgBVk8S11qci68CLZn7BwUqpgt3Lkpql8TulK9YcH-9X2OKxMSyVB6Xj-1U-_pH8T-uwGECYsSNiRoms8Q8GpC06GbBiGVzSYZShBWIIiVl8KUh1NeT5yOqwNtkylbI-PGVhUNl7bawBHmREDVrCJaKFtDwQy8b1yPbQli4eSYiD7wsborq4o4I5LnuwWNNJfJ86ftydZ52cf8_DoiIroWEI2AwGp7jWAsA4qATWue-R4ThvevxmWyDbuivu80Jhkq15qA7bSLLFvJph1e-k2QcFYKgRPE8o22KDqUuBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوماد‌های سابق و فعلی علم الهدی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/82047" target="_blank">📅 18:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82046">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">زن ابراهیم رئیسی با احمد مروی, تولیت آستان قدس رضوی ازدواج کرد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/82046" target="_blank">📅 16:44 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82045">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ویناک میگه دکی لندن نیست، ترکیه اس
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/82045" target="_blank">📅 16:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82044">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZss7mBW3j4FxWeOpYgucN_T70WJIs5YnHRtol57gmfExDu3N-oBDeui8aP3JdQclRfqdzy0rLdoiq2L9D3-1n5zGX8-l9eHEv-qW8pZc2546Et5CMSUTj-nZ-opXB4I93M6Fekbz99fHj50x7T6pF3QwS7KhIbmA9m2KmKESfi6Joz9rJ4mMQ5R8-f2zRLQfPZM1Yr3GUET9kruCBN4vKmqmP3Po3kGk25Bna3ktxGev6ti_nzJsZWMxGNH_1_f3EgSiO6JnQFQChIpG0-auW1nowtmGg-gOUfK7mBDWPpvjDOqEfD_RxrwHvh-iKZsYTzrW-4LYadI4OLqAXsKtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو به روایت دریک  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82044" target="_blank">📅 15:23 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82043">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=DVy3AlqKUmvO9o5Qq8RT9n-6pqk82WNXbCkpbvP6fJkP7Ko3qSRPVMHFCZQfynJT54gSLqdgks2D0B7Xw8bO1he4zn1dvSs1CWB8NKusEDKycCl0mR66o4WKccxU_FMTKk1buRrQjs4mdadLqC8_NVtbiPPiKxeh0m-TUvovwpLJAL2vwPo5oJYh-kWfWNjTclakTPPHbskEvhp2a_lvb9_IcM-m5oXit1TguOlw7ndkzciDhLogSsYGzAhaHLv2MlLKs8FU-N5GpiuI5FpYnBMWf7rXLjb05XCCi9RiLFQMOLaNqyaLQ8xhdrQPbglWyewqsSlVkAwASoKU0Ze01g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/48e95fc990.mp4?token=DVy3AlqKUmvO9o5Qq8RT9n-6pqk82WNXbCkpbvP6fJkP7Ko3qSRPVMHFCZQfynJT54gSLqdgks2D0B7Xw8bO1he4zn1dvSs1CWB8NKusEDKycCl0mR66o4WKccxU_FMTKk1buRrQjs4mdadLqC8_NVtbiPPiKxeh0m-TUvovwpLJAL2vwPo5oJYh-kWfWNjTclakTPPHbskEvhp2a_lvb9_IcM-m5oXit1TguOlw7ndkzciDhLogSsYGzAhaHLv2MlLKs8FU-N5GpiuI5FpYnBMWf7rXLjb05XCCi9RiLFQMOLaNqyaLQ8xhdrQPbglWyewqsSlVkAwASoKU0Ze01g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سگتم بانو به روایت دریک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82043" target="_blank">📅 14:56 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82042">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3v37DpYU-Cx-FXcPfAtNmxIIG4HlaP_lQ0YOoRhu6JJkuDJOKCWk76fb3iVDMIizG0jj6zisdGKZhP6rjr4e6dR32AF8_sLibaC3gPv6qdUtNlmQqDxzWJFU_9Hp9cDPUOFI2tmC_T_uIDlrEalxk-h3uVp-Nv9H2hO5HhfoAEvH1g81ddSTDRpq3OXoyF9R238Wkiv0QKUQeIMTje6D1tZHeg2oxyonX34o7OConpR9q9PjAYrDZ05SSjei_VOlSOrMq1CRKcQ_DTIK1DyXV2LLUmtZTA_RldWBrGifhinZazBc50HD-qqtAZzpbp67z5ZXDJArhNcPPj9YeWOEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۷  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/82042" target="_blank">📅 14:49 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82041">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فابریتزیو
رومانو و اهبر رومانو این روزا سرحالن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82041" target="_blank">📅 14:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82040">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW4Q555C_GloY0hVfZMyiJouJdDODRECNSh13J3Q5k-anQ05CtNyaO1jV5gG5qPO_ecrHNdPFvotELxtSO71PDeOKBVuUUgfTQdWG59f3KApyhCYyJXRFCNT3EShgeiPc3Sve1N_tuZGhZRQ0AFq9OnITcPDImHp-DULSFNiIJWw-scFVUpXOUsOgJEGfyY5TluQRMiEJWZBpWtE-p9zyKTFW2JVK93Y6yqcnDZO05A7W1s5WpH5RgVD5iuKgSTM5_X8Qnwq05-6xtNEyf5v5xPhX6GBrEXb6J5zD-MR1iS7vhbNuiVvyTLm16OlF6DwPZm09pLCFwVBil0XLJr0pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عادی ترین رفتار پدر ایرانی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82040" target="_blank">📅 13:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82039">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gruH-bODUscCq-xlMSiuivdsuP-zdE4B5ZlUONHzvHmn2n7IFwPfdWFP9O-LOKJP7VeWef6QKvrbobefDZa3o_mq5DpQQ_H6X9x3FclFTSfVfuTVpnO9KKiYaIihl8q9lbfX9t_fxLv-Lfc1Xiv9dGpNQe7Wpoc8TLM8pKB_TOOqud_SDZw-yYypy4Ekun4-2xMsIJhSiYjzivmga8J2w-wydRr103OD1EyXh1YUcWx0wJr4yrffNiDzzuQqNwLOocUM0eLW_5x5ufTCVIl-I03gPkGd1f6r19cEJWhULl4h74uIvdfAD6JQL7UyJEjEmiSb8qKdxsq0dQpAlCSE7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نماینده خامنه ای در شعام، محسن رضایی: باید برای رفع تحریم ها بریم یه اکانت فیک از ترامپ بسازیم و توش بنویسیم تحریم های ایران برداشته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/82039" target="_blank">📅 13:15 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82038">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SO6vNMZhxttxsNkD4iJ7tcX3V_R0H2reDL7JGfcTOqB97Imw63fKHkR4cXytJB3vuDxGgb5_GZg8cuLEQ16XWr5L2C0FTVvc-VRej_oAkyOQmxMTP5rDRPthKZkxd4YueXkVhGvPZbQXkZVlt39CWplbuV-JOsnX7rnFm9g5n2eRCK2qW4gLjJ9wtF81STI5U4zUk8jxG1pBt8id49UcbF-K4iZnNb9J4ElUeXGXURL6pR_RV9KPl3yQmo_jXotqsD_TY32MqqV-U5lhYmRoriqHPIQNsrG594Qwq_JX0yJSfbbKvlmaj4dpUzs8wumal_sPkQpt7OLq4Ygdln3oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فداییو دیس کنید تقصیر اون کصکشه همش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82038" target="_blank">📅 12:55 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82037">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwSr8wVncAXN9erRGbSCgrSoN4iRx9ufzmSLSJby4cMpep7-ucDxZrz3_wBZVHp6BHAqyMIEpXFAGvh9OnjU4who2HnlbaqfKcTCL1iVG5eWNf5LIe-Gkp3-ISaSTV3zX69ZGfPpdE3IeUEkuTumwJIregP0OGg6A-oPqqq444lpcPuOs3EBkDe9iPxO0A9iBrUQPWr2HRokLWQMvK9yHfnJtZKVM9UPVq4C53PSOrvnna57FO9KtC_VGhc-kubqlkq4m4HTjAFrD8aS5Kt41OEm8HDrq4S5o9EoD-FlJC8eOQhwQ6asgT80choCcQeWcNzOItNoJ9scuf300DSBHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت ترامپ راجع به ارزش پول ایران
کپشن: ۵۱ سال بد رفتاری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/82037" target="_blank">📅 12:37 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82036">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uglEbAjxIolKSYuxu1C0Qr6HGD1P-sik4S-QbX125Av2GYBBQH1JU7yZTQV7tVRMUAhimmISrOhwJ6NFYNLMp036KNYp54PBSkBEPVaTsBooCOxPvjPy5v0mUisuZN1mFeE6iNH72fW0A29gsHihc--zp7AJmtHa_-L5egbKIRkjveMNbEjl6Sr6cTf8VC92Z7BuVFX7zcWI3MeH_1JA-xj_zvv4bqAvyUhPyHHGwmiVs5dixkOw_O7yJlOSxtfCHL8-9BGYkXXIFQxxGC7_XE6z7yoqE01FdShl4QgG_Ica0eNUBlCZ2b0l2c2uFG6iszsbPMUKlUKdCh-eqA_G0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کوروش به همین اسم که تو تصویر میبینید بزودی منتشر میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/82036" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82035">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DMQ60GzPIsg2F_TQyRtMenlPciywvMgVVPZa3mGLd4CO3O6a9sRtV5EP8ISf3MxJRAYsias0tt39IR2GFuozM88yMBaUDvckzKRVnQW9aoB57jIoYvvMf-zfMiunUE_OCoLD_AMLhfuVcd_XBUX0u4OE09vSrMVFWAnTM6oy-cHZiUlEEvlgIscah8ZVyNF59fgwETd7bAnzAPhRaM5S2rRNsAFgU23w5K4A-K3pGdkTYLNBdzu_9VSgPIMUkY87x58-XWgmOW0aaD0_xTcZWiBTthssw-fm0JmLsGCE42Pgqg-1HVNTs2n7fVry_mpBVveKkyLYrSiaQ-iOrQBX4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
تا ۲۰ درصد بونوس افزایشی ماشین اسلات
🎰
در روزهای دوشنبه تا جمعه، با حداقل ۵ میلیون ریال دلار شارژ حساب کاربری در طول روز و ثبت حداقل ۲ میلیون و ۵۰۰ هزار ریال پیش‌بینی ناموفق در بازی‌های ماشین اسلات، بت‌فوروارد در هر روز با توجه به مبلغ شارژ حساب کاربری تا ۲۰ درصد از مجموع مبلغ پیش‌بینی ناموفق را تا سقف ۵۰ میلیون ریال به عنوان بونوس به شما هدیه خواهد داد.
اطلاعات بیش‌تر و قوانین بونوس:
🔗
bfrd.link/SLT20
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r19
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/82035" target="_blank">📅 12:32 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82034">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JkcdQ-YsBOY_jzEcA5qSQOzccHDQalZ3YI-Zz6j7JONIJvxjDwjYSDsh9Zvaf6xh4A5WBbNji1vpV4TIoJBLX6YSYQmdAmIHwsAnTn4YMCqdJ9n92ASDQirmY6nvi5anztB4G7-U6a-uEmYisiyPM22NU2y8wTARFL_V0m4MljZ3OK1m-6UT4fOKceDCe86jdLfHPF0wUfRlGmi8B6IcS0IUck_jHl_Via6NpNeg9lL-R4g9lU-PDRzPF0top_ObMFE5V1k8-3dgXEtdAilUwEiBAaj7cbSO9VFHi7DlZsYJNzC7eOo7KmUf6_y1TOTbc7HWpzHuR_P7oTP5sQ0Kig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپو میخواستن دوباره تو زمین گلفش ترور کنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/82034" target="_blank">📅 11:54 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82033">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از لحاظ روحی نیاز دارم قاف بیا بگه "قاف، مهدیار، ملتفت، تهران"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/82033" target="_blank">📅 03:02 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82032">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WRJBjHWEudT_Kyb0GEjlofcTyZN64aAmlXSvH3aUy6jte_c24GDw0t8GFSKSIMXGjxSUdw79yULjdDchu1TIPiTD1aEtca-KQoSuTChzg452n37JS0-MFNlr9KUOWDn5knjx7X4b7amyZb6QlwOvLd0lGLmuK9IMr-MFOj61eMi0QUYvfGcc9-k8XfSH6sAJnyBjiYEd38B5ur4QwUidRGbgvRtePjOF-EMRLNm0H0E8WeNNhwY_Zuh_lgQonSL4sbZ4TiEIshk2Rs7CLHC-VIAOvFuo_uQCMfdHljuf5717wya_twiQ_EhxIPpUpI3tt_uTReIibugwOl97EVYf8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار برای سروش، خطر در کمین است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/82032" target="_blank">📅 02:57 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82031">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E3-xiRSxnmUqr0TU58o2XUMkYwpSDi70siBFVL0C0J7UTZqAvmdZr_Ahfaf88JYivDIePT8PCj3j0bw0vaks1TrWodnOp8otBm0zJHo8dPLwPUFMyuOu_86Nv2kHAQu2zPkPzmQEOTxMmYZ_GOti1BZUMydIo7Wc7c8ioMlZtEkWdY1FS5X7uqFbckAxcbSaDvcl36OLof-vUC7r5WHUbrXWrK1x_wvm-Xzoe-heDdAV0Pr-EtdgmshE3oXgjlTK1OggjaGKwB59uayxYar7VC9jbBqCHSJIp3v84ITP3sDFoUsQhRl7A1YfDFiY-CdqLXszGFqsYZAPAgJLFwZdzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی داداش آروم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/82031" target="_blank">📅 01:34 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82030">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">منابع امنیتی گزارش میدهند که ناموس سجاد شاهی ترور شده است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82030" target="_blank">📅 01:14 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82029">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">4 تا انفجار تو تنگه هرمز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/82029" target="_blank">📅 00:53 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82028">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سپاه زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82028" target="_blank">📅 00:36 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82027">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb6fwGKgJPeInTEz4YbiEwNl3FmZCvzWareAVHg_F2noBppxdTA0KES_041LKDOork025iSpz9HMRhkQnHTuJSzKMNBkAzdvolhabn5VjaVFJWBmNmq7UGwgFYwb9WWB27nVZ0ZULcJ19GQWq7vC6BBuXErfVhgF1ksOFUB3YLoLj5_G-aaN8GQJ77NvzOjmlCv38lczBf4_rU0Q9OSZyf5K-TXFkbPj0B7JwiCq6cQ_mzqBDoQ-iTzysxQVBCIpKWL_8wcyks0lACggXtymQr_kDWPWPCerFosSlf-6IBuuNemPGGNtsjJ0wtxVwigXI6zlOquFNR7HU0oGC9sKRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چقد عجیبه این عکس دکی و صدف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/82027" target="_blank">📅 00:31 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82026">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">ژنرال محسن رضایی رسما دبیر شورای عالی امنیت ملی شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/82026" target="_blank">📅 23:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82025">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=UgHVT_MTfY17yHVtxeu4SN_Fw8uMKr1VK5HCzXMer6d3fACN5DpXlq6sJfuexkRwamCsIX9D9ZJKOk6d6ldbzPUpbZvNS3XF4L_Q9siANpsNLaQ03W3xfMKXkMUGuwZnVY8YZvxzkwareUdkKijan-cLbf7QX47oFitiYg2WIyVNyEOefXIPdiTZKVxbpoI-bSUaS8cnEbK2wU3omJjnfP0biGKgd7N5CtaatcselB5xk1jhi7xfIg1m-AY7oV_OFsj8zufV5nG7vlWPzC6wcGwzewViqlyLv6vG5pSU7ZfUhWuR2RDG6qNEPODzLX_GuXE27NVEOY-SYohFYF8NFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6de7c57540.mp4?token=UgHVT_MTfY17yHVtxeu4SN_Fw8uMKr1VK5HCzXMer6d3fACN5DpXlq6sJfuexkRwamCsIX9D9ZJKOk6d6ldbzPUpbZvNS3XF4L_Q9siANpsNLaQ03W3xfMKXkMUGuwZnVY8YZvxzkwareUdkKijan-cLbf7QX47oFitiYg2WIyVNyEOefXIPdiTZKVxbpoI-bSUaS8cnEbK2wU3omJjnfP0biGKgd7N5CtaatcselB5xk1jhi7xfIg1m-AY7oV_OFsj8zufV5nG7vlWPzC6wcGwzewViqlyLv6vG5pSU7ZfUhWuR2RDG6qNEPODzLX_GuXE27NVEOY-SYohFYF8NFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر قدیمی خلسه راجب شاهین نجفی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82025" target="_blank">📅 23:07 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82024">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">۰۲۱کید تولدت مبارک ولی قبول داری شبیه شیپ استیلر تو خاندان اژدهایی؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/82024" target="_blank">📅 22:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82023">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=ZC5LPFYLpLN1o32ZJm40_304jg8bWfqiLURm53amdji5uRI3OclgDE-1LWXPQL_V2hCZMLIhG_t6SFR50rEZGOavHYj88gONC4YjxPxJUo7d3yj3KrUH-nsRxWDDjGuCgvlKghZtVbly2IWyt7XZ7lKtJ5Ppf7e9IhLXJMByY7rUivr4Lx_BZY3oiRXGEVbDqZNtdQvQ-vcpesyx7_61yFgN1c850T6KSZeeAmnDi9rWoXQHUZW9Fo6x_qKLIAaT38I4Q5hyU_yXUkgRk19AezESIHSze0OjkAK89OhDAqjrSyZBI9D9wtzEX36iqwlsxpmMqSvA0ajLCsc375RTZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147038d4e3.mp4?token=ZC5LPFYLpLN1o32ZJm40_304jg8bWfqiLURm53amdji5uRI3OclgDE-1LWXPQL_V2hCZMLIhG_t6SFR50rEZGOavHYj88gONC4YjxPxJUo7d3yj3KrUH-nsRxWDDjGuCgvlKghZtVbly2IWyt7XZ7lKtJ5Ppf7e9IhLXJMByY7rUivr4Lx_BZY3oiRXGEVbDqZNtdQvQ-vcpesyx7_61yFgN1c850T6KSZeeAmnDi9rWoXQHUZW9Fo6x_qKLIAaT38I4Q5hyU_yXUkgRk19AezESIHSze0OjkAK89OhDAqjrSyZBI9D9wtzEX36iqwlsxpmMqSvA0ajLCsc375RTZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعضای زدبازی، حصین، پوری و الباقی خایه‌مالا بعد از لیک شدن چت‌های مهدیار و فدایی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/82023" target="_blank">📅 21:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82022">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q5K8XWcqrGTvFhsMi5F8ZEe64z9d12JYLAUlQsKnf9TmqauEY9pwpqLJwdsgG4MYKIC11BRcMtyZDvQk7gkF5W873DkE52Hj2feHdPiIVAX3-MKvKQaBLW5VU1fmKoV5lhJXQx8aEnZveHmfJbMWzgrbel6DzDhHofTWCtRC2I4FLgNbX4U3xET0I2Mio1eciuszMFEDn9oK-mONAtLMR2DbhyPyp4dXnBwUZvRl8PkaT-voYmb0G3PH8avPCf0OOIhClLs_AoYcvwkhh9hTDrvb1KEpExztYC3Tdq_Hgau6irn1_keOgXmGODaCOS-7GcrcNsHmbqt4gtDGZhgFPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توی امتحان سلامت و بهداشت امسال سوال اومده که یه مادر چطوری ایدز (HIV) رو به فرزندش منتقل میکنه؟
یکی از دانش آموزا نوشته: سکس مادر با فرزندش از جلو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/82022" target="_blank">📅 20:25 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82021">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CaopkQBvlg9qVvWl7gqEkfXKkGdmYvEJqhU38cS5kk6_DBK5MtQaaJTSAgA613gHMRp6QMw98Ud11ivQ-3AUCcHiQ_oIOinOYfe4DClqAWGcJ0zNrL77iZs4qlEDuetIDeiOcIf-JWLXlHKYsAILR5PQz5j8FOeXdWWQZBEetSxg_643mfQXnyKDqMFIEAPNgVIGZq1ElSm8mGzGbiKuXu9QzewaotvInb8m2GMm3GI7ss-SqtN8Ri_4tM-1kxAbKrQhl3-kBg0ZWVitCLmIbq6zy3Zv9DtqjUABZpwtpDlgrF_gbxpU9lf_6_B7xS2mR4cC9ujVMvFiUZBd3aE1Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوری
❤️
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82021" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82020">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uaaOhC3u5nmKeT8ukJtV5lWhp_ozSCdSLhnlA3elKkp8C2j-i-h4jHJQPuSoDybWeWmKFb_LgA-cTcZLBJMOS6woBjKI2gw_CUXK-4pf8AhC_p-lSBOjshZxmRg89v97ABS9k8ij80oNn5hJ5xnYpxGcVcY8Dw1ajFta2CtTFr-APB0TXsSLyez_7TMbpiTvoy4YYG3uAcJXbHufC43qLo7Sy__kzFDr-faxPWeKc0dHpkkpGmpcgB9-aCVTcjS8yKLY95SVzlrsGrxjn3l8Qz49ZtpKcGLj4_c3CTLHoZ-kWgMBC7H76XsqSzhul6LTkuIjMC2DO7MdRGUHb8aLpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
@betforward_bot
کلیک کنید
@betforward_bot
🅰
g18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/82020" target="_blank">📅 20:09 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W6MfXXnXp-c6IsxFqSCVSs4pdurSSHnNoQk6Eyo2jBSIt6Es1xPQmbWZVGRH72w3oBM5IC01d5V5JZY0SxGp8IfvrI2mt1BBJPewMwUairAgq-ZoBoIjwEfJbUfgdSMnEAwtTNLoyGRK0lF21hl0KcIenz2Ai9u1mX27UZVJtYfj_wJWSiJXMQ8Kj2On0UjiVRVo110drZqtwVYWb7xjRO580L3ztknr6DR_nQj9qwSZffR67_7KRcA5YObuzUooZGCYyub3GDaCfkHJ7umg7C6vUyXe7FQMIa8BmuFX1mUxC6PWtbe1m65h0l78nRDXo946t4P4XMPTabkn1UPeSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HUIEE-zqQfKC4J5WOdgrTUKbGKeznoqj7RhjKj36GzFrVruv65UsCkx2JrME95SfCKoAy44PtUQ3f1jiIqu6yidtHTed-vIZ6zOMv16vxbl6GDS-Qe_OPg2HyPybDyhntDFXPW0EJiGKoJ5qGAX6BExRISEkb0LH1IDUmwV4QUcZXcfTaAhg0bTCPfnZj35u-XBB1rpStGDI9l8Lcxrb-QdoRA2L9j1ATI8FvI2k9a6GaX2S0IZ6eLUpzJ3cc4xxV07GLBjHvO-iqC3xyAaqYiaxQvKa6UxzM3iDQheKpsUgde_rm-j0BGrnJk5IkY6dG_MswbIEfbay5DNp15Blyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ngHWXMNWUCuGT9CkHjK0VH80nZQqXtaXfoh3DTwpdcxfmUP_Xv-3qEKtYz4OZ_lkagjQR7T1450CPGSRHesMPrMleTX7tWwbvUukf0e6aWhcuoytdgsIoqMoWzY5GrIa2LJ6Xc6a0gtPwUwvPTdut1rBkzlfa7BQ_w4OsOxanMCcGDXPp2Ps7IAhyqMnjNAbZHC-3Yp2yy6-zqonSoTnuVLTQ4BCvRm8D5HERa3kjix5Hlujx-imgM8-JvWDY2Iuacgg_BsnA53J7se_1-R1ZM5gMY6u3uAOwLqjAwjjgG7L5xgZ5lX_TzWpwp8JRkHIdPwWnVVjZpuaCgjOqC5AxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=ikScH6dvsRgn5bTyD10Dfh6nr1LbJFURsSpQZPBaZ8pr0vqRZreLw9j9okWXD4xZOji8PzbJCS14QD5VdD_kSspqRD4yLAP0SEzuBxLyMuvCONnq_GU3ctKbWRZcdgJFnt-SyhxzDbA2HXS7YDnvCrunBdph1QnuKieC5RX1zdqvT5GWZC181vP1HZDZwAT8rqGrBldRsMEyHh3F2J2L_ri3z62M4IozvnjAjCt6jXjJvXa3HVU5RB9UFN7vViUkGM9P-81WO-rOlcPEN40SZay3E2DqlfW4PTKuBoETzab82kwxud6KlbHxI_Gri3aNkUvrll4cHK1Q_IFO3tVtmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d21f2b9ac0.mp4?token=ikScH6dvsRgn5bTyD10Dfh6nr1LbJFURsSpQZPBaZ8pr0vqRZreLw9j9okWXD4xZOji8PzbJCS14QD5VdD_kSspqRD4yLAP0SEzuBxLyMuvCONnq_GU3ctKbWRZcdgJFnt-SyhxzDbA2HXS7YDnvCrunBdph1QnuKieC5RX1zdqvT5GWZC181vP1HZDZwAT8rqGrBldRsMEyHh3F2J2L_ri3z62M4IozvnjAjCt6jXjJvXa3HVU5RB9UFN7vViUkGM9P-81WO-rOlcPEN40SZay3E2DqlfW4PTKuBoETzab82kwxud6KlbHxI_Gri3aNkUvrll4cHK1Q_IFO3tVtmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پیج اومده یه ادیت فیک زده که رونالدو بخاطر فوت بابای مسی عروسیشو عقب انداخته
حالا کامنتا ملت:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/82016" target="_blank">📅 19:34 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">وزارت خارجه اسرائیل:
در تابستان ۲۰۲۷ ایرانی ها میتونن از خود ایران برای سفر تابستونی بیان اسرائیل.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82015" target="_blank">📅 17:50 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eXDz8SylHzpgvxQVDyKVRza0M3ZsddpRaltegRL7ejf0i4sJUWUJdpaEjZjffaKUjnJTqJ_QZjM9pFRAHc0qvOqt-6vJxvc3mpCJJLs2HwqL49i2Our2ZeLqjrlf5yaYGAysqfD_QhjP2NiD3yoBFpn-jngk0DvB9YUbrHNiCbnZZUMw7xx-i08qR5c9WmPmH4WC8hJGA0IU7-SaEgc-4CjDsw8OlsmnPmL-rIFijKHOU-r6AZfkXuWu32koWpYJaCEsQhKYig2iC0nosZdUKsowdpzGjAkrp8zOQWqECaAE_g2noB7MmnoSUG9ptzQCuCPS1t5lk4ZM32MrBYHgDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تیجی به نام لبه تیغ منتشر شد.
YouTube
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82014" target="_blank">📅 16:14 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خدایا یعنی قراره کی بهش دیسبک نده</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/82013" target="_blank">📅 15:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=vEPuvE7gYov5G8RMvdKA6M2fkRgqdbizGK00t5ASWprlyxz2eLTbqffMVCNr-B7bUNxb8j1B1i1aj4FJ4mPEXtaXPar45jLYXJMd1WaNFd0CH2O7UMwHvtB1utE-qUD8hpKnRLicjJ_afO_Da_nUI-12ga9L19tgEfE-IdVQ-BZHUrBojRR4SaDjBSexOsicWSyjP69blYijafh0qTXfL3YmSk6nwzBfHCN_NgpH-nhKSWH3ZmCNwEJcSctQAIUfuLoAD7QE5aDNTttyPl5NZoNcUd3vszWGPyKf-G_8CEkDMeNI3trB-BVbivKcR8yo5Gcg6Wa3szIXW8ZO-YyNRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba5625cf46.mp4?token=vEPuvE7gYov5G8RMvdKA6M2fkRgqdbizGK00t5ASWprlyxz2eLTbqffMVCNr-B7bUNxb8j1B1i1aj4FJ4mPEXtaXPar45jLYXJMd1WaNFd0CH2O7UMwHvtB1utE-qUD8hpKnRLicjJ_afO_Da_nUI-12ga9L19tgEfE-IdVQ-BZHUrBojRR4SaDjBSexOsicWSyjP69blYijafh0qTXfL3YmSk6nwzBfHCN_NgpH-nhKSWH3ZmCNwEJcSctQAIUfuLoAD7QE5aDNTttyPl5NZoNcUd3vszWGPyKf-G_8CEkDMeNI3trB-BVbivKcR8yo5Gcg6Wa3szIXW8ZO-YyNRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رضا پهلوی و پوریا بشیری
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82012" target="_blank">📅 14:54 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=l9VMwVX8uSVA3s8HHHTaVsQonlWW7bo4TIcC-t1UVSqJf7eeob5CGKey6XFyZZQMrJo-Z1BTN8uScjpy43JYwd8VXld79k6JILqaRJ9OSK6Z3jTVwkyLKl6c7AJsk_oooii0pGA6gnqP4u13yLvgbr6O4nFQ686u0ZIapI2GjlsbUdmmKJUQA264gVc5FAD3qmYk3XRmvlgQxCRXtBFmBfK4H7od2WcDoDiEAb1Cua9gL4iP1tV-iB9W0n7Siv5d38TfZ8vkHCa6qXnE0Ve5pJUIhDMVIVh16sV1A00CnhqYlymKzExXo-aEIK3SqqxvGD6aG3IfpWSl0BLdvR-1cQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1384fab4ec.mp4?token=l9VMwVX8uSVA3s8HHHTaVsQonlWW7bo4TIcC-t1UVSqJf7eeob5CGKey6XFyZZQMrJo-Z1BTN8uScjpy43JYwd8VXld79k6JILqaRJ9OSK6Z3jTVwkyLKl6c7AJsk_oooii0pGA6gnqP4u13yLvgbr6O4nFQ686u0ZIapI2GjlsbUdmmKJUQA264gVc5FAD3qmYk3XRmvlgQxCRXtBFmBfK4H7od2WcDoDiEAb1Cua9gL4iP1tV-iB9W0n7Siv5d38TfZ8vkHCa6qXnE0Ve5pJUIhDMVIVh16sV1A00CnhqYlymKzExXo-aEIK3SqqxvGD6aG3IfpWSl0BLdvR-1cQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد از کشته‌شدن مداحِ سرکوبگر، حمیدرضا رجب‌زاده، این یارو با انتشار ویدیویی مردم رو تهدید کرده که اگه بازهم بیاید تو خیابون چنان تیکه‌تیکه‌تون میکنیم که پزشکی قانونی با کاردک جمعتون کنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/82011" target="_blank">📅 14:20 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82010">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">جزئیات جدید از پرونده حمیدرضا رجب زاده:
به گفته رسانه ‌های داخلی؛ قلب حمیدرضا رجب زاده رو از بدنش درآوردن و مایع منی خودشون رو روی جسد این مداح ریختن و از تمام این لحظات فیلم گرفتند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82010" target="_blank">📅 14:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82009">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">محسن رضایی جای جلیلی رو تو شعام گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/82009" target="_blank">📅 13:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82008">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">جواد لالیگایی(نکونام) به تراکتور هیرویگو
@FunHipHop
| TaymazROMANO</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/82008" target="_blank">📅 13:05 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82007">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QEoCsgMcgbD1KF1xr8Y7CmtmXji6r8nz6tgSHbIrMczGKmAzXBpW7kWv1jXUBbmYkh94bI93sTULQCASAVMUFTS_MUVYPUBWHcCR5Sc-3_OyGoJoRVVSqDZQ1uH2FjfDwlZHgiZt8uJpL-s_xA_39MCU3vTYf7DRaoMWFHN7Omd9cJd_Rp3qAaIp4xjc56GIi64auCmbKwfPjMCAEC9-byTKhI9I2mx00Iix5Iju-T-RgeB3CL94cKt4zCiqR9qM7i5k2eSNSjsNqn15NYjk1BCHnfMvRMmnJM2dpoGeE5t3-3mhdhGGfrouGL4ehcfjzBVZJS1Za5slypIpU9uhJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هرکس سالام
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/82007" target="_blank">📅 12:51 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82006">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🔴
وا
عراقچی: در حال حاضر هیچ مذاکره‌ای با آمریکا نداریم، همش تبادل پیامه نه مذاکره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/82006" target="_blank">📅 12:33 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82005">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">هنوز متتظرم تا انقلاب نشده آیسم نخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/82005" target="_blank">📅 12:12 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82004">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fv64IJw8Ejugo9mePNmkXqCyE2LWArM5hjIOA_nvnGe_x6dOuq93Q1z6WxMge6oGSIq15Dx3u5qJoYDq020X8U83iaOVs6BNVX5KSvpoXBjwJw27LSsZaYvyx8cJgQh_Yds5eDQW0UuLTJil6R2zQ6IO8wvRW_TjM-osLqqVBgkjOlE-7KR9L_TWvowvMkRCdS1Q0MmBrFNF9x7Jt0LhSnlGOvVUw1NJqvFuOEWfv6Qo74dWF1-l-ftx-gvRWNT3LDbdVeRF-OFumDbyTwvKb231Bp2-mggwJUcvXnquhJUnS18pnkXpkoPxGyuocMlYyZ83_Rvo2OwA1-0HvuXCRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکس Calvin Klein صاحب برند معروف لباس زیر به همین نام، کنارشم دوست پسرشه
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/82004" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82003">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HBoErxarR4EfGcrmW3NfmniPiNsy04lWH0W3r6nPBl-H-qRord7fBhYm6NLyPwzSPjukTCibRg0udWsX1TrQa9TXmUmRVrAB6_3Kt4iYCDdpMHaQrMlv8KT5P1egsObVHvMiyUDKmkz2xTqNFZDdLaHHTyIpZs7SYPXvhMbN9a9Cp9kvVohffUgQRDmL0zKLfFPc3am51OKVqTACfap5McQYxqUeEQvRWouJN_ZjIF2V7FMjwnBniMuSX2M_Zm5eLgB3wV947TJGwJidIaYs3GXGhZHROO2PdFW8cHU7jan-7rliyV8xro6lSJuKDdKcM6EpbSXk3W84zrbPR1FVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏩
کانفیگ فیلترشکن و پروکسی رایگان در ربات بت‌فوروارد
🎲
🤖
با ربات رسمی بت‌فوروارد در تلگرام، تنها با چند کلیک فیلترشکن پرسرعت (V2ray) و پروکسی تلگرام رایگان و امن دریافت کنید و بدون محدودیت به اینترنت آزاد دسترسی داشته باشید.
🚀
سرعت بالا و اتصال پایدار
🎯
کاملاً رایگان
🔓
دسترسی سریع
👍
برای دسترسی به اینترنت آزاد و بدون محدودیت، به ربات تلگرام بت‌فوروارد مراجعه کرده و سرویس مورد نظر خود را فعال نمایید.
کلیک کنید
betforward_bot@
کلیک کنید
betforward_bot@
🅰
r18
💻
@betforward_bot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82003" target="_blank">📅 11:36 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82001">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a80e3df60c.mp4?token=lvPlM8PFNkkvWIpl29p9_OjGPKub0THDxZGf9gStOYACKFPMKzRsPPEEkBwfAiuqmsjGalx7h2ZEOlIwzjHIzvjZTrX7I5jDzVeEiABwkJ0hrrPw9YUic9orBcfi9kSA3VBA-H24lplmO8lNywWwqSAaJf4tCz2iH471G8igc5NZsRgACqfQ6Aor7yCkCrUCoYBHNmuw2vY5TaV_BPgbN5IIxVwGyv4ubgGF9A2CwYvLxWCgl254x_MQvQA0TBLPbx1QNRMqsX-YPPDrq6yYzfalvTMpeyNwSZN1UsS19qOVnsN7A-iQemucgeMzliJAVTLLkg2W0xIGKXmfPPnm1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاسر قلی‌نیا پس از کسب مدال طلای اورال کاسپین ‌کاپ ایران، عکس پهلوان مسعود ذات‌پرور را بالا برد. عکس قهرمانان واقعی مردم همیشه بالاست؛ اما امثال هادی چوپان، جوری فراموش میشن که انگار هیچ‌وقت وجود نداشتن.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/82001" target="_blank">📅 10:53 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-82000">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/82000" target="_blank">📅 05:43 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81999">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">بیدارید؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81999" target="_blank">📅 05:42 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81996">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/afCqrjbhkkbxDUm6Frqx2X0sgBd0eXUtng8LpqfOUgbDo2DCWmfd5wEVq_7zzYD4t8W3kW99LbMgOu6Trktt41WKSiPMyoJbul6MilJml1RkUNzUowf1E2ScdjZWrYTRYTDIDt-khXX36s8VJ1F-RRlfUb1Dod2z5388uJXb41GcWPDy3QUTQRUi57j4pOCsCyQK53vpfwN31LElyvlRY2asxlaKLSyTxHWjXhMMX2-u8q_Clj8KKsP2yqcxmFKlXQYBwl02IGFOvRh1-J-V4SQN1gYj5RfpssclXi5vIpcoIOMqNiX7XdlnNNiYMq_Z5xxczw64cC3hldIpCKNkng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtpV918FrZ5uhjpjuGnEvb1p-FG8komFfzmNDaCsZ3JXBDOvnBgMPHz0tOpR_COxlTDICQqaUigtVOwdud30PnnisXb12GGDdJpWBvO64m7ONl-MbRm-ZOtTb7f5CgDucVP2lcsJ9MIgEnthJAUaPXacf0joQftAzZUvEMwIiMricbwdDPlNdjIhqaUnY-1gMR90w4hqfzzTjRmmldKG0ajAGye321qZbc37__tqnpZAL7Gk75PzJ4-ufQNdRj5nBQ8Y8Vw79WFeVfcqOswuqHa3AEjQCCMRovhiczXV4BGBNFCRTjI5f1Y4jqxddBef6BliW-R6uyusqrlxVwiUGw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بر طبل شادانه بکوبید
جواد محجوب ملی پوش سابق جودو ایران که قهرمانی آسیا رو در کارنامه خودش داره با رکورد بدون باخت 0-5 به سازمان UFC پیوست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/funhiphop/81996" target="_blank">📅 02:48 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81994">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0zquXKXM-XNGKZnvdu2ZzNE15ZBHOsH__63oeXJUTsjMVtxte10Ao9fV72UqXSnQnj2ib54F23sr9SAKt1xL07WAAu4O45kl9GC167fY0Wixx1l2uII3bYgHcp-ABC750WeT2bZVC-R9RnDljXNJbdVhcxv_ClhZgp9gBosUGkbsb3AsLvCWeKh9jzuUkkWRIBaxt4P71EuG8TVgyeZgMczPkSMA9nx6iyErg4WrF3YZ3UUKlSXiv7H3QLIhmSWlAI6VZGTIgI1_zAe0O-nEFYQc83L4GVuCq67LTCyJSg6OhNGK70LnZkRLJW9vbiFS9ehPnfspeUzIjJjzff0yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید کابوس و دیگرد به اسم انگ منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/81994" target="_blank">📅 02:31 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6HO8Zwnqduj0MbHLLy_hJLYDWLXAR1ZBos3TsFaBw0xrcsDgYZG3JmO4hJ1hqbg-eURJY3nj9U4uJQcR89OWTKsFJ4p9WDag80rmxpBUWjBS47IiuUa4LbpmO3gDYUMNk0GRjNHp5Crk1oiRYVzwZ9dyvUowZm8ROHNoLguzf8-AvBRKhLeEttJZrNHvrw6sik6JbeUqdXkyz5-Cn4Yofb38AdSIXmqLbQJ6clEhzHXWmUZZKX0lAYbhO4X_jiywztMDcJEZ9lxd1Ptz-LoKaKXa2N9juVrwK3lav9YuCSsno4yV-J0c4guK8zwzXWZ1Tb68nQSbrHFUcBWV8lrZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از اعضای سپاه پاسداران در شهر مهاباد با نام عمر دهقان در روستای «گاگش سفلی» از توابع این شهرستان کشته شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81993" target="_blank">📅 00:16 · 18 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81991">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">این کصکشی که چتارو پخش کرده چرا اسمشونو سیو نکرده مثل کصخلا تلاش نکنیم بفهمیم sha کیه z کیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/funhiphop/81991" target="_blank">📅 23:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81990">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eMDDiJcnsclxqLOa3kphgEQ6bvlbPu5kv5jDHnLjAinFMFQD77n42oGq7KPlVtmRQsfX9QlBgxZvFDjPCq2luJoKGq_hiA1qu2WfJR35QML6jeVWh-DrOnU1gwelg-_iq03dmwdUQW_jEduS2cB-3U_g2cgHxwVM3KuA0PTYPCKB4Kb1Ogsin9CeqTNGaOMd5rREcoYHuAE23kCStKD1bS8IyLeH0ggrJzI99JjjElBkPrxAuf_AIP01A9ySqr67_wP7lNpTSKwiw6Tj0l30wp1Z6mjrQFjvTJQW91ydEJt0OXTlA7WjMBG8xM5KeYOdDqfb0l0gxAeOjgH4ONsofw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من که پیشنهادمو دادم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/funhiphop/81990" target="_blank">📅 23:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiWUoFAl1c-RbvdOtqUwu9YP8Eq26a0ug36zn3bMi5XUbyszGpabPp5T7BwtJIhXDR7wDtnJMOrZbDrEwGoBcaO02vVzJsEYRW4XmnfheW9fTWIwExD3kVwehuOVTJOSdYRhEvJU-CI4VTs3antvMSojqAHf3Y92ylILDSwGAUxAnUTPSotAU0WWRQYfe3usIlIG4uHUvO-qfr332Famvhs0hc38DVR95J-xGRWY1i4dgx4TG4_94rGqTAL9wlxjUoZkfSuk4CBRMrdHb68QSI45uRcXa1cRgqZ_cm5JUIxtUJ3fWE9hIvQ0NHdbEwYdTSflciiX7t8Bb2-ctesA1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">100 کا اومد به لطف بیف با بشری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81989" target="_blank">📅 23:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">کار به هیچی ندارم ولی تا تلگرام هست سگ میره سیگنال کصکشا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/funhiphop/81988" target="_blank">📅 23:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81987">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه مردی برای مراسم ختم خامنه ای از آلمان اومد ایران ولی موقع برگشتن نذاشتن برگرده چون کارت پایان خدمت سربازی نداشت.
مجبور شد سند یه ملک رو وثیقه بزاره تا خارج شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/funhiphop/81987" target="_blank">📅 23:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81986">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iLc0fLJMjua4cADnawmtvoSYdMPdp58bclIDUFa7QR2HTqHymMH8buRY9iMQzrRIMQ6x0szgRXo9c9oRv9Yv6dIgRobXOiDeLT_qLdza1pxRoUQ-78RKPgayYcXURvpqnGv2izEAicQ37PaiVYhahQO7YKs5LM7C9HVEgV1K_uK3SCfylPZ2Jn8kyG9cBh0E66xrC64_askJ5d15AqXo0d4JdESqonH_TXLJ888xMJrCN_WbjWyyK4cMifDlXevRyubHeMKJDHW058CqR0ohxUp6ujk1cHxZesYB6uH2u5yYk_nHDma6ZvBUyGWeKWltAinJ9hAHDDS8253szirQ_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/funhiphop/81986" target="_blank">📅 22:39 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81985">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RyKdME6IYNL4ujV7W_d50b0okY2NuoroAgXhPjH7LEecqAahNZx1HM1GgThf4_qgUlPTmLj3hns0TAHLC7q91slc8TlDp1mUsjIaN76ZlfmHwRVpeH5HgJ-7DZtA0eOuYYCsQOBuCLhCziwRkp-VouJmvRbSItghTMOnT-CKnFqRCYNFZjuuZpi82cR5d9fDuzRXvofhD6NaD8HGKHkIxHa9ztaGGkGnFu7Oq5PcdzgZ59HyWz-ZE-aqs0m7yvWAtyrHNQ8f8kRswYn1alel8H0tLIuEPrMDyvuMximKg1IShp8m8WgB4vBFJVap7EmpxbWNP1iyXlUk6Exm8MpkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وای این فلک زده رو
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/81985" target="_blank">📅 22:27 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81984">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">پوری تو ترک جدیدش یجا به مهدیار میگه رضا پهلوی رو انفالو کن صف تو با ما فرق داره
ما؟
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81984" target="_blank">📅 21:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81983">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">این جمله که "فدایی موزیک داد جوون مردم و فرستاد زیر گلوله" همون اندازه کصشره که جمله "پهلوی فراخوان داد مردم رفتن بیرون مردن" کصشره، فدایی نبود مردم قرار بود بشینن تو خونه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81983" target="_blank">📅 21:52 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81982">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">قدیم اینجا میگفتی کص ننه فدایی
خشتک رو می‌کشیدن سرت
الان چی</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81982" target="_blank">📅 21:45 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81981">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVX2InUjkVyqCFhoUaru3QarfiV5DIdjr-2fA3enn2gt1t6Q1W97OIyI0aL7aRztmEWELiCHV3BkEH6V8OTgdVgFhvcbGdumxUlWlYIVH2cX2Erzj171ufPZkA3hrTCZZcd4kpZ3QWYsljrGQBd9jfrIvBVtbZ0dwBHURfR0HbqRoPNFlkD4BzziFGEszjAYe6duV3q1Oyv6oE0QAmTretudQG3CcKm2Yzxy42qyOIC17Ko2B95XoQIufiHr7Xkzhe4y8eNO7Hljwvu-1Ycpny1WE0FyH-J2EiS2NcI_RqdUJWQm3Wkg2ikyNCK2H1wX49R73gFu2Pdb1Rh72lkBbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هی میگفتم کاگان چرا نظر نمیده، که اومد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81981" target="_blank">📅 21:40 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81980">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اتاق اصناف کاشان اعلام کرد:
کاشت ناخن در کاشان ممنوع شد!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/81980" target="_blank">📅 21:02 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81979">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">جذاب مثل بیف آرتا و پوتک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81979" target="_blank">📅 20:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81977">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تنها سیاسی خونی که باقی مونده ویناکه فک کنم با این اوصاف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81977" target="_blank">📅 20:30 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81976">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">من خودم تستش کردم
راضی بودم
👍
گفتم شاید به درد شما هم بخوره</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/81976" target="_blank">📅 20:12 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81973">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eb7vxf2s5uCz-Mov_CruGGmUqxDXAL2xOOMjMLWglw61jfKG3R3erSv4zadOCtI8jsnP_jQAU9CYSI1gDjFd9jTBFQwhygss82km4h-ShbIp2zGYD5XoBKKmNYXgVmeGpg_AWOrU8pYcllJjWr_Fb_IBShblCOzG5Sk5odKScaNuL1kBGHqaxtuRVszy8C54RHf6t494_O7bw_ax-BGH1pYo60YJT2XhMkwDwNcdHFdJaz8vu3JxvXHmcsKKjHdWo1sx7nFXWbwMFmOa8UhLqAN-U_QyZB3lMmqlkwiMt5JB6btPDq81GTlkc1mBlxvFF8lXv8tKtM-7B2dtaXHuxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ویناک وقتشه بری دایرکتش آیدی دکی رو بدی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81973" target="_blank">📅 19:50 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81972">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaWBH6nRG7doUeOugMhmvefQOauMdaK5X94GtZb309FVwiOMtUjHV7AgpuFvuGNCe4O6HSZX9mc74TRzPaPvcbZuuQIP6ewr3GiilmmZ5e0eEn3trQs7Eo8Cr3sAYICT1CxkVxPMhNN9i1vhldVDwiiHImnQDusS8wX48kkaXvzGFkun3iZRtoN6vYP_De4rB2Rt1i4PRvIZxwouVOUAWqN5ZFFih5Bjab3tYqW9M6JbFx0ZYN9bn7Ljohd6-rqo1KalOcHoj7qny_sM2S2ydfWn5qb2OSDvBVJx0M0Qvf0Kj2dzcfm7cSm8HSps7B9MDSAMFCdD8vSLmch57UAQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام پوری گفت جاوید شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81972" target="_blank">📅 19:24 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81971">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RH4i3o-mQ-t0k9B6MrIQUz3ulPrtmXnxFrJdOjG-OJyMrWOQ-xVsvkXZ2qmd5tOba23Kg27bO-v85z9JekBIf0p6Scp3muMZoN2r3a9Q2i52Vv7AoDJfH82CeQlbn_f3nW5sKuTwYkUHB4A3-RPnPFgHlz-lrVedN_COpKOcZElE-7wGWdkLe4VnabGI4K4TUXcJaIf4MXWjZHoZIR-4d9KyKlBh1r5MU56pQGU5yPtzJy8v4RPWQL85S6rJ975_jw4Ri2VJi2zuc-O361C0nAeYhfVgXn-yuaCunHldvaKpF7uWPBtZ0yF-V7443FwQaTIHvMpeQlfPDyg6nm331A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک قاف به پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81971" target="_blank">📅 18:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81969">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyeZx5-Qzcut44ZyqqVYspUG7TAAe8QrJ3s3l-shnDJW4gmBTA5AdeE_F0pPbyz2zVV3O5X3VnzZBgMWlDMtc2EKSt5XyXVB0SgOocILj4QacW_1Q5Z_4EEpzKa_11JeNFbjhoB4EZNl-vJBZZ0RAUow9UddH3v9VFH-YV3Xiu2G67gU628Hza_8rVx76hZKmSnLUKSbbtUeeuKrXXInWCzwjvQxA8S60WSEEFomoBVdUaxBV0OH-p8ftTPga38xs1zdDbzEDYBBynZXotsgmzqLu0otqgAWv-0zHvVy1tZo0Zf0bsgeDCJyglapg-rUeHVcKRRzaTnURCm5VicXjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییتا اون یارو که چتای ملتفت رو پخش کرده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81969" target="_blank">📅 18:54 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81968">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMY0wwbkA6e4oK_smcrVcmXjrj7nPZfElGwe8ajDvHFzmFmlNxNNVTWQfzCK7olzKbeHTG20zc7hEztrcRhjgp_vjdoioD0yjLdE4IRltrs4fb7SQ07mjSUmyYYX3X67INeprG28nd9rifaJU60oGxZq5qqNVlwZIhdWnJfX-s7CXcomHR20V79BJlIeNiq8CnCs_b1hYzbBYuRIiJaxwWk2wG1aFsAfK01HjdEBTuEy8iLD8BO0ECHGG_a0WBAimwBd8SBfAYsVUPUTNiJFBVHe9spgk7JgfSkUyx9FPWvJw8us7iyqMsT-zDZIawrxJo6zODkSM8yShqGxlT_Cqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اوضاع کار بدجور خرابه.
@Funhiphop
| Arash</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81968" target="_blank">📅 18:37 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81967">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خدا لعنتت کنه پوری ریدی تو کریر فدایی</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81967" target="_blank">📅 18:35 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81965">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">برگردیم سر پستای غیر رپیمون بابا، رپفارس اونقدرا هم جذاب نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81965" target="_blank">📅 18:34 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81964">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromA²</strong></div>
<div class="tg-text">فدایی 72 ساعت وقت داره بیاد تکذیب کنه
وگرنه دیگه مورد تایید من نیست!!!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/81964" target="_blank">📅 18:25 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81963">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">بعد یجوری از فحشاشون به پهلوی پشماتون ریخته انگار اینارو دوساله میشناسید، همیشه پابلیک اینارو گفتن دیگه، پارسالم برا اون اتحاده اومدن ازش حمایت کردن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81963" target="_blank">📅 18:18 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81962">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">چتا هم احتمال زیاد واقعیه، ادبیاتشون خیلی شبیه فداییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81962" target="_blank">📅 18:14 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81961">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">من کاری به هیچی ندارم، تو این سالها هم یاد گرفتم به هیچکس اعتماد نکنم تو این فضا چه فدایی باشه چه کس دیگه
ولی سوالم اینه، اگه فدایی کرج تا لنگرود رو نمیخوند اسم پژمان قلی‌پور انقدر ماندگار میشد که الان داداشش انقد معروف باشه که بیاد برینه به خود فدایی و همه ببینن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/81961" target="_blank">📅 18:07 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81960">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">من متوجه نمیشم، مادرجنده بودن فدایی باعث میشه که پوری مادرجنده نباشه؟ چه اصراریه داره برا ثابت کردن این.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/81960" target="_blank">📅 17:58 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81959">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترک جدید پوری به نام تیغ تیز زمان منتشر شد   YouTube Aparat  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81959" target="_blank">📅 17:36 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81958">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خوبیش اینه کم کم دارن فدایی رو عصبی میکنن و بالاخره میاد تو بازی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81958" target="_blank">📅 17:28 · 17 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
