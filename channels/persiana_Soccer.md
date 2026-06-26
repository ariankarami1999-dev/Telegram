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
<img src="https://cdn4.telesco.pe/file/BTzqOyjUJdCc5XdnxlQ7zqFf2zaoV5tgStPezha8ou2xCAp3s5f4hss6muFsAW9u5yfdr0mBp-JJQLdFvIOIGviOzHT5W8CvNnM7TpRufMPJxgb8KSLvb13QB9xt8GjNKHc4wj3WVVX8V6OBfA37juzjG9iHyxDfRdGyQT-LU87GrMi1CxR5RIyd9J4Uy1nnUmkxEJ1cE2h7mP_5zzug5hiw67Va5v8mHTv9prEOeOCoQr84_y3Bh382olVZkmacHllkJ4DCDTlnKgqAB2tBLjbjZ5o-rLe7Ajfggbj5OO6N3F6UxyHVRfAVfOTGTgo0yzc9aMIwqpw4kPqahcVKeA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 20:43:45</div>
<hr>

<div class="tg-post" id="msg-24395">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uan5GjPljwxSWYxX0BY2zGElv1zsf5YEhCN5SGwSlNcwAOj8AQHCkv8wz20Gx5NiQsVsshdj48HQfpeSaiN1UuOfNZsUALo5QRNPAVAl_rNcao5vF5yekR0wS98PRtlsfOTH_dEi__4kKbemB3xomjLVH-e8z3Na8kWHgy_EFJBVzp0EBeVCS-iUOFsVRtV6liRgYG5oCKb0xHx6jmJy2nfMzrIQNyXolS_qlpkCJdIkIPbjylYYVAJVEN84iutWBVOHkh9_aXJ2wwit6SF40VVxTMs18FHkgguJYG5Gf3y6xvXGmlKIFRBQBafe5jTu0XIlzWmQbD2gTNRpbNvVWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات
|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/persiana_Soccer/24395" target="_blank">📅 20:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24394">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C-RUDcoXnH8pzKil41zqn3N5qvdUdrK2TMZTc0RRlPe37bK_lvSoD8J9_AYj1aBvuR7Wrw6vI6vjcQO6kR2CirdrzaUh1O94xr6hFsDjc__KmmRv9riHWX6YB1uzBpAKg6k8P99Xy_VPuXJqdBH26JKhNq-QbRs5nWqewsv_BzFjZShaD9g6b0G5EPoS4q03jVmYaJiu31UjgyL_jl1yJxbCpUf5eiMQdKDUP4VSl3cBpAtLcY4gAAWynYX7Bre2lWH5hh1X__ZvizAhZZKEbHniFSbm2hllrNQu9857LkD4h9294gA-V5jBd0lWhP5TOWSrbF3EZp4jkXWZOtYfdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس باارسال‌ایمیلی به باشگاه ملوان انزالی خواستار جذب فرهان حعفری هافبک تهاجمی 20 ساله این تیم شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/persiana_Soccer/24394" target="_blank">📅 20:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24392">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YOdKetYj2uDmGoh9sdtsRHIH9vupsCyipiLmmmpzKv1qESVUdnwnv5WLK-ji248mtb3WZoiHUI5rUNP3cnC8hVpIo8OJhRxa0gJneq7gBUlogRnPzoC2ypXKDiGGkcBmSqyPdwHYU0T4cHVodRocA2-cqI1q_Y2OadlC6Zy2nj5GyWd3Pv2odN3rA-NdRu7NDTWfnzNJJX_KuDzzNor7OWYCK615-8SJWPt7sARXCEEYy4TUaQ5mN6vGwiGiDXCcG3_KIdfeyp2tI1sKO6BWgecQmUEDj1svQ_FwFG0A1UgXYxtlTJGkCNiQdKtcaUwN5GAzpR9d1MEVWDGgJmFVTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I2wV3ULVbhYfJ0bBYM-jK_DoxO5dc-NwBnEEky_YNzNacZMjGQkODF8I5ubkIp1wUd4g407I5ouZcYazemhXe9dqfQ9trwRulZzCBj4ePUWh-Q3IjAUBYXQf-bgYlFBD5fd4SslOTBrvHcbaVGo3Vsrqw4hdzZXJLoW3fFTnIwOOo5oXi2STAV4XoDUjqQLR5nV-pWJ8d6erFvyNkeg0fia2MNJPINl-J9mTnoRcmuKN9L2l6Ux8nsYwCe6QnYgD0EpYS5_v8oLYniAmByCQDiYdGCVw5hL8Caky9IsqhF-97XPzXDG0iu_KV3htRI1uCITbR3v09F6-m061zkPEnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ناتالیا شادل مدل استرالیایی دوس‌دختر کنان ییلدیز بازیکن یوونتوس. این دو حدود سال ۲۰۲۵ با هم آشنا شدن و رابطه‌شون رو خیلی خصوصی و دور از رسانه نگه داشتند. ناتالیا مدل قدبلند با حدود ۱۸۲ سانتی‌متر هستش و قبلاً شایعه‌هایی درباره رابطه‌هاش با زنان وجود داشته‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/persiana_Soccer/24392" target="_blank">📅 20:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24391">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/co2FPdErwdQZ7v8eF7v13oyjGrxq_JWINsII2X3YoRMIucQOsiAlIm5VsnRQ-cL5kZqVFLXQb-5jKNCRbmpvM0uEGf0lZdsM-AFtL__XEeGj3MgH4-GesS65ubKGFzsOX0F9yojXohXYTYEP4U7uigRTBY8S5f0vaXZvnWJz3XIY8_qpflJAwOdlPuGWACwBYBOgOz7JaBvee0M9L_lEiMEbYdpihghm_wjIPj5x1nfh14RcmmSC71E9wkiDBeO2VZXJzfMv-0mE3Ol7t61edzbXvcDZbt0PIVmcdOTIG5-exNc0dsEQwGgay2iF1v161zDvnZXL7NPE4QidK-IWog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/persiana_Soccer/24391" target="_blank">📅 19:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24390">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pI57yRFHscgzso6SFLAZRfPWox73FwUaETer9I3Zgco9XIBgpJgQMddy-ionHP90p5j6Cg3v-gHrUOUKKobLyDaCOUCml-9L0U_hoQb9NX63HpxoLHZel7_3L1DU0LGkxfN4ym07iqc8Rugb729KspgcubPxAUxfgSjzCGjucBFb_AfM8lJXjcZ8uKfjzGWYu6jkAgi485u4yb6FL9uure7Z5wF9GhjP73VnSBbF05ND7M_6d5UZ9fioq0gRfYe2u-VuafNIqQQtoiV-yrFUC5oePMHGfqJIDdpgMhzV-7eoCsjFLDehpIkAUOzGY32LeazilsPCHw47_ONDE11juQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
تورنمتت آسیایی؛ لیست بازیکنان کامل دو تیم چادر ملو اردکان
🆚
پرسپولیس برای دیدار امشب.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/persiana_Soccer/24390" target="_blank">📅 19:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24389">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBsxD5Zz9oGlQISOztox5woh2J2dD9xzUF5wQIaTVUXsI2FCaXApDqZbCNf5NcddPm8L-5cLUOj81Kovy21VbIW6uXbbivTK5eDOByphAiMUl5QjbmYaOV0J_0vR9I-NZmcqrIw-pSGYpwtA9OKs1vmrlAtdc1wnagpQqPiwWk9D1RXDRsoJ0MzkxzUlHcqFmtcRx5FfcNvAcJmHG51Z3ha2WPVHuI_Rdxayle8b6p78j00pPB5YyUifVTEMbgq3blkHwo0Z3W9IJ03GpxCVGH59R1-GByMRoqjvgBXgscnyP1-OW8cZjJ6Dy0HkKaGDChvvRa4_5rucul55pZb5qg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24389" target="_blank">📅 19:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24388">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bKCBsuGnmP0dQ-UdLHm262vcLbN2TdN9H5sbzW0c_hlclFBi_ajmoHYkdgLuqcnxjrbEIcSprM_sMX3lmIHVJoNTcUzDQo8bb789UGoUW2VyW13RVS6Iiejk4p6JKE34hBG4r6BR6uxlr-U4COG9w3ur285ufbearhakI5w_7_M_CrqwArASrEdAcGcviOuvXmeiT7QrllNzVNyim1Qmm8_piYMdBs2HwrCCFBUVj1DV-7zut2kSuLqJE8066ABA_xBJZ8asR-pNZ9Wvlskh_LFobvYfCOgnKWsMRxRwthkMPxx-4hqtorhrpl7e69q9sFKxU6ARIVmjj8voBo0zRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/persiana_Soccer/24388" target="_blank">📅 19:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24387">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dRdo64N20t61CF90DyZ1y4WXDZs888BCWKKydAoHnrZBx17Ov651Yp7qOtouHtspXX5UM7ag0dm4E7c6u5Yn5j8u2ydgXDZKzbcylKQvcwZ3nzKaK8uNRVwuBZhXOnWZjHpO3ELXV-EU5LgHRFGaI6O3ZtDNWEGxdzjOysY3DGHEUxIncMgI6Q60iC2CEIA4WiFb5YjYT809M2phD6-qqwpmurvhj3gtAqd8DsVNbriq6Afr1oCRD_7HQKUqds6Lm4kg4zX-G4HBUnQYcgruZKhsw_fIVrmvZV4j6AV8TKHgz3AtJ6ytftOu5W1zO03yMlEYFxzvIidMyH9fJZyB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/persiana_Soccer/24387" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24386">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XIBOZhVW1dbedMYmLl33XmrGDCjNvYqnqyD7wrlhDbIAnRAN5_bkEyLSdpSiP_ss6bRxwc9H-7pp554Bwb6KhEWZoxJJCdHFZbCg1xcHnlxbacKJCuATyoZ92f-U363Z2OWJObm_YkTvNJ_BnIR4M6jaoeoWJlLe-YDVySLIyATJMG-ddbljmzeaCFgJiX965vIyZFAibuybcY8NweKOYjkQpYwiwshn3gdhJLJsvgzELsEY5tJoYGAaA-VOWJCRYGCM_V8xbU-VyJS1p9rofVOL354KwneH-pGqTvohPeAC03yrRtkK60cFv1Wu40NeFHjs-Aar7ZXxJ_hVeq0f6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/persiana_Soccer/24386" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24385">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/Iia6EI6fZV6cmQ2ptU1Wx3lfPYZaYOT3ZopJ-9AAF2IKVe4RPluS0OWcuQxhyZvX7rfILl5x1ISeSk-lebO8yO6iQZIKr3XEMlNagdR8jW74IKChOxY9VA9ypGpt2fpkX5qskIb9F0MWUCrD1EhCgT1xP7ml9ACX5KafBpoCulhyAYtjWYpu4GhlZzrCd0xvj4yxj-6mtHAPk23Eei-pWOK4yNF3UL1IBTweX2zAb0ugRGT_5pIlPI4XUiNZOR-qH8f-GicHjqmsn7xhoS0uj3EK7UF4WPFwEKK6jejAo4tb0PfDN1iKzROaubjjSNq7ZUqKopLS7eBQH_tigWFXjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😮
جذابیت‌پیشبینی‌مسابقات‌جام‌جهانی را با بونوس های لنز بت تجربه کن
🔄
☄️
بونوس خوش آمدگویی
🔤
0️⃣
0️⃣
2️⃣
💯
بونوس روزانه ورزشی
🔣
0️⃣
0️⃣
1️⃣
💯
بونوس کازینو
🔤
0️⃣
0️⃣
1️⃣
🔒
کد هدیه چرخش رایگان بعد از اولین واریز
📣
بونوسهای‌باورنکردنی‌لویالتی‌امتیاز وفاداری برای کاربران فعال سایت
💱
کش بک هفتگی
🔤
0️⃣
3️⃣
💳
کارت به کارت آنلاین و تمامی ارزهای دیجیتال
💬
🪙
واریز و برداشت آنی جوایز  5
👛
📱
@
lenzbet_official
🌐
https://www.lenzbet.cloud</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/persiana_Soccer/24385" target="_blank">📅 19:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24384">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stxqfAWEuU4eao3usK4uLriyDfvGdeNzeggeD-NqPb6CIM07uzJEHE0MgF-sFOPqCDG92mVPf9a9MY9pVABXZPjfILcwkMwY6I4rF2jCbN93ES1UxFUIcC3DalpYW2IpwPwbMipNKcyU2LEnKxzaQY5e4KZUVe_0rxIUYi0ig_8HA4ciK0MRwCpfrDBd_LyhDmjuJheBcTiqEBLUH9aKxj6A_WniYsC6_ngzrgbydG1l3bvHiiV4DIFL347tpptr66cqc62EZxbDxSC-rl5rPNcyXBU5ZyuZkhVdHrzo53wQAy4QOlXV1wAdQEPOlPy4zByUy9uP2_TdCi3_heKvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
آخرین وضعیت تیم‌های صعود کننده و حذف‌ شده جام جهانی ۲۰۲۶
؛ تعدادی از تیم‌ها صعود خود بمرحله یک‌سی‌ودوم‌نهایی‌را قطعی کرده‌اند و برخی دیگر از گردونه رقابت‌ها کنار رفته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/24384" target="_blank">📅 18:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24383">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HEQ7fWFlXnEv89sO_tE5uvGgSJqnJiGQKOXImPlI2e4J5eUJRAE6wOB9e0YcE8U-4kW4_0mbqgzRpZ0d63JkE0bkj5YTWmVennzm36O5jB6gZ-EsdZWJpyNUYi1A9IEPSh0sutyWz1__H1bFAYk5VHuQTKUMYjI5bmxpoRnEzG6eIn-v6C9aXLyb3HNKkIwoWXILrwbfDuJHZFZ0C8WebfXDkpUfFYZspui8fXVR-cIDI7P1z2_KiusNrRMzeQJwOWsbfhNxxTxfXPOqxQuUfA3sOztkSq1APJcIxDHeXapSBriUAji0TLQuiRIuBpFZ32WbsK_o40QO13qb_7pQqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران با ژاپن؛ ساعت 18:30 از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24383" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24382">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saNN_UQXyCgS9dsGiBd3wXJcc9TasnrobI51xOw7y828jrmeTIIvVTbTFIn8p_C_ZPSarmJqbJi1ByT9WlQGFjtAImL0-ILDwRNGVpOO5kx43kShusoGgQGkoj5EFwgbPIZwhXjVfVSIs61iGLVIzDr2Bwx9pCFFLuTP3Tq0FzwqhFkdL7cAsTSKBs6W7iqtQk7TjqZn8oJdDms4_ajtLYwTH-iNMyEsJcTS6Iwex9eO-NzLCrImaZik461fkSxitvbqeTMX6UsY4-z4Bl2-VFazC8523bDKiwSoY0bW4D1HVl9TxixbgK3N9v_By46KNBAOmRSmiHVlsru-BezAEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24382" target="_blank">📅 17:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24381">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b5c2TC56R9nHRzkvwjJCL6I84MZWWXQqNM4T732JkDj-8UCOK9g9k5SuakxHwCrEyDnJfpvurF-SaMm6k5fDFpQ9O1Y2RLRj_2dXyTTB7a2gWoSKKFNpeehHaxbIc37cOzx4ZS0IJHL4S4SZCIO33eZ5wZzVecq4dh7p8LMNtpzQtEmrb0aXGc57F4-bhL2EMM38fCOVFbDHNDXvLM7SPs4Qh78AmsTCnyFB0nAQP96HNnNXx8miQx6j_4tt2z4aUlcNK1nLlJlpRyJWtMhBB2pevRcF9BvxB3Vd77yIhkm8WWLiuMBznhbFEQMV_HAbXXioHGc8loz3Fqep_eQ5jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرچم‌حمایت‌ازهمجنسگراهابین‌پرچم‌ایران و مصر قرارگرفت؛ فرداصب قراره ورزشگاه رو از پر از پرچم های رنگین‌کمانی ببینیم. فیفا گفته هرکی از قوانین ما پیروی نکنه بین 250 تا یک میلیون دلار جریمه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/persiana_Soccer/24381" target="_blank">📅 17:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24380">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7htThZXDe5psyKVisSdaaZGuyEDnmt4IqSHcQosd9SZaFI0zrFyeWe3dxjQcFiEml2vBnRYJskjBS6ieOtRwsmYcql947onFdCRsNTTNxffT5aATI2sNGq_8jd3xqcFAmUPJAmD0Bmzsytw5429IeisAVSpIO5Lg-wekwXlGihHOmZpDldO2b5m9BoaLOuCJLHfljkQ-NLKgg6026NuAQOJKEutcymViG8svIsA9E7P6rGgkYK84LS30aeRFqFcN-Ho9Krl_v7R77nGXI8Mc0nx7aVFAkUpvWLCvwUz_8vkItn69FoBHNup0TIMydHicnhWq1CDGljpUGwm11TSAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟣
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت‌ باشگاه‌ پرسپولیس روز گذشته با‌ارسال نامه‌ای رسمی به باشگاه الوحده خواستار جذب مبین دهقان هافبک دفاعی جوان و آینده دار این باشگاه اماراتی شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/persiana_Soccer/24380" target="_blank">📅 16:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24379">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EagfVo9qqlk9DmlMoeeFyG4Cfe5iI7vWFKFtsLB6pFeRDDdUCBJCmaZRITbz6xKvumV6WfISsLlvGSER1Ob-k5ybN2-E3bHFgqJRB1Uvhj8JM5xB_qNTdofUATJhU1d4hEvWSYKRHo8Myjrvm4TPXOqJPwAxMn_OUPrj_Jjqzb3dFc6clYCAW-7ExpKchcOZOC-B4mdRJnpT2Z6v7djz8L-L_yho6JMkMx3CDxsLJnEwnz65d9m4nvD-JGID99UfKPJihl0jhXMyrTZTOv6yO6z75lT2ADxzCt8LBz1S02ety30q-VUwmKwJmeEhPRD_qKXCRB_omW6x6LTAvvg4KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ داکنز نازون مهاجم 31 ساله تیم استقلال دربازی بامداد امروز مقابل تیم ملی مراکش این‌شلیک وحشتناک‌رو روانه دروازه مراکشی ها کرد که‌با سوپر واکنش استثنایی یاسین بونو مواجه شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/persiana_Soccer/24379" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24378">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d2f7b8fb9.mp4?token=GjTNx-FAZV5WInt98k1YXETXcJAAcuXlPUxMnhrIBSaTPwGF5ae7QxvirL6z6CygbfNmwerCsNtVpf3X7pDMkugNpkswNtkzBc7OhE-43yHzKnvHe1JUWmjZjnCcHGtPyYqBNj4ezhc1qv12mWlKCTHFv9ygqimhjL-yMoq2SwBIZQeg_PTRnoTw7xchHy88XnkHd6pZImT97HpN_uk12o8OyWePaHFz3MUPHTBUW1mY_E4_7CmmeTci3bwfB9jwMQz5Z2nw2_iaJTZNiWl4FRUkhMmnYn7dWthYgL02VJnTOenllglElphRYGZtKj7udlYTAwmC6oCCJBPnMoQuwTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
توصیه جالب جواد خیابانی به محمد جواد حسین نژاد ستاره باشگاه‌ماخاچ‌قلعه: هیجوقت تنها نمون. همیشه مادرت رو همراه خودت داشته باش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24378" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24377">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QbbC_TGJdKwNRvN4Cv3fskrRNnsyFiPlHixoBk5Stv0bo51s1_TqziDVAYFTDvvIP99SXh-GRBzZu1FDda5YfTdjyd9opo8YKQGP4YIi3C9W9C59pqISSD11p5AevFT2t_1C8e8N0cUjx8n-6CNjwxWxrFnvwGvbs-X9NBNBu0bs-vvCdgZCJq1a0LqYnU4N1q1PTJNIaV3XQB9A7y1HJD-Sx_lT7l_X6ZEv_0MSGysm5gfv1MnUi7fAgVNwarduoM-SRb-PaOXrATT3UhNXr6VB-ll2oSTJ0vT3xnThFmcgVTHAPhfDtCwWWW93gD0rS4M_Z4AwoucoEWN8kDueug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
🔥
باجمع‌کردن‌امتیازاین بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
فرصت‌رو از دست‌نده‌والان‌پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 33.6K · <a href="https://t.me/persiana_Soccer/24377" target="_blank">📅 16:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24376">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JzzLm9ZnvbB9AhhFMYuU33UhxPRIq552v_mmc6jVcEY45_BO36y1OOtVzip0tHX83M9YCdtDqFBCq7NqUN0QizIWEXLzcgH8ICgGNk4q9NIJzWf6OTIb6CZ399CiJeuBSgDaRaayMxfPX76xTzZr44bQHP7Akq8DBtp9DwQtynjetvWPq5Ql7JG_vaZy2qvq-L1rmIVakMEQhgbIbKH4klywwH4s_JDFHTgX6BRwbnjmeNfX2YyLX4WlxlcdVSTxgyOIt2AkjR495LNgZJpxpxio-BcOPDoRcOko-KniQ6pNbf9m9hBMx37J6eqh82mhYhlOBApBdCTtOz2R4C_laQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی
؛ پرز از اشتباهش درباره مارتین اودگارد درست کرد؛
باشگاه رئال مادرید برای انتقال پاز به کومو 60میلیون‌یوروگرفته و یه بندهم تو قرار دادش‌گذاشته که هر وقت نیاز شد با پرداخت مبلغی ناچیز این ستاره آرژانتینی رو به برنابیو برگردونه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24376" target="_blank">📅 15:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24375">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFlPzzGiwuhJOaU3p0QZ8b0_SuC0pR-aH6wH-7oiv-EXik-5DIGAqunYkYVH3FKZNkVnvEhM9mS5CvM3R0EkabtzIny3RtjvldDyMpwxq4QSDajkhhDdaBfZspiupd4dIRCRM61Ljxet0CQHYTnK_DMVUMdsEzifSrhjFAJ_rDBFtuxzW57WMiI9VSS4blKF2jKeLRM4LIrK5_FwQXUAoD0X_DLTKfKq6tsR_ZpfoZL99Aj4Re_OtO79scgsdxUyMTnqSZK_Efnh3ZEFDSdyuu8ji5yOFddAf9vTH-MKTKRRIhyfZcnitN7WSXzxausocyxM3KgPjk5flioG1ZOKHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/persiana_Soccer/24375" target="_blank">📅 15:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24373">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfOdsDmRmhKaF6jCwS4q9_Z1HdMAKzqCPo1F1d0GvCpSSWY_XUyVnevELbCntJhTp-zrGgzpzIpMF00pATuCSPzdhMln-SRcLoHRfFq7LrsPP1qOa34WbIMNFTThsLkaEoqLAO6CI1TWhjfz0ONJD87ltZ7AJHh6kMJuJs0T1YeO-8EjhpjsJxOyHidIapLBBEHdDlurzeiV91NMZL8b6rNGzYXs1iN3vYzJ8A_oQDWv3WcvtQ6YBGoRcRsQLjatYOKmK0SxuVz8yXeJGecKdFOIwXop1Z2fy96tjVnQAAcT6ZYY5GnYV1FAIyKgaczDy4_CdJcGkbLj8rZay_ca8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf0fdb6b2.mp4?token=aSCAek5Y8mlyk5pQ2OG6eOVMEzoCRrnZZg-O0LeOO1cB0CrJAEnUftLaSh1jhLdbjwmKnJeEqPBB7qG79Yg6Z3xpebyQ_NydbVrX7-VEe1xgKIw7bX8_bUY53ayvu8p6m39asC5sYUlxmMgleW_11EeXJtdO3-TPrSSrmtiMo-NuVfadE2IlSufYHHDmZgQvOvrtB2DuH4e4_D09_D4ek8DOFrqACKLmHH8CrDQvJcEBilRO8Z5CFn2i69t-71jiD_tlvwPjenzOj-rjzuEjbOKC-pQPS6yHH5a0DowLkHOrs7t3zKXgplTNAxxrhAEfrtsy_UWlDVkE-VZcu8qnuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سباستین بکاکس؛ سرمربی ۴۵ ساله اکوادور بعد از اینکه دیشب تونستن آلمانی‌ها رو شکست بدن و به مرحله بعد راه پیداکنن اینطوری از بین جمعیت همسرشو پیداکرد و از نرده ها بالا رفت تا بغلش کنه. البته صداوسیما این صحنه ماندگار که تیتر همه‌رسانه‌هاشده روکامل سانسور کرد تا یه وقت تحریک نشیم. برد اکوادور روی احتمال صعود ایران هم تاثیر گذاشته و ایران با مساوی جلوی مصر احتمال صعودش به عنوان تیم سوم فعلا از 90 درصد به 60 درصد رسیده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/persiana_Soccer/24373" target="_blank">📅 15:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24372">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0edb018d7.mp4?token=UcJQx60hudCenOnC1WKpXI8VFz-_5OzzHtPg1WN47K9hMMq6xk_nrmiSEW5m9mkO0GhAY7ktnuQbxLFOr8UQyVs-sAChZl55yZx2X8rDAUvRAEJzkH7I4XhJwbt6wIKZlbiUWDgGzTbsUEpqspWFgpLF4ulJEUf1o69P7w_Mwogt7m70cnT5Zj1OnSfNp-XzacnvJwZON5uGCRSDPmVOnZVLgSmgsBHfvtL8SKzo0bJNd41WNnwTQZ3xQSUq-dbduuDUvMudphb4tcG9u46wVtZmmKbbnckPhn5gfCzKpM1Qjnfbse_gjH491DqszKzD3xfU7xL2r4EZiEqfdr5vYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏰
بیدارموندن‌ساعت 3:30 صبح برای درس خوندن
🆚
بیدار موندن ساعت3:30برای بازیای جام‌جهانی:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/persiana_Soccer/24372" target="_blank">📅 15:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24370">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nz6J_6vAlYCqvIcgiBy3mKrNZwWzHrCB6D-bZUd7sHcR18TjOzrMrNU7w3dSMvinbpXPjygj2xtKi91g_Jz7T5Z-z14M3vlrrjDGc3Y02WY7bjajApzBNGpZepXQUX-yiA7BW7eumfE0WxBCDJ3pfVO6FQsMwTuVmiUqoFHPyRq1lem2-G2AMUwa8AqjXM33Z0kD6UiZmaRmsQMf0kVlOQWXqhtguQn6SfEwahzVlqlIAW8l8Zc9XV7c5eei-WnxcnJ28ZiWe0S0NNlH2WxsLT3U3UOdki107wc5DhQkJFOjwQp1L6hDR13DEEDmNTs6LHX9WccVRgyO838WDflqJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lcsGw15g6qf-_r8f6fdqwF6ncvF8-4gawkZgcmQiPHWKhoZh6ABdXPyvh3SumXiuAPXGnfFvmLSUMBjH3OW3QmbVg_AWiCS9S5NM7aJHv6rkBrHD6Jj-ZBKEMNYMZCeEqBkelU4m6CRd1xW6eSi1nTfFzuRX0GnbHQKtBIiyk9oyt625tacRfDkLWdxacXL1gtJ5Bh5arhALcgN93204fYo6qmsQ65Jr98JqmWWa25dn4DZt_t6xn1IDmVZkq6wQHG3lF8VcPDMaXTNDrDKN83JmLhSMUYwfpWJC-pYWk6CKKr_qJAKp43eSTDBF0FSxmJzjXgUtDOnSn_RfytZTtw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/persiana_Soccer/24370" target="_blank">📅 15:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24369">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kWIujCFNNI3qoCjo9nGWt8U1FQnRqCpXXzKGGx-ex9r2DOzg56uPQ-BW3h2ePD2dcz1oDSVvZlUrTqDuVH9bKxf2atmhw8cFqE45pinEjPB4fZzCTou_O4yb1vWWqY-ec-gDrs2wIMet_0vkuiWnfYJ1oyKw_S1A80WgBOcTbZhWR2OqzgpObnoM_e5lKqXs7t-mvDXe8B78yft3E2y9hMJkknsKFO_AFONNQ8P14JMtmeqAQEqwMS6jNlo9r6Nlka7ufJI5UDOLpJs42Ri0_3Bat-OcfUqtF7Wy4wJodu9o8arsP8Bv5pIGW_ctPaZ4_Cfw2n5I_Rq0Hw_yCs_faQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سال ۲۰۱۶ سمیر نصری که‌بصورت‌قرضی‌تو سویا بازی می‌کرد، برای درمان‌سرماخوردگی به یه کلینیک تولس‌آنجلس رفت و بهش سرم ویتامین وصل کردن. بعد از اینکه کلینیک عکسش رو برای تبلیغات منتشر کرد از اکانت توییترنصری چند توییت عجیب منتشر شد که ادعا می‌کرد علاوه بر سرم، «خدمات جنسی» هم بهش ارائه شده! توییت‌ها خیلی زود پاک شدن و نصری گفت‌اکانتش‌هک‌شده.بعضیا هم حدس می‌زدن کار دوست‌دخترش بوده؛ نصری امروز 39 ساله شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24369" target="_blank">📅 14:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24368">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ab6e00db3.mp4?token=FllIAr9-LGPkZrlZWWaSNQnwU6E4YJk3U5s8WVwnYVPsYidfbtzno5MgXoZdxaJI_HU-2h_gsxdik_WEKa7i_Lx6f07w6HYv8U43oGlY2DGBFZrMJxhK4TE9V6juQRF9Et1d0gzqmlzFYD15woLQkj0G4dpAXnfmMbXtjSrXnKnFBGvQ6f8NpkfIl8D4Qd9EctUAFGI5RIGFUzGxRNbKog2KriKt6pwRSKU81zH2rS4YMEQ870ORzuwOfE5p75vbdqaDyRtcvU5pRp61JRczDH81VGgLFmBKglQhIH_O9R314bYAJGyr62a3UoFlZajJJb0SgqluDyRntFdYcJyU2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
تیم‌های ملی ژاپن و برزیل بعد از اینکه از مرحله گروهی خود صعود کردن به همدیگه خوردند و این مصاف جذاب رو رقم بزنند مصافی که قبل ها در کارتون‌محبوب فوتبالیست‌ها پیش‌بینی شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/24368" target="_blank">📅 14:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24367">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bb5026706.mp4?token=MNVPdKR9nVycxbei2nlE_-lrmpqU-v2v1ze7d0CFH04WTTJ79e6hVOGCt5e3sMYAmby893U6p3PSdJ6NQ2AuocfT9R7XOqeRNjTrvxtf7QlqNbrxPvU_ZohOVKsVza1_oPUM20JsutT1XBdcG-sk4M8OzM2psIlZ-7ZruKKcoSOIYWeQqbtmJvw2p1e4k-kZ8pOg9VPGkdpw7kiz8Ole4LB6pBHM_qB0OrgMs6e9X1Ca6gIY4ufDs3CAqA8eeC-MCz8SL65N22tpsrWvKjNT4HuVvL_XaENuKvbKAo0hYKksZpfItst467FxhFASDSwvuyJY-AfQOvFcBUKxGEdv8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امیر قلعه نویی درباره حضور پرچم‌های رنگین‌ کمانی‌وبرگزاری‌مراسم‌حمایت از جامعه LGBTQ در ورزشگاه سیاتل گفت: مااینجابرای فوتبال هستیم نه مسائل دیگر. تمرکزمابرروی مسابقه‌وکسب موفقیت است. درخصوص موضوعاتی که در دین ما ممنوع است و وجود ندارد، نمی‌خواهیم صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.5K · <a href="https://t.me/persiana_Soccer/24367" target="_blank">📅 14:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24366">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i9sY7JxCe5orYuCGGRp3BsQQw9eEmZS_Qoij7gRIJYJK5HMe72-S-sWvpj2L_hg1db2mJo5D6H-OARh2SWhcXkWF_W4lBh_tJ3B40k-tibOE3fpQNlo62-c5AYXKZXevpl1T7A2KuCbkoYxZdcsqnra-XkL5A8WRs4tIbwd_mX6v3hrAiX6fj02WO0wq5z0EZQ56U_Umtu-JDjoKCmkjvduKmHYSZLdb2Pj6MQnJFcj6vpZvkznPkQiD3mI5GfzSdIVT5PsU1b83eohFcEu2ShZVETkiVNhbkwg6WK-0GGvi_Kz8xxLJChbfy5EN2MTyw13YYAu1VhMhrua3hzf4CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
دو پست کریس رونالدو و لئو مسی در ایستاگرام رکورد داران بیشترین لایک در جام جهانی شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/24366" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24365">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dGm3sdqCl9YZpQAzFD2voZyXdZMCBaFIjC3OHTGdWEjxgtpor3eR6ULAz0JoQ9ciKyAI_Kkmt6lhe5D_PiQuAu7j1vt_2oafN5IVbNXW2hmERIGtf_qL4ld70_Q6rngm92V6CnWmZ1cd91SD_FyZILKImqgVYfQV7ZdDrm8EOpVI2YWqapqVw9K370HngXcozpMsScqlL-xz1EWosliqDMcx25ic0hJ2ODwIWbXcIjdPckQdm87ySsLRgQPOXmedUa0HND7yYPvV9EMJLcWwnWtqEaXNb0opI7wa8Vzuy82AAwil24y8nalpkdsqFcQZjPe37YnBXTBA5Rl0Eq1vzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇬
عمر مرموش ستاره‌ تیم‌ملی مصر:
ایران تیم خوبی داره بازی‌ های قبلیشون رو دیدیم اما ما اینجا هستیم که قاطعانه این‌بازیو ببریم و صدرنشین راهی مرحله بعد شویم. بنظرم بازی رو سه - هیچ میبریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24365" target="_blank">📅 13:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24364">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHM2qTBQFI2PWoZvj6ny9cWMVZ9Y0J7hg4mROrwS9T1bLWl420vEyyAswtN5A3V4aa1B5Peql8ksi4Ki0X6e-aarsI41f_fBv5KtNmb-LuHqftADA8xcZB6Bm4asi1j3DVpDkXN3rEeBUGPVHM64NdQy-8Nef4Shs126yycMShtri70y1lf-yvQpz_njv3_2CLB2OMGfaqXNBc9F8MgAmoXCkw6lX8_qgMgp4KmQ0B1LTZbTVWAAwKN2qvAiJH9_RO28tfft8DA41oZKQmTge2tBW3uDWrEEgJZSEQuutq9WCRRwfYikQA6LNzQugZYQu9j34puN5OPLK8bANchxqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇦🇷
اسکای‌اسپورت:باشگاه‌اینترمیلان آماده است برای‌جذب نیکو پاز ستاره‌آرژانتینی‌رئال مادرید نزدیک 70 میلیون یوروهزینه‌کنه. پرز با دریافت این مبلغ بال در میاره و قطعا ستاره جوان تیمش رو میفروشه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24364" target="_blank">📅 13:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24363">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIa_eAhaI4WVa33haRI9NEmHvs96ySdVTLy7cEx9VF26OQ6Vf26ijxMiW2yMlL6CJLIoCbDyJrJcUrseBCk2dfc8k9MXVt5MCssZDqtKOMZ29ENuMPLZODqdzxJ8q3SyU8uIGty0Xqr0Cp8odBSTuT6pb62rsFCRyFP5hMYkeMkJ_OPb6M9BycxXBJylryvHuNtL9fAHhoav_Wzv6f5yKRjKJFXpdyBtoQNAYp3YjmsmzqG9xp8iRdV0zsjXuwiPcjk55uFAjhrZfJpaC9RIS__W0AJi6F4Nh_sX09Yf3EFb-BFOxVL0BZP7zoL2u_MutEkx4ebxsz_-axYan6lbcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏰
بخاطرمسابقه‌امروز تیم ملی والیبال برابر ژاپن در لیگ‌ملت‌ها؛ بازی‌دوتیم‌پرسپولیس
🆚
چادرملو اردکان از ساعت ۱۸:۴۵ به ساعت ۲۰:۳۰ انداخته شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24363" target="_blank">📅 12:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24362">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHwXoJUAEaV4Xaiv55MopL02r3SM8YS1hsKPOwamOx6UYMFIiCrcn-7qREoIAg2Mktx_4LFUDuNtjdmfZ62vQDwFko4NPpTFmYstMPllvN8rWW_02O6pJEjl7QJ7jLCH3U2CdXSOMHYjSB3uCElvE5ioAT5-u88fmMhXsaEEFekgNlDqwDkHrDxEakjSIv8498YVLO1bJyTseLWc1IoCRtvGFC0sQzeD87n8evHn-B076W-vOdu9lnA2AycIkePft4Oe6AOvvVoPklDfvF6d1kWzfQdMjrcIgi7hzh_P-SLByqSY--Ezfi198oyDsQkYQw0B8fL5oEpyrQf3yVYNWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب‌احتمالی‌پرسپولیس برای دیدار امروز برابر چادرملو اردکان در تورنمنت سهمیه آسیایی؛ 18:45
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24362" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24361">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/upiFSqODacQdRwNUbIJX0WGDqfz8V_tiiQiJ-e_5gIidr7rZeYZNoqKMUwiw3NB2e5xVHiLg3qVX3p0OpPQ6Qd4ZZqMP0LFuw1Bel2QFk1-mPdeauX6RR7AU4svf4lZnr6gb7TETTcbWA11LCwAB3RmKuAfjkT75yhTCuFgsAZ7P_bvxrwJ1BS91ZzReQro0FwpWlfX3iE3TwJasMrelIzszLcIBwQY0hSSyAdhg-uBVLIiPInNlRB-gBPtXbJ_vGqpigyYbAkR4xSg8AexW4JAnZUpOkyTfA7iGDNkY5ZBHwjFlmkGydYLqA6FTf4d8e37BWVblmEwY9lYAgWQYSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فدراسیون درآستانه‌دیدار فرداصب با مصر بیانیه داده و گفته‌رژه‌همجنسگراها قبل بازی رنگ پرچم کرنر و پرچم‌های بین تماشاگرا و هرچیزی که مختص این موضوعه به ما ربطی نداره و به اجبار فیفاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24361" target="_blank">📅 12:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24360">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=HERjXnOcWzDJvHvSwfnRM-ICll_HhQ6U3WnuF2mnYZEGO7kEwW8O70H_lTqo4lCeYKwQBi4x9GBJRCBUPEkU3WHv0AiTcNZchJdJXp7ZyOpEBfwA1GtLiGErnUfoD-i3kVYEhlD0lChGtxaP-4yRi26OkHgBWLqq7ZXuwAUBaEFViQTB9aQY9OVf_ncVC3FaCMfwKcBITNSvUMMItKNrpdktpo0cRQ7X9H5BAtwPfb40n5oQOqjv9EIpA60JEmFgpyomJLgSAxNYmy0qdS1HEqnzqvhSka_w7xsyl4v7z8836mreOiIPT1Uj1CInIGxWt_U3iqLPRtJNODfiwSV8mA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b03de0d7d.mp4?token=HERjXnOcWzDJvHvSwfnRM-ICll_HhQ6U3WnuF2mnYZEGO7kEwW8O70H_lTqo4lCeYKwQBi4x9GBJRCBUPEkU3WHv0AiTcNZchJdJXp7ZyOpEBfwA1GtLiGErnUfoD-i3kVYEhlD0lChGtxaP-4yRi26OkHgBWLqq7ZXuwAUBaEFViQTB9aQY9OVf_ncVC3FaCMfwKcBITNSvUMMItKNrpdktpo0cRQ7X9H5BAtwPfb40n5oQOqjv9EIpA60JEmFgpyomJLgSAxNYmy0qdS1HEqnzqvhSka_w7xsyl4v7z8836mreOiIPT1Uj1CInIGxWt_U3iqLPRtJNODfiwSV8mA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم‌هایی‌که‌کمترین‌درصدمالکیت رو درتمام تاریخ جام‌جهانی داشتن رو ببینید باحضور افتخاری ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24360" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24359">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WPCT26uk1SNfZd-sv8FYSFbAYwDGDIqpl0fi5NKz89TFH7EwcNfdC1v-w_fG7VbWv_cl7ej05xdTrPT3HqQHH_5o0Il4gAtnXfhgFdFRf6M9_M5WQ4b07gmJB9RmrBnbrjrCCAXISsVCnegezQtFDx8ukaZ72zFb8rb5Q1QKImMbrEQnzB4YgeMvOxzAv5YdCjPGUB3HRiTFjybmWptuJP3_mssBEsQeQjd5jjpOM9aSeaF1R_FafeIyPtKp3sufxHbVokNt73Qg76NLzNVKARORA3pUjLifL2jo-pjmH3VUkI2kotb9y4NbW5umUZr8ka8JQ1wSYVl-uAEhBhnIpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اخبار مثبت 18 و جذاب جام جهانی رو در پرشیانا آنلاین میزاریم. اونایی که جنبش رو دارند اونجا هم جوین‌باشند. ادمیناپست‌های خوبی میزنن.
🫦
🫦
🔘
@Persiana_Pluss
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24359" target="_blank">📅 12:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24358">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBpYhhjeAwADwu28oAyxFGI-7qnFbGHwD1drEeaZVtoL6l-1rfqvBGXLEvxtCjOOyadWm5pnnvjS56tUowBSOgVqudRxLUEoBioQTCfNfPotgE3xq3GSZJq200m5VUM0hcF78MV8RPrn6HLFFhm5CLY7fyPujpeBNxCvFE6y_QWCWzkP9KJV-jZHbdCRo7hBd15SRrQM66MO61WqxhKPd5mPqZ2oMi4oEKXx5zg1m7pG2jtkLeZOKT6j84RO-3thcjH01SOBMlT6WRdeviCG_NkQ0KHdhXvLipbq0wAATdh_M06AoUOs3F-Oc7nR3t3ukBZzlLUWGS_rvq5S2NogWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تونی کروس: دراوج‌فوتبالم و درسن 34 سالگی خداحافظی کردم تامردم روزهای درخشانم رو از یاد نبرند. موندن نویر درفوتبال درسن40 سالگی نه تنها هیچ کمکی به تیمش نخواهد کرد بلکه باعث خواهد شد که مردم روزهای درخشانش رو از یاد ببرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24358" target="_blank">📅 11:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24357">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nFeDAmvy6Aoo_YeljDsbVDbr7UCcIUEVcMM9VptXFhF0mhmKZJNtnpkDXb_lQkg8jp4-Ls2Hr816BlH08k3Rlbg1xIKORekRX_fd8wwNfkcRE7bjrgW_ttnDm32cRq8ypAqgYvS0wx--4zhw1VodpEi0vBzuTh4SEGISS-8j3tlCNU9xyA65hp6Fj5nSFoI15twxrNHfl5vw5Dua18m7TJLtDbJCAbzYX_AjUTqy0S1GshC_GO--ginB-teYdkKjYd6fTPPeLkzNELgREEZdvzQlg4YhjSH0TtIaRVbWijdHhbDgnzVEA38rZpVzdp0fiWVkJTr1pmTE2InGsbAXDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
الانگا بعدازمساوی‌سوئد باژاپن خیلی‌ناراحت بود و فکر میکرد صعود نمیکنن. بعد از بازی رفتن باهاش صحبت کردن گفتن آروم باش، صعود می‌کنیم. پاترم توکنفرانس گفت بهش گفته بودیم مساوی هم کافیه ولی یادش نبوده. بهرحال‌الان می‌دونه و خوشحاله.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/persiana_Soccer/24357" target="_blank">📅 11:26 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24356">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dFS0Q0-3RmZKMon64cvhrzhQYqfyvRewe9ga770RD9Ry6Ffo3J68go7yQHN1D3v-3l4ynMDvC-VlynsBYMugbcIi8xQF_JpO0coZG--Mx6TuKff0xnq5zmrs81O-k4kG9Tb_146KBA-3mLsjBX2vfcEemlRf8LNRViVArU1yXRY6IpP4R_wWlEmpMT9jlLKln1mJIRx4h328wYGTLcTVWTAK7ACC2ng_veJHdUNn5buv67FLv3FZj1OLowE5xS0RGy9XxYt81RVsyqbyDBB1I3mChRw4qzQXrqV3C02uRi1rw-B7gEKtpt4qW7bNRa9f-0F77sh_riOOo_2GLoTjRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇪🇸
ستارگان رئال مادرید؛ وینیسیوس، امباپه و بلینگهام در این جام‌جهانی در اوج آمادگی بوده اند و ۶ مورد از ۷ جایزه بهترین بازیکن زمین را برده اند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24356" target="_blank">📅 11:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24355">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kBlSBn5B75aMQYqe8-OfLV_ObSFQ51b2RH6eH6EHKyIB57RdbY7IHYdVYFkPb5gMgNqj_W0eIoRVKtYXukAf_e6zXxwS-SnAYz_HWAThI2PHX0JzG1gIcyJSixrB5fAyjEvPZFx0Fe6LigmmKMgrLSzp2mvSKcwVF4lFNcrJop4fQPYUJyhwjYlha8TxuMb0Di8OaqqBEDBVLN_BrYYCBfco8NuVSBQNZm4JTCFSMXf_M5qC6eoirkNYndbBBtakFkTspiUq0qytrO_WafkTmHVTy0lJ4mhO4CzUq6AOxrMcz9I31x0ECufI-_wRPVR9x8GpVUn9hG9wfA_Z8JqavQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق شنیده‌های پرشیانا؛ مبین دهقان هافبک میانی الوحده امارات از وضعیتش در این تیم رضایت ندارد و به‌دنبال بازگشت به لیگ برتره. دهقان فصل گذشته قبل از عقد قرارداد با الوحده در آستانه پیوستن‌به تیم پرسپولیس قرار داشت اما عدم توافق مالی دوباشگاه‌مانع…</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24355" target="_blank">📅 10:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24354">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0e3e7e8d6.mp4?token=cwxpe74IG7afhelsEtKTAXNqO1UzvtHXtdIri6CeJ4oB-a8iW6-yrYNy0ZCe89U61XoFgNjca2uAKSqsKOub5JfR8A4u2GynDsBAfs9yEq54MwPawueNvTE4Ba_bt8fLYY0pOQmb6UpkE-20G7OAV-x_4VKSclJ4BcZMgAtjXKcOX79tH8dVWggwSCYY6k93hrPSSnkBP7nezJdhf_mB5D5ZH305CrJRPK4FRf7LhAisoTLXYbV0XhLUHa53Pl20KBTSVF5VzAXOfS3wGP9QiX6PqHXmjM6r4yqVQcZKwrpwrhWu2NR6Ngbt5zGLwOHHGE4C72CsfSK6BZ-Iu4zMOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇪🇸
ژوزه‌مورینیو:
من دوست دارم بازیکنای رئال مادرید درجام‌جهانی ببازن و برگردن به تمرینات تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24354" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24353">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🇵🇹
🇵🇹
سوپرگل دیدنی نونو مندس ستاره تیم ملی پرتغال دربازی‌مقابل ازبکستان رو از نگاهی متفاوت ببینید؛ همشون فکر کردن که رونالدو میخواد بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24353" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24352">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HFVixNwE-im0mbX3A4fCLwQI8DGUvHK9Y_ZxP_Pn_juShNaMkZQynWgm_5_qlexZKNXSFJfNx1xuvsIur1N9_qlOzDRrPKJMB6y4q72O2lJNt7ln5P0aYFv7KA1SoCnuBz8fIjy2vxiU0b5k4xaSTkPB6Fqq4Om3rEPg4c2QbbE5SLSZa8ifTvKRCZa6s_Zvg8_1DD9i_pMQoGTcCR8gcdzNW49Fht_KPQ3PWm8el1a4XQHf5WXTO8fh-wCqZBY8DYWk2B3xPNLeJFDCUyz4ZxRU-6hz8OHDBYPCUsjyBiYs2yzsX1yltG4sTjZvJjd8ThpC5dhC1e6bGu11481dGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوق حسااااس
فرانسه
و
نروژ
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
📱
کاملترین برنامه موبایل
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود به‌سایت‌فیلترشکن‌خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/24352" target="_blank">📅 10:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24351">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIuXlL90dLiwLBLKCz4pAMtc6tEX7B6anC0dM0JxSOi9zp5FF0Hk4aFHMRUzNtd7qC5nTgmqgly5W6hiZJHFUi-Kp6B3-9263WRY45AIRfiPjKtYDAbakuyFGaVNiklP-p1DgTwBeN0XHwoSpKMrYFmSoLFajcKwSC44VxBystIvmsdd5FBj2htGO7bJzk2O8T33OqgsRdkK9lWGd6fblVemCDi42d8PW4TPhF6pqDpx6LBm2AhBAxo-vBsZQGUpV3oi0gva_m3WQbESX1e5S-6U-_mv76UY9kDdSSQoOxPu36anIlBjj-EYc-9t6tMTXW_wdIFFN1zlClcg_SlcXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24351" target="_blank">📅 09:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24350">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NcWYagN48mEjmeDW_Lac6IJOYSYFuXfjvWu-hlc1cV1E_E2Lz6sDBLOqe14f5avCHgDHeC2RlpodVpeexW157BvqqTzErlS3fouk6kR6QdU53pI351MroTTNgIbFvw95sBd48Xz2b0sl3bC0qXe1QldqMJZyi7NVZhLfV-dKKzkR71FmsniRcu082r-O5FIJB2s3TvDes86nkuP8kCM9SRqcxTVvrql34mKFpoVMPZi8oSLJ-n3cyN_Dm3oGFHoarHPr-Ostf20g1wWiBIzHaTFI2bHlJxnuw5wM6E187JvsSNa11ZF74tbxCzoFxnkbw-bYvelnA0LuTOPjsXDnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ برزیل در مرحله بعدی به ژاپن خورد. هلند به مراکش.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24350" target="_blank">📅 09:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24349">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=gMINe0RXzWQ5Es1rIhT53smzxJ-cS6zqCuxDCHzWE9IZZZjIR6ly-oZJlEAmoVvQlv71COcjTMrKVOUVaDBg6OxFgizyoDxkAqUIGlzR2G95LA7NKelwrAj96c_5cK-OG-yKFfgCdORVthY7PonhcpSh78nPl6gRUUIPvEgGc9BBPxfcMlA6jEe5GbWBT7qbwgM-sNB7bhFoq9GBphGSHioDkdbp3f_fFXdhtB8PXHbUwIkgTVrNiw9lXRHkbT6EEHOEMgUZx3aMHicGtAKpZK20hT-Q4WZa03ih8u-4GM1EwEea9KOd85M4ygZCYOeryulyon2flVaNwmX_bWtnBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=gMINe0RXzWQ5Es1rIhT53smzxJ-cS6zqCuxDCHzWE9IZZZjIR6ly-oZJlEAmoVvQlv71COcjTMrKVOUVaDBg6OxFgizyoDxkAqUIGlzR2G95LA7NKelwrAj96c_5cK-OG-yKFfgCdORVthY7PonhcpSh78nPl6gRUUIPvEgGc9BBPxfcMlA6jEe5GbWBT7qbwgM-sNB7bhFoq9GBphGSHioDkdbp3f_fFXdhtB8PXHbUwIkgTVrNiw9lXRHkbT6EEHOEMgUZx3aMHicGtAKpZK20hT-Q4WZa03ih8u-4GM1EwEea9KOd85M4ygZCYOeryulyon2flVaNwmX_bWtnBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
نشریه ESPN: بازی دوتیم ایران - مصر در جام جهانی به احتمال فراوان بازی حمایت از همجنسگرا ها خواهد بود و فیفا نظرش رو تغییر نخواهد داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24349" target="_blank">📅 08:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24348">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZGC9QebCJcyXdBaHEGxCKqtJC-Q7x9P7a3MVuNFU1zryDD8zY3-pUFsQGdwCvVQChTHlknXMnmbUDNMtllF07uiuPJQgBmQI2dRLbFW8OLcZerxFx4zFXryGOL_3jwtZqdOXGLO-8Z5sTn2lD1W75k98rkL6uI12y3QZDYvyJ1aBXYIyAqybGEHoOmh7ABI1Ggag_dnr_95QejKfRo7iqoBNfUii8JOgCXShflVQT-8FILuX1VkP8XpWZQsQgV0Yp1RaT2pWNx1DFWkvYMm-gb36n8KzyfkNtaD_Cv1aqeq8DIXy2OYOdC3kOwM-gUosHOKO-H4PQlpk-fUdHGBOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛ ۱۲ سال پیش در چنین روزی؛
آخرین حضور جانلوئیجی بوفون درجام‌جهانی؛ آتزوری فقط یک تساوی میخواست، اما ضربهٔ سر گودین در دقیقهٔ ۸۱ همه چیز را تمام کرد. کسی‌آن لحظه نمیدانست آن اشک‌ها اشک وداع همیشگی‌بابزرگترین‌صحنهٔ فوتباله. پنج جام جهانی، یک قهرمانی، و یک خداحافظی تلخ که هنوز از یاد نرفته. پایان یک اسطوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24348" target="_blank">📅 08:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24345">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hr25EMMMsO9Cya-S2AZYoP_9PJbEkAP8RSk7piozOy8zr_08F6Z3KduVl7Rv1MGixfdvQAePRI_pZqerKo4XaHOhx24PMvVhgL-TZ8FjfGzY2uiazYK3SXPS7kP4gjcpNYusHrZxM9TdF5zkk8Fc-3qx0DMNSK4ddS1XEAl85k-0Qef3jUKDGhGa3qxgq6P-zY3q-3dZLCezdnf5JlvarPwQ9TBOfuyw7RHO2wXtQuy5onMEgfopPKA7u9nHwgjeK2Pob9k_TkN8NwdUfFIjoEhtWvp8xmOXvRkSaqDhxz4Hg09uGFSEuoSrfrzQNBzuRTPglcR9VfSUOIQu2_3I5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول گروه F و D رقابت‌های جام جهانی در پایان مرحله‌گروهی؛ترکیه‌بادرخشش آردا گولر سه بر دو آمریکا روشکست‌داد؛ پاراگوئه با استرالیا بدون گل شد؛ هلند سه بر یک از سد تونس گذشت. ژاپن هم با سوئد مساوی کرد ولی جفتشون رفتن بالا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24345" target="_blank">📅 08:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24344">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tn-53FaZ0JUNLovaUN1KlYj62lIYmPgQBut9rJBmyyLHgzL81y1U0H7uqhJKoAqBZL5KxOYOH3XntIv8LWSIJKSRHLL7fmOydPGHR1KPcr19H9Gz_JbZWydK42EckNwmzCEtDIe0pXMpTKlx4MAvT9HxMuun1FoSdP5QURZ3UCTrrimK3ckwasGyLfsyFQ44RZYbU2QO0KxRtJpI4E2gPkNsXXz5W7bGgJGQQzP825rZ1lw311U1usgNuH9k0U-3YYip7d3xJBVhs5gxIyCSFMj2K3BfpIQaVWi6Qz4nqrXEn9vZS7NKm7LPIg3deR240ta8RbhQ2GRAqZf9R2vGcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛ از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24344" target="_blank">📅 08:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24343">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YUJ8JuZCDHwwFpeeMcoamgdZd3L5nEwhhiIu866vqo_8T2ulLmkmlBm-d3gGRgas5LEHJj4ZcFDs_aNdzbMgqWk2m4NcDvChag72tTXLWJ8DoLeBtkgxA8TiYUh43SS7kVPQIoVQaKwFa9qiOLi4Qz63C-FKyfWC3kgbMHCp9jotR5kUwFqddYZaD6A1mw-hYKUIo3qz4iXmXX5egzcl1acUk56qb8MPhTPnAsAg-J4yUEeQo2ntDcXCDr8i_CnULrzIv3PEfDstmMhwQjdDE5aLFCh3HVtQoogSYI-aK17vPaV_lq9Bdlt4zhHBvJGI08Nq0xPSKLdHexvHlEYJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24343" target="_blank">📅 02:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24341">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oFZvo6TATQwif7-FPtjXC8UGhQmvaY1gP4J-RRtaZSAvtGf6UDDwOFRu6SJsKdj8AdbWz51WRe8yqAdm3ijg9TXlUSttCXMpyKbkSfITJ4gUOxarV4-nd0M722MBLfAGqO89rYkjVUd_k5NtaQX__jZy4kE11nr7RuxK69j3d2mvV5W8kURn6VGkrzksLDLy7SSuO8_FzhmW-4JnxniG49poyB9NEDxysFlB_832GG0kW0-gfvrDl5tkFon52aAD7iRKaXPUxdsrrN5LSutYCA9KuFE2spO8oMmN7XuQe6CUr3_yeTxRtS6YxrAfMNk0tI1YM4SUwNA6L0JhUmv1Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌امروز؛
از نبردآمریکا مقابل ترکیه تا دوئل فوق‌العاده جذاب یاران امباپه
🆚
هالند
🔥
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24341" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24340">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g62pFV8w6GJE-bzupDaBvzgJS22Tcvn1WgxxtE1OqeL5pL5ki_SY0lu6c-vTgw_A1UUn__wqxO4fkMti158kjASWAzuTka4XceRCS4BtfHAe3kKahRUjiElSGwyXDn8oDU6TcCKvx61f2QPmugiw00lhQ61QI98EZgc8s9Anq95pJ_LTbmeRo-6EKOaHG9Br0CMHJhXAM0w_ABJnafU2UCpqWhIMFCf0QWPsCpkzsDDybPBvlnTijOrY1DL-YJKyUOrDITViG9OnOMEQJ-0kX8AfqinLZprAhP2W31j-MsbfK2w3mahTnxxbCRpl8x5sP5lTXjFTvf_NZcuOjpgd3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌ دیدارهای‌‌‌‌ دیروز؛
از نمایش خوب شاگردان آنجلوتی بادرخشش‌وینی تا برد دراماتیک اکوادوری‌ها مقابل مانشافت و جواز حضور در مرحله حذفی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24340" target="_blank">📅 02:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24337" target="_blank">📅 01:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X883fcCTGPtl1hOMWHP4Ds7OleOofz4tVZpnJ-d1nsna5lLDzgMon_McrwacL0XM_squxoKUlo_62hLtPu-DVZ9tJIrel0_0p70gKnxIzUMtbz9TwFYQa9x5Hqh4hnyfhhSWwIJjrC_RvCQwsEKVDOuTrYkwFa2X-4vIlHqyd7TEAhWKyBrAEmFdeybS2zcV4dNMaoBM_deDHDei8hWweV-wE4V-SSrP76PRLu2jLP7-Jwg8spvwGPiCfDAp2Jy4fBUXuSWA5yNh79UpR1Wtgl-TfNj6GB0HwFVnzFewnI822ljF0S6HiTX6wNrzzkluuL4QkNfNPmTMm3xxBxX5NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهEجام‌جهانی‌در‌پایان مرحله گروهی؛ اکوادور درهفته‌آخر مرحله گروهی دست بکار بسیار بزرگی زد و در گروهی که نتونسته بود کوراسائو و ساحل عاج رو ببره آلمان پر ستاره ناگلزمن رو برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24336" target="_blank">📅 01:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CG8v-ing3zrPfJWswcZD8EA2SlEISiei9gHZp5bcC071av36QXraL9-nYLjA5b0De2_1Txb3LhtQuUKK3K2S_1qHdFzlczfQJ7iK4Csd4GPDQf199vXPM1rD2c_5Li0X7KK-FdTzQd7R1r_hxMq2VODa7xMaWQSg5pxJKgNFxaYkqCiqBw-iYsx4YXJQuaxtc20RvpFYPUtmzZ7szcfkPqUA0xVl-udVoT0gcK1mWGoDRIK1J-hv-PWbWuhk8wyj6BeTUMc9ihAv4U5Q7B2hr0F0BWMuwK9Dv9OGNp-NTgUDLSM0O7DNW_DSPeoSq-WqHSySYq4QzXBVj5E7D27WIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24335" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24334">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=Bw7UZiyzs7yUJIeC9wzPKWOfgrKSBSnUnRbD0jte0MLSeLuwNmj4P6PHM1D-9nCXPUTSwO9OGqpva3ZKj7iVskqP3X8YpVQQvJ1QAFKBVd8K82_9T-ObBO9pIt-vjTJhxl-NsOHxwpc6MzZYrJWiwldH1mY6qxm0RN6vwj4vXy7O9DYqAbVTuKYXp5ZyVp92C7TuG9XSMqzvv5xQAewy2xp-FjWbEC3lhagcxvLFHK4AvSoTHzs9mgNZGqGr5FvtI2JSs8Zr1FkNjFgVIIMNWnX92xdm-Tkcc-OOvUYM6XSqKnhqQGixtRzkBvxsFX8P0dobf-lJE-QzIDCeT6yw_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1e2d32269.mp4?token=Bw7UZiyzs7yUJIeC9wzPKWOfgrKSBSnUnRbD0jte0MLSeLuwNmj4P6PHM1D-9nCXPUTSwO9OGqpva3ZKj7iVskqP3X8YpVQQvJ1QAFKBVd8K82_9T-ObBO9pIt-vjTJhxl-NsOHxwpc6MzZYrJWiwldH1mY6qxm0RN6vwj4vXy7O9DYqAbVTuKYXp5ZyVp92C7TuG9XSMqzvv5xQAewy2xp-FjWbEC3lhagcxvLFHK4AvSoTHzs9mgNZGqGr5FvtI2JSs8Zr1FkNjFgVIIMNWnX92xdm-Tkcc-OOvUYM6XSqKnhqQGixtRzkBvxsFX8P0dobf-lJE-QzIDCeT6yw_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
هوادار تیم ملی عراق که تو صفحه‌اش گفته دوتا از بازیکنان جوان اسپانیا بهش‌پیشنهاد رابطه داده‌اند‌. اسمشون رو نگفته ولی گفته جفتشون تو بارساست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24334" target="_blank">📅 01:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24332">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lOumRe-p5ZJpf0-OsGntQ3hLTpQ7t2M7-lcIsJWKgFUnNHBMW451TANpRur5KYyetCUhqReJEDcRqtnIpp27K5cQ6KK6TD0uR90pFrIeqccijc3wig9HGRdM3NSOO8cLdmAXyZQdaWRjl13BnrGLeC5lep5BIO01-QmoVUnsrBzfkEW1wblMMA-yUXHgDw2oLfa71DwlO0pXQRmxdj9MmWxeF8nES32hQd2Cg9ZckwUcTK_EOGvRURt4FinqVDDrNoPeWJn5UzFOyYAdwMo0OZD7mK9pNYTwwOxU1DPcSW8zuzsjSAFshVsZiroYICOiBwP7T8w30a-ba3SNbeBsig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ طبق اخبار دریافتی‌ما؛ باشگاه‌النصر به‌ایجنت مهدی قایدی اعلام کرده هرباشگاهی 3 میلیون‌یورو پرداخت کنه رضایت نامه این ستاره ملی پوش رو صادر خواهیم کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24332" target="_blank">📅 00:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24331">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XI071PMW8cKQZyuZq3MiVFboZQ452Mc0EXN_iBnLRhgAkFTcWedDNCYnzJ-hWTqx-XxOwCPUrmtbIX6_pl4n4qHhAW9DCyzVrF6J2bBZ2n3Z4NkFoEw4x7I_TgghdK1DLsXPWrxVU0xu5cmHat-UI4o-2D-ciJ0HzA6_89bKy53Yx12A3iZ95RELAUDRacoEpm1HHg_ubgBBgF-sS6y6ROgVOzCI_99KTxOWp5yPpvsBrAZzWBjP95VezMmIVYP9Z792_mVi_f0bNdSTNdhMyT7RE_gKzjYk6pQ4SInwtXLFbtoRiu0Fu4vvu3JwjEq2OnC9QYUfBgoJR9Zy5P35uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات|هایلایتی‌کوتاه از عملکرد درخشان الیوت‌اندرسون هافبک 23 ساله انگلیسی که به زودی قراره به باشگاه منچسترسیتی بپیونده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24331" target="_blank">📅 00:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24330">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dv9tEtHa_VTUI5ItMKD3i68OBYNpY2xXDjhI-B6FpthVqg4CJoKDtY2JsnxjpUtYkPgSwN1ZKmlY0MNmew_T7f3ZZtjrcSYvswa6gHPdbUqitTipiZVEpkL7r2pmSdYmPPjoZu59vWHksjwzciuH2uar1QHiUqtLuEXjXHXN0Fxh0o-k_CdPnXpNd85nQevG4kTR-L2ths-K1vRLy6eqBBZbKl2DO4fozbxz3gLn0PvrHyLWAHR2hGTmerC-T8XXyU6lNcrQvyRgEIrcn93aCaGm9fRyvkDGWAq1hI7R56mQ4hmfk4Oqr4DW-YiTL51JafI3iQEp6TO47HYVH3g9Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24330" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24329">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhSXtvb9wv8q87ZdTRj4lABaZvjeQG2HQMB-BLRTyAnAT62B_0jO7Da9qQqVCSOq3MgBopgYLzEhyVsXcxx_lmzzT8q97MriFdL-W37zeasTJW45GGeCgs0Ris_XfPJAeS8FA-zIwjSDUH3P8aKSfj0pUrioqKQAio2WHEuMY75t89DYqNow2cxYDXFzZj6GZ4-c1U6wQ8ZLjy2Vtc4-XI96aXid31e_zMIHw1L8Hz9-wvCszQ_1lJqRunD84cG4LBQ_yMFmymm6GevQgJqryeqCESdiKQ6-bI8_wXrhm7bpfxQSYSY3zdGTt0_QWNmE10dYPumPFDRb-84n62e4kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فقط ۱۲ تیم‌از ۴۸ تیم‌حاضر درجام جهانی بازیکن سیاهپوست‌توترکیبشون‌ندارند‌.حضور فرانسه بعنوان تیم اروپایی با ۲۰ بازیکن سیاهپوست از نکات جالبه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24329" target="_blank">📅 00:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=PU-uf4XoXyk-O1PA4kGUq4GC4y5SzFDA9973uZIj2t7p4p_exWS-y88jmBp8ms2fA-Okd69LsX-jPAp_Pe1TaMm8IdTomVuIVlzJff2WfrUQNcA2TCPv5RvNqjwC0IFtGxS2FU6YfzZ-6jfBfkLUPS876lCy1j4CSbmH0xlckOYa0N-eo1X6a8_kpWcIaixd1yDPTTbIOMZqGOzS7CR4JW4ZbVRNEXSmZoi7ZtZRAk1m07q-S-J6lCsxZqrjdvnQObkYz_kWBtW4Pjx5VQoU_a-kfhAgU7Lkzmt2iA5Nmnzu1fuDCdyfrntBV0sOApq8svtx6KzybHGC0bcvY3cGlQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e5436aa7e.mp4?token=PU-uf4XoXyk-O1PA4kGUq4GC4y5SzFDA9973uZIj2t7p4p_exWS-y88jmBp8ms2fA-Okd69LsX-jPAp_Pe1TaMm8IdTomVuIVlzJff2WfrUQNcA2TCPv5RvNqjwC0IFtGxS2FU6YfzZ-6jfBfkLUPS876lCy1j4CSbmH0xlckOYa0N-eo1X6a8_kpWcIaixd1yDPTTbIOMZqGOzS7CR4JW4ZbVRNEXSmZoi7ZtZRAk1m07q-S-J6lCsxZqrjdvnQObkYz_kWBtW4Pjx5VQoU_a-kfhAgU7Lkzmt2iA5Nmnzu1fuDCdyfrntBV0sOApq8svtx6KzybHGC0bcvY3cGlQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇦🇷
بمناسبت‌تولد39سالگی لئو مسی یادی کنیم از مصاحبه ژوزه مورینیو در سال 2016: زمانی که لیونل‌مسی 34 ساله بشه، همه گریه خواهیم کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24327" target="_blank">📅 23:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YEtRwyB9eCu4mD6WvI1PusEp0GsaPm12BcjCK-wd82u3Y9VVZbkj--aAqa_bIKp5aUXMeLMcvKnMlWQHkrKbtr6BnRGDFKEbsBeu_ox3f-gCf4HjBYxL3MDrfQ9EQq_i-YULAWCkzZwvOcbWHOqZGzJKdj4xcoOmhUY5wddCTCTXmSDULdDj_n_SxbaNNfh0j5elHZ8_0AmAIUd962u4kEjgohb9ynRWAbHDDqJtWufRXHgXEtro-SmcHyUNZE_qj2luWGE76yPjD-Y4gOfV_VDE2oAE-rdtcK87WnNGm-O4_fT14BBLf_HHUKnseRWBGR4AY8yftcg6VZdi_XmZAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تمام مسیرهای احتمالی شاگردان امیر قلعه نویی در مرحله حذفی رقابت‌های جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24326" target="_blank">📅 23:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bg0JrIxK3CkDrKsXmh5qzHbgQ4JHVZ0jp8TyUs8TN8-vIg31UWT9zWr6O3U6YCaFiMWC7ioNzRWTT26vStIZCp-otl1rCkiCKDvpzumfP0XSd7338mHYwaK3AcXdGAVXgoMs0jiv0wsd6e53wnZ1BuZ6UJREOdyjjFkUEjEfenspFqbrmoQ9aQi9p4itFnCZCjUx6m-uGE4DVB1ch5ozfQyiNc3Bt-o9THrQZ9SVX6v6rbwCo6xYEAf04SU4_kExviogqPywymSx-T9q8iJAIaLIdjIDFlatHnkk50JF176-uHrTzyac1Q0VswCXWY0zrgg8l7ZhdmNEV21Syl5Spg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
دوست‌دختر ژائو نوس ستاره تیم ملی پرتغال هم امشب از نزدیکی شاهد درخشش CR7 بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24325" target="_blank">📅 23:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‼️
🇧🇷
خوشحالی‌منشوری و برگ‌ریزن هواداران تیم ملی برزیل حین گلزنی وینیسیوس در بازی دیشب.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24324" target="_blank">📅 23:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1t-GdNaO41cLHk3loM53yH1Hf6YWbYQC0DS9YBpoew0-AVLYZZg2lTsLKT0BgkuoiblINPr_Wr1DEwriORASwxAzL_YLU8ymvurCctFj2qhdAMLRCvsahwrKXNh5sw63j8BhEdE0N1T3akIiL6k0hU_2F0xsWhCWL-sWHDd5TfxDfu3JRcB7pIsb2SJjpJXxlPxD7JSWS92rQxQ80BF5hiyFE8iBxddPCzr583c83RfNMvUiW83nE57Wc5J9F1zAW7OmSy_pH7rqooryeTNo88zBxRD6FtfwBlTg-8fUTLoAkTjp4DA5F6SKRtZ44HloyCJfC0nTbR21C_06eyycA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24323" target="_blank">📅 23:18 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24322">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBzU-tUMXbDU69N9m6wlYV8Xyi_K_9caawrYmFP9hwZXUZrgTJQ9ULdGlp9lWKHUunQSpk0rWNlITk2VLbiEF4xq75uSDsMI8zJvp0joNtjWtIMtw1xiNO9PALu8VdvCVRCsts0p1yI8nc9YsjLMhwtfz44CEVEuLt6ju60Zd3XgzRFOz8y0iJ24M3LBEBwz7nl50aaNfWUgxK3vV8ayj6Y0MkGL4ONSzFc4BLHaOUHNJnuKmlEZVT2p78lPAo10oBxy8sH0ZuhfNZ1IiWup63ydpM5346Bn2ncfylgxtVEhFVc4aSwmJBOJ9CyoUIgOViIxfY3jPH5jxcHkOxRfhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو: باشگاه رئال مادرید بند باز خرید یازده میلیون یورویی نیکو پاز رو فعال کرده و این بازیکن رسما به باشگاه رئال مادرید برگشته. حالا فلورنتینو پرز میخواد این بازیکن رو با رقمی بین 60 الی 80 میلیون یورو به تیم‌های انگلیسی بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24322" target="_blank">📅 23:05 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24321">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramCYS3ZeufbG8OmrF0XWPdhCavD51rz3tGbPw3jE47CCtPVY9CBPrQdGAo402Sie9NNE0fsICcTSFX6RzELb9U_iBiXxRqJ2zPrurGSwnPn-v1x5oRmETNsBmg0r6CrwmW8q3lx34nSrsX550PXV02Yyccl6dR4vc1lEN2QkHs2GXVnQd9ZFh9WzEPfuSOD8LjmUYXnsFje7i-xkabtEDTPhvQE2uPHXfnkfCiNNQ5U1MFkKuPcFpMnD0DRS6d4B2i7G38AUYAvn5oXh1BSS3m5TILkvEyMQeKgc8ysSxC1czRQOqC6A21F1IZOY4bYSksMvcgaMO25ut-6nomzwcJpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42251bbcdd.mp4?token=UcpEd_BozMH4ihXV_HZpz0cZ75ADKcY30fz99TlZ6aU43AV5XXCEq6jMTho-u83Tr2tVlkR5_KmtDn8Qp0VVU2e9OkjuH30YeGKOAtEze2s5Hfqfgku7Uy2iI-s4Cpf26sWTUpHz2SjbXbFIMJ8lsYvWbCtLSrq9LOt0q8Cm6sYj-zN1WdqcU3i66QyIeTPnziDfMwIDmLRx4WKSyp11EBJSE-U0E1bbzpx5ZFv_EU4E-RlaGW-Iu4ly5CWIfZivbvMkSyG8u52t6WW5NgkbGWcoCKxI1pQd8cdHWhP8-GFWTdJyfY07-TQzcc7-XnOXcFSx4J4PaM5s0Vk2d7ramCYS3ZeufbG8OmrF0XWPdhCavD51rz3tGbPw3jE47CCtPVY9CBPrQdGAo402Sie9NNE0fsICcTSFX6RzELb9U_iBiXxRqJ2zPrurGSwnPn-v1x5oRmETNsBmg0r6CrwmW8q3lx34nSrsX550PXV02Yyccl6dR4vc1lEN2QkHs2GXVnQd9ZFh9WzEPfuSOD8LjmUYXnsFje7i-xkabtEDTPhvQE2uPHXfnkfCiNNQ5U1MFkKuPcFpMnD0DRS6d4B2i7G38AUYAvn5oXh1BSS3m5TILkvEyMQeKgc8ysSxC1czRQOqC6A21F1IZOY4bYSksMvcgaMO25ut-6nomzwcJpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مرتضی‌تبریزی‌مهاجم‌سابق‌استقلال
: گُل نمیزدم چون یک‌گلر مشهور برایم طلسم و جادو گرفته بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24321" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24320">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=UgskX_scLc9S2TT8B0X0NSD0-dCPfWPCUcudTWo5f-x3pACCHkcl4oi2ZbKsLmAqF5ot2wLDm3KW4rS-EHOs6wy0DXiP2aBr-KJ7XdTQ_5IQQ4oyZiyNYH6cFoiYZOQXEVi1BXiO-2gc_JVIeIWYQzDeUUwMkd4Ms_E3wJu-kdJ6uNElkwFjhPtMTpXzeI3qPGkYqmgaRsX6le-isPlWNcJFZEDp2lPuOhEJaxuSVC6mAP6jqkMZvm0r_JDqyjj_7b85D9g2pK1ZfTUab8OA_xNiXEjFhsAUYR8Lh2heNPluDWd4hKeXo0UaiW0YfP6lBx_XNd6Ew7rdRPXzUnh0nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af4a69cfca.mp4?token=UgskX_scLc9S2TT8B0X0NSD0-dCPfWPCUcudTWo5f-x3pACCHkcl4oi2ZbKsLmAqF5ot2wLDm3KW4rS-EHOs6wy0DXiP2aBr-KJ7XdTQ_5IQQ4oyZiyNYH6cFoiYZOQXEVi1BXiO-2gc_JVIeIWYQzDeUUwMkd4Ms_E3wJu-kdJ6uNElkwFjhPtMTpXzeI3qPGkYqmgaRsX6le-isPlWNcJFZEDp2lPuOhEJaxuSVC6mAP6jqkMZvm0r_JDqyjj_7b85D9g2pK1ZfTUab8OA_xNiXEjFhsAUYR8Lh2heNPluDWd4hKeXo0UaiW0YfP6lBx_XNd6Ew7rdRPXzUnh0nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
صحبت‌های‌نیمارجونیور ستاره‌برزیلی‌سابق بارسا درباره لئو مسی فوق ستاره آرژانتین در روز تولدش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/24320" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24319">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hMC4C-9wgQYhoqWAEiB_LLOITkhZQuPQO0GOwhPjKcmP0klI36KbVX_HuHB3QReu_jlujilZ_9Bf7YUcq95TBQQH7vya2i2-A2eyl3EfbJH-_UxRLI2JVv0A4QOS9QXtKQx_wPW4ntLGQ6wSyR3-_26iiL-z0qKadyqBYlZsBeRyMMyKyOzNJN9oewdlWzkpaY90Wc8SfNqroKwNJh1xJ7Iz9Bb1qYlufvyifVYmDr72j4HIKpBJBpNtbt7MhnAxjjtOFSft3QkOHlQPUlWsWH6kBqD8xd1lge6L8YKuimm6zPsaKrkjclV_YNS_-PXn0iYsfHNKAFcoaBVDMtx14A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24319" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24318">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GlE-eSI0hGCW2dMxoqrT-GqQ-TEVnOdfQYCOOLuYp-dtW52MFE9oZEIquExhTCA-_5ltAPY4GKk3Vh6z3kzLEvNM4oQMWsX2RRM13QZve7V3_yZRBgEUBJq_V7h2HtyoNnT8iHsGUfXQlF5GebyCguXrwSHVW0KG3Hr-P_OsHaJVgBZd2hBgC9uQK16G_ts-V9fON4hAjVFmJYHPmyZKSw9L9arXneQ0nikkYG2NUi1j6TknXIQJfK6CbyY2AKwaKYf2cVwRdoDzBfbXnxwzs1pFYgnF_MZpx1oYV6x7MY0v9oqbD3iSz3_oDMGBwHZLtbFo4nvXTsrkLLzY3iw63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
ادعای جدید نانا کواکو بونسام جادوگر غنایی: من‌احساس‌میکنم که جام جهانی 2026 برای کریس رونالدو و پرتغاله و آن‌ها قهرمان خواهند شد. قهرمانی‌پرتعال دراماتیک و باورنکردنی خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24318" target="_blank">📅 22:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24317">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snXUMq1xzb_lr4YncIxtoII_6a8N04mKdJk2v_FoctQC7joPEA7wu0ZqQ-LhVK-uidRYWUT9wh4xqYZDer58PBSbaK1ieqkH-36tBtzngAEO9UAyx1qtBgsyhwvPkO9H-dioK8El8nU9t_Q-whA5lITmetkqNhbAEj6bIGPL0rdTfAr6o-d1zJzjXQqZc15-GteG6achHumhHvy0k0hRxEnw6gvK2f_mgIOBY0YUm8jTvKWhG5fmDW6ZDRpW_wmG6gFIniIByHYBR5_6DDjrbfosM4MofkimIuIbFnGZbdPQbnbYKhaw2VR3X07XtTEIdZzoMGAC2XCriGBGhrBnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24317" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24316">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=Pw1KltNTLH4kO7GeZs6Q8iukM9epcRByc-ZWzIaYyoLUpn1-eKmj8WYlPbik5F7L_eZjC-CfJxL2v6oA2CTrGDskwfJks0jKIHQasRVLcqku-EjRqbnaqbDGTut_m7O5aYitnEuHrsSm7E8HlB9qKUoyAABRorFwGKYitfIwjrpUUxh43x5o1Jk7LWlAOqzSCF5ZRRZ0f1yRouyGCZWlONz5j0ZGWlEJZ-4yR7vof93PEeA9s1bupF5dHmnUeWbtBvAMiaEelsbMEO5RVktb_RlmlFIq2u8KmlyOQC9lg2xnZm41wL4LoArRSF6cUlawXxoc9B6DLOCZO51UdCTA-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9f872bbf2.mp4?token=Pw1KltNTLH4kO7GeZs6Q8iukM9epcRByc-ZWzIaYyoLUpn1-eKmj8WYlPbik5F7L_eZjC-CfJxL2v6oA2CTrGDskwfJks0jKIHQasRVLcqku-EjRqbnaqbDGTut_m7O5aYitnEuHrsSm7E8HlB9qKUoyAABRorFwGKYitfIwjrpUUxh43x5o1Jk7LWlAOqzSCF5ZRRZ0f1yRouyGCZWlONz5j0ZGWlEJZ-4yR7vof93PEeA9s1bupF5dHmnUeWbtBvAMiaEelsbMEO5RVktb_RlmlFIq2u8KmlyOQC9lg2xnZm41wL4LoArRSF6cUlawXxoc9B6DLOCZO51UdCTA-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خاطره‌مرتضی‌تبریزی‌از زمان حضور فیروزکریمی در ذوب آهن: 3 روز مونده‌بود به پایان لیگ گفت تیم از نظرفنی‌اوکیه مارو برد ویلا یکی‌از دوستاش تو کرج باباکرم میذاشت کباب‌بازی‌میکردیم عشق‌وحال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/24316" target="_blank">📅 22:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24315">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r1j0vx3-RV5g_kSjHXHTpx0t1BuY-su4bdqtGi6YyEJYDhFJz08jI865cz_RN-UV9C_4YJw8og84YxRgqvu3tPHI-Es45uiyDJ99k1FzmN4Dugb1BvkvCyN7kuYGI2LnbBI8IdJTk2YbQd9rOBtMu4dsxTa6u3-J0kQzxFpdVTxZHgVtFLexoTUceZVCV-XEgMddePG4ak3nWWK2wKodMtfrZIegazM1GgPF9PPxkcAjOJLZsllF4CYvQ5vuSsmR6GGRUzof4Ib1ofMjwzWNWTmZkiI809qLuDag9nMuTeBylvcDLZr4aBHvxQrsrVVhK56DNEBnmPZ5f8366jvkqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24315" target="_blank">📅 22:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24314">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DDZ_liI3FymelSEbyZEVeyYwo6_K2M_lVhiMPmS3JLMOvttI22vuBZjsTTad05QDh1fW28hG-z7Dt74SZ1xdcfO6pRizeI_7-KJvYNbrCDc3EBO8Jd6aMPImHbCe30dsMEjNVERaaH2AYwY8fElpiamZNWswB-zHsXTwPxPeE1b8tPR1ZqPiQDi4Hxfa5waHjDpxWjTsgexRaBX_BQ7ZerOBDN910QxxgR122hclmLN5-0_AJEC9j7axMXIgBI7L4SYsGMD8eEgJpWJGbX1ia7RYijJnZ3xq_Ww_Pe8D60ADmEgpuNOeeigWQ4UYv4bZtK-kZA7avqHYkjfOBLlHwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇧🇷
عملکرد خیره کننده اشرف حکیمی و وینیسیوس جونیور دو ستاره مراکش و برزیل در تمام دوران حرفه‌ایشون؛ رئال مادرید چقدر مفت حکیمی رو در اوج جوانی از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24314" target="_blank">📅 22:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24313">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IDfy08WIUR6tJcsC15f4ifkelDTRPhqfqPYkLZGr-ZQ5enaXhOgd45MSVVg7cdMTgVlr8XOvx8cNMggrtI_dJFHbaINDoAm0D1CYDwb07AEA9SgAmo_t9qZb5spG7J2SPsM7m3JYlcJQInxoVD4zVuv3OuOkjThdESEk6RhTwA_GCNGpIQzZ3NS5ESqU75TF_X-gVepAHytiP5eP-9QZ1tX85LnTdl_Graudi2J0LZLdyPJ1V6Rf782DrPVDZJk42-Lij5N55lNptt3TcHqImxMIncdC-c7mzCep_MkceVmEdNapxXQPWu2p71gkNXO_8HM3hiDnN0_ceiF3VVENIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24313" target="_blank">📅 21:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24312">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVrfSFbF8nSfxcg2UgqABC8bfgX_ViK-bLZvxl5e2pqkEv2cnt5dWRiE6q9lA0PzURXI0_33kubufPFbgcE5WeumhZ2aXOn9tyQIASi-yZe8GeBYRND0IZ9O2MRUa4sSd8GD7foEX_giz6w4bg0rZxAEYvfgqgdKOW2gl8_w1yZFUKNKPFaliQy1bq8FewHiC_paWE_r_jWkfo_gESXgMXdvFJQLboIS6S3h_pmBJTW-6BpS6K_S3bT7pSU5UgWaIWY05_LMMOafJvMHAyhSyMX_GDNH9VHnp7vMOVtwDEJghErfLCmZiBROBgqBg7WF6SnR1RWWDFswlCHniDcnmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
موعودبنیادی‌فربعنوان‌داور وسط و وحید کاطمی بعنوان داور اتاقVARدیدار پرسپولیس و چادرملو در تورنمنت سه‌جانبه انتخابی سهمیه آسیا انتخاب شدند. این دیدار فردا جمعه ساعت 18:45 برگزار می‌شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24312" target="_blank">📅 21:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24310">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d98Lf4T3ek7eAc1QBCuj3ZaRhfRMlFE6Mx_rmJ_aFcQ--bUMm6LLoi2c5m_cMFZ80DZB_uFoBqdUm2MjUPagwDUOvULRkbZAQXM0JIz3ofXTKQfyVj73gb82j4XM-l8JQSMf-7JpHVDpMz8oymKBSjs8z5LUclfcFg5ev4qyTL7-p24r4RlSq_N3UvgJbzuI2U0ZPR4WMGDBnqVxHICwk1m88A6JwS9309ai80SAaybxldtxBni8sUa-d5Ds0mN8XDYFTH4MkvjhxzZpeBVp4N5-ekMUyl5MT40oUNr3iqPZh6XAhbd53r_HUV7cjNI5VH1zINmO1BKY2wsxRwUU2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JHqYAWa0p-lPpgLF_WHYNzfQqjPT4mvQOlrqG_AB_nsrDwvWWSSLICuduUXXn8iAtgwYQdJobMdGyIIEatIhvyvCID85BoFqvNjNZ74oK1PrEA4rBeTkP7KsW0yswhuRe5TGb_PotP5QXCuoyYAv2j3heIXo4YxGHKlifjT3fOdP9gWDoVsnMCxbmPY4c9uxUizYgDWCIFFVnGOlYgD6YqsMNo-xRw-rHYXPqc_arbw74YSrTzTgBxLh5H7q53OV3BmDweJAGgDQ4Bx_Main1lti9Ycm_eqnQsqHt92my1MGm_bbd1X7OuyezsVMTWOQO7H_legfDuvDHDFmX0lN0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇹
🇧🇷
#تکمیلی؛ بازیکنیکه‌فقط برای کشورش خوب باشه ولی‌برای‌باشگاهش نه رو دیده بودیم. بازیکنی‌که فقط برای باشگاهش‌خوب باشه ولی برای کشورش نه رو هم‌دیده‌بودیم. ولی بازیکنی که فقط برای یه مربی خوب بوده باشه و زیر دست بقیه زاییده باشه ندیده بودیم که وینیسیوس جونیور…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24310" target="_blank">📅 21:08 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24309">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HdCDqcDw3V5t4KBFm3Bwb5IaZsgAVwaP_p0wJUDED4C2ZNnfnY3ytaaL0SUZy6mQ2cX0oGFcs7mqKMLVQIDC64rkAwTfdjKppVNu3UlT7miv0xeOohb8m78xOAcVYBM2R_hGw5SoBJBruPYkr_QGEEGqWbTtS5ao6iNW0UtHHhnc_TkWo-LBVYpkWIwzfidVfwtKSXh3afq9jvWMMBOUE8Bpz1jFiJSvpMKsIP-nGVuU9WSHE8iANHeFLCP1iYlxH0E11Bolpx91o2UVCJaJX9_pK-A2HB9kfqIgphwbhTO4Ao_HOi6rQH24fNMsZqbPgob9pKH1fayHkc5NfAVbdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کواکو بونسام جادوگرغنایی: حالاهری‌کین کاملا آزاده که گل بزنه، من اصلا دشمن هری کین نیستم، خودم بزودی بچه‌دارمیشم و اسمشو کین میزارم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24309" target="_blank">📅 20:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24308">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpVa9tQ-IEwiVsK8mQkQuTa_AsYtorBAOk6P5m_Rpk6cK_Uq1W5UH0Ovxk3C6YnECqbA-iyPN_Vaeg9HYGjCxKuO2H9-XXKjXDklxyAEIC3BEef5mMaZsAqiH9XymhiSeiij3v1FrRiVluYVn-DoWSwxasFW06ioCmrwDUpE1lEqDj_cTArGODWUysb3Fb_sLnmsOcN65-Uz6VGABTEiCOeW0vER2auRZImorGz_0ggIzZm_EXlkcRs5QHc0pUKS1ylR73hPSFaSeItj3PWQDYURUy3IV1pjQXuqt4rZWfircIT3z1tqZbBH0B_nyotXKOt5ZweigIHFIMWclOAxkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24308" target="_blank">📅 20:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24307">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU0-WxJ93BYOCZQ9KpodESx58HjVC12Od33SRR9EHtpAZ2GdKTIIyqYwQWOT1xDFS_56l5tHj6gJGx6AKSTWRvZfLH544lsjeeQMT6OP97nzSo161Z6llt64kSBvc_Dns4Or6e75Hd3WFwckV_t_nzNf8wL5n8FFS3RlLXNSbHR_UPSZnHxg7DAbVXJUy8JRijXEy7qOWNNXJYfYPdk9VkSBVyFAkX0Tugukh78bzUq1F-7h2HyDAehbPpQCQa94dYNx8yaBYdQX1n0Q2bpbiWm4AZ2VB_QCjsRSksLJw2fEi7yKgKXH-Ds8BrHrM-idWdpEnUyq5d-XzbWA_LTohA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
عملکردخیره‌کننده وینیسیوس‌جونیور در مرحله گروهی‌جام‌جهانی2026: سه بازی سه جایزه بهترین بازیکن‌زمین؛ بازی اول یه گل زد و مانع باخت تیمش شد. بازی دوم یه گل و یه پاس گل داد و سه امتیاز رو برای تیمش گرفت. بازی آخر هم دبل کرد و تیم روصدرنشین گروهش کرد و برد مرحله…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24307" target="_blank">📅 20:22 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24306">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=d2qR3mil18tTBU7ekdaTwpEoBUZgAi63ajHhAjDYvxGrdXJWH5QvZtX31AuVBGXJBgc1UX_cymPvDtoRloGPToDL47P_QjeIBxWfQuoZLfvzSKGtmnAbKtNFUr26vVANw-UIG6P3KJuEyJ-4dHX1nLOuVMyXdAWIqc5kcNqR2WKeVm_VVeW4sEDKQmebEIVdz_yCvkdZN3A9dsuKP7oZczT13nkM4xHHM-enk1GHlh4pHAOwR0s5qY_xthr_h58A7W9wACsakzROvzRZIhcthzkYmLw8tJFI-F5PPd3J8cEIwfII8r4q3GWqTlC81ABai92Mbgw078yCGsi5gQ-HLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/992e363cb7.mp4?token=d2qR3mil18tTBU7ekdaTwpEoBUZgAi63ajHhAjDYvxGrdXJWH5QvZtX31AuVBGXJBgc1UX_cymPvDtoRloGPToDL47P_QjeIBxWfQuoZLfvzSKGtmnAbKtNFUr26vVANw-UIG6P3KJuEyJ-4dHX1nLOuVMyXdAWIqc5kcNqR2WKeVm_VVeW4sEDKQmebEIVdz_yCvkdZN3A9dsuKP7oZczT13nkM4xHHM-enk1GHlh4pHAOwR0s5qY_xthr_h58A7W9wACsakzROvzRZIhcthzkYmLw8tJFI-F5PPd3J8cEIwfII8r4q3GWqTlC81ABai92Mbgw078yCGsi5gQ-HLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
از زیبایی‌های فوتبال و جام‌جهانی 2026
؛ وقتی میگیم‌فوتبال‌فراتر از یه ورزشه دقیقا منظورمون اینه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24306" target="_blank">📅 20:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24305">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HTBNr2ZiEvpcvRcW9ObeYi64GOg8UnKh6zxDsufmo8edzAkszj_dEAPGsc5hRWQE40TabKg_Xz7jyF-H7yNvY-CGfrSl00KoY0juKsMCGqaPJ677JUlZ8L8z2RepzOvMn4IBpMADQXpApxwd7Go-s0al8X-D9_QfM8uuNdUNfIlqJTeQ7cKHdGMdP5zAonInvdZSccnzf6JS84ckWYPUOuMaLpbFdbNXiteeoa7mz6w0Qr3RweBOokukj1rf9Db3OGqMYOAgHvkQFmrAUyO3no21_WTPKJIRoX1jW8ma6JdrUIwzqGLzFe0_iHldRGug2n6t67W5yNv4041vM4nUFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کازویوشی میورا 58 ساله میخواد رکوردشکنی خود را تاچهل‌ویکمین‌فصلش با فوکوشیما ادامه بده و بار دیگر بازنشستگی‌اش را به تعویق بیندازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24305" target="_blank">📅 19:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24304">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/meLcyFky6SztZq857SfULJtkN7yPz1yLIxmFKdXbI5GIGZfTJZNlylBFlR0fKVspCTAmqLgGR6uiRzY2pt7itPTzp2VcEups2SxULAazCUguW99zS-c9ERL7AcxWc9ERC2uKrmyqXY5VL-Jn0VcoslpPS6yr1Lu7bGN-C8kYApgW9qbgiEnIw8PXGvTj61vPhUiG3vximSsIPlvTfhjlcA61DOJf4fZ19GMK5-W1X8udk5PtklBCOzvOULvEjD3iKPhsJ-Y_n5cP_ZsNILmJzwfCb4hO-SSsp-CZYysjQeno9M_zCPTc-9kDvwSjKTqekPliY4FyURT1ZWdFiDby0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ رونمایی‌دقیق‌از رقم‌قرارداد عجیب محمد دانشگر 33 ساله‌باشگاه‌تراکتور تبریز: فصل اول رقم پایه قرارداد 85 میلیارد تومان توافق شده‌‌. فصل دوم رقم پایه قرارداد 105 میلیارد تومان توافق شده. همین هفته میره دفترمحمدرضازنوزی رسمی میبنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24304" target="_blank">📅 19:40 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24303">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r-BFT682BqIY5yKGOmDx0io2GFLoVGwm8Hnvn07zt1aeI_deyUqiyp0ZjiklO4Xd1hToMl24a7hWqgpuIThYX6QgCd4P7MfiPcAafyDS_Uj1nGjpBpQIIvjLUJGI0NWRqSes_oOcilgiPYB9V81RRRjLL335C7CC0vVQ9ZVuO450Db6sqIPfyI3onK0xnCAyEJgq_jd0l-emxeJVcB05YM78idHhPABNMJWtR9FNbframe8i0CK3jtoJPNBCZ2ExoUxTL_Jg8E9LWkZ79eR_Upz5sD5Gucrq27ZJXCxd-SMZGWhJLbv42ynn5CImEqW-JK1W51p9w0xiPu1IVW_JxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇹🇷
🇨🇲
#نقل‌انتقالات|بااتمام قرارداد قرضی‌اش با باشگاه ترابزون‌اسپور؛ آندره اونانا گلر کامرونی تیم منچستر یونایتد رسما به جمع شیاطین سرخ برگشت تا مایکل کریک نظر نهایی خود را در این باره بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24303" target="_blank">📅 19:28 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24302">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=exCq1ugvj6atToCXEwbYaL7L_ZM5qNHSkst14Clbe_8mued-7P0QYsRC24PmTeREHUcfnl5Zz4bTpNyPlWZwbMIyNXtuJehM099F5YqTwNyLBmR2rzYwLzqrQ44uurWsfVJOdA06hiMyGI59y9peyC2gJ3WKXDYob07mbQZ0JldC9fD5y4fI1h8ydu-hV4c2B8DbHsoe-FWbTBOdYBRpB96RtdJkzMpOAvsNhWfK5RV8lcGp_oe0uWJKisewpM-ItJN8RPvmG-3O8RAIUUxPr9CWkQweQyIl9GT_3iaJzvePESm99E7vdVn9VFenQWMTedEnkBYgPQZAbA19OcFn8hIO9SxATBI8IHn2mE7uvOZrLqkBT-9gAWfT5w3cf1bxlFCoYtV1uw-mDul48C8Ksg0lKjTiq5tcpkcDUTH_5v7zpkfe0Y1AkrbzMk5pT-7Ts-HLCvY6wQLp-VKFsefBVEWO1JzCrUyzODy9E-wJEeGG3ZffgDNR5d8Stm3Em7cZDA0o22OZxRvCayfyu5MXb7NoEqlee4QFgBxkqXtxBL5CWu1pXn8vhixYM-B0Rx3Tnmx_dy3xGKLA6VO_TEKamLvuSZ6_qrNQ_3m9JoKBw-qALlQCKUh-vpCWoZqQssNRzGLsVaegrLL1vVFiTYi1s7phadOGmfXeXdkAB1Ua_MU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/895e84fb44.mp4?token=exCq1ugvj6atToCXEwbYaL7L_ZM5qNHSkst14Clbe_8mued-7P0QYsRC24PmTeREHUcfnl5Zz4bTpNyPlWZwbMIyNXtuJehM099F5YqTwNyLBmR2rzYwLzqrQ44uurWsfVJOdA06hiMyGI59y9peyC2gJ3WKXDYob07mbQZ0JldC9fD5y4fI1h8ydu-hV4c2B8DbHsoe-FWbTBOdYBRpB96RtdJkzMpOAvsNhWfK5RV8lcGp_oe0uWJKisewpM-ItJN8RPvmG-3O8RAIUUxPr9CWkQweQyIl9GT_3iaJzvePESm99E7vdVn9VFenQWMTedEnkBYgPQZAbA19OcFn8hIO9SxATBI8IHn2mE7uvOZrLqkBT-9gAWfT5w3cf1bxlFCoYtV1uw-mDul48C8Ksg0lKjTiq5tcpkcDUTH_5v7zpkfe0Y1AkrbzMk5pT-7Ts-HLCvY6wQLp-VKFsefBVEWO1JzCrUyzODy9E-wJEeGG3ZffgDNR5d8Stm3Em7cZDA0o22OZxRvCayfyu5MXb7NoEqlee4QFgBxkqXtxBL5CWu1pXn8vhixYM-B0Rx3Tnmx_dy3xGKLA6VO_TEKamLvuSZ6_qrNQ_3m9JoKBw-qALlQCKUh-vpCWoZqQssNRzGLsVaegrLL1vVFiTYi1s7phadOGmfXeXdkAB1Ua_MU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇩🇪
روایتی‌ جالب‌از زندگی سخت و باور نکردنی دنیز اونداف ستاره کُرد تبار 29 ساله تیم ملی المان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24302" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24301">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsckixZf_GOf7giGAsd7OnJMJSCKwHb3-vutCy_F9S3eTEHa-01gLZ481j9Get7SbwMYR5k1OL-LiR7Cx-LhU0_6g_DWRqQHXOMO24aDxR0bH1sonKRljDs9j9YX7OD6TJOaFfzgQJ9fRSBAWTpbV9oX-7pTQM-R1zp8RjiakraEsFeKfE0nKtnBDCoHxmh-0BIB-81E6ACPERrSaKi8Ql_x65DFXKeI8YosmBUziOQ0daFCAogH7a31xtIgMPTBry63lgcoCaahCZUvYBVLaSEieLWN-QcQbiRRiBTt5zmRiICVKSORLuLjAGQQrsmUzHr7SPjSrVh3RdprS8Z4tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
اگه پرتغال درهفته سوم کلمبیا رو ببره در مرحله یک سی‌ودوم بمصاف پاراگوئه میره، بعد بلژیک و اگه ببره دریک‌چهارم‌نهایی با آرژانتین بازی میکنه. اما اگه ببازه یا حتی‌مساوی‌کنه انگلیس، فرانسه و اسپانیا در مرحله حذفی رقابت ها در انتظارش خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24301" target="_blank">📅 19:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24299">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmYP5h9XlAecnGGfRk_nOzWA0s0NxrnsZQvhwW3LCDuXJzkssLrC-mVtGv8NwizSsuzozg9CS6PxTeVsjSNPccEi-PiLd7-0wUSkMcUA_yiu3A2yTQY676ifkLEd27cW_qsiQ96pjkrYThr8suzlVv3KzpJqopSdUczC9KIVczE3rgnbAXxwtfWwQ0p5dwtKR_EeaPXQ4S9aRT4CZ9b24cRTP8Z1hFF1MLaXvd1oxE5nyonNCubKSZ1AeSqJ_eTxwD2ZEO-61sNKNH_0GOhjBZD9iA_5Ka_Q_QNy8wK316gTo4wtcvGzZdHo5IFw0T-q8mcaiIQvCEcRBeSebpfoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24299" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24298">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-AtY-c7yxB16nNssl1wDOYbkEeg0ZeyNgB32Le5mOCZKIHszWDpn0Bf3rQzRwSEVLscnH8i-gWCK5zug2BgXo5ra-IAXj42Mr60EEcI0qrDpGvAvq9lZi1An4szNXAnUkspeo8hP1llEsKR4H_DzunxMrls7LI3-3LkYzBEhsHOsabIV9mNC8hbK4vb0tlPX5CnxmOWNnjGKor9DzFwU4Ir2QaJflo95fsWQ96QEtHtaVHNOsD-ZDccAFXEWM2ZcxMYPdW_vrW_chZcEwzZyLLxeFvO6uS_KHmeMTIx-scf4DfzJPMPdq_ZhvPr2bboSbGx_ogr_GwW9S4vo8ytBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیماریزیو: رئال‌مادریدمیخواد بند فسخ قرارداد 60میلیون‌یورویی‌ نیکوپاز روبرای پیوستن‌به‌ تیم‌های لیگ‌جزیره صادر کنه. مورینیو گفته مشکلی با جدایی قطعی نیکو پاز نداره!!! دقیقا اتفاقی که برای اودگارد رخ داد و چند سال بعد رئال برای جذبش اقدام کرد و آرسنال گفت…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24298" target="_blank">📅 18:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24297">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rRaXgON1Wxkg_FubVOD2IHwoZo7t1o-AREnaIeH6W8RgBqk9zm8PLOnOvYcC35UlW58eDYJSY59KXBjJuTZ6lNjSR63d70dpc9rfT3nSmUeg0sxTJGqU-3fwTKpVpzFHFUqcZLylAasNM5IHz2R741z8gkKK3PlYwVXbDgFvpvBCgIMe-RbUM_jEQrR4uNzvqYfd2AX88ScbqRpt9thyE70y9xnpkF9Z0J8Pj8cuj9u3XQhLXxBCpSK_xhcP4uTL6eDBN_Rn6r2c2j9RWTjXmsLpOfbZwEmP42Lkd2t-EvNOw8TzPba1vd2ODNMxbdEC95p_eu112eXSDgT2iBE6kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کول‌پالمر تو یه‌پروژه‌دریایی تو صربستان 10 میلیون یورو سرمایه‌گذاری کرده ولی بعدش فهمیده صربستان دریا نداره و ازش کلاهبرداری شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24297" target="_blank">📅 18:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24296">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEMKUNZ83b2hYmJCiYHtCcdeCvxAxZ7eU5GJaVK4G-PNcpamUMqqOng0n58bw0YAmxuzEB3dY3X0nHJ2EPx2V89R8c3rtTzfTcwTR2ixLgfLkJ_4q6urLCN8nBNyHzwiP94LoaSr29ad-QrWOseYC7ldA2vfg40uQrhi4SY21l4K3MTMU1JYkMJ00nRG7tSl7wFvzyJumb2IJdpDz9KdlNQof95ogulsRRduRAmdcvwrGfVAuSmPii6ZbyIduC1NtmlceZwgaN7j3bgu0-MG81yxn5g39vyme7aLMcfh2RwLNmNFipKuVBYVHfloZXA-E0a_BujhYncO_LWSSjn90g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم لیگ ملت‌های والیبال؛
ترکیب تیم ملی والیبال ایران مقابل آمریکا؛ساعت 18:30 از پرشیانا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24296" target="_blank">📅 18:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24295">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E2Zosvs9BKrH6m6myRKbyQny6AjaDPGDmSPE06GE2CF7_znRm-AczjhPzyTiLLFYJmi2psIs_hrg942Vt8yCnAq1dTtgsLPk4--53aU-SbJGXnrpsOQfc2RU6ZGafU8G5dFrQGmRAVZ3yp96XU6BlyCw5Sw2yjTpmip8u5ECs6rubRasWdKhC9fxhuh4HAkRwkDLPoZmAMfbv-nsmIlrBY13FfiN2JB23P5iLcs186rblb_Xj8ZMUjA01zHR0wGtK9JhC9e6rCR-0AYhmKT7iLagsLh9ONqenkFnmvikT7JteyxRLdmWDbg-tgZloIzhZRrjBxRDb0CweqaQGgSHcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24295" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24293">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ek_9_w7soH8PoGSU2gM7DmevOshat0YYztnH3wDuv7O4uMtPbqxhkqVDHu27Gxu_7BJhf6ZVEzAlTeGebFjN52wuJNjYXJGm9Z3dEj46PUc2TUonWcXukS3ZGeL77ADk4GKmQylvfMGBRI5XFhDVGv1n0endEj7WziHGSCSe3niQI2kLH3epOXVU3xWFtbNe8ElyiXv0qzKQjgwz7OuSnMDGcs4SF0fcU5COFVmiD90AlI1a_9qi_eLtWROguaiXyW1tqJ2PsY18P1d0kW31g88aL8kbiXrh1wGbTOqnZkM9mwHS0lSn4wCPL6zv29yijoaIjd4cmVXuFIEOqF-9nQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/StofEPVbgqAjqiQEkiw5IFf69x5bv_LTxPqx59dyZMq4F3kZjdNCafMGjIT4yzx11SvAJFqRBhVCcnCaE2hMVqBYB5LMtzaY8RhG-Wst3-pN_teFpWo_JUfkA8Q8K5_iKCrpYGgB_T79t8AeYe4pA2mH3BGC6DAhCjodmkkCgFbwbR_5ynIk39forUZeoY0K84zwps0FgAgoA0GD9hcWKxuSq3Nwcip3DaMOyRN-B1T7OZT2KanmFXr2pWgHSdf0jBTS0wgok1BrisVgSZFXc1frhSe3F2WPPUOTt3-vg2pM7VE5jrg_-Kbm2Q6yCk2G4qzN-lrU_8gLCDLlcOy_8w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
"هبا عبوک" اکس اشرف حکیمی که دنبال ثروت اشرف بود و بعدفهمید که همه چیز بنام مادرشه، بایک‌شاهزاده قطری که 2 میلیارد دلار ثروت‌داره رسماواردرابطه شده. هبا و شاهزاده تو جریان جام جهانی 2022 با هم آشنا شدند، زمانی که هبا هنوز همسر اشرف بود هم دنبال ثروت اشرف بود هم بهش خیانت میکرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24293" target="_blank">📅 17:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24292">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UegrF3Jl6oZycJ9QCGradXsu33Mo0r9i3L_jhjP7YBoMwEr-JcEujSmUBxPbkS0QH5nMbhe3PbGhnj9e7wAoJCW5CQe4if-Kbmx1cuDzO3AwS4AvE4B7uY70wFqrXjAddOwAnLWp0yF-apEJTZARbGfxTyji5RRbtKvSdTJfe6gFODGSRGMPql6GYYP0uJpYFzdBprRVyxBlzF66CmmNIh5XfWSGBwbpRfl_R4lf1I6wMFJR26BsHOGG4TEmcCHjvsd4OVJOozzy-Mscw3PueMDG0qgweSKymJprzZmPloetOzw_P280G-UIWBTbHsqDna3znmWk2Sh8ABSOIgxDZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ دراگان اسکوچیچ کروات‌دقایقی‌قبل‌رسما پیش‌نویس قرارداد دوساله‌اش با باشگاه پرسپولیس رو امضا کرد و رسما سرمربی سرخپوشان شد. باشگاه بعد از فسخ قرارداد با اوسمار ویرا پوستر اسکو رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24292" target="_blank">📅 17:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24291">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUvg2RfXjePux-w_K-G9g-NHKtEYcMUoRyUPgD2PKYayKbngT34CB2t8VPhMcHLBAp0RiwPt6_H92FIMgzpqpGlrLX6Eh1npMcloMcK3lkcUunG14jctRJVN-AUpLqLrdLSlk2yyLJ6ZSwDoGqb-R26Q8ejF7s-6j3_LeElHtMBTahDZN_olAwdc91WVBlK5wQDsoNL11HXkrgHj-E0E8Au1nBpX_4vQvJJ1SJ5NXeUD4n6RYOuPOc3oGTfxeWDxkbqF-vRAIfmvskcVQSBz6ZKoVDCQlmJjxpspiS8LIwrDdQdqRQvMItGjDmDEOYlG0H0LM2c377s7x4BqIVU0xQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
استوری اوسمار ویرا سرمربی فعلی پرسپولیس درفاصله 24 ساعت تا دیدار مقابل چادرملو اردکان
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24291" target="_blank">📅 17:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24290">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=Vu_9grbZjE-Lelcv8IAiaMmeE44NpqUCw-EGJHodfDiXwteNGWOfNBRynRqrO69snhkGJc2N3C0DB3C_JOwBptWU7MXDq6FJ_qWHWvwroSWpqruPg3NIiUMGMhsXbbala-RY9ju4diFfspiiPfeYZ-_Kd-JgZHDQjhMpaGE-YpMKPrNAlw6ItPlZgv0t6EnKCoVBhbH-ROL4Sc52iSUWhOLlm6DsCtP7cmtRIDreXpGBd7B6qgBZ5qIBG7Jel0IFEiW_-YfVvdM0UhbNnV9ga4tg1w8p3Xc3B1p61DTklY4ocitkVus8qIjIfOVYf-TVixp-81_gk_Md_-VKIK-_T4Hk19-62_OjBEjLaa-75CVRaf4y3PohLFHRx_cPZSVfi_QdiwGtxi4jq391mvRg_vKnLglTtuctWtGnHH1gFLvrAqeicxfQdilu8ZyCByaAWSZrCq8hcGDP9ejVXzE9IVuyRHDLefmJoxho96zTPGO6iJwzTQd06RXQUgJMJtpo9HXztCSC8zORZATOAQkGgqb2zvTVB_OSJixc1poILS1H12JJI0pe81yr_jjygpUY7avMZlkj3DFB5cUtNhJaGHFJ-JeBLISNVRofMtvty_-AQpkmsBHR416DdvPYVtRwIMXfKwk2DXa2XCIqvQWzN4CkX5wZ9I5hmAHokL3YbSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d5e9c8b86.mp4?token=Vu_9grbZjE-Lelcv8IAiaMmeE44NpqUCw-EGJHodfDiXwteNGWOfNBRynRqrO69snhkGJc2N3C0DB3C_JOwBptWU7MXDq6FJ_qWHWvwroSWpqruPg3NIiUMGMhsXbbala-RY9ju4diFfspiiPfeYZ-_Kd-JgZHDQjhMpaGE-YpMKPrNAlw6ItPlZgv0t6EnKCoVBhbH-ROL4Sc52iSUWhOLlm6DsCtP7cmtRIDreXpGBd7B6qgBZ5qIBG7Jel0IFEiW_-YfVvdM0UhbNnV9ga4tg1w8p3Xc3B1p61DTklY4ocitkVus8qIjIfOVYf-TVixp-81_gk_Md_-VKIK-_T4Hk19-62_OjBEjLaa-75CVRaf4y3PohLFHRx_cPZSVfi_QdiwGtxi4jq391mvRg_vKnLglTtuctWtGnHH1gFLvrAqeicxfQdilu8ZyCByaAWSZrCq8hcGDP9ejVXzE9IVuyRHDLefmJoxho96zTPGO6iJwzTQd06RXQUgJMJtpo9HXztCSC8zORZATOAQkGgqb2zvTVB_OSJixc1poILS1H12JJI0pe81yr_jjygpUY7avMZlkj3DFB5cUtNhJaGHFJ-JeBLISNVRofMtvty_-AQpkmsBHR416DdvPYVtRwIMXfKwk2DXa2XCIqvQWzN4CkX5wZ9I5hmAHokL3YbSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
اسکالونی بال؛
تاکتیک آقای لیونل اسکالونی سرمربی تیم ملی آرژانتین که به شکل فوق‌ العاده‌ ای هم در حمله و هم دفاع بسیار عالی عمل میکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24290" target="_blank">📅 16:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AEuStT-iIc4yk-9fwDQS1wc6-AZXufS3o_SxQ5jFE3iUQ2In2zS5hSEWWEIzSx6VYettGZukZXfn2oAp6mQHOKn43x9tIbhp3EctmV6Zlzfav4mfBdNkRQDAs05IcE-kj36Vqhsk5gq5jF1lq1sxp4EnrVVAc03XDESWFaD-VbVggz2WgO2653bemBV0rwZFKyTCryDg4Ktwv84iQ1BIjwTM7eVd0mmYxAWYFyt3lGizW5YBIR5dascTVt19iZ5SG5H75a7DyHJfyCOYOIpVYKL2DdbauP9By9K4zHfcLoF-bsmGHWQd65vD6FRWq18yMH87adCPSDnDDoOEq0qhHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=ByseQ32uwagKNPpv1eZC-hnufUxteNrIcUO5ODxjS4ZUtWakrYDlgF1h2xbgk27BSaJwWUDphNOvXwWyVqr8rD1YvvKzyZjteQXzj4Vkpenu7zRcyY831CS76ztc9Qz33EoFTnzSIBlSHVsvf0_-OUm08cQ7Kyw-6uTdtykxsTGRk6JHgSFd9PmKKxX2es7oIvYVOFNXxfyRfWNoqQWCVSA0GpN3ZFS-9pnAPpDDVj_9omPR-bDmQ1aQSyp4-woGSv3gSUEtYnLm4-MGyXVvWP3tlU0a4zm-1MXLz-Ib4P3K0PcnfupTRoH2H-Gl17D2_cBqAfoXm9px5Ml0JIOJPriTk2TSis2xtRhqhdfx8Sclm5Vkj1rJQ9JVwJ4uT6D5g1GAn0ds2Qy_Qhn0rljFiQIqVSwwordS95M28J3K1jCoWNYwCABDn_P0ZgvtLmW6wRrtvpeHeF8zHHZWhlBzW7n77VCK2ePQJjka3d914kVvGkkDpTt1VXsAREXna1yqm4d21_xQsF328VosrH1aARhODHvE_28tqdiLILo7QuLP3n4daRq2SbPhzXyhZ6iVbX8_IeIGUaFDn4_SAAuHydLo_6qzCnoI5gk5-TDhy-a0e7gm-F05eGFZ-NoGSbbS-UHhe2sLQQ6ZgyFOivUZNo8F8BKp2mHQWY1T3aV9IdM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=ByseQ32uwagKNPpv1eZC-hnufUxteNrIcUO5ODxjS4ZUtWakrYDlgF1h2xbgk27BSaJwWUDphNOvXwWyVqr8rD1YvvKzyZjteQXzj4Vkpenu7zRcyY831CS76ztc9Qz33EoFTnzSIBlSHVsvf0_-OUm08cQ7Kyw-6uTdtykxsTGRk6JHgSFd9PmKKxX2es7oIvYVOFNXxfyRfWNoqQWCVSA0GpN3ZFS-9pnAPpDDVj_9omPR-bDmQ1aQSyp4-woGSv3gSUEtYnLm4-MGyXVvWP3tlU0a4zm-1MXLz-Ib4P3K0PcnfupTRoH2H-Gl17D2_cBqAfoXm9px5Ml0JIOJPriTk2TSis2xtRhqhdfx8Sclm5Vkj1rJQ9JVwJ4uT6D5g1GAn0ds2Qy_Qhn0rljFiQIqVSwwordS95M28J3K1jCoWNYwCABDn_P0ZgvtLmW6wRrtvpeHeF8zHHZWhlBzW7n77VCK2ePQJjka3d914kVvGkkDpTt1VXsAREXna1yqm4d21_xQsF328VosrH1aARhODHvE_28tqdiLILo7QuLP3n4daRq2SbPhzXyhZ6iVbX8_IeIGUaFDn4_SAAuHydLo_6qzCnoI5gk5-TDhy-a0e7gm-F05eGFZ-NoGSbbS-UHhe2sLQQ6ZgyFOivUZNo8F8BKp2mHQWY1T3aV9IdM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjXdIz5WQpy0We3qpyeEaSScmbSgqvMUujSQTwAMu7Mi4mZshHLA-zzDpmu6KtQR_uyApJZ9YO5B2JhgdHdrXMmsBLCBidiXsMoIrM5kjRpQo5ROoqbIj9TpHGTWhaVL6rCKDLQZgCC0J1sTl3dPwjTsBzRVmrSbXYw_cuZzrOsPvjrDyEtxg0dt46u6wA5ULgMHAiMSve_qE5zkYDwDMz3wiTq65wz5owCn4FmV7PGLiuhWrNOwe9Iw-dDkeAizrLldWPrjGiEkd_igyMr1puOoFj4IMGnjRpByX-SL5SEv_eMI-pkmksHhtsbdzzDGVOOvm4jdG9ksUX9pgPiPAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uQXMqz9_1_YKq_Zi-BVzR2XTJ3qelvqEM3S5Z7z9mBxOo4Pk7JhlkSTHnDokMV--hRdBivazDRwdOPAtoDNq5qgqSBUdaU-MbzQ5fBEEpXt7RDhEZO6m1i4nYmdQQdOwVttTn-77kAINosxKglqVHfvj8ww0kn5ufK3JqhXu6zgg055ZYC5-Y3Fh9dPcnAOWOc5fbLmyeWbVuJPCiOGFrumjmK8sfp0J5ohxvTVxtjX-Eu4vIP4-e3dzqXKNe9g2-sgAOaecHXeW_nV5IaSSn7wmEKYvwDziox-VIF5_SrBOXYB18Y543dy-4VB4xg6Fx2ueRSgfSSLh1UtrwDnQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pldRNKkqEDjQ34vgebw7c-Ks5t0rRVEX-LfKvuBaWwD2SP17x6ScTd0AbChQlxswhCcoqKM_JDq32ZkEb1EPq9CJxXZW2Q1lQNo6tkstr5lsq7ZLhj1-eWXkDjWLlH2ZcDyelBKEvLeULzlcsdpkhn1EeBdE5iPkEzMplQXUglpwzMaHZo7iSGY1G5dRFWxoZDI0Y-OWEJLkaFX-lvD84TihJJiuZW80AYPDTU-FtOcKtHMyhYlIo9SSKAvoAPjulgFFyIMh4iKfi7UIC7C9yTYvliak9Oe3V6rH8pC9otHejrhMGo18sYpoeTCV0VE_GMUvtVEQ2SV8YaztkE_TBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/II2WEQLuLGSkGrPCnNAS8TUWeh65ye9Zbc0jSEaUmY2CphsQ5zR88ruPwdlQ1Zo-oSjMo6c6jLLiIjGuQRTCPAjWhGyXDlV2opZREK5I49BOUDZ6qwBn-vQ9qx-_LNwiZ8KvG1MbbwsXb0apUX_fXc4EPUA_UYzEZVfD73dKQioVT5-_Tesy8vtwRz1qxsLk2D7NhSMaBYu8RQ4_n65_aGer1epBMRPaPXcyl1XAqxkC7in376jwD_DDCMYrzN-CgHt1Rywkq4jKP5FE0fhYUxpobULeocic51DaB4wHA3qPIbY7grJcMZEccpRJGaRJ_8pRUG3bXtAC9gQC-1YZ9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/arkzwD_F66VwAb9LRyjwPYNFrpIi1jO6cvzAhcbkW3QGT_nS-eXDDyHc8Qk6WtUZ52dK-TCwkbKZyc7fYmLh1wQtinyP70rpdn5fAkwOgN9JAUAvO0amA3G1qVh0B5nK4N4FfImn9a6bV8QF_uAiZUXt0mW6i7AaQacQ7rC8Y5u0EnSzqrvOSdt199yxycTPo-yi0hcwrdgNUUMSwvfhTt5xuxmtRAxsG_u7MYJWtzA8ge_4zXwSgfmCDDCIcCBB3N1DoCIkmosZjNwFFH5Cg0p66TQu3yevRfMwBygWBLLMYqyslSycq6vEUCeA1Ijfs_HMSLVkmBHlQwA1RaT33g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
