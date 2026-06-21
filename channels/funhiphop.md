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
<img src="https://cdn4.telesco.pe/file/fxibIMi-HLzfU5Ye3DlVNumLiD5lXY5fiOBwkNADAy-Kx6hEcbs6KRn37RfYde4nxQ-a4LrhZ7GhaIWaKPnn50WXQlR-WrqqLUW71XrTr4HvAZqZ0f0ud4STxAy9bmt-qxI7DNeai8QClt5p3b-LhpaY-9_ZhWSFKNCw0AeUd3azo6lm02ialKLQsCIGFNc3L5z8FVgElTwbL4nCgr-03zz7zpj9RUIakuz-BS6iZcflH46fBMj4kd3Qg74ZLkCQRqecobXEeXakDgHceEQyGMI9m06KH505iOxSVXuFPhAlNrcxBkmk0PsEGPnnMiOvBXnWq9NIbRwfq9jKVHys2A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 06:21:08</div>
<hr>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCwqUfwAH-r-1mi5E087L997Ok_FxISNSIcHU7zyZFT7QsXNirfS1Glok1PqUwhd2QEpdrZVIBZ7r_cErGoC0hXcyDOFWhdSVQje7XGotmDEnqMHP8XV4UZoBTxvkHRGmTQlmT0gZa4qymZdvYw3sZizhl85KcATOLqa_Gj6B6ANRm6LTXRWDBRKx9sjffz1U6QFIByqp6V0WjoTh25avhwjC5uhuBkwdFC8UGyT90CB71lq4qbk3FCbAjj9pK0zT3wnNPCqSuI8CnBgw5V8_tPSs_Jc437RdyYfmTQ3eA0oiDIlPKG56AN0QduVY18sZmwgquQPteG5V0OjZphvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ldxf7nHsuSFilaw3CDNRYbLAK1Vnqq1T-8tkrH0Ce2AeS58K9HbaQrWTFiNTXLjnpFcOqUvTSmM9yyxZLUQd7abSn43AR0AX-3d1TJYQbZimyK2lVMyJ-YRdDme_0Mq7WU0FpLt_3WxiLEidmyijsgxpksYK1Xlu4yWI7nMvT2ix3Tl4MtQLxmC8F9b4o5fbTFHHfvGGZ2jNDfy-fI-7wWb85G5cTGKdJ98jnFbEYydxUC8VPy-JLQ6DUfEMo5GGDdGXDxNLbZnmPWXC9Fpz7-DKPvd4s4SZIGMyjXyWHJLbHpPm6juU5ZITgFloQze7wThF54TaAhzlvhOrGb4jKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.83K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_V6g0SbjHdmsUr2guy4EGzIbZPmb7MyzXctb1Hq8SqzMUufPAyWUlnsOdQndn3Scy4KHuI6axJj3a5dnJigHfgJeilgSDeUXfRR49bixfRegg4bEpk9-Mc4ElNK8zj20FREvVD1-MGH0ZjdA2JkYajizKtk6aQgpcG6yThq1BC_BF2YT7Jo1g3qWgHXWTTDujxMKJ9fq21l6Uv9lxjnBWMx3S2A6oLnZ-vawpgxlUht1SRvxNsA-YmWHRloXx5jJU3tyOig-dAIntQvtc7g7B5joXAPleie28ivOgJGvM8bWwGmKN1B7iqPzXjQtM4qCHCiCJ747CLWFnxtZ11a5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.72K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.58K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oSm5Z5qh12hZHO0YsWc4evG7Xt0nXMRbr4acPmCuXMca7BNFnCjim9g5V52TntYju2i0lJj7_iQGOberP2T0pG2HFUmAdx2VBKPHTEBjJ5713zpOesIF-8Hkpc3wQArPyfHhxUL9S-i_OuD6qeEi_VztFSvUJClSAqTKzBzps1L5Q2wMGp91qKg6PXgT800-yLN-SrIEuUCio1db5w1BM-7lmKfGxrC40pPJwjshNi_wjQUttOeaaQhwnsR1cVQvSRb4LsY__fpWz-kE14bLC3qHMfqbg14bDDvLQMtG6yvAz4ailND4efCTcWzIWHZKVI57x73NaTJ7HuDb2QjMQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.76K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 7.13K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.59K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78305">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">دوکو به دلیل عفونت تنفسی، رسما بازی مقابل ایران رو از دست داد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/funhiphop/78305" target="_blank">📅 00:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78304">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">المان خورد</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/funhiphop/78304" target="_blank">📅 23:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78303">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">هلند تو این تورنمت همه رو سوپرایز میکنه
یا با قهرمانی یا با حذف مدعی های اصلی
این پیام بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78303" target="_blank">📅 22:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78302">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">گل پنجم برای هلند
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78302" target="_blank">📅 22:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78301">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">سوئد یکی از گل هارو جبران کرد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78301" target="_blank">📅 21:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78300">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">حساب کنید ژاپن چقد سوپره که ازین هلند مساوی گرفت
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78300" target="_blank">📅 21:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78299">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الله اکبر گل چهارم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.98K · <a href="https://t.me/funhiphop/78299" target="_blank">📅 21:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78298">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گل سوم برای هلند
سوئد پاره شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/funhiphop/78298" target="_blank">📅 21:39 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78297">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلر هلند عالی بوده
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/funhiphop/78297" target="_blank">📅 21:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78296">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">سوئد زد ولی رد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/78296" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78295">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اسرائیل آتش بس لبنانو که پذیرفت الان شروع کرده غزه رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78295" target="_blank">📅 20:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78294">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">هلند گل دوم هم میزنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.84K · <a href="https://t.me/funhiphop/78294" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78293">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هلند گل اول رو زد به سوئد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78293" target="_blank">📅 20:36 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78292">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGfWcI2yeYLYaHftHZpswNfTgjVDwBz5wEhRtlCqMwkW2HSOIsxcD05qcVWCOngkeY40Qd_Hvy8818UZ3pLPaX2u39x6Ro1oJO2xfEYVYkQCAIev8nOyFAXFtCVro_u4U-lb4--8bUi-j_6TSalJ794W5-v9bgKZdOqQF6FsVR6qB7rcnBdEyTCjqiEAzAfb_t1NZ_SCEmMejs1Av8sP7Ehqc9NKsHyIhyXLOkm2O7pwhkY8lkx3QFd0ouyQh-s05IOvZ_wGdmzO2f0NfTkRtbilSYmCSsdvq81M_Ol0hABjnV6Si5RmFs66TEBkqUf5Op3gN6SVqaKBtn3VjmY70w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیه هم با باخت امروز صبح از جام جهانی حذف شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78292" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78290">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RaVbpnZaYNYsLA2xaVnsRO6PNbrs2H0SoD-DJZKtsNnFkc9wILGvbOcWgV4WJgATdRNU7e5_Mp3I-As-ZhxFg7aJV-PG-UfzDojqGSzC2Knwo5F2lYJkC55rSlkY-k0ZYmPMe73JnwxhArplbPfy2WoO_Qh_5cmScb3zt-hYSGhLFiBgIELYXUKFKdYYFh353kVO8igZPeiaQ_bdmCl9XxwRUSBUsCZ22hbb8ROag6LneFdXWHzn5wZXEfzCq0rvozkh6cMqkKLcWI458nd-dZiyBIKxCAqi1EWrmwRNQWeP5nP_U-K8Wa_7tdX07QnuYaDuk6HZSg5CAjEaD6Qg4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mPKoXYIvgDu9o12hiUUqIRifih2OBVk4xWfBxLlatfNJsvMLXhE2JFAxi8DL34HszcyiokQuj4K6WlWVOkSyhlkH75845SKcslm0AHscXiY-Nk4yI2o1ZNg9yDp-7gVrmPrqGXDwfXr83dvVHsijYPKvNoCC4izCGqWZ03IvlVLZ84qKXqIKvtqyYEnlojO6cOUvqw1QuEzFQW4BNMUtERN-YdFzyQkZt8_FTXTOllwnGh3eCLhZUO7ShqnCbIuGEX75PBCkA3348zznqqTEvIvhMBUPvL1aenAV3lUbNMZwzpkqb-cIs180BzYErXo_2Xzpot1NY0o0SIoZ02FsyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترکیب دو تیم
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/funhiphop/78290" target="_blank">📅 19:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78289">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a-IOZVb7vnE9zYidljHQz7aAaHcmACrTMUESnHYnXvqnZJ65ixxWAYMd6INSUnXaAHs3OvLkjX42976iRcFlX8KMuI4KUXgX_pQQ5PCwwY269os3UPBjaoxgiWs-482E-AVzpkMzCfsxxBW8-tdIYbJIW49e8HJJxB5YmnVqYFyfzZ8Gymq0ZMC1BPKsfF0_u5kwFIqtqL1YMGLc0Gvn4A5fTB6crMmEf6mL9wqFi-uBc3xrpPYrVO7Ry2YQyuLuTYKHBHzCWa3RkN95fgLs88WIh4dWF0zOwsITMP8j_gZzWYc99kZdUiZsFZe1eKwhQlM6dSrWIZai6Wnb-APkDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78289" target="_blank">📅 18:27 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78288">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AcHnPy64UYPiM_rS5gBvMEF2AZfvCsfpjXUyv9cHBx1fn2y6POovFi3t8KWE727VJnNz_TwOQCwHN08V4K12xApHogZh_fQDAYzHU885eqLwi5GlYyPpzI__xkHt_MJN5PxqKQhwxcGVIpeLurkMUGJMFpx9SxPUYz4o2A2UwnVOgGnySn1aC7UX4-AS6JkIALI8tEUZlHaUCTj-PJ9koJbh9yQ0G91yn-3gcAz26VpholBP6T3M7Zrtn3xV5O3VODzGrZQhxLrrYLJw4Mmsm8fukNfBWqKu_p3KN0s68eSYyw0Cmt9Fsfwl4nEXBkQC14ONq4zz-UaCMjCik-L32g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداشاهده بمب خنده، فرانکی دیونگ و تیمبر تو تمرینات هلند شاخ به شاخ خوردن بهم و الان تیمبر مشکوک به ضربه مغزیه و دیونگ هم احتمالا بازی بعدی غایب باشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78288" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78287">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
همین الان وارد شو و علاوه بر
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه اولین واریز با معرفی هرکدوم از دوستات به وینرو تا
🤩
🤩
🤩
🤩
دلار درآمد کسب کن
💰
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/78287" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78286">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OCURw633-WlvQx9xOc31kHHY_EvPjsjFNSPRcgCHUu9Vm-XwRQ4mVtGubITDcvfGQnvMVB69HPnaFWztPgwWpVQl_OLCBE34CISifKEZoY6qmH1gX5U8ZdeoUjifcszFePLA4LJKx7gmp3fmfqhmkpzmO2wUCYJILbX4pp0o5IylboAQdCqw7-NnVQ18jw1D0HIb0pPYFuRpYmFIxjF8GaLwrzbeNSazPT1njdR_RIxPEsgideHIt79gb8RzQW7TEjQz7axdRUilIYz9VpanE2p_rd7npuKOgss99ZG9wJXmZfIhqlIVWeBIZM6VXomudITwy1wV_HC4tPrz6kapug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
💵
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت آنی میتونی برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
🎯
G30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/78286" target="_blank">📅 18:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78285">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q8k3B03QqqFtgIuReTj6heX9bsKzpyWkqjTZLZuJXD-P0lJTti7fzkB0jjwv_27I0q3K5mcu8PeTcK-acs1uAOHbDNA8vgIoZHkK39RGtCbcHftH-sKOaQFJDv6Q7njPXhZojxdQd2K49ncXqsM3xbCywHNtRf0oOW_8JKZSyMHsHVI9gSKRILWbUwns5LmUOBtWbeTn0A2jUZTylJ5X40cW11A4Vjf6HjV7FYwpFTlRGVavcgOCDndgW-NH0GjF_pB2aFIgiDM6BWLjE0fAM1a8kp2KyZwzf1E3Cax1jiQjmVwuQey97Q56ubm5dnR3FDQbYsFeDlWTuHE3aOEIYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه نتونن تیم ژنرال رو متوقف کنن حریف احتمالی تو دور بعدی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/78285" target="_blank">📅 17:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78284">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tLKglPph_Frox4bUTgYoK2VPwXwOM_AQ4gVLoQ_pbKqo2HnvacDw_y1TEcNl5qmPO0TcaPc3mZWP28b6BEjJjh2EQ8ytbxR_-56VSk1N1rVLMG3itwmdlsEy3ywATlLnd8fdflYpT3c-aYpEzsY5hdp7XNkTjgZpejmI7pR0Q1G3Pq2UNQ-0fp_FBCEivSiaugNa1xlGMTyMztyyyNiv82Kx9sDLzr84Yj2guz3RfAaSNxVVhm03_CQdYcrQ-QETieFPBTYujjIkRkoMfLvlua84nawC8wqzzruD0abI9Hdv1jUD3CGYcK-MhvrX7b1ZEBmJOEh9ODk9_6PibTzudQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت فعلی تیم های سوم جام جهانی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78284" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78283">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/78283" target="_blank">📅 17:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78282">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCnLzzTDZeA4SR-iSOdBpd4WJAobwueJCUnqc_4SKxVtqUYZNFjqWPzgOsuhC106Ke-YPu5t1wbXevgg-6XuxnWJXv4ewbkg3qnqo2iBgbcjbvSJ3TT7hPqVYxXDyVJ_QD9DtNg_9gLVxRINWDk_kT20FrQydpDbKmzFPG5HmmISYqJ5BwZYt2Pi0ixZ8eZhn5E2Q598AZ0b3MDRpV_dvh7MKvSe1weMSKHPmsv0THugmootxKCQ2Ua_YDdYdhR3P9ansNWFizCKyze3DahLdSlv0TZOcaUWCrsA_lmINWKxFgC4owXPItrUPnSVfSDN70q13Z3Tn0i8bVrwSQDIww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاظم بالاخره افتخار همبازی شدن با بهترین بازیکن تاریخ نصیبش شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78282" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78281">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی وزارت کشور: کسایی که به مراسم تشییع پیکر خامنه‌ای بیان، به صورت رایگان تحت پوشش بیمه قرار میگیرن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78281" target="_blank">📅 16:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78280">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78280" target="_blank">📅 16:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78279">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سپاه حوصلش سر رفت باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78279" target="_blank">📅 16:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78278">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">دولت عراق مجوز استفاده از استارلینک و صادر کرد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78278" target="_blank">📅 15:06 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78277">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mz0TDJzyb_-E4Z0qvO4ssHhL4wQDQDGzTwaEPxceWhUIkdDlLvMmR7R5m7lVN3NouOrFEzv1vqeM34CWryVC0D3TrreEaptKW9SszzdLtckifA3B4s5fjdgO0mTkZlO1DyQ7r6xJv-DHFFlby8VjF_ghJokfOyGsofCNVk5s76arOpOrTc6Sq_Oj2R8dX2uQaMXUo5VFGayh-nZcKn_KPOLrz_zIrmGKWYRjD0NltX6TviGefG1r7PDLraVK3I6p-ycTrtPUOygZNPF0nPhjVynKtFBssKlKA4NAQQdHhm-u8XGvLFURGFDn_k7gGkLAw-V39nclRcsQI49kWVR7Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدینیو و طرفدار گمنامش
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78277" target="_blank">📅 14:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78276">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uv4Winwp-ZaoEYeksvnvXzA4RI3td2isisSVMEwmeybBZxl5Dm2vSwb5CFWBPdh0d0JHZvgKDW4x4ow5N1_f51uc_IcIqhdkqXQJjmZE4H_MZkVcRp7lgMOQrnjUdpPjPzg56YnDelH6aKrvmrPfrraIRY8Pd3_Ng-lHYHbJmFnCSmRGYYwKnmrmQFPop3D7qnY3LgP2PqRmkBI4MsoC0CEYwkCVcEM9oYjP6hfIGKl3n7u_5uHmFx2dVwcMEEVBqFjkjK0DewPqyuZhRoIngirB7lpja450rwdOE04fDL_-KkdYv3qytTAKGYRlSkN_RH3XkfxFuXa10GctWM0eFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باهوشا جواب بدید
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78276" target="_blank">📅 14:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78275">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">تو جنوب لبنان داره نسل کشی و زمین سوخته سازی انجام میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78275" target="_blank">📅 13:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78274">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qCU6jcIe_RKS-sFbuU5_na96YrhkagzUM25cGPVzLIdZ1sLe0-7_VCBk6x6A0uX84-HIvLTaG5Tv6xqAdla1xGUu412AFC78YUmjnh7tNCl4_iInr2yzdnrbzd3O7IntN41ubL97hNSk_vn0OxUHk2qJiZ6tD0C0L9Wz0jMtM0Wea0EwOBI4eGIYYejmcI3MbgUfuFxKZaQPP4MpOBAsB8nB9MQdWyqW4FQzWcz1OQ0Moq7UziNEfZUjEPJD_2NCADluWcLOvdqEYMh-kyMWdK7qiKy-rFJv-vqZXNrLSXGVq-cdyj_Yywj39xMlE2LWeZPI2SXDL99WFByz1ESL2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">میخواید اعتراض هم بکنید لااقل یه متنی بنویسید که با عقل جور در بیاد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78274" target="_blank">📅 12:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78273">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cG0ELinN3iHZAQWMgiimDnQVrJT9Q7211M8X2UC5zltvBIHtJH-A9DUg5gQ80mhmECMcXaeEps9j__yt5jwCw7dKUBUZ1-RMBS9GnYiaMcY70yaWTIPPKsC9zGPpBP_PTu0KrbdrqFsH8sJXAx7jevkF73wS8IVUSWwO0dvEHxOrKngNDFcrBcQGMMWyrrhRbWn7tp8ks5ViyS1Vjk6xi23uIqhOmMQT6N-d6uRjgP2YDn0nNmIcquWkUqket1L1f8rZzku20lwcmx7JDKamgHcyUywAaYZfTHACGS0jaNjSO5uhAaM5x3TSf_ciCe7PMPK8h8rFBCvOs7qajdSqbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تیک‌تاکی ها هم کم کم دارن آدم میشن
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78273" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78272">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کاربران جدید،
0️⃣
0️⃣
2️⃣
🔤
شارژ اضافه برای اولین واریز
💳
وارد سایت شو و هدیتو دریافت کن و با خیال راحت پیش بینی کن
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78272" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78271">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeoLMLU0TFZndwE41ud0QvJJpkLkrAD-QfovIXui9VRnY_jBZOcBHK1I3eYRnwewtSxU_yR4jw3sGBzO6yk9uckSwVqvfdG1B2BJpN_5BpaQomPrXrSISmgJJ1Nws7wULRToDH_6WjuTQr3QN5nYmaU1ZMWHDlY4MFWl1IGXBBmns8eXlCyZ_NXNc1fs6Keanj0VQZOz8eeYPx8AMlyD6hvt5csxfB-AKM8dQbaEYfeA-4DHA9PGtahAXkLF8So6w8GDfqK6LlBru04RZjqz5HwZY4hbA4V0Z1MzunZU2HbmShCFy1_tHyPfWJF65NQw2Agzwl46Un6e6ILvBbZ0qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه‌ی ویژه برای کابران جدید
🎁
اولین واریزتو انجام بده و
0️⃣
0️⃣
2️⃣
🔣
بونوس اضافه بگیر
💰
⚡️
فرصت تکرارنشدنی به مناسبت افتتاحیه
⚡️
🔴
تا سقف ۳ میلیون تومان
🔴
⌛
فقط برای مدت محدود
💣
بالاترین بونوس‌ها فقط در سایت وینرو
🗣️
امکانات ویژه‌ی وینرو
R30
🅰
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
🎰
همین الان وارد شو و با اولین شارژ تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگیر
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
📱
کانال اخبار و هدایــا
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78271" target="_blank">📅 12:23 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78269">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نمیدونم چرا بازیکنا برزیل نزدیک ۳۰ که میشن با هر بدنی تبدیل به شیشه میشن، من دوسال پیش اون بدن رافینیا رو میدیدم میگفتم این اصلا مصدوم نمیشه، حالا ماهی یبار مصدومه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78269" target="_blank">📅 11:55 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78268">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الان وضعیت جوری شده فنای مسی دارن از پرتغال تعریف میکنن فنای رونالدو از آرژانتین
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78268" target="_blank">📅 00:59 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78267">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78267" target="_blank">📅 23:51 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78266">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">گل دوم برای آمریکا
پوچتینو تیم خوبی ساخته
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78266" target="_blank">📅 23:15 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78265">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">ترامپ دوباره مصاحبه کسشر کرده که به خاطر اعصاب ممبر های عزیز ترجیح میدم پوشش ندم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78265" target="_blank">📅 23:11 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78264">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کشور جنایتکار آمریکا گل اول رو زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78264" target="_blank">📅 22:41 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78263">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">بازی استرالیا و رقیبش هم داره شروع میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78263" target="_blank">📅 22:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78262">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lby-LG9HbWKqIB5wpCESYv8MqsPGvqmyBhjJ_YVKiZ8rB9Y-dyeqZDQN8AyOtRxgsdTM41P1q5VvoG8RS4oz7SimBokPuthpNTkql8JXraB-oq2l22zpLkPWLoZX2cFlgt6LXWJHe-h_NribiNR6NLnJu4ZaFjdRQszbANv3ti-HUtwZsEtA3axX3yff-5wI6JPpr2ByvJviF3f251S3LvXLR5wBy7S6jLuJAl9AZszEaGW58arEkFeqO2ad7Cr3FjUM79j4hY8_IuXVe6SdvAi1WgXup-UU2ILuWTvZEi97sxTo85BwIiWVvIFlWDITlcr5Wo-QBxzKDbFMQtOExA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین رونالدوی موجود در جام جهانی 2026
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78262" target="_blank">📅 20:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78261">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXYsuHe5EYrCKJD1awVAfmpqJbIqWm3iPzgxDDkul83s0zZbGkaYNSkib_8Iu33-_9liaxqrz2bBcjCR24pDuXsYkaDrsSl42BuCzZV81XIhVk_bSFDAtWzXyJyS-has3ZGJxkl0Al_DS3iEWDZDIqJgAy0BVQp04edrUqBmceGHjutpPV8M42c53XxWnYbFiVLyfWNMokrxftP1-CGAULI3Lyv7xWpdzcTlHoU4VRGkKNL5-ROT3DiTqpdy2w6ORfVGfpqF_clnKhZyMB0Irdy1Nu_YbWj24J2KWVFTyYZX7Mr_dXNY5e0ILyEpfXK13NIFCF07zYNigEJjXtz58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باید کون میداد تا بهش 10 بدید؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78261" target="_blank">📅 20:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78260">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">فنای رونالدو به پیج کل بازیکنا تیم ملی پرتغال حمله کردن دارن فحش میدن
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78260" target="_blank">📅 20:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78259">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ta6XMyS_Fdb-BIR0rA52hrrD4_yipuovdopnoAiarn_yEkhz0tpINPw94gaU0d1uK4NLv0RZboZPae_biGjrliaBBLrKTEX-n0TVo50HoTaZQdV62_yaFrb3j_MQBWj1sjDpvZ882IltDAMUpMw800uLMnaA5QUevGMtWzwQ07mps4frlE0W5J5WJioU6PyPs3U83G0NoVhh5XG1LExNeq2v-oIQPgQNfOzDfEk0cUcqzRLmFKuMZI-ulON35n-4OWAgfiiRs8ZR6bnqtxKlWejrkWHZMoLKYMvR5rJf6vfWf9h3XBOoMKe1kYGBZCtNqbgGb2c3Dwe8G4iZ1CLSqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید شایع به نام بلاتکلیفی منتشر شد.
Download
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78259" target="_blank">📅 19:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78258">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">شایع ترک داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78258" target="_blank">📅 19:01 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78256">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UnTxKl5_gk579r9u--twGapi-3W2NxU-U13OAjsj622klyqpYOu23nqEtXDs9wEjNOH1HNOQ8hWrN8AJFyVqZxD_ahyxSpWqyQXgSntS7xc6pLRvw27eEswQkUCrGBRLDq6sgWuU8bVUi2QcoeXTaA3uZ5CcFiRWFDu8_hvFwmPGcSWZQSDcqbTeEOXFSrWPkxYSJhxeQsXCFHtMaj08Ecw3w1Aq4QnwTzm8ncegIT8bgL-dAVTOww_3MaF9PqmxsfVz_Z3czZYC112vbrMxroaOBB-LonjiEc1p5mEwtVykmtzQdszY25dnc0aJjQ-8e4tB6sg7vgdH66Mt5KL2YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حنیف عمران‌زاده: یه شب تو باغ با برادر خانمم مست کردیم تصمیم گرفتم از فوتبال خداحافظی کنم، به خانومم گفتم یه پیام تو پیجم منتشر کنه که من خداحافظی کردم از فوتبال، فردا صبح بیدار شدم از تصمیمی که گرفتم پشیمون شدم ولی رفتم تو گوشی یهو دیدم همه واسم پیام گذاشتن داداش تو ادامه مسیر زندگیت موفق باشی، منم دیگه مجبور شدم از فوتبال خداحافظی کنم با اینکه دلم نمیخواست این کار رو کنم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78256" target="_blank">📅 18:43 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78255">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tUr34l2IZH303coInkn46pcIlXThyCezxOfjo7rWGr3Z1sWINXoiPilSNB4joJMH_TSBCBYza17qKOb3TBPAlGrs_Y1vs64AjK0BWaNx1aREOcNjRRo6cs2lM0lNjQa_WQkGx4P592-5kGx81-D1L42d55_y4aQ1MclLPaHWSw2__Ziec9saEVAoU785x9EX8WsWhDYXM5GyVwKTHnXToa3SCyvLO2dXUaGaaeKo5JCY_DopvrcmRbey5lnJC7YeWsKo16o0K881ly769GnyWC9x9lf-aN3YLPcZ56tWsqvYC6RGROycm-pJz49OeQeXCN6MINfk4qNEjm8pvuiq5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78255" target="_blank">📅 17:57 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78254">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NPFnH5RUoZIh28s3B9BZg8Bc-Uk5K8Itn0OCAGdN2IiahUSkPB4PmI5dC7KJgktIkcFibH8_NJNVnHNsqGsssiKopjcKaEnCDKUjz1RWd_lgsdzsEzN6Hl7gSTXgEd-UhiSKcDWLXtyl37E6oYcU7qjyV2ouDSyPpTm0J9N_Fe7ktFcZeDjVsi6tkadWVVkvsFHi7T721kd675WSdg-shMx9aH4e8HCKyqOesq7clv1YLAUY_-N69cj8ADoHMANk9f_1K4KudSPfjTMEwML37hJ1-Ni32MPqWxvVc8y_CaIpiB-x5S08G9Yq7RPK0_5vsHXkrtN6_Uf8YM9F5bQOqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من مردم.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78254" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78253">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">جام جهانی ۲۰۲۶ با بری بت شیرینه
🔥</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78253" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78252">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🎁
🌳
جام جهانی با سوپرایزهای بری بت
🌳
🎁
⭐️
تورنمنت 1،000،000،000 تومانی
⭐️
✨
شارژ اضافه
0️⃣
1️⃣
🔣
برای واریز کریپتویی
💰
🏆
5️⃣
🔣
کش بک روزانه ورزشی
🏆
📱
همین حالا در بری بت ثبت نام کنید تا بهترین‌ها را تجربه کنید
✅
G29
🅰
🔴
ورود به سایت
👇
🔴
https://gfyweuuchsa.shop/fa/affiliates/?btag=914641_l303106
☑️
کانال رسمی ما در تلگرام
👇
☑️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78252" target="_blank">📅 17:56 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78251">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEhbyykTMc4Iz-YRj0JNL-wSfBxkVpbYTfGkCtddjae-4eTf-XUfeIoDGpjk6KOKpkTBWqUqc6hwzel7VnkRj5HUrk4CqHFfEbBkn7WgcXj3vva3KvuS6ODq9uMC3eiLVVOXK4y-UFuD3myvn8gn-hfN9l9GZW4U_-HhA8zyiA8FR_X7YzH2TNZuXHTGjRpGLZ4rDI6RuPTlZImGVcFrw3yv9iExEGVHJZkmu9KmJDfWLycjxV9r9cPW7J5b1_B7Q4x12Wu9AXmTUe-82JWD0UPn4OTI0xkTOUcqGpilaVCSHmAZrEbYQzG6Vf7wLgNPoCC6tvAleomZntG8sRCP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژوتا یالا از قبر بیا بیرون پاس بده دیگه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78251" target="_blank">📅 17:21 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78250">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DtXU5uBQsvWa9mu0StsKDTh6PVQTA_gU4QIXL11FD2vlzOnk5IqaPFKrQ1MytxeXdqftma04yEniG3Wc9uWBIuxT-w7UtxRL5OmvxaRnvjZaeaJZA3xK_tcT_AN2pLiiF_N47cGwgnK_f_3-Y7vyXlEvsBRy-mwJvt-_ApZSV_-9gQwavIImtT7YVxWUBQN8HL4xtK6pwdiAMjlbKTPYHjzw1CTkbDGgekHD7ZSglE_V_ptfC7ez_KMrt3kjnkxnOnJv72655XTO7Y-YaNwpofWpxQKt445_tOI_JQMvJocjNIY4iv2qYGVMU0H1ieaykbos5Jbk6mII8CONOFTRoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مکزیک به عنوان اولین تیم به دور ۱/۱۶ صعود کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78250" target="_blank">📅 17:12 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78248">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LHfJrGZ1mIBKcUN_SiAWt0O2bQ384J61QUht8XU8iLMRjAAL2l-aX58PBjBW_eXbb7SMKGGLg9D761AQheXIIo1b4WpFx5G-dimhDQBw4IG-yM0xt7KEW0sBBXI3nyDOga6jnkJ1GVpt78WDsP-ZmzElne6b1mcI96l84j5qSzvEgdQLCKLYUJUj_BMG3Nu_L7lc9PSwUbqJ8wgRG9f86Lcs_EzMNMueCVS2W4KvH6MKusgRJKKvl7JlMN_z9KNI8t1tGUWLvAdYcvfulA-8aDZBfM5swM5zpt7rD36GI-hmNtLIcHo9PLptgUZic-RzcKIQJQU32FxF8427a0U-Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در واکنش به لغو دیدار فردا و کنسل شدن مذاکرات:
«ما از روی استیصال به دنبال دیدار نبودیم؛ این ایران بود که چنین درخواستی داشت. آن‌ها تمام شده‌اند!
ما همان مهلت ۶۰ روزه را تا آخر اجرا می‌کنیم.
هیچ پولی هم دریافت نمی‌کنند؛ حتی یک سنت!»
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78248" target="_blank">📅 16:16 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78247">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bc3p924gf3wO9K1RRzanZJlFiVNZKprjRFQFBKNOITCCmV6CCcviTzt2jhu4vpIVcIWVMB1El4kq0ypc7DhLd4yrkRbjSwcie8W2ad8sNE3v7jmR-mF3LH8sy5UsQ4rWFVxe4azfYe9vyDZLLBqy1rGbl_GBW42kzCQpc3MI1pdQavPyDaBTDguVYGuC_8dYluP9ZpCbfQprIzYZ7b3x_PMeLiSCiNvdY1oDEk65YK4dS44xzqAtVXkkttN0E8eRrKnkyv6EyIoMsjAauUTukzDKFf5DMd1sZX0H3fS-zFyco0AL4MG92sTJ1CzprLAJm7Bn7fcobvefHS5u-iECdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید بهزاد لیتو به نام "Late night drive" منتشر شد
SoundCloud
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78247" target="_blank">📅 15:20 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78246">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نتانیاهو: دستور داده ام، جنگ در لبنان با تمام قدرت ادامه یابد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78246" target="_blank">📅 15:10 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78245">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">اسپویل از چند ساعت آینده:
ترامپ میاد خایه مالی میکنه و میگه اسرائیل باید حملاتش به لبنان رو متوقف کنه وگرنه باهاشون برخورد میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78245" target="_blank">📅 14:46 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78244">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">سپاه باز تنگه هرمزو بست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78244" target="_blank">📅 14:32 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78243">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">معاون راهبردی پزشکیان: تجمعات شبانه باید جمع شود. آنها سلامت روانی جامعه را بر هم می‌زنند.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78243" target="_blank">📅 13:05 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78242">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">مادر اشکان لئو رو گاییدن الان تو کماس
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78242" target="_blank">📅 12:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78241">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMFiI029IprZNnnUdwNS6IicKMIDW0D_wKzsnuaqkBeuKw_HKBCms83nfmO2fz6f1snlMcsdcaL9Y6go8u0_YxQ0OKl8FQYp45CWhK1IqkcJSqZBLYwlSZIa_6BxtMO64ye-zhhOniZFHJwg5UvRDoheUQQIz-nFF19Jyl_uWwPS3ZcgVV5qFpAqLYQbYljRh3TDMctBjq5hFF0n6HgXhu3BxWGDSDx8C1ktzFwfxxKf0OPMcs3oVOleY9K50yIPGC6PQAnW1C566-ENTh1J-R25JbDE1sLXrRiO7qP-eZrmrI1rvYcFt4Emmt03HorZC3LmZFxiI_mqHJIqp9EuaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهم ترین دغدغه این روزام اینه که بدونم این یارو پایین تنه چی میپوشه میاد جلو دوربین
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78241" target="_blank">📅 12:30 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78240">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">جنوب لبنان چرا منهدم نمیشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78240" target="_blank">📅 11:50 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78239">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJxPFeotfsHSm_FZLW4mF4twO_NqsWOWDxvp_ac6U9CjM6rUlBRcpwJqwprNS4c4bMMSQItOgPCN2DDOteFNkWJBw1mH03wfcqZvA_ssYa8U_5iKOpL_rIKEuiL8ubn3J1-cwcxrquANS1OVhbRofrchBIWuEKPz0ZWZ08duihRUY1oxswbld19Ur9E61VpgQFFowoyXQ43rpy_rHeaNZgVT3l1qQ5kfbHKwZNx6AD9h6wktnphMziwD_etriX_oTtvXbaMutZRCvf4_ToM_skAR3P5KRwplvetJq5fKi23dxhUxVH1FUI1lCb-GOi2V77n8M7d9An3SIZP0FAaY3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قبلنا که ترک پوریو میذاشتم آرشیو تو کمتر از ۲۴ ساعت بالای ۲۰۰۰ تا فوروارد میشد، امارش تقریبا یک سوم شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78239" target="_blank">📅 11:40 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78238">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/beVX0vgAoOlR9eiOmVmLEGJA7f_WckaJXm9d8nb8wF8fCLDv0_OrQXctmlUq9YLzm2GNmfQ5zTODmPqo2y_TO9S2FCBdWU6DobldXJZ4Cu2RaLS8uUfsOKvLiEEVQbBJUq5f6ng9YFaJUjWXKKSXqQU3XyPI4Bj3Nm71vezRyffkd-HvaD11vsWKiL6JpxDLZoMl32HfpwUabaPntCmJ49P9Bf2i1rqYmQz2cRTuFRqdul63FLJS2LiobfVOFxJckpkaf_rDEsUVhGsE5iQjhNDWRZAInvUsSziL9lXHXdG2-2IrDRyTkOIIjaNG-_ClZZl0RASy68qmcihIq0dVlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای مادرجنده
💔
آقای مادرجنده چقد فید شدی آقای مادرجنده
💔
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78238" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78237">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78237" class="tg-doc-link" target="_blank">دانلود</a>
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
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78237" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78236">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rU-Tq9GeZf_4WaGqqZuXg69Gn6wITn8zhvHYa5Ki0ee3g6pU23mFti_7RPJGPQhsm4VpwfPs_EZm-SMVOc2RSMaBmoCPe3vs4tsV2MCVRUWsDJo0VQyRbxA1BtcrsEpHg3h35L-xNCneNvjUk9YBUD2WoMw4YrAxCMP6tsV0U6eo-KAh7vmHO9_GCWGc6qTDYZdlMnYptUndbR-b0KuPpM1lR9UaLrHZ-2i0EygRIV1flYrvAsXLe0fPbH1gEDMKTnCyC6oeesyuMuExAuA_I81w3e6_C9UofdOjKYX-8p5xSJUZ94mT6s47YCSkPMrcISTvcGCwoSv5LxHn-Wt21w.jpg" alt="photo" loading="lazy"/></div>
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
دربی‌بت؛ بازی کن، ببر، لذت ببر!r29
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78236" target="_blank">📅 11:37 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78235">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سوییس کنسل شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78235" target="_blank">📅 11:28 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78234">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ولی سکانس به درک واصل شدن حرمله >>>>
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78234" target="_blank">📅 02:09 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78233">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">دوستان کسی از ساعت دقیق پخش مختارنامه خبر داره؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78233" target="_blank">📅 02:03 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78230">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/78230" target="_blank">📅 00:45 · 29 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78229">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">اون سازمان دریانوردی که اسمش یادم نیس: تنگه هرمز گشاد شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78229" target="_blank">📅 23:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78228">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تروخدا وضعیتو المیادین: هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78228" target="_blank">📅 23:57 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78227">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تروخدا وضعیتو
المیادین:
هیئت ایرانی به دلیل ادامه حملات اسرائیل در جنوب لبنان، سفر خود به سوئیس برای مذاکرات را به تعویق انداخت.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78227" target="_blank">📅 23:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78226">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شجاع خلیلزاده به عنوان مادرکسه ترین موجود هفته اول جام جهانی انتخاب شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78226" target="_blank">📅 23:29 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78225">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RLXzyyOYOTfWVeSWipZQB1CbC6xNxu8FBhwevgMSkfP2AoRXyv3WkD1b_CFlQxhAdZAsE9BdTEq04GB0q3d1EzsY0jIk8V4dIMyZhi7AWtq3o1aQH09iTArDwxq7pvXOSDWO9N_feQgqeXvg0UkIczrEUmuD-Q8dIwnMcrMPZZ9nOrb-OSzPlUiA-TtDzOL02kt8cklV_d4JDb76Hw13J21z-YwbEgHYHSIZdQzNikq3alK2R-c3cKhXRfCLUUbIj57Rd05Xu8zKl4-G71BeSewVW8XKx948-yzlSZxeZUv0zumtfv-59FrgZr7rVmeTV2X-xO-7prgdJfKXv_Om_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستاگرام چه داره پیشرفت میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78225" target="_blank">📅 23:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78224">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78224" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78223">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromWeera news | ویرا نیوز</strong></div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78223" target="_blank">📅 23:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78222">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5U7TFchoF3Djssw9YDU6YXK4EHhxbaIbJIf-oOMHHVldKs5ktdpByCkeX-sO0G6ETJID3Wd1S-u6UJUTxi_kfKtBFti_aIx8pFjRTrh6R1r9ohBxpBAiQZh2M2YwcBpqhKg--uSGh5fnMZJy95mPe7AlFPohkTyIAhLIUcbyPeEfVc6rhGTsp5Iy2D0NuVtWgiHPiCFla3u4Nai1xBW03_Nh0gB8lgV6IolFMJehWfZWZCE6Gdyweo-k4BlQ534AiSZuWkZF1ILp2uUT5W95kHBm3PV-4Fb-_J4vDWdb8JKRIO6oQ7Y0dZLZ0xPZ-q4dQgpxtq0BfJCASAK7En5Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون ۱۰ نسل قبل یارو نسل کشی کردن یعنی این دختره خوشگل نیست؟ خار منطق
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78222" target="_blank">📅 22:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78221">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">خب حل شد</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78221" target="_blank">📅 21:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78220">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شما جنبه افغانستان ندارید، بزار یچی دیگه بزارم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78220" target="_blank">📅 21:46 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78219">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">پوری کیرم دهنت کاش خایمال نبودی</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78219" target="_blank">📅 21:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78218">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تنها کسی که میتونه برینه وسط مذاکرات تندرو های داخلی ایرانن، تحلیلای مرادویسی من‌باب نتانیاهو همه کاره اس رو جدی نگیرید، نتانیاهو خیلی وقته قدرتش تو لابی کردن در آمریکا از دست داده و توهم اینکه آمریکا سگِ اسرائیله هم از تفکرات رائفی پور طوره
ونس امشب یه حرف حقی زد، نتانیاهو بدون ترامپ و آمریکا(عملا یعنی بدون جمهوری خواه ها) هیچه.
تا فردا صبحم لبنانو بزنن هیچ آتش بسی نقض نمیشه، ولی تندرو ها تنها کسایی هستن که میتونن کیر کنن تو توافق بین ایران و آمریکا
اینکه مجتبی خامنه ای امشب همه چیو ریخت رو پزشکیان اگه نتونن جو رو کنترل کنن میتونه استارت یه درگیری داخلی بین موافقان و مخالفان مذاکره باشه
تنکس فور یور اتنشن تو دیس متر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78218" target="_blank">📅 21:35 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78217">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78217" target="_blank">📅 21:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78216">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a862002bab.mp4?token=EBGkcnB8CzYXKa2QzFcUDJroVR1KK9mly5F44LMLJZmTpLWq4BHdUQboSSQ1Jbgo8AgVgCyoMHFn1e2AM35S1ib8UffZ5gwAxLH5itIiNd_xkC1bWQALVfOBAFOJx8znyOVIq7EUK5vnTcr6yLPKBVVWvfkQrLHmxKAgbHjVMtwoVKJfGr9Ln0Y-aq7gJCYfQJgWvMVOLEmgZKN2gUz96M47NbRPxn85BMdOt_rSybqx3QFqGVDmklPARkRBiVZ3xg08KNdZGQCAoo8zzQAtDqCIWDy2UnAYaK-hiX0hzlO50mHcRiIfvvuUn4sSVj271Kht-xBxqjA9D8djwXCRiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a862002bab.mp4?token=EBGkcnB8CzYXKa2QzFcUDJroVR1KK9mly5F44LMLJZmTpLWq4BHdUQboSSQ1Jbgo8AgVgCyoMHFn1e2AM35S1ib8UffZ5gwAxLH5itIiNd_xkC1bWQALVfOBAFOJx8znyOVIq7EUK5vnTcr6yLPKBVVWvfkQrLHmxKAgbHjVMtwoVKJfGr9Ln0Y-aq7gJCYfQJgWvMVOLEmgZKN2gUz96M47NbRPxn85BMdOt_rSybqx3QFqGVDmklPARkRBiVZ3xg08KNdZGQCAoo8zzQAtDqCIWDy2UnAYaK-hiX0hzlO50mHcRiIfvvuUn4sSVj271Kht-xBxqjA9D8djwXCRiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظریه داروین درمورد تکامل انسان
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78216" target="_blank">📅 20:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78215">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">محاصره دریایی تموم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78215" target="_blank">📅 20:36 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78214">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پی دی اف جدید مقام معظم رهبری در کمتر از یک ساعت دیگه منتشر خواهد شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78214" target="_blank">📅 20:04 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78213">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B7IMDrfsFmOM1S3rTDSVBfv71EvxiDm2dyoqeBLC9f51sBF_Rpdk-OmuDero8oO2zqt5nTUmMF18Ud7Qv3nF_Kse9JbKBpBm40zQUke7mQS5f5aq_E5Vmh6JLP7SBWQgBeTJ6qYGHQf6d-xGYp3r4laHNho4bebx5q7VKyUOyqpHO82AkztAezLORCbcMA2bF_ayk7ZfK0pYsftqIM0tYkQJJielOzsxF9PIsog3Xppem8j-ovP90gnXXKOkFDku-nNaRtuSbOmbobUqq7XmRhBf5ngWHe7jn9bDPRFvPSyPkcsd0XqgTjp8EpOo46jLM11LftbATSMPXCLdPycVuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تتو جدید ممد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78213" target="_blank">📅 19:54 · 28 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
