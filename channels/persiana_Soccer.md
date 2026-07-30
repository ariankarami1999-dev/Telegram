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
<img src="https://cdn4.telesco.pe/file/Z3Ch8Y_mxb-anIyJIR8PBMgI8u5-UGKPWkvQCO4lOV6FJjib6ZQRPAHMIcHj3V_iBPdm8-IpO5Iy_wl1WKkOt-qEjJNWPAtX-J1Yu-yz4WsfBDUK7iebyBfDN3KFs1jW8_7mOXGuAM-2Amx_K-aQO2NrZ8B8q5-Dfdjg7QGNsCOvvWF-NltI8nzsTCcUVATD9QYsCPVNlYoX1dtYkXejt75ldGGjW5Bnt-Z62iqvTQhz6ddS8Yc6OBN6NRgUeUe0J5Q_S8kCXKH-qXDOfpqvpHwuwDxKpJfZHfelfVUPxYXB2kibrO62yLtSdFHJmlVpM-aLou-uEkfevvKaeLT1CA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 611K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-08 13:28:27</div>
<hr>

<div class="tg-post" id="msg-26813">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DeqCHsVSmKcwfef0uuAfsyFAN89AmFOEDyXkbeieSqfhqe6Shy6iAieDcrxdALYIJiD0_y9y7hxgmHBSLsCLBdbGfw7PZEaU97bXYJa6ZZzNNz7pLXlmreXIcHiZQC98GH1ULMmWlimvanFblUsydykJbliUbo3xlvpoRoNsYPJD1DGLfFqgL1LFh9rZIXlMl08kndKozqfcy4Flju2B357xN07oF2dPbFsfRwQf5Z9yGpajf5nmaa_zAd5upWA55pNa5KtHrwL5Ky8Tzu3i2H1dBaAM_8eawMbMnlKkwGcoZBGofHcuRrMsZ00lJadZ8HKcpUnR51id61EvPpfi9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوری؛ آلوارو آربلوا سرمربی‌جوان فصل گذشته رئال مادرید با عقدقراردادی سه ساله بعنوان سرمربی جدید فولام انتخاب شد و در فصل جدید لیگ جزیره شاهد تقابل جذب او و ژابی الونسو خواهیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.75K · <a href="https://t.me/persiana_Soccer/26813" target="_blank">📅 13:21 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26812">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o_zVqty7OpBMxPod8TM7LOLu6TH5agcQElx66oUHF70rQc9rinl-LNM_NwR8qKYCMX0ptzlrIkUYGhWg2YNZ7QswzWBbNw0j_NMZSMgT5zhRy9Ng_oV5X7IimxEzvU7y4W160t65lLyqVWQrplNmCnMj80GttzJr2qWBWGd9eKvH02InGYyOS9l5a64JZzcTx2RqpNaZE5WWsEdSkchMKDsxL9f25kXldK_8bpFjR7Fhj3_q99DrwHOyGMaLE0eQLHm-wlI27VW1AyGgNwAXQXo1O1AnEN7pb3SH-sHuAomsLj4suhgHQ_uLYANsqxkcsOKKGzYpu48D8pjqOHJGOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
"بچه"بالاخره‌کارخودش‌روکرد؛ باشگاه پیکان از عقد قرارداد با جوادنکونام منصرف‌شد و قرارداد یک ساله باساکت‌الهامی سرمربی سابق تراکتور و نساجی امضا کردند. نکونام دو شب پیش با باشگاه پیکان به توافق کامل رسید اما تماس های محمود رضا بابایی باعث شد که قید قرار داد…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/persiana_Soccer/26812" target="_blank">📅 12:58 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26810">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TEoujU2QW28HpXPT-yPVJcOzLixNW1Z10eTvA_th-lo5rc_971i9-2ZubA_Daxn39lCmmPQnBz4h1uTKER9eqHuhfZGj69REVpajqmJIPbo7AjP4A5cTaBfEVB8ogF3BUeIXadTGpy-P-VFdAJBs5bC8lRjGkepuBkPew-iEoWHGxtuea32kJG3e9fsHs_Hroi2IDHGfdagSzacfBy4q522GGCDxrLGJ4PJHezDkWJ6c-xVBdSqSeQLQDzN0FGkaPMjjize5Hqdpb47Kx43R-Swjrx-icokMQWDax1FP2aenEUNB-rtzyJq5B38aWvNnPqLHknHU8Z63xAP3HCH_4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقای‌اولیسه‌بازیکن‌بایرن‌مونیخ‌هستن در تعطیلات که ویدیویی ازش وایرال شده؛ به قول خودش اگه رسانه میداشت حسابی دهنشو سرویس میکردند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/persiana_Soccer/26810" target="_blank">📅 12:40 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26809">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K7vZombwTJZvayKQ7KQs9Jv3LwT0RbTPZrNG11zVVdBRHuKL-JfxBiCfX5MK1vDtHaXX7oJJc2KjeyR6XWPnJZtOmzYuT7yIVmyZ1riKLcE-PmWV1ZAoRJDQ7h9NBppEaKWHX_dIS6lgG2Sujo0A0n9zgqjblwqd-CQOvkNBWBvRCsonHsm8IrJImNT_m1P5Y3ECGKBBYc5_BzyYUhklfLzFSFzVkeRUHKZMbLPTUbsvI1TTbmWwYn8qxAXBorBNTa5Tol6btyv-lZy047BZp_WyLA15pjcguOtLVJXI18ltsex_c_FEWn7tm3DoDaK4dAew_20KEETabDQDIbZsKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مسعود عبدی مالک‌باشگاه خیبرخرم‌آباد: باشگاه پرسپولیس سه‌بار برای‌جذب مسعود محبی به باشگاه مانامه‌زد و مذاکرات‌خیلی‌خوبی هم داشتیم اما خودِ بازیکن علاقه‌داشت‌لژیونرشود و ماههم به تصمیمش احترام گذاشتیم. محبی راهی روسیه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/persiana_Soccer/26809" target="_blank">📅 12:28 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26808">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmBXiVSnDKqMYhlnCCM3WhmCWu1dT0EXB3p3Wbw-EK2jV2f_0-cKt0vEKZ4xfmiu9VPSVhUjq-SaS-yG6e7gBIpB7IJeabMmtSNQzCsXGJeo8S5-K26fkToVQskkqdmAonss9GaFiGTiYbCHhM_PP92UG0RzDtT1nuf4oJDrE7RG0EMs8MsPabMfG0M9ypGWA5212DGp0wg0tDQ7FrNeZYhDohVFvvqjbQFBLdWkOmjWPuKhQUV3RcGeqwv8Z7nP8skwhCrRpe-3t3h192WUnUKeDRm12MLRPFcmykAyjtafgEsJda4Hj46dBDS_55Yjnc0h_RjaFOjE_iKq1KtMPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا:
ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/persiana_Soccer/26808" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26807">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a69d4793.mp4?token=XI6K0VihnJBbTzpgRavkj46ov3aj_QKjA3Ep6KNXQ02ml1J8d1MWCcwcWboJpUtDvXY5iSvjAnRJFb5TjQDfEyBQ9cmZoWV1gikzi1YOeGkmbsZR9242Z00RRZRxnzciyupndvrn3DcQNdPF0h_nFMYfF2IFWjt6aHFsi8KwTQ6iy6g09LjnWZfAZhnDWqQi9XJZb6omUS8O2XAXaQzsUUghNHJfbVFSuI1ZQbz3RNYh5FRTfgBIHF_o8REMHMBgem6SKPXiTOnGzPuL0nFi0J-AmfdejsrIA9yJXOf46yOWbVLvRWB4XiQk3z23iNnA_U9xJ9FHkg4gF7oCBp233g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ نیوشا ضیغمی، علی دایی، احمدرضا عابدزاده، علی پروین،نفیسه‌روشن‌وصدف اسپهبدی درحاشیه مراسم ختم زنده یاد اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25K · <a href="https://t.me/persiana_Soccer/26807" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26806">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBIEBOR0qy4ny9MvDcJe2F2fJhoK02bLWjlRIt87zslVjeG37G9owh3RAnKb-aL8hNlz1S9CfmSANJoJui7Uvqnt7r7VD-GGCp1r-BKixDM0I-m06Ehr1nwlxH6UqN93HPaah2--7Qc1jnl8LyP9Vt57Vdhp6O5BbO0EztkZ7Ty-BUZlFivilPbjkQ8-EYrJK6hGhS4VpFvsz7zHgIia8w5S-umIfJXQ8lNi0T6dGCt3w-Wv3asde2hHpE7aHeU_XvXM-qP-CBicaoCle-BYqB1safCKGSLTrOQPwlMavYePCfW3SvZysCImo_b8zDErLL0Q07rCWXyhSkw7Y7BFPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
توام میخوای به راحتی از فوتبال و باقی ورزش ها دلاری کسب درآمد کنی؟!
⭕️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
💵
اینجامیتونی‌روزانه‌درامد داشته‌باشی و سرمایت چندبرابر کنی
🔗
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 24.6K · <a href="https://t.me/persiana_Soccer/26806" target="_blank">📅 12:23 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26805">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q0PrpqWZKu1mLPv3lxU6cAmAk9O6-LSyNpx_qKCs0V7hLogWJgR5JzUNKONW_1QnEnmYdGCWyHq4ZtXoHEDgqoVChDULTuwFKcK6HcrqMwQ5z9f89aTofE3_GYpCLNupQUJmN-8JC7e12VnSx_RNoHcmLO-GX49V3Q6wjYHu_ff4mFfH_MDNNwDB47c4Qexd5-EWixvmchKSG0FwMiNpXFrD-964EYClpnsK7D9uDkxqi-5fQ77Kdg4jIfS1M_nA-Moo0HxX63uoD4QU5l1wvyQS8wtpo6kD-YSPwqWnJpwPaw64LzhPKhVwQXLMw1UqyGkjG9h0LAMIrVBjGLkL4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
طبق‌شنیده‌های‌پرشیانا
؛ باشگاه سپاهان و استقلال باارسال‌نامه‌ای رسمی به باشگاه فجر سپاسی خواستار جذب یادگار رستمی وینگر چپ سرعتی این تیم شدند. هم محرم این‌بازیکن‌رومیخواد هم سهراب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.3K · <a href="https://t.me/persiana_Soccer/26805" target="_blank">📅 11:37 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26804">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ple3gSemwVfU3UjSdgxS4UvTAm48R8c54wThlXKU-GM_wa5MrnKlQbyPjM8g68jKO3OLRC0x8tijFxze_sfomRnBEWG6SVM6MgiEmuB_z-sJbNnwiGZ8c99KMDJt5xjFnK2N3LisUSVLWJS8YIc53HPGBAoqwAV6NJNhn5C5qDF29IVN0f3W1whD4Ks_dWRw0JIxbjCQ0keTAFi0Y7AIBtnEdK3A23EHiO9ptk71R9Lwu7lfzLj1mYdbsSEdWqk1ELqQ1eDoNgHn6TqKsoEHHtTWRa3OZ8dhKmnRgh9UxWqz57oOnRMLD8NYFWCoMXBRsjEX-ItJhGzl-IsBCUgLEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
با مخالفت مهدی تارتار؛ باشگاه پرسپولیس با وحید امیری برای‌عقدقرارداد یک ساله بعنوان بازیکن به توافق نرسید و به این بازیکن اعلام شده دیگه در تمرینات سرخپوشان پایتخت حضور پیدا نکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.3K · <a href="https://t.me/persiana_Soccer/26804" target="_blank">📅 11:31 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26803">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">‼️
ویدیوکلاس‌رقص امین حیایی سوپر استار سینما وتلویزیون به‌همراه پسرش در فیلم جدید «استخر»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/26803" target="_blank">📅 11:09 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26802">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KN4XLSHvtvBLsXKH8UCu2yhZvaggDImoB3mDvmvLc2TjQ52HdlK6jNHBc3NYqycm9bVS0szv4Xm8B2Fj1k-1Jw0CWoGfJyK3-2Zi5b8WmMmO5YC5VX9naIFYXI3Xg8C_aOb1RzyLMgEu51Tq98fV1ydRcgqnepcvALwuoX2XtJ5MNsFdlySi8nPROIN5XIYnxaPZZEL4Y-s7y7Kd6JBfAcMbZBwRuh0Cz9zPVgjMf4K1pzo0uDb3DL6wj1jmii-TasdRm1thkKylS2w25IaBrH3BIEc2araDnws8z7c0ra9KeFrNtwK-gh2CVCDctWhyPCAUQ_V7ogYKhyrOFD2Grw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نشریه‌مارکا:ظرف 72 ساعت‌آینده‌انتقال رودری کاپیتان تیم‌ملی‌اسپانیا به رئال مادرید نهایی میشود. سران منچستر سیتی تمایل خود را برای فروش این بازیکن با رقم 70 میلیون یورو نشون داده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/26802" target="_blank">📅 10:53 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26801">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78462fd8c6.mp4?token=q256eCaGcVlmd7EbtB_5KeNY2KuWs9R4-KrybX7sLMvjwrHw-tmnL73hICFnVgB66QEQUehBQ9WX5E_lZg_w3cb7yZ9M5pq7tXKtOlShFsmuKB-5QkhzW_wLywqbNGEFRPS9qhjBXj9UIDiPc5CosC6IzJEvt8P8NFuI68LloT9HPFNJTyTcoHG1XoMR-xyTFO0Ok6wJO1r4t2tR_NkOZz93Jcqnb6ZIh0lI4KsRqAAdVIQjNpr4hfDsG5_x6ftwKuBWBORyGiAu8KQUBJeBnip1OLZi7tKK674VetDMhyjdjSF458JhBQCT_Y8qmDwXIZ5DVKRI7Y4Ph4PQYQNPCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
روبرتو مانچینی سرمربی تیم ملی ایتالیا:
🔵
ماجرای‌من و تیم‌ملی‌فوتبال ایتالیا مثل داستان یه‌رابطه عاشقانه است که به خاطر اشتباهات تموم میشه. متاسفم به خاطر اتفاقاتی که در این سه سال رخ داد و تمام تلاشم رو خواهم کرد واسه بازگشت تیم ملی ایتالیا به جایگاهی که شایسته اونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/persiana_Soccer/26801" target="_blank">📅 10:20 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26800">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇧🇷
نیمارجونیور ستاره برزیلی سانتوس شب گذشته به این شکل برای دختر دومش جشن تولد گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/26800" target="_blank">📅 10:00 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26799">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r7LhOHECopCBunuZXulm-XmUww9iv-6qDXYY9_40uBMP4tH9BLaEguQ8dsIqrh2XcOvs7dZqxd0Qhkz2ENw8Xvp0IKw5qnHTYqC-kmgXmBeQ6yY6y_xL5OFwhLfsIRWxBYE8LalIY2Tg9rDsUZUfuHmR4pGlea0vylHOSwF5tipNRJ_KpNjZ_I8YfvDXOVP31dbtSRAJ3IoUb4NSKCrUdnn5mrN_zUTR6j89dMu06txU0lRQFfIK7A7zScMBEd3QFj6MWewK5J7HuzTOBk5xunGUkeRREzUL4NtfSB15haXJLC3ospK5f2f_SglcTSBg7G_g8lnkhofl68BUITjCVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اکثر رسانه‌ های یونانی از جدایی قریب‌الوقع مهدی طارمی از المپیاکوس خبر میدهند. این‌تیم‌چهار مهاجم داره که گویا سرمربی این باشگاه تصمیم گرفته طارمی رو در لیست مازاد قرار بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/26799" target="_blank">📅 09:46 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26798">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uoZi6PF7VZJWzMFzkZKh1qn9FsssHnQ2Bqxhs04kqfD6nFywy--emJ3MFsuRAW4DV_8ARMPuXnRZ4npC7-tSqQWWL9OINw6-28wPVUb7HOB3cFyAHAhZEkOV8xidQ8m9EjoYvugoFeMsOQh0Qhe9rbf432EhQR5fIywhNsQwSRG3mfA5j0Ef7VmN_m6DlwsGYPimajwzJWoDhJMDJReUf_-j8AlXJeK1PNd7sXKr00QxmKAFWAEujgJ9lxuRwgtkayB1rTH5etuDayOD2JLEuM5-BAgDvPhW9Qz2ye3hTeCtRcZ-CzXixNM1HqCetFfMyDEJgwNzl53hFCbTL5zVtQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدار های‌ دیروز؛
شکست دورتموند مقابل تیم ژاپنی و برد سانتوس در حضور یک نیمه‌ایِ نیمار
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/26798" target="_blank">📅 08:01 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26797">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UikECKDFSrKlAb3urrHBCyT5tFNVx29R-tDqJ2lr-vgT1e4rDf09UWIzG99YRKVPD--hF7NZ7_r7DVO0kaG_Do-RJ842LTY6jRiEMlsqnn_3p4AFREQg1Z4Q5WFt9uG23j_HUtmqz7jwvpM-gMbf7Obkr1GK6jCF9jAcCORAggfW1zYxIab4qhZD2cW18PKtxHNO4HakPrYJtfBvvRVZRnVQ9KJ0PyQNsfHcfY0zqPEyXXoKJcOYsh7Q3zmiIBTmAtLfayRicuH1-PpxFRFMqo3wGP2MyAijWrV8Mw8O4XT7SUsO7IZQLQ7eqiR6hgkOfB9NeyX6350BN3gdKWJsmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/persiana_Soccer/26797" target="_blank">📅 01:49 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26795">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fda6c0e0e.mp4?token=bCn7KhNtg7NpJEdPrN7La-2xapoOKAq6Z7_hpo4zF5vcg6zA2S5x_MddrpVCoKvMwnKdJorA76XVdveW0ip_V3jXHVPGyaSTDGCC00E_gZKxROMNc01cdCG2cQTeNpJDNG81d170RdxNSfvwHmE7r43tDGmxE1yNUbBSTf8d-GyMAOgW9E6ig4bYsYDV8iiVGe4ipWu_4xG7zLk6s63feZTgTKB3ERTXTVJQQ4hG8ghI9gbf5o6WWeGkFL7fQR3gFRr1Pyt4YF44P7sQdESF3iELKR3dS5aLhbn6BakcbFJyn3UgDgojdDu49AB-IY0L6olpKh1hVtoY_uGz3DeokQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دوگل خاطره‌ انگیز از ارسلان مطهری و وریا غفوری به پرسپولیس و استقلال در زمان حضور در نفت؛ هر دو گل هم در دقایق پایانی زده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26795" target="_blank">📅 01:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26792">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RqXzCkLIMtXGKhY1O97RiCxHAooruwT1CcydwUKIGR7c4kzrrBavHDWbMtLLTzR2tzxQdWMZ0fWuHxP0y0pGK4coEfeeeO3F1aCMUvC-FIPU0-urBOZvPgulxdWVdxrv-hOSWdXYXEz2C_FoqTYBNn8dz5HVZuPH24nYC_WfPaa3XurURkApQHkOmC2a4efCI2NvJISFrd8anb1Mnx9VWdxYixmCeSrpPcfgHeVCgqmBiohzf2NF5xFxBhZSshqxXWWGYpIUntpXAqnzl1kT-xpGkIHn4BOEuhtryABfgPR7BPMWm6hrUQO7HQLFKMO4Xm-WswM-y4ZU7LvCDYmXGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
کریستین تیو:
وقتی بچه‌دارشدم، همه برام کادو آوردن بجز مسی. اون‌بهم‌گفت‌که کادوی منو تو زمین مسابقه‌بهم‌میده. کریستین‌تیو توی بازی مقابل لوانته هتریک کرد و هر سه پاس گلش رو لئو مسی داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/26792" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26791">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZKLAlL-ExMUGqoAsMb5D-v1kRt4HxjhzSKljxcWCJZXjRFCBhlm2gqXHzfRlpwPVv6GohTe9mIG33ONT4D0gtlkaNQSs3EIn3ltzS58iQLY3vLb5oul18wZ9f2Bkh0KJ6Yv0OmOVV2raLhkcBhMFWjKuBQLarQsfQbeFTstkAqXsvk_BFv3Q-Y-Unhvl6LgBD5ikwuyXgBlPTs9nV1g_6LiJFaoM9xiOWpy2FPDr2dZvhfktSZrpmHtfaQ4UQ1NkvHlcAADss3my_qyyDIbNPUmHAFRxs8lEm3-DQDIZfgJcNY-ejKCmQR3AqMD0POElobLEcDL2zEM5E9cnso4yA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26791" target="_blank">📅 01:17 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26788">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L4HoJ6m5_qruuKxpO3Lnp1nyXDdFHOqijscSsCV1Z3cIJ_cO8Wyy2AQs7WmN4CHgcdcuCmTJWOSE1kLEQ-mHse6bdEttgohjXYmEOQ7O36WRDcpraF-K7rA3BioLgd_7DeKZNdz5phiBR33Bfp7QMOGc2JUHhdQ9tDEveP5oiY9ZefyOSJXr5wKzYYf14f2z_qo3NDshZnBAbiyFGwb8sVdK-n9u2WQn551aQOIlmBflamwosMULxmbT_feZL6gI0LxEWHaG3fsVXL0809h9hlqv167D_eZI-J7lbcWkgjDXIrJwJJeaeJJVRRSDXZgAiPLDGNM5e1O_OA7Dg099Ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Wie6JgANgoom_Avx6vLpS7p1oZ3mO80-tZKsFuHPjHewAKJa-do4LufBgpbrbsA5sNkmONJiWSsUgXkoQpQfEH8G9ZyjZ1xgssGcHLKtp3mmIO7lfmVPDQWECpVCETddFxIiSaNokaZ3I5I0tc1PcCqyJ14MM0J1clnpcmbZjTIggne1rg5XmjugCNX0QchUVY6Ev2gaoZ6K0edn7y2K-g0QBX-dNfLX1ayOEq7ecrofYmwh_IcO62T5nOded7QoieaeBX6qrQh0XQcH-oLq5dQDXQFd37q3iG1jrBnJ8yidc3EVmZ6tDTkM_H5MwCXBmmdjgzwsHWs5RA7mJwYy5g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26788" target="_blank">📅 00:34 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26787">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d1f12784c.mp4?token=UdI6MwKVjvpUCMZA3fRvjf8BDu8uUPonAciwD4uAqUSjU30sfQoaagnVdzTebzynTLw5MRZNZ3D0gNYEAxAOIKSaoLgfY9YvNo_xG3qo0LtR7vCxzJgIcttqwi0ZCH0kQX6ooCi26aD_giD9KKpobLjD-zoIi_ZLbnUd3OVUaTqsWiEfRNvRf0hT4TDwqmmd6JMM60y_MD5p2ESpviug8BhlIF_OAAjGiJKbLEGW-Fil9UGgag5VY8j8J4Wwedi6Mtv26mhtnVpe9xxjpBUp7qvYqDxr-6sVxMUZ6cORrbzNgaym5UPSkVERTUA0jjEjR-shqB2F0TAlGrVmod4fGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛عصبانیت‌آزیتاحاجیان‌ازسلفی‌بگیران در حاشیه مراسم ختم زنده‌ یاد اکبر عبدی؛ مگه عروسی اومدین؟ که لباس‌های سفید پوشیدین و دارین سلفی میگیرین؟ خجالت بکشید بابا. مثلا الگو هستین.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26787" target="_blank">📅 00:19 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26786">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/556eaf6051.mp4?token=rmqUPhk8ymmFZv3cofUrkQs0rrievJuY5-VxQpsrc6hnRYnVuRUTPxa6bLsIgjXKg64Dy49g7g7m6lqDdHYm71EUyOrKNHo0j7k097CaqOWFT-r6Q-vr3OWN2sQSfeDrGstPoKpD5x6jDDRTTdWEeD_XrSSJZxOUYZUC0mBTHl5DSmEHGvCpDTQVvDQxmRtEDdtHQn8L6TpLLrcibSNiNJGobXwO7b814v46L5zU2OP8opQRAOSp3f8rDUp9rZ8F9EdLDyriONWpdYwL0_qIi9waleE0a7L9uE9QaP0DufG71ElVYIeBj359AkgVaECmjam1j5zf1qQGatX7OYTrzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/26786" target="_blank">📅 00:16 · 08 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26785">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GswMRoobA8GYonPTH4oHbCoe6yezwLNzbhfFqwXfX87e1xwTNJ9ZppJBVNez2v8kMCmuvOJ4hxfA8QLz7AeUS4HzY9baqZch7YGGHUuRtMlwojURWya-4ahPILku56Rqy-ch-Qza6jIZLE-xc9PvSxlNb6KlMBlynb2EiVXnkUEkj4lsNK7wwG7jeUCzijdfGuX7T0EwkyYa50dsCHstLSN7EyYRL70aUd4v4mIgOYihDxLr8bhpLwK9BhOeCv-OgJQaiGLTgOEbUa7ZgV8TY4VGAQYqVihgYYpxZIth1e-g1tM_a_360iqpjH1asF-S3MWIyQvFcuEI8BQ9btD0Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛ مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26785" target="_blank">📅 23:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26784">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vJmTNGFdA9fpcR1jWhaSfqZnSfHboihMhmR6TcmxB01FPHTyIM7yD7Y85Fqx8e5yHYFaOSlGUWnBSrUy_OYA4adXdoBA0RIZGt3gIA1uXnfivcfW0ZEiuj6rO_D78p27JWtsNiAF0js-ELF8Kr8extCa8ITjwZcJ4Sd8W0XAB84UA2EqJFXxSKlYGH8toeoFJKCDGiNaeAVQmnSGMmlN87CcZz4aMKBsvH2rbdxtlN-XhZw3KAMSI7JHoyluBrV0jt5KJil9yZuzMhIitou46ApVk3nEvdTY_IdjZ6v3bSFj57q5kA7Arw06NNq6iUaWKCXWBBHqSFAx_UnSx2fPtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
با اعلام باشگاه الطلبه؛
مرتضی پورعلی گنجی مدافع 34 ساله‌سابق‌پرسپولیس با عقدقراردادی یک ساله به این باشگاه پیوست و شاگرد علیمنصور شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26784" target="_blank">📅 23:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26783">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/787ac45905.mp4?token=rJNR9u1BC7fd67qQMnxdy4PqTVSWdPyFk9mGzgufTTm5_5hZHN09f7qVQj2CcqoIOw5IaUBIXL3LPVc2Ngqy_kaycdevBuyCJRjaWko-Cp_GFTM1QvW2sBE5oY09ENTP2F32UAHDVLACoq_unJ43vsajs9vd6rDBibJZruFE2bZeCwwiT2IafX8YvnJ-KdaKvv9TKpL6HD_g2mz8VqTIId1CYFpTQ6Bomntwzev-_x8av6ArSq8FF4PnA1PmW9s0uMZ9opAhhqzmguXNGiq5WEviK2WGE_-y5RpWNZxynr0z0xWSTpVEO1zwa997kWViD2tTK02qVhEfr7Obujqoig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌ازاین‌گفتگوی تاریخی بچه‌های غلامرضا عنایتی با عادل فردوسی پور که عنایتی به بچه‌هاش گفته قبلا مربی بارسا بودم؛ عادل از خنده غش کرد.
امشب غلام رضا عنایتی با عقد قرار دادی یک ساله رسما سرمربی تیم لیگ یکی پالایش بندر عباس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/26783" target="_blank">📅 23:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26782">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f6c32deb0.mp4?token=Epx85H4WKTggt0l4kDwMlCUfUShoDFOlUCKRNJyttXoBe1IR65kFxAhx19OrdBqEp9NO72DvJtRWH4U-atehfYIdVfIy3EQxJKQPE_vZOCPvOwpXa_X2Otg0kBW7P32rUlem_py2SqGn2em69TLnjUQi9d2NjYUQ568MKDdJBRhZajAfMq4Lwlcd87WZrNaeJLSxX6R4UgKBpe2H8O1pRLAwlSOLMOdqdnB3fw2HQKC9RC_4j79pN-KCEtb5rJDdCrHnH85bn3a2o9b53xi7X6c8tYxO2dwtHu3PdvvnwQ2ALahU4FgEUw2eAafBuhmbPqoG8-cOceo773YYh20cl64ixnjcrg6nMc1H1soPLkLqYSoyNOdJzKP0EkZizXYYCSpRh3zEGEmxV0XsHGxiKa6jjIfIKnJ_slaOEOKiUx63U2jdoD2osAC6tSuiI3kkK8zOMJFz6lDZHlR-iPaoD8siSl1tbSDw23WH2tcdA-Y5c0BtZFuf-MAsYUy887G77XbjpQeDbrIzAAJgi33h4qzO9frIi1WCPUyaHYzI12U15GuOndl5w-VR1V-9o7-4-2O83blhLwS7ZgCgQLdGK7NqmNChCAR3IB0L4hvvPiB42wzxvAf8pXeFBRFwZL5EL_JbwMaPDZBKzprgtMJpDsYd7B1xutoFa-VvFfMxd9o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ سراسر سم از گفتگو جواد خیابانی و خداداد در ویژه برنامه جام جهانی؛ خداداد خواست کاری کنه خیابانی کم بیاره ولی ببینید چیکار کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/26782" target="_blank">📅 23:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26780">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uOiSCF02LdkNe7XeUEA2OX8-fI_9HdyCUxMvf-adhWYKxDYDzOv4g0s396P_Dxp9k_CRDGIAbG_K_fIuLMx-ps3JxqU6wvEvpyHfFM2WoVOkYvYZ2qRfoU7WN9jz8EslTQHHxzE57sdn0INz9DwNEaa4EfMv2x7sAoD-UVsIJLeO1i8HDl4uE7XquBKi1JwJv0BrNXMLOnDF1zgtrb6rbtLuQnaMxO-Xf5x-WfBGqG5RCdnZgOGBriPBSpgZ_bAjBicY5g7e8roM71C4ymBaQPlNiDmEC-AVeuHF74x5K_tnyoaJR8ZVNAvqIZb5IXDU5vypKsZSQuyuCCOwYr_i0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iOxe1LFexCbOHlVa46EMKe3whmsUYawgjtFT2tnZ0H5u_SsCUIIeyZ9DwdSgvwgLwq8ccuDkTwfpeY2igQyRYbTv2kH-zgQrQ-u6QdZEqUnPT0inNnZjBlgmirQACuZ72H2Xk47gOkABq6Ho-Eq1mmuGoNPIi_YCa-q4ZhCzil7fDmSzFx54TMFqLuAN3npiFgMkmGemJwczSKi7JW4dHAVOyt8eZzCsk4WhxhTDuXvuyy0W7l1XjkkliyKr3hkYXu2WINXuHCFeJO4Ax_7pJtH2RnlG6E4mImtbvXjIKdwAHisI9fgDGldCfToDMxtdDoLwcXuXsmuwSQvrrgVIgQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌دوم‌وزیبای تیم منچستریونایتد انگلیس برای فصل جدید رقابت‌ها که استقبال ویژه‌ای ازش شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/26780" target="_blank">📅 22:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26779">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbR00GFTRWAt3QXqCJhSjEOMiBNkyuRXHx8Z2Ay1ZnOxvWhgGyU5aZD-GaZRWbOBs0mPSVgcy0Tmo0L2yCRlGPIlmDbpsp6nMQW78gK0FiXMB1uOl7mJeXZk17jidD7YWS8Ipv7gEBt5JL5O0m6qWFZyxFR_h4-aYwfjU5kqj1PiXP83PMo-jDQL5USA02D3mppjKtaiwK138yO_oF-vphHPkO6G2FHuF4885zUGsKu_LEPm83Qghbz0nYi8KrXLtHkKKk-prhuKbLuxndDH9wft9m4ndydh-JhltHEEDdjvBmue-9WSF8CPrzwsjemRWAcR0feVPVPK6K1Cl-RcaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه استقلال بامدیربرنامه‌های جلال الدین ماشاریپوف‌ برای‌تمدیدقرارداد دوساله‌ستاره 30 ساله آبی‌ها به توافق نهایی و کامل دست پیدا کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/26779" target="_blank">📅 22:25 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26778">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gi-4SOOeMmEtmquHY5lqGqFJlbqG1N1rotZbFboVSDgjt6Z5bf2gNPVqGp8RnU3hedYUElT3bmyRMwJi48ZY3rN4usDjUdYKJVW82se5slxSgOp8JcSsbBye8iTjMZuN2ES1rsuOiWmEFRqi1QmDG301W3sFhloiSe2vTbiBwhQgEzG-Dg0e7QiUfCUTo486xMSbDyJReodhhrjtcAmzHzQR0d4oqW2pC3dDTSMjfeGg-YC9UKkZxXuxdSNL_3iTv1OD6PEDf7vc095YYpF2XG-Gp-JJdMjpKX0a44XAyuDYpgkzFl-bmRduz6FR1P4fJCJR7waQXEF4zZbKjSBCIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26778" target="_blank">📅 22:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26777">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CEYuUktl0rcezwmTOJfF0NLqzkxLfKLLd_hSwkb4PjxZTRB8i82cyjbr2svo5rqybgRHaNwJ37svPvTFZgBwPm3nm0EaZIz0Ct7Yi21Q44-yCcqGKqYp1bPi-3wXKyurxihNPNEwRfpXMnodYo_s2_6-yfUDtZh514MXlirbSx3JoA0pVjG-RiPiC-AxuqVgxNh-oSNsKo-mtEVZ22X-tqXd8vzbI9duW-sKltZ8O22K6_b4_2tdRfxSUpngxXznqbGvdTfUS_NdxKMb9x4dFSIqEhjqOD3ATU2qmwS8Sduy3GxeCCYnVc8EJtVtxVHuKwVD3S0wUbeNDiVT19DN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
خبرنگارشبکهDAZNایتالیا
: آندره‌آ استراماچونی سرمربی‌ سابق‌ اینتر میلان از فدراسیون فوتبال ایران برای هدایت تیم ملی این کشور تا پایان جام جهانی 2030 پیشنهاد رسمی دریافت کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26777" target="_blank">📅 21:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26776">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWzOFoFdeadkCYEQBbuiMg2C-4Y2fAMF8BP7SQhpyZ7N7tubH4A3kZ9TqHEer3Yi-evVfK8-6drIARVWAzsCHAtUJSbJK-d3iSqOPSNDhgFGV4-4k9m01bRfqtOZxmWwlxIvP7pbGgXoNM974OnSw-0rXx9bdmIamEI5n63gWc7Dax7YMMau7XH-kZiXE1CqixXbssB_J8OXuZVf9ZLgq_JvRZUxW5BGjfmogLA3xBouuoU9fUoTgHPHXoDlOY-6f26ZnUa1a_DRzAbBWcsV8mnwl0O8nbGBzaWKSXpyiqiENUfhR2VmzZtmPcu6q4F3w-kPoENWU4Wk6w01d9ch5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26776" target="_blank">📅 21:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26775">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/762527d0f1.mp4?token=ANkwv7BWnrIBf0tv-infjyV76zmTEqi01www669_nk76SIu57Ubm4zvwqXczAO3M6tTofnqMmAwJ-EMqwXMigt_rWVzwLPQIn-T4ErtgF_g1mYqTDq9fzLlIJ2aP07lu-20LujymAOLN4PFLTItBf5A_W1CEn7-V_2--IBHCAyagakZ9F3rT7XJClCzMf7a65qC2LvCg3fI9FGIvBMIgnxlWn5qTA3nb9OOmhf__l5BwcThe8jHoNRUPC8hqtDZerRe7sPbGkXnSFcJ_1_v2x2v-ZYmsW9_lPBlaz_yVbkIWMyy4ZXEgFLP-cQZv0sfCQhJA3TWlqu1ox5VYp5hSqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تاییدشد...بااعلام‌باشگاه‌سپاهان؛قرارداد احسان حاج صفی با مدت یک فصل با این تیم تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26775" target="_blank">📅 21:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26774">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4063938cba.mp4?token=qO-TmDosqF87CAZUdEOrT_cMkRg_A1JWBinvqE1lONoNTP9BErHdMKVtnSpM5XZyIBoHlPHEaXHncBa7IKYpaO0Ro1FaKcHogvossbB4Xou4s0Sn9lAdOgffs5xopfGfxrHRKEVwpVJaMfMJymHBSsbOrt19Sib5BgZsfVK9CO3XVEJMm1hJla0TZhAD-EwKaN3a5Aasjv2ylYUYOnty240GZKENYiiX4pm48k8agW6yvt1N4DNr9wTStyApblqIleZjyloO2-9lJtpq2FvJj0iAL7qT1BJ3PkfIfNQl1P8n8q4xv0Kwcmbp8VZW9Jo4M3nCcepCFkOvSWShWcfSdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
استقبال‌فوق‌العاده مردم از علی‌آقا دایی اسطوره فوتبال ایران در مراسم ختم زنده‌ یاد اکبر عبدی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26774" target="_blank">📅 21:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26772">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhPEm4GfwBGNvOgC-cWcee2XiRZQFIaM2k_VJDa0PUt0PPunEfG0hFY4vpBZj7_7EhUBatX4PlkWCpam4rs_HKtuhrBzlwR5cfVFgOzZVpnWSVgbJ77-SLJ-3iqjlAV2ayKmxz4DssVEtNEia2pICH_zyuNTkqxAqsiz_lHesyKv22u52mAVp0ZdpyQgS-CI9J1YVDtshL2rjKdhBnqHYg8jlwERe51peSj2FdeASlGi0zyyiLFvVFIQXRMvWXk1uAhKnGZQclikKoMiVGmm5SwyD-_kzVzyIX65TG4mat5CA2zUxCFGz-js7G9Bfx58q29yd43ZU17_ppkMbJ-DeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-_yEyu3UHNpDbgVpKGUoQNbTr3QiYDo7rQFYGgf0v8Ni-Gtr2LdEwH8Es9hs6LGMfySuZceKY3L355KeR3KG6dsdX2ixGk1Q9hUm-sUeuP3ttfdFn00U7mwvJCIT5ZnWuuXzEzxcI3btemFFsDFoNXVHewrMLsnHO3q0sC4qn8Nz4aPGN_vXXhGAI9ZZCnXT2wagPwA_ZHtC2T--jWA2xP2v35x60WCBF0iI3t31uWJO3XGiyrTfExVPtxSwc26qkeboB60sd-CS0qXlf2hNpwMEGNwjMIyJLgC_kQEQRBa6G1BA9dS8_TjKCMlc2tRsR52uDqXUrkq14zd_nMRxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
ویدیویی از مراسم عروسی شب گذشته گابریل مارتینلی ستاره برزیلی آرسنال با پارتنرش؛ مارتینلی حدود 8 ساله که با دوست دخترش بود و بالاخره دیشب باهم ازدواج کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26772" target="_blank">📅 20:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26771">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3befee8bbd.mp4?token=YNIegXpTOhkGOk6_wFaZ_zJxlQdw4djI7kgQM7YF-UcW21vkvxBI_QEw5EPuedFDZ6ZwhpUETgRNFmQeeyJZGZ2ORocCVYDVMjTx15rHolExjgzETjuJ118ii_ZdolRwdvOLvdI52l36GsDEekch7PKET0yyJp1vcosIoWz1AxIJFrZXlJh-TCYfnxaa8EmDOWBaPegCN3j0iBl6OsMAHyrADfyDDVF1GscsPoj3uZ2Dmj3QnYSI09p15Ag6-mZbIxL2hPTERWvFSt3DtFYyqF-w4qVZVNJWlQLiB1RURlJ8MSysUIyPxa8lVBY25yFytWMmfSwQQd7lqt1xphQTUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
حضور عادل درمراسم‌ختم زنده‌یاد اکبر عبدی که ساعاتی‌پیش درمسجد جامع شهرک غرب برگزار شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26771" target="_blank">📅 20:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26770">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujiVCUmRHR50pJ5Pz4_-iCo--g_U-Y7zqjcN0V0pTjkM9Mo3Mum_IrqnDDtv0YwMjwHJX6GrY9pB2DVRjcVttnFmO9dlf7Qm_YxgnKLL_Uk3LGdqc2c2D2fpzdl82-tWJYVV1R3q68VEvRfkFVjBTwIZ8mYjCUaV2cfkbUSn6wIkKDxOL-hr_AcvWa-yLGRbpYxw7I77Q6_nfwc8IyyKq-18YUOjDiLz2xPlsKs5k6dfzmJgiby7mrvGzozTHm672xbwfa6obaa5AziOxFzrOIlOL7YjDsM3K31vXbuEuy8GqakFIbN-7-s0ciEsaocJY-5GDHf4nPaoLe6F_rxvxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/26770" target="_blank">📅 19:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26769">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPu0WBbdhEffOdbCexdbnOYSlHhwury2RBeKNjtMiO_-Ix6byhE5iQz9o9yhB--zgKGrGMB3tnIiNCENhpHweJAl9CpyqXliQNNEAXHr_agtNfm_3nbd3YJmFkXHbBhe4nD38JQTSKshCFIZF5Viyq2mJ1ecNZ7GQPuhS85_A3I6byQ7mjnJd2DLA9rzP8Rb3ZshuzKoa-pMUOGdnO4xpF9eSu4lj9FUPt8DqKylKB34oouhmLMgYryZqsj3ZN-uIP5DociTEjCnhPpTSRtTVPCZTkT4_EPa3cFE5mW2WTD0-LPXd2MRdOrKk3mS9LDIWgVdh9f8JEnCT0KBDljzZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
۱۰ بازیکن‌باارزش درمارکت؛
هالند و یامال هر دو با ۲۵۰,۶ میلیون دلار درصدرجدول ترانسفرمارکت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26769" target="_blank">📅 19:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26767">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee1553fa64.mp4?token=c6ZN0vfxEd3sqq5CDMgIrj0pgwZnoQCm3LG2rXaQ4H03ciSeBHQFVDO7CthTLKc0-bU8y53hdmZ9yTxBlhwtN930JMsknfJYmNjfg_TOXjjDSip5BAn8Z7w_o8fdP_4F6GgdsgXKCseDZ3VOc5j0ZcvA46ap_lMQI69YVs3NbMIKvcS1gzT5kFKfPc-hHyqSJ8AlRZjxgiI7LpU4stRmawjvREo9oH3UKRPZ9gMN00k1W2FiMqRJhiK_0kwZBWf7ZIRoKgrl78NGXm5ts5gWy0T72Du_WWRSH71JPZs1Iuyy12x9ipmagQ2ExIbiBqOXGAQdCOXOhDMVtKogkdbkKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خوان‌رومن‌ریکلمه درباره‌ مسی و مارادونا:
«مسی و مارادونا دو نابغه‌ان. عادی نیستن. کاری که اونا می‌کنن، هیچکس دیگه نمی‌کنه. من عادی بازی میکردم اونا نه. حرف‌های فروتنانه و جالب از مردی که خودش هم هرگز معمولی نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26767" target="_blank">📅 19:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26766">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GA4dII8JPLK7MJeBZyaRyq6gXtRkNvbYcvbGmIjX68eL_q5UlxR-uGQesBpOac6qN6VKe-1SSusJ2xctmZjGPCORsoc3qUT3rTqkwb_Tx0O-IVisNfwh1UWZ_DsQvWo1XDW_WYdGIVYNtJv9P73O3o7QGsiQ3gHusv1uPR_85llgENe3aoQRboHAkIwYNz2lvlvRrB0JuqsubPcgSDyIv5_p1bhOrNc5oDcHT5E6jZ0u2K-juOP6UzeVAkNmn2Yo2s8hZV7tgtywevmJtmNB6AUkI-fFQ0nuzK0VMstWXhIpCCfgOxx5WTE3t39n8fsaNulcXOPy0ohjdcH4xJ9yNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26766" target="_blank">📅 18:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26765">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xubzsl3fB4Drur9kZpyfAjw-xTgPrf012KKQAHaF4UX5pF40390gFs73YfNy2roXqrm4uAg1z6iUhy6giUEtJWDXqPg1B2nHOR74mRVwUygHFbIgM75lH8XDi1lTaYGu9FZQPn39O0qtcUoeeQfRAgkU3LatTzmpuEcvp-wnzav38HOmH0cOyfLgw-ekARrAXpx_TX1JCOD7okiQGMimMsxCzThF7Z4-sVXfZYkrXLXNO3nHOL5Wvbfcd36sASVZn_AfgscxTRHPMdxN5vHzb54IUgGHbk20SSChvaN1qWbK6F5eizVOetMbhswncIm4TXJM0FBEK0hs-yJsD6jKwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
نگاهی به عملکرد کریستیانو رونالدو در چهار فصل حضورش درلیگ‌برتر عربستان و باشگاه النصر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26765" target="_blank">📅 18:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26764">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97aa505010.mp4?token=CXuDZrLCo8j9LDUzkXSrSIgdqLvqaYDlRvaf7K5RLhwbxQslVlhwqSJib5RwDG6HWdUMVFavzqReZap9jSlRMGgEDCJYVBcnjxoKj_bFYkFqGqHnyhgNCcDGSjUIqUNNQt4928vM29ADkDvEt5y871PfMgLcZWia8PZ_piA9M4-M3ATKloACP2gR1GVQAh_ovGSgJf7xSUXK0K0PQV5FxkmIxai4aLbGz0qGFVUoTdSstPIfX8CvMx1-wj73mjh-_Qqom9cKDKhtCvDy3jTipxnen_Nu-Nq_GPvQQpXDmo8fPO7DSvPTnefAY5Cc7VYIhn5Uxxij6ZqCcL3FbYbJQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97aa505010.mp4?token=CXuDZrLCo8j9LDUzkXSrSIgdqLvqaYDlRvaf7K5RLhwbxQslVlhwqSJib5RwDG6HWdUMVFavzqReZap9jSlRMGgEDCJYVBcnjxoKj_bFYkFqGqHnyhgNCcDGSjUIqUNNQt4928vM29ADkDvEt5y871PfMgLcZWia8PZ_piA9M4-M3ATKloACP2gR1GVQAh_ovGSgJf7xSUXK0K0PQV5FxkmIxai4aLbGz0qGFVUoTdSstPIfX8CvMx1-wj73mjh-_Qqom9cKDKhtCvDy3jTipxnen_Nu-Nq_GPvQQpXDmo8fPO7DSvPTnefAY5Cc7VYIhn5Uxxij6ZqCcL3FbYbJQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دقیقه 92 وقت‌الجزایر گل‌برتری زد؛ گزارشگر: 7 تیر رویادتون‌باشه؛ یه‌تیم مسلمون باعث صعود یه تیم مسلمون دیگه شد. دو دقیقه بعدش اتریش گل زد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26764" target="_blank">📅 18:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26763">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YTwQTeDZFEgzR93qNWtLK1CrRHx9cpQNVasD8ep_IEqI9QTWC2LhvgZpFi1f9kZW7o_uVEe1rgfAI-KGNCycZCVBrV-9gRSoKej5bxP-LLVPXW7cyPYfN2_J7RxL2gv6rPn5KbBFe7HV_l6FTiRh7l0-Q8ZIJNKB-1Vz4d7wCSS4v_8aZ5GBcveE0QG6fv3l9lkN_lBKCSx2gPIPP0wDrK4-Do6kUYvI2kHfEyfijHeXyg0y8NHXALYQTEIUNZuAasIBSwXMkvGLlwurDk0Fo0dPahKGbmn7wgSZJBlxmmZotEspp1ufcxx-uoH8TSEkqCfQzLoaIVtZizBta1VhqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26763" target="_blank">📅 18:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hpokXz3LU4HweNx8-kwILcG7xXDRWo8OzJe4boZxQEM4nuj4QusYxAM2pRioe3vlVbPx916yE9996zq_YXBYse1v8JEByL2SV-JqjO3gjBwE4zq9dk0osSHptA0OfQYfYpiWtJnC9XT3MalrozuARCXCI23DtfYbt8W_o4T_8nsCyP94cSPlsTdlad5iKWACUPusKXh29anVvd5LjCIUbRnDrZTdMrkaboa1dFPJgF9nt5u7TCV4-YA3wCMK6bCtHbfglp0b5Gjcg32vx_d17k4n_RJnC-y-4UqtkMtXI5DGqXtZI4n2Jh5QU2iLQ_55CQnrP364kCATnZql_E3PHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
دنی‌ولبک مهاجم35ساله سابق آرسنال با عقد قرار داد دوساله رسما به‌چلسی پیوست و شاگرد ژابی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26761" target="_blank">📅 18:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mnb6Gxx3JVum60zVFvTjqiq70crjRrpEsq3Zv6NRn3FB9fi-I7f7Yw3jO_aup56umclhWVzPXXLqRTkoi0TIM0EawQ5131dMMDXfSVNrUwuh7Eq9awIrVamygVPhERnMxcD2l0xgS2loSYmmVTrP7iDPVSX5uCvz1yHn13i5LKRLhbEYZcfuScgZwBzhtQBe_taeL72ItGICfHk754KeDPctyGSfthKFnEQatAJUx6Hp4IPNo52lxSg05pxSkiRT5oH9chLhq0jS0kKRjmhfgqXajnvt1kRsfNpqEMyGixxVwuHYCvTUc5vjr72vzjlx1Pc765hSWqO33rLckVoHFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26760" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mTL2SVPRO3EDX0dSl7yaiq5bA6Q7W8Qp3W1UFwD3OPsy5jNV3F4476eqGit38L7rmOv09RJkyLawD_WlsLXM6smB1oQxRwBl6MYQ5K9mPxtxWyvIz2YAd7ksZzO23W7H5KMqfkdUWL8bQOCO05-2ozOl6lk5YmizGTqdgyt087sf8gqRRhyk9KVm66H0ysBobzo7yOvZPgAit1uegOsbYcOFCGIxUnuNTpRTiEVtPgJNRmLX-HjvQxZXJTJRsjUgcM_jTRXfWASHJlRBgiWzRvETTfdPbiTBAx_8PTvpJkDT8nTiwkWlgOcsPBpydtKQYB-emkB6D1UwzzuCxPkBSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🇪🇸
🇪🇸
باشگاه رئال مادرید بعداز توافق کامل با رودری کاپیتان تیم ملی اسپانیا؛ ساعاتی قبل اولین پیشنهاد خود را به باشگاه منچسترسیتی ارائه کرد. انتظار میرود که سران سیتی آفر رو قبول کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/26759" target="_blank">📅 17:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26756">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fzxOi6K07trL7ro0ivf9dq0h5mmr9TdN9hPxtjrAD6Z3G9BCXPjUuXV9kBFvORh1TBCOb8TYW_SHM1l_4-YvlykpXS4ixKLDlz0fJbnl9Nv73I_ZJw3jEjOg1l4Slt8jz6C13vT456eBLipFXNXL_2SEHkS6aGSvECnlf9wXRvJ-nGsr61Wmh3k0YxBfIt0W-dMLdK5Cjzbusfat6ZSOXU42cIoOnU_NRPs_3ijAyfBLHeDG9wHWA9GNaqw_EW2qBx9_FQBsunk6p3htCLug8p-9hyL0DL6qPDyaV_wwO5bsQsOzvJPdSyg7vMPRd_P4wg238ZQ4vHbsdzm2CNVWrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rer4RD2Rh-Bwwc2vExdpvndxYAhuV2TJeXcz7Z9rNMnIBURgI-dVmGvTD7Gr-DshQB6D2PqwZC5EVGvy5yAXu8G0RiYElWP7J6HBFWEQH_rg-FMQMN5KZNbxl3ce4SAu_U6dzAAEndjtaIX6uFC0VNe1WkjO7JkbBHcXetGf3BIgF5HTjrbdaQDRBZp1hblzdXXUbuGnCNCn4Qpd9xtYNW1BDx1ALqzYnj1vo2HAoI2umARBs-aPXKjlCTbskYcp9y7Vi-k4qG8IkNBip6mTf_DSeeR4aXRjn-de2vbn-uh5ltf0CdqOugwfbqvMCSC1ULdl5vgklJ_MxnzeJ64a4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب‌منتخب‌ستاره‌هایی که تا به امروز به هیچ باشگاهی قرارداد نبسته‌اند و بازیکن آزاد هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26756" target="_blank">📅 17:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26755">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=MYSKVGNiYFXZjhlqS-qJIrthm9XfCI5m7erP4AtsVtyK3tSAFQsLQeTrdJ1jnA-QIMMfxFmaRaGd6_kDlYxKls1iQ5iuXvDRN3Up4ChHkSpV6-obUoNGWpgUaIoxah_pyIkZMao--giSFMHbF17kP5U8jSz3DYEqqCqdW0cMjPXMygWAuFNADiOBs3STUIyn2ZbfJIJtee-ijF0NIsaGCTg8MTN12l7dnNiAg04AqbluhBHVX2XV61ab91HkvQNOmZhv4OjuVqf-fdc4uyTnT7ect9oHEI8kaAi5qXfw2Qw3orwk1CiacAvqrNzLMW-36nOzdiTV7WQzAX9KS0TyjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03d21e0c25.mp4?token=MYSKVGNiYFXZjhlqS-qJIrthm9XfCI5m7erP4AtsVtyK3tSAFQsLQeTrdJ1jnA-QIMMfxFmaRaGd6_kDlYxKls1iQ5iuXvDRN3Up4ChHkSpV6-obUoNGWpgUaIoxah_pyIkZMao--giSFMHbF17kP5U8jSz3DYEqqCqdW0cMjPXMygWAuFNADiOBs3STUIyn2ZbfJIJtee-ijF0NIsaGCTg8MTN12l7dnNiAg04AqbluhBHVX2XV61ab91HkvQNOmZhv4OjuVqf-fdc4uyTnT7ect9oHEI8kaAi5qXfw2Qw3orwk1CiacAvqrNzLMW-36nOzdiTV7WQzAX9KS0TyjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه‌ویدیو از الان‌وقبل یان‌کولر ستاره‌سابق تیم‌ملی چک و باشگاه‌دورتموندببینید؛فکرکنم کمتر کسی پیدا بشه که بازی‌های این فوق ستاره یادش مونده باشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/26755" target="_blank">📅 16:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26754">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xj77F4t9ZT5iKXw930N3wYmJCxhGP2OLZMZ2lq_6LtHh-kG0emsvCv65DiCMrGVYhY0MrYSjlfmL2hzu3pdbxjYKIVcb0Uvsh-gRYPwg83XHBO5XVpD8BhWvPfoMN20TMvtPCGCiYQpYfvrkHTWF__vipPfyROvFoLQJRU0N_f7kA2zYFo-J_0k6lr3o_zcwAo2m_ks1p30bKNr8Zvw72ngkUAI4zOa0uJtRLwwocnv0INch-Er3v5VWIxsMRZjt0iuG3dIQIv6zfYA123wWxUA6BCtzhmHnOF7STVHazCg6QSMuqLAWUuew-1TdxI3IALvRx-ZaglSjTy0YAjBccw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26754" target="_blank">📅 16:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26753">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🇪🇸
👤
امکان نداره هواداران رئال مادرید این ویدیو کوتاه رو ببینند و بغض نکنند؛ هایلایتی خاطره انگیز و دیدنی از مثلث وحشتناک BBC در رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26753" target="_blank">📅 15:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26752">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aZo3arrVtzRtfa2PLXu8sEnGig_Jbyccl5UGqwl8FfB3BagYEJwQl_5U1HgmyXZKWAAJ9DydMir3rfeISwwlGZFx0dUGoUteZF0MelCzSMJ2rMSlEapZ8vuH8So79rLhbbfx-rkb6VvA7Sy6BbqKkosJIKDa6fth6cOFfelodzK95yGx8izQtG1HP9MJ79HQfwpoJdgrAEf5RQGL_EcCHKe7-YE6VN6Cp8iJviQ2BY5cxzWYUOyFLkSEggC3JSZOISO1liD4chz-t2Vsqnu5ntE5cf6fKtJU5SkirYNVauH5xKAlycuDxd_M4dRzYIbxJIUA_ylk_KjHiBTcWfWzGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
نیمار جونیور ستاره سابق بارسا و تیم ملی برزیل ساعتی قبل رسما از بازی‌های ملی خداحافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/26752" target="_blank">📅 15:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26751">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=rLnXJvpkzU4mj2XgflK46r5PEbSymrLDULAgd5WLSZCSkWCBaqauViU03m7CTj2m6bCy1cRIevo6352914iFIjxygegAd8xy2SQ1gLltwdHcvGBsSQPO90MpXtJ42RlQAQj0PtwT2qKXDxdjvJTcYPLtkMKPd3htG1Dmqd8IIcNXZvhdDZfWSZ822i1JandZIAtjigbRuw9NJJp4xDoo3_InReDnBZA8qE15Fd7_Yh3pFgw-4JTaKHzhzYeO1F2x-TV3WWMSLEgm7mNylc10cI_mjU1kPvYWhrsVIv2sqMZZeyLEzAFRC3qTI97_MU56fyG8jA4CkqWYT1LlLB5_5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4c3851e11.mp4?token=rLnXJvpkzU4mj2XgflK46r5PEbSymrLDULAgd5WLSZCSkWCBaqauViU03m7CTj2m6bCy1cRIevo6352914iFIjxygegAd8xy2SQ1gLltwdHcvGBsSQPO90MpXtJ42RlQAQj0PtwT2qKXDxdjvJTcYPLtkMKPd3htG1Dmqd8IIcNXZvhdDZfWSZ822i1JandZIAtjigbRuw9NJJp4xDoo3_InReDnBZA8qE15Fd7_Yh3pFgw-4JTaKHzhzYeO1F2x-TV3WWMSLEgm7mNylc10cI_mjU1kPvYWhrsVIv2sqMZZeyLEzAFRC3qTI97_MU56fyG8jA4CkqWYT1LlLB5_5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
تعدادی‌از سوپرگل‌های تماشایی سرخیو آگوئرو در دوران حضورش درتیم منچسترسیتی؛ آگوئرو در اوج فوتبالش به توصیه پزشکان فوتبال رو کنار گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26751" target="_blank">📅 15:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26750">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ntz0VHEdSmnatTIwhqcw5UL0YUnH7bcRNr4cYsH-jwr3yhZb6M7YOlNY7ECNyZaoGCK6Cuov5crYeFSFHN5Dei3Slb9KibH-D0m7e4LbZaiO79MNMLfYqH-_bE2DvoDXseNBCcE_KI0O6W2NBfRZGQdb92NZ_a6UgrBDA8P3M7gC8Nez1c9W4XUc-ak3XV_KFiKGzUEuRF5xD-SRah541mgLa-6mw_nl8Ml73MDIaLD9tldOaiREI06bO6DMsWfJqhRQYap56JSTeTmGg1NPN9w0Yu98kZHKgnsQBi4uvdHWPnBFsxHlkX7Z6MCxKYkssJB_d-escHhj0FyOaOL2Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های برزیلی مدعی‌شده‌اند که نیمار جونیور ستاره 34 ساله سابق بارسلونا تصمیم گرفته که برای همیشه از دنیای‌فوتبال خداحافظی‌کنه اما نزدیکانش میخوان او رو از این تصمیم عجیب منصرف کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26750" target="_blank">📅 14:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26749">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYJweaHxNe2NpljMVNztJNexH4qfS6LyjJ7_L8gr3EUnHrjtkmpW5JRH-EPJymnYVueIbCgzl8AjWU6spVtWQ6S0ViVBoWa0eqWFchzjXXfUC2mWCBvXTyv_fRXANyVotpeODmtOidGteTst8Z0Z8sbgwmJyLbg8VHP6FLMgvUf_qYJK-Vp4EPda5Bhu4H5Nui7RjnFPJRzITyn-bEB94c_Wd0UbXansOFIbLQU-cX8qz8QA9hBqoP7CgYdVM-CQDLYZKAAli1O5ITH_d9YI-Wq2e1IObiccfNCP1KC_blJn1Tv9bPNURv0xCz3sDwS73yDvak-muzotzp5yF1knhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی روزگذشته‌پرشیانا به عنوان اولین رسانه؛ محمدرضا اخباری با عقد قرار دادی دو ساله رسما به باشگاه گل گهر سیرجان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26749" target="_blank">📅 14:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26747">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IDSrkcyXj6R6DzrJoLaAg1M_OIwUxGXuiaba0n1sD3ienO-LRm0go_59Lr4MLV-I--o5Ykv0rM6YMepGfvW9MGHdI0rz3EKXVHXtOYU8bVqdEmSQ_JzWXw9hOkJP-R64P2McIE-VjBYbFk8x6MllbN-9CbF4ZNWMfSg7ADblNeNkswEcLSGUeJZVeCV8Lmk3paeAccjUtS-Exx3-x4gBeoWl5nDDzf1QWjpYdZhRUgRA2dwTs8a6ZxkhAdLOwBMJuSjz-bkIpvTzCQ2LX4yuiKbARtPD61aN6xTljDA4j0DqkYI63iB4c6MuXm-wiIoi9ylFW3Sshft7i6FnwhsEtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dTe2TAXp8G_IJzLoBdlhsZhaFNs6zgXfIVvADgH2bfceuvZMPPuICJscUmuQr39OQrwf5EVuE5-tsj7PN2lxgFyPmbcS1EjZH8YGUz5MgMU7t5fk0w74VaR72LHUihgBJIn8fVfYCWwwEWglm5onSfYRZp4U94lf7EVI_qhiPEQFfG9mEnhcEFMOXS91MXAQUP3QESdxmh2GN5oihedVYkl376vBBe775C3QDSTJy8yyRObbcHrmdw3P10l7u2ybotJBxfqq8e5imhJ1YO_Ho6XNTeAip30SK547S1j0J3zp6mU6-KkhLVgo-s6dN7KpiRqhAMJH87UkU69jGUGfgg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوست‌دخترنیکوویلیامز که‌درمراسم‌قهرمانی اسپانیا حضور داشت جدیدا نیکو رو با یه دختره روی قایق تفریحی دیده و تو شبکه‌های اجتماعی آنفالوش کرد و بعد از چند سال با او کات کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/26747" target="_blank">📅 13:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26746">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dy_cvH3MGdGgU2W4gqf528yyn5j1xNA5_U3RP7jBzTsM6Jt1baMHzouEg0iLsZ0BoK_tfrdgG0x_ijgCQS7PBLiqmyX3M1Bwz-QofxoeCnt5JQmU7aouVTFoYbSJot-ph7HFNz5-Yx_jVi4kxjojVK9OCqTRSICRD7rUrEqOHGBjmrvzooOLDJ08ZvYjXx3mC0rH4xBoF54fRiuk2onRQ4TVUJ2UXIcycsw67_5HYOHUj0S1sd9jX9lPBuyYL54NfkW2GHYBKabX_t5o8Eryi3DcLmkDmtu3j0-yM123GHNk7Q0cnbeOy7YgPUgwLXcKTJGBiwMCvA37EJ-TqLRS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه عملکرد لامین یامال، وینیسیوس جونیور و یان دیومانده در فصل گذشته لالیگا و بوندسلیگا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26746" target="_blank">📅 13:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26745">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/389ac26246.mp4?token=KaHuAVbVoXKLnHXkOlMZAq_KAxHxZw8y4du-gL8EGQ0vg7yyxgN0D4mJJkR3n4o9xujB-dBty2KHIHBs38LCbkN53RLjVg3H6GWBzEGHEBKGiYN-a5hk3y4XnP5ud8GyIpbizJcEfeWmapIee0zXO08NPePcEq_An5XVYiodbnF7AiHcp2pd9RAtO3jnGZzv42fyGFLc3W5K8Z8Zx25PcXxMUDd3PnkWgvxCA_lh8rB-mXHcJkuloaFwhlQvmtsZjNnUnwssDnLQhZRKw5X-_l5WvsQcCRZPxIyool4D6Ltnut74uyfUGkNj5Z1-X4F-yib9e1k6IgwJ2wxCbg78tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/389ac26246.mp4?token=KaHuAVbVoXKLnHXkOlMZAq_KAxHxZw8y4du-gL8EGQ0vg7yyxgN0D4mJJkR3n4o9xujB-dBty2KHIHBs38LCbkN53RLjVg3H6GWBzEGHEBKGiYN-a5hk3y4XnP5ud8GyIpbizJcEfeWmapIee0zXO08NPePcEq_An5XVYiodbnF7AiHcp2pd9RAtO3jnGZzv42fyGFLc3W5K8Z8Zx25PcXxMUDd3PnkWgvxCA_lh8rB-mXHcJkuloaFwhlQvmtsZjNnUnwssDnLQhZRKw5X-_l5WvsQcCRZPxIyool4D6Ltnut74uyfUGkNj5Z1-X4F-yib9e1k6IgwJ2wxCbg78tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26745" target="_blank">📅 13:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26744">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6T0oKXdOXlw-DdVicpMAo12jQ2ddGt06pykuLyoE8bOPDazMlsg0wIWdjOr_2u8cFU4HimHS136NxrNmVdVhSGL3V8U_r7iakxeNyL4a90kjKjplBnbNKv9lRkOajfzkque9Y9fXb6Z6NeePleeLGBu15khzE2v7GsGRteb-pSs5esIVVH0XjyEGbdiwQVtLivcmYpDhrsq61l3-3GLwxAb24ANvb9aLgnK3ZuZeG7NTR7ACeZLOZghCWso9NYouFY68wMweXJFv6DDIb4kJjpNAnKiMJj9KlRNI9BKO5kmVPn8Xuu7VE0Zrv1fXGaoVHRnzL4gjdkTZlf033TwqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
رسانه‌های فرانسوی: رودری پیشنهاد باشگاه پاریسن ژرمن رو ردکرده و گفته هدفش تنها پیوستن به‌رئال‌مادریده. او به‌سران منچسترسیتی فشار میاره تا با انتقالش به باشگاه رئال مادرید موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/persiana_Soccer/26744" target="_blank">📅 12:47 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26743">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MOmrJJqPo3NhQSGKMe8U6odp9FOIqEgaVAN4K8AMskSiYGqpZXoSp4FyqAyB7pCzhXN31s-gmyP0c50ioR8DU8_N-INiLUqq4jzuJKisUOIYtZF4PS45N3f6cit5uL4WWsEef5mShsuU0CovgyvRmrwSxnJlujUVp7kDdCvfojinU9G1gHx2de55heklaFnfQ4W4h9vzb8md71Mw7hy2xb2-raXADRsR3E9MQ78iYicEkdFlAtNsQ5nbrQJc8QeyF4hm10noUXjl-FSIs20gDxRKlgrEYr16IZeHrryTcpHl7etY1NChXAzb2rCXbr-PL1ezhdDPzBwB_c04tPnTYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛ درصورتی که پنجره استقلال امروز و فردا باز شود مهدی گودرزی، محمد جواد حسین نژاد، محمد محبی و یک مهاجم هدف اصلی‌ترین گزینه‌های آبی‌‌پوشان هستند و قصد ندارند بازیکنان پر شماری رو به خدمت بگیرند.
❌
باشگاه استقلال درکنار این‌ بازیکنان…</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26743" target="_blank">📅 12:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26742">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=oBMvNDsYSpSc-7KAnxV0yDuBUxR4O1btkt36ZQYS3JLy-UFgN9VBzz8V-NZtKudBBcUwOn8cyZINcVvP7x_Dsfsir-hHq48xH0AJnP9zQLxJQ818Uk7g9RhdYBKikWTl4sNcDg86cmf_Zla7_RmOVsfGweTxvtVga1qHLSNKAxWQ0t0jtVZrjNPlIu8CyfH3v4hQa4PLb-jQKOPiKzgk9-vQDS10M5zFJUuN3O8mYjqzavuBWgHOpWrLRbuQsV2wPgy8xDPYk1Fj5vqIhfHoyqd2CnS6XI5HQ7s2KPGkRjK2k0bGuyPINNLeJCfyybhhLplGYRxyT6vDy6qMauG1wp0Q6Iaf0BYOrk6ntHacrlnyqR7d3X65PUJD0upsPGjgG9IltbxHh1YbVvXVDxYRsM2YWTtsRodmHqsBI5OsTOeIJyNa4KU42OEUA9d78yeQC_5x7PkuOdbt08PGFJ1eB5rz3vQCeQtUDZdkgHq_cDtUdk5nT4oa8WWU9KnX8NdSLYT7DVU8tGW88zfgFYAxN3uIFnjYo7bas-Okhoj_hxSeQOyw3C0ip2KfqGCbSRqI61e1dMq4AY7NsZOZPsqTm9HrEaOIFQPOkvGDhpuBxrXCk0uCeAg57fDlDpsDGu3ygnq6UQ7cs2Sc0CB9UDkJra7upNShm-dT95alBPAcroY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2cc2d700a.mp4?token=oBMvNDsYSpSc-7KAnxV0yDuBUxR4O1btkt36ZQYS3JLy-UFgN9VBzz8V-NZtKudBBcUwOn8cyZINcVvP7x_Dsfsir-hHq48xH0AJnP9zQLxJQ818Uk7g9RhdYBKikWTl4sNcDg86cmf_Zla7_RmOVsfGweTxvtVga1qHLSNKAxWQ0t0jtVZrjNPlIu8CyfH3v4hQa4PLb-jQKOPiKzgk9-vQDS10M5zFJUuN3O8mYjqzavuBWgHOpWrLRbuQsV2wPgy8xDPYk1Fj5vqIhfHoyqd2CnS6XI5HQ7s2KPGkRjK2k0bGuyPINNLeJCfyybhhLplGYRxyT6vDy6qMauG1wp0Q6Iaf0BYOrk6ntHacrlnyqR7d3X65PUJD0upsPGjgG9IltbxHh1YbVvXVDxYRsM2YWTtsRodmHqsBI5OsTOeIJyNa4KU42OEUA9d78yeQC_5x7PkuOdbt08PGFJ1eB5rz3vQCeQtUDZdkgHq_cDtUdk5nT4oa8WWU9KnX8NdSLYT7DVU8tGW88zfgFYAxN3uIFnjYo7bas-Okhoj_hxSeQOyw3C0ip2KfqGCbSRqI61e1dMq4AY7NsZOZPsqTm9HrEaOIFQPOkvGDhpuBxrXCk0uCeAg57fDlDpsDGu3ygnq6UQ7cs2Sc0CB9UDkJra7upNShm-dT95alBPAcroY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
پارتنر گابریل مارتینلی ستاره تیم ملی برزیل هستند که پزشک هستند و گفته دوست داره از بین برزیل و پرتغال یکیشون قهرمان جام جهانی بشن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26742" target="_blank">📅 11:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26741">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kV-SNFI0JTRAwaE2My5u80I6ouwlu1cvEXDbDNnNSkvISTpR-zHZWOnS9zML2t_Q52f1lyqs4e-q_z9vzlywjxKjtvqXhAQTUU1TAp1H_aMg2Wf6dfqzZYYiNg6v9gbo64aj-SUbpY-sby47shWcB8iuHhBeehWGL1e1dfSrIBf9PAvyd0DgrK3NsbDhbfcsMom88SXPapxCNLlyHdgEChKaV0eNPA0DfGVqy41nEVKx4FcPUjbXuk9bG-y8JeMsoUWjc4SLZuwbb6gBXB0lWnoWAji4C2_HLu51rJfJzDGN-yo6U8Wm0TDsV3b_RvmpOkJe7qtS5DI8_-nSAwJwGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیررسانه‌ای‌تیم‌پرسپولیس: اگه کسری طاهری و دانیال ایری رو‌جذب‌میکردیم بعد از هر بازی رقبا از ما شکایت‌ میکردند و ما هم‌ قید جذب این دو رو زدیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26741" target="_blank">📅 11:14 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26740">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cwe6Jqq7IMFe0pBuHHlF4fouW4hNWRv8nO4KhIICq67EthIE0Zhzp7gT9OFBdSHn4QSMEb5X6FYmnRgd_0Q3AVk9zwPx5dDrnpVJ965fg_mKT8Bjh0Ukzqt-bjPBInLTo1mGtSGIWOFltn8jM7Gac7BLfi_xdD1eodYj5CifwAb912rRiahDdpwkj3e880gEux55fB6qri2NdtHb3_PNvgY74gHSOaNbghbmBOmVaL5ZrZCGR-C-KK3YE6JkZ3F_0WNa87RYC6YnaakiQ1SLB2pHEAxUOfB9qWxZlRWfMhjrMqFYDIhaKtHcaLvtWW16lzqwCZdA9djjA5NaUcQ8Wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26740" target="_blank">📅 11:00 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26739">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98e9665500.mp4?token=uu8U26KhzhavF-7hpwkJX2wS-IUoybw_8QCLQqt5dkxU7o42uyFy8G444XG9paX5_Bf3QXoELhwC2rBHJBh1Ffjd4TJou6HJoUxq5lMUqpt-TNYaS-yUIaUnAzhHFZf12DU-Kn2pI0-LvqLBU4SedlOFYUHchzC_a5NHMeD3db2g3IWqXcVOY3lWJD_Hsi3Rj7Ysd9scYszjK0gMggp3hh3_GubmH6Ve-K_gLtWkeIu3eDaD7CEizaGeyw5VF_wmS2cMspF3mNgNfPoLUHuGZdNclupxw3p9BH5sTSlIfhSYfMZove7LNBpjmneOQ9pQ_cSimjOkRXmikXscxSqiEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98e9665500.mp4?token=uu8U26KhzhavF-7hpwkJX2wS-IUoybw_8QCLQqt5dkxU7o42uyFy8G444XG9paX5_Bf3QXoELhwC2rBHJBh1Ffjd4TJou6HJoUxq5lMUqpt-TNYaS-yUIaUnAzhHFZf12DU-Kn2pI0-LvqLBU4SedlOFYUHchzC_a5NHMeD3db2g3IWqXcVOY3lWJD_Hsi3Rj7Ysd9scYszjK0gMggp3hh3_GubmH6Ve-K_gLtWkeIu3eDaD7CEizaGeyw5VF_wmS2cMspF3mNgNfPoLUHuGZdNclupxw3p9BH5sTSlIfhSYfMZove7LNBpjmneOQ9pQ_cSimjOkRXmikXscxSqiEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/26739" target="_blank">📅 10:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26738">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=BnjoqT6dCOu25D3mz0hIVKoywN37PvB5Foin5GvaoyzQMSUJUF3n9HbRdUIeAajJYuK9ia7XmZiAV5kjGrTrRyq3qCyDaoLE8xzoKmT9Vj9Vr5pWoHrSih6-r6bx-kadyURt5m0YI5C71wyJn_BzfKEXYvVj5WfzLdvDtJt-qeOG3oET73AzExR7WlkqhfEE3xqe8ELSfrJwGi9medhVaRI41_v5cUux8mVsuPY_NQKTCsTj4VA9VqX0XuMomGDYfLEO1PBDy3Zeji46ZUffOfhZBuJCR8dCtBSCt_-vBH7ndthLSAGSKSDXNmwBisI4jaV0Qm6kKYJJFelPSjfJ5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96f6912da5.mp4?token=BnjoqT6dCOu25D3mz0hIVKoywN37PvB5Foin5GvaoyzQMSUJUF3n9HbRdUIeAajJYuK9ia7XmZiAV5kjGrTrRyq3qCyDaoLE8xzoKmT9Vj9Vr5pWoHrSih6-r6bx-kadyURt5m0YI5C71wyJn_BzfKEXYvVj5WfzLdvDtJt-qeOG3oET73AzExR7WlkqhfEE3xqe8ELSfrJwGi9medhVaRI41_v5cUux8mVsuPY_NQKTCsTj4VA9VqX0XuMomGDYfLEO1PBDy3Zeji46ZUffOfhZBuJCR8dCtBSCt_-vBH7ndthLSAGSKSDXNmwBisI4jaV0Qm6kKYJJFelPSjfJ5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شوخی‌های بامزه زنده یاد اکبر عبدی با همسرش درآخرین گفتگویی که با رسانه‌ها داشت: کسی به من زن نمی‌داد با دختر دایی ۱۴ ساله ام ازدواج کردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26738" target="_blank">📅 10:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26737">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jmD42sN8_NGJVfQriilwHXVTJ_8SvymAZkHY3Gmc5wJMkhTk7A7eBv1kaRYm_cDKET34wbi6B6NJ_pPa0gyDuXI8rNg3G-W9HH2YLvz-a1Yf-4wgrgm3m-qrV6h-bq2ZlczLIzghMnLII0WBpqyCysIvgz04uuzqG4KEdposUsIRX2XHKeZK6d2ubvp5neRUv9IyIJLYvjfn9CEExCi0BCYpYGs8rCElKPbtvKs_TlRWO2rACfsko7dgzTft00pClhPbHG70AM72D5L1Ah6rvSEc2ZGkjHbl9lkTw1lxghh007hB3LH38h6pULLL0XlK1uTX97oukSezuNkZawFbOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس امروز صبح با سامان قدوس ستاره تیم ملی و مدیربرنامه‌های این بازیکن جلسه‌ای دو ساعته به شکل ویدیو کال داشته و به این بازیکن اعلام کرده علاوه بر پرداخت مبلغ رضایت نامه حاضره قراردادی سه ساله با رقم بالا با قدوس امضا…</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/persiana_Soccer/26737" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26736">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXZl82EIaMP2NpRPLn8qlHbp_Cs7BL36b5mNm0kImWUMgMSgaaSFeAJrlclQOh6ABZxc5oYzK3ZxolLmlJCD-uLKyFN-wIMm4VolpDcem0kGV5qV6nfAdI6Rn59IRQqclRmgBLU8hVQr1AAD1tQe4UoZ8C7wRbeAnvca0ciwobWS2uWM-BXu_Uvz_XVhgWJmmlYpyJw0WK3PCNVf1Ka-FAaRlj_ddP0PIrZf7IKqrb5z14hOmw_Bv6P6JKqhX95PnsIgFO_3huodpgqT3WKsNBl7X6eO6XAIf7puKV2PuOgRUOGJngMIqmppeZRGkZISCl5BRArC6vfqV_YbTJSe-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
برخلاف شایعات مطرح شده؛ همانطور که گفتیم کادر فنی استقلال خواستار تمدید قرارداد جلال الدین ماشاریپوف شده و از مدیریت خواسته که قرارداد ستاره ازبکستانی آبی‌ها رو تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/26736" target="_blank">📅 10:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26734">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hSqhNLAddwpJN7i-MfP_29aO-5_-YGx-d_GzAXVq2vSy-UzBhQY2zEQkUA8sPctfDXynaF_Wx88IUnS0DOt6jDtkCF_CRD9OJEQ46u-mdYex60QY2nbv_sU5G2LopR_fODYiVgw3D2g-j422UmLf_IIIl5kBX_mbNMGHGRyVDmTNbEI3OgGr0FIGpp0L17MU4U2PNsvXFQzNByeAqDVHPqgK_jIUi26CtCTAG2-uKyeb9EFthvV0fw14gcEym9-okh5jlPlQdSawxJ8QgMkrvJUyoc9W3hg-6aYABZjUwsus5_NRovmpzMAOrvBWmc3KgYEZkxnAjguFauSz8SZEtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛ ایجنت ایرانی نزدیک به‌ عثمان‌ اندونگ به مهدی‌تارتار سرمربی تیم پرسپولیس گفته که اندونگ از سپاهان‌آفر دریافت کرده اما اگه او بخواد باپرداخت 600 هزار دلار میتواند رضایت نامه این بازیکن رو بگیرد و او رو به پرسپولیس بیاورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26734" target="_blank">📅 09:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26733">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59d676a359.mp4?token=D1czr_Sa_VdmgKvR-iKb5uMMYdI1-bZp8Dl3JkGyPA-frEZKTwZ329BgzvrfI_xzawwRozjGUWLKJstgBM2hwUErRgoWM9O5DnvMXvagSpMOi9KzYxGrcHKHBgvXibJsC-AR46vF1R7HCTP69VRP4cMjtMoTyC1OIJ7GDFVtbBS1wWC-bhdcwAjS263GRWw77whD6y9ZhrGc6Fb7Qd64xu57RCeQ-EjnjV1V8TFQ54oJmCjfLVoN2pYKxi23LFiI5-8dthhtgyU6suhkeMct08tXvyym8vY8HC8LghzRk2HetQ47AeDWqdvz5rPFr4J05Wey7Cub_re8C2uzP9FGLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59d676a359.mp4?token=D1czr_Sa_VdmgKvR-iKb5uMMYdI1-bZp8Dl3JkGyPA-frEZKTwZ329BgzvrfI_xzawwRozjGUWLKJstgBM2hwUErRgoWM9O5DnvMXvagSpMOi9KzYxGrcHKHBgvXibJsC-AR46vF1R7HCTP69VRP4cMjtMoTyC1OIJ7GDFVtbBS1wWC-bhdcwAjS263GRWw77whD6y9ZhrGc6Fb7Qd64xu57RCeQ-EjnjV1V8TFQ54oJmCjfLVoN2pYKxi23LFiI5-8dthhtgyU6suhkeMct08tXvyym8vY8HC8LghzRk2HetQ47AeDWqdvz5rPFr4J05Wey7Cub_re8C2uzP9FGLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
تیم فوتبال چلسی تو بازی دوستانه امروز 3 - 2 از حریف عقب‌ افتاد ژابی هم کل تیمو کشید بیرون و بعد ترکیب اصلی گذاشت تا بتونن کامبک بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/26733" target="_blank">📅 09:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26731">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=pXjezvkIMkeRV6QUatE6VdXEPZxLJ1LURBGah6or1jErgcg5vJ3L5XnthqlH1zagMjItLOfNg3WpZhDiacDX1dT9s1eXB38QDSnSu8M39jqfkd5ZAINalhinRRW_LbNOtG2WY84YC11EJZ34BehCjw7UhzYPcx6fpJxmWb1eS0CCn4F3BCGepMKpwoub62TTKgxLMBTMgE4YjFfVfkCfPe2Idn74K1mNzlQnXntlwqKDYFftnSfuj5nMPLFlhSIMr95cLP6rCjd9MFJ9e8mVUkU_sI8VQz2ZaTasHerMv7zzquqamvCYC-HO6zDafUK0RaFEUaCvJHIELK-1i60TwG8FPTWyMRdymXnCFKm3KtcL8QQM3jrfqAnC1YLo0DFtK89EirL4EtAI4jyDvJOgfD1_AWRfvz2SV9vhLnNpAzt6M7Q8Erl_hFnQ8cTL8Xw5FAQqV7kd6R7IpkhMXshIM91y_kkNIhYUgydYmTMw0XYLS86nrBGy_HHRkVRcD7_iLhGzt2ZmW-0t2JuTsVRr11s3YgXikC8bOZ95ta5Rh5pdMAo3qWHzFMvNT5a_Dg00sCIyPIlkZlffRv6LMe3KYGwbxWmFuBJZv3a7KdTmpiukYeYQ7tHtfLkbphOnVfqdEb-OyZIKGyJvva1TWGGcRc9g6GymsvhrUBHtXAmch1o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/01bf39426f.mp4?token=pXjezvkIMkeRV6QUatE6VdXEPZxLJ1LURBGah6or1jErgcg5vJ3L5XnthqlH1zagMjItLOfNg3WpZhDiacDX1dT9s1eXB38QDSnSu8M39jqfkd5ZAINalhinRRW_LbNOtG2WY84YC11EJZ34BehCjw7UhzYPcx6fpJxmWb1eS0CCn4F3BCGepMKpwoub62TTKgxLMBTMgE4YjFfVfkCfPe2Idn74K1mNzlQnXntlwqKDYFftnSfuj5nMPLFlhSIMr95cLP6rCjd9MFJ9e8mVUkU_sI8VQz2ZaTasHerMv7zzquqamvCYC-HO6zDafUK0RaFEUaCvJHIELK-1i60TwG8FPTWyMRdymXnCFKm3KtcL8QQM3jrfqAnC1YLo0DFtK89EirL4EtAI4jyDvJOgfD1_AWRfvz2SV9vhLnNpAzt6M7Q8Erl_hFnQ8cTL8Xw5FAQqV7kd6R7IpkhMXshIM91y_kkNIhYUgydYmTMw0XYLS86nrBGy_HHRkVRcD7_iLhGzt2ZmW-0t2JuTsVRr11s3YgXikC8bOZ95ta5Rh5pdMAo3qWHzFMvNT5a_Dg00sCIyPIlkZlffRv6LMe3KYGwbxWmFuBJZv3a7KdTmpiukYeYQ7tHtfLkbphOnVfqdEb-OyZIKGyJvva1TWGGcRc9g6GymsvhrUBHtXAmch1o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26731" target="_blank">📅 09:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26730">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lbUgyORBXS0LL9ftWf3QRUk6RGMPQKxsC1KNGeShh2a_cVzrk8pRX-LOVJ2CfC2qlUUY5aWvZYGtAj5quvbEEpk7QwpBqRJtmYd8ThXd_K7SQDVn3A8-JwLWzUmqMOaUg9pOAQC-mnIr31R1wIazU1Gn18Op9EQuGgpzbpAF6FZfCuwp7qpvzCVWlU0Lr0ASiH1oq-iVcrPDsIYaCLV5So74aeiCFxheojb3ziBsgOkAuNstUsAXVUWw87NhyQQe-6e0yff9lVb4jnRveBcAh4u1NhbDRTzVr_xbxCJi3i0ETpLXzAgljMD3QiCMVFNiivHjMsY489QqPGA8TptzvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/26730" target="_blank">📅 09:01 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26729">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HaAUJ_Ela6W-ql1fxS_1hKR8dxBheiDi011yM7phn-zQW_IKl69qUNJPHGvfplDTX5vH3WODA9-HvcD6riNmMpSppPL5VkVmickNjSVg8RxW0n2D973jbauEiDng8d8e-IKWR5vjgLZa3unJXqp8TGxCkUa5h6fBi4OQpqa6Oxmr0ovjsJRt0hBCqmh3R0ynA2EB-YJNh5fTFmPevX0_h9ugj-_0UERn37tLw6aBAoLNCS65KihYFP0-PjxnTPXeu8R0FHlrT0Q9Nj7RfLovQUO04vDkT6aA0xeta-EO78KYSHET0D98FR04orTzYCsEHgK9g4BBdzUJsxf6r5xmrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از مصاف دوتیم تاتنهام و دورتموند با تیم‌های آسیایی تا دیدار یاران صیادمنش در دور دوم پلی‌آف فصل آینده لیگ قهرمانان اروپا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/persiana_Soccer/26729" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26728">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aW4OzApvxaybQovMXYh4wOZS98gvDwk7LXdlMVzkp8N7rVA6jTt4clVsF5AFRXZysaNY3O7vZQpIFeywnwdr402uxUPdTtOzRyrmmC0dLZ0bhYek1L-xXiZftt-_JO3Uhjz5_h0-7wPpj740cLCs-l8E0THYB9yMZb6m33RpWPrttblmyw7ZWV_u1Is15k9vIPfrP1tszuRc3dskku-v3gIRUOuKqSCFC9SznL0tdol6GTkgJipF2wh5fcnWVgmWhVQqnN_kZW70yzq_NHvEtC_WNhZ5YO0gxeElBJ_8-eI-rLxykrPMdiKWufCJ0kKId85mR3YLEMiZheLzb38OuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج ‌دیدار های‌ دیروز؛
برتری شاگردان آلونسو بادرخشش‌ژوائو پدرو و بردآسان سفیدپوشان مادرید مقابل لگانس با ترکیب دوم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68.5K · <a href="https://t.me/persiana_Soccer/26728" target="_blank">📅 07:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26726">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyyPPNI6tTp75LiceJIiGQsBN2KKL7_AIikGgPvWCnJkn19cghBnzulGojkQE4z4Sa8WeRfzSgvsbxBWroDFLuwZ0MirHzGaWUhmhbq_ugq-GqXIMDiTMQ3y3ZFovWJ8xH6HVLSGpuG7xbsY2hmwXNkwh7cmakPuCB76aw6wWkodY6AC5tV6FReo5eWyIzOW2WwvA3gknTLMFggWF3M1PPyH_oDeaO5v0ZE0Keuh-J4MlHLw2f2baO4GrLJXW3UTti5GErh_j0A7CiseRNg_Z1WE1UgSDMxAU2vKMKFJpFgepmiByC-HMwTdDjJ6PdhytHNfixusUIIKJmzrZYamjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvSVJNusF28jD1eiX9TvG9LXLFSWFx1M-zi2z3lBAxywFmxNL4GKG8TS2iL0IcE7Of3WKZl00crmUx4xAMy1gwzEbZC1YlPpD-HWE_SErn_aa8JHJVLoTQs2ku5Yos2Fgv1_-TN6YHBi9jX_mAVm_iqcpetpzJKVy3TJAgQJ0sFKuGVsO4Vz6l-A0E8iRcLhxqkEFWz9gyMMlLCDyAm19pubxlbLR8vXo8Ht2nocNgRpG6tgRfoLYIpAVWwakeMK5nJU7h-Gn1_Xu_WqmCqdKzVsHaMyUBLk34gWfG8Cw1RgmIljWLJDV6I-NSwSeTtJ_AXx_IvCzmfBU4P230_wdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه مسابقات سپاهان
🆚
تراکتور تا پایان نیم فصل اول رقابت‌های لیگ برتر خلیج فارس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/26726" target="_blank">📅 00:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26725">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GPge_dwPdMIIlfeC9xUVBOVnuNUrzTQDEFirV5Sw_4AeSKh2TAsyNyZTKfCXccgN3pYC5I6aemKA7lIMUTgpBL43eX5aAqDby3pASBQOJf4n6R0RXFgFf1vObTCc2UOCL_KUW7g89ISW18rNCAdFsS3oslEED0haNNyFggh2AIL_zpHVQahnfw9QedpdwTrlaYjF-PUQKHf8OrBINhyzP5xgR-9tt1iPB9lqueVZBBYE94j7aiDwJ_qRcyelbXbRMNrEVKlrbvO7CSpsm9UMSyYkeCPwnnf_OZl52SoLWSMNpXg5M68paXg4np5hifkKyaOXO-k3X26szUbGwbYsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
طبق اخبار دریافتی رسانه پرشیانا؛ معاون باشگاه‌پرسپولیس امشب با سامان قدوس ستاره تیم ملی تماس‌گرفته و درتلاشه که او رو برای پیوستن به پرسپولیس راضی کنه. باشگاه پرسپولیس اعلام کرده مشکلی برای پرداخت رضایت نامه 500 هزار دلاری قدوس ندارد و تنها اوکی خود بازیکن…</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26725" target="_blank">📅 00:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26724">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q3bbZMakCTWQNG-CJMP4uZtt1-iAubEM4l3uvEcgJjSPlBzxdN_J4f5g-0zvQ4ZIVAUd-t_ALFPkapSZk720neEfcvGIw-3-V4HgTn3Z40Tw0S5fppnOCyLuxb40j0L1WEfVUC3JD7LcrTNgeYE4I3mK9b7gylDbXh_Od1cXtZbhXjzeZprViMzc6WXcxmwlRqk6ZRhnCTTTEXKdPdPjW-Z0HLk_hbhVe3EsfQKKjkdaNQJ0f1AHAO1UIdg5h7yNZxolSXnEN3OeWXoIGGwrapIj6F_R45cQxC-7BI5EClUo5IBWbVXUzttosjQnz4xWg4vslPMTL9ISfBeieDDxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ قرار شد امشب‌دیگه سامان قدوس پاسخ نهایی خود را به آفرباشگاه پرسپولیس بدهد که تا روز شنبه زمان خواسته. طبق چیزی که از مدیریت پرسپولیس شنیدیم قدوس‌خودش‌اوکیه به ایران بیاد اما همسرش برای اومدن به ایران مردد است‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 94.2K · <a href="https://t.me/persiana_Soccer/26724" target="_blank">📅 00:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26723">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=ACA0xUEmo2KWS44sTeaZcXirVKYyriR-MdUaK_WJ5d8JObjUfsXbr19GsBESA3H-AOHgmvlB0C0byW_2atX12fkGv6kwbG7NPMEhLkNNZlmPo-HodlsyKPjfiIQe511cIVrX4Z_xMYDcAXtnFnnEfosUT1f1bMyrt1LbUTSDd560HuxDWvzyEtOwUlYNobMi_tMkUtne-66F_nQJ0KNB1dBpKsHfuKZzW0TgNlh0u1T4Bm25bql4MPgmFiKgFJ20WsWdwJpkmvyfSNBc6GmN281fW44nYeNObqAvkQSvM4_q7AP6L7cgfGk0_jXypanx3nyiv7sLryi5JjLUmm7j3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adb5d2d50b.mp4?token=ACA0xUEmo2KWS44sTeaZcXirVKYyriR-MdUaK_WJ5d8JObjUfsXbr19GsBESA3H-AOHgmvlB0C0byW_2atX12fkGv6kwbG7NPMEhLkNNZlmPo-HodlsyKPjfiIQe511cIVrX4Z_xMYDcAXtnFnnEfosUT1f1bMyrt1LbUTSDd560HuxDWvzyEtOwUlYNobMi_tMkUtne-66F_nQJ0KNB1dBpKsHfuKZzW0TgNlh0u1T4Bm25bql4MPgmFiKgFJ20WsWdwJpkmvyfSNBc6GmN281fW44nYeNObqAvkQSvM4_q7AP6L7cgfGk0_jXypanx3nyiv7sLryi5JjLUmm7j3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇩🇪
یادی‌ کنیم‌ از شبی که جود بلینگهام بابت پاس تماشایی تونی کروس به وینیسیوس جونیور او رو تشویق کرد. بهداز خداحافظی تونی‌کروس نه تیم ملی آلمان روز خوش دید نه باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.9K · <a href="https://t.me/persiana_Soccer/26723" target="_blank">📅 23:45 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26722">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X3zJ33Vvs-I0k7LbEAc_kD0fSpTtxIzUg5A1pN1qOzIPgdC4JpAZXiNwdnVjjUjZtmqVRMql1pKaU16JUo-TH8S8FeDdW37MZ0oaq_Jm2coAC0wo5PjIfvxVzG0DNL-2P3J8JdEY1ewVvRhPCoKz8w1AQBnb6m44O_hJ_EL-WlIxMQR4j26vZytClHWu2ZdNAQmtPSk6UaZetu6QV0HPzhZFXIdl-mP3qY8CNJ9-LT2zbXI4On4No13e82wf1rO8f6QXodfNhYSbc8-qmDq0mAozJDuEYhNUjJp67VGG8-3OCyW_zQSZNdaa9cPyM3EOwUF3pmklDw6eoHUFMMSg0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌_پرشیانا #فوری؛ برخلاف اخبارمنتشره‌رسانه‌ها؛ طبق‌پیگیری‌های رسانه پرشیانا از مدیربرنامه‌های یاسر آسانی؛ ستاره آلبانیایی آبی‌ها مشکلی برای ادامه حضور در این تیم نداره و فصل اینده با شماره 7 استقلال به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/persiana_Soccer/26722" target="_blank">📅 23:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26721">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gx4lF36YkahCleud_72SlekqFYApd04zvfMrwQzmiXzGHCx24VBOuqTSR_WKFXRFY0YnAEiY96ZeuQM6oJVkDbmfRYODbdOvJHeFht9Om-dUFub6PtjRVZUqfSM-8oqHrd_RSeEBW9jnKwdjiiJWlMaKVDloiPZYZ4EsUNWic0KGCCysOAwWHwngZhpUiKc8_lCCMNoMVcOHNgj252EBWQM_3Z9kSHCP8wgqsB7NegnsMiIh_19u_HocsWSBdp_YcGQk7TVX8iRQx8t7bZIRiUExsvpJ5KIydi-A5u81nic2ROu3aUTJe-cu0NBqYmcj3yOQVSU8EslV8qtZLB_TRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
احمد گوهری دروازه‌بان سابق پرسپولیس اومده ویدیویی‌ازعملکردش‌رو توپرسپولیس رو پست کرده. تاجاییکه خبر داریم مذاکره شده. توافق هم شده اما تارتار باید تایید کنه. بین گوهری و عابدزاده یکی به احتمال فراوان گلر دوم پرسپولیس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/26721" target="_blank">📅 23:15 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26720">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qvt7MZaGo_8_uLA6oWFgaMhUOapn1g1DLlJrk7JP6IUNNwQG4_H9Dy-qhbe5efVYv4FkasOXJrKLDaOBzUnQko2OPoQxjHoRNJ1BpiX-wDW4NX5RuHvoUxDrao61uPt7YYvWwXzakrduoe1mlrEWfxxjw4AJNPdiQHCOKHwrkd2FA56Bt2MbZLAXoUTdSUDbmZWjQv10TxqXz3-YR69gHKlW1QApAzf3fHpeLd1Hiea6nn0Q0PBBq12-T0hXaOdHD2g5dFQxx384FXWi8Tlv6xm95dSgoRtXs7qkfDFwDEFWFdglhxUZ8MwyPaLIeGJfPiiaGQuxF7XcnoBIHaDvng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/persiana_Soccer/26720" target="_blank">📅 22:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26719">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g64UXB2-z9d8ORJW-tBz9W7_Vp9EhBVRy0AkdJFNZH1qKd9-rWqx4EBlJRb1nhPpFLdDhRYwE1uDyNmax3lWlCpKP4LVA6sarL1-2lAF6lScpiRB4ViNxuNM1YUcVezoFL8aDND33t480AV6Ap_6d36CB0Oaf98kJrXrYaoli6zRj2VVJJNKIHLZhhpOwEdsS_D3YVRJk6IRaFVvH08kc5WCr4dhZBwvWePgT_Hgjt0aicuWY8Bn5XzJkWlhXPfWd-NaVDmVjHAJqnx8ZAcrhqWH0sQTGo5y1ffeRiBGyBFHuV05wowv-aiETBDRfYDZJZxk19JjzSETFtMux8_VNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نیکی‌نیکول:
یامال‌ التماس‌‌میکرد باهام باشه‌هفته ای ۲۰ هزار دلار بهم‌میدادکه باهام باشه‌. یه بار بهو ۲۵ هزار تا دادگفت‌نیکو ویلیامز منتظره برو باهاش وان نایت بزن که من‌قبول نکردم.میخوام‌از یامال شکایت کنم و به زودی اطلاعات بیشتری ازش افشا میکنم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.2K · <a href="https://t.me/persiana_Soccer/26719" target="_blank">📅 22:22 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26718">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PvLc5GlcgHr0g6DB4m91s5LtFSk_NLvwwGXvnCspB2sZp56Q8NXEaLos-kL_aQ3CmpphXnuxDiK1aidb59EJEE85tNqFLX35LA83cx6KdQRLi80G6J4Q6APNcNtze4bIVSjfbnI-EpitY40qYZbuLYEwUarc0VT4DlxFzZJj5MROLNZ29JNiw9VHgcmgkv8vhFi8zWe5VJyjx8NLLMIO_zDdkdLyK7NVQf2MKyaQ_Emt9dXbGiDnz7GMw-AG6P3pzDY6nvZui8IJbhWmyqtyjBNMaxubA3xR_VjWHnQE5feEG_uBIcVbDWRzo0oDCXpII51UWB6SNy-D1ejGMt_8Ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dbedc9e3b3.mp4?token=PvLc5GlcgHr0g6DB4m91s5LtFSk_NLvwwGXvnCspB2sZp56Q8NXEaLos-kL_aQ3CmpphXnuxDiK1aidb59EJEE85tNqFLX35LA83cx6KdQRLi80G6J4Q6APNcNtze4bIVSjfbnI-EpitY40qYZbuLYEwUarc0VT4DlxFzZJj5MROLNZ29JNiw9VHgcmgkv8vhFi8zWe5VJyjx8NLLMIO_zDdkdLyK7NVQf2MKyaQ_Emt9dXbGiDnz7GMw-AG6P3pzDY6nvZui8IJbhWmyqtyjBNMaxubA3xR_VjWHnQE5feEG_uBIcVbDWRzo0oDCXpII51UWB6SNy-D1ejGMt_8Ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
رونمایی باشگاه نساجی مازندران از دانیال ایری و کسری طاهری به منزله ماندن این دو بازیکن در این تیم در فصل‌جدید رقابت‌ها نیست تا روز پایانی نقل و انتقالات هر باشگاهی مبلغ رضایت نامه رو واریز کند این دو رو جذب خواهد کرد. اولویت اصلی نساجی با پرسپولیس بخاطرمذاکرات‌فشرده‌ای…</div>
<div class="tg-footer">👁️ 70K · <a href="https://t.me/persiana_Soccer/26718" target="_blank">📅 22:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26717">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH2BlSC_zwHCulSLjnErVeJ0y7wHiS0jG0fdVWILp8VhnpiC3g0G_BYqBZn_4KdMhOuqwFASWv8VGKyAh7fW3IoNmNwq3B-MBq101-1J4ri78rpZfwMfRgkJmqua2esuMHlT_HOMlZoxx_khtaxEhuV0_TIrUE8qOQlRVWxFbjh5jIDM-ju3ZPO04s3WkeEfa4cMgrxUj7yzktCaHfBJ737FlqSjPIfvNzsdgW78WahWvWFy35YcLlD6m2WrbaHo0be0AL5pjPUhH4OVQ5Td3rbRJwQLRw_96Z9rnvd-5xyv8qDlCZDA1vrQ3fWAXKCjDIRVYbe-3IgS7ONfo80l0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه اوضاع کشور آروم باشه دیدارهای هفته اول لیگ برتر روزهای 23 و 24 مرداد برگزار میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.1K · <a href="https://t.me/persiana_Soccer/26717" target="_blank">📅 21:48 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26716">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiE7p7UfaK8-M2lBtL5073uamZYAzEfaQfbn-D7QNi7M_ouB7YvZzJQ4Exx-M1quJsvVvvNeJiJ8nU40HL7_5Clnv6H2xFQ6zhKNSUm1Mb8zS2uM_7bNw9IIlisc_hjPesk9vv-Fs69KkW5_zdZuW33rOIDBgKncTe6I6dwQ-bz7TKzaMUR-2HgYEfDN5CWvV341XRWfmRt8wiNkpDvJesEqhmIc0aiJ3R6Xri0u79RN60V9QgIEo9TBl5vDd90L_OF4TDao8N1XS_b3YIZeXOPBn8OnJokPb7w_l8VOQ-somCHdLBI0SqNgLwKkT4OCKel60qohMH8FeQfdwvuxUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باشگاه نساجی مازندران با انتشار این ویدیو از کسری طاهری از خرید جدید رسما رونمایی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.8K · <a href="https://t.me/persiana_Soccer/26716" target="_blank">📅 21:27 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26715">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PU21addntDmmC7vsoYLtSt90GbZLnaWh9nkSNWG9MbKMLBiBJ3ifi377tEem3oaLWKWMxz_lROuECOGMo3tyOG3-RhbkAaPjh6GNl_k-zcik-AjvdkG9Ev4gu2Z4Z0oVGeEU2sO7t3nb5eTu-T6cW2wDWoGbr6eA5PPPs0X2iIvSzK0Wec2Yv-Ihle91o0SmKp-8icJKQJtrEVbiCkrjlmapKaFKfzMdGrlEQjYtjuMqMi5yrj8ikHVjC9d_doHb5j-uTs_AiIOSLg9kugI3ePeWLVAtE20KkQwWvBlSdaNdUSeVOQc-WcVDXayI2HnxzCLeU71OtBjsdOHa4-RQDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
🟡
👤
#تکمیلی؛ امید عالیشاه کاپیتان سابق و با تجربه پرسپولیس ازطریق‌مدیر برنامه‌های به مدیریت سپاهان اعلام کرده 72 ساعت فرصت بدهند تا پاسخ نهایی‌خودرا به آفرطلایی‌پوشان بدهد. عالیشاه‌ امروز هم با مدیریت فولاد خوزستان جلسه داره درصورتی که‌پیشنهادمالی بهتری‌نسبت…</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/26715" target="_blank">📅 21:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26714">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Yr1YMIG3DX5-_y7_3bbJm4dyEE8o_0_HgPjqurYvA8WwlPIuoEGlKAgClQIlND9jo6xqFKExbwkve43NV6hPy_WCSjwsuaul2mMck_E1S59ch8olFp_IdRtV5SKCRDcUN-k-3DtxS1C3o7MlgiJ8V9ltnyT62CBpMuX5fkzjQm2_rpBYdOYvHrO9EFCehUgpzQSp7BhtztQGZZC-6DMWkEjJgsSMXo8ko6JKgZJbxoyApskN-RjLXE51xl9vfqzQhuU7_85IZibss-3bizrbI2yyrFpV09g7rqhQPXv_lool--cFacfW94t4QZIQYDgtMkXHz2mA-NbjNn1gijYaGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c8d48ffad.mp4?token=Yr1YMIG3DX5-_y7_3bbJm4dyEE8o_0_HgPjqurYvA8WwlPIuoEGlKAgClQIlND9jo6xqFKExbwkve43NV6hPy_WCSjwsuaul2mMck_E1S59ch8olFp_IdRtV5SKCRDcUN-k-3DtxS1C3o7MlgiJ8V9ltnyT62CBpMuX5fkzjQm2_rpBYdOYvHrO9EFCehUgpzQSp7BhtztQGZZC-6DMWkEjJgsSMXo8ko6JKgZJbxoyApskN-RjLXE51xl9vfqzQhuU7_85IZibss-3bizrbI2yyrFpV09g7rqhQPXv_lool--cFacfW94t4QZIQYDgtMkXHz2mA-NbjNn1gijYaGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
#تکمیلی؛ شوک‌شبانه باشگاه نساجی به باشگاه پرسپولیس؛ طاهری ناگهانی بازیکن نساجی شد.
‼️
درحالی که روز گذشته باشگاه پرسپولیس برای پرداخت رقم‌رضایت‌نامه کسری‌طاهری به ارزش 700 هزار دلار به توافق‌کامل رسیده بود شهاب زندی مدیر عامل جوان‌نساجی امروز صبح به مدیریت…</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26714" target="_blank">📅 21:02 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26713">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=r9orvM0HoTtsjnjuBI2NeHdFwsDdCp1nrrtkltcDO-k10h5qS9tminDotOLeHly9Z0VdICjyJj21vFeTDZ3jkZ1ra_kFanPZlRxPrUgt6GuYaF3RLtd8why--FgHXEqqVViEu81AnD8qgRWfq8vM0QFEQbuNojd-qlyU1L_AsknF-DV48K19oIU1vWOSUOp_VQIcbscuYL_5rEn_mxzjCauqDCav62QIz2HJNkdvN-GtEzk7dEynwYCHkGI1jW7Aa4kEj5cI93qO5WDnbWOcKkhvCEM-5AwdGW-h--f2F67iqIHVTOa80xvopjoBTcP04WyQz4xzgyHfXi6si83lNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3548b140.mp4?token=r9orvM0HoTtsjnjuBI2NeHdFwsDdCp1nrrtkltcDO-k10h5qS9tminDotOLeHly9Z0VdICjyJj21vFeTDZ3jkZ1ra_kFanPZlRxPrUgt6GuYaF3RLtd8why--FgHXEqqVViEu81AnD8qgRWfq8vM0QFEQbuNojd-qlyU1L_AsknF-DV48K19oIU1vWOSUOp_VQIcbscuYL_5rEn_mxzjCauqDCav62QIz2HJNkdvN-GtEzk7dEynwYCHkGI1jW7Aa4kEj5cI93qO5WDnbWOcKkhvCEM-5AwdGW-h--f2F67iqIHVTOa80xvopjoBTcP04WyQz4xzgyHfXi6si83lNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
پست‌جالب‌مجتبی و مصطفی بلاحبشی بازیگران نقش‌رحمان‌ورحیم‌پایتخت درصفحه اینساگرام‌شون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26713" target="_blank">📅 21:00 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26712">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkw4NR6GaCggPYzFU3vYspRPrUAx3bjIntFozb-pipQJ85Gy9bU21o_NIzSXYPdI8YexLn6M8C2pA-Y0Z0fRZKxdrptquz99cJxpUuRpKj81b2Kdoq-DS74XWvJqEz1vjR6y2Lz7mBQrJkfQ1Z7ncIP4E230WMbEshSHLRkNFIJdRftWJIsAW-ZehTddNDIIdm7QcHd_jBx52CLbqW5W1E08RMRoWU_0bQBZUock94Z5w1wdYAH_x7wIs4T6p7AS3IwV6G3V-kWbGDIrwVejNFnhEzKUjIiNWh_1pbdVbRx27mXA5C-Lap6ExggBzsgEVlVAV6st2k8xr4f1GIpktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
اسکای اسپورت: وینیسیوس جونیور این تابستون در تیم رئال مادرید میمونه و قرار نیست که جایی بره. رئال مادرید به تمدید با بازیکن خوشبینه و هر دو طرف خواهان رسیدن به توافق نهایی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/persiana_Soccer/26712" target="_blank">📅 20:42 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26711">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BINouE785OSn1f9FfqCpezMJXSpiBmNNtVp4qgjbphB1YgyEMR4dmqQ6i4M7WoEor5EAAwkysYRwYFPSeCHWV4U0lqXKVv1SStyKeVZF9W5Is18V7uUHxOlsWAx9uJm7W8Su7RFiQ3ZfEXXssaiyzdWPIbTq542HAD0Z27GhO2KrXEPfrJm3tWLNxP-axILivYKt8HEdugH7r8g_95L2BwzsnELyaQlYVLY9l01nkGH-raK4ZaG9soo79xtKTEvqa04mExrSe5ZjfAcsCMq5J9qyiz2qtYErqn1CMW4Nd4zBL9tkABAKI5OC5VuVV17pM4h-ALdZFyx973Er-gX7_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔴
👤
طبق‌اخباردریافتی‌رسانه‌پرشیانا؛ باشگاه تراکتور رقم‌رضایت‌نامه‌صادق‌محرمی مدافع‌راست30 ساله این‌تیم روبرای رفتن به پرسپولیس 100 میلیارد اعلام کرده و از طریق مدیر برنامه های محرمی این موضوع رو به مدیریت سرخ ها اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.2K · <a href="https://t.me/persiana_Soccer/26711" target="_blank">📅 20:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26710">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=K6d7ydBZQGg5Eev_GR-4gSNbgeNnqM2161ekxhNY-hxMDPJLWOHZdYPM8cOEeMA-NA4_roiQtxdlirWr5HxQaTWk4ZSXP5IFuU_s6Xr12IyFa1wVNr6zQIKDgIz0DY2ctBCaMuVeGlc5YvvUYJYXCamP3B4GcMO7LT5iiak9TNNTfR4tKxcVtlkrCJrbsKjvWsX4SEyM__QSotz1bAAB6DuQ3uDJS6auhQZvWZL9YLofG0rMxJ1_UdjtnslHLR0Tofoh3AEJ4dBi-Dx69SJ8CLPms5nYcsRupAhbuNu_jcXjgeSq5VbLi00FVrwjy4jhmfJe0c5GxywTOekySOmdMw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24d9dfad66.mp4?token=K6d7ydBZQGg5Eev_GR-4gSNbgeNnqM2161ekxhNY-hxMDPJLWOHZdYPM8cOEeMA-NA4_roiQtxdlirWr5HxQaTWk4ZSXP5IFuU_s6Xr12IyFa1wVNr6zQIKDgIz0DY2ctBCaMuVeGlc5YvvUYJYXCamP3B4GcMO7LT5iiak9TNNTfR4tKxcVtlkrCJrbsKjvWsX4SEyM__QSotz1bAAB6DuQ3uDJS6auhQZvWZL9YLofG0rMxJ1_UdjtnslHLR0Tofoh3AEJ4dBi-Dx69SJ8CLPms5nYcsRupAhbuNu_jcXjgeSq5VbLi00FVrwjy4jhmfJe0c5GxywTOekySOmdMw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق پیگیری‌های پرشیانا؛ بانک شهر هیچ مبلغی به حساب باشگاه‌نساجی‌مازندران تا این لحظه که این خبر رو اعلام میکنیم واریز نکرده و باشگاه نساجی و مدیرعاملش فشرده در حال مذاکرات نهایی با باشگاه استقلال تهران هستند. علی تاجرنیا و هلدینگ اماده پرداخت پول رضایت نامه…</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/persiana_Soccer/26710" target="_blank">📅 19:49 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26709">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ve5e2Bxzj_PxPNn_26_r1qSLUahL8oSgsFRB3NjmgTzEXYQ4Q8eTA6-GWjEMDap-ATIIeTTncIzNP9YFCUpE6ZQZpYLIgnh3VJsVizcw5o-So3Kc4n6JcHvFK9QKzkyHoFc1xcvD7LnZ8ZOP5VcmbY_oPNVeozGBcx_zjvrazsoFYvI7FyF4MjYU6jgaq-77IDNcvWZ5WqJj2I4V6IFBT9nb8gNSaiKsCIhVKLvTm71I3T6GBKSYFrdhb6taJ8ANlnjGTyFJSJwJA_sEHfa5697_LCdpKIlUTf_2PtkiVzdAd8sra4eTpicX5a6grQ5Gk8B-Q2efDTvpFkE5Fv38lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26709" target="_blank">📅 19:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26708">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXU6Tcfr-iUIkF5WveDyPH3Jhvfs_PmIB2S0pXEuo9U0vKMQ7fljnUx_pz2MIIvDoca4vOx1Y3xlG1Hi5jlHoDhkPYjEnqaDSAs7_N5kOo5bxNl-BxnX8Ol6rfhu6ngeaNkgfGkRZUQ0RjPBvQ9JIb8XtBXpVPqBs2xxPU6RGELlj_57tthfXOO3fOHSYkNjhBPIxu8z6uxE72aEwFYly4lLP8xoGW-BB5h7sIMOLyYS4797-32C2s6gQK0DyIaq8y3ktFV3e3RJDWgchg6DmrH4ZGmO-azgj6JKxZwIuqDv7g8eUMX_wgCcG3Vqyfkcp3NSkGy-6qFVfrcz3IeZ1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
با اعلام سازمان لیگ؛ لیگ برتر رسما از روز سه شنبه 23 مردادماه آغاز خواهدشد و روز 2 مرداد نیز قرعه کشی این رقابت‌ها انجام خواهد شد. البته همه اینا منوط به آروم بودن وضعیت کشوره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 68K · <a href="https://t.me/persiana_Soccer/26708" target="_blank">📅 19:07 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26707">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGxN8GgOzbTxRO_NzNO_icq7yBSDf7pFfCXjOzM4_BYs3UnpHBP7B9wq79-oM4BKQ3uqGtUW1kR7MJx7QEIqsNhRyW0vGG0HbBYvCmh42BWOBzxo-Djuh7sc4ZkfmWkVd-pNTFdOy8Vwcezw0tGbewwhMHjk5GY8vAZCMShQNQoTkF9JJxVueAz1P2jLfHYWUAnaC8Q8UYa42q79eDXhSphszpBKuGYDsZd02pErQp1q-j00W8Mps7zBQjnhFbZs3Y8Hoc8RjDPS8vUrJAVLCGpSmdkZ86u20n0hwYNzRi32-jQWnxyl7hht8CSmZFkhpQFFxWf4rapfQUy7yjOEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛ بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/persiana_Soccer/26707" target="_blank">📅 18:39 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26706">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=W-7iObjeDjNOfbARYLNkG3RJvJPaEmSVMErqS52fqDjsJpYuwtwPibHgK1CInEqdFf0_b87AAF6MeLbqbCXdI3r5kZDlc8nGdZXUodYprJbKdtdsqB8YmyMjy0tfrdseSurDMqAQh6B9ZQmy-ROVkewJHyYBXndAb1wx30xsDnBZTS89x-S_iq13FdYA_wavr19NA7FG0zXW7dkrpPLZqb8sJ-vIaEOzX_1O0d3bbpUmEDX0T6Q4V7nmxEZ-Z-lHfE9wDGbb5pdknRZn1v7vp6lUuPurJN_GbQvC6FHEmzuM1xab5NffEUzguXUwQHNvlO0SHguyIB-hGo1fLbgLcI0KL60ywcyjXOBhjgEVkIblKPAjWYkZoEPr2pzYlUK5Sic30UqrrH9-kQg55x_Qej0lFkyRMqd3TGkcWB-bxf5mYh6kcghBJ3pwLVeHCYSc5KGUGtLl5WsyxYKhyximzPMX_3KFnNPKUSsJrWskF-iygvyRXOtXk9uWDtd0v2nQ-maITfODMbRJMoWMaZHXyox2mRqYK9BeC0I37vCX6OGVoCowTfWRv_up5W7c98jaEDVOdu5mvx5a_V3JW7NvZcXlBMUxJ6ExlLMy0zFvJ6qLI2horbiYh4XkNZ2zkxSRHyYR53ZIj0CxBVPcVZocJJIC3BqeUFxiRSVbSlZwIbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c3c711337.mp4?token=W-7iObjeDjNOfbARYLNkG3RJvJPaEmSVMErqS52fqDjsJpYuwtwPibHgK1CInEqdFf0_b87AAF6MeLbqbCXdI3r5kZDlc8nGdZXUodYprJbKdtdsqB8YmyMjy0tfrdseSurDMqAQh6B9ZQmy-ROVkewJHyYBXndAb1wx30xsDnBZTS89x-S_iq13FdYA_wavr19NA7FG0zXW7dkrpPLZqb8sJ-vIaEOzX_1O0d3bbpUmEDX0T6Q4V7nmxEZ-Z-lHfE9wDGbb5pdknRZn1v7vp6lUuPurJN_GbQvC6FHEmzuM1xab5NffEUzguXUwQHNvlO0SHguyIB-hGo1fLbgLcI0KL60ywcyjXOBhjgEVkIblKPAjWYkZoEPr2pzYlUK5Sic30UqrrH9-kQg55x_Qej0lFkyRMqd3TGkcWB-bxf5mYh6kcghBJ3pwLVeHCYSc5KGUGtLl5WsyxYKhyximzPMX_3KFnNPKUSsJrWskF-iygvyRXOtXk9uWDtd0v2nQ-maITfODMbRJMoWMaZHXyox2mRqYK9BeC0I37vCX6OGVoCowTfWRv_up5W7c98jaEDVOdu5mvx5a_V3JW7NvZcXlBMUxJ6ExlLMy0zFvJ6qLI2horbiYh4XkNZ2zkxSRHyYR53ZIj0CxBVPcVZocJJIC3BqeUFxiRSVbSlZwIbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آنتونی‌ جاشوآ بوکسور سرشناس‌ بریتانیایی و قهرمان سابق سنگین‌وزن بوکس جهان، در مسابقه چند شب پیش خود برابر کریستین پرنگا، با آهنگ مشهور «نقاب» از سیاوش قمیشی وارد سالن شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26706" target="_blank">📅 18:35 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26705">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NDQBLtDLNpTc8EfuSq1LMLRow_LWf7PYI8AMVNL84OXPo9fNQFHfbL0VIVbzR-v2IFqfbN2HBLI1n98h8icEuma7CauRxIxM8XPgZrxyGn8kOfWgOWc-F1dg-hs9Ce-efVRqTymcIcyC-1TjSI458yZsu5HynZHOC1HlIlRBi4DQbqTTvCAOhefZFOMHlh4uPOqjhBcvl3G1dGGvvTZr79hft--XaeqrWlDsL2f0CHu638VBjS939wgc00XmRwRDqNm0uKVhWQq8XyUyu63lYZK2NxjW8SLKZi8h8mvSMcVQRe-Ih1gf7V5pN8sUERcZdAqqU2QVY3BKP4Fu1zrEUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی سه روز پیش پرشیانا
🔴
محمدمهدی محبی وینگرراست سابق سپاهان با عقد قراردادی 3 ساله رسما به پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/persiana_Soccer/26705" target="_blank">📅 18:01 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26704">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">برنامه کامل فصل جدید لیگ برتر.pdf</div>
  <div class="tg-doc-extra">34.2 KB</div>
