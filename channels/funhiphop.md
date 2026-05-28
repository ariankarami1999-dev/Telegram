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
<img src="https://cdn4.telesco.pe/file/EPE49LvCbpzSSH_H9WhCeNlNkLd4VTq2mzE2MpD1lcBGk9PP9nwpg6oaIoat6scIXEg9iXfI7Am16jhUBQEsI2Rpr7XGb3q7Cr2XxC5aCTsgt8NmdZkP-cuGVEQ6iQnvFmh71QQqfS_zpcOVDtjw1lUXtbMBMpSRmuvQSZ_E7uye0shNY3-hskqTFWN7Lu_Wyu1LDZ61bcjTl9FtVnzt4AF6nN1-1SPp_5dkJnwdeKiSydE_mAAZIxvcvS41RPPQ58OKn-0rR3vBMbEuULQV6m-CeZd16mzp_fL23wZxq0KmtxnaW-T2Fi-dbhZSUBoO6AKPyWL4q3tx022t1LgOjQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 180K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-07 14:16:28</div>
<hr>

<div class="tg-post" id="msg-76162">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">کانال ۱۲ عبری:
منابع آگاه از مذاکرات خبر دادن که طی ساعات اخیر پیشرفت نسبتاً چشمگیری از لحاظ رفع اختلافات میان ایران و آمریکا صورت گرفته هرچند که چندین اختلاف همچنان بین دو طرف وجود داره.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.9K · <a href="https://t.me/funhiphop/76162" target="_blank">📅 14:06 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76161">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">بارسا که دیشب گوردونو خرید امروز هم برا آلوارز پیشنهاد رسمی فرستاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/76161" target="_blank">📅 12:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76160">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">بنازم پرزیدنت پزشکیان
جوری اینترنت رو باز کرده که آدمایی که موقع نت ملی وصل بودن الان قطع شدن
@FunHopHop
| ALI</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/76160" target="_blank">📅 12:37 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">یه لحظه یادم افتاد قبل جنگ یسری جوک ترند شده بود که میگفتن "کشورو بدین دست وی پی ان فروشا چهار ساله دارن یه قیمت می‌فروشن و گرون نکردن"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/76159" target="_blank">📅 11:56 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76157">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">صداوسیما رو باز میکنی حالت بهم میخوره، هر اوب زاده ای رو آوردن تو هرشبکه ای داره تحلیل جنگ رو میکنه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76157" target="_blank">📅 11:32 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76156">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ph-Z5Bs54_WWbRHPiIJMr5F3zZMmPIaDtYVF3D74yXndXZslqo6kKOamCdbY5ndAJJ8Q0lS1XiKy2b_BxmDrT7wMjvWF4zZSda5DDdP6Bl6JeRKTYyivElqz451Z6aQXiXhkbUPHEMHqSSoRlaUZNNQ4-l9zshEmA4UZuLM2gF28QkaZKLq8nmCTcyiQnh592_suFwQ_gGFlRQk2l19sOomyg9rSaTADhMa_bgIYwubIClNrSMtcIDkIxh9pqEN0jLFMHkJwNBLwC0u2TeB4S8yD2ZwDGM0AfnNJJNevF75sJjGvKb_4WMz3Ug4LGCIBHMMBbmb14dN_3_v5SboLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حکایت وصل شدن اینترنت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/76156" target="_blank">📅 11:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76155">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F82gFkbVe_099bZ2wR0ivaMPB7OQDMmJGKhrqt4KIu2TGPUDgqyxriqZrZSwLv0MX_q4R7rh-iYOFlW1xQMnuyYN_hM5UabaUlO3F5wJG-6_FIrVBJQ3WoWaM3b1YgQWr8I3otLoThl4eLZrY2x6u-w9psBTe7NAIqKt1G76OQyuguNv6I84kJNYAFZ21OWtkOMiPbYaFXPytUlDyg4fsOVXsftEUWMhL4-Lk4vACXc3lClgTvJDRyR4AJrnyHkjI55eXooXqeI4P6ISbLmbXq8gMqDNAEyVen9oBKmGUe9YLcnOQ7dLniWGQjUyDNM7xnIPt8h3zaEyzWAFdKKjwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امسال عجب کیتای شاهکاری داریم.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/76155" target="_blank">📅 10:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76154">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بامداد امروز بعد از شلیک موشک از امیدیه خوزستان به سمت کویت ، صدای انفجار شنیده شده و ستون دود دیده شده که ظاهراً لانچری که موشک ازش شلیک شده بلافاصله توسط ارتش آمریکا مورد هدف قرار گرفته
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/76154" target="_blank">📅 10:47 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76152">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mcQqGChJ8r96wfeE4nC94soSDnTSwFWVzbd3b5JoJOZgjuFDnYGUGQKeBR31dLguyxdQAvKNVja0GH-Wb0Eg-ua_WMJzpRUsjnOES7Fhs3W3-b5w9o6Rlb3rUDWg2DKk6RuqsMM4sLzZrMWpGGv9LFVC4JCr1i26JgbncAvakG9QHMH_Sm23WMJ1GDNg6AcXyqShpenbSv3Sz_LEUyGht_gjzcyg49NoqF322-ovUN10MIN-WeFqhhys5dIgdvtbstexi5yQTV5HJfPg2mceG_hBitQ60pVk8oQh9G_DP9B4MZ0N5gO3e_CIYm3lTQTa6Ab6h5PjCSCC7DncmBsD-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RVAC8ulVQV9gVIFp9QmIU25lA1ajHFA-iczCqjpMTeAbxtztdeNsizj66EndD7WfYUHbC-WNFwYICQpkg_qbYu2DxuJwM-xGDs-CdacR2h5teHU9qZAjfmLzBHlhgJe2VtIB_6qNXVoK3xxANcB1TPf6EDkz-62jK473rPNFyai5ngWRkPzDHJvEHSdRtgf2mdcUD4X0t72dt1MZalqo3o-2HVC-A-e2ivawRlJP_Utvp5mJTiqAVfxVR5-lV6XoNtSlEyx5vIS_fgEuJCluKQJ5AHZvlovXfVnJG0lqM9cDTrOUz5todU2j5u01JGYoqdcJ-lQuWndQmY86XObKVw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از سایز پات معلومه اوب داری پسرجان.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76152" target="_blank">📅 10:38 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76151">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knwaNJBdcZB6YeMF2iiiwYaNmCwCgTT8sF7BPeiv8pAmxPx8MUI0JeIseH5_JrvykHLGGzkCl5MkWnCwu9uvEVWMBzgfXegfIJtWf9OKbLQ5Cy_wV3ZC7-20B-twW67kDFOveO4OdtEOpjSItEmtmmPHgSEuFjxnqDJoaT24pNwElb2ODPwu-Z6KhSEbiLb3C0Wl1uRT3xLrM_RJCCKs7C4OKdKmgLRfHn3NzpVEom_g2fwULqD-Jo7uGReAngCJFCKoLioPGI7uaCkye2mvI0lPCD8JftwNUGkFDRDyAKTM3f_iQ4valsjFQGLeEhCdLHc29-6h2PHw_ZoEODCcUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این توییت هیچوقت قدیمی نمیشه.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/76151" target="_blank">📅 10:29 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76150">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QtRbpfpO9sWhSnP1tw8L09zLi0GmB1MDgfQfi-6HY5Mb1ms0nY4Cg4wIinRqEIiCABoQ-5suB3WBY3jmRODxWligbCIQjNDA3sFMtjEUdZqJpbp3Gq_SlrRLW6TH4k0B4Aixo5xscwWHuEkNVCCgnJbGRS8jhQi8ydfwPEloaNvvdY4vUwqGiCxhlWuCY5vbvHTCERfVUNy3GAWKMYqD3KDge_yAV5azwmCFyVjo3iL_8y1FZJUxFIHVVOIbXXmvm3Z8uFdT6fpY2WR1lUbi8RZAOe1d1UBkTz640k9cNDF0fPuar33w5AsZJJiHhaQsmSCtKYTUybMLcI_9CIAtow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیمی نام ببرید که توان مقابله با این طوفان را داشته باشد.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/76150" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76149">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76149" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76149" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76148">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bm_9LHUfLFRsTnF1vijU-Rf9PQgYp0TDE9ZKOOO5x5zYV6P_17y49qlDmC0TxL49b4P7b6S5vC3HqZFHPFZIji70CzwxXlvCn8En8GcVRuoDU9lC12e08vurUxT4sx-fNR-aoFbSXdpir8bdk9ckU87xAB6dJrnp36T8rbB6wEjidIXkCxD2HxlSJK0MCVMj97wDUt44RMGdfnLaT22-fHX3G8p2JDPZLWZtuz-YM7pDOFtaappH74a-TgjsFdX3hcRaU4yLKz5WZlKsrnqxv5bY_bO5BDzluZeW9JjUJZ38ieBwi6ul-yLyeN0QpwuiDN7q6R4A-IBU8y9r0BQTLQ.jpg" alt="photo" loading="lazy"/></div>
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
r7
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76148" target="_blank">📅 10:24 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76147">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPUgTj_yL29KQFlK4jeMcCUOKEvgFPTni3RcZtP-ihN3ZtVnLibjus6PwroIxlpV4Zuamn24h3WUAcwK0Cmg5K5ZvdZqzkpQKHUVSEvjx6z86zh8JrVeai8dDSVMfrwEi2-Ylc57W_8dAjCiq16NXbiotlyQDNRqdTdhbP-DhsKw3w0ZyYHgcz7qdzgNq11q5rMq2QD6Ya0EDbt7lGtY2KWoo6x0SQ2RsTIny5Ufxlzn4hWh9y6TZXNo8hl1LuTaee306pXY_KpujJMRoQVeepgBrd7CIARyN1aJarDX4acfNFJvBiBvV3mVEzc3D8jICO52iP4QUmWGCbTygNN1bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با شرف
🇮🇷
🙏🏼
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/76147" target="_blank">📅 10:09 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76146">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=N4S5qcbOmVsRItwKRolwgnFXa491GYLCN8gltb54dvz7WknooJKOPCgEjlFqAyrxyUlPQxAMO-Qg8_LoQmMoXDXydJgYTMMk4Qy4BDdY3b8R0CV3ADEnUbyYVdgxtHJEMiMljVkW7DnsPRN-25veFXrybr5yquAhwYxdOSg8krgkZI-0yhmSYP6u4b8FbB4Z3HTE9HagcnN1BK0oPnoJTnshOVMd1vAb5mvppQN3UB9OWF74531SVCPXm0tOjMc7CAncUqvkOxZ4qoTJjuqBuTHv5tCACmkjaRHiatrsYNqhvwNdHu2oMkBrLCub-P1tjmcAC_IHG1_r0A6LlFlYpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=N4S5qcbOmVsRItwKRolwgnFXa491GYLCN8gltb54dvz7WknooJKOPCgEjlFqAyrxyUlPQxAMO-Qg8_LoQmMoXDXydJgYTMMk4Qy4BDdY3b8R0CV3ADEnUbyYVdgxtHJEMiMljVkW7DnsPRN-25veFXrybr5yquAhwYxdOSg8krgkZI-0yhmSYP6u4b8FbB4Z3HTE9HagcnN1BK0oPnoJTnshOVMd1vAb5mvppQN3UB9OWF74531SVCPXm0tOjMc7CAncUqvkOxZ4qoTJjuqBuTHv5tCACmkjaRHiatrsYNqhvwNdHu2oMkBrLCub-P1tjmcAC_IHG1_r0A6LlFlYpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه که توش حرفی از نقض شدن آتش‌بس نزد:
بسم الله القاسم الجبارین
فمن اعتدی علیکم فاعتدوا علیه بمثل ما اعتدی علیکم
به دنبال تعرض سحرگاه امروز ارتش متجاوز آمریکا به نقطه ای در حاشیه فرودگاه بندر عباس با پرتابه های هوایی (گفته می‌شه تلاش برای ترور یک مقام بلند پایه تو ماشینش بوده)، پایگاه هوایی آمریکایی مبدا تجاوز، در ساعت ۴/۵۰ دقیقه هدف قرار گرفت.
این پاسخ یک اخطار جدی است تا دشمن بداند، تجاوز بدون پاسخ نخواهد ماند و در صورت تکرار، پاسخ ما قاطع تر خواهد بود.
مسئولیت عواقب آن با متجاوز است.
و ما النصر الا من عندالله العزیز الحکیم
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76146" target="_blank">📅 06:49 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76145">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فان‌هیپ‌هاپ نیوز:
بازکردن اینترنت نشون دهنده پایان جنگ نیست/ تقی به توقی بخوره باز قراره ببندن و همین الانشم درست حسابی باز نشده. وآماده قطع کردنش هستن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/76145" target="_blank">📅 06:10 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76144">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/76144" target="_blank">📅 06:03 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76143">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JmsBqz5o0567dOrFcyzzs-JhdLK5VFN__-tk8pFT3nfn-Hr_LOa6ADGvUSbzK6pAh2mxG-hF7renR_SC1nLGdG7ANzCqiKvLTXHq1zLeT4cYMF_vx49sePRZBIYOxuRh6uWCC8SamBHzhjxFHxSS17WiivjoiXb_3--ewXVdRU0fbHmzwzV8r2BKS2ll8lt_cgh6pnkpcHKEO0CTqAkHu1kgMm-_UiQIG-SmM5p8f83T8054yeHJXxqlmLN6XPJcmL2jCWmN_99f2ja_1Rh_Y9DAqykHLvUQ8iMECXJStrfZH-S5M05as_OqTNeE-NfqDcyjGVAo-gJqlRNiEa44dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمی‌دونم چرا و چطوری ولی همین الان آژیرهای خطر حمله‌ی هوایی تو کویت روشن شدن.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76143" target="_blank">📅 05:55 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76142">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">اشتباه برداشت نکنید، قطر داره پولارو با جنگنده جابجا میکنه</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76142" target="_blank">📅 03:27 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">به گزارش رویترز، ارتش ایالات متحده حملات جدیدی را به یک پایگاه نظامی ایرانی که تهدیدی برای نیروهای آمریکایی و کشتی‌های تجاری در تنگه هرمز بود، انجام داد.
ارتش آمریکا همچنین در جریان این حملات چندین پهپاد ایرانی را رهگیری و سرنگون کرد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76141" target="_blank">📅 02:57 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76140" target="_blank">📅 02:28 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromYashar</strong></div>
<div class="tg-text">کانفیگ فروشان با پول کانفیگاb2 خریدن میخوان نتو قطع کنن</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/76139" target="_blank">📅 02:18 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فارس: سه انفجار در بندرعباس
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76138" target="_blank">📅 02:16 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76135">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">سلام فرید جان بندرعباس صدای انفجار میاد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76135" target="_blank">📅 01:44 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76134">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t399RRoINs1aNieeaX9iuEi8ErPXNS5v2hJjGhbPGbZTL9l4f0fNZuELh1BsdVtLd0o8-BiduhJCikrBEhat3o9exsmY2MsCnHRZs-kN78YceCbSQjYRyU6RPmXG980HwAMILrutrskx04BLvaWWLw58UHS7HbYMaKZ6umidalHWRE15YSvFrVyoKP6MqWq41XakdR8Nk0TeWsSxdsLKDY_gSTiBQKVAec-Ml83VcL96g7RcwK311FLehUtbeClyPpfyyySd8yDYPieO1GOjdHCq0glNZ_7mcIEymVxIrPi46pMIDv0fdFwcAV7bjwKvALJ2BDrJ0XmLEdzqhdm_GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور ابراهیم عزیزی، رئیس کمیسیون امنیت ملی مجلس:
ایران با سخنان تهدیدآمیز ترامپ از خطوط قرمز خود عقب‌نشینی نخواهد کرد:
حق غنی‌سازی اورانیوم، مالکیت اورانیوم غنی‌شده، اختیار بر تنگه هرمز و رفع تحریم‌ها.
واضح است که ترامپ، در جستجوی راهی برای خروج از این بن‌بست استراتژیک، بین صدور تهدید و درخواست توافق در نوسان است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76134" target="_blank">📅 00:42 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76133">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">گوگل پلی مثکه رفع فیلتر شده
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76133" target="_blank">📅 00:01 · 07 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76131">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">این مشکل سامسونگ که بعد چند ساعت استفاده از تلگرام تلگرام هنگ می‌کنه رو شمام دارید؟</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76131" target="_blank">📅 23:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76130">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzRPaxi0W8UTzRJu8A1d9RmaxYK775U-91Il-u0dxpTXh94ZueLdEa4M8gvSBP26Gc3b1WBwpTRUdk1rj6nD4DelfyRHj1s4Zx0C3fm0bQj-Dx7wNe6FaZJaOxyBFDmOYMx7IA1jdZ08dehAVNSG-UVEmoHGaEgRxD4T5ttY2eKRY8nNn0uY8CxwNZHHkzYpzqQ2yO7zUBRxabe4Svy_TkX_5M79jjKEk34EZFrTA_ALqzWR4RWv3xDfY_TgQGFBD6KB-L6GJtRM5KHtUFDjw_I3oVq9XlDjVSzK_dkO47naCjGyY24GbAdCBKTcnQSc7JN0d62YZCOUmLg1LMVKbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton = $1.904
💶
327,221 toman
💰
درصد تغییرات: 5.98%
🔴
مقدار ضرر: 0.113859 $ / 19,568 toman  1405/03/06 | 23:41:05   @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76130" target="_blank">📅 23:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76129">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a3Odv7lZTbacOsX5fIUM61NjEJfrqAqd06NRDU69oVCQsnE35x7zRncVtUd5sVI9jIucEq7zz1bX_a6AQglh1jCAbEj2EI1-jvGqAZguaurz3ozd0X88ErfEWPHAn1YsE4Bu5Xiyne-Oc-5CmEDPbKL0upC2peBe7dzrLeTMYDX_YB2v0YBOzsRO9qXfQJ2AJSMyVtbtRPioyidEzGV3jFeYvwyG0IMkwPGgRtkzFlCg25-If5TwjmjKtYNji1Dfgi4ICZfnjKECV5r3itoHK33K3ja6Eh09qRYVl6SaYhHmstlF0fptHtXlJjsxe2t6TSOnAh-KtLvDBsPenAOErw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💎
1.00 ton
= $1.904
💶
327,221
toman
💰
درصد تغییرات
: 5.98%
🔴
مقدار ضرر
: 0.113859
$
/ 19,568
toman
1405/03/06 | 23:41:05
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76129" target="_blank">📅 23:41 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76128">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">سخنگوی ارتش اسرائیل:
ارتش اسرائیل دقایقی پیش دو تروریست ارشد سازمان حماس را در شمال نوار غزه هدف قرار داد، جزئیات بیشتر بعداً اعلام خواهد شد.
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/76128" target="_blank">📅 23:24 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76127">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اسرائیل هیوم:
ترامپ پیش‌نویس یادداشت تفاهم با ایران را به نتانیاهو و رهبران منطقه تحویل داد تا نظرات خود را اعلام کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/76127" target="_blank">📅 22:17 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76126">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eaXfbO9qSuqlguXu-qYE0JioD96hkM5cB7ysZt9tK7EpaG6A5F_CblgFFgtu7suVFVqXktprS-zjbRaiQq0OG3rxA2FPyo195WaKWPCigvqwTFdhXtUV13vqolo9osBkeoLRjjD71cCmP2pr-7wYszLBoyaOls8F7U1_eYPGDX0RcqBhu4UqinH76o36f9tq1K94PGbbDwKt2ahcD1woMljo7RfuJzHIJy9QwQrmUAh2wtewmBYUqIv1Q-SoXxVxA_ssJqSSH0WouyRTDPbVWvUj8VVkMJOiNwalOn-SqbcSZjvVEYFVZGvnnWLrAsX1ViSTRj4ccZSQpx60RhDlwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76126" target="_blank">📅 22:06 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">اسرائیل همچنان داره لبنانو میکوبه
@FunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/76125" target="_blank">📅 21:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">نکنه رئیس باند فروش کانفیگ ایران لاپورتا بوده</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76124" target="_blank">📅 21:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76123">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ:
عربستان و سایر کشورهای عربی به ما بدهکارند، اگر آنها به پیمان ابراهیم (عادی سازی روابط با اسرائیل) نپیوندند، من فکر نمی‌کنم اصلا مذاکره و توافق صلحی با ایران انجام بدهم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/76123" target="_blank">📅 21:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">با تایید رومانو آنتونی گوردون به بارسلونا پیوست تا درصد اوب بازیکناش از میانگین ۹۰ درصد به ۹۵ درصد برسه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76122" target="_blank">📅 20:54 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترامفض:
این کاملا رژیم چنج است. ما یک رژیم را از بین بردیم، سپس رژیم دیگری را هم از بین بردیم، و ما الان درحال مذاکره با رژیم سوم هستیم و خواهیم دید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76121" target="_blank">📅 20:52 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترامپ:
به خدا من می‌خواستم بزنم ولی فقط به خاطر روی گل عاصم منیر که خیلی دوستش دارم و درخواستی که کرد به ایران یه فرصت دیگه دادم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76120" target="_blank">📅 20:45 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db6012f650.mp4?token=YmDOCYoGmWN-1zq62Vk6bbNjjAVpKaV2U_VMN6IHslHdO4kloHltw8zAsdxi7x5P9MSnfFvskuFX0ygXQrPkSsyXSrIadg9gxdZcYhq87e5DAy7P6RN2FyFF_l4SYN8HQcTszKk-yy-5LoukN448jiqB486u4DTLrz7ZdUglZqrqmpGyqN2Dzus2ZXXik1SJbyh3UkAeMtcK00mDb5b7eqLlfV8q9jyHTXRkdZSOi-sJbXE1KbC9KLUdWETXEhMFvKVE7Aj-afYHKI2mti-7PQMZKbGwROFczQY5lF3-aEBUMzcyt7hYS_YVklj9i-frPue71c-PB3L7ZwWVHN5PUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db6012f650.mp4?token=YmDOCYoGmWN-1zq62Vk6bbNjjAVpKaV2U_VMN6IHslHdO4kloHltw8zAsdxi7x5P9MSnfFvskuFX0ygXQrPkSsyXSrIadg9gxdZcYhq87e5DAy7P6RN2FyFF_l4SYN8HQcTszKk-yy-5LoukN448jiqB486u4DTLrz7ZdUglZqrqmpGyqN2Dzus2ZXXik1SJbyh3UkAeMtcK00mDb5b7eqLlfV8q9jyHTXRkdZSOi-sJbXE1KbC9KLUdWETXEhMFvKVE7Aj-afYHKI2mti-7PQMZKbGwROFczQY5lF3-aEBUMzcyt7hYS_YVklj9i-frPue71c-PB3L7ZwWVHN5PUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ما اکنون درباره هیچ گونه کاهش تحریم‌ها یا پرداخت پولی صحبت نمی‌کنیم.
ما کنترل پولی را که آنها ادعا می‌کنند مال خودشان است، در دست داریم. ما کنترل آن پول را حفظ خواهیم کرد.
وقتی آنها به درستی رفتار کنند و کار درست را انجام دهند، اجازه خواهیم داد پولشان را داشته باشند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76119" target="_blank">📅 20:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ترامپ درباره ایران:
آنها شروع به دادن چیزهایی که باید به ما بدهند کرده‌اند. اگر این کار را بکنند، عالی است.
اگر ایکار را نکنند، هگست (وزیر جنگ) ادامه مذاکرات با آنها را برعهده خواهد گرفت و کار را تمام خواهد کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/funhiphop/76118" target="_blank">📅 20:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=Md_TmMSK6kfEB5wa4Ag-hbL9lNyxBSqymTOLnJK5wuZH5UEo1Tjt-djTJEtdo2pX8BbOhAr9xQH1IGDp7hkIwnfltT3UqwvqvQttYkb6vdBwj6YmFmCPn1PBfDBGGPrnIAVDl3wZsVZYEhOQpkcYwIouDASlRqbFONH0RtBvC7DSPlEqfytJk0_1GIkO3zXzpb9ZiWo1qMSfHVbPh1XKXxqky8lvFex1ZKjke8E_OjRWuFxWrP9mFDWbX3giPahQ4POhpSRql4SNPgcd91Mx9KfREalr_REcwPapEdAYbPiXc-mJJMsOmTopSH15fkk15XOPs4iCxKMdrMYVf7hdpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6a042bbf.mp4?token=Md_TmMSK6kfEB5wa4Ag-hbL9lNyxBSqymTOLnJK5wuZH5UEo1Tjt-djTJEtdo2pX8BbOhAr9xQH1IGDp7hkIwnfltT3UqwvqvQttYkb6vdBwj6YmFmCPn1PBfDBGGPrnIAVDl3wZsVZYEhOQpkcYwIouDASlRqbFONH0RtBvC7DSPlEqfytJk0_1GIkO3zXzpb9ZiWo1qMSfHVbPh1XKXxqky8lvFex1ZKjke8E_OjRWuFxWrP9mFDWbX3giPahQ4POhpSRql4SNPgcd91Mx9KfREalr_REcwPapEdAYbPiXc-mJJMsOmTopSH15fkk15XOPs4iCxKMdrMYVf7hdpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
آیا از این موضوع راضی خواهید بود که روسیه یا چین اورانیوم غنی‌شده ایران را بگیرند؟
ترامپ:
نه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76117" target="_blank">📅 20:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درمورد خبر صدا سیما مبنی بر اینکه تو پیش‌نویس توافق گفته شده تنگه توسط ایران و عمان کنترل خواهد شد:
تنگه‌ برای همه باز خواهد بود و
تحت کنترل هیچ‌کس نخواهند بود صرف نظر اینکه ایران چه می‌گوید؛ ما مراقب آن‌ها خواهیم بود.
عمان هم باید مثل همه رفتار کند و اینکار را نکند، وگرنه مجبوریم آن‌ها را منفجر کنیم.
🙏
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/76116" target="_blank">📅 20:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cFBkXEotl0YH6hptQP21GK8AcqsTS_TcTi6t3-GADX4Vsl_LTAU36Erf0bq1QWhrhKRFlAuPR6PZ9MmU0TDrSgx1w0FJ2O0aoSQn9TINl3-OhQc3iRJIQDhsrdaR-_mHui0PFIusyd5GMDHJm2EVfa3kTX80W9AHqZhyPnzzIG40_r_kiI58xbnaGAEQZv1mihxH8WE8lTFyUPvRqDSSq4vPGXMXsRxIV6OyD6NnTAsH7UPwHBnDZjEGmlPm6qUeUxQebBWAkcSZOffwgyNCu-FNbYPluBt5YXeCBycyLCSngspV6y26hthA_lozmxGf9wFGKyJ-hxRpYqKQV2t8GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/76115" target="_blank">📅 20:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=ZfsYBnH84RFzusGgKFN1bkV71zuCep9Wjk7ul6y2oAAcPBVpwENg8o5t3zX8c2dxnC27UzdyJ3ESrbuTFzqGfJ1bZJWvXZx476UNkzyobV0B0u8UWe5PRCm0v_Uk3BTjbBRXYCjWVVf9sBwhU0K4w44fGqvfqAeJGpfr-LoWMrcXZ-vSsqgZ16GHcj8OnYUTOkN-Y3r8XY_7l9Y9B6-hvO9qkV3USsqUu5iWyMmGsYOaEhJJ046IND9RPgRNuBfAlE2pY2BMrREAe_C0rjqw0c3hc6653lIb4Nr3KUtbQLaEiC7-Q81UZkjjqu7GspmV8h5lVudo2Ywa7uLbWGQZ0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c4635a829.mp4?token=ZfsYBnH84RFzusGgKFN1bkV71zuCep9Wjk7ul6y2oAAcPBVpwENg8o5t3zX8c2dxnC27UzdyJ3ESrbuTFzqGfJ1bZJWvXZx476UNkzyobV0B0u8UWe5PRCm0v_Uk3BTjbBRXYCjWVVf9sBwhU0K4w44fGqvfqAeJGpfr-LoWMrcXZ-vSsqgZ16GHcj8OnYUTOkN-Y3r8XY_7l9Y9B6-hvO9qkV3USsqUu5iWyMmGsYOaEhJJ046IND9RPgRNuBfAlE2pY2BMrREAe_C0rjqw0c3hc6653lIb4Nr3KUtbQLaEiC7-Q81UZkjjqu7GspmV8h5lVudo2Ywa7uLbWGQZ0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته   @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76114" target="_blank">📅 20:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">خبرگزاری مهر:
آتش‌سوزی در یک ساختمان اداری در فرودگاه بین‌المللی امام خمینی در نزدیکی تهران، پایتخت ایران، رخ داده است.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/76113" target="_blank">📅 20:05 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">مارکو روبیو:
دیپلماسی گزینه اول ماست اما گزینه‌های دیگری هم درمورد ایران وجود دارد.
ما معتقدیم که پیشرفتی در جهت رسیدن به توافق با ایران حاصل شده و در روزهای آینده خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76112" target="_blank">📅 19:57 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=NG4QNn0nYlAcW_jU8Aqsi7nqOGAmOWXrk4hMWof3lj7NPjIo4UJddD0YsBXy6xHCdurC0v2dZes5nExMoqQuhfDkKlkslUmGlFYCfRXL50vavUT7QwsCDoXv7nuM5YDw8okw68U74cA5spBDEivCySUQU_7rv0V3UcagcPky-zRy_IoJ5Lm7pSD8_f5-pHjt9wFK03d7B3QrOdcFpBjyUMyJxHC-z_ojqdOn8vmPZExjAt4zn0sdq8sGpxpFV-NMat8kayJ4fFZBe8NtCbz9940-D9wro8g-K3An_i7MbXZYSVcfsJ0mEQqLFbgpfP5pdFycEg12xUsaEaI29soD0g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afe37ba190.mp4?token=NG4QNn0nYlAcW_jU8Aqsi7nqOGAmOWXrk4hMWof3lj7NPjIo4UJddD0YsBXy6xHCdurC0v2dZes5nExMoqQuhfDkKlkslUmGlFYCfRXL50vavUT7QwsCDoXv7nuM5YDw8okw68U74cA5spBDEivCySUQU_7rv0V3UcagcPky-zRy_IoJ5Lm7pSD8_f5-pHjt9wFK03d7B3QrOdcFpBjyUMyJxHC-z_ojqdOn8vmPZExjAt4zn0sdq8sGpxpFV-NMat8kayJ4fFZBe8NtCbz9940-D9wro8g-K3An_i7MbXZYSVcfsJ0mEQqLFbgpfP5pdFycEg12xUsaEaI29soD0g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نه داداش ببین طرف خیلی باهوشه حواسش جمعه به خدا داره شطرنج ۱۶ بعدی بازی می‌کنه:
با وجود درگیری با
ونزوئلا
، کشوری که دیگر نیروی دریایی ندارد، دیگر نیروی هوایی ندارد، دیگر افراد زیادی که کشور را به سمت مکان‌های بسیار بد هدایت می‌کردند را ندارد و رهبری آن از بین رفته است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76111" target="_blank">📅 19:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=rwkurkAe5uDC4mdEHgZdVNN7XNTAxEnmb7oW5wIR64t2VlEns3cluYwHx9--LHnFLP3KQQtbtzkIJUyP3DyIOyH2bfOaLeL-gKTNbekrxblQRVJyxr8wSW545aLNnRoOEztsfX-N2Mk2kFJzFS23qz6nOX9KxTbwjc-LRYcAuz1zEzpZt0JisgEx_z7BVh0Rymt0Ycawy0iRtrOzaK87jA1TU6jCeWqjI82t1NYC0_is8yHxPk0UZrVnZQzLxrlIRTMWI4KZHxkKepgT5qiwrh2RYnNQPFvGXFvGn6s_6MemC5K3IUujv_6FdnD7e1b8k9Ua34y1ldtsuR0bvEkBHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4df9e7ea0.mp4?token=rwkurkAe5uDC4mdEHgZdVNN7XNTAxEnmb7oW5wIR64t2VlEns3cluYwHx9--LHnFLP3KQQtbtzkIJUyP3DyIOyH2bfOaLeL-gKTNbekrxblQRVJyxr8wSW545aLNnRoOEztsfX-N2Mk2kFJzFS23qz6nOX9KxTbwjc-LRYcAuz1zEzpZt0JisgEx_z7BVh0Rymt0Ycawy0iRtrOzaK87jA1TU6jCeWqjI82t1NYC0_is8yHxPk0UZrVnZQzLxrlIRTMWI4KZHxkKepgT5qiwrh2RYnNQPFvGXFvGn6s_6MemC5K3IUujv_6FdnD7e1b8k9Ua34y1ldtsuR0bvEkBHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
ایران بسیار مصمم است. آنها بسیار مایل به انجام یک توافق هستند.
تا کنون به آن نرسیده‌اند. ما از این موضوع راضی نیستیم، اما یا راضی خواهیم شد، یا اینکه باید کار را تمام کنیم.
آنها در حال مذاکره با توان کم هستند. شاید مجبور شویم برگردیم و کار را تمام کنیم؛ شاید هم نه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/76110" target="_blank">📅 19:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76108">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">⚠️
پیشنهاد استثنایی به مناسبت باز شدن اینترنت ، زیر قیمت کل ایران
🛍
🚀
100 گیگ پر سرعت +ساب
1,000,000
🚀
80 گیگ پرسرعت + ساب
800,000
🚀
50 گیگ پر سرعت + ساب
550,000
بدون محدودیت تایم و محدودیت کاربر
⏰
🔴
بدون قطعی و افت سرعت
🟡
بدون ضریب
🥇
پشتیبانی واقعی ۲۴ ساعته
💸
ضمانت عودت وجه
❗️
این قیمت تکرار نمیشه، از
دستش نده
ثبت سفارش
👇
:
🎙
@Mohammad_vpn2</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76108" target="_blank">📅 19:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76107">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یکی از منابع فان هیپ هاپ تو نظام امریکا
‏آمریکا به هواپیماهای مستقر در اسرائیل دستور داد ظرف ۷۲ ساعت به پایگاه‌های خود در اروپا بازگردند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/76107" target="_blank">📅 19:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76106">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترامپ کاملا از حیطه منطق و عقل خارج شد و به PBS گفت:
ایران در ازای خارج کردم اورانیوم غنی شده خود هم رفع تحریمی دریافت نخواهد کرد و به طور مستقیم اظهار داشت: «آنها اورانیوم غنی شده‌ی خود را کنار خواهند گذاشت اما نه، نه، اصلاً. هیچ تسهیلات تحریمی‌ای درکار نخواهد بود، نه.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76106" target="_blank">📅 19:22 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76105">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">بمببببب فارس:
ا
حتمال اعلام یک‌طرفه نهایی‌شدن توافق توسط ترامپ برای فشار به ایران
منابع آگاه می‌گویند دونالد ترامپ، رئیس‌جمهور آمریکا، احتمال دارد طی ساعات آینده به صورت یک‌طرفه اعلام کند که توافق ایران و آمریکا نهایی شده است.
این اقدام از سوی ترامپ با هدف اعمال فشار و القای توافق به افکار عمومی، پیش از رفع کامل اختلافات، ارزیابی می‌شود.
بااین حال، یک عضو تیم مذاکره‌کننده ایرانی در گفت‌وگو با فارس تأکید کرده که هنوز برخی موارد حل نشده باقی مانده و تا زمانی که همه موضوعات مدنظر ایران حل نشود، هیچ توافقی در کار نخواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/76105" target="_blank">📅 19:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76104">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">علیرضا جی جی مصاحبه کرده گفته پشمام ریخته که جوونا هنوز ابی و داریوش گوش میکنن چون ریتم آهنگاشون خیلی چرته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76104" target="_blank">📅 19:03 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76103">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بارسا تو ۲۴ ساعت گوردونو خرید، بعد میگن پول نداره</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76103" target="_blank">📅 18:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76102">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uI4azrH5FbLMWNGWitY4LEuj-wCwubM2Mn-jJN70iAa9g1hiMxF_qQfJcZ5TuiEeHHGg9Fe0XvnEsy3qoOYkaOVfQQMnPFcGflYsy_cPHcDHcVdaRAvJXKGdRKzbZIWs_lCBH2TjaawiJr9oS8denxehF8IuLUHrnoxVTBYABAc1wkh6LCNh8fV2kYt0SJ38VZMkObrzBlMhWT59Y1tRMa32dyjsn3M4eYE6T68kqS2FTipcEvSeGluUDcCkUH_-DNv2I3QcJUG7MocAZwewFidj59GvQ7P316QrY2Ibe17Tijaao7qYAo7xMn4VyLspkNJnGWLY1WsbP9vlU9-pNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاخ سفید درمورد گزارش صدا و سیما از پیش نویس توافق ایران و آمریکا گفت کاملا ساختگیه و در ادامه هم تاکید کرد: «هیچ‌کس نباید آنچه را که رسانه‌های دولتی ایران منتشر می‌کنند باور کند.»
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/76102" target="_blank">📅 18:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76101">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MichkVGbAdoJZDMeBvvLQ0z-5gmy1VEyyKB4tK05O3Tc6chUuA8kp73R3G_CuVwRygWXoXuwLuhpL1GP13ysPVc8oUmW9x3W4mMPJe1xDFHMTOz4WdWxI-t5GbgGsEuSvA_CyLc7XkxrLQRu5xbY113O6MaICetnHRw5n7fzFUojbt8-B_OAfEoBzPKOWhWskygafMKxyLQ41a75Lljc4IoU0mmQbIVfNiRw3xyexWX5ustNw161uahQPneJDezYO9G0wZEJqhNSeDY4CpeAB26Nd89E6bDZcT62l2oXC1ntXZlN9iFbGjOMR4OX995i5c8d0baqClxOWexIum5gkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها ترامپ فکر می‌کنه خیلی بامزه‌ست، لطفا بهش بخندید کیر نشه.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76101" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76100">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hLQSc198xbLnBCzZDakOsJfeov0wGbXm__buTMlaGUELPv7gxw2vKnXjD_CdEtnqyYPo9asYbo12_HzQgEazWv7nkhEXu46NRCiKxT9B-Qo3eZVgbafkl8kYD4EmIRTrmGeWXZWqVlWvqs7wAhbm0mzBdsIEuYUcQKWoLAhtxD4ty_fIgddQ0O4l9WePh-oszAjTidjdfsom_P0ekfpk4Bn0s6k7yqp2TvcS7JO1fDbHQmZzNGv16vF5WThEZpwjyb_2u4yAk9fmgfNw8i8GWjOjgVZ6aUxOzoRwEU2eX8olgTl2OaBGxhhwOaD86UmYumjiZpmLvbej-8FFQjtJLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✖️
سایت بین المللی
bet120x
✖️
👍
دارای مجوز رسمی Gambling Judge سوئد
👍
💳
شارژ حساب از طریق ارز و
یووچر
و پرمیوم ووچر
💳
تسویه حساب دلاری سریع
💊
بیمه شرط میکس
⚠️
فروش شرط
🔔
ویرایش شرط
3️⃣
2️⃣
🎁
20%هدیه واریز از طریق ارز و ووچر
┅━━━━━━━━━━━
🎁
10%برگشت باخت به صورت روزانه
🎁
10%برگشت باخت به صورت هفتگی
🎁
10%برگشت باخت به صورت ماهانه
💻
ادرس ورود به سایت:
https://bet120x.com/fa/?btag=971470
➖
➖
➖
➖
➖
👈
آموزش واریز و برداشت دلاری
👉
🔪
کانال اطلاع رسانی:
👇
g6
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76100" target="_blank">📅 18:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76098">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ظاهرا به تیم ملی جمهوری اسلامی اعلام شده که اجازه اقامت تو آمریکا رو نداره و بعد هر بازی باید بره مکزیک  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76098" target="_blank">📅 17:53 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اکبرزاده: دیگه فکر نکنم دشمن جرات داشته باشه حمله کنه.
پ.ن: یادش بخیر دو سال پیش جلیلی و ثابتی هم میگفتن اگه اورانیوم ۶۰درصدو بدیم به آمریکا بهمون حمله میکنه، چون الان اورانیوما بازدارندس جرات نمیکنن حمله کنن، اونا هم عمه های من بودن تو ۹ ماه دو بار به ایران حمله کردن و تو عمق ایران همه رو ترور کردن کسی کیرشونم نتونست بخوره
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76097" target="_blank">📅 17:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76095">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال 12 اسرائیل:
انتظار می‌رود هواپیماهای نظامی آمریکایی در صورت امضای توافق با ایران، ظرف ۷۲ ساعت  اسرائیل را ترک کنند و به پایگاه‌های اروپایی منتقل شوند.
هواپیماهای سوخت‌رسان نیروی هوایی آمریکا در صورت از سرگیری درگیری با ایران به فرودگاه بن گوریون بازخواهند گشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/76095" target="_blank">📅 17:20 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76094">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ظاهرا به تیم ملی جمهوری اسلامی اعلام شده که اجازه اقامت تو آمریکا رو نداره و بعد هر بازی باید بره مکزیک
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76094" target="_blank">📅 17:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76089">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJOzgO5UZrsUHwAFqtTPRmxdyKDGeHdbQhOBYT7pB0D6Xux2TyDMNIXxWmQq_RTwhQb33lAnWx4hgR-04IbWLF5Yxg4752Qpj76CBBvzDqecOLrgQwCxXMn5IpnOSNRNeHJU1XVdQf7CtRPyrHlsH_aO9pw42UgCZRAes66ig2VoLetAjhRT0TEL4Jp3OI0KseOy-90BQ5x28179HxUXb3HdjvkCqjM5yDb7qeLezXKhWBlJHyyKFvgVcj6KQkOJcBvNCBS0imBAI250QDyp-398iN6weIpmu8FplQHcX0UkXvR0tWsPUCYpcyGailZwpzu9eTFAk4hU9LDQVueCsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.   @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76089" target="_blank">📅 16:51 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76085">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯ ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76085" target="_blank">📅 16:43 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76084">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">❮⬥مــنطقـه آزاد⬥
🍒
💋
❯
ویسکال ۲۴ ساعت بزرگ ترین گروه تلگرام
😈
https://t.me/+Q4LrN9EBJM0wZmJk</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76084" target="_blank">📅 16:40 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76082">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پزشکیان در جواب آنفالوی رسایی رضا پهلوی رو فالو کرد.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76082" target="_blank">📅 16:32 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76081">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromReza</strong></div>
<div class="tg-text">خداروشکر
همین کم مونده بود اینو به عنوان چهره مخالف جمهوری اسلامی بکنن تو پاچمون</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76081" target="_blank">📅 16:21 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76080">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انگار خایمالیا سردار جواب داده و میخوان برش گردونن تیم ملی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76080" target="_blank">📅 16:16 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76079">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ایران تو صدا و سیما هنوز با توافق مخالفه، تو تنگه هرمز چپو راست داره کشتی رد میشه</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76079" target="_blank">📅 16:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76078">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPMitX0zZn3zPY0YA4Khz4E28135LiojIcdgXkj0zyV6Sh93ksGwhQRjwMO-49ZZGmkfTZiefdWUltvs4ozvyJM-1Jnhk_x9k1iZ-G8JlYqy2LHr8OxVX18YDN7wvAyXlTo8GrWtuVg0qyCppjWhZGB-j5jDfuNmQfYcopROUortngnYOj5tpjneknjila4IJQHflwOvdaRT9gBSwATMqPyp0SCXZOehFAQLvDE7Zx5XiIkVTy6ioxg3LmmV4al3-09sRvtKuMU_Zu0UPiElBXRQ-LY_jG_AcCW-n4AJFVmhGS8vYl-fBqwVfe7pmWKsL_0nqvj8nG8Iq6T3xZYsjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نفت برنت به پیش‌نویس تفاهم غیررسمی تهران و واشنگتن ریکشن نشون داده.
@funhiphop</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76078" target="_blank">📅 16:02 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76077">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">رسایی: قلبم به درد آمد وقتی دیدم پزشکیان اینترنت بین الملل را غیرقانونی وصل کرده است
پ.ن: کیرم تو قلبت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76077" target="_blank">📅 15:48 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76076">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">ارتش دفاعی اسرائیل حملات خودشو افزایش داده و کاری که چند سال پیش با کرانه باختری و نوار غزه کرد و داره سر لبنان و حزب الله میاره.
نمیخوام کل حملات و پوشش بدم ولی داره تو لبنان پیشروی میکنه و برای چند تا از شهر های لبنان هم دستور تخلیه فوری برای تخریب ارسال کرده.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76076" target="_blank">📅 15:42 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76075">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromꜰᴀʀᴀᴢ</strong></div>
<div class="tg-text">اینا اینترنت رو وصل کردن تا حواس ما رو از عروسی دختر شمخانی پرت کنن</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/76075" target="_blank">📅 15:29 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76074">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">آخرشم پزشکیان میوفته تو استخر نیم متری و غرق میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/76074" target="_blank">📅 15:26 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76072">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Se_JvCtuHfdKuVd0RnBEpf0f25DwN1z235egeeihW2_RZUxPEm-PSWVXGy_Cq7Zy8ChQvWv2iSz_Mv_9XPl5eHz8KdLFCoZtZ23UrMU-Yu3jSi-HLsu7Sq4u6BDFwXcLk1lVr4B7l_d6xHn79NMc85sN18aZEQvF6LvrqSj5lBQoL2fhnqNtsQxucSVvW1hCPBNAf9ezxn2mT0MCyHtggOmyODV6A7EQ4T1NB9j75t-NyyE_vlQUt9gRyHJNqHiBpFVIrZrPHnGdEgAi0DhTrJGRr1l3Vlai-NHWHnGnJOzkq9tv2iRj6wRe-bSgu9egR5wr-bvDRTZXq9SaLLEJvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mZMAl3KcSbzbtQx5qwKtRHAdOOrNWI2UInO9jkc7lckSR-O72yrACIxTrfUyaSaxvwry43HFXL3qAa7FiOxsz4jgWdvnbekRCEK4ckoLr11LyZKPDh5GhaFStnQB5iqi5kzeqon2fozQNlbuIZY-1xyDM5qoazr0L4_MnIM3TdeFon5zaSyeybgrlpKpuy59VnGK_fuRKk6UQY38NuHtycqCwZaaby7ef1FEcMQA7e2G6xIjK08Q_e-3VinimVDWysXDlVm_ZyjhGLV6yPQk4UiWKHCNsRPz4wIumuheAiqOOX4RdjlXQW_SVz7VfBWFyWWMHlhNjO5nmNJtJDV_wA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">همون همیشگی  @funhiphop | reza</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76072" target="_blank">📅 14:36 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76071">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انقد پیام ندید، گیگی ۵ هزار تومن وی پی ان نخریدم پیام بخونم باز، فقط ویدیو های بالای ۲۰۰ مگ
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/76071" target="_blank">📅 14:15 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76070">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رافینیا ده برزیلو داد نیمار</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/76070" target="_blank">📅 14:11 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76069">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">فوری: طبق گزارش Jerusalem Post، ارتش اسرائیل و سنتکام در حالت آماده باش قرار دارند. به این خاطر که احتمال شکست مذاکرات هسته ای/آتش بس با ایران و اقدام نظامی توسط ترامپ است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76069" target="_blank">📅 13:59 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76068">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">وزارت اطلاعات جمهوری اسلامی ایران: بعد از اینکه دشمن توی جنگ نظامی موفق نشده، حالا بیشتر رفته سمت جنگ رسانه‌ای و روانی. به گفته این وزارتخانه:
الان تمرکز دشمن روی ایناست.
* فشار اقتصادی روی مردم
* ایجاد اختلاف قومی و مذهبی
* تحریک اعتراضات و ناآرامی
* ترور و خرابکاری
* قاچاق سلاح و استفاده از استارلینک
* حملات سایبری
* فعالیت رسانه‌ای علیه کشور
همچنین هشدار داده هر کسی در جاسوسی، همکاری با رسانه‌های دشمن، یا اقدامات تجزیه‌طلبانه نقش داشته باشه، با برخورد قانونی شدید روبه‌رو میشه.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76068" target="_blank">📅 13:55 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76067">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=EjQDQ4Dah4d4MijYHtaFApEduNaKRtOPyvDlhPz28kJF3ZUHG7f23uHWzqwyzenR85brbmrp2Qrs40jeT-X8b5H5FfRG_URG9XRKxKBHQxiktaArke2eokk5JnMdnX_8AjTlROy3fsEFFMnQ8HFB0qOmS9dN0HHxN0AYJbSC7pNfoFVS_Nh4YYIELjIicR0CS0-tHyzC5rulOEajyKkw8Iyo1U0DMfziSPhX9ckuKD0DP4mLd6Pl8t1lr-yOf8mVXd1_bxW6JxCP-wlmeLC07S05lgfWyEBWfYcJr0HGNlG5Ix8ZwbPmgwsKT8xG0IlqqksR0xOqPxXw9AV1RBXUTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/70ebe6aef1.mp4?token=EjQDQ4Dah4d4MijYHtaFApEduNaKRtOPyvDlhPz28kJF3ZUHG7f23uHWzqwyzenR85brbmrp2Qrs40jeT-X8b5H5FfRG_URG9XRKxKBHQxiktaArke2eokk5JnMdnX_8AjTlROy3fsEFFMnQ8HFB0qOmS9dN0HHxN0AYJbSC7pNfoFVS_Nh4YYIELjIicR0CS0-tHyzC5rulOEajyKkw8Iyo1U0DMfziSPhX9ckuKD0DP4mLd6Pl8t1lr-yOf8mVXd1_bxW6JxCP-wlmeLC07S05lgfWyEBWfYcJr0HGNlG5Ix8ZwbPmgwsKT8xG0IlqqksR0xOqPxXw9AV1RBXUTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارش های تایید نشده: فرمانده جدید شاخه نظامی حماس، محمد عودا، در محله ریمل توسط ارتش دفاعی اسرائیل ترور شد.  @funhiphop | reza</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76067" target="_blank">📅 13:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76066">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آقای پزشکیان نمیشه اینترنت رپرا رو قطع کنی؟ تا عمر دارم مدیونت میشم بخدا
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/76066" target="_blank">📅 13:18 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76064">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76064" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76063">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">میخوام
🇮🇱
🎒
همزمان بزارم کنار اسمم تو توییتر
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/76063" target="_blank">📅 13:10 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76062">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-OpY6R3Ax6wYLojiyzzQAx4w2uSjXLPT6huaFVDcnOhAltf0TxIs57y1KHwM1CbqgigEXp0tjR55g0uAxZdZj3kH1mgrrGVeZF5XQJ8HW6lZYjUXy1ZbGO4slbmfgxzPNmkd20hEFSaqj5vgS2j-Eaby3XuPvglsMGpT1fGJfnv7_WJ5t9lM6nqHoY8Z_Wp8NOo6K_Hn4hm1_wDO63pTT44ZZCmCT4dCYykdJgTbCl-h-s2QsHXHTFml4qG7KaApNH4tL_O1BGKInqTmb1r2eloRDzzdOgKDKLE1IAbd9LtDl2echyomwcpfUhBrF-iJRQ-Aa76_D0NY-4v4VQ42A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادمه ی سریتون کصشر می‌گفتید که رهبر سالم نیست
چیشد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/76062" target="_blank">📅 13:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کاپ رنک یک وسط بازی هم تعلق میگیره به قیاسی
کار بلد بود ناموسا ی جاهایی داشت باورم میشد
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76061" target="_blank">📅 12:49 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76060">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">خداحافظ وحید جان</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/76060" target="_blank">📅 12:39 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76059">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زنگ بزنید منوتو به امید بگید کانفیگ فروشم
براتون اشک بریزه یکم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76059" target="_blank">📅 12:33 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76058">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">گذر پوست به دباغ خونه میوفته
Make Vpn Sellers Great Again
#MVSGA
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76058" target="_blank">📅 12:31 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76056">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMahdi</strong></div>
<div class="tg-text">یه ترا کانفیگ میخوام بودجم هم حداکثر سی هزار تومنه
زیاد نیاید پی وی حوصله ندارم باهاتون سر کله بزنم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76056" target="_blank">📅 12:28 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76055">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کریر کانفیگ فروشا با گیگی ۱.۵ میلیون شروع شد و با گیگی ۵۰ هزار تموم شد
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/76055" target="_blank">📅 12:25 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76054">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وال استریت ژورنال:
حکومت ایران قصد داره قبل از اینکه بحران اقتصادی دوباره منجر به اعتراضات خیابونی بشه، با یه توافق اقتصادی با آمریکا جلوی این اتفاق رو بگیره.
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76054" target="_blank">📅 12:08 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76053">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینترنت هنوز به وضعیت کامل استیبل نرسیده و خیلی اختلال داره.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/76053" target="_blank">📅 11:56 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76052">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">معاون فرمانده نیروی دریایی سپاه:
با اینکه احتمال شروع مجدد جنگ خیلی پایینه ولی ما به هر حال دستمون رو ماشه‌ست و آماده‌ایم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/76052" target="_blank">📅 11:27 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76051">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJYuwtNlPUa70S-YbZdpeHbiaNbH-qVi0YGL7v5Rma1oIURa1elvCUANIDsXJT-bVN19-dsnvbOCZyaYaq-_Jv3pW8RT3xiaZhNaHlm5-864Jtur2xTNxzKiA9I34JUr3eifkONl-W9J94azbpKEXMpttCn_9eYXxJ2T7WgL205WuLyOtVEKnQtD_GrrOcs1d1vbtDNayOe7K0R40kPOwrGOCYpwOJ__d1RFCML_XF4drX0zccFaxx7Ezt6VK0Xnf_wzNfqA7QJAmeFDxjV_rsHAsZHqkLfLPiGddRoy4Zm6yJI2PjjwSsC0WAjFNjgYhUe4HcrH4vTksPm7ws_mFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آرام خانوم برگشتتون به فضای مجازی رو خیر مقدم گفت.
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/76051" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76050">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/76050" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76050" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76049">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VFuhKVN8_6LUpdSi4N835hcVMs7fmMCzXrSqXyo5Sbmfa3iC54XxzplNDapU06pV-TeGtzLG5FVIgRJVQSI3ag8ABhRNsFU3FWypDEhb-t5kJTWMJSDUNU7ffVLymeuxXmeZ1neisDGReFhiCHQmqwjX_orYGNHIWSzOxQdOezxg8KkKkNbSMC4nTYmBNEg_bX0gXgYXlQMy4Li3axI16tpVyQHeEy2sWQ8iwwflrzoU08X3ZWmBT5Y6yTQblY40hq6PM6Uy0Q1K33f0hdEwUqSCegK3dOI70ZiI7vs6pQ085lCsM2VHQ9sHZeDDlHaxlyHCkN61nsjS-YbMvZk6dQ.jpg" alt="photo" loading="lazy"/></div>
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
r6
🅰
✅
https://t.me/+kpFvLD9kaeJhYTI0</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/76049" target="_blank">📅 11:14 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">وال‌استریت ژورنال: ایران در مذاکرات با آمریکا، خواهان آزادسازی کنترل بخشی از ۱۰۰ میلیارد دلار دارایی‌های مسدودشده و دسترسی به بازار نفت جهانی است.
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/76047" target="_blank">📅 09:07 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=WWHSbcbX9dpn9WE0seBf6XsqGN4VaXrA1ZtfnbOwsVyn6PzJxBoUOQwrrn6zebDAGvciJzhew6o5GcyEg656AScjnmW9rj6BFswll8Z2KYPRInQnsKrgvYMwaXkLx1MCuefK6r7hX4xDH_heOEitLpSedwPWzB0R7m2Z9LU8XO8t9Jsd4-X6WQuimHK858Z9ONP7bvfHgdgE5mM4-WmNxK8OrZfROFN93KvENfZa-YGdZDMK_IGstjTuYoJg-m7NFpnT-TJZoVBXsnU0o_Zl_b-bzEgFAVn66FtUlAzttq5VZ73xIXk8QWl5SlzJ-JoPokLxlERy_obuwWWLhPLs1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/247eb1347b.mp4?token=WWHSbcbX9dpn9WE0seBf6XsqGN4VaXrA1ZtfnbOwsVyn6PzJxBoUOQwrrn6zebDAGvciJzhew6o5GcyEg656AScjnmW9rj6BFswll8Z2KYPRInQnsKrgvYMwaXkLx1MCuefK6r7hX4xDH_heOEitLpSedwPWzB0R7m2Z9LU8XO8t9Jsd4-X6WQuimHK858Z9ONP7bvfHgdgE5mM4-WmNxK8OrZfROFN93KvENfZa-YGdZDMK_IGstjTuYoJg-m7NFpnT-TJZoVBXsnU0o_Zl_b-bzEgFAVn66FtUlAzttq5VZ73xIXk8QWl5SlzJ-JoPokLxlERy_obuwWWLhPLs1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شببخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/76046" target="_blank">📅 03:13 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76044">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ممنون از آرتیستا و سلبریتی های اونور آب که در تمام این مدت قطعی حداقل با بخشی از پول هایی که از همین مردم به دست اوردن یه پنل خریدن و کانفیگ رایگان دادن به ملت و نزاشتن این حکومت خونخوارِ دیکتاتور اینترنتو رو همه ی مردم ببنده، کمال تشکر رو دارم ازتون عالی بودید، دمتون گرم و کصمادرتون اگه فردا روزی باز از همین مردم طلبکار شید
ما که کیر در بساط نداشتیم ۵ گیگ کانفیگ دستمون میومد سه چهار گیگشو حداقل به چهارتا دورو بریا از همین ممبرا میرسوندیم کارشون لنگ نمونه، عرضه همین یه کارم نداشتید جنگجو های وطن، بشینید اونور همونجوری بزنید تو سر کله هم تا پیر شید</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/76044" target="_blank">📅 03:00 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76043">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تا کانفیگا مفته بخرید که خیر نیست
صداوسیما: بازکردن اینترنت تو این شرایط خیلی کار خطرناک و غیرقانونی بوده و سریع باید راجبش یه کاری انجام بدیم. حرف پزشکیان مهم نیست و بزودی اینترنت قطع میشه چون حرف دیوان عالی انجام نشده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/76043" target="_blank">📅 02:47 · 06 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76042">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رپرای محترم اگه میخواید کار بدید الان گلدن تایم کره گیریه، از من گفتن بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/76042" target="_blank">📅 02:17 · 06 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
