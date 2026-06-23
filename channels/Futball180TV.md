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
<img src="https://cdn5.telesco.pe/file/NlRYHpfbA9eTs8I9V2rRcsntGC62IRydWo03sd5Zt6THfZ4NUaU_peuzXCT7svTbwHxXR3tc-ad6tUBsaWwp6ZGQwVArUloMGg8-C908ojgR3vG7kVuzJ7XTheoNCyYTvPeydYmyDGhoJ-VaWE4Cc-I6o3kqMwRgO15HAxAj6dMPWV-x9WRD5Xvfg__z6D_eit_stShGKDM_XnOKb-93AlG4ZzzbP1qICZKZNbRMETzYwREHiFlSC_IXNFrKL4KQdGzZRBc6_twA2zSCOzNQlMn63LDObI4Be0e1FCLa_OXBX6bN9PnkL6wbHk7ZDsJ5SHpnUMTayf73Bve2o_EhCg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 720K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-02 22:53:04</div>
<hr>

<div class="tg-post" id="msg-95525">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HeMrGAfIwFyiC2qHysLRBKc_hFk4rOZLwjdrA180Nfx515PpYWaiMvlpoZOuFWq3fygKjDeJhkm3yARO2vcHbmVwr17c9hXd6DqjS3ul73-pGK8aigNP6uPy5kn-bffnE0UdSBzu44QJJTGRCMPMxsskagbfs5f4CJ5sdSgReuzWm6geGYskGQZd0O6-MfB4hnLjnDiQP7RHrUoM4mBvNVOt5U5eaEylwyCf2egSSQDdDsFOds0HyH7UFM66MKSAavjn213o0qy88sUq2YnMVP4J7d_Gy2r_5kfYbLkWHyiZHRMiWzbtVZQ7ERbHfeIvemy0WYE-MNAVk3C05Ni0zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو: شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14 · <a href="https://t.me/Futball180TV/95525" target="_blank">📅 22:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95524">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD7u3JdI9mcJNofAq27BooI28jJZGNgthJQW0P_pF59BV2gNTGI5WNuSntnoiNosjJIsjqnw8DWBIbeHZvGwSj7br1vCwZ0Bmh2Bywl4frcVF0VTQsOmLjsuU2JCwZQvsji5Q9z-Up2PbmVVL3_DD_owrnaqN2fyKTqpbdWL0Vt0Blb1QAdoBbnKf05Iid9iFN60_OOCyoqhKKoMANeR7J8bKdwnlvx032OGtBKEDHTMEaKPp1sf8EW4VCahLwiH2qixACgjKKJHxeS35CHs0fim0wP3KKxdG0uY0AGx9r_gUT_RlXqwChO1bVm9zz_GeE_MvEN3HluZttncBd2QFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کریستیانو رونالدو:
شایعات از بیرون پخش میشود، اما در داخل ما متحد و یک تیم هستیم.‌‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/95524" target="_blank">📅 22:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95523">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B_-4uUqIHwmkXYPc4FyZwa-iHAAfVob5_vMBq5_3bGWiII_6Dn1kJyUrV6wPpSwTk5ZkxH__G7VUZnuT0g2xFJlTiwPvuhue9JpSE55lvdH5Ms3MjAh3CN_xRl_2qcuY5vG7V5UvYlofwsAq8f_mRgzWc5xN_T1uAFROcZBA2EGIbPxfWDyp_-x8SdocrjUNuJ_Y1KKakr4sULHTmoZ5Qpw0IMehF1RpxIKlrbyhICyo0yoir5JGXhItKzWAcr-jObPn-3A35hiuZX6XTWrtf96T3pVBrTR-fXA9OmVIdiaPp6ChwybWCXkMYWnd8V1UWZ8GJTI4OtQjSkLG5sEmtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فارغ از تمام کری‌ها؛ خوشحالیم که تو دوران شما زندگی میکنیم و پرایم‌تون رو دیدیم.
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.06K · <a href="https://t.me/Futball180TV/95523" target="_blank">📅 22:48 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95522">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🚨
🚨
🇪🇸
#فوری؛ اتلتیکومادرید به آلوارز گفته حتی اگه کل فصل بهت بازی ندیم، نمیذاریم به بارسا بری. تنها شانس رفتنت به انگلیس و آرسناله که خود بازیکن کلا رد کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.12K · <a href="https://t.me/Futball180TV/95522" target="_blank">📅 22:46 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95521">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.15K · <a href="https://t.me/Futball180TV/95521" target="_blank">📅 22:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95520">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bR6my208vS2jkhaHeX8xJO7jKMKkgxEyFK_A8XN-bo_HnjAZNbv-e_71Sau3VPy0gattyYWiHjraPKI8WQnmzKJ_-ZQ0y5Y5c8dLst36J8fR3JzdtQHDIWgX1GOzc0SUB5SekQqgroEGjBY2LMsIGCyJDRl74wRPjiFRvURsGtOpfCA_8ME0ImdIOZdpGJQKf35Gd9JIWPNy3tWmG2QVFtWYa_WUjoy2zglJ5q5UYD69Pgk8Jp_qQC7NVM596-kZe9p4Akmf3u7W3J2yCVUBv2cYZPtKT7ehAOMyMgsWZcYynMc1i1K0ry2zu0GNOskeRgYA-ydNky5UA5Qiju1XCQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
کریستیانو رونالدو پس از بازی:
"ما برگشته‌ایم".
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.2K · <a href="https://t.me/Futball180TV/95520" target="_blank">📅 22:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95519">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/Futball180TV/95519" target="_blank">📅 22:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95518">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s9gAzm26D16_yNV3xDNK67zDGBuq3VerCMO-aP26AeZLwIkZKUrrMrKpa5tT8IHMlYRDcFz9-rUMQvJJs4JC10K0onyE69q9ZEFasQ3rkSaOFRAzcUCJnJ3wdG-dX5_7BeVaJ_Oep6XPi_A3OGckfVrQXSyyigtI5MSEvH5k3i9KJP7VrhwhNNwkXVSXbaQd0Rc0jkNPi7MJja0EmhkwlpjYSYxNBWYv_5l4eLI7wuUvitUljev6ZdWkiII0UQCuQJACqafHJysT3riwELLpz9ynGFoP_420zN3bIDC5or9FEkVO_tnL10xShCAPdl14BEp3Ebj9IAbFIpB3ZlhlKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بهترین بازیکن زمین شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.23K · <a href="https://t.me/Futball180TV/95518" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95517">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8aI7fOrCFTULtLqbhshmO5AdJCFZBVTLc78hBkhgdBO5b5GeUu5mYPhO-yFO01ASEe8-SQeSRU1FHHJYyNL552KT3TopeuPB1dhW6cXbO_sbDWDaeMdFTLZz0iyOiMb9AaGEyoU9G5fFplFoN-6Z_1iSJaO0jb0yfbl11C8ELLIBkkHXT1juIspDgW8XwqUWpfk1PebHAifuZj8V7VPZwpkkytl9py90RP0tzqU_yAGtMMuJvcYjsyhtp5aXM0w3ThGK394dwyDG8hYfQX-8TE0TV4JsjkIxXrys2nzJPP26QMYJ35I_Fg72s_riGKQyrdiVumsBKDMREIskJY5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
پایان‌بازی|تحقیر ازبک‌ها و برتری مطلق پرتغالی‌ها در شب دبل رونالدو.
🇵🇹
پرتغال
😄
-
😏
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/Futball180TV/95517" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95516">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">وااای کریس چیوووو نزد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/Futball180TV/95516" target="_blank">📅 22:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95515">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇵🇹
گل پنجم پرتغال به ازبکستان توسط لیائو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95515" target="_blank">📅 22:23 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95514">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پنجمیییییی</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95514" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95513">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">لیائوووووووووو</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/95513" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95512">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گگگگگلللللل</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/Futball180TV/95512" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95510">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TI1Wjwd5Y3qExBknit-E5hN0cLLVmINWWUjFt_HyDfxPlYSou7WOMCGnaeF07ylqRFxK44x2gwSnjpn1gCCnk2eDQ-cF40PSob1nCoTBDSURj6gKroc-cPlnc2CG5r8XcRLEKO5ALA5XVk4fldd5AQ1E0slxtQ_Vn7F_yGgUwk12N1BsAKXiUQdd8KocrXVigRzuyTu9mpV2L4oxL0TsxqFKYlS6yWShoNQ39OSs4oaGNzWNPjt3zm_ug9C5bEam6ESga0_fZiyXft66mUxBhKp-d2TJUS9YIabbk7pTGmTG1r7BumHNVCi9RMX4U973KkiVBODdg7m9xkH1cAGC6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h3q48KibmGpHOSN9bTDsb7Rxh3WdKvMeAp1x4SERWr99kxkJTp10CZ09dlLuLJ2KC0f0_TcPtZ4GzNMnCo4wtRG6VPq4VqMaunchncBApUMCTy04UhUWYLdXQ019RgpgwPaXOzKfR3FAbWtvMOOhVgr35myqApejaNB3U47ESHds5jQfF0mXpoAXVA6L1oITlWMscG1sI0bJYWIj5YhPWCvoiNUeowceQ3G6j8BjxrMKwA1QOpOS4M7_rz9C6LZZSHLDdZZF96P3qHaORAHFJGCMXX0pvzBfrAohYsBW6qpj99BOhmBDfOG1Pi2UWejapEXvzr2pBlCaBc1KRC6vHg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇬🇭
🏴󠁧󠁢󠁥󠁮󠁧󠁿
ترکیب انگلیس و غنا مقابل هم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95510" target="_blank">📅 22:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95509">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">نزدیک بود خییلییی</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95509" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95508">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">نزدیک بود رونالدو هتریک کنه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/Futball180TV/95508" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95505">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V_5NLlCQTUtv1i3ksO15NNypYwBQ1X7J7kBodp_Ik7YXOQHyvJTDvHpjYYpQy2e1PLpaMiuBr-v-i2EfhYHR_eMSx13lKe67pXjvKm_1--ajaZ1O5Ar9Bq5b3Y1PaJB9WQXf3feKROR6iWUUN0z0YDrucdF_t52tHibBCCm-LNirz6ohgbr0VAKL9xOfAawPlXpgl9XyMvTo1CFHvaQlTxJaY24uyaGOk3ym_9PPPyXb_k05XbfsQjkVQ33lkGIbEvXes0hL7QcX6WGu7e5YyfdCr96tgOOA6s9H3pjEDfhGLP_eQwNzACONYWp9W15IBsAZwZw3Uq1vZtOEgyzW_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZlWklQaMFguoW7lYFuXKVftumSRsqSNCAyx3QJn8EWlCa4BONp2zmQK2OdhJqZE2hNpx9IG0XD7mlvEOngmDEzhaNFRpeXjxEmcUZYZ3gHEmZRtMRuXMotaYeMLI1vgIaul1JF6aFwU5K8Z-s18MdzSjmkmPDAPhpcb_7cXMxODkOlUWN8hl-_eT_bDPXudnWE5KYrX4G1Zcz_Jwovv4KXoLAFaIpHjDWp5xUdf2IQxj3YCUqf7DOAbKYmNrElEQqIKA1bGB4qhkYrJtSrsyBE_q2Zmugym1ZCEEbKoSL8sfoDcWj_JvGZkss1ZlzD0yTmhtzscsMlo1ZzpaaCTCQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دوست دختر نوس تو استادیوم بوده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95505" target="_blank">📅 22:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95504">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=L4Sk6cla44OhAglxldYzIhxfF-L1_i0CAvVaZFvEIJHLHpA0TR9-pJTLwZTI7PhrZPbg3Vaq_oIMU8rTwz6Y0XisFCPgnWiqT1whKYTWkuKednHAB9uN76H3tqpEbHJKzCsKyFB_wHUUuaalPMBhA7p36iVyGavFf_nWptUO2RkPni0W56QL15V6IXf2u2tRdUv9AjQ9uKSyX3zXKRUKk8qrAyfSFdUX1eyUIujQVkWqfHPpYRvElBcLMrQLJ6sbRgI--4zceOc2577u5SK7mADo6VAHwRl3SxtSsY-jTMhJASWxNeSGmDO_XIdTenhskOle74b_IK2M_Smt0UpH_JfCQs0CB5uShZQTOzgx_YxZr2EmydgMrzuZdWAoEbqhDbWOqw-iaexspLKPwdfFaMv3mZI2e_0SCv7_i8jXYWmfBkPi_dwG8MDwMOzkk3leGIJg-0AQwehf1cJDYtV5Bflj5D31Aw5N07u0gbtiJbA7ls8eLYO-o9okzA_yoEz7D--XXcmsqlzRG7jaXs-Boh-fVe3tbAIVicpd6P5zIN5EJ7VK2W3ldMWrIuNm-7G-oligKyyEiKk0FAVDHjamCxs1EgnaRIbqqvZhDTSmIMOUdoemm1sN9GENEO5wiuIRkal9VCe4z4PlvCJpQejEVCkIMREdZx7QElN_efs4cMg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b28394b6d4.mp4?token=L4Sk6cla44OhAglxldYzIhxfF-L1_i0CAvVaZFvEIJHLHpA0TR9-pJTLwZTI7PhrZPbg3Vaq_oIMU8rTwz6Y0XisFCPgnWiqT1whKYTWkuKednHAB9uN76H3tqpEbHJKzCsKyFB_wHUUuaalPMBhA7p36iVyGavFf_nWptUO2RkPni0W56QL15V6IXf2u2tRdUv9AjQ9uKSyX3zXKRUKk8qrAyfSFdUX1eyUIujQVkWqfHPpYRvElBcLMrQLJ6sbRgI--4zceOc2577u5SK7mADo6VAHwRl3SxtSsY-jTMhJASWxNeSGmDO_XIdTenhskOle74b_IK2M_Smt0UpH_JfCQs0CB5uShZQTOzgx_YxZr2EmydgMrzuZdWAoEbqhDbWOqw-iaexspLKPwdfFaMv3mZI2e_0SCv7_i8jXYWmfBkPi_dwG8MDwMOzkk3leGIJg-0AQwehf1cJDYtV5Bflj5D31Aw5N07u0gbtiJbA7ls8eLYO-o9okzA_yoEz7D--XXcmsqlzRG7jaXs-Boh-fVe3tbAIVicpd6P5zIN5EJ7VK2W3ldMWrIuNm-7G-oligKyyEiKk0FAVDHjamCxs1EgnaRIbqqvZhDTSmIMOUdoemm1sN9GENEO5wiuIRkal9VCe4z4PlvCJpQejEVCkIMREdZx7QElN_efs4cMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل چهارم پرتغال به ازبکستان (گل بخودی نعمتوف)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95504" target="_blank">📅 21:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95503">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">گل بخودی نعمتوف ثبت شد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95503" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95502">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پرتغال چهارمی زد</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95502" target="_blank">📅 21:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95501">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95501" target="_blank">📅 21:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">چه توپی رو گلر ازبک گرفت</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/Futball180TV/95499" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KO_WE27VvkOtyiIr5kTJIbOBEJhkj4w5vQpzyyuY4MqpGxObuV4f5DVo6HOZgzDYdLVhG7cVwMpoFxTrojnj26SBwAU5w2qPfBxlBD-3BXs2mVSYuXaKy2aylNOJ3t7MwZXVdhmbklpVAKsYbBtKQczDfPS8xhQApV4RRjejUHFJmERcom-fA1Shn8iy9KR6zP1ttiRma_he8DoI7VXPCttvnCS43Iy3KZA9BVz2JeqcN61EpVYpMSGeYkOFPiL-2RTOoiF_uUWkKLizfQvcmU97hZExuV2aEbWZap-0wKMUgwrFBCskpImFW-ptQgSWl0He5lTOsQBomME4Zu4AiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
واکنش ریو فردیناند به دبل کریس رونالدو: ببندید دهنتونو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95498" target="_blank">📅 21:52 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">بریم سراغ نیمه دوم</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/95497" target="_blank">📅 21:39 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TGF1mNMcSoaOIdh1z2eNOvZYmAUHOZRSUr_X2UjXKTKRgTRVdvRcqFKqEYTEqPf7KAOrWrIVXCrT3qJWKVoFkAC2GGSmIfphKdyJ8NSxjIto-6XkCrm1-veMxKeUeAYmmLfLTupGpRQKxndvLkZj0EbSeWP5Zw39lc4y7IikIBEPljx29UEXmPHjZZdZMYUwQUlWfQZWTABNARGQMi2h4MdMXEGRR1QUY6EPuRzbk5veN5qsdFyrqHXzPX2cRg27NB8J5m2B9uYA9f4fyhqzi3QMjKDvWo0ZJaeSv84Pq63Ks6rvz2TdlBjnI3c0tM2n2YwgdjMIcREmekl3QEEYyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇹
کریستیانو رونالدو با سن ۴۱ سال و ۱۳۸ روز، به مسن‌ترین بازیکن تاریخ تبدیل شد که در یک بازی جام جهانی دو گل زده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95496" target="_blank">📅 21:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQ1IioFqjfPGOgy-aALMeUacZ-KmouSYrafWZZqu8MQixofHHbjAldXOD-fSF-pRXUZotSR54GEQufrYh3oBi7UcqFXCFoXuH5Ww-NHjmV2AdPi2BsGX6kAyNEfPyLjJ2-zqmnP7ZjDnpayKAFiQAOWymBHziSv_RAwidR9gzH8ZzwBbA10bre4qkgtwV8BhK9faFTbXpLNUBCpm04sbz8dcpNXyJuHz--7dnSfwQ-n6nRF2H1FinJli9LC1p1FAt-gvXt9gcfTfSJoPcbs2Ay6ZUt_1r-m8dHkMt1lSrVDQCkr_xH-TwFPfXwkh3HZU5MjGZSSKEYLBFRiV_dB3Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
نمرات بازیکنان پرتغال در پایان نیمه اول
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95495" target="_blank">📅 21:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">پایان نیمه اول؛ پرتغال 3 ازبکستان 0
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95494" target="_blank">📅 21:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j_gEh1FXxm1sIiE_9-3h21qFLGdOvXhzGD0lSKCqjsBrywe2fA2JeMEoeSujlnchzkI5v8sNFKHJ0-IudlSMENw2vwjHNwafhMOOby4uuOsA2paM2CcX6xDUW1K9JTN1DreeTptnp7ghOm_HmFQ8RpQSLNl5hPNb0RxnSIBEeCDdDrYDCMZpzKSkrX8fUgkM5w9-ZisDWYdP6j5TnfM69fVwJ4_ax2Pot8D10i_DbuUMbuQ-i3_ZenfwNadM34c9-F2dQaZXDpW7DN0jqnWa7-Jl0gAYVBOTfdipK7Bu4PpqSVnmroToy5pkjs-hGVpmq4FGtEqjIeA8bo1w4LNvvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری بانو جورجینا واسه آقاییش.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/95493" target="_blank">📅 21:15 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67baeb0629.mp4?token=ICG1PY6lSTDdma4BHH8y0MZU2UXuk1NAEKSz_91mVj2khi270Zp3kMtt-zUAmkKazUTaEn7ZVAGoD2Y9T-pXWnNf_gwW982t3MVqOaN9ewI_OzuMfeykcsKegvl8F-052Xt_YQFRPtPIGpc6OtZQlu8IfgvENhZwplBT3Smd3sB5BhbG-uYKkXyh6YDp37qGGEub-myEqydwa4GGTrDV6-dr8bSTJXmDjPXmQUSWYG3sXg_wjVCktGZ9wskCIm7K5QQaut0KR__KmW5ZkWr8D3KxT2YG33o9V4KxRkecluHP40kvZxSEFXyMV5O7jxPN-gmk40r4Dm_LqLVFa07UUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67baeb0629.mp4?token=ICG1PY6lSTDdma4BHH8y0MZU2UXuk1NAEKSz_91mVj2khi270Zp3kMtt-zUAmkKazUTaEn7ZVAGoD2Y9T-pXWnNf_gwW982t3MVqOaN9ewI_OzuMfeykcsKegvl8F-052Xt_YQFRPtPIGpc6OtZQlu8IfgvENhZwplBT3Smd3sB5BhbG-uYKkXyh6YDp37qGGEub-myEqydwa4GGTrDV6-dr8bSTJXmDjPXmQUSWYG3sXg_wjVCktGZ9wskCIm7K5QQaut0KR__KmW5ZkWr8D3KxT2YG33o9V4KxRkecluHP40kvZxSEFXyMV5O7jxPN-gmk40r4Dm_LqLVFa07UUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید لاشی بعد گل دوم رونالدو
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95492" target="_blank">📅 21:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برونوی بیچاره هم الکی فحش میخوره خدایی</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95491" target="_blank">📅 21:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇵🇹
گل سوم پرتغال به ازبکستان دبل کریس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95490" target="_blank">📅 21:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95489">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">سلطان همیشه سلطانه حتی با ۴۱ سال سن
🔥
❤️</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95489" target="_blank">📅 21:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95488">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رونالدو دبل کردددد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95488" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95487">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گلللل</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95487" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95486">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">رونالدوووووووووو با پاس برونو</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95486" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95485">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گلللللللللللل سوممممممم</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95485" target="_blank">📅 21:08 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95484">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f0F16X7rno9qg9S6g3cflZjhr69u_humNqGepxTSVWW_Q8vnEJoE45OHDFqrlbzNHUQbYg9dSrF8n24jrU4ThoCTzV4JnQAIj_WBhh7kzmJh-uaRE9apMKKJBjHeN9JErtfBvvfHPELXrnW8yFRH6pIqiPAbTY5hPqm-Ru0lwofLpwoYeB1fvbCxNZkztFjK6TPn76MczrcbGMqfJAKrzjOGYkzcRjykOwE18owID_Un4gcW4wfUQy9UmivGtg4SJq6NMEGuq7FwqRiEIFZ4L427xqMLw4f3Ep7bZM9kWXJvfO_N6SH_aMC4I0bREl7hQi_eCZrZqnDAXckZ0eGYKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇿
سوپرگل ازبکستان که رد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95484" target="_blank">📅 21:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95483">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/843fc3ed89.mp4?token=A3T5NbS4EojYyzwQTnejy5_w1BSQ98PpbozTvG-dcTWdYGlTGv4O1U3SY4W1Uf1fzsYorSEKBt_DO4-yal_PW-TVUO-dpYvkBMm-p1chsPWk3dih0JBCQH3A0HW17uW1jwUytYkt-nFeNlWKvjpFS7dy2EfI6eChEnEe-O60juFPEe4heD5QQmwczUIgAhUV7byeiHGXGM80KwbcUZwYt4WK1Tn3L4QzhGgjPlPY2nCsSfmoBcwO9srbsNiO5rkXY-uI6Ds-TtvshGXlJWmRABwaRYFkY4E0F5Q-P6jz-VFQNtsvvo3hNxXpd10L-bm5SWRCLKqNnsg0Xdd0bv-KO6sQj2YeYJjCzgNE3Ylo8wZmjaEpp_mUcOBgrGOqyP1JJ9xCPCzXL0kv_74A2MVQXZ-L6PMMv2BVRef0INDXKkFBozM-mvCANxB5YyJ7d8RWFMfUvKXL0x7j5BLlPgewqtCui0wec8eB471aBpRWuyWwLVouqH2UdCK5Diu6i9lFyr8Q_QyAPIig8NbgwWHRUkIUDj1VhRWlR-DUw1S0wiZ1bJ8sCM5Ferzzwhz0kocp08xk1ds1xQBtDRNDu0cr5iwuI6HiFF9PFffryz6YsjX24snglI1SL5U6j4htGR6hq13G8Z7EFjeiudIKmHY2DsNySSp1XgtERUhgK0lE0fE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/843fc3ed89.mp4?token=A3T5NbS4EojYyzwQTnejy5_w1BSQ98PpbozTvG-dcTWdYGlTGv4O1U3SY4W1Uf1fzsYorSEKBt_DO4-yal_PW-TVUO-dpYvkBMm-p1chsPWk3dih0JBCQH3A0HW17uW1jwUytYkt-nFeNlWKvjpFS7dy2EfI6eChEnEe-O60juFPEe4heD5QQmwczUIgAhUV7byeiHGXGM80KwbcUZwYt4WK1Tn3L4QzhGgjPlPY2nCsSfmoBcwO9srbsNiO5rkXY-uI6Ds-TtvshGXlJWmRABwaRYFkY4E0F5Q-P6jz-VFQNtsvvo3hNxXpd10L-bm5SWRCLKqNnsg0Xdd0bv-KO6sQj2YeYJjCzgNE3Ylo8wZmjaEpp_mUcOBgrGOqyP1JJ9xCPCzXL0kv_74A2MVQXZ-L6PMMv2BVRef0INDXKkFBozM-mvCANxB5YyJ7d8RWFMfUvKXL0x7j5BLlPgewqtCui0wec8eB471aBpRWuyWwLVouqH2UdCK5Diu6i9lFyr8Q_QyAPIig8NbgwWHRUkIUDj1VhRWlR-DUw1S0wiZ1bJ8sCM5Ferzzwhz0kocp08xk1ds1xQBtDRNDu0cr5iwuI6HiFF9PFffryz6YsjX24snglI1SL5U6j4htGR6hq13G8Z7EFjeiudIKmHY2DsNySSp1XgtERUhgK0lE0fE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇿
سوپرگل ازبکستان که رد شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95483" target="_blank">📅 21:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95482">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل اول ازبکستان زد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95482" target="_blank">📅 21:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95480">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">سوووووپپپپپررررررر گل ازبکستااااان</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95480" target="_blank">📅 20:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95479">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">گل اول ازبکستان زد</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95479" target="_blank">📅 20:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95478">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57cc14c630.mp4?token=nxFXu_05eaa86Y0-IuBpgVHc122-v1J5ikqADi6TidF5tJ_Rw5ulmsaVZvF6bs8E3exJ89NzJ-3rU9dNtYVmfH2QipOPjFyylKEwRox7hgc_DSkLQQjXvA36XxYlFH52q2UpJM_OD7PD4pnDnv0dvardVM57RaRuFG4fuaUcq6glMVhjGhHAh3UBkkjfhBxmLk6YabKQoWgGQt1ajYm3vwEOXGyFLZ19yXHElAsounxiMLdJ_4OdDhmzlZJ2P4VhrvCJgXgUzwjusE9sPb5Aj5SymB48Mj4HyXcvP67slkWWvvnYjXoCWsQKqOgdcjzJW0AVloDBWMOixW1BdWOWRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57cc14c630.mp4?token=nxFXu_05eaa86Y0-IuBpgVHc122-v1J5ikqADi6TidF5tJ_Rw5ulmsaVZvF6bs8E3exJ89NzJ-3rU9dNtYVmfH2QipOPjFyylKEwRox7hgc_DSkLQQjXvA36XxYlFH52q2UpJM_OD7PD4pnDnv0dvardVM57RaRuFG4fuaUcq6glMVhjGhHAh3UBkkjfhBxmLk6YabKQoWgGQt1ajYm3vwEOXGyFLZ19yXHElAsounxiMLdJ_4OdDhmzlZJ2P4VhrvCJgXgUzwjusE9sPb5Aj5SymB48Mj4HyXcvP67slkWWvvnYjXoCWsQKqOgdcjzJW0AVloDBWMOixW1BdWOWRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">Siiiiiuuuuuuuuuuuuuuu
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95478" target="_blank">📅 20:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95477">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b8dd0a3bc8.mp4?token=VbDuqO6SZnCpb5ciao37b-eo3NzJyGMq29FAL_N48o9mWbgmYZbuN_vNES6IWsKHJ2KSVITX1SRnkdL74jSlflaAJGmkNoriw_lUc-RTH1abWaQD9jvzwuk7GAB5I1rT2nIAC1E85yPlFteZxt3LXrWmrEYjeaYKXtRKxeDaKjNAJSi7_NVaqGiOfxG3K3Qdgo1svlbMOjlu6MncpqMM02Aaw1TaQ6DmpUTSaMolDWc4SIsolCVLljmuGUwLqCwRKlZGe3qLs0V1oPCtG8n4fDU46LQ0yUMGs3y73WDy0nZtxWPAE0q5km5Uh-6anTmiazw99zXe462zHvHbNwdnJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b8dd0a3bc8.mp4?token=VbDuqO6SZnCpb5ciao37b-eo3NzJyGMq29FAL_N48o9mWbgmYZbuN_vNES6IWsKHJ2KSVITX1SRnkdL74jSlflaAJGmkNoriw_lUc-RTH1abWaQD9jvzwuk7GAB5I1rT2nIAC1E85yPlFteZxt3LXrWmrEYjeaYKXtRKxeDaKjNAJSi7_NVaqGiOfxG3K3Qdgo1svlbMOjlu6MncpqMM02Aaw1TaQ6DmpUTSaMolDWc4SIsolCVLljmuGUwLqCwRKlZGe3qLs0V1oPCtG8n4fDU46LQ0yUMGs3y73WDy0nZtxWPAE0q5km5Uh-6anTmiazw99zXe462zHvHbNwdnJ4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل دوم پرتغال به ازبکستان توسط نونو مندز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95477" target="_blank">📅 20:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95476">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">منددددددز</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/95476" target="_blank">📅 20:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95475">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">گلللللللللللل دوممممم</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95475" target="_blank">📅 20:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95474">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bedn1sJik5MXVwbuKc33AEE7HHc7I-oNOgdZ6MGAvsaHltwbBDrhAT2m2_zCDY7Pd61NEx2vgUplRkkGXJ-PFY9eOuvyleNtdpSJEjD-y_D7n2daDprxe9d1T518nTcjU6BEd7VPalHuoKJ9wn5Vyx97Tk9FpuC91ZRWt6X29YqC9LoCYsKoK8_rqfMLhfiUmzJZ6hA_k7YpzyXMPyCs7ppRonhrnjRHtxYDfWzpD_SJZb4R4NiB-YSPi4QPYkqdjX-U-Ho7nq1CxtIh0B1GMq8PSiyEtJswPqAZJXSeA1rCuFPyYYf94y4otisNTSyECXcqL0hfXr9f9kDCcC3ffw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
رونالدو به اولین بازیکن تاریخ تبدیل شد که در شش دوره مختلف جام جهانی گلزنی می کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/95474" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95473">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">گوت گل زد
🔥
🔥</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/95473" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95472">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2401591606.mp4?token=VD1usQKfX3ah3iZ8rzOsfYXOJKwVKYieDBYfvm0NQxAJU4RPm4R1BoewKwfg0ymSCsNpFpW2lPtcf_9nhMzkAAOJefyKKu9g0xj6_jIZOTiOlDyaR5UXVGsL-PyZffiiME8yYkV2nCw1FEL8Br2m51jGDSutwuNfpf8NjZxpWDQBu6gmzZv3ZNUbML8X2jAdn-mijQoLXEnrKQdmRFXz41RPDRCGPoDty_4eqFzSs1pJYl3Rlz9N9FnwH3LpyA3CbaZeoH6oNqJuevc0MF4yLYwlnAH1WCxvV3EzMHj4aN3ko05KYnGLum8WMKWm-VTWGJEG38getK2VceOlgf0vV0Fq1aJlrKMlA3s1WGK4KHTh-w1InZOnwjmXnDp8yxWlf5xATGYxL2NYXyp0CMI2kDayhxwD66_dDPcKQ0bHzW2u7lyQ5ckc1DTzpSU7ced0NXV0ZUN_Yl2w-ZzOqLNsRaE99FYSeEY1UKiQYhvFBzj0E560SwiqJ8Wu4443Sy7GOt1CHRyuRggBmBEXiWkRf_-68h2yz7RuigrvC24y_0vi9cfk3O3IpyudvSj0mPVxpWnDJfjMcgtiEeYZb0ZmXabOdsqVUrDKf0Pj5lFlv9jB46u8d_OiV8-iFUBfKUq_-GdrxkqutqoAoLnuorWeYhqMU0SxIBoG6i19M5qDzUc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2401591606.mp4?token=VD1usQKfX3ah3iZ8rzOsfYXOJKwVKYieDBYfvm0NQxAJU4RPm4R1BoewKwfg0ymSCsNpFpW2lPtcf_9nhMzkAAOJefyKKu9g0xj6_jIZOTiOlDyaR5UXVGsL-PyZffiiME8yYkV2nCw1FEL8Br2m51jGDSutwuNfpf8NjZxpWDQBu6gmzZv3ZNUbML8X2jAdn-mijQoLXEnrKQdmRFXz41RPDRCGPoDty_4eqFzSs1pJYl3Rlz9N9FnwH3LpyA3CbaZeoH6oNqJuevc0MF4yLYwlnAH1WCxvV3EzMHj4aN3ko05KYnGLum8WMKWm-VTWGJEG38getK2VceOlgf0vV0Fq1aJlrKMlA3s1WGK4KHTh-w1InZOnwjmXnDp8yxWlf5xATGYxL2NYXyp0CMI2kDayhxwD66_dDPcKQ0bHzW2u7lyQ5ckc1DTzpSU7ced0NXV0ZUN_Yl2w-ZzOqLNsRaE99FYSeEY1UKiQYhvFBzj0E560SwiqJ8Wu4443Sy7GOt1CHRyuRggBmBEXiWkRf_-68h2yz7RuigrvC24y_0vi9cfk3O3IpyudvSj0mPVxpWnDJfjMcgtiEeYZb0ZmXabOdsqVUrDKf0Pj5lFlv9jB46u8d_OiV8-iFUBfKUq_-GdrxkqutqoAoLnuorWeYhqMU0SxIBoG6i19M5qDzUc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
گل اول پرتغال به ازبکستان توسط کریس.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/95472" target="_blank">📅 20:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95471">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">گوت گل زد
🔥
🔥</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95471" target="_blank">📅 20:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95470">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">رونالدووووووو</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95470" target="_blank">📅 20:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95469">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">گلللللللللللل پرتغالالللللل</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/95469" target="_blank">📅 20:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95468">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نزدیک بود بزننننه کریس</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/95468" target="_blank">📅 20:34 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95467">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">پرتغال حشری شروع کرده</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/95467" target="_blank">📅 20:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95466">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">برررریم سراغ بازی پرتغال و ازبک</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/95466" target="_blank">📅 20:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95465">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/u9o93nH2OwiasF_Q2LHknO-w-UENnf5qUFR0quOUqSi3DaGSSLkDB4ZrgJXdgdigy7htI6YVFFJ_obloiMYnOem38SjpJ_RPg7hFgXib5TqzoXRCaqxcYaskO-B-Z7VEOMSJKXglWX8EEFAqzLR12H0CZqN253OctQiULO7z8Nnlz8lsuPFKTupODo8_JSnT-oKv-UVQ5_uDIlEi44H3LaTVkBOL2fviCeh0wpwQM4qMSGWUw0byrV3llD0_LFk-BwR3m6R_rI76A5EfeI18UFacSXEqZpRwzXuhncqby48D-ngIxX8Jk15KIj5jtRtRx6dfGfoAIs06Eiutwc6gGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش رونالدو با ژائو نوس قبل بازی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95465" target="_blank">📅 20:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95464">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wm4Oyy-_RG7giJ0imrw7MCJtU3YASli1tzy5RBu7_d8omuytv7kR5K1b_aB6ETqbhNg9YOeRETbCe0D-rznIqQ95QmUA-smNvx1QAflPQCtpKXMBNJeJ0bsKMqlEAgPJnhkPPN6e4ETPzyVGnaS7wc7yykwwGUnKCZD8cY6VcW4dR350IF38WV9e5_eaoUkkFiJDnMJWWyG1SmCUk6n_XOi9OtC4bC7t3CmfyKXMAcyjM6NsvHjXhomYmORmKhfkq3whKnahga0PB5EUwKHyMfKO7P2LzAFigpagueUBSrnaS1kodkCKBrlKw6UMpiAuE1718sRWVvaMMC5sDG8fvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رومانوی لاشی زیر پست دوست دختر هالند چیکار میکنی؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95464" target="_blank">📅 20:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95463">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IY5if0q0rQok0rObvW8o5RFhtCC77OenyrNpD1Kuh7-sQnPkCY7B7U-mMjZ_tqOJ-GWFLk4Sh5yLrjQ0FtBsZg4kZ55LH6klV6O3AXXTzxnivbTdFpn_VnNED__NCMgi03KiF3q8AY-ReTJU9xoe1rBeWZq8rhKwm_Ya6R2qYisjZ16JIAJtnSW-r0rfD9NkwAatejj2Txs-Y5xJaO4yazP-5a_58MewFmg4dLdIQEq2RL6dhht1W-cSMtRoHjffH-dXDb0ZOUK6652F6co8iwMhay8VYxrY5DfHQBqP1R6ykC3TDwOlCz3aWmm07plcf6ufkqEoMyQme7LqZ1gAGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنر هوادارای پرتغال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95463" target="_blank">📅 20:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95462">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55d278d4c6.mp4?token=lJp-RzUzqaSFVpfkMtLGV2CwLxRk9w_kwy0bIFzkbumPqiVorVqzLiJ4SIAdLki8q5NYY4VL5zWf7iKlCyN-gbgC1A79NlTQ1nnwcMmwuLRK95LhR9gJzOHk2e8ZTo0wkyBQjK6aYOkCtPpyxK4YXJC2BSccva7SZ95deKFRsb5iVV0p3DmusSntQLX9QbkbfULN3h2gyaSaI5qJB-dqKLYLJx_oSzrJ5-Mc5ArJs3UET_hVT9LbY4p52DWZK0x1pUCD81R7vcvaxIwIF8oSogIsBNdEEZf0KW2ZSa5Mi7eufy476xGlIN7FIKTCdSboN2IkcNGVkOYTh4QGBX6I8LfCJ1lzp6nZZkW1Wds47-l18x2kl-gOQhvA3KkIXwP1bb7nQ7oaidATOcBGhGB0Bo9umrz3i_XfWhBYDzENhJFKtV3o988NqelJaqnSHFs6nySU-WGTJjNfenvUJon_TPqZyW6o2qJiLWyWe7BkRu06qoRwz56FF8OBT2IjxgOEO1oXo9zXwijfM47Fr7Nrsifz_7Qy5gmg0C3IamVmJIWrL_eDPvJtEEr5zzosYrnVR4sEOMTyyXshyyWOowEQsVzx5-Nx7Tlc6FlkOqFlQq7P1hitDrpaBviTaTPfD08jQx608FA8rriBECetwaG2a85-Y6zB-z1uSCfBPfZJHSI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55d278d4c6.mp4?token=lJp-RzUzqaSFVpfkMtLGV2CwLxRk9w_kwy0bIFzkbumPqiVorVqzLiJ4SIAdLki8q5NYY4VL5zWf7iKlCyN-gbgC1A79NlTQ1nnwcMmwuLRK95LhR9gJzOHk2e8ZTo0wkyBQjK6aYOkCtPpyxK4YXJC2BSccva7SZ95deKFRsb5iVV0p3DmusSntQLX9QbkbfULN3h2gyaSaI5qJB-dqKLYLJx_oSzrJ5-Mc5ArJs3UET_hVT9LbY4p52DWZK0x1pUCD81R7vcvaxIwIF8oSogIsBNdEEZf0KW2ZSa5Mi7eufy476xGlIN7FIKTCdSboN2IkcNGVkOYTh4QGBX6I8LfCJ1lzp6nZZkW1Wds47-l18x2kl-gOQhvA3KkIXwP1bb7nQ7oaidATOcBGhGB0Bo9umrz3i_XfWhBYDzENhJFKtV3o988NqelJaqnSHFs6nySU-WGTJjNfenvUJon_TPqZyW6o2qJiLWyWe7BkRu06qoRwz56FF8OBT2IjxgOEO1oXo9zXwijfM47Fr7Nrsifz_7Qy5gmg0C3IamVmJIWrL_eDPvJtEEr5zzosYrnVR4sEOMTyyXshyyWOowEQsVzx5-Nx7Tlc6FlkOqFlQq7P1hitDrpaBviTaTPfD08jQx608FA8rriBECetwaG2a85-Y6zB-z1uSCfBPfZJHSI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
ماجرای مصدومیت علیرضا بیرانوند در بازی برابر بلژیک؛ قصه چقدر جدیه؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/95462" target="_blank">📅 20:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95461">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgX_QN0qBjL4vqGZJcPgR1WSjVpUIuPCEhayQcsemLzr7QcpVt6f3VwiLhNbeLQuRsuJ3YYuswDcRr6x0Q-rsFgwMEOs5g42ngrQesqIAAK4gQxjZNYFCfPQ65bYnzHqdkurIFg3fkJwOX8zpQt6cAHxUQbH758DBP1VaWq9hfzNg8G3oD5f1y-Bbkdiyji0W1KyCm-747JCfj4CLB0XkJE5Kuu0iJuBdbcFkKfktN5nhMzPV8QeGCGOPPnqzkmUAKflLISXbwQCIsufwb40D57jd7iCJHPlPKGVxdrCz2qPg0_Kufv7XJL5kVK9cznZJUxSjuA4K8N1SqF46-h7Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😁
توقعی که امشب از رونالدو دارم:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95461" target="_blank">📅 19:53 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95460">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/mpiuKKAQrNthfEXRNen-ZToXFxDQAlVuT2wXLjhwynA_aFP1JN9QCtXBlHKLAmDAmQuXRa7IW1sOfw8TOblxBrS2T37G2FpDIP9KAqzYtSJ4JQ7DuidPMW8-33-h-LfLUhy10L6dv8qfVA5bSx4VyBRADAhK5B6FqPzDP5F7_VVzifvYrGG0eaKmkFiOrYh0drqtgywE1d_lNwu5KOBvYFRaaqF3XdlbZbj2avNFq3pE5ajzklHHQtIoGZAi8wvAxm6ofgi9OM4iGk-fembDLs4bk8z6Mo-qSvo2EFaFj2lhvC0jqL7hVFH9IYbYQwvE4NyhBgs2vnQohOjOMwmivA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
بازیکنای پرتغال با استقبال هوادارا برای گرم کردن وارد زمین شدن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/95460" target="_blank">📅 19:47 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95459">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PCH3x6X8OzrVHMKWaeClu0XR8ErdpgsA8wgSHCJrLK6IeqMdZ3C4okt2CBMRvDp8MnTiXeScGvTE4hzqsw8G32lOVwE76dYKg9T9diAbodPwCgI14rPnMnNc7aybeQwn8J64hhbR7bJI_8QHObmMNDOLXynQ7jVgSNVedfGTma2p7pd_wBwhvEQOfy_izYp4xilcMhYFA42iC51wZjtw1UC1lV5PJuPLYYAVOdt2SvPQPEGZsh0fT0wuGPJUHiDIy4qeTC7yPwUFW-AjaeE0_WwDuINRi5qfU5LETp4W_7DRhfk_2U3N7iGQ7SF5MEOx3pI4t94l2OJ5baXNoXUWKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند و دوست دخترش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/95459" target="_blank">📅 19:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95458">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5123cb7d0a.mp4?token=kLK5Bgk-lzW7xVIDAJbcE8Mt4zAOEW3Ik1mIQ3mfbuOpdV2f4AY2IyG4UYlkDA9wKA1V51sLduUeM_FyNMnLekR4M_-3WdnOUru8ONwC3KiMNcMYUHQRYGyOYzAXn5SctrxKOG3xvPYDljnAjsfPLavAeZPGvPbEsZs-F84yVamFKahn64jRLrnfPJ06mzp1S6QJg3cs2WY4DHWO9fwbcV6OUBDbH5US5EvdddzUozyrxe1QPrdjWvAmN1rjo9tBsfzwKrEjTu1IsVxqzV-LRnbpKuN3GHRGI-PNgxVL1Ls2Ykde7vvfyUM5AKCIzA6-WdEI1y3uHn0CGLPcVfOPHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5123cb7d0a.mp4?token=kLK5Bgk-lzW7xVIDAJbcE8Mt4zAOEW3Ik1mIQ3mfbuOpdV2f4AY2IyG4UYlkDA9wKA1V51sLduUeM_FyNMnLekR4M_-3WdnOUru8ONwC3KiMNcMYUHQRYGyOYzAXn5SctrxKOG3xvPYDljnAjsfPLavAeZPGvPbEsZs-F84yVamFKahn64jRLrnfPJ06mzp1S6QJg3cs2WY4DHWO9fwbcV6OUBDbH5US5EvdddzUozyrxe1QPrdjWvAmN1rjo9tBsfzwKrEjTu1IsVxqzV-LRnbpKuN3GHRGI-PNgxVL1Ls2Ykde7vvfyUM5AKCIzA6-WdEI1y3uHn0CGLPcVfOPHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابلیت جذاب کارت هواداری فیفا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/95458" target="_blank">📅 19:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95457">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUh_hmxXCsNY2vLL5T_SawsjefI2Tf7tfGqoAGP0Jn8y5HcS6yr034B_6IUcLU_BODiyQw-8SKQ4w9wkNhHBOTFYjS7AgSZtpeYADZprmp6_ngx7lZ59N1WCJAzI4VvSd0OMhuz_lMJofet_i_Okp4db1Ewn3MOC29rlpc7PYtoOESs0YxakUueL8R9CYRX_rdGVuTRi18pzOzWW5MaAj6NxooeDmyrO2vEg8ypHTzqzaEVhM3Rpd6txc_NanpHxxytzTE7rK5Vvj7z34FfyOaYSMkeU3JyfCSETdr8Xi-A0yg9FKJfXoqVPnER9SV6l06hrBzA4Ssram9XHsbSoDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🆚
🇺🇿
🗓️
۲ تیر
⏰
۲۰:۳۰
پرتغال
🆚
ازبکستان
📌
جبران لغزش پرتغال یا شگفتی بزرگ ازبکستان؟
جایی که یک مدعی اروپایی برای بازگشت به مسیر صعود به میدان می‌آید و تیمی آسیایی برای زنده نگه داشتن رویا حضور در جام جهانی می‌جنگد.
⚽
🔥
پرتغال، تیمی پرستاره که در بازی نخست با تساوی ناامیدکننده مقابل کنگو شروعی مطابق انتظار نداشت و حالا به دنبال یک برد مهم است تا دوباره به کورس رقابت‌ها برگردد و برای صدرنشینی گروه خیز بردارد
در مقابل ازبکستان، که اولین حضور تاریخی خود در جام جهانی را تجربه می‌کند و در دیدار ابتدایی مقابل کلمبیا شکست خورد، حالا نمی‌خواهد خیلی زود با رقابت‌ها خداحافظی کند و برای کسب امتیاز و ساختن یک شگفتی بزرگ وارد میدان می‌شود.
🚀
⚡️
آیا پرتغال با ستارگانش به مسیر مدعیان برمی‌گردد؟
یا ازبکستان اولین شگفتی بزرگ تاریخ خود را رقم می‌زند؟
👀
🏆
🚀
بتگرام در تمام مسابقات جام جهانی ۲۰۲۶ همراه شماست؛
با پوشش کامل بازی‌ها، آپشن‌های متنوع و هیجان لحظه‌به‌لحظه رقابت‌ها.
👉
🌐
🚀
betegram.com/affiliates?btag=3_l7
🔥
⚽</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/95457" target="_blank">📅 19:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95456">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h2FLgpKg0OyXFeEK99A7A6KI3QQtqK-KUu1_AXEOVVYgCGYgpdWqVKr2n7Heu-0Mbe_IYFPCvEIeItKzyDDAnwcjyjLDbl7WRMIES8kJ1A7u9rxh21ssREG-R8HmdoWyeZmzBtCKGgqQdmm9iEWoJXZM5pyuTXQwBkj2hxkizQnE5ZvKRDwWu0hCJOdH3x-jTFeFTP9TH9vhX3jY9tAd9_ot0lBaD6AkBEl_moaYFVeXLfXJY5rzGgLqfkYvNAhQXQ1lNYelOKQ9E0DZ0sPUFWN7UhvbkOM746EXZvQfSuKWEpkgV5kFzRFH49EyQNdwpvjxJr-wLD40vtKQhqf11g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
نزدیکان نیمار میگن نیمار از همیشه متمرکزتره و این جدی‌ترین حالتیه که ازش دیدن! اون داره روزی ۲ تا حتی ۳ جلسه تمرین میکنه و چند هفته‌ست تقریبا هیچ دردی هم حس نکرده. توی اردوی برزیل هم این باور هست که نیمار از نظر بدنی آماده‌ست و میتونه تو ادامه جام جهانی…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/95456" target="_blank">📅 19:36 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95455">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XfRk7K9JL0SxcbxnR09KiddSf6GrkfpJu2iNCk8vjIbTsQp46VzJLlm6CVpU5bxukvVm6OAVx-h9uZTc6DkEFFIanfsCN3ZXFvG2yLkUIeQtoiycfUaMBj-1GYua6l8k0T_S_ZVxVHFrTjTKn8q8lvtEHsRj4gEVzYf3MDsA03QIu-mSPSqiedICr9AQpuH1X9HQW8yGh8BWNWH9lJIjIyA2I2J-5qDxQxOo2H-uKcsChPDIOL2k0ZA5kAccaWJWqu-VO8J1rkZwzXH4AUg2MWRMOIWcb3JU8aoZN2DOMhzIW79--kmOMSc19eue-8vUeAgEKbI6v7bz1gG9ss5neA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدو به ورزشگاه رسید
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/95455" target="_blank">📅 19:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95453">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IdDrYPQP7OB13fRaIRyLY66t6yYW5kRwkxpVav21ZFdLBCKhl3_h2x3NM1-hXYvvynr9kIo6FwpLFVjFlRt47y6o2ovu4deW_tS5NzyPD99vsd0-fC_C7yyRNyushYZwvdIgcxEapSXAzdclBa2zEJC-J9OEvI-oUt4xztmn2JzyDQgEGzKPAONM86-yecwDdDEkI7fJ__FHE37jWalCkp6pFHwEqpmkFEU7aaHblyUrKlssVAESq7qjaUmt3YTusDIeBYpwcD-10EFRJZiXzfL4wvoyXBWD-eldAVCft1ApJrPEhmr33vczHjkPzxAve6H1GZFyr_CePCIM_YrTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RT_G6FzLf1uC1gF5-8Ruj2PauL64qiinXQcyyQ8gDWc9BWl90WwvL2h5yucfdCJ9BNYwRGzlMIYOT1VWiiKlbwJKu8H0M0liw_ybaAlv-JiVWXi8ZnVNAR8SpvUCYaZ5RhVulL_EgpIXtgNyG4DqJmJYuD37YEfkp1XTLUqzvBUJYG9HArCZTM9bj2youtu4u7PYVrrEXZ2k8aaaDBvpzCKl0UbCKJpDtH2RCPcnnLFwGnBPlIedKCkWw2ZSDul_8p8bYmLrRMIUMrNZA8v8mM3H2rdjW3c8voJFnaTv2Rv7CnC44bgWcrdYRwmNWyfmoAXgRfvYmGJQ8Z9q3oxdWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇵🇹
🇺🇿
ترکیب رسمی پرتغال و ازبکستان با حضور فیکس رونالدو؛ ساعت 20:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95453" target="_blank">📅 19:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95450">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ksmjrwJYnRTZyVzo9E7zR8CyqQZfWbtxLTCMxLJ-lGEdZq4dn9QX_uK8SN2EjytjvdDYmC-Ki4vrlcAv1S54cg5GJFaESfHDFYNvrffw4MWXkdYMz2Kfe5ZwCwmyZQ4ZdesRAzWIRTE3GmL66w4HYpoDIe_cKpLsnvu6HagDwdbzFz9kvX_RcKFPUS5Jgcmpgjvw0sRis9sqfeC3Qv_3BtNKlLRwK_2k11gqkWLz4CBuDPaIpN5SzFYhShRy4TM0Ht4YRofnf6M6ax2rkNClGB0xAcrSHt68UZz_W20mdP19NeuxLmcUJ8FEdJ4rM3BhpPXwF7HHKkyyKSnsf2Lmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qK2moyO9XV3dFFxibtZxVMrMaQ86IBWsGyRTrM8bgVlTFrVwD7qwmRpV_dRL-Pic2-1Y0m99OruuFHY3EtgdEl_Cch9ERheyS_eooMeVLMOCJvgIWh1B1xx0Qy66wjQLkQdbbXrvev2476SHpKNyO9n4mX5OmaaSUcNTcPu_jeG0Jmobl4Ko71yFyuqaYxyexxgEUbD4At597NCgAbjodkTEf5XS_KxjBnTC1bDBla5eRuwHxDYG70MiGieIOJwjI-zQypRHn3-HNdOJ7MwTShTiQ9M0062EYaH8WOp0S-RYZdFbOljWi_K8yEV7uk9frrJ4OFszwHT9R4SNCKZn9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v45pZAXQGO7sOXAK_xSjgcwofvVLtQFbhM-sKyZthhXDPtlLD94k6Ku7mYnpwCFEP1xjxhCfIkZQTNjQIW7GPkH-VD52SSaXn9nCuSWxPkB9NrTG4kpCW0VYNPHo7jE5VLmUMzh6ICxt4nhtOGhK79I2auKBNHV7uzEp8F4r2smO1mo9vw_MHgX81aYCQDeUQrpv-iY6RmW2oOil0Pg83ChGee-QPQ1Xr3DzSzqJ0zNekbdEXCD6ZsJ0mQmPnfEZsJ0M1mZj6USZmkZef1pyJHsSlKsH7X5vUeRYNSRmIDQIkugIfJzH9b6a_VSkdT1tWljM2ogRFbmglvE7tIIG9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امروز روز جهانی صورتیه؛ تبریک خدمت تمام صورتی ها
🩷
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/95450" target="_blank">📅 18:58 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95449">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mZOn1iT-Wn7Om5liH0FUk4Cv6aNlP5aDHaUu6sfxndhwgMywPs3bJTA8jvzpX0oPFvyadesHqbh6lTsGtsFr0L382Zj9jg2cO8eAU57Wo6nRTX9mFPe1sKw9nx1PRw1jbIUNXR8UzKjOwtm88ca5GgEBFdDsMwfy3F8fCTuMtGwVUlJGvCSgo-ZamUfV4tG1br0184ncOlwz3C9iqZ4sqASaTJyrnX-NXdR9HDV2z4AHSAMjBf23xxe0EWXmsvxTgr5Wom0DAJ43fCq1-iMUmtXnA6NFVcncVRD86pMDBmkX56CVgUT5iH8i75g_2LOyizSjBTB5ULdCxD33WROrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کلوپ حسابی داره از بیکاریش تو جام جهانی لذت میبره
😍
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/95449" target="_blank">📅 18:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95448">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53d1eb5a1b.mp4?token=rAiOJtcIBT8m52AN_3nHraNaf7XA7CAUaf8T9YqqYAgqAkZERA3DhBhTuFp9gcbfxlhK6_MTgK2o51GYsFwcL8BZFj6Oo56wTAEkOQ7qx9mFLeT70yTz5n9cdWDIS8kftWgy_sP7R-72pv5Uk6WekjZL3XY_ZFMgnD7aeKyLKluGC13YhwrG0s41B3dXrsayfSvZltoV4eTV74haeyjdJCxQNmescfXGqyhHcMA6tjUG3OHbbvNhexA2CmsESUGByg51G_rcDVSycJBmDACgZ-egrF4eY7he3LFxgIGRW5l7v4V5vkLNmjPn9Nez9ucG7z0PTpFkSqCQbSxsAkWQIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53d1eb5a1b.mp4?token=rAiOJtcIBT8m52AN_3nHraNaf7XA7CAUaf8T9YqqYAgqAkZERA3DhBhTuFp9gcbfxlhK6_MTgK2o51GYsFwcL8BZFj6Oo56wTAEkOQ7qx9mFLeT70yTz5n9cdWDIS8kftWgy_sP7R-72pv5Uk6WekjZL3XY_ZFMgnD7aeKyLKluGC13YhwrG0s41B3dXrsayfSvZltoV4eTV74haeyjdJCxQNmescfXGqyhHcMA6tjUG3OHbbvNhexA2CmsESUGByg51G_rcDVSycJBmDACgZ-egrF4eY7he3LFxgIGRW5l7v4V5vkLNmjPn9Nez9ucG7z0PTpFkSqCQbSxsAkWQIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
رونالدو رسید ورزشگاه
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95448" target="_blank">📅 18:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95447">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EmNmZwSA3C92m7QVH6ptyLwzSJ0TAZc1KvMu3yZe5oeuR1TDrebEx8VDDRTDYtVZ3YBAcWLldmZHw-MqsXLBVwPh08ijiaIMobIBVPMWm7okiWpVc2qagL_xgEFOfegbpxFe2mxqhIIiMEGCT3ZCKwIKHPaOsy-kAO1TscBCAPBiCgUv50ikDnOhnUlIbijiMzHQu1S8UUqxwapQ5zi7FdI7nk6ZZTWQe0XhV2dhxyCJPQXYnRHVO2TpwM6PYaBlJQ8te5xQ49yf6efRTJpwq2hkNGF41vbPnaucclceT3sIfDNGwgpxTIG0fj_Zol5SnbZ9imFv8PtlMqSLZlAe-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
نزدیکان نیمار میگن نیمار از همیشه متمرکزتره و این جدی‌ترین حالتیه که ازش دیدن! اون داره روزی ۲ تا حتی ۳ جلسه تمرین میکنه و چند هفته‌ست تقریبا هیچ دردی هم حس نکرده. توی اردوی برزیل هم این باور هست که نیمار از نظر بدنی آماده‌ست و میتونه تو ادامه جام جهانی خیلی تأثیرگذار باشه.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/95447" target="_blank">📅 18:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95446">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/657bdb6ab5.mp4?token=bYGa85I0R_hlm3Eu9v_HtVVjLw5a-sNNkZhGNG60oklRLgl0AGq_XWTW7277ta7TGLKBpRbzeM6rwPKIrauNlvXfZw46oeMnQnMKJWBj6bqYsqpH0lu1S5j7XUYOs3UrFPXg2Vu532a-FaWDaIA0Z5vmsAZhRc3oNHGSWMo-B7eUx9zbh1gbsDrSUsPAt5EbzgdkgYsSkhGIl082Nc7GiiqKafg567ENmrrXwUZluWRT8DRSW7GxMH3YL_rDl7mjld_mN3ODMcoOq7Wksb6446r8u48I589k7HNmVPU0ybO9iIotRA47mFRq1d5RU-zohwy6_TgIDnGZiseGcsW7N3I0jrNn04wOIGO9pTENXedIClhZVLRkzbDbO8ash2csGjCQGM8hN7JYZARro40lzmwK4On_1_PZfq1jUI22rR2_mPr2lxY14XXFKWuIYwkPV0lMNBFuQEjXNPICnjIn47vH5zNmR1_M2s2f00USmbeOVlZqLUP0WVEQQsphJS4FFOpiQgsLftwnqA3o8HjzEgbH18Wj3Qj84AHJQrOkwr9d_Kl4WmLjhwMAiwlCpcc3n6e2lTZhhH5-sORXEbhAY60JP5lYJgoG_1WxTBj7w5PZujusUsezFU0e7rU3S9kbyEgvUT3q2MlvoSMiFWEdhSyroUvuxtIxz5U7Byj6VEI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/657bdb6ab5.mp4?token=bYGa85I0R_hlm3Eu9v_HtVVjLw5a-sNNkZhGNG60oklRLgl0AGq_XWTW7277ta7TGLKBpRbzeM6rwPKIrauNlvXfZw46oeMnQnMKJWBj6bqYsqpH0lu1S5j7XUYOs3UrFPXg2Vu532a-FaWDaIA0Z5vmsAZhRc3oNHGSWMo-B7eUx9zbh1gbsDrSUsPAt5EbzgdkgYsSkhGIl082Nc7GiiqKafg567ENmrrXwUZluWRT8DRSW7GxMH3YL_rDl7mjld_mN3ODMcoOq7Wksb6446r8u48I589k7HNmVPU0ybO9iIotRA47mFRq1d5RU-zohwy6_TgIDnGZiseGcsW7N3I0jrNn04wOIGO9pTENXedIClhZVLRkzbDbO8ash2csGjCQGM8hN7JYZARro40lzmwK4On_1_PZfq1jUI22rR2_mPr2lxY14XXFKWuIYwkPV0lMNBFuQEjXNPICnjIn47vH5zNmR1_M2s2f00USmbeOVlZqLUP0WVEQQsphJS4FFOpiQgsLftwnqA3o8HjzEgbH18Wj3Qj84AHJQrOkwr9d_Kl4WmLjhwMAiwlCpcc3n6e2lTZhhH5-sORXEbhAY60JP5lYJgoG_1WxTBj7w5PZujusUsezFU0e7rU3S9kbyEgvUT3q2MlvoSMiFWEdhSyroUvuxtIxz5U7Byj6VEI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
خوشحالی پشم‌ریزون مردم بنگلادش از گل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/Futball180TV/95446" target="_blank">📅 18:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95445">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/761652d2d6.mp4?token=kMUnSxDJ4KJkv-YJncUtVT8HTID9rqQN7rSszQjRQUu48dS4EICdhGmTyRIE_sUONa4tTVZro36vCgcd4ln9qI1h2ucs22JT0Oc7sZz2JPQ0khm9TpjJpqcdE0m-br85Ux3RtPM0pkNSmrLDgWVEmBVJu9YvlsQAQo4VWxsOpdfKM994cTbLA9KoBw0CD9FyNDJwA3bvmXsSZMyrzdqj9Ud1uuOt1Piv8lDL6JHzbEwWbCj-hLnwvDyp6OdYIXZvyOD35gqeAlMa1u-n1DXEn6PcfQ5jYNT8Ao0wfnOI-2WrMf_9Y2UZixEwXgdV9H3ITeZIm6ot6hFM9yqm4yvaMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/761652d2d6.mp4?token=kMUnSxDJ4KJkv-YJncUtVT8HTID9rqQN7rSszQjRQUu48dS4EICdhGmTyRIE_sUONa4tTVZro36vCgcd4ln9qI1h2ucs22JT0Oc7sZz2JPQ0khm9TpjJpqcdE0m-br85Ux3RtPM0pkNSmrLDgWVEmBVJu9YvlsQAQo4VWxsOpdfKM994cTbLA9KoBw0CD9FyNDJwA3bvmXsSZMyrzdqj9Ud1uuOt1Piv8lDL6JHzbEwWbCj-hLnwvDyp6OdYIXZvyOD35gqeAlMa1u-n1DXEn6PcfQ5jYNT8Ao0wfnOI-2WrMf_9Y2UZixEwXgdV9H3ITeZIm6ot6hFM9yqm4yvaMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شوخی سمی عادل فردوسی‌پور با لهجه خارجی طور اللهیار صیادمنش
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/Futball180TV/95445" target="_blank">📅 18:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95444">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e592eb1d1d.mp4?token=aZVKPcE4HcrNxkLHKnPGuG78JxZHpqE_f-OW3JVeK4sa9qFV-iHICPIsDKoetdY1jWFFVL4qHTKym-kTY9DHITNx03WDf50l2ZRSiXW9btqs25UbSFthlNdStk57Jpx_XEJiR7uGOiGnclV9kwOYEYa5E-jvIlDdvsxT24vZBnFCoEV-pyZd0zkcj8HOEI-muQxwm7AI1Vh2e3nZiIGINddsR76rSCNZ96tR001HDwJtzuArrIoplOO3w5aT3XIdXVLa9eySVSkDkVIhBIyoZM-hoGvgFwCXWb6w_C-JQmzrofffT1S_ciIQs5m7_whyIMvQ2rzDaU2EHdm3GhYrww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e592eb1d1d.mp4?token=aZVKPcE4HcrNxkLHKnPGuG78JxZHpqE_f-OW3JVeK4sa9qFV-iHICPIsDKoetdY1jWFFVL4qHTKym-kTY9DHITNx03WDf50l2ZRSiXW9btqs25UbSFthlNdStk57Jpx_XEJiR7uGOiGnclV9kwOYEYa5E-jvIlDdvsxT24vZBnFCoEV-pyZd0zkcj8HOEI-muQxwm7AI1Vh2e3nZiIGINddsR76rSCNZ96tR001HDwJtzuArrIoplOO3w5aT3XIdXVLa9eySVSkDkVIhBIyoZM-hoGvgFwCXWb6w_C-JQmzrofffT1S_ciIQs5m7_whyIMvQ2rzDaU2EHdm3GhYrww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فودباله دیگه سخت نگیریددددد
🤣
🤣
🤣
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/95444" target="_blank">📅 18:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95443">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jLRP8a3mFhuWMTbE9H1fbAgOpK7X02TvvXgCcp9sAgzqmQFK10aEaWXxrwl6-G-iZ_TOmmYsV_4cK83J7EFtdTxRSlyLdYXQC861cFqOsX7Cmp3ifN3PR1GP10z9lTEz-oKyrHG7lp1RN1eoFw1qifJvODjvbDPIvE8NVeFsDxO4o_iKXRy_If1P3qn9QKgYs29V-bsqD9iDyqBZJWrN4mLUvfInj815xFbBNlvh2qFlZL2pC2JSEbMrJubocOPLh3g_CCH_mkGM-GW0X5PhLOU30x0bf3RWIJ01kzBmSMi-Vrn_8sOI1sT4kFYTZgK8nnB821HaX-dgywXUleY-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
طراحی خلاقانه نایکی برای لباس نروژ، خطوط روی پیراهن نروژ از نمادهای باستانی رونیک الهام گرفته شده و با یه طراحی هندسی، حال‌وهوای هنر حکاکی‌های سنگی وایکینگ‌ها رو زنده کرده.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/95443" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95442">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c332525e0.mp4?token=SwiMjc4L1pCrkVY67ewsY0X6SMtNW-xwO1sUgfJqGrWgwkWz2ccVIXlFromiei6DWf7S82z1WKjeTjpOyidFMnPtWWeu0dl33zuzs5E-87m43ihhxa437UrqXTgsIaGXLqLUW7bPC2raFCe2QWBwo7r3hIjQz_X3pzIZQ6yq80rulYxi1sIMqgZmzl72LwVoofhPjoDqzaDmWOkZvL8Mz-REKuKk5VTgVqrt_jcYWgQ1s4rTJD7vWIKtuigcM3JWhHdgtotHu_M20xVLhTpO3NlZqDHpg-wWSTDqq_Gb3gq5RhP3_1sS-fb1IDH9qypzFIpZ_II2zQeqTL8UACTXzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c332525e0.mp4?token=SwiMjc4L1pCrkVY67ewsY0X6SMtNW-xwO1sUgfJqGrWgwkWz2ccVIXlFromiei6DWf7S82z1WKjeTjpOyidFMnPtWWeu0dl33zuzs5E-87m43ihhxa437UrqXTgsIaGXLqLUW7bPC2raFCe2QWBwo7r3hIjQz_X3pzIZQ6yq80rulYxi1sIMqgZmzl72LwVoofhPjoDqzaDmWOkZvL8Mz-REKuKk5VTgVqrt_jcYWgQ1s4rTJD7vWIKtuigcM3JWhHdgtotHu_M20xVLhTpO3NlZqDHpg-wWSTDqq_Gb3gq5RhP3_1sS-fb1IDH9qypzFIpZ_II2zQeqTL8UACTXzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇦🇷
واکنش جالب مسی وقتی خبرنگار در مورد بهترین گلش در جام جهانی میپرسه...
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95442" target="_blank">📅 17:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95441">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMXz2mSpOvH8mcBwBZg-ArB4KpEC4nNNAHbFQlVP6N0L0IurdkbD28Ma8mzcjCw9Ruo4aN0A_l-Nd9GYUt69hiyAQFmmBWqV7KGrXtjT68pCHWkLD-p7xVMEFSQue1x52nvbhAD9Vz0w78sJ67FE_QCED8612agZ-3rBbBQ6v0KzYd84aNwU6eQXVD7xX3Wyy_8ApAaTya6vpdxyMmzgzElUrwbWvh0s_3Et6-YSrVaigqzCgiSguy-xTwWSQvaKLnCBNmGVS6NRX9-SKwi1MFMdM-SosG-j1hgPoqFdd4CXYPUh_aMp3DHep6MbElgAnBF-WYICSXFHb3F9saVT1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
توتو اسپورت:
یوونتوس چند بازیکن از رئال مادرید را زیر نظر دارد.
دنی سبایوس، فرانکو ماستانتونو، فران گارسیا، گونزالو گارسیا، براهیم دیاز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/95441" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95440">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c26ebe56f.mp4?token=j45ay5LmYC2GR6vuVX5jE7PnS32TlOy4ZeIBFx13wVQKl4H4qldtMlpgxMhQG3_vS9n6K1YWiLYm10neu6vgCED6M2tH0JRd7nfHdO1Pfz6pMBjUdkVNINwi0JNFnGA2I6FXAv-RGDn-V7H0FOJ-tjaCLzv4HjZTkkU-AY6UOA63WvV2HV5-nsdPkd7JsZo_Gb1jnOpyP4DhQC3dg4PLX_oEq7xbVv73UQ_ukLkfs9scs5nAkvaPvDv-E-2mI7YCafZzd_in-BJjzHgIddQKxEHOqzMVDsP_KOCTXhQBF-3R4VpcAay0Hv_kcrpa6Ob2wzbLbH5n2Gbft0PX8_e4uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c26ebe56f.mp4?token=j45ay5LmYC2GR6vuVX5jE7PnS32TlOy4ZeIBFx13wVQKl4H4qldtMlpgxMhQG3_vS9n6K1YWiLYm10neu6vgCED6M2tH0JRd7nfHdO1Pfz6pMBjUdkVNINwi0JNFnGA2I6FXAv-RGDn-V7H0FOJ-tjaCLzv4HjZTkkU-AY6UOA63WvV2HV5-nsdPkd7JsZo_Gb1jnOpyP4DhQC3dg4PLX_oEq7xbVv73UQ_ukLkfs9scs5nAkvaPvDv-E-2mI7YCafZzd_in-BJjzHgIddQKxEHOqzMVDsP_KOCTXhQBF-3R4VpcAay0Hv_kcrpa6Ob2wzbLbH5n2Gbft0PX8_e4uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون خاطرخواه همیشگی مسی هم دیشب تو ورزشگاه بوده. کسی که تو بازیای اینترمیامی بارها به مسی گفته بود دوست دارم
🤓
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/95440" target="_blank">📅 17:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95439">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W3UEQYmb0u0f4C4rajWCsm_Kd5cygkRor0JKvwcyyllhdYK4YezZytCCCmskdYcbUKcH6BKhGq-I9of8cRzRdn-LvQzvIMHqB_j_N-1sW5VDOs1IOpVV9Coi3NkWkc94gzpqRWpV2B7N9hQvI1LB3v1BLyIpoxTcwnLTVVEs7w0k7mcEOz5wTT0RZXoM3dwAFr2I7JGjrKkKZTM4kfxZdR5ZgVGTPA-pGNoZn1Hi7h4NmAWtB1JjVwsw9cpWm4fwV3dtMY4csYreZBOR9bE4vgERQ2qwH2_dCuAJwsHNbZAXYl5GSIA8v_2S2zd0ue3fPgJni7Ph56nyeIH1eAaBpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
اروگوئه تو 10 بازی اخیر بدون سوارز
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/95439" target="_blank">📅 17:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95438">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2ba609d7a.mp4?token=a3DWzBo4h1CYA_qj0lsXXmydLrC4RVUY6lPhuLGuf6sORUiEJt5bk7lq-xXtD66PUf-qyjZfGW-43bZ6Eg318IJegAUAJ19vRZ0tvUbtRM2qPfY08ioCdyBA_pieHn4ENsvyP7oVfD4-fgTKLNcNcdGFWAsMmPRa1Ys5cfHQtuSQ4xwJZIs-VR_LLIGGQ_YvZyi7ySr6Rv9vOaieytkQvU6PO_Gyk026qCfQzN3UIHKMN2bkuxqZepl7Jxx8VQwniK3eLyv0pw-ZeJsqOzb0r4j76lLcW_IYtsKk66xo79h9YxSfSJhrXEOJrwXxmVECbgphsTxUgDSTgB46n1DzaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2ba609d7a.mp4?token=a3DWzBo4h1CYA_qj0lsXXmydLrC4RVUY6lPhuLGuf6sORUiEJt5bk7lq-xXtD66PUf-qyjZfGW-43bZ6Eg318IJegAUAJ19vRZ0tvUbtRM2qPfY08ioCdyBA_pieHn4ENsvyP7oVfD4-fgTKLNcNcdGFWAsMmPRa1Ys5cfHQtuSQ4xwJZIs-VR_LLIGGQ_YvZyi7ySr6Rv9vOaieytkQvU6PO_Gyk026qCfQzN3UIHKMN2bkuxqZepl7Jxx8VQwniK3eLyv0pw-ZeJsqOzb0r4j76lLcW_IYtsKk66xo79h9YxSfSJhrXEOJrwXxmVECbgphsTxUgDSTgB46n1DzaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ارلینگ هالند:
فکر کنم گل زدن تخصصمه... راستش مثل خیلی چیزای دیگه، من فقط توی گل زدن خیلی خوبم و خب، یه‌جورایی خوش‌شانس هم هستم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/95438" target="_blank">📅 17:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95437">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/EwsZTjzjI_WmVS_DOfMaA-EebcFB_-zkM5c8puovIAZKze9sZ69Bc79UUJVmVkdYjqCDRXHDjuH5nJYQnIfNuRl-4hO-M6fVLReiBy7Ksup3zq7gO5bfWmH29Fh6NJFwJSzqx1zvyKTmDZqXoVGeQ3jpgmzQQk-6RKmq-e7c06bm-Igz6HfU5hbUmZATY8uj0nC7a6ggXFRLsF_4xY8lrv77YBBRjLb_wUfrv-zp5eOcKAR58OSU6K9Lv4OPTPZFztmuVd4cs-fNW3x2dOyQG5T_8tHmQ1RjIRU7QZjJXWvPZmwGV5gbQ_x22Jx3gzhoCE-uU0sBpEiGb_e1zwRZbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
⁉️
مطالعه‌ای در SSRN با عنوان "هویت سیاسی فراتر از سیاست" نشان می‌دهد انتخاب بین مسی و رونالدو شخصیت را بازتاب می‌دهد. این مطالعه شامل ۱۰,۶۶۱ نفر از ۲۶ کشور در آوریل و مه ۲۰۲۶ بود تا بررسی کند این انتخاب صرفاً سلیقه ورزشی است یا نشان‌دهنده ارزش‌های عمیق‌تر.
🔵
نوارهای آبی = تمایل به مسی
🔴
نوارهای قرمز = تمایل به رونالدو
👤
چه کسانی مسی را ترجیح می‌دهند؟
◾️
ایدئولوژی پیشرو — چپ‌ها و پیشروها مسی را ترجیح می‌دهند.
◾️
علاقه به سیاست — کسانی که به امور عمومی توجه دارند.
◾️
تحصیلات بالا — افراد با تحصیلات بیشتر سبک تیمی او را می‌پسندند.
◾️
شخصیت متفکر — کسانی که عمیقاً قبل از قضاوت فکر می‌کنند.
👤
چه کسانی رونالدو را ترجیح می‌دهند؟
◾️
محتوای کوتاه (TikTok) — کسانی که تسلط بر محتوای سریع دارند.
◾️
اعتماد به نفس بالا — کسانی که به خود بسیار اعتماد دارند.
◾️
گرایش استبدادی — کسانی که به رهبری قوی ایمان دارند.
◾️
جنسیت زنانه — زنان کمی رونالدو را ترجیح می‌دهند
❌
خلاصه: مردم جذب بازیکنی می‌شوند که تصویرش با ارزش‌هایشان هماهنگ است؛ مسی نماد آرامش و تیمی بودن، و رونالدو نماد جاه‌طلبی و فردگرایی. این ترجیح سیاست شما را تعیین نمی‌کند، اما ریشه در انتخاب‌های ناخودآگاه شما دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/95437" target="_blank">📅 16:59 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95436">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b088ab51e3.mp4?token=AU_5B9rIOn9yJlAarBg9lXMuj3OcB7DUA8CPlDly9vAMtc-j526r0lJFbQQBv9lugO-q9iohT7WaU10kTZ8TFltVw8R2FAh_HK-BwsP9U3oNx7DESjGRXgwMPzZW8Z1OPRA0DzO96LUsrJ3TeFgqWOT8_9cTMGcUicwlCjopMpiCrSZgsDhPzuou-R5EZrG6z0EaFPsXfq378CYJeMZ4itw_U6XYeO7W4KU8EXsn--ElcqeHzoA6giUxTJUyZHxucqObWxqjdjKTTG5v4JucIjZQnr9QOhEsF3r95NLZh8ZYr2B1kSrVWO-eHNBNIrKLypbNKRE9V8HeGZdqpCbCtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b088ab51e3.mp4?token=AU_5B9rIOn9yJlAarBg9lXMuj3OcB7DUA8CPlDly9vAMtc-j526r0lJFbQQBv9lugO-q9iohT7WaU10kTZ8TFltVw8R2FAh_HK-BwsP9U3oNx7DESjGRXgwMPzZW8Z1OPRA0DzO96LUsrJ3TeFgqWOT8_9cTMGcUicwlCjopMpiCrSZgsDhPzuou-R5EZrG6z0EaFPsXfq378CYJeMZ4itw_U6XYeO7W4KU8EXsn--ElcqeHzoA6giUxTJUyZHxucqObWxqjdjKTTG5v4JucIjZQnr9QOhEsF3r95NLZh8ZYr2B1kSrVWO-eHNBNIrKLypbNKRE9V8HeGZdqpCbCtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
🔥
حقیقتا مسی و رونالدو چقدر خوشبختن که چنین طرفدارانی دارن
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95436" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95435">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0dbf8afa2.mp4?token=EnUjuUg9_HL7Xzc77gP32NERQ2ku3C6sd9shoY_LLC2Hgq1BXNICcwcx30_YYtykwX44T7-HylX1JByfivZ5eVw5ZZ1HLqbFr1hhh1Txszpf12f-5KQjYpO-VBow-xolmPZHLvAhTqSK6gXo8nnrp_sKaItWk_DLfEwaQh2ZoloTBvZoDkCrDKBKPnuafZk-cDjmxMvCfXOVYdzqMh605GTOItLYNbGgJfQJ5n_OavLA-ZCNLpjx7MdiT8yzO1dtt41rJYGRlmJgrJ9To0SfnS0fOdeJGsouVbgy3YeHzaxi0UyRX59LzYc02WuUZ_1wpoKqSw8833NT0zxBSixVGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0dbf8afa2.mp4?token=EnUjuUg9_HL7Xzc77gP32NERQ2ku3C6sd9shoY_LLC2Hgq1BXNICcwcx30_YYtykwX44T7-HylX1JByfivZ5eVw5ZZ1HLqbFr1hhh1Txszpf12f-5KQjYpO-VBow-xolmPZHLvAhTqSK6gXo8nnrp_sKaItWk_DLfEwaQh2ZoloTBvZoDkCrDKBKPnuafZk-cDjmxMvCfXOVYdzqMh605GTOItLYNbGgJfQJ5n_OavLA-ZCNLpjx7MdiT8yzO1dtt41rJYGRlmJgrJ9To0SfnS0fOdeJGsouVbgy3YeHzaxi0UyRX59LzYc02WuUZ_1wpoKqSw8833NT0zxBSixVGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🏆
صحبت‌های شنیدنی ستارگان آرژانتین درباره درخشش این‌روزهای لیونل‌مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/95435" target="_blank">📅 16:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95434">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ofO817xT_EjQCZT6q29HOcL6kroQhyryI9KASlzB5hA4_WQH48g2HZY73dOidy_FhH0mjJ9Qm5Us1c9feux109r9lV1nbMmIZJATm8gDCG3j226Xeky-kH3j8yTFUqQ5TMgN17kaue3W3UxiMS3rl_tl1EL-HMCuwF0JBAZFSAhmrPPUMUlIV-EbUerOnNoI350GBebugizlDj8Cd-WBpa48dDhzrbm3IZj5JVyHrIEPK3DQSLe9wFKI97J3Fv-kNiE2eOGAgdXVLGV6S7wuU8TyYuhG62JjiLt8XGo_mUkCSapH_0A50EEU3ZOpSfU1VBkohsAhAjPim6Z3WSJ5RQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نبرد امتیازها در «همراه من»؛ حرفه‌ای‌ها جلو افتادند یا خوش‌شانس‌ها؟
🔹
لیگ پیش‌بینی جام جهانی در «همراه من» وارد فاز جدی شده است؛ حدود ۴ میلیون کاربر در این رقابت که جوایزش شامل سیم‌کارت‌های رند ۹۱۲ با کدهای ۱ تا ۳ به همراه گوشی S26 Ultra برای نفرات برتر، یک میلیارد تومان جایزه نقدی روزانه و قرعه‌کشی روزانه PS5 است، حضور دارند.
🔹
در صدر جدول، کاربرانی دیده می‌شوند که بازی‌ها را به دقیقه ۹۰ نسپارده‌اند؛ فرم تیم‌ها، ترکیب احتمالی و نتایج قبلی را بررسی می‌کنند و فقط بر اساس علاقه انتخاب نمی‌کنند. پیش‌بینی دقیق نتیجه، امتیاز طلایی می‌آورد و می‌تواند چند پله جایگاه را جابه‌جا کند.
🔹
در کنار پیش‌بینی‌ها، ماموریت‌های روزانه و بخش «تیم دیجیتال» هم به ابزار صعود تبدیل شده‌اند و صدرنشینان با سرعت در حال انجام ماموریت‌های امتیازدار هستند؛ امتیازهایی که شاید در نگاه اول کوچک باشند، اما در رقابت ۴ میلیونی تعیین‌کننده‌اند.
🔹
همه این رقابت در اپلیکیشن «
همراه من
» جریان دارد و لیدربورد آن لحظه‌به‌لحظه به‌روز می‌شود؛ جایی که هر پیش‌بینی می‌تواند چند پله شما را در جدول بالا ببرد.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95434" target="_blank">📅 16:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95433">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔥
خیابونای بوئنوس‌آیرس آرژانتین هنگام گل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/95433" target="_blank">📅 16:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95432">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V9ke4DB1B9MSl6j768a06QYLrE82e5pDRmeJIuUEp1JEqQQt0uqzuHB8F4ZpXgxBmOHcbfn3lgo8nyAPbkfyW6vk9WgdWGc7WFzTW9P31TDMaIzvZGmcT-wVKwdThONGxEn2AAN1sMWn0WMj50qN5yYioHuFzLylfyKc1n0O8-mH_TuLFsPb3kyzFA8rEPVPTIXrKU8X3OwYRsMA4FlHxvTp_uGOu2A3DjIb8lGsKABdG77gI4BrcrtD3uoscUhJKdpahc9E4ca2C57uGOLDND61iCmcbG2J2kt-mgc551ncxpiu3tb1boS3CgiWXFtUI-ZyP8CGQ44-Q0sN-SDmAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇪🇬
🇮🇷
#فووووری
؛ سیمون مارسینیاک لهستانی داور بازی ایران و مصر شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/95432" target="_blank">📅 16:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95431">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vgDgzarS2tTwOhYd2nnZsN2D2ZPufYFnlmQhr_zWAhH6GynPPoT4sTSSBMpR1it1tnaZVk29PiMWr1Aa9HuepcSlilRSnCWdfAJjf0QNxDj-qJR8LvVqMGqZygxLgGWfdsJu5dQG_JyslmJxcHecpW1pgKwfnpZa-EQ7kSM8zaLn2zaTgmZJVEKug7PRhHoJ7sCXCDDFCr9VWOYmWgT9lgnhGwEQLiYTu2NXG4n8_HS0R0NBJW38ExFH0fOID0zIxWvDfcQkhY0YP3hyETfbVHsLGetth3cAXeB-U0jyslTD2MPi2YJtz8MN8LMWuOB62ZH53c8CsXDyoLry4vHdqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
از وزیر ارتباطات به خاطر عملکردش تو زمان جنگ تقدیر شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/95431" target="_blank">📅 16:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95430">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf62186867.mp4?token=XnUnRYLgHccUF-xRN8dQAq5902oyVNaBunjolbXq-qz4C566UCWJucv4bB-CtJeVODwXALdeK7S0KMPnLi-0zQ1R7kBNCQNj9lR1A7AbERK3yWDlcIeLY2uQJNaxivPWxXoGLbbPz-yUFDbX0UVUI-_vhu9ZUTbdSadEEkNx4tAbrmgDqoXwLbROiWCgOKEVa8vflQKIUm4-MT5GOEny2oi0r58sJlLRbWlccfTcuysT4PDspwylsJvrpOys9qufsNoEdYV7U0wXT7AumEGTEfPfITFdE_hhunIZqLrMypz9dA_P7TAakfiQdSGA-AiafLNzKyxCKesfKYxpKFUqGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf62186867.mp4?token=XnUnRYLgHccUF-xRN8dQAq5902oyVNaBunjolbXq-qz4C566UCWJucv4bB-CtJeVODwXALdeK7S0KMPnLi-0zQ1R7kBNCQNj9lR1A7AbERK3yWDlcIeLY2uQJNaxivPWxXoGLbbPz-yUFDbX0UVUI-_vhu9ZUTbdSadEEkNx4tAbrmgDqoXwLbROiWCgOKEVa8vflQKIUm4-MT5GOEny2oi0r58sJlLRbWlccfTcuysT4PDspwylsJvrpOys9qufsNoEdYV7U0wXT7AumEGTEfPfITFdE_hhunIZqLrMypz9dA_P7TAakfiQdSGA-AiafLNzKyxCKesfKYxpKFUqGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید لاشی وقتی دیشب تو بازی آرژانتین مسخرش میکردن صدای سگ در میاورد
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/95430" target="_blank">📅 16:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95429">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jiiH9XZTfnvEhMDPjfvLfYUcBLTNb_0k21A6ZLEsDJgVUkbXBHbAk841caVRVffpXmWVc_tNIiMgX7frrjEfAYx8vHqWkhwgkaPbq7n_6hV1TwDssFaMlOiBXO2HkopeC8umnl8p4xiSzA5Ovylg4fWSjDh0CzihEQG3kSUGJstLC9n-0yM1DvztIBP0Zn-btU7h7hPR_OcbYgvpJ975uJ0mpXFyTci2Wr4lDRiwBaRuz-3J5TcRnKzBfliG2g3TDQRVi7PyJ7FlPMDFy1K9g_9GVsX4LiIamp1jl6J5nGLhT7M4J92BfhaLe_FFGUGuuhmq0KpQcrVmvb58d_Rt6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📰
🚨
🔴
فوری - بیلد:
لیورپول درباره فلیکس انمچا استعلام گرفته و مدیریت باشگاه از عملکرد این بازیکن خوشش آمده است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/95429" target="_blank">📅 15:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95428">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aeb7842be.mp4?token=J3oKyVyhqSIGe0pK8LnslQ7NLA4rQngJWuS3lm-sKSXDssxA-wS6rrJEmbYFcDRE2kJybXDP-DBOKOsHooC3_LvMqmyYrQC08F3_RXOl5Ecr86r3YAdFaa4PIiBAGxQpQ-_kitzMRszu0acwi-IhOCIyk9mPyPd91af62k_vXfFFdpyaOgjjF2N1RX2sYM0-EcMAjB5W6GFjZSL1z4XMcMXaxYrwulZlI50TVwrKhsFgOhAOzbMAtaOugmFY2-jBb6BIdmN-pPDcpcm1uNfeWmo13BBuKu6EC3-r-kvo2DCgCUkUKoVZZMkOyVipIWMPbC57KwexdVCd9UsP8hmr_UYBAVxDCl-Jaj9S0dOva3Tq4mEHZQQoLLX4jJ_XlR9gFfn8RqrVWpYCEG2A9QRt2USgF3ReHIppNswwByxVNND0_jYKFIbsjCtp3bDeBWCNKM9rU7MlEX1od4Jw1HuKQJ_RpmvLWhlNNipnb2TvSfF-LC2jL71PTO2j_6B-gWGu3oZUN2VQKAaMbV5wZMXngEwHX71HVgfiD3QVKQO8J27WGj_ZRZeM-miHZF4iBtQkqQJ_e-oLpuC0kOrJE8Hvy_x-mMKX016kGSYluNMLqcGrQoGlhivqs3dta_wz0Y-O0akWSdpuyZ6RhzlL7irHJZjzhEg8T2otmV5MHgJFx4I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aeb7842be.mp4?token=J3oKyVyhqSIGe0pK8LnslQ7NLA4rQngJWuS3lm-sKSXDssxA-wS6rrJEmbYFcDRE2kJybXDP-DBOKOsHooC3_LvMqmyYrQC08F3_RXOl5Ecr86r3YAdFaa4PIiBAGxQpQ-_kitzMRszu0acwi-IhOCIyk9mPyPd91af62k_vXfFFdpyaOgjjF2N1RX2sYM0-EcMAjB5W6GFjZSL1z4XMcMXaxYrwulZlI50TVwrKhsFgOhAOzbMAtaOugmFY2-jBb6BIdmN-pPDcpcm1uNfeWmo13BBuKu6EC3-r-kvo2DCgCUkUKoVZZMkOyVipIWMPbC57KwexdVCd9UsP8hmr_UYBAVxDCl-Jaj9S0dOva3Tq4mEHZQQoLLX4jJ_XlR9gFfn8RqrVWpYCEG2A9QRt2USgF3ReHIppNswwByxVNND0_jYKFIbsjCtp3bDeBWCNKM9rU7MlEX1od4Jw1HuKQJ_RpmvLWhlNNipnb2TvSfF-LC2jL71PTO2j_6B-gWGu3oZUN2VQKAaMbV5wZMXngEwHX71HVgfiD3QVKQO8J27WGj_ZRZeM-miHZF4iBtQkqQJ_e-oLpuC0kOrJE8Hvy_x-mMKX016kGSYluNMLqcGrQoGlhivqs3dta_wz0Y-O0akWSdpuyZ6RhzlL7irHJZjzhEg8T2otmV5MHgJFx4I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
گل‌دوم لیونل‌مسی در بازی دیشب از جایگاه بالای ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/95428" target="_blank">📅 15:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95427">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3912f4917b.mp4?token=cCp5DZ2maYryYGs2GNMbQGF2jfcovV5h3BKHl9fK3gY0abS5yi1vXKJVnguqAlxnkUJRuQgqfLce6PkyaksaKkIdu7imxwAb-a5-W0z4tKdbTNcCVQj9EoF9GJ-x7CwU4i89taV7IsNv3_mqs_u3Czxb3K24f5u6BMF5bbCsqHYRSm4Ra0Szetuy71Qmpb29dqzkSj6vMf1_Tsg8pCQEvZyWFNplFr1xbXIQPNQFqvYcGCNZKh9O4wbgBv1aqnMqMAIzuoKCo24QdEBCWLC9opaL5jQSrsALL2v2A_0aLiLtJGN_ve3sW5VKtWB9n2AoN8ezWCNcpW0KEdPWNqJmWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3912f4917b.mp4?token=cCp5DZ2maYryYGs2GNMbQGF2jfcovV5h3BKHl9fK3gY0abS5yi1vXKJVnguqAlxnkUJRuQgqfLce6PkyaksaKkIdu7imxwAb-a5-W0z4tKdbTNcCVQj9EoF9GJ-x7CwU4i89taV7IsNv3_mqs_u3Czxb3K24f5u6BMF5bbCsqHYRSm4Ra0Szetuy71Qmpb29dqzkSj6vMf1_Tsg8pCQEvZyWFNplFr1xbXIQPNQFqvYcGCNZKh9O4wbgBv1aqnMqMAIzuoKCo24QdEBCWLC9opaL5jQSrsALL2v2A_0aLiLtJGN_ve3sW5VKtWB9n2AoN8ezWCNcpW0KEdPWNqJmWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇦🇹
آنالیز گل تماشایی آرژانتین به اتریش
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/95427" target="_blank">📅 15:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95426">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4rdun3qulRCPKGWIkH9xU2el0LYohQ6okEkWU-Dfs09dbGFmb5-IZF8xo8-19nfUOPZxc3Ke8e2extj6Nf9qUqXWVd2wknzrdk6b6R4JGVmkQqVdlYsEt59L_pDSZB8M6C4C-Vjv2UujEpFrrFhBOee5sakaYLp3BS6fL8O2TZywYUdKvh3Wys_7vRcT1KJg_JlCnX5SkAcwaLPS_nHo9xuYFP8dFbFLPOaBSetZQzdqP5jQhDtO8uJz7tT8I__LYH2T-O0ojejBNgTVOuqyB8fbzRyynLe51xXxm_xL0JTu9JBUNCsPyB0IptKf-Lq9a7zZVdcp_0lLMAFoQW-sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
حمزه عبدالکریم بازیکن هجده ساله الاهلی مصر به بارسلونا پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/95426" target="_blank">📅 15:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95425">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5UyrfckzpTWkryG2LZnGhc4ULlLkUttPRhrf8d8WeH63yZUQRHCj9yWA2RtLb9dYboEolGyzYTjQGZZoCXROxwv77-uLVU-GRdc8DgdsC4M-ME-tG6L6ZrDGnlbjvWrw9fBVWnf8oZrTA9OyQM3px8Y6ssZOzPivkcPBNBHpLCzTC-s-rxemNjY7yLF6UxCsXmf1UKasj0eeCICIRiJiWo9lCq8sgZiewnwdf7GoH047m3IhB0lg50MxBGLVxa6315ntAQZOkThaiajhh-bf3EzdHmhi3ehnPuac_IuQRp-J7CQfqiSPlGwhU2e2c_06fmXZ5rC1Q3zHInbPE71Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
روزنامه پرتغالی A Bola یه نظرسنجی گذاشته بود که حدود ۷۰٪ هوادارا گفته بودن دوست دارن رونالدو مقابل ازبکستان فیکس نباشه و حتی تو بعضی ترکیب‌های پیشنهادی اسمش حذف شده بود. خیلی از خبرنگارای همون رسانه هم رونالدو رو تو ترکیب اصلی نذاشتن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95425" target="_blank">📅 15:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95424">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d665bb9f8.mp4?token=QLwqP3KmkHkA995_vOGaeMWvW2Ybqr6bs1fXANuigSNljfh4kw7CFGMi_plRwe3ynA4SkVu_zPFOr-e1RcnaK9q528FLfbB7uo75RJWfvKtGvGP5T2xt0P38piAXtM-64hq5OADH0imIsXiluK4hz303ss0i9cgyaa4B5VQTuvcDZcUroHgBcMQpL9uqTrJFtacfVqHNmVazpzCVcgxxhaZFghQjnV_oE5eFmsruySSpL7UVyMBvdBlr7I3Qq2S3YuIJSl_AZ6ykQrPdtbK2p2-sJQaByi3m1gP27VQ5VbWBgnmAgIOiEgsW-JKV3RZ9e_0DsYkJUY12ZUiA-FhG6w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🙂
🏆
تو حاشیه بازی ایران و بلژیک، یه بلاگر خارجی تو استادیوم میخواست مخ یه دختر ایرانی رو بزنه که مادر دختره سر میرسه و پلن پسره میره رو هوا
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95424" target="_blank">📅 15:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95423">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MC86VlvY_W_0UyhbqQBB2nHZI02zAsdHivfrjRDwk5gLG5cjpK_ndjpJRnhezjZVTYyQvRLUIvA_egm-e8lp03XNYQS7fi8mMX7G4qOkuOLW7smMqztmalcw76GZkVjJjtir3JwIvxLzAhFqbMlUYHTyPKSz_RRRhGbro5TEEKuY4WSyGw5Pt1Y8cOtm5Dy-qx9nIaGioTjBnNJCQesxP_Wf0BfYoWZxgEqmlrX-VU-1P_qhXwI_yaBkeceeaIqPvyYIjeBaI0eMP-IKkYT6IWe5Pcf-nhepufXcvoypLlF3R45OhbHprXKB2t5lg72JE9ZqFslwlOrIPUkZ0Wc6WQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
⚪️
آربلوآ با قراردادی سه‌ساله سرمربی فولام انگلیس شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95423" target="_blank">📅 14:56 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95422">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5r-vCPBASfkgC-9osaUEfVVceCnVwG3Y5m5JnLI9T-litllrz-fgSCm5jP9PHL403rVkv5gD8tnH466Ja8Kim7SLmTm1jFGiLcspk6_hKcaQuWKW4GVDlX5TyyhglCeyPYIr_c7-dE1sgsxaWCd_DNLo8OuGZHRJ_VSzVoqhdKDsej6rep-ZDHMbB98CGr8QTjQLPcZ10qOmuwzyMePJ-ztoiGcMVnuHnIeYKoAfgBe2vjZWGJHn7pdmNHTBtDw5xsTsU7TcYXt3T0g-V4oyNGPUtyoAxD3grw6ir1BZT5ae5Yo158I1_-KWLwNY0DeuvykxwKBUgy3T-nMDIJH-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
ستاره ها حسابی خوش درخشیدن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/95422" target="_blank">📅 14:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95421">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eed268b84b.mp4?token=HZcUtuwVFpX9m7XsiKPU4sArp9-Dc1hSr78zroIUXEk9PhmZC6b0bY1_lJjHL1EpRAguPkl7KL26pq6XRgxzDSh_HiAgxymYFwY5k-_T6OtoDDOe5BuP6zSe5xgr7rt3adWHVH4AAwDdt7m6eqfIvZDjToJ_-tjolHU68R0IJEMS1hedhj1mtRgvllXHkzywuioVYV99Mx99goYln7eqz6mphybbdwrlM9oWwCEKkFrgkFqTgK0PoUJNekc0_usxINCF6IfJnwVW9tc9f7F4d1J_l0muS37FXkeepXtlSOG4Eqr2ydkaydwPAAWTpd3SgsBzGLRzhCBHeziUuU71JISX82JezfHQk3fT6IdyUe9YcFuMcKklDm95-I6VcVxo-sgL1pjFUOVbefdhZBOx7d9MWR_eqkpFRpZMQonGNUU-jE2IU6P0vwrzrcO8A41oG2JMh6ATdR23o0K4Pnqis7uwCrVRbSYqCGuNo0Bs0R7Xu0pmfmm2qjpXYH3vomaBqe_1CQgWVL2_WavB1WrW3ByC5LntbalAc4EcnbYetLWn-w_ML8GQ2izZglNTYX7h_EkNXI07xEOj2xzBcq_MoRmZm8R-0MM5lExLzX53eym4kYuVbI54A6VJfe2F6b-qFc2bNQoshad9VjPeY9bTQ8KmwiT24jUtDtsUpo4j1L0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
خوشبختی برای خارجیا يعني اینکه آخرین جام‌جهانی مسی رو از نزدیک تماشا کنی و لذت ببری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/95421" target="_blank">📅 14:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95420">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AS-d1vrMxt6ISQ9C4wxKc6vQKyYx_xUrlmcfERQNdRlklxqD1rC_ZsiN95mY22OM_3KryctMuErBTQ4Mn-IsnNLhTLYbl5-FH3CTehqj6Khb2SmHu4N1a9Vdk-8YfpjMAH8MICUjw8vT2-zWF79InMp1jGk0d0khkT1yP7l1cSmuz4pSEHQOBYMu6mCq9zapIBmb1CyIjTcS6gxN6mtDX5yXe6lnH773E2-swq_3ztfwgN1NJodES0wPQnXUDLHVXx9uBgnqmWFAwGucPgO9VvL9MNK2dMyPIn9_vnWrUdVhXJF3Z6vxRQCxGO9ol9CguuM5FQLZTzFKdwLsg2XcBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دکلان رایس:
ما می‌توانیم هر حریفی را در دنیا شکست دهیم، اسم آن برایمان مهم نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/95420" target="_blank">📅 14:33 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95419">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/raApuMSaDlgjBwJvKFDL8gpFitW7Dfd7MG_BFfzVI8wgCPHD38qI9PNqJVmJ0pR-F5UcYr3zPgJw02cFk6XOxQxv858WJKWLNGVx22FkjoVRywnpjNIDW65AGdybxW0Bct5KkfCcW5pUyD0cimPa77J14tvIcDIWO3VfBVvgqhA8GH9W8HRw47mbI3FumeUsY0ZHyoGZfW2H8FR3x7DON2fC_LDtAgHitxH6EnZE8DskUuTrC97LyLkf3DkDo14nD86JbH8LXf-RVTCsxArhJMs0v3DxZfZ4Mt19vJAQigQHD7a7UPCWnbBpPfMtVeyxsUdJhIoxwajVpn94a26tbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🗞
آاس: انزو فرناندز به رئال اطلاع داده که از طریق وکلاش، تمام فشار خودش رو به چلسی برای جدایی میاره و مطمئنه که فصل بعدی به مادرید میره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/95419" target="_blank">📅 14:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-95418">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DNLp0WtFb2ekjA-Irl61DD7bqvNbdPJ7qotUZbcJ09AsOOx3CT7vN8VITCZSejL9EnG7cRHqMT62rKrAZS7YhRSdzrmd5PG7t7jNbYA1_XOwKz_lHkJvaSfa3E4hImLswVaDWeas5NHIflLKRsOY0eMwNIpUI8T97EuebVnAxVSxXN70EVQVXVAkWI3a6fVFlaXrhWOW2cb9kHxei1y38YcBeQW5_3xdO4HzNohRI3KyxP5BKYk6RG-79oyLAwmWKRA7pM07mqX8SAePbMIVrrJyQV2ZaMLu922mZzy6GglGUdGCp8DESEmd9RwwCDD0AAFnMGTHxKOdAQkQfBIMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فووووری
؛ منچستریونایتد در صورت دریافت چراغ سبز از رئال‌مادرید، قصد دارد برای جذب شوامنی به عنوان جانشین کاسمیرو اقدام کند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/95418" target="_blank">📅 14:22 · 02 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
