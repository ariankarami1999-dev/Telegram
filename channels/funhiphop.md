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
<img src="https://cdn4.telesco.pe/file/tXKYkniiWao3s_e6EefuYrklfiHigUF2ErfuoFQlZvpEjoHcu-8DQI_jUwyCnhZqyW9CMUBB6Xsf7ymXjTGOSz8sAkwjudV1y0TBhJRr1vXao73lbdbA26OX6CAzqaCtDL91Y9eIAW73gsqAFY3e2OtSOdxHoxZO-Gv5fNquYIXorEJqm_fDWOS42osKrEDOzjC86g7r0_V2DpIg1APqoErl9bk0aQ4OnPzDlUfMjVXcWQEaDeLk5N3zW1uETz84PKyeK70ioLQJlQTMLkvx31ChqPwJ-ytlh--m6GQKgcu4ARteexmwCqONpgCW6GMHsZLaCZhqgKLfzpKGaYTk2w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 231K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-24 04:34:56</div>
<hr>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfgAHE3rlCxN9DyHzfZWu99wZPePA10Jzo-jaKmXGq7JJU_XcJvx05QDftXzwOAFp6F3bJwqMN62ZmjgKo7vVvVpyIcc39RfaaLlb5SE8rgHKAyCv2675WOzLXw85ByuOHfyWeopj0uFPgLzobAtPk9du6j39Cjy9D8-hyctkxwX5liTOYnNWRcSPruLLTswc61ONYLarxBzy5Tws6J3uDD8GxzEOgJDAMCVDhumxurOZP963kOBcS4cjfKQu5wt0gukvms2ycpqyIPlmX0ix_u4kg07pyEoo66F5o9tX3dsjJMeMmC6QwPrj0c-80HkpZ313IDAn-jImPGEHhG1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآ وای‌لی برای سریال "The Pitt" برنده جایزه بهترین بازیگر نقش اول مرد در یک سریال درام در مراسم امی 2026 شد</div>
<div class="tg-footer">👁️ 531 · <a href="https://t.me/funhiphop/83475" target="_blank">📅 04:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNJ4SHWKrKlfvjQokahaSfY2szxILud4llpgUlhTq334y3IY1c9pTPb1oqdV-7N7iqJ_eq0w06-EKfWMMn1gDu3fH1V0IJ6sqBvSGz9IYa7aJFu37Y61eg2s0zcSbZXXNfu-FKWlvvnTE1IIwMx_UGC2uocjWcfsOh_alpVDb3ArEN9PeR9suhIrPtSHLEwRYGlOFQame_8KMtG1bBanjCEFdNHB0IuohKbGzhuMwTEo_pEamJFDytZWvMF-fIuzTlA5IOl_GrgJMVirGMJI2npdTyP0ur0u5rWF8ZB3n5UOnjEluV9XK6Tp_NEQgw38MLzCg14UIElqmvkdM6siVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjJc3ss-9Tx1fUpErkSW42UyMOVDYxSCW9Af7ohpecQmdoAQzo7Y3rOtGwxgrLfILORBNFkHTMYJ61cOIbFj8fv7nuCPj48WriZqmKVB4qr48L45lKLI2lC_Bwo0G3UEOv9kz6vGMTSgL2h1naq3hf9RSG0Qky7A0Je-MdcRitC6ykQKYLpQUMT0hkRPLDMajy1Qtxbf7HdxSvq2iK7Ktjqy7BLfRFTMYo0Smhn5k1ZT9-oTVwS0cNCJInjCA-frc_KzTyR7O7lEebyily8AT4fqG0xv5IKAVhtNlcDKtmmByy37C8GraVyMphbmeAGtv80Uc_4ce8P5uXIuTIRM2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سارا پیجون</div>
<div class="tg-footer">👁️ 996 · <a href="https://t.me/funhiphop/83473" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83470">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ov8MuPAHlu5AMZHH2-q9sZwURGFU__nlocSSeI59bo19ZrxANa6wZIIqAit46nC-u8l5ucLmAPXVaGbszUCtE-phU0F2ReytMvxAA2_vmGSJZqOUJ-XQPVKVTzNR1Mot8nGW7JLAE4GV6BzitFu1nGk3VXBhvWxTHZM8a7DMWVEmhSSO3_B4KcBbZ2t06t5M9nym9V8V7AIKIKrgXT-h6cFeO1QY1P46ZbYwodQTIZQPgxf59zPsWXRL7PGNGNAd0qwGf4PIKdHDrfPgJqXbpXCe4fudN6amwwYScnDKgW3QTjRfhTOTikhPA51MOt3tpHUK2J6IzEknqUBJdb4jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OB2CV-iZICBrTylZWDmxP0cIe1o_iARnjuYw8OGcb4nK0cjnpgMZCTR7dELSERut7MvmADh7JkiqaArK4Bdi_n4Vzu4ogGZMQ5iim65sG7x0pXoGvhNcoqhg0EY0FWTMdDLPOBYJh3fc6qN38vw5UmD6cuMaVZd94adoPmAqoSk9Wqy9ok9yRp6dBKtmTW0L619eY5NeVHQ7uOOQgQQ_By_Qdno_Da11BJIDBjt8ySE5u3lE-O3llp392Bt_HNSMWmZSnAi8WwAiwuhh2Glw5cC29IzVsolPuNSUeAS9fL151lNCci19o3k5ZB-j1hl9n1V0Ox4tenrqQ2WhDk0-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا اینجا کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)  جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)  متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)  آلیسون…</div>
<div class="tg-footer">👁️ 1.71K · <a href="https://t.me/funhiphop/83470" target="_blank">📅 04:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83468">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT9-xtqn2yoptyHopvaklqkLtUhMfk4RzUX26zzeHEhjLkC4ae197GocX1KOpXC3FZGPwBw0MNHAyrsyQ3646HLKywktN3sqUIbd3Uhp8dIm2jGiHm838STFFON4pkBheBXaB5TDSfd3EBGxnF4GVWijUrsM1JMiI27ZRtrivjf9NN0u3YKsc2Kc0qFuFUEJB7ZGYML2RvVG_NzSfCCgH7yb7Pz0Z7r6S3ev5z6AE-85K8lsoxKQTSMnf6IFzMtSDK5m6acs6NLPRBItanUXS21OfYFAfAPye621sh9XppVp6vIvoRyrdMr2gPUiU39HpTvrC7ODlGzuu4LuJaZFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kq1KAQmVpSGZUy5PpEUlgD4tR9eps4ui6XJKsOoFrlwCgqA3qYIgD8VAdZ0RqhgRYgVA9jib6chnqf-MfS1DaANpVF6ILvsc08T_Ieacq8YbNqV2v1ez_0dU6kZ8s98nm6bLFu2rr9BjPJt6ed0MgxHdABauR5zaXiGVuBCwmGPLcwASpNnwVd5r6DoY5h2K9cf55jnvCnefvHcy9FBFqIRaIAJmgtPJb-h35C7d3WoqX9HHqFvKNaoVdtFQ3Nh0wTf3rnJ1DNf9Zg5LyqSUuWp0g1kclzb0DeSZQo5_LuvICWQvV00MarnSTbKWJTCXFOVaE890ImRGC2tsbj57NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما درخواست پستون داریم</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/funhiphop/83468" target="_blank">📅 04:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83467">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تا اینجا
کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)
جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)
متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)
آلیسون جنی بهترین بازیگر نقش مکمل زن در یک سریال درام (The Diplomat)</div>
<div class="tg-footer">👁️ 1.79K · <a href="https://t.me/funhiphop/83467" target="_blank">📅 04:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83465">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSJBf6E_KjO_37xQENH7MSMizIWmNX-0jw96GkVpQFgS6et0mZzdwkwJKsvU_F5q-bZqq1-ZVGcBbCiRRyJk1QQpr9LgYwLT6N-ETb6YflNF3OqWa5yjUIgcTIYGX6B_BLE_LarbgJVmQfGENS3HkY8AeGNrcczFRGQCTNlV3Mj3ztZnAvzckor6G5mQl7iNlBBAIK5FYRM4VsBLiRuT6taKKFNRTS3HmLxw-zHGz2LqgGXvPGngDoAG_oPoZ8Xg7EZ5uabvJlw63v4S3EmGhUVCVUPV9eiuqsNFdS1bkJOqG3sIDu1DThUfLfxx4gDd5i48_v-5-UvpNejl9QzESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHUY4s0DWV9vU7nGplxsTE-GtgIRl9p8AL-V-LIf3jEjeH4oMTCDhX9LA7ox4jj2yDqtCWuj6X_swzI0vrXrHYdhvv03KycvDXD8JT6RtPXinuHTRdKmh3NR3SoQFE87fdNW_aUhHcgZmqdivu9yAJaRkcjw5Vgd2vyD-oLlr0tGTZSuKhK-FwfwHIBQ0erugidYeXx-N1Q9Q_QjLA5EGsTjgxyVmG0t7EwwR8a5kOmFiZSv1VUgC3pyFGpdfGB06jyiVw4mCHq12lO6ukJ-K0MUCPbUHmu27oUh-qjR2mSRcNmpx_ehgvlsRK4lFLB4OM1vlDwRUAjQHzpBxfsf1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اما دارسی هم با استایل تام بوی های دبیرستانی ایران حضور داره</div>
<div class="tg-footer">👁️ 2.01K · <a href="https://t.me/funhiphop/83465" target="_blank">📅 03:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83464">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">دوستان ببخشید پورن استار هایی مثل سیدنی سوئینی رو اینجاها دعوت نمیکنن</div>
<div class="tg-footer">👁️ 2.18K · <a href="https://t.me/funhiphop/83464" target="_blank">📅 03:55 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83463">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_vWTfP1oWH2K6IzdmC22H-3aEYeGVMPfT9UODvs7b--8Qa9H1kNSu34zraNtFB_FHJbLuv0QS2okyhGwVYCE5ztTqcrCLnNHR3LPoBCTSVg3HtBEjFENhy2-nbBjJKIj9RrQIWl425DpIJEAfpz4MuM3sdwZzyhi4Rw1vcToFsAdI4hksZ1NIVCt6L58raE52qwOuvKs1i0uoQqBCdfAqM4FDr-GeEKLTMiWMgDuDxaya7CagspHksqzQRf7Jq3HidVoxU6x4lMZoo6I3tLmu7l_nF-Fe_ksGy7S54IgyMxzmJDCX_g4A88kXn7rmhMzGVCYIIQpMms4gHrxTrIBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یا قمر بنی هاشم</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/funhiphop/83463" target="_blank">📅 03:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83460">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/leYYppCo2Q0dLp-aFwcI4EMjjh4-SZhyf_4o8ml6lWEwb-elKqI00bCpJ9WFOTk6O3twEDRXlKhUgLoJkDlkIv5C1sGOG7qm2sr4KLguWuufTl-6H6r_T9DgHm5YK7Mp4vMhU7IZCKTStfwnBiElkJxIrYyEAVsCovGrga4X3MHcu05a5ZZqvtTH1AIvya9v-IXv1OJk1GsJGNf9kYGtMULLdTv0CGBwEM3rPznt2fo19lZa719OhNsr5MH8pkv4A3rxMOlxhfVuXOUQptq5Exlv2PI0E1mFKO0k0LjpbzMLmFrXqN0FR4LpOSf1r0PK-Ea6at8ojiOfFt_nhmZqWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAjWF0BNe9WRkIbEkbFvziIb2KY44OA1gAFnqTXvil0p8hobdMoHAIeFCr-334lcW1w8OtXAntJCj4ORN3k99FGKIrcAVEwP4GyKDWCDhcbR8bHsyVpbY-sPfCu-tQsgXCuGUPLKLXkBkXQSJGyV6dT5DW3_Bufnd9SCt9DkBTYogwKoMzvVGzCpb5_4z1mZOBUFt3bMDit9LMwZLbVhnexk2WuoIQA2JTGNQXtFFOeh6-ngDjDqwNhX6BNR4Yj_ChTcjgYhL2cLNOgpS5opedwLDFfkakaLt6s_IWsMaBx6f5DRzqHQKMspqY2pIMLZkfBXMVI2HQP38v-a8MRgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQlTzZTyvPERjRbH9MJ6tXawBeml2epfU_tJ9y6f2NfdGMt4WQjkr7OFIigK43NKmKinAgTg8JIg-WzBLU6A5xxsoF-wpkRsjUCwnF7J2aSzVeWXJFuqAsfGGUvNn-SRvP-wzvfDCfDpQmns9f3nKvhTEvRI6ZiBil_Xbsyynfqxhx19kfGoD4IljAHX-gEiqx8dqq7O0KhYD28g7OCIVOjvIl1p1H0wIdt1BbXlB4Xy7N7sIvUmeJPQztDdY5OPiWwagNqBZMsOo5xP4mIs9-ir7vAx9KNFgsDNu-0WI8RHrTMYL8l-vlhAu_kDzTOiTcxCKLjojg716ADwgLm1LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپیده خانوم معافی هم هستن</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/funhiphop/83460" target="_blank">📅 03:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83459">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SRf6CX6SMbe-6sMqJG4ATsa68Xib8i9rEyTf06Vff_1kFHwytVfSdrPPVEI0Ym3fZuvCt5PRojYpFgK1_4-XRJy35kwwcuOtJF-afblOfvFs8xh0_fuT5tQH68In6m9xERvtc_8k8LCQl9EJM6KYAoPR29eo0084HgZzn3hgouh7tYynfgk88yderoVWwOFl9eRQegYWBfz4ih4O_oTwZbHHwHcLvTiTQOgpTH4ESIcnTWjm-avqhvu8L3bW4inXhuof0hlipD3yEFhnc_J7zgrF9zGpVZ6895QP6-aA2CCVKu2d3yqZIsI29wp5ol_XL01Y6glTJ3ob4tiDrA6Y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولیا گارنر هم برا خاص پسندا</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/funhiphop/83459" target="_blank">📅 03:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83458">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyVe_2piLHYmoXmvMb1jzAHom9uFg2IBltpdFdlTxvtCNU-sC57B8e4DDqXr7w8NDvFmQFXwEzoZghv0i4IEHrZxbmMVp5Wy5pk7KHtEtKJgmFI6xc1sIyoHPsDYaFN49k0jTltiPZ--mKzAriEKud6kk-IvXL0oJyGQZ1uNnKtEGdWGCm72xLKe7FQMGzlh4wXynWHwrepq8fn_Y89v2TCjlY5gCHmz7PFWL2Hb3Zbq68md_7AVVx5_f8lhjvDzHlbt3YxV-8ufxlE7V9Rcpq91Hh5d7TDYfcG01sqdoQBzyjxjoZVKYixs8wU90JYAC884wfMCBoEwQLZkYxWZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلورتس پیو رو پیدا کنی و نزاری ناراحت میشم</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/funhiphop/83458" target="_blank">📅 03:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83457">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD9th79dCc6vC18vONR9kCC9zyklcb4-vYFQnni-pu4wOr6r2IfdNRL05SkAauEmMKWAWXLaOBHSmEiHg8Q-YfpiExqlmMK1ZHp7TUShckkvNSL2qZoKRmprg0WWi-YC6-qyGgYRrfiiSNfFJz3vSfvGajDFa2qKMhkSUOcEM6aETJEnE8aO8HXL-EtPsyTqH3CZ5Axf6rzirepTC6L2b3MDNKOB3Om4R4HFi4Ga37wNVn86wpp9ELVaEpQCK564WGjrE3ygSRaZvRUtmT9RxxWwWpyBiB12ncPopgGNV_ut5pXKSqo0HqePRhrsaHGzEO44Cd7FYByGz7VM1gzEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهرنگ خبرنگار اعزامی فان هیپ هاپ تو مراسم امی حضور داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.82K · <a href="https://t.me/funhiphop/83457" target="_blank">📅 03:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83456">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_KrIHzi1qc-O4mmb1FiTqSPegy5ViKHciOIGu6K1TV0h74pih0kF0p9HTLx2ipC4sY1xRcdXkIBHU3ns51UvkZ_VlriVNyP4Q3UOiF2I_g6VrOhNLeLBAZ9xuKmtfZbNutscZX0lxqalsVHXTvvaGb3OL1bHU-39n9e-j3X4Dad1795SvsotLj2E9ArFg2T4r6C4BKvukCLqOuRfxT16SwMgVzLwYt5G10kmfOlwEfNg-mlwp4d9onAheM3H_9pkrRI65_QGEwcKx8LQpGi6yj8GQtECNgpVNXtmbBSxHtMEIThG4kvuCAOiMbvd_JjRjT6XmSWMuJyGu9cn__Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندایا رو خودم نیستم ولی شما ببینید</div>
<div class="tg-footer">👁️ 2.9K · <a href="https://t.me/funhiphop/83456" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PALpa6K6SbM5-vIx89oFbpvwJkoWVYkxzOHWnN4WYfpqVN2oyRPkfdQ-j3zV8gKoY6o5Lrd88tlCAqxC710qVg0oaIkRPY3OG1BXYfXdlz4fMjznQw7AZrpWu11yqDY9C9Mv5jSzGCDU8t8Ldzau5TAua0nxuYemX4Qd6KCiXPHatxcMH6wEdZkGNYT-1b7ue8O5warbzaQJ8Snp4vJ8FJ2b4nZ0XakfUbtOVW6BeVgccQPGZTmaHhUnqGr-agN_wyzzjFwEfJEOHDbv6g5bOTQfappjpD9Dad7I40VvfrF1nemRHiNcTa4B067JWUh56VVEKNsZd7tkGS6A3rwXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای ال فنینگو بزار زود</div>
<div class="tg-footer">👁️ 3.11K · <a href="https://t.me/funhiphop/83455" target="_blank">📅 03:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ببخشید مردا رو تو چنلای دیگه دنبال کنید از مردا بدم میاد</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/funhiphop/83454" target="_blank">📅 03:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mv-Hjnhkzgd6uweE9N1vEob0Y2bS3daN-sK8MyWspt5ogPZ_wCCNtUMBeQ7dJ3mDH6C4ZEnQ0c3CE_vTZgsUrunhmMJJRBH_A4ExI4c1bltXk8WWdj_31iEogIZtwPGuzsYkrPSn_iP2H6L-U4E7TGcLXl89bILplmWYPA7bHQrR7arCO1MBbkO_7RwSL3kS1yOFnIsTvZNdqcHCaNmMTPn6L1sutQXv34aTMWQTeQnzLL0Ck62lfFdU9oUK0ct7kBTySrwMBdK92Oq_RqYcfo0lqErd8uQgbZejXgYGPox7-n7jinAXCiZBK6JMKi2As97y_EyjSdojqE9Fsi3oHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو</div>
<div class="tg-footer">👁️ 3.29K · <a href="https://t.me/funhiphop/83453" target="_blank">📅 03:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 3.21K · <a href="https://t.me/funhiphop/83452" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qz1WbUSGTlhd6_0aaLEzpvjctUBFfj3C4iUFICxS5bth9kbRhl-ur1b1VTGR2Y0OonqO3HALHylGiPyyoSWILqj2_S1SZBqr8xVAq1VI0pmJE13W0ozVd8m6z4pMcE1dW95SZ35PVoS57Ty4-t9fNTzAfVQnM9r2Gnp-h86zHpiRqZ6jkDRFgnkPLYlh-zu7UGiXs1CQm7DWJQ0pVyHOfOpK166U7AkazkN_-Zv3xmoBOzRQfORm-WseROpnxypK05P3Xjszvj8YzsSA6WMKIFDmSLvmjjgB6nGXHaMFIGk8na97W3Lqnrqpfd21ygAOBehp3luu3nBPC_OEQaYOLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/funhiphop/83451" target="_blank">📅 03:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83449">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmf5t4yTPD4fX0kPwkZB4cme1nvTqelkl6K2xkiskKOG7d0rGeAnhCI4F8gCTQShrmaiV1PChRSkVY-YUfcSDNOtQH5lj0Ni1kPD14xCzODbpNoRO0kw96daOVcsBdPem4oC414-PR8DC523UimwBfgjIWOSe5dugOxM_t2SmxWOqToVu91DMPfyAg7GTa9ZavCOauNOM6yBQbqo0yiit-rVVCeJSHguqQfimLBRiZH1Gt3U2_DnuHCwB9s4yoAH35jfGbF5jeDO8x7_yExLoEIgLbR39-M0Ai8AvoWEl1N6pSDflgLwul3J3y8b0QIPDc75fU31SiR1DVksmkrHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W1nephaIqG159R9Sp8mshq62QdbzF3ryFprEePYCHmYrvncZwg_AGBSv3dScZ8lHUAb2eDSg5LHkFcFoR1mkgYRww99OYZQacjBP0vP9SGcFdmvnfanUW_GNdZyCdRiLNoG7LMj9AbgQjQ6VEKaCknYaO993aygpBcx63x291GxhL4mLV_aIK1-Fd8LoJfMJhCZYqfUboV-k473GwEaHIfgODO_NTiCf4nPBxr8tUk4zIJ1PF4mkpBvnXXx1nuO5JHhDDzRQ9bRwxfI6DnkVrIRgXjh4svquFCtsU5Byu_zFTjJTW7afcchn68mX08emxQgtJAOGIlh5bU1xMfk3Hw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو کیدمن و داداشم چارلی هونامم هستن</div>
<div class="tg-footer">👁️ 3.34K · <a href="https://t.me/funhiphop/83449" target="_blank">📅 03:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83448">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyHScEoMayPg_alAROfiWVEiQ6gal4dpC4hO0hYRFNKzsGcxWkrmFkeRayBPgf_Xaxrun-KJttVPHzTiqCabBpdbE5KNc6q8v58JA8ed4ToT-l3FaO1qJktv-EM4eic2s-j3hzJJxjACUaclqwa33nSW1qV9Hg72sOKXA2fOxlHKg3_fTEvF587BFEfhcmrv8tVMYfsNyqqjYYNNXjU3UrQzLmMhv46veY7zqH1Be7iKSqGbeYLUjoAuhwbdpDwsHcyzx7YQCMgbwX8Dwi3IN7ctMkgcp7mYsVHhH043ffQFyUeTIf2vCXoiU_NzLJIOpRhdi_fVCEHiBwK-5GqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/funhiphop/83448" target="_blank">📅 03:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83447">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 3.49K · <a href="https://t.me/funhiphop/83447" target="_blank">📅 03:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83446">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcA3XInvl4OeEJ9YTC_r40YgbUpU9Ts_vN-NPs1tjdhfrcfD6sUrficiWCYqQZFo8EAJ63bOk8L3sXJAO4i_wzSC2xjoC4bnO8WKgNguk0cyQE4VorN0tw2EHhIP_XJZo3sG4peb1wwtSz4V_6A1MWp0Kz_Ob0MxsgferS5Bb_yH0qgryDhcrCrWTXYa5fx4bu1R2lsW5H3pGEaM7wwfqbuAVOCQXp-OI4LzxiAMR95XYzG2_FUKRaSCoJlrdCUza4vRtIhth_OVMEFFQrrRZVn97nNlReV9WYvuuz-1NEJBkaX0hN1f9mHoBN3LRELxXoQWr6RYUYfAonc3IlQbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی زشت شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 5.79K · <a href="https://t.me/funhiphop/83446" target="_blank">📅 02:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83445">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=N4ZWoJgoF0sW3iz3s9n2akLwOtZgNn6G3ANO8YYnfVwDpRTDJHavvT-v01zhWm_V8jbpI7We0d5flFvNEgXNvrGtFvgzSgMZbZuczxUX2S5fqztI7fWqPV5wY5FRz6-ponOuFejh-w6USZ07xJ3_LAD52iXZpgv8BJUgPXz6Q4Is35DKUErqdN0g6q3DiWB0VYniGjixbVLdrRZEh645QgFHOCcco-H1NnVDqZUimW1eGmFU9fR0JeiY24NONZwbtPuufmJgdNuHC6G_AxJttwUFOZZrjvemuHmWl-QhY-qtgLHqSLyfcM8nR_8PPSFdVSolomEWB-KjgrfEDtCK_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=N4ZWoJgoF0sW3iz3s9n2akLwOtZgNn6G3ANO8YYnfVwDpRTDJHavvT-v01zhWm_V8jbpI7We0d5flFvNEgXNvrGtFvgzSgMZbZuczxUX2S5fqztI7fWqPV5wY5FRz6-ponOuFejh-w6USZ07xJ3_LAD52iXZpgv8BJUgPXz6Q4Is35DKUErqdN0g6q3DiWB0VYniGjixbVLdrRZEh645QgFHOCcco-H1NnVDqZUimW1eGmFU9fR0JeiY24NONZwbtPuufmJgdNuHC6G_AxJttwUFOZZrjvemuHmWl-QhY-qtgLHqSLyfcM8nR_8PPSFdVSolomEWB-KjgrfEDtCK_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یعنی جدی تو یه رفیق نداری ببره درمانت کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/83445" target="_blank">📅 02:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83444">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">این چه مسخره بازی ایه ۷ نفر شانس توپ طلا دارن، قدیما قبل مراسم همه میدونستن میرسه به مسی فکرمون راحت بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.34K · <a href="https://t.me/funhiphop/83444" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83443">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=O80g-DRKjk55tFKQl5bbTFxtDNILk9hQNAypJrS4Z3T90avHyQo7lxgcWcRZvyLoqXQMT0XnOUrh8s57dgrVmfaER4_Q0B2UL2-vTugtpxN5zd_Od_iw7FZwVAeqKM3LHKknMxlxE8V5uHF8bhWeAHKsOimfcIicvzOM5CNeF5ocn6vYnTozOb9_wgfTjY7n0B-48TfhZvzY15buhBkWi4VGowZRXW-K3aUBKEaiC8028mwKzW9oDLuKO8___9WKk6yY-wLilBbzg1AYu8SoawcVWV_cDNPpL6UgJmZYvqydo0hPwUuiT6JgU_kfYyNwBaVRNk9tenvybgSd2yJQCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=O80g-DRKjk55tFKQl5bbTFxtDNILk9hQNAypJrS4Z3T90avHyQo7lxgcWcRZvyLoqXQMT0XnOUrh8s57dgrVmfaER4_Q0B2UL2-vTugtpxN5zd_Od_iw7FZwVAeqKM3LHKknMxlxE8V5uHF8bhWeAHKsOimfcIicvzOM5CNeF5ocn6vYnTozOb9_wgfTjY7n0B-48TfhZvzY15buhBkWi4VGowZRXW-K3aUBKEaiC8028mwKzW9oDLuKO8___9WKk6yY-wLilBbzg1AYu8SoawcVWV_cDNPpL6UgJmZYvqydo0hPwUuiT6JgU_kfYyNwBaVRNk9tenvybgSd2yJQCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 8.11K · <a href="https://t.me/funhiphop/83443" target="_blank">📅 01:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83442">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BwFDN-qdsrqGLW5nhTICvjDvBbXVISTs6uv5LJzlqqlQhmo4bJPnZ2IXVvtpUxwSQh-6xDiRPgrYJ30qDklQPkc-B0dPmuFHeBbOfwWTOz4mz9KVl4WJMDsFJEVInpQYuWH9h1ZCSTwNWRpD1sc-gK7nMNUgwpQHfLi0G8NbfqMtvxXttulQOkyM4AA10mWVN0r8_q4FQUxheM-bIZ9u6sLKH_AlXCpsLDUThxROVHdiLwbdQVC_IwCk3YBVSHI6nwCnJERNHpRPNDvbEE1t_ENIJ8UAUqBD-bI6gicLk2Iae8dKS5E9LxFdjYyZM-GBHgoPw72Y-KVWpwSgOUowPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد میگن ایرانی فراموش کاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.27K · <a href="https://t.me/funhiphop/83442" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83441">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">واقعا بامزه ان پوتک و آرتا
پوتک یچی میندازه دو دقیقه بعد پاک می‌کنه، آرتا راجب همون ۲۰ تا ویس میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83441" target="_blank">📅 00:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83440">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J5uk-U5n1yHs3ue6QMqeAK5_m1SKGkPtmzuVex9NWp2QIo6HbC24xROT8pDCfm3rJQMN106A7I_HPAKHIpHXKmdzjytk862ebAMFJs8z2iXjif9bS8Oxz_UZD0_4uTEqUhIii-sBYn-9o8Ppj7nnaxVUCEnscZeil1Rgm2JeQ-eILwv2zE54YGcWk0dp3cnlQ1owwZ_72BhB_jV_HlG6vyKSpqui4QCV7VVFmk4JRNvbNgLjsHOZ3evoik-FJjWYWBcKbLbFWTpj5WB7lYm-9O14EmQkvmi_yA0ZvHyLpflr7K0tatIqNB__0gjrQOHn62kqdmqJFMGHTTskx8jbEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک بعد از کلی ویس و فحش کشی با آرتا اینو پست کرد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83440" target="_blank">📅 00:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83439">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1JJUIPPwynEFVJBCNdNe0a9E4bBgq9JUQrbqEI3MeZc3BgGnRsiNN3jloKzfzsqwXTZqSa5TjvOmgy5IeqEMAn1Bt1w6Goapy_kZeKeZCWPZw8ZJgo8kv7BO3VfsgvonGfFVu0zpxfZ613An0BihwwDd8tuVBuY_bxqjo8KuCMMOYPXkybKEDu71ransRgMhHHDjlu2pQQg9X7qo6otiIbJ4XPriHV8BRKr6pP7p494ASGvIUCj0rsytWW-3vYzSIdCwrNija4hIIlZS2x3u9wDp3bd6PyIDawzLoM0cyIBEYlPR2oBvFhMNp-pRsuBUQSHqOnwXMP0LK7VySb-lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم سهرابورینیو با 137تا پاس صحیح 3 تا گل به السد زد و برنده شد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83439" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83438">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">حقیقتا هرچی پول بگا دادم فدا سر استقلال با این بازی
مساوی میشد فشار میخوردم</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83438" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83437">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">برید بگید ال نمیدونم هرچی که دوس دارید بیاد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83437" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83436">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0jv14INjnfFgJ2KPIxAJoPP6BTEEZXloRWafSVmgmvAcUKR-YjP5PVzDr9x46xoUoi5QoU2g_paPx7lgwf8vnR4I2V8AEF96EsQTHACW1wuEHIcS_ibzGQllPLofsXLskf2Pd1bQupycfkQHBxsjMX2OSTVADWPKOGU2hHQVfXAXvZJUmY3J0JMYJU9DfetOYzNUVxcb_vlzl7FoOj01ZWPl6n3NTJolHnPCw0ldMt77hzqGVJ2qjiIhbDDaDmINhj-ReTJ6LTkIMXo1QIP--i7YVwU5I1omCB-eb268Yiyy3rPcL1n37rd4Jfdq3osqtP8IJyiXWfUqoLnMzmP9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداد عادل، برادر همسر مجتبی خامنه‌ای:
آقای مجتبی خامنه‌ای عاشق سریال فرار از زندان و فیلم‌های کریستوفر نولان هستند و به من گفتن چجوری تو کریستوفر نولان و موسیقی شاهکار فیلماش رو نمی‌شناسی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83436" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83435">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">ویس‌های آرتا در جواب به
پوریا پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83435" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83434">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">رد شد گل السد</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83434" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83431">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">چه سعادتی بالاتر از گل خوردن از فرمینو</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83431" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83430">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">یچیزی بگم نخندید، السد از جام های داخلی انصراف داد که تمرکزشو بزاره رو آسیا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83430" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83429">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">استقلالو</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83429" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83428">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">از بازی استقلال کاملا معلومه بهشون اطلاع دادن من رو السد زدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83428" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83427">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">سحر خیزان
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83427" target="_blank">📅 22:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83426">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">با 50 تومن وی‌پی‌ان نامحدود بگیررر
🔥
- 10 گیگ - 40,000 تومان - 20 گیگ - 80,000 تومان - 30 گیگ - 120,000 تومان - 40 گیگ - 160,000 تومان - 50 گیگ - 200,000 تومان
💎
- 100 گیگ - 400,000 تومان
💎
- نامحدود (1 کاربر) - 150,000 تومان - نامحدود (3 کاربر) - 200,000 تومان…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83426" target="_blank">📅 22:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83424">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F9FwZZaYJPn5zlqftHEVA6QKwkpMN7nqrh91trc7M5v-m5yCuJ3mEOHIQ7uGOCOitt8_2_7LryYTdJpl74nLe8NQDFKrcCxP3j5CUjvfp9NZw1WySe4R1uek5jmCqYN18UI8sQH8tisJir8rGyoAErMjMd018jTg_shIGRiOHyyG0Aq0yrhiSYfWgKcZNSHXpQEgTaLStk5ODtjph13CrETxvqrYuQx8xlK-N-GD9BoSI1rXi-O_ICQeNlmcxp-OX5ERTofeRSFUTyryijvdS9caUUpHKL2AIdpY05RzAEUfPJGI3gIgDaRSqSuJXHi03eoUUfJ_3dcUykjjoGsO4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با 50 تومن وی‌پی‌ان نامحدود بگیررر
🔥
-
10 گیگ
-
40,000
تومان
-
20 گیگ
-
80,000
تومان
-
30 گیگ
-
120,000
تومان
-
40 گیگ
-
160,000
تومان
-
50 گیگ
-
200,000
تومان
💎
-
100 گیگ
-
400,000
تومان
💎
-
نامحدود (1 کاربر)
-
150,000
تومان
-
نامحدود (3 کاربر)
-
200,000
تومان
-
نامحدود (5 کاربر)
-
250,000
تومان
🧨
📍
سرورهای حجمی
بدون محدودیت زمانی
و
کاربر
میباشند.
قبل از خرید
سرویس تست
از ما دریافت کنید
🙏🏽
.
برای دریافت سرویس کلیک کنید
🆔
@VintraVPN
|
فروشگاه
🆔
@VintraSup
|
خرید اشتراک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83424" target="_blank">📅 22:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83423">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">استقلال یکی زد</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83423" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83422">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83422" target="_blank">📅 21:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83420">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">اوه اوه دختر بچه ها دارن فایت میکنن
ویس پوتک خطاب به آرتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83420" target="_blank">📅 21:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83419">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/baj3RkpGK7BGg5i023ftqb8cf0uGvz5jLZkMEMmT6bCquujPtuAeHzLi0Ormnm7y0edll4W4dhzPu5LbbpW29Cfk6s0l9YtFhbsNnVQQ_iWc3hEmVT7u89O4nX9Otk5mRzGeVKhP_mBluMdxOo0RUM1GaV9t3TJFhrdpBQI-r0WeErPXAqNVEB27uSzC99UcYD2O6m-9olDo4s64JXtSIuieHe5Y9R_qqXqrpNQPI6qCgUMpJUccNNR7TnWLtvY_JCllHsEXGygvHkvMboqOZq5XedfZrHFKc1Z_bTQkySdBoaKiIB8EjcG1TIW1pEZDjchI1yJvpjvuaYzCHkACxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها این پیامک چیه برا من اومده؟
ممکنه منظورش این باشه که یعنی تعویق؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83419" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83418">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=RVXqaug_WzJMBDGWy41qtq1eOcS9-nJjO_5QcWCkhFRw2KhH7fmXo2ztxWJtKdEV_M-tdtiuJyI6T263Y3olMERN4ZWYr0fZ28HRChHvXFiG4vvhk2yB6jPRcaB_w8hCe57us6IbxSxL57OmiEnRAlNWPtUXizGGWDk4nOMXoZJBBi6UIRR6ot8Wpf-w7Abne61OvOJ1zt5Xj9jAijfOY9csQnU6KuPkwOCuoNfMM5lE_nbC0RfFClCfVBWvbUMajPaBeMqPMB0kqnEC437jTFmyy1VEA0OMvq94o5s_ztgFVqgiha-GrGtFGsj1VZwV0iM0GIQZ_yeCAfgV4D3QWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=RVXqaug_WzJMBDGWy41qtq1eOcS9-nJjO_5QcWCkhFRw2KhH7fmXo2ztxWJtKdEV_M-tdtiuJyI6T263Y3olMERN4ZWYr0fZ28HRChHvXFiG4vvhk2yB6jPRcaB_w8hCe57us6IbxSxL57OmiEnRAlNWPtUXizGGWDk4nOMXoZJBBi6UIRR6ot8Wpf-w7Abne61OvOJ1zt5Xj9jAijfOY9csQnU6KuPkwOCuoNfMM5lE_nbC0RfFClCfVBWvbUMajPaBeMqPMB0kqnEC437jTFmyy1VEA0OMvq94o5s_ztgFVqgiha-GrGtFGsj1VZwV0iM0GIQZ_yeCAfgV4D3QWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هیچ عنوان قصد جسارت ندارم اما حقیقتا بنده احساس می‌کنم این رفتار و محتوا در شأن همسر آینده بنده نیست؛
امیدوارم محتواهای بهتری رو برای ساخت تیک‌تاک‌های آیندتون انتخاب کنید لنا خانوم، وَ مِنٔ اَللّهِ تُوفیقْ
🙏
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83418" target="_blank">📅 20:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83417">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آخرین باری که پرسپولیس رفت آسیا دلار 70 تومن بود</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83417" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83416">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">زندگیتونو بزنید رو برد پرسپولیس و اور ۷.۵ گل بازی</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83416" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83415">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">سردار آزمون دقیقه ۷ به تراکتور گل زد</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83415" target="_blank">📅 19:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83414">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">سردار آزمون دقیقه ۷ به تراکتور گل زد</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83414" target="_blank">📅 19:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83413">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGpR-IOKfaNRqZNeeKwfhzucz6cr6LRiiruO6wSzYbWHn6fmSgh8qEOWn_2KRlzbGJAwnQrIPuAzgMBpnG_3XGXKkTeAQJxiJhlFKg01231F8oJ9f8mWN5HS0sH5EUuoz8vISf15NyBSPJ6wLRcRD9HAwtjYR3QSkqgKdcrpCp_EVlFuXGT8MXMecDW_prC2z7_ePWhxZW9KUKAYVvN2taP52DPsSSfcDdzccawQBk_yQrR9bqKNZyUJ9zvJwCxF_sgdaVqIAd7u_WcXTzaEfUsaXR3KbOHesiLMOy4GhLGByLSA-lpEm-UwF0eIah6c5co2saTRhOw0RP8ZgR1e4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایلی خانوم ریخته بیرون براتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/83413" target="_blank">📅 19:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83412">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ln1_WdUYLxE9dS-QDq0zSeu39ni7ZVPgon_vdmXcqAM4DAGSdumWx7syqyLz1qTMHXIZfns5vuRXt1iRx4A9zlO_k8WwolXr6OuXvdkGa4ZrBrN7V2hNCOFxb9exEX10kO98QOmqWD5_7BEn8C2OFeB32xHLDNa7hajzRHw5nHNR_XlTHuS3l0Twp1x6nNKERLyUU2yT9CPRrDGq5m0XlLW6NZf3xfXYD7Ilr_e3LSUAiezb3qjJrN2V8WEWkiRfw4_NL46eNaSzRCg0cFywGTrzPDm9J5lYGgGjVNkHpzc6FxTWk6iaYOnw4jYOtFu73RBMJ2LJTA-CZBkm8A6HzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=ln1_WdUYLxE9dS-QDq0zSeu39ni7ZVPgon_vdmXcqAM4DAGSdumWx7syqyLz1qTMHXIZfns5vuRXt1iRx4A9zlO_k8WwolXr6OuXvdkGa4ZrBrN7V2hNCOFxb9exEX10kO98QOmqWD5_7BEn8C2OFeB32xHLDNa7hajzRHw5nHNR_XlTHuS3l0Twp1x6nNKERLyUU2yT9CPRrDGq5m0XlLW6NZf3xfXYD7Ilr_e3LSUAiezb3qjJrN2V8WEWkiRfw4_NL46eNaSzRCg0cFywGTrzPDm9J5lYGgGjVNkHpzc6FxTWk6iaYOnw4jYOtFu73RBMJ2LJTA-CZBkm8A6HzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g23
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83412" target="_blank">📅 19:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83411">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iZKFo08f_54z7wOuC5XQCNrHinKqQf2fo7oIlS_wt8PPbgbAjyZysRO3-oyNb0mDbodbxhvSqzPOvky4JkHVrlwjmo5RYulaTE9IhWtewcxj7w4dJRM2PV91iE_Y-qOx433pcFp8X9UeW8je6IRekUgjeujXgeD-WLrwL1HxiATzTeVFpnDC2zL5Nck397e34_qed7HNp-MnQWksfHlHMpzNHUsqAljPuouMCSm8FjAssx272hs2wddtRAIIIFglCyFNIlI6h7UFVlcNaCebo-voMPKo6KylxkqTFS4zAkN1O3yXu406aynfolXtPjIgvUQNT2EicVZ-eupnZhVaDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خند
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83411" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83410">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nQXjD30_VTlRc52sBmphm5fYH_7yF_S7GQvshcHl13l4gPnwcUxsmF_HR18NasjD3x_ob4hqWraxG6AVKwsMvOM4E5ni9fvCw30gqtL9vfdZxnK4RdX1q-qCuq8cD5v11sn7gLfMmE74f0-lzy-k7sTQmliLvKlUotpAxqMlPhShgPd5h0rw089DbcExqV8mSo9G_TxcVoxwGkxZA5i5weFoIbxId5UTwlqzaeS3rJlzlMzLmxHt3CeRGQEYBe8tcDh0HMYNHCrBFDBd52Oj6qmxXhDrrJQuK4-QGb5Ta8iP11o55aNPtdeq1RYqoiZM7YAu87areYMNrDiqZauv9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست موثق‌ترین و مطمئن‌ترین اخبار ۲۴ ساعت گذشته برای عزیزانی که وقت نداشتن خبر بخونن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83410" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83409">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S30ymdfoCZdO0ZGpLsBC7gVV4EtB4UE3mWy-jXQwVNrBfmKKJ5BxoZEbuROpwRub9dYfBwMavGyRFVM0XDjL_J2Fd9feZkGnGo5tNqSVYzZAfUBZg4N-5ii1ItbQxDbriAbU8IIjYDL6qsKKBuufhH15aM406mMVcR6QFSofvXNVseqPbhYQWjXtMJeGAKn5jAmz0DIRlkFwelECEL7YMJzso2XLX1SD_55mv_bgugMeKMLHIUZu8PU2BqgQIgWZmLO-o5wH7a3xpX46MwhVlGWEI_YoUGseRkuMYT2WRuJDyK4fXcbEqhUJzXyTyaqpaa8DAEHNgKcfQeoG6DhzQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید میکنم   شین: چندین انفجار در چابهار استان سیستان و بلوچستان  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83409" target="_blank">📅 18:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83408">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">البته مطمئن نیستم ممبرا تو کامنتا گفتن</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83408" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83407">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">البته مطمئن نیستم ممبرا تو کامنتا گفتن</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83407" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83406">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">زدنننن</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83406" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83404">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83404" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83403">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin</strong></div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83403" target="_blank">📅 18:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83402">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">حالا بازیگر لر و پژو پارس از کجا قراره پیدا کنن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83402" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83401">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vS9Vkz4lyHUdKfZNxTCMIKS2GeVqOrpAJ1h5clUJkH9uuhj4rzeq1Hsbz0qjBhN9Nct3nOKLkZyAZvCBh34jv_ENT6jvJk-VNB_8Pg2-Pg4HKWqCYMCC1rUO0tzpHT0iAYRh0AIEqBSTDWlyOeez6Xo5c_rUupmGrTtUoZ5MYaW1syrlO92eCqZ1Li6bZhkaDHlgx2LsCfnkDQrb8JRDoGtYUNGDPaBmc0BaScnU9LWVWg4H1KDgMXIMfeGvl04p5Tk1JQDSOKLocS161QkyYxEm5VkpUqDCFGt9IfcTaI_nwC5mw09BtHXq3o9mpIXJ_N3h6-WKgys15VGVvomNTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال seal team فصل ۳ قسمت ۸ یچی تو این مایه ها ساخته بودن که خلبان امریکایی تو ایران گیر میوفته و میرن واس نجاتش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83401" target="_blank">📅 18:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83400">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">بازیگرش تام کروز باشه کاش، اسمشم بزارن تاپ گان ۳</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83400" target="_blank">📅 18:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83399">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">البته یکی دوسال دیگه فیلمشو میسازن میفهمیم</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/83399" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83398">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83398" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83397">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اینام ادامش که میان و میبرنش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83397" target="_blank">📅 18:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83396">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع ۲۱۰۰ متری بالا برود تا از اسارت بگریزد.
او در گفتگو با برنامه «60 Minutes» گفت: «هرگز اجازه ندهید کمبود انگیزه باعث شود پایتان به تلویزیون ایران باز شود.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/83396" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83395">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">مصاحبه خلبان امریکایی که تو ایران گیر افتاده بود
«براوو»، افسر نیروی هوایی آمریکا که اوایل امسال بر فراز ایران سرنگون شد، می‌گوید: «وقتی به بالا نگاه کردم و هیچ چتر نجاتی ندیدم، آن لحظه ترسانک‌ترین چیزی بود که تا به حال دیده‌ام.»
چتر نجات او در جریان حمله به جنگنده‌اش آسیب دیده بود. براوو می‌گوید در واقع در حال سقوط آزاد بود و متخصصان نظامی بعداً برآورد کردند که او با سرعتی بین ۷۰ تا ۱۰۰ مایل بر ساعت (حدود ۱۱۲ تا ۱۶۰ کیلومتر بر ساعت) به زمین برخورد کرده است.
ما هرگز نخواهیم فهمید براوو دقیقاً با چه سرعتی در حال سقوط بود، اما این برخورد باعث شکستگی کمر او شد. او همچنین دچار شکستگی دست، شکستگی شانه و پیچ‌خوردگی مچ پا شد و از ناحیه بریدگی‌ها و خراشیدگی‌های سر و صورت دچار خونریزی شده بود.
براوو زنده ماندن خود را یک «معجزه امروزی» می‌نامد.
او می‌گوید: «من باور دارم این گواهی بر لطف و مراقبت خدا در زندگی من است که مرا از آن لحظه به گونه‌ای عبور داد که جلوی مصدومیت را نگرفت، اما مانع از آسیب‌های مهلکی شد که می‌توانست توانایی زنده ماندنم را از من بگیرد.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83395" target="_blank">📅 17:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83394">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VzkhWilkQQKF3sDKvsJbrJKdiHGjvYTD-rZJUeFeHOgP5jIytoWxiH7zAamQmbBe9TZ9Q-8Sb_D2DDDQMBdsZEqB29Nkyp0e35Zv68yj9qlYoI5ZdQKFgcuZ_mcY5-QsvM_VObXEyhNaiHajD9pXgQRlGoxxfQiwrgTZypG34gqoI6gmADVA_P_qBNgSC_6ofH8V9yXdiY2CCqTxpys_oO57Kxr_sCFdEWagugABTjwlkdPPmWGkFLFQE3vKtMnyICtBruzpeaSfJKrrGah3OvNvVe5M5c7F7o1OaDH6W10R6fuSKwLE-HbQ7oFxFwpuz85HVdMRNDNCNPfsG9cYDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان چی پیش خودش فکر کرد گفت من هانی رامبدو معروف کردم پسر</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83394" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83393">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">هادی چوپان چی پیش خودش فکر کرد گفت من هانی رامبدو معروف کردم پسر</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83393" target="_blank">📅 17:17 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83392">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">هان اها چی میگی ها هاها اهان ترپه ها
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83392" target="_blank">📅 16:57 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83391">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">متاسفم اینو میگم ولی این دفعه پوتک جواب آرتا رو میده و احتمال زیاد بیف داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/83391" target="_blank">📅 15:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83390">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4983eb567c.mp4?token=aISynd443IF9QW8MQ4FeYAH9U2OIddw2dvIgBJmw-MlzsQy6NM0d7HSsQpYk5M27iCVWfRZq5-V--EnrTZkPrynlGBaOI14AV10JzGTQOBZmovfBWD3bwnrNFJJqO7V-GxWibOzujX3MXpCxO0Wqyw36h3BZ4a2tIs7nol5y02mLZ3piwtkQOtwxmiiSnZMndPfoEqD4Zdqb1rCHM6qKXXLzk8dQM4JS4SpjIAkWAJLbY_t2TDYmWmT8gcGF8f1GA_Ryw7g_9XosefAyVaSyM9vzw7gNPG07m4cci92U8ZPQrgfJ24U_eMVu8kyCJj393ypYOKrfY2N29aDjtlbeNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4983eb567c.mp4?token=aISynd443IF9QW8MQ4FeYAH9U2OIddw2dvIgBJmw-MlzsQy6NM0d7HSsQpYk5M27iCVWfRZq5-V--EnrTZkPrynlGBaOI14AV10JzGTQOBZmovfBWD3bwnrNFJJqO7V-GxWibOzujX3MXpCxO0Wqyw36h3BZ4a2tIs7nol5y02mLZ3piwtkQOtwxmiiSnZMndPfoEqD4Zdqb1rCHM6qKXXLzk8dQM4JS4SpjIAkWAJLbY_t2TDYmWmT8gcGF8f1GA_Ryw7g_9XosefAyVaSyM9vzw7gNPG07m4cci92U8ZPQrgfJ24U_eMVu8kyCJj393ypYOKrfY2N29aDjtlbeNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتا این فیلم رقصیدن پوتکو گذاشته چنلش
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83390" target="_blank">📅 14:51 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83389">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">علی گرامی ناموسا من آهنگتو پوشش بدم خودت خندت نمیگیره؟</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83389" target="_blank">📅 14:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83388">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">علی گرامی ناموسا من آهنگتو پوشش بدم خودت خندت نمیگیره؟</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83388" target="_blank">📅 14:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83387">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">یه کشتی اردنی رو تو تنگه هرمز زدن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83387" target="_blank">📅 13:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83386">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKmhVMcQ5bJpuNSnpvYKyswpBlRbrI-lgBhcu7raF0OXvcecmaNeYlp3MQUVAqzyhlYXWaNplNkzZpQniDSn2wB5dewV_1aXDSbv6ybExliMp0R79E1oBFco24tKtseTtCf-OFk-CXy4lGwU_kKOB7w1bJnima15oN8wejhx73MZJDqS5RdVeBe9apT-u7vNS6zwZMeDL4p5nNPx1iKpys1juEBMSnsgifoS2rYXxReripvknlSrKVorf6vdhWLvCKQTeF2DGNYRvJ-aCYKL4TufzDD_MAMlkwOU0umlv8sPkqBKUVOtZgmU_i153orqw66DhCUw-7TlmDbHjIp-xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بیا دو خط خندیدیم بهش فروتن بازیش گل کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83386" target="_blank">📅 13:47 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83385">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83385" target="_blank">📅 13:44 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83384">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/83384" target="_blank">📅 13:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83383">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRJiWlf-3KC9oScpgrmf0FedY1d55yerkvJVPMLyyBoSjyZhevBMkshcZONUHKSsdo9Xp0W7Jh3lra4bfJRlAcibmJbPmJxcd9JX_RSpsb58hknYYTGtfqINlaVQ0qXJErU42kar8WycQYMAdqe-If4xKIVF5V05hsUViusy0njfzrAB_YX0tP5bx2aACihikKn2CJ1XjZitSjpMEHu509yM7Z7WxqJ3a7T8dC8_mI5DqJv9Q5SkDxOs3Z3r0DRZR985GN-3w1fSbMGnnLzhhAmEtYq_fDdajrgLzu1XQeMJEB52_QExOie3HWATZWVqsx-Dh0EsEUoP9sLCAlu2_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید آرتا به نام "X Mamnoo" منتشر شد
🟠
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83383" target="_blank">📅 13:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83382">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=QNqOE0iJ527Kw0prSN3-3oSgUR71hft39r4Bsfy4svxmmd7rz5VqBsDYqAfNXjEEPlTAqtofCW3REaT05yq0-6QLmviVUAIfu6XKwy2B_S8r32j2aIyBH4Yk2MyGjNdjFCYbNgS5LYNwE-d6aTRIw5tQUME8STfueU_SLhY1ek9k9srFSO3Va5w6UXJCxvkxFM50xWYcjDirlHku47bAHwIEeYj6ubprIQJUZV_NdPVeW4vJxt8QqqkHgh2Am_RTtbwvztnXW973oSIEFdew9PAV50a3ctqffOFajqfVb1fRVqJcV23ZRkc4ZY7bwi_bLpIofayPP9q_VQbLIYHJNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdb90dbc68.mp4?token=QNqOE0iJ527Kw0prSN3-3oSgUR71hft39r4Bsfy4svxmmd7rz5VqBsDYqAfNXjEEPlTAqtofCW3REaT05yq0-6QLmviVUAIfu6XKwy2B_S8r32j2aIyBH4Yk2MyGjNdjFCYbNgS5LYNwE-d6aTRIw5tQUME8STfueU_SLhY1ek9k9srFSO3Va5w6UXJCxvkxFM50xWYcjDirlHku47bAHwIEeYj6ubprIQJUZV_NdPVeW4vJxt8QqqkHgh2Am_RTtbwvztnXW973oSIEFdew9PAV50a3ctqffOFajqfVb1fRVqJcV23ZRkc4ZY7bwi_bLpIofayPP9q_VQbLIYHJNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آرتا پوتکو دیس کرد</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83382" target="_blank">📅 13:36 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83381">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FA-POeC4kp5McO6eLXex8dSzWVYvA1TLifPKMBfulgvFbPu0R5jeL-1UqlJhY8FCvzGB3DPKpswsP6jwG4U_71_wcf-1mBH7rEOJGK6huTUcDp3vNRw2inRWAa7ScQsiSq_9JvvShTEvQGHbCgkgH99_7Zc2dGoYcXD4Sm_U-eZua4Av9apfZWaYPb2t4bCVfGVJNNvp8yn3WqfNjzSwwQZu38_cLFE9SHOC93_Cu2zaId0sRvKVdUvJ_reR-Bqch5JnecXPAXL6zFrj2jNBVPJx3vXU0NGDpXH_niOTl5TNSnWGRrLyZfiFWU-rsAnjpUXHfLvbnZRZpLdpiX0rSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به خدا اگه دیس نباشه یجور فحش کشت کنم افسردگی بگیری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83381" target="_blank">📅 13:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83380">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d85a866ba9.mp4?token=j0qhM9JBBv0-Ice2n8n6h82h-G4m1Q3RLhSFCyTWfWbGJ_nMLv2GqLfTi9Il14pC_iG1LFx802VpWKSVxe3dhgBCvvuZ_Es1keZE1o3nfBaNx8EfIl4mcsZzDA0lnKrTfqP0fS7ZzZqHfvGITcK_qRelC_u6Zy9ScCdbONCUi4z3P8xOvraYelCoi15q3QiVtyCaCkqJt9gEHbj9TeljJ9nwFEFxFQmkyjB0jGKoHwV0OmTzMtqLjbaeTZvA7f4KXsgvYZb_SWLhg345RoYsL9ayuu-rqo0bOXDs8p0DezBjtk2cc-RtFCHGfgIdUSn_9DllBkIOMhcfiPtadpsIUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d85a866ba9.mp4?token=j0qhM9JBBv0-Ice2n8n6h82h-G4m1Q3RLhSFCyTWfWbGJ_nMLv2GqLfTi9Il14pC_iG1LFx802VpWKSVxe3dhgBCvvuZ_Es1keZE1o3nfBaNx8EfIl4mcsZzDA0lnKrTfqP0fS7ZzZqHfvGITcK_qRelC_u6Zy9ScCdbONCUi4z3P8xOvraYelCoi15q3QiVtyCaCkqJt9gEHbj9TeljJ9nwFEFxFQmkyjB0jGKoHwV0OmTzMtqLjbaeTZvA7f4KXsgvYZb_SWLhg345RoYsL9ayuu-rqo0bOXDs8p0DezBjtk2cc-RtFCHGfgIdUSn_9DllBkIOMhcfiPtadpsIUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشهدیا تا اطلاع ثانوی شبا ماشیناتون رو بزارید پارکینگ
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83380" target="_blank">📅 13:18 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83379">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">بقایی:
زیر دریایی آمریکا به غنیمت گرفته شده و غنیمت حلاله بخوان دنبالش بیفتنم اصن پس نمیدیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/83379" target="_blank">📅 12:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83378">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6f_L0sHRQRG9urTZmFZEQeTPcghatlhjljcGCOS-OOK4SDN9T1nQu4-TJskXWDNBXkms5O63dZuTmrLtlkkmhifWF7Z0vn-shp-8rb8NozzT5RULm1Fx3xtjbUAqMTdqKm_vcFQquiWieNjw3M9Sh2pxOM_9REHZdty3JUqt0_toiaruBHXJtKIpfrQW8uC1B2oji7ocgiyHNa80Y_JmDpUxhLAT4K1Xu_FxSOBg23ONnR3qCnf1yVJu0Z5cEpI-8Gr2EFQPQhHN7RxcDO1jyeTSwIJRanZUobCp2C_xO65KzpPF1WiWhxVuWS_ld6UY_8gf4RHSHGvqyWi9EK4Kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید کوروش، اصلا معلوم نیست منظورش پوتکه
🤓
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83378" target="_blank">📅 11:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83377">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sjSau6CoE0Oy-gO-Vz8m5730Wou0WTjhTyXS0bmqr67OxOe1o0ueEvvcYn1-cDZEFLE0CPXmhKwLR8uMnhsHNPXgCqGw7n0yzvirfYxMsBzhj8BUPxeKt54WP8SFyVeqJX2Bgt1hf_0K-fRzW-gRWri-m8echMj87H67XkKs7jk3uMNDS5803kDJqvoUBSqAItYPs3m0bcXDO7rC2d-r3XT3km8M-jUoGp7ARHtWFUIezflZsKte7u89IbHvYQW5AdP7GAg5pOxdnBW-cIOXWXi7REAgccNnE0n8wuUByXEmapyWeke1sZZrKMb9UpyA3RXriFHBsqZudja56VCo5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه رپر دیگه رو تو آمریکا کشتن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83377" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83376">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">⚽️
مهم‌ترین فوتبال ایران و جهان با بری بت
⚽️</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83376" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83375">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lQb1qs8JJ0Es1OkeIzsGGeWV1Mihr3FJ825nGMqzkNkKX1UX6w5W7iOLWUjVFaFlE8uNMCs0AnDGlXke1S0VKonYFiRywv6fJHXLzbW8-Ms7TlnyzXYSL_UiuDIcoIdW_Bhw3ks4VBGdms5B1hY8ZM22LkxT1T4gzjM7I2_ecOhwhwrV3XDwAC6MFQoLOYWtYjAYeb6g4pjBCKc0n9FAiPsyIAtiismZE-z_W8W6ZsGjZVY6lzd37R6UUgppSlIROTMzFJYAg1nu8x4J6L3HtOBrFrX7IXSudAmgeqjmT1_Fnb59GE0N4WcI_fac5OJsFM9N0xF8yWwqQjwBjEEjcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
کی میبره؟
👑
👕
السد دوحه؟
👕
استقلال؟
🧑‍💻
از همین حالا با بهترین شرایط این رقابت جذاب را پیش بینی کنید
💖
👍
بهترین و بالاترین ضرائب بازی
💱
😀
تا
🔤
🔤
🔢
شرط رایگان در صورت ناموفق بودن شرط بر روی تیم محبوبتان
🍀
✅
با بیش از
🔤
🔤
🔤
آپشن شرطبندی
🧲
0️⃣
1️⃣
🔣
شارژ بیشتر برای شارژ با روش رمزارز
💰
R23
🌎
ورود به سایت
👇
🔗
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
📲
کانال رسمی ما در تلگرام
👇
⭐️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83375" target="_blank">📅 11:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83374">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اگه گفتید الان چی میچسبه</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83374" target="_blank">📅 07:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83373">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">اگه گفتید الان چی میچسبه</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83373" target="_blank">📅 06:29 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83372">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zem95_0EWG2UqmDPISoR2nVw1-3NAyLnaLqMBwZUxjPEJP3WeM1nPhJBzmMDkFJy5DAR6v2UnVKWk9VFrHLgQixWZN1t_YE9MZHAL0at2c7N_1IcrLJBMx15bwD9wYC9U9Nt6DilE00H5TF7uMKefMPM3YJYrTnAvUzcDe-fQ_aPLWC0QZyrc9fXjB9jCZYlgb8ZC0-g5cXF19GV9DkiW82tC70UB_JXboeV59judi8trIw_WHqXBLuVIR5jpUkquddGiKuuFJl4aFHNeVxRnS0tD0EwgqGgQxfo-A6BVvyoFK4wLflFEOhcLHue6aNC5Qzq5UmRnUN-M9weQ1-WXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام، همستر با سیزن جدیدش برگشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83372" target="_blank">📅 02:14 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83371">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Daf Zadam Roye Daf</div>
  <div class="tg-doc-extra">@vantaproducer</div>
