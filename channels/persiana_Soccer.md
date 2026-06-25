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
<img src="https://cdn4.telesco.pe/file/vJM0Blj1ZfLHKPSPvru6ho7JvClCvqDsL9rl70_CST0BTh_oGY_MYQDHaRV5zSg6Pi2EGW_soVY9I8NqyMV2PSRHe7IPmaKGoK_QX8wUbw_-5V-QVa-oIniKWX5Ka5_sNn8ABdi8lTgEQcBIYvXDx3BoMLS-6-vo8W5Wj2B4DdJCzHjUGgb09lMgsEyNqrahyZB9KyV5JHrE51G_kmlOlCYMrksorM0oDbcUVzS2mQPzuJcmLTCM5mOmTc385MsjMIvAwokZBi_NFKANFd8ob7rJGx4V_E6ZdTc8LkNG1oLbFpf2Twf3CHDwf6DrDGxxmtd4gPLQNhQsUbdsxiPG5Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 318K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-04 16:41:52</div>
<hr>

<div class="tg-post" id="msg-24288">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HOqvRh9k540kzKOL3G4cicVwQI1w5C2gmf6wfc-_nDPMARYTuI4Ag9eMC3oi23wuzUVH_Kj3UoQMpGU--XP2LUWTG-4TLNLFrjgPuGSuJ-PASsV1zw1Hr3_-E8fNugb1EdGO7BqmRLLa1-T2Rkz7lafeNk_ngBHXTljAyC4l9tfcOcnrWzHT9vGEZyuiMUjUVLulDU2zY3wvN_OriyggZOmOnYuftxNTdtkU7GEvxyCbJWL92YqmC-CRMp9ltmiIKDBCDgtQ74_hBe-njTi5Fuvj1QJ4gedAVEnfzJzqViooR-RSRKEK-f5l-2Olm6G36xUlMoZD_D_-jmVNyUwSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
خبر مذاکرات‌ نهایی‌ باشگاه‌استقلال و توافق با محمدجواد حسین نژاد که امروز اکثر رسانه‌ها اون رو کار میکنند. 10 روز پیش اعلام کردیم که باشگاه استقلال اوکی قطعی‌رو از حسین نژاد گرفته و فقط بازشدن‌پنجره و پرداخت‌رضایت‌نامه او باقی مونده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/persiana_Soccer/24288" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24287">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=BaHiL7gLpgYGEip-S2XKlQS-TFZ3nojfEabL_u5n5FJbCXvZQ190zG_8ruJbTOcIkznA3VvxwVOeHrmsLqg50bfHoVNvOogH1KIT73WfIrroEZPpen1FGM5QJ66P5b7gQvr-4m6nZPdpmy-P7jjgwJOYRm9bUps-5P9NWJgM11cv95YHVFWsTWeSBBYkdDKwiLKPSWdfFcGedbfJuSBUJUI6syv7OKk9MkqTmJxaPE9I5jv2cQVAP36lT9zDDbAZFPSZNcht3kjXQ0_EBDcb81JyZ7BtE-TrRI_SoI3tj1pKOJ7xXHe9AFru7uyCceaMQIZuGDrYWTqge4VMQhB5LD3zGkfbsOTSdKJs2UhxPdvsK3pDCptqJPiohVXgIvv5J2rEnJ890Fd3ZkKzPzjO1SeDi2Bk6QmjqY5dWGLpM_7AQi6dY3mVlrQPDle7H9aVznpkan7w4EIaECiUb_tQX18ATliLBObBgpvdQtaheot8yZld_0_LFdFb5lEoUBKwptLkLNj0gjgJq13_4FJjfVp1q8A7x5QZ0ti65jXHkDiXEHPWWC7krHJFabNeIuwytBkOsAn2pUiOlm-Kh0qFjD5udb9ku-n_8C1Gbw4VBLEFnn3-m_guIT_J2uz2vdAE08rH1E-n_rsKhNO7HNzq8ju5ckJJJsTAg_PuZw-xDS4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fe43357c8.mp4?token=BaHiL7gLpgYGEip-S2XKlQS-TFZ3nojfEabL_u5n5FJbCXvZQ190zG_8ruJbTOcIkznA3VvxwVOeHrmsLqg50bfHoVNvOogH1KIT73WfIrroEZPpen1FGM5QJ66P5b7gQvr-4m6nZPdpmy-P7jjgwJOYRm9bUps-5P9NWJgM11cv95YHVFWsTWeSBBYkdDKwiLKPSWdfFcGedbfJuSBUJUI6syv7OKk9MkqTmJxaPE9I5jv2cQVAP36lT9zDDbAZFPSZNcht3kjXQ0_EBDcb81JyZ7BtE-TrRI_SoI3tj1pKOJ7xXHe9AFru7uyCceaMQIZuGDrYWTqge4VMQhB5LD3zGkfbsOTSdKJs2UhxPdvsK3pDCptqJPiohVXgIvv5J2rEnJ890Fd3ZkKzPzjO1SeDi2Bk6QmjqY5dWGLpM_7AQi6dY3mVlrQPDle7H9aVznpkan7w4EIaECiUb_tQX18ATliLBObBgpvdQtaheot8yZld_0_LFdFb5lEoUBKwptLkLNj0gjgJq13_4FJjfVp1q8A7x5QZ0ti65jXHkDiXEHPWWC7krHJFabNeIuwytBkOsAn2pUiOlm-Kh0qFjD5udb9ku-n_8C1Gbw4VBLEFnn3-m_guIT_J2uz2vdAE08rH1E-n_rsKhNO7HNzq8ju5ckJJJsTAg_PuZw-xDS4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇬🇭
​​
طرفدارکوچولو و بامزه غنایی‌که با جان تری اسطوره چلسی و بلینگهام‌سلفی‌وفیلم‌ میگیره؛ گفته ازکی‌روش میخوام غنا رو قهرمان جام جهانی بکنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/24287" target="_blank">📅 16:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24286">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7Ja3BXP2dMTGFHubzE0T6hY5vlwq-rJU0mxiLJIMb3jfTq8qmkeSEVDsDOb3GH8pNIx0i6Cnhitjp2-8HKeBsDM8I2lBVW2llYMQehjV199TLo2abzpqy7e9qgRiTKMTpouXJInUD8M6eWHwcsVabfgiaCTRZ7BNrO-lR2UDIlu_EWMLz12C62LpSJKGqZ25SxbutF95cH14SSWUcd2nuFD_fSQ0d2ujk4oBW9g4DagVxl9GXM07rP-lDJN4tNwBGyINX4oozlAAiHFd2oWqmD3KFwWzfeCM9dlGNHG4KtTRVDsP3MTwBWP5itq1NUiO__YpEd0nlR7Hiq3mPiqHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
#فوری #اختصاصی_پرشیانا؛جلسه بین مدیران‌پرسپولیس و اوسمارویرا برای‌قطع‌همکاری دو طرفه به‌پایان‌رسید؛ اوسمار ویرا موافقت‌خود را برای جدایی از پرسپولیس با دریافت 900 هزار دلار اعلام کرده‌ قراره بزودی باشگاه‌این‌مبلع رو در دو مرحله به او پرداخت کنه و قراردادش…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/24286" target="_blank">📅 15:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24285">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzk3oqbCgyjWp5ZUqVaf66AdY9wMM6wbLccAVfhR9QNMRUBqJNSy6AhA4RT8H0O-MreuTjPNJmfWNT1yTfUDf0lCJm3tate3YZTmeP9n0_L-dSuZIx-6_5oXOoUXBrtz8KO45PMKby0A-zfapbe_SZtNlKQEj7PjMBNWkKRV47tZLkFQSfVSDt2hDRvuCqWsdxoJsVe7IKtC3pGu5HWCa8VZBtYvygI7WiJBbUIDpaPfvINoNVoscdZHwK8oRnEst2rIj_LCPtTsT0zmT4vCscfNwBTGI4h_DasXRJfhig9ktZBxHPQTqEMSubTPDRKp9MMlyk4zlwXw-7eYfGEbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اینکه گفته میشه‌درصورت عقد قرارداد بادراگان اسکوچیچ؛ بازیکنانی همچون سروش رفیعی و امید عالیشاه که‌کارایی‌سابق روندارند در جمع سرخ پوشان ماندگار میشن کذب محض است. سال گذشته قبل از چند دوازده روزه کارتال عالیشاه رو در لیست مازاد گذاشته‌بودکه بافشارشدید…</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/persiana_Soccer/24285" target="_blank">📅 15:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24284">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXbkbKJLAlz2ESbu43Q7RwBbNXKDsmkFjvSikIYd2eL78PsmQjnhjpF4_pzYUU7UoJbl3aa-pg4Y6oEVGrEt19RPJT2gejG1DczTvHxAJ-535jOwyWypEeMtcGfu2nkhjYKwSlNNknVGZDK3hca4qJNTA-D1Iz7fo0k7VNbl0T8yVuQO5wBslwUl2RjNZYEhvE9L1dnYSAbu6-Tc4AuDe_2mzP0FPgshzUFFlDoGTBsy3tk7Tap1OKMJ2FWlFbuM8vf3rvbKBW2gQF_ASKZvV_99WHrA4qLpPuE1qWQ0bWucW2sGnuXFFS9FiM_q3N9v_RoRDfDdD911kAY7McsRsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق‌اخباردریافتی‌پرشیانا؛
علی تاجرنیا رئیس هیات‌مدیره‌تیم‌ استقلال صحبت‌هایی با مهدی هاشمی نسب پیشکسوت آبی‌ها انجام داده تا درصورت توافق بین دو طرف؛ هاشمی نسب بعنوان یکی از دستیاران سهراب بختیاری زاده به جمع آبی پوشان برگردد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/24284" target="_blank">📅 15:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24283">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f30x5-UJv0u9R8-m0-y9HQd0rS89_bMHioFiXF0cX9Dz2Yu_4dStX7RLiS9DLKKtYnff7bUbJKVyHPFlROrGQgAmjpkB8YhBdvm2DJQoditd1LYD2CitUdw2iFAY-XVNDX8cpTPg_bb2iSq1LB0K5NsZhd1jvICxBupqknejmwWEsfFq5GCFPVsDYNe1Lh2jhXMVUh661xkLVA5jQaj2He7AGFpVasMhqgrlDEN2jB0wDErRBlMGAgbL750xYos8zWcMbqP2osXxOMySuAVvbnQbzM8UM3yzz_YJzqfg1ptdr4VsyOLb0FksbB7pV25ZehObb8ZTeLM_OvEstA-D_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
یازده بازیکن برتر جام جهانی تا اینجای کار؛ با حضور رامین رضاییان و علیرضا بیرانوند از ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24283" target="_blank">📅 15:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24282">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qrv4EUV9oGyBtbIzQhHoSXL1p9PMbC91G4V3idZN9ltlkvNJuStdweEAS1aQRDvOSpyVEru82XALmYqIgTDJHfELg_Ex86Pm4HslNvp3Z3J_Ut2LGrUvhLT4PzI5SZNMA0MWF5P-prk6N04afM8nRlvprncU81auqducIjVPu71bRGN1D_18WxKZ87RTZRuWTPJ7CCPqA-38QVDjFNlpKYDkw0q33xAgbNO8HJVaeqOZshhqobJoxJYst8dAZbXWZNXB0Syoo9QyE0TYacIcIrxkIwQGDaYEZOjgQDmnU2YvSAOU6S9KKMlEeJ8C0avBKJMxNseRoXrrpcieP88EwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
اگه شاگردان قلعه‌نویی به عنوان تیم سوم صعود کنه در مرحله بعد ممکنه به امباپه و رفقا بخوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/persiana_Soccer/24282" target="_blank">📅 15:03 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24281">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=cIPYYtxQYzs2J5Bh_oXlvXX7sDsootI8eBXXL4PIuNNmkghJO6-2JLZUZ3V-nVZMUHdNa56HHWyC2uJnXet64lk1OzhI5W1Dfw-Vs8qmlnsLjvIP-s539UJaOqOR1saH3nzb0s1E9Ml8lhQ0LDm04fsqWTdWyXHORxf7joPf49BzZ4BUqKEt02P2FDlXJkzggN30PrZbK8zE5g3emghfGi_AujZG9Ohrse1bDiMnbmNSQmIb3nIF5TDMPYVjgoGehVwlQJq1h0AwrLsBZr3fVApsWQSDw-mbsst64f-9IFYa9h20MIpYMVlJ8sa6XVff19srOTVAD8SPdCkEb3fmfA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4afba99e55.mp4?token=cIPYYtxQYzs2J5Bh_oXlvXX7sDsootI8eBXXL4PIuNNmkghJO6-2JLZUZ3V-nVZMUHdNa56HHWyC2uJnXet64lk1OzhI5W1Dfw-Vs8qmlnsLjvIP-s539UJaOqOR1saH3nzb0s1E9Ml8lhQ0LDm04fsqWTdWyXHORxf7joPf49BzZ4BUqKEt02P2FDlXJkzggN30PrZbK8zE5g3emghfGi_AujZG9Ohrse1bDiMnbmNSQmIb3nIF5TDMPYVjgoGehVwlQJq1h0AwrLsBZr3fVApsWQSDw-mbsst64f-9IFYa9h20MIpYMVlJ8sa6XVff19srOTVAD8SPdCkEb3fmfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
⚪️
اگه‌تیم‌فوتبال ایران در پایان مرحله گروهی صدرنشین بشه مرحله حذفی به مصاف عربستان یا کیپ ورد میرسه. اگه دوم بشه استرالیا یا پاراگوئه حریفشه. اگه بعنوان تیم سوم بره بالا کارش سخت میشه و باید به مصاف تیم فرانسه یا کانادا بره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/persiana_Soccer/24281" target="_blank">📅 14:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24280">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cKSNaJ-73b2y6NiGFerE99Lk-cEAeY1Jjh8BaEESSONWpnsNpFusFpEW-5PExjZD0srP8N2mvADhLv6U73rtEWahbj2II8nSbyeJ400PqOWjPkRxfNdopd4qDyb6iq75Nnlv62INACMOTXpgxmxtecJrMbW2RUJuXsD6d4mE-agEPmPpjgVi4-vRqBbJDHXKVKcGiCUsvmdIRjaUXVfEmv9P0aTx2--HDI-zg8-1kjPv05-Wy2YTX7I72RxWJpqrbLvh22H0jMQzilajPMt-7q5aM3b8SRz2mHScZsYdarad9z2Xx3edFtdtoVak_Mo5Ir8i0mN4eoNgB2Q1qSvLPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
امشب‌بازی‌برزیل و اسکاتلند درجام جهانی برگزار میشه؛ تقابل این‌دوتیم واسه ایرانی‌ها خاطرات تلخی به همراه داره؛ ساعت ۰۰:۳۰ روز ۳۱ خرداد ۱۳۶۹؛ زلزله رودبار-منجیل؛ یکی از مرگبارترین زلزله‌های تاریخ معاصر ایران در شب بازی برزیل و اسکاتلند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/persiana_Soccer/24280" target="_blank">📅 14:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24279">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s-5rGw3pXCX_hyYuvBMRGzgicTsx-sTaLzMAWGh4vJOK28OX6yhWyNWG0C28OjQSQHw_Soi0qq5lXHKRgHVOf2KoorebdAtb3iYUtXoCnKmMcHUS2unOtNbd3D7cq3S2GCulz477lxkz22EaVFdqV6zt6pVjb6n6BmpsV9PjowMd29LcNR44DURQBTiYRTtfzJ5RlfZreQlCaQK61Jwi6MIhlYVdbH2om3WL_yoozaZSy_O9DeoR8_q7eWodJMUsCHWK4DTmM1q4C1VLlfkpORQulG2TJQmwE-2b4GSDDhsKwiINuiWZnB0WxsF4kQA1DfRAUB3hnbCUJWxcUlVQ7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🏆
جدول‌گروهA رقابت‌های جام‌جهانی در پایان مرحله‌گروهی؛مکزیک‌با 9 امتیاز مقتدرانه صعود کرد. آفریقای جنوبی نیز با شکست دادن کره دوم شد و کره نیز احتمالا بعنوان تیم سوم صعود میکنه اما قرعش سخت خواهد بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/24279" target="_blank">📅 13:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24277">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QyokP_Jsm6lahdKA6-i0p3Ca2ErjpMEoAQ5g0jLmGYN5E-__VSYHsKTekBZipvY0QUcAtYTmb-5vn9A7azwYTJe-JsAWJ5_jweNjFVK857bHAOarF7mzOv9BuZJMwPJPaA4VrEpKXGmBLlgsAcnUAbwiBeu_alkcbRKjjSMDvEHQbCAFFQxync1mYtXDajWuAF2Lj0jVZn2ccYFhynojzjZJduu3c2HkDGarZ4ASq37AKGynphD_mY0VphqevJIv_uLSxuVnXsaaxSDqpJ2jV-YEYJrTkjzd-wxPd7trkaLjm1et7nmXrvAy5ic7kxgGEI2UU6Q6SkIhtyKmWWD_hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ فیفا امروز صبح به فدراسیون‌ فوتبال اعلام کرده در بازی هفته سوم مقابل تیم ملی مصر؛ شاگردان قلعه نویی باید با بازوبند رنگین کمانی که نشونه حمایت‌از همجنسگراهاست‌واردزمین شوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/persiana_Soccer/24277" target="_blank">📅 13:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24276">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=ZPm3X78XbGpWLdmHShLGOXa-fLhgXqOJgYLljs8qxKZnpqNBaNJj39LoZNnu7IOu4ON27iOmYEy8GJ-J9RekQXLPIYfeSmH_X0QCVEGdScJwh8TdfgvVAVC4Y0am2hdFe2ve5Er9IJRM8X-ebQUr58R_vKSeXz4ZQ3gLSBO8fK6NAZsQWmSqL4uiY1jdhmJq25svJAZn0w1NS9epq4NoBq2LDO8_vShz63V5OWMSDluX-nXXKxXCTpLUxQpDmaLIJrS8_rnxXfVYwCO6bEuGQApEDePbtGm-zx0qCNub6I4wmKSPe4oDv6iByRPu2wsmjb062dG06s95SkSZOGNdBXFZCDhtD-8Fw8-Xmp4kfMtdlCMrQChF1KKLV7_72hkYYwx2ZsJ2sPPsdGAWbLz9kQ3P8T5z-mX8MQOjLa6aOY0KRhRa3aQ_xIwnS0Ad01MmYc6ZC5HYfCFb-cFv9rEm4VO-wClR6TrlPD84r7nqMu3eaeSVxIK-E6rf7fkEc2MnneB2KEdB5RzrTRGXtLzHYypUqHfpl1cFZnpJqXVFVv_FY_bsyMs-VA9nKyC2LBqd03TUuc6Eh_IJ7e1yGqBWTT1UR57KfQPHjsepdkvUONyS3blvJy6SxHu9TAg0rXZ5U8tux1XhcMcltR-x4f_c4MZ_77k5m4lTKT9WnHbNEZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c0f79258f.mp4?token=ZPm3X78XbGpWLdmHShLGOXa-fLhgXqOJgYLljs8qxKZnpqNBaNJj39LoZNnu7IOu4ON27iOmYEy8GJ-J9RekQXLPIYfeSmH_X0QCVEGdScJwh8TdfgvVAVC4Y0am2hdFe2ve5Er9IJRM8X-ebQUr58R_vKSeXz4ZQ3gLSBO8fK6NAZsQWmSqL4uiY1jdhmJq25svJAZn0w1NS9epq4NoBq2LDO8_vShz63V5OWMSDluX-nXXKxXCTpLUxQpDmaLIJrS8_rnxXfVYwCO6bEuGQApEDePbtGm-zx0qCNub6I4wmKSPe4oDv6iByRPu2wsmjb062dG06s95SkSZOGNdBXFZCDhtD-8Fw8-Xmp4kfMtdlCMrQChF1KKLV7_72hkYYwx2ZsJ2sPPsdGAWbLz9kQ3P8T5z-mX8MQOjLa6aOY0KRhRa3aQ_xIwnS0Ad01MmYc6ZC5HYfCFb-cFv9rEm4VO-wClR6TrlPD84r7nqMu3eaeSVxIK-E6rf7fkEc2MnneB2KEdB5RzrTRGXtLzHYypUqHfpl1cFZnpJqXVFVv_FY_bsyMs-VA9nKyC2LBqd03TUuc6Eh_IJ7e1yGqBWTT1UR57KfQPHjsepdkvUONyS3blvJy6SxHu9TAg0rXZ5U8tux1XhcMcltR-x4f_c4MZ_77k5m4lTKT9WnHbNEZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شکیرا به پسرش میلان میگه قهرمان‌های جام جهانی رو بگو اونم شروع میکنه همه رو میگه بجز قهرمان سال ۲۰۱۰ که باباش با اسپانیا قهرمان شده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/persiana_Soccer/24276" target="_blank">📅 13:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24275">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VtrY2GgLOE0lJlwSKExxvQ0T6WTN3JEBjXEJ9MkOIuxhUM0G0qnilcStB1hwIbbux2GL-Z8D107J7DRs8KZoxijS_k3Gt-3xOCviep2FLZEpetU34YB-MWaRhFOxQ5LQbUwztWR0woUwI5eXS5aWaybyl3-XONpb3_ig95bPANcj1kAlTmnXPQRu0DGXm6c6a8xpzMJRVYYCPQHk1H_w3B0Gu5NOtFyXtbhyiMUMTeu2AcEBSK-V2BqJXoXv0s3v8URAv-HQfi4iTfmzfOsL-9dnad57a952EmocBa6P2QuRPCdQ9c3_ImuSX4bahrBF4BFI7B_LjKICUcklVC1HtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
باشگاه اتلتیکو مادرید: ما خولیان آلوارز رو زیر500 میلیون یورو به بارسا نمیدیم. آلوارز زجه هم بزنه زیر این‌قیمت‌فروشی‌نیست. رومانو هم گفته مطمئنم 150 میلیون‌یورو بهشون بدن درجا رضایت نامه خولیان الوارز رو برای بارسا صادر میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24275" target="_blank">📅 12:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24274">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkCmaOhw8S5kCW4WjTayEM_da_EUkIZWEUqn0PJajSRcUeSe1O3ZtTaVL_b25WmlZNxGVnIh69D4d6HKdIu1Y5bJTX-U7IrHLxDRf6s91_p-Sz4107n5gSXRLtLJbtpbY88beFUALuGdbCOhYA-cjXM_6ut_2ui_Llpiy4RDTBWjkVXy9GR76ydlM1mnZK9c05qooIwpPB7Qc7y3L5AVIvZ2d4oxzSMXoCCTjLL1j8F5PRLPa1bfAnWoSabBP7nZAr7GuLVRRG-Shl4E-QLvpYG0b9IXZjkzvw26iLSOkDT9YrOSTRe5MGe_Qz4a3Zx--i47A5fo39bD-xfSLSyAniPM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06bbac815c.mp4?token=PDjEB4ieHjPs7iR57NU21H3Irq6QENoyW0M7vcd1Rp171ejO8l5BAvoJQaCyXOFTSt7h3-XAuICc1ckY6R2OPm8i6GqxOYeMMpd9XO5lH_EodSFk-6Ni2DiM3xdp7ECesmh_F3_zOde67-DIGMQuXgvkoo_042OlFrEDBcsHdVBjaBFp4VjjqMhfb6RiIitVHGg-eSRYtWg2WAOxl3PZol2JJIIsacZkY0JVInqEKy6X9LMBPKqLq5rcwY2v3qD4aHHKvEgqUfRWkkHzYe53YojbLmZiXphZcjYNV6pd7BcT9OWHRgaYbk59oZuRAWZ-wytAWwBJjkyiaJs7wPgLkCmaOhw8S5kCW4WjTayEM_da_EUkIZWEUqn0PJajSRcUeSe1O3ZtTaVL_b25WmlZNxGVnIh69D4d6HKdIu1Y5bJTX-U7IrHLxDRf6s91_p-Sz4107n5gSXRLtLJbtpbY88beFUALuGdbCOhYA-cjXM_6ut_2ui_Llpiy4RDTBWjkVXy9GR76ydlM1mnZK9c05qooIwpPB7Qc7y3L5AVIvZ2d4oxzSMXoCCTjLL1j8F5PRLPa1bfAnWoSabBP7nZAr7GuLVRRG-Shl4E-QLvpYG0b9IXZjkzvw26iLSOkDT9YrOSTRe5MGe_Qz4a3Zx--i47A5fo39bD-xfSLSyAniPM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/persiana_Soccer/24274" target="_blank">📅 12:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24273">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=CHCPyl2eX7UObo8GMtRvodKjwq0X7jjji6Yg-2RrNjUFyYLELY_rNrtP_b93rJ88yumqGibUqZJv85E1yOAwsqUoDuBiq1oRqFtvN1lCodIVEhSGvoIn91zWzTkpehdd-PCL-sccLwFxA8-OijeAypLVAjpn-MIC3gGL6mP1RSYo8T9QTAispwAQcdLaOHJvS6Ad_7ITufVbYYnpNzdtTwOsQn6FBnT2sUGvgAUvhKAmo2y6rHsxkgf92RPvvIlT5idPvzeCmbKb9fQE8kll1TCjSO4lUFQEN61XH4stP1-vUSG-6682B8AKPAJz-nGcP99yYhbJjy5bQXkGWqAPrw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/edc9cbc45e.mp4?token=CHCPyl2eX7UObo8GMtRvodKjwq0X7jjji6Yg-2RrNjUFyYLELY_rNrtP_b93rJ88yumqGibUqZJv85E1yOAwsqUoDuBiq1oRqFtvN1lCodIVEhSGvoIn91zWzTkpehdd-PCL-sccLwFxA8-OijeAypLVAjpn-MIC3gGL6mP1RSYo8T9QTAispwAQcdLaOHJvS6Ad_7ITufVbYYnpNzdtTwOsQn6FBnT2sUGvgAUvhKAmo2y6rHsxkgf92RPvvIlT5idPvzeCmbKb9fQE8kll1TCjSO4lUFQEN61XH4stP1-vUSG-6682B8AKPAJz-nGcP99yYhbJjy5bQXkGWqAPrw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه استقلال قصدداره که500هزاردلار به نازون پرداخت کنه و قراردادش رو دو طرفه توافقی فسخ کنه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24273" target="_blank">📅 12:25 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24272">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oHPYLrpmmB0xUx40WLvBzbT35SwKX9RYZ-i9TlfSUCZz8rccBHEFUcC5OYtBj_YVjXVmSledIYcAbXSBBAKH-xB7e7f0SPKTaciorjlZ-U0qKdQBsVRw_aHT0aR4fn1JjfHvv1bvPruFLdS-cc8IxYu0cP0vPekrigmyju3mQzuThiHzh5Wzz4GZSJNLGWedOSd0IW0JVnYl-NwRthx3wjdmE7q1T40EzELqD1Ze-t0QglpMn7mMeAWprgBZlp08nHlEBM5FNk2M4QUako9_ylNmyk1z8MFdwfvBrmXrrDngYao5HmNzSaqeiPxZ0B5RgpY855HPwmcRWkxM0qURUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
تعدادفالورهای وزینیا دروازه‌بان تیم‌کیپ ورد در کمتر از یک هفته از 50 هزار به 15.5 میلیون رسید. تعداد فالورهاش از 8 تاازبهترین بازیکنان حال حاضر فوتبال جهان بیشتر شد. عکس رو باز کنید ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/persiana_Soccer/24272" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24271">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QCEr29-SMLEnpPebMhVMH5UKOAsMIVXVhVrX4gX3qfvdRvhwSgmeFW4ux6LNEeBI7_DjAhCgkzYaMNuG_bssw47wEXydpruxrwAsuB3FAdfD1iCS7QiIDQchwf4AV0seZhi9pbUVMpE44nV-Ztx_yqU-ir6xqgG3bg515vz3gGW6HQPh3M4T6uTJ69PNavZBG5ku5OndTIWp7tmwh6uSGi7729-HZzMXi_xYGpVB1ClqdK6MfmUzQ2s0JWjBPWaFqpnQSfHJ4ge85IIqFVf3n4Fav2nr8_HgaDBV6ggMxyLMW8KPci1tmAokewyEOvOoAUheWMFCo72MUE2r0DmAYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
گل‌ های دیدار امشب دو تیم برزیل
🆚
مراکش و دیدار دوتیم‌مراکش
🆚
هائیتی در هفته سوم جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.5K · <a href="https://t.me/persiana_Soccer/24271" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24270">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">⚠️
خیلیا نمیدونن که اگه ثبت‌نامشون رو با لینک زیر انجام بدن...
⁉️
💥
بونوس خوش‌آمد گویی تا %220 بیشتر میگیرن!
فقط کافیه به لینک زیر مراجعه کنید و وارد ملبت بشید و به راحتی ثبتنام کنید!
👌
🌐
لینک بدون فیلتر سایت معتبر ملبت
👇
🌐
www.MelBet1.com
🎁
بعد از ثبتنام، وارد حسابت شو و توی بخش "بونوس‌ها" فعالش کن
🎚️
نکته:
فقط این هفته فعاله، پس از دستش نده
🙂
🎁
کد هدیه 100 دلاری فراموش نشه:
Sport100
✅
معرفی سایت و اپلیکیشن مل‌بت
💯
ورود به سایت مل‌بت (فیلترشکن خاموش)</div>
<div class="tg-footer">👁️ 33.9K · <a href="https://t.me/persiana_Soccer/24270" target="_blank">📅 12:06 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24269">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m5vlmjYi2XK8HvjDyui8carsJo6JDtwyGT_njQBKOeII2U7fl9IY3Rvene0g2PpqNJ4s53KOEo1ArvaEcMQjuP9XRs_97QTddIgSM8il47yM5bY-X5SynmW7xLGMZ9LHCGkyGrD-EJWvcI3zH7xK39uiuusVvzJXuySD3KSSJFAFbdsUedtp3WMq3d15pNMTs88qQqh_w9jSN1Gr_C86ES1I-zf_VJSZzL21VpE-q_vOto2iOFhu5EtGvWdgKd5SRsdm0cHSy3j53CrV1F1L16TJvGCjbmTACaIihofXemjk9BvXaYbsyyodrmPiR3L8Q5TRZLhvFzXoZ70Oy2-TKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/persiana_Soccer/24269" target="_blank">📅 11:41 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24267">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dxd0AaDHdeMEWisGtGlfRWdbHtVnj3APFh58L9Y4wLkibpOR0E0bZwxTFHOReyrlwCys1RbydASl47XzJ0mw1F3CWVeXTCB7G4pSFZAa7NJghD5ILdryem9mQot8N5cTgl3BR5ZpOtOoN0s_G9-DGXVMt-6M_QjscW83Lv4Qkn0juxgySaRTqNVuSgeio-GJemJHfRAgfqGpAwy4tNiWFwNJWPcXG8s1d_2l8kAwiCxa9ojftl1GMksQRGl-MU-hqZfbhNtVzEfyJSdk_NXD273zn0IYZglosluZAubt8oZjnMdMJcOmlADK8rFn2h3jUm8HlOBXCK5CkuEcW33Awg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KdTagD3sxbAeLc6UKGfqxGghZ3rPBP4Pws2BT0L5XKtLoYY7IEXZ0NmBxrgiLDZqJII7H2oU0WvhUpyeueBjQ9JbIdyhJWaaqvlzj05CBD4hhS1ssiAlMVzu90yGlMffOB9FsvXPI9Gy9wRuFv-FrA1s4k5lAa6doWQ3S0I7ycCKUnFGGMXdZTpsW_gvU0wpWr9o6SLDkvf_ooQK5dCMvJfeGas_tHVjvi7zSMVt8Ec-IHSz2eQEFntYbKsOE_H28WN_ek_9qD13yhtMeBtSflIkK6QVOcMzC_wR8gkzblfdRneD1QdSUJEMHvMXPflJuHztq04nRBzXdOwKdpj1ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/persiana_Soccer/24267" target="_blank">📅 11:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24266">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r3cMPRDUrv8xDN3rsPnGLDVQE094vuRynzhCL48YT-n6x4V82-09l4zGUSO1gT4V0w-jLx7m6IqayoIt_Qe3nk3cEiT6HK1kn0YTDYtlCA8m3-8HQsmAHCAJ3fhz_mM4xAvbz_R_Vf6hdPunCwFaswBbC_uH6dDaxf09HX7fCkvIjQ_P0dkXKqDDLeQRry9VM5X6XUzwib39SAprJ6nCZtXNnvxE-TwPHUV1LrmEYdn5TndCIRYFdnSJP_09M-wRWohBgD3xFrVJG48vOfQVk09yOkY9xqUwrKQvR30ti3lAsgj8GDxMHXBR-eArRIuBPFftGcUVZmDFmSjLlR3wBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
نیمار جونیور در بازی امشب مقابل اسکاتلند بعداز 981 یک‌روز برای‌تیم‌ملی‌برزیل به میدان رفت و دقایقی تاثیر گذار در زمین حضور داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/24266" target="_blank">📅 11:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24265">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=AAnnWWarpZreS6t1xkjux2dXZDExXbHmaCwuhh8ptEKUoDd3tejiOctEeDHkUdh2daSMhnrt48ti5nM9K1WWBuLGYjvAzmHMLqqMYe4Z0WhHN_HEbVGvN7O5BiebzCwuf60hlrqryqEGIxhRJx_4jT3dTM5WxS14h5DKE3QziQW5qg65TGGM0rofsF9D6550zQC6MOrwArCQ3nlewFau26mzNg7seVibop0Y0bZhBHtdfaFTQ5u4i3kl6OH_JvFgp48jNE1FI4Bhipb4M8gpoLcyvA8ODlDO5kTvCiVN80aOZNmds1oF6O-_WWMEzXOJF59180puxX-5PAhxaTSjkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07d25b9dc0.mp4?token=AAnnWWarpZreS6t1xkjux2dXZDExXbHmaCwuhh8ptEKUoDd3tejiOctEeDHkUdh2daSMhnrt48ti5nM9K1WWBuLGYjvAzmHMLqqMYe4Z0WhHN_HEbVGvN7O5BiebzCwuf60hlrqryqEGIxhRJx_4jT3dTM5WxS14h5DKE3QziQW5qg65TGGM0rofsF9D6550zQC6MOrwArCQ3nlewFau26mzNg7seVibop0Y0bZhBHtdfaFTQ5u4i3kl6OH_JvFgp48jNE1FI4Bhipb4M8gpoLcyvA8ODlDO5kTvCiVN80aOZNmds1oF6O-_WWMEzXOJF59180puxX-5PAhxaTSjkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24265" target="_blank">📅 03:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24264">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🏆
جدول‌گروه C جام‌جهانی 2026 در پایان مرحله گروهی؛ برزیل بادرخشش‌وینی سه بر صفر اسکاتلند روشکست‌داد؛ مراکشم چهار بر دو هائیتی رو برد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24264" target="_blank">📅 03:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24263">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CNgubZPLOyqo8_G64h9XHsE4F-xHcJYifurOd5B_UxiCbkg9Zcr-fpepDNR19Fjhulx4I5j_aIZJHJCKvXnpVMpRATwuHz7R49BZMYbQ3O-O89OmiRKz74G9W5zOiv8z1sB190L3kukrrvRuHUK2OWjZoAlZhNt0Hc4eclmlroN4owSywJJ7T6UU1GtbggqukwHWaypkqJSPFc2u-hRmw1iGo3VbZm86Oi8Q_sPfQUjNjnLlm9joODDQPnLkAhKGcf1SwJcUpOxcVeXvMFMuq9ueQXKMGmLZ_KUvEkD9dZ4dGoT36XsCyia9D39Kxxyb1LDlDpq9jfN8TqRYLTX3nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدول‌گروهB درپایان‌مرحله‌گروهی جام جهانی؛ سوئیس، کانادا و بوسنی راهی مرحله بعدی شدند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24263" target="_blank">📅 03:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24261">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cI8PieXAgXWL4mnuzoJF-32VlF7IU_4s_SnRD0IU-QYK2BEsdhhaYJudkiyv4GRWLnKGVPCHmXwlmOKgZn7V4n4yMa-lLJ2DC-JsSbZV-RsNklTLYAHqZCBqO8DuOs6GxeQ2N7MkaJObHbi-_i17z21xBkvfxyx7fosqeuMpQjiWP5CHndov-FI6fe9MOUNjpdoZB0AG1yd0P7MT6_4yT8kuOdfK5IgkIIel7Ikk_SMDqEsU3HxyEG86-08o3c83ZJS4f38x3q4IEGsbKCMjt-H6hkeeMcVenS1IMRKmNxA__dXVqPqtX-vdgHRGxp6J4ZIWTRfnUS2O-BQ6jeTCAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=JxvuOsY4G-eH_yAqlE0L37Eb3p73_R-ibUYIGUmzCpknwRc31WwGKHEUlThi5h5lw5uf0ADsLsqsg8L3OPcF9_8NcigJVyfHYfsoXInE9Avdk_-Xh-VmkG7mpoPqtLvb8o6Oq94_cqW-D0aceMszHtaXb6DDxUDy-uLLGcgPSjz26xlpIUgKw109Hu5vlQYK87Li_DPXpWItYo2x6x4X1LUDUjj6l2E5Y9FJEWTORWHp9B_DwbcJAVHE9EEcjkVmywJgOqoSNY2pmVSzPtuC84wVF7yUIUal-FE5RYrqYS5JHNZNPRM7MkLt_9oXI8IWiAsSshEu2DZ5e15i6LgzdDVDjjS3zIx-Sly4myXqJmq2FMz1kfZ4AaJ1Llr74dUCtOMDPmQFdpwIqSp5ql78m3wMN-cOA1AtVRxx48Gn3-fxNaRS5bliPcvY-NbXD8-vahLWz_5EV-UQQB2cO_LGR2AXWS8cni8tLwjlJZzPKxiYW1AB6Ld0aDgw5FFrzZogrKA87lKXv_pLByYczMnW7B5LgemwI2r0bVwMKOiAjf062AX4TK6XshYFl_-JhhkzTKotPJDg-Vbr_qBtvRZ4QTXjK5es3Fg1IarC0lP3RRzlaHDmEyvYhAgayOIO5ajUjxA_0-wK4Sns7BXWrjQFvEP-IKwJXwc0s3DXPaR1gcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a6d46fb08.mp4?token=JxvuOsY4G-eH_yAqlE0L37Eb3p73_R-ibUYIGUmzCpknwRc31WwGKHEUlThi5h5lw5uf0ADsLsqsg8L3OPcF9_8NcigJVyfHYfsoXInE9Avdk_-Xh-VmkG7mpoPqtLvb8o6Oq94_cqW-D0aceMszHtaXb6DDxUDy-uLLGcgPSjz26xlpIUgKw109Hu5vlQYK87Li_DPXpWItYo2x6x4X1LUDUjj6l2E5Y9FJEWTORWHp9B_DwbcJAVHE9EEcjkVmywJgOqoSNY2pmVSzPtuC84wVF7yUIUal-FE5RYrqYS5JHNZNPRM7MkLt_9oXI8IWiAsSshEu2DZ5e15i6LgzdDVDjjS3zIx-Sly4myXqJmq2FMz1kfZ4AaJ1Llr74dUCtOMDPmQFdpwIqSp5ql78m3wMN-cOA1AtVRxx48Gn3-fxNaRS5bliPcvY-NbXD8-vahLWz_5EV-UQQB2cO_LGR2AXWS8cni8tLwjlJZzPKxiYW1AB6Ld0aDgw5FFrzZogrKA87lKXv_pLByYczMnW7B5LgemwI2r0bVwMKOiAjf062AX4TK6XshYFl_-JhhkzTKotPJDg-Vbr_qBtvRZ4QTXjK5es3Fg1IarC0lP3RRzlaHDmEyvYhAgayOIO5ajUjxA_0-wK4Sns7BXWrjQFvEP-IKwJXwc0s3DXPaR1gcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇧🇷
یک پیش‌گویی عجیب و آخرالزمانی از یک پیشگوی برزیلی بنام «وو باهیانا» در فضای مجازی جنجال به پاکرده‌است؛ او با گریه و زاری مدعی شده که در جریان بازی برزیل و اسکاتلند در ورزشگاه هارد راک میامی، دو سفینه فضایی به استادیوم حمله خواهند کرد و در دقیقه ۳۸ نیمه دوم، یکی از این یوفوها اختصاصاً
نیمار
را با خود می‌برد، در حالی که سفینه بزرگ‌تر هزاران نفر از بازیکنان و تماشاگران دیگر را می‌رباید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24261" target="_blank">📅 01:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24260">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=s9KhQZFNwxadGl1Wj6Y0RlwJagJ5LD1tm2nUsYtLPhGPQMo5wMW5kw7VGSK_pxDSld4OnYyh3fV_Xd3xxA91iumLhn11gZ6U4_OXuv1oKLH9DvafkrJeXS82heaW6lOS1RXX_opUorGp8mHa-QcPlyu2y-YxWG5Xxmz26VNp9IX2uYKSZPUg6GeyBZfj4mwKiRbWB5Gs8y3z02jy70aTo8TRZtIA0Q8OoCyYasGdlh60ecQjqxERbfKUgDUmEQkdl5kdIbx0itrL07IYVrC4BNyoyQJuvKdTd1vCMKziKqDaU40vumA8rXlMxgIcpbX2tJuNec5Dw5Qw9APlpPFRYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed8236df4e.mp4?token=s9KhQZFNwxadGl1Wj6Y0RlwJagJ5LD1tm2nUsYtLPhGPQMo5wMW5kw7VGSK_pxDSld4OnYyh3fV_Xd3xxA91iumLhn11gZ6U4_OXuv1oKLH9DvafkrJeXS82heaW6lOS1RXX_opUorGp8mHa-QcPlyu2y-YxWG5Xxmz26VNp9IX2uYKSZPUg6GeyBZfj4mwKiRbWB5Gs8y3z02jy70aTo8TRZtIA0Q8OoCyYasGdlh60ecQjqxERbfKUgDUmEQkdl5kdIbx0itrL07IYVrC4BNyoyQJuvKdTd1vCMKziKqDaU40vumA8rXlMxgIcpbX2tJuNec5Dw5Qw9APlpPFRYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام رسمی فرهنگستان لغت فارسی:
آب درنگ جایگزین فارسی کلمه hydration break شد!
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24260" target="_blank">📅 01:23 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24257">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAqxVhi-xhVLwL-_114Gj1euJBYbZnBC-mV87Xl6gGIiFRn_MLP9I_qV2JFOHgyLor0k6GnqZCvbANHceHrQJgfHnpCYsY9kcuIfFuT8SGEKLlSmdpXjasx6UXVNkOD6IkqeRpMsZd_0Z3vNiJF5z-FYHfZW3e0_9M1I_TyVvure0H1s4CED8RfN5zV4ciRmNN6c7p8wlMVhqlVPhb9XL20SNgzZ6P0vj1Lg35eoAl3evXqqysrE90Q5fMWkFRjWttk7Tad9_crrVBkQV3XVIavO_w4cM6ASPQ6K-5rEiCGH7BjiCZR9QqkuhE-c0v2bzZ7Q44c1u1TuA5f6WbqRGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارهای‌‌امروز؛
از تقابل حساس سلسائو با یاران اسکات مک‌تامینی تا جدال ژرمن‌ها با اکوادور
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24257" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24256">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VxRp3WBTu1-XYmH1bzf9gbp5j_dJecfpLkrqYFtvmPBd-3S7bKJAZZ2ZjHajJwIfWWafNpS0SXLLL7YSrIMlwaYpPzY42WGu77TzPeKkcseNfnRJjK7czj3ygauXxZw_aaYrTH4azRKNiWqmPpFAlZw3zCMJOn-YcPXpLa4-y_S6qViqa1PmCmqam-ybsl3g_E-THKL6Qi2rpdDuMjsfUgdeS6spyXsU0QVjIvQmzI2tSLo5RRq5vVQ_T6ysAdVFeD5j1kT63NTHtJ6rCjoJITNGwSxDDoeMr_OOfE3xlRz25tzgVRwxYybKpIBsPAZhD01J-m82GYkiyUrvlZYxJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبرتری‌یاران لوکا مودریچ برابر پاناما تا صعودچهار تیم کلمبیا، سوئیس، کانادا و بوسنی به دور حذفی رقابت های جام جهانی 2026.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24256" target="_blank">📅 01:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24254">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j3XmJK4-6LIa9G_vVwAVIT67vm782_TP_Avwe9a8UBLfeO-opO8KFYJHGKBNgu7SAImhhCFG4aR3N4WlB0JNiPtM2td71VfRlzSEhdYUUM89IqJq8H_vor79_XAiOO_e-rOIJNR1KqbrprGF0935qErEPRowWfGNncZGmVy7BUjUFBsB4E1NfuN5Q8-GWPvRd9FLlVxMyrwvPwW47hUzQeRPlfImvVhKDEtf0SWFVWvATNJdeOxskXxdj1CPHxuoxWBtaaIJQhNbYlbON_WHrsWJ3MNBlIsUlJh3Mmgan9N5ByROfwIZM-cn91AXqZgHFpSvIRU7EG-eop1dvkxlQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FjoJIUvfCV2fx35wN_xv7-zrvUSuutZ5xT2sps_EpimRxBSD2PDmHtzuS7h8mgCtU1TqZ6syfyNMqLQTj9TBtoxq69eDf9YQirppEdkA_v69UnDlYeV0HbLInHTXHLKa5Ord-UfWtPmM4jAaRjHgfOrLpAi6nFyRUWHO3pleso25ez2sAklTdqwa-tTTNoSUGJE8MfPxiQrvorhn-7HTo6Fl-8aURXAk8DVr8P_xtU8fs47UTomcJ-EZ6JrLVUkV0qP5k-ghYcg8Pz3qOfu5NbafVXGRZkZT7LAHmJ1yuzWwD1GOmswftsxNPBZehcngGyCTflmGcvvTEM4yS-XV_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
همسر گابریل مارتینی ستاره تیم ملی برزیل که آماده دیدار امشب مقابل اسکاتلنده. جالبههه بدونید که همسر مارتینی پزشکان زنان است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24254" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24253">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwAx6xnhLN0LVN2If3HVKjrqIvzdKaOm6Nn-XCQa2GvSQy_82QGgR9iidCnvumC5m7hb2PYZ1u_YDOn_A7SPrUirI0eeBbEmOsxTTqRz8mCV06MpxeaETIKvBVt_UUf-yFfHMCLdjUf-8zjUPrUbMq4h3Sl7yRJDz5hae1t_5t6Zvxx7j9r7RUX6vDLCikKuTG5ISr-25Zc2bsiv8ya5F-F_QRck20X62Vaq5Q-sO6GBt9ocl3XR2PQZ3BTtepwcFkp-r6SXaw7Qb14gPKTwAUyBYSuCA_gG9GiqN2PWJKW0fzcz0dylrUd_AP8xTG8tgQBCf83rf0rN52BdRWcKBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ توافق نهایی حسینی با استقلال، رونمایی بعد از آزاد شدن!
🔵
همانطور که درروزهای‌اخیر نیز خبر داده بودیم؛ مدیریت‌ باشگاه‌ استقلال‌ شب‌ گذشته پیشنهاد مالی خودرا برای عقدقراردادی دو ساله به مجید حسینی مدافع 29 ساله تیم کایسری داده و حسینی…</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24253" target="_blank">📅 01:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24251">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzMVAhBpZPJ57xeKgFOCuprjR95daBbv2X9CFFw2snlsguGPFvBWAUMkXWsEdUAxbp6q1cvh6zbfv2MmhLhzrZIVIh5ePGkYDY-3hxP6lPJ5Y2gIvTkVJ76FuPRykTzmvLLBmmYTr-1hsfx1__ugjWU2PgnOO86AJFCpDPqaE7k8EM0jlLeo9w1UmmhgNOINbLiNTLRGvLFVQ1ZHYmG4uSdjj2M7SutD-XN5AfgN44TN3WBSrcr53PdewpzH7cxSfyBIeOfZ4AGTyxk5EmewHpgsZaDL4l6YsA-_hk-sJ6MvfcUBCGz1W5Y2Kt9wooLBG8l2V1ejkyPUH-dxu43xmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
هفته‌دوم لیگ ملت‌های والیبال؛ ترکیب تیم ملی برای دیدار با فرانسه؛ ساعت 22:00 از پرشیانا سه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/24251" target="_blank">📅 00:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24250">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSJoacyYojNFhvFQxq2Djs084GLCTDUVYQ5mbeHCaaffheZh66pCiCkU801z55tFc9L9c9e-TbiemXB98R_KRmMXib7fxMq42PxPTtYwlnThQGAwcc0rPP0-Mxv3F6Gx0eOA5O_26uht-xA4SndZiQvlWoA-4iWgksAmxzAnDfAAA8vWFHl3GmFUQx2ht1o_xVy5jQs3GYvkSDU4bSTI_FIJGHkdt87jTx5Zmx01B4qw67TbgyeCJ3jGWGbTFIVHCbF2Fg1B-5CSof0sjmtGsRC1b067gOW40t41BDafvKQ7Ir6VcVonCEQvhr2fAMfZMLlXaliBisLZ4zmMIl5msQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هفته‌سوم‌جام‌جهانی2026؛ شماتیک‌ترکیب تیم ملی برزیل برای‌دیدارمقابل اسکاتلند؛ ساعت 01:30
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24250" target="_blank">📅 00:42 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24249">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FO-uqXMidAkP9vYMOG9UH2uN7xFGzNZviEDIsKlFqbEo3b1LDStv6Q2NdA-Rgqij8pDK4hLQgfdwkI76dmHg-n8pRmuwvIE1D4dj_pEMTee-4wAthgtKcbCtqsb6BmAdOkj_qIswVraijxvc5xdw4V33CmdPWuqi_fJKogmBa9ElMFmn1HqIzE3mhLB6NDe8LfCE8ontI1u9mUTqU0hQ9lFMg1gAJEtNRQSA0_0DgtvbmBzR2rl7gfrz15FZtUO-p_6YMBnvcEtW34mSYm6oIaUilOx9kQhuqGyBgDxomICcIwLAc6y4MYbGvZR_B9JZQhn--RHsAdgjaKsvhss1Iw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24249" target="_blank">📅 00:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24248">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=t8KmGFVPb5JqjpxRWY9z1NxDWyMMD1BJjJPfOAVEW0rC2FpTgJx7cu8LPgqDWBxlQhITfXlpUYmM0Lmfd516FyGsFadYykAOvLd1aMT3cVY8VoOM_5NLqK8hgpl2Y0TCLO6Bfl0THBVLYevjssJva2RYpwusj3Z-WjQefhnWUAsxgk12t7cYaSB14wXpHBY-OxmmUOSXxMFkiaGxOUyxgJ_Q_5r4SMwSTxtgqAW_qEvvbSYIaZNFUHZJpM9w-doE-YtWqR153_Ac3zvQ5elH6f7G44K3rP7M2fTyK-HS-epHwbMy4vEF80P3mWjDwVgXXM5IOS_f45Mc1YfFNJMTTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81b3f9aaf4.mp4?token=t8KmGFVPb5JqjpxRWY9z1NxDWyMMD1BJjJPfOAVEW0rC2FpTgJx7cu8LPgqDWBxlQhITfXlpUYmM0Lmfd516FyGsFadYykAOvLd1aMT3cVY8VoOM_5NLqK8hgpl2Y0TCLO6Bfl0THBVLYevjssJva2RYpwusj3Z-WjQefhnWUAsxgk12t7cYaSB14wXpHBY-OxmmUOSXxMFkiaGxOUyxgJ_Q_5r4SMwSTxtgqAW_qEvvbSYIaZNFUHZJpM9w-doE-YtWqR153_Ac3zvQ5elH6f7G44K3rP7M2fTyK-HS-epHwbMy4vEF80P3mWjDwVgXXM5IOS_f45Mc1YfFNJMTTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏میگویند کیروش باعث‌شد فوتبال‌ما تدافعی شود. مگر قبل از کیروش فوتبال ایران چه آش دهن‌ سوزی بود که نگران دفاعی‌ شدنش هستید ؟ تیمی که حتی دو دوره متوالی نمی‌توانست به جام جهانی برود و در گروهی مقدماتی‌جام‌جهانی ۲۰۱۰ پایین‌تراز کره شمالی و عربستان قرارداشت…</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24248" target="_blank">📅 00:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24247">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/po0N8SYrs3Zx2uuiD3B_NKmRAP9pgAP4XoQDiXE0prUrSKKCS7tWWDXwByx0oE8IW1L2Pq7Ep4EUEmpKD1fISxI3w2nNOMjZ_OS1IgRTt77vJEis3MZDZE6bldkad4eALuH6xMe989D3CpDqtAJ8oCP7IBmAkWLQGbHS3UAKAYc0gWSOar_PRbYtdQa9QFcPB0-ieewEF3wxKSvBOI9NI9J8QUdjalGmeJK_kTceIaoqR3B0tyZtjnhOh81_zL3wWYFyZHAfkn9DiQQPCFAMBQ37dzf6s3NLN9UbQifVG389tMpmVwBnwSPzXiQ-8JNcZGhH5d8xRYkm8mTxPn4btg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ با اعلام کادرپزشکی تیم ملی برزیل؛ نیمار جونیور از هفته سوم جام جهانی میتونه برای سلسائو به میدان بره و مقابل اسکاتلند بازی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24247" target="_blank">📅 00:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24246">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xd0prh6vQu6XzsSfY2VgMzs1VuUxVqRsN4x37-UwKoAkZ_UdOkgMuIL4vvJDG3jz4Zj5PMWtvKuZZ2ZA6strUlGHZ1xiTxTmgC3RD1_zah_6CHBr6PF-yMCFg7oGdWdpFC2GgZRoNbp3SkM6fvBFeX5dQ6NYMp7H4X2ySaFJntMgxNcsh7ONw3oyr-q2zp-Dk_opeDxEpG8plB9E1el3rd1I7f1k7f2FBdkUWnTOz_ohHOuokJHt6dqjVlw2-DMycDbKgMXs_wSz6rnndi9kHKmEe54HD5xECcZBbLvFoxWA24Fbfkc73TDemhhvcjbMLTqdVQV0OZD0dNckqghmQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇬🇭
#تکمیلی؛ عملکرد کارلوس کی‌روش در تیم‌ ملی غنا؛ پیش‌ازجام‌جهانی‌تموم بازی‌های دوستانه رو واگذارکرده‌بود امادرجام‌جهانی و درگروهی‌که دو ابر قدرت فوتبال‌اروپا توش حضور دارند دو کلین شیت کرده و باچهار امتیاز در صدرجدول گروه قرار داره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24246" target="_blank">📅 23:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24245">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8XVL2u1nYnGRmWjx71l9xFKRJ8G3jqNNsE1ZfOolhcwtORgA52-XJ2Ae4KkNrdhVcQsfV_nib8qMeCFQAWpbRHqfGa_cr2Mm8Uv0PUeT2a3rWe1S8gqLZsHRLQvEslnXy4ExW7uYc2_i1HUL6nqHbEfmEAgVD-SJ0XV5j7Xt94Ei5SRjxrIi3EFkSe--wB46c_FeXdpgLa6Jwrt-wsGj7Xn-MXC9G64GSTQMfL7Tbtp3ICSVZlnSBQ32WFnBRNBx5A7wc3gyfgUAEOlEUjr4BgblE3ZR-lkycU3h6LGr3XTJcY9DhcfZchGrimUDdQcHyCjTnLer302HfmqqdO2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌شنیده‌های‌پرشیانا؛
محمدرضا آزادی از سه باشگاه گل گهر سیرجان، فولاد خوزستان و نساجی پیشنهاد رسمی دریافت کرده و درصورت موافقت سهراب بختیاری زاده از جمع آبی‌ها جدا میشه.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/24245" target="_blank">📅 23:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24244">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cjp-JRWpyBoZ8hAYJw0f2EEfNYgQS9Fuprbo-4YfdEx2rAlZJ0XlI2E0955uG5i1wk01he4llKRk2h-p11bQF_IA64Q5NnzFH6mWOTJkIzqe5IAVCBRl9JPG4TisZSTnVCdzV2rYx2gva31ohuVbm-wJijaIQF5BL5DdgPUmcmUG88OzZdvm-xyZyaQlf13GQ8zEMazf4Or67Qked5mo0E6jy17HcRI8LQL7ZX2xWCU9zwSFQ4IEoC31Pa3wwgtZnFMPXIeEpoIwkQIzoRbset7tl1Y_hW929lfsz_WIgbsUpXUA8offp6VGioAkgPor-ve8IlIxeY9BxjOEUdvUIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پوستررسمی‌باشگاه‌کوردستانی دهوک عراق برای یحیی گلمحمدی سرمربی ایرانی و جدید این تیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24244" target="_blank">📅 22:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24243">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4YJEOqf3qlPEN6HVoOA1QtY3sVSAVaKP2bZ0iFdI5FJGLjeJ5PCSR2iXQwrJ9q4r1LV02jh9Wd77LULdVkNacVvCnnV-uqDNJbS1jejE8L-Ba9CTzfGb6XMYQ6Uo1qtGQ3ZefTz68KltRE3XtBo772R6QkcJp2hFlvbQ5L7_Ze5fEV404__gVHPZcr9XNlfjN62TXM22gsBTN3C1utVQBvckRFBpA1ibJ14Pt8bKiEegyJ6UdWjWvROELMUkh4lCQs5hrc4gbIw10-_uYGG9RgPOjL-JWCFfNRgajpf06L2uAk0t3Kji2IxvwUbw2s5_vehaLQnCwzej6uiFaZkaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24243" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24242">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">📹
این چه سمی بود دیدم؛
رونالدو، یامال و هالند درمدارس هند؛ ارزش دانلود 100000 از 10
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24242" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24241">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dwy7vI11P31tqyiXHKs-LUKHIk0iYIICLD8CLjbJ8Z0mjletNeXqvL9954_RXs02-3WJWSgA5_Y4jwt14614Gcpncickuxm4U3Rop3YoHzbUgW5gGgL31OVaKHry-y6MInjLVSiP01__dLvdHYvuTj9kg5UqAq37PcDXOkLBq8JX637LcnCc0oFtBZsGcuoXNAyAEK69miseBaNKQFtuud9QIPy76CUTc6_hJSLCdKx6EneLTKauu8-EU-IzUe7uQZESLiUzoOLz3K7U_r4BV0HnRgoTtz7HIVTfdp5KhAfqahLjABnwOBUvTwfeKn3xzWc16yVyY7vWii03IWt-rA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/24241" target="_blank">📅 22:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24239">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F11M33HLv4aellkXQ4iLFySctVlP7bPl1GWY7YZnil069IL5b9FHVZaryeeprJqrnp2VysgnARk4CnjDMmOHUkD92stPhgNyENfPXAkkFV0gr4fxPAwwC-r1kcMszIVROWdtKEzb5aAZZnYi9OhTuOtMcz5AHRn4DScx_NdxagdZv4-vvz596_rN8fJlEuVweolt90GcWRakNP0JA3oDik2jk98ZLCgGF7k5zaoNxTtOYjnorFyixTXHvcI18E_dIRsASc8KQDgy2z9KkvAD7I5J98yBIJ3JCl4nZzp4G_Qza-JYZY8-xRAYe8_bIKrY3Cp5khU8OtLgm2o3GMGQcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fvv0DBMlYQzc64QiolUM1fgZ-MRaawqoUE_xCs4nPCvirSl_AxyaIqjsu_ohNw4E46ZVb0YuXxrAL3H7ToKrpFT5d-l7twvIfoegANbo33L5_GOZHRd0cnu_iS4cVhHJaaZp710d7lFtll7bPbJIUa92eK16ZBVz_usYm__LsA6VS4YfM6vxgVq4fsdhJ5A5njwamkJZtF1qS2akvCjOkerdY-WsLeLaVVL--gRfbhFSVZAB3mPznByoJnwD3vkKKBqKEc5-m6uuvWaJm_w1HhftMfAWFRJN-dfowyoq1V5Tum1uWhMH-2waMuy-PMNUjpHYGuYRSeniuLUhO48rQA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🤩
🇵🇹
تمام گل‌های لئو مسی و کریس رونالدو در تاریخ جام‌جهانی مقابل چه تیم‌هایی بوده؟!
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.5K · <a href="https://t.me/persiana_Soccer/24239" target="_blank">📅 22:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24238">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=VyDdN1_b03P6LA_ue7crXVuunLVh5nXNV7bjxOykQ7xOaYKIb0pA3gJF59Dcp86Lhw8LZE2h3SoSS-TcD4YYJjd2Zvn1SY1CMVNscePjCXOqhphP8jiNgvD1OquS9vPrusqapH38_Mj2VgPrTznDIYY2-IsPyhwembLOfq14TeLlUOtEPLSPEvCVrDh8wvDvRIfS-dJDM9R94XCdVORja4e-is89Orbakc6MNG0HGbfbl5zoJnZqhPVT9uqKKS24TSKSLtosL7bLtvx5CqoWcUcjLpx3Nqn35i69DVSsF_Vp__4NY-5mOzZhNqBCxx9vlD92348wxtlB96roR33JUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d46a7b1648.mp4?token=VyDdN1_b03P6LA_ue7crXVuunLVh5nXNV7bjxOykQ7xOaYKIb0pA3gJF59Dcp86Lhw8LZE2h3SoSS-TcD4YYJjd2Zvn1SY1CMVNscePjCXOqhphP8jiNgvD1OquS9vPrusqapH38_Mj2VgPrTznDIYY2-IsPyhwembLOfq14TeLlUOtEPLSPEvCVrDh8wvDvRIfS-dJDM9R94XCdVORja4e-is89Orbakc6MNG0HGbfbl5zoJnZqhPVT9uqKKS24TSKSLtosL7bLtvx5CqoWcUcjLpx3Nqn35i69DVSsF_Vp__4NY-5mOzZhNqBCxx9vlD92348wxtlB96roR33JUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
ویدیویی جالب که لامین یامال ستاره اسپانیایی باشگاه‌بارسا امروز داداش کوچیک ترش منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24238" target="_blank">📅 22:02 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24237">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kdPwz4Q3QbupmtN8-AzhzilltccpO2nQOv7wVNt5iX7ACTKvaMSVtSlFr-hebkFcohzf-lkq5A-dgfSrCDrti66HDF--IkNVcHsMojKIFIXQQmUsQ98osuEEBHm9X4oYv53QTE3sg1Uz45tnaCtgy7JOEnxbSD26NSb0K5p_2YxlKqkVtpf2mnYbjquexxEao8-F-ki3gpNwRdSxdBiBH09W17AbK8-WMH1ghA5wCt-VrEV19vtXy13Pz9yVEw4qdpheVoP43VBFwZLpZCqBSCN318jDfbK9Bc6pO2B3iHf5NZIQE6Vqwsk4mw93BBcCUAt2dNrChcHGe5vf8x0n5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24237" target="_blank">📅 21:45 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24236">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PnTwKF6hToYsaI7drjvQcuOkKfXfTjmhjFkaoBE69AEZzYZZAi5WuKXO9xB84dBC4dTPKP2kWlNjDrTEYjtuN2_5IND1wcReCLJXw92mR4jgoDqCyey-6uBA9p7eaa8vRzpr8utFiB2RJlDdNOPgirhsxW-KArhM_P76TG6PCMfAcrkxo0WgU-fFYKpAB98Y4qUimFvaWfqsfK6BudrVxQzRItjC27l6bM7531sL745cPi6_tUhVOBzr8W8JMkGKNusxaSXfyLiB88OoZv2bGHtB3wtPKrs00kW9yQHT-4MvOHWo1ItTZQuEszDWTWx8NFS4_zs6XWBF6niLTnEeVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی‌طارمی و سعیدالهویی، مربی تیم ایران به محض ورود به فرودگاه سیاتل آمریکا توسط پلیس بازداشت شده و هم‌اکنون در حال بازجویی هستند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24236" target="_blank">📅 21:28 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24235">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSPFl4U8i9Y9c8J79JP-qkdxn8DCU1RT3DrbXuNJ8srJbzp19s9uitv_LXaKPonJt9dFTWp2SGQoslDU3XQ22qA46Vg5cgnLGxA9P0S94vn5ka-wv3p1x0xzQ6V-Lx-9POvETyNRT6D2gd1gjQjynSpGjl5Q6pNhSQej8DMHySSZM6bM6ulbkU5oiFDIbaMP5S1Q7BiN3cNPZHBLBxVIiLMEXSahwP_SFzcn9uUi99RZgzFehCnIKHfi653Cgj8w0zpmphHYTL684nrZ5ZVd4-t_ZjnuyGT1Rh_hyI_-hFlxkQTOvf7F26Xu-AlnMCE_tp1rLxqXujFFBLMdhDRV9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
طبق‌ شنیده‌های‌رسانه‌ پرشیانا؛ مدیریت باشگاه استقلال ساعتی‌قبل به مدیربرنامه سید مجید حسینی اعلام‌کرده‌که درصورتیکه‌خودِ بازیکن رضایت نامه‌اش رو از کایسری‌اسپور بگیره و بازیکن آزاد بشه بااو قراردادی به مدت سه سال امضا خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24235" target="_blank">📅 21:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24233">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ExZvynmrHSgR3QCniSNZwBOC3wrPMoVC01DZEpRD6dCqAwXhfaiv0NCQ77WUVtX2Shbv7QWpEhe1whBMSTerq3RDp7CEGZlPjiWIVnX5LZ020VLhQsibH1gFRXmuLx18Chre8fzzLj3vVEafL7FLLIiGDHCiP6gskYTnEiJhkskGO9J-W4PckC-yJRoDeBhxaKt92UvLRpz3-C8FbgJvoHcrZv72Or944cWwkFdBhnkLMTdCrW2wzStWI1V7dns2V6_p4Zau60OeNZ7uyxEANH904kZERegwkqqNnAW9feQdCHCDo13kf-ZjPLvNYR5IuOGHLNKRbn3GSUgTXjUM_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇵🇹
ژوزه مورینیو سرمربی جدید رئال مادرید:
رئال‌مادریدبهترین‌باشگاه‌دنیاست و بارسلونا هم بعد از باشگاه‌رئال‌مادرید یکی از بهترین باشگاه‌های دنیاست. درباره کریس رونالدو بارها گفته ام اگه از او متنفرید دوحالت بیشتر نداره یا او تیمتون رو به شدت تحقیر کرده یا از بازیکن مورد علاقه شما خیلی بهتره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24233" target="_blank">📅 20:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24232">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bEnh4wgrhJva59I03rgz0qLpWigGVZI_jfikNg0QLMm8SDSe3Lb3MZARU_Bon-_uyRjuRsrIenbsNBjqo9ensg83AnD4cudWKa3JkCl5JW_NfbkuYFYweqvYSG7D45TOTFayum1G7J_u011SR4zTXPvTvU2nYqyTrFrB7NVSaAdoX8p8IQ04E83tAwuuhnEhXrcOvTvhHibJfMMbnPop0hN2yhXTR4X9Wy8_vw_kP5vynuuiSxPgkKB7whJukK9hnzMbSvuSErDp16JV-eH2a5kxOXp3xyfWhObkkMYmsBQ2xoS43xurfge2LMbD2VLvwvmjVCaxb2-CyrZ8-btEww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
قاب زیبا از دواسطوره تاریخ فوتبال؛ واقعا هر دو بشدت دوست‌داشتنی و محبوبن. حداقل تو کانال خودمون برای این‌دو و تموم هواداران شون به شدت احترام‌قائلیم و تموم امار و ارقام و ویدیوهاشون رو به‌یک اندازه پوشش میدیم که سوتفاهمی پیش نیاد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24232" target="_blank">📅 20:13 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24231">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t1Xi5Dd-fKtGIk7eY2n68GV8j7OXyHd_KqmVOpulZV90v4xnNrR-9MW7tUfNoQ5tuQ_UbDHlBGOaT49N4nAb-pRo0zuuYlW-5DIluTMmupBWp_AvPCzSqygVXyGhjCQr1bTYJ33ZyOe9fEofqAPfl1oehh3TWkg8_Ue1Ix49GqpeqmSrE6ty_fN81mR2og7HWRIEnX15ecsxCvwkiO1z3iy7NYiwtEZmFSUnaUFH1a41e98MHB8xZJnAk_I2ViMN1wu17_i_UeZOxmrXvHKvKLoWQqyAqQKxcRspGX5lvIXJ_LzwbwNVjW7MO8YSxKvKAX_ZqMBEr4MPMriudG3NBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه‌کامل‌دیدارهای هفته سوم رقابت های جام جهانی؛ عین برق و باد دو هفته گذشت. یه چشم بهم بزنیم میرسیم به بازی فینال و اتمام رقابت ها.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24231" target="_blank">📅 19:57 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24230">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XbQiCziih3w2yiRLFt-HJIqNGKGBX9TL37_2cc-4MucvNqJkIHEmP5m_xOm8XBzJR6HsRVYcFQa5EwVBAO_1CayD8_0BuWJmxhf63tuqMf8fIdtzEEIsPjlHOP9iQSpXIvvSTMHq6FN-xQsdzv1kGk_t5OQwAzyFho8WyRx1KVvO7c6udi21zU8mkqGUhOqunfMuyTPOqE-OVx3UXNaJzgBZG9fk0cMT4Zs33pbD8Kw10KzLh3UmfEk-CVecd9GBDaSdUgFVHQOM_HWWKigruHBRFiNKcCuqP5QOwWHVOKJQpWy6BBsmIAuwC_XioWZxxlBVcydEULihsY9HRn4jkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
#نقل‌وانتقالات؛ آلخاندرو گریمالدو مدافع چپ 30 بایرلورکورن با عقدقراردادی سه ساله به اتلتیکو مادرید پیوست: هزینه این انتقال 10 میلیون یورو.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24230" target="_blank">📅 19:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24229">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j1FeXTbkZfNWvYIIrtRtYuXhTFVYs-Hb4St69Kp1b-tC3RAeKdUhYTfLH7DTDci4MSWB-vBv0RdZLjOwIEtuLKA03fTX6GBe0i1_cVVha6poB6t4FYagoHed3Qr7K9lO90QsTUE7tWQ2onwne9z7Gr4lnsN3TI49GrF5vzjz4wJQ1RK1x_0Xa-wkmcq2ClEgJ7vYCjVRCcgc2HJx7iV0VJUER_dJvBk_5Jly_5-IiPIMPZ0hykY4C_XAB4g9WgiE5jEPGaetbQgH5Yt_0EW37SOVU1kHiyytwn4j5bnhJaj1QYdW_p6oYperkKs6ciW-rIz_QtjVEqwA-5PDD7XFxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24229" target="_blank">📅 19:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24228">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lrfb_rMJo6dVRXgUzp0nkxtlJaecSTI0OW-NsrxEUgKm53bSXm4Xn4MFp4ODaZxNvCpTJRWAekRFh5Q8mrjk59zkrLjWWicUQpSIY81Zu24flDYoSETzcAp_4OIsOdGXR0AlBVuxxkqmd7uQ6xnYNAXYHBibp3qmcHjyTkFxD6bT4tByNB_LpbfXUWkd_46soPMkYElByCDZDjJMIn1FMYOxmRH8P4z2G2_n9-1Qp0XTecInkTHpZVVlAooXFsVAz_XhYSRjW6lkoyVNbuz7-8eDDvLQf37u796IaV7txFPxz57TL7f_iT1DgjktCq8bd7PfwAeyx2FJiYPi31am6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇬🇭
مصاحبه جدید جادوگر تیم‌ملی غنا: در بازی باکرواسی‌تمرکزم رو اینه که گلر تیم ملی کرواسی رو طلسم کنم که تمرکزکافی‌ برای این بازی نداشته باشه. صعود تیم‌ملی غنا به مرحله بعدی نهایی شده اما اگه کرواسی رو ببریم میتونیم صدرنشین صعود کنیم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/24228" target="_blank">📅 19:03 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24227">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M5Ie3_BiPFZrBdzUTXGp8kCLsOeTEGE6jqjxnWzkt9u2yXW5MwusBmfblBpi4a6ButbLI9Ee4AmYKqr0SA1hx-N-O2iEfiBfNU8YUUgwGMLevBHYd1ynBnfh9inQrqIIix4n3PyBNIhlAvTy-u3xZ0GxQ3Vpm-ToyLfamMWWfZH7_8oERp1Vj1AV33TU52ZKuec2yNiYxgUH9CcDk-jLRHnvrYyHE8YabrTfQNAS7BD7tead_y8mLRgqoywd2O03NqpRz6BEGjtosZ4qGxE1E5JTKABOYR2XANKx2yIre0umEjAMJAURmcBV000FxQkIO_SBv9Iag-u0CwMCyQ7rsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/24227" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24226">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc38571967.mp4?token=ZFO2_EluYVMBXf8Nzt2J5XgWP9ZYNTV_i6ljafDb2OLPAZdb38X4KrayJpVAsLVHxXEnf9vBtvIxYTeNeSc_fnorUdlKRry9pX4yvZEHN6Iu_x2LYXamWfqA3aei5d4gMt98zIzyLX1wLu0_PbsTmPfRo7QqWifBcdLP5rzcDK7NfvDb7u50ryf1-yNLuzmr4QId1NBF7MjogV8b0UlVbUZN4PxKzkDJonjLJZSiYaA505wSpsXhVRlB8O7xiG-0tBuiTkjxL72Udiood54OvvsHMM_s3-IByIx473ZpcGC4qtTJgBeMJBZbklgXFwzINkFPpXvbrS625toKiwcK5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc38571967.mp4?token=ZFO2_EluYVMBXf8Nzt2J5XgWP9ZYNTV_i6ljafDb2OLPAZdb38X4KrayJpVAsLVHxXEnf9vBtvIxYTeNeSc_fnorUdlKRry9pX4yvZEHN6Iu_x2LYXamWfqA3aei5d4gMt98zIzyLX1wLu0_PbsTmPfRo7QqWifBcdLP5rzcDK7NfvDb7u50ryf1-yNLuzmr4QId1NBF7MjogV8b0UlVbUZN4PxKzkDJonjLJZSiYaA505wSpsXhVRlB8O7xiG-0tBuiTkjxL72Udiood54OvvsHMM_s3-IByIx473ZpcGC4qtTJgBeMJBZbklgXFwzINkFPpXvbrS625toKiwcK5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
۹ فکت‌شگفت‌انگیز ازکشور‌های‌جهانکه‌کمتر کسی میدونه؛
دوست داشتید تو کدوم کشور میبودید؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24226" target="_blank">📅 19:00 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24224">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=Jzc0n5XVLS9Qw0E7JorPWXEoxHeHZTUYF5Uj2XGfQ7l2bw7XDHd8k9FQ78_J0wodXTWy4bjdzBQMbvir-SNi9wBRo9wYKQLz0cmbVXoXLL-oAx9KBGq4sp7FXOpnZQvnm1_l0a7zfh0nS1yAJ2Ow0VUuI8AWtQLkq5B1c_lzjEcIQzqr9d6hoS6TvU-VRUrJCXadzUKIo4Ycyuc4GBcWS4UiO1kNgYLto1KdNN_ID0S_wfOauZh4TwS5VxT2r2i2EHocKMqMwd2A3Kc6DOcM7a-iJg4VM3Ujf72P6G88U61m0AY9_79aHW85cLMTx4b60dqyoDcl-0GxMoGwXtFGQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0eb571605b.mp4?token=Jzc0n5XVLS9Qw0E7JorPWXEoxHeHZTUYF5Uj2XGfQ7l2bw7XDHd8k9FQ78_J0wodXTWy4bjdzBQMbvir-SNi9wBRo9wYKQLz0cmbVXoXLL-oAx9KBGq4sp7FXOpnZQvnm1_l0a7zfh0nS1yAJ2Ow0VUuI8AWtQLkq5B1c_lzjEcIQzqr9d6hoS6TvU-VRUrJCXadzUKIo4Ycyuc4GBcWS4UiO1kNgYLto1KdNN_ID0S_wfOauZh4TwS5VxT2r2i2EHocKMqMwd2A3Kc6DOcM7a-iJg4VM3Ujf72P6G88U61m0AY9_79aHW85cLMTx4b60dqyoDcl-0GxMoGwXtFGQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
دیگو دالوت درحمایت‌از رونالدو کاپیتان تیم ملی پرتغال: "فکر می‌کنم دیگه همه بدون کریستیانو چقدر توی کنار اومدن با انتقادها مهارت داره‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24224" target="_blank">📅 18:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24222">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5kjT7O7IFZliOVszEcuU8TF0rQoIEu_Ron0XJqWsi3Mcrh9p0Tc-j6gN1DZx2K58ISO1j1yjVXyOVWUFjeAE3GpcDZwRfBI2YQvWvcJO36PiVFQ4-ZbNA6R7briwxoc96DlSb2AfqY5ceyM_r8X5RQo8_WvIttjujsz4DvwRU9FlN5j8nx0vVUGH_XMgdc2YjYZxSibl74MdijI-TS6v94VF3RVir-HnsuGSSFh9NX8hndeLgYW9JmC6wRsuiMDSaqadyQRxV0KQXL5ciiYsE2n9RYsxPB5loKCVGiXXAmzJwC6dodRoqL-sOwEt-R65MlssCpSxmgtfqgwPCifyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BDzLA0hzuyf8IP7HbdtXfv8sDAtZgYlxQbJ4wdPuDasp_qOVyW_71He7pSvJypZVKbUre0AQDpBICj7CtabkQK0_65HmADqCKLJPA6c57449QVLGajmEWRy1z_dXIkwvj2IUQNVzNHX7_fX_ua_0HNf6iVsC6PDHzGRddWLbQ3Go6iqPJVLFDVzDHPMKsFZzdrafmQ7MzBZ4f95Ru3DJD0mTzIjswPHA0RlS8K17fFFrjuf7SxDBVAsyQGNxKC4yUVLspYLd48oj_dp719JS8yMneFmZnwmVCEwu6uTcxM9FOI4hHqhRQeG2Pj0oTPaUjOhrmJ0IU485NAad5hkbbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/24222" target="_blank">📅 18:34 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24221">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hEq2xns3bLIYQzL3dCHbOxO7QbhJELYyQz8xNNFqS4iCoMHHb5T3J9SltfuQQLgY8_c7Ai7u9s49jNdF0IhT9OIAgdhZtyqbEWwNgjY33_JjPBhEJwkvTIT6THM57YSYy_w1d7jXj46nERXzhHGmLtbtWX09YST_ORAn-SkdO5xsTBMQejKY4YWwlAb5otVsVuQNCOL0qGBhu3oMZIKzwkTaL3zTrkDEWjeN-AdUn0y23rVZ3KuiMaFj2ysG7Ys62Az4CbN6W4E-sXiswa0I2b78Fa2vrGAjZOSrC2ZKTeHNGG81OkHpOkt_gXUg0PEcToIkaCj67EDcAg0KWDSNJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
باشگاه چلسی: انزو فرناندز بارها اعلام کرده که قصد داره بعد از جام جهانی به رئال مارید بره. ما مشکلی برای این انتقال نداریم. با باشگاه رئال مادرید به توافق برسیم بند فسخ انزو رو فعال میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24221" target="_blank">📅 18:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24220">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O-zouoa7d4G3iD8-ef1Dd15LL_p0JBIpvjt9st06D5MaT0wI10ho1K2xFymbV5ra7nrdW89y_uXgAY3-b1krY_hPwF3cdh3vqVNMDQ-BOQgfYCmxyKDK9szBltXo-yfGJjiL6m89Eroe6wEuNIxNXMY8mgHsfTjBcZvSmaUdFy7JANRI6GrqNvhfOy1rjpYMZMtdpp1mFOr5XT3DpYFbe4_CgU6aRO_xfxKxvfr4mqR2dDlWK3m5D7J1z-NnsTadifr-GLQW9f1CRPc-kuLU3Fv6UARv305edtLRLl1Y_p9EMlCwPdj0ZkZVdW8N38RmRmsrSVCy6Ja_XVhic8r9aQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24220" target="_blank">📅 17:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24219">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbJJh48_K_hkgyf5Arvg5dHbCHmb9QwymKEo5OxKbv78uRm1t1QB5VOgUDRTXis9tm5e48xHXJMFdRYEM-v6lEMNlMXn17EJNcmgqvL5vTDyHY8HcU9uePJbINZN5d6zn6Q4oTNtF_BUIVKMeL6TervygWK99DihuI_zUaRJ25UU81U5EAjWxXH8dwoFKW-oOrop9D0A8lPVdfReDx0iNouZXoC48tbtX9KGn0or_QEdKRwmSHwGB-5IMjd4k06DloKZGAyUyWORwqRk3_4L2VEtzGqKBr9XKUwg_rYu186zg0l0ILRapCvePs1vX-Njvj3zzkIhoOgQuE5NMqfvaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضابیرانوند گلرتیم‌ایران در رتبه دوم بهترین دروازه‌‌بانان دوردوم‌مرحله‌گروهی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24219" target="_blank">📅 17:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24218">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rv7jC-6cYI3EblPMspa3hgqY1bQtQ29wJD5yqsRBq6zAWY7fzMrnffuQpP1vY8mccndj26SDU1ngZTlyTvXI8Lah6b5SMwaquf6b2IREzy9q5oaQ6YxOQdtw8kgD4531zq8X_OZefCkwM_zvYgtXUqVHzoIkm-B8ggCAW7PYMD1RXDe8SZtVP9zWlcW4zqySDGdJ0CnAvi7qSn1-n6eyUIJ7Taic8LThb3DnCjbGHNeej5vhjPb_AAWHJmHFYgRz0aFNpU8I-Q1ukXOpxuMORby15M7BDzw-EwREskkCPvg5VU_s5xtdFHbrTZsfa6BPrDi2EHr2ZZFOEr49UdGmkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
علیرضا فغانی اسطوره‌داوری‌فوتبال ایران به عنوان داور بازی جذاب کلمبیا و پرتغال انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24218" target="_blank">📅 17:30 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24217">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NjkQt_AYYW92keIMAtHoLgoCU2OriUCY6mXU4nRvk4LJy3fLQr0PUDKKHDEgdvBrimhhfVpVlMv4XMwFDjaNC-LJN6Z3iRVrrHdy4Uw0Verh2tS9MRq1QvGFHluQ4APVp9eNyYjXBTM_3JDQiRwB2HTtlWeZxz9ItWNg_GWrBa7po2A3VVOl7kAZb1yg0uIIQ9OtES7VNyBxibqNXDmIoq1M7NjKftbFUZJMuockLuhatD1g_lzuP59CeM5ubjPgY9NBdpv6k8zquamAfBJLhJcQ7Kw81uqmolYTSlWdqX8lUheEWIhmr7ALt9d5bJoK2huuZkkIS8mrPCS5s1H5cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24217" target="_blank">📅 16:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24215">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ROYLeCcsLJGnAUWE3S6NGJTt0OcyUlPGOMmMwtpYiZN6_YJkr52Oo5y_1KW2oTMG01lBCqzOURePl5lHkCQkVdnmtL8JH1xdqeVgGYP6bk0jr6wnUZ-gYnOx7jsqEVefcDgBI_yCfdEIVPE3eh0NUUziQfZNo4J4aESQ08kIgt0NlhBNGnqi_y87i9bnNm9RQNS6CJoD6U1Anf3jw4LD4sBtLVXcSrxRSK8oXIACruERxgl31k9NPqWblBIG2sSQ2MPM7cC98yxlopSq-mK0LfY44fpl_Yg-yFHt5ltcVaHz68TSq9wlamR0Ulxavc4i0BMUM_cr0bhUeiZMf9vWBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WPfAmw1dn8uJTb1cGjHkTMDSOOxnrzur6lEZavgXXN_juAYBTKvqGh-GUPJK-iMD8mvMEOs2Ld_YrVuyLWS8eSP0fsMRes5JjCYDeklSkIzevkQsv1EvI3AWfrHcqD7T6-5TeoMrDV9vPk6L1JzDHlRRhSl3JnA3f8obT5CggwhbR8VDJaV9tQ_OUqMThOsS9ULBuQu3G9GLkj4nEYokvW-AHbWlKWPUVzwGaEKuU8VL9vreEtXjkFRMpB_2aj4iQ_ZfhEJQCYI1NuLVQ1B9WGFXipd_xxV_tBcrx5DBXMzYM2oLNDmw3cA5TIH4AwJ-HVRNAznjk9LdfHlcmXxwNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇲🇦
این هوادار تیم ملی مراکش گفته که تیم ملی مراکش به فینال جام جهانی راه پیدا میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24215" target="_blank">📅 16:10 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24214">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a79050b237.mp4?token=QEBZRriGhOlLZEyehUNVVm_u8ucFv4uCI9dNRwk5P6bXE9P8uDGKyeg9XAbnv3Puh2pCkv4nq_trFcpKWyz3T38BFEl20LTJnQL-GIi7U4TFdNWUVom8das8WqDO0hWWueUQ2ebN6BgNumWyxSYDun-t4QwzAnS6QwZu9rXFwU0vJBMJqnaQ0m-SIEeVoMApvqQWFBiNKnk6JQg0rzhz2nfaPGfBQ0QPMnTjgLt_ajo4FLsxgHgdeHwH8r6yXnMvzVSjqTSclEUz3fIAmUGUh77DZUmY1oCQTu2qlQMxvbYWYZFpj1wZWwQ9ZreSiidGZ-TZgz5DHLp_Cqk83Mu8ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a79050b237.mp4?token=QEBZRriGhOlLZEyehUNVVm_u8ucFv4uCI9dNRwk5P6bXE9P8uDGKyeg9XAbnv3Puh2pCkv4nq_trFcpKWyz3T38BFEl20LTJnQL-GIi7U4TFdNWUVom8das8WqDO0hWWueUQ2ebN6BgNumWyxSYDun-t4QwzAnS6QwZu9rXFwU0vJBMJqnaQ0m-SIEeVoMApvqQWFBiNKnk6JQg0rzhz2nfaPGfBQ0QPMnTjgLt_ajo4FLsxgHgdeHwH8r6yXnMvzVSjqTSclEUz3fIAmUGUh77DZUmY1oCQTu2qlQMxvbYWYZFpj1wZWwQ9ZreSiidGZ-TZgz5DHLp_Cqk83Mu8ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
ویدیویی از تمرینات لیونل مسی 39 ساله
؛ نکته جالب ویدیواینه که تو هر بخش آقای رودریگو دی‌پائول فقط چند قدم با لئو فاصله داره.
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24214" target="_blank">📅 15:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24213">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FsfgTadKRA1jFNcj-MvnsayzTftSCRxGD3cLzNWnC2XT1dFZIr_4vIRk2WnhKQmC0rfHLqXCEdUpb-I6w6BQnWYEyQJj_RARO78SMywKnKHpbDCg0yRWXBFie9BHYdsmyPtpUlLyLxflmMSPcQAIdSKGgJ4TFb_cWD3HmdSTGxV1NGVRq7NCzHaLp4gj6F3njZWORrHbXmPIVUEL_5BFzfwLykCLqcNNMeKrSYpuyp1xg2GjELDBJ35tVxwYOZaudysHaLwI9QrYwAv-VFKE1wwc2sw-5K7SBjk8N0tXFTmfKJTk8h6U1pL4iKRxizI216M0ChCeoiSP_Siyx7oviA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌ های پرشیانا؛ سیاست باشگاه استقلال در این پنجره نقل و انتقالات جذب بازیکنان جوان ایرانیه تا درصورت وقوع جنگ در وسط فصل اسکواد این تیم خالی نشود. در بین بازیکنان خارجی رستم آشورماتف، جلال ماشاریپوف، مونیر الحدادی، اندونگ و یاسر آسانی در تیم ماندنی…</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24213" target="_blank">📅 15:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24212">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/paSSU42bywiomqkCsM2KNzKLFyegnaFCRDvZJcNJacdhfZYV--VDZirMtfaeTONuHvIs35qTax-MHNgZCTF9xpd0KTvL-pezNGARb0Z850ApxZAqE8pNOQug6g01C2nLN2RXEW73_fikzD1qKDjACbjaqgDz9-f9Q2FbBfkwnSeK8rNIzxt7uRUOwnZSpH6aU8Zht22MEGGqGzkTE2ot9isOgalVhBDYIP8uvSvC9yeD8ju964qki1g6wO_p0pamrmH5DvvjrodjTEpZwcxpSK1DCIKsFLi8kcFSDgVFBZ0PsmQ3qbwi1No9NYILgb2eraX0OGhFiOZFVN6XV-7PMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
مسابقه امشب والیبال تیم های ایران و فرانسه به صورت زنده‌ازشبکه‌پرشیانا 3 در یاهست پخش میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24212" target="_blank">📅 15:25 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24211">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVYgKAk9_dr5AC2GRCLRUqMNk3Wv-0VK2wPHjxXRrlN46DueVvDsO4gG0Tbm2fXTk3t3gNvNK9A4t0ZWju8uXPfELHsQF5JLZGiQGfG4p-ziX13P0A_U56JFrxdrWqOySetIUiarUpv_YHJkGeFJ2suW_SAXPsq5BZjEO4nt6Hnk6HUpwfv4W7JgcBYpll--7lGgo36zOuKq-2CUHszjDoyVgr5kmwGLnLNMKaqgGEPoxGPCSgZMdm8jPFhHSAeAx0e--RQ4EuBBw2rWlhytqFG1hDC2fVEoxbOH4CzilFRbo9YkIpxuaheTHSjFcMDq2-kErPHPdWBDzjg-WlSGbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی‌که‌تاالان بازیکناشون دوبار بهترین بازیکن زمین انتخاب شدند؛ از ایران رضاییان و علی بیرانوند نفری یک بار جایزه بهترین بازیکن زمین رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24211" target="_blank">📅 15:18 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24210">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hM2CieLQYqz_zbM8t9RyV4GrheRfEoTlOE5enc0iHIFXiKamgHkZOWL_FJZrIveS3s9JHLevWooyw2FSIK9452pgMT8TgxasACbz4UEO0VyIYZPVWxpRr17y9H52vSNyyXoRtyhsnlCJbk9Y1XpjaAQWJ1YXOkddQaPJmZLO1QlMPbfCRxmTsd-7pvj3eg994cnSYWX83ojWRGc2xy5BoDSLytYupzhM6lTRs-S_8yLPdKO4YIQ3SkX8Ht1LuwimWum2PFzaFnxKE6rLuMM-oWU_dToePg0JkkpvVfotHmvijvgvTCux947ctjK59ULtUXr0FbRVPhGnICfnI-p1wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه بین مدیران باشگاه پرسپولیس و اوسمار ویرا برگزار خواهد شد. تابرای فسخ قرارداد دوطرفه به توافق کامل برسند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24210" target="_blank">📅 15:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24209">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/spwiW_YghnUvmJTkZCWtd5ELDuJ8FaaKBzVbEeY0G13pAo1pR6JwgQaeMe_XRFlDukh3AFOmHsB7fsNq4LAMevRUQrrhJD5jTwtU5Pzx8124-D9ssCwwJ5ZknNMn4mljFGKRjp1GFN0bIXpf8LLzMU8sG6zKpRUm32fd02W3npZvU9ieH3slkG35rCtVkNqr3rpVN4CGsjldMzJzwfxCm_kttMv1fgnKSS19hU3fIDopYyUdYNTHj-d_JnwwTlw4_Z4nXm9C4OjJkAEz1iJJeVHThBiQiuU3Fc-ajAUGwu4Cyppc-PNhwMMmRYxbXAWs7sjGZFTRLzosTEw4yRXFhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👤
مهدی طارمی کاپیتان‌تیم ایران:
بزرگ‌ ترین شادی صعود به‌ مرحله‌ حذفی جام‌جهانی این‌ست که مردم ایران به هم نزدیک‌تر می‌شوند. اتحاد و همدلی بین مردم داخل و خارج از کشور برای من از هر چیز دیگری مهم‌تر است برای رسیدن به یک هدف.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.5K · <a href="https://t.me/persiana_Soccer/24209" target="_blank">📅 14:55 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24208">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm4fWAufBtMzArDWk1s7FXfCYCmVYp-OyFCRCtjf9Gk3ctseWNo142Mx7oERQal6ZctYL-uVl9ic9F6nR2uQ7ti0jfGk9o3eArrYvv5bdBeuhPpsKyRncR4UB9JfGX5pBz9miys6jhlXsqa8zgMS-xw4Ljyo9velZW8E27SDjS7Nt1X479og5grfpinjQ5XNqD1ZlYkzMMU251eVuHLYdrBE5c6XksL3h7vEcVZmcGDKqWELP5HxWTINaJkDaKDy3VfioQ0ble4ZI10H-xfdSvHHeCUpRtLvIXeXmM4MjDNUgIMl47F0cPfQtt6FJF-2XOuIUASM9K1qFo84uFtReQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24208" target="_blank">📅 14:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=rkQwNp972pC7lslE8Or28Cn760cgkcnoJ8bJcXA7ie4A_4pZ-hAw1kxyRk-lPtaSB87sUp26_5vByykUP2Zji1IeHYQyTZSvDkr7BHMRbYf-Hyby797z2Ro1BEHZaYbYgpqUNz1GYDKPV5TGGprLpDMvQmM4R70K-TbcVNYf5JeiBGPZlYV7qKSJzK9bh2M0Fxx_S5MF01C4_4Sj-RSaZ7NoEx-DyH0VZs5WFkzEQdV6Lnq-08mCMxbFA1U2dqt-dlBGJwz-_E6UCrw4YMxg1J1bUVF0JmRTQOWyCVDS5mUxvfAsDZ_-n6qHo0D6ZZnVdbUiO_0WEpD98Li0m43k7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3a203ff625.mp4?token=rkQwNp972pC7lslE8Or28Cn760cgkcnoJ8bJcXA7ie4A_4pZ-hAw1kxyRk-lPtaSB87sUp26_5vByykUP2Zji1IeHYQyTZSvDkr7BHMRbYf-Hyby797z2Ro1BEHZaYbYgpqUNz1GYDKPV5TGGprLpDMvQmM4R70K-TbcVNYf5JeiBGPZlYV7qKSJzK9bh2M0Fxx_S5MF01C4_4Sj-RSaZ7NoEx-DyH0VZs5WFkzEQdV6Lnq-08mCMxbFA1U2dqt-dlBGJwz-_E6UCrw4YMxg1J1bUVF0JmRTQOWyCVDS5mUxvfAsDZ_-n6qHo0D6ZZnVdbUiO_0WEpD98Li0m43k7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌مکزیکی‌انگار خیلی با پسرای کره‌‌ای حال میکنند؛ هر کدومشون یه پسر کره‌ ای پیدا میکنه یه ماچش میکنه. ببینید چیکار میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24206" target="_blank">📅 14:16 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=QL_YDwBRtYxoOdtyAxxaz8ZboCjBDmKyR34XKi1PvehhXCvJ5je5X5fAJ5KbRYTBTX4JI-SaRCli4M24dUYbZlqQoSQY0_WCxau_8E0tXuNKOw0hEblKknK0_bGgvZrkx3D8SjDj1P7j6y6X1d1acEx8fpDkkZKwZwOsbv0pV52R_ECxTClEvFT_D0IfcqQyLFLgnHxQTedSX19pGqCdY_ohWykTQdwUycV0DW2OASk1VU08JVNToOkjJsU1mzXqTXS6R7-wx61gv3JbhHFrT928ZaAhXW6KUvOfbQ8wApOtbBRyG3LsdFOrpoGh85APPJZsm3UTustIqhcwF6aBdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8cf62dd03e.mp4?token=QL_YDwBRtYxoOdtyAxxaz8ZboCjBDmKyR34XKi1PvehhXCvJ5je5X5fAJ5KbRYTBTX4JI-SaRCli4M24dUYbZlqQoSQY0_WCxau_8E0tXuNKOw0hEblKknK0_bGgvZrkx3D8SjDj1P7j6y6X1d1acEx8fpDkkZKwZwOsbv0pV52R_ECxTClEvFT_D0IfcqQyLFLgnHxQTedSX19pGqCdY_ohWykTQdwUycV0DW2OASk1VU08JVNToOkjJsU1mzXqTXS6R7-wx61gv3JbhHFrT928ZaAhXW6KUvOfbQ8wApOtbBRyG3LsdFOrpoGh85APPJZsm3UTustIqhcwF6aBdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کلیپ بسیار سمی که صداسینا پخش کرد اینقدر سطح ریدمان بالا بود که از آرشیوم حذفش کردند.
🔴
از سر راه کنار برید ایرانیا رسیدن...
🔴
علی بیرو توی دروازه یا که نیازمند
🔴
کنارش شجاع و کنعانی میشن پدافند
🔴
تنگه ی هرمز ما تو دستای سعیده
🔴
شوتای قدوس و رامین مثل خیبر شکن
🔴
مستقیم به قلب دروازه ی دشمن میرن
🔴
ترابی دریبل زنه، نعمتی هم حامیشه!!!!
🔴
مثل هایپرسونیک از لای دفاع رد میشه
🔴
یه طرف میلاد و از یه طرفم جهانبخش
🔴
پهپاد شاهینو رو دروازه ها میکنن پخش
🔴
حاج صفی، حردانی و یوسفی مثل شیرن
🔴
توپای علیپور از پاتریوت هم درمیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24205" target="_blank">📅 13:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uw5S2loRYdjwzXh0ecKFOUQrdx0cDEb4S_160FAgl1Q515KSxnI_aVCtFf2rBD6IsjSDZvCpJ4TMr4BLoJP53wPMSa1Jl3yioKXG-dWs3q0QFd5Tg9WZpJD2U1Va3mdAulwB0HsL_8m5fT00wrDiSlHgr11_DF5wXd0iR2-4mtDStXT4zSfoallU82vlKbUCQ42GjHXCb8cDBq0cJq2JiN-6P58FrXRkP9KM_g_6BJ4YcqC_-fLilP9Hcuznz1TrzMA8w0Yolo4ofgyZ5AwhXtsDYBWxbPPUrezNeGPhi9tJSF0JaF1jzyDlqyD3ve4W37DXBvbDv719JgClH8sQLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پس از پیروزی پرگل 5 بر صفر شب گذشته پرتغال مقابل ازبکستان در جام جهانی 2026؛ پست اینستاگرامی رونالدو بعد از گل اول او  به ازبکستان تنها در هشت دقیقه دو میلیون لایک گرفت.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24204" target="_blank">📅 13:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fBCEwCNwxemKSyC4IYkaICuzpEGv9ipVlpjKfq6VKwZeg10Sw2j2uQ2lccA4IkPdVJgFs-pdjrUmMf7Q1tsnLUKxdCW9iX2u1wM5eDSpTwnMpDelU1nHTbbWTkJJPlVGEVudRc8-TFEjgLq40EWr9W5S_N4sIXU-vFKttRxBCloCE2Lc9iUaX9C1yq-MODy7yZDvSDkTzuTHivCUc5d0CTnSs7rfyttr_WTw6g-UQuzUCcTSHHZ-W6M-5BQ_o30Y5yTcsThA9NzrbLNU4QG0eh5x7CFxuBkD8884hHM1rUIypS2_4Z-T6JTqYq_XBOkJ1eMCztJz89Tp3ww-5eGhTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3i5p1tjDRI9kN3i9_oZRHGAuYkq465F0x8emuqqsNGRYZfEgo_gb5Pufsp3u5-ddBQqIhgaImdJWHeoUfLj8VGBuuBTAfdHFI9fGYLgg8se9nGM5Es5Y2bmZ4mSOZ0cJijlZQ6f7KnS4DOfYO9QwBn0yn7uKUYf5Zgwe_xeFMQxPC7iJgrkmEoERjgn8v0i5HVMtV9Fs2JS3LaoNVIv_ss49SS8hGfd5VsXdbtPDjMoBjYyD8WOlz9QLhnWc5tY8EAsPwZjeOH3V7bmlSrveGUoWbwi_4ITW7BYCcHPFYW6Gp8T3JG9LcZWEEfM45r1fJQbkGHNSttQO7oFS64hYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hhDYjtFzC8KU7Eu_0Iz9t47_88kJYio53gFr4xqD2d3WHwNrGBBeEEuDrX8iupmIh5--yYsLrds29anTJ_KKcGaKmnFciESitc8IPeVm4N09OeDidIjS52_aFaihQdP-UK2C4vXsPvlmXfuWwGzoif0jVy6LPPNSj844BQUdfmqx8qQppbEwM-m9HJ0vb2Hk7Jv_fNKjydJpXn2D2yWG3QNEvnPJvkzaeU2EcGIwhowHSXIjCKRH-t7X2rbKoRYgzOxwflFtjeXghgFhqrcOdUwHmR96-AaMZgRs4a2SW33UtKno1dhN09zVPMPiB9zpgTlSSW_-GcrNZl0dvLDXZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=p-I0tOQHNzJBhf1DiUfw9xXbxXVl-BxbOK4izruva34Qw_KHg11nXwXjHRKVH42Vtwrg3e3YVnX319YNhdt2TVADOYHa6GCVZqQ05iuMNLPwhUfMJ0t4Fe3jZx3WNwVM0JSOoFIxoU3_vYPYFz9dDU19oNDi_2UF3v2dKlZkf6Eibd8-k66FtyWEBgwdkzx3eOeA1JxXUDtoCq_LxHNg9GH4BG1JRs-C4iYqVRyg3gIu8UtsYSe2hUwzYvVqe0ely1ZacDH3U9r2EdXTFsUqyg3gCwrWMjyKwPRnqZYDwVbWFJV9INx6WMFWKU5UxMjHP8OTtsG92HWbg2573ocYSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=p-I0tOQHNzJBhf1DiUfw9xXbxXVl-BxbOK4izruva34Qw_KHg11nXwXjHRKVH42Vtwrg3e3YVnX319YNhdt2TVADOYHa6GCVZqQ05iuMNLPwhUfMJ0t4Fe3jZx3WNwVM0JSOoFIxoU3_vYPYFz9dDU19oNDi_2UF3v2dKlZkf6Eibd8-k66FtyWEBgwdkzx3eOeA1JxXUDtoCq_LxHNg9GH4BG1JRs-C4iYqVRyg3gIu8UtsYSe2hUwzYvVqe0ely1ZacDH3U9r2EdXTFsUqyg3gCwrWMjyKwPRnqZYDwVbWFJV9INx6WMFWKU5UxMjHP8OTtsG92HWbg2573ocYSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FY7DbqrN8inA0tFKlelS1DOtJAseBLP9OgkhKgP6yjnqSxv1RdLIGNBx8pjwn5CBi0XxhvpKjlSDKHqsfDPQwya5oV8jdfurr524No2H6Ry-Elqh4hJvuKvs0CSZJKh3l_0eC6MG91Utm_e61uQxZX1Styeb2nhLAgC6w4kUY9yHPXZi6tA8M6a-N8PTRQ3JM10QlOqvHcxJ60O_N9Dg5eB3IlmCKZNzd3Rw-_AAJbtauZvzYUSyVP2r02p69p9S-NnsdKfwsgH60_XqJ6YmDGdfngExgW4JGLketi7tlzz21RexoDr0ZvccqHeriMDJo4xM70rYLAhXJ6MJXDeifw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=JOWlVk_v2GQostvkHVshK6lxiv8CY0ZGcS_2_vq0YjyAKPOLMTSq1_qxgT8bjc7FKdSlxKQ7AuGy633zqMl5d2b5DegPftG70qrjqRq0di1-V99TwcUYtwbYdY1m35gFzB5m8WX-M80Ugx9hvxyKHMqhcVvwWbYz8UdttgmSZLWdTgi-K64c_LM9hxGirb93Gp_obcIsBA0G9ykDGRnINw-U1rO8fd1kXoLTdfZxMGA5kr1vx2inWLQpbyXQFsmEZCUBAT79U6WIeQzAlOwxFJto0UbC4ZU9Uxtbk1x_iBn6BsNymsWuI9DOz0pKWUNSdnnFlavPrRmqLrEYa7Hrng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=JOWlVk_v2GQostvkHVshK6lxiv8CY0ZGcS_2_vq0YjyAKPOLMTSq1_qxgT8bjc7FKdSlxKQ7AuGy633zqMl5d2b5DegPftG70qrjqRq0di1-V99TwcUYtwbYdY1m35gFzB5m8WX-M80Ugx9hvxyKHMqhcVvwWbYz8UdttgmSZLWdTgi-K64c_LM9hxGirb93Gp_obcIsBA0G9ykDGRnINw-U1rO8fd1kXoLTdfZxMGA5kr1vx2inWLQpbyXQFsmEZCUBAT79U6WIeQzAlOwxFJto0UbC4ZU9Uxtbk1x_iBn6BsNymsWuI9DOz0pKWUNSdnnFlavPrRmqLrEYa7Hrng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lKTJVBCRiuJNqgqLD1GcHWIoIrmFyEniZyPa9BrHb_sCG3o5zhCk8igiBUDmUXAtiWMCia18F-XqF82bCpGt0Ggh2em0O5OyHfiQ3tftkRZ_XmMJPtB2Ai8J5TNEePvZUH0wdB26-4YOG-4QJ10iPsRR6ybe9-e04jRXj8nMoPS7RgPVc0Wm5ltY-DeTrE6eV3A3eZyuKVygVlIFZFF2ba6wr20yEvximd3whJ3zEfXu6MHYCZRW0MxxvxrPiDhXj3_w2ou-dU_LVDYEz-PNV59Q1A9SXDYdh_uZAtpG_WIqo5rA4Bz3c8zoJsGNRgNiX88i6UwTv0qgfCfgW4_hVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=HMnXd5pOiJO5pz6vz5efBIV39GOQYyJFq0Gr6nrruwEDupNnx4mKDR58tQBnqzAvWSn-kYzGCoVuIqlx2fIxSNzLypEquhnOaP8DCTHxtRwldCmyNyyWJCJ7gFBMm-9oM5xOqa1cTMWpcE1tdXkWbvY2UJK63ElKzDO44SIyZOHB5CgjODwfk_VEIk3zD_cZJOI_YJPpFqWTdm9epiBWIq-lnqoBAmSHVq2ubHvKdc8-3JfanT1qBmIR1hC48lm64guNd1yD-qkFcA4VbieKlHE68m4hg5xNzFO-QIQbvFPgf5FDX44Rvt-mTZqEU4aZg3MCnIkSmXqmOhJgpAbeGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=HMnXd5pOiJO5pz6vz5efBIV39GOQYyJFq0Gr6nrruwEDupNnx4mKDR58tQBnqzAvWSn-kYzGCoVuIqlx2fIxSNzLypEquhnOaP8DCTHxtRwldCmyNyyWJCJ7gFBMm-9oM5xOqa1cTMWpcE1tdXkWbvY2UJK63ElKzDO44SIyZOHB5CgjODwfk_VEIk3zD_cZJOI_YJPpFqWTdm9epiBWIq-lnqoBAmSHVq2ubHvKdc8-3JfanT1qBmIR1hC48lm64guNd1yD-qkFcA4VbieKlHE68m4hg5xNzFO-QIQbvFPgf5FDX44Rvt-mTZqEU4aZg3MCnIkSmXqmOhJgpAbeGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OQS9WLc9esdrWlD1KPMJ5HJj9Ce5c0G1GJkHhOuhe8IVN81U8V7ql6RHMgEevKR43yO8H38PxacJC4u42gU8qtrML6AfEPPE8gmggMXrTPvD33yucK8x2T6oUPh5hBvRSttf2A7--wBAXbYkOFacEkgpwNSuaWm68TGGJz1PsY3aIlQFsgZC5CrhCbSHk3_8jwSbWBROxHqK_Fw8HZSPImYi7pj2iu-gWH0Nvc2ZB2s27J2XFI5Luym-0KAgWvf20xrz-r5IWxuOv8siK45kFyrkdZ3udeMXRQlDLjEIbJuDkHkIhz-t4p_EkbDt0FbLPf3CM7Xwm4aon6t6D-ilaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=qDwodr80nYray8b6_psL0D0fDq2w6rnvD6pjIS38TQLuSZ_MdyeVgCcRh0NeoSfpttsiudF14PcfYhWsmKPriug50ncYBssYX1vgt4g0iyB1TbPV6PLWS3FpwJwkeccNASXvdPaalxEVM4e0SqFgrqQ0WDJbLCt6wqfJBgMxAllymwyTGoWyELfHjbQCkZkx42IN0FA4W_SaIKSKEutLOfb3qv7wl1WWszBVGpn7K7sgKZFdi1FMmSdcVQ6OTIQsey-DFhRlkg1nwuW7dQonjLf7VnDJQ74u0TLogaRACaWUBatCSqkylZsdef339E02zuKnVw9CtuIuPUhQ9RnKhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=qDwodr80nYray8b6_psL0D0fDq2w6rnvD6pjIS38TQLuSZ_MdyeVgCcRh0NeoSfpttsiudF14PcfYhWsmKPriug50ncYBssYX1vgt4g0iyB1TbPV6PLWS3FpwJwkeccNASXvdPaalxEVM4e0SqFgrqQ0WDJbLCt6wqfJBgMxAllymwyTGoWyELfHjbQCkZkx42IN0FA4W_SaIKSKEutLOfb3qv7wl1WWszBVGpn7K7sgKZFdi1FMmSdcVQ6OTIQsey-DFhRlkg1nwuW7dQonjLf7VnDJQ74u0TLogaRACaWUBatCSqkylZsdef339E02zuKnVw9CtuIuPUhQ9RnKhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=hmijb5vU3z3ndmkxp1tmmBnnqCz0D6FgUfNUAs4KGmPUn4XpQxpboN7hewakDEhaNQj5ljQbr_6whC1ux7_KO335-ttsqZC6W0fbyydhp4hQ7jl8bLdl783-k4HiGC8584j-K0fKem2R_wvmciNmJuWU5lR8rNLRYRfZvVLrCOe8qsFGAia3bUS1OpCWWkEFdD0SlsIphn08TCNQnFGx4kbp1gT-Txc3Z8Umb047xhE9En2RcmyH5jxZprMgO9jWXx_3nJpG0sIWerx3bRTIDDtNpI0qENakL60oNN1L4EdQyvI1KPKgky4-dfuKHwPhY_J0oyYjWZNyiS585NShBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=hmijb5vU3z3ndmkxp1tmmBnnqCz0D6FgUfNUAs4KGmPUn4XpQxpboN7hewakDEhaNQj5ljQbr_6whC1ux7_KO335-ttsqZC6W0fbyydhp4hQ7jl8bLdl783-k4HiGC8584j-K0fKem2R_wvmciNmJuWU5lR8rNLRYRfZvVLrCOe8qsFGAia3bUS1OpCWWkEFdD0SlsIphn08TCNQnFGx4kbp1gT-Txc3Z8Umb047xhE9En2RcmyH5jxZprMgO9jWXx_3nJpG0sIWerx3bRTIDDtNpI0qENakL60oNN1L4EdQyvI1KPKgky4-dfuKHwPhY_J0oyYjWZNyiS585NShBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mp5a6Bh5cUzg5gKXTP9hcVXxDHk63EMUCtXhqEXFvH--ob4XCiu-CbmvN_M5CDtW8OccRyQLFwZZblyvJ49ufI8DVATmuPv7PiY5JgeIKoNLxdhrakKChV8xn2UidtH2MfWhzGDOmI-wek6CsSMSiw16qkiMxBvMdobbb0tySt231Uzn02DJUtuDcEtWAfXMPmAyxQGQtJj463kOURU0BfuTuV8e-qO3FCW1XS5XBJZswLjI0t2_9doMNxfxhQYc8GUUmyvkhoLEzorzLVIctnPUQGGiq-IHVHhFc2njIgtt0hvNF3yAMXFnNSllIhxeWR9Moq-qyR5AgYYOHV7bqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K6bUtHZDRVfkO5EeZCToLQ0KepH0VTFQlO2MPkagGK7YnssAj4FjXboaboYLLfYOL7s7vKiE_95FAif9FA4Ei8U9rROuN6W_AXRXHgOEIr3DiV7bpCO2gfUAYfYlRlTxqVhFR4O4t8-EtgCrPl-VWEJB9VmFhdvMU1VrW_JLDjPHVi-CJ-efuuhfBxtRdN4VboyZ0vwt0laeFY3hTi3sc7wUg8CFVRXCzhV1i0JdeQEDSX0b2yZECheD_HiEd2H63bdK9txrKHEFxI-C_yTlp_Ttf_UZppzPppEj30cP6ogTCWPmRdkCRBLNPKAqIM2Hsmcr5d8TnntYo4JCcXKlWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pt_p9oV92v2p-t4xMcIpaAEg35QhW8dSi0VudrfH22zsiBLaDTYW1DXrZLzSZWfEbPnUy4RuRgT4QAU5ojyXR7ypLPbdPQakJTnQSSvTq7RUsz3ZLkhDPR6qHEm5KOd47eSvN2luD4Iw09eGqGzrr66sJVH9YCC4lfY4sPchXVCc6eynTSCC54I3w7tz5cumRsVaTDRBhh1y3Gxmofy4p3UD99BP2piNiaO4L9HR-4XY9_o5MbZyABJ3f-iCYTp2v3ySiIqJz1481WSmVC4QAkLFUlzHlEgrbb_t1vjJgENxp2rexIUv_EwoxjR7IRH1wSwbSTBMpQ3Sf_jc92S8VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=HglqilS0cTAhB4247n5rhnbEAuHCw4VAK68bxIxgNawXD8mgRcksqCESkuRozJtwWaThpU0mNZHUNrhGHBHUMi5CsVAGVgT07cjKh67WOKZ48zGA-maTG4prGrI13eVcGJlLvmYZGpkYewvcjbkJs900GHDTq75ewLcv_o3IgQhhl2d95ZHypXO9qhH4fgfGZrgQ_NKJ7Hr2TZJfNkvuQlIL44Z6iQ3Q8JZZRq9La6JSM9K4HCBZefVPdqzcFZ319N9urjoujUcbU8UAJMbdfNpb9iPzhpuWcvvf5tihKSNTfqVH4peUi6nNSPHahfbIbA7nzKAUgXjk7iFJbQuNSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=HglqilS0cTAhB4247n5rhnbEAuHCw4VAK68bxIxgNawXD8mgRcksqCESkuRozJtwWaThpU0mNZHUNrhGHBHUMi5CsVAGVgT07cjKh67WOKZ48zGA-maTG4prGrI13eVcGJlLvmYZGpkYewvcjbkJs900GHDTq75ewLcv_o3IgQhhl2d95ZHypXO9qhH4fgfGZrgQ_NKJ7Hr2TZJfNkvuQlIL44Z6iQ3Q8JZZRq9La6JSM9K4HCBZefVPdqzcFZ319N9urjoujUcbU8UAJMbdfNpb9iPzhpuWcvvf5tihKSNTfqVH4peUi6nNSPHahfbIbA7nzKAUgXjk7iFJbQuNSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SQeM2U9dcYlVhGs4wTGRfYxzcl-SJV88uZkP9s30JWvyqNOXT-hhW3aK4wZmcr1APghuBsrCArIjFKh0ISKOo3V_vRwLqUWZR1Fuyz9vpjpvwMu5PwtR4wpv_asI80j_WStqvxtT1JG96_AsjVC7l3Ix3QXcPgGtL4qrH4vhFBXpUmIThzR8VrmZdvARMWiIBPksYbkLa0I46SHTzPCJhP0iXd3HWNnXCZWUhHhaObpjX_vs1uo-N8zvOj5IykjIOuwTD9ZcfJ17FtmSLUHcBsQoqdhWvYS9P4rvKW5ZXUKJgLZZRNNBLoGFZwrwSBG-6DumBxpxPy-UYhJezBYrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JhIUsaYteuRmJkznAvfvOzG5FdAkvy3YlNVg9s9HgISyn8h1M3hq_13PKPJyV4RKp3EGcCr12iJY0y8tjHcxEslEWwAC0hovbBLXPEeq_mhSr4tke7yVUik9h-L6ORa7TIvetiXa5Q2WIQNAX6R-3j5eAQiB_rVDVvVe8c1mEouZtsoMlgy0sNTLgJON8gK95vNNAvp_v2AKZBRACYevLHYEKjME8AWSTH2VSiKUOjJoVYtiW50s2j4CDnuoQ2UJRbwJTTCXBfA9b0m73jbOhp6uUrMFGfyMxtyFIq8gHWLt6tw74su9ivZf16O9VesBBMLsI_FtaCMJ8KOu49qlIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T0_Lfd_RCktYn_kqjRyP79reMXAKPa0D-ODyim3IM_QDz2c8PH-z4g_31qN0fUzpod2dVQbTs7hsgoapVkKooh9q02EzYP7NhQASJaov8giLkGZ33yJ_Syk0-abH0qNNhK65ZxJjGUs0ozfsqaK6re6DJZTmwypQVnJ-TFgHeHjnXNIYbMDOfvjjkSdDxunjMXZ12jHJnCW07Zkq5ja0TvEA0b82QDO6j1pUJbMftefkzT3vUOzm2gVcWhFKaqaeOrGIlCzzHuTnEZ06mDRD7eSWiIxN7X6SWfhz78dEBIKYNzxR_vwcT0rgCsqWJSmOv1MQv5GcukUie2k2ZCYqMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QO42EgTLXOAp0h7S971Q9RiS5jTBcnq89TC455vH4YEV9W2HpeCfUZZVW6Oj068yLT49lk0UrYrmy7-TXKj3nj401U1nONGYeth1I9w8Fa4KYJWP7hG1_04N2kDpw3s4KNLCakt0dU-ORPrF4Cp4pf0vu7iCwbtFsPRK7JAZUEd1CcOvCh5FJRVIrAgRHgpHbFr88KsOqoFOo-HXRSjq_ix7brrKOf84aNPH9ZzfIjisV-Cy2ugGxYGx7125qc7kOvafX5V12HMi5N-LjJ5hXj6d1OdJtAZ2n-c_OTUa_V_JCUe-Iva3g3StU1iTmTncEQyVovcUYxS1_UbnQglt_w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxfP4sOjGTaHqvDyODBz5Fqdkf84PJrZ9AWzPbjWHQTY3h-Gwj4cRky83nMW4Swkf2sd6aziC43SC08NRRv2N2cPUZ_WSmsWAA3RvlaW_1GxDWK1g7kbDjONxxVwfjV682f6m8h-49YAalZDYy29qANoaDHjev18t56bmg2BQI-Lpl6YRd-gSNDWautpXXOIZ9rn3Gu_DwgrSTQA1e1cR-_Kptk3VK-eF2rTkAbDVdmpgtzJw0uxfnDbMAXDOSfs2AB802mYHkrIj3tkv_aDsmYGEzH_4jZIpzQPnAlAqeMovtdpNlSQMWG3HWDjxcS_bnq2ZRmEpazYYmsy1HcPeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmU41QvsBG_cbJ4ozK_j_IzM6XWFQ8MVFO8Q7mI3muoriAik0Wb6Lq7-HXb1y3a3z42odjG_OshASNZpVW2_zS3k2CJstdVwuuMnHbM8_v5wsw90Vzzv9CCE0dsrHQ0phRoewR5FlbSl8gTSoF_0G_FnnShdjTtrp9ZlmczikfD-daGRTq9g4u-xqME9TlCG2CmNRMPn02gRexPzSB31S4SZHqxDqC7RAA1QVtB6_RZ2GrLOd4OJawWS71qIHknUKu7nS5OhfkB2D3q7VpmX6ZDoPhAydR0kpXVGuhdGo6aw7p_xNtp-10I_NGikPbK7qPm--K4d0si3jJWGtmV3zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P9Tll53XLuBX97uVZN82ShL5udokmNPF-X50eZXHJC3u5FJbBtJRF3jqykVGZMRfsF2ghs3MWiSSi3mhppFxcu8Rey6T3fNxrEWgJ8O9Cd6baQ0AJbVEDYUr02d7RTuLTCshKGPdba0Zd4ALpkY2Jna3zjnoPQmoC3yATJ5c0KXF-MwDoAyfQpSz0fu0LixKfiiHQKYRAk3m11YZnDGgE1ktxnXfLT1HoX2b-NTWuOPW_Uj04_Z4WOPBnoE1-dHfyQdsc70NgIHHq2F9X_VevZszbyaw9AzuWeTntuTKb1xWZyCsTems_sze9ECej2CYQAWrn8SztqOpBGjtYlxCJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Hy5gQCt-6dCRpWAuQA6YUNqsx9d4QGcapBQTbQidobEuWiP7j_cyEwRnehwdQKk2AwSxUgM4XCGVoQx-z2ynEaDfFdPz37BDbdxI1jGFilvfLUESbxtWQ2uOYShMENk2UQa85rTC5KWbUrt5Y7DOO0M27w2CYhUIKKXhc_XuyBSOKkpAT5BrM4Gy59dpCnEVDLXb5iMmfOAfG5qg0WfSWeflfZkD3CJH1fSeh62Kq_dDztRtxWOWrx0CA51-k2NOdouzggi1KmMi81d1SLg4s9uk3S0vjiHi9xB-cdJkq92M6DfgJ-gh1NLQb9bxYrjsf8tv6o-bf39Nnt1cDkZGzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=Hy5gQCt-6dCRpWAuQA6YUNqsx9d4QGcapBQTbQidobEuWiP7j_cyEwRnehwdQKk2AwSxUgM4XCGVoQx-z2ynEaDfFdPz37BDbdxI1jGFilvfLUESbxtWQ2uOYShMENk2UQa85rTC5KWbUrt5Y7DOO0M27w2CYhUIKKXhc_XuyBSOKkpAT5BrM4Gy59dpCnEVDLXb5iMmfOAfG5qg0WfSWeflfZkD3CJH1fSeh62Kq_dDztRtxWOWrx0CA51-k2NOdouzggi1KmMi81d1SLg4s9uk3S0vjiHi9xB-cdJkq92M6DfgJ-gh1NLQb9bxYrjsf8tv6o-bf39Nnt1cDkZGzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fm2RGp49UnpvBgzuOQSeYToY-4Zzwr14bd294R_Nj7UCUsXsvyJhZInM7eU10L_zYrDVOtvBJZ77MktaLThhBV96U2rDtMwwQYMCzdQsbDdWP5JpxKGwpAKkD_MO8KAhinZrZ0wszQLRIZtavqylS8b4fEA_kaZLlPUwWjRSPf0YRJAIK55r3CK2z91PPxXvY-v5hqcA_EEHHHsVUH4yy7DvBPSyxKstOWAgFJOJrISYTK7wivwlEzie2cPXwYQFt9nyZfURgb_jIMCC13yp4LzY7UmngbasNOqnE0QswDa0JiCLqY1sRyDdQXUhK3tmivq3x__1B3APTgg9EgYHjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFFQ4Bc4YkNyB73RMykhsP6R6NEoZ3yRK1QX258bqpVJzqxnwcgflGe4A1gpO_EorpQaID-rJmRBfHl4KnsZbkiqUfz0OPlWnRPZluXoqzU0wJ1Qrh5QMJf3aHFi7Jh8GILOlFYdV55DkyAvQSMNu4Owhl3Gw3AY6VcjK1_BUK_8afi9BDXDvBhl1cf6Fi2q44CWUpmmbzr87nQ5L12RPdbHfjdYUM6AtY6Yta6Od0tsiHUU4GY2S8ZY3Remf2LXVQyHWoTFJGoZ9YH2_YOZUOCB6NACWLrdUjHN66-TQIpdygzpV3N6dStNVH0itkFrNgyOBp3Wk_Rh0ejo5IuAMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=tSSVE1RsUpCkbimmxfO2sgLfFX3-7kTFyG27vhw3_sHW_pNm8jjf2cXEsYEaEoRpNqWwh_c-aDD2o5OcAdz4YZt9LbBV1CE0GUNxN0OJlD6HP5lykZAUddfTLRg2I5OSHTO-T16wA3AWBf_jt8OYoynlW95YDyzrd4loDyADoEsojBv0elm3ZYs5hwfQgNLgtAoHzcDnwp4d-Iqwh_MeemxLsu7AMgNNwXUcZj_hVofDoFZcE1LoHeDIoTjO6F-JmXXW-_sOiLG8Ed4ImYZhXuARhii9bpCaoIi6kOG0Ti5aUD57Ob-6ubw3TIxMOPuOjezv1uEDsw25_rx-YRqkWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=tSSVE1RsUpCkbimmxfO2sgLfFX3-7kTFyG27vhw3_sHW_pNm8jjf2cXEsYEaEoRpNqWwh_c-aDD2o5OcAdz4YZt9LbBV1CE0GUNxN0OJlD6HP5lykZAUddfTLRg2I5OSHTO-T16wA3AWBf_jt8OYoynlW95YDyzrd4loDyADoEsojBv0elm3ZYs5hwfQgNLgtAoHzcDnwp4d-Iqwh_MeemxLsu7AMgNNwXUcZj_hVofDoFZcE1LoHeDIoTjO6F-JmXXW-_sOiLG8Ed4ImYZhXuARhii9bpCaoIi6kOG0Ti5aUD57Ob-6ubw3TIxMOPuOjezv1uEDsw25_rx-YRqkWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pn3Uomilt4dOGVS7H4pxOt2H930GiSRsg6KIoOD1vIBdC1w5NFgF_Hrppklqgfz-nz4Vhp3iHWjiga6KlamyoSMlq602wado4aURutvUggm_MpMOBE9iXuhF3N8jND4qoFtRmI78dZuncsHaZlMl2ZtcxPcmy4ZFPDpasrMGN0CT32rKWll3ip-rlu1eQ3Tq1dyVtX3ZoKetd9JtzIyK_x6G-hcqdSfOISu_jwl2meiT5AAm2wJYXwNj26-tG9x2U_yBdbzZC9A6ATAptr1fbIgS1EL6O4F5P1baA0it2ZO_2JfNvho0eU86UaLe6w6i1Ic_z_7I8qU13GwSeH3ENw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=HZP0CCA1U7masOYOpMonL6LhqAPouYr-tAok8z3meGVJBC6OzW0-ne37ETQfSv6ayLwq1JD3U1sxNqx2mS-c3jQwM47G-brDrKK5r-8hR_VLUo9AeZobfI7HRQb8DzDPeZb3VC-766Dpwu9myjJRxZN9-pc-CDmvgU8S-Dgwwrr9gtnynSnA0DA2u_r3pxdHPpQ2FAPnHHq0OHjx-n3gA2L3UizHFQfg9XfzkiBQ30pUaacMCIYvxnttYiQ43vT97xb7MIbVnh9iV0gts2QBhD-IlpGhmA-V-_d9gSqC4cxNAiGDplIEGIWqPXpYAcXgH1MjM6rtLeMouEEbMPKFJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=HZP0CCA1U7masOYOpMonL6LhqAPouYr-tAok8z3meGVJBC6OzW0-ne37ETQfSv6ayLwq1JD3U1sxNqx2mS-c3jQwM47G-brDrKK5r-8hR_VLUo9AeZobfI7HRQb8DzDPeZb3VC-766Dpwu9myjJRxZN9-pc-CDmvgU8S-Dgwwrr9gtnynSnA0DA2u_r3pxdHPpQ2FAPnHHq0OHjx-n3gA2L3UizHFQfg9XfzkiBQ30pUaacMCIYvxnttYiQ43vT97xb7MIbVnh9iV0gts2QBhD-IlpGhmA-V-_d9gSqC4cxNAiGDplIEGIWqPXpYAcXgH1MjM6rtLeMouEEbMPKFJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVcYDW5qwpWcBKxQQNPKyg0u9_-HRbDi1S06M8kSFSORA92QLsigDl6woUBgjkgQ67h1Ljs9UnzsOHDGLt8UJDVaDZsNhgsIapqwtXre4ty4yY9iWpD-S6Lmvk8kEErxtDq1bGXX_RgJcR_GdBHedjfc7v6Sr3vyJDisL7-j6DohfGTms67CPROFK5lvNNkk7Ana8vafo_Br7Xhq95xXWnvCi8wihabJmwuAbVh9EIJwQYPC8AK3H6lBHhwBymgQ615FTsdQyxb3Tw-NmZFB4NQNC7T0Dlrfyk7ug5zlQ2kxdIs5wjpjmADtSF1ica5nlfNFsLBNPA6t5LbXcZt7CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=DSDLf97mYxMFcF5YQN85T7C1Op7GMgTqcYlLYdKJ0T0sVrOYA-4rqwaPmWj__8nFVpbxLh-1jroAadLE49D5hM5Xb-A76vNdCehgUEdjeemXO4_ylUWrdkFvHfvPyfeGnk3gyFIdGWX8bEJUvtjnl9QjZCh-W9lOEngL6JyH6voPEujuIo-zUBxQeHAYZWd1htRsvOJKgo9rsVOUIi_3ujZa9honaVGUsscQK-CQCKoxCsWjkQGq_UeNm6lKZokashtifYkZxhznkEZtJgbW5hdAc3zx7Y5MRpoNlBg-8f72iducQ533OOVc7oVfoxDc6IvAl8OV0U31Sr5huDDkrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=DSDLf97mYxMFcF5YQN85T7C1Op7GMgTqcYlLYdKJ0T0sVrOYA-4rqwaPmWj__8nFVpbxLh-1jroAadLE49D5hM5Xb-A76vNdCehgUEdjeemXO4_ylUWrdkFvHfvPyfeGnk3gyFIdGWX8bEJUvtjnl9QjZCh-W9lOEngL6JyH6voPEujuIo-zUBxQeHAYZWd1htRsvOJKgo9rsVOUIi_3ujZa9honaVGUsscQK-CQCKoxCsWjkQGq_UeNm6lKZokashtifYkZxhznkEZtJgbW5hdAc3zx7Y5MRpoNlBg-8f72iducQ533OOVc7oVfoxDc6IvAl8OV0U31Sr5huDDkrTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
