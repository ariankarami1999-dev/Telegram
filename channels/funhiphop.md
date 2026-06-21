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
<img src="https://cdn4.telesco.pe/file/jThnqugnP8x18RGiS_zkUPZ-CIXnZyJ5E0U1Ttm48i-IQSMFu9UTNoprDPgFhFvFrJW2CuEQiun-GUIwGaGS38Bzi0MsWxFX8kPjukh8hYGWYkndBBDj261BmquOY7_OIpigXFxCDbMw1YbNlu-fGZN_yoy3Mf0zWgx-09ZTkKmRmhXVOeNPJ-CePag0DP-GSmC7E1PG5ifMJeQIbIpESvkN8wO7kS97XQ_tLiYewIJlRI6I06LbAfUendvENfNZDtpVHhnpHlW8L3m9o8mVjCX2rO8I8pCeKnn6rS8BFOu3lZaQz1AgDscaBFr1vNWncuXjpEhrbRv9H_HqGBbANw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 169K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-01 02:32:20</div>
<hr>

<div class="tg-post" id="msg-78458">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هم اکنون ریزش شدید فالوور های گلر کیپ ورد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 1.31K · <a href="https://t.me/funhiphop/78458" target="_blank">📅 02:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78457">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">پس فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/funhiphop/78457" target="_blank">📅 01:55 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78456">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKJ3hUuyQiqLbGvrykJawl9lOS0b7MGIV-L0oh1Dzqu2VUVAuCZFRXxqoAD-nbQVtZ2p8DlAt9iDsuMLw_V2RBf7YeUqw7J7OeOus7dIA0whGqXSiaQoFf3XUHB2ZZJCGycIZzEvtxO54KxY4DYikqJ6N18DxNbGHMuE-Edt7ZXtbv7ALsOGdH1CnVlBDf8o5cszLDJ7lGtO9b4aYvY8tZiR2OpVj2xjdmk5z8ZX3kqpkx6UWGJsNNuHInMZD_Tom1gUJNihtTXXgd05Bxw88cZ0kIpW-b7u2cCPijEPdexCCnV8O6Y4r6wYE3VBIejAQa6-DYe1tjYIfUgUs9UJZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">و اما آخرین پست مربوط به فوتبال.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/funhiphop/78456" target="_blank">📅 01:46 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78455">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">الان بیرانوند هی اینستاشو رفرش میکنه ببین فالووراش ده میلیون شدن یا نه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/funhiphop/78455" target="_blank">📅 01:40 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78454">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W99mvx-eSGKBXGRVdGOaS2BulUv7L1PMZFpOCF5vQvN_5hGKCdiuvDTuF4ZF_dOg3ThRA1SMD0VmzrYsZb-CsCNCd0rE6i_EqxcdCz90h6gBQA5qL9_xAShfuxL-liWYUbDsv5j9_T1qmUdgIJS1xwboaiOBf4rqkByJAa_JS0NksZtyeLT5oBrn1fzUv1rCccL-fNLKdRYlwEeWtrjhlZBjpiu-7bBDlpRtQGCKAPvSvVvaoPzvlWls3hCJARlRxhFpDo9IzcU-3MbcrbVUbhZEAFVMUm9l2fGhRpaOfeGM8xhnZitC5moyqbCfAnDzpEP6GuWdcpyXNsHm_8uc7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید قالیشاه: ما اینطوری از کشورمون دفاع میکنیم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/funhiphop/78454" target="_blank">📅 01:34 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78453">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tDH3lWv76TrR7vyXU2Xq7aC3PBFM2LzdJw6eYTkG1O-S2T0IvXe4Z1tdOryDnnFKrYAOWWIO6KuofylYqJm502c0yLV8XFZdRHC96nZwpwQ55bgKoeuvmFjsTQ8Ku1fYDQzElAswtO0fF-XtZgrlYS9jO1E_LDa9vddYVNKZHtPG2wv3OS5-8feTkpHFxs7_iWt-1k4wJQTkeu4Y7AJ3NPnBriAcnQ2eYR79fbRBmFeFc5M720lcFTZemPKZxRu3BMm62vRJ961KebJ1GbB46YgcEaW30qyX1Vzs_BUo4U5CYqfw-nnS1D7shCeM1fJpIUT4gdy5tHnTeAK7LxtsGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهادت بده نویر
اعتراف کن بوفون
تایید کن کاسیاس
به راستی او بهترین دروازه بان تاریخ نیست؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.88K · <a href="https://t.me/funhiphop/78453" target="_blank">📅 01:29 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78452">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب کصخل کورتوا هم نبود بلژیک گل خورده بود</div>
<div class="tg-footer">👁️ 6.91K · <a href="https://t.me/funhiphop/78452" target="_blank">📅 01:24 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78451">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 7.33K · <a href="https://t.me/funhiphop/78451" target="_blank">📅 01:22 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78450">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ولی جدای شوخی واقعا مساوی گرفتن از بلژیک ده نفره اونم با شیش تا دفاع و ی هافبک دفاعی کار خفنی نیست، اگه بیرانوند امشب رو دور نبود ممکن بود باز نتیجه ای مثل بازی انگلیس رقم بخوره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 7.32K · <a href="https://t.me/funhiphop/78450" target="_blank">📅 01:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78449">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">خبرنگار خطاب به کنعانی: چجوری تونستید بلژیک رو متوقف کنید؟
کنعانی: رفتیم تو اتوووووبوووووث.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/78449" target="_blank">📅 01:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78448">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CHuXW1sEouqMqjSu6K10wqiqxXXOk2QN1ya1jTcM8PYI5CpzzyeZ1bu2Z2Djti7be_cccHU3X8gj3q2TYFpn_NS2YsSAqNGKDHf3yHdo5zseQXj8zt9D3PQDiO0USe43If2OXINxNH4YVB-O-7hFwHAhoA24sH5loN9z3an_vBLpIBLxwNIYW-ZaGdOcBaOvecLTGmxJyLYanOgr0NOH6a3GKEz04ubJvAxeav6tBK7jU-qi9mkpuB7fEm4HA-8MlWWiW4N2BOdFW47NwO4Lt3TKc5xtInUejRCSvVBQnvUoS_fsvM7UYjvwiHVLdGgv2RxDg-y6-h0twpRSuKztPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا شوخیو بزاریم کنار کسمادر بقیه بهترین دروازه بان ایران ایشونه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/78448" target="_blank">📅 01:06 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78447">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lovUydjRVLvqQuLdbjMlwvT1mBwhBaa1ZKrxuMerDi71JbCWiwcuBxs5Am5hMNSBkcTvRXkWqLhKGZeKlnhAigVunlSDVsawwAi3-pAAxTw5JmLoMyvY0DY1uL7jTb7WCr0rvTtFNsYYPumKI-ZVRksCy8eScWNtB9VbCRAobT1lmhyhE1b-EqKc4-SfMM3SWUBV_qah3zBNdyABSgJ5cx-hhTqBQzPMf7Eq4WAZFKuSCJxIhBc0lkIONc8NX4GBEnauET6XrK-YUXP5_pJlmccjNDE8ALpAa0E1VKT89nMvMAbxaZx_2MPWmRi4gJ0sX_GFvQg_TJalBcRaTFtKYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/funhiphop/78447" target="_blank">📅 01:00 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78446">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_gV_wpyuqhaY-xWgmfdie7dM-ICHoE_iSyBJQ6RDVk4Qfc3_0XCcKmNCQ_dZPUJDCpDRVVymmTcX-LLrQ6VevotVnX_MHQjzdG8m83Dgck6hMSLnzlwBHwF5gHe8nAw1Iybs5BIVIXWvWJpkWstaaSVVvDtXvnAz4p66yzgxwaqsh_PWoJR3vFhhgUfq5uqMuzl_o6Um4p4wO1PKaRvBgHj0bE9BCwBh4Kf4MD5CErnlOr695NiGyqoBClT_HfiOx2YSwtF8UKDmxUqBAywViUJ4qbg6lCacsank2m2786HXmUF8ha7WOH_Zm0vl4fnxZLhTf5Dt2IfMBmuAT69gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دسخوش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/78446" target="_blank">📅 00:54 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78445">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMmOYmasKJ0EIOHkOk1dqcTPmyd6v7F-1R35wMHWS05EAo_9FjoNrT3hCi_6q58XpfSJ16-74B7PAGjcM2cumOZbhs_2Y2MiCS2om92FkJiGtUdXGzT0L1asm5KlQDCq_bfG0V9H2Js7f6PPcK8Gc4CEXTLD-taQpcA4H834GVd8aGP5iqSkNvTbf-aXn6srXRql6STlvWlyj2_HtnWfIsSVyxmYelmAoKsEDBEypNHdZ7AQmE_wmJPhhdEdwrTCMh4N5aZppgKVJiX9LCDdVIGrqvwEBEY19QNuBXTOMok966i8b2Y_XpX2j-awfGOtIHFg0duRn1qeKHZL_ohaSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/78445" target="_blank">📅 00:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78444">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">نمره بیرانوندو  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/78444" target="_blank">📅 00:42 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78442">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HoAgfJF72XrHTUy6hwwA7B5DjEU9fSZc6o4NDKo9ONLgTkBjC8Geso_J2zOYsRxFz8jKYLKibRvkh_Oe1PFA2cSg76tPfbLmNsCwoyaEV06I3j3JCAoqMrAyM5lw2YMaNj7P5ua4n_vwFLj-WKHBbGV5M02uhtcRn-KyboPjbhrsfLIKoP7muK7FrBLfa5UCMTyN3kFQ78T3M_ANP5RKJ0p0L40RcXFcGqxmbgvLD9IbcZE0HtSp9fvGRe_OCCB9qcQk6HZ7ANFx8XhHtLvlMw_AIyY97SAFnTdZ47h5_P9BKo-OV5ZLdLgxa9wYF_IA0l25I-zGqWQAGMQ-3IRKjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمره بیرانوندو
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78442" target="_blank">📅 00:37 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78441">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">یعنی الان بیرانوند قراره ۱۳ میلیون فالور بگیره؟</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78441" target="_blank">📅 00:33 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78434">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=BEbAfF3XAZJUPFzikW9KxbA4yx321GEZTQdzXiCoMf-JIr73k37HLsZKAQktSj0WIb32nhQvY_VmzT9OsYaV07BYJMcDmOZJJLGCWQNTqnkX_iWLan0XG1UEQdhvBXaB6TaDir_rmSkosrijRqbDTO2G-xFX6_7HWN6ovxw_uOw9xgWZBRza1ynJicuGUKhBEPFUyU8qxc725yyFZ1g0-dbcNTlcddzO7qKFkXJcolu4Ti1Cu3RWG1fb_YrCPHzrdyO2MTrs4y1Ek9oAY_vJpK5R1WhTBeVu6kOfXBBMy7OC6blLRyj9RufxlQWHpInh7F406JL9m9-JMulQjBNG4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/25a83c28b2.mp4?token=BEbAfF3XAZJUPFzikW9KxbA4yx321GEZTQdzXiCoMf-JIr73k37HLsZKAQktSj0WIb32nhQvY_VmzT9OsYaV07BYJMcDmOZJJLGCWQNTqnkX_iWLan0XG1UEQdhvBXaB6TaDir_rmSkosrijRqbDTO2G-xFX6_7HWN6ovxw_uOw9xgWZBRza1ynJicuGUKhBEPFUyU8qxc725yyFZ1g0-dbcNTlcddzO7qKFkXJcolu4Ti1Cu3RWG1fb_YrCPHzrdyO2MTrs4y1Ek9oAY_vJpK5R1WhTBeVu6kOfXBBMy7OC6blLRyj9RufxlQWHpInh7F406JL9m9-JMulQjBNG4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تاکتیک ژنرال برا بازی امروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78434" target="_blank">📅 00:23 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78433">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">امریکا هم نمی تونه این تنگه رو باز بکنه</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78433" target="_blank">📅 00:21 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78430">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=og4xVHmCL3JLRCLtyU-Ax1Rzo4MhIPrkvg20HXI7lwqC_uJUReklFz5mevc7DsDGoqlhlr9nE4p5wpkq4J9ZdmllWJ7pCsG3rT-wWERVAKMxiotXuhC0-9tWGiQkyTrR-JOxEJBH7gI9H5t_cdJeM0pXjl_KMkbBRNHNhwbvJmiHROOvK9gTXdBaJVRbeJYN282bxHxhOc0eHT-NaPVBlSYYF1cZ625ZddlXiNkuhu7QRPp2Nqtb5sKdzrCR2LcwujZ5kPqU9g3wp3ajMAJk1FpPlkdGcfEhbJRVFQ0GwtWL8uP9eiY18l_H5rtU6d8YJ-2_vMGwMCWNeDjjkR_0Ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d6215a59f.mp4?token=og4xVHmCL3JLRCLtyU-Ax1Rzo4MhIPrkvg20HXI7lwqC_uJUReklFz5mevc7DsDGoqlhlr9nE4p5wpkq4J9ZdmllWJ7pCsG3rT-wWERVAKMxiotXuhC0-9tWGiQkyTrR-JOxEJBH7gI9H5t_cdJeM0pXjl_KMkbBRNHNhwbvJmiHROOvK9gTXdBaJVRbeJYN282bxHxhOc0eHT-NaPVBlSYYF1cZ625ZddlXiNkuhu7QRPp2Nqtb5sKdzrCR2LcwujZ5kPqU9g3wp3ajMAJk1FpPlkdGcfEhbJRVFQ0GwtWL8uP9eiY18l_H5rtU6d8YJ-2_vMGwMCWNeDjjkR_0Ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سطح ایکیو اینو حاجی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78430" target="_blank">📅 00:16 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78428">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سیاه پوست فیکس میذاری همین میشه دیگه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78428" target="_blank">📅 00:03 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78426">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بلژیک اخراجی داد</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78426" target="_blank">📅 00:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78414">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQSyDIX-MGij956PvVtDsy4w6BwlSmd1nBKMhc1ADQ7xKWLJ0YssJQ_we5_pTsdPmPmEheEkvM94F8cGrl5Ktu2pDxx-n4J-IHW5YkIjabl5hkX9RoSDPcrGu0XaHUbUZPP4acmzz5HpzFac5lIGPP_1FCf9Q4LQdyGII0HQB-nSOXO6hY9uwOVseWGVk00obyZ4NlHBA2bSZmmSQMXMz2CZKOnLnfBQKLgq0XoLtsIJsmGEHoh5_lZf9pFeujqjdwNEJK4aEXJ2TZ-wcv8CTkHqNRcQQgwsFzF2GIr0h-HyDd68V6s3Qdcv_pTdwZ1qGxKkry2-JfHocCcSxIOxrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر تماشاگر ایرانی
رشید مظاهری کجاست؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78414" target="_blank">📅 23:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78412">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78412" target="_blank">📅 23:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78410">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دیبروینه سوپرگل میزنه و بلژیک میبره
بماند به یادگار
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78410" target="_blank">📅 23:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78407">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">عباس قانع راجب شیر و خورشید: پرچماشون فیک باشه ولی دلشون با تیم ملی باشه اوکیه</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78407" target="_blank">📅 23:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78406">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78406" target="_blank">📅 23:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78404">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">من کاملا فوتبالی از این تیم کیری بدم میاد</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78404" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78403">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">فوتبالو سیاسی نکنید دوستان</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78403" target="_blank">📅 23:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78399">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">آفساید شه کون میدم   @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78399" target="_blank">📅 22:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78397">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آفساید شه کون میدم
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78397" target="_blank">📅 22:56 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78392">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78392" target="_blank">📅 22:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78390">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گزارشگر آپارات اسپرتو فک کنم بازی تموم نشده بکنن تو گونی</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78390" target="_blank">📅 22:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78385">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">بیرانوند همانند شهید تنگسیری ایستادگی کرد تا تنگه رو بسته نگه داره
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78385" target="_blank">📅 22:36 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78382">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">بازی تیم مردمی بلژیک هم شروع شد
ببینیم چی میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78382" target="_blank">📅 22:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78381">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نتانیاهو:
سال‌ها به ما می‌گفتند"نمی‌توانید به خاک ایران حمله کنید."
بله، می‌توانید عملیات‌های موساد انجام دهید. «ما هم عملیات‌های زیادی انجام دادیم، من هم تعداد زیادی را تایید کردم.» اما نمی‌توانید نیروی نظامی‌مان را به ایران بفرستید.
ما این را تغییر دادیم، ما خلبان‌های شجاع‌مان را به آسمان‌های ایران فرستادیم.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78381" target="_blank">📅 22:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78380">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔴
رفقاااا نیم ساعت دیگه فوتبال ایران تو جام جهانی شروع میشه اگه میخوای بدون سانسور بازی ایران ، و دافای ایرانی تو ورزشگاه رو رو ببینی چنل فوتبالیمون بجوین عشق داداش که چاشنی جام جهانی همینجاس :  • @TrollSporte • @TrollSporte</div>
<div class="tg-footer">👁️ 9.81K · <a href="https://t.me/funhiphop/78380" target="_blank">📅 22:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78378">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ddRwf2Bi0olF518yDfe0jwPd0VnHluOetZ9MX-0KPJvOotzt7eS9L4y2uUabVTyUYtmYaYQHFVr9XlUZ3b9Nnn55hC9E35ESxs7cAHPhXLwT7CmfCsTYY61n_ojT6e0Z7SMqqHfz-pFI2Xnd9cdbiU_3m7_dhu-Lo9BSyp941ajfEOTf0pUYs5CHH0Js71T9Ncnq5fkL5CHKR5Q-2I2pCmpZ633mDWzokS2jEkWXrKwzPK2fFHo30msdSYIV3BgDI_iso07zHgHF_smY5XEQZHG5Qmib_v9eS_RPIKSYKPM7gTbyqCuJqn9hCaXjKo91gtjFjM7SqVnSjDtKbvxnGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
رفقاااا نیم ساعت دیگه فوتبال ایران تو جام جهانی شروع میشه اگه میخوای بدون سانسور بازی ایران ، و دافای ایرانی تو ورزشگاه رو رو ببینی چنل فوتبالیمون بجوین عشق داداش که چاشنی جام جهانی همینجاس :
• @
TrollSporte
• @
TrollSporte</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78378" target="_blank">📅 22:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78377">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bzI61nHuUPbY1w0ZrDcACknVqNEVw12so70EA9bwvin990PBk9zCDoT3W7qSWHmQldMy_Nq5OwG_inBpKw0CdObd__OP_8L7RkSxc7BdLBCp5Q8czAosCkET1ZoSqY8KqQev-DE7SAuSozY3c_ptDgODLdKw5AwAMqLwvBHgN_CUAb4ZR1HI45XlOwXSFHhRKBblfvvNeU42Lw5DTHQUki_Fv_dZJdY0z4GzINL8nXFOG5bMTWeaVr0WJPanBr-FTkGcTekiEgP4QP_fq1gpJZOoC_ZP-OlIizlZ-4EXrYgZFJaVTNkUh37KhvjcnuEhY_fxgwDDOPpApp84uO58EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.64K · <a href="https://t.me/funhiphop/78377" target="_blank">📅 21:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78376">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">رو برد مساوی ایران بزنید پولدار شید</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78376" target="_blank">📅 21:47 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78375">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A5sZ5Qn9wOzJA2flSvYZxFSC8qotPGo6BguL72_1n8eXwGbNoyBE6vAb_vki5WptDSQ6beSLScezkOnX-D9v26xN1CnHNrt8E_bCan3J2OPR_OulRWqLdIDjftZmyybRQBYNBYn2hWt2bVmeN_UOEzUMcjdshyP7qybpJ0v-t8Y3rgNklXBRh9I_7znM85v7fD3EZ_jOzLAgdM4snkeIomRQseN1fjW6AoMy-znw6kicAv4dCkNmDYVkf0G2UAaVOwKIh-SGsHETGbn_Dy3Mm9r8Alc5oHyCjg2DSZbpFvyDmo6uRHPyd16GuJxwYH00XU9Zt4vEaYAh9RuYPyJzxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال کاملا حجومی چیده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78375" target="_blank">📅 21:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78373">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">امضا میکنم که نعمتی امشب بهترین بازیکن از نظر ما میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/funhiphop/78373" target="_blank">📅 21:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78372">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apptZspT7Qh9NG6syvFTNCI3nhbCxlVJxlC-AIp_KRjh2VHuEf122LFnhQUd-SiMyIecjH7nKOzyccx8KdT-pzS87mNbb80QYz-Y_XH4NfWAAtL4ZWsuEqYPGHEW54miKx38zmpXRZlFYjLjBuQhvWIRmjM6wdS8d_p0gKdpcfXgOOgmDHTkdXcXaK2hEXeuaOZF3ESvuEuh_D5NSkKY2Gfg7jLdS_5G-JinDIE0z5NWk4Q9Yubv6D1EoM08BZw-ZAFDbVhlMwj7LeXhVdwrr-FEUOJX6pUgUP8duPCd3X81pLX-WGRhOw8bCXJ7JqXxH8IMmOMBNXgD_UGmiTXEkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب مادرجنده ها اومد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78372" target="_blank">📅 21:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78371">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ajpe-XycEV8tphlX5QUgt69r4EJcyLLhCxrXcS-qwYrAVbB1kTZmg_UCssVdBupcHmwPqqF1Jp7Uiv4fiwYy6ik8kt1wk4kKgwPGA2mpW-rzwvVThRWa-dVkks--LYrLBTPTTE0WnXJIIyJWZoxfJCHVmgYmd6hHkUt8zHnK19t9Td4gsF4IJZGRNROV-LLqKSuMsZ7cBEwj50Ppdu9-pjh9GOiq5-q9PhWDpfAuE7-BWjW2EzUPbYHFbucD2KGSwWLRnFbQ80oBwoyx3IXYVtEZkhYUaLVedp9fiWvzgoC5W6w_kTVg6kMhXeMNX_hvTI6Pl3Vyre59YG2qCFT5xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محرم ۴۰۵
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78371" target="_blank">📅 20:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78370">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=Mi6VVYrbvIWVXCvgI1hnrmfuDKbXGtc00qkxEhS1g3S5FnwS4O6DQqPgdjs8rrPqU4ZSM3V1qyN4QX15-OLMz2y1IKHQ9NdRHkErVkdEoxACB9KbjLuKdP3OgGoCcJqk7ezdju33EXD0qTcgKSClLIXgrsZka6RqKteGFD1JIHaS36nGV3ATI--TjUYv-rJJIu4uuXd8aCQSzRmRwCHi7b-I2JnSkYDuJ3njjpKSejRB8vFiuN_qJVvmy4ZuDszA-zbo3ulK-NvJHFDUAry9nAiuvw8MHM01vDUwExu8uoOk9XNJ1eXAInBMvUHrVOLPDejiRgYMsI-Tae41lzrvLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca8a4c0df7.mp4?token=Mi6VVYrbvIWVXCvgI1hnrmfuDKbXGtc00qkxEhS1g3S5FnwS4O6DQqPgdjs8rrPqU4ZSM3V1qyN4QX15-OLMz2y1IKHQ9NdRHkErVkdEoxACB9KbjLuKdP3OgGoCcJqk7ezdju33EXD0qTcgKSClLIXgrsZka6RqKteGFD1JIHaS36nGV3ATI--TjUYv-rJJIu4uuXd8aCQSzRmRwCHi7b-I2JnSkYDuJ3njjpKSejRB8vFiuN_qJVvmy4ZuDszA-zbo3ulK-NvJHFDUAry9nAiuvw8MHM01vDUwExu8uoOk9XNJ1eXAInBMvUHrVOLPDejiRgYMsI-Tae41lzrvLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهدی رو برد یه تیم میبنده
بازیکنای تیم مقابل روز مسابقه:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78370" target="_blank">📅 20:35 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78368">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">ریدم قالیباف: تهدید های ترامپ بکیرمونم نیست  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78368" target="_blank">📅 20:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78367">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">اویارزابال هم که به یامال  ایرانی پاس گل داد اصالتا اهل هراته و ریشه ی ایران باستان داره
هرات استان خونی خاکی ماست و به زودی به خاک مقدس ایران برمیگرده مثل اربیل و سلیمانیه و …
دو ایرانی اصیل کارو برای اسپانیایی های آریایی درآوردن
برادر برای برادر
❤️</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78367" target="_blank">📅 20:06 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78365">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">آرژانتین به عربستان باخت و قهرمان شد
ولی اسپانیا داره به عربستان تجاوز میکنه
ینی قهرمانی اسپانیا منتفی شد ؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78365" target="_blank">📅 20:00 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78363">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">مهد اسلام داره فرو میپاشه</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78363" target="_blank">📅 19:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78362">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oz-6k0yywRtmlGRpPEauhSqiXRlAXmJkXdrHdsQiXgZFep75Ebx_XM9aUKWOuJG-bRb-KHxzmPuRBk7sPFrPn92BZxf4nw4EI5Yl68WlxzCfezk6nq89OD0RqCwDPaai3YnqFFW6nuyFsrtSG6wjE3ByvtvGeoKACQuLRR8UCTNO6oCAeHhsJeP6NHwKTVWSL5GGSvniFrQQ-r1s7Y3tFFdRmbOP3FXEhRMomW8uLLFYtc7iORL1TCYk0dWAa3ceXSbXOK85QdJSSVwsp1z36-SmdSF1RFCQuG282V6ZmDTMGEUhw8LdJUbgelBtVNMPUfm43tp6qOCumF7CddZx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
قالیباف: تهدید های ترامپ بکیرمونم نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78362" target="_blank">📅 19:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78359">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">نتانیاهو: تا هرزمان که لازم باشه برای حفظ شمال اسرائیل توی منطقه(جنوب لبنان) میمونیم و همچنین اجازه نمیدم جمهوری اسلامی به سلاح هسته‌ای دست پیدا کنه.
ما از جنوب لبنان عقب نشینی نخواهیم کرد و هیچکس نمیتونه اینو تغییر بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78359" target="_blank">📅 19:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78358">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🔴
عباس بیا بگو چیکار کردی چه سوپرایزی برامون داری از مذاکرات
ترامپ به فاکس نیوز:
شاید کنترل تنگه هرمز را بدست بیاوریم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78358" target="_blank">📅 19:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78357">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">کونکشا دیگه زمستونم که مدرسه و دانشگاه نرفتید، دیگه دلیلتون برا تابستون فن بودن چیه ناموسا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78357" target="_blank">📅 19:04 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78356">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">اووووو رامین رضاییان
🗣
🗣</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78356" target="_blank">📅 19:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78355">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vX0VAeuBavhOh_jupEEAikwDHxHRiX718hATf6oe64MYu2-Y1KWBQcXYXw8EbPaqfIHSbTNBHfNu6U2wUnkdxK3BsFVCkypUbw05V8FSp0Xwu14_DKoBa112DIegnMXbUne_hYHxnH9-ipMaOAmatdYEqvZyFh2OqHzzEttbZ7I8T4Sm4mg8PEkXNwpKGNx5pYwN2K0-FFP2qIiG9LnzttjUBlw_hq_CI_VSqSsyleGaNh5Q9rElwzo3XWsFFrhOs3wu8y0hcoEomd7QAa9f-f3cSUQREdC8UHIouz7iOe6z2aiMe1tfnx1nJ6LjsCLSdBiYlvNQUJZbG2DjgRvirg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شده در بازی آمریکا و استرالیا
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78355" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78354">
<div class="tg-post-header">📌 پیام #45</div>
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
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/78354" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78353">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHYIAW1SSFeFwxeabBkT7qcbkKM4RG-OR4FR3-cv3xJHhcXmuYDxQIkSRH7pJ4KAp47cuwR_ytdYmrYcQ03gfLy3JSKiMwsuR3iBVEuDvkYVZUUV028FOjFsenAwhgxYYT7m7P7tSLilBep2pDoGnzbEhQMEqZVLQX0Hs8njVw94cRW6eKVBKiZDpmX9lCCc_lTbPpHMKPi_RpWJDb3GTI-R5uYXrh84JSFQc3F7p7N2Os-ruVW31QcFM8kNPbE19q9zFNyvP0CECv5_gYTV8IczY-fiCqQTtCUr_0Lah9UN4B2DfnmguTGPrzSAT40VDf5Jq_lVNyIPgIqcEd_ngQ.jpg" alt="photo" loading="lazy"/></div>
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
🅰
g31
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
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78353" target="_blank">📅 18:58 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78352">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">تحلیل فوتبال با سامان ویلسون مثل تحلیل سیاست آمریکا با مرادویسیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.35K · <a href="https://t.me/funhiphop/78352" target="_blank">📅 18:52 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78351">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">مطمئنم که سر مهریه به توافق نمیرسن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78351" target="_blank">📅 17:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78350">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامپ:
به مذاکره‌کنندگان ایرانی در سوئیس گفتم اگر تنگه هرمز را ببندید ما بقیه کشورتان را هم تصرف خواهیم کرد و حتی کشوری نخواهید داشت که بتوانید به آن برگردید.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78350" target="_blank">📅 17:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78349">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترامپ: جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78349" target="_blank">📅 17:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78348">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91dac02670.mp4?token=bpVIuiX-HQs1m1jM5EAgMv36Hv0J0hmaGMBqbhxpLInQKSNgVOl0QzgpOzZUCLMOrsfYX4E5iAq9lxhdAEckgNRI1Nzep4wdXg0mDN_K7aQV_xandeEDo8exoklLI96UJh-Ctg3nVv8qKe_P5ybL3jfwAjqOtrbCG97yWUm2_kAVnvoHeMyChonbktcxBusGZUvIGUAQC9oykFasRGwroFfX5pnNf1IRYlbbPS_CdScRH2BULyB2l9uS7yKqhvmCjbXnaXjH-twcfHLhN9IqUYrCLkN2NHNSXG8VNEcuMC557JO56l-0UzyKU6SqimQ8bwAOJfoeYRiwEG37PQ5d-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91dac02670.mp4?token=bpVIuiX-HQs1m1jM5EAgMv36Hv0J0hmaGMBqbhxpLInQKSNgVOl0QzgpOzZUCLMOrsfYX4E5iAq9lxhdAEckgNRI1Nzep4wdXg0mDN_K7aQV_xandeEDo8exoklLI96UJh-Ctg3nVv8qKe_P5ybL3jfwAjqOtrbCG97yWUm2_kAVnvoHeMyChonbktcxBusGZUvIGUAQC9oykFasRGwroFfX5pnNf1IRYlbbPS_CdScRH2BULyB2l9uS7yKqhvmCjbXnaXjH-twcfHLhN9IqUYrCLkN2NHNSXG8VNEcuMC557JO56l-0UzyKU6SqimQ8bwAOJfoeYRiwEG37PQ5d-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ونس یجوری نگاه میکنه انگار اومده قرار دعوا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78348" target="_blank">📅 17:14 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78347">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دیت جمهوری اسلامی و امریکا شروع شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78347" target="_blank">📅 17:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78346">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ترامپ:
جمهوری اسلامی باید فوراً جلوی نیروهای نیابتی پردرآمد خود را در لبنان بگیرد وگرنه ضربه خواهد خورد ضربه‌ای بشدت سخت و طاقت فرسا
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78346" target="_blank">📅 17:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78345">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aSyEJTBa_CxP4gmTfgsKNVhfGOKLGrpHMefL5TOywO2Q5c2JxXw7alwf29Z6wNGtgaK1RXrUKEGTjBljVEyG8EPbrr_t0ipwaEv8783kVAQxHidsJt9-OYifD4CnxOBVsqbpkE9REdP2fnBAas1jzApWqsO0QRtSj5cxj_MWgxsd1BczqPD082aiMyVhK7K4UN5lKVDQ6OGQymidI6OWhwAJPqVDJKbgDmxmR4NZrM1Vv6sVA2DDQUVVm63lGQo6CgvcpT7xrQcETX3vjXhR0bs8TjIedgnHodMpFDj5617GQooN0XG0XOeAwqeGVTjkYP9Q7QyukuAltJPKh3MJaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت صادق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78345" target="_blank">📅 17:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78344">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">عباس دهنت سرویس سوئیس هم بگا دادی اخرش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78344" target="_blank">📅 16:49 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78343">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=E42ANPnphn5nsncofxy4StYCIhB88C1qG9lON8JmAn6Ew3Rn0yEeqqd_KophCFFBW46tXXnLoMkS0xOWZ6yhDwY5maoUKY8EW0gU00Lj4JLkr6WISTHi068Wm0gZDDnOkVzoQgIEWfONXUYleohPNB5aWyG6pW2zYVjnkUyHmVuNId8wJZl3EMZg-p1UFgZueOQrvB_4jwbB4yByaCIW7kZRFaOS-p4OGiRn2nN1hS6efOQT6DVcEKDT2toV6DNCHhG_jkfogRiAizkZnO5CgtxQvufjVKQ3TcGR7viYczEr7jL7tDXZtFpDqWyxYRheTM7MVcpUulidRd0wc5FQkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60c4bf1909.mp4?token=E42ANPnphn5nsncofxy4StYCIhB88C1qG9lON8JmAn6Ew3Rn0yEeqqd_KophCFFBW46tXXnLoMkS0xOWZ6yhDwY5maoUKY8EW0gU00Lj4JLkr6WISTHi068Wm0gZDDnOkVzoQgIEWfONXUYleohPNB5aWyG6pW2zYVjnkUyHmVuNId8wJZl3EMZg-p1UFgZueOQrvB_4jwbB4yByaCIW7kZRFaOS-p4OGiRn2nN1hS6efOQT6DVcEKDT2toV6DNCHhG_jkfogRiAizkZnO5CgtxQvufjVKQ3TcGR7viYczEr7jL7tDXZtFpDqWyxYRheTM7MVcpUulidRd0wc5FQkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بوفون و نویر وقتی میبینن نیاز نبوده ۲۰ سال کون خودشونو پاره کنن و چارتا سیو جام جهانی کافی بوده:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78343" target="_blank">📅 16:32 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78341">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">پزشکیان:
نگرانم مردم ناراضی به خیابان بیان و اعتراض کنن. اون وقت ابهت ما فرو می‌ریزه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78341" target="_blank">📅 15:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78340">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اگه برزیل با درخشش کونیا میتونه ۳.۰ ببره ما چرا با وجود اینهمه کونی و مادرجنده نمیتونیم کاری کنیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78340" target="_blank">📅 15:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78339">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">پزشکیان:
توافق رو گردن من نندازید، تمام فرمانده‌هان قرارگاه، سپاه، ارتش و امنیت در جلسه شورای امنیت ملی با توافق موافق بودن.
دیس به مجتبی خامنه ای؟
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78339" target="_blank">📅 15:39 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78336">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دوستان یه نکته ای بگم
مجتبی خامنه ای طبق بیانیه ای که داد گفت به اصرار پزشکیان این تفاهم نامه رو قبول کردم
نکته ای که وجود داره اینه که حکومت اگه یک درصد امیدوار بود که این مذاکرات نتیجه مثبتی براشون به همراه داره به هیچ وجه اعتبارش رو به پزشکیان نمیدادن
پس نتیجه میگیریم که این مذاکرات صرفا برای وقت خریدن هست نه توافق قطعی
ممنون از توجه شما به این موضوع
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78336" target="_blank">📅 15:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78335">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">مذاکرات تو سوئیس شرو شد
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78335" target="_blank">📅 15:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78334">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">یه رپرایی با معروفیت کیرگوزی میکنن که سر جم ۵۰ هزار نفر نمیشناسنشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78334" target="_blank">📅 14:51 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78333">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن    @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78333" target="_blank">📅 14:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78332">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ولی خب اسپانیا چون تجربه ندارن قهرمان نمیشهط آرژانتینم چون بیش از حد تجربه دارن(پیرن) نمیشه، تنها تیم معتدل انگلیسه که اونم لوزره</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78332" target="_blank">📅 14:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78331">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هلند بوی دوباره کیر شدن تو فینال توسط اسپانیا میده</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78331" target="_blank">📅 14:01 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78330">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">ژنرال شماره دعانویستو بفرس
تروساد هم از ناحیه کتف بگا رفت
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78330" target="_blank">📅 13:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78329">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">نصف بازیکن های اصلی بلژیک بگا رفتن و امشب در دسترس نیستن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78329" target="_blank">📅 13:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78328">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EMX8snf924bHHaELF57pNxDUWxkrxlSptiI5mJf5sRQ3YuQ2Sfb5C3Rz2U8mQKFE1sF83rqYcrWFESx64lsR3SbJH9mkYbT_LFQRNXOXfmP-HIdvud9uSYLuPLvpiHjM0thIm6tGZj78S1X5SkWR2s_ZhRPRPGgOnhkhU0Qqw3_Ck8TJ2rU6vTwMzwvo9wFG2oqehP7t07L5A98HA6HddaUxbAKEm84iu44mRJix_xBaSmw9hiqlW_VDbl7UgqIJu1KlY7dU7FsUWoD9JBYKt3EI8r640-N1eTPkWH0xdHrPAUh4aIXOCV2ivTa1gJ5ju0M-4Yhcqy7EttZYAK6nfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرچم یکی از پر افتخارترین تیم های آسیا در بازی دیشب
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78328" target="_blank">📅 11:41 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78327">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_eVU-O5CVGPRJYHRGu_iYz7UVX-RolXKX0tNDKxb91Yo-16mkW6tFEvN8eBQny4ugw6yjYCujezgqZFCttXPD28A7BmzxsaB0tLL0mKcQKjy9GX1v8_8q7kzyeXmP2bLNhg6isbwgoozs6czjGDu7xucuBgrtlv8ib2GZUXOIJ9_7lltjh-hf_N1HDdPCxI8G6HOBaaZK2t2rdqCVkridq2YBmy2png3TsD3-g0cSt4cvISUxZYxJRe0GV-pr1rekr14-KPz5aqyIni97Qyy63OxIA2x5mcoKOB_QZS2TybugG7jrlqc8AVwjWVcutlkk2jWjgZ2e9DiBAaURO9Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ژنرال توی یک تاکتیک پیشرفته رفته عکس بازیکنای بلژیک رو زده روی دیوار بازیکن های تیم ملی تا امشب بازیکنا تو زمین نتزسن.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78327" target="_blank">📅 11:15 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78326">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ICxHoT_VRgG6PBiXylqdaLSnEzSkW_Z4VTX_lnEX_DJrUOAzy6N7DiyzxIxIQ8JpUJu80vpsRIINyWQev125RMiyPYzbzs_iKfatC0qbA-7QKNbLhK4vUn30oCC1sjP9U8OJu2UJmSqiPIihAUJG3bao7UfU-GzvDVT0X_r2AlWjUWRvL8UrcO5w2dHQ-kId85R7ONxpZxI8z0Q_ZYUolSaJ3_ojueQWskEpPDeL-J8AitacO9RnzMOHGLGwytMbnS8jxYEFaN8I5_ymwysJ-39DHQthz1IRETTWQLGtHk_tq36rUARs5vsfaNQy7GKnZ8adyhMuNK9HU7QGkzYsQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنظرم رونالدو از مسی بهتره، چون ممه های زنش بزرگترن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78326" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78325">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
فرصت محدود
🙂
🔤
Winro.io
🔤
Winro.io</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78325" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78324">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVaROHDV_BLW3JNB4i2h7nuniJnPoCky-RDx_B2nDqBS6W2Hr02GgXqzX3XbwqdBnZLqjRaqayQ4RT3fEFX3Aq4fS_na84XJVOF0S_-JiSn4WKCHQ8czVLyhiTapqv4bySWN5T4daCwdy_1iBNBDMT-M00B9V1UO5AuMBLQf3bwceiy05FQ9aRe7eaOACEpaAlJskAocWrni_Vpx2LPSVNoM2gew0boOTR4kmdS4hPr1RKIYByEgm_3kF0OdRDKs4h_2gfSDsVDits-K3EYPmXqGBx-GH7ZjkJiTvorbF4yoj_cjQDkcRofpHn_7N-YIMuZkdDoCwiSqND3FK5G8RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
پیشنهاد ویژه فقط برای بازی ایران
🇮🇷
- بلژیک
🇧🇪
🎁
🤩
🤩
فری اسپین رایگان کازینو در انتظار شماست!
فقط کافیست حداقل
🤩
🤩
🤩
هزار تومان روی مسابقه ایران و بلژیک شرط‌بندی کنید و
🤩
🤩
🔠
🔠
🔠
🔠
🔠
🔠
🔠
🔠
رایگان دریافت کنید.
⚽️
بازی ایران
🇮🇷
vs بلژیک
🇧🇪
💰
حداقل مبلغ شرط:
0️⃣
0️⃣
0️⃣
0️⃣
0️⃣
5️⃣
تومان
🎰
جایزه:
0️⃣
5️⃣
فری اسپین کازینو
⏳
فرصت محدود!
همین حالا وارد شوید و شانس خود را امتحان کنید.
R31
🅰
❤️
Winro
هوشمندانه بازی کن، برنده شو
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
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/78324" target="_blank">📅 11:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78323">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">کارتون فوتبالیستا تازه داره رو ژاپن تاثیر میزاره</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78323" target="_blank">📅 09:09 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78322">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">این چرا جهانی شد  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/78322" target="_blank">📅 09:07 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78321">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTA97I4Qp5msM4azvF25FPfbcixURQ82-_761MDyst7gQX-GaPIV2aA3G9Db3mz7ee32DHc69BiNBOfNGd0yVOFtDjNoGoKPSr_AMx_dcN54p2V9x9idxZzec14DPei8nqSxFW9XeK8kjdQGII93IL2Djal9YC9-D6_5dsiZ6n6tH4A612XiHI41mzgfPLqKrg-RZjlLd_92lJlqUOH_LckdgruxvyZLZKXKzCvGX2feZut8LtT-kkqORqfg6U-uD8GEjaLMMW67zNC_TSdsnNeIvwF1cKA2HPI7ATMPeKwxD6dv56JgzSCFORpgrWdkYjJzd4pBg1DsW_SpCAaRaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این چرا جهانی شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78321" target="_blank">📅 08:33 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78320">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">عباسشون رسیدن سوییسا  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78320" target="_blank">📅 07:42 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78318">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pG4wHxAIgXvehPiQyczH60NGdKNtGBhi9gXhF-uaW_lKnUJ8WflWwxWX0XBvGoeqMoyfALuUgnaaTrgx-uxS7Gnwci_eXzQ8LW0TewOs5xmCFJS71ofs5JlXTn7z9RmZUtOosnumKYoCdm017aLidcBLYrOlfbjZcW4u1swA1LZqad0RHbTAEFqkrDxE8bAn3zlLatmMUNNGDYl1S1EBdT9l9BRO5so0gW8FmsEWJaBPXPKGuNg-1RGl4nxlkMsfaPwlBG2-Nuq8dCN4fHW3hca7R_8HZMZt91ABvGNL5BvnKHHnKSLATSRzZ9llxm2IquL6fo7IGhg1voW6nWfC5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چیزی نیست دوستان ارتش اسرائیل یکی از گسترده ترین تونل های حزب الله رو کشف کرده که پول من و شما ده ها سال صرف ساختنش شده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78318" target="_blank">📅 02:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78317">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGLhA1S22lkI5BYA_iMVJtRmaAxetTv2XwdE8yPKbJKOMSR0RoIbxDG2lGMIpf05E_EMidGBJMAzt6yj8kJ14zh7SEf6v6oYFmXpz9vQK5idoO5GaJiJD0Ppqz7IQz7NNA4Q3VI6chX2f46uGm-lcJyCgxgV2CpRnTn05CJrusvkDfWhhYHVIqMGX8XIF-7rDn8OMusdFcuNtB3JXKisoT3VORKjOzqac1UBtZzMqdeq4WZ1AnFjA65PT2FRUQ15tBaCd5khwrNmx1zGx6_TcrXaoIrtnWcsmWtChkETiAAtpQki_h6-Si-WRsAuk-MrIkwzLZLUXS6eaqt0k9hazA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Iranian power
❤️
👌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78317" target="_blank">📅 01:57 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78316">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">حالا جدا از شوخی ترکیه خیلی به کرداشون ظلم میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78316" target="_blank">📅 01:46 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78315">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Keabd8HQk6JjEbbEQV0E7RQ3iVY8EEoMeFHv5bihyXMU-2gqeBKlxL_rc0hKhE1XhGDUHr8a4MUg15pFNxkXCFlTTfJ8JzNlvjL7yHQzduePkVkI_PvdOpIcBBfJyn_Ua9v-53CV4tMzsQ9OV67QMUAge3EgbDdQF2PUul7ggOvkZOykxo8-k4wcqLYZ7r-n3GqT7pPIt6lKW3rIbAVbtMchM0oke2-0Rm8goUWc1t7cGFUWo_T-Y5ImoFbCX__uzGFn5p5A-RxARefHylG2vzaBfyO8ft9z3YTzIoMGCI5vCKNWGenRTLz03Zosid4AMPDySuVyHEOTdLs5lJ-MHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴ کامبک تکمیل شد  @FuunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78315" target="_blank">📅 01:37 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78314">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">یه طهلیل بریم
آخرین بار ک آلمان به مرحله حذفی صعود کرده بود قهرمان شد
پس این سری هم قهرمان میشن
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78314" target="_blank">📅 01:31 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78313">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">گل برای آلمان دقیقه ۹۴
کامبک تکمیل شد
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78313" target="_blank">📅 01:27 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78312">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oU0FcE1900PsVirFR3dh6HwNMElEKO5QMqj_QkwsvL7NfQ-s8Hp3jwyBgCjiqG1WwnCD4rgq70IhixA5cpceARLefdCxpQm0HPYF8qibUn8RUyypyDR198crpfVBssPCtqFyvV8Pw3VRfkMXCSS9TxASD4y5SShfHW4iE8jQbpw3UlZwhoSIanM7Eda5ZPdV7nb5SiYPm8ADyP1Vzy2G4-b3ZRdEMWi3Z-3W9kS_H3zA0II2jgjM8ojtSEYMasPo-Yta8nQTuaJ4g-JNIGBfLmmz1OlvekABdl2YOYTlbygO_ZnLtMsAdKvHCVaeobRIIENjHBPapWly29ikUk2DAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمرینات قلعه نویی قبل بازی با بلژیک؛ رسانه های بلژیکی میگن لوکاکو هم از لیست بازی فردا خط خورد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78312" target="_blank">📅 01:20 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78311">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">آلمان تیم خوبیه ولی مثل تیمی ک اومده جام ببره بازی نمیکنه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78311" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78310">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">آلمان اگه این بازی رو برینه عطشش برای ادامه تورنمت خیلی بیشتر میشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78310" target="_blank">📅 01:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78309">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوتموب باعث میشه گل زدن تیما برام اسپویل شه، لذتشونو گرفته لعنتی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78309" target="_blank">📅 01:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78308">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">فردای شب جمعه خود را چگونه گذراندید؟  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78308" target="_blank">📅 00:54 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78307">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">عباسشون رسیدن سوییسا
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78307" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78306">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کیر نخست وزیر بریتانیا استعفا داد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78306" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