</div>
<a href="https://t.me/funhiphop/83371" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">تنها حالتی که علی گرامی میتونه قابل تحمل بشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83371" target="_blank">📅 02:07 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83370">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پرتاب موشک از سیریک به سمت دریا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83370" target="_blank">📅 23:48 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83369">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">امروز ترامپ نگفته ایران نباید سلاح هسته ای داشته باشه احساس میکنم یچیزی کمه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83369" target="_blank">📅 23:41 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83367">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">شلتون یجوری افسردس انگار ایرانیه، خودتو جمع کن بابا کون بچه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83367" target="_blank">📅 22:58 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83366">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">۱۸پرومکس قراره تو ایران تو محدوده ۹۰۰ میلیون قیمت گذاری شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83366" target="_blank">📅 22:20 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83365">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vIa-Wt7d9gvb_9lt0TEshDoTLhB1hNDI5SZbBkRdLTh4Ft4Z9DjQ8QZZQwO9KriJa5Zt32vL8KuH1YKrJ59TRb2UX3_gDamlY6SWD_9Z3hsosMO1eX-Y4xaGxJSBFr88PSOMORQkv_N7CdUyzoOgBg987jlfCqSN4I5Y0by2D1mNnwFil5UN5IhxdmQYd_KX0cmYV9hq_XEXvj-C6P8rXUImI79cVF3hFePEPmsPJiONcyawgjIz8nTo8q2OfOUWY_8ma5CiEPLQpvjTByW1FiTqr2amwmXgE49Qe1ldOAlWFIdScVL3MbXBNsrNHTUGm65o5JSDGNM0JMx0SAmM6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شو حاجی خسته شو
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83365" target="_blank">📅 22:15 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83364">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">برید بشینید مسابقه شلتون و زورف رو ببینید خداست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83364" target="_blank">📅 22:13 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83360">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">ترک جدید پوتک به نام «Honey» منتشر شد.  Youtube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/83360" target="_blank">📅 21:54 · 22 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83359">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">اگه رپ آمریکا به کیرتون هست، باید بگم که Lil Durk تبرئه شده و قراره آزاد شه  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83359" target="_blank">📅 21:46 · 22 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