</div>
<a href="https://t.me/persiana_Soccer/26704" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔹
این هم فایل برنامه کامل فصل جدید لیگ برتر؛ ذخیره کنید و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26704" target="_blank">📅 17:54 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26703">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtPCVanOj1PHfaZaH66xuf8YMERVQOR2kmvDhBdoUogsYvrA0X8PdQy2G1dohIWbtF1lu7BrrJDJ3-5SDWNWummAIRz4jXiAAk-3w6T9kPx0ToMXOp3qN0eqql3-hhNYR_9D38W-tYw7IAJYhgvshptJ8mRmfJyqZehoRfV7qYGwFBxYrCVqxfuT1l3n_fU8uTS5guJVUocGSeiCnQ0xmPQqsvCUJQpPFi9mc4E57kqHL_F6vqCNw9pQxQ0EESC8KSqN3y_tdTZLRlfHEjrUi30PpsxXW8ZZNvgU9_kPkJKn9Eh7N7NaFAR2XXvKCSnifBe10_d0gyhD7VOJ3NoZrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه دوئل‌های جذاب 4 تیم مدعی لیگ‌ برتر
🗓
هفته دوم:
سپاهان اصفهان
🆚
تراکتور تبریز
🗓
هفته‌سوم:
استقلال تهران
🆚
سپاهان اصفهان
🗓
هفته‌سوم:
تراکتور تبریز
🆚
پرسپولیس تهران
🗓
هفته پنجم:
استقلال
🆚
پرسپولیس؛ شهرآورد
🗓
هفته هشتم:
تراکتور تبریز
🆚
استقلال تهران
🗓
هفته‌پانزدهم:
پرسپولیس
🆚
سپاهان اصفهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/persiana_Soccer/26703" target="_blank">📅 17:51 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26698">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ILDz197irizA6QDL3XmGYjdVLPU5Vriw7UoWM58vbsTscaEj97aTI5cSiQNn_xPOQ5HBQLx0G6XAbaKzXpcRvYC6YV1A5253MHLWe6W-s9wDjjEAXWiEFRHAQNyYdB4RreHs4MX4o1pPc6JAl7eeUZ1qPvrU8K-_0U5Wu2_-kkJPWTJy1M4_RM8z2KxFc0GUs79n-WbEQQfvGikSX67NkThB8UxF52F6g5Uz0aqrSBDEAm5bopUC7cCxo4MOeXbkWzdtnWU1x9Pc_N9wpoYsE11udCLPICxXYUvKiUyJ7mNe8xQKMtqIs47BqR9Lv34ffIiOaTJC4953O3Ha4-WPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/i5Tsh37sl2T8k07pGE1vQBKTDM8FNjLC52V79VsaJE8h1hnmcEqrfWeBlJcKGvkgWXQ7FcEfvj_Xc38rB9FDK0FZUAzAO1F68RoiS-IenzCAQb6ldMUVJ-lRjXidM6BU4DoxuXAyqNA2bpXdZABQXKNFQSNN5U9mEueRl9sPsi4exxyEcO4VWSfgv5Xtk0imvtosor68bE709UCKl6xuqeRV3NbG38LnOmoN-gdszhULatYJbHYgjO1aOXa4Xq06I8dQUlMWMluGwJFkZAS6XKEnTEFseVYTtuyxjy2O57PIsEzuwHa06NOejnXM91q-0yVRGJvbULl1mUtKJnXOUA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65K · <a href="https://t.me/persiana_Soccer/26698" target="_blank">📅 17:29 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26697">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kFfmZXb_xiSt3pHECUEMGxWqZkodrheSvKv8NFOc9efyA7STOfL9IBQXyMlyjZ_LYFkrzMUX-IybNojvdleKJC6rgGUjl80P0ofnqVRyZj83nTwXF39y_tLKSluEahn7_xF2J3D5ZCkyMhGKKlbu3xUh6sWQBwQn4UZ-hC15v5ym5VlIfZClTx766CtLEj8KY9_Vsy1ChQuhzPl_G4v3TFy9lZpPjNjEuXYBr4mP8k84uqqHbJ39WtS1Hk8QvIKQpLB3_j81lcTqEESALMhZgdZB3Wvew9PI_YJlokc95f75AUshTrGcpEfe3f3jPre9_MxSwhOtLwAULfGklUgU1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26697" target="_blank">📅 17:24 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26696">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vl5PhJYiIaY9Rv5LxvpGbqZKVB-MgCsQdEOLGPYioiKq4U7Y736PQ1rvJyPzaPMiTNOzkQCeN8TqEwyCTndwtHMHUG57mN08GPGBus3EgeBS5iYcMeycQBM17tcwOrOqNH3yXz47om-8Gb4ScTLFXWRrgqE28ZyvYrnz4U_OOvVXpXW-l0LgU-6uxke9Uq5AiCbryy52QhrGlSOuwXlUAUYamnyI4FKrV15PbpFk0jrvB0o2U8eRM-RqNQ2p5WNAsJNN7NItDFB3rK31-wCIkeEflNh9Kc8kBMzBpSKkpi8vV0ZTkua7roDSDCKm4pGHllIIUjzXJIUh7Ah6E9XXYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ بعد از عدم موافقت باشگاه تراکتور با پرداخت مبلغ رضایت نامه سنگین‌محمدمهدی محبی؛ مدیران باشگاه پرسپولیس ازشب‌گذشته بامدیربرنامه‌های محبی تماس گرفته‌اند و پشنهاد مالی خود را برای 3 فصل حضور در باشگاه پرسپولیس داده اند. مدیر عامل باشگاه…</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/26696" target="_blank">📅 17:20 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26695">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-Igwk29X43oF1HRiWU9H66PhGGwwUbn9dDaalzTCkP9miyBrl0TakXcB_DvOTUJRhYmV-vZGsozIn78RpTIBuTBbO8YpSUePznteBjUSilwOhvp3N85uymhdx-BYTOit3hBOK8fht2CGBhNTXRY6KyJd197z3SqkW9g7ovIKRXVMf8-SSWY-PDrAaJL0WhzooFQzKQN-KsQoSP8pGUaqSdREtEVzIiulup6SKKj-8nEm1hSDO5s1gAlyADmJgydxpVAlGZRWdSBH1BWWeg139L_c2PY32Q7BuVsm1qpsBdcaXH5rzL7t8UYG8XhtYiHIhJwwlYTHro2pq7jAqKE4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
برنامه کامل فصل جدید رقابتای لیگ برتر خلیج فارس؛ هر هفده هفته مسابقات تو ویدیو هست. یه جایی سیو کنید و برای رفقای فوتبالیتونم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26695" target="_blank">📅 17:17 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26694">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31211ab420.mp4?token=KX3kmVcyqB4_hfLmcfjM2DA9kWDNtJ0B9R1j3CN4uXEJmG3ADmGhIUVkkJlEFKraG73UXcBmpWShCg2GjQ12KONt7GMqd7Xkx367Ojyknhi4GRMTS4ms_RgIcYM3gUKN-949SmrqOzlKepu3Y8Q51plD9mRt8DQZNMVxRH4ojvlEsCnsyxNUfI7P5-OjYBbx56p83wg-iYlQnLp4ObESTTLnbh2GrFLJqYU7e6nWYOpbu5PZzPA8FEL9BUKgkoyb0km2xmvQxJFD_7Wb7oHDae7steO6_N1Ri__PGZZBdvOmC6NmwnCNCcaIRwIaAbZK7lpmdasFe5yETyA2vfFEoQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31211ab420.mp4?token=KX3kmVcyqB4_hfLmcfjM2DA9kWDNtJ0B9R1j3CN4uXEJmG3ADmGhIUVkkJlEFKraG73UXcBmpWShCg2GjQ12KONt7GMqd7Xkx367Ojyknhi4GRMTS4ms_RgIcYM3gUKN-949SmrqOzlKepu3Y8Q51plD9mRt8DQZNMVxRH4ojvlEsCnsyxNUfI7P5-OjYBbx56p83wg-iYlQnLp4ObESTTLnbh2GrFLJqYU7e6nWYOpbu5PZzPA8FEL9BUKgkoyb0km2xmvQxJFD_7Wb7oHDae7steO6_N1Ri__PGZZBdvOmC6NmwnCNCcaIRwIaAbZK7lpmdasFe5yETyA2vfFEoQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🔵
مسابقه بین دوتیم استقلال
🆚
پرسپولیس در هفته پنجم رقابت‌های لیگ برتر برگزار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26694" target="_blank">📅 17:05 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
