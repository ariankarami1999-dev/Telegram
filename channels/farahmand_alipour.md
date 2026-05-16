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
<img src="https://cdn4.telesco.pe/file/crjvH4-wtC2X585RNZps01PPoysuokcr0RHmiNBbTsMCM57zmFnsmzQ8Pe3r8pO6x9VlB7NAetwaXlzhPbvjaQJxl4DUlmdYCYYm6nuJlRIL7oM37vqo1e6I1ElH9JD0AChQqxeDl9w_BsFZM2Ry8ctt_m23S1N2TLoQEInmmsj0cw738mYvQh7v687_JT5TsN6VmZTDgJ3yr2s_jxLoH5ChyDZVDRj38Ac128hF8YP4EX-30F8mIYUEjaizNlSwM3e3cpnCW1XZPNzlVY9NH2jGRmHv8C5IaEBnZCzjrndDAhOmE0ac6LDjXDE6IokHnBvy9gVkgaTZHM_3_2s-MQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 61.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-27 01:10:45</div>
<hr>

<div class="tg-post" id="msg-5013">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=XHd0facDdDaYz76imKcDp9RMMs-SF1Uth7qw3jXc6zoWwW9_g1wtpc87MvEqCQZhdr6Q6Zhc0q1sAP__IvnOcRaWhu1V1_peq4a6kxrwHB51pfknqyFGZZ8YZBRRYbs-UakMSVPpJJ2vhgsj1XvMm-7ZVrZ2_Md4F19XIr8L8K7ngzBngX7a5DbeKr6oEc4gZbUVr0hU6yPSZLteHF4Bgslq7rMctFBo8qu89bzt8EDwzSbCxUWYieCzSx_7EdS2zO893SLImzJ_oavXBLRrMV6iGPwoge-rIRFKjV-GWhziykNzNAmV6HWYFfr2BdCx1ROAKNKvm0jR7KvQr2L09g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0bc557a11.mp4?token=XHd0facDdDaYz76imKcDp9RMMs-SF1Uth7qw3jXc6zoWwW9_g1wtpc87MvEqCQZhdr6Q6Zhc0q1sAP__IvnOcRaWhu1V1_peq4a6kxrwHB51pfknqyFGZZ8YZBRRYbs-UakMSVPpJJ2vhgsj1XvMm-7ZVrZ2_Md4F19XIr8L8K7ngzBngX7a5DbeKr6oEc4gZbUVr0hU6yPSZLteHF4Bgslq7rMctFBo8qu89bzt8EDwzSbCxUWYieCzSx_7EdS2zO893SLImzJ_oavXBLRrMV6iGPwoge-rIRFKjV-GWhziykNzNAmV6HWYFfr2BdCx1ROAKNKvm0jR7KvQr2L09g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آموزش کار با اسلحه در مساجد</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/farahmand_alipour/5013" target="_blank">📅 23:48 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5012">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b965352735.mp4?token=WNzUC9LvqNTh1v8GsTktaUNvapW2U0Th0BEfQEnTyNKUZTVdyKSyHMgo2GKHm4zv5NBCOffxcz6hn164ulMhE24nm07k1wV569sDtYCjfGydxXn9Jcy8PYlWJMlAqSue4KZ4iIlbWRrzzO3NBgaQ5J0LbVZrzEvaOuOzcbRDpDyd1SYuz5THjZrlHaVIduAhTwTOT74bSMh2GxSpfQeHsiAALumGZ41Iafc8dtVbIm1SKUPcPAdNWNvYOA6utmSm8AIuj7vYPLlsHENDTGnzCOSFmcrejTRYsOvIdKPn1n73AgfxMXm-8jlgTRkVrOAxgt0JYK2hgfQ8Wg05-FAW1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b965352735.mp4?token=WNzUC9LvqNTh1v8GsTktaUNvapW2U0Th0BEfQEnTyNKUZTVdyKSyHMgo2GKHm4zv5NBCOffxcz6hn164ulMhE24nm07k1wV569sDtYCjfGydxXn9Jcy8PYlWJMlAqSue4KZ4iIlbWRrzzO3NBgaQ5J0LbVZrzEvaOuOzcbRDpDyd1SYuz5THjZrlHaVIduAhTwTOT74bSMh2GxSpfQeHsiAALumGZ41Iafc8dtVbIm1SKUPcPAdNWNvYOA6utmSm8AIuj7vYPLlsHENDTGnzCOSFmcrejTRYsOvIdKPn1n73AgfxMXm-8jlgTRkVrOAxgt0JYK2hgfQ8Wg05-FAW1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست جدید ترامپ
که مشخصا اشاره به جنگ با جمهوری اسلامی داره</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/farahmand_alipour/5012" target="_blank">📅 21:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5011">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/316762f84e.mp4?token=jA1IEzA08HcsY2yuAnVJlQa8uPoTfrwgrftnp1TcbZ-dfuRf-7kfKnnWR5Epo51vswyjkkuVIeGNbM5_ZRL5-SN1dQJnT63jgiQdWeo59gC9RG3a59_A16rdis1JQ5yw6T6FRnIqXzNTIuWGDoV0ny9igBoWrn9WVb_X_cj-Vqd91KLDOC-OdmAjS4D0g5Ug2KTQuKzWbVcLoqyVZ_OXWlJt-xt68-7R3wbq3Y9QWtn3xLmcBK_7MIVu_j9ZZFGHhr6Vf4ocrp5hQmnnOW6383Mh8RwsFAyRZzdgfIdyYrcnoKgD2HjfC3nWwxu0eBtXn9he8K5JfOMk_v-72gDAHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/316762f84e.mp4?token=jA1IEzA08HcsY2yuAnVJlQa8uPoTfrwgrftnp1TcbZ-dfuRf-7kfKnnWR5Epo51vswyjkkuVIeGNbM5_ZRL5-SN1dQJnT63jgiQdWeo59gC9RG3a59_A16rdis1JQ5yw6T6FRnIqXzNTIuWGDoV0ny9igBoWrn9WVb_X_cj-Vqd91KLDOC-OdmAjS4D0g5Ug2KTQuKzWbVcLoqyVZ_OXWlJt-xt68-7R3wbq3Y9QWtn3xLmcBK_7MIVu_j9ZZFGHhr6Vf4ocrp5hQmnnOW6383Mh8RwsFAyRZzdgfIdyYrcnoKgD2HjfC3nWwxu0eBtXn9he8K5JfOMk_v-72gDAHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی  تفنگ به دست در تلوزیون ظاهر شدن خوبه یادآوری کنیم از سلف اینها خانم «هاله مصراتی» که ۱۴ سال پیش تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/5011" target="_blank">📅 19:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5009">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LbZfCG7xkByBP5up67Ovq7AoGeYCiCWTCIByWxT1kPaTs2Quee0w-GKKkKxs6QErBE9Kx2kYgMSIHFZZFbgoeyQJGt9D_QUCSzvrnxMlPJMheXFzjSv3AHWGyj0NVp64PTSRuf5zGSmctTK1pXbkjZpU1LEHQ41vKtNvZft1Yvj8FqVNZJ9ab_B8aeqT4C_r9d_DTBhm9wnmqfMHgR9rW89qlYkG4hbIvblGieUAi8MEuBKGqdcOVmuoVupXz6-eFI83N5YEL1Fz7OOGIVs9Wn1eu6qs63PCzIzOELuTIdEIlcnRn0Zb-ByR_-vQv24oBBr2GuKdPKmgjFaxQzTm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v2-L8uJg3DeOnFDMF_KHxZ8S9aT_GNH2ZFPizgYXeoUfuWjl4PAK0xWLtamzmOsofrD7pMbybLi5pbrkHe46EDvTySnVcijAxhhALHs8ByUz1FKdXid9o88d8Q1Swk7Z1ThK64Jy_vAN6ZSD-SkwVHq2Uq_C_NBp2mSXi3Mi1gO2tSRNouEWtdFO0NuCdInvQN2YeCdVFo-it-e5aHT6UI9KCDJ5H7EXSicvXi-eCpsUEjCB597Jbzv3PLS4tcCjXFnljpP3VwI4fHk9B9F69j7-MjFzlor-4a4g1d6ZvuvrWRXxAUpCl5qhMiQRzPHjiuDT5eAnz-PoGyqHxHk1Rw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا که مجریان جمهوری اسلامی
تفنگ به دست در تلوزیون ظاهر شدن
خوبه یادآوری کنیم از سلف اینها
خانم «هاله مصراتی» که ۱۴ سال پیش
تفنگ به دست در صفحه تلویزیون ظاهر شد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/5009" target="_blank">📅 19:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5008">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دوستان بزرگوار، این صفحه به‌صورت مستقل اداره میشه و من تقریبا همه زمانم رو صرف انتشار و پیگیری اخبار میکنم.
اگر این محتوا برای شما ارزشمند است و اگر مایل به حمایت از ادامه این فعالیت هستید،
این لینک پی‌پال در دسترس شما :
PayPal link :
https://www.paypal.me/Farahmandalipour</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/farahmand_alipour/5008" target="_blank">📅 19:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5007">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">در ابتدای این فایل صوتی که خبرگزاری فارس منتشر کرده، به نقل از
حداد عادل (پدر زن مجتبی خامنه‌ای)
نقل شده که فرزندان مجتبی خامنه‌ای در این ۷۷ روزه پدرشون رو ندیدن!</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/5007" target="_blank">📅 18:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5005">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iLOwUyn-fRlgKspfHwRk34Ae-u2FeArOZyd4y7sFEg4TVkN_B2DBHh_r9R3po-nKapjz_1IQ8PL-9VrFF1sAqXwBi8U1mpsfJPtPQXKLX7fI-n5kVTXXTecyyJmXDqUWyVO1DF3XuMQEJPScnrxzbD7lsvwm09C69CqT91TgqChqcDXxsQqx-7Hf3hPBipwK7dc9tXq22NSBS83aOdvcx5o0-88MenBy5Jt2OoxphMiFdZUDHV_oSeWru3nUD7P53yumg9xAIThDawEoHmbd1tA3BDlda29hXoEjMIXK0HCFhDxm_-IOVxt9KrbfYwpdOxxPh5ZkvETI5-8dT4rCGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hddSQqW5W2IzcEtBuo_WTsODJXL4tqJiFM2o-Vp-mVHSIGjC9VATOUK1i9sGCaVb-IFsAa_vzJicIeN0hvatKflg18_u89_b8r-OrE-CjwUqz0tlJP_bg-9qHA30mNZdTWPrDK6sP8DbIieSI0DhNIotd9kHmb6tKpb8M3qxVtyj53sykdrMXpC-sqtuNT_VpcTyKdpB8-HtEu2VvNKFF8aOqn7PDdZ8UjBhHYYi7p6SPTVxJfYwdLrvljC_DHUgyfNGNLrhcnv-r8wgYqm7XhCyYAsES4C99tdcTo95_SP12o6Jg0-khdPntCvzeOgfeN866QNEe_i-g_YCXP65ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟  چرا خانواده ، چرا فرماندهان؟  چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته لذا شرایط عادی در بیت بوده»  صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/5005" target="_blank">📅 18:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5004">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sLppUA6iSgjWa4-HVPYKMe4SPLDmkbuP7N4Q52ty75uNjhFv0DNh0-IUx7S2NZYgi5EyjIMywc7MUa9tM13Y8pKfa5MIuLadD3IkGt8PtengEvBSR5zD3I8kqftdBZBayhpReBlLsWTn20_2zciHMizkrMFS4m_HR1Gydm7UrSMHthv2UBstq43kTLPLi8NngGF6A2a-z6hHmiOt69jvBIhJ0YvR1e1m0cV6qdEHEoRo4JV1ERQg97CTcCTFrPPJMUTuimVCa6IgDehAHYqOSwRRB0i1O4qhLTy5qAnqvSOn467IEHEuleq0eY_g_kdZWB6to6HzcSPXoyMRA2Gu9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a3c1e532d0.mp4?token=sLppUA6iSgjWa4-HVPYKMe4SPLDmkbuP7N4Q52ty75uNjhFv0DNh0-IUx7S2NZYgi5EyjIMywc7MUa9tM13Y8pKfa5MIuLadD3IkGt8PtengEvBSR5zD3I8kqftdBZBayhpReBlLsWTn20_2zciHMizkrMFS4m_HR1Gydm7UrSMHthv2UBstq43kTLPLi8NngGF6A2a-z6hHmiOt69jvBIhJ0YvR1e1m0cV6qdEHEoRo4JV1ERQg97CTcCTFrPPJMUTuimVCa6IgDehAHYqOSwRRB0i1O4qhLTy5qAnqvSOn467IEHEuleq0eY_g_kdZWB6to6HzcSPXoyMRA2Gu9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔈
🚨
چرا خامنه‌ای در پناهگاه نبود ؟
چرا خانواده ، چرا فرماندهان؟
چون «اطمینان داده بودن که کار نظامی در این چند روز صورت نمی‌گیره و اتفاقی نمی‌افته
لذا شرایط عادی در بیت بوده»
صدای ناصر رفیعی</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/5004" target="_blank">📅 18:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5003">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پیام‌رسان‌های حکومتی «بله» و «روبیکا» دچار اخلال شدند و بعضا از دسترس خارج شدند.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/5003" target="_blank">📅 18:31 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5002">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aTzijaqj3SOf_d0w7LffZQPGYtHfe6ewVp1Pprx_zYYFjMeylNKMRxlwa3fiQaufyR8GUXM15o3V56DV74Nnxy7d9LkJvgpH1G7miFNT-sBER5mhTD8-4fdrznqMTs1ECZJyY19SlnxgZbfogyxTmZd0IehvI-OiNPJEIewhVvT3torO-YsbZHlJ_vP_oLC1CXW3XuaC9Mqb-y1J2IH0liX53Fkierz2sJ4DQKl_pUGrZjfhxFXITPSZ_WPvlWJsKpHaC0zyEKHwgySGAi51qzcx4RNhoY44EmOLUjd62GBC9DsZp2YOf2JWTUZAY9QILXyByVa-XBTXOEPTLUOJIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7df9e2073.mp4?token=aTzijaqj3SOf_d0w7LffZQPGYtHfe6ewVp1Pprx_zYYFjMeylNKMRxlwa3fiQaufyR8GUXM15o3V56DV74Nnxy7d9LkJvgpH1G7miFNT-sBER5mhTD8-4fdrznqMTs1ECZJyY19SlnxgZbfogyxTmZd0IehvI-OiNPJEIewhVvT3torO-YsbZHlJ_vP_oLC1CXW3XuaC9Mqb-y1J2IH0liX53Fkierz2sJ4DQKl_pUGrZjfhxFXITPSZ_WPvlWJsKpHaC0zyEKHwgySGAi51qzcx4RNhoY44EmOLUjd62GBC9DsZp2YOf2JWTUZAY9QILXyByVa-XBTXOEPTLUOJIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سازمان نظام وظیفه از متولدین ۱۳۵۵ تا ۱۳۸۷ خواسته تا خودشون رو معرفی کنن !</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/5002" target="_blank">📅 18:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5001">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=pJSSziJQBOZnNQbwT4OXWI9PpjTcJIuGjjEymGpT-eyFCFLRXl8ADjaBq4h7REY19B25i05OtQ5sW18UIDzfvziilSjtnwjwvHwgFSeN5X4TUOmvc8gopTKWaUAosUSDYKlXlMo0WnRNMCludkgTrCQ-5Tosc9f5_TCK1hfcRBkaz7FHGKv-JpmlvA6JNs3ZXlu3ZxdOOzD07QAfqhtDH_VzZTifGdyNWk1isLFYkRwqCYts3XTKIK9373efb2C9WxrLAjT1ogczqzxilIE8J5e7nPXHo8jBrOYInrwbv5xsCYS-mlI1_ZD4uQ2JsO2nUUeOhF_EfuBjJ-Px7aoZsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d3b03183.mp4?token=pJSSziJQBOZnNQbwT4OXWI9PpjTcJIuGjjEymGpT-eyFCFLRXl8ADjaBq4h7REY19B25i05OtQ5sW18UIDzfvziilSjtnwjwvHwgFSeN5X4TUOmvc8gopTKWaUAosUSDYKlXlMo0WnRNMCludkgTrCQ-5Tosc9f5_TCK1hfcRBkaz7FHGKv-JpmlvA6JNs3ZXlu3ZxdOOzD07QAfqhtDH_VzZTifGdyNWk1isLFYkRwqCYts3XTKIK9373efb2C9WxrLAjT1ogczqzxilIE8J5e7nPXHo8jBrOYInrwbv5xsCYS-mlI1_ZD4uQ2JsO2nUUeOhF_EfuBjJ-Px7aoZsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.
و نتونستن چیزی پیدا کنیم …..
این همون حادثه‌ای است که میگن
مجتبی فقط کمی زخمی شده
این همون حادثه‌ای که توی
صدا و سیما گفتن همسر خامنه‌ای (مادر مجتبی) هم کشته شده
، بعد از ۱۰ روز  گفتن نه! زنده است!
یعنی وقتی داستان زنده موندن مجتبی رو پررنگ کردن، داستان مادرش رو هم تغییر دادن!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/farahmand_alipour/5001" target="_blank">📅 15:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-5000">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOk6yVnCyKJ-lKQ261QYzONTKnuJNHfdaDIW54dEYAfrrk5DGKYL1V2eLjEHp-WSuqNz8o2YMHSuTrzXo0Ro9R49Wphi6RR_n1XBHDJbvo27zyiwFoe3HyF7_HhS6apBlOEzj3Aar42eCLUDutuVCcrYs36rv6JOMfwqMXOodpu1E0yiOkWTzx7H5Kjd9imEykZgNjn6-q3oPdcUpDkzPOOXw1J7rYxYHWoxqy6I6JoVY4e3klYSd6jnHoO0HOay31BvvrxE3UuSKsdR6tWDpq76y0RWVQZ-LRGpRWE0RcSN35R-8KwVCrpyNqtQdTjVp8hNlS0A75K8qcv1p_2atw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/5000" target="_blank">📅 15:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4999">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Q_thJFQ9Twl2s8EUg1dVFRjY3XOWAvuAojf59yz0lBEoFJ73YH1Wt-_lbUDLwtnVSVmAzXcZEDIHk0jRy4cktAvOg5Bf_nF1j8_6AveXvA_cPoIBP1iD-9YzKY6cUQpX1pPsQpZ0e6wkw8A4I2gtvmRrtevBKsXXEX-CmjFg2wjLxPXQRDB4myQfuNfZfJhp3hDOEWtfJUFsORnhBqJwGXMFgkFjR05J5pq2h1kYAlBUbCmIT6NFNOrTHegf_uYu4EU7IbMOLaaayKK1Y2p5GODEb461ltRYf2-2CO_FJelgEHuL3-cTsc7POFjiemDEZcpyEoObPiSDCp1brFTXeBrM7F1fBIS0pszfBmTAJQUGNFklskdK1IAvWjVWYH-G1k7CNZQWyM40dU0d4tNcIglPILy0p0jI4HlZtwK2Jf5aOePeaOZGBpjJ-Sq6tJRUDmrwPNM8sbJOV9-s1s76rGAXD0xWl_oKjc8EdkVxcA6Da69N29hb9IhkhR8vwbtd6L8pgT_vOHejM8GK1sjrJTfsrgbxrGRqKq2n9rSSwTTjIIOcqwyETMMtjc1qKAKzwnZlr69iYYu6e1YROq1AFiKgbZA64tiR7j6d-VjT1mA59L8p2OK8fa9PzgbVBa03GwQ97a59mQculQ4G5XyAatlG_8UanN0ftiQjYY16AOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f56f6e59a.mp4?token=Q_thJFQ9Twl2s8EUg1dVFRjY3XOWAvuAojf59yz0lBEoFJ73YH1Wt-_lbUDLwtnVSVmAzXcZEDIHk0jRy4cktAvOg5Bf_nF1j8_6AveXvA_cPoIBP1iD-9YzKY6cUQpX1pPsQpZ0e6wkw8A4I2gtvmRrtevBKsXXEX-CmjFg2wjLxPXQRDB4myQfuNfZfJhp3hDOEWtfJUFsORnhBqJwGXMFgkFjR05J5pq2h1kYAlBUbCmIT6NFNOrTHegf_uYu4EU7IbMOLaaayKK1Y2p5GODEb461ltRYf2-2CO_FJelgEHuL3-cTsc7POFjiemDEZcpyEoObPiSDCp1brFTXeBrM7F1fBIS0pszfBmTAJQUGNFklskdK1IAvWjVWYH-G1k7CNZQWyM40dU0d4tNcIglPILy0p0jI4HlZtwK2Jf5aOePeaOZGBpjJ-Sq6tJRUDmrwPNM8sbJOV9-s1s76rGAXD0xWl_oKjc8EdkVxcA6Da69N29hb9IhkhR8vwbtd6L8pgT_vOHejM8GK1sjrJTfsrgbxrGRqKq2n9rSSwTTjIIOcqwyETMMtjc1qKAKzwnZlr69iYYu6e1YROq1AFiKgbZA64tiR7j6d-VjT1mA59L8p2OK8fa9PzgbVBa03GwQ97a59mQculQ4G5XyAatlG_8UanN0ftiQjYY16AOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«راس امورشون ۸۰ روزه تعطیله» :)</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/4999" target="_blank">📅 15:46 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4998">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBCgEYRQy_Lvacoih-YU6pG_Y_iYiyuvHYAGIuMMjckV0n5EQQEu_Yr80JaHZhFPPKYMGgUjZBHqIAKtIef1uGdN_w8ihUJ_ojHo3zaDtz-mq1DIdER5aIekWLyKXtbGgvQrkowZiItGmdZnlS5dIfrxfTOkQ4TNnM3c9w7PLogwtYBCB4-6fg8DQV8hoS1ox9maBenN-CgE_zjXiCBwvAVfLpuuFuA983BK_cdPKHiOA5Jlv7JYJjYnz2WsQzvPkFuQuPobRkPmuRf20tiDanEQazAOf_6Ym6z7g4zK0n1aa-pZYUDD-BG3_PVx4Bjnyk_bLOv-5KSonYPpRdYDLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4998" target="_blank">📅 15:10 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4997">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4af299654a.mp4?token=rkZ8BOZSW1P2ceGPFpV2dgYDaRkLee_9tNAxWMAszunkqLLh1B9OxMWVkYJY84VllUFhsnJaW9jXPVP2ivmh1rLUpLZ9cb9i3wgnTO8cp9gXRgRNtYlpv2QD-bFjcVMrhLvYzcdNK0_E4oS5scRDxIOFmgVpiLoJnChaJ7qH1eMmwioL2gbzs-cyDLIzbzET0Jo2tO_ZhbFZmNmE6IcTJXlRxsxq-kGRSEHgiqSiCswvdyERDDZj5C2ED0vqMAfVehfuzI96w2lcEUDrd3gKRoMeuVLfnkkcTP7-88YzTGYGx7y3ER8ju8xZslTO6GSNVu_vyupSu0HX7UskJOdkGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4af299654a.mp4?token=rkZ8BOZSW1P2ceGPFpV2dgYDaRkLee_9tNAxWMAszunkqLLh1B9OxMWVkYJY84VllUFhsnJaW9jXPVP2ivmh1rLUpLZ9cb9i3wgnTO8cp9gXRgRNtYlpv2QD-bFjcVMrhLvYzcdNK0_E4oS5scRDxIOFmgVpiLoJnChaJ7qH1eMmwioL2gbzs-cyDLIzbzET0Jo2tO_ZhbFZmNmE6IcTJXlRxsxq-kGRSEHgiqSiCswvdyERDDZj5C2ED0vqMAfVehfuzI96w2lcEUDrd3gKRoMeuVLfnkkcTP7-88YzTGYGx7y3ER8ju8xZslTO6GSNVu_vyupSu0HX7UskJOdkGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مجری تلویزیون جمهوری اسلامی:
- بگذار پرچم امارات رو نشانه بگیرم
- احسنت</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/4997" target="_blank">📅 15:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4996">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RfaHA_wPAIoru64Z8cHKkugFJz-uv60SUOf23Z6g4WElObZ1EWwg-W5kMYlRkhHCxYXdwzrLS41DAhUKrcCVgeclNIGWTnFSYCGJid2-vtuNJr9Y9dWPivC5_oV0_iIwDjEadosBng8fcJFWP4hvvgBdhnQ-CwVJBVxhytBuEg42qKM99ieH0AbGsW3xYE_WA2mwYQ3tg_ouZWjBEsJxUaB4yCIX3slobbg29p6Qb3PML65nc_UHZhIl-eFejxJrVnuNjSNG5NruH9PpW_yn6bmPX1KWJxRa9e-QodO0JKhagF4ifovnLJotbkllzMuOMaN-R_OjhtOA5dvTUDIlRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمانده کل نیروهای قسام در غزه دیشب به دست اسرائیل کشته شد.
قسام در واقع نام نیروهای نظامی حکومت حماسه.
مثل تفاوت نام حکومت «جمهوری اسلامی» و نیروهای نظامی اش (سپاه پاسداران)
البته ج‌ا ، متفاوت از همه کشورهای جهان، دو نیروی نظامی داره: سپاه و ارتش.</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/4996" target="_blank">📅 14:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4995">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZK3LthxXKjc8McKTUR6_XuVY97RQyxvUjI5sT0ASfD9PZA5wZTK0EyriuPytzXZjdd8YKnbOYOhgMRMr2fzrupjWurPoDpRI-g7ysp15HgOIPVoUPfmTVEbY2ECKzbtahzn3AXF45TtbPMSlV2hNTZUDHNkpcicqzx4e9NHduf4AK0gQ9WWfjLUGH7Q6w8Kf6AD0XwS8Wzu38V0aZhrImMNl-4GCODosCQ040BzvJqHDoy-er2npHq2o8XPWAH9lpkV0dBo9A3olWoer1kROuOBi-fKlz8FHG1hdvM7U_KpgrlCpByuoc78dM0YYNkfQEpbD4HLKg4H8jZAQyS7sRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینهم جنگ بعدی‌شون در ۷ اکتبر که توی تهران و قم و مشهد هم شیرینی دادن و اینهم از ۶۰٪ خاک غزه که از دست دادن!   دیگه توی آمریکا هرگز دولتی سر کار نخواهد اومد که بره به اسرائیل فشار بیاره بیا و به گروه تروریستی اسلامگرای حماس خاک بده کشور اسلامی شعبه جمهوری…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/4995" target="_blank">📅 12:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4994">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptqOZrt6_PJG50j2AJyrLTPh1Ngog38XLsI3dDgm6bvVRvph7RbismJo78cO7_Y-b3b3pcFYwFt4ejsjMHaDGnLHEnRETh_2Gf7vMWrPKiTyZ1YpV00JrSMY9sQhZ0uqdg6nRm2uN7yle21UNKRgUZsTBy69JUdW8CFSddlG0mxmbbe_wB3RJHimNnVuJIo4RFfsGFQd8Sn7r3tCmS_IjMUHxZtiR96CWFxehAgOy4H4hgiDi6fZFRiEkfjtm2WBHKF7YHil6Gy8sCkE0jm-f7YP7XACZxC2UTlEOv5asgaB__BPCVOFraLHpmrMfIhYBDTZDA0L_93QOUAn7zLLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا سال ۲۰۰۰ از توان خودش استفاده کرد، به دولت اسرائیل فشار آورد، به شما کمک کرد گفت ۹۶٪ خاک اشغال شده شما رو از اشغال اسرائیل خارج میکنم (در کرانه غربی)  غزه رو هم که خود اسرائیل رها کرده!  بیایید و کشورتون رو ایجاد کنید.   عرفات گفت نه! ۱۰۰٪ ! کرانه باختری!…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/4994" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4993">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGtDd9_rZsEW-Y3sR5EsG5K_7qcfq1KNL5x7XO7xSoWy3yhubLzzp4oq4ehXl8LUs6B7qfyD5f5CSi8BdknN7bCgP2v7NJP0qXHf1c4HvTdDvgUQzHRiijK4VnkrwLgfSWcNzLMkNuKeE_G5OdpTdn7lKVozT1eSOo3im-6i3ObWXJ6CGKPC4msYEbq8S9DjcFEeNaZwvuYm3L6ADr2kGTijfm0Vl-cXCwWBWX1-bKlxIgBtcU8vfaQXe3oVzUKNHRuof6n0gX-_GMVwSz1B4zlDzXS97lDW26migLhT5A76gcFdCB8fdZmSmatJ0Bw6zaNsFiW7kf6oy6VEKY-smw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در عرض ۶ روز ، مساحت اسرائیل ۳ برابر شد و غزه و کرانه باختری اشغال شدند!  ولی اشغال نبودن!  برای ۲۰ سال هیچ وقت دست اسرائیل نبودن!  دست مصر و اردن بودن!  دست عربها بودن!  گفتن بیشتر میخوایم! نه بیشتر بلکه «همه» رو میخوایم! باختید! شکست خوردید!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/4993" target="_blank">📅 11:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4992">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVkWuKMEohGymPNo-W28A1wQ8L9ugXbM3zkF4kkEP3gn6kG1DK00b085bGw1qbhmKGrKN7_ncDrT297t3Dc81eOvc2ljitFRNZHN95bGDU3vWBl2FRHZVg0pFWw46POfIcY02RQq-J3TUsRIh1LIULlQ6MH2ttrmaGhP4g68rwFCU8XoMcBICep4FYOcXxprVvCG_QwfymNIUpwNbJaf6gn6oxrvsUQ64Gu0_LZk4xweo40n_XYJdTYdiHyNKdh8yi5YKdGIS1h1MWv1FFAs5JJiSBhY1s2k9NNZsdjQI4f2C8fXYvFJ1CnAcE0G7s64ES2j-XVK39B24FnLFrBzew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد برای ۲۰ سال!! از ۱۹۴۷ تا ۱۹۶۷ نقشه فلسطین و اسرائیل این بود! تمام این‌سرزمین ها دست مصر (غزه) و اردن (کرانه باختری) بود.  توی این ۲۰ سال می‌تونستن کشور فلسطینی رو تاسیس کنن! اما این کار رو نکردن!  چون «همه سرزمین‌ها» رو میخواستن!  اینکه دوباره حمله کردن…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/4992" target="_blank">📅 11:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4991">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ecKp5X7jVip5CzLcnNNdmw4_qCueX3VlqENXcZyRMvUV8Tm2i2JN8R8p0LODARY067rprYemSRhfiKJtjrniZjy_Is3_zVvzXzpL1fWGwp-uRljZd_FSKsbakXLJsnB1OAIjyam_2yKfj3owfBcuGO590TwXjaT_LdQ6vQy_wblBWaP2oveDDxA-AuO-7mgaF3BHVRU0wIH3-ddZlcKa81cmJHgjRqx1y-cGjwYTyr7NlDt4r9upELB6_l9r-0Djx9P51J5qBuFT27wZZtS5MfS5nD8xYh-8Rx1qrB8m3mEbaWI8OVmIxHk6U4979Ps_cKyv6aP4nobdyht5zi8ZCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی سازمان ملل، طرح تقسیم فلسطین رو ارائه کرد (فلسطین یک واژه و نام یونانی است برای این سرزمین و هیچ ربطی به عرب بودن و مسلمان بودن نداره!)  اسرائیل هیچ سهمی از «بیت‌المقدس / اورشلیم» نداشت!  در سرزمین‌هایی که اختصاص یافته بود به اسرائیل حدود نیمی از جمعیتش…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/4991" target="_blank">📅 11:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4990">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHQkloWiVZngrsyquSbjjRYQgR31CL7YWWBsTx2OpweQVjPUCZkHYbPw01u4z1vMphAsuoAomga0_96oZ37Ik8XL3aes1NAebsklXZ7UsSFXno_IePp9L9LQaIcpW0yhGsLrg1QBMx1TPJnwvlmO3Lor7I6xLS1LXZZZLs7ZOejR5HcGM2yIkYHJKoPjsJMp4x0ykXyYHx5vkEOG-KQicfAJKHv4mMzQwHrQq5GoBuz9ylIqlPqJCucdIYNMzD2cIlw_8Qo4c0m-pID8vZ4xHaqDZaPxZ0oPtbrJKzf66UIouOQ8_JKn5UFEUCdFNou1v3kyjIumYGwtOEej7JU27w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیل کلینتون :  به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.  اما قبول نکردند و طرح رو رد کردند.  حماس به دنبال ایجاد یک کشور…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/4990" target="_blank">📅 11:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4989">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=qfUVr2sHFQVgpYFcuYjWmdEKpcwL3SR1fp7dTWMaeTJ9uxVUcQaDd3_WU-TY2xLi7vtzM-tFBqu9V4lOtVVSRj27emMT3LpEhW-udmnpsryWqNLvM88eu_aezojuDzp9yN2khfpsGTuSZJHsCy_qkgsSRV9pOYw7EPaZTagN3rk8Wh2xwxl3OX22xRDAmEZK0Wn8gIZIqxPRXCYY5FwzkVBaIEGlvQUztDvKUVncPyPJUed-Pc59KH-Z9jNAe74fZ85BGgsO3fqCZKmEh1KSt_xolWvtsqSye5TKjt0470Ih00wZnm5RzLsdXcScsPgfJWbKl2m1TLnD8SuivZV4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/997bda43ac.mp4?token=qfUVr2sHFQVgpYFcuYjWmdEKpcwL3SR1fp7dTWMaeTJ9uxVUcQaDd3_WU-TY2xLi7vtzM-tFBqu9V4lOtVVSRj27emMT3LpEhW-udmnpsryWqNLvM88eu_aezojuDzp9yN2khfpsGTuSZJHsCy_qkgsSRV9pOYw7EPaZTagN3rk8Wh2xwxl3OX22xRDAmEZK0Wn8gIZIqxPRXCYY5FwzkVBaIEGlvQUztDvKUVncPyPJUed-Pc59KH-Z9jNAe74fZ85BGgsO3fqCZKmEh1KSt_xolWvtsqSye5TKjt0470Ih00wZnm5RzLsdXcScsPgfJWbKl2m1TLnD8SuivZV4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیل کلینتون :
به فلسطینی‌ها پیشنهاد داده شد که ۹۶ درصد از خاک کرانه باختری [به اضافه نوار غزه] مال اونها باشه تا بتونن کشور خودشون رو برپا کنن و به جای اون ۴٪ از خاک اسرائیل بهشون داده بشه.
اما قبول نکردند و طرح رو رد کردند.
حماس به دنبال ایجاد یک کشور و یک میهن برای فلسطینی‌ها‌ نیست. فقط به دنبال کشتار اسرائیلی‌هاست.
🔺
بعد از عملیات ۷ اکتبر ۲۰۲۳ ، اسرائیل ۶۰٪ از خاک غزه را نیز تحت کنترل خود درآورد.
در تاریخ ۷۰_۸۰ ساله اخیر، هر بار جنگی راه انداختن تا با جنگ، سرزمین بیشتری بگیرند، بیشتر باختند.
🔺
امروزه در دنیا، نه آمریکا و نه کشورهای عرب، هیچ کس هیچ فشاری به اسرائیل نمیاره و دیگه سرزمینی به فلسطینی‌ها تعارف نمیزنن! هر بار بهشون تعارف زدن گفتن کمه، جنگ کردن، بیشتر واگذار کردن!</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/4989" target="_blank">📅 11:44 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4988">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dP1agC6EAQvYQ8t86xmIQVtinS_xQ8N3vjhp53FrCFEvh3qY24rM9DnAnX3FISF53QFA6aG_5aKIrlizSmook0bkmoCXHlgMvMe_-ao9gPdHXz6COLrqvF1VYIILxwsOhAL_EOUFFgcHTGIytej2qfLZWcqTHPyq2wFKzSve_LSVfBGkxK1KHpkNFJE9E1ETqWvR6qlYRLZJ8matKTOWWb6AF2LUkz0W4UK_z10ZjUpt33pUtR3qWgnd7-nA0wFwq-gMgdNvOofOFXfU78vJFAoaag5iquNspRt8I53EqNh-eafSMntkK-53EmAXTR53-VKZ8mhCmSsmfyd8VaccgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/farahmand_alipour/4988" target="_blank">📅 11:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4987">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHz6cnM7zuQpkbv3V9uTKkdBXXPcUjqp8iskE06ni-R4MzUwWgZr6_mkApQKkyO54PBuyPpf24ILAeWOGmhkqwM2K4gk43u2XZ51cUi8H7i6byWZUXRXack7bw5GYVgtgB80_QtOI8zCkilysbs4DCMwfuGMCfRrDVt-lY1wvJnKT4zV9ClHfrqPY5ekvx_qc-UIyhjAmgrOMM26bdcs0Ik6ijN6pkO2rebBZbaGCVwSfWAkK1X1bQMFdgMFqSwOylUd_91F6OcULjp4-yVEVT62gmGzM2vYJiGE5NcpoUJQbah5jtLqjGbFgBEWx8fD_uJO1jqYT8SKp3uOGBMmDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افتخارات صبح‌گاهی‌شون!</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/4987" target="_blank">📅 10:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4986">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cECXMRLkgMJNZIZfrZneC87SEYhkd2DTiMQz5xoBjub3g-DniZtlH7IgDGw06TWai8omeC-DgY35JXhRUbCRBcyw9RWNRy2z-zQu8LmDfn3rfRM6DcSWbZGJ9hG18Y8ncr9XB0d9Yogrkyczsgy-6QUL-Z9nh-cBs7dFPmS5iru2bsM4w17KuhBuCC4NL8-DZWvaaL8pLhM9RX_ivG7sbkPhZK4caA9J2XHHP199ysR2upJdAJ7rXMnRUgSnhCTUAsUW6YvZQBL61bJurS1X4-C-qlBW8shLrQlGXmWKxrweVBNw2Q6l55JmltfBuF-5cyPXBYBNxZk2aH8QTF_51g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/725acd2c9f.mp4?token=cECXMRLkgMJNZIZfrZneC87SEYhkd2DTiMQz5xoBjub3g-DniZtlH7IgDGw06TWai8omeC-DgY35JXhRUbCRBcyw9RWNRy2z-zQu8LmDfn3rfRM6DcSWbZGJ9hG18Y8ncr9XB0d9Yogrkyczsgy-6QUL-Z9nh-cBs7dFPmS5iru2bsM4w17KuhBuCC4NL8-DZWvaaL8pLhM9RX_ivG7sbkPhZK4caA9J2XHHP199ysR2upJdAJ7rXMnRUgSnhCTUAsUW6YvZQBL61bJurS1X4-C-qlBW8shLrQlGXmWKxrweVBNw2Q6l55JmltfBuF-5cyPXBYBNxZk2aH8QTF_51g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین یکتا، همون چهره‌ای است که قبل از شروع کشتار ۱۸ دیماه اومد تلویزیون و گفت خون هر کس ریخته بشه پای خودشه و بعدا گلایه نکنید!…
این همونیه که اومد حامیان رژیم رو دعوت کرد که هر شب برید توی خیابون‌ها
حالا هم در کنار تیم ملی فوتبال، در یک اجتماعی اینگونه رسوا، داره مجری‌گری میکنه و میدان ‌داری.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4986" target="_blank">📅 09:26 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4985">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمملکته</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=vLjFNWs6WJNbRyje-FylQ4BKv-CtkPEemWgaNWmSRJt9ROtBtQy0oiTx6KTZU8vwHEmvpS7budoO7mOTmTGH40KxKqPWigVutSLRfcw2OuTkpVhASeqQdMBMXKtDZUD0wSTu_yDLr6-z7aetq2STqRdvyC0qh7eJkqyYoXoWV6r-bKfQfYB443MuvAJDkScHAd4_NSKwC-oLZpCTnS9o9zRr-fL0MeK-lwZLT8_83ofPvVH9KsZP3RnSi6KfHhM51euR0lG2lD3A78sKoRM1LckQkqzBj-X5nEbxvh2Ah5L47JAw104q6bXXBmOGNbdByPmXhVyDkfVB8l1RTx8tdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f69e049f42.mp4?token=vLjFNWs6WJNbRyje-FylQ4BKv-CtkPEemWgaNWmSRJt9ROtBtQy0oiTx6KTZU8vwHEmvpS7budoO7mOTmTGH40KxKqPWigVutSLRfcw2OuTkpVhASeqQdMBMXKtDZUD0wSTu_yDLr6-z7aetq2STqRdvyC0qh7eJkqyYoXoWV6r-bKfQfYB443MuvAJDkScHAd4_NSKwC-oLZpCTnS9o9zRr-fL0MeK-lwZLT8_83ofPvVH9KsZP3RnSi6KfHhM51euR0lG2lD3A78sKoRM1LckQkqzBj-X5nEbxvh2Ah5L47JAw104q6bXXBmOGNbdByPmXhVyDkfVB8l1RTx8tdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📺
جمهوری اسلامی به جایی رسیده که نفر آورده با ماسک آموزش کلاشینکف تو برنامه زنده صداوسیما میده
📝
توان جنگیدن با آمریکا که ندارن (در صورت جنگ زمینی)، این برای کشتار مردم بی‌سلاح ایران در اعتراضات آینده ست.
📝
اسلحه بیاد بین مردم، فرصت انتقام تعدادی از ده‌ها هزار نفری که توی دی‌ماه کشتند هم بوجود میاد اما ابعاد این احتمال بزرگ نیست. ابعاد احتمالی مسلح شدن، اختلافات بین باندهای مختلف مافیای اشغالگره که با تنگ‌تر شدن محاصره اقتصادی، از خشونت سیاسی به خشونت فیزیکی دست خواهند زد. برای پول راحت‌تره آدمکشی تا برای عقیده.
@mamlekate</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/4985" target="_blank">📅 09:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4983">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoYpjvMjvBwvYor_7z5qEwJ16YgfxZS-Jh_qH-FGHWgXK1vIb5HZjoNJ6ktsZBXlkxXgKM5hAsElQz-e18yjzwCA4EpTUhJntWCRD_6cMsNM09JttTeFBse0PSt70ujQDC1FyC2E4MUFdeCxFUlU76J7G-JrhKPzbIfoFWhOCf36QLabmQwr60qqBLEpBwKnMCgj05WCJ3sIRpq4zb9BxCE33duoXYaozjXep-F0cl7MokKjcqm7zKpG7xfE4QrNrfRzlXtswIihCLfQ0gMOYBD-0rs9Pu695Gbn-qiLHtOwiYKX-QlUray-mv3AaQYof6c87rnr0ZwhD6uAEDuXpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=YN3mKfZ2joC2mWAMWeiz7lwfqv8cVznGGAWENzDk_gOdQGuhYQOT68zE7aZfH9YBDcSH8ohbEpfSTBSuZXK4jGZGcXh33HJiK0rctGnbStnNzEhcJTrUmIPSqyJHirk3Na63JYuomaF1m5Wryzt0qvaSPd9mB-WvBK7jk2GDJVAmXgIbhU6lPzjrvviZwxN_II1poYTFPeU-6QQiqrIN0UIgqD05oLVWYXjYIq9IyFrx9WcQgcpBSwfhtkfeaJFH9Ni0nlw1CMuPMO4RzTvbefcYWtzlOxb-F69Tl9EQ-fLMAADZZ8bmMx9qoAO2CcdfX1i2Kyc3KxZNqg7mgKHHGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0eb0451b.mp4?token=YN3mKfZ2joC2mWAMWeiz7lwfqv8cVznGGAWENzDk_gOdQGuhYQOT68zE7aZfH9YBDcSH8ohbEpfSTBSuZXK4jGZGcXh33HJiK0rctGnbStnNzEhcJTrUmIPSqyJHirk3Na63JYuomaF1m5Wryzt0qvaSPd9mB-WvBK7jk2GDJVAmXgIbhU6lPzjrvviZwxN_II1poYTFPeU-6QQiqrIN0UIgqD05oLVWYXjYIq9IyFrx9WcQgcpBSwfhtkfeaJFH9Ni0nlw1CMuPMO4RzTvbefcYWtzlOxb-F69Tl9EQ-fLMAADZZ8bmMx9qoAO2CcdfX1i2Kyc3KxZNqg7mgKHHGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پسر سرلشگر موسوی رییس ستاد کل  نیروهای مسلح جمهوری اسلامی می‌گوید که جنازه پدرش ۳۰ روز زیر آوار بوده.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/4983" target="_blank">📅 09:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4982">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏ترامپ: امشب، به دستور من، نیروهای شجاع آمریکایی و نیروهای مسلح نیجریه، مأموریتی بسیار پیچیده و با برنامه‌ریزی دقیق را برای از بین بردن فعال‌ترین تروریست جهان از میدان نبرد، بی‌نقص اجرا کردند.
ابو بلال المینوکی، نفر دوم فرماندهی داعش در سطح جهانی، فکر می‌کرد که می‌تواند در آفریقا پنهان شود،
اما نمی‌دانست که ما منابعی داریم که ما را در جریان کارهای او قرار می‌دهند. او دیگر مردم آفریقا را ترور نخواهد کرد یا به برنامه‌ریزی عملیات برای هدف قرار دادن آمریکایی‌ها کمک نخواهد کرد. با حذف او، عملیات جهانی داعش به میزان زیادی کاهش یافته است.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4982" target="_blank">📅 09:08 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4981">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=sP10t5iaXXN7EMGx9JjHfUa6eqGT0Ec1WPRTRX9SKugcZ5Hqq7jO_44nYl3pPq-EDD-uDJox4iLdet_ntKETxNM9IKigrdA8imvOVMX-ns0gB0m05742y1EXHDRsFTVB9uFjizMoKMb_xWJNKNqDstwrbQqntv-Cnim7-7GUtZnEDjohZufCX9hvTPmfsu8EqNxVGmimpd4TOAXlsjfqXB3vV4DUvC_4cd12ONvI6F8RdV3AFYiLCmaShR5qaQ5VB8irNj5xDS22BCCXQtGY1gwnMJyKDOCz6NrOgfCLBBPcmhjypxebvOW0VJt-pGNhJeJdsnfCMdZy9IcFIevpgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/022ea313e7.mp4?token=sP10t5iaXXN7EMGx9JjHfUa6eqGT0Ec1WPRTRX9SKugcZ5Hqq7jO_44nYl3pPq-EDD-uDJox4iLdet_ntKETxNM9IKigrdA8imvOVMX-ns0gB0m05742y1EXHDRsFTVB9uFjizMoKMb_xWJNKNqDstwrbQqntv-Cnim7-7GUtZnEDjohZufCX9hvTPmfsu8EqNxVGmimpd4TOAXlsjfqXB3vV4DUvC_4cd12ONvI6F8RdV3AFYiLCmaShR5qaQ5VB8irNj5xDS22BCCXQtGY1gwnMJyKDOCz6NrOgfCLBBPcmhjypxebvOW0VJt-pGNhJeJdsnfCMdZy9IcFIevpgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینها نشانه سقوطه. نشانه هراس.
پروپاگاندای پوشالی رژیم رو باور نکنید که میگن بعد از جنگ قوی‌تر شدیم!
اینها ۷۰ روزه رهبری دارند که خودشون هم تردید دارند که واقعا داشته باشن.
اینکه ۷۷ شبه، هر شب هراسیده در خیابان جمع میشن. اینکه ۷۷ روزه اینترنت رو قطع کردن و علنی هم میگن چون ترسیدیم و …
ترس اصلی‌شون هم مردم ایرانه!
و اینکه خون اون چند ده‌هزار ایرانی که ظرف دو شب کشتن ، حکومت ظالمشون رو غرق کنه.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/farahmand_alipour/4981" target="_blank">📅 08:58 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4980">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OptsqDEuvyGVnFCgChF7KbOVPBzImpFdbpS2myD2wC1Sf9aTwpofDcduh8RfeLToaMcUw60fORtTyWXgL9UgJkniTGkoOE4HAI1Xpk5EE70JrFRDcwnDHar0v4FsXqDKqkh5-gFVBHqLwv6fETOREZQrKtWeIawNEdeQfgv2MUAQUA4jfAzd25YKjUallo8kVjZiot7xwL4OjNscadJtXkj7dnu9SwtXB0CxC8a3kI0pxLh_SOswkQ0UIR5cLf31UZEHEOwUcftcLiaWGmXdt-HsGUGBJSi6n9XL13BhDkmKViG-RYboKu1xh_et8lRVSqE1A5kIyNtyv0wXJcphKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در گفت‌وگو با فاکس‌نیوز با اشاره به افزایش هزینه‌های اقتصادی ناشی از تقابل با جمهوری اسلامی، از آمریکایی‌ها خواست این فشار کوتاه‌مدت را تحمل کنند و گفت جلوگیری از تهدید حکومت ایران اولویتی بالاتر از پیامدهای کوتاه‌مدت اقتصادی دارد.
او 'گفت: «متاسفم که این فشار را تحمل می‌کنید، اما باید جلوی این گروه بسیار دیوانه را بگیریم.»
رییس‌جمهوری آمریکا گفت شی جین‌پینگ، رییس‌جمهوری چین، برای کمک به حل بحران ایران و بازگشایی تنگه هرمز اعلام آمادگی کرده، اما تاکید کرد واشینگتن «به کمک نیاز ندارد.»
ترامپ گفت چین «۴۰ درصد نفت خود» را از منطقه تنگه هرمز دریافت می‌کند و افزود: «اگر او بخواهد کمک کند، عالی است. اما ما به کمک نیاز نداریم. مشکل کمک این است که وقتی کسی به شما کمک می‌کند، همیشه در مقابل چیزی می‌خواهد.»</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/farahmand_alipour/4980" target="_blank">📅 08:36 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4979">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QV7BYjWh5YT4uoLfvL7mfvCZJ5NejJwL0UVTYscEoBBp-uW6b_hd6CrR5UFn6zzI2ICNdblj7oEqTxf-3sexjI36FQXKXX4LxUJ8bGxpHz5VST4CC_5nVJGplODAGof9rFBfO13RIp8Bl_7knjxqDAbfc_wR_dKmxcn4WtnP2T9Ty2LMwIpaNwr9MYEHCnKocwTJplJrDKj1CtaJj7wlgzVBB50I1nYLsJAqLCZyqpAfzMtVqisduofia5guY7LVdHXqQJasYB2z7hNqy2wsTf3WTECvp8eVkI7vJk0nX64q-1lqMM6OZlN7Y8Qx6MHnp5lH_3S03xGUc7Ddqs8duA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میگن رهبر شجاع‌شون  ۷۰ روزه قایم شده
یک عکس بیرون نمیده!
یک فیلم ازش منتشر نمیشه
یک فایل صوتی ازش منتشر نمیشه
پیامی که میده حتی امضا هم نداره!
از طریق امضا می‌تونن جاشو پیدا کنن؟
یا موضوع چیز دیگه است؟</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4979" target="_blank">📅 19:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4978">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDI0Veqa24MGvyn20EW9w4B11y_ewM4LDlS42bi6hhwKFOuJihsUzhLQdD6AcBLcGdeVvdXEqfYgGs02QJkwYkjShmlXRAfmMY234gncWYBXApztlCHBHd9-uJuHa2QKZBBPPzyoa4jh7gtEXXT4eWIK8wyM1Kes5eOWZxi01VdXLqSOtpcS3UXoV4GeyK_MQZPzcHPl0sW5H6HiCEZ9Pwb6GdpnGOz66I0JTexWoPkUKnRQyD5lVHBfr31X--ywH_yXdErZsiNLcNeOjHY3y-npTnaXBv3QcAvWGZ6ZzlGtFk0MvbdM6SpXzikIoHuKDimBDZ9DSPDP8Ip8-VoHlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4978" target="_blank">📅 18:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4977">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMMHypQ4e9-z4iXNeALeIqUznF54zfV_mThV8y3cbcnDFHlu2HHh6QDeVHOwMGw8i85zbLHat5Bwtd8Oy8J472Dmx0O2zJHEvxz4oLBhehEX-DQFNLALAz_Orj9N9Epu5fxhaW4tQ1kXvO9aIZgnW0r1JqhkxWxsJN0FcvURoK959VgRAi71KuIidMTn9aHbNUw869zWN44Slg3j3DOk1hgs7f4sG5Js0j5hA1uQ8Twl6TFedBOwk0wGoPeFthCv6eEWxNtQ26JDquVkdB0u7ar5m7VGlL_SS_9TdNcZnpBtQBHnUMp2d6YN9bl7CpoWBMhTU3SD5DNzhJCnLpNMBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیئت آمریکایی تمام هدایایی که چینی‌ها بهشون داده بودن، قبل از سوار شدن، در سطل آشغال ریختن،
نگران از اینکه مواردی در این هدایا باشه که برای جاسوسی استفاده بشه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4977" target="_blank">📅 16:54 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4976">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🚨
برد کوپر، فرمانده سنتکام، گزارش‌ها مبنی بر اینکه جمهوری اسلامی هنوز ۷۰ تا ۷۵ درصد از ذخایر موشکی و پرتابگرهای پیش از جنگ را حفظ کرده است «نادرست» خواند. او در جلسه کمیته نیروهای مسلح سنای آمریکا گفت ارزیابی‌های منتشرشده درباره توان موشکی جمهوری اسلامی با واقعیت مطابقت ندارد، اما از ارائه جزئیات اطلاعاتی خودداری کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4976" target="_blank">📅 16:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4975">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=lqG2F6-x69vTcAvPDcW6NokT6AQmp4ckz5DCLcgnDSG-QNdNGu-Mu0v3F0dsE4QdX7YFsuTWHcoN1XdU_iFjc_3KSxc4zp39FuQ6HXoCylhz5Lcx9uqhUOu9IWj8xYrF0rrqQUmilCbT7WStwRKnrOG3ep0YDlggqoVs-QEmgPmfbUtg0giBrvTjTd8bGU_DVwKyxhAUt6tzMuK8s2md0JnK0Rz51RhJA2pA2gsp_x3ucq4gd-U6Ejct3nTo9CvzsU0eXg3ud2sKvSH688qJ8TvZJ5I38htNgFrK_tOrBQ2BS5R8yeZu4XsQWRH-1SmHESe17-CbWSJCIj6Symkgtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e75a34a18a.mp4?token=lqG2F6-x69vTcAvPDcW6NokT6AQmp4ckz5DCLcgnDSG-QNdNGu-Mu0v3F0dsE4QdX7YFsuTWHcoN1XdU_iFjc_3KSxc4zp39FuQ6HXoCylhz5Lcx9uqhUOu9IWj8xYrF0rrqQUmilCbT7WStwRKnrOG3ep0YDlggqoVs-QEmgPmfbUtg0giBrvTjTd8bGU_DVwKyxhAUt6tzMuK8s2md0JnK0Rz51RhJA2pA2gsp_x3ucq4gd-U6Ejct3nTo9CvzsU0eXg3ud2sKvSH688qJ8TvZJ5I38htNgFrK_tOrBQ2BS5R8yeZu4XsQWRH-1SmHESe17-CbWSJCIj6Symkgtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار : می‌دونم سؤال‌های زیادی در خصوص سفر چین وجود داره ولی بگذار اول در خصوص پیشنهاد جمهوری اسلامی بپرسیم ، آیا شما طرحشون رو رد کردید؟
ترامپ : من طرحشون رو نگاه کردم از سطر اولش خوشم نیومد دیگه انداختمش دور!
خبرنگار : توقف ۲۰ ساله غنی‌سازی برای شما کافی نیست؟
ترامپ : آره توقف غنی سازی ۲۰ ساله خوبه، اما در تضمین این توقف تردید هست باید ۲۰ سال واقعی باشه نه ظاهری</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4975" target="_blank">📅 15:57 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4974">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🚨
ترامپ در خصوص ایران: ‏«ممکن است مجبور شویم کمی کار پاکسازی انجام دهیم، چون یک آتش‌بس حدوداً یک‌ماهه داشتیم.
‏ما در حقیقت آتش‌بس را به درخواست کشورهای دیگر انجام دادیم.
‏من خودم چندان موافق آن نبودم، اما این کار را به عنوان لطفی به پاکستان انجام دادیم، آدم‌های فوق‌العاده‌ای هستند، فیلد مارشال و نخست‌وزیر.»</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4974" target="_blank">📅 15:43 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4973">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اسکات بسنت، وزیر خزانه‌داری آمریکا دیروز گفت که : «در جزیره خارک در سه روز گذشته هیچ بارگیری نفتی انجام نشده است. معتقدیم مخازن ذخیره کاملاً پر شده و هیچ کشتی‌ای وارد یا خارج نمی‌شود.»
او افزود که این وضعیت باعث تعطیلی قریب‌الوقوع تولید نفت خواهد شد.
با این‌ وجود امروز خبری منتشر شد، مبنی بر اینکه  یک تانکر بالاخره بارگیری کرده و اعلام شده که «برای اولین بار» در طول یک هفته اخیر بوده.
جمهوری اسلامی بخشی از نفت اضافه خود را در تانکرها و نفتکش‌های کهنه و‌قدیمی ذخیره می‌کند تا جریان‌ تولید، نفت متوقف نشود.
با این‌ وجود و در صورت صحت این دو خبر (عدم بارگیری در سه روز اخیر، فقط یک بارگیری در یک هفته اخیر) این به معنای مشکل جمهوری اسلامی در صادرات و یا ذخیره نفت است که می‌تواند به توان استخراج و تولید نفت ضربه بزند.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4973" target="_blank">📅 10:00 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4972">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🔺
رسانه‌های اسرائیلی : ترامپ در بازگشت از سفر چین، در خصوص از سرگیری دوباره جنگ با ایران تصمیم خواهد گرفت.
تحلیل شخصی‌‌‌ام: گره میان جمهوری اسلامی و آمریکا و اسرائیل، از زمان روی کار آمدن مجدد ترامپ تا وقوع جنگ ۱۲ روزه با گفتگو باز نشد،
سپس در مذاکرات در حد فاصل جنگ ۱۲ روزه تا وقوع جنگ ۴۰ روزه، این گره‌ باز نشد،
از زمان آتش‌بس تا امروز ، که ۳۷ روز از آتش‌بس میگذرد، از جمله در مذاکرات سطح بالای اسلام آباد باز نشد!
بلکه حتی این گره به واسطه بسته شدن تنگه هرمز، کورتر هم شده و هم به واسطه حمله جمهوری اسلامی به کشورهای عربی منطقه و پاسخ نظامی آنها، وضعیت بدتری پیدا کرده.
از آنجایی که هم جمهوری اسلامی خود را پیروز جنگ ۴۰ روزه می‌داند و این موضوع در مذاکرات اسلام‌آباد هم کاملا واضح بود و عامل اصلی شکست مذاکرات شد، و هم آمریکا خود را پیروز جنگ ۴۰ روزه می‌داند، اما تمام مشکلات هسته‌ای، غنی‌سازی، موشک و… سرجای خود هستند، پیش بینی وقوع جنگ سوم بعید نیست و احتمالا این بار جنگ با حمله به زیرساخت‌های ایران شروع شود.
برخی از کارشناسان جمهوری اسلامی در صدا و سیما حتی پیش بینی وقوع «چند جنگ» در دو سال آینده را مطرح کرده‌اند.</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/4972" target="_blank">📅 09:42 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4970">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XdeRry5iNelidiegNTjVvoa-vI7TiEeZYLJZFlp2uhtuD_dRk_DeRB9K3lL8GHIvME1yPft0QJNG54J-vhKdevUyRU0egDJX2NaR_-s26hibT6ZLq0RebT6J4naYb7fedlTuwWNwYKDVmI2TWQnDy_x5fHsJB1cWAAn3l7IekUROLLA1W41W1o2i7pN3cchAGw91JA5Oczrd7IeLnPou1yY-l0ybCEhA26f70iRpo-LQ6MCGf5StOvjZOnV9jGoDj3IJL9yyyPuXumaMr5br9dA8ZUQlkFJAimDESnoqC2wO9MmsIhQf2I0abYmwQQZmSdd0Gfzp_QnJcME5WNxQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kzL27c0ZJAyH9J09xoQJRA3DAqFNwDIQGYGgyclv5W-SGCDIGQMg9l88CD4hHDT37W0QNcUBOu4hN_K2DBuJZavVj2LcirQcfWbCgrSgmgPLrI7LGZ--037vbQIFlp8NUmwI0HNrcQmVAjJK0gB98_pv3ZE4enNKLPP0I68T6imsThr2a-vo7Wa8kGPTEfcwaveg9PMuL4F_yrhBQMC472J6sywaHt1834zEtGDdvtrRlkSGHobT4HdZ6rDhuD_NrkWGNB4jbjmzZqAW65-J7jhYjDV_sVQnSWKsCxhVwBkfvH-rskEzESmF4vf9CPhwiZ0mCuWbEOb8IoVmweEFFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اسماعیل بقایی توییتی زده
که «هر کس در نهان خیانت کنه، به طور علنی رسوا میشه»
که منظورش اماراته و بحثی که بین عراقچی و نماینده امارات در جلسه «بریکس» رخ داده! و اتفاقا حرفهای عراقچی نشون میده که امارات بوده که اینها رو رسوا کرده و به شدت ناراحت شدن از حرفهای نماینده امارات که چرا در این جلسه چنین حرف‌هایی زده.
اما با زدن یک توییت! اعلام پیروزی میکنن!</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4970" target="_blank">📅 08:38 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4969">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYjwVfVhpGtjbLQq1oSzgLnWtrkOUuOd0WC-tZa9dMRid8TFXmSqHJH56n4Pp2Tai1xJGenWMas8hswazOdr-G2xTCm9gKaF_APIFmEid550Rmk5fHJYpAnzB2UdDRzyURcYCljqtbTYpsKMrSCyl93pyoNL1PDwt10BQpgvRjX1C-kdYgnlvyshcb-wyyoL3e0gvR48E_R26yj-F29f1DJq9K4R2neT9w5_iYFQHm3FkbDOntNTx6v0NTkceCJioy7RUY_d7zMx2QEoj4t12_NOvb_0aFILRv0oJ2UiuWBJexg66T5ZVR4IfHvLLubeaAijvksCc_9FAtMUN802vQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون رئیس جمهور در صدا و سیما:
با علی افشاری، پرستو فروهر، عبدالکریم سروش و….. تماس گرفتم
و از مواضع آنها تشکر کر‌دم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4969" target="_blank">📅 08:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4968">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">نامه رسمی کشورهای عربی به سازمان ملل برای درخواست غرامت از ایران
بحرین، کویت، عربستان سعودی، امارات متحده عربی، قطر و اردن در نامه‌ای مشترک خطاب به سازمان ملل، خواستار پرداخت غرامت از ایران برای خسارت‌هایی شده‌اند که جمهوری اسلامی در طول جنگ به این کشورها وارد کرده.
این درخواست در نامه‌ای که دیروز به آنتونیو گوترش، دبیرکل سازمان ملل متحد ارسال شد، گنجانده شده است. در این نامه، آنها همچنین ادعای «غیرقابل قبول» جمهوری اسلامی درباره قوانین جدید عبور کشتی‌ها از تنگه هرمز را محکوم کردند.
پیشتر نیز در اجلاس اضطراری وزرای خارجه اتحادیه عرب نیز قطعنامه‌ای تصویب شده که رسماً از ایران خواستار غرامت شده بود.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4968" target="_blank">📅 21:05 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4967">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=YckfA9C5sDwFvdK4HrzTpY9umfWX7018W7ItPQj1wZQldFCscppNKDTvUVVxYV7ZjJe_BtlbwFmzgTVn1OjulW-vzGnLwd4WraITt2AtkDFkt8YZLE6psh9aAp0K__cGnFl17HgrzUH-y4dMAgikMqSC_-eXS8udWxzRwdi_yBwTEdY-ZSBpVVZQgHGZHoaJRNQNm880vxixDGnDLe6tit-B6l4AwZfyvZelaPA8jBKB3TW5-32lc6z5GpR770f3On60lDz102O33k-n5a62BChzj35rEh4LfLYmZhIwNvoNVSK-5A3JnSc2vtA2gTNPe3b-apEDM3mhLhBaZL-zCgzOnI8yj9tQvf0Qc3DmQz977crHMrFUsXwSc75cV0ZOikx_JUapWFOxj6SzIlFA2hoJc_rag3ttoWpwuluX2UkJvSlQpaDG_8MH0UQv2faT7z0G56XsplG__UohnmdX6FpUrf7ycOHsC7nQNT-3EN-vntpyVrpv7bAR65lFGHHQrat4FDNRco1TG5xS7Gfzuhf-d8TEHuLWtoeQWu5CkfsVJRBxC9zFXCPH5f398ZjtPR6sGla5eVY2-uN1hkbu9P9ElmavH5LdeRpn8csVyp40nwtfF2ihpzs1vY3xgMZ1nAwFUPKG5oRg-Xv6WCe0U9_stMtjUm6ePGzpIdcpQbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7748c731ab.mp4?token=YckfA9C5sDwFvdK4HrzTpY9umfWX7018W7ItPQj1wZQldFCscppNKDTvUVVxYV7ZjJe_BtlbwFmzgTVn1OjulW-vzGnLwd4WraITt2AtkDFkt8YZLE6psh9aAp0K__cGnFl17HgrzUH-y4dMAgikMqSC_-eXS8udWxzRwdi_yBwTEdY-ZSBpVVZQgHGZHoaJRNQNm880vxixDGnDLe6tit-B6l4AwZfyvZelaPA8jBKB3TW5-32lc6z5GpR770f3On60lDz102O33k-n5a62BChzj35rEh4LfLYmZhIwNvoNVSK-5A3JnSc2vtA2gTNPe3b-apEDM3mhLhBaZL-zCgzOnI8yj9tQvf0Qc3DmQz977crHMrFUsXwSc75cV0ZOikx_JUapWFOxj6SzIlFA2hoJc_rag3ttoWpwuluX2UkJvSlQpaDG_8MH0UQv2faT7z0G56XsplG__UohnmdX6FpUrf7ycOHsC7nQNT-3EN-vntpyVrpv7bAR65lFGHHQrat4FDNRco1TG5xS7Gfzuhf-d8TEHuLWtoeQWu5CkfsVJRBxC9zFXCPH5f398ZjtPR6sGla5eVY2-uN1hkbu9P9ElmavH5LdeRpn8csVyp40nwtfF2ihpzs1vY3xgMZ1nAwFUPKG5oRg-Xv6WCe0U9_stMtjUm6ePGzpIdcpQbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور چین، شی جین‌پینگ،
با موارد‌ زیر با رئیس‌جمهور ترامپ موافقت کرده:
۱.
در موضوع ایران، به آمریکا
«هر چیزی که ترامپ نیاز دارد» بدهید
.
۲. سویای بیشتری بخرید.
۳. نفت بیشتری از آمریکا بخرید.
۴- ال‌ان‌جی بیشتری از آمریکا بخرید.
۵. ۲۰۰ فروند هواپیمای بوئینگ بخرید.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4967" target="_blank">📅 20:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4966">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=Vrxj3c4E4ixS3mOw7gONH49NIKBoYQT6CRKQ2ruYUlUNmG3pBUNHv44J2E6ob3nJnsaBJPxfKRLXJKRHhlD22WlW4pZO3Wwi1Zb4AwXWsIrvn7mFBPrJPxf144fgizQT1eGOPmEEkSzZzfZuDqKuWNDDCx8rl1bVe-e3ep8JaWOZ54maf_DYGmW3nyAx31YR6_OGaEr-Ck12SzPRNQekHq7SzytZKAo6mYl3hSnCR0RNGafwByt_0UNbvYNxTPE5gi9nVnbWl-V5FdnriEH-O4AkkhL4nzsZ63bc7siBMjT-J1RozTt7Vm0ZxVCIn241Mmunl7SZUBe5ZFpUa0uf7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24cc1c70c2.mp4?token=Vrxj3c4E4ixS3mOw7gONH49NIKBoYQT6CRKQ2ruYUlUNmG3pBUNHv44J2E6ob3nJnsaBJPxfKRLXJKRHhlD22WlW4pZO3Wwi1Zb4AwXWsIrvn7mFBPrJPxf144fgizQT1eGOPmEEkSzZzfZuDqKuWNDDCx8rl1bVe-e3ep8JaWOZ54maf_DYGmW3nyAx31YR6_OGaEr-Ck12SzPRNQekHq7SzytZKAo6mYl3hSnCR0RNGafwByt_0UNbvYNxTPE5gi9nVnbWl-V5FdnriEH-O4AkkhL4nzsZ63bc7siBMjT-J1RozTt7Vm0ZxVCIn241Mmunl7SZUBe5ZFpUa0uf7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4966" target="_blank">📅 17:03 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4965">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2182de948.mp4?token=YBuPvUTY31n8VGWS5M5ITR_PmOtIj3RxCX7UkUWB7G-c9KLyg3Tpp4iL25AjionpeQgUUdF8ShRWfSnSZYqiOO0rgo9u_jdkIo-w4Ykjmc-fCUx5Om99QKsXjjevNrD2fZ2OpikJDuPYzaZd1ZHncjMoAcQp6_LWDIi5QyDQuCMbLCoiwJQ2lVhTUDwzl7BBRFjfJJdTdM7oHdw6eBsYxu3xwY1KBUESvzOIEk198YULGBUskgkYgV2nsP-TJI1aIlEm1xgbRbrwYVpGVtJWi1_4Zirliz6SvmwzLTEllxjaDpR-shO8tnLaV8Bg2EYHRJHRQS1Uoy1W2uydTjVFmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2182de948.mp4?token=YBuPvUTY31n8VGWS5M5ITR_PmOtIj3RxCX7UkUWB7G-c9KLyg3Tpp4iL25AjionpeQgUUdF8ShRWfSnSZYqiOO0rgo9u_jdkIo-w4Ykjmc-fCUx5Om99QKsXjjevNrD2fZ2OpikJDuPYzaZd1ZHncjMoAcQp6_LWDIi5QyDQuCMbLCoiwJQ2lVhTUDwzl7BBRFjfJJdTdM7oHdw6eBsYxu3xwY1KBUESvzOIEk198YULGBUskgkYgV2nsP-TJI1aIlEm1xgbRbrwYVpGVtJWi1_4Zirliz6SvmwzLTEllxjaDpR-shO8tnLaV8Bg2EYHRJHRQS1Uoy1W2uydTjVFmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک بچه‌اش رو هم برده چین :)</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4965" target="_blank">📅 17:02 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4964">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
🚨
🚨
سپاه یک کشتی رو در اطراف امارات (فجیره) توقیف کرده و در حال انتقال اون به سمت سواحل ایرانه.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4964" target="_blank">📅 11:34 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4963">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=YXb5c56FehNwMtWHolzfok4aYgEJ6nvX0ywY6PobUFO0ftHQx3D2Alkzh5Ffh_nxQFSS-eygDEar3spY8r7ELj5D41yHh2nlddSlk4lGs4CywwJ2BtyL-tokHoNC3ivUJEq-1J6abvVaNyC8pLNCdGRaqCWD5cPXUMn4rt-DjYSlhk2-Iz1q8WOkYQr1j6uQI1C-GQLqyxdttPfhBn8r7Id8F51s5cyRCfUo0ohgxDaOPzG_QUsYjOH2XOMF87WrDuW15H-3lIwJMkDXXxm-ZENSqCbufIsliPhUoXs4zedsEwprqeKZm5vv1aVqGELKlsteHAA7lg6XuhPpx_8IaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/006c04d7ac.mp4?token=YXb5c56FehNwMtWHolzfok4aYgEJ6nvX0ywY6PobUFO0ftHQx3D2Alkzh5Ffh_nxQFSS-eygDEar3spY8r7ELj5D41yHh2nlddSlk4lGs4CywwJ2BtyL-tokHoNC3ivUJEq-1J6abvVaNyC8pLNCdGRaqCWD5cPXUMn4rt-DjYSlhk2-Iz1q8WOkYQr1j6uQI1C-GQLqyxdttPfhBn8r7Id8F51s5cyRCfUo0ohgxDaOPzG_QUsYjOH2XOMF87WrDuW15H-3lIwJMkDXXxm-ZENSqCbufIsliPhUoXs4zedsEwprqeKZm5vv1aVqGELKlsteHAA7lg6XuhPpx_8IaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خب اگه نهادهای اطلاعاتی آمریکا متوجه شدند که جمهوری اسلامی به ۳۰ سایت موشکی از ۳۳ سایت موشکی در کرانه‌های تنگه هرمز دسترسی پیدا کرده،
[دسترسی پیدا کرده، یعنی در حملات آمریکا دهانه ورودی این سایت‌ها مسدود شده بود و دوباره دسترسی پیدا کرده]
نمیشه سریع اینطور نتیجه گرفت که : پس اگه جنگ از سر گرفته بشه جمهوری اسلامی قدرتمنده و…. چون دسترسی پیدا کرده.
این گزارش یک بعد دیگه هم داره
:
اونهم اینکه نهادهای اطلاعاتی آمریکا روی این۳۳ سایت موشکی اشراف اطلاعاتی کاملی دارند!
می‌دونند دقیقا کجا هستند،
موقعیت جغرافیای اونها رو دارند، و این گزارش یعنی وضعیت اونها رو مرتب رصد می‌کنن!
و خب اگه حمله‌ای بشه، می‌تونن در همون ده دقیقه اول شروع جنگ،
اول دوباره دهانه اینها رو ببندن!
اگه قبل از جنگ ۴۰ روزه نمی‌دونستن
موقعیت این سایت‌ها رو،
و در پی حملات موشکی جمهوری اسلامی پی بردند به موقعیت این سایت‌های موشکی ، الان همه رو زیر نظر دارند و رصد می‌کنند
و شناسایی شدن!</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4963" target="_blank">📅 10:50 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4962">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">فهرستی از رهبران کسب‌وکار که به همراه رئیس‌جمهور ترامپ در سفر به چین شرکت  کرده‌اند:
1. ایلان ماسک، مدیرعامل تسلا و اسپیس‌ایکس
2. تیم کوک، مدیرعامل اپل
3. لری فینک، مدیرعامل بلک‌راک
4. استیفن شوارتزمان، مدیرعامل بلک‌استون
5. دیوید سولومون، مدیرعامل گلدمن ساکس
6. جین فریزر، مدیرعامل سیتی‌گروپ
7. کلی اورتبرگ، مدیرعامل بوئینگ
8. مایکل میباخ، مدیرعامل مسترکارت
9. رایان مک‌ایرنری، مدیرعامل ویزا
10. لری کالپ، مدیرعامل جنرال الکتریک
11. سانجای مهروترا، مدیرعامل میکرون
12. کریستیانو آمن، مدیرعامل کوالکام
13. برایان سایکز، مدیرعامل کارگیل
14. دینا پاول مک‌کورمیک، مدیر اجرایی متا
15. جیکوب تیسن، مدیرعامل ایلومینا
16. جیم اندرسون، مدیرعامل کوهرنت</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4962" target="_blank">📅 10:24 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4961">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=rrH1s2yS2mAdyI6KxKzIW3aZ7M2zvOWeouKmBrPMb9ESfFMVuKMzE6P1aOxSP4M7YOvyJLY9RXcEAqywi2EPEkC26q3ojGJxmJ_PZ5PtijyKJQ_zVl-OlOKyRLE9dgy-aE9Q6PrGgbnfd3p7bwrRGk3AL11HLF-4MK5SMstCR1QL4P-4mwR83ypX3TONyce3quEsOIEBvLFpidMYq2SiEkkFZT1HWwQOSMqGlddJJcn8pj-gjx2Txk19VsiedBzzlKj-HMBf0jZdml61ZLunCLkOTq5dG3bA3YmDAx_5P6zLp_JNT7R_alVYjQRREbhetpNQZjXknzUkSpIiHIM_Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3de9e8dca4.mp4?token=rrH1s2yS2mAdyI6KxKzIW3aZ7M2zvOWeouKmBrPMb9ESfFMVuKMzE6P1aOxSP4M7YOvyJLY9RXcEAqywi2EPEkC26q3ojGJxmJ_PZ5PtijyKJQ_zVl-OlOKyRLE9dgy-aE9Q6PrGgbnfd3p7bwrRGk3AL11HLF-4MK5SMstCR1QL4P-4mwR83ypX3TONyce3quEsOIEBvLFpidMYq2SiEkkFZT1HWwQOSMqGlddJJcn8pj-gjx2Txk19VsiedBzzlKj-HMBf0jZdml61ZLunCLkOTq5dG3bA3YmDAx_5P6zLp_JNT7R_alVYjQRREbhetpNQZjXknzUkSpIiHIM_Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس جمهور چین در دیدار با ترامپ :
چین و آمریکا از همکاری سود می‌بینند و از تقابل زیان.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4961" target="_blank">📅 10:23 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4960">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6tqOXFsZ-pcPI8EQGD-g6WJfEWVsBAqb5fwGMj43fIeAzGcp51qe8GlGk8GQeFJcpERKuGkCZ30vzDqCur9GpesHATA4HbAuqMY1FIWzvKlnjS04g9CmwTVKikCi--k27qwUO8Kuj1g21hnxO89-oDKeaqbpa98hZOAsQq8CeaWlExd2atvkdPlfP2Zo9JpCfZvXTU_z9l40_iZad1cv4oaQ9mgwpHQm5TTlbqfsgnu_YOKzlWb51I6JLeN3XvFIkS9YYhmsFnOldRxvpsN2qXtlxMxm50V3f0BD6zMpOYAy-rn8J_nMSpJ5qOQx_aG17ikRThrEoAaWX-Ln7ODEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امارات در حال ایجاد فنس‌های محافظتی برای دفع حملات پهپادی است.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4960" target="_blank">📅 21:33 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4959">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">جمهوری اسلامی : ۴ مامور دستگیر شده در کویت در چهارچوب ماموریت گشت‌زنی دریایی بودند که به خاطر اختلال در سامانه ناوبری وارد آب‌های کویت شدند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4959" target="_blank">📅 20:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4958">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
ناکامی «هفت باره» دمکرات‌های سنای آمریکا در طرح محدود کردن اختیارات جنگی ترامپ در جنگ علیه جمهوری اسلامی.
دمکرات‌های سنای آمریکا هفت بار طرح محدود کردن اختیارات رئیس جمهور در  جنگ علیه ایران را به رای گذاشتند و هر ۷ بار شکست خوردند.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4958" target="_blank">📅 20:47 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4957">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🚨
🚨
🚨
در یک اقدام بی‌سابقه دولت لبنان با طرح شکایتی در سازمان ملل، جمهوری اسلامی را مقصر تحمیل جنگ‌های ویرانگر به لبنان معرفی کرد.
لبنان در این نامه نهادهای جمهوری اسلامی، از جمله سپاه پاسداران را مسئول درگیر شدن این کشور در جنگ، برخلاف خواست دولت معرفی کرد.
‏این شکایت می‌گوید که این درگیری منجر به کشته و زخمی شدن هزاران شهروند لبنانی، آوارگی بیش از یک میلیون نفر، ویرانی گسترده در روستاها و شهرها، و اشغال بخش‌هایی از خاک لبنان توسط اسرائیل شده است.
لبنان در این نامه گفته با اینکه سفیر جمهوری اسلامی را اخراج کرده، اما او خاک لبنان را ترک نمی‌کند!</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/farahmand_alipour/4957" target="_blank">📅 20:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4956">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f9eG6kD0Zt6QSyi_ZejLmboyLyMw8xaN6xac3YI9OF24aXA6qcsz-xF6_ELmNUUjvNVTbWw2Lc0FU5Wjg_U7U-o4O7rOiyYw2Lpr2r4eax7rEgkvHOmDHyXsCVwypyT204Gt-060MRwzYTJmtawni8R5tKdW-AeCtdg71koJePx0w5nx-x_6iTLfvU4pKsilpU0bmd4tBKK4wYSnwOIiQLtK_jAy0cuWPhIGtiDolcsnA2buVHAD8aqBu1l5QcZWyXLqt8YzgdzhAFGDeJuFbWHqzNN0hjmIHNzhIXhCdMcszXGjfMY1lVOxj6eA19LCTMkmyQJTJaxOJmENC25dPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برخی از رسانه‌های فرانسوی دست به انتشار گزارشی به نقل از «فلورین تاردیف» خبرنگار «پاری‌مچ» زده‌اند که حکایت از روابط پنهانی امانوئل ماکرون و گلشیفته فراهانی دارد.
این خبرنگار فرانسوی در گزارش خود نوشته که سیلی که زن ماکرون به او در کنار در خروجی هواپیما زد، به خاطر همین رابطه بوده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/4956" target="_blank">📅 14:23 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4955">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تداوم انتشار اخبار مشارکت نظامی امارات و عربستان در جنگ ۴۰ روزه توسط رسانه‌های غربی :
وال استریت ژورنال : رئیس موساد در طی جنگ ۴۰ روزه حداقل دو بار از امارات دیدار کرد.
‏گاردین: ‏اختلافات داخلی میان کشورهای حاشیهٔ خلیج فارس، به‌ویژه بین عربستان سعودی و امارات، در محافل خصوصی معطوف به این مسئله بوده است که آیا خشم کشورهای عربی از حملات ایران باید تا حد تلافی‌های نظامی ادامه یابد، یا این اقدام ممکن است سطحی گسترده از تنش غیرقابل کنترل را ایجاد کند.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4955" target="_blank">📅 14:19 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4954">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🚨
‏«کنگره ملی کردستان»، نهاد فراگیر تشکل‌های کُرد، با انتشار بیانیه‌ای صحبت‌های دونالد ترامپ درباره ارائه سلاح به گروه‌های کُرد برای مقابله با جمهوری اسلامی را رد کرد و هشدار داد چنین اظهاراتی خطر ایجاد یک کارزار خصمانه هماهنگ علیه مردم کُرد را به همراه دارد.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/4954" target="_blank">📅 14:17 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4953">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SXF7H2LqykVzZaJ_5_oEKE42PYNWYuxUuSf0tLgBurhFZocjkcAPhmMqlh-qhDbrBgvdUxEaYCIBYnYkt78agMYofpL4jWlGxFOFQiVGfdmzgz4iLwmAJosKLf9WZgWklYFESDH5oirrVEo5DYo9k_4l1fiOqz8olhIxxO5Ldqn9UMoU4C0TQMkDeSVkWemmCvLO8kRL5QwuzDIQszNp9DwYl5KlLkCA-sv9x9QQqklzFwQXG5E8C9MnJFxKQfHV7Ov_sZbD5l9za-FoaTlqpWKSEcEYxM41JahpDSk-nWveyeFtQrIuncmBPU7SodMjwZyekag-i4kFxZZAPWfJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها دولت و حکومت نیستن
مشتی راهزن و گروگانگیرن</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/farahmand_alipour/4953" target="_blank">📅 12:01 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4952">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lIVw0aO5E6RRktuoWhTyzdH7e-5oxWhn5w9423jNy61Oia_X10q3nsHuLd6fl889rzqBIicIWahWrKCubDmnzNC5MLX3wgyL5tN6EvN4AkyJIwsCmfXBnzDyKxmpy3zE2u3S4LDJpfZyXy7laCRFtjR9ekA-oT8tNIubGwVWB5Za7FuasPXOIScKHV0vPKKmOUeDOjmYCMwx7Ijuy8E7EC8fcFhrpq994QDY-02-gQwInsjYBuSkADs1-5_GJ5cyNQeGny8j9xy4ufd0UZTDWImcfvTkiZu5Edlluc_DPwCS_2-dLEUI1tuZ5QGBa8H7VHW55shzwWLbL8PM7ixABA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپانیا به خاطر حضور اسرائیل مسابقات «یوروویژن» رو بایکوت کرد و دیشب غایب بزرگ بود.
نماینده اسرائیل اما با اجرای یک ترانه عبری - فرانسوی - انگلیسی
به مرحله نیمه‌ نهایی رفت.
در اسپانیا فقط ۴۰٪ از جوانان حامی
این بایکوت بودند. (در ایتالیا ۳۳٪)
یعنی از هر ۱۰ جوان اسپانیایی
فقط  ۴ نفر حامی بایکوت بودند!
نماینده ایتالیا هم از ناپل بود و یک ترانه
با حال و هوای جنوب ایتالیا اجرا کرد.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/farahmand_alipour/4952" target="_blank">📅 10:58 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4951">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SEijOBgYpAjzcur6KpiFhhmIrTQKtAb-FYGaQJ71JQwKRlIVq70ISUgBF5kkjXJIyOAsWatvUCJ0mzktr21-e51Fl5X4WkrUN8GR0GvUBHatyy22tNVr9bI8fVIXe4LmUTFtrykPMU3xVq7-kWgWYp5miUx5isBj1OEua2VZfF1Hkrz-31cIifwienPJW1t5C_TXP7CSqBT_OH4RoV7JKAmboWqAb52F9cAEevc6o9gR-_oXd8w_VwJqr3awDUC_x67FpIDnQDne5ir5uZZPLsFyZaBifTM8oWQlty_YP9uu03yiJJlHlwumDzj9Wfxk-F1Ygpt2Dzv1hZEanZUE0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏نهادهای اطلاعاتی آمریکا:
‏جمهوری اسلامی دسترسی خود به ۳۰ سایت از ۳۳ سایت موشکی خود در امتداد تنگه هرمز را احیا کرده.
این سایت‌ها در زمان جنگ ۴۰ روزه با حمله به وردی آنها مسدود شده بودند.
همچنین ۷۰ درصد از لانچرهای متحرک خود را همچنان حفظ کرده.
‏و مجددا به ۹۰ درصد از انبار و سکوی پرتاب زیرزمینی دسترسی پیدا کرده.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/4951" target="_blank">📅 10:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4950">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rEJr2GZAhzPFF7cmYx11cnzfEUFPI2G9zKjcHsR8BSoZtgGFsW8shp4jw5M8A9zxejj1AuaM3WUsblG04cI7RXh1cKbqRN3hWFrrnW6F4_yg6nGEHwoqioIdwjAWTn49ogZX9cK9KLHlc1SXqj0wwdxaFyH4c6fnSvvLSFZyjfysWpxM9hSnIGCOdWhdjo_AsrSIu2qd-oo8BseaW3d_6sEBwvWBIkl-EOdBBmZB4ZuWRyE0tS-Spmnwuxm57K9ppec_aCJ_Can8HIepSFz_oe-rtg3zcbHjSOEOv00NgsFA_8LwwtflAzVq0GyTzC0_tiwm9o7VmaogNWJaJkJcbcY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4137eb479f.mp4?token=BJo6iH-suW2b_RCJj6p3SpKlgJPQX4vPcwuOXSfpAu38DlUxcKIIsmB-bJtTE_EQMT3ZedmhJ_ooRn6RvslzozsFXIAsQOxr-BM2XDfq7KXOp6yxNktQQftSDw8is3v2SMiC6lOyshal--46xjxL-g7hGJQp7Zi9eBDbCz9goXYmrJuru9JMWlCiqfTdQTgW0u9wJPL-ditCIKi-0p69z0PJVTpnR5_tNGq0bEnfPve_lNcGDQ_T1U9n9__jZiHs3CHwL4fcV2RvzTv-XnZTwINt_LENK5BuPHbepZ4VEHmC01-dv4ZXRrBBgPtzb9juE9trhsNB4Wp6MjntPZo-rEJr2GZAhzPFF7cmYx11cnzfEUFPI2G9zKjcHsR8BSoZtgGFsW8shp4jw5M8A9zxejj1AuaM3WUsblG04cI7RXh1cKbqRN3hWFrrnW6F4_yg6nGEHwoqioIdwjAWTn49ogZX9cK9KLHlc1SXqj0wwdxaFyH4c6fnSvvLSFZyjfysWpxM9hSnIGCOdWhdjo_AsrSIu2qd-oo8BseaW3d_6sEBwvWBIkl-EOdBBmZB4ZuWRyE0tS-Spmnwuxm57K9ppec_aCJ_Can8HIepSFz_oe-rtg3zcbHjSOEOv00NgsFA_8LwwtflAzVq0GyTzC0_tiwm9o7VmaogNWJaJkJcbcY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انتقاد شاهزاده رضا پهلوی  از سیاست‌های ترامپ، «از یک طرف می‌گوید مردم باید قیام کنند و در عین حال می‌گوید صبر کنید، ما در حال مذاکره هستیم. این همه را گیج می‌کند.
شما نمی‌توانید سیگنال‌های متناقض
ارسال کنید.»</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4950" target="_blank">📅 10:12 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4949">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ccf3usB4plVdsOdTxf1EmSXmzaqxM8s79lhV2aNVLpqVygNS6v2FMbp5DA3EjY690ez1SbJhjEUluzOllUUefEqWfte9OYJp3jp799dXm6rq1SRtNfl3a6Y3Pu0xAoOzMAGVwrpPof88hgK05KDqM-Hrb3X5lZR5lNZJuUsJ_uMm_IgTTqlxbcSX86Xmd2yiT7Nc9QFvJtK7yjQpCqTJ_zkDSMkrpMknWvStJltG2-6RwjEHQCuX_iE6i5wyvrbDMGcM6CCTh8m5bOKfqO0eTaei_-Aug0sOVJtYFQXjlw7CKP8pckJ6VpZaf_tfyBRRLs_DdMPWoveTT_Duc-EBHF42gnhsjfkkJ4OPC1VrrzMi75TNBJ--f9WSAUo5OmLBE46zBZsM54Wrr39LKiV6b1UgoS_K1VPwf2_EzuMqMqCNoYtstwSCI_RHqtGKYMWXItzHEppWUeKEFWRn8maq0AhZf7X6piuwayYaTtRQAmCCXW8MCX1FMSlKA2rm6CZp6zWBNuxjpU4EhztduE3kJyS3MOrMxZY5AVmUMLlvyCBzSG09NqNMgMQZ_WVwg3I1sOolFIM6N8HQAOuQKziY3dYjx_YRpcaJS9tzwvIE7VDVBU3viLFmjG7gB5_hzpFutj8ByMAGTaMx1RmEKLCi-aHW5EXcmwEGPJdhid9Ru5s" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa82a5c855.mp4?token=ccf3usB4plVdsOdTxf1EmSXmzaqxM8s79lhV2aNVLpqVygNS6v2FMbp5DA3EjY690ez1SbJhjEUluzOllUUefEqWfte9OYJp3jp799dXm6rq1SRtNfl3a6Y3Pu0xAoOzMAGVwrpPof88hgK05KDqM-Hrb3X5lZR5lNZJuUsJ_uMm_IgTTqlxbcSX86Xmd2yiT7Nc9QFvJtK7yjQpCqTJ_zkDSMkrpMknWvStJltG2-6RwjEHQCuX_iE6i5wyvrbDMGcM6CCTh8m5bOKfqO0eTaei_-Aug0sOVJtYFQXjlw7CKP8pckJ6VpZaf_tfyBRRLs_DdMPWoveTT_Duc-EBHF42gnhsjfkkJ4OPC1VrrzMi75TNBJ--f9WSAUo5OmLBE46zBZsM54Wrr39LKiV6b1UgoS_K1VPwf2_EzuMqMqCNoYtstwSCI_RHqtGKYMWXItzHEppWUeKEFWRn8maq0AhZf7X6piuwayYaTtRQAmCCXW8MCX1FMSlKA2rm6CZp6zWBNuxjpU4EhztduE3kJyS3MOrMxZY5AVmUMLlvyCBzSG09NqNMgMQZ_WVwg3I1sOolFIM6N8HQAOuQKziY3dYjx_YRpcaJS9tzwvIE7VDVBU3viLFmjG7gB5_hzpFutj8ByMAGTaMx1RmEKLCi-aHW5EXcmwEGPJdhid9Ru5s" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد یه عده زمان جنگ با آب و تاب می‌نوشتن که تیم جمهوری اسلامی همگی «دکتر» هستند! دکتر قالیباف،! دکتر رضایی!
دکتر لاریجانی!
مثلا دکتر لاریجانی چند سال بعد از اینکه
«سرتیپ پاسدار» شد و رئیس سازمان
صدا و سیما بود و صد تا شغل دیگه داشت، تحت نظر «غلامعلی حدادعادل»
مدرک فلسفه گرفت!
اون محسن رضایی و قالیباف
و بقیه شون که هیچ!</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/4949" target="_blank">📅 10:02 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4948">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.  هرچند…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/4948" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4947">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e32rZwQfwIvv4r75eLqnoYpzFqwmoEhy7BcdSQqAU769ICEmYBlUJbVCQm7GEd_6Cjqlx6VfK3yHegAHR6LYKUJkwk7RtlcAwkIG3TTaSui8eTuq0a3RL-YC20s8LGic_WSzGjBEVeAh_HpEsHkyElHNmlTvKzupebDSpFd_h_57p19SOUM4vjgXtWTXoRsEh-12kd34AQSEP79tuWZFRM5XNvRpYp-_VApz_froAsAWEtSnJ8eohyoml-STcTX1t8i16UupOY5FHnplpqzeyBHzUgmIBXmUE7-FJW5sc4Y39uO4CUFL9yLbG4pV7bzwPDJfdo_PR2jqqITyMaLoQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پاپ لئون چهاردهم به محمدحسین مختاری، سفیر جمهوری اسلامی در واتیکان، «صلیب بزرگ نشان پاپی پیوس نهم» را اعطا کرد؛ بالاترین نشان دیپلماتیک فعال واتیکان. این تصمیم در سندی مورخ ۸ مه و با امضای کاردینال پیترو پارولین، وزیر امور خارجه واتیکان، تأیید شده است.
هرچند این نشان معمولاً بخشی از پروتکل دیپلماتیک واتیکان محسوب می‌شود و معمولاً پس از چند سال خدمت به سفیران مستقر در واتیکان اعطا می‌شود، اما فضای ژئوپلیتیک کنونی و اظهارات اخیر پاپ درباره تنش‌ها با ایران، باعث شده این اقدام به موضوعی بحث‌برانگیز تبدیل شود.</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/farahmand_alipour/4947" target="_blank">📅 09:48 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4946">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mUr0Vom3K9scoRuNgPR9JQq_5e6SyOgRAde1FGW-5eh-V7sE5e2lkaX3ru_xcVVF-T1URTSYgxM7F15J71kZ7ij1xJz1Lqt1DDPmPDkzkOE0l1Fd9X9l2BeRkaYIgjOU4jWWD2KUF2_TWHh_q-asdXXmeEDMxvnwQIwIbSfnMT3j5IJF8dKMP6BZcopbjgw_TzuSRKT0LcKbaGinqbXzy75Bq0OsQiIjJ0UEExPI6IEp_e5dvhNCeXFofAWZPNjPRsS91HFWRWSYYBodFPbAWhOXeUXeODCok0tNtc7IxudRIIAswj28fFm_SSVrbeo3wnEsXALzZuOCoF423QSnkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر آموزش و ‌پرورش وقت، در گفتگو با خبرنگاران در پاسخ به سؤالی مبنی بر تقاضای برخی نمایندگان مجلس به استعفای وزیر و برکناری مدیر کل آموزش و پرورش استان آذربایجان غربی گفت: «شما چی؟ شما را برکنار کنیم یا نه اگر به موقع خبر می‌دادید مواظب مدرسه شین آباد پیرانشهر باشید این اتفاق روی نمی‌داد.»</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/4946" target="_blank">📅 09:18 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4945">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N0W4n0jx37IUUIyuCUY8H_QTj1Qf-CwY7XnMzwT89Kj_W6EMtYJvtYWLxVmQztvZwHUru-_RwTorXWeXY9-QmYu0Lu0sIl-I52kJHHZUCR9bbKH8flsTydV7HisM0OuBKNTskvn_wotK3QtPw-IvW7FK7qAJTd00GkPO_gP4ZvK6yVCwxyOpUtwxC-10rXOWle1fbz3gx3BIsg3yfbQsRaeuzJRaAcm6tsfIB7ta4B-rGylRGfla7P0-GsbSbv8ybfGSX9sPT8AhhN4K8I9unTI8GhYuvvpVbD2TPoHskj6ZtqmHyVexECBGu8LfzsHCnrqd2soUd8_3rdHUwxKxNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/4945" target="_blank">📅 09:16 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4944">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g-I_9aCcZRiSsS78iMMBfYZzeG7CvkEXulxvxT3mbQGxlUDIeaWt7qNNZGsB_MhjA4KPrBNfoX3nYlv3esddTiHzmEcc092lUVX-VfZVwhMNmcru0sCzJwHZI4U1RJeCIfVq5ws6d2mxi7uEvhGeHRYBuMQW_jDBv-l3EFf9SHRQbcKsSHfdpTzOf8n3eOg-43nbfu3ay14Z7-hUcNYCs2tmmVG4ybOUxb66dJfJHn65uH-KJ16o9ecJRGfffz9q15vdQ9isJhgbuW8HHu-Eu469wWBn31C6jKr1NMs3QRgI9MdPvqMLY5qWm2H4zpke6AzOIq60EHKvebsDtOkCyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحی دیگر ….. اعدامی دیگر
بر اساس گزارش توانا
احسان افرشته
، متولد ۱۳۷۳، دانش‌آموخته مهندسی عمران در مقطع کارشناسی ارشد اما نخبه شبکه و IT، اصالتا اصفهانی و بزرگ‌شده تهران، او در ترکیه بود، نیروهای امنیتی پدرش را فریب می‌دهند که احسان را تشویق کند تا به ایران بازگردد
و می‌گویند خطری او را تهدید نمی‌کند.
احسان برمی‌گردد و حکم اعدام می‌گیرد.
پدرش چند وقت پیش و بعد از صدور حکم اعدام پسرش - توسط قاضی صلواتی - سکته می‌کند و جانش را از دست می‌دهد. امروز هم خود احسان را اعدام کردند.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4944" target="_blank">📅 08:45 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4943">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dnyq-y7C0ALWt3TC-VW16K5wJJgGRL6zIbntrytaCEjFtsXITEWtgCrMOUPTRiRpRW3Pu26DczoMVNDr-o3tZm8DC24QD4_YfPOvSvKxvfM0koOzXEtBEBjywtMRoXM2v2neOLOQg3P5823F_QMK665kTiAxEPkFTVwxwI-Dbf1mQv1TpLmEjDQ-bFqI0foDA0IidFmPFAEl-Sub2_-EfJBJ12dKl2cQqplunojinT3qFOsLNVE5GoehKT0WwfuFGMT-kVknz6G5Hbv-tC9RHT7Aov9UgH9n-vBkjCmrwHIcU1TxOYGlqBSoUYnrsuFxihktuYTHCQX_pgyIP9w-aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/4943" target="_blank">📅 00:40 · 23 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4942">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🚨
وقوع زلزله در تهران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/farahmand_alipour/4942" target="_blank">📅 23:48 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4941">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🚨
پنتاگون در حال تغییر نام عملیات حمله به ایران از «خشم حماسی» به «عملیات پتک» است.
پنتاگون میخواهد به این شیوه از اختیار قانونی رئیس جمهور برای دست زدن به یک «عملیات نظامی ۶۰ روزه» بدون نیاز به مجوز کنگره استفاده کند و با تغییر نام عملیات، دست خود را برای دور تازه درگیری نظامی باز کند، بدون محاسبه روزهای عملیات قبلی.
بر اساس قوانین آمریکا رئیس جمهور می‌تواند فرمان به «عملیات نظامی» دهد و این عملیات می‌تواند تا ۶۰ روز ادامه پیدا کند.
صدور «فرمان جنگ» اما بر عهده کنگره آمریکاست.</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/farahmand_alipour/4941" target="_blank">📅 23:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4940">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJL5BEo9MQkx7odJtryeZtvV7eCgmroTmQp01pP2Q-QyEjxfZEYKpDryA0A68AoaJQOeYCsZeaznqDLBilRrYcTBHRvcCVJmSBm-EElOXQnWRTPUCaFkK-5CTRYBaM6WfyXSy-ONjyt2w5dbpYyz8b4ugOvNMd56Jv4gMLmXuEFO6Kc4bybCLEdhNYZ4MDWA7yBoCvM3s5kSU8hqbD32gi_H6rZqTHWkzff49wXClKKF-SurY5GFB1bz1h1NeWLamEdxC2xAEzm_d-kE2r5Gfiab2ZnrnvhIWBBqkmTCRjxNJC3rCo_aJAfxjbpfGvyGOP_B_lFnsQKKzuGL4DX3Uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای  رسماً جمهوری اسلامی  را متهم کرده که گروهی  از نیروهای ۳ پ  را با قایق ماهیگری  برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری  یک نظامی  کویتی زخمی شده است.  کویت که امروز سفیر جمهوری اسلامی…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4940" target="_blank">📅 23:39 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4939">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7_zu5V7NeePpwDjZnjs1IsgdwR-cpDm2fCHHrA_ghaDHdufxBTYF4O8w2wTuPbWqnyF58dZHYFNYEs1eINxpMjK70RYz0HlafPZKB8MERPb_Dz7ue_nrJIllbDgpAprAnOcIpywJ5S9w7a1ighmzdggFa3fO6WaXOdn1VhMDKQx4cqStZJyxuNbT4yT77CB68At-aZXruIXpXveC6U3vOBgjN7fIotIaf-he2okUTAYS_1j3pe8BwpfMo2yV69EPI10MaA86c2CrvQzf5GUpxjigAL7mRvDVt9w8OXyO4UWmO9bS_mAbbVta0YFHip-MuWu6ZgU2Qk2cDNUCEpSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عربستان اما در میانه جنگ دست به حمله به ایران زده، در واکنش به حملات مستمر جمهوری اسلامی به عربستان،  نکته جالب اینه که رویترز میگه عربستان حمله کرده بعد به جمهوری اسلامی گفته حمله کرده و هشدار داده اگه به عربستان باز حمله کنه عربستان بازهم به ایران حمله خواهد…</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/farahmand_alipour/4939" target="_blank">📅 23:15 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4938">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH-kHPzvcPbpgk85pgyN9dEfSY_rTmavMseRMWIUVHOLOOrRYIODzlh8DC3P6ua5Ty7JFcdba_C_nz5f7OlW7v_W0S3b0xsqQzruv4SUaHku7QxbPr5PlnPRQ7Ggo_iFDZjIf9I3usZfQLmHZDcv8PfUYloZVwRgp2LGq8MgKKvJ3dQA4YfG_wTTwxuZHyHmgThKNuzynyCS9AKff3YaTza1AyR6uPfmXC10ztwGaD0Q--Vl2YVHfEj3IWFmbBLIm1HVFXMt7PmJ_KebkrBdtPjnLBtE3OxPII3rFyco3GGLYWCExDsc_RgM1dB6LcoKF-oXJsEkeDKz1VReNAlIGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی  به ایران داشتند،  امارات بعد از شروع آتش‌بس دو بار  حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.   امارات در صدر حملات جمهوری اسلامی بود حتی بیشتر از…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/4938" target="_blank">📅 23:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4937">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O752COy2tdGkmrQPpXUeGnppvHhFj1xbrDRaQ0ig8KWN3u86vTDy4o9iS-0buvtAH5BWH02tb91O6g6k2vEOq6aLlFIg4RBwRbgzTK6IHXADidhhPvmngaky0W2hb3D0IskpiCE9iSefIjEirEZ2pJRMzvtMt-f2q_wt_5WFBuMjbVGQJzECBjXoLzoWfhp7iUzQZLQvDSriZpzazPmI3lMsa9KIkYf-FZBrCtk03s57q5ZypbOKgAtphk1PE1mZ5UYzrLCt3pPRv7UBzsPhvJ4KM0ksm78Rnx1Yf7nKwP27x2nHoSfL6LQSvCwk9AnTmeNnlpSIaRrRgPQ0tBRIiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در دو روز اخیر مشخص شده که دو کشور امارات و عربستان حملات هوایی
به ایران داشتند،
امارات بعد از شروع آتش‌بس دو بار
حمله کرده، یکبار به پالایشگاهی در جزیره لاوان و  یکبار هم به تاسیسات پتروشیمی عسلویه.
امارات در صدر حملات جمهوری اسلامی بود
حتی بیشتر از آنکه اسرائیل مورد حمله قرار بگیرد، امارات مورد هدف قرار گرفته بود.
امارات پاسخ خود را بعد از شروع آتش‌بس
بین جمهوری اسلامی و آمریکا داده بود.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/farahmand_alipour/4937" target="_blank">📅 23:00 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4936">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=H9Und30h27kkDbkwlGaV0g6GdNGiOHkzUJPLKzCj0LFYVM1HkixPWqwNy2dPhXLbA0cRwzeaBsF-v4MHdwNxUxeBrslUZtnY76wpHoIXeRJe1X8UEl4RTU54iBwRME13Rzb7Qn0EG_TuGbTeB80xG1ZWNl-_fVghgRgGgb9Tjn5_Hd20Ph4DTJs2KoZEYTaxgckwwM2Hum1vISM3e5Ng9qxxNYJ9QmeN1dpJj4lvlr1pFz7h7e2nWub0wXz1LKwGX9lkQ7delRG-dKhvgOm_Fq_C2uTFAmUIEu24ipdLWsGeyxKWHjggtS_cIQhhhDqVB5QJhF6Ry_sKpHw3MdD2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e0ac8ea1f.mp4?token=H9Und30h27kkDbkwlGaV0g6GdNGiOHkzUJPLKzCj0LFYVM1HkixPWqwNy2dPhXLbA0cRwzeaBsF-v4MHdwNxUxeBrslUZtnY76wpHoIXeRJe1X8UEl4RTU54iBwRME13Rzb7Qn0EG_TuGbTeB80xG1ZWNl-_fVghgRgGgb9Tjn5_Hd20Ph4DTJs2KoZEYTaxgckwwM2Hum1vISM3e5Ng9qxxNYJ9QmeN1dpJj4lvlr1pFz7h7e2nWub0wXz1LKwGX9lkQ7delRG-dKhvgOm_Fq_C2uTFAmUIEu24ipdLWsGeyxKWHjggtS_cIQhhhDqVB5QJhF6Ry_sKpHw3MdD2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ راهی چین شد.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/farahmand_alipour/4936" target="_blank">📅 22:46 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4933">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EjRa66CfrWvLbjS8PMQd_uGfKWXLkO6-BQeKawuG_48-CY8vgQfbdJu8GS0iBVj8g9aWP7RslV8Se_-JG1NlkPD6Bj3GYqFYCEXcpegKhyXJNTTSQ_m7VMcfmB3i6ynJoSlsskyZy-YAMoMAKjYo7Xy8NYo9VcEm0A0soEMiJgwVR3Cv4y1yEku2Q7d9MnBK522EBFHlmnPe-e0F0YGRISHwJv9dPEb3aZOnkz4f2f0jsYfUh-ORUZb5VxYqFMGlNsCO60aui9sDPNFMAXWJ3iUWFbx4t2H2v9_lsMKLWpg5GZ21EDQsWLajYIluG0Anh-4DXDFDQpHZKcQBG9hciQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxJdhkAJwMYelpnFK-pAg2j7FBSAd2xmiBojyEjiMFBIE3qdKiYWs0Ix19N4AKe5M9_QLkLG8_VW8FXP2x8cA12bKUF6_lV3Jyg6wBsZtgt78pZfVYO1RNReHmEDIx0TA8zxGe76m7pEgINZbeE-31mTcHiRPloPsc_g5FiDgONatG6pDHEJMoKa2K2ewVW7dIQZxGlQMqwMdEwl-yBfpnQdHb6J37lJGX1WLSWGUgJRfbZtEH4iY13SWKNgeHyueuObOlRxCR8lacDbEQYqKOtJ_5iLQUouUrOdkvWkz8aSxLYSbT_UKbkDHJkocLm6m3VmwE1Nj-6XnfiLXnYPNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fs9ah3uFRvV4SlkuwMhO9uPTHM3tu-bx0EjeN-kPjIINj0Cxzen04xKBb2BlED7hOXDwJ5tdgAOu1eiwvOFXIYR_XVc_XyXWVM5z8Nl9nRiDIvgL7ykq4xkKI-Hy3asiNgFdHpzfOhD25guETVibo0GgDDuBc_OKm9_myrEGEPvWxf3bz4XRSuBoTPqfZPeegXqtmZ19OVuwGU5Nb6j4mEWsN41zxXXkRSjMBWFm3G3PsU2jNPrRwukhqkusVMutThF6u4yPzbc7t2RGvttb_isnEwnFdFiB-YlxU3B8PBb38KwSKEeBtr2tEgx6nzfbmz8hLDfgfYYohbG_PcnhIg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">۵۹ دانشجو امروز از غزه وارد ایتالیا شدند.
ایتالیا در مجموع به  ۲۲۹ دانشجوی اهل غزه بورسیه تحصیلی و تسهیلات اقامتی داده که امروز اولین گروه آنها با یک‌ پرواز وارد رم شدند.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/4933" target="_blank">📅 22:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4931">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s_MHX6je3iA8VVhISyhLB7n3GsTCfZRgWttWWm3jsGzJJYVdTumXf3y-zHD3OXtuR9JF3Hi-MtAj5TDE3AiKLXk-F2RskVSGkYzsjWH7yqtrGOhRuVoz1T0pEwKU-d0RwyCJBJljDiafmAEZ5JP5NkHly6M7WGkOconRXNmtAuehtss6tuu89JLUKBhiZJuK49i96KJEMdLjaiy49sp-hLOGggSWJrGPAYBKEjhT3hI5-5O7kQyT6_AnBb9d-PGSyGsRW9H9jGzk0aCXaTCktNuaA5Seqvr5Iz4w8XJJ0LTg39MvJ3d2MTEtE_6x7BC97E2FoZeJqxZ4wjtcbnYf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بر اساس گزارش رویترز عربستان در طول جنگ، مجموعه‌ای از حملات تلافی‌جویانه و بدون اطلاع‌رسانی قبلی را علیه ایران انجام داده است.
🚨
🚨
آمار رویترز نشان می‌دهد که پس از واکنش عربستان و حملات عربستان به ایران، حملات جمهوری اسلامی به عربستان کاهش یافت.
🔺
عربستان سعودی به ایران در مورد انتقام بیشتر هشدار داده بود اما کانال‌های دیپلماتیک حفظ شدند.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/4931" target="_blank">📅 21:58 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4930">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🚨
ترامپ در آستانه سفر به چین: نیازی به کمک چین در خصوص ایران نداریم.
🔺
یا ایران مسیر درست را انتخاب می‌کند یا ما کار را به پایان خواهیم رساند.
🔺
‏من به یک چیز فکر می‌کنم: ما نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد.
🔺
با فوران نفت در بازارهای جهانی مواجه خواهیم شد.
🔺
همه زندانیان سیاسی ونزوئلا را آزاد خواهیم کرد.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/4930" target="_blank">📅 21:37 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4928">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUIf0zbav_tBurJhAKjeKWQWBZtCvkQAA-FqGUdwc2XpiGyHVdVmmiWBjJbXJ8RGs2ukD7NaItGB8Nh4lpQuzYtrN9MSNBuuCL-TlvvZZE82Q8xGEKXx4RW-sPJ0c1htyJM-364cae2L8YoaO2XkaGLzujncTGX8wSfkT3sQiIP_SnJLaZ2UpmSvgc29ltrtWFqJi7ZmLjHSQgLY0WyzABIqnyHNU_5swfg0Bj6uY2vzxP7uwzwsP6IQcub9EWPkpf-SQkaJEQZadGQci9bkyR9abGn_24Eqs5SEmiwN8Br0X2BqQtw1cAZTOzPq9u6Hzsgd0ZldgpHvfOajCqubDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1S_vUivkpORIfvKyJuSaGCzGgL1en8HFvkzbjojxyw0avmtMZp9r4ZO-apn0FHVIR1jJfiCSbXSWKLyYS7r5_l2fe23p_TLfqHPSVACRQcBgXLCplLS6IsJ_45HiVHI4R8XEARoHpmVIpyc5KOKB9xRPl2GBYVIuscVdquCFIH4jA2UiBR50q9CTTwWDW8elYSpBWYYCnCSSQYyGIk1lJyIguhnUxUG5QrDqoIkJU2KHdanbZpCZeYl5IdPuODsUTrY7x-qkCYFGlBDK031SCxnpsxjkB37eCvkA3PP3FBKy94r3XOGN4pJDehiYvSBHSAAAZ2Zu5HMyEMJhNvdNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
وزارت خارجه کویت با صدور بیانیه‌ای
رسماً جمهوری اسلامی  را متهم کرده که گروهی
از نیروهای ۳ پ  را با قایق ماهیگری
برای عملیات خرابکارانه به خاکش در جزیره بوبیان فرستاده و  در جریان درگیری
یک نظامی  کویتی زخمی شده است.
کویت که امروز سفیر جمهوری اسلامی
را نیز احظار کرده گفته که ۴ تن از عناصر وابسته به ۳ پ را دستگیر کرده.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/4928" target="_blank">📅 20:34 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4927">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اینهایی که آرزوی مرگ یک نوزاد ۳ ماهه کردن، عمدتا عزاداران کشتن کودکان معصوم میناب هستند.
همه چیز این جماعت دروغ و خدعه است!</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4927" target="_blank">📅 13:06 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4926">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSY-QM1F1zVq1zoevj0bh8QHfOeHoVt51diEZ2EEdAGrjrlRIcvrB8ZNBwxuRopoT-KyhxXvOkOBK2cI7XnqXE8AcHxGBc2X7rjxf5kUkoBsGgCMuhXfUBfT96BJ0xLLCtDIHF9cdqTzLH3pUgzV1LmXgDjfnbXAevPSjkhjH-9piuy5ifGZu8RGPo3zO_SDG5AfmdkiMJJUF7ICbK03Z2yEy8Ek7mibGij4zZOlu0-IXmaiNA9Afhny6OGtU8xLr1l9DzmNjOGvaQ395fuAEE582b1LURDDr1wZdYRiMzE3J3YpjENmT2-VUF58UGV_z7KSIcIzU7ZrlKHKOY85mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرامکو (شرکت ملی نفت عربستان) :
در سه ماهه اول سال ۲۰۲۶ به رغم جنگ در خلیج فارس و بسته بودن تنگه هرمز، این شرکت افزایش ۲۵ درصدی درآمد داشت و ۳۲ میلیارد دلار سود به دست آورد.
بخشی از این افزایش شدید درآمد مربوط به افزایش قیمت نفت است.
عربستان از طریق دریای سرخ روزانه تا ۷ میلیون بشکه نفت صادرات دارد.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4926" target="_blank">📅 12:33 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4925">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
خسارت قطعی اینترنت توسط حکومت جمهوری اسلامی : ۴ میلیارد دلار!
اینها زیرساخت نیست؟ سرمایه نیست؟ یا اخوند اگه نابود کنه ایرادی نداره؟</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4925" target="_blank">📅 11:26 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4924">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
سی‌ان‌ان به نقل از منابع آگاه : پاکستان مواضع جمهوری اسلامی را «مثبت‌تر» از آنچه ایران بیان می‌کند، به آمریکا منتقل می‌کند!</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/4924" target="_blank">📅 11:25 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4922">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oOrrazGHv3xTTT0OB9jyQsBTik9sk8S5fmFhvOGty0FUMsmA_Hv-vmrAbu6NeC5m0jO2zktJf7tJxPjGumbqBE_xTuMnxay0VmeOkWVkdkyxgrHfW1bYW5mDMlZ1IVlX00a_Uy6NAAVtGSAWgXWu2rA54HWtWy1D-6UU6Hg3j4tIgy6gWn5LhNEVEoEkRkbNym4paOwSnPt9OowQJ4_cQL4lUxwwcV9l-K4RES4VCCmCi0S9f6Pu8rsdo62VFSCj2PXGVml1sQSQ7M9mUe7uCl3AlQlnQHzzKQMTM_B_nkMEhYd4Ueb_E45l6h2jBkDYaGuPCyyTTaVKdIasxqfXjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=eb_6N7iIc0F4bKxkE6IiSRU7-YLfUgNXEUIiqgC429T_QeylhLj6z3w4xM4S5hj0lc5I4Aburza-NaL_OQtTCDP5S65mrmIvMvrUIyJuOrty_HWW2AlLKMEBmLf7w7Jgbk4njGYhP5UmFuf4D3ncGFd5R6IEXeKW06EO7C401fuZ8VWidlK933jfKlVjUbDV0SnMATegj8dWm5fp5_LfNpF887qGtHbu6yiCt6V67vr3EeUJeGoJkMevkXUbvEmkBnuMD0PGBmIFkbu0_u3_9oMNmGtWiK6ykogi28f0PulyxkjVoSy1BnfXeG9XcUcT5HCE_Oc_XJrp-ZSMdbzTnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b194f425f.mp4?token=eb_6N7iIc0F4bKxkE6IiSRU7-YLfUgNXEUIiqgC429T_QeylhLj6z3w4xM4S5hj0lc5I4Aburza-NaL_OQtTCDP5S65mrmIvMvrUIyJuOrty_HWW2AlLKMEBmLf7w7Jgbk4njGYhP5UmFuf4D3ncGFd5R6IEXeKW06EO7C401fuZ8VWidlK933jfKlVjUbDV0SnMATegj8dWm5fp5_LfNpF887qGtHbu6yiCt6V67vr3EeUJeGoJkMevkXUbvEmkBnuMD0PGBmIFkbu0_u3_9oMNmGtWiK6ykogi28f0PulyxkjVoSy1BnfXeG9XcUcT5HCE_Oc_XJrp-ZSMdbzTnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تلویزیون جمهوری اسلامی، اعترافاتی از «عرفان شکورزاده» دانشجوی نخبه، پخش کرد که بگه : القا می‌کنند که در ایران اگه درس بخونی آینده‌ نداری. که ما در ایران بدبختیم.»
بعد بردن اعدامش کردن! تا اثبات کنن درست گفته بود! ما اتفاقا بسیار بدبختیم که اگه نبودیم چنین حکومتی بالای سرمون نبود! در جامعه‌ای با درس خوندن میشه به جایی رسید که اینهمه اعدام نخبه و فرار نخبه و دادن سهمیه و پذیرش و… وجود نداره.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4922" target="_blank">📅 11:10 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4921">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jTmkv6_0JElz8P0-pq_5sRPjOTgRr-It3mM0pINj3dVB1dlUQhvQhDtSZgcRffZh9b5lB_n9tJGFRKRmYRi8zt0TQUSrvCVOvJw9wqjAxGIEI8WhNw5TDSGKdzQe6PR6b_oj3SaU4rjdFIdC7xvko8ABPkWnY8uabFXH-xdVrAzroAGabYEiiYy3HcJxbXqCDzENwItpRThBT6gQFqXM6YElx5IikFWGqExszwVBxLVWS51BICuZi7uwZx10jbW20UBUJL1WOzI6N6VYiD3ueub_Z1ZZCeesSiFc6hUr9spOKt7aF9Kvtxau9TNyemR5df_oCB-XUK5yS2mC3Q0Pfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
جمهوری اسلامی تهدید کرد که در صورت حمله مجدد آمریکا و اسرائیل سطح غنی‌سازی را به ۹۰٪ خواهد رساند.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4921" target="_blank">📅 10:27 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4920">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJURmhhbySGUIwpaN_jPQjqQ5dOOPllq6KrfSbSUJ3ZsiPm9NJZ3-iSpjAaeYAhbXV9EkQ9eoZ8z-VSFzcK3cjiXr9UuKVX4MRdlbPtyuxboM8_lTYraYgSMl275MBW2KND-qlSXnTFFXxHg-hKF8euop7cmIBdzg-el9_xlN4XksmySWh0Bl0F7bOCeLM20jgWyAQe7aH3DDe6bQIWfUIMVkQJ5qRG5Vu5BUNia1e-UVmRLopTotic6x2iHb2T3qfKQBxetRhNxFn7aEKIR2awwLCpLcsREOLyRHt9zxAVRRFyRMm4rypZop2aV6Wd_GLSQ0H8Z_5jBOEEIrB7w3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/farahmand_alipour/4920" target="_blank">📅 10:20 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4919">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال: افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند   ‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه…</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4919" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4918">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLWYoZ9uxw_IednNWJ394QEoZvw-Z96pkqwPuOgwHXt-Q4T6Un0_ca5cnZlKxMopQ876CIgPb23tUD2_pPYVhtthixkpkFuNQUPQrxUdOtp2QopLJFIkRsVO-3m2OA2FKqrlrb5bHcEymb6lN3V_hj6mtdSIbpaZwRkp3RKfqYPHO8IqvexnfKClMjHAfN4JuYbxX0BdkEdJfnjUVKkJJgZwKJEK9O4fLfLDrHkECoX_VhNdeA0JGqepnFDlpD0Zy53Iz-MHVSh4SAFvVb5_sjSi7lQ5QStUkn5UzYufdKx0Rq_UxnXLoIpTgxhoAel_zALMDImNiLI5a0TmNkrLIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
افراد مطلع می‌گویند امارات حملات نظامی علیه ایران انجام داده است، اقدامی که این پادشاهی حاشیه خلیج فارس را به عنوان یک طرف درگیر فعال در جنگ معرفی می‌کند
‏این حملات که امارات رسماً آنها را تأیید نکرده، شامل حمله ماه آوریل به یک پالایشگاه در جزیره لاوان ایران می‌شود.
‏پژوهشگران به تصاویری اشاره کرده‌اند که ادعا می‌شود جنگنده‌های میراژ فرانسوی و پهپادهای وینگ لانگ چینی (که هر دو توسط امارات استفاده می‌شوند) را در حال عملیات در ایران نشان می‌دهد.</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/farahmand_alipour/4918" target="_blank">📅 01:03 · 22 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4917">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">در حال حاضر : جلسه ترامپ با مقامات ارشد نظامی و امنیتی آمریکا در کاخ سفید برای بررسی سناریوهای شروع دوباره جنگ با جمهوری اسلامی.
🔺
یک منبع آمریکایی به اکسویس : جنگ احتمالا قبل از شروع سفر ترامپ به چین (پنج‌شنبه این هفته) آغاز نخواهد شد.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/farahmand_alipour/4917" target="_blank">📅 23:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4916">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">‏منبع ایرانی به الجزیره:
واشنگتن در پیشنهاد خود خواستار دریافت ذخایر اورانیوم با غنای بالا (۶۰ درصد) شده است
‏واشنگتن انتقال ذخایر اورانیوم با غنای بالا به روسیه را رد کرده و کشور ثالثی را برای انتقال آن پیشنهاد داده است
‏ایران انتقال ذخایر اورانیوم خارج از خاک خود را رد کرده و آماده است تا آن را با نظارت آژانس بین‌المللی انرژی اتمی رقیق کند
‏ایران آماده است تا ذخایر اورانیوم با غنای بالا را به سطح ۳.۷ درصد و ۲۰ درصد کاهش دهد
‏واشنگتن خواستار توقف غنی‌سازی اورانیوم به مدت بیست سال شده و ایران آن را رد کرده است
‏واشنگتن پیشنهاد پرداخت جریمه به ایران بابت خسارات جنگ را رد کرده است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4916" target="_blank">📅 23:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4915">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OshTTPCwI6CILMAajeVzM4uPrYRZkTPT4DbXHsf9YwzEKAn_Ra9leSGSlUDgvd6UKkj6bDKG-b4NzMjIoJO5sb5pcN9Pcpc2Da3lFZd1nmjwWc7qWiixmpSCXO1LanP1GpbX6qJcz3R1yW8eVTi3KCqnAsg6mUtHCh_qJ6ESE22k_hBUDdxMnkkN1UL5SKQYR7UV2cQiW2SgKFyH0_Ml3Tojc050Pv2JwnGuk0K71Miy3WIrcPLJ8hSPjtis0CaIEbRMYQ9UM3X7JDFtpEGHBt98PWDsh4z8leolZaROaBwv0Ll33fcEuuUNhZLDE4ceHgeR2RgoA6KWmdC11ynp5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏قالیباف : نیروهای مسلح ما آمادهٔ پاسخگویی درس‌آموز به هر تجاوزی هستند؛ استراتژی اشتباه و تصمیم‌های اشتباه، همیشه نتیجهٔ اشتباه خواهد داشت، همهٔ دنیا قبلاً این را فهمیده‌اند.
‏ما برای تمام گزینه‌ها آماده هستیم؛ شگفت‌زده خواهند شد.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/farahmand_alipour/4915" target="_blank">📅 21:54 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4914">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">‏ترامپ می‌گوید قصد دارد در مورد فروش تسلیحات ایالات متحده به تایوان با شی جینپینگ، رئیس‌جمهور چین، گفتگو کند.
احتمالا ترامپ قصد داره غیر مستقیم به چین این پیام رو بده که دست از حمایت از ج‌ا بردار!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/4914" target="_blank">📅 20:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4913">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
‏آکسیوس به نقل از یک مقام آمریکایی: ترامپ تمایل دارد برای وادار کردن ایران به امتیازدهی در مورد برنامه هسته‌ای خود، اقدام نظامی علیه این کشور انجام دهد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/4913" target="_blank">📅 20:27 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4912">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آتش‌بس به صورت باورنکردنی ضعیف شده، در ضعیف ترین شرایط است، بعد از خواندن آن ورقهٔ آشغالی که برایمان فرستادند که حتی خواندنش را تمام نکردم.  ‏باید بگویم آتش‌بس با دستگاه تنفس (وضعیت فوق‌العاده بحرانی) نفس می‌کشد.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/4912" target="_blank">📅 20:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4911">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/farahmand_alipour/4911" target="_blank">📅 19:37 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4910">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
ترامپ : آتش‌بس با ایران در وضعیت بسیار شکننده‌ای است.</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4910" target="_blank">📅 19:17 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4909">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ترامپ به خبرنگاران: «اگر اتفاقات آن‌طور که باید پیش نرود، ممکن است دوباره به «پروژه آزادی» برگردیم. اما این بار «پروژه آزادی پلاس» خواهد بود. یعنی «پروژه آزادی» به‌علاوه چیزهای دیگر.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/farahmand_alipour/4909" target="_blank">📅 19:15 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4908">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی: « آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/farahmand_alipour/4908" target="_blank">📅 18:36 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4907">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">🚨
🚨
ترامپ با اشاره به تندروهای جمهوری اسلامی:
« آنها در نهایت عقب‌نشینی خواهند کرد… آن‌قدر با آنها برخورد خواهم کرد تا به توافق برسند.»</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/4907" target="_blank">📅 18:34 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4906">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeYzokE_Ci_krUQZPcVfG8EW53zDd9cifm0Z8p57VZCXtXjl8Uo2sG30PPJr8eRsOZa1dzxyxp-HMmsnYjmAm3nJyZB0g1qfDWwAU_4ruAnWGb8xrKmaKe_ftub9w02U6MgQJbiJ-o8yrZPGliADlrBt3BOrQh8HdVpSiAtXJrKxkVdFy96fczBrzKPgIBct7OEwqSQScHGb_RzDuzaj1bK3_YCe7q7dW9d4MN979Xpp-6bCR3KZkyb1iRQcCRXhusaYGAJgGjHHhSZHDFAiKXeymp49FuFxU8kyxGvYJq_BUGhYoQ6Bh-IYxeLQFOqtuQqXju30Cpgh8oBhQTHeqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
روزنامه «گاردین» در گزارشی از ارتباط اسحاق قالیباف، پسر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، با یک مرکز پژوهشی در دانشگاه ملبورن و سرمایه‌گذاری او در حوزه املاک در استرالیا خبر می‌دهد.
🔸
آن‌طور که در این گزارش آمده، او از طریق «اجاره دادن دست‌کم یک ملک در این کشور کسب درآمد می‌کرده است».
🔸
گاردین نوشته اسحاق قالیباف چند سال در ملبورن زندگی و تحصیل کرده و طی این مدت با بازار سرمایه‌گذاری املاک و نیز دانشگاه ملبورن ارتباط داشته است.
🔸
این روزنامه نوشته که اسحاق قالیباف، ۳۸ ساله، همچنین موفق شده بود اقامت بلندمدت استرالیا را دریافت کند؛ این در حالی است که کانادا دو بار درخواست ویزای او را رد کرده بود.
🔸
در این گزارش این پرسش مطرح شده که علیرغم اینکه قالیباف، از فرماندهان سابق سپاه پاسداران و رئیس سابق پلیس ایران بوده و به نقش خود در سرکوب و کتک‌زدن دانشجویان معترض افتخار کرده، فرزند او چطور توانسته از املاک در استرالیا درآمد دریافت کند و در این کشور اقامت موقت بگیرد.
@RadioFarda</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/farahmand_alipour/4906" target="_blank">📅 15:03 · 21 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-4905">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZMnEixGY1MhF9Mp2YjMvkRwDUQC7cxsk7NxdyQDwTUI8EI7HP3p8JLPcTthTn98Ltpb8_HdkLpqIxYLrY5QlyEpnsiuOoLJTscbOSaMU65SgsmPZ0tZE4DxXG7P_wNln8j8UI2pKmuOt7AD83RTw44DShzZTmJ4rKrARA08_QMI2VABiXcCURbRxTHeGLq8ZZjEZ4YgXxjVDwUFLiu6nwJtDeZ6drCv_-ya_f3z9HiEpbTaLgw5w7yh_uDoc6_-sWEl4F45XhG45fGB2VzJ_rfSouS_IMDRgPWxWo4udP5Jc4wbGxXK8HH9-4Rh6bXVgfTBb0mEuY3I9-R9_OJws9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هشدارها رو جدی بگیرید</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/farahmand_alipour/4905" target="_blank">📅 12:47 · 21 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
