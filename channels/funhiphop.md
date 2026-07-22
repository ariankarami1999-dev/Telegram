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
<img src="https://cdn4.telesco.pe/file/o_lRHE93BO-BlXU0ssO8OVadZk5JJ1iT6FJx8IG_jDOxv6BrHMN_IKNS3M4PVHLrhC_ii9g3fHJQsaU0mz-3na3bmzBg8v27AXbi_sWrSuXYqP6kbgaUdwlCyypdZldJdH46Uf0tHdIcNAB1oj1lxMQFtDlfikZyqhFXr8f_RfX3kzvclz0ghXR9PjlvOG6jXBgVokiKxeCi1dh0-Zhs9I8NOWJF4c-Bi-J0MTHHMRwgLG_5_mUtp9QObz8vz_g-vq3-IWufFmoE-C8x16VeKvtpv_OTi9SyFwS3VK5COuUovUFxrgPMFD9HwKqLmDcuj_JcwKk_S85TBj9lGutaCQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 205K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-01 01:04:23</div>
<hr>

<div class="tg-post" id="msg-81094">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">پرواز جنگنده های نسل 66 کوثر بالا سر تهران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 2.64K · <a href="https://t.me/funhiphop/81094" target="_blank">📅 00:52 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81093">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YycYzzrX7dKM3ZseNUR7vq_DYIC4fhrE2S5ENC9zzjCCiBVsUid1f8fhgkysuj8nJbjuXBKSn_fqvPKmL7rfdCP7tlnpRkakThujxA1FsJDHm9cbS2nlyeyoWhtCtIz3SdCjcfwd2GmgTgepN_WUn4T4Kq941oDGY2DVNe6HWs5kYD9ZXakY8MjY383AcYwKKUiS1mbI5FbKxhXC85PLPwPMBi5n2XnJTS3v-9pNsFlrQTNDwiCyBrQCesIbzhRdDqewtrqR0hPg1jhFn0RSGE43BwmpYtJIZyPFuOI_X9pX6mCkyzE5QnI5lYEGZEV20SxfKyG_UUcfpksdUfhdEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق مقررات جدید چین، استفاده از برنامه های هوش مصنوعی عاشقانه برای افراد زیر سن قانونی ممنوع اعلام شد
دلیل نگرانی سیاستمدارن چینی این بود که شاید افراد وابسته‌ی ربات شوند و تمایل به ازدواج رو از دست بدند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/funhiphop/81093" target="_blank">📅 00:47 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81092">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/funhiphop/81092" target="_blank">📅 00:40 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81091">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">انفجار در ماهشهر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.48K · <a href="https://t.me/funhiphop/81091" target="_blank">📅 00:16 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81090">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/81090" target="_blank">📅 00:00 · 01 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81089">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامپ میخواد در های جهنم رو به روی ما باز کنه نمیدونه ما خودمون تو جهنم زندگی میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.14K · <a href="https://t.me/funhiphop/81089" target="_blank">📅 23:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81088">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">کان نیوز:
ایالات متحده به اسرائیل اطلاع داده است که قصد دارد در روزهای آینده حملات خود را تشدید کند، از جمله اینکه برای اولین بار در این عملیات، از بمب‌افکن‌های سنگین استفاده خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/funhiphop/81088" target="_blank">📅 23:42 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81087">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">چه بدنی ساخته دو رو.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/81087" target="_blank">📅 23:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81086">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJzYCRFlRXHLateEucHsamE4Fl8KyDhxNl5wQuiQWRzdBIp0s-koh5DHDuOpFI4Zgu4jpMFgILuVWj3hGWLh4WZVkUfXCW_mX7W4phb9OlcgaMpSwsRCAtb9C0t5Cv6wqDQ7TnwCNV8gKrlpmOtnZ2iAGvyyrtaZFyq5OtY_sFyQhwxpYgQ-Ezanr1dhEFahHCz1KCRtKEG17eVdYzvRqWeEd3RjhHhLWj-ii0vujNpu48c7OJ9l1Nv88MP9sNU6YyxyWTYz6QRQeubnt5jpnK11hpSq6i11gbcF5MpPTR_ITFT9njIqIt2KGlkFQnEjtZqHD0FMajnJ6lwXKT6JuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چه بدنی ساخته دو رو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.02K · <a href="https://t.me/funhiphop/81086" target="_blank">📅 23:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81084">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Au9okRD93zUs2_VLFu0pRz1yP1X9hXwewmGRnbQodDHRw_8lElU02Hi6ffPFvJSafGfmrLVrWxGH3MA1STYZZ8fh3RvbCNkFL_2NmMaho3LOUUmPFfNxoWW4PZYpv2Dk2wky6c1fPbucr2xDKhR7_BItQi2wW3oekKIT1sSX1oO3h994kC03STB0c4xCyj7FtkcY6JVpzycbvSPm2n4Y6iD7pXxfTYo_4s5mh57Gn_A_t8wNUDNo-cuAnyA8ReUT31tTShDWrnjjMIS1__SwuIsODQGAyJ2PQ-MIfKQrTR4WyngN19vPORhjPmP_Oed0mkq6S4PdMi2xsB5x8kxo9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سردار جان پس اون پلا و نیروگاه‌هایی که کودک‌کشان تا الان زدن چی؟
اونا جزء تست رایگان ۷ روزه حساب می‌شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/81084" target="_blank">📅 22:55 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81083">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l9jfjB0iZT5dlDKMZIxvt4LINwUqwuCBde3H9Fdn72ZsOFkaR_G8xQMawhGrQJcRqOJGhieg8gSSkdSK3xgWOcseJHg0nKRntLaWsIokX5DgRvA3kajALuXGPWaUDO8tACp3tQ-Z7lMHNNJOm1yfAnP3N2rNu80g8RpDqUcPhLBQ0ZAHnUp3h7PqwPmTP5BvXpPi-iXv2w56K-f3BicR8lZD7tpuT8S2ManBgc9KUX_GdkSFLmANL7zYPgw-0CSKoDstJvEAe-AIsUAX0UUBHP2g1zL9nhOpwNf4OO31-VLeep6Ce0Ja9uh4_37L8lpchXeUVXAQq1Jf3Xb5MNtf1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا نخوابید خیر نیست مثل اینکه
انگلیس سفارتشو تو ایران بست و کارکناش رو هم کامل از ایران خارج کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/81083" target="_blank">📅 22:40 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81082">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mXXBHyy2yh5Z8sMmQPaRPP3O3Z-BIXrySsCXpcowy2Z9TPsCfU8i5_UdQzHZuOPMbvUK3IhLSAGAQR2Acyc6uUxTVCl0IC25Wpin_14xm9DBbZtpojqiNDATkx4W5piDpbRnO2cRMI70U4xUF3Am92ru2SAm6UCTtgtv4kvOM0hmF6qyJnRGOCKA5XDp7NjNQNPu0VNUgs0dKObogNG1mh4q0aJtOoDhfzC26Q-Fl1WL-1CPnAdzmqu_Fvec9xgOWZWTx6g2gomuBjESJ5dYYwprld9dtOdTx-y3bsaDKsegqtIFbLV_vNrYL35fMe9596f5X6qNGaVeKJ3NGzVTsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حسینکوسمادر فرمانده گردان القسام حماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/81082" target="_blank">📅 22:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81081">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=U1u7VEotLvCpLVIQyUUc788Z0tLxN47mT0F7qbvoP8Y9Nc-Rf83ymVilbMOgPADloqMIJnXUaj_F9LNHNceoWxJkEQvXljQeEUlSzgVqDrqBCLuhwTp6NUKrV0X-Tm-kzD2700tvt79RWEd-WbMc7nOmf89A-J9_bUwJsIz37bgyOPaiS0ow4zwv-OK-NgqAUaC7ZAYsC1WPmpMqoi3mNwVCh1L4tRn7R_Z7kWt1Q5WzUT0q_lnnNCfnYVTAKlnrlFPqTdnjoWXALohhKnnsQH3dno-3TYVijZ75_SvEg8haVemDb4OD35zeQ6jJKGCIqBjdLSCb9e27RHxF-IKcbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a367c7357b.mp4?token=U1u7VEotLvCpLVIQyUUc788Z0tLxN47mT0F7qbvoP8Y9Nc-Rf83ymVilbMOgPADloqMIJnXUaj_F9LNHNceoWxJkEQvXljQeEUlSzgVqDrqBCLuhwTp6NUKrV0X-Tm-kzD2700tvt79RWEd-WbMc7nOmf89A-J9_bUwJsIz37bgyOPaiS0ow4zwv-OK-NgqAUaC7ZAYsC1WPmpMqoi3mNwVCh1L4tRn7R_Z7kWt1Q5WzUT0q_lnnNCfnYVTAKlnrlFPqTdnjoWXALohhKnnsQH3dno-3TYVijZ75_SvEg8haVemDb4OD35zeQ6jJKGCIqBjdLSCb9e27RHxF-IKcbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر بار که با خودت می‌گی که خب خدایی این دیگه آخرشه، این کشور یه پدیده کاملا غیرقابل تفسیر رو به طور معجزه‌آسایی خلق می‌کنه و مثل جامپ‌اسکر می‌کوبونه تو صورتت که بگه گوه خوردی که می‌گی آخرشه، تازه کجاشو دیدی؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/81081" target="_blank">📅 22:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81080">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه  پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها: پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/81080" target="_blank">📅 21:17 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81079">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GOnuTdo_ieptWWqdXe_nTV6S7lXCbyZofqHMPf_nnVuA8n4hzR3fWOlzUOR1l5JMPOdyRnNZBsmA_ndkbzesllolDO8-3-SIi3FKKbKHC57mLG22c4TcNZCOXUP8LomRL_Abv9lMN6yH0EYxtkxehQfo6xS6-KBcpvigZsRX6cF2wgHnviGl6kaMPyhDer_Rc08Buky3nWzN5zsuPDqt51q1QsI5Vv1OIfkjxVVSyxaVLc2aAxgHpPOP_9FxzqYRAtgdCsCZP1N2ErUMaEVgjSPAb12nZCQs61fZycaoJ3-S0l1B0sMtzqUG4n0XAAm5lgjZcYSs7iX4KLZO_nRPnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راحت بخوابید که شدیداً خیره و توافق نزدیکه
پست جدید ترامپ از تیتر یکی از خبرگزاری‌ها:
پس از کشته شدن سربازان آمریکایی و حمله‌ی ایران، ترامپ به سنتکام دستور داد «دروازه‌های جهنم را باز کند»
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81079" target="_blank">📅 21:10 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81078">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">حافظه تاریخی پرداخته ب فردوسی پور
برید ببیینید</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/81078" target="_blank">📅 21:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81076">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکیان دستور رفع فیلتر اپلیکیشن و سایت عادل فردوسی‌پور رو داد.
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/81076" target="_blank">📅 20:59 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81075">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">صبح امروز، مهدی خانکی، دانشجوی ۲۵ ساله رشته حقوق که در اعتراضات دی‌ماه دستگیر شده بود متاسفانه اعدام شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81075" target="_blank">📅 20:23 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81074">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خودکشی جوان ۳۰ ساله پس از شکست آرژانتین در جام جهانی.
«سیمون حسین» ۳۰ ساله، متأهل و دارای دو فرزند، تحقیر ناشی از حذف آرژانتین از جام جهانی را نتوانست تحمل کند و تصمیم به پایان گرفتن زندگی‌اش گرفت و همسر و دو فرزندش را تنها گذاشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/81074" target="_blank">📅 19:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81073">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/81073" target="_blank">📅 18:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81071">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/niwxicfJdOromcK4wiyJQuPU2VZf5Qz7CE2lKvBadYPN0cWL6tSqgc8ydWMoukc2LN6cJ6c4WcWQrBSJ8q4Gjguxi_jLaF-DR_Gz4mJhXC6tClaNvGKKA-XOF3BM0BpDlhu3jR4KAFYA35io84pNDHWpGMGnIi3D4XVsN10HaRI6-fGwzsC46SgliE43hjcq_CpPrn2vfOvEG9NpjlMHSttbqeKvZ59qPoercWNlDISr9mTSFrEQsbKkZ6u17Mf7WfYEk2AwzlmXpWFsH3PbGqHTkF5mp26EIwQU638Ik68bKDMbGpxhZ_5aNFnfHY8aWV-Zm-yzd_fHYT1-wzN94Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BFvNw-0v0Ywnmj4Apgb2bpiPvSPX_B7hYp8F78m7dbK7IdF3O8RfOvfWqnXhpRUglf5INEXDP52khfJc0KnBi1l6FAYrGtOArtdp3zz1BUr7KExRMgH4xzJ12hCM02GtmFY4IzigQI2zF1SAE8lQRLduln9za-A_CuWlJMlvcLHywNPfloAELxCeRurP_HxKFWib6B4ByUQ_snC35uR4UkdjUALbfEnZVRB5r0pJRMepbj0gVA27BDSmqUY9ErWxBvlK0wYWRNUjApI4PqvTnsmnBy7xyxvaeHeXTXeq4tB6h70Obse2vd3nixrUNQRsKsL6CkfS6auR3hIM5UpnRA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینیسیوس عجب کراشی شده.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/81071" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81070">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SMMLIYEs11XTBnUHvNgNCSTBVLLGK21xv0atU5bAeTGkJTBuN5st7oBHSxW8xyeEAo55ES87Q01-sMqb7NauJARN_20yhlPV1QDEZsZzjTo31BhOkHW-9KnrSFCWSNg05WIFSGjGSJdHhRzrUBH5k99mZ67T-jMZPWGrzfgTdElyEvu9Yzo5Ny0ub2Meqnl0ArmCdytuS_saVFchtNKjyGmRu196EJTzACCjMhwDWNQ8ZrEbevPZ-UPwlPv06WK1JhtkP5Pn5FbY1uytl5bbLIrBbjcfTQ5WjCsiceFLOaMsv8M6SwlZ7B90oEgT8mIC-bGJbLumDTgmdRov2FqWSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
هوش مصنوعی را وارد پیش‌بینی‌های خود کنید
🎲
🔥
دستیار هوشمند بت‌فوروارد با بررسی داده‌ها، آمار و اطلاعات مسابقات، مسیر تحلیل را برای شما سریع‌ و ساده‌تر می‌کند تا انتخاب‌های خود را با دید دقیق‌تری ثبت کنید.
🎯
تحلیل مسابقات با کمک هوش مصنوعی
📊
بررسی آمار و داده‌های مهم بازی
💬
گفت‌وگو با AI و دریافت تحلیل حرفه‌ای
🛠
ساخت پیش‌بینی با ابزار پیش‌بینی‌ساز
⚡️
ثبت انتخاب‌ها تنها با یک کلیک
👍
هیجان پیش‌بینی ورزشی، این‌بار در کنار قدرت هوش مصنوعی
⏩
مسابقات را بررسی و تحلیل کنید و پیش‌بینی خود را هوشمندانه‌تر ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r31
💻
@BetForward</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81070" target="_blank">📅 18:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81069">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.…</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/81069" target="_blank">📅 18:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81068">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">توافق قطعی شد اکسیوس:  ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81068" target="_blank">📅 17:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81067">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">توافق قطعی شد
اکسیوس:
ترامپ در حال بررسی از سرگیری عملیات نظامی گسترده در ایران است، که احتمالاً شامل عملیات مشترک گسترده با اسرائیل خواهد بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/81067" target="_blank">📅 17:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81064">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kUB2q1zVHuCBYxSxcvDsIei4v3da_Oq3wElQ9IaAI7PsKkp4Qg5m_KpjpmgYyTgvwnFb-0A7_ZGLyQJeOcu4csPNITRNlE-A0uGEXaiecfxGr1upcbKvT0DZdxNdwrnLyn1nEKJgUvO9M4_I6WKNHKzQ0E8Ou5ZWVX4bnZjg0fZz7IfS9xBMH603PIl9zwNhEdgjIZKwwk4IT8hHoKkw8aKvTrZnBXJvytt5U8dI-RjGYjzbWmqbP32GemCIE8YTs0Fmn-ysXn7ZSba0ifYfeCuJC6fd39Yij7atMUj-xBPGGVTkL3QZY1SOqKpcRVz1URb51agL4SHVBHykc3cSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWZvemOmB8NAJvnUJ_b9qcXbr4jLYmSpENiiPtJUHDtEYobYFomaJC6V1E6MyzJDfOownsG8Z4aewwsqReVqcykzWsA3qOGF7fRWb_kZDKW2I4Hf6VZhP5iG33_I5UgFH7z2sCqw296dZUN1GSywFCkEi6TSXwUSYqB2jjx8uQ13e-N0qKFQtB4SriSx4NfuCIsxzDYvEY0ZDaoXjqNfje4j9taA2iCSGtaLdK6jRaxPVtXe2D82m_KOm_-W02RQawA00RiauYwh1NYP_2hzjUheLjNrRCN9VpSULu9U042KZjlgQQ1-c2ho_OTiM2k9lLJV3gPANEFX6iJ7_D4e6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SKWzvz6W_1OweKhgiZIZ2ku5HoKSXc62B-ZjgNw0xoyCAl7NIF4zqU2WSNzLJmJoTEZ8vRIO3Pdz0yGEYON0N1kr3Rutm3kKYU7vO7qLWAYL_xgeNqxJt27Tgo-mNv558o7UsamIZa4UfN39JqYxrU3eajf5cNo1ZUwuYFfF4EmeMujbVEp6r4N2UK1UJ-FAUVX5rkcSEOpG4vvsGfqsX8yNGRDluyr4FWJkeEa0RFV0b_ecOzXI5N1Qk9IaG-CeiaFSAOKJFznl6KkqiIZsTxwi5S3jtqU_QNVeYHNqba0mxP9_hMqns2XXBPK7Eajri2ubRXnnbd2vcpgRE6oEwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حالا ک بحث عادل داغه چنتا شات قشنگ ازش ببینید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81064" target="_blank">📅 17:20 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81060">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟ شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/81060" target="_blank">📅 17:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81059">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">دلم برا رها وانتونز زیبا تنگ شده، چرا عکس جدید از خودش منتشر نمیکنه؟
شنیده بودم این اواخر ترکیه زیاد طوفان می‌شده امیدوارم باد نبرده باشتش.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81059" target="_blank">📅 16:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81058">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">ترامپ: از این به بعد، هر زمان که جمهوری اسلامی ایران در تنگه هرمز به یک کشتی شلیک کند، چه با موشک، چه با پهپاد یا هر وسیله یا سلاح دیگری، ایالات متحده یک پل یا نیروگاه را بمباران و نابود خواهد کرد، از جمله آن‌هایی که در کنار یا در شهر پایتخت تهران قرار دارند.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/81058" target="_blank">📅 16:39 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81057">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">این یعنی تعویق؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81057" target="_blank">📅 16:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81056">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S2v-RQ1tirt1XNuvUIb4bEQXqwGsNCMAsDLDXa9XRz5FSBXXFdvP31-NX11J-eZRVxT3YmFXTVTzEOVkoVgIdhmoatqsq12W_Npoi-rMdeRV2d9M5-kiKTcInKOHO14MngJH52RZIKltcGRGBwWWPqI7pU5lk6UPSlVc3rPBIWC7qTQqRMkSiutM464vIK9_KQDyTEE5Nx9nAiPMSAcAYdWRK7MN-uZpfRWnhoPlcW-rjR0uI6etX1Un0C2JPbaLTXmZpSmyqgO8MAMMLXTjdoHh1ZIXuIO2peeQ7KySl_h3GqdWY5A3ysfAQgZvSOM8cGAOVT5vh7hvwkZpJFCHmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هیچکس گرفت رو فردوسی پور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81056" target="_blank">📅 15:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81055">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/81055" target="_blank">📅 15:15 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81054">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fmxtMhvOmfIqUjshLkLcKYZweAWhwsLr8mFT5TsWwjm1R8kXZ-8nphhLxRyUMfz_4ssQ7Ac6Esj4Tc6ijrs4zknDfItZPcSeq6Aqxv3_UpcLKO6lvQZznWeJUN3cpj7wwhc44B8CY1Ks-3Uh3qdHsn7b2cmPlhgM0NMFjKE5b5b9xzsEvz55vNIOtiPMW18g9iCOv7oKmUqGijF_hr85K9k0QngoWeTVDLLTrLm7pxleYpITCnlZKe9qeRahrx_mgIS5U7rkBvqgnpjeMKp7OrLY0J-RKo_yxDptAnniRMejJiQ0PPlOqvnagOfQTTUroaoJErZUHEodbVUXQnPlgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داریوش بالاخره ترک کرد، شات جدید داریوش بعد خروج از کمپ.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81054" target="_blank">📅 15:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81053">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">سپاه: اگر تجاوزات ادامه یابد، آماده عملیات پشیمان‌ کننده‌ ای می‌شویم که اعلام عزای عمومی در آمریکا را به دنبال خواهد داشت.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/81053" target="_blank">📅 14:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81052">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">امتحانتون چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81052" target="_blank">📅 14:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81051">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">توضیحات مراد ویسی در مورد فالو کردن عراقچی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81051" target="_blank">📅 13:44 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81050">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ببخشید چه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/81050" target="_blank">📅 13:26 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81049">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">لیونل مسی بعد ناکامی تو جام جهانی اینفانتینو رو آنفالو کرد دلیلشم به خودش مربوطه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/81049" target="_blank">📅 13:14 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81048">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BTMVluf6qC6plsw2yDixy6obaj4B61iorBpUdRW7Trj7Zid28qVrA0cVwScaITC0Gh1rp_U6BEsWOAWfDCxjrKdVIl4KTBPHJwpn9oJOyfjvBXywMZy9A_OgdS3ewDLkfDuSp-0hYxWTNlT3vj-NrBiMrwK1d0ItFSSXgVPwTp91lu45MIuIWEvL3E06Lc_5D_T2w519nyZgVVLfVJTQaiEpfNGtKIhgueWWbmTkhBbW67m66B4YcC-NZhZaWYE5BXfL4hnWGZVTWrzCx-ElRUHbfdB5oFRSvx9EcZF68U80dByOaX6pgdmFoPnPBM1qHXKrlETee5xzaZ2TjohW9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا من در سطحی نیستم که راجب این موجودات نازنین نظر بدم ولی ناموسا سینک جای بچه نگه داشتن نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81048" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81047">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qNH0oQkinpfE3S8z9fQAyhhBsfysg9kc4z_6hsKsUQ7f8qi6TAf0cZ1-lIC_IxPA76541d7MjxDftLpEE8yq6lW2uPXRDUD3ZLUCmAc5IGwla7dcVKAREcQI-ZtP0_rxeNt59_kyI-2hGpBumWawVMftULZKlcDIAcdSdg2F9uqb3AhpC6wrsaCl_KH4cYTZOCkM02C0ATgPDLx1PlIKOl_MnA1Gh_R8c1U5jEwqESYvc0CrpGSzJsEpMr8HaLwc_bbr-w4cq26277jZggp6CzQMM5ZpP_ZwudJK6_y-di3r2ahalzj037dftVh8f_tZ9xMZcDlCUtY6gfZnG-PkKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🧠
هوش مصنوعی را وارد پیش‌بینی‌های خود کنید
🎲
🔥
دستیار هوشمند بت‌فوروارد با بررسی داده‌ها، آمار و اطلاعات مسابقات، مسیر تحلیل را برای شما سریع‌ و ساده‌تر می‌کند تا انتخاب‌های خود را با دید دقیق‌تری ثبت کنید.
🎯
تحلیل مسابقات با کمک هوش مصنوعی
📊
بررسی آمار و داده‌های مهم بازی
💬
گفت‌وگو با AI و دریافت تحلیل حرفه‌ای
🛠
ساخت پیش‌بینی با ابزار پیش‌بینی‌ساز
⚡️
ثبت انتخاب‌ها تنها با یک کلیک
👍
هیجان پیش‌بینی ورزشی، این‌بار در کنار قدرت هوش مصنوعی
⏩
مسابقات را بررسی و تحلیل کنید و پیش‌بینی خود را هوشمندانه‌تر ثبت کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r31
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81047" target="_blank">📅 12:30 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81046">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سجاد شاهی این پول ویناک چیشد</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/81046" target="_blank">📅 12:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81045">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قبل اون قضیه نجات خلبانا میگفتن نیرو های آمریکایی خایه ورود به ایران ندارن بیان سلاخی میشن و فلان
الان میگن خایه اومدن دارن ولی خایه موندن ندارن، بمونن سلاخی میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/81045" target="_blank">📅 11:54 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81044">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ویناک چند روزه به دکی نگفته پول منو بده دارم نگرانش میشم</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81044" target="_blank">📅 11:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81043">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">سپاه صبح ها نمیزاره عربا بخوابن آمریکا شبا نمیزاره ما بخوابیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81043" target="_blank">📅 11:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81042">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">تو دنیایی که ملت با سهراب ام‌جی لاتیشو پر میکنن دیگه این که فران تورس جام جهانی داره و رونالدو نه چیز عجیبی نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81042" target="_blank">📅 10:01 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81041">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81041" target="_blank">📅 09:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81038">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">زهران ممدانی میخواسته نتانیاهو رو تو نیویورک بازداشت کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81038" target="_blank">📅 08:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81037">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">همین بین که شماها مثل سگ استرس امتحان دارید رفتم سنگک گرفتم دارم املت میخورم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81037" target="_blank">📅 07:28 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81036">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">ولی بیدار کردن پدافندا الکی نبود، حس میکنم امروز صب یه تیزر از اتفاقات فردا بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/81036" target="_blank">📅 07:09 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81035">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سنتکام اعلام کرد عملیات امشبش تموم شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81035" target="_blank">📅 04:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81029">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">تسنیم: دشمن اومده رو آسمون تهران ولی جایی رو نزده و فقط صدای پدافند میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81029" target="_blank">📅 03:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81028">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دانش آموزا بگیرید بخوابید فردا امتحانا برقراره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81028" target="_blank">📅 03:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81027">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نصف این گزارش های انفجاری که میزنن فیکه، تا الان پنج تا انفجار برای شرق تهران زدن ولی هنوز خبری جز صدای پدافند نشده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81027" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81026">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Ginza</div>
  <div class="tg-doc-extra">J Balvin</div>
