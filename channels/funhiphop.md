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
<img src="https://cdn4.telesco.pe/file/ErhpPt5WgizFglEtEZosEsqqoGc8CneqJQnSaNcOFM1QO7eniDBke0ZWkjVSzANW7DsWb_1di3F0I_xPFJAmT6FayXwiSgvCTCM0EG1UPj9bncNxyGGLHwkq3xvrK2u620tw2WTSAGwy7M_oG4y_tXuB5_0MaJWitfTuHNZnBba4iZ1uAGS1Ln31My230B6TCe8zZ80fYluYphLtGoyw-IPR9v8PxGt0sNvt8VtiLnI6sCSou2rL4Nr2fGptDIIULHzoah_yVcDQSp5Sx5k-1QzwnvQSrW4qSY5yUng0OP8mzIY5ILW1POXrsCMpVAO2wDU61jcjNgmbJ-iUnq3g_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-21 17:32:06</div>
<hr>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">ویناک فک کنم داره موزیک یساعتی میبنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2 · <a href="https://t.me/funhiphop/80125" target="_blank">📅 17:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حالا ما هیچی، کانر خودش خجالت نکشید بعد اینهمه تشریفات با مشت اول بگا رفت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.39K · <a href="https://t.me/funhiphop/80124" target="_blank">📅 17:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6869027e93.mp4?token=SSASZbXc1_h5JYLgUNjT7dJMoYu11XS1qBL3gS0FZ3LJhq-IQ8fZEJBOLji2Vs0hHr49VIDkEP14h0uja7diK-RX66-JT-IpRvH_nL_T3HhNkQD6dbuDIS90DKzd0nCgz2dhK8bMyn6eEBE9PUA1hop5cSjM2PAmviJX-w1OgdFwF5ghdy6t8EBiiQlA7VtNz3bYnnv1S_CqCZI480RDNkevD0g4zSlMcnBiOFjqKQhAdX0hm-3GKdmmUvucOYW7iNOVk4zkCxC1qo3VfdGojbyf41DtGSH9sfwSHJmjGIRixrh3fFMMUpsoGogni37L4bPC1lPDIoN8Y0KVJEI0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6869027e93.mp4?token=SSASZbXc1_h5JYLgUNjT7dJMoYu11XS1qBL3gS0FZ3LJhq-IQ8fZEJBOLji2Vs0hHr49VIDkEP14h0uja7diK-RX66-JT-IpRvH_nL_T3HhNkQD6dbuDIS90DKzd0nCgz2dhK8bMyn6eEBE9PUA1hop5cSjM2PAmviJX-w1OgdFwF5ghdy6t8EBiiQlA7VtNz3bYnnv1S_CqCZI480RDNkevD0g4zSlMcnBiOFjqKQhAdX0hm-3GKdmmUvucOYW7iNOVk4zkCxC1qo3VfdGojbyf41DtGSH9sfwSHJmjGIRixrh3fFMMUpsoGogni37L4bPC1lPDIoN8Y0KVJEI0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/80123" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbFkH_j80uUcZjUxqHATH52Nn4uLEvBqcHNAbdrXuFpwCP4L9pj21PPg1nvSjKTDahiFG77UPdLSIFMQ0EfR2k0i7BCDcifdI7X0irFdU_GId33ENO7RzHdnmA4fzEDRt8sV16Qt643-C6QHCcYViWoaICeKODs2xgLCSsFyW8vYbSvunCbw5MNhYwDV86bMn8gho2eEHuX3SGhQDtcPwHeWrm52awQtKyBSV1UWGbIRNT9msH8q_rq2kWSbIdlxgWepgnULqxv4E0Ec8C8ln6ehfqs0r548VQKZ6yU52UceEXRFVTvIu8adOx3itkWj61waaNAaZgTwXK14d-gZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده من تو این هوا بدون کولر چطوری زنده بمونم وقتی برقم قطع کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.16K · <a href="https://t.me/funhiphop/80122" target="_blank">📅 16:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دشان از تاکتیک های ناشناخته فقط یچی شنیده ها، اومده خبر داده بیرون که سالیبا و اوپمکانو همزمان مصدوم شدن و نیمه نهاییو از دست میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/80121" target="_blank">📅 16:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80120">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4XcySMJtpLr_mJO0o0AEhouOfYkZ_6e2SeyO5WwBGjp_DrzlN4ED0lK650Vy4_zQ-9VcdZSw7EDA68lPF2q7H7yQYLHRSFgWp8S8IXXAtU1vYtpYYROnnziO-LVBRN-GETjhCnF1aDrUYCa4vyDvqysMBLeI6dr-iOC8-mm3yDjBG1vjY9c-zWOEc1NoPuo0H-ZDuhUmLsHRScwGF6KZiawkQeeRkXrvdiBPuQj6xACk91Z2AVbOAHHB0oexLnavGwrfstiEA5F4UOjnkm_0d5jRc2m4xfgZZqOuJ8XB7_EbPwcr7d231wPaC6zOuDJdzay65i86v50-17faISguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک جان کیرم تو ناموست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/80120" target="_blank">📅 16:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80119">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستانی که امتحان دارید، فکر کنید موشکا ستاره ان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.04K · <a href="https://t.me/funhiphop/80119" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80118">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">امتحان چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/80118" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80117">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این رونالدو فنایی که به مسیر راحت آرژانتین برا نیمه نهایی اشاره میکنن خبر دارن که اگه تو گروهشون اول میشدن همین مسیرو داشتن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/80117" target="_blank">📅 15:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80115">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80115" target="_blank">📅 14:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">شبکه کان اسرائیل:
ترامپ تصمیم گرفته که محاصره دریایی و عملیات نظامی‌ از سر گرفته بشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80114" target="_blank">📅 13:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">شبکه ۱۴ اسرائیل گفته سپاه به کارتل های مکزیک پول داده داخل آمریکا ترور انجام بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80113" target="_blank">📅 13:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80112">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">والا من هرچی لیست تیم ملی انگلیسو نگا میکنم تیم خوبیو جمع کرده، این بازیکنایی که دعوت نکرده فقط اسم داشتن وگرنه بازیکنایی که جاشون دعوت شدن سال بهتری داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80112" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">از ۴ تا تیم حاضر تو نیمه نهایی جام جهانی بارسلونا تو سه تا تیمش بازیکن داره و فقط تو آرژانتین بازیکن نداره
ولی بارساییا فن آرژانتینن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80111" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میچ مک کانل یه سناتور دیگه هم سکته کرده و به بیمارستان منتقل شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80110" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اینطور که اینا گردن میگیرن، همین روزاس موساد ترامپو بزنه بیاد بگه خب اینم گردن بگیرید کار داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80109" target="_blank">📅 12:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU96eQkt2rbXzKwEOm5Igvc2XTdw2fPqVRfXERhiJ0_UJ2h-BA6aC5ZcGAMUqLjMyRPwqWY6PVrDPbEu6CEmP0mNzCKfCXrqIr4BaoU6SGqXKHo5obj_ytCLbG_LS67KfGmeGo6O2kira7lhIgf7ZBvAZwdQ6-DtzDmw-aldIRAdIhiRylGFRDi3IY8-gbryvKOvlglg4BiX9PdTnr9fWMdU-w15z4eD2simRKky6IYvYKS6mATuRfkTshmvH9ioTab-fx2AsTrsVpyc3pXLAoKBMrHBxhybDJHoLVEP2RgbyUt4DmfWnz8PCAfDeZDTbYFSu6Qd5wkUm5YuPrUwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=uvDhXhlP4MHN3Ms-16iO6qPmHvs3hYi0ZSdWneudZ7JkxXJrnCLYpeOimXsqLgwLlEA9fCiOvTeonC_Q30-aYNXJuyqZbJEZGdS-3RrNqMuzSiH07Q14UsKjZK6rTQ7bIPrxTfVe5tKx_ufRgAJYQF_pzTO6x-toFFL_Xi5aZc6QGquUXO8XqwdLo1Gjp78t5MNycJVYNDeqchSuF-POzeGcS02yQBuUmCGRogDaOS_VVqMw2US0alfm2GcGs8w-wTrQ--XuxfNJ3ilcQMq5it1xqlT-1X2iHkqJthnaEDwb8uMCEbFNheU990ILAXtu5h6CDm16pl_yahKA0GjSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=uvDhXhlP4MHN3Ms-16iO6qPmHvs3hYi0ZSdWneudZ7JkxXJrnCLYpeOimXsqLgwLlEA9fCiOvTeonC_Q30-aYNXJuyqZbJEZGdS-3RrNqMuzSiH07Q14UsKjZK6rTQ7bIPrxTfVe5tKx_ufRgAJYQF_pzTO6x-toFFL_Xi5aZc6QGquUXO8XqwdLo1Gjp78t5MNycJVYNDeqchSuF-POzeGcS02yQBuUmCGRogDaOS_VVqMw2US0alfm2GcGs8w-wTrQ--XuxfNJ3ilcQMq5it1xqlT-1X2iHkqJthnaEDwb8uMCEbFNheU990ILAXtu5h6CDm16pl_yahKA0GjSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداسیما گفت که گراهامو ما کشتیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80107" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">اینطور که داره پیش میره یه ده تا کشتی دیگه بزنن از جنوب کشور یه خاطره میمونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80106" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=kCtlRqLvM9RPg4bmNkdJCtGn-oUrEuLIx-9e7vk5tjVe2O7bZ9QDKXKvGG5cO7YzsnjK0RMep6Tv4F68d674lQnmVWBDrGlo2u2ZArtD4Ybx8MipD4I_08QQMY5uWJ9IO-jg9oJpbFvFqFSXpHq743M1mGt5WLGERAhRLh3-FBGIHGJi4AjfKZaKNFyBnq6Op1wVQZIoj6mlFIZfZFRHhOXt-K-8AX2DaKa2TyP3_xrUjuSL4WyXoc3eQbp3Vd_nzm633l3nHmLx6K4pAzuCfMVieCgGK4pFUikf_0BIYItwPGRVBWcI_PsmESonRa4CDCIZpKEbh5fkn_gPIG5drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=kCtlRqLvM9RPg4bmNkdJCtGn-oUrEuLIx-9e7vk5tjVe2O7bZ9QDKXKvGG5cO7YzsnjK0RMep6Tv4F68d674lQnmVWBDrGlo2u2ZArtD4Ybx8MipD4I_08QQMY5uWJ9IO-jg9oJpbFvFqFSXpHq743M1mGt5WLGERAhRLh3-FBGIHGJi4AjfKZaKNFyBnq6Op1wVQZIoj6mlFIZfZFRHhOXt-K-8AX2DaKa2TyP3_xrUjuSL4WyXoc3eQbp3Vd_nzm633l3nHmLx6K4pAzuCfMVieCgGK4pFUikf_0BIYItwPGRVBWcI_PsmESonRa4CDCIZpKEbh5fkn_gPIG5drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر هم صب همین که وارد قفس شد مصدوم شد و فایتو باخت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80105" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80104" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">انفجار در فرودگاه بحرین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/80103" target="_blank">📅 10:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">لینزی گراهام درگذشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80102" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">آرژانتین هر مرحله که بالاتر میره بیشتر به هنر و توانایی پروردگار بی بدیل فوتبال جهان پی میبرم
با ۳۹ سال سن یک تنه این تیم رو تا این مرحله آورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80101" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گل سوم و تمام
صعود آرژانتین به نیمه نهایی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80100" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">لاپورتا ناموسا بخرش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80099" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یا خدا این چی بود آلوارز زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80098" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دوستان تازه بیدار شدم اتفاقی افتاده؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80097" target="_blank">📅 06:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cUlCKXyh6nkkorD0PFEwMd1qocB5IrXWZVmFiSUNVVg0_YLkBSQRDBYnFxoVwL2JadvDgGCxBPbanubQ_VRomWhkWTUX5AlwRgeX35gIlsxSHPo19n18s0T48prtedJjNoUSbDt59-TG-ZiFCWijMXH5mk1VwDB1ZDAjf7celV9xQaJ69s5GcL6P0gXQuo_OAkPxXX-PLA7c9BXheq1yTRMkTXF7JJpmdmdnLKSiSnOMSjEQvfv0dYkBT9EW5x5VeXplv7UTj2_yuD4aPiPv9LJuppTQ_wrVIZ6gcIAM-aufRIOff9JqMdx4f1xR5Wtuk5Bcev19fDZAEqvGHcMsDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آرژانتین مقابل سوئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80096" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پیت هگست: ایران انتخاب بدی کرد، حالا تاوانشو پس میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80095" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فعالیت پدافند ها تو تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80094" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=kuARoyk9gEtpPrphxsvIX-h3JTYf5LLCBb6iYYDXFYFQKw3ln2QzjTlS4vubXLJzKMIZYy4gpphqcJU2moHTWtszDeX6N0VFqce6rs05rTiswjYA_Os_AhFypz6StnjktG1-nvmemMDzGY3uaDl4cIq5T3Rib6LZarlPjgpjMLppw9FtB6E6RE4tDUA8ejblxvHboa5wQHGWHqn5cni-c-dNoVBdo2y3Vx-0T3EY7R8sY1zy4G8zzxfynY8mFI3DBb9SAprVVyqrw0KzKy1NP3SxLDM4lUKCjnnvK1r3pAMqsWMgyKK5LLX78wx_17sOWgO57vb-vbtOvo0Xf78EFjaQO0pKVL15ZHWeFsxPzEVvMZMldMkVVA2fud90pUU7UDGtjOK244kum35V6caikHqWo86k5N-FnpTaxDOnjQmSeEQ9srAQ2OsN59qyQV26jHM8rqQRNZJu9p7eQ_viHwXaDpNXneDhKXjZEcefaWCSG64RFdU-xzyFdVKe-d_Tdza02YEFaTMUtgfXShhpU3Z2wc0AHBnneaZzBDQ8dWYj1e9PEe8VSmJEGDzoZw25LKvSibj536MrRAFF2geDJsVD5SVnzTak-tweWcNpGIY0pvnV0A5CeKngZsABXdpDdemVfKcPqIJH_ymweXxsYHzIW1jZn7_GFeVt3XtWdyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=kuARoyk9gEtpPrphxsvIX-h3JTYf5LLCBb6iYYDXFYFQKw3ln2QzjTlS4vubXLJzKMIZYy4gpphqcJU2moHTWtszDeX6N0VFqce6rs05rTiswjYA_Os_AhFypz6StnjktG1-nvmemMDzGY3uaDl4cIq5T3Rib6LZarlPjgpjMLppw9FtB6E6RE4tDUA8ejblxvHboa5wQHGWHqn5cni-c-dNoVBdo2y3Vx-0T3EY7R8sY1zy4G8zzxfynY8mFI3DBb9SAprVVyqrw0KzKy1NP3SxLDM4lUKCjnnvK1r3pAMqsWMgyKK5LLX78wx_17sOWgO57vb-vbtOvo0Xf78EFjaQO0pKVL15ZHWeFsxPzEVvMZMldMkVVA2fud90pUU7UDGtjOK244kum35V6caikHqWo86k5N-FnpTaxDOnjQmSeEQ9srAQ2OsN59qyQV26jHM8rqQRNZJu9p7eQ_viHwXaDpNXneDhKXjZEcefaWCSG64RFdU-xzyFdVKe-d_Tdza02YEFaTMUtgfXShhpU3Z2wc0AHBnneaZzBDQ8dWYj1e9PEe8VSmJEGDzoZw25LKvSibj536MrRAFF2geDJsVD5SVnzTak-tweWcNpGIY0pvnV0A5CeKngZsABXdpDdemVfKcPqIJH_ymweXxsYHzIW1jZn7_GFeVt3XtWdyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک  ATACMS/Prsm و HIMARS از خاک بحرین به سمت ایران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80093" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80092">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C09YrrBGrdpqXLMt1y7kCTbaCYlhqoL0sWqSQe0UqEbvAlE7Xgm51EYO88IqYrcsop4dsg8yzHY4GS0mzOqhW7T0mcX4X-tMWzDFN4bmsZhIrAXKvrvt8UMoYQvPGQmBNOxS8bi5V5s0z4hwbRPR9vv3CC733VMBcNG53qHCn2dklFG1VWukusarJbPI2DsqUJG2Jkb355Nl_BIVLXianNepmzrsRnMTzBp_aMzN2MA0mfNY74-zgKvmJ1BM6ed0lwbPubNrXhi3jYT6wTCTY_kHu7skRwWNasOcOOKeCUnZ2XxIAC9MjhufljQKe5W2TfAy1taFjdeowqGAFye57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این روش میتونید دینی رو تو یه ساعت تموم کنید و برید سر جلسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80092" target="_blank">📅 03:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80091">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سنتکام: سومین دور از حملات خود علیه ایران در این هفته، پس از حمله سپاه پاسداران به کشتی GFS Galaxy در تنگه هرمز آغاز کردیم. یک غیرنظامی مفقود شده و کشتی آسیب دیده. هدف از این حملات، تضعیف توانایی ایران در هدف قرار دادن کشتی‌های تجاری است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80091" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80090">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AflVPHwvPAbYnMoNl9HdQDLuscJdmcJn-m-e1BW0c7jnsTD-ybblZWR1Nk7wrJyT2GVGpdyUwzx903bTv7h35V33qka-9FrIFbE7GcFUoiGLyS_7AH4Z7w74TpkZeDnePUhpor4VXHD1qjw4RR9FAJJFzu0lwz8mPjBd81wavDqaFoEDhJEg87jGbpe77slbgcU5ZmOnuPZDQVdKNcNRTXwU7jpRR0AAa4WyNlUBbkraeXIfa3NqMVOss6vxcjBhHY5yu2up1kTby-wSa7Eq6W9M1btN4Vfy2eQoA-iQQMr8iQlKPgaDJF2kcIS9JuUzaCf-P5iEuy75AWJxcTgTzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این است خاورمیانه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80090" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80089">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شین: انفجار در بندرعباس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80089" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80088">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آمریکا تو حملات امشبش به جنوب ایران از موشکای هایپرسونیک استفاده کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80088" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80087">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رسانه CBS میگه تهرانو هم میزنن صبر کنید فقط
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80087" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80086">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام اهواز انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80086" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80085">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxIJX8p-fKaS8CJkUj9szC4zAZjx_rp8AUApGyQ6c9krRoAv5FLGwf4Zc7cJPjm_sG7WThC0raUPzA-eFWw5SPEDsKB5EJ6lE0CaVrhdHOqeTENdwfMLVRrAmUDK_uQpw5p3DxxrBQDgdiDtMpxgX3e1x25KvmGBRFYA3XzF4KxwBY2S7V08ZI2aTThiS6KX4FZ1y6aqq7t7QCJc3WmYIT3KuN4lkSxcYDhCmWsKfbOP4fLA2PV6UWu3KpH4Ow8T1IrlIZQ6aZAuxmXXahVhdhhhyQVB4VaqVLK2a_DcMqVH2P05o266wzMNipiQ5lNGJWTq4HuxNZn4GCRDKBTtYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر دیر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/80085" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80084">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">صدای انفجار در بندر دیر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80084" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80083">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سلام اهواز انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/80083" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80080">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">انفجار در کنگان  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80080" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80078">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">انفجار در کنگان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80078" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80077">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">بوشهرو زدن
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80077" target="_blank">📅 02:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80076">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">نروژ عزیز لطفا تو دیگه امشب فوتبال رو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80076" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80075">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">فعالیت جنگنده ها در اصفهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80075" target="_blank">📅 02:49 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80073">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">انگلیس زد که مهم نیست ما خاورمیانه ایم</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/80073" target="_blank">📅 02:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80072">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بچهای نهایی خوششون نیومد
العربیه :
هم اکنون تماس وزارت خارجه پاکستان با دو طرف برای کاهش تنش در منطقه در حال انجام است!
﻿
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80072" target="_blank">📅 02:39 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80071">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سفت بشینید انگار اسرائیل داره میاد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/80071" target="_blank">📅 02:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80070">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گزارش فعال شدن پدافند تو تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80070" target="_blank">📅 02:32 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80069">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">هم اکنون علاوه بر فعالیت یک آواکس آمریکایی، بیش از ۱۰ سوخترسان نیز در منطقه نزدیک به خلیج فارس درحال پرواز هستند
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80069" target="_blank">📅 02:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80068">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کاتز وزیر دفاع اسراییل :
ارتش اسرائیل برای حمله مستقل به ایران آماده می شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80068" target="_blank">📅 02:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80067">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">‏سپاه پاسداران مجدداً کشتی‌ها را هدف قرار داده است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80067" target="_blank">📅 02:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80066">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">منابع عبری : مجتبی خامنه‌ای شخصا دستور بسته شدن تنگه هرمز و لغو مذاکرات را صادر کرده است
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80066" target="_blank">📅 02:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80063">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اونایی که حوزه شون بغل مراکز نظامیه مراقب باشید سپر انسانی ساختن برا یه سریا مزه کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80063" target="_blank">📅 02:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80062">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">خب امشب منتظر پاسخ ارتش امریکا باشید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80062" target="_blank">📅 02:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80061">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ترامپ: دانش آموزان عزیز ایران، کمک در راه است.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80061" target="_blank">📅 02:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80060">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ: دانش آموزان عزیز ایران، کمک در راه است.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80060" target="_blank">📅 02:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80059">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdKO8pFE4G9Bj2wxBFxgdaplRgfo6xOo4emrncRQfsf_ZyO2fVEUZFrtc5iOGk1yxCk-2ZZOT7_XgAzr--Gt-qI9Zl-g1H9BuAYt8Ry8Eho77EfDvSiS3jZX47yx4ew9gVQW-mFCD5xVaRKmm24Ips3l2S8sbXb2TAEppeXY_m0AXaMb75TDQlngK30VnYSa1k92hYbWB8w6OEf_i-PthAwXER6IZt1zmdkXPrY_9kCNC_bznPEzJfnh_Vd5epc0FRaGWNVVwmEZvglP-gDUf0ZXS4q6enNurB54MmopJmPf11MidMXGlQDYerx6Q48lfb1NDdTJpsKjjCCpgT_0jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بشینید راحت بازی آرژانتین رو نگاه کنید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80059" target="_blank">📅 02:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80058">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بابا ما نمیتونیم همزمان جنگ وایکینگا و انگلیسی ها، دکی و ویناک، آمریکا و ایران رو تحمل کنیم
وایسید نوبتی بزنید</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80058" target="_blank">📅 02:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80057">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">تمامی دانش اموزانی که نهایی دارن درحال تحسین سپاهن بابت همچین کاری
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80057" target="_blank">📅 02:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80056">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">اکسیوس به‌نقل از یک مقام آمریکایی: کشتی مورد هدف قرار گرفته و آسیب دیده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80056" target="_blank">📅 02:00 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80055">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دانش اموزا نخونید که خیره نیرو دریایی سپاه:  به یک کشتی که قصد داشت امنیت تنگه رو مختل کنه، شلیک‌اخطار‌ انجام دادیم.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80055" target="_blank">📅 01:59 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80054">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دانش اموزا نخونید که خیره
نیرو دریایی سپاه:
به یک کشتی که قصد داشت امنیت تنگه رو مختل کنه، شلیک‌اخطار‌ انجام دادیم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80054" target="_blank">📅 01:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80053">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">نیم ساعت دیگه اولتیماتومی که ترامپ داده بود تموم میشه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80053" target="_blank">📅 01:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80052">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اوه اوه یاران آلفرد گل تساوی رو زدن
بلینگهام زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80052" target="_blank">📅 01:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80051">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">یاران زنده یاد بیورن آیرون ساید یه سوپر گل مشتی زدن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80051" target="_blank">📅 01:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80050">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">نیم ساعت دیگه اولتیماتومی که ترامپ داده بود تموم میشه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/80050" target="_blank">📅 01:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80049">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نیم ساعت دیگه اولتیماتومی که ترامپ داده بود تموم میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80049" target="_blank">📅 00:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80048">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ هیپ هاپ موازی ]</strong></div>
<div class="tg-text">واقعا چطوری میتونید بیف دکی و ویناکو ول کنید فوتبال ببینید.
@ParalHipHop</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80048" target="_blank">📅 00:10 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80047">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">فک میکردم دیگه دکی مثل قدیم فن نداره تا کامنتا چنل کاگانو باز کردم دیدم همه دارن سر دکی بهش فحش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80047" target="_blank">📅 23:43 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80046">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">پویان مختاری سه ماه تمام برای جمهوری اسلامی مالید تا برگرده ایران، وقتی برگشت تو فرودگاه گرفتنش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80046" target="_blank">📅 23:28 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80045">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">دکی تو بک گفت پرچمو تو دستت گرفته بودی در حالی که خودشم پرچم دور گردنش بود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80045" target="_blank">📅 23:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80044">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تا الان کی زده
دکی
🐳
ویناک
🦄
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80044" target="_blank">📅 23:03 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80043">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فکر کنم محمود داره یه 20 دقیقه ای میبنده</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80043" target="_blank">📅 22:58 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80042">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">بنظر شما کدوم میوه مادرجنده اس؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80042" target="_blank">📅 22:51 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80041">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">بنظر شما کدوم میوه مادرجنده اس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80041" target="_blank">📅 22:44 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80040">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">۱.۵ نمره خودتون تو امتحان دینی مهمون فان هیپ هاپ باشید  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80040" target="_blank">📅 21:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80039">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80039" target="_blank">📅 21:00 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80038">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E7QkoeNCrqxfGBY_CDftWOplnBwYaKJ9kFAfvfNs6RploltaTLLnS9faYcBd4XV26i-ylEoCjsRCgTlPppeblf3-HwfrqdVlSbloR8J4zUfgevg8mMDjZBukHe0-qBPnSaIVpsr6dcpLhsUaHLQS6-g3gR1jwyIornq-4KLfx8cRg6BVH5e3R9G9OyXWghmG6rvYJLxYGWm7ZOpQsWiLErnfVHEHm7syMfm5EBYDeQJKrkbHRVin1h6j2TCOv4zLge5H_Zc3D6yz03nrQ_a4Kp7shERFW7gnylL1FI9HJHggpWYAyX8yR03GPlPbvVEivJzIuNsuqcyn6PDr9q5uUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لطفا هرچه زودتر اقدام کنید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80038" target="_blank">📅 20:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80037">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ولی خدایی ویناک چی فکر کرده خواسته با این فیلمه پولشو پس بگیره، پیج صدفو باز میکرد عکسای بدتری توش بود
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80037" target="_blank">📅 20:36 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80036">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استانداری مشهد میگه ۸ میلیون نفر اومدن تشییع جنازه خامنه ای
یه حساب کتاب سرانگشتی کنیم: با تراکم معمولی (۲ نفر در متر مربع)، این همه آدم ۴ میلیون متر مربع فضا می‌خوان. توی خیابونی با عرض ۴۰ متر، طول صف باید ۱۰۰ کیلومتر بشه! یعنی تهِ صف تو نیشابور بوده، سرِ صف تو حرم! دمتون گرم، حداقل جوری آمار بدین که با خط‌کش جور دربیاد.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80036" target="_blank">📅 20:31 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80035">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcZfz0O1cbmCthCclaYVvkqBBsv1vHreJ7c2tAqccvFDam6HazrN3xvLpOOmJeQ-Z_VQicyA4ujyeHScYTizzULCHy8CsnTRfGKEW2xPrafDrIUaclNbhjTH8OlSkT07IU1FfxVQ_QHnb_BH7kmk4IBrs4C5xKhPJJOYaCdHRriDgx26g7FtpHcozizHmQJ-h5vO9mCodr017z8cfk2sUjYskOAJEZ4KwLRkbq7T3ZrTUtjoj7qm7ORrvTJGaibkzPo-kEmsuEVxlx1dL-4FZGJQ37DoqibVSwW1lAp3wsPY5YQxDq-brh6Z7DzRVyKPMitQa7nW5Z8M9sagSZhQ3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوربورد یه ورزشگاه تو کرج :  @FunHipHop | Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80035" target="_blank">📅 20:19 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80033">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80033" target="_blank">📅 20:14 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80032">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ویس جدید کاگان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80032" target="_blank">📅 20:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80031">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714a553f9d.mp4?token=YxuoDE1iI9l_Egcu_GCObtAyLrlmFyFEybXiwaGu0Bn5SCJ5N_VI7F96gccUFHHr7glqfKRUMWif51GrmQ4KSNAsG6Ecr4sdwMivvR90ObotR1kFxPnz88ZTq05YE-N2wGPsyjsj9XBK_-yWUjW9avAPwm7_qbntJNVznf2PXCNfiMh_XhfVRUc4EWBBIXDSrzaIjin635sThorvdmuOVmhX2aLTpD3feRUzKvG-FXfFM3VFqmZoI9xjbTtR83ulu1u4pHWSGQXjmBTzUWlUMPS3RxbnAWDzLagg26Et5-cxZxr9cIgLESBqCVh90xRAmXwrPRcbOSE6rD3--n3kt1YhedcFxJ1Eg8BLaGiTaTJCtep-fIwdTzpPbZAd8zW6FqHFzTZkjW3dbCavN0TYHvk3B-719ca-kPf4zhdaq3JHPmxt9uSfA0Vi4fH_E0LcMeVwrCWQ3nWQMMttha5H4G3lbAMj_z0OQCY7vqXTiPhrpKszC-bCjiNcL25swt0toDsX1Dx8CSxaZbr4ra5Xr9s6zb1rAYtSNzgpVJQYSLTS3AHJ76Q-HbbsX1im8L14z5gOK4G7PoCCx2Wg0LfHsYvS2ukrnm9gzsQQZqjXyRwzmNCiXy0xTh7eynr8ed5L73GJx1wBBB3D733G3MTyS4PN4ny0XiAG-ZazPBahHZ8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714a553f9d.mp4?token=YxuoDE1iI9l_Egcu_GCObtAyLrlmFyFEybXiwaGu0Bn5SCJ5N_VI7F96gccUFHHr7glqfKRUMWif51GrmQ4KSNAsG6Ecr4sdwMivvR90ObotR1kFxPnz88ZTq05YE-N2wGPsyjsj9XBK_-yWUjW9avAPwm7_qbntJNVznf2PXCNfiMh_XhfVRUc4EWBBIXDSrzaIjin635sThorvdmuOVmhX2aLTpD3feRUzKvG-FXfFM3VFqmZoI9xjbTtR83ulu1u4pHWSGQXjmBTzUWlUMPS3RxbnAWDzLagg26Et5-cxZxr9cIgLESBqCVh90xRAmXwrPRcbOSE6rD3--n3kt1YhedcFxJ1Eg8BLaGiTaTJCtep-fIwdTzpPbZAd8zW6FqHFzTZkjW3dbCavN0TYHvk3B-719ca-kPf4zhdaq3JHPmxt9uSfA0Vi4fH_E0LcMeVwrCWQ3nWQMMttha5H4G3lbAMj_z0OQCY7vqXTiPhrpKszC-bCjiNcL25swt0toDsX1Dx8CSxaZbr4ra5Xr9s6zb1rAYtSNzgpVJQYSLTS3AHJ76Q-HbbsX1im8L14z5gOK4G7PoCCx2Wg0LfHsYvS2ukrnm9gzsQQZqjXyRwzmNCiXy0xTh7eynr8ed5L73GJx1wBBB3D733G3MTyS4PN4ny0XiAG-ZazPBahHZ8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏یک پسر هیجده ساله خرم آبادی یه رولزرویس رو یک روز بعد از ترخیص شدنش از رو کفی دزدیده
‏ رولزرویس رو تریلی ماشین‌بر بوده این با هیجده سال سن اومده دزدیدتش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80031" target="_blank">📅 20:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80030">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XdVdk7x_xu8pBMRjw6eN3vwJjEkILwMwbl-7hus9hZh6da1hHiZ72OYjHaQiD9clZvKmEYJ7FCaW7V51Hrwd3WySLzcsHkDwQS586QVMVzXhFC7-a8R_F7v2PxPpGVnVWtvJBwO_FnyhkTz1WInk1nGnfbxWjV3FrpKrDdIN9eCmgiVHjy1HX675o8qYIHkNrjEivPw2yaY6gYanxXqAO3kZrCp3rXlBMsvL_vTrZuTBJKDaqsnC3CBSh2kp90dR6srInS8f67R7z9u_EOfWF9SNu0OYDuXywR489n7mIqvbknNaOGmp_fy_lcGQ9NJWsHR1auomjVALMdCLdzWgeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوربورد یه ورزشگاه تو کرج :
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80030" target="_blank">📅 19:54 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80029">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">شاپور بیا رپو نجات بده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80029" target="_blank">📅 19:52 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80028">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">شاپور بیا رپو نجات بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80028" target="_blank">📅 19:50 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80027">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">محمود فکر کنم دکی هنوز نمیدونه منیجرت میخواد هرکی زمان جنگ به تلگرام وصل بوده رو بعد از انقلاب اعدام کنه وگرنه پانچای بیشتری میخوردی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80027" target="_blank">📅 19:41 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80026">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">وسط تابستون برفو میارم بزات</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80026" target="_blank">📅 19:29 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80025">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خلاصه دیس راجب اینه که ویناک داخل ایران مخبری کرده سروش اینارو فروخته، خایه مالی کرده، ولی کیر شده
و میخواسته با فیلم رقصیدن صدف قبل از پخشش از دکی اخاذی کنه پولشو پس بگیره ولی کیر شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80025" target="_blank">📅 19:18 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80024">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80024" target="_blank">📅 19:15 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80023">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/80023" target="_blank">📅 19:13 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80022">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80022" target="_blank">📅 19:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80021">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80021" target="_blank">📅 19:11 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80020">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد  YouTube  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80020" target="_blank">📅 19:10 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80019">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qQuzsjDF0FfTXDOEUt6LsqfY_6kzJMY0WhIQnAwJQwTG1mZ1bDCQWAEKNouwXTkR3DCrrJJaUluXmqODQfzabKyW467YlTsWIwQkM-6PmAbQG05BZzj_LhGCb09c9m-C0FrzyoPmxzJHt3_TlOW5H87zBn3Spp_oy9g5NJwJri0z_l5l1ED91imiUXTrsXhrLzxGAAbfEC4_pP2E6RRdNpXAhoQCs85IkMJBmGRqTtzBciF_sLN_faB_Cz4wQ4pxFBUlH2cSwBzH103W5bwq6cXGeQyWjVQb0qgfIlTr_xwnChOsRU27M5sEC5rbt5rH0J1goZEKE7gqCLu6sV-Apw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس بک دکی به ویناک به نام انحلال لیبل منتشر شد
YouTube
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80019" target="_blank">📅 19:07 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80018">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">بیگ شگی معذرت</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80018" target="_blank">📅 19:05 · 20 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80017">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دکی بک داد دوباره</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80017" target="_blank">📅 19:04 · 20 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
