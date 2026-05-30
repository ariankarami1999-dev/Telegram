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
<img src="https://cdn4.telesco.pe/file/oQliOaVH3QWR7vIbC25hx1AG6kcpCeBd15yOL1bYOaoyeVQdj24c7-TyLDpqHLruRgubFs5QlEg9ctvQLiIUE2Ey1YXw8GoszGTD536fnTtKece8cnKA3jbeA8dzxaDTffRx8uePGCaoDPLlCibfHDqXe7HFwx3oJGWaN9jZ4Zdu02t8tk349VaNsxlXpYZSehqYHEXu7bqasN8xlCPUwmcFP3_4Bp6OlkunXULNy_hB6OL2BhI_uWM56VU2lLxV3yGA3OHFmPFXHXCo2Qxjx-V5kSqphFAZHT4L4Es4XXVFEulScytPsnJidLvr9mOeXKKPRMMouBu0-NDEsw2T3g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 179K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-10 02:20:11</div>
<hr>

<div class="tg-post" id="msg-76428">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k16_Adx56I452YNIkpHfND_mBT7jubkktoNhXssYni4eJSwQbJEYB1M5X-oGuOmrchWbBzrsZvoVC9zSst50GvE2P75RLqipJL2xSq0AHAECp4oQ1Ver5c96a8jo1jjokIsT726oSdcLOZ7AvfUjeaPPMz3XXs_tbPLfg2xBH6RJoy-VoeS8hyErEyUG0f7OxGQcllAfbspJ9heC_PpeDCpcTgBU13uoapl1HgtPAyP5C7tqlAFxsD38bw1bR-FqivUHw5KrkxY_sq1-Va6LnEyzSNkqg4g2B5hK0U73N3vy-NzYZEvfweKAieo8l-vSRHcb5xh9RC_potoOvxt_2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب با پست کردن یه عکس از جنگنده‌ها و ناوهای آمریکایی:
شما درحال سردرگم شدن هستید.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/76428" target="_blank">📅 02:06 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76426">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q2SXQaC-SA6GKt6UJg13ezKn1Ued9Y2tlGnT2zdtcqoluhPzMnMzWSU_nL0xgVJff0jWup7fWJ5FiTd0nJuUyzQ9j0QaEyBE1fRJMiM1ztN-xAjulfstVRyn80xpfbIB5FxrK5N9lkuv7bRE0oYtmwS2Kf7vPh6kuttQxhVvyIl9oHyy4rG8pb_J2SfjVBkV3TJ2d8Squ5wGFKdQHMrETqWNUcdwJa-Lolj3XWfBrI2Y52viGPLEzCLx3JbVY4SpJiqzDe0lReM_pOHr4H6QFHQOD7yZ4bbK9TbEjw50r0Zu54OFnlpTdiSDUryax8aBcF916c_7PVwqZ_UfBmTyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد خشن حمایت نکن آرتا، بهشون رحم کن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/76426" target="_blank">📅 00:20 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76425">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T-Wgzawaq_TZ4fy5tl2lxT-jkHcTfLpqKsiQ0I7LzDCa-ztrK7rZbZFP_RegvcLqSrlFpqM-tGtTT6ykLZyZaGlc4UsoT5AJ-y2WdakMY0zBcjz_b5vo7bL4r_n5KgBWk36u6aRURP2FFBsICzSSPr81rdZsuIIZUAOJiW7-8x1gEBYja_Q4v4Lqi3-EKhSgbH_imdgSCsPnK5sp7ooTz6KH1vsYQlF2Tone9zD1VcNf171WIZtKOmZ0gYkzgPNaTOQhu6lnCY25NK8M_iCKAIN40edozr9D6ZmaORvHiVcjFpW8ffRXXRC5YUtqBYydfX9TwveNZ24v90vKNh3n-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینو میخواستم با کپشن سه تا تیم نجس تو یه قاب بزارم یادم رفت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 7.54K · <a href="https://t.me/funhiphop/76425" target="_blank">📅 00:08 · 10 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76424">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اینم توضیحات منیجر ویناک راجب حرفای امین منیجر
خلاصش اینه که برا ویناک پرونده سازی کردن ازش باج گرفتن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/76424" target="_blank">📅 23:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76423">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMY6f_SRYUuL6EXNpHJDkrPiqXbPOioiTiu-CBboRA6gGB--3dJewKH-_PXBlmZVf6HInHkUaS47hMAzmKjkBKLQIbn6UtDp35xZwKoLsAGUTRbpbsf96Vz2TXlEK0_P2w28G3B7GgSmEoESp3guk_SPc60CaC0y7PdzhPGvJF3if8gvnpRSd0QNSHE4Yi7f0p6E_ruMOWRw8n6Bspnmml_BlZsl22dlPIdr3vqwb6yjiWn0jTAStwutGTr7kw_DWF6Q43uN6SIyU6F_-uBhFEInr7rnvd474S9VimgFEGxPZEAuvy26d_zlJzEIjYkJgTBp4PCx51PqeRg0TKXmCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینم گذاشت چنلش گفت بگم اینایی که باهاشون عکس گرفتی شغلشون چیه؟  @FunHipHop | Menot</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/76423" target="_blank">📅 23:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76422">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OxcPGtDT0QeiuRi53OfYElZGoC0IfkR5dccHXn0HUVgVRLz_01tWHY_64jeKn0BwKHegyOj1LNF26NFFVDZf_Y8156TA0bf8nlrrF3xdSypqdDZ5GJZM5-Y1F5g5xU156YY7wQI1_4Y7B7UrPFZEweRJCpfTctpawgiEeUad5r7Isam0ZFPfoPAnflYqMHscCSk40-6l4gomUi43dQrAJMKuvqi5-KRKuG302YbIDowCYt4jsiB8uTHiOH4B3Svn75sStUndyrNaVVrg15cOvxti-s1dy30RtGbvBfdLwpUS0pPCGP2hAB0FqUSlVEIyImL4Rb569eO970L9bRULjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام آرسنال قهرمان شددد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/funhiphop/76422" target="_blank">📅 23:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76421">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P2nDoU5tB_JHlaTY8n5Gp4Ovf_3rqU7zEjiiTW-vTA8uf1xeBtmTHsFbDTXpKCpvMtLmUM7XDPb7w7J_XnZAOHi4ULPwTY1jodg9BGHC5QisCxesL3v-yInQ-r8bNc-UFRIqamKGvYLPGZYvT29HjNJS3zt8k5yJUHBD7YUf9c-Exd3y6_GX49-_hXui05XXfNNhasWc6OJ3sP0YoeM3uMPOHEOCzJCsq9-IVYPEzwT5uhFnktD5bCgC2PFirrQK4uEkr8rCOO1iAuL8MIykh43RIbXhCdp5m1ig4DoPZcUkLJGgH5FbCYTY5l0nSJ1ASiW7NaYKOPeGSk8m8M_PeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم اینجا کیرخرم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/funhiphop/76421" target="_blank">📅 23:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76420">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :   https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/funhiphop/76420" target="_blank">📅 23:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76419">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9FjsaMnW9e42nYH-m0TXI2QBPkaQOMPGgXsTbk9aA0ePL9PoDL8cCQnBA6iisWitQvz6QfaTK-r6PUYYJ1kn9p200Q1uH1MsXm3IMGphgLVK20lPt4G2RY8S3FBqvIsoGz6EnuGr6OesHeNODmTc4fxfCt6ks0q6cZir3qLLVawfaShgq7W_1LVYxNGX8bcbh1GnL-27pmHXdtTf_5LJduLjpe8My_g7lwOzq8cIfJmSiSK2gkLTykEgZstiJJKFZ8nWSAkvI3jN_Gyt4qSeW2IHltLBhai17zM24x63JSxCQQQhEik-a8mhEp21G6_wynBhact60ydyysEr4rrqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه من همین الان با یه اکانت رندوم یه همچین چیزی با عکس خودم پست کنم زیر ۲۴ ساعت اکانتمو می‌بندن و میان میبرنم تیمارستان می‌بندنم به تخت
ولی این کصکش چون رئیس جمهور آمریکاست همه می‌گن پشمام دیدی چی گفت پسر
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/funhiphop/76419" target="_blank">📅 23:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76418">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UstPA-pqAvIBW-Fvsatmdzvg37HAGAIWcq15G9mEFeHSNneBPxU8ydN_jAZ4dgqRDgOgpHgslxrb6SMrG7BeUXeCvJ9gh7vXLKeJRHrA_VsX0rUeYCJaLtss5_S80ZpAWSMihci82bTOaHihn59ges8q23OS54W7WLv_4EJNm6bKbjN7XyctypOtWiria6iCk76hpNOIE3je30DOvm7G7WUyCpc149ZqKhwUfjFrhfBiaAPxpL0laM9pxjlTnaSNK4HcKstVO8GNAx03xx_-vDVBqU8FLWRb6gpQqOh5W8t4dEFrmHbr2R3M9k7Jm5twqHK5_iyzza-OVp962fyIfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی فیلم خاکبرسری ریری هم اینور اونور توسط یکی از اکسای قدیمیش پخش شده واسه زمان زاخار رکوردزه
😂
😂
😂
😂
🔴
برای دانلود کلیک کنید روی لینک زیر :
https://t.me/RapiFreeBot?start=get_uplzypfzeequaabv</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/funhiphop/76418" target="_blank">📅 22:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76417">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">با این نتایج انریکه چندسالم نتیجه نگیره ناصر بهش دست نمیزنه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/funhiphop/76417" target="_blank">📅 22:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76416">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اما امباپه عجب آدم بدبختیه
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.96K · <a href="https://t.me/funhiphop/76416" target="_blank">📅 22:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76414">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SacIZ4aia98P8EMsHSQpMhz_Taw7kVKEKcmYpGnnq-KT67eW-zLXeQI1r2Oh_Se5U9CmDUWuKv_259TkHTJ_wzNgzVnTVZOHc4Rp9L_Gde3yndgALYeCALUFAyq_ciSqLoDvrUHsS3bmhwwp68zzvWTCDIBCgoRConABwrry0HNjqAhiLsC_ER58tMXoPb2f5fOgOy_HzqseF32HqfWouPzHkaqT0yQ33-kWHz4_1V1M-Vku-M-2TnPudHWST7p6rKljhVDJESP8Ec8JDZ4aUqGeQjqil1OVWLnpvBKbi2QBSZfVLtmB8yVbTUeNkgwkpDEJTXaoUpeoWwTRrylJug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنده مشخص شد https://t.me/FunyHipHopGP/12247710</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/76414" target="_blank">📅 22:44 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76413">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/funhiphop/76413" target="_blank">📅 22:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76412">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">هوادارای آرسنال الان یه دوش آب سرد برید حتما چون بشدت حالتون خرابه امکان خدایی نکرده سکته هست،حتما یه دوش آب سرد برید و سعی کنید گوشی رو بذارید کنار تا فردا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/76412" target="_blank">📅 22:40 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76411">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PIQbBszGNwV47SyxozY0pPWimTrVEjy8EIiJ_9kdR_VyUVpBdLOg8R-6vWWIB-JT0Gn9ZLUKV0657ANPy0lIzpY-e8MsSwJ-S4uNJbo1T3zV9kVzaOUNLNMbmXA1YCOH-0SZpGyauSsO-qiZLv00Bu_c3-DlKRSXMkP26WrCIlL0J3mf3K4Tej--rRX2upS_w-rY4KHFZHYxlATt5eckZ4QvuSvttsoePXpwJXQfkm2ntNR6Mhaz1HkddvHSHkHhxAo3P30YMoq4Ws0mpTHbWhfvqR5VzYKCg8UVI6PXHUqBF5eoHtE6nrj4P3t3hJJP2ufDxbyieD3OkgEU9Bk9IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پروف
#غمگین
#شله
#نور_از_دل_عالم_رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/76411" target="_blank">📅 22:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76410">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید  اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو  یک گیفت Nft میزنم برا اکانتش  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/76410" target="_blank">📅 22:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76409">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گابریل
❌
اوساگونا
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.83K · <a href="https://t.me/funhiphop/76409" target="_blank">📅 22:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76408">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">شله گرون شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/funhiphop/76408" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76407">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پاریسن ژرمن برای دومین سال پیاپی قهرمان لیگ قهرمانان اروپا شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.53K · <a href="https://t.me/funhiphop/76407" target="_blank">📅 22:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76406">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">تمااااااااااااام</div>
<div class="tg-footer">👁️ 7.41K · <a href="https://t.me/funhiphop/76406" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76405">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پنالتی  رو ریییید
❌
❌
❌
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.31K · <a href="https://t.me/funhiphop/76405" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76404">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">گابریل پشت توپ
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/funhiphop/76404" target="_blank">📅 22:30 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76403">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گل نشه بازی تموم میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.82K · <a href="https://t.me/funhiphop/76403" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76402">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پنالتی پنجم پاریس  گل
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/76402" target="_blank">📅 22:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76401">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">پنالتی چهارم آرسنال گل
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/funhiphop/76401" target="_blank">📅 22:28 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76400">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">پنالتی چهارم پاریس، اشرف گل
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/76400" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76399">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پنالتی سوم آرسنال، گل
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/funhiphop/76399" target="_blank">📅 22:27 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76398">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پنالتی سوم پاریس، مندس رییید
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/funhiphop/76398" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76396">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رییییید</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/funhiphop/76396" target="_blank">📅 22:25 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76395">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">پنالتی دوم آرسنال
❌
❌
❌
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.5K · <a href="https://t.me/funhiphop/76395" target="_blank">📅 22:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76394">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">پنالتی دوم برای پاریس
✅
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/76394" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76393">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">یوکرس پنالتی ارسنال رو میزنه
و گل
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/funhiphop/76393" target="_blank">📅 22:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76392">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">گلش کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/76392" target="_blank">📅 22:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76391">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">پنالتی اول برای پاریس
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/76391" target="_blank">📅 22:21 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76390">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">به گربه های مشهد دعا کنید حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 6.57K · <a href="https://t.me/funhiphop/76390" target="_blank">📅 22:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76389">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">یه پیشبینی سریع کنید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/funhiphop/76389" target="_blank">📅 22:16 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76388">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">رفت پنالتیییی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/funhiphop/76388" target="_blank">📅 22:15 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76387">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">خیلی حساسه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/76387" target="_blank">📅 22:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76386">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">موقعیت ها ۱۹ در مقابل ۴
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.86K · <a href="https://t.me/funhiphop/76386" target="_blank">📅 22:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76385">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آخرین بار که فینال لیگ قهرمانان به ضربات پنالتی کشیده شد برمیگرده به سال ۲۰۱۶
سن سیرو
رئال و اتلتیکو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/76385" target="_blank">📅 22:08 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76384">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">بعید میدونم دیگه تیمی گل بزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.16K · <a href="https://t.me/funhiphop/76384" target="_blank">📅 22:05 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76383">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پاریس در حال حمله
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.05K · <a href="https://t.me/funhiphop/76383" target="_blank">📅 22:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76382">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیمه اول وقت اضافه تموم شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.23K · <a href="https://t.me/funhiphop/76382" target="_blank">📅 21:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76381">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">برنج کلش کیری شده میگه چرا پنالتی نگرفتی خارکصده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/funhiphop/76381" target="_blank">📅 21:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76380">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اوه اوه پنالتی نبود؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.46K · <a href="https://t.me/funhiphop/76380" target="_blank">📅 21:49 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76379">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">گربه های مشهد گرسنه موندن امشبو
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 8.08K · <a href="https://t.me/funhiphop/76379" target="_blank">📅 21:38 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76378">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">۹۰ درصد ملت لوز شدن</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/funhiphop/76378" target="_blank">📅 21:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76377">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تمام
بازی رفت وقت اضافی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/funhiphop/76377" target="_blank">📅 21:32 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76376">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">روح بن لادن رید به خودش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.09K · <a href="https://t.me/funhiphop/76376" target="_blank">📅 21:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76374">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">عجب فوتبالی شده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/76374" target="_blank">📅 21:19 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76373">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">چه کووونی آورد آرسنال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/76373" target="_blank">📅 21:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76372">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">اسپویل:
بازی ۲ ۱ به نفع پاریس تموم میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/76372" target="_blank">📅 21:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76371">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">گل مساوی برای پاریس
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.31K · <a href="https://t.me/funhiphop/76371" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76370">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">خراب میکنه
😉</div>
<div class="tg-footer">👁️ 8.03K · <a href="https://t.me/funhiphop/76370" target="_blank">📅 20:59 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76369">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">چیو وار چک میکنه صد در صد زد پاشو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/76369" target="_blank">📅 20:58 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76368">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پنالتی برای پاریس
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/76368" target="_blank">📅 20:56 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76366">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">روح بن لادن الان در آرامشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/76366" target="_blank">📅 20:29 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76365">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدا سیما باز اون پدر تپله که پسرش رو شونشه و هردو عینک دارن و دارن خوشحالی میکنن‌رو نشون داد
چیزی رد شد؟!
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/76365" target="_blank">📅 20:20 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76364">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">مندز چه مادری از ساکا گاییده ولی</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/76364" target="_blank">📅 20:17 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76363">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دوستان من اشتباه پوشش دادم
آرشیو وار گفته قبل گل آرسنال باید هند تروسارد گرفته میشده نه پنالتی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/76363" target="_blank">📅 20:14 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76359">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">تو ضد حمله های پاریس هم باز ۵ نفر تو دفاع ان</div>
<div class="tg-footer">👁️ 9.12K · <a href="https://t.me/funhiphop/76359" target="_blank">📅 20:10 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76358">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازی همینطور ادامه پیدا کنه صد در صد گل مساوی رو میخوره آرسنال
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/76358" target="_blank">📅 20:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76357">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">گابریل و سالیبا عجب غول هایین</div>
<div class="tg-footer">👁️ 9.14K · <a href="https://t.me/funhiphop/76357" target="_blank">📅 20:03 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76355">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">گویا اخرین باری که آرسنال تو فینال چمپ گل اولو زده بارسا قهرمان شده
بارساییا نا امید نباشن</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76355" target="_blank">📅 19:42 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76354">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🛑
ازدحام جمعیت در مشهد بخاطر بوی شله</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/funhiphop/76354" target="_blank">📅 19:41 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76352">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">هاورتز متخصص گلزنی در فینال لیگ قهرمانان اروپا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/funhiphop/76352" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76350">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارسنال زد</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/funhiphop/76350" target="_blank">📅 19:37 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76348">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بازی داره کم کم شروع میشه
به امید قهرمانی رئال مادرید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76348" target="_blank">📅 19:31 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76347">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هم فنای فوتبال عقب موندن هم فنای هیپ هاپ، برا همینم اکثر کسایی که رپ گوش میدن فوتبالی هم هستن و برعکس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76347" target="_blank">📅 19:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76345">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان به صورت قاطع فضای فان هیپ هاپ برا فوتبال مناسبه یا هیپ هاپ
فوتبال
💘
هیپ هاپ
🦄</div>
<div class="tg-footer">👁️ 9.94K · <a href="https://t.me/funhiphop/76345" target="_blank">📅 19:09 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76344">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba  پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/76344" target="_blank">📅 18:51 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76343">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">جدی چرا اینقد آرسنال منفوره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/76343" target="_blank">📅 18:45 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76342">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEfHNMdVY824aYgIxJGmmvZkZ1qg6_pk9G0Itt82fb0aV3vIweSeYg9hjnxENtGAjNxdLq26v1XEtQdsRq6j9pXwucDSt5p5poxPgNvgd4UIAGWhw_5POtt6aQGwBSN_KccJazF7pUOxUqeua-5P_w8fVbarY3xlT30UN3hS_7TXS6QOCDx46Bhoo945x2VgeKtpUC7chiPaLg2GO9KCN6LRbjoOXljE2MvPs5a2pyIGR2L4cb9GnEadQE6kbTEC_ROlBnSpaghz1q6Ybb3OJ-xOXHCOLPN1zJJs4gIe671LgyVRJ_EXP4yEAL75zNyAyeRSKv7WaEK5KB7UI0Phyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیدمجید نقطه زن، کاخ سفید رو شخم بزن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/76342" target="_blank">📅 18:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76341">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">شما منتظر فینال سی ال اید من منتظر گیم هفت سری اسپرز تاندر تو‌ Nba
پ‌ن: فهمیدید شاخم یا بیشتر ادامه بدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/76341" target="_blank">📅 17:39 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76340">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMImqoSp0jVizWsLP_PMEUdGPoXiKUV3lOKYvHdyXm34LFMT7cIZyW7UmZc5_D-yNFOjJXCsJ6fXm32OdFnUhNJu3qCX_8nV1JPtan7jeQlKLz3y5BjoE_fj3209-mLu9RiJ5dzIwDitrhf1iIPIbrdhElM1oUb15P0DzmO6vFMETkbbgbaC8bhMyqHCy0mDQO3q1Nr9JLpZrfp_X2HG6sPD9Z_mGgWtP7kqeseVeZB-OYfYtcWGjcCfAIVZPoAcNRysF-jg_3HeFy-dO2AQyyobGH9cslAclKam1u39QBdJnfc3fDx7Y5XL-2KIf8Dl44j0Cwrc5xcM0xDj6gqlFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید؟
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/76340" target="_blank">📅 17:34 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76339">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmCe89m3lwhQbkTOnuISoM6ZEqyWbDo0RVYFIsr1k6PVLU92MUkwyfO7O4VL6e0Xf_MKlfSbPFSjr66Udn4LdsQaUSNgU7PxqMRRQ85uZRxCJeFfsIJrz5lI8Ao0BOezgbWX4pWaoPsI65LlLT97OEq_TnGuGq2JLsCea-2qF4EDKcmesldOal7VqZ3Hst6b2QvSM5OI2N1Necy-y4ozh1Net2gXGpof64McS61NY6ArFfbfpmKiXjlCcHrc3bN-rmTw5fPOV-6OjlxNbkYeN4CC-Vt6HSsx5EIG-nbLyWtfvu0tZCUP1fYMDQOCI4r03OrIWNZi1m8HzFhf6o6mrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشب ساندویچ کباب شامی رایگان از ساعت ۱۹ الی ۲۱
مشهد،نبش پیروزی ۱۴،رستوران پلنگی
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/76339" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76338">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vfjd0oB1FcVwt6tUJDCR0vGPJVd6OfrqYNS-CpBVFv-exsLc5YoCxjv4XQLNYCtksogc6jHA_2_edOrc9b0_JETAbM3bj00szTjFwCfnNk8nF0FR_vtipj8zGCMdZDVkgET6thth0Q_bHDCqzm_d1B3fRXJLlwYgOnmR7YcEx5p48EXh5pI47F6NYBv3ByEiAd7_tA854ZizDwG2HCbAzBKrlXA9PihHJnKt61P7_Nl6ZEVPK0JSviPW2TA6hlURJumirXxQ7QihQLJz9CMDgqJd5NJbKxtrebWp16vcKQaT7U1nse0PZMS8JFC15VBzuzhgCbngtp_kMRx5N7zCww.jpg" alt="photo" loading="lazy"/></div>
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
g9
🅰
✈️
https://t.me/+RvVnWMHCqUc4YzFk</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/76338" target="_blank">📅 17:23 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76337">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">تو کامنت نتیجه بازی امشب رو پیشبینی کنید
اولین نفری که بعد از اتمام بازی درست گفته باشه نتیجه رو
یک گیفت Nft میزنم برا اکانتش
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/funhiphop/76337" target="_blank">📅 17:13 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76336">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gybqzG-KfzASpp3_MlZoUaMkKvXqxWF2WXNBQ2QdtV27fFNe3W9vOH_l5YhBnTDVIJk_HxSRgq2FAKWNo0ITC4SrD7Xych07xj9_u2XhQTLE5CWceaE9JENYowguZM26qv74vOMkg1IcwqQDa4b7FXIogEaHw4zQ9SSgO9KDLTL7qDCtG0H-YgFsZ8mQqKuY58fg6l1oMZrxtf4WPzTMthq67PZUcHrnJPFSl1_ZLHPfYfr0fIIHot84VLRNH4GV6b8YJeptl9j-M7eko28zht6Wn-u2yTf10O9MFoSIoqYIwFBa-c9FYZzbMRkJ2tu0BNePfVn9PHbsEUd76Goo1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پایا فرار کن این میخواد بخورتت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76336" target="_blank">📅 16:50 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76335">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c-W6eTELdi-lbSmJ6BhfJaLj4x1gF7-e_6JgFS0IomLEiqgEYJHL67UW_IW6SQC3GbMCFKonVvTkIQT9WAGNPXjD0AlpHtWQIvxzoMhDQ2E7q-nBLVs38xgSfUeAuq_8VXBw4XIgwwnYMzGo7i963D0B3hLxFleRJPyv2xJd9amy988MncL-q5L5C3foA-wnvcMX1Nf0dV7RVmcXHpwH3YQ4MKVBkVnE7dm-3fnFgaEUWJyPO8yFOvFthBCoDuwBJoKw0MR37h8G12t3FYdcc8tWLgE9Xh2I6eJpnqeL81702hPTHFe7bNbySv50C4lzpDdZza3VrT18OtiV37-UQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شنیدم مردم کوبا ازم کمک میخوان، میرم اونجا هم یه سر برینم امیدوارم اشتباه شده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/76335" target="_blank">📅 16:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76334">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JSQmWupNPqrRuhxPc7nqaWPDUmtkO72hUvVczrOtsIS_2W7OKFmivCMJES_rpsfN7xBsymNJD8luL4W3FKOsdwOib8zTtwaqrlt8M-BEId_eeNvEZ0T5Gak_7LT5RUmiDB1PGDQubzn5mzqa6ujTtzg2RiurYJ4RfBM9l17hXEudR2LE9jMmbKOcjg65h687_M6mQyLRkwMwqfai5IieU1taeb3L_n7HBMBplAZppp7QEaQlAFEGdkLhwFybob8I5d6UuvTTC5jTGHjrYkEXvWMhiejxJL0JJaWR0vqg3U4ycxtm9XJirOB-w73RX6DHUvWoZxW1bwSI_2a-7t6laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/76334" target="_blank">📅 16:26 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76332">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">اگه عکستو فرستادی برا ChatGpt و پرامپت آنالیز جذابیت رو براش فرستادی، قطعاً و یقیناً کونی هستی
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76332" target="_blank">📅 16:18 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76331">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید   آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو…</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/76331" target="_blank">📅 16:00 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76329">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سلام به دوستان عزیز در خدمتتون هستم با برنامه فوتبال با فرید
آرسنالِ آرتتا تیمیه که دوست داره بازی رو در اختیار خودش داشته باشه. از عقب زمین با حوصله بازی‌سازی می‌کنه، با جابه‌جایی و پاس‌های کوتاه فضا ایجاد می‌کنه و سعی می‌کنه موقعیت بسازه. وقتی هم توپ رو از دست می‌ده، سریع و با فشار زیاد برای پس گرفتنش اقدام می‌کنه. در دفاع هم تیمی منظم و سخت‌گیر داره و روی ضربات ایستگاهی هم خیلی خطرناکه. به طور کلی، آرسنالِ آرتتا تیمیه که می‌خواد با کنترل بازی، پرس شدید و نظم تاکتیکی حریفش رو تحت فشار بذاره.
پاری سن ژرمنِ لوئیس انریکه بر پایه مالکیت توپ، پرس شدید و فوتبال تهاجمی بازی می‌کند. این تیم با پاس‌های سریع، جابه‌جایی مداوم بازیکنان و گردش توپ سعی می‌کند دفاع حریف را به هم بریزد و موقعیت خلق کند. بازیکنان در حمله آزادی زیادی برای تغییر جایگاه دارند و به جای تکیه بر یک ستاره، روی کار گروهی تمرکز می‌شود. همچنین پس از از دست دادن توپ، تیم بلافاصله پرس می‌کند تا مالکیت را دوباره به دست بیاورد و اجازه ضدحمله به حریف ندهد.
پاریس احتمالاً آرسنال را شکست میدهد چون در انتقال‌های سریع، حفظ مالکیت تحت فشار و استفاده از فضاهای خالی بسیار قوی است. اگر پرس آرسنال را بشکند، می‌تواند با سرعت و کیفیت بالای بازیکنانش موقعیت‌های خطرناکی ایجاد کند.
تا آنالیز های دیگر بدرود
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/76329" target="_blank">📅 15:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76328">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پیت هگست وزیر جنگ آمریکا:
محاصره هنوز برقرار است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/76328" target="_blank">📅 15:22 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76327">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">المانیتور به نقل از یک منبع اطلاعاتی ارشد اسرائیلی:
طرح سرنگونی نظام ایران با همکاری کردها جامع و مفصل بود، آمریکایی‌ها کاملاً از این طرح آگاه بودند زیرا یک جلسه توجیهی کامل دریافت کردند.
کردها مشتاق اجرای عملیات بودند اما واشنگتن در آخرین لحظه آن را متوقف کرد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/76327" target="_blank">📅 15:12 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76326">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">آرنه اسلوت لالالالالا
آرنه اسلووووت لالالالالا
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/76326" target="_blank">📅 15:02 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76325">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">بکیرتونه ولی آرنه اسلوت از هدایت لیورپول اخراج شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/76325" target="_blank">📅 14:55 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76324">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5Egks3mJQbiisDnOzrS48JgnfVuK3D-cCbbDGrvYuCuXShG4y_5yp5DeyDbKXH2EdA4cL-O6kmzIfG25HrwqnrSta1hjqz6BxA6YXq4IQlUB5FWnRCgnp0Bg3YZxtflY-5LP1jjJsfcMzp6ApxK_sGuaspH1amHulfl-qA-7U2G3F8XguEC3rrNNoUr6nm8YCsNwSuAkgxjKHHURGJjbHB-lzZM15qsDn5OIptfsXoDY-hFjqgpVatKt1m56YKT5TuCpqgLNeCotPZq1EBQ_UHUWUOIZEFsVB3aLCSbwOcu5WkdkZl1P7Xm1GMqik4x7_VXYga3t7kBPXad8kauRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسب دستور مقام محترم قضایی این صفحه به علت فعالیت غیر مجرمانه و طرفدارگونه ترفیع مقام گرفت.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76324" target="_blank">📅 14:33 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76323">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده بعد کاگان میاد باهاش کار می‌بنده الان  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/76323" target="_blank">📅 13:57 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76322">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">برا مثال شاهی به هیپهاپولوژیست دیس ناموسی میده
بعد کاگان میاد باهاش کار می‌بنده الان
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/76322" target="_blank">📅 13:52 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76321">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">حاجی شاید نداشته بنده خدا مسخرش نکنین</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76321" target="_blank">📅 13:36 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76320">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K3rdEBpujToiluGWOgB5Heob1SNhuKJtwOvx6oxOjbemjYjKmkdhPb1IT9WHXjFtitHnf0e9tpHU9djTLfF7R3pRbCGna0DXpAjyPDY2pTKcw_bh4DLF3N8UrwhwmRieiTBKkmzh-gTeZsLIHj-lNmmUizkXONptyAHhTCUKYHC_QIOpvegUVhaBRdZFaFCr4M8f5FxfeVc-QblEu-uAL6J7Kk9llrrQce-hSOMT8IRhkpbqbPvxZPdIGQSOmX_v6eckohhYuoTXCMTKrjJ1ZAfm3v-YpYzouxTZ-1tDacoqTgzMWmnjmJyl7NsEn_NZjZ3Xm4vt2MWlLpxh44Q9xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیو نمیفهمن پوبون جان؟
اینکه چرا کصشو تو میکنی بعد پول بیمارستانشو ما باید بدیم؟
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/76320" target="_blank">📅 13:35 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76319">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتیجه بازی امشب رو پیش‌بینی کنید، دو نفر اولی که پیش بینیشون درست در بیاد باید نفری صد هزار تومن به کارت من بزنن.
@FunHipHop
| محمدرضا ناصری آزاد</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/76319" target="_blank">📅 13:06 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76318">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJrFsukjKO1TJRBFkwXLgftpvZJHQK7kUg2TVeHVqXOeVY33n_NSDxKYjhlqnIAbUgoDfvLov7GUFx3Ezuc7zFbAjUEDc5bSodo7J9_YqLWN47LAcn23LhsHLUchKXe_ya0IYRTrBOoMu30Iuc9QiM5uCJO18kQBwkHMg5SfofxDxWDT9eDZ0UeJr9lVQFez0kka2gwwMy9GDww4P9QAhjrVckB6evh9NDTi3a-mOYwHkJREgcT85DYrkQFtHdPWmwh6tawOnZ20hZbKMaGyVcmh1xe7J-SkYa8kuifUgOuf7JlSx4BPFqD81Wqy7DThJS4Mqg7Ae-4F8je2CwZTdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/76318" target="_blank">📅 12:24 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76317">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">خداشاهده ۳ ماهه تو ضعیف ترین نقطه ی ایران توی روستا توی نت ملی و قطعی کامل اینترنت من وصل بودم
تا پزشکیان نتو بازکرده نصف روز قطعم
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/76317" target="_blank">📅 12:01 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76316">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">کنکور سراسری به همراه آزمون پذیرش دانشجو معلم پنجشنبه و جمعه ۲۹ و ۳۰ مرداد ماه برگزار میشه، البته اگه باز نزنن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/76316" target="_blank">📅 11:54 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76315">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پولاتونو جمع کنید ببندید رو پاریس، دریک رو آرسنال بسته</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/76315" target="_blank">📅 11:43 · 09 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-76313">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-r71Fi9t5WYacAPycOc06tN3vPbKir-42TZvymNBwYCvY4cOpV_nFgaa3JOge6kdlTMcVLS_b5ZBzLKDhgNhgQKe5NMTJygMR2ezomwpZMuAOEH-wudigVHN6V3H4g4J0an4gWNb6H5kOvVOriq6HNk-73Z9FXbv-E10Hf36sDmiUixP3NcXvv_pHvMis70s3QjoZghYtxrZ33q98js3M8CxYG4LmtLii0wZdrxIko017V_IBwrGBLBz4jCaaAi_hGXmtEhE0fef4VBJ5v08bIqC9nfYNXxQhiWMgdgrBLrYEGMRj5E81Msbpcu24uRF-vR_C7BLyTzIFL6rPK7vA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بورس تهران
@funhiphop
| reza</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/76313" target="_blank">📅 11:23 · 09 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