</div>
<a href="https://t.me/funhiphop/81026" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">کوبارسی اینو بعد قهرمان جهان شدنش گوش میداد من وسط بمباران
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81026" target="_blank">📅 03:36 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81025">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/81025" target="_blank">📅 03:34 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81024">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromZahra</strong></div>
<div class="tg-text">انگار پوفیلا میترکه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81024" target="_blank">📅 03:33 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81023">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پس خبری نیست، جنگنده اومده بود پدافند فعال نمیشد.
@Funhiphop
| Erfan</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/81023" target="_blank">📅 03:31 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81022">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">صدا پدافند در شرق تهران.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81022" target="_blank">📅 03:29 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81021">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شبای خاورمیانه واقعا ی حال دیگه ای داره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81021" target="_blank">📅 03:27 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81020">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">شین: انفجارهای عظیم (حداقل ۵ انفجار) در مجتمع پارچین، شرق تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81020" target="_blank">📅 03:21 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81019">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=EKKTwV9N2ApLmnUzUICFYICRsXNzghVtCD6Aj3OgKtUc-tasU6RMD8HD8jXfP8Uvo8jD9VDn6ctr1M9hYjXU4Mn4nRANxJ5Oh4kuT-HwFY1Lh7Mfxb4nE2MLkJIgml_VJ0jZZpB3WRLHiq9GOLZawG-W9pz1ZnYUuvNrXRvYo0Uxn2ETvk9p3G8gEnrRJrZ_SRqMeesWko527EVcM3y--_gFnCsAK3d7u-6E-AiQSvEY6v9q2BifjVvgPS_6RcVLpee1u2hYyOnzkNRpM0fvh2HMKUKGzDxVXefTyyaWvADhLWUEuYl1VCE3b0NhS-3WlMsnVijh2vl_9D9hXfRl7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b1c9a3f5.mp4?token=EKKTwV9N2ApLmnUzUICFYICRsXNzghVtCD6Aj3OgKtUc-tasU6RMD8HD8jXfP8Uvo8jD9VDn6ctr1M9hYjXU4Mn4nRANxJ5Oh4kuT-HwFY1Lh7Mfxb4nE2MLkJIgml_VJ0jZZpB3WRLHiq9GOLZawG-W9pz1ZnYUuvNrXRvYo0Uxn2ETvk9p3G8gEnrRJrZ_SRqMeesWko527EVcM3y--_gFnCsAK3d7u-6E-AiQSvEY6v9q2BifjVvgPS_6RcVLpee1u2hYyOnzkNRpM0fvh2HMKUKGzDxVXefTyyaWvADhLWUEuYl1VCE3b0NhS-3WlMsnVijh2vl_9D9hXfRl7DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پالایشگاه بیدبلند،ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81019" target="_blank">📅 03:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81018">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سنتکام:
نیروهای سنتکام از ساعت ۷ عصر به وقت شرق آمریکا (۰۲:۳۰ بامداد به وقت تهران) برای یازدهمین شب متوالی حمله به اهداف نظامی در ایران را آغاز کردند، با هدف تضعیف توانایی ایران در تهدید کشتیرانی تجاری در تنگه هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/81018" target="_blank">📅 03:07 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81017">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=YaRDXllRm4htcpkte98nZwqYEhcnN8fnUWlXBuz7vcTySg1aYurlYGxNb2-h-0uIbxsLXEScv5JJ9tji0GZLjP_Ea6BV4xbeM8hVx8Z6c7Rv04GNip84AIEaKHaxyaL5vz-ZMsRizBHOmQ2R79q_ePxIwbqmTIzAXmGKXpI0HjgCn3ACqW00vPL_ieY8DhWBiRr3cosyd8CGt4LsU8bMyLwiIWgnij-upoCjZ3h7zE1_oYosxTjivzHL2n0HSRJirlGnaumHAkjG2zgK0Mmm2ygRLyr3ZZy9oMq1pmS15VfPqw4cQUPgS9hPNzIwlIzH9riD-s0Gq-ZpWDXeqZ2fZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c60f68ed4a.mp4?token=YaRDXllRm4htcpkte98nZwqYEhcnN8fnUWlXBuz7vcTySg1aYurlYGxNb2-h-0uIbxsLXEScv5JJ9tji0GZLjP_Ea6BV4xbeM8hVx8Z6c7Rv04GNip84AIEaKHaxyaL5vz-ZMsRizBHOmQ2R79q_ePxIwbqmTIzAXmGKXpI0HjgCn3ACqW00vPL_ieY8DhWBiRr3cosyd8CGt4LsU8bMyLwiIWgnij-upoCjZ3h7zE1_oYosxTjivzHL2n0HSRJirlGnaumHAkjG2zgK0Mmm2ygRLyr3ZZy9oMq1pmS15VfPqw4cQUPgS9hPNzIwlIzH9riD-s0Gq-ZpWDXeqZ2fZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/81017" target="_blank">📅 03:03 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81016">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">انفجار مهیب در بانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/81016" target="_blank">📅 03:02 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81015">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">فعالیت پدافند هوایی در سوهانک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/81015" target="_blank">📅 03:00 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81014">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=f4V_7YwAr__dgOYQ_yb9t1lUBNxdebMysS37UoAe1eupbxdPYyNdPPDmSejKnJjBIgyjRQE1X80Cw_Ge7NesDnDmUqo_23SUTp2-U6LwJ0J8EcuNoblP9LOqmz6ycVFcNXJ3XaI7eyJqHVlikO2v4pa6xo4zx537JK7SWIZZOnuabGAaeETRo92Deib-sB_5yKGhpLq4fSKjOFLAk76tTbY-Y-r-08V-sJ-UrXnqPJIhM3Gx-KBDqFRFZ72H7VOKbW1feTTLFly9A02Qjzi5gdISU5EqZksz0JpdP-auvdEvNxO6CoA1kSGhS5pvwFWIw6LSwMyJLaRoDiEwMJ1Odw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1366210ff4.mp4?token=f4V_7YwAr__dgOYQ_yb9t1lUBNxdebMysS37UoAe1eupbxdPYyNdPPDmSejKnJjBIgyjRQE1X80Cw_Ge7NesDnDmUqo_23SUTp2-U6LwJ0J8EcuNoblP9LOqmz6ycVFcNXJ3XaI7eyJqHVlikO2v4pa6xo4zx537JK7SWIZZOnuabGAaeETRo92Deib-sB_5yKGhpLq4fSKjOFLAk76tTbY-Y-r-08V-sJ-UrXnqPJIhM3Gx-KBDqFRFZ72H7VOKbW1feTTLFly9A02Qjzi5gdISU5EqZksz0JpdP-auvdEvNxO6CoA1kSGhS5pvwFWIw6LSwMyJLaRoDiEwMJ1Odw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/81014" target="_blank">📅 02:57 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81013">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">تایید نشده انفجار تو نارمک  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81013" target="_blank">📅 02:53 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81012">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۵ انفجار مهیب دیگر در بهبهان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81012" target="_blank">📅 02:52 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81011">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شین: ۶ انفجار در بندر ماهشهر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/81011" target="_blank">📅 02:50 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81010">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">چندین انفجار تو تبریز
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81010" target="_blank">📅 02:43 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81009">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نت شمام کیری شده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/81009" target="_blank">📅 02:19 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81008">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">تایید نشده
انفجار تو نارمک
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/81008" target="_blank">📅 02:08 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81007">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">به گزارش نیویورک پست، دونالد ترامپ، رئیس‌جمهور آمریکا، خواسته است که جیانی اینفانتینو، رئیس فدراسیون بین‌المللی فوتبال (فیفا)، به عنوان دبیرکل بعدی سازمان ملل متحد منصوب شود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/81007" target="_blank">📅 01:48 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81006">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">حالتون چطوره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81006" target="_blank">📅 01:12 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81005">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">چرا باید یه کوه اسمش کلنگ باشه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81005" target="_blank">📅 00:32 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81004">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اقا جدی انگار تو کلنگ خبریه
قرارگاه مرکزی حضرت خاتم‌الانبیا(ص): آمریکای جنایتکار مراکز هسته‌ای و حساس ایران اسلامی را تهدید به حمله نموده است
-اعلام می‌گردد چنانچه ارتش متجاوز و تروریست آن کشور وارد چنین مرحله‌ای بشود، آن را به عنوان توسعه جنگ در منطقه می‌دانیم و همه منافع آمریکا، هم پیمانان و حامیان آن کشور یاغی و شرور، هدف هجوم قدرتمند نیروهای مسلح جمهوری اسلامی ایران قرار خواهند گرفت
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81004" target="_blank">📅 00:24 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81003">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">به سیکتیر (۳۱ تیر) آخرین روز ماه تیر رسیدیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81003" target="_blank">📅 00:05 · 31 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81002">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد. در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81002" target="_blank">📅 23:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81001">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LejrFCI0AHv0mhZVyrplvA5vEOXo6Oo2gOo6UbS505o91i2sAsNuuoDWZagjpX_SZ9In8fdDVWpJGZM7MFBAIdlprZwyTdNu7-RlVbOjsihX_5P4BAF-v2o1YOWnd6VrPpAQWWib8vlcCtNPpPwDQ_-aoRPhjc99h1PlFGIAtwyzsrfm-DmydNN86-fnDMYRhe3kdqS4eGcmZhxb4ukyFFiFqzlbPlfHuYofYdla6_MnepQlLKqzvVgd8_X_nrvjEptcpQK51_p06Hv4kbCr3bQYc-thW_sHgIgv2J0T23OZuZ15E1CoGGsLzxY91OeSffEUrAhHX3vliOoPhjTMRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۵  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81001" target="_blank">📅 23:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80999">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Y76VBmnZTSFCJsd__a-ij1koJiXo30k0bww0K6FmjRyJxTBsWbPt10UbLHSmKKq-jkSuTINnh6Gu4Bg7jXutNGwSRQa0XUFmE2Vl77jALEm9N4TXFjhWE1v-QR1QlumTKUSQ7KZDrs4Yq3sHYZvt1j4PdozaDnjFS_32aP8thqPKHXvV1SHMAJUqziASq6S-fSEpozq5wlBZh-j026_c3F_Y674ieIWMPNAeQ5sq8XRRrsIIO7jxvh-ha7EXHAwuighCoi2um1LFZ03Z8eUMX3KdmQqlijNlVTDEudSRGflPvYmZ5QwO8SCG2UnoSzrh_-oQ68sHvN2Fw1mqRltaGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/umvqsnWwRBpUU2-MoTJ4PpFSG2dZtW2BMQSAxKfGCd6JhYBmNCDx5UEovdEUDaVVmF4iMxbUd7GE_zg3Z3A83gDklNpEPFr1DH_KmPgHU7P--o-Jpgf60sCmgscf86Iz8w-94eLmOM75Pz8_K3lOHPyDjNS18zHBLSzLmtx7abqnf0z3F-ValesYKlmjcZGH0PNnp_0S7z2XqaYT9lF5yISVBwSudzriPzzG3vEf76kNLCY-s1EBSgvD_XpdYTUrx0Wnfz9JqR4l0_HRP69OJp5Goa6QorULgdWLfpfaQhiyyfKb0K4bOVBABPhzi1CMno86R2vtt6uezMiqtwzh4g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">افتخاری دیگر برای ایران و ایرانی، بستنی سنتی زعفرونی ایرانی مناسب برای افرادی که ضعف رون دارن، بهترین دسر سرد جهان شد.
در ادامه هم فالوده و آب هویج بستنی به ترتیب رنک نه و بیست و یک جهان رو گرفتن.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80999" target="_blank">📅 22:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80998">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جدی این یکی بخدا عی ماخارنا ماخارنا بعضی رسانه ها میگن سپاه سفارت اسرائیلو تو بحرین زده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80998" target="_blank">📅 22:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80997">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">هشتمین روز اعتصاب غذای گسترده زندانیان در قرلحصار در اعتراض به اعدامها هم سپری شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80997" target="_blank">📅 22:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80996">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80996" target="_blank">📅 21:53 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80994">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sWDsjJjZvwRmUt12koS_H_NRA09eWyfRcPBOSSixK0sF879MOl7vB_U_4LuBVgDxhQ1ZD32QdJ-MNHH9LCtKeAlu0IQTSkw14F39ncS5ENBcaKvWewoJfDI7dvp09ZMr44vhRnyaKpUjBuxKuKOvBASYiscq1DhKm9b5qYzsUZXCKrXWW7xAJKzhFHp-scfHoIo-AM0JhQNelAumFxOAoWGlS0AiWsoROiRY0Hagpi4ZedyPNk7T8STOz9mJJipmcVdGdhlPrrKqM0kUcAsNIMoJ9xHWjSfXl2GgV7_TFh0dwZvDFI_g46kPYmuVeoICZTfgvZgRWbPbHwL922kw7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MYhSumtNWjXtPYv5hjFTyuEJh3fMibOPIGPt-S7xP2-zn_uKQJ8FjST0tKnRBVDfQEPXN39HBGuQatSaRN09Tx5oKJNG-EgwOCioTdWNAILUZ-RzbJfhaD-2rx0r_Iul40AwYNG8lkuwuTxNr17ZY0--GGmDg233rl6p7CWq0cgrmZFD61dnNfPIfn47lldErUJV0Pz5aT4EbpgKdYv7wpeEIAWfGtsT507RDB3CYc0k1wqA_ZIK3k2rKbbHvdPCJZIZJ0fQXTndG40giHwjrTNCJXYK34pZXQ7Jz1tGNNRzGF2EjT3H9uuOGzxvrkiakR_CvpAhVRTSjgh_BtHdZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وینی چرا این شکلی شده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80994" target="_blank">📅 21:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80993">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترامپ گفته تاسیسات هسته ای ایران تو کوه کلنگ رو میخواد بمبارون کنه، برای بمبارون کردن این تاسیسات حداقل چیزی حدود ۱۲ تا بمب سنگرشکن لازمه، خارکصه میخواد چیکار کنه خدا میدونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80993" target="_blank">📅 21:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80992">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">بمب افکن های B1 آمریکا از بریتانیا بلند شدن به سمت مقصد نامعلوم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80992" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80991">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KS5p1YEuZg5Ej-hLLruXrd-t1McHc5fUwu8E2RG7UHBnTwDmuKlb4odnDF3FtwVqXcaFuZRvLt5eC0yN2-SILWmU4hVqQTZN9sby-GTkTDwgxhuUqyp_1amgWIZaPGE9oVeTmkazgS71R7Ko57daj1ckMS4Co9Q1Q-7q5JQ2vKf26bYbO3xybgcABtF_jW3z9DBCbXhKneIFCZJH-ZsCvuA0QFUd5lSDy33vKNil_FL57UjPTjkFV-pyKFBzKf5-P3d-BFpLWCHxT6HLn0QOb1NYB7lY-qRRclZS9iUppIMi-0vfMoJFRBU-8LtcO38_xka7RJP8vnZLm1W3GQMo2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/80991" target="_blank">📅 20:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80989">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R5jW4Adi-etZDJDRByU0-CrLLSXjzcRgjIDNGiodjKJG9lI1tID_GEliy5QntLqUr-E8JCBv-lt7wD2kGWgUcTLPLJ3_UZGQXnQc6jMVrC00v4Q7fHoxqkC1rIGS-vAq4RwH-JCIlEEEgYvWFIhwmeybs9-Yh3ikHK0bz1yHuXxqzuKJdqlWuwt98Zku9iYEVRXsuWv3bs68XBPOJO3l-tKlbKhlr_ftUAOQatj-5cggFTSqUlhdCqJoCejal4kphwY5EPtU3VSeUmIWW9PKo36c6-WxjuXXfTiOdWX3aVAMhSVCSvbEF4KypeCxWCG5q-xjMjRE0I2dthQxUuZjVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lA8S6mCJGuGrcz3gaFYH_g5fn0ZSRRJv80AnvmK8n1_5a280uahXCrVd9KEN3VJGqe09Cf8-33avT6l7z9_bQKrm_ykhOmR2SSMI52XjRR4mvt590g2XYPVBLzX8qyu6d_1Nr6x9zQ0lrCy8d3jVC8G5PukYq8QcRNLidxyVaqrJCqpes-vTofyneh8Bne2WmM9W5nlsE8glfnkDa1uyi-mn9zlLzmPT9RzaADsZhcPqUmQahPbHv4K7Lo-R4dkMGEsvjnm42ZxVwyDBShfsUZHKl3A7lh7XPm7-QyQyPGpwKuJDC-ydNgs1V85ob-wZxtBR1_M4-AreEqiX_4SNbg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">به گزارش خبرگزاری verse خانمی انگلیسی که با خودش ازدواج کرده بود، از خودش طلاق گرفت چون تو رابطه به توافق نرسید و احساس تنهایی میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80989" target="_blank">📅 20:21 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80988">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=IobZMj5sw-yNP80rIXJM23h801SpZSYtKR2Y24-4ldwAE8yyFwIJ8D9N8R_DtJJAes60JFee91_UTERbje2iBgDxg8B5XPmqdvDOtkOMjduyczMrqzMdH-WEAcgeJkBjutt-BbuV4W8eyTgTjEPxn4DP5La1j1zwdeXTRerbCfnGWPwe4haRjYC3tEm-DUCYdMCQMjmKweCOWTPNiq_aswhIjBjmjHNMdzkuQfvGRrdNaVbYKUBL-7vLDbM5FwKZxqYkeb5QchfbcjVOHRYO4YmZH7oCKUjIbK6Ebv8p9EC2rFIt0vyJLiUQ0sM-Bp85SSu1vNmMUD_sXMtv2II1Sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc36a1a784.mp4?token=IobZMj5sw-yNP80rIXJM23h801SpZSYtKR2Y24-4ldwAE8yyFwIJ8D9N8R_DtJJAes60JFee91_UTERbje2iBgDxg8B5XPmqdvDOtkOMjduyczMrqzMdH-WEAcgeJkBjutt-BbuV4W8eyTgTjEPxn4DP5La1j1zwdeXTRerbCfnGWPwe4haRjYC3tEm-DUCYdMCQMjmKweCOWTPNiq_aswhIjBjmjHNMdzkuQfvGRrdNaVbYKUBL-7vLDbM5FwKZxqYkeb5QchfbcjVOHRYO4YmZH7oCKUjIbK6Ebv8p9EC2rFIt0vyJLiUQ0sM-Bp85SSu1vNmMUD_sXMtv2II1Sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80988" target="_blank">📅 19:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80987">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro  پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان ‌
🌀
2 کاربره | 149 هزار تومان
🌀
3 کاربره | 199 هزار تومان  پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80987" target="_blank">📅 19:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80986">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRetro Channel</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QqQ8PSyv1sgNa_5-BOTFRJ_EfTExsKvLF_bXq_6l8jdL33wczh-Kqb-R_ZLmXzVRkS9heT5jCZg5yD5nqI_0rawMeDBBfCErUP7iMcCW5PDhPB7ixESvPjOtXszAEC9i-hEsg810EUEV5O7PQl_34X_Lkwh2FsMjMzyFiFLbRnc1_0ycbJHyvNIXHfNudaR8GeWdGpeyCccG0pqpbZdcGS0rcRmaEc9HTrA1P0YQwSZ2T8aj8oC4fwSb3As7savAph9OZBeB5y9lWWgD_Yq6QCFvUASdi5TXHtr4_V3sQrVtb2_swlPJqKrJDJhxbYcgD3Hy9cFx9NlsOucZIQzr3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗣️
تعرفه سرویس‌های Retro
پلن نامحدود
1️⃣
ماهه :
🌀
1 کاربره |  99  هزار تومان
‌
🌀
2 کاربره |
149 هزار تومان
🌀
3 کاربره |
199 هزار تومان
پلن حجمی
1️⃣
ماهه اقتصادی :
🌀
10 گیگ | 30 هزار تومان
🌀
20 گیگ | 50 هزار تومان
🌀
30 گیگ | 75 هزار تومان
🌀
50 گیگ | 110 هزار تومان
🌀
100 گیگ | 175 هزار تومان
پلن حجمی
1️⃣
ماهه VIP :
🌀
5 گیگ | 35 هزار تومان
🌀
10 گیگ | 60 هزار تومان
🌀
20 گیگ | 100 هزار تومان
🌀
50 گیگ | 200 هزار تومان
🌀
100 گیگ | 350 هزار تومان
تمامی پلن ها دارای تست رایگان میباشند.
⚡
پلن های حجمی بدون محدود کاربر هستند.
♾
مولتی لوکیشن
💸
پشتیبانی
7️⃣
/
4️⃣
2️⃣
🏪
⭐
با تهیه یک اشتراک Retro، به اینترنت آزاد و بدون محدودیت دسترسی خواهید داشت.
⭐
خرید
|
کانال
|
پشتیبانی</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80986" target="_blank">📅 19:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80983">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LteS8xBYD4Lka5TE2v2WKOfHGj2pzdu57l4JMkxkRBfGhUOVY0OoAlOtxfz8yaF8jZOZg3bAcqdpEonnRe4w9GCis1kRIKj551A6OueWUJeivz6sHH-37lV9IUIXI4SgMTVdyESdJvw4A4XSFyzzd0s7dj8PeSrVMz2isksf7yq4nnVZ3CharE6_MEvs3eZcqJT2Tr1z0TKdqIGHWFdRz27yKSL3nAXT476dlhUyDGSoO1Zc_S6h7bK27_woPMAMhAzuYhzoAIm5lXfYF3IzPERgnveK6Fq0PWGufkp_SPffrqts9CvrdGdR3PfYRPRUj2tPlXE5gTfzV33PBrtr2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PgYAVkHmTlKvjZL0lUrTOXOcuI2iEj57xUjYtpfUAlZSVDPkFSS7SsYF6wUaYLi4xxJ10auJDvGz5jUVxHIAfUUL8w7_SkjUSfCmtGkSBdi5B_Xmy35KEoz2mTMP0T28uqCLr-yo3vuIhIxTc-TfrmKoc0YpaJlEUQ0B3fHKGAS50xULFS7TgqwyHby3wZRct9IJFt1jXi9AxYBffslqYMhjwYy9RgVzLlMOS6lCy2HN1TChAa0JDn52kV6unSPer-gdAJoCqKjWWGjI0bKZYV8yow063ZVrESCEtWzefJhf7HE6YSolbpIa5aJrH63_IucAn_td9yAfTqw5aTrDeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uZDts_2C_XVicqblfMdt_1BwsnM3-QtUd22ASsVs3z8DqjfP6zjtDOAgUudxjmMz16_lOPLY6UkIhDh8sC9uskhdFZSEehRp6Fj7h9FQmD7tCcdkyYX7t_q7DMcqBbB7fCQgBOvmywZmNeMP1ftrcV16TVRf3yb29RF4VQTGh_NHpF_CqFRib3St47fMauYTXyoWaDDkYWP8PbRV_sA1qoKYH1n-AuR95_IHHkjRTQ7pUpxe3NI_NXqu5KmbY8IPYuKd5RNdtBIsXfWCGMoRgdrnCvo7RR-YxKm3IaFCAjf1KpGO_14PBcfpS5AMndGbixq9hYcjl8W4sGuKNXKEow.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فعلا عکسا ربکا رو ببیند تا من برم و برگردم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80983" target="_blank">📅 19:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80982">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=mj-8mHxcxP4Pvy1k0wsg-i4BD4K0GJXXuHOOC2R-T1DeEeIZupU76wrHIYY32AhhewhxcAX8v1c2isVTVBBJTIUBU1z6rVRdzgrD9WrzJ96qlQkku2PdedGLLCZ8rc1gONmKWC33IcmP2igRXv0ye8AL7Y6ucAZ3hiAIpEykASpvKk9RcqU5B4OWSHUYPfhpnrtnC7nrbvtv0AEmtMs1j1x1rit9PD_1Ftfeflhjz-8-cltlObh9e0DNmwPDPj_B0d0QgnMDQz5Idm74CFQDnNPl7BkBDyiXiad8gfEjypaVZ7t6azspRtaA4q97WTwLC1K0TixQtViPsV7CRIC8WwrBK5brMO8a_qdOdUlaHXzIXvEAnj4aOwamtdMMud-uR6InAmJQkPxUXBhSkVTWGq1lgO_T3MelkCz2TrjWOT4FWsu_NgoBCYvGItY3o2Ke2HQm4OlJO46s4KbBlf6sThXPIZInvygCOxJ2B_OelPt0KZILZmAN6J8mD171fA3cPG8hhHd-eqe70OpW6KkcaRKE3DO9et5SsU4cxOsVyKrtuzeYu3vjzctZFDLAPy_7UGoUN9vK4N7Duith3cJSzo_zObZXmB8rTaulQtnDb4euoaICMRUUorjtp5XpbcDjDWzwU_5KJOrp1hN7ywcSGcLLe6LyHphVRbfhG9XzOOc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4221f89e3c.mp4?token=mj-8mHxcxP4Pvy1k0wsg-i4BD4K0GJXXuHOOC2R-T1DeEeIZupU76wrHIYY32AhhewhxcAX8v1c2isVTVBBJTIUBU1z6rVRdzgrD9WrzJ96qlQkku2PdedGLLCZ8rc1gONmKWC33IcmP2igRXv0ye8AL7Y6ucAZ3hiAIpEykASpvKk9RcqU5B4OWSHUYPfhpnrtnC7nrbvtv0AEmtMs1j1x1rit9PD_1Ftfeflhjz-8-cltlObh9e0DNmwPDPj_B0d0QgnMDQz5Idm74CFQDnNPl7BkBDyiXiad8gfEjypaVZ7t6azspRtaA4q97WTwLC1K0TixQtViPsV7CRIC8WwrBK5brMO8a_qdOdUlaHXzIXvEAnj4aOwamtdMMud-uR6InAmJQkPxUXBhSkVTWGq1lgO_T3MelkCz2TrjWOT4FWsu_NgoBCYvGItY3o2Ke2HQm4OlJO46s4KbBlf6sThXPIZInvygCOxJ2B_OelPt0KZILZmAN6J8mD171fA3cPG8hhHd-eqe70OpW6KkcaRKE3DO9et5SsU4cxOsVyKrtuzeYu3vjzctZFDLAPy_7UGoUN9vK4N7Duith3cJSzo_zObZXmB8rTaulQtnDb4euoaICMRUUorjtp5XpbcDjDWzwU_5KJOrp1hN7ywcSGcLLe6LyHphVRbfhG9XzOOc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید دکی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80982" target="_blank">📅 19:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80981">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rfVF6z3qvAiNlqQM1K5-bGXkNC3km3DITm4cQfI6ZPX7C5ivdEyQskRAki-ZZy2m5iuLiGM5eio_sbDlnGFNp30zAilw8ikmbXe3jfUcvkbaBpGwpQXx77n-WVUfXHeMFNcDD58IXpcMrsfOY82DiHjUy0qDoepNnHxobFQ2_QwTKKLpeUOtXtxQbzh5pl4dUa9leX-qeNWLnYn7-N2_rayilU92UWAMT-qKZFpQ9TWpnM6BpvpjjYE8AV_-z9ewkiwseCkBExKc975HNLo5SFJ5_1zSd7yw12_UoVPLZeu93N0HF5qHMYncQZwx9_v4_z9Yfa10FHg9CKV-3iGKDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنگوی جبهه مقاومت شعبه اروپا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/80981" target="_blank">📅 19:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80978">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b79960724.mp4?token=NYIPQWprjaL5jL9wRP6GlbIvJ0QA_BguXNbfWheXAg7fGy5amK3IiHXrtZ19BHSCCQ8RF0jkBoJxfewhaK-EP8c7n5ZXKH0oDfXGBgiCdZE1Og49ub4SImGtMO_Ax4SaS9VDLG3nc2gl8Q0XmqJkXeBqN8NwyDjOYtwFKfHwmkRTBy3GxuldePQwl_61Nb-U3CmpAL9F2rCJWzGS-4eFMZZpjbExFhmhbTENMGqv9yuYZwxFrflL92A1lzvNaiR26wYsEidwkDZC-4uUH3vMT3-efx_tBqvrF5XSgPTuUfnGMwmNgNzCUYVeJi0Y3zMv_AGECJxwB9llAoA1mYLsYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b79960724.mp4?token=NYIPQWprjaL5jL9wRP6GlbIvJ0QA_BguXNbfWheXAg7fGy5amK3IiHXrtZ19BHSCCQ8RF0jkBoJxfewhaK-EP8c7n5ZXKH0oDfXGBgiCdZE1Og49ub4SImGtMO_Ax4SaS9VDLG3nc2gl8Q0XmqJkXeBqN8NwyDjOYtwFKfHwmkRTBy3GxuldePQwl_61Nb-U3CmpAL9F2rCJWzGS-4eFMZZpjbExFhmhbTENMGqv9yuYZwxFrflL92A1lzvNaiR26wYsEidwkDZC-4uUH3vMT3-efx_tBqvrF5XSgPTuUfnGMwmNgNzCUYVeJi0Y3zMv_AGECJxwB9llAoA1mYLsYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو جشن قهرمانی اسپانیا یرمی پینو رو اینطوری معرفی کردند:
قبلنا بهش میگفتند کریس رونالدو ولی فرقشون اینه که پینو جام جهانی برده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/80978" target="_blank">📅 18:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](𝙼𝚎𝚑𝚍𝚒)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1PPQahpR4KIW0HOm8GcplUtWrhc8CdT6ninfao-18WqZzXBMoWxWOwmBMMZaEpxlX3U0AgBhfnEAdC7VVJ0BQHLITxtoxt56JNCDvClHcmZ0xHWx47Aqfp_Jxx9SRKiPwqVNwuQS7nrh2c7pWXob1nmZ9Bz7t-4LbdBRg1DBMixPXK_LjXrFi2rLqnD24c2TgdtAAPZfWidWP3T70hiqbpcoLYUCfs9nnANH1G8osSJl8Fpfu-pF9ZPiwc0pX1ZBWgplfNUybdxN5aYBNVgq7z20ldK6I8wFU6uFoutWLgZeWeBUAuLo0k4w4wtyhYJZWsHGSj8qVspmgP-zoviIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حریف نبود</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80977" target="_blank">📅 18:38 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80975">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">بگردید کارنامه منو تو چنل پیدا کنید، قبل امتحانا یسر نگاش کنید امید به زندگی بگیرید</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80975" target="_blank">📅 18:33 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80974">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">امتحاناتون چطور میگذره؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80974" target="_blank">📅 18:22 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80970">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خب دیگه چخبر</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80970" target="_blank">📅 17:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80965">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">آمریکا یچیزی حدود ۱۰۰ تا سوخت رسان تو اسرائیل جا داده، این تعداد سوخت رسان میتونه ۲۰۰ تا ۶۰۰ تا جنگنده رو ساپورت کنه، معلوم نیست چه گوهی میخوان بخورن.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80965" target="_blank">📅 17:47 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
