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
<img src="https://cdn4.telesco.pe/file/Wb-Ss0AqSTsFYj58dPUV2mO2qoM213g3lwYFUifnSBumLlKDHE83DeGHfF8TFnAFKOrm6PPcb5YO7G011Hco2jdosLJ1D9HGzFljKNFJ7Pgwt-5tB66NiQyyLxNZQwEmpsPeqn48j8nIDGYDniNTAsJwMoQFFiYGW0xXTzGSk7fjNEmkPES2h4Mw1D_kaAliBZ2tJ2XUOUBM02AdhatrewoRlligoo09ekpDESD_9J9LXsrRfwQvLhHaUlRPTNKcUN_Gv9IvS65waEpurPWt-89mvOHkJH3aSxeRZatOcczToWPfXq_ybKdVIRLrXAL3FxAqngUELrNZEx9ZwGOW2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 171K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-27 08:52:21</div>
<hr>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYx81fIi1ds0Aq46P3vslxSua8OUP9eDDF-Ou2fMsGeG4XwUgi1FDIKAMhmssBOoXTzaRSCfcDky1X9Xn-8lCtp6Kc6AUdu7HtnJAIkq2silaLPHDrTVGg5zIuuf3-rY3QxYn2fhR1HIowgtZuYx8zQvXO0dur_VFFqsiymDHY2VTVGdMgzaYmuEZCDVQhc71x6XelrASw9Go6poxvy16WvEWTNHZjS1seAjtG_WSMh_l4Tg-dgEPP6KNx8KwinLEdZZ0navWnDEElQnXzxixeKPjsuJOqgwYyFFP1k7w9kPzFfpZLLDMuDXjZUJj1KAMGVPZKCi7X9W4Y3ZuOG3OQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.52K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78083">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گللللل
لیونل مسی
کارگردان فوتبال جهاااان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.67K · <a href="https://t.me/funhiphop/78083" target="_blank">📅 05:54 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78082">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">بهتره برم اول وضو بگیرم بعد در مورد خدا و اسطوره بی بدیل فوتبال حرف بزنم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/78082" target="_blank">📅 05:49 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78080">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">بهترین بازیکن تاریخ چییییی زد</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/78080" target="_blank">📅 04:51 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78079">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">سنا با محدودکردن اختیارات جنگی ترامپ در قبال ایران مخالفت کرد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/78079" target="_blank">📅 02:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78078">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">خوار عراق رو من گاییدم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.5K · <a href="https://t.me/funhiphop/78078" target="_blank">📅 01:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78077">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هومان بدبخت یسال موزیک نداد مجوز بگیره، تهشم بهش مجوز ندادن دوباره شروع کرد به موزیک زیر زمینی دادن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/78077" target="_blank">📅 01:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78074">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBPgEWvdz98N1Zv_DTLraUsIzrZKvaSs5EL4NISN4t8g30svwoOvQiR0c73Kx_5Aj7a3-38Uidi-ipDHzkNwk9HwZ-dtZdprBG0BcG7-_cZF9VrUEzGSbCMfeXAld9P9ar9TzN8TEGOUmzFmW8oyVe0BrFrZ9mO7wD5WsOFJsVgyvM2CDHLvHU3yQypiLt2CnF9SH1a3uO8lIXeOlcO_15dB5-gvDFhAJU_PBdggxf1LN1s56uVdTdXNH83ag9mHWcyk22Nf8uRZg0d_LksU4iY6Kde-hc4TwCJnEdBx55tqcqHatEo-5j7iwYurPSRfjlQ7RO9p1yilULihwbIC6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کصکشا از مزرعه‌ای که توش کار میکردین خجالت بکشید، یعنی چی صفر کارت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78074" target="_blank">📅 00:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78072">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">قبول دارید کسایی که جلو اسمشون پرچم گذاشتن زوال عقل دارن؟</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78072" target="_blank">📅 00:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78071">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/guSLL-OOwuKLZDhAc9Wsca8IjOkENKy-j-_9TMXoUcgVd0yEG4tgQaYCwPc8vjBNDM-ixyOKWVejcv9xFZZ1aHVT5MPIrEDWy6wm_Da0yQx7j4aGL6GWnkOfXtbfyy5_KQyTU3hqSSHU9SeVjfzArSnlFvyvKuNqW1zvCdIjg0GsKceksEwvOKXJJwd4mLGX8OaqQTTg99ZapYJoV2clgSPznc8gH15HdRISjy1uMqNooVYRS931I7JgEkzG5TMnCPGjoZ0woIWQin8T1LNofCZHoCoK8J5GbOBhTe793HeDHsAYHOxOImjlzBWbycfqfNFmzZauscRD8-EbzbOYiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78071" target="_blank">📅 00:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78070">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">احتمال قهرمانی ایتالیا از پرتغال بیشتره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78070" target="_blank">📅 00:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78069">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78069" target="_blank">📅 00:22 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78068">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">بنظرم از بین آرژانتین، فرانسه، اسپانیا، آلمان یکیشون قهرمان میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78068" target="_blank">📅 00:20 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78067">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گل دوم هم زد فرانسه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78067" target="_blank">📅 00:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78066">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">این جام جهانی احتمال زیاد امباپه رکورد کلوزه رو میزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78066" target="_blank">📅 00:06 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78065">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">چه‌ گلی زد سنگال که رد شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78065" target="_blank">📅 00:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78064">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">امباپه زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78064" target="_blank">📅 00:00 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">کیت فرانسه چه خفنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78053" target="_blank">📅 22:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">پسر اسکوادو نگا   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78052" target="_blank">📅 21:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t6okJ6oNRDEy-1WHA0RFLRYQ6t_EW5IYV6sg2aiJrEERYJ4NKUrSDqygVZNo1sKKXVf0jFMhxoc7XCofFjlmeuGlxmtOF3dRq-QUZKubwpmufHcMkVuBQeJySYHptPRGZ22lKsCBc-y0ZA0lIx7O6BDIQWqT7PZQFNZIzPI75_8Kg6bSa6loJL-kxmNhsRW2NdCljt3kZxno-SelBFU7OmudTxW4aDJmTYyxr67DjI8u_gkCwCvMWXX-ia_T8U4hFRs1tUW-Ar9hUoEA7rDsYA35DBhVeuudYpkgPy3n3S7y7PKPzcEbqWvZ_xxf_4xQ5nucXn77GD8PdXhF1sp3vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر اسکوادو نگا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78051" target="_blank">📅 21:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">نامزد های انتخاباتی در اسرائیل تبلیغات خودشون رو شروع کردن
و جالبه که همشون از طرح هاشون برای دشمنی با جمهوری اسلامی به عنوان اصلی ترین تبلیغ استفاده میکنن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78050" target="_blank">📅 20:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78049" target="_blank">📅 20:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iknjyocQ6z4gCke2gMZSiuHk3OUniDTa70h45w2iMKqGCBoBUSy1nhfK35wybx9tRWGSkQDkRmqI5qi8oXXRseVqX13fvgWVvnj2c1SPNqlrTIfENDbHwQ2Nwc8PgN4rHniz7u2RoQbmu-ROzQ6hWcHnRoT4FnqccobAoIPwE7LtYcr0LuyPiJKaPeWTZnG7BWB6koHcJS3HkCktxUv-SsIbgVZX0XKcvdUw2hCDTBQ_Yf6zpgMw1Sq-ap71MMvny99N71vac2DUUgORR8Ds65MGt4qLxlDzdmbvCOsK8jkxW92BCahGfkCuudkHj2Zghw1z-wP46kwVc2RRHXKmbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78048" target="_blank">📅 20:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وال استریت ژورنال:
یادداشت تفاهم آمریکا و ایران به ایران اجازه می‌دهد فوراً فروش نفت را از سر بگیرد و ممکن است تحریم‌های بانکی و بلوکه شدن پول‌ها و محدودیت‌های حمل‌ونقل را برای تسهیل معاملات مرتبط لغو کند.
طبق گزارش، این توافق تسهیلات تحریمی گسترده‌تری نسبت به آنچه قبلاً اعلام شده بود فراهم می‌کند، که احتمالاً صادرات نفت ایران را گسترش داده و امکان بازگرداندن درآمدهای نفتی که در حال حاضر توسط تحریم‌های ثانویه آمریکا محدود شده‌اند را فراهم می‌آورد. (لبیک یا اوباما)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78047" target="_blank">📅 20:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">رادیو ارتش اسرائیل:  ارتش اسرائیل قرار بود در ساعات آینده حمله‌ای بزرگ به ایران انجام دهد که شامل ده‌ها جنگنده نیروی هوایی بود که آماده برخاستن و هدف قرار دادن اهدافی در سراسر ایران بودند. این حمله گسترده با فشار ترامپ لغو شد.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78046" target="_blank">📅 20:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSoQAuXWJ_pKIT37qYUx6ZzemGpXhbAMOtb3IzQrFFX4oVJu2cuDtPrkWfkSc_gWRC4RKVLJy4w796erXFGtZRlORiDliRHOFzuJWw_sCGtSF-cwGwvDEEJYcyWnxegSfLMC8frjM9QauoHXlLb7XEMzEqQrXmLQcTnoN0HezdwfoXwDMFwDSNsbrD7NcQHwQx4BXlqc3myfpkSs7zMaetS8ZI_gYzEqhhyRlpnqtKOADDt2c3A4PLqX-NQOaM--C3J6RvRHghYC9XjfHjywKfRGm64hDk3MaGMOwUZf8KnI-aRKsEA2LTD7QZOdho3M-z0uMX6x0aLhCzFcCasL5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خاله شهربانو ازت میخواد همین الان یک لیوان آب بخوری
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78045" target="_blank">📅 20:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cZVah-eooDnZXFK_qduNu6KqfVcCqEkr-q3KbqBaiTqNCQdWhmPd25iyleg8rPkKbvJxKrwPXs3k0rXs7WYn69Gnv9RBet1kZ-DkWbupnosvWyiYfu_IQJGTvh3xtULxnhFxaUfgVpsIhuiwQ_4Ls2B8dxpd_n4HAcRLPk0DVWaS6qVtxh-KbVgbjMK4Y1KVtlT2Ontc3SO9lIfvfev3uuSc6trt6RQlluw8bqBy3SHavYO5ldXl85lVHU2EzTpLOKZenlIhSIy-u49s6LgP4WWNEZdXkGj6RHDBn-QU_sOFZrFlt8At18BdcecPPglqjQbMRx0S87LTI8ALD1H4Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوکو خدا به دالگت رحم کنه
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78044" target="_blank">📅 19:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fAn2hLrzK735W-6ZS-RPzyawNRTkPjw_MLT_iTLyFLcKt6pU_Tq5lvSQECb6kx2Ux5YgFJpuseMoziE9psBnzYujCX9uZQDrCSR_PcuIRha7FpTVM8gEAt1NwfTbufqLfmGElnJ-gFYj-GtW6NjrNQl2JlNQnIJaii_VVN9J8hlgpmRzqGEEfh1h2mEEh5iAbmmb9JCcfQYWOaGrhxp--rNX8LY-L2En79pS1SEo5Pt43xYlxbx3xqsz6ca2KyOT_jmkW4h2K-iqMhC9WXioeUOOuBbP1shYHrCTa7Uj_xuxHLzQdRGT1VEJ9dzAi29e97HMUeK51X_nMEu0y8DAWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78043" target="_blank">📅 18:02 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLx3NXBBe8aD7ntYuNxLU8G2EVqwK5VQxUCqHhoL1c868hVHo9lHFqOzN-EAktYvy4FvONQ34PTsxX2EC1bp8HH-sWdc4gP75-v0BFtRAgbVLTNUeI0ho0vELBnevaeRJ0Ovzea8MeJmeNxl4p5Aoc_BBPtUXTjlldXb4NzyWmo0yYOgV3r2drKRAPZV0jMR8lAZeyksHnPXR9ngqvCUxF9mA7Uvz2LAUiPcqVJJY2wh8MJ5rQ_eMPpKsmVmaXhEccP1J8sRCQ3SErLFw7xN4Dt7VgO-NKWyqsByTO0UgVCoT46zf3O4doDFfGoa3oYgmmi-T9ql_vf97aKGar-mCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همیشه تو قلب ما میمونی
🥲
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78042" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/funhiphop/78041" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mjMq2oSlpT2Ow_8gTO2o-Z09mVksn83Eac22qfpGGHX1U73YtCWsgEsZXaBVYXWtLqf_WRSDgqhRToHSniqlFmciE-uGQAG_zDu1cr7-PaOQtGaIhGd_DHKuo9sAyVSmfs8QXPvmhvHHjhHcVYfighQG39BLH47gZZb1_kvx48yuHd_8zcJV-F2CyUhnIHqLUjgRtYXtdsZttwg7bde4OYdXshGCC00E2KgIPQeQwKJ2o7cAiJ27Vti6OEBWIDV8c6qN3LyuwKPj1x8N0_uPLwj3obsmPQa0yPanDugM7DIqdqs-J7MBK_T8uZnhIqP72N7NsluRq6pwj-woMM0mfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g26
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78040" target="_blank">📅 17:56 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده  باید ببینیم تایید میشه یا نه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78039" target="_blank">📅 16:46 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">بازی ۳.۱ به نفع ایران میشه اسکرین بگیرین
👍
😎</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78038" target="_blank">📅 15:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78037">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78037" target="_blank">📅 15:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78036">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">شایعه شده که ویزای مهدی ترابی و مهدی طارمی باطل شده
باید ببینیم تایید میشه یا نه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78036" target="_blank">📅 15:37 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78035">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf7f045c16.mp4?token=SelYTSpwXNffNH6q32vOMuPCb_uIhMj1GzrOstPIp9Gq15wgzZFY1hLd7-ey57k4Al09crl80WfcdfNyB7l_KsTbCBBAsEHrqbjfkcK_VWf_TG3Sx2n6Dr7H5umzxUAxY97g3NNRMWda6KfmhV762gJyyZA0wxP15vNmLsTgN1hkYENJqCzv89m1IeX52BCmPVfJ-fIIPXuoN9lvdR8Yl9dIlsl0cuGqKWtuymb99kgVrbz5ak02JzecwE3164AY-QmV4NuZAEZcGWD83FQfea-FCZf_dQ6JbpOlL1FiUGGr2DOS5j3qnsWoQZbIk7Zowqm5AJdbxlKEaeGTLTubew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78035" target="_blank">📅 14:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BXtk02OVHd3r-o89dz3Iu7eryjb9HDLqM4xGjFf5f-JE6I2uLobzwkkSSv81hp3N0T_kzP9akVj6jFO9O_BNTSpswlSkbirttJ-OJnfyjR2zrQpufUMECzp53CxaykxE0D_idueR5hGWz2P6tRy3Gz5lKK5Zs26DvHopkz7PG8GyvdSH1hH4ZPVIuaRO8yM9lzvE4zQxapsj0A-kSQdMnd_8Z-bXBipPYUjYKQ-FvxiOKuJUDxaPTW2GOweMGghaY-ARwL6pEJn9rcQsjj43XtZKFK6h4wm-SjGuLrqGznm2x3FrwCT9F39G7w_vpKyK9ZdwMlwPtfqXtj8_xhaFKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5d3ef255a.mp4?token=bLk5O_TOHGmVXxnoyAmNMnRwU6bJr8_42yYRITnpN0NFoUqaHZwnQO2zOXh4bZuTJLCHDmIIOJsRpzZ-Bq2sivnwitUvglNcDhwE_--B9kWpvUm0ZZ0rdEutprkUdQs8TWSqBfX8URMsEF4r9Hcwgasag_oIYCUjzxObCOJ3w05bOu2mEFbanEZQw6hw1yfWBK6OY6n7bXCb5q-vsVy0VXz3AwkW4294S7NO1mElwUa1oudBohEo803406jXJ-k8Zm3HV9fm1S_EmRKOlaXfGJFFZN7AnvLGVjRBvzhEUQaldG7tHSucBaj4XBnxVn2PQ8ywkcwcuQ-BIjJaMKLqBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون وسط محبی هم داشت به در و دیوار شلیک میکرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78033" target="_blank">📅 14:09 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKHmCh5JLhRhLRml3vIg5opnNCJX6cyK8RlQNnW4KxR8--rFlYJIR2y3qLV8Qb2thLBOY0_48YFNwFdb_wE6CHPp3Ca5oFivP8cSq08p0603imHH2_iCXz0KZFVjSlodXtUorJvUqXm_71pn7zxE_k1mwDhLoq6O7V_xkKAtLBdCbHRmyZ3uQtpCZjrHq3Ne1gRfGI8biWHxkfbpBLi5t_OLoX2pFOPifoD1B8yKroN1UG_iMfoAzTCYc9rShhMsdrJ-JafBKQheMWBmXFBN2A0uW83QeSy4l0avtgtr0pqddFFONCTuoDyYpPip5fn6EFtmnigf1dn3xu8ItOjgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78032" target="_blank">📅 14:07 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78031">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78031" target="_blank">📅 14:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">یکی که از تحولات ایران خبر نداره دیشب بازیو میدید پشماش میریخت، همزمان پرچم های شیر خورشید، جمهوری اسلامی، لبنان، اسرائیل، فلسطین و آمریکا تو ورزشگاه بودن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78030" target="_blank">📅 14:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">من به اسرائیل پیشنهاد دادم که سوریه مسئولیت حزب‌الله را بر عهده بگیرد.
@FunHipHop
| دونالد ترامپ</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78029" target="_blank">📅 13:42 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">حکم اعدام جواد زمانی و ابوالفضل ساعدی از افراد اعتراضات دی ماه اجرا شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78028" target="_blank">📅 13:00 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">حسینی با یزیدی صلح یکساعت نخواهد کرد؛ قالیباف و ونس توی مراسم امضا حضور دارن.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78027" target="_blank">📅 12:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln136Pl0g530iWVCexnLpBIEkC4Hv4vwaTytLurL3oKfNF2gkgu2d5dR0RrbBc8zkKLO39pehAclXoDYwetC7QOmyuOGZea8ABQrUVsXqVzhP8Rxa5dYBRuxqnc-zqQs1lF5bGsSjdLoVNfyoG7iVlDCcE4bf3wEhZ6wcnSFLq1dm05xzgrlrpJ7twchDdYF3bs38l_9u2xr9gLMWQDqVPZb6Jj4iM1cCRqlVguRFk65WShYBut7Qj1VKrB47BUKQgnWcU0H-xWT3qn_Dvz5PE2tflobHKUqJL9HRNpZRzzHHO_DG-6QFbSGNuNTnn5i21mAC5w8L1ayLdED8v0PVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها دلیل باخت تیم نبود این اسطوره بود....
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78025" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78024" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78024" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JxrHBbm6Ckj5FaZOH98wdDBSiqT0IR34CKZHgoYCBJZMVqX01asa1VWqpQ0ugY2TqTUhimnPskywccpq0NVXm4NidLT97hLmYmec1Y9kRcWpGDmSbBbHN1avRFyo7Nvzp04uvKWRaFptoyjnepwtVIVWK0VzhGH12v-WFQCsDBk6RguSi7hdPQQ2MQX64H28YCVYlLl_QOYmBNxvL-94BMz6Uy9NfiDjJmwiFwUki7i1q0pHMYeOGNRGnVgeSf-AbwvX5MKEd2TQZrwmYq8Ebq7jLEy1oqdZ6VUCN50bauVTs3POmNC4ugwcDHatWxVzRZrBe4ywrEVvcTRWuR2ybA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r26
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78023" target="_blank">📅 12:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">بیرانوند: اون دو گلی که از خط دروازه رد شد متعلق به چین و پاکستان بود و عوارض داده بودن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78022" target="_blank">📅 12:28 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بمب افکن بی پنجاه و دو آمریکا تو رزمایش سقوط کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78021" target="_blank">📅 12:17 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۲۰۱۸ بود ساعت ۵ صبح داشتم از گل خوردنا تیم ملی حرص میخوردم، ولی الان تازه از خواب بیدار شدم نتیجه رو دیدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78020" target="_blank">📅 12:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromDiscography ship(blue)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjqRRa36xYrPvghTfWUoK-xC_RKEUJ_KzjfuYBH-jd7HUmifreC50bOsXJSHTQ4jXBCNt2j5iqx5vFWkWm1Kjjkb_0vZ0ellQd2NU4y_Z34QEFgVH-M5wBLKom6WIPf_mcVDbK01W2NnyCmayUr8iFSaQ8pF_G6yKEq2eNT3wjv5pF7EbS_NwvLYs1VWi_-gFuxNeVKGfPFCFlVqATiwBzlKcWPyCE8VA5sRA7HgFyasJ624f-3D7mG9z-lyp8at9TntmcPJecvJP50IaKa10mPiqgjC48WukJFK8INjAG10WUc-P0W4XO5MSiJjTc60f3jv7a4giqKckV4Hpw_OQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Complete Albums Of
Playboi Carti
📌
I Am Music (Deluxe
)
📌
I Am Music
📌
Whole Lotta Red
📌
Die Lit
📌
Playboi Carti
📌
In Abundance
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78019" target="_blank">📅 10:27 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDiBAiLM5UbAVbeOOCMqekehQr7urScqIosr87wbgZt3JCBNQq6mKDmgp9ysW9-0q5dQzcRq5MwRP6FyHdXsc0iWQjmLONY7ExtVnec33uUEu1TX3OiwtQhwXi01VRSGT73GGjy3y7q8lgHX1NNcaYOCLVm9jXznH_WhpPdMTNK-SzV4GEpqVzL0s9J2tD6xcx-v_kFkCAVY02s82idumHPjW1MGXyhGRBmYs5Q_KMst8mHvUALH9sqb37xi6-x_pozlCBZj5K2zZ-rsDfWDjo7zDVWme8RE-H2fjqm95FPL-ptz4zp4ErQTpqs46xmQg4XmZkcWgdSUizOk48LF0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ffq81hOm-mnl3VXcjI8yQ-BX8ZvTVtCeXG8eT3O6RrLsiJdGGnrCpDwRIXCg7iPU4XcLkwGGFBFgdZ1HHakpXEhmzsiL6R6OtFpxUZl0KBV-AxDnztIoLx66f-UGOJUKvP2yzm4iDbBPTEtXd9J_IXaL44XHchAXkJbnEQHvgZQZLp85saRwEnHFjIWKW0LODTPFM15Nhow1MyyY7SfOozGB47bhZfs_6dwgljo5krgFxQXxN3IT4mjosbH7iPMUIxo8vvy0OIqc8h-sIbFNuuO1TJKTwbJWv0tmUlJZtAydwp6ZNtgljGSCgSmT6k8b6Ohy4dbTx0KmglVFdTBcyQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78015" target="_blank">📅 08:10 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینو یادت باشه که همیشه تیم‌های مدعی قهرمانی جام جهانی، تو بازی اولشون ضعیف بازی می‌کنن که تاکتیکشون همون اول لو نره. صبر...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78013" target="_blank">📅 06:40 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78012" target="_blank">📅 06:38 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">بنازم ژنرال تیم قدرتمند نیوزلند رو متوقف کرد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78011" target="_blank">📅 06:33 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شوت سعید عزت الهی از ورزشگاه رفت بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78009" target="_blank">📅 06:23 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">حسین زاده جا طارمی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78008" target="_blank">📅 06:18 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">نعمتی چقد دلقکه
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78007" target="_blank">📅 06:12 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78006">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">نیوزلند تحت فشاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78006" target="_blank">📅 06:11 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">منو بگو که فکر می‌کردم ایرانیای آمریکا از ایرانیای ایران آیکیوشون بالاتره
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78005" target="_blank">📅 06:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78004">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">محبی گل مساوی رو زد
۲ ۲ مساوی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78004" target="_blank">📅 06:01 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">از توپ لو دادن محبی شروع شد
با ریدمان شجاع ادامه پیدا کرد
و با جاخالی بیرانوند تکمیل شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78003" target="_blank">📅 05:53 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">واایییی گل دوم نیوزلندددد
🤣
🤣
🤣
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78001" target="_blank">📅 05:52 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">علی علیپور اومد کارو دربیاره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78000" target="_blank">📅 05:51 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">چرا سکو ها خالی شد؟</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/77999" target="_blank">📅 05:45 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">آقا مهدی باشرف (
😂
) جای آریا یوسفی به بازی اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/77998" target="_blank">📅 05:43 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فوری از سخنگوی قرارگاه خانم الانبیا:
به زودی به تجاوز نیوزلند پاسخ میدهیم!!
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/77997" target="_blank">📅 05:34 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJh4e0IK213ARIe48lXlTcRctFEIKs7himprgOy9pC6QoIBC_4xHaEoTmU2CKaps6TzOTmn4CarQuzj20xeywbe3QKkhSZA-xRbNM1G5rkeuudUgAYNS0GQBYk6v8DVKn-hXlHpLnnpiS9gIoqKd4-voateZbYskM8ETb3BsrIQt0W0MQ8UlKx_ev2ryXFxrChfgKfoj0XJ0GYk6weErlj6YNsAKJKSZam0FNIsHplhlbrl3u-M03qkCMZYZuZ4Ujdr19U0ihPhW9mQuVK1WMs5luc5R-edAh1eeJRImSFKOOhXH2_VsJapjNGTpHyRT2BhpzsTzGwnWn-KBFUwiJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
امشب اولییین بازی ایران که  داخل ورزشگاه بردن پرچم شیر و خورشید هم آزاد اعلام شده ، اگر میخوای بدون سانسور بازی ایران دنبال کنی حتما این کانالو داشته باش که تمام بازیای جام جهانی کاملا بدون سانسور پوشش میده :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/77995" target="_blank">📅 05:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">نیمه اول یک یک به نفع ژنرال تموم شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77993" target="_blank">📅 05:26 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ریدم علی نعمتی زد ولی افساید شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/77991" target="_blank">📅 05:24 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">گل برای جمهوری اسلامی
رامین رضائیان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/77990" target="_blank">📅 05:06 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77989">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">ولی شوتای قدوس>>>
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/77989" target="_blank">📅 05:04 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">این چه کصخل بازی بود گلر نیوزلند دراورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/77988" target="_blank">📅 05:03 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استایل بیرانوند دقیق مثل‌ بهتاش پایتخت شده وقتی ک سندروم میمون گرفته بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77985" target="_blank">📅 04:54 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PkPPoXF5cJkyqGAwM3fZ5J_4Z4rQkt5C-xlK00B5jCN2714AgUO6VSAojjdnkkD1b-_TvysRfbHwuJVDMVa6qkw1Kh-2nY8_sTPrpWQJSPfCaZa4vUFYVKud4hiW9TU9qmDNVMFXEvGvSzNnxcme4Tu8jonIBwEHRNq9qM4S0ggwuuwaduJfesEJLpiiTA2DNXc0voOxofHyjDBjh0pdAqaylfI-T5x0k2464imdvMBVJTyGc-MhOsKz_wTr7q19mcEeiMMaUKkLV4eELt5u8O1EwvpceaO5nwBjuNn71Tq00XPPo9vPVRnDnjHLhBmMw55krBSG0rO_DTf5mWG6dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل خوردی ک جاکش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77984" target="_blank">📅 04:50 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">عجب سوپر گلی زد نیوزیلند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77983" target="_blank">📅 04:41 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بازی یک یک تموم شد
بهترین نتیجه برای نیوزلند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/77977" target="_blank">📅 00:29 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">محاصره دریایی رفع شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/77976" target="_blank">📅 00:20 · 26 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.  - تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید  @FunHipHop | Constantine</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/77972" target="_blank">📅 23:49 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWSX3cKrfhCGpglH1eaytUUH8xaihJnm8eTsku6Hp3Rac0q7E4cRR73JZm4mrguIL8V5g6hRGuiTxHYye_oNd_KsebQ88ebVMJ4Pxn0MOg5JAh19p1ovdGsJTLN2vKnEu4yXp6bGzrEqotS-lB6xtHw9g7Rsa77ktcsU61ef2sATaf6_Vp5s9UI19d70jNM8CBjWq37JNKMRlSUOyQBuc3nKScbpF7rzhFLMDSzdb5vfRv4qZAdxnHJm-iZKrnKUTL5F8y2DfP3U32NP_FtmT4muCewgxyAWvt02_dc2PMxKY_k5ytZZoD9UIUurLW9vyB12UQDKJHEwSm0Tje2e-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عباس و باقر فقط از زنده موندن آقا مجتبی خبر نداشتن و سورپرایز شدن
وگرنه همون روز اول جنگ رمضان توافق شده بود بینشون و توافقشونم ساعت ۹ونیم بعد از ۳۰ موشک به بیت رسمی شد.
- تغییر رژیم هم از نظر ترامپ همینه نه چیزی که تو ذهنتون ساختید
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/77971" target="_blank">📅 23:47 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cThNsvSIZwuiHaqEbbVtdS-kiqUn5jhirpdb-CCHZwHZhXFtsPT4eex7b-kVSJUDTpRKigFYZYxU-zUe-k_A573Np-xLLTY52s4V6tXUB5899-wLFd4rjLEcVAnxDgmFgrhkH9G4EUXpj95X3EeS5ueS-c5WObvtvMIz7bBZcAJ5D2Yt3eXAmYPLiJtc1iqXbYdr1RYctsShHlUnJPIzVRrTobj3oHExWCJM32o0bbvOk1HRHEVEHZ4XUDZcPO3i1mIgu_n-ToQmK6RZJ2tSvXJ_Ztqh9SkcGEfmAMlpCpWPaRVbwQjDoUFioE020NVz0_MK3NJEK48LjU-gcYTAzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایان یو واقعا کونیه پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/77969" target="_blank">📅 23:05 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1FCXSV3NEngUNusK_Ppq0_ksAVQM0c4KmejhJvtHiRgZ0ppDCmbn1b6ND5YweeECJ6joOfh5eodQwYev1DZCdcpVyrFif9fJ3RN9f9HmPvCTnQFm5_cdLW1tg7k050s8ltEwkt_gwQVti4QsRWa_0GcYq4Xe8QDXR1lKkW4__zY5ByvgMIUjEU18bcaTY7qL-dTjdQ1lerU5SWxPHl5eUvJq7gHdlutvU7YUea56aOi97qEOe-PSBHBwOJoeXEpbfEqBte2YxD324xB3CVHU7BEG-FiJXffx8tziKWnemYAQN9PIaRfnTlGYMgZWqzJefNh-EDsevygONo6cQDakA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیکای قشنگتو بفرست باهم گوش کنیم.
🎵
🤍
گپ پلی لیستمون
🌓
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT
https://t.me/ORGplaylisT</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77968" target="_blank">📅 22:56 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">امام عاشورا برا مصر گل زد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/77967" target="_blank">📅 22:52 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">زندگیتونو بزنید رو برد مساوی نیوزلند</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/77966" target="_blank">📅 22:00 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAmir</strong></div>
<div class="tg-text">اسپانیا بدون یامال در حد پرتغال با رونالدوعه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/77965" target="_blank">📅 21:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">کیپ ورد جلوی اسپانیا متوقف شد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77964" target="_blank">📅 21:40 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ریدن تو این بازی باعث میشه اسپانیا خیلی وحشی شه و بقیه رو بگاد و قهرمان شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/77963" target="_blank">📅 21:26 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfdIv3BKEqNUzeWyjVMNKEVbASEj5SrMKUJIbcsx6FuLpYOWfLAN4oeiElkP0-gtf6X_kVOm1IUiMQn2PttRtkah9HON2y-yz0hrsOCecQ1PVjrZtvmrXmTyqNKwmO93l7h_IP6d5BSkb5fRQnw1JGQwA8VaDrGLyDf9boLiBbMzV_GRwGlhuejGOCGEFQfsHbOxbjSJDQ6qwwuKJQT0zKnyb-eExpXBuTmJ2GviFuxtZ3PVnBS1VQje2qfTvfXy2LQDylHxiyhCuyHn28PvGvL25sSZclOFxA7Ws6mxTWra3Fu4czFaUoN6zRsT3sxdZEwv5jy2My-m8EMy2Er1Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیانیه جدید باقر شاه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/77961" target="_blank">📅 20:59 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77960" target="_blank">📅 20:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قهرمان جام جهانی ۲۰۲۶ خیلی ریدمان شروع کرده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/77959" target="_blank">📅 20:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">آپارات اسپرت با ای پی خارج ایران هم بالا میاد جدیدا، اگه خارج ایرانید استفاده کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/77958" target="_blank">📅 19:57 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">فردوسی پور هویسن رو آورده برنامش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77956" target="_blank">📅 18:25 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bEG0nCk3Od19K_RTguwVLMYeWCrxxB8stXcb4RG4uqdRqtOjTgtxKJufZp2mKRusJUX_U6CSHuQeDS3nttWwozFBWoJBMT_lhRZLTnYFlQ84IjFUT2N8Aq0a8sgTsEf6ckNCnD3WScoS934MTu0F53SDd7IcraSWkF2Rncoj9WxSRcmUcKaMR-Z-1UL8nBvD3fUZRwaGSibmmLj4ZlvWjsV34xwSz1NmadOmWY_5JmKrIjnFIjOSklsGA5ImGNDD8nSR--C_WG_gLjx_PVG0v_NKJ1oJTAgy-77JVjsgSabe78t604eagJ4tR7Itq2YQnffHyiD5dLxcVPa9iCFQQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vBciybZ06CQsGOOq_PkuK1GIBFL_R_d7jBRh8k64sW57LSlg5I6JKpeFmmQMxUYDU1ExMxRURTxbmtPgFY5mzLdndxkEvdccX8VjtskTtt1WV_VVr9x5QZklinZAPmItMH8OXIiP08F7OKSc8K0_zWvJ8ObkQTOzq5qg9aegmAzTlg1ur_FXujW7YjmTl38QZu8MV5F3GCItVg9RlVeWoTUNTSglJiW2K4NRBb5tuhR8MfjwoquN_86XbP4Hy2vjVSIHNNI4nl4LplKb8660gjm1KPN5WOJ7nL68iwofwSB1m1vcTkDPOkhVjFt7GLUgEZZ8fJiXgWMiBzEt8NlJGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">استوری شوهرش همزمان با استوری خودش رو میبینید، خداشاهده شوهرشو نبرده عروسی
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77954" target="_blank">📅 18:10 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FnkBNseC9xmJFIAT4Iep8LOjza2cdoJHB0NwKkZbzckLD3bxSHWcBCiQpFh4dUZDAH7Al8XBx8uc5uGqfA7eiaMiQLk7QHjRO23y4fGc8bpy_GCbLGAKYalcf09HsVdp7lYspnc-84chRHJChQxZOp56d68HJ8_4LMIw4sAZcF_vkjdxpHWflhK8-aEaDPLhCKo0gFui_iLvzRhdWr-7fkSdPSHSWT-L-VfyN2LuGBHy9Bf3-Sws0uF2XlpJHKEEVtatm796uSYFBSS84Hp6R8i1QREkEY83i79BST5pZpVoWg4A_KEelc4YiJ3l1jWwpwl1nFsZPOvThOq1AbpeYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/77953" target="_blank">📅 18:03 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77950">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djDaGcFqNgmi1Gibqhc2mrD9707kOxjBFr2BRpIkMITEGLxrqAEjb5DTfpB3xwWzg0XWWjfHUBpEWHNOEALmpg_PoNafw1CT0z0k0-9VAxrhO7dq9ZzpPd5-o_zniNxE3fuNj0DtSVo92PAI1WWvrDgMM7WRyvzXDk6XW0j6s_wW4nwyfx2SwGReSt_zSDPQiH-b3d0IKhwJAIP94TzDza5zAyJP8hoFSVNyjF2b4djfREtq7hIVkP2BKVQdFmcary97D_jLDHLzdwAJV5WDMxrsmmBAtIvJiMHlrlJYjWcxd-aYM_ze1Qdf1YVQLga8njzRz-ovlBxD9mh08BvESA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مونیکا بلوچی ۶۱ ساله
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/77950" target="_blank">📅 16:08 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77949">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KJDizDA1zgROKsBNxft72DQs8jwDLiuCgv61P-NUk9XQbXaDH33xCjCl-i6dWVHg1_Afv6HnHpxEeOeeMI3pvioJqbhaXrCXkSCagKE4FTG4EcUO6NqpexvMsa0jjUiso2O4VE0dRbgx5rzyWD_URxAp1Tb7sIr3K8kgTnMJnVpDVRicf_0ioLYFYLu1XgSxrOrBiHGCUO4F5EgE0dsc35T_m-g5_mpHWzVF-rQbSgVZPJKu2drwehvsPMhl14MJkgCBxoqnC7xgBn1c2I7Zctl0MaXt3aqLv8szV19LNg3GMfzG5yn9MuH5mJhrL4SBueQt55UGllGjKQ7BEvoL9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
😂
ببخشید دیشب کم خندیده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/77949" target="_blank">📅 15:51 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77948">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FLe-6PvIKBQMSq1SSJv_dl-W5zfmnOEff8v294VyiN5HeLIO0vioEUNNuXHVuulgKGQqDH9ecG_4-CZJ3qvUs9YhSQ6Ins367TkRwFHbfhjvRqz333Hg9MxNHNfGNgBg6kMc_grLW9hFoIFGeCUvgZBrgbSp5IKWEJyXFBs73vjT7D77vbcbN4ucAqtXAbRW7GucKRVJuCtD1L5St4QOtNdPw6kMUt9zsnSWrUTiO2WC0OKfl2goDGuo-sX0zYf4vR7aitXd5oUODD11D2vqQbZwqUtE6RkA1y_RdJhbRjN5pDVbKft9dDJb7v--mnzjeo5GtEKWXFdywaRPYds11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو وصلی؟ نه انگار کانکت نمیشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/77948" target="_blank">📅 13:54 · 25 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77947">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">در چه حالید دوستان؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/77947" target="_blank">📅 13:41 · 25 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
