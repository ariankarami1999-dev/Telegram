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
<img src="https://cdn4.telesco.pe/file/Zai4LCb0uhtXYbzoHIons0JyxEsqsqGySXsWD5lnwAlQzyMX7G5rf7yimedA6kHjULBKtTCXQpteImxQxouzHMlIR-uqmoraalO6lekhptjEf8P1Sm4_mrFFx9gkfPkLh9a_yv8pkxJ16yaRfHkfB1hHqyBNI1WBGsBfJHpxHp2lkMzA1Vpb6xnJlCsjYEB-ufC5ui89HAngBtDE4JKO1P2NhDkHEvudGg_ujCu4Q_bwNIEmAsxIcKz46-8QCM02yujYYfRTfItrHaQT-N1oH_eJQvcJ8WVUG31iFA6YbjWrlKBA0QSWsNlUURlOCYeWRZralpBGyOrSxJH6YW-QyA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 172K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 17:59:56</div>
<hr>

<div class="tg-post" id="msg-78578">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PR2kUV8PdPwo-sK61EJhn2uxtK7A6CDylq_tXpnbgHSn3lTvDvoLKWwh8AQsH1wtzZVJ0WQARlOdHxbkoB9S3CjkLfb9t6G2dUSldXf83YgREl2SKLMGKxFuu_3A44jfNPprf46p1eMkmUjpgYPh5AdD_jihZK13t1iEmP7TBX-Npqg3NzmNq1pHSMjYj07tLpkFOQwuDXqHSaLmkiuQsDAc4ZOLBXsCYA0mAMOwhYFKK5MTsfhjxXvyEVUmxsFbKgXXzFn0lMPdfnAEBId63BRI1JFuzZ_0-zNviJcn4qo2ZtgA3TTMJkMAjXz5N22okD_nmDzNaMMOL41mbDZtKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیت دانیال اصلی و مهراد جم بزودی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/78578" target="_blank">📅 18:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78577">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tFOg0iKY1yl1WQznvKc7ILDMcA7q7DgZmXMRVKJv9MS7-RxXeZrJMX4gJ5W_Ay--0Xtj-FF9FOQH0PfYeDSCG-CHSSh7ZJ8vI4U5MZwkwZBkEnb19lRVdTVQO0GelgoyIpcYglU2R4ZI4nyUZzmv6-Bn0E_s96utSWkSvQYpVObFSwsE9MnRbNOkjawjSUjKqCbzHAta4VfsZ_q44x7QFR3_v8WgabWu4EFttOC7v2v4_yQmMMnBSCBtWqzP_54koIya4UNhFCwSZFtrtjIWKiHGBFsclJaIOslfNkZ2Ys1Pm_jmj5Vupzk8Ri25YG_kWVDR0ofn_LTklUnIezAGEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاری که سپاه قراره با غلات بکنه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.86K · <a href="https://t.me/funhiphop/78577" target="_blank">📅 17:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78576">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">حرومزاده این همه ناله کردی که آه ۴ ماهه زنمو ندیدم تروخدا زنمو بهم بدید دارم می‌میرم که در نهایت ببینیش این کصشعرا رو راجع بهش بگی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/funhiphop/78576" target="_blank">📅 17:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78575">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">فک کنم پدر زن دکی پوریه، وگرنه هیچ توجیه دیگه ای نداره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.39K · <a href="https://t.me/funhiphop/78575" target="_blank">📅 17:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78574">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 4.01K · <a href="https://t.me/funhiphop/78574" target="_blank">📅 17:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78573">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ PlaylistShip ]</strong></div>
<div class="tg-text">فقط اون بدبختایی که فک کردن لاوه فور زدن برا زیداشون</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/funhiphop/78573" target="_blank">📅 17:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78572">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خجالت نکش داداش از سکستون فیلم بگیر بعنوان موزیک ویدیو اپلود کن یوتوب
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/funhiphop/78572" target="_blank">📅 17:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78571">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">دکی: صدبار تو اون خونه کردمت، جای بد نرو جون جدت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/78571" target="_blank">📅 17:31 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78570">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دکی: مثل بابات عاقلی مثل مامانت کص
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/78570" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78569">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اونجا که میگه چسبوندمت به دیوار با صدف بود یا مامانش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/78569" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78568">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlireza𓆃</strong></div>
<div class="tg-text">دکی وسط سکس نمیتونه چیزی بگه چون پای صدف دهنشه</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/78568" target="_blank">📅 17:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78567">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فکر این که دکی وسط سکس به صدف میگه مادرتو گاییدم داره مغزمو میگاد
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.84K · <a href="https://t.me/funhiphop/78567" target="_blank">📅 17:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78565">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G8qVhFVNrp07JfXpNG4V3hFY_bnRKtDYpJa9g9kN9Opmvkqq0MO7DZAoe6BOX68no69TYdCu28uzHyZ_AWJRG3VHN2m7lYIAFCb-DXC8nTf5mkFCykvPRVfv36Rtwf_VFrqRWt-1Yt6gDwB3qbBKcBqKcVboldAp9EfGcomG9lvqELabAjUgo7Rv9Euy1XiOfTGXMIs9CnvFlnd7xE3DWr-mMb5nJcsq38Nk9HedXobHanFqF_YtEdHCbDwzfVmFSWQgq-aKBlELAEmHIVCkP3M2rOwfsVGoRjzBqTA5USLQDC42ZJQG5EHCKoJBhWXKoiz94_zkDYXltPXovOx5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NbB4gukqBz3hf75XI730WPdgEWQP9tlOZgzmou6Yp0o_hBwkTsr4AAolzUh4hjPmzbxrf2vSLdv96jgfI6MuYAFfA9RDtmUQ3d8txwc-PcJ7GWXScn_SMCH8uT_Q0-0UvsJCSEhIIitmnW0mxNJzCax0pEFHC_3Tw0xggIqxlX_zonKRQy7UmIfwr2zaciEEg-DXua-R08URG8-4dWUmEWNogZ3OBA72HRg26msINSunXQ55WNS28h_I9ZYLRUHXuuUurDubGil2RfXT7o2BNc9r20a67O9xw-9NK0O5-ZwQGozyarAEpyHiWSVKPjFfFN7HH1L2MLzp-1HtIv1bUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.    Youtube Download  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/funhiphop/78565" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78564">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQRMFnNDkBhWL0knAR6LXrKFnb5v1YrvAAd-MrEP1mrPPZietNypBvBQRYZT-4PQQPLY169lgTV4Zex98wo4xJgb-mPGrOK9PufKArEQ96etN_jkeZTtr_b5laLMy3mTi8HP3gLYM5yjzWQ98TrqxaBpM3H6c7AD2jVa7lID5dOoqdoLCke8TdGtW8M6BUEgCJiniEDUhyR6BMrktgyb8ZQPOWkKfFYo3fy3T5tcVpzy6WI8Uysbj7-HHb6IHx1Hu5_u_MeqH0Fsjqht2inGhG27_tOWd8zBS7e9-U4lmyNAixQievlso-mQKbxfa5kEQYyFXI8TnsYAlZlHniEDYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هیپهاپولوژیست  به نام "مامانش بیشتر" منتشر شد.
Youtube
Download
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/funhiphop/78564" target="_blank">📅 17:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78563">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کونی رو ترک عاشقانه این چه اسمیه گذاشتی</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/78563" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78562">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دکی کونی موقع ماشین شستن من چه وقت ترک دادنه</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/funhiphop/78562" target="_blank">📅 17:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78561">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">تنها چیزی که اَ بابام میخوام عشقه فقط
من برا بابام قیمه میبرم من من عرضشو دارم
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/funhiphop/78561" target="_blank">📅 16:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78560">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jz0ss2p3fhoLlwweMV1MMBXGkWFv8SJEr3MMLcWqvDj262y_FouopSyUQiOugqJgw1NZgDKTagFHjKcNO_HTQDnFaJoQCVlrws6IjfTSXsgj1qG5f8dyJi8rZCj44laeuWXzvtAxp3nILb73kon4slqRHO4AJyo8or_7ayJj_O8wEylJqGc5L1b_WuzPxwjwU6sEDM7fXzj0yHBrAugHjEF336z4mvQIynn7Nvh1UGORw0Nu3jiYcvgL0UTAdfzWc0VrRLIwfqZt5RV06Wwo65ViT5VISzI5YP8VOIjwU8qQfMX1AN9ROS4jV-G1xbORSS2QcmehOw9t2M-ZSBPd9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو رسانه‌های آمریکا به جز فاکس‌نیوز کلا یدونه نیویورک پست برا ترامپ مونده بود که اونم کیرشو کرد دهن ترامپ و توافقش.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 8.69K · <a href="https://t.me/funhiphop/78560" target="_blank">📅 16:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78559">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TQgpekpggBkZS0J4-DsGii6QPwPTePvRSnnlhBcZXE7VcV4dWbXSbiK-9iXUCAEm9R6Ir1ui5IJnpZTj37uysSJnrtd2-G_YkAVvCGWHBm366JUe-4UhEpFTXAenxz1cfk8dBPrF1okLQwGIghCmty9CKNy1pWKUBQW-lY722TpdrifiaOKqbpQxRDqmMs-2EWGfcFXouhGOZ28KVUAIHTKEXNZLnu0Q5H7WiNZNdu20ml1b0bK9ss7gENsWnS4kLb9jT-Tx9sd79RQjSFrcPUDrvOncF1RRRJipLPWEL9ynlvDa7eGnpFgcwqg_fnoRMk4sgGlENJtk29vV__7-qQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا با دست مسعود روی شهبازو کاری ندارم
چتر چی میگه اونجا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/funhiphop/78559" target="_blank">📅 15:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78558">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">پزشکندر و عراقچی رسیدن اسلام آباد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/78558" target="_blank">📅 15:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78557">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">علی گرامی بخدا خصومت شخصی باهات ندارم به عنوان یه شخص بی طرف دارم میگم، یه آدم رندومو تو خیابون نگه دارم بگم بیا رو این بیت رپ بخون از تو بهتر میخونه، روی این مسئله شرط میبندم، پس لطفا فاز نقش اصلی سریالو تو یکی نگیر بزار یه نفر این کارو کنه که بهش میاد
🙏
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.69K · <a href="https://t.me/funhiphop/78557" target="_blank">📅 15:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78556">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مسی و رونالدو جان جدتون زودتر خدافظی کنید فناتون مغز مارو گاییدن
هر سری یکیشون گل میزنه فناش مثل زامبیا تا یه ماه میوفتن تو گپو چنلا سوراخمون میکنن که ابر ستاره تاریخ فوتبال گل زد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78556" target="_blank">📅 15:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78555">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJgVA0gxluxbj1l6-6DoUX7Exz9pWrbHMzz6QZKI-fKOGnyOzEyc4uFtfbGBS7GjAJlCydSp-FXteHjHZM13e70ek_Gs4hGFOkZLfriKD8TDhX8VBb7g6AvwhmsvLksdv7VXcdJ9hB6QPcIeo_zzIavyE30WkKboWowXhL_EV3lyr55X3WCQ1G-_R-8SFt3MBsuFnPbKqIefr2GSC0vGmlpK9P_u4gXN87KpBhNg9If7tQx5HmPmIcReXFW67xsDBXHtB_EhGfEd2Nl-2vQCHvtFhWM5j9f0oSXsGUM3T8t7T4DJL149tljSKLyDgwuvJvM82LIYDTq3LyIKRBU6_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78555" target="_blank">📅 14:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78554">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من ک میدونم بانک هارو بگا دادن تا حواسارو از عروسی دختر شمخانی پرت کنن ولی نمیتونم ثابت کنم:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78554" target="_blank">📅 13:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78553">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">مثل اینکه اکثر بانک های کشور بگا رفتن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78553" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78552">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">آلوارز گفته از سبک بازی اتلتیکو خوشم نمیاد، اتلتیکو چی گفته باشه خوبه؟ گفته خب بیا برو آرسنال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78552" target="_blank">📅 12:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78551">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حمید سحری عزیزم تو ویدیو هاش به کصشر ترین تیمای جام هم اشاره کرده ولی به ایران نه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78551" target="_blank">📅 12:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78550">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tHar68exqNBPAs6TYnfZblvYaih1H9BR3059fBARq2o1zmIgZ344Gnyn5e6CyYYcVbEuVY7I18Yi7iyUZ7BL9XCC_w3PagnD0U6usC0FZjIXyp9WYt3V7wEsrjtzf3XkKBIlREuhRadcAKwFtpojP2_7g-5pjGjq78N9Ba1VgZYdlh4OTZnESJ4oXn3xyPNS_XOyY4ifgdKubkiTk2Sdki3Ai46EWB4tXSrenb9250AzDCLv4_nQDx-5k9iq8ygr2KTF7u9N2U3HC6X5lCUW-q_eXXi541Mw_HFIVVgYqk-IAco18Hb4NOhn7rnOU_ZWTlDo86hCijulcwGtYoJNTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78550" target="_blank">📅 12:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78549">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ehc5uFF85238ZCGL9wL03FeAX7gqzt-_wOIRyxi0HZ_Lxdjv5KxAX1H_rBf0HWv_S5pJ0u_0XXu3e4S-8AeRBcM7WUx5wAw_GKT8TbeMY8hSyalvCoeaCCTKNi-xVCo7Z3R7sXngZ6ifedDHKZ2XMt0pfmyDgYGvwWFWFQTntVjFz91Zu4LAkOBJZIxmleakOg7wwbkriPeXAGiZFHAhNGE2X_MMBgia5mmAhqpubxGA6JCez4WUAfFtD2O2tdvI6G4j6-qpDi_HgIU7Z6JEcEKZHDoE5Wt9GW6ENFpctC4rd7Hl6eNt4lwBobP8QIEtS4Yg2dojznG_oFNrcvbsDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان از ارث محروم میشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78549" target="_blank">📅 11:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78548">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/cBqVXBo4jyr_J5_3FNQbeeIOQYLC_tc8CCbk6yM-awvRzMylyPNQEKqX-VJFGKgyOfU5mPYlpiWU5tnN5VNL-JMRPsCDzd76oWbm1wEL3T8gxIhQ8d-U6MI7NW7AK_mDIC_AWx0oEnudzuKWJJF-S9CVUzYg80lPR-LsbviaEPfWt9OhNjcSx37wAIiaYTZzdf1Ewj22qkAcITClA0xZ8OhQ3VUkLJ-ZkhFYvmVpOQNjvZQdeZV2JRk1o08PwbKf3ILsFcnGK6a_dfYgCmnNBNv1qW2Ek5n9H5p_KekM6nW_9w9NQreoWpu1q6h6IXWs10UGPB486ULplCzjAIcFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارلینگ هالند: راستش بازی با فرانسه زیاد برام مهم نیست چی میشه؛ احتمالاً اونا ما رو میبرن و حتی احتمالاً قهرمان تورنمنت میشن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78548" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78547">
<div class="tg-post-header">📌 پیام #70</div>
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78547" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78546">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UH6QTpzvqlpYqNfyZ65zSbXYPfwCu_Cpn7xtMrbEizIJCfwJsOgELP_aDvgSuaD3lwQRfPD5Vqnw-1605qoVzSiXjk7wToYy-3i7U9K8eHEzDJ4PVZNb5znn2T4vywfeD9Dx4V7yfxvo4KLLWIl5_mtkk_PQoJtFtX3RKjygIL2yI7g4Py5ztr9oiEX-42I_ylRaULDxrlfeSt6yyaovSvy3QtMCdA-tQHZ6Oznx6e5qsyeqtmE-I9vnO9LlcEpEyOCDCdGAWeXBqGCH1DT79BZSk3uNyUQWs94Z0m09shVSJQWVjcix1OWOSuJ3ORMKpgPH6n8qCOh3SODUFKNvLQ.jpg" alt="photo" loading="lazy"/></div>
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
📺
تلویزیون لایو برای پوشش بازی ها
🛍
پیش‌بینی مسابقات با ضرایب رقابتی
🎇
بونوس‌های متنوع و جوایز ویژه
🔝
تجربه‌ای سریع، متفاوت و حرفه‌ای
R2
🅰
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
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78546" target="_blank">📅 11:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78545">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ilzs8yM2K80TFQev2fcZ7xvOMpTCEED7Oc0GF_NKXmCjmFvW3MvoEIWIewHU2Bn9j0foCabIeQ1_EHH9Lm9UG-VGasy-iVSX0I_D7mqe405wAXYeUhoQX6YhE7Gq1lg03i16pnotbu7KJzkrVjIQj29hzd5CO73zKzZoBm1xUaqeXWTBulIr-mZJ8EELQnIFCTfxJ6JiWH-3gcvxcVc82-oOm7K3jwTwuzi1g3usVPHJoP3vFGWNGFoGdzypXtl09RfdjPb8DAQGrHL3fkG3k3AsoIEk35VBVDDvcEUmScjAA3PvRJ9NjjOxFTe3Q5cX0ZARAQSI2yMZQ27vlCvC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این الان تو حالت طبیعی به وانتونز و ویناک گفت فید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/78545" target="_blank">📅 11:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78544">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بی شوخی هالند باید پاشه بیاد بارسا و  رو در رو با امباپه رقابت کنه تا فوتبال دوباره جذاب بشه</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78544" target="_blank">📅 11:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78543">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Svb17VF-c6GxAZ12KovtyW3RS9I2bziOiHX_hPgiT_a2sZ6Fa_rs8sEOLrJX26IcxzWKkisEpQmYDlWuENiC1sKuSB9gxmuIOaQiwwttduEtaXR4xr3BwHVpTcoeC97bZwtEC31jK0wp_cJGuNiJKyaTX7aG-fDCW44UOexJW5Z2cZfkEne_DjNUUMWUoXeDSMzk8wKol92WMrEXmVEaqF0S4ymbqgAugPTLOVI-fwV2cvhyffVGeOYgEs74kNFOY89fHRJPVbDg2B4t-vUnfObzzKD35eIVuT4OfrrjK0x3y4crvZdKVdGITaPtY3NgT6L5ZAAmXUMPsIIcAHefnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کون مسی رو ول کنید کصکشا مثلا بزرگتونه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78543" target="_blank">📅 10:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78542">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GGKXTf1o1s8U0CMzDFykor_dhQy-ksnNxBrvRNJ-sHsHtQ2MD9U6xhcSAXGUtFOwc2bI_XCP6q9VPNyrtK2dMJkdEV4oE-Gu6GrtnQnA3IvyWsorcTDvr7u5BBLNti3dE65unMytjPVswkkhEUMFGxOvtv-4aAzGhjN0tRhBL_2aeNdVnsndz4lGxTHDm8dmxHfWwbJ1xBt58qB5NcGUfCNtIsHS4IdW3CGRGbsON45kVLqLyFIlwzobLsfb33I-Hl8Hczl5D4LBLiVlrJAUPV-4sBrXL4qDGh_K_bEiCsyIcY56_esXd_INOFUic1xmWht_tMFKQ9TSRPznHcLylA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی رئال اولیسه رو بگیره کون بارسا تا چندسال پارس
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78542" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78541">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بعد اون همه کارزار گذاشتن و اعتراضات دانش‌آموزان پایه یازدهم و دوازدهم، آموزش پرورش امروز گفت حتی یک روز هم امتحانات نهایی رو عقب نمیندازیم و سر تایمش شروع می‌شه.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78541" target="_blank">📅 10:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78540">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛ یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس   @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78540" target="_blank">📅 10:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78539">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=BmyUZH-gNaw3Jf_weJFvmFum6T8lGvtQGa7gp-y46mXTZBZhc5Fss45dIIau2ymXyeUbkP0q5icjGXoWj9PopJECt3KllI9IAoi7IHcp6rQjnKS3a_sKUm0ribLcBlhKbMDkQB1WWSHpfCgGe2Kzlx_vHH6dWQhydCz6bm1-lR-rLcnvIwE3CrU2SMWtxdZQjTnYlrThN_fiIvNcC_a46-tGk0KnLNRIl3CDJpNQuXFu4k0QRaMzfqwo37mbBfW52nYBAQDHpFGCZX0zyscFDiMWdpz_MHYoG2BZzD6l6Nvd8baJUd657BtWDfTKkwKtx8aEbN4i9cymu7xQRsvbTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef49ae44df.mp4?token=BmyUZH-gNaw3Jf_weJFvmFum6T8lGvtQGa7gp-y46mXTZBZhc5Fss45dIIau2ymXyeUbkP0q5icjGXoWj9PopJECt3KllI9IAoi7IHcp6rQjnKS3a_sKUm0ribLcBlhKbMDkQB1WWSHpfCgGe2Kzlx_vHH6dWQhydCz6bm1-lR-rLcnvIwE3CrU2SMWtxdZQjTnYlrThN_fiIvNcC_a46-tGk0KnLNRIl3CDJpNQuXFu4k0QRaMzfqwo37mbBfW52nYBAQDHpFGCZX0zyscFDiMWdpz_MHYoG2BZzD6l6Nvd8baJUd657BtWDfTKkwKtx8aEbN4i9cymu7xQRsvbTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من تو کل زندگیم دو بار واقعا از ایرانی بودنم شرمگین شدم؛
یه بار بعد چک کردن کامنتای یوتیوب استاد فراستی
یه بار هم بعد از آنالیز میزان ثبات روانی و نمودار ترسناک سقوط IQ ایرانی‌های عزیز ساکن لس‌آنجلس
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78539" target="_blank">📅 09:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78538">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78538" target="_blank">📅 01:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78537">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=TAk7DY2eGIDifjdkaBU1aO_EZ0LGiTJtBwP3puRT_pcAh0u6FgnE8T311v2HPtr5zMhBo_lDXB2zHzG2YCgH57L0wXILz_X7TKDRA9S8k-zlcwUaCHwhKm_qu05VYV7NXUpINFBthEBmCcqViGOQL89PpJ4-c47Rp5fdJ-RXKE9gC61M8xym0c-lKvTc9jkai96t6Ijz72gy-nEGS1ea12f8_nxBGoyavskJEpsVM-JC1PQgc2EJS93lVVoWytVI6P4WJm7vxG36WSxCTEJvCJrjVWdiCIGo9c2MFgTU3DjvCOo_d686R8LSyiChvi686FeSxtiYLpOo8Jqc5OGFYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0ec905e2fb.mp4?token=TAk7DY2eGIDifjdkaBU1aO_EZ0LGiTJtBwP3puRT_pcAh0u6FgnE8T311v2HPtr5zMhBo_lDXB2zHzG2YCgH57L0wXILz_X7TKDRA9S8k-zlcwUaCHwhKm_qu05VYV7NXUpINFBthEBmCcqViGOQL89PpJ4-c47Rp5fdJ-RXKE9gC61M8xym0c-lKvTc9jkai96t6Ijz72gy-nEGS1ea12f8_nxBGoyavskJEpsVM-JC1PQgc2EJS93lVVoWytVI6P4WJm7vxG36WSxCTEJvCJrjVWdiCIGo9c2MFgTU3DjvCOo_d686R8LSyiChvi686FeSxtiYLpOo8Jqc5OGFYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیف فردوسی‌پور و خوش‌چشم از بیف تلخون و اشکان فدایی هم جذاب تره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78537" target="_blank">📅 01:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78536">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgU-zMxUm-Dj2wZGE7W8JEGvmLdOICI3rzvZpuf3xsveMILAdZ6ItfzU6vsHsDXO8Cpgr7FCWVQCTnlLwmPOnhdqzOjqwifTz1QoDr8h31Ed7xipzmKjcyp0c8wNq-iUl8CmkHrqkYrm73oNj8jvL6GpLqBKA-sRLvY6xYd_h7spPey-JqxAoiB2VPWcy-jdWwoq133QTN9cVcIH7CkOaEJg2ugmstKa9GlDyLBQ7wgMPMR3_ip5T-r0ysKXEL1R_SwrGxs_xh4rmUfPiFYDvryUHm4TrnUv6Aw3cICDihNmUd-tEaNeJafixbu4XTPomS04zwg1X4qL852-v8BYRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طوفان هشدار تخلیه برای تماشاگران ورزشگاه رو صادر کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78536" target="_blank">📅 01:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78535">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78535" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78534">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نیمه دوم بخاطر کیری بود هوا یه ربع دیر شروع میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78534" target="_blank">📅 01:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78533">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78533" target="_blank">📅 01:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78532">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">امباپه احتمال زیاد موقع پایان کریرش بهترین بازیکن تاریخ جام های جهانی باشه جلوتر از پله
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78532" target="_blank">📅 00:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78531">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کصکشا اینارو من ۴ سال پیش دیدم، چیز جدید ارائه بدید</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78531" target="_blank">📅 00:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78529">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">امباپه چی زد خارکصده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78529" target="_blank">📅 00:45 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78528">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T079QCBDhyIzc1eq3CKGj5fAfnAugckTWZ2nJVD2FTyH6zkyCnjokL318G-riA0nVsG-7D9K33LHZ2uxLTUnvgvIo32IEKCqE5596ns3JpuO7-fClSbNguELnjgE_Z7KpnasWPlrrHLL7nDSsDoqB5y30ygbeCBAR5-glUr8wpbx9wR5HDjAsohyPnIwfj9p89aWksBbjngzUJOoYd4LLBjUQXG3XOpnAIoWgSEfvLWZO-9Mqcs6EMRuciPwOk4Z5BvcEUpHv9XU8QI5Qd7vpQ2pfnruYgjJZS1B4BOKsvyoU1tuvK4Mq1ryCHdN4U_avyVN0YfXrOK5n5P1o3OeRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی جدی مجلس چهارماهه که کامل بسته‌ست تا کسی نباشه که جلوی باقرشاه و پزشکیان رو بگیره.
یه سری از نماینده‌ها هم علنی دارن صحبت از کودتا می‌کنن و برا یکشنبه آینده فراخوان دادن که برن جلو در مجلس، اگه باز شد که برن تو و اگر هم نشد همون تو خیابون جلسه برگزار کنن درمورد روند مذاکرات و جنگ و اینا تصمیم گیری کنن.
یه سری حرفای ضد و نقیض هم درمورد تصمیم نماینده ها برای استیضاح فوری عراقچی و حتی پزشکیان و باقرشاه وجود داره.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78528" target="_blank">📅 00:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78527">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دالگخیز:
پسفردا به ناتو اتک دادن کیرمم نیس چون زمانی که ما به ایران حمله کردیم کیرشونم نبود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78527" target="_blank">📅 00:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78526">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427abb0164.mp4?token=L908g1z5-Q4OSvgc5Se7LIe7uCw5322BMDuub3Zp69uLPj1p-g-dqFiO6budreVqLk2a8sNtsjxmRx0xVuO3KLpHaFeMd0w_lN1ZBayE9Zz_m_TOqTGunek8c88HGFeF8rAjJ8D_hjqBzpiecS9ZXwjc9-eR3zHZqGi29o-Liy1foa4SNouTG3DM2u39_aNPGhx8Ae_8cThqMxIAVTimnxcm_S_YqJ_cLcCNoq6jNGUf3Xkd0zs-tnK9BE2Pzgb9YfmmXnI12GjSGaUs_1qZIEBQcb01lwPCglDstRpMDllQeNt1Iv__a8dIVQrIw9aqVFtKq_beqgU1hp8iVbk4eA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427abb0164.mp4?token=L908g1z5-Q4OSvgc5Se7LIe7uCw5322BMDuub3Zp69uLPj1p-g-dqFiO6budreVqLk2a8sNtsjxmRx0xVuO3KLpHaFeMd0w_lN1ZBayE9Zz_m_TOqTGunek8c88HGFeF8rAjJ8D_hjqBzpiecS9ZXwjc9-eR3zHZqGi29o-Liy1foa4SNouTG3DM2u39_aNPGhx8Ae_8cThqMxIAVTimnxcm_S_YqJ_cLcCNoq6jNGUf3Xkd0zs-tnK9BE2Pzgb9YfmmXnI12GjSGaUs_1qZIEBQcb01lwPCglDstRpMDllQeNt1Iv__a8dIVQrIw9aqVFtKq_beqgU1hp8iVbk4eA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویناکیا چیه دیگه کیرم دهنت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78526" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78525">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اگه این جمهوری اسلامیه از آمریکا مواد غذایی میگیره میده دست بابک زنجانی که صادر کنه</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78525" target="_blank">📅 23:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78524">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ: دارایی‌های آزاد شده نزد ایران برای خرید مواد غذایی از کشاورزان ما استفاده خواهد شد.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78524" target="_blank">📅 23:50 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78523">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78523" target="_blank">📅 23:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78522">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قالیباف: توافق برای آزادسازی ۱۲ میلیارد دلار نهایی شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78522" target="_blank">📅 23:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78521">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">پسرا رو برد فرانسه میبندن مردا رو برد مساوی عراق</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78521" target="_blank">📅 23:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78520">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TDdRGRVmSy6HIu_VNyA89B445_Dma_TktsZwSFErOo_CzHI24cB0LzFvMFuWrxnaCpCHap3njHR8Ej-G2Z4Gfi7r5tEABVKDmDe5YtE9pIzbBD1x4iD7VtDPCq_AX3pHZ7_j1JQfnoeOY1vyCnrNRmCcFIqGS7_hocOab8al_ScJsJMZH2-pQyp-1EJtt2-Fcale1nyuLpOiNORunIZlt8A9f04bsppCswSASOwk1w2d2BQaB9sZW5lxGLGMTMAQ5AUehyp2Xl86j6FJ7ywjiIA-m2nPbNEsxRk_SHeIH6rNP16D0Ae9NHcsEqVoGyZ7TIT977O3XjgK32_GHF95pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب رسمی فرانسه واس بازی امشب
اگه ببرن میرن مرحله بعدی.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78520" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78519">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تا الان صعود این تیما به مرحله بعدی قطعی شده:
آلمان، امریکا، ژنرال، مکزیک، النصر، آرژانتین.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78519" target="_blank">📅 23:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78517">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R2ukvJiP3PwUPLkdDb09g7iK3S4TVHwXwF_uiH-nNfczQ0UHy3ZgAxCzac2uAwALnE7RI8MjSFgNfGQrH6f2BKnahY0FR2HuoaUaLL2MD_BF5peoCffrTG12RUceCKdwOWBYNNhFOM0t0SNaBoxMU88HhwPov7UMgPf6Kj1wD9hUYyrGcQECWwzbKhtPG_TWpLjVF4kXKFU6BAp0Tq7jZgwbjzGO7kfPrk3L6UXB1Z9Bd7cEL-jAF3WaerYqZWLzV4qhb2gi_GLZVp4plnY2XOGaSFd8qg15GigdHoghUhSZG4BcDrj-AispSChzofSccnfwiKGBWG7yLCqdAJlZZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NJnlDYxzjPRWJTjCtekmTMlvFrCF-bpek_DyEChPLsvev3sa3YV-n_OM5cDXW-EF4AXcsY_EslA4_goZnECo4QFx3y0Cxgf7MSOevevh_xroRjsyVabT_bkoBMUitmFJcESwQDUS1bGUr4bsUeJwwD_iwXA-a9Zr8bkVTWf9GN01L52LJrMPHdn0LjkWSSJT30_na0dnmgwlwv-tyvcJMKZmDcsNbVKy9AgnHbzxdMTaCtEL4A83LP2kYiXsTun3zb3MF4Et49PZCcQXxN9A6L1zMh-Og8RpIRXbm4BG1ixoghHPgw2LE_n_fT7lgZYFneSX_LNwB956VAvEXxQOxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78517" target="_blank">📅 23:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78514">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">خداوندا سپاسگزارم در دوره ای زندگی میکنیم که سعادت دیدن بازی اسطوره بی چون و چرای ورزش جهان را داریم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78514" target="_blank">📅 22:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78509">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">رونالدو فقط و فقط ۹ تا گل فاصله داره تا آقای گل جام های جهانی بشه</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78509" target="_blank">📅 21:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78508">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">متاسفانه نیمه اول تموم شد و قراره به مدت ۱۵ دقیقه از تماشای بازی خداوند اصلی فوتبال محروم بشیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78508" target="_blank">📅 21:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78507">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rb4WDCTiSeG9ASGt4CWWX-e7AyGpvFEVJ24T9Aa-54EyT_QDoH91AFNHcj-bD8qotAd-U3T0xy4dk59MltK3lXIRJ5emiLJdiGz9fs0vwZa3la0jonuNxwF1pc9A491yjzx8W0ZpoBvqgWIOityHwLubvaL0PE3NigZy9CFlHVByfm8bCu9fnjLnU10vl1ELJWyywuHMuR9NJFptyz0ptlm1xrRtQECEsUgErB86svk8BiacIgjLBcXgXGdwj8juXlJtfgiIKdnGe8IjJFSRNyscky6PLBCNuXrZokeqqtWiie6PBGFWl_JogvZyapTJohk7rRmc4PlKO0GOAqEr6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78507" target="_blank">📅 21:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78506">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjaoOe9FKY2vLkzBSvdL7J31EWXZnuMOqAcNvzKi9tVTCSBCPPb8ylUkZndFjVE4ABvcSpa8Er6DQTF1dt60hqoVT32C66Eg0h0WDzzJz5Axn2lKvcB9lCOeRjTDaNTYD6Iwj-RJ10LnxeWca-d4EhKuJZQUR2JdiLUDim0geRsU7HD-owhTT33DP9iiBTLx4g5xYrbo9E9nlRTU1DyGvLDs3sjSaYVK_xItRteUQGLYcIL19ocAiS0oUclBC0JfuBSSuqWsI0_n9KFqllwCrjkHbO43TufFqzoeYXVuLA8IPpzbdX3oL57ijTIW_yZXhPGRSyH0932VaR8bFDxF7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78506" target="_blank">📅 21:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78505">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">رکورد کلوزه شکسته شد
سر تعظیم فرود میاوریم به احترام لیونل آندرس مسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78505" target="_blank">📅 21:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78500">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">رونالدو اینو میرید رسانه ها عزیزاشو میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78500" target="_blank">📅 20:57 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78498">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پشمام
چی گرفت بیرانوند
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78498" target="_blank">📅 20:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78497">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">وقتشه پرتغال یه ستاره بزنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78497" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78496">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">نویسنده کتاب تاریخ فوتبال اوانس داد و پنالتی رو زد بیرون
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78496" target="_blank">📅 20:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78493">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z9ZdUbiOwOleMda1dMytAdDeQvzhz8GFh5cyTvcyGn7Ij6ApswpcSNxiHJhEQwvOsiHC8gLDkpt7AORwJWPvVJWBcFzdy4tZkwRWlxyK04KtkXvjpO6WhEeVoVMlZrBDjInDUWG3_d-RC_fZ84gsdRvFCgIbFsADXg7q0UqcdOcqE-jVWFrs-joDIeSIaGxAkxIOA0JzzH2hhCx8ryv8Bj-jd3J2Y80pSaZ-KTeR3Sz2H4srQlDJxWKiBZMflofRQljmj2GhgEE5GttgWW0HNi7-F0Fc8nMigpY0cRgZcQ3QdBd2Fwlg5Xwr842zzHdqXTXXDBLkckI9GsLr447HRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این پیام رو نخونید!
نماینده رباط کریم رسما درخواست فیلترینگ میم الاسکی را به کمیته مربوطه ارسال کرد!
میم الاسکی با سابقه 4 سال بزرگترین چنل میم بودن بهترین پست های کل تلگرامو جارو میکنه و با ذکر منبع میزنه چنلش و باعث شده مجلس از دستش فشاری شه!
جهت حمایت ازش جوین شید:
@meme_ol_ski</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78493" target="_blank">📅 20:30 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78492">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">چیزی به بازی پروردگار فوتبال جهان، حضرت لیونل مسی نمونده
به امید درخشش برترین بازیکن تاریخ
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78492" target="_blank">📅 20:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78491">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=O6KWdpSfVxV-kYKIXoepHbIuXPXGOIRG-5VfPCKAtmF2oXEGymUSa0d9i3Y2dq1fd-brQbWx_tF6IA4mNDhgaZ6gb1njl8rEbDQfYGa1tsmHAod1ACrHEZ5txnT7yVJCuJVs4Mf0hPPfcgJX5jnGgdbP-lXEkgj0n8pfxAVnnvv9hX7KK04NkoKT9ACmiAOILTnV501sr1jRP-YrJk8P_GQM1Hn3Ke_HBLZsp56-pXfsiBBgdz2cCxh0TWxmQtige84pZjUNcRSz_yl8l59j9HdLx47xK_nMuAdZ9VRs9Scca31aS0S6-VObZZq4Ou39cin4CfYDeOFbt65Jp4ntonNFLIc9jS3lR6UUiQ9wBs11Fxby2iK1_dVHcN8Nk5sNfZPZHTaxIHDY3SMcWX1gsIDzrSCfarYWGjctaM4saLOqtHcVWNbDOC5NkKXW5Z9rHCkJWWZyIpuW_707Ae7eNam9N3s8loM6yOpePedYnYWKHGomtqDahPxF05SIyHhClePyxpxIBS-ZMs-rXBdItnpjpTAYVW4TCyWpqxpZpGAfsUif4uCkR6gFdH_7ki8Oj7CIrhhJvd6IJb4Qgmt3H5JkBtbv8xvQKd9QLdaohl0OuxR57FP9_CpLvBux_2yJHAMQcDnvzJOjddBmApbYjWqW6kGQPHa3mBca6lnKraQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49461d24dd.mp4?token=O6KWdpSfVxV-kYKIXoepHbIuXPXGOIRG-5VfPCKAtmF2oXEGymUSa0d9i3Y2dq1fd-brQbWx_tF6IA4mNDhgaZ6gb1njl8rEbDQfYGa1tsmHAod1ACrHEZ5txnT7yVJCuJVs4Mf0hPPfcgJX5jnGgdbP-lXEkgj0n8pfxAVnnvv9hX7KK04NkoKT9ACmiAOILTnV501sr1jRP-YrJk8P_GQM1Hn3Ke_HBLZsp56-pXfsiBBgdz2cCxh0TWxmQtige84pZjUNcRSz_yl8l59j9HdLx47xK_nMuAdZ9VRs9Scca31aS0S6-VObZZq4Ou39cin4CfYDeOFbt65Jp4ntonNFLIc9jS3lR6UUiQ9wBs11Fxby2iK1_dVHcN8Nk5sNfZPZHTaxIHDY3SMcWX1gsIDzrSCfarYWGjctaM4saLOqtHcVWNbDOC5NkKXW5Z9rHCkJWWZyIpuW_707Ae7eNam9N3s8loM6yOpePedYnYWKHGomtqDahPxF05SIyHhClePyxpxIBS-ZMs-rXBdItnpjpTAYVW4TCyWpqxpZpGAfsUif4uCkR6gFdH_7ki8Oj7CIrhhJvd6IJb4Qgmt3H5JkBtbv8xvQKd9QLdaohl0OuxR57FP9_CpLvBux_2yJHAMQcDnvzJOjddBmApbYjWqW6kGQPHa3mBca6lnKraQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس علوم غریبه و جادوگری در شبکه ۱۴ اسرائیل:
دلیل اینکه یهو رفتارای ترامپ ۱۸۰ تغییر کرده اینه که ایرانیا با استفاده از یه سلاح الکترومغناطیسی با فرکانس پایین که توسط ایران و روسیه و کره شمالی ساخته شده، مغز ترامپ رو دستکاری کردن و این افکار مذاکره و امتیاز زیاد دادن و اینا رو تو ذهنش کاشتن؛
از منم خواسته شده که مغز نداشته‌ی ترامپ رو به حالت عادی برگردونم، منم دارم تمام تلاشم رو می‌کنم خواهیم دید چه خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78491" target="_blank">📅 20:12 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78490">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">ایموند داداش این چه کاری بود کردی</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78490" target="_blank">📅 20:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78489">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GpR4HKtE-4Cg8jw6N24ihrPW3IQazqmnx_fLz3gXNONfiBu0uRL6GPI2M5tm1ys7-kn0wt74NpdR-5gnqf9E8pAQlfNAL5jlhunEw-mYW9tJ5KV7QB1xYVCIt_PHrMRiz6Hb9-xKDZwFxc7fzwLc5pHW-p8O_28BCx4-OddbPVJeSaGd3xPN1GBbSd_j6aaZnvA1hvO5wZw8md_XE6d6aNjKv2Hhiuq5KuXJVJ62ltjVE2IQQpAt1lYC4pIFKVST16ePAMYSEQexba0rRJckKws0V7fn8ueLqdNJRd8y6ghn33zn0N3o-OXNpm34I5XqRIq9f_vPIHBvH7SYGy-CuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دست خدا عیان شد سوارز جوان شد
بازیکن جدید لینک شده به بارسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78489" target="_blank">📅 18:58 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78488">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78488" target="_blank">📅 18:52 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78487">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">فدایی به هرکسی دیس داد طرف بعدش چرا زنشو طلاق داد, اون از هیچکس اینم از حصین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78487" target="_blank">📅 18:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78486">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">حصین زنشو طلاق داد
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78486" target="_blank">📅 18:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78485">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آمریکا تمام تحریم های نفتی ایرانو به مدت ۶۰ روز برداشت و ایران تو این مدت میتونه به قیمت بازار آزاد نفت بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78485" target="_blank">📅 17:26 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78484">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zvfatd53JNcN9MTYA_4qpm__C7QH7ddTwkhNFcBFlzvxH53L1fZUrK9PclcPTTJHyg9uq0FUMD_FzXrTbwnSeumCzB1v-O2ZquC-1n9utZhZZTKVRk5ddcmhmWQFfUtUKPjtpLPfGHyw7WyR-p-FHBalOYxNLPtfz4Z6y3gkHnyYtywup6L4Ee1GZ3cdXbwaQDQiyyrp-DBwukFGRMD6cBiIxcOp0jtuKVa2lP4ul_TDY_rDJiVB_NxfOpU-Wb2JQFbTheWkwcmdR8NMpNV4iDBerNSXaJZWw1yuONCSkyoUm_XX4gijE5ybrvcPGOpLGOu4zV1Mu3rQ0OMp42Owaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودمونیم ترکیب دیشب ژنرال جلو بلژیک چقد هجومی بود.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78484" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78483">
<div class="tg-post-header">📌 پیام #21</div>
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
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78483" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78482">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v-5XwfVVenYPEDXYMpY_QlGXF9p7uTxkwwbQKO2UXmjP4Ql5cFAueufSVExOoPGUGRqVSOkPxILx6sh1kBUUVUaZHEJkBG9faGZNeWKi129NXjH_u21HpAbH5XpxScam9PvBYrtIldRxkZAzfLp-IePFp-g7v-B3J5AMPM5v_urV_EQS1F77VJ-UFXyk5URSF68O00m0Gri-rCliy0gO01Is3y7kvwdEATAAL9web8WmVGJ5Oo9A088tQv1C_hwHyd4zJocbyxddoMkeJst0lvl2uJeMFOGjzIA5_jO2juiI_gmNy-tBZas94ZvIfb3bmsL77kN7qTW2-yonhLKAtQ.jpg" alt="photo" loading="lazy"/></div>
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
G1
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78482" target="_blank">📅 17:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78480">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">رفیقم زنگ زده میگه ضریب عراق جلو فرانسه خوبه ها
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78480" target="_blank">📅 16:18 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78479">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=RUPZkR4H2G9eOchZHY3gjSbxjNAyvJqyOr7QJt0oqyZjONUU4DZnZg22J2ptuu2t2EMwBsKxdTUAlNGqXKwu6lNN4B0wX-GB7oxLELBwFTifp5ey6Fz6sq6XsR3j5IT0aUc3U-O_gA4xhmfraJ1-F3u_yFGwPEllQh6poA-i2_s4824zFcgBnWWFDMJwxDqodgtgrL3jJydanKV9qruLCM463J8k74jdQI3P0HxUiBallRIYtSn2x2FrR4mg025SPaelsspt1B6LbY7WC-BRaR9EBF1Ty7ne3n7oYVGfp1ttARDEISkaz9hLK8ugV1PUJlaKNahDcXYL61PUraDTYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbfa646697.mp4?token=RUPZkR4H2G9eOchZHY3gjSbxjNAyvJqyOr7QJt0oqyZjONUU4DZnZg22J2ptuu2t2EMwBsKxdTUAlNGqXKwu6lNN4B0wX-GB7oxLELBwFTifp5ey6Fz6sq6XsR3j5IT0aUc3U-O_gA4xhmfraJ1-F3u_yFGwPEllQh6poA-i2_s4824zFcgBnWWFDMJwxDqodgtgrL3jJydanKV9qruLCM463J8k74jdQI3P0HxUiBallRIYtSn2x2FrR4mg025SPaelsspt1B6LbY7WC-BRaR9EBF1Ty7ne3n7oYVGfp1ttARDEISkaz9hLK8ugV1PUJlaKNahDcXYL61PUraDTYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78479" target="_blank">📅 16:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78478">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">برنامه ابوطالب فقط اون تیکه هاییش که اینستا میزارن جالبه، بقیشو ندیدید هم ندیدید</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78478" target="_blank">📅 16:04 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78477">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">کورتوا حسین کنعانی رو فالو کرده، احتمالا بمب 150 میلیون تومنی پرز کنعانی باشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78477" target="_blank">📅 15:27 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78476">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پشه مادرجنده مگه قرار نبود فقط شبا نیش بزنی</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78476" target="_blank">📅 14:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78475">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eexm0QdUrdbq1A1epUwxeLTwG3D-dey1JFLAJM3pRlrsaP7BU6hHcb4mqG5RoTVqhTihbodBXJtHd-_BzVXW2DwpN4n1qzzOlepVEEJpHi28V8_N_Ng0af7PEVudBifajOVt14Zf3LuXXxHaNotkvUauBcqLuxDv2HLPA1hZAbn8krQinoFbBV5i_SurIY7ZvuVlUv5ZE0Wfddg4JsGD3NcUBaCdVm9QMQXlmU4cR51FcQ_hPB22qJjwwzRUF5wP3fd6CwUntmL5K5YlqS8aBx3sVmBYhoBg4XdLHhkxfWtA2ZfhhjsTi55FGsfLwTnAW1TCLjOUv2z6GgmD1EK0hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا اینطوری قانع نشده بودم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78475" target="_blank">📅 14:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78474">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">تو جام‌جهانی فقط در صورتی که دستشونو بگیرن تو دهنشون فحش بدن اخراج میشن؟ یعنی حالت عادی بگن کص ننت هیچی نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78474" target="_blank">📅 14:07 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78473">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qFgll6vjuT12FDzsj_BFZVO9vbLEmq-YwvjEh5wwRDASbnkNEkahla3w_mDmfK3CBMXfVATwK6Pc-qHn9fqj9yB39IcR80HXw_vze-Vw372GSFy2ruwJsr-tvs3SUuV4hLFB4_q-6Hgy8wu5oef-aLLpaZBLquH_o_VvzcB_g3p2a7H5URMFZ1o5tf-_uw4V1dW2g5hjOae910qEl6GVu2pFwYqsScelOsHNmAbZuW2WDAHjTEjVlWlJ-J1RnfCzw1bh7pOe0cc-HO6PlDObfe3YX0AbNPBMbVXohA0aCMspuhI15umya8jIx3dbwAH5xaQBJv8Ac7j4gvYCcuSQUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش کبیر از اون دنیا هم رفت
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78473" target="_blank">📅 13:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78472">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">با توجه به اتفاقات اخیر بنظرتون بهترین آرتیست نسل چهار کیه؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78472" target="_blank">📅 13:31 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78471">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">کیرم بعد ی دوری بسیار طولانی استعفا داد و برگشت پیش خودم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78471" target="_blank">📅 12:49 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78469">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78469" target="_blank">📅 12:32 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78468">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هر سری که کارت بلو میگیرم جنسش یه لول افت کرده، چه گوهی دارید میخورید</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78468" target="_blank">📅 12:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78467">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLKausBBJUet3fjgJ32o0BrXlXW51MWVaUra5H2RdX-8bka_4bAzH0t9bDaP-YQW8Y7H9IEbi04sFyRfhcMHy9OvnBmUEPoGLGUDPIhyb3ZgKtCahNXLMufu2yLg-3rIsRodtjjZD4o-OKn6WyLPVBtTchnhgxpkYMkMmZZUSCtNF-9ShcFVgV37eGQ2w9u1MfguKKzaEKkgLhK5gyhHrBSdYha4aBKG5HCgMIVwa3n4mk7S-R-x-QZDjJzOuIKFK0USfLMRLI9CatDe1IEjoM8x4gQ5m7JbvrUXJE4JAjzs527PDjo4pNnb6Gv60MLeTGtWWYWKK6DlRdf_y0UDfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصر هم بازی خودش رو برد و جدول گروه این شکلی شد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78467" target="_blank">📅 12:15 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78466">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hgA-F2ujDMVeWBV5IoWqEg4nTKwz4DyTGypTxkit-GcwFx97l33lg8fPlQrzLzw_f4X0bfvfQXDRYLiUuuVeAQ8nkBJc0Zqm5ZlgMEpFg0p_Su947akusJ-dFtZZ1sm40fNW65cC7Z7cj7dWzjsvNIxPgzCrjcr9Mhuja7ck1Pl4i00gLPvYKxgvDM247rgtbfn7yHkcG09gEj_ivSc69Vkv84cCZrrbhKKEHAAs9t78c8CXuh6pWGYxXcKOmS37iYYwA3DohBGR1d3GJanO_uTLt9_fVBWKw9v8tCmDoHdPcN0jVvTGSoaKXVgSa3cu98aRAQ6Ahq8xigaLmXh11Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب الان این چیه کیرم تو دهنت
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78466" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78465">
<div class="tg-post-header">📌 پیام #5</div>
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
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78465" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78464">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYVaxj2godLlLHQ7SBRX7-QDGda0P3SlRNR-f4b-WZ-POF7yVPvWoJYoOEdxmvLsMVb6k2FKeBbn7Bu7BOSnfBl1YF-ybehYA1f_LgjNvFh2pb2_QhguFt5S9DsOol0LS9nMU5SrGll0-f2XxaMPWwj3S6KKmDDyfVYTFHOgeRPeflPkGc9EQobsXNbLZMLLLWVEy9sZyYskE92duJtkSS_QFGiirCVYcIfVq3UKUMkq8i7ifRVHn63Lp4UDs7vihI1ttvJ5alufwtGS5Xhwve9n_D_YpYBRFGuBl9CiP479x4uoRKUfeOf4SgLnU9h1JWbFr8G9ieFXkRifMTlqEw.jpg" alt="photo" loading="lazy"/></div>
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
R1
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
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78464" target="_blank">📅 12:11 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78463">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NxMJUfdAyoEf_qXSZRhkq_eOF29rA42-Vz8kj0VW_Q0LAPqxsfm111Yk-WlihQJhoXE22Nk4SCWkjC489jFtcTlmh4gqBPuSpsKXYN-yp5yFNldXa-KjgATwjMV_rll94l-xrU4nWKiegY-yCPChn9xmcDBpq4Bq0Ua59-P3lqA5RTCg7uLtpO-wQFAXkczFcX47G36dqBbpEqm4_E3ZgZCSf6oTuDj5tgdfgyWXn1H_cfAoGMNvCrfrI44xc5LkHW4zksRLeoh-MeavB3dTPSKXefasXqEU4BajC0dH3IauHjcx8OawN1xkLti87Xm0wAf9VH5YFr3HEuVesMd9bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78463" target="_blank">📅 10:05 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78462">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z5oB6ulroSyNbpVS3Gw0neoQ7HLbfQ5ij_qwc9QZlI5PDPA5TlNymBd6G0rP_D85e-6YTfmzahPNu4QAtm4T5Nbgs_bzDCoaYHUunNIThZb0YaTg8KATj_q7WNmzsiLvPvpJue2sKvmaOA4N3MFCfEjpD_x5KmIbq-XzI9AgAanGvcw1vobg9OuUc3cr2PGvISqFRf9oaIumOOva_5PIBQUICRPz-VanPDMN3p0dKhshh0-PVRWml_nhKoJ_Okc4khglMF_tE8A5tJJu6bdB2137Kj9V_GKN2hR0P0swtiyOjiVQK0AOBo1SAHw9xQ4Z5NSxbklThUwMAGhVVpa75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رائفی پور آمریکایی ها ام استادیوم بوده مثل اینکه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78462" target="_blank">📅 03:47 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78459">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">از وقتی یادم میاد موسلرا فوق العاده گلر کسشریه
چطوری نزدیک ۲ دهه گلر فیکس اروگوئه بوده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78459" target="_blank">📅 03:02 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
