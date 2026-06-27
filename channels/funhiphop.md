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
<img src="https://cdn4.telesco.pe/file/txEDj6jrL0VBS5W3Ml8mgcXNWNzRtkXCTciQADms9K536QgiD2y0vH8NH3cIB4N3BDRnybWkPegWz_EOtdP_6TtFHH1Osl7ISGH2QVBpRRCsFbrMY5CEno2uBoTru_bjxdJ-qNxJSXyh_fOGd738oxINHIT4tEmnAJ6c6p7vl7dqYPeZUvkXWzR2EhgG0imafB0L4NYRA4Dj3mO1xQS4erpR-8rYaAdKm3uRMuOs85cKBhEIQ46tUkDvMXwctt1LLpn4Xlso_1Jt3jvlDs1Ae0EIN5Tr21DvZznf07CXvR-3zlz_eN0wCCuqSoxcoNhTDkFLD2bjRfZziujCC0sW_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 184K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 09:53:06</div>
<hr>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">چین به اینترنت 10G رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 936 · <a href="https://t.me/funhiphop/78882" target="_blank">📅 09:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">می‌ثاقی:
اگه بازی تو لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات درست و درمون var نداریم الان گلمون آفساید نبود و برده بودیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/78881" target="_blank">📅 09:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VA4PdB2M3Q3xMMWiaAZsVPPsnmEaUzmIgAvSygRd3gcOuxmF-lblSp9SEmgQ7R7lYpBY4ESv1HRuhMZRfS2dfPQDCgQX87JW29vk1LmrFZAmWls6VEmLGIP-RnlS_qktQLo3809inXmug5Osm6pPhTzdW-iBNLukzjKZM10GkSCYPQzVu40eXZUoPyhoeB37L3xtY_oJiFQ422LbagNpZvf-kWAbfl8565jMn5DYb2VVOZNVo53OFPVthxIQsLaVOCSYpPZ5YdDmIXHkJF9DvW6TIFReXHnpMDPzh0JgR1JR6krvrcg5re1f2E7-TvV7EFic2lXTy1PBrxrE2KbMfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوست دارم بدونم این شیر ایرانی در چه حالیه الان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/78880" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.61K · <a href="https://t.me/funhiphop/78879" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQdfVvg3tOK4o6tRd6723pD5zpMNTZzW9V2gtj0zquMi8dpfD4aRit4Z4nJAliotJENTcG2F6MnSoPQy3nh2f_tYnkZ_r5q8QN59xCiPQG8-oUPR9jWrDm3g95pveZGr047VzuBnEZOIXgbbFRJeRjKGBRdAJX2bIjEgKJphtqxdPNgwUqPjgcpdFsU5HsHAj83k-8qrvy7CPgu2QHzNBlkUZwnorbr7_x0-6GGpH4KsZBTWWEQFSVTZyY9xf5pOqM-nCvDYzAtOVOFKhDyzPC2Bwgl6ZRaSeaZAlzLCX_IDZyG4WNOz-oECEPlaDwmmfEyURj9EktDryVmL9cWQAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی عکسه رو سریع بگیر تا نفهمیدن کیری فازشو دارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.24K · <a href="https://t.me/funhiphop/78878" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">رو دیوارای تهران نوشته خدایا همه مارو ببخش بجز طارمی، مردی که ایستاده رید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/funhiphop/78877" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=AHdq57_T0IEQrNM6E4uQTOY-cGnSaoCmu8GvzuCTHB8PyqXgBRO5V0pqr85CyB-mNYzvUFm7Y_jEJ568jSPVzBDGbzkZ9BXbB0coiArA8M3QrOKOOTSgBkdeKjODa-Bzr1uQimCZ1uGLBQagnf6QB5_-K2sYluFu7L0tUTCAYLLqrwW2pi4JvauCcIF8oqoWR2hMRSUaLqQpwRRbSYD3GTkVKKR4ZxdlY8_W7PfS2YmRxKmh9JANVQ6PLDPnOAE6v7DdHZqb1NejwKSjCJr5_9U-IGklNsOL-qoahy5SvxBUAC3VLs2zI02oGfz_OAvsFXbL_hLbku36dNlxSdXmSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=AHdq57_T0IEQrNM6E4uQTOY-cGnSaoCmu8GvzuCTHB8PyqXgBRO5V0pqr85CyB-mNYzvUFm7Y_jEJ568jSPVzBDGbzkZ9BXbB0coiArA8M3QrOKOOTSgBkdeKjODa-Bzr1uQimCZ1uGLBQagnf6QB5_-K2sYluFu7L0tUTCAYLLqrwW2pi4JvauCcIF8oqoWR2hMRSUaLqQpwRRbSYD3GTkVKKR4ZxdlY8_W7PfS2YmRxKmh9JANVQ6PLDPnOAE6v7DdHZqb1NejwKSjCJr5_9U-IGklNsOL-qoahy5SvxBUAC3VLs2zI02oGfz_OAvsFXbL_hLbku36dNlxSdXmSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت سرمربی مصر تو کنفرانس خبری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/78876" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ولی امروز دیگه بهم ثابت شد هر پیشبینی کنم برعکس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/78875" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IkAljcj9YnLOQNtj0M0fRI92_avX0E4zdavG2ib_eq7_bYnEMldaoKd9q4OAU76B6wqYW68IXwaIH3WRqREdIGiNef2lCiAes3aFkxVnXBp9lAnsms0d_S9wPnl6bADp323hGp_XQiQbfn5QD0KHpoI0S6GOU7sibW_4UAeNEKG4OA80mF_DUS8GsTkQW9_oUiGn9nDEBFD6QFh3n2GxnIMBSTipIoq3FbiRTjJw0OT3RzS7Te0KKE6wzWrgDNHy17UnJXE6ZIOIqglXGsRpHuiH4CjGxLld4keQ7M6ViUmBa5X2Qm09mI4QHKO_EJoAbgRPkdQf0K1ymFSnFxBh-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر عشق است
گریه نکن رامین جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.06K · <a href="https://t.me/funhiphop/78874" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">احتمال زیاد تیم قلعه نویی صعود میکنه و به سوئیس میخوره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/funhiphop/78873" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،
2: یا کنگو نتواند ازبکستان را ببرد،
3: یا بازی اتریش و الجزایر برنده داشته باشد
هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.97K · <a href="https://t.me/funhiphop/78872" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ah_WeqOvPC9Bj_Frc3ngqRg7OLHfCAWEn9NvhnDa7ckqApnKceUDedMlqSOelI_F92o4ZXy7YresPdPlwolO6PT5UoBJg9eyaGYUto77To7jy8vusTkuRMyiQkpS0dG4Y_BEYsNY6znDsk53-KXPUFgaMyDcOQYWZ9WBUGMDhoqnOe9EjdK5j-Mn_8DHqlVsKnUcRzG2cj3EO95ZdKimItYTCs5UIP3TZXpWHLxAu4eYoiQvUovvPg2o06rfin38rWADiWZlcWQGJEqXCdMCeM6atoQyisOpj2a8TrDdX4yZK3WNlStopExACod6KOylMVRxTK7hbc5yVDOLHEwKDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ ترین کیر شدن تاریخ فوتبال
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/78871" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78869">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">شانس آوردید، ژنرال فکر میکرد اول گروهیم، دقیقه نود بهش خبر دادن که برای صعود به برد نیاز داریم وگرنه هفت یک برده بود بازیو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78869" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78868">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">رد شد
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78868" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78866">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">حرومزاده اعظم گل زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78866" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78864">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حسم میگه که مصر میزنه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78864" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78862">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">البته یک صحنه کاملا عادی بود
هیچ جای نگرانی نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78862" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78859">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">یکی به مربی مصر بگه صعود کردید تا سکته نکرد، قلعه نویی باید ناراضی باشه نه تو کصمغز.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78859" target="_blank">📅 08:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78857">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خود مغانلو پشماش میریزه وقتایی که تعویض میشه تو چجوری بهش بازی میدی نیوکاسل.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78857" target="_blank">📅 08:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78855">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">راستی این حمایت از همجنسگرایان چیشد، چرا صلاح و طارمی لبای همو نخوردن؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78855" target="_blank">📅 07:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78854">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">الان باز مساوی میشه کلی آدم میان میگن پشمام حاجی عجب بازی کرد این تیم</div>
<div class="tg-footer">👁️ 8.65K · <a href="https://t.me/funhiphop/78854" target="_blank">📅 07:54 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78853">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">صلاح تعویض شد</div>
<div class="tg-footer">👁️ 8.62K · <a href="https://t.me/funhiphop/78853" target="_blank">📅 07:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78852">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1e03861f6.mp4?token=HF0KlZ5ZOY43pTF7eo-F25JCOXidpK7C5npbV29RSll67dyA9JkzzPyNEwctCgkUoJbA3BP24hmglnEKJp7ZCHGVY-Zaq4N0GpjEKh5MThUMHsQYxURTv6Ug2rPo54NWDv2ryDzWzWF9VfYbkd1DRWkvzOGQg-A3zi-Jxdbeqknt5NcK7Vt3STr7RBPyz3tNoLm65T5JMtj6WDc_Y7p9Er1FdqbDayPhxi5Re0Zg_0wB87AYZHMmdniCs86iWewC_H70qx0wBarXZHXjzDLQUuuNWfdVXwxvy9WT7p0whGfoHUTv6xlcG9_MT4JouHq-IckDrDEQdg1_FDiT7mlSBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1e03861f6.mp4?token=HF0KlZ5ZOY43pTF7eo-F25JCOXidpK7C5npbV29RSll67dyA9JkzzPyNEwctCgkUoJbA3BP24hmglnEKJp7ZCHGVY-Zaq4N0GpjEKh5MThUMHsQYxURTv6Ug2rPo54NWDv2ryDzWzWF9VfYbkd1DRWkvzOGQg-A3zi-Jxdbeqknt5NcK7Vt3STr7RBPyz3tNoLm65T5JMtj6WDc_Y7p9Er1FdqbDayPhxi5Re0Zg_0wB87AYZHMmdniCs86iWewC_H70qx0wBarXZHXjzDLQUuuNWfdVXwxvy9WT7p0whGfoHUTv6xlcG9_MT4JouHq-IckDrDEQdg1_FDiT7mlSBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 8.47K · <a href="https://t.me/funhiphop/78852" target="_blank">📅 07:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78851">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">رامین رضاییان اولی رو زددددد</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/funhiphop/78851" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78850">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پشماممممم</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/funhiphop/78850" target="_blank">📅 06:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78849">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">طارمی پنالتی رو ریدددد
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.66K · <a href="https://t.me/funhiphop/78849" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78848">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ریدددددد</div>
<div class="tg-footer">👁️ 8.6K · <a href="https://t.me/funhiphop/78848" target="_blank">📅 06:41 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78847">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بازم طارمی با کصکش بازی پنالتی گرفت
😂
😂</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/78847" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78846">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">پنالتییییی برای ایران</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/funhiphop/78846" target="_blank">📅 06:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78845">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">مصر اولی رو زد
😂
😂
😂
😂
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/funhiphop/78845" target="_blank">📅 06:36 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78844">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توی این بازی اگه مهدی و پسرعموش تو ترکیب بودن مادر مصر رو میگاییدن، دلیلش هم به خودم و همین جمع کوچیک 180 هزار نفری مربوطه</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/78844" target="_blank">📅 05:37 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78842">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/H9OVptWZp7o5GFSWfysze6Aob55DzW7RqDUno051ZFgGEjhLFCFU960xuxHky1IDNpcydO9IZIlV7qPpYima3rQYDLI1VFBjb_eB91naJu1KGzhC5lw2fywCdHgcZb37aLCE0hdKg0xVfA8YeKSpfSMQQ7HylKQOPHxfX3ILsq_8biqgaXdYo-LHOe8zRJ5aJo9OzStD9Ia0HiQd-QgLXKz9FRjfAaF3w58tajYWGcBfSgPfSzuEq62EqTypOwNeLV7eIBBj67DZLSA3KGC6LVuotPrwh2_NhQD956JBEkvOFKLe6MGOBcvxj_k62PGTiwAb5U6_Pyrx0FL9FErwrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PaPsAg-85vU0gIwssfqh39B4AuL9sdLHlNwHRlTJdI_RRGhWdTCGGDLRupNxqAJSepI8wJC0ducEeHigWQxB-9cMFXTA4tFTlLoqIPOaK-JdVzmrQPIy7ZaNWptFdFlOsCmGB8nmcosf524DCTA1eAxSru6HudoTyU5iG3zxOAlzlfTRy1_jawiz4QADSqQvga6y7pM1tOV0TXrrYJN81wp1YoXPYOMoQIhy8IYa75DZaZQp5Ww4TPP4P85P1qey8HYLB4vGqynewQMR93mHfls9LtL9MOykzMkAM52wEsCKu8kzDxbKknRTiPXcIxrMEjE-JtDDwXTtK8xvLr2UHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">محبی داره کیر طارمی رو دید میزنه؟</div>
<div class="tg-footer">👁️ 9.78K · <a href="https://t.me/funhiphop/78842" target="_blank">📅 05:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78841">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سپاه: بخوابید خیر است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78841" target="_blank">📅 03:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78840">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یک خبر دردناک رو الان متوجه شدم
متاسفانه پروردگار و اسطوره بی بدیل تاریخ فوتبال، حضرت لیونل آندرس مسی در بازی فردا مقابل اردن حضور نخواهد داشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78840" target="_blank">📅 02:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78839">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">سنتکام: امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.  سنتکام این حمله را…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78839" target="_blank">📅 02:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78838">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U0CFGRXgzt0eIVBifrAV31j667IYZFeYF2ooEkqeEm2pI-kuyohKicOkRa-QfXdFwkw4Okrfpa8NJSuj5dFlIfRk12ifO8FQLc4aN-NsJagXUIPQQbnGvmN345nPHbzn1FFisEXr5E-jSMvAzLovfQO5nhLpcGdEfTMcwXG5huyxV3YHo2rJc1QGjl21LbMlkqHSVACbAvcktJ1DPZ2Tt4rX9GGz0641uB_UPgNPc85o4kTdob5XBgjfgAyg95E_I5xnsffZc-rMAgN5wLLQ6QLiXrhDhkt8uAaNBgKFAET14k9JYYAlmg9DHKu4nU5th6uZNer2bMSUBIP5KR2iGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب تیمی میشد حاجی
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78838" target="_blank">📅 01:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78837">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">دوستان چطور میتونم وارد بخش سرکوب اغتشاشات ارتش لبنان بشم؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78837" target="_blank">📅 01:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78836">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ترک جدید رضا پیشرو و علی اوج به نام شهر خاموش منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78836" target="_blank">📅 01:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78835">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترک جدید رضا پیشرو و علی اوج به نام شهر خاموش منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78835" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78834">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d2g8nVBxXITPr7o12h6w_aE-e6NhpaxoR5bhfyotThyiKqikp6zPrpD4bi7T8xF01JX2zMU8YKanHSMoHDR84lOzJbJJybqFzRx0HKTUotrAucdANY3AQEThqHL5EsYnYAK9mKtSfUvWmVNiNOF2WcyNrvPMCoQslXwrTc_u0v492PVMZN9WZorWME4bVAOz6LxP7ctmuaRJ0y0tRcqkebNL51smF6rgjJHtaT9twUw_b2HySbLhDTrqM4FSK9kCSdQqfoijKLA4ZbUeLtWz7h9cMgXqO7fDd6_Xq2fnfI1z3EdvMBWGvxdkiGmmiuwFA6bxRp4BMSCjXSB6DUxKbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید رضا پیشرو و علی اوج به نام شهر خاموش منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78834" target="_blank">📅 01:33 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78833">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K05aOPvzS70EQz3FyHNpDWxLK81Sc22z9aoQy0D_V0jEI6RfOtkHc_0eJmI5XAJeyrupfKh45IQtrJwHHM_i51Yetxk8I3L-hTAUbmKTwaDve7bUrzkV6-PSPjEevZcdOao9-gn9lYu-RXvzysN_WdHXL1tPj5KV0MuwJJKqI1neo35E_OdxM8_AGEQgKTvzLEQbS6m9h08xBES9Vd3fdDszp_oZG00xIskVEtERAs2L5bOhEri_ZNyZF_KjidBxEvTkKuZ6Ec9DxcN-UNL0P79_jVEn6insxgvqtatRbXkoAHyvBioD4P1KglAIXlFm727XwygtTzfv8mbAYOBVOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«اعتراض بجا است اما اعتراض غیر از اغتشاش است. با معترض حرف می‌زنیم اما حرف زدن با اغتشاشگر فایده‌ای ندارد بلکه باید او را سر جای خود نشاند.»  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78833" target="_blank">📅 01:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78829">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5vYrq5sdeo14B0mEnNl9-gOtS9orUbSo2eYfPMtHhLu_m4-glzt7aJPB27akkVplDZbYN0RBRAaOLaoN45861mHhM89bUPzUX3Elp-BFasZi27w_fbAMh04iWpDPvPpaeYlHzhiefOCl1J4s8vIj9ajOSbH2xJua97l26tYWEl9MMyI92s540cYOV0Db99KAokxVGnlEiiXQ6pAeadiuDEtDkeDaO7B6KLyXmBcqac5f6ql9_ZYRNtrah0ocpZddFEdtljAe3zPNhD14NMNoIBcjcohp1ChGF6fpmxiLTpjo-8r4fCaNejhAzUjQkJ5qSwiQmjSk6VO8J5BSRBOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a599e4c2eb.mp4?token=jGD2hO2P9e7zJ7A1yNWksGNgJ4qG39TVqA5mwzi_fX-EE3SNM_5uDuzZiajO6TrsR2aEaUV8WAOvu1OZf3ac3SI7tqNLgQMmsgQ7XaCkRM-Zl88sZnTKBbFbn2D-UWzxvnHHKdG-ZBs_JFd26iVSBTrbc2Z6SRMAezJrLSKLgsghNNtlpA8-nS2qGabOA7EA3tXERoaSpCp-Sq9351dWdKfqdLD3JCeC5lnVUzsNVvfeR5CzdMYEXQaN-AFdmKqCzmA8eqlaSXh_H4UM4h3_kJBqJgH2tx-dEyaZZyxfnl5mFk0k51yF8b0Qq0HYC1oiS7dvGLE3Wt-zFD7mcrLnHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a599e4c2eb.mp4?token=jGD2hO2P9e7zJ7A1yNWksGNgJ4qG39TVqA5mwzi_fX-EE3SNM_5uDuzZiajO6TrsR2aEaUV8WAOvu1OZf3ac3SI7tqNLgQMmsgQ7XaCkRM-Zl88sZnTKBbFbn2D-UWzxvnHHKdG-ZBs_JFd26iVSBTrbc2Z6SRMAezJrLSKLgsghNNtlpA8-nS2qGabOA7EA3tXERoaSpCp-Sq9351dWdKfqdLD3JCeC5lnVUzsNVvfeR5CzdMYEXQaN-AFdmKqCzmA8eqlaSXh_H4UM4h3_kJBqJgH2tx-dEyaZZyxfnl5mFk0k51yF8b0Qq0HYC1oiS7dvGLE3Wt-zFD7mcrLnHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پس از اعلام توافق میان دولت لبنان و اسرائیل، طرفداران سازمان حزب‌الله در بیروت، دست به اغتشاش زدند  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78829" target="_blank">📅 01:23 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78828">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">پس از اعلام توافق میان دولت لبنان و اسرائیل، طرفداران سازمان حزب‌الله در بیروت، دست به اغتشاش زدند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78828" target="_blank">📅 00:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78826">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NrJoiV40PGQZzCV7fHbsz-_balpaVaGJW1fV5O0lxG8YrvO6gZn5KQ3-Z_8mgRq8L4sXv4hwXJtk-4n04-MtqZu20r__dT1dzv8NVzUoBRwrZA3DNBuBmd8F6R1TH0MvZIH467EpEhQ4WSHa71lJ0BF-W5OsyHtRymAtVtDa935nu-dJhaD5pPeTktMn7HP_M6s1g4L49G6eLIS9G7KZgCJdOSO4W-8U1cYVX1bmLtl5txL0MkZ6lwXXggNvA10_MdbxebTziEaGJs2oBlzjYJNAjI4qEr2UoYvJJb-5h6EbojOVqvKQpoCCg-3khbFXNRiWAdGrnFp7PKcmyznVSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78826" target="_blank">📅 00:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78824">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">در پی حملات آمریکا به جنوب، بیانیه سردار تنگسیری به زودی از خبرگزاری فارس پخش خواهد شد!!
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78824" target="_blank">📅 00:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78823">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">سنتکام: امروز حملاتی را به سایت‌های ذخیره موشک و پهپادهای ایرانی و تأسیسات رادار ساحلی انجام داده است تا به تلافی حمله پهپادی ایران در 25 ژوئن به کشتی باری M/V Ever Lovely با پرچم سنگاپور در هنگام خروج از تنگه هرمز در امتداد سواحل عمان.
سنتکام این حمله را نقض آشکار آتش بس و تهدیدی برای آزادی ناوبری خواند.
نیروهای ایالات متحده به هماهنگی عبور امن برای کشتی های تجاری ادامه می دهند و می گویند که برای اطمینان از رعایت کامل توافق، هوشیار هستند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78823" target="_blank">📅 00:21 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78822">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اسلام تو این جام جهانی کاملا منحل شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78822" target="_blank">📅 00:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78821">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">بنظرتون ایران از گروه خودش صعود میکنه؟
😂</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78821" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78820">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بنظرتون ایران از گروه خودش صعود میکنه؟
😂</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78820" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78819">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام: با جنگنده های اف 18 محموله های ذرت و سویا رو انداختیم رو سیریک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78819" target="_blank">📅 23:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78818">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">این وسط از سیریک باز صدای تفاهم نامه اومد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78818" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78817">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">این وسط از سیریک باز صدای تفاهم نامه اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78817" target="_blank">📅 23:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78816">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">این همه گدایی سهمیه کنی بعد سر بازی اول پلی آف اینطوری ببازی
خیلی زشت شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78816" target="_blank">📅 23:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78815">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرسپولیس گل خورد
😂
😂
😂
😂
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78815" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78812">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دمبله امروز عین آرین روبن شده
هر سه تا گلش مثل هم بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78812" target="_blank">📅 23:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78810">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بهترین بازیکن جهانو</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78810" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78809">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">هتریک کرد</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78809" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78808">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b88dcbe7ad.mp4?token=WXWLGUcWJBfCUYzDWl6aN_HyR6EV91C2LhuaZAlNJDEb-DTiaVrfugg0O7wMmFpLLVSdbrreHLCMIzetY_bGFOgwIJT7-NkRclkbudO997BNcLtLPJbkZePOPy5omOXvgtp_59002bajeXxaCJub1SpBh4iU97GvufPlGZBFs8HVbBEtRLVJCed2H2xoUXh4-8xSGgg_syfx8oB73s9NqiZE9dl9qwXpF0vSo3hT5xrWmEpACsqHehc1Ok1iNwpTeoGooBpU8TsuxAWnJq2DkDDsPwQWjnNa3-ZfBXdoDwVJ_IMJmUhCZXI1aDJ8ew9l0tNy_-fRh1EInw8huFA-Eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b88dcbe7ad.mp4?token=WXWLGUcWJBfCUYzDWl6aN_HyR6EV91C2LhuaZAlNJDEb-DTiaVrfugg0O7wMmFpLLVSdbrreHLCMIzetY_bGFOgwIJT7-NkRclkbudO997BNcLtLPJbkZePOPy5omOXvgtp_59002bajeXxaCJub1SpBh4iU97GvufPlGZBFs8HVbBEtRLVJCed2H2xoUXh4-8xSGgg_syfx8oB73s9NqiZE9dl9qwXpF0vSo3hT5xrWmEpACsqHehc1Ok1iNwpTeoGooBpU8TsuxAWnJq2DkDDsPwQWjnNa3-ZfBXdoDwVJ_IMJmUhCZXI1aDJ8ew9l0tNy_-fRh1EInw8huFA-Eoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دمبله چی زد پسر</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78808" target="_blank">📅 22:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78807">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اوپامکانو چرا از توپ فرار میکنه</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78807" target="_blank">📅 22:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78806">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نروژ سریع بک داد</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78806" target="_blank">📅 22:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78805">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دمبله چی زد پسر</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78805" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78804">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">بسم الله الرحمن الرحیم</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78804" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78803">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خود اوسمار رو نیمکت داره بازی فرانسه نروژ میبینه بعد صدا سیما داره بازی پرسپولیس رو پخش میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78803" target="_blank">📅 22:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78802">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">فردا تیم قلعه نویی مصر رو تحقیر میکنه
بماند به یادگار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78802" target="_blank">📅 22:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78801">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">خوار نروژ رو با لفظام گاییدم
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78801" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78800">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دمبله زد</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78800" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78799">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">امشب رگنار به نوادگان خودش افتخار خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78799" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78798">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">واقعا چطوری تونست به هلو خیانت کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78798" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78797">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">مگه اون سمت جدول چخبره انقد بکیرم طور اومدن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78797" target="_blank">📅 21:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78795">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7XteEQAOS9HhgNu6P71AXp2DjT4QKQw2tpt-oezTABcQprZwh5scD166BoWayoAKReLjLJEkOntOZigR4jTYnNs4QdtSNLBUM_GtkKe_1AfPBWWg0dJ_VJZWNhU2OcianaEBcZSsY14suSUkgArET-Sb_Ur3-BKhyJm7S06zVPIrQkAPnk9XoW2avZFrOWS4LQQDnJeQDbODp4JjpbycSWJ3Aod5_gpVr0JEE3CF7cfA8wO6X9TpMjBMjtGvFyRDxNYQOQfWw10i3PsQUfY6310yGX4arQ5wf7a3-tO-_CgvwH0yMSb5lJtL31PafwEhu6BTtZXwZgRooBM-3U7Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78795" target="_blank">📅 21:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78794">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">میلان چی تو گونزالو راموس دید ۵۰ میل براش داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78794" target="_blank">📅 21:14 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78791">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxb2nrvaQTDujo0NKj3Hm-u-QLkSJ1NNnc-iBtTvbS4cpL7CqccZTdKxwGoXDQ5ywCQSJkvTuftxhzV6PxG_4m9DFxZPb9kAUH5N44t1iYw7gexp4-obadfGSS_SM72YjsxNCOj3-Y_pSG4Y3nZ7mg__k6FVUUtnOECP2RBu28TeXAaxBfgJUHDvv_PXjGWG4qCuzEoIe2p01gwNiFxMFU-DgptDzxW2JsobTE2GSPAv_PnRAnhFrPjG0EZvlsjmmropRwVZyoj7vtmizP8jHq1u3RTG331U4qxckja8yl8UeLimM9b7lyNIOtXR8v1q6PMEbGvQVieKxU4eDfodFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجب بیف جذابی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78791" target="_blank">📅 20:46 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78790">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTFJdPcvbBNBiorgNNsscAEWC2rCNY9t17PR5XjelfWiPrFqASK20nFtVHkGzZ5_i_qYEKPjH4akLso32-9JK4q65sxvkNbc3sUO8RgcTwCxWTcH-AlTwviwAQ6CgwvRWPkvJ6MM3MQBY9HWHlUluOl67tVj_uxJ70G96iw_I8w86WgTk2NqWzyprJAA7T3z8xF9r1jXOQZYPW3ln6z3LXu4ux7JwKeCcJtJLlxjI237HEEOykgtVwfm1grgNX-mftqGA36c4aqdBn_DR8Z4i7iKGpbjATT3Z_0ihi5sSvOMvUq21MpRPmG_ZlSRqt-A790Ur2d4dhzW2uYV4XkGnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارگردان موش سرآشپز اعلام کرد که قسمت دوم این انیمیشن هرگز ساخته نمی‌شه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78790" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78789">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromApexNet Shop | اپکس نت شاپ</strong></div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g - کاربر و زمان نامحدود - 480000 تومان
🟡
سرور 100g - کاربر و زمان نامحدود - 530000 تومان
🟣
همچنین سرور تست موجوده حتما قبل خرید از ربات سرور تست دریافت‌ کنید و بعد اگر راضی بودید خرید کنید
✅
🟣
برای خرید از ربات زیر استفاده کنید
⬇️
🤖
@ApexNetShop_bot
🟣
برای ارتباط با پشتیبانی و مشاوره با آیدی زیر در ارتباط باشید
✅
👨‍💻
@mehdi_splus</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78789" target="_blank">📅 20:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78787">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چیزی نیست دوستان قعر جدول لیگ ملت های والیباله  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78787" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78786">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBfEh9yp4-8v4fMuwdw7zydJLMIuY9S17zvreP79j0p8qlfs4M-SKgHP6EgrBpB9s62rW02Ub-ATeW-2HOBDzDd3Q_TodWbh2CFTpE6Y1lUc8AHYimxQJUpa7JKkjS0LTo-eGfKrFjtWzdlrXU1iL1zMC7n2Pqv1cyPjUdkR-KLZMnaA9L7oVY5yu0c4WbqVcI8KZ4QZXve7UBLShBWGKpk56gBlUU6RdludbygzS8O6IdL9vPJDFnkRHSrfoAz7S8ROVpONkbEDQihA5jyeisOhhGM7Km99PxEoiqXl-d9N2P12KHs7tN_hzQiSHAjQqEL2w7prGmQcnMqsU3v9jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان قعر جدول لیگ ملت های والیباله
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78786" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78785">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUUC-_QRBMSz8KQsHj8jcw1i-az_4yvISqi7CGQ1ks2-SoeztqqhOQDe4rMzZf3kCZMcJR-P3tXjhIZS2rmTXi9TTK95uUmw4SdXIxvfWZpjhY2wNEjj8XAhIcP41BsIUWdxgmne_gDPdESWE-j9pVo1Li43Fp5ZqFlHL5yAtrOSdx2a9Ke7aVW3qybzziJN4VZ7ZyuvBpQPh06hWRJW2K9aqeBqjtX3hhw5TRcQ3eRp-o00RWIWPRr0sPVuDeNxSluWFcTJWMC2fAM00IWQcElK0NEtjF6SbHlI2CfMkCXnhZ1RCKDrjWXhXyZ1LTZYIVmFCS2Xl7nnBC4GM9cJOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78785" target="_blank">📅 19:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78784">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">امشب نروژ، فرانسه را تحقیر خواهد کرد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78784" target="_blank">📅 19:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78783">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">این دیگه چه عنیه اینستا درست کرده ریلزارو فول اسکرین میکنی نمیشه اسکرین شات گرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78783" target="_blank">📅 19:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78781">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کاش این قضیه حمایت از همجنس گرایی رو زمانی که شیث رضایی و فرهاد مجیدی تو تیم ملی بودن گسترش میدادن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78781" target="_blank">📅 18:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78780">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rfr7Q5_5Aj7Q6fCWXamgyEeSR9-2-Bpc8w9DcgWRIVVjm5v0PkdNGRUR3C7pRuIn3bKD9AXdoSTFdu1mz0uYyuiAl_rt8fGNIjTQInk2JMpeUIc5Fwk-KbRzAKtj47RWRpb9qfD1Dt7xzuFS5Ylkxnca_ekhscaqzbzOGQaYBBp7s-jmZqJQilKIBW3hO2cRGL6pYOS7QLGaW0vw4kU-HcKpWzFu-Y4AzPBKgqIv6wsGH58X-HEJUXfsZ-b1jPcmnfmip3OnJR2ZBJ45Ph3CfxUx8wrh7ntt_xREGd6-2FMXquSyxAMiMuTt0MgcZc9h0H_1aNfTAmATui9jFRhYUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78780" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78779">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cNtAMfX2vn1YphOaz-2Q7rYTT_egC4oXVV3Jc60SpzcLEsRfrpde_LlhBKHI8wIirUH-KThqFl0PX-TgWDSSxC7zVjLPQMs11yPY8pb8iuPwWo3Xlt43js0IC9q9i_DD1knKzOmr8X39JhZ1D45_Cx8q4uKaOZs3NWAFgv2c1ojZC7Br5BSWSQBfMWZ4aSNnNwclk8YOBSMkrjgiF6tKamH_A1WzkzdHhmthS4iO_Tb-9tqU7H6_crQhW8JNM2CYjk6AXoKR5Y2HWQs_-92JhvatawikdvoZlM0zX8otBVBZCPwoHqrr3J1vCqpy-se9UuecCgcZlfXxhYlh8AS3Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی هیجان‌انگیز از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
فرانسه
🇫🇷
- نروژ
🇳🇴
⚽️
عراق
🇮🇶
- سنگال
🇸🇳
⚽️
عربستان
🇸🇦
- کیپ‌ورد
🇨🇻
⚽️
اسپانیا
🇪🇸
- اروگوئه
🇺🇾
⚡️
وقتشه شانس خودت رو با بهترین ضرایب و متنوع‌ترین بازارهای شرط‌بندی امتحان کنی.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
G5
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78779" target="_blank">📅 18:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78778">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/923838e44b.mp4?token=SABpJEJ4uIKAS7obbAXfz41skkFCm4SwFOCAeUT34-Cuc2l2CrVGVlq1aVedxrLoKiIqCJpyLzU1NGe3A9MzZMKXOlBsCkgthHhcuq6-4kVvg6Rps8AZG5HLqDbhgrs0vTOfgHRRHFlp-O9jyTfeaayjDXvmqT3ObWMrBElo9RBVl2C09Cn5DzSRuRLoKEABNCMXymE46IBJHCHXIKqb7OE6qVehLXkStCumpjTpb4QGps6cchnoFA21mnOBGc7YnCnDXKNrS5oydbxX9rz8nN3nSc-Vg4lhk0a86fpZVmx39i5mK-wQ0zRfmAXOMoSeDDa-CpqN0V_PmBofuPCWpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/923838e44b.mp4?token=SABpJEJ4uIKAS7obbAXfz41skkFCm4SwFOCAeUT34-Cuc2l2CrVGVlq1aVedxrLoKiIqCJpyLzU1NGe3A9MzZMKXOlBsCkgthHhcuq6-4kVvg6Rps8AZG5HLqDbhgrs0vTOfgHRRHFlp-O9jyTfeaayjDXvmqT3ObWMrBElo9RBVl2C09Cn5DzSRuRLoKEABNCMXymE46IBJHCHXIKqb7OE6qVehLXkStCumpjTpb4QGps6cchnoFA21mnOBGc7YnCnDXKNrS5oydbxX9rz8nN3nSc-Vg4lhk0a86fpZVmx39i5mK-wQ0zRfmAXOMoSeDDa-CpqN0V_PmBofuPCWpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پشمام سجاد شاهی عجب موزیک خفنی داد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78778" target="_blank">📅 17:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78777">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzn7n_lKbx31Sz_r8PmERymPl5EXEWSy3fjzoFREmVG8NhKB9lO6B6WCP15Mw6w-M3poI2n1Vi_Dn7LRf_jnJdFPYuQsLxmIqAiZzmSi_5VKIG0F34ylzVar61mmEBxWRIHPH2RHMu33GWGs45lAjFeqoHdP4SFQh-2UJgj2BoEYGvmOkJNVg9VM40g8MM1Uh3Rlg12p-1_RNz6XxdpM1abL_jlWrPNOHkAduBVzqLXxWKhgH6Jcqm8RcreTi6u1nyUYJ5FxAmuV7LQx7lqBxvpZXbHRHs6GMtK48T2XzU_bDrh-hKsNQBqwAQ17YgXpCY_3tkx3eJj_n6erKupdyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپفارسی نمونه واقعی جمله "کینه میماند"
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78777" target="_blank">📅 17:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78776">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78776" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78775">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">منابع عربی از هشدار حمله موشکی تو امارات میدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78775" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78774">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gv_-YGdmbZuqlYx2KKxDBR2m0WYkdyouCcep2d9I27plRFZa-rHxGdi_5LoekTMHhlygBwEOdrRXs-UXtaPYVz8MBduf3GLY4LqOmmvfZYzxlLDpr9klSE6TvoVPle4MLwto3XVl3X4SkT0YFbi80bJtNFR9mi9DbyNl_VO4gmS6ckUcPYXLUaNCeuWLjY1Tjji4MRNpoHpmVMShPDjml2nAZPFiXHuUp3bNZeIbuTPm89R1mkrP7EuBvr62huwnCCkKXXRX2TZeD1cgE0M2SvQAK7dBcoFRNqoxrAnKYWs9uJhca--fp85nHVm3e4yDkuA1gBKb76A3ivvSinAj2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر دفاع اسرائیل برداشته یه توییت به زبان فارسی زده و عراقچی پزشکیان و قالیباف رو هم تگ کرده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78774" target="_blank">📅 16:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78771">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">رئال نیکو پازو ۶۰ میلیون فروخت به کومو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78771" target="_blank">📅 16:17 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78770">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=dltqQvuM-aa7zbxqW9SxYvAKn4imoTCaUl_dRbwnfGPhOhFvZVxsMIW3oLBBh_qGFBaYCwwMaHx0LD-xGgdjZ9Ici9yVG6HKo0BVQ3OfuJJ4Cl62kiJjOGXt-paEearpFcz1buq8Sa1fq9kZAQORh9AFkOkePy31E2VbsZnYgaiUQ1DOyw9ShXWyzJ8oDeHh6HsUDQHQ2RCQ0Lz6tidopnC4vhiBn93DxapC_A8OAaNeuRhADB0gFnNHkw3t-gP6itFcZ5NQEVol0Xp7-TrcO_nE7aeAw87o203FJui39OVFaBxhcZtnHm83DqjYIVN5NgMdc5T6n6G9Ir0ddYp5Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4e63ecc73.mp4?token=dltqQvuM-aa7zbxqW9SxYvAKn4imoTCaUl_dRbwnfGPhOhFvZVxsMIW3oLBBh_qGFBaYCwwMaHx0LD-xGgdjZ9Ici9yVG6HKo0BVQ3OfuJJ4Cl62kiJjOGXt-paEearpFcz1buq8Sa1fq9kZAQORh9AFkOkePy31E2VbsZnYgaiUQ1DOyw9ShXWyzJ8oDeHh6HsUDQHQ2RCQ0Lz6tidopnC4vhiBn93DxapC_A8OAaNeuRhADB0gFnNHkw3t-gP6itFcZ5NQEVol0Xp7-TrcO_nE7aeAw87o203FJui39OVFaBxhcZtnHm83DqjYIVN5NgMdc5T6n6G9Ir0ddYp5Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مسنّین خلق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78770" target="_blank">📅 15:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78769">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78769" target="_blank">📅 15:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78768">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uFSIaKWO2YyM0AWqi2gEb5sHOblecO-T97VGR3qdgPfu9ANYoJMdiIddaBIl0y91GbJQRz_aOXTek2xe1PDGW-y_yoCLDMe2jCokcojdUx7MXAPw0R2BZKjDdhDDr8cVKJy3A2gfmxNvtfx29f4ib7I7QEnGjpQs1exMfECdEyZtMqY7HTS5nON3dHZoCuvkW-n21TU-13ERLS5U79zeAfBxop2n_e9DnPMZpNe_N4K6Co5ngw-FLCUMEw6HfuCYgnPKvgvSOYu3wICMibGS3FOIdiZO96cXzTuB08hrLrNsBrgm9JCXqht-_EETAXIiPAzcMG7SQIAm6JmBg7i94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78768" target="_blank">📅 15:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78767">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">بهترین ترکی که بعد جنگ منتشر شد چی بود بنظرتون؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78767" target="_blank">📅 15:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78766">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">اینایی که از علی گرامی حمایت میکنن اینستا بهش شماره کارت دادن یا تلگرام
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78766" target="_blank">📅 14:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78765">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M-y2C6PtYyf5wQTjyXacXkQh8vgzjFs6PCkKi2j90bS2UwN8EjYkpaFuzehp6bAcAXk1qdOfR6eKZbTRFezvOjvqErs1nyDm47RUARrosav74cKWG7i6Vtl-2wqaQOA5Dl9Rh3XP0K-3pKz6hmL07oamrEEhxCUEPW3t6TYagkPoYeCZQ1w5sXwn2ViA45pnujLyuPoj59Oj3YQDBiihRMKhJe7GLkooG7kR8A_a9VyANPDDl_MkovmqTm_WUE4zI4xRcQN65tBtbXhS7YX6oovBHdCYAU5VeH-IL4j0-eMdFY1zXFayAHlAfK_tFfvSyIpsg21DKksDYtXco4QaOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمبود خواب داره بهم فشار میاره، چرا دارم دونفرو تو عکس میبینم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78765" target="_blank">📅 13:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78764">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">علی گرامی به کدوم قبله قسمت بدم نخونی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78764" target="_blank">📅 13:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78759">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78759" target="_blank">📅 13:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78758">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یه‌چنل بزنم فرم بزارم برعکسشو بزنید؟</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78758" target="_blank">📅 13:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78757">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">یعنی چی که به بابام میگم سند خونه رو بده هفته‌ بعد دوتا سند میارم برات میگه نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78757" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78755">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IR5ZCTuvHuhEeeXjvFr9XXav5IjTGtiyEVpru-56U9NG6YHGTVef92X0oPj_BGOXAF1l_hjxtrKzlSv78ufaFIYfHnRdUTF7s0__CDI3bkEm7Ky3cyI4Ia24jRBslUOSRU3vxzMmzAAa8rxdz1EUgZwQodedcdsybJk6125Zw15nfAlf47Zgfrqpvm7zCfRdywUrKYYP4fsWS4cSQT0DTKKXlICsqwD2IGqWc4HZBBz6B_qiCWLsRQxgqQmsCuEzSPYkKlXx6DAZa7NM4-IRuidSvmRays85flJftZWoa-81p5RrQPqL6EtA1GqHoGw9QRnlb06xV8TwTnpZPpw8eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وا مگه شما به لباسش هم نگاه کردید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78755" target="_blank">📅 12:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78754">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GwnS94Y3T3Hw8LlR6Q85v2vSi2OiJ9xYS_tHMwbLqp4Ndxywhz8noOFSFXcya5xt07_2uwSbR0Oi_kFuZAvyJoiB4NcflN44LrhRQZt1WonahFjZ_8jxMzqWLvM-o3bqtRPKEtwQf3U_h_ebkaXOdU8V4HMxZLdtoRiKO9TvmrTMQGuHUPivDm241epOWis9c8Vt6PzScP_JY-P8--W9v5eZ0xlXTPXyU8u2kmE_fBeETjPMwAtMnbaJsl2uyFupf5ZBG2EyNWxpC8jqE793GuevlCjc-6DG-K9ipQaSL8uyCGR2mdjTQUHxsyRFnS7EceKZZqjOM9CZzS6OemQR9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمومش کن تروخدا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78754" target="_blank">📅 12:16 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
