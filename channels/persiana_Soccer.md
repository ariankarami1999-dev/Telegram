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
<img src="https://cdn4.telesco.pe/file/fK9E2iL09PAcfkBnyrTi4PSNrmDCnb6pBZolFUEdYxRLFkQVg5xVmPK4Ab0-PgcqjBDnhSO9aL1iMsLOzNRF7kp7iCgpebXVMz1GubhEmOQOIjIf4oMLbWH_g_VGM0iMHXByNIapYX49KnM_5mXVEssh8T-Ph50pfQ6Twjg5z4Kk2wOSkfzeFtoYltdQ1aQ3j5lpi3BysBLpOxQh0jU83AFh_DAXpj0BJfDLv3k2MYTbYOfQHvVG_7sYVdnwgbsz8wRpd4UOoOsfgf4cvXNe2cqWbpkY3G0sqtTq2LpQxPZk6saOrrBFNBZOyJhdONF12aZ3j1A0x7KgOU5UZf-DmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 601K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-15 01:59:55</div>
<hr>

<div class="tg-post" id="msg-29152">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12f0529daa.mp4?token=vtgU5jYeJ20rPDnPSjpBh0KXWfq-ycj4As0SFafbvezMsxx6ls04i2fnOqcffr7G_lQy7Na5V428gyNilLMf57LvL4ewrijUakPT0ZBBQRt8EojrCRRlc2DE-e0FHJxO0Jlv6URsjsAcmzpy5UN3SV_CHOScRT7SpbMu3DqlNmJHB_8450cXpsxmrdF4DWlhWc8CLk4zphbeBm1_SuEZtXbFiBhv5TvTsWJsT7WI1JGQn9JEwZzmn_gOpgTUVmJDPV02FyMd-x8-c3Z1MYivFAagL2hexfeTq8E8kpLC0AE3aqYdwa8_jMhVAnbA8FfUC8GT0_3KzdbRVq3XmV2DIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟡
👤
رونالدو دربازی‌امشب تو اینصحنه داره تلاش میکنه ببینه رو برگه دست بازیکن الاتحاد چی نوشته شده اونم بالا میاره برگه رو میگه هیچی نیست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/persiana_Soccer/29152" target="_blank">📅 01:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29151">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6zhiesy1spcnHhzmDkJVOf2zVwFkuXroufn3QyD9HzhvgYDAv1gGsU-b-w59u2ODokNlZwhXvOQYKj7cL9IlKBSv91bbmazoOTCJwfHonC0Xs1ZAGUWkNzX4Q7IX9aJDoqW5QzJ1wi_RNrZVEDwYDjoSTFq6miCKFwMOSfciqYKBrYlf9Z1el5InlQhCgicksxNyB5ZuFe6x-oBQzvDVRNs0w0OKrlh6qsnn-kyzkjgnIJIMyxBBRNYlWx1p4w5SZ0NCJ8aFP4AOSwIR6wiHpKJuNamzfAB_ybWJN8VnyybhCj9p4Bfv-QwCmh1mPJMl5kzZXlYWVhFC44WUMl89w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
در هفته سوم سری‌آ؛ رمِ گاسپرینی در دقیقه 90 کامبک زد و دو بر یک آتالانتا رو شکست داد. لاکرونیا هم بادرخشش‌خیره‌کننده اوبامیانگ سه‌بردو ویارئال رو برد. اوبا 37 ساله فوق العاده داره کار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/persiana_Soccer/29151" target="_blank">📅 01:25 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29149">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7TWOftEc0n1E8Nty8X4kJ24aZUoDwG9O64vMIyr13JAUUvYIEBqOOlOQYZzD9ZptxkVQe5IRBFtv0srKg4bUfgLszjBW8ew5DcxlMEhJXAUBKZtEeyxWfxfzcf1lDi8Ex4U8hdQK3IR3ZyuI86s5pxKVQO5kzqYRE9uNzHtUd1Yf2FW1wY-gbjy-iLj-tHa5FvFMBi3J7KlioRU_p7pdvhJTQfezfn08ePQZzHMARq6CvKtSdak2IDkpYiKaSPcgVFo3jWu2V6TGrnuW9TCRh31WJd777ER6O6j5IPe-K8UcMqJKnmPjBt5VVxdiQ7iZ-OPjS5_-64I_hInDbo9NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛از جدال استقلال با ایرالکو تا دوئل شاگردان آرتتا و آلونسو در استادیوم امارات
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/persiana_Soccer/29149" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29148">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJ_rLt_kmrALv8RPve3vUGEXTqxQw0Awu3KNnYoPDImABt0Xu7RVFoAD37D0rI1gld7fYMxlCdMvzW5eweFWDCull66n749aLfxJz_q-LWiPOxUOjappLPBMR7i12vpVNzzzFq-F371_N2HIxFxb_CbNlrZZ1twdohpdP3UqYgqMpWcA8wO2Z0hmc4lrfkVpgqLvKV0caGiaA7yWjSdvw0X4stMPoEn5mlGrbq1cjwkwfYPjUQZTCbI9llMVEYYw_wFf4Ghn95VR5uo6Hcwf3mbCcFPNRojpDt0dcCy19-mJZJBpAX9r4MvxwassfCHp_S27ilLmylHe2-NgX07CMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
از شکست یاران ال‌چولو تا کامبک‌های تماشایی دورتموند و آ.اس. رم مقابل رقبا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/29148" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29147">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xktb6J9A3CUCfTEZ0FlNmqJ9nl79qC_ir2lGssIaQQdEXIb7IxARkniqmmgtTSoprOt4JbOuSki2GHQH1q_tyicmcSBkW3bWBYTiRBAbF01qOJhnQMJQhFRDu9rqMHsF-7V1Urbt_JexbnnUJv_bBzF24WvAMa5ZV-WSWuP2C8eIuGG-AGwyj7S3R0kaXBoAVW35mLCfZp3DMC-dVxl3wRvwKCfDt_7Z74Ca2pEbzpBc_zqP1K3jGNxx-03sU43D1ySW3wI_5tg6mb_6P-fHR2rVzOfRY_6dYXJUoa9QYAbrHejFAbwuP6ZpFgsb4s0ebCajLIIWBU9xdzta--CFbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 9.4K · <a href="https://t.me/persiana_Soccer/29147" target="_blank">📅 01:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29146">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02d43ee81f.mp4?token=JyONFOoQ5-ixW764f612_5I_RPl2VGj5Hv3M7TjG-Qrz-5Ck1OPfUxv8aVyv7zB2lBMRxMJY69b2OQeRZWJuK-94crggGWrFjkNLUdYMqg3tVUqrWrTvB3TIjHLrn0KZ_Ul1fo0Vb8ul6Je1CpuFVFuDgmbnGkQojPCto5LgqKkYbo9SmcLH36OAxIEWdB04DTGtmBvRXn-pO8uoxF77AMyz6yuDF12QkzDdgyLFOUMB1940NeXOJblOGgxTWzHXTPC3_IVudh6PvXfhwG9mpw6E05Ut-FqicbxqumoQ0Z9w2RD9doJcYrzssDtrkAR-5fsMOsPMw_pOjrfP8cw_pLeCtRfEpFyBcI4B0wlcDpNZ-9wODDf9jIm2o0QNzDjHFr0KtOAo4uy6iU48p0CCHpwGFO_6Sh-lxGZya30FZ257WcxWAzICuAZ6mZUGa7MzG1X341fuY0hmuX4UbTIgzjlMAGXIjmH-oKPf1igEZ6IGSzFy0e7mP0YgqCyWzboGAG1uNV-58azUjhELpI7V0C6fsX1mqxkSEoeHubq9KIXN-uTp9WRQt2S-9QCA4sgstGhK0gXC8Vxd9Ews6Jt9EYvm_YW5CUpZDuRdRl7O0UMEYBMQWl2uLyw_njMkP-_nuVghSxRZWve-y3YNQPPhzN8BSRUavYJvWfByGYnSYbk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویس فحاشی برگ ریزون و باور نکردنی خداداد عزیزی به امید عالیشاه در پایان دیدار امشب؛ میگه منتظرم بیاد بیرون کارش دارم!
⚪️
@Persiana_Soccer – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/persiana_Soccer/29146" target="_blank">📅 01:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29145">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/persiana_Soccer/29145" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">‼️
باشگاه گل‌گهر: خداداد عزیزی امروز الفاظ رکیکی رو برای امید عالیشاه بکاربرده و صداشم هست که او به این بازیکن ما فحش خار مادر و مثبت 18 داده!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/29145" target="_blank">📅 00:57 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29144">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt4P-VEHNRlG1Bla8dJmnrPmyXJs6Q1jFKptx2XOGZgUMus971WwnK8us50y7JK4rux_8F1j5Gjq9yFrRSuxzRrAqnxKMMNZZyRC2EhsazcBCQbSKI8GH_DMpVpuiBlBa_2HOXdEilPTnYLrlHSCAi1MYrjZ9WdhDQKMqbq3DHBmd4iYVE57HG3hasSb67TnzhXM5FoAQnWXyhR9c4bvKCnJ4XesbIGthJ2MfiDeieu-hgoI9NPzvJ9Ht-Q_bWvzr0oFCtTzF9aQkWto9lgMoikl1vMq_FOGQNzDrRbdauh6CS9iJXH0I-v_uLNePmsD_WvvJwzqYdib4yPHACR1CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دنیای‌عجیبی‌ شده؛
یه مرد تایلندی که از فن‌های باشگاه بوریرام نیزبوده دراقدامی عجیب بیضه‌‌هاش رو به 2.7 میلیون دلار فروخته تاماشینش ارتقا بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/29144" target="_blank">📅 00:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29143">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KcAQozp5n4WaSOADLtAVvxSCq3YFMEvNBv8GCIGCbVBVv7fqgN4rUqYQYdUPoLWJ8w2byeSzdcaSFncE-T4ung3TaLTLHZgKWsWcqKC2r1-zXHLC6b7qrxr1HezKLAqVaA-9R3rYshHujOkrcz6ZVyQ7gbsR7oQ8LYgmRRdYL66I6lzZSzK0vr7JCSOwtKgr4iANjNfuNEB2Krl96IQ3fNuo9oudLEtBzb7bRC2byWLRqpQPhDYgGxw-aVXcg5AgIWjlupquR5OCg62QmejWqxdwp5VQlOmjWArE_VxR-IOvPYVbjSpxMYY8KM2cw7j0xlI6WjVfE-C5zAKu2q7XOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیر امریک اوبامیانگ ستاره37ساله‌سابق تیم‌های آرسنال، دورتموند و بارسا با عقد قرار دادی یک ساله به‌ل اکرونیا تیم تازه برگشته به لالیگا پیوست. جالبه بدونید دستمزد یک فصل اوبا تنها 600 هزار دلاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/persiana_Soccer/29143" target="_blank">📅 00:32 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29142">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b37415d11.mp4?token=e-nd1tEEExfL099oqwNbBUufS1BxoIfEqhFVEPcYmaJTTTwI2Q628ceeJ5q6iOCklGTcNArwFHypcJ6iFd504c0BXnvGWuKJv3iboEbQjKQNHJMeDNMyTX5nuQq_yBPLzGFq4NsrXf47RcQb0SvYsygSkCp5g0vv2qe48HBSnUOER2cIDjBpzwQiwMFc4nI_0h_X7580v2hahD0n2_baJxjCirB5ixL3jucOGPPVDhz1looBH95I27U0D-YlvseyD6rzi8yWq-lKaJmA6S4tQvBInDsrA4Q1KH4bs4k0yuGD4wfbgvYzwNE9Q0Qk-tHCPEp7SDYPJpjhg8Cp_Tu55Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/29142" target="_blank">📅 00:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29141">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pNzb07PK6bqqOILnDvKMvxisPKpcYdyJrm9Tm1fE3n-ID3tIBudqRrMGm4PtziIZZIQuVEQe5v33FbqeOuUy3vV22G_OuT6J_JUjBQEWeVDiRr4SPYDSOi1GNMI0m02-6CGYiUA7DFH_cfTRH5Lo7KhgWHegQMlpn-XUUOMQuY4Oy7msacwHzBCZGNnGkvDOonMqLDGRfRHS5SUPTo6VGtLgUmzGkOxe40oZb-ynpKqQn21g2q4Jx-xJRaiwdiYRzj9bwPm-nDCBHrWtID-4CN7jP2JMaJRBi3OaUMaBcFVNMl3AnxXnntgfKz4-ChjuOXJrl8_DvErlGrsm8udhfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امیدعالیشاه درجواب‌صحبت‌های خداداد عزیزی: اگر سابقه‌ملی این‌گونه است خدا را شکر که من بازی ملی ندارم؛ نان بازوی‌خودم را میخورم نه چیز دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/29141" target="_blank">📅 23:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29140">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JbTxZW1CtHvk798qaprIPq4VO6SiOPHH0dLKjTOUsnEDI4Kz0jSkMsqnusFxDgFzbKIcDCd4jLoFNGHTKI4vrkbpGUHm8RdNAfZD2LuFy5sHbeDVjAf3pMUVSprh9VwB3L0f_d7HFZZiZdX42VJ4yu3q1esQUfa0ZVS0X5LjfhXR7VUVUHb96jaB7zxZCxO3OvcIZZ_R2N-DdYVTpXOfz2SG6Q_ROhJf_IMvu8sV_7OBmXXIkfB2tsVfG364zsfHIMcV--pTz6wcRrJB3OVSF11nR5t255oaOeJydnf9Xz_-We0vZXAViCrOKC6n2LAuAkAXBw_IzCBSLIkGGK_zVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/29140" target="_blank">📅 23:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29139">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdQsboB7rMHY0sIiMqs1j0_5zt31PgLmfceK3vQ_7vBTF9N2w3eDQbtfC9mRB4DRUF0NPNvcEFxXibza8dQhufNOAmJJ1c2z0KDfdSwpOMnUqq2erZAIyIt0078MvzQTCQ3_Ld160VlHw0GOFv-LX9130w5e8JP6rQbRtlucDomMYGScSp66xkbaXfqeMpDllMZNDVi8YRneQJ4jQll1sQDXNWNxABiZa9JhsVChcApsuL8sKESnh5CafV73s9eq4EYVHNW10_WStyJCnq74pSa_V0bB-VdRf7O0G43kLu3Cqld6xE8xaOEI1zC-Gf9otk4LJjt5o7M4xyhy0JGtzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
جدول رده‌بندی لیگ برتر عربستان در پایان هفته پنجم؛ النصر امشب دو بر یک به الاتحاد باخت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/persiana_Soccer/29139" target="_blank">📅 23:32 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29138">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43e4d2c6f6.mp4?token=YovPMbtstK5tij0JPOIQxXzILvSGc9VmJBCBU0dKwS8wXGC7wMDaHzg4CQj_G7Dx3OCa7ML830W3RvOmquCxs0aoVl5HAjN8HxzQQQQ7X1TDfHVAFng9VT0dDqI2YfvnLCTuLreBIpHOIo7FLMgKOo88FuN3xscnuev97vvNrGzmNaVLaAtvGhaDyTm6A7fQHCMPeqtanGlyiXs5k_HEbR4jB00O7hApBSOXWLplfwyHzVGea5FOk5QKSlFZ-ccmzVW3uLftV0VLvphzp_BbbCgO5UA_4bgb31pUmYaKQ0Uk4LCgBpwoK2snb5bWTZMVP_jucv82MO0KzMleFZOJtlSu7trYMJ9d19U8n1pL1PTEHkleLct8Rrj62GfxV7ow8JOlokZ8KEI5as4Vff3YBrJqcwPGmXSzWjnREwTRnSm3SVPw6Q9F9gOjt8kOS-s1LtHuy5MfP4gcR4VGSzeEW4Z11re6oWxWjx2XE8_0bMoKx8X7vi-tLORjrOhm-jsVDPrmem1gm2v6stnoaKiaxFI8bzflx1mGmskkUgoUJI6SUGlNw3K6dhyl7FDit8SQOa5GrHMDGncvrxvgvrGsOk9gjKqnqqgx-0liqWWneUKidAGlSBBYSkvFUbXaktJ75hOvIcWCNGZ1hxWmFuGJwp9YT07mjjH6rY4uSnPI8cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.1K · <a href="https://t.me/persiana_Soccer/29138" target="_blank">📅 23:18 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29137">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jy0mE0gHIgpuQC3Od16gGsCGXJFLw2fbBjiPt6BarhPxkUUz7yduoromjWA18PP5xnALv1QwDEi5LdEyzGTqloqkrwZ-PI05I7w57DKBZkwS4C5a5CpR7JGrwC2v_fBhG3tgmlOt3goz9Uoo0MUoyn52r5ncN_ynVNRuuHqrwoe9K_C-Adx0p9HKlbp6ocBzsk9DuAT_T_5-azuv8X_Zboi6N8nnIURiMs8m0UrTSiea-8dC2KRRFSt9LC9s1AJV7Ph4LoNCdsybYPnSzzqrLHCPaC0pQV64hrvgnBhKFznUsOiaVHEo-M-N63XzvTrtRCBW7ZpD8t80zZABeBvF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
پیروز قربانی سرمربی تیم آلومینیوم اراک: آلومینیوم تا حالا استقلال روشکست نداده؟ خب نده، اگه‌ اینجوری‌بخوایم نگاه‌ کنیم باشگاه ما تا حالا بایرن مونیخ و پاری سن ژرمن رو هم شکست نداده‌ است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/29137" target="_blank">📅 23:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29135">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BZy3bb_hWm7J5tx4JoV5tum6N5Y9Bz0CDN4lVpf3DEgidAtXQmWQwKcDX6_TZmZochdpcsu_NwccmCB22kTWD5NJOZH4yyQwiA0sI3kXkANu6MR7wRR7neyep6xiHCvf8rlxmgJLYxgI6aZof5UfajIOOHvZGFZlJ_vFGzsUpLKis14qTM5P3jw-KCyETjNdrYbixjtO0jRvlKhb20gyj0rAu3QC8i6csJXu3eDKwMHAK6nhSTxJsqOjwxmSJr2RfCrlTLjN4OViJirdgowrrRCfvpdd_QCUc_CGzRA7bohCEiN4vahFU8y9wp2G1dQnoUrlUpQbBVXbJ-35fyDN_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUebRUzK8OaPIkFVDMBZRNxjp6YXqqOQctUBqDeurq56S3IR3uaibe9R-MYylTCMFumndpI9mDZkuXa30sbhDZVaVqwaJXAuGlKbbOFVL8U0y3sFZXKc60BXnYmEUdR_P7AOBC5SqVQUnDhyMsPuJOVDsbq-nXmaFjzxS8zj0-M3GbXAtMOFR66J5qj3XTKesiLByhyC86DGQhXL6z0Lw7m0DdjasGbq2MEhUOO2M_BI71ciCtu41u8N6kAkdRvCEaAQlSxxvp9Y22oHcrL88MMyHKHs2RXtURViICdDx4PhRQHgD8xjN1AZggalLQKOw_vaKd4NHhOhdte-9F521A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
وضعیت برگ ریزون بازیکنان السد و الجزیره در آستانه دیدار با استقلال و گل‌گهر؛ السد امشب چهار بر یک الغرافه رو شکست داد و الجزیره نیز سه بر یک تیم پر مهرهه و پرستاره شباب الاهلی رو برد. تمومی بازیکناشون آمادند. العین امارات هم حریف هفته اول تیم تراکتور در لیگ نخبگان آسیا دیروز عین آب خوردن دو هیچ کلبا رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/29135" target="_blank">📅 22:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29133">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pXIauOqpONpe-hxerj-sBquKqmdZADGNHhPOrBZ4Q_wu0AVTKUvIHarpSdTKUpXrydskEjqQxB5kQ4RZgJz9YU4_WwGbtvMC1MumX8WxFLsL3Gb1EDAygSuD80h6NGFvgt3nEWWVeKPgHYw2hv9dZYmC17jyC_U2FVlA6tIKy-X4eSuujmOKlBAkqv7oi2MJ6RJOi_hz5ZeYbmFEzc_hXmS_w1mcFJTLxDyyqtfSd7K-HWpaaUNf-1I2kqn4qGFiyIzDrb41y1Cy8L-XRAhHbgtOVkfR07BwKP6IkCUC4X0fQzjt_CSqBxS40gnegGFjkTEt4ikoBr3M_upJv9H0CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LWC-VIiXDE76ZJmy9Ujp62yaHbTv1pi031dDINf_zpgx17p-pmM4L-WSa3_-125P-S_iMobGWk4fmrx_dQSbuBwzsheaWJwsgJs1xM1Chuj3QlI5Dujcl3KYPO9zu28BZ1f3lVr5DReaePf8VJM4OCk0PVibIeKGJF5iGGvgVxn7RzY1MCZPrdKDzVDpE6gRAtJiNnyzP9yccQnGJflSbMize2DRwwLhI976ZPcM0ydg-nTCU9d39sgeDyEpZ284jM_mLlAApciJhEF2ubKJGSIrN_UYDHsILSqF_Ec5jdxAWObgfq9v2ssE_EFP-3fX_rKJhb7FL3fM-d9UwZ71XA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/29133" target="_blank">📅 22:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29132">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/29132" target="_blank">📅 22:04 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnHZaJ64ATF9kzONk3Ck1LUpnt9RCKPYKSv3KgWrZHKMjJaCan4DAOcD5jNxOwSLMP25NQcNIgV23Nj9NoauS6-wZx46MTpcbv0jFMHPvLjz6M9U6QUCtOZkPDRudYqY2-2bhsKJnSqDXpFrpZlzvTldPmxq0-WSLw3Hpd_O_-CGaHoa71V6SVm_PbwHIU09Lz0cnvp2uQXwE43l2rt-LBAHrgsCyENbGd9iBKyA0cGhmvBrqYpcOFGFJ8QQjwDOCE2benEhHeD6hg6qQC4U2R1kAlzk3VLVI9-VaPhn2wfLyvjLhUU-OwkmuKXTzptDOTFYXdOpRhznHUxDyummMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwvgUdaQLB47huEDjWHBasqgFLVLvOn0pl4G_Sh8FGjQzvRc3BGJamvYOh33gd1EnrBD7aC00YaNbBrzlA5IihgUD8s-bRKjv3fCt8pcy0paD6DGrA9WJ1634hIO7MSDDJb-9uWDJ5-f4h4u3kgvxzs_9zPEjvUgd9wmAmqfu-VWA8QcjFTLzp1gtnIMebfckW4TY8X1A2c1rnwUmKx2Qyq7Nc7pAy9cfWv4C1qkNgg_tDRHD1qF7gDnTiVN0jAEpJVKduPSm5e01Lre_8oNU6_--FDjVJ5GwI57fz1j9tL2YRqm4ibOkWAm1REO3YxofUVH_3trKQsqKEWJvMm_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKMq5MBB8Oo6-xtiCmEEh88TtZvZGFESZ4Fgtpz2IhXMNxwWXnZu3e-XnPIMRfN5pwWlYxtH283bMgo3RYmnjNx8xG267N1XEVuh3PyCDaNhUloEkaO6iQPNiZRk6JsXhw4_RkQpVpl939Sp5LrTDuBnLwvS4qlAcp9KvYzksW-fRQS1WdwLgm_ELaAcVNq3iPg384QlDRGCIkVl12gw8JPXY16viIG7HMGeD7ZNZszWMNOw2XRpq8vA70Fvn01jP5jxOfaBuY21X8shoYhY1sSJ5ksqRvh6A4E0higQpJc7MGj6CeizafHQAj7otILvPGROLs7c1gds5ThrHaB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoB1OqMz16KKwAmY1fRYX5FAtsHYpHZFDTa99AOPMdZF524bEGFDrahTfwOtThuFDTs-_7wcvxj-zu2mas6FtP-SQJ8TdZZRow9VwlOGEJhiw9TQ3vRRggHByz6KjvFkXQwWXGnA2z1r3srRGoPelkS-X3NtHMFRndcBnifsRdkorQIBCWaq-NwlxQgje8M5T0IWIUMW1AY3Nbcnp22UQRoGjCrO7rEK7CK9lX23GGifafoUYafWIH8OpszAlefu5eg0sTVR5u7aTxmMU9633aKawHVPiDaW1QZIZjq84uow_i88P0eV6TvsinkrthO3zNXNwJHMH-T9XjPkXlRsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPt2mIiOiii9SfGn1V0cDAx2kFk0n0iZkuOo7W0rWBsfpklfR7YsgXF1tJnxOEz6sWULSl1OkFE6t7tUvfsQ03keJ6kxQFDIf18bjTQsRZgw_mQrhnsRLv1FEDvwTRZljHbu7rh43B7tsLTbgcY8nLxOWSZ7YrYENWkPeZDfHd0gCSgT-TGJ7rnhhlS38u6RAI_Xh5nCkZE2KlfLjzOh9orA5MLIB33gIerl9e5wUbrpzgaC_JbZgjM-0hACbNSqqAv7_0v8saEtiR2i3-h-HF3lvwTUAe8LKYHBtCcaMf2KabsQeTrUzZ5r8gnS6XeysMN404xoQ_R3S7TIlsJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3u7zN2tjDQzp1DPz_FKwiaMetFl-LS4p149dHZL4DASuVc7Kw4-bc8jYZvIfW9kepv0Ym8S-gVvN2uxtniTBYlClUe-zR7-X58QUWhcijoZjddXROdgOpVTPxBgqOrrAARKL4oQvbNUw9Eqf29qKGTi0TgOOcT05CgJYw8r9ByAf5ducG7OG9zYi301KtdMb1g2flvqOi01UvyR41VwtjPCqeCe4BdETW6PMvAH7qU9vkplZH5nJt4HGW6CqW0V8YmZllDvkgbPXHIMb1VeJrygTNwvbOxuTPalD8OcPKlBqNlM3c7T9qhBw_ynod5PTQdUUlJorC2a9KLgS-Bwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfokdBVAU6grW5pAAh0wsu8bKTJFn3S-oswTJbJESxCIpWHim0HVdZPEApj6yX5DQoXS-dA4g0wCyVQ3Nzzmm5qBqJ0jsAwCs1yM9wJZxTliTlasQKxLbAu8l2iNu6rXxzs8n_xRnqOJ_DHY7mb4gyhyWnJhOduB5DR-0MNNVEAr9xwaUcKidsMcSXLCP3Fba9azOksZwWwJdMkhtlFwcyCoEuXU3xKtnf6RlGq96nS8unQ4r1ZPC6JQZPrjI_xvYP2-6MYYsblrtHqLNodqhyMNqN0wt5YiqNTUwkpvwP4IOVxXKLNPxOgFBJ4u-13KU8f9JkivZ2iT7O5fEfdhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fedqSG8yGwum-Y49iHJDlOoaGV5azJym7WmEyOIdXKajHhejboNYG2MqJWDo217QndVGS_QA2dQMwz6BZgJtV25oOlVeRWvknFmG4IELFVhX7RzL--22tj-5z_uqPZSY-X6jfFKqgeTwMvYhyn9yvWKuh3uC2qXvsVy7B0mDMPCSR5qrPIncPazQbI99YnhLSI5aRXRf11atY7rUQ01y34vpbNaPvxt2FAfduKtN7WPhmc2MZh-km4nO8-nFwtGVoDK-Aiwu06BXGgSNMYMQGhwwTXxir_p6ZER8arzTNYuQgAyeQJrQbMrD3xiWwboNrZQnO0LD1DX_heOSXiJMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDzUGwconhZO35XvDTlMzraXzb--yicwbjvby9SElzQCBxtqO7LZeQlngwZYdDt3pgAq28MAxbZo5bqlBdtZR9SaKPwCkHpkX--e9toJsAfDkAXD2w4273ZPqahxf6pH2CMLuF-4mrWVH2Wzp0ASknyYOhishjdsrMymEEXFTl5phR7-J6GFunQw5JfxwNMwZkfhiv6FpZnHHuGaoRgFu1hNo5vHUBfKuKZX-AESZO14Xtj_rKcZgmr9gsfQODIkOsD3gBnIQXZfXImo2kFf_P1-MV03Fm1YyLePnaa3pOljBBLopcOFOFVksHAvyojGQQ-VRoSIckp4_Pqmd7fxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DARHFybZGpY54D9fP342nFE-N5G8jM_SXz7oXq7BnNPRfOkjldt-TlZvdY9dTpYexrH8F5PftGWQofDZCqH8rki7PGFmk0bQnNE71i8N2Enx9nYT2dme6PbvjAbits8wrre3lu1X4vMQe6dIFm_qzRLNOfyU-HPmZEF3-c2d3v6cLQAO7O1QnrvNtBPKRfGKzQUYUbjuoAH5ISK2fqFhT5Adhmli5wFAapBgqnKWkYwWG7ZCHbL3hazG_dBQs3pS2NE6p7RsAR8ywzbDm0tx8R36tuO57XwBcRifo6cRVtatMDFdDAprpKpWD8Op_OoxhhVG4ja7rJKmuzUHCCbWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFfSZ2BVOqIksreZvLFlXGzn8bK1KLnVISCbYNmOnuqPXKbpI9n40BZyfnzUnXkW8ICmVIWI6urzrouIr1_Y4bbXpCP_bQTfMe1SXiiXRhx_sCWfBr2wRCDwJxuO9aBM_k26MoYqEFbfjEgD7wCW26V6m5ZaMwmxDzUWD3KAf5bdEVwiUQGWccO3ii_xahqxLvsXaNmr_pT7kgf0NSu8dkJNoHwVK0iN7mGqDd_CCe5wR9lDadPBWLiElyvhOE-_dfo8JCTsNLZZjMyH_wrC1ls8yliXEne-ptqemcEPDkGXNMaIpQJZxPR9ZEWsZdgMFf8cXuhT4QLGC_zJrL3pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK_68ZN1nHLWoN9e9tIPrxnQQ9jiPgJ25OSth3eC8ygMWr3PJ11DcYNGxO_vL9s1ONGS0LvGwbLfCtOunYLQUpUuRPe1gHkyxKll31bLJ5eFI8P2cfNpcrSMGdFe16jHb6XCln3NoBlREiLOxecr1djSfYrvauE5Qb-rlsqLdy3TXNnZl8kgigCs0_Ma02heSZ7KdQcKOkj-71hAyc0sI97IwetVzK8_7YywrFpHX8XTKYjyNrh3eZVL-zSh8pjSy2M6leNjisAQeFEGc5w2MGMrvVH3DMpn9WuHXsQsmVM2XGpzNCZ8ItHVyii8bRWlSPEhlIHFcRlJIJD5xKI7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtjtEOmcsnJXQyrMlch-s5XgZyAsnQ47t3iGLQADUGTYbWcvZqx0MikOl28YOZAxC2dvdHWJmYdjQ4WbeZD4O4uCKS9pN_Vxk4loYDmXs5co4mQ8PmUmTHH2HeJvfwq-l8fgxG-3-yxkCvsR6RgEkZxTtJzYychji_PBSkxluNvT51yBwzq5n3agBgYD14H8UKKLiVbDXEx2SnbGbFn_aWwKBZGc6-zdAi81D1SfDZSJyp92ldQezL6gvBNbxI9mj2UKwKctT1SUUrs9_zKZ0YzfKOFfJCFQVA2aE3ljsMH3HJTpRSUMGmq7yUsFmQTwVYRRXkSaorx4msO0gysZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=sX_KZsfRuL-PxbH5aCkbM2F8yXNojW5njW_zcykeq3e-D151Ei4axiSLkpnVbarlfqUlW1egi0XQkcl2m_yLDMcP4pEYmFBFQrG5NEgLyLoLz2diKyBeJipXLP8L73HP7Se_8oJ4CHnytBr4QM93IiDoq8Fc01JJSnY6pRxQGhROu7nNyXXmVR-NGvverQboKR3SXUkEDEn54khtAgwbNi89sjgJ2KdhH2OfVPzvgNfzcmJVg2Y5gPq6OWVKFERxQjODi9ZuBzcW1FpJlgmQAX790EiQnUkRqigXYkLrtPp0s6tdV8LHzCfUlD1ZHmtnDuTNuZSX4srYqsoS0QLl5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=sX_KZsfRuL-PxbH5aCkbM2F8yXNojW5njW_zcykeq3e-D151Ei4axiSLkpnVbarlfqUlW1egi0XQkcl2m_yLDMcP4pEYmFBFQrG5NEgLyLoLz2diKyBeJipXLP8L73HP7Se_8oJ4CHnytBr4QM93IiDoq8Fc01JJSnY6pRxQGhROu7nNyXXmVR-NGvverQboKR3SXUkEDEn54khtAgwbNi89sjgJ2KdhH2OfVPzvgNfzcmJVg2Y5gPq6OWVKFERxQjODi9ZuBzcW1FpJlgmQAX790EiQnUkRqigXYkLrtPp0s6tdV8LHzCfUlD1ZHmtnDuTNuZSX4srYqsoS0QLl5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdaK7jhl2uw3gNsws2HOdV2igU5AyVnh8BrV9BcdcUwWDziW07CfJjv9CNI41i9RwFQWwCr1KS6tZ8GjIKW0474188VJLiSn9ktoLyVQEqV_WZsgCCaFsVDnjAK3cYBb6wnEHbv1f2GloJoIPlX8MAHBBROx1iL_niyI2WCBvESKqeUOGpmngAOxFp2RnY0DqIw3_xlhwIFmf-uMTG-XsgExWPziQMreemkSAjkYhMz9fVaNb909Vzs_0iOEN-dyIMBytYg1c5xmTw6blKevt2vYWisDp9FiLJq53n1-gyL6PdwxfDs3mg32jmHBQT0fsFQQ3XdXyJSzbmGXH_F0oA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0SGA-MN-RlZPg68zB6eJu5leExQ7S_Kcl_O-Wur2I2RqA0Ip6UHPkRr3jN642lADIMN4PtRA3885sD0OlzH9vqy_BNfuLM5cbRhHRNHtmXYlC92-YMl3mScpOI0t2AqKHTsqK-4l6NFmQtevZsaiUGgRdBVwU1ajilHBKshKfvfGVLlDozgl9zZdK1U3e8weOXIGXzmeciTiK1IpXr2l1zVXIgQhKYul6WPPrnVHNUNS3p3Gdv10jXW3jodjpx1nvG7y9y6MwnRM_Cec62fImfPuVM01rBLcZ1MYL6KNi2mpw3Ot2nCtKXm6znHDApRx0DjxosqWHpS3cA7G7llmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jvwPrX65zC8gKoivk5ho9NdIdh4EPIiIzhdN_ZAOJWAIUF488NXeP_1jgRXq55dcj0X8H5qy19g71QoYwnFRudTG57j8E9_YC0hJWuyD6lPVUJnvx-f3AesEgg5GIiYgARATOLc2yYQDBGQe-7qo_ssGQZuidxV3Lg1G60AE3kbaJU0TInNH0gSqhZFRGtxWIKSfGW0ZBhDPfeP6ZUWSCy-cdKTt91ooDV_sEMPHqxePoMJ-VFiGs42F0EtnDhhiQeWpA514orGoXbzjH8082eG-mbCFOLW9-2Qj9qK6RHHJOe00cTnN5E4--M2041SgwTDILLRud0jIeUDCsbjtoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA8MdZwtzThLPYtPApPnHFTkfRfHfy7760oWuNSG_brt7Fv_fNKHDY3AHCiiVGGWzLeVJzHfZi6Id8sLnV-lrCNumhcyvY85d7w5-tq9Qr0PDzNYhqwgk8uvXeYsibeGlDM7sA6NJNEP68Vwaq5wJkWjuydQ6994CYnuotRhvhwiCUjC6yaRcp4JyJ5B8Fo4aT_R7PDjBvFDQMlMLc8J-pziddORiTGjhsI0SNEDhG7tQjir1Cck8Eho_om83MjV_zAqfOYabhz4Q3xY1Koe3uZyWh60aK2b_pNfcK9g9cl_TIJZybyMY1QmnSp-trI6wykT6Drz6Q3Er8u9BENYWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbaDpp0OCNf6eHTaP2VbJhWjqKNO-GaYnGc-tpFiHpAsbtwbx1ozYFpcXajwt1gBUU0Fbg0-QndX5yFBsPxTk4YVQMiQDJmZ59HS3ZhX7_KJx5c6_Zeb9yFQjZRom4KpmGhvnVajz5h9OET54OfHZzTEbg80RTMg2n8vDxiy6QvxO3C8HC62Adby_KWbL80ypqtc-ZHDKPt1YIoqLqcscXeJuww4Jr2W6Y6FbVAUCSQFid7efKk3t3CzgkouN09BI-BvtYPDy1wYAymnBZ209tMoscKiHKQTvYTHYB9zqs0KlCetDO6dRrMg76T0Qy1hYk0F6aUvoRS3kEXneyXhXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/csJMSFxmeQ2a2JUR5w6J6xLM40fukMVDNqlrdLUbAgiS6M3xMLdc46ZN_5UeZK3KBXaxZJfZ1AkBgQv60Q9XL1cN35nM4fqtHzO3W1zoagWZmmL2OTaIV6OMtC0LcizubKEykEwzYxbK-HIFPzPOtpCq1nMeZN6G0_VIZze8HTeDQwetZeEmzJ5g29q-HySvkyBWLXDSvyzIsdZZFBFyKWU6owTP_9Qz0tg7yM3A8Y5Uvvwu5bYoF4KQ6yOsp8_Oh7YWRI_xTwAPAnLupQNZjljnqpNN-euGJH8jZathx43EMY4C1becUsizat2TAURmL0EE8Hl-m2hd5i18_K4Ygg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdmSbIysH14wLsogHiUmojO8S3uUsHiYUn_TXCOWvz0U85f7u5oovZcD5IAs8eDBo2e9eVGK-2lAi7yVrh6Bpm67FyTCRYmCLw-OyQwa02pZ7o_34rRoz-awrldXwrFlXaWxGamdkiq3DeI-sHKYBYRr-I4l4HGPB_ZnBR4IEE08bPbMcnsSotfcuez-2tF4e3wHiZqOMeXexOAInTKY9T_fybv3bmPMQQc7BesQJXDk4FRcaOfM9_jlKdp4_eGrKXvSr_YkmtFi9e6B5vq4jibE82zGd-aFMKUE0VmPXYIHgEOXdn_w3XgF6kO4Tt4c953dD3nS2BacBKJCT3r_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfQCS6AvjKUPW42bU4G-956TjDd0uyfRMbEYretpP5SYxcHCtY574FeJQoptdzGMsWF7Cr9DZXMwT2sgs-LzQuhz27NtaYMQJI8gkbrDoY-kf9U9grhLglJp4_7iScr7Wlasffue9slJ6ks9rQJ72nHdgSzEJ5dHr0sme_PrheVzb7FtOsliLbaHCFTfg8Gx8Y8WaoGeIg2OZvR8H8TPvNHX8XuBPcVx3CkqEeiJbnIMBoOyrd6ouptVDr5jKVHw0AbzkfoFuKxI17oimcOnGnfNfU8NqQnRXjRT5W_Ap0MiY_N6fpR6Yg7ULaGuLaPxPsk9K-ZrEr7HORDQ__FMTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gMtvvzKZzLGkC_IrOa2vFCPkLK0RLHC4C1fHp6h_XQaW6_jssJHo7QrHR5lu5nzu8xbNHsyTFm-Wawg74RJ396cXCOBqF68gNW61JcFWnvoQE6QuKIqCJwxHCDUgRlCvJMm0rfj8JFttova-c2qYgxaKjaaBTJ2uJ4KOFRO0of7YPfkh7Ib5p63fCaZSz9XPJgRbbyjS_fefOaNkOYu0NmJXsBKS1szhJCCqADC9DKajJHm2VKxqMV_M_wiFdZHMOjGZuL4rw3-fMM4Wdphj1KMd0A5JAg2vCgoI4bglM298Xw1OLNc-JsC43M1yswR1AmOHQSVNsUonj1HOSZQueQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iv8q1FnCYhjc0BVOwknab0M8vTtaWEx_ZZEHqI2fsgGjN5aANev9e_xd0y39qevEN4Wk6_UHAH6Mpr_PRIRmytMEFCfx68n7Wf_iRwNiQi93d7zDb8yDTkof3Oy1aY6sJ5tIsRtCP0LFy_8NKUgVy7Qh9a2S4_furtL2wAMD3DFxF5DtAiVjJjiPfOkQT8pgrYnsaGJSysGQHaFIUIWzYi2viAE-mfAsDsnLTmFufDc4_4F_Qud1Tgybx1NjQeUIdY_zrh89UGCdajvs6vJ5JEktQUMk41yarcbqr_K-SeD8K-X5zU0SDHOyy26Il1TF7ZiPVtvcYRHnQzECuupj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7yEgoD7huqJf9tPnVZ9iKBec1u-4ONSnvPS7IQSibz7nf6bYvKBaDZJD6Ox_aqwnYo_WkTD_kF16D5fDIUX63kSi5NCDvfAarus8Y4PGYKH7lgcDPTa8OjPSDYz0yBua9phxzCzgQVEy-7UlOEjspQVURIvXgvuUZjZc-MWxVJVEp5aYkSh328OkF1jcuO3cgdmSJKzYIAIgq_0GJEzEeKPonI65CQ3FU422Jm1uaV0hVDbo5guU6ZRUC982f9Mx5MPiZOp1RNx2E1Du63cAInp040FK0UatkoyVkmAEOsNxsOJP0p8a7pEI_tYNz32loW9nVNM61hGkhphGcVpiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A9jpGIniWriGuM4v5sN3qDwjJVut8uzTyoeRlIofaY0Fp93ygLgoVpljwuiXUI8AYy44_2y6plmBz10TKVbXS-gjanhtOXYvpfQHNczBExRiMq4L5Mn66_-s3L-SHriz_Ow4bGADPdBE4dqxTOPcZCpijo3vnstyeLVSBHv7tGx3-kivrsTCZUS6xQmg43lrvbUEKuX10JJdaqX_n46XUF41GDaQ9uWHtHapabsS1n3jsq9F1dYFNUHujVaxrXvAcMl3KRddMwxuFgxaY5KCv-H-f9v3_rJa2yQsLAnEIQjrQThEGFSVZNEz8LviRX6ZzaHqnOoz6-jMUtNcyl97oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t8W45AYepa0r8p3L7eRLifguzDXHZF2HEUl1PB0HVAjAVfLcnCW-1pkx7LgFh8799c27V1iNC9z_-grcOTw4BmkbgAMCC4Pa27KVp-Mrw8ytod0GoWFoYL7pErieZKE9ILGI6tkRSvLGSV1vbd6vKQUmA5rL-xlu5LHZ5o08JH0bUYA3tkzRs5Tbfp3w72njSX--jRLJ1dzd5NQSrjVnPJP8lVs6cIUExLibWyJdDZFDDNa5U-Ghgy44xbPNWMvtPUxSuu3EbUexqzaFLF1EgX4kdXoHjEHRAt_Fn4pjILBwP8E6o1UjVSKpD6Usxsnw0n6dYNEZ7BxhsO7HA4-qZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sc0mDV85mrCaYJLWhMykmeKHzoVmpIg8okFMximdYg5_5-wgWZapjVY4QvfVxc9hUVNDzc9aRdOEgHbPYaUotALuwSV477zXIU2CTz2RGznH3FTxfDp07ZcSQcRtWAYW1YH5D12zA-2WTcHroJch5IjhptVHKdC8TzNw-MEuiv8iz2bw9-RTO9v4QhdPpKWvsOoLdXIeQB0h2iz4crljtsT6MY7EcqcYQGWrLhyT65su5gYjaPdNCQmWt-NEkQ3NiwFSmD-GN0x_6CUUXRARqZsxIHHcYp1LjV8bP92Q0aiGl5zMjbUDKlKCW1XzyBe8daGM33wrDsgx1mIRDZYGPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=DDIi9EtWLqPP9WJJ--Vk9DZJiMhY_wxv5CBECFDFcV0i0BvF3LuZXENFf3wlufOpGjdQTfV_bYvWLEea9KmH2K_HhV0wK9d1s5SNopDKdQ8u0SmblWwydAEBcbYKYCSP6EMSbW0XRtGEiOYOvitKHfRXyaLSimeh-wAc6VAEKWzjzh_uo2IVG1AMYsiDB2jdNZ7YrdL2XfnRAWjDHpeCcAq8ei7QpV2NkVFM3w74BFZmnekphtXCpGSP-WD4vyfJUWZYTZ4Xq7bMsKwnvJUXSzpnGX1eAvHXX9-b8Ytmbi8_9awrj5MYjdPgHdmQ9pn7sGGmGuQbv7vetmzSdkJyrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=DDIi9EtWLqPP9WJJ--Vk9DZJiMhY_wxv5CBECFDFcV0i0BvF3LuZXENFf3wlufOpGjdQTfV_bYvWLEea9KmH2K_HhV0wK9d1s5SNopDKdQ8u0SmblWwydAEBcbYKYCSP6EMSbW0XRtGEiOYOvitKHfRXyaLSimeh-wAc6VAEKWzjzh_uo2IVG1AMYsiDB2jdNZ7YrdL2XfnRAWjDHpeCcAq8ei7QpV2NkVFM3w74BFZmnekphtXCpGSP-WD4vyfJUWZYTZ4Xq7bMsKwnvJUXSzpnGX1eAvHXX9-b8Ytmbi8_9awrj5MYjdPgHdmQ9pn7sGGmGuQbv7vetmzSdkJyrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V1Mvw0VF9yKsvwo3XMNWkdg7LLlTIeMAbLxby69VrrmVsqS_3eoGsN-rPACLF7C1RW_j4aav6Qd9N40_hq2DErJkCJjS7Per4KKAq2PVSFzcD_-3XUW7zo17azWCSeVFLvNDwUaT4BuDGj3X06EWlic_JqKBm1VXpA-BElTi_tywuSji0JkDD1yjYpMKZ5bA9P42sEfNkT2nH99wI92oxA9J_1pkO7hCMtnKIq_yR8NUWo7my5fPy6MbP5J4wbGGq2JOZkzmiD2AbU7LXhRWIao9Cz_7y8o98IYiE1DSeQo9oJU22c2CpgeVjjutyTud5dF6Rg-gpzxUul9OyUQu0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkn2oOPAAkm--eHEtC4hodvVJ3u5RVCsyZxjqUaD2L9PZ_ni9f29-4cDZtD8bIt5Kd-RoNAnIEfJGYy0S7IJ3iY7On6D0eyx9AmSvP5HfFNFkekfck39KrdywTOTRRI3u0MnMDEIYivOxhDo0cy9o8c9jL77h4P7HqjTeJCRD5jyWuOvOR2EKFJyltCGRI_3-n0S-Z0vV59AsTy6ScNqtz3LOk_5grOAGDuiLFNFHZmlKiuOjVTYzjZHhuJKdARkGWGKnF2gPRD2_FFJ2yV290SDO3iZB79bvYXX0Etl98JD3VYtDhi7b1qCwL1b7fZHzoRJYKrJGRNLCrl3f8CpvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAtrAP2T43sUJ4WNda-6f78fIX-sNOoXxSC-93mGvqFs_8w-_IwnZaItIyFUkbKVr11zpBSpxmSLoa-9pdvcRzcpqBcXfCxDIax2mcZLnSFRNvNRXzNS2Oh2Vqdj8cS9oQHspsPtK6oo3RnWvmwy4R88_V3JTBnyNWqm3w00RH4Fn6iolIvMogj0sO4rwshbgiKlLRThwLlQP3QEXI1DquL0VtPw1h6zgbyDot9XyBA5HaZzAKWcmEJ3SA8hXwrq7xv2eKfHqNZUwoLu3MYMUYFqvxLgJSYK2T6Eh_B7PxZ73P3r8gL6XFZT8XriyghupQcT0t_AshjcZa7CPrRyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KCa8521npHG4xfkB3d2W7GqBnzHxMtP-XydutOCGe_iE82aSZDwzZTBpMyWjUEqQYP4a4f7P8fPfma9xgffqx588ly1vRoXETlBTGAMpXgVLIbcSQNq7LbGmL5uHl1d1HBXAzD7n3jfKNT_aNa7sFqptBD0XMsMBXHIp8PoL2LIMmvmDjvRt0ZBW2kslgI8PmNjXseTyN9YeGZOveOuzv4JFO08fQF5-GUCINh49Eyf1Ru5fBAy8dKrkIUrde6QeQct1hoFWVL0Myae2Uazd14bH17WYj3p9bbyEMY4QGwZhoiyGsARgXk4qrDcGUWy681RLKnuGHLgqOo4AsNrxrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=iIG9ecS2YxE3vL7JTdipky9KhKGpgD0jPAV384ZnXP3BEMCOC14oHrufEoAgbF_M0-K8xeBTBZdZSBf-ZKwVMb2aLhnYWzG7AUy0Wgqv0UQqj6MmLWbzyRTxM5ckXw-CTP_ipH6mZRT-NJIl0Yj31iVfwplimSN7AC96FCcLQX96PD1MJGKP0UVJRFIPJ3bI4gyePGJocruB3Ynwf43pO2MDz7Qhnb3Ynah5IEP9Ist3JxWxNxSJ7k4D9Onq37pRl1hosayICssp7Vj2yveO86UxnyksW6XYWzHy2W0hnI5VDxiqv-TbvaDKQ9p20hd2XoUjMRKcYoZKxqy85UkNiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=iIG9ecS2YxE3vL7JTdipky9KhKGpgD0jPAV384ZnXP3BEMCOC14oHrufEoAgbF_M0-K8xeBTBZdZSBf-ZKwVMb2aLhnYWzG7AUy0Wgqv0UQqj6MmLWbzyRTxM5ckXw-CTP_ipH6mZRT-NJIl0Yj31iVfwplimSN7AC96FCcLQX96PD1MJGKP0UVJRFIPJ3bI4gyePGJocruB3Ynwf43pO2MDz7Qhnb3Ynah5IEP9Ist3JxWxNxSJ7k4D9Onq37pRl1hosayICssp7Vj2yveO86UxnyksW6XYWzHy2W0hnI5VDxiqv-TbvaDKQ9p20hd2XoUjMRKcYoZKxqy85UkNiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29087">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MW1YLe5NeWFe8QE9GG-es9_l-W06FIqd7LSEU8YVt-JrSCKSNtahF1m3wLT8bXFnuQ6efh6iszlQ5jeGz0Uq__6CPqKJWYT5c1s0OWxEMWMn6UGzh8J2F64HjdUSunfsNSuGAqfFkLU5ihtOQaJt7m2IFZXciNHYmZwqDlRL9-XWMgEO2Y34U7l6ffQNF0VVUVdpISLzigNtZYLyWqL4tnJZYBSYG2683Fpwenvvsw3SWgFobPM-HahJruXB5VKaGc-EKHI6h5JJgmYkfjc6gMxdKxXKH4DRn2q9Mhtom_ijIA7y8xWhMM-27bJNBYp-__eLRtbqk-Hgz3wS21Ddfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
🎰
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/29087" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Usf9v__LQYU3Xz-CW-1oJbaA167ocT3_1mTgF4cprxN7UwEFBfHsawkI3pd5LaPn3EjC2ZILPSJCaoBd-mfAm9KuZpJdHhyl1OiYJuc_8s2yuA68P1uZOzkm12aWu6S-xABfp0uleeui6mdamz3N0x4IsXo-1qbd2xrGOhi3XurHG6K0KCTrlTi61tW2P2CR3Z0boa0m8-ZxfkhiyskEYjIvsBeW9TndZkzah4Kzljkyq6_EHOP54jBd3hBVMNv_tdSBh37zLbmLDWGuEC0WUB7jmekanCrmBpbS_Fk6GheTsNGvdG49G5MZlR1FaPOBbO9v63kChUnK0QRaT98USw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyEKdvvS1w2qrJ0LiAZGYgZeqZHLl66MLv0y7663aYvmo9lMs7TOz3_1DcPLzkvCuAifJHDipMFrk3F6Uy5K1TKh301_LRY31hiQ4PosQTrEkCycVrwfkXa0LUjRjywz19yCxqvfkUuK1UrAicH5_Rc4oD5yiLgshpvzw-VdpyzYMFJbluFlUgi5HyBKHZaCdAlWMNWS57mgGa2YeIJrdYl5wFFKyBww9iN1OpLouUjsolm6cghgfDpUuh3h81BknpTl9hqRS17Fuhef5NhJNB7gNixn7hY2dhBJv4DZWOrq3_3NI66RpL5uPhTGBiLrKHDxF-UeIQrEwNPQuXKMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kOtHMkpYOmm2wbNYr4ZKh56rpbK8Xh-UCc06NgegYgwNIuZN9FvFh5d7V4C5WUXpwEoWLupfgSidJJo5Oj8AYjPak678UMAto3miJ7pxJ-uQg4Po-Bnojv8_EXXwRE7Ir1uOk48z5UnA9x6W3UgOxHdsZLCXON6LqVtoGhSUANXCry2gmi060XVVa9GqQ3ygSg2Gu7kSJIJbQOcI0ZzpfEbQ1IMtDl7fxC06dAVcWf-gqdwQY-0T3ZOCtVtACgOLNTrRLIIlj-RnSlIbqbDzBRmHniBGg3R8_Y1ch_pSLvQAwKS8ocxPfRZ8nyDowK8Qe9MHhu2q_nv8WAWi1bCmEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pH7934e0rVDon5l4OIXhMstfa_GHUau--Bzo4y_d9j09XZ5xQ9RgWw1MtrvOaMa2DhUGHMapMlFCTuvOgJTj6YJVwK6rUkQy4x0obp1Mxg0boS7Vjg9Ne5emU1bJiR2PfKaQK-jSIrZS_7VwLGpBTCQk3jR7aSQKfznDBlD4ACzfIfHPbqMHGW5qgT_Sj3zjWCm26buivcK_0Fu23DsjxjAkQ_d3l9hhK9pHhbOfxeVwNVVWss4Zh4iiAg_T8ReM1Jq1W2rSRYkCEEXS7a2EHmCQeKMVRweT6gPvij_wFW8xGbc6e_hRDz0QrV_NsNNoN8OSgI0NY0scniROmP9dog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 85.3K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyNMPU-1uw9SleeCewqBop8FKTOg7L25FHSS-vcZ_2XItR3QhkTg7jHBCQfyIzYAJqvyzDqc7edK78ZWoT72Xy4DcLW62VZ6nbh_Aanc5O75fHN55XsMskUu_obMprek4ISXU726qlBNTcRKsbolMB8IIau_QjHV2N7Kkq-2ikWIWjXLWgylPXd7TjqOXXUSGaYqLsH9R0D3GW2FEFFItHmM4-W6t2w9VKfS38LV5oHBHjIxOjNdjAiEOROayaqd1Tb2aQCOsKkaihq6Aw2XaH2g0Fyeq-Nn3p9GL3OcHm8aWk9nSWDqvineZtwpWmFN_2WxW3Lu4VZCli8lvuFJUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 78.6K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QlcWcw_KDa6OTm1IQ-pVGLjK-7HYi1ZfzXo1yISZWyTx9d3NiGqOh6kUAUYgob1WKsanQ6YQqsHMDw5bN4GZ6NoLiG--DRV7XyEelCLvovu966hZf73pMh8bL1yKHUiOjajnc3xu_2ijfUKUIVt6GG3k_J-vkYhNgLIQ9RizNl8Kojj6YxBTepmHHY8xtW2D27QLqC4PBLWPJIJrx5LlcibOtFiAS8Tv5KMp-JEG3dQC9fCVQbjbZUwlOAnoPYn8hSAR-vaw6kWeK9qx8Fu_oDLx9DH4TrrRTCWUfm3E7S08QHZKV4qDuZ_RX8-1J3NgepCHZnElPmmefCe1M_GVEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 81.5K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lvnrP_1B4F7LToMQMPiwT9p_hV6SA064UKUTZnVdbl1SoMiVsOhSoS9zRsLMpxfKw0U_FUEtUsF-cIKAfWptKZOZ-hotmftnjZMwKB4K7A3uohSSeHG9MHcD9nT0o6IrJLPUDq5xfh4MpHO0wk09gmBHp2V_dkE9U2WwjycPR-YcRpN8mbhqomKHuR12aSlM6kxjUWEoGoT4JO4_Lk5-t6diRMSvpbYTlhiMxb0hQEHy85Ectt7jlLwA660Tmwl3Eg4i70-lhNzKxW4SvdXOhyQ2OfRD4upRnUxr13_OOiqIkZhL_FbrlSFIX7MZ5ePdwqnFuPWLvGJqCDFF1KKn4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 98.4K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fox8eOTjMIoFUiv_zoM5tmkY_gkr4KfMNpItWO5IzM9u5AMdmYXm4HtOwFo7iZmca3b7Xj50nLHe_4-S2PCDzUVL8PU8_AxQMZ3Ti3FG4BuzPfbqI32hJOPgoJnwlOVOvboMiYOsDFH7lUZZVjnpvCayDWNeq88eiTM9Yw0wtSCiRtWiwg1HnOezzEZ6lIGwLj_vJ6y6izp5ebeWV3zHmyK4hZAxVuzJVxxJkbuo0R1nngIgaofsr5FexGblxm34LAgZ1SDFsPh-cemBdEkUcFvFGdc4EagmEkGk2thQtfoRcsC3NuZF_EWp2HacZ0cd-lBsBtX3j3MPYH6Mnvcxxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 95.2K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXcsoExIyeUWcVq5PXAp5sjr4-kICxzJ-7-dPOBeoQcLsFEi9y6M9gujzbwZkBvUAnfTRCgejhLD2U3_s3zre5zjlbRjGx0vTb-d9sPY4n58v-CaYhGsEwurknbaxaomF4GluXtIswyRxiIlUc2pyeo66sah8xDFy7ZlqDOtCe8cbx2a1PTNSD8pzFNdP-z2Cbf5GOeYwUQbI3g_TaxBdaBdcyeAoy4thOAriUwFKI99xOkdc4b6q0kCwaDa49XbxtlUwiKCEcy1UJfaUpQVR8yW2Y0UIXIiEheyAtxARq_kti3rbU51eKhXgNOhFdIRIHDrQpURNVhg0uFMHQrVlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.1K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pPyRKVZU4eJfg4Don2kP4SUCr8Zpa2vQAuhUR9UYAtfFT-zHlcdCC46lu0hpbZTdakJafqSops1E7CiaEhjVexUYMJRQBzDAgOBsbg-dqPSVZMKVjbp7ubSecf7x31JzJwTrOQQZuqLYbuzyRhYig0JqrTXa4Gav8iqAd0YQju9x3dQI3kgZqqbV4_mVUqPfKz9gRwOAUQtJqpLtVgjBMUfk7ZA5chs3UhvBJfkzCBDujUPHYa5I4sV3J--Z7B-KHurGjjenNna1CovSx-kgWYrM1oDPy0gT-udfe2rwNspGw6uYMZ7n9fmwMhaJX-iA-1HcyVOsdn8j4RM7EjxjpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahfz09MCBCy83fpD4mxnLjKFYexvKomc9VUhEGgW8swOJnT6iEu-DGV8V087F9def6zpllY0gecy314su0GRbdMltpEjI3woSGiuOGAdr_v58ykz-IhXdBQy0-QGAm-TrJmc8GEw9cRbQDm3hH52NAEX9E1B_Ki7OwDUqyByYOPIT4IOH3HfflFvBXpApMhWBeVMLGJv8Yuf9Y4-BgMNtok1sZl6wTahu2Btbml_VG55s1YniGVFIrQsHQMKEW_Az7Beftf9oe9euFgVNly2r7AGa5uJgVVPYm5EfzSPycBTJsYk6Q542n4XiZ1DZ23-7mSTtPAyM4_VOBsQ1-rOtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1_2CdR3WjLrhCoUVhlqXdTrg7gYi7w-6QurLeL39iL9HYUatyw3qf1ivrkv-EPwS2LjlBlius0DrePcq1pZpvpr8dlwzhCbkadpGyq0pTDiSRarzVh2cv_90yx-0Q8C-e8lz0HSSbaqL51vMr49nUKYtHB6BiXX3VOni8fblcA62uO1YgKKq1X8UcdWspX0DQ2rTSaBEaoUI2c9-iIOVwKxW7fyolw22q9HEWwTqPRHB3J5FaxNaFM0gCQdJej1rXFUcb20V_8RtXUzL2cdwaSZb84NjKIE1UGAms3kZjYWrgpf-l-UHKmX-hDSaE-jtQGKaO-tFjq9dC7BODO0qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RQStqmDkAVE62GXghqIjDQubviPv35KeapiMJNgrr-TkG1Vja79UwYTsOe0IRU4yTug8CfpsH3JQDGrJhKWE1CQ9eWagaHc6VLsVPAB51USGAjiuvYYo32DU_fRBZw4uXcekVmYkB1mcDLz2IJ60K9ggGeL_YGVNCavWGFRwMMfpJ7iJJY_m_NFSB0ZzJmT8d14RVPj-Y3RKkftqzKE816GZi-MyVlSzbKog5eOEy1c7tRFvtwTFqqLZ9kwiV-pbEyxObeeyoDJ6gPAAjvxSpqXZ40iyrLpZGbiHFmR_nh-tCE4QtZX05OWLmajjsJ_ltwLjrOR0ArVRpV1nxSr-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MlkBUf_vnw6cx_d0wNcD6xaIl7_6hY7fZnhhsrGJZjCL5m4gFM_MzfBFYymC9l6bztN_t8AHcTZvJ-jJZD6ThChxpO3PI4xceqXw5K2MNR6EfCUSE5QNkkXPFHXqJOncWx8TZhghqOvINBtopqum_wAphNXHwa4WHnFmuFuOS6oCLAtHX-SQauX0_GTKQ3DR9IZ1MaAEwjkVAxuklOAjsy95xKYqvI2_H8-7-F7JTFvmVTtOfrd0W-TSeHKx7FjqRwIA3z2fn00C2imhXFlLA3oRZ-qqwi4jlxThk30ySMmg0gOG-_A5VW1i_u6vVbgpQEDXb3gefdDsCePZezk1og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEb-SMg12fZL0GKa8LoeXukid-VnUnvMoCg0oQzuN-7-L9FIWGlXT0BbBHZyKvez3NESX1WiMNyBEOqKfrykQIRFRidUOOP96qT6ZtrBfvkZax0nnbivQXv57ejSN4VPhHIeZGIJuNfG23X5ldVovb6fAYBUW5meEC8uanN-b7_wcqZbLFEwGm8-J7M2NTTMopNJdph2Fhq2sL-8_e4_e8R7zM7S1H5ETXhWvf-NL6zXZnnFUe6zlsZ2Z24PKmjbxMiO0DyqPQy5YbK2pqleAJ_P7kp-e1XOhbiDnapNLU2MfG2SpyyyOPAokxJAD45AORUO5B_x6ngqZbO9x7R5gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grpWCr_x5RxoBDMUtvTznk_CYxi9MiUEdR3Ev201bcA1vapga8fuNNI89XCfaTm2IQCM-IKNj-5TJ-3Xk8QUajBTsBZN58uMN1UltSc47P7_kDbU6Ym72XtZx9M9_QTvH0nH_dtp19LUSZBdRZREHtrpgBQn-Z_UKz5RF14qFOLYlfhBPr09hoiBc9aOBTlphXqZqX_RxNrf3_EF2EZvffYqezVSCVobt6odNyaBcBqjeRZNk85Qlu1RXyzzQ22MKM1C64cK-6DIV5rFA2F9w_u-aMT6_7NKYMiDqtxxfV0dWHSmRaFncWTokCa0p0UsyQQOsZ4p5z7rocLR9CQKcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcEHJR8YV45hv2_GbVibzbf_FcxERwBx7EgqHxp0jzcuc023TskIrBwUDrzLfgFCqpIaoj8OFNFnICqNW24cLDzqUep9NgW6WsDYrJzyLWg470HXZmrZxGKLl1UEvtaH2IPfP-6SXo-WD7QnjETnqk6PgsqetO3DJ9WXPXjY-f6x1-hODySKAQskf_lr01-DZ6Da43iQxOyDx-ybE13AxQjeDv7tuNVu2WJdxopOJE9RBt73Y-PxgdPBQE1BUai_snfs8n-dpG4Y5h4vIdsQqmcRDT2oBFV08L_pelPWFYTPcENCJyxUvS6ai0h_SroVbiOGMhmT9qJyE6TL1K-RFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XuudGUFU6DsNVZTQB7bhiy57pMMtvB_ReRVxaAL7gxeZlOXhJ2P3Ii1xuDCeZ5Iz_p45oi8fXtTx9f4VQQF2U7hoEZ2zl3Vk8LZ_N3vpfSqAyGGlbAU2UGNmQFXv12z0rA82WqBQFFMqglK5m06y1xLMyQEI0fv8GzGA4DeNczEkK3183_U91lseKxDieiNqee_1Im17jbU8WowlFzPZZinpn6w7IHOYJ254-zB1qxPpnW-BBwMfsB1Bgupktg5ucQ2NBav9WuStybSxZl0H2adXqTE9d-wOX1hhrRqudbsfgBQUOGNaf_YroyQoEPMDoN8hP1au2Yqf-_306aS3Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQaOjCffa-do6qTA0WhZqyj1u-GXMJ8X6ZtWZXi1weMtlgAIj-ttA9lbktQTK6jmjsOiF83KQCoivmxwraJVGp4idDimvXYyiKuc3WyEYYwu8XtiLhyfoJkGHXilBWLVpS8dZX6iIXCo3G5uhJKplo6ISlQxhcO8MwnyLM5ZPXEM1kmfI1NVKOzU0m_1IqYQ5gGNSUomiOP7KbuORoaO9JXLuYAV7wBualdUbV9PDKkznDZBidmvQoRHTp4YfzT9WpVFZY8lkQzm-tWjOijlptsiG7OZTK__m6WThQK7dNLFNof3b1Ryy0Nk5dcVZtpPPZTQ-1Xm0koJ8FDDWmV3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwQHHZJ4lnu1aoahO5E0pSASjEljIx_ZQXuYvgaTFDtoRm3ZeofXReB71DJUNiJGb4SgbrPlKtBuUTstVD7CPSISXLIQJ0lzluZPPmEiw3L1gW3PYaMhFgIgFRjGD0gFZ-R3c2Qhd6XT6rBgdgSEynPB-NAZJwRpdaybozI2vkyozriHZK-x1HAq8hZDN6nqyH0yEGfPrBSx3F-NyPfr0LT9ZqW_mBX6vf7102-6tqhDbmL8rd80EkOgVBWhm0ZiElce2zOdz85gdwc-tDmQZIt9lXVMzVlhj5Qe0nA203-SqZYnZvdYu-PznMxE8eBb4SOsxQH3UIe7Oxtq9UOF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/usifjvW7tlu-9Fu3hev0Wk5vDOvFMt11y95H8IMpRq7swF_UUuwBymA17tj1PBDEC9GR7_vhmSsp4ikyFFlv7JvK6gjwQ6KM-xuSWDcbvw9N60YXYWbQqwqTwM6L36IPHFOtM1mIWwrREPRA1P70y6JRFl5y_KSX72AO54waWGAg0tAdTGmklshQVPX7-SOGWPjfglur-PrftQcxIEypOObHeqg1RGas5G2qqTlP3Y-N3ICvlYyu_XmIyWL8YnRVWK2Mgh8HOccmWfH1yEdpF2zJ6Ar6VPKe1jtUeKI8Am3bEr5_wiR0hE0yEtJw8X2JxPpt4Y0EKiuwPJK0YuBZTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lA4bpehoJ54P7bWXb6P4j-wFesxT5vKTOiwHN0ppAXtz2OmrT6S2SqDHsZbCgSg1LLyIx0jlv64xUd-D8WYkDWTSiQW3tEyFkkKvfXiwFswcanwRqnREuQiqV6BhTeml-pKzRI9LJtrs-RdpqQR1By2DnE-Ft3dxdaSA1fNQ5m5rsvwjQUy36enAbGwJwXmV-AYN8e2GC5OBXpRkCv7VlwKGkj-3iYHaxuEYjQR_GYwXYY9OEXvomPDLOBlljquyxM3QjRO5T3d9psMEqy2aUWVJOEIQXWu7QPJDS_mowbuBtOhlzxVCyJ5aQoEhoxhRPMkFeKfmVrowpCJVH5IIaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=P5u_sQnVAzlBjsSNisO-juuhAGYYse3oOlbJrQbgwlVgwJ17Z32GiCFaCxhkjEVhjp1JvY5XiSWtUEc3CaPUILGWGcrqfWxSSwg9I833ZApQqCsCamOk3X49p3teryL3Qh-7zTos6tBM-9m7X3LU8UwRWqFwl0ptLFda4Rju72R75iI0TrlEsyJ7LMHptSm6TzMm1KrUapzshBBNDPetXHT5egKLckk8cM6kelvdwF_pOQI6ROEAwoe_zwSFRsspp2Dm7OSR37UsSpxDNlUElxYTZsxLTm1tYctTnUJKI1RJFGQojNAXAzNriW2JeIk0UPIF4WmjHltctO5kR2Lctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=P5u_sQnVAzlBjsSNisO-juuhAGYYse3oOlbJrQbgwlVgwJ17Z32GiCFaCxhkjEVhjp1JvY5XiSWtUEc3CaPUILGWGcrqfWxSSwg9I833ZApQqCsCamOk3X49p3teryL3Qh-7zTos6tBM-9m7X3LU8UwRWqFwl0ptLFda4Rju72R75iI0TrlEsyJ7LMHptSm6TzMm1KrUapzshBBNDPetXHT5egKLckk8cM6kelvdwF_pOQI6ROEAwoe_zwSFRsspp2Dm7OSR37UsSpxDNlUElxYTZsxLTm1tYctTnUJKI1RJFGQojNAXAzNriW2JeIk0UPIF4WmjHltctO5kR2Lctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jKtNu9avv_QxTuzIyGqKoA64mhAuPQaixIg5hh-WeJxn87TR1wM4APfz_X9XZviRrNRxBXUxXu95Y_Q79Psi-G5HtE-V020crdJbORwjdrrsJjlxL2UxlGn0GAjMXTNVJpubFKP6MDFr6EqDQzJB9cOgnT7AE_Wyo4nMONJGWhqqlzOmnZvbQrhfyxg2oY2hYfJMHQoJ1OKTso8YvimDONX3NqlyEVqcB2g1ET5j90B8drRZtKSsa84HxgIcdVZHK7JQMhT3db_kl_Xb_fnOJhB0sIginHllZy2nZtbkz_NFrJ4dVlauBJSlCfBIqJBMwvdyhAv3tmatqm8W2iG1Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=nJ5ZLD3naII2E5fPK0Pfh6e7_diLnQ0gXavKKenKAYmQgwH5KvUDgXixWU4qbbegY1QRhk4_iaM9UPYuEjWnCULRVmpR2w2pbTXBlObC7n0Z_b2yCKsy29BPKNKI31ZmS3LIGt0tsnus-K1yqZNV_uioiTiHv75puXdlss_iHms0GvxTEGfSnZiMFxXd44nMmRyCCvNWjnIHCHXo3_XqXrPsutj9xSXOQPnGBqy447yzFSePNrIbYKGc-5RNF33EayluRD1QVznUU__duhqW-cfVAtaiZdSHd5gdDCtlBu8jyvV6T2ds1GxLUO0bJ_m0CbmaPzVFcb02avExgdHPLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=nJ5ZLD3naII2E5fPK0Pfh6e7_diLnQ0gXavKKenKAYmQgwH5KvUDgXixWU4qbbegY1QRhk4_iaM9UPYuEjWnCULRVmpR2w2pbTXBlObC7n0Z_b2yCKsy29BPKNKI31ZmS3LIGt0tsnus-K1yqZNV_uioiTiHv75puXdlss_iHms0GvxTEGfSnZiMFxXd44nMmRyCCvNWjnIHCHXo3_XqXrPsutj9xSXOQPnGBqy447yzFSePNrIbYKGc-5RNF33EayluRD1QVznUU__duhqW-cfVAtaiZdSHd5gdDCtlBu8jyvV6T2ds1GxLUO0bJ_m0CbmaPzVFcb02avExgdHPLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=lbWDqcEJ95rPtl_cfECPKH3zR58y4WPGRvoqNeXB2z3ur_h3scTQ1kHrH44eUfXOOzvVGJlDZ1O0K7vUv6bJ7_Sw4_UMz-647K_4YrPzJbi0eqkk7Pv2CQ4L0TH0Ps2Z8GE4oAKjO3_NC9hIeTbFI4vdk-eHK8BBb9tKsZ5J-EmmBuVtT7MTcuNTgOOUaBiPjwjYcHm3EEUsbv4WD6d8UrG09vM46Avn9qcX_LVAaYvoD2L68Xj-0RsspwvXvAsoSLtGKJpDaptU2GY5jCutoRaEwbl1SByQjjx0GICRqzw6tvaoN-gvrFeMcnsESVLn6wgjlmckPlH_s76zcupK3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=lbWDqcEJ95rPtl_cfECPKH3zR58y4WPGRvoqNeXB2z3ur_h3scTQ1kHrH44eUfXOOzvVGJlDZ1O0K7vUv6bJ7_Sw4_UMz-647K_4YrPzJbi0eqkk7Pv2CQ4L0TH0Ps2Z8GE4oAKjO3_NC9hIeTbFI4vdk-eHK8BBb9tKsZ5J-EmmBuVtT7MTcuNTgOOUaBiPjwjYcHm3EEUsbv4WD6d8UrG09vM46Avn9qcX_LVAaYvoD2L68Xj-0RsspwvXvAsoSLtGKJpDaptU2GY5jCutoRaEwbl1SByQjjx0GICRqzw6tvaoN-gvrFeMcnsESVLn6wgjlmckPlH_s76zcupK3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ngGhCoSv4cPiuf2ObD5X8fR79uc-YkBcNjMK7hJ-cxk30tGk5tmsgKf5BO7YhHEPOLPPsxWSQBJYvUEr4_L508ul7QPUH0Hmgk_-dUYIOnRncZ4MBEXBgIAAmdeyhcRy1OtzcCCT4TQKfcklIXqh1pTzFNOuo2ltLtZFPhAVY_kNgMVs49bECHwsuRGc1gcZgSu2CsW1pq8kFIPcXnEP8IOWxk-xZh3cHf14Z4YnxCdEoMykBHzLZOgEcPtvAFvvxVcRZD6H9tkfJm5M-7FzvrrNGuKp0uNSKjgYulnlk6rBEVbxoEG004ESOb1cSG9tkr4N9mo3U28QHZvDasJm_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JBFALc-uIZ5A9QLZpc9T8rCRxwrbci62ZYto-Xzk2h76OsjUsFhrmgjOLp4cI0C66TOdr82eilR48kQfgCytj675B42S3AK666TbAlrfNsZ6MclqZj-UBPpvaD_Vy8bXSvukCT6RYHfTnlFUplV1mt93mUf8RrsRA1EebSjsGIPN7APSVpeSqTJrC9bACPIVOTtmADRus66ZITBjabsvnkeEQAFCF9D7J69Bn25YU8WkFg9emLneHm2zW0zyX44Ru2bW1qZEqfHXt2RHB5BWxEDwa9pFS6xh8aiNVSADslMVYX0PlxD1Lp06AOqF6A5VVuO8XlcnQtm4whzQYp8hIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OdmQo7cUa6FcWsX_e_mc4cU7iKD9dxoGBs5BTXCrq1VCh4RH-2o1aWeqRUDntGfZyvfq1IXrPJC84wV7IRLfvEkYNRvZb6BHqlM1b8RA9z1oZnqV5TK5mbbBhLbJRfmF9o4Bcyjww9XHniGB1G7aF9yuSdtkz6F4YK-MjUxgkdfWXTr8dddDufdBwKKDDkWErzc4qbo7oIDSX4k0fm_1aG3ymX_FPplNG5KqpIOyvP9_IGm5P-AUZoQswUI0L_pvLG3CnOIusf6Sx2gtEq-YYLLGnDGzqdKdUceaum-gZiX6xy-gYdUCMjlnCMxAi64oTJtK7kJJezw4Y44bd51nrg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gk6KvcFbASfljGC_280bPL0e32QxZRYfJPgaAn75wRb5zXHZIM16GQ-1XUEjUTsgp2Xg_1FXhbeMiQKnxToBq7RXRfmpYMipO7Y-qgDt02kkVHqDP77ypqn9o2d0u-d5bIed5mx7VrPP6CwFGZ-gWL6owBJM_Nn5e3NQ4UmoSwXIo9l-d5_eOnaIknCtLzFBXDovJ729-Puvnl8Pcg6qONRxRiQhzVhx9uvUARwPyvDT6nSbNmJP27uaDmdBygGQfeF3fAwjPI5OgqPctVjvvFokyCJn3P-XNQouHQvj_ylLNMpfJfAr64Z2bP_GhZAjy_Ie7t-cRjGHStyK9frsAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=aj1lS93iEurvHCFUE8EIiQUnJXjNwoc2yrurIBKJdnRji6wKU4QUQfrJrQZqwgEeDcRrv4kRxwA8XCnvElxQWhePz6T_XrYzfJ1IJktn5xULYPtFPw0fxRKEOhhHOZearCBrTXT4Sdp47dUpucqArAQsFr-DZ4i0ocSZ5gO2Zs4GbeEIB7EpD5LUjxJtAYEfnNOETXPR3jnjAe5qOMXuRxLNSYV5iR1Bo7g1v-9f154Xy7q4qSVrfYZrsSf5rPxXnLI9r3rnq3n6q4aKu-oRL3P218MZQMNxvW0kkftq5e9EYUcPOGryzbPtrODdeFjmbBBP5ERVQI7Huc0wNbWwKBTGyybWLqICgvWne9DWMdRtrDDRzfUyLvbzxHEezU27AtThSERpI0rF-rX9ckf6fJW_yw_iUEoYrhckrg5lcwMwuOcnrI0P_YUlufkoRiod5bqpEFU2_afVkpDhKZz_iPTMpHJkGMq-Sy6MHU6RA3S8ic1oczLBAwOA8pB2JvvFLrsfQJt4IHwZ9-91-t2NkVY0XIqLN8calndWVXeZ4qs7UVmpFZxMjRnETuMgYNV__2HisdspeIP9cUTzRxsQ7RKVVHpgJOpyZn9a1_3xvw-nI02_QvHj2pcsRwMwU91DNredwvlzKb4pbPd_1GpxuryZHqn7-rUAo3eWEb5q0lA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=aj1lS93iEurvHCFUE8EIiQUnJXjNwoc2yrurIBKJdnRji6wKU4QUQfrJrQZqwgEeDcRrv4kRxwA8XCnvElxQWhePz6T_XrYzfJ1IJktn5xULYPtFPw0fxRKEOhhHOZearCBrTXT4Sdp47dUpucqArAQsFr-DZ4i0ocSZ5gO2Zs4GbeEIB7EpD5LUjxJtAYEfnNOETXPR3jnjAe5qOMXuRxLNSYV5iR1Bo7g1v-9f154Xy7q4qSVrfYZrsSf5rPxXnLI9r3rnq3n6q4aKu-oRL3P218MZQMNxvW0kkftq5e9EYUcPOGryzbPtrODdeFjmbBBP5ERVQI7Huc0wNbWwKBTGyybWLqICgvWne9DWMdRtrDDRzfUyLvbzxHEezU27AtThSERpI0rF-rX9ckf6fJW_yw_iUEoYrhckrg5lcwMwuOcnrI0P_YUlufkoRiod5bqpEFU2_afVkpDhKZz_iPTMpHJkGMq-Sy6MHU6RA3S8ic1oczLBAwOA8pB2JvvFLrsfQJt4IHwZ9-91-t2NkVY0XIqLN8calndWVXeZ4qs7UVmpFZxMjRnETuMgYNV__2HisdspeIP9cUTzRxsQ7RKVVHpgJOpyZn9a1_3xvw-nI02_QvHj2pcsRwMwU91DNredwvlzKb4pbPd_1GpxuryZHqn7-rUAo3eWEb5q0lA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=Qo2GnT5Tl1ify-qpnHFAn3JuJ8OZbro3S49tuHCebxjmPA1OW4_uh3WhIJId5_Cp2cJ97DhqQqDSiLtMbI0CZzb1I7dTVmQLIGuCGVC4VHXFN7hmg8EbV6Mefa7nskmGZRkdxCRQeMCXyYMWqXPlGvsa7zKxkMlUpIQkRGXgoPIHqN-KO6ioAaakBgYtOwK5nHoBOVtwG6nuYcUJFBS5FzuvIzcPJUePlOecEfqnut1G3r0inooxGWPmdGsp1ejR-MSYF12u1qgWno15rQsJeuAipk7vWrORTrkHl-zD2TyKLFHQJ-OMuKmaxlxGxiIgoU3x3cgsHCd138PQn6NHkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=Qo2GnT5Tl1ify-qpnHFAn3JuJ8OZbro3S49tuHCebxjmPA1OW4_uh3WhIJId5_Cp2cJ97DhqQqDSiLtMbI0CZzb1I7dTVmQLIGuCGVC4VHXFN7hmg8EbV6Mefa7nskmGZRkdxCRQeMCXyYMWqXPlGvsa7zKxkMlUpIQkRGXgoPIHqN-KO6ioAaakBgYtOwK5nHoBOVtwG6nuYcUJFBS5FzuvIzcPJUePlOecEfqnut1G3r0inooxGWPmdGsp1ejR-MSYF12u1qgWno15rQsJeuAipk7vWrORTrkHl-zD2TyKLFHQJ-OMuKmaxlxGxiIgoU3x3cgsHCd138PQn6NHkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nTw8pj5Hrlo5QRbpsNMVjru17-shAtMvCnZESqbnRMVFk7t8labSY5TZUAXUYB4bYMgUnVXEXo2EHs6Dnpi5_XpTk6QGw1bZZHPuYgQNnV_Bl-UCGKVYGlaY23A0kQMR1HwULE-LMZGXGHg8fYUrHayvLLdstALji6qRv5xCLH1G1qlv7zDaZYfjUQcvlQMfgYAqezcxt5REqhnpA0o9hzVElmXZUnQasMOiro5ToEWz7TkbYA38_VwPVYXhzwqhH1fSR9HFx_BuGriawkd3L9yd_HRgXB8D36Oi4BaVs7Su6j4PYzVaVa03s4WLzdicwZITp5rG6UWo09YosFVRiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPmSICQiLpizNo34J_onPlXgetVHogDSTFcKYmfqjfgfyEJDLJsvU-UJlcN7NkOwvm2e8rIaijCKXHO4sSwURsjPTHBFLjgP4K7XpaWkxFf359n3fSscG2X8vtnTHWh780mYGrCpkiqUVW4Q-IRVidCLTBw7lUVDZYTZ2F8sse0owbNhO7PYz-iD2YBfh2yL9yjWx3jGMtZlKPTrnFwtnJsFTPUOBPIzs1PAdBydFQV6YdqAIITguYhH7Uf6JwbsVQvpZ_4GAtuz9G0U8kit-1Aw2WlPK64h4_-Z9GFNVz5cp8LeldnUqwvkzs6hYYwKPAYXI5w2tXwSHWROoOjfBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RZoAuf_x9rpzULT4F2QmvzMuB9JNQX-P4FCj01Swoag3wTcyuKN1SzpiXunJMz0wigQW70p6l48wC_65lf1fE7XBomvDna5-6Ch1D8CZg-8OwDlQ3kyS8HGIaWo8zq3I-epSNovZCCDNi0MRVM3U_Gx-1ZdnA29Zx_eeXzAcqWKr6zpkzK-FgHoS2PY6T8ZU7_PuqAJluSfvwxaXX8eAYzHkhQMWGEInsDibOJSbTC4ydzrz9XrrFdmPIwR-0g1N0mN_XLpL6FBFblaoWbx7OXqobRfC4xjjSOTmyexzJ7kQom0wLnOjJzpT30k9A6dG_4Nv5bNe55O1wjeqsC6z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MhSPU6KzRnD3TDVm466B-9HY24jcv3Y_a6lazeP68zMBdw-quwwWmyBMkkwd1WYqF1Ohq7TqhjEioE8J0tVjglXGHHIZ3qazm2kRU7miYZ-4ku8eIA5hKY26e0wJWwchyjRypXBtQPbGOPUVUdtEHD9dTaqCHYFZYJ-Xeim6Fi2q921H5v1Im2euASRiO9u64tW-gw0H0VcS7XOZ6TMIntYSfMRFIz7b0TJLjtXpz0Vn0QqtNPrGdObjxg0P2uTOcsImMcuMXd8eyI_G_I8EWYQlnLWSzgD6SbcV4fl45hPDD7H7fK1ymTBgXvFIw-X3cEhizsi1gSb9_1RnKceWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p0XDnlLzZJ7GciRn2c_CfMVSB7nZcy1YrYfTCyXadA5a35kZotB4ICoXUGOHteueawZTfArdTeq2CPeWVJPzXz3wfOGs9R36-V9xLp2uYylDjjizZfwd2GwDZ-1L4LyO6nt_9pcNzpejQWHKSOGQ51VQ-RvrA7D7R3sLEPTlS5oDEAOu6msXMpzO0bpcWeWxGnVCuJ2vJLT2dCxxQsM3m4UTb0NnLmQ484o1126snforpa2ushLnO8je8JYdA5oZguBndz5YOiDwWEbMI5yhiqPTkD4ykZcnEaie_3w6e-WE88sbVkAQEBqZalhayQ4KqlrBaMpY5-R3J8AFn6QXuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=MxrRbrKk-VZ8iAd5YorzOanSae_BswAhiDMO_EXUJi4rS1bHYS_PsOtc_g1brwldlK4UiE3qkk_ubENa2x5BxwM0EN-Lwd0wHbC8bCnKq3TNnPRnf7zTlHTawaDeM1qievLuLwUnWrq6qtOW0RQdUnDAWW7a_QJsrGCch1Xhke1Fe9NDN0a43vgarOkFMTcHPWw238FC5Eukvu7CjYT54OL5qEyvBMgN_d87ZSfcLZH4tCebIy_EcZ8W_ZOFntmyoxgvVlBoEjBGNq5OrXJ6n8hoklb9sXnlJLHQLKj28TtxvfP2SiJ6vtUvydBFlE_kIyF3iITdhmUx8z2dRQU86A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=MxrRbrKk-VZ8iAd5YorzOanSae_BswAhiDMO_EXUJi4rS1bHYS_PsOtc_g1brwldlK4UiE3qkk_ubENa2x5BxwM0EN-Lwd0wHbC8bCnKq3TNnPRnf7zTlHTawaDeM1qievLuLwUnWrq6qtOW0RQdUnDAWW7a_QJsrGCch1Xhke1Fe9NDN0a43vgarOkFMTcHPWw238FC5Eukvu7CjYT54OL5qEyvBMgN_d87ZSfcLZH4tCebIy_EcZ8W_ZOFntmyoxgvVlBoEjBGNq5OrXJ6n8hoklb9sXnlJLHQLKj28TtxvfP2SiJ6vtUvydBFlE_kIyF3iITdhmUx8z2dRQU86A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=qYvt3ELVE227Ar4ZTZ0t46qJ5oWyOkFiSm35tD25OS58d9iuiFV4vevRzxoqE73u2TdozA9k3wDV9bFMqOdtpt3802HWsYZ6OyzVT1jYv-JT2SlI1fIpdWSKTLVpcDLqUWX0KFCDJSYZacAGaaK4FlSJ7HLJwmOIF8PJJpwoOiKN38xeq9iE8KrLLwqLExnmeLSUoBDoBOihasdIK3_j3imGNhdmTUgEZePFky7TvZOxNTjKi6JiOz-63rsoiKXj8hZwfr82Lw24IMBspdj1s8aCMtmxLPq9X3p0c4opA6PSAYdRvgXMib9l-L-_q41TRcLHKnyo-_wY6NTcPgRyjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=qYvt3ELVE227Ar4ZTZ0t46qJ5oWyOkFiSm35tD25OS58d9iuiFV4vevRzxoqE73u2TdozA9k3wDV9bFMqOdtpt3802HWsYZ6OyzVT1jYv-JT2SlI1fIpdWSKTLVpcDLqUWX0KFCDJSYZacAGaaK4FlSJ7HLJwmOIF8PJJpwoOiKN38xeq9iE8KrLLwqLExnmeLSUoBDoBOihasdIK3_j3imGNhdmTUgEZePFky7TvZOxNTjKi6JiOz-63rsoiKXj8hZwfr82Lw24IMBspdj1s8aCMtmxLPq9X3p0c4opA6PSAYdRvgXMib9l-L-_q41TRcLHKnyo-_wY6NTcPgRyjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzKPzt0ZMEqWh5z29HiVkGLyN1q5cX6hirEDdqQswzR10HOv8a3N4fNhboDcNPMf-pGuIxZN3GSveaEBo4zv352fxT41tvhX7KMXI33l3Zt7XdsAUeQzMV8XnKtWs99QIJAUOMxQxh6dWP4LdsEZhwJs_6Wnz4dC_OdFwid0IJWLq7engmmg8SOea5QyOT0m0FFHY3gL5bRvz458hLoPKxBfbsTScRXRn-eAiwBwWlsoTTNEZ0r9KWSmgKB5NI4aW3XebZh3fYHxQGE9w3ECtuxYtAt0NA1NjXT9arnvVE5RXl_SuB4xHIx0ulE7MO8aFXZTa3QiZThuac_bqCes2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxrubZnL7dunrZENcj218YEDA7SuukFbYB_RRuN91HExRvtdAOIgIcywguOCq-wRH4P6UIvRXUsZ74QIhFoMGfeyHUCJdrfwRceVKKx0vhRL36k8IpTCFMTrc1NZ1Z9VI7LKQimOFVhBWiih0nUubk6PEZ5dJxzh5_fD2dTwApRaN0NKdR5DK2EVQSgTnG4uYGyWRdzGwNN4r11cS8psfTpm60W6Lvfb-U1o9UsBSzEIurKBOEW66nsBL0zo-Id-BkujCqHMbhQ41Hyt-w7yKJrmf0eXEi_kqa7f8YTmtF88mYY0ueVYbKgzhdW-NmkpFr50_XYX6sSn4yHJvCBamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
