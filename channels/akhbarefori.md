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
<img src="https://cdn4.telesco.pe/file/JdMi9JV36DLpvEf5klHmupy0B3KUsp23BwKuBSo41U1KuiIAeOhyqPkeuzOydAcadUH9EbnNWkatbZbTHcSWhsD6OiKckGFcgdD2tTB4oOQCdxC5vL_8xBvkcsatyjQb54IV5E1sUUFvNlYqjl6X5T2jJ63jTG9PlC_tmLOvFM7nbPqEGtUApSw8v_fLZ02MQJUp_dqBkW79UI22_HcM4vR-6inq-0JDjDWDuFvtnbH5J5x-IuXYZrv7FK5Uc1ITRinyVRdJ8mmCgzc3aH9Ilqs2lZpv_MEg36nOiVwBLDX3xA7ObZ8KgNF0INAkKeRHxWtJrprEbyILGmcalMuOWA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.1M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-14 05:13:01</div>
<hr>

<div class="tg-post" id="msg-655965">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4-3VRzvxnOWSjbgZXuhnkKk5lCms7HLZ8DFBsKlmjJeboIfeth5V8Et5XZHbvnw06j0EGdH6c1G8afs9e2iDswxNwLacqFFjuGObpNbyQmVQOEmaudwTLv5x5gIOGBwI65-DVIVIsXjASQhJ1B1Jwy1PWkwDE-obYcCOMhkAmF1LAf70rboW1h2atzaUwzGC7NKjbro-YnLEf1XyDuCMPgGvJylNJ8aiD3P19DYVMpM8yiykY86GUwXrrHFi9s7upS8jWoWl3_HGRBt9L7QW7GVzBBMatOe4Gm7nYQ-FdfdLp-tdFQFsZzE7JL58gbq5QCfk3M156f-esCoPFUkrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حرف دلت را با امیر غدیر بگو
+ هدیه متبرک
در روزهایی که دل‌ها در انتظار ظهور منجی به سر می‌برند، در پویش «
نجوای غدیر
» شما مخاطبان عزیز می‌توانید هر آنچه در دل دارید را با مولای متقیان، در میان بگذارید.
کافی است با مراجعه به صفحهٔ غدیر به نشانی زیر، دلنوشته‌ خود را خطاب به حضرت امیرالمؤمنین علی (علیه‌السلام) بنویسید و ارسال کنید:
🔸
ghdir.ir/k
🎁
علاوه بر قرار گرفتن دلنوشته‌های شما در ضریح مطهر، به ۱۱۰ نفر از آثار منتخب، به قید قرعه هدیه‌ای متبرک از حرم مطهر علوی اهدا می‌شود.
@ImamAliNetFA
🔸
🔸
🔸
🔸</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/akhbarefori/655965" target="_blank">📅 01:30 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655956">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tX6zF8xwGgG7tabzNRsD0w_yiFlzS2loP43dfhv74RH839FwZOkselXSxTbaYCUCxrtd7RyjlEBPRscieP_n21YC0f9AMxdp-8T4TkW8-XWEG1xyQ4HdD_lU0D0nGJmOey0YqyujUUluVGCMf_wFQX5xQAq5DqVQzOyA8R3iwn7u8q4UKH7nXm5EIO4DkFKqkOaLNBech8GlAU_Pz6YtR7dhFsC3QeIGepLMcZGzVt0vnpZGW2Ayacj1Y58FXrm10fCYQ_2gbuXUwm9tsU-yYwIBfGKXt_zJAj7K-26FWJ4xPTw4hLIkkr1Zu5C3Nq6GIgBwLXi0abImP3kVVDbYwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/swtLr394GlLVY9pYkXys4O3MCJh7eNl4NHpzYf4_NXDWmQCV2ag95UfN04YfVsQ6toHlzV_bR7zSRm6uN6OzeJI-GtFlf-MuBRrL68-4ncYO2YNTihIGfilIPbShYMntLJwCtFywmnRozOjbzHK1Nyg9C0JOuZf59CdCuM4ahHM_AmOvLmVIttGW0UngjBb1KSFEFdsC9Rw7oDGl0POTMyvzLjhzHmCS3cvnxKm5F_5tDC0R9FEh1HyOyWCFncUPvokrEW1zphkvWgMax4gUfKQWKx77jCrTu0Gbd0I3e7cZizd6C6cp6R7ZFKqt7kUHtWR8zlb8Yr3eOZ8ME2-TsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwX4za3oOeXOnn65a3IBs1de-mRCOekNajK_ppU-J0BsAMyIfLGa1oXvyhhvgaxxpVUY7Y9r1bRxm1Aapc0olQcWJo4Bt6xJtxRxGSfdFbMTzHQq_qu3-N3LwzT9-U_E6vP8-BdaMerIZYlv-FRCqNwYyI0UPDliWFdVKPAG9lG4VEdwEZGgmbKZPXkHxXF3iH6tYSjLdrZmT4CVaCHCgpu7PhCvacX73SkjCm0RDtUSY65DCsiJXgbzRmC-ptkrieGE_F-GT0KbTbFh8hZ3Ziir8xOcG2IswgDCRNQh7TMEFvSpGiqXkisvC2Yk-5_TNTaafv_XZSWEN1a6K4LHdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oMkGduz4Z3CMBDHp-vpQYxrLcu_CsE09vGULHZvyguIo4th27W40TvjPC1TkcWu7ZAvGBZY7owP5elahMP0DgXd4A9gDpOkck_IJ_cZ8fnpdPpbhqG49yf8Y-2Q02G-Q1XDX3GLSqBnIehw_-M0p759OUYJw4K7a8YkM-jy_PboEkdF0OG9_PEJQHQUP7onQNmhH1T_1cOQt6Ou2NXEqMljyxDnKquZktaapWLUCMmGmpfdvyGV5p9ybdD5nL81CAxlwfZpev-RS_ZTQtvdpUm_uZPKwv0Lxz0D9aIecE-zWaEgmpOZvZVSeiG-FIbNnUB4UTGeXEjxRJsU2oc5EHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DTvARff7C1v-Hng0C_LIp0rno4dZbQf7_klEY9Mq1_I5XorA-m4OdJVQZYPw-zla1nAFtqc4MNHVxdjQZ6X_HTJJA763Cymnb_fL-AnUoKjI7I_TQDhrjByxAaDwD9X7vlUp2VBRGoF-MnfxfLqD_PWjY0uotyuUFUCHbYqpzFelr1FW_6zT2_X0RT45oZKNOvAhzxDRR5LsgbC9OKEnFK9Qa-qFdJisnmwiba4_ZA9DU7Aiew2P_ZbmAp2CPZw1DSaP6w_mgwnLUYKvuokN4iHCdbnOgRyydCmJKvp3mJ_zEVIxy4T-x94siOHX1iuJEM7_d6io7lAUGITXILEB5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/seVJkI-H-DmscgmjB-n4msZje69fyp1lpfH628k-VSm6Ky5zsrIZVIX7oo842dtogDaog797BTk0gn1h0fj2eaXjyS4EWLEStm9oEAxcefTGDX_vNdA7IXA9vafBfYPSMkInlfKwyjf6S3E4DHToEY-Etz62VRJCooLw9HYo9V9pjdyypDSOdMnm3Zrst8RuSrrJ9b0rNnhJhcnp0xrxC-iKkurrc421KmAu8o45Qwyu2FxbtdB0Eyjb5LwWKyc9_LuIENghDW5uIUaYvjbsKMaJBvSh8qYVg0P-bXrO0Rw7gEYQ1o9AKx5oLG5kzvLt7k80kgCGsN9WHIeuPZPLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eXxsd-PvF2hLmOa49tI0Fon0JORYw-oDb_dipMdnjiPeUXlOhM-2OxylMm68o7vbW6MZby_CApw-_Vi9tWV1XP2lDi9M3Q4kmmqC2B09p_OPqT_NmQackKP_2tvROisGf-DU_LsJeg5Z0kQT-2rLOd9wgKl4cVEv8x2jnBFaj4kB7exj4n2PZ7t9-vIM2y5Bf3E1ZrlfmaFLvakCO7fxI-R7iMXTMnGDzNrckpYY6CFkk0H-1ayBRnbaxXX4TkLW9BltasrT-963YEFwRtP5KcAg5Xee6J6HRLpKGzfmNMjZj8d9fS6JyihhXpmrEfj61t9LJg_0PrAOr5W75TePUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CytGKtMjem6W2PaoC6NmVUIcgHgD0kTp6V46EJ6uH2JHWXMy0yYt4tgfe_8ASBXrxvUUhFWG17ik05CNY4opyr4fManfiEwW6zgjA-3IXpYpqvpTiG-PL3DO6ueNgejRTpNHxWDTwDmOxW71GA2YT7dJL2rUBK0rpf4bIv2eS9cmb-GjrmulgFsSj9jIXntm2dYTuVMCNqIytdr3ZHW9znFHw32ZbVK-e4PKXSAzdf-kt3zUzbjZuOXa_enIkWz2O4OuaUrDrzNMUnH_UwjPrKQ6xPei6o_eoQWC8hqIYQ7aZcwBtB6Pau3KCqomr5LLCJfFBILA-KjL2YGZY1CxIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ewxo5-2OneBzunYt4plWpu0u_EskX5Yy6IogedGGlDpKkkC4hiphHK42hKddoyuSEloFA0AwyB2YcalgS2uRhjJaGwWhw6eJ7SiUJAWy3xljSm4AX0SADF2azW4PFIHY5dEd8NeQBNNU2WdhS6SYzPv0JsjPX6GfBHJuhRJvV96_2hLc09HvhoTMMkwwsJ3znSZEfWiVs7Q2L_vwadGLRvX30rWiCEpztKuzxJKkJJUpLrlcJ2RIZ_LDBifHHqhDDO_DEXmegxLubnkLiQx_WN1tHGlB5F3LtMlSu8Pue2IUZ3DWSxvprgYUMLBK_ywRpqvsF-K0Rp9KGUMTVCpwaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
فردا که هرکسی به شفیعی زنند دست
ماییم و دست و دامن معصوم مرتضی (ع)
سعدی
#امام_علی
(ع )
#عید_غدیر
💚
گرافیک های خاص مذهبی را اینجا ببینید
👇🏻
👇🏻
@gerafic_gharar</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/akhbarefori/655956" target="_blank">📅 01:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655955">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
ترامپ: اسرائیل بدون آمریکا نمی‌توانست کاری کند
🔹
ترامپ با ادعای اینکه آمریکا تأسیسات هسته‌ای ایران را شبانه‌روزی رصد می‌کند، مدعی شد: «اگر ایران این توافق را امضا کند، به این معنی است که موافقت کرده سلاح هسته‌ای نداشته باشد #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/akhbarefori/655955" target="_blank">📅 01:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655954">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c05eb7d7e3.mp4?token=ePTx6ltzlaFF_PARfrXBFASy2iST0Ww4-y9G9pbXwOHoTkD8NPy2FnCjkGxfz4HE7fmfd3G7nEtWs_n1z_HhTKacit9iZwQKa0nSbw9Z1pHz-3KNh6_cd49j6N_H2bm1ZJFpbvinq1YqhusniKKJajIYV2O_LViAYnXmgLh1JYgidQ6GU1aoBeqZGQ4qvEN1Lo3Y0I-l3FiiWrbyToIjcgMGeTY2uZxZ9omHKm4L_tIhCRBmXeY1jWuVSVAWs53yRWVGtzPeLCFnzYsqmhE-KKjuJIavjgIcV0qgTzJAlBs009td74HIkHRWZCWiAfTvEy0_WAtncQGuNGSReI-J-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c05eb7d7e3.mp4?token=ePTx6ltzlaFF_PARfrXBFASy2iST0Ww4-y9G9pbXwOHoTkD8NPy2FnCjkGxfz4HE7fmfd3G7nEtWs_n1z_HhTKacit9iZwQKa0nSbw9Z1pHz-3KNh6_cd49j6N_H2bm1ZJFpbvinq1YqhusniKKJajIYV2O_LViAYnXmgLh1JYgidQ6GU1aoBeqZGQ4qvEN1Lo3Y0I-l3FiiWrbyToIjcgMGeTY2uZxZ9omHKm4L_tIhCRBmXeY1jWuVSVAWs53yRWVGtzPeLCFnzYsqmhE-KKjuJIavjgIcV0qgTzJAlBs009td74HIkHRWZCWiAfTvEy0_WAtncQGuNGSReI-J-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ مدعی شد: ترجیح می‌دهد جنگ نکنم  ترامپ:
🔹
ما می‌توانیم جنگ را دو یا سه هفته دیگر ادامه دهیم و همه را از بین ببریم، اما ترجیح می‌دهم این کار را نکنم.
🔹
توافق فعلی، در صورت حصول با ایران، نقطه مقابل توافق قبلی امضا شده توسط اوباما خواهد بود.
🔹
محاصره ایران…</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/akhbarefori/655954" target="_blank">📅 00:56 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655953">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">هم‌زمان با فرارسیدن عید سعید غدیرخم و برگزاری مهمونی کیلومتری، قطعه «شاه عشق» با صدای رضا صادقی منتشر شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/akhbarefori/655953" target="_blank">📅 00:39 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655947">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d74e967f12.mp4?token=EHJAYmzk5JgJu3OinYbFjdFuqTDEpZzWYtRe-UAgtuAm-Pcg1Zqj4FIfOAtmEPGsZB_AbktxpBb_ozdHn2gKV1qAJN8Ej7UeSlaFwRLV2FWNTVz2s9HmfYZ_XyqOoa2K8GpyLj3z-9tB8sabV9pY1PM7jHHfD6lwLIy2t57lY3L8XHrYnZD0KPIwS-hd4CDaR1oLhvGjPW3zhu9z7_E1zMNydAZc2BGPyiHuPh0oPXjRsFXfybe7HVkgJYGC1kHbNcZC4Nxv8ZtRAlFPaVdxEapGCaLxywytTmoDbXO9xTmijkkJDsG9p1qGQRajXYjqyDF9g4XEd3Z_tjwFa4CSPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d74e967f12.mp4?token=EHJAYmzk5JgJu3OinYbFjdFuqTDEpZzWYtRe-UAgtuAm-Pcg1Zqj4FIfOAtmEPGsZB_AbktxpBb_ozdHn2gKV1qAJN8Ej7UeSlaFwRLV2FWNTVz2s9HmfYZ_XyqOoa2K8GpyLj3z-9tB8sabV9pY1PM7jHHfD6lwLIy2t57lY3L8XHrYnZD0KPIwS-hd4CDaR1oLhvGjPW3zhu9z7_E1zMNydAZc2BGPyiHuPh0oPXjRsFXfybe7HVkgJYGC1kHbNcZC4Nxv8ZtRAlFPaVdxEapGCaLxywytTmoDbXO9xTmijkkJDsG9p1qGQRajXYjqyDF9g4XEd3Z_tjwFa4CSPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✨
پک استوری ویژه عید غدیر
✨
گفتی ثنای شاه ولایت نکرده ام؟
بیرون ز هر ستایش و حد ثنا ، علی ست ..
🌿
#عید_غدیر
💚
#امام_علی
(ع)
#استوری
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655947" target="_blank">📅 00:26 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655946">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">♦️
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔹
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید! #Devil
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655946" target="_blank">📅 00:10 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655945">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f398eb77fe.mp4?token=C9Zv0rSfR3Lk81V57wclIj0v79108o3J4RWmK6pGyZYWkUeI5lWrgsHhEdl5ectaFRTB8B1fOnvckcS2lAFPUco56T5JjT7PPpqztLO3DASP0dfmXEP7Ux4RXfr55rwadqfslhc0QmGm54R9k0ZqiDbSpK62qM4f5qzfGqCQHeADWcTG7VSs5ff4n39Lnqv5ojarJeAEyc5-qlnMylb2tpuMTZeycbr1hRUwlRcmRo7lk2kgiC4d9z70NKXixOnA-kdNcbA_tcTRgqXJlylWm6VGMtTIw8qUcIomlGIc2xHJ_l9nSRSHaNuqQPLikzUm_BWuTLZ3sNe3AlrfnY9C4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f398eb77fe.mp4?token=C9Zv0rSfR3Lk81V57wclIj0v79108o3J4RWmK6pGyZYWkUeI5lWrgsHhEdl5ectaFRTB8B1fOnvckcS2lAFPUco56T5JjT7PPpqztLO3DASP0dfmXEP7Ux4RXfr55rwadqfslhc0QmGm54R9k0ZqiDbSpK62qM4f5qzfGqCQHeADWcTG7VSs5ff4n39Lnqv5ojarJeAEyc5-qlnMylb2tpuMTZeycbr1hRUwlRcmRo7lk2kgiC4d9z70NKXixOnA-kdNcbA_tcTRgqXJlylWm6VGMtTIw8qUcIomlGIc2xHJ_l9nSRSHaNuqQPLikzUm_BWuTLZ3sNe3AlrfnY9C4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ترامپ: آتش‌بس یعنی شلیک ملایم!
🔹
خبرنگار: تعریف شما از آتش‌بس چیست؟
🔹
ترامپ: آن‌جا [ایران] بخش دیگری از دنیاست. متوجه منظورم می‌شوید؟ در آن منطقه از جهان، آتش‌بس یعنی زمانی که با شدتِ ملایم‌تری شلیک می‌کنید!
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655945" target="_blank">📅 00:09 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655944">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l3RXjD40cEk-hA8proKLXj0oakqMDuYGzvlyRKO129O7ocxMN3jeQZcY6I_yMj39TI9q9UmxLa80DZLICrNZI9UOWnzRO8jVxqbXVCvgEKRgWtxSr6W-dKxB_RV8HmdJ1dZyQRm-Pv6-yfH5-TnooX8K2SUBPssu288Ho9UusTEgjikYgjLPcswdQ0MTEb8IQVZ1ud0p4O9Q07006jd0eNSa4sPFVrrMQa5Sz5RUJCzgBIhk0fTGslFeO1o305W5pkWuiWPIEnHWp3ynRtqAllD7GEpcLYgl5KsPNwUG6L0a-GVaAvBgfQ5mRI3NSFt-vbcBr9_GjNGP1Fyk2lICDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
*فراخوان، رها ۱۵ ساله را به زندگی برگردانیم*
رها، دختر ۱۵ ساله‌ای‌ست که با سرطان خون می‌جنگد و برای ادامه شیمی‌درمانی به داروهای حیاتی نیاز دارد
💔
پدرش را از دست داده و مادرِ دلسوزش با درآمدی اندک و زندگی در خانه‌ای اجاره‌ای، به‌تنهایی از او مراقبت می‌کند؛ اما هزینه‌های سنگین درمان از توانشان خارج است
😭
🥺
با هر مبلغ کم زندگی را به این دختر معصوم برگردانیم.
😭
🙏
🌹
💳
برای کارت/شبا کپی کلیک کنید
6037691990480709
5892107047084630
IR420190000000216756895002
پرونده بیمار
|
مجوزها
|
پرونده‌های تسویه‌شده
|
تلگرام مهرآمن
|
سایت خیریه
|
برای گزارش پرونده های درمان زیر ۱۸ سال پیام دهید
@PoshtibaniDarman
👈🏻
خیریه مهرآمن با هدف کمک به کودکان بیمار، تهیه دارو و درمان، و حمایت از کودکان بی‌سرپرست و کودکان کار فعالیت می‌کند. مازاد کمک‌های مردمی صرف امور مؤسسه و یاری به سایر کودکان محروم می‌شود.
💚
کانال ما
👈🏻
https://t.me/mehreamencharityy</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/akhbarefori/655944" target="_blank">📅 00:05 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655942">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QAvhWSyNbw44_6Os1jii9vB_saAjZLFX9SmemAbdwL43a4mvtwiuE9SWyZ2g9lhM9OyHlOl15HPhUA86OeAORWSZKwKogDC2BKa4n0H2yodcscqVJK1zBxdlzWbuF60q4rfejQQ8s0rolILU34qo4elH92mjf8FalPw05N-Jt4G07N_-yomwwwU2eUU_PhpiwcyPVxr109OLYUmGIJKjcFqD_WPPmil_ZYwri4sj4jCRPmESGgUZM1fiuT1d8TIv6gbqZqYzJe1BPlIbF0fgpskSreSRA4aq7JYqFzeLJ8jNfcU6pRmBr68e83G8rpUD1-63WhN48tuz3TXfNzzF9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/akhbarefori/655942" target="_blank">📅 00:00 · 14 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655941">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ اسدالله</div>
  <div class="tg-doc-extra">حسین طاهری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655941" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
می جویمت می جویمت باید که پیدایت کنم
می خواهمت می خواهمت باید تماشایت کنم
ای دل اگر یاری کنی یاری جانان میکنم
مست علی تا میشوم رو سوی ایوان میکنم
🎙
#حسین_طاهری
#عید_غدیر
💚
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655941" target="_blank">📅 23:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655940">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54d945556a.mp4?token=uZRMyiW-cEuxG0F845dFL7JrP93Nh2qvvICrN9PMtUi2fTL5InqS4mmU7ieDyPzxUQhmR2yQ-iU6vOidp2X7rCzc-OipvWyT28YZ3uagwm2Ba3k5Z7c-QorcVmoanWpSeAn9oRNMK1zopomcRECy1-8zDKRarGvTjG269CSycOt1WiGXuzu-aHLiJCNL50SpPrUeZXHYloVlIlzKDuOKKJa6R42t2qS6kYdPdKuFHrc8T6y__ebSugxQlRLy3tiqdPrXr0r1cmb98U75ZT3wAZC-8mtskDZ09OXzadkyIFkdyrEgxfUKGtU-53ROnw-IOg0O1uehrZKGfW7vzdBmyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54d945556a.mp4?token=uZRMyiW-cEuxG0F845dFL7JrP93Nh2qvvICrN9PMtUi2fTL5InqS4mmU7ieDyPzxUQhmR2yQ-iU6vOidp2X7rCzc-OipvWyT28YZ3uagwm2Ba3k5Z7c-QorcVmoanWpSeAn9oRNMK1zopomcRECy1-8zDKRarGvTjG269CSycOt1WiGXuzu-aHLiJCNL50SpPrUeZXHYloVlIlzKDuOKKJa6R42t2qS6kYdPdKuFHrc8T6y__ebSugxQlRLy3tiqdPrXr0r1cmb98U75ZT3wAZC-8mtskDZ09OXzadkyIFkdyrEgxfUKGtU-53ROnw-IOg0O1uehrZKGfW7vzdBmyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت بغض
‌
آلود دیدار بانوی لبنانی با رهبر شهید پس از شهادت
سید حسن نصرالله
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655940" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655939">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نماینده مجلس: دست تولیدکنندگان خودرو و دلال‌ها در یک کاسه است!
فرهاد طهماسبی، نایب رئیس کمیسیون صنایع و معادن مجلس در
#گفتگو
با خبرفوری:
🔹
تولیدکننده‌ها و دلالان دست به دست هم داده‌اند تا قیمت‌ها افزایش پیدا کند. خودروسازان خودسرانه قیمت‌ها را افزایش می‌دهند و اعتنایی به جایی ندارند.
🔹
مبنای خودروسازان برای افزایش قیمت، مواد اولیه است ولی مواد اولیه‌ای که نیاز داشتند با قیمت جدید نخریده‌اند و دو سه ماه قبل، خرید مواد اولیه را انجام داده‌اند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655939" target="_blank">📅 23:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655938">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
ادعای ترامپ قمارباز: مذاکرات خیلی خوب پیش می‌رود
🔹
دونالد ترامپ، رئیس جمهور دولت تروریستی آمریکا در نشستی در کاخ سفید مدعی شد که مذاکرات با تهران خوب پیش می‌رود.
🔹
خود مذاکرات خیلی خوب پیش می‌رود... ممکن است انجام نشود، اما اگر انجام شود، احتمالاً در آخر هفته خواهد بود.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655938" target="_blank">📅 23:51 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655935">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">زیارت-عاشورا-pdf.pdf</div>
  <div class="tg-doc-extra">115.8 KB</div>
</div>
<a href="https://t.me/akhbarefori/655935" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
فایل pdf
#متن_زیارت_عاشورا
همراه با ترجمه
@Heyate_gharar</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655935" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655934">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">-زیــارت‌عاشـــورا</div>
  <div class="tg-doc-extra">| هیئت قرار ‏@Heyate_ghatar</div>
</div>
<a href="https://t.me/akhbarefori/655934" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">▫️
صوت
#زیارت_عاشورا
🎙
#علی_فانی
@Heyate_gharar</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/akhbarefori/655934" target="_blank">📅 23:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655927">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F0YMlm3Ng6ab3ekTq58jvn9WXFwuNsWSBTc_O0btjKZxkRktvY11200QVcjj3CqRm_06qm0hcWLmuHcf80IU6s7PqN1wDCr6T9lN2gJE9vzDZYQp3lqIfZyFZZpIkknQKQi4oBZ-YvebZPUvufIVmx2o0sufGrvi6fbswyE8CoR0hibwZR8xFNb3bWwUL5IfOSQTsfZkcYBpaXEUmOP4FBx2oAuZ5wgG5wvkbRrmGbtEJkUEtdt0rNkI1T3STekYdaKJaYcD4EJI87cuQmMWSAqGlUtiEMmwcLrJ11C0VYwBJGtYUK_bN7xM4qBa5a_9nuchSQZzOrtC5_sbEFp2qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5YaBqMz8yynsdpktvLth1UARvFs2aAxLtTWKEoYigRlr-V3r1Nx1KCqSS7K1MikS7VKGJOC5vEiF-kZH-u72brjuL_Z5TWPwsJM84W3EfYvZBsJJ8doEPTPy6EQVcKP4ZJVFbnEIZ8wQHxaN3yu3BahXUI2xoxZMbE8g8tJ2SgV07szkdOErQt-Uwb41_h_ISdDuumZPMYW_bTe4rEYYdvAe2Qs4XUgwNBzPyZD_lyqhVufRnBIk0caNLoKilG4dEv2OEERA1XV2pMDLRXrJ8jGhGL1lRD4gM-vCkG-2-1jO6e6dobpEJv_1Z5CSZpBla-DcOiwgiTVa90zMuT25w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BuvX7z1TxfP7S0Ck-ECkTXJGP4I1hrdddTTtA1R2njRNt3iJMo-O-VW2Pna5eRlpUErzPnMZvYU8tUAsmiobHsXNQ3A1TmtReg8zSvWvv_KlQmgEmh3EiDHSdGMShPCPpsUlrgUqeemc8SH6eevGckq9wnaGBIY5IqpMU-eVRIxwCOyNz0XG-2OlSTsCYOe_NbtgIXZtyv2a_B7Yb6_zry5VsZMUJSnbR3XYzaW6ygTvF_nK5gpYBTVyHF9gshN1KGSXELVAOynS3ax3X_U9ptpVrdBuHuzZHUdwTbFPUloooY37ctP3IZYlP7f-ERygJDQQ7xRYpVFsfRAkNc7vDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gq7B1QVKYGqH2daYhYc1SuKk8Mb6yXFmsknNTSoJ0ocqc2Ze7KIAvQ_qZOGexH3gNgFVz3cDoc-2kG2sNdtoC29teVNfSgWfllXQ2J8A7-MW2Wcga39MrYsJ86itZwxmpBySZyc_nULN7ZHWi33bLadY93unNNEi2z6GAfBz_H_g-XOzj8he1Yn020YAs6w-kM_yXFaqC7Oue0XkC8rztXh1DPz0xmRThTfiKAzsXsbLqXHM-g-CdndOBx8MhZOR8HJv-ZE3MJHEsw7NWTHwDwHLcs-y96yAFtsMjmYMJmYrAXPZBHP2MMpMmj_TUg-Lz7JaalTswVR2zMN_aO8nCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fegg1pUIXiODtMPnZyuZOiilkZINWpdHwoD8qKwdQiOseCDRAceH9wO2BzU2HoWfRyxWQ_5xuHo_1uvAfb3r9BuZqNbd67-IyrVKsWf5S-xnN1WmEyHzU6dM9XYQder9y6_TppL4lNPyJs2RH1WWsyfOeYqHLLTV7tWc2bsjZxnvkJjygYdzM5OdBXVMN_ptUxi3oDyqj2jNps2NLLMJVSyyx4rEt_WN_QX0vrqZqJ9YZjeMQWB_iNYWOl5oQ-DCCZswzhSJ21qgkMNFqVT2Gie6DzfrAjZRxTcPJlK1TKD81Hr5RTIFTSg-ZgFLltmHAh4IVrP4CJgmfWgpmxfHrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uurIAvfKzToJHSIwYqmL8tI2c210LU7JKt454JRzsma1CFVRVz8uC0m-fypdSodxkKkkJB4p94AjkbxhVx6pkvA4qPy-mf0eLikdjHwvqZt0ww6P5XQI2hciIeit2B0bjjM-xVjs71wV63cAMN7rqOZhiMmXx6DmJMssG9wRr3jQySyQonPzZkiqfahtkgEgfNWKdCkqqXDBQvp5DCfPrZbkRzho3d1BTPAQ9_uy7AXosnOA76X-pcUHnvhtfGVzRfgexGKhhRjlYH7CzxioioT5hopaqVSzW48HE3mcHbwPj5Qw2eyiHT_QCx7jW2L7jo050u6di9BwAhqHGUobaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XBTI8F-KU1_c3vL59NZjR2K8Z8_qyZaB8iT0oEsCYgLPVJwjHX-yYFvpP0CBVaNJKcKcwwtUx3DzhyBIyqOO_DEP9IC-AsQ18wChrqEbTmwGOZ1MOxymjpBldHr0gWidXBwB5UmqMaXq0uQt9kw65BDyC_y_WNf8zb5XPamfaUlgGFejsunWKHSBKEsbkOwrm8cXtqutjhpDzAHSIIxGbqI6Bh_zDq7KYA6MdISzFkq_4txwWKpjtt32HLqJfxhtmxXDrPgvVsNjORVH6cOa3cH2ieEHIQFIEkh7CVVGRpAlNaQsl_WtDP3pqd5lsKG2tA5zOnW1e-BrsCJCfOVSXg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از مرقد امام علی علیه السلام در آستانه عید سعید غدیر خم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/akhbarefori/655927" target="_blank">📅 23:46 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655926">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/soLA5cxexLzWfO2uokFY-1BVnFHafNw4JQIpTlF7Cfc38sQmvVR9-HOMqag3bE-27Hk35nprPv_IF7WRMypNPhoIx-6tDu_KTAdGtP4IDW9cXpjGZG0L29UfiT1NkdC9KFkLH7K4UjH-o-pdgzZoZWEC7BDkxtqsRLd5QNC1aHGyYPXYBkBOGmsPpkq9vvjJm-JGEFzUH0TPo7he1Kj2P2Owg5Q_Re0-qi_Ux-6Jqnkqy32Maeck8pRVsF70BeB0FjdyFl8J79gRoDP3S5eCuITIfeH_9EtZPHYwdrFX9VQntrY3mILmbonNolX088ZprDsOJyje4DPntEWPGpZcNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا نتانیاهو مانع توافق ایران و آمریکاست؟
گاردین:
🔹
نتانیاهو، به دلایل حیاتی شخصی و سیاسی مانع اصلی توافق میان تهران و واشنگتن است. او با انتخابات زودهنگام پیش‌رو مواجه است. کنست اولین قرائت لایحه انحلال پارلمان را با ۱۰۶ رأی موافق تصویب کرده و انتظار می‌رود انتخابات پاییز برگزار شود.
🔹
محبوبیت نتانیاهو پس از افزایش اولیه، با طولانی شدن جنگ‌ها کاهش یافته است. او به روایتی از «پیروزی کامل» نیاز دارد تا در انتخابات دوام آورد؛ توافق با ایران این روایت را نابود می‌کند.
🔹
جلسات محاکمه نتانیاهو به اتهام کلاهبرداری و رشوه از سر گرفته شده. او از جایگاه نخست‌وزیری برای به تأخیر انداختن دادگاه استفاده می‌کند؛ توافق، موقعیت او را تضعیف و آزادیش را در معرض خطر قرار می‌دهد./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/akhbarefori/655926" target="_blank">📅 23:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655925">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">♦️
روسیه: ایران بارها اعلام کرده در پی سلاح اتمی نیست
‌
نماینده روسیه در سازمان‌های بین‌المللی:
🔹
ایران بارها اعلام کرده است که در پی سلاح اتمی نیست. ایران بیش از ۴۰ سال پیش، زمانی که به پیمان منع گسترش تسلیحات هسته‌ای پیوست، موافقت کرد که هرگز تسلیحات اتمی در اختیار نگیرد.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/akhbarefori/655925" target="_blank">📅 23:33 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655924">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qTzp_2ofL2ibjEiXg2jp-h5MRkWNaZ_3ZBZpbpDfrZerFQBnDY14kXMr0Kr3BMtnRU52v9mLlEs1Qsltc3OUtv9k6HcD6ufDsvNr58LDiok4hsQFIV5x34rQCG8F9Qo2FMJCLijM8_N6d3D5LnlHVTj4udcXuK8SxSjNLJfgnoPMYt9q1kHZCwNiZ2t6IWVBinCn2j0q_VRSgODpE8Wi32QXnCtnyhd5O-oNf-oGOVxP4wU9VRgVcc2iOAOL-a5uoTJzzzkQqhvu0yKw1rUN2xm9m6TSqI_ufGcFMBYuXzVgtK2GKRLjG09Ou76yR4cCxdIpwQ1WYM3ljTY74T5zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر را روایت کنیم
🔹
امسال شما راوی عید غدیر باشید؛ عکس، ویدئو یا حتی یه متن کوتاه ارسال کنید
💚
🔹
همین کارای ساده، حال‌وهوای عید رو قشنگ‌تر می‌کنه.
#فقط_به_عشق_علی
#LiveLikeAli
شما هم به این پویش بپیوندید
👇
@Ertebat_baforii</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/akhbarefori/655924" target="_blank">📅 23:31 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655923">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔹
خبرهای داغ امروز و امشب را از دست ندهید
🔹
🔹
ترامپ: دوست دارم با رهبری جدید ایران دیدار کنم
👇
khabarfoori.com/fa/tiny/news-3220188
🔹
یک چهارم کودکان ایرانی از تحصیل بازمانده اند یعنی بیش از یک میلیون کودک
👇
khabarfoori.com/fa/tiny/news-3219779
🔹
واکنش دوست محمدرضا شهبازی به شایعه تجاوز به او
👇
khabarfoori.com/fa/tiny/news-3220245
🔹
این دختر نوجوان فروشی است!/ عکس مادر در حال فروش علنی دخترش کنار خیابان!
👇
khabarfoori.com/fa/tiny/news-3220211
🔹
سردرگمی عجیب در اعلام روز کنکور و امتحان نهایی/ کنکور رسما بحران شد
👇
khabarfoori.com/fa/tiny/news-3219943
🔹
ویدئو‌های جذاب را در آپارات ما ببینید
🔹
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655923" target="_blank">📅 23:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655922">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28189c9644.mp4?token=tUh2bK7yMyrm8lwAyhQlZDafxxiEfLa6_wkO84fhtiJfTfePOsSY76fzizushhjTaKZIEiQiw1S4M55Nz2rUJIMi8Qy3NTtpxPl3OWM1aYHsDVy5u9EiCh3HqPa1awuJXgX0Q5b8GP8YYxPmPNMk3aZ_3txLYZbJ-As7myYbkVgqgiychUp4eu0bA6NkByWL9-FOnsyFewgkRUBAc__YJkPL0gNVs_kLwrMOjCTB50tEWIZsULIk28RS5I4mryxqeBAHZnJLb4MM7RB1_W6pxxvb-kiZoO-XgKHCMhXuFcb55SEQGcGg4g2aUvElkkB-LL-4nkWh7BSwJRyClxM7Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28189c9644.mp4?token=tUh2bK7yMyrm8lwAyhQlZDafxxiEfLa6_wkO84fhtiJfTfePOsSY76fzizushhjTaKZIEiQiw1S4M55Nz2rUJIMi8Qy3NTtpxPl3OWM1aYHsDVy5u9EiCh3HqPa1awuJXgX0Q5b8GP8YYxPmPNMk3aZ_3txLYZbJ-As7myYbkVgqgiychUp4eu0bA6NkByWL9-FOnsyFewgkRUBAc__YJkPL0gNVs_kLwrMOjCTB50tEWIZsULIk28RS5I4mryxqeBAHZnJLb4MM7RB1_W6pxxvb-kiZoO-XgKHCMhXuFcb55SEQGcGg4g2aUvElkkB-LL-4nkWh7BSwJRyClxM7Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و در پی اقدامات تجاوزکارانه، نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655922" target="_blank">📅 23:29 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655921">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tA2WtZYbPemmL5eFrMViTy5sjXLv60tk2wdnxTaAvBtr2pok_cdPwvkqVEk_lY_aCOioHd_TIXtl0blTgN8gjnSXPrMRItj37xjvCUMnnQvMBwb5ZbGH7WlRou1-seoiMYDQIdw1oq1O3jL7p4nK-IQcaXU6oEtQsERBm1kKAN0U12w9jNqaDMpwBT8TaqiZcKNx8yCzxSwVqm7Ay6dlzZ9K3hfMhMDOWp7voACsdPPiIuo6heUu97J-r7NqUrenGVi_ajsFmiPJymPM2cCn-STI2mCXmu367n_eFuqmchiFnKtoa63vdb8qg3fsH47ifh2npEwgSWRsvpIE-FRz4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تنگه هرمز بمب ساعتی شد!
🔹
دفتر توسعه و تجارت سازمان ملل هشدار داد که در پی بسته شدن تنگه هرمز، رشد تجارت جهانی از ۴.۷ درصد به کمتر از ۲.۵ درصد سقوط می‌کند.
🔹
اختلال در تنگه هرمز، هزینه حمل‌ونقل و بیمه را به شدت افزایش داده و فشار مضاعفی بر تجارت وارد کرده است. همچنین رشد اقتصادی جهان از ۲.۹ درصد در ۲۰۲۵ به ۲.۶ درصد در ۲۰۲۶ تنزل خواهد یافت./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655921" target="_blank">📅 23:25 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655920">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">به ازای هر کودک تحت حمایت بهزیستی، ۲۰ خانواده متقاضی داریم / در بهزیستی هم مثل هر جای دیگری ممکن است کارمندی کوتاهی کند
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
تعداد متقاضیان فرزندخواندگی در ایران نسبت به کودکان ما ۲۰ به یک است. یعنی به ازای هر کودک، ۲۰ خانواده متقاضی داریم. در شهرهایی مثل تهران و مشهد این نسبت ۲۵ به یک است و لذا ما همیشه با خانواده های پشت نوبتی مواجهیم که فرزند می خواهند که ما به دلیل وسواس و حساسیتی که داریم یا به آنها فرزند نمی دهیم یا کند می دهیم.
🔹
نگاه ما در سازمان بهزیستی این است که سلب حضانت مسیرش را کامل طی کند و پرونده دقیقی تشکیل شود اما مثل همه دستگاه ها که گاهی آرمانشان با خدمات‌رسانی‌شان متفاوت است و ممکن است کارمندی کوتاهی کند، در بهزیستی هم ممکن است پیش بیاید.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655920" target="_blank">📅 23:22 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655919">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o-L-QWhQU3sxRKFB4aV40sguDJb_P9QX5h0enbbjAmuP-yGa1hSwOn8bJFKfUFuVIsOhuBpGAHcm0M0eMM8MZh204wsEC-LpZks55DhhucHbp8J8bt2xyQkv_3YvbWtyZ9X0W0U5CPupAq1NeuTFBVkWjJXQDPi_BkKTPrOokUuzxQZWgYMruN_-F9nHbJGLnLL-ODZZkylq8ekhyKj7KuaGI1NSuZkmlL5WhDdyDyL_9tX3ZFQ3a5r18-Y9uboa0KOHN4seZqCpDCIl1CT6ENiFxhWu65GPhgUszDbKHjgM3ICOfwJnHjqFQoXv9Bq8z2dUV_UTuH20-r3T1N5B3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برنامه اصلی مهمانی ده کیلومتری غدیر در میدان انقلاب اعلام شد
پنجشنبه از ساعت ۱۵:۳۰ تا ۲۳
میدان انقلاب اسلامی</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/akhbarefori/655919" target="_blank">📅 23:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655918">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ بیعت با تو</div>
  <div class="tg-doc-extra">حاج محمود کریمی قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655918" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
ای دین و زندگی من مولا
بخن بخن ابالحسن مولا
جون هر کی که دوست داری امشب
به ما هم یه سری بزن مولا
🎙
#حاج_محمود_کریمی
#عید_غدیر
💚
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655918" target="_blank">📅 23:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655917">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0FrfCa3jFFQNkQC0146ag-y2lO71DSlN_uX6yRwvy67DNOUEvsCmyv3X0x-oWFoPxVOEH6UNZjzvwKh-IKYrq4OP535ecRq-XYexlEt2aJQShE_0r90hLHg3seRHQVXJmrvEen5s_DZwo5VvovF0Z7FBRjWcuUGQRrgiIPb-Pt-ICMJm4hZyE9pJj8c31DUXmBo8mKjs9axqG9Ym7TfTfRArtxOESM7SkAPs31GOPChgtZnOKHm9L6uI2t2VjhD-waHIJBl8JwKI6-vIO7Xb2VC-CK9R3pGz_rHlyhzZis9cvqejcrQ5F8CAGd4GxV6rm5aDES-NiRiBxwJayHsYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
وضعیت دفاع آمریکا از کویت
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/655917" target="_blank">📅 23:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655916">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ed9351f0b.mp4?token=D4S0d0CBbrbMn0pzn5ZWtol21CoOuhgEiA6BshcPYpytq1j79nwcg4tmgRXfXeskSIGlhRi4lWC8JvfRjLDeBZ-EdWuFMSUgt4oQ19WcjBzjof62ojPQqPhB3i4baPnllSPn52Nd0endrNGL21Cxl2REGrhkhNEGKsuJdYmcNLoDAiakrsWWOtqV1JDz6dNNWLDyQRg69w7Mzn5ppaIzh9anJ5pBmZrFJ2b0YhL7by3SE_pmyc4cU4C9pWQn2827k6-kr6zFTIDcA5acNMV9IeXB13QEOVBo-BuGJZPVgT_3KyFlwfm2qNu0sF6VGOEOSPm3-c3qFeISTUCUgzAtwnSJlT941dMvH3McIMytUQ8ornZzTy4HzpETMp229KUprcRCBwfBGl1q6WykncER1rAu-Ne99eP7Q841PCEYcCbSYLcrepmqwzCYqpzO36UqMjm5-k1MxhFCSAEwsczV3MEKMstyCPB-nJZ6Kj7p3ZfTzhTkwXVPFs5mXyam86TPnJdxyDSHibDrvqJiLL-GTQKW43LklpBeN3jAlPUjqjmI9aCtBTVIBQr380aDooiFXs6RYSo2mfZfEHcOHF5Ifh5SRJsA_9vEMMAunT_rUHEELqBfEFjTmhMeEld0r3zn-MLB4DSKu_XBAarrHceap94X12X44DUB61hAOgkKr_8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ed9351f0b.mp4?token=D4S0d0CBbrbMn0pzn5ZWtol21CoOuhgEiA6BshcPYpytq1j79nwcg4tmgRXfXeskSIGlhRi4lWC8JvfRjLDeBZ-EdWuFMSUgt4oQ19WcjBzjof62ojPQqPhB3i4baPnllSPn52Nd0endrNGL21Cxl2REGrhkhNEGKsuJdYmcNLoDAiakrsWWOtqV1JDz6dNNWLDyQRg69w7Mzn5ppaIzh9anJ5pBmZrFJ2b0YhL7by3SE_pmyc4cU4C9pWQn2827k6-kr6zFTIDcA5acNMV9IeXB13QEOVBo-BuGJZPVgT_3KyFlwfm2qNu0sF6VGOEOSPm3-c3qFeISTUCUgzAtwnSJlT941dMvH3McIMytUQ8ornZzTy4HzpETMp229KUprcRCBwfBGl1q6WykncER1rAu-Ne99eP7Q841PCEYcCbSYLcrepmqwzCYqpzO36UqMjm5-k1MxhFCSAEwsczV3MEKMstyCPB-nJZ6Kj7p3ZfTzhTkwXVPFs5mXyam86TPnJdxyDSHibDrvqJiLL-GTQKW43LklpBeN3jAlPUjqjmI9aCtBTVIBQr380aDooiFXs6RYSo2mfZfEHcOHF5Ifh5SRJsA_9vEMMAunT_rUHEELqBfEFjTmhMeEld0r3zn-MLB4DSKu_XBAarrHceap94X12X44DUB61hAOgkKr_8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عراقچی: به طرف آمریکایی اعلام کردیم اگر به بیروت حمله شود اصلاً تحمل نخواهیم کرد
‌
🔹
آنچه در این دو روز گذشته این وضعیت جنگ را متوقف کرد قدرت مقاومت بود؛ قدرت نیروهای مسلح در ایران و مقاومت لبنان.
‌
🔹
وقتی دستور حمله به ضاحیه بیروت صادر شد، ما موضع بسیار قاطعی گرفتیم. نیروهای مسلح ما آماده واکنش شدند. الان چندین روز است که اسرائیل آتش‌بس بین ایران و آمریکا و همچنین در لبنان را نقض می‌کند، اما حمله به بیروت یک نقض بسیار بزرگ بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/akhbarefori/655916" target="_blank">📅 23:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655914">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
ادعایی عجیب؛ تمام خسارت‌های ایام جنگ به مردم پرداخت شده است!
علیرضا نوین، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
هزینه آسیب‌های جزئی جنگ در کلان شهرها پرداخت شده و بنیاد مسکن در شهرهای کوچک زیر ۲۰۰ هزار نفر، خسارات مربوطه را پرداخت کرده است.
🔹
تمام خسارت‌ها پرداخت شده و در بعضی موارد با وام‌های ودیعه مسکن و در موارد دیگر نقدی و غیرنقدی پرداخت شده است.
🔹
پرداخت غیرنقدی برای ساختمان‌های صددرصد تخریب به صورت تراکم دادن انجام شده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/akhbarefori/655914" target="_blank">📅 23:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655913">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b43bd65e5.mp4?token=J_K1KDp7RkIlxy7ffeEiWpWRF2BmCdD9No0cGK30FvyUBrfAsHV7w4xCjW_KS7cEQOP3UlBW7gMiA2gueglMlRmUZX4I4cQYwyuAqmQ7nkgfHA-FUMNrjXLjnWTXsHXxIqAQf2ucsVhqC5ecU0Fs4-fl9y8omWrjiVR4l4bYOzyQjUaGklW8OY9a5rekwmK2VdvkAVtx7rMlw8IARHVZRp0r8O7QSHNIrLbHUYv-VSQKWFBtLidTf-ILzQu_6Ga8gT1dLrzuCuYDOZxu_xEGpSIZzq334vf9nmJimBuPW-irn-AnHGicqG3e3b7EXtMIXz0tBjlQ8uN2IuJJDFFm8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b43bd65e5.mp4?token=J_K1KDp7RkIlxy7ffeEiWpWRF2BmCdD9No0cGK30FvyUBrfAsHV7w4xCjW_KS7cEQOP3UlBW7gMiA2gueglMlRmUZX4I4cQYwyuAqmQ7nkgfHA-FUMNrjXLjnWTXsHXxIqAQf2ucsVhqC5ecU0Fs4-fl9y8omWrjiVR4l4bYOzyQjUaGklW8OY9a5rekwmK2VdvkAVtx7rMlw8IARHVZRp0r8O7QSHNIrLbHUYv-VSQKWFBtLidTf-ILzQu_6Ga8gT1dLrzuCuYDOZxu_xEGpSIZzq334vf9nmJimBuPW-irn-AnHGicqG3e3b7EXtMIXz0tBjlQ8uN2IuJJDFFm8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر اسرائیل پهپاد منتسب به حزب‌ الله را به شورای امنیت سازمان ملل برد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655913" target="_blank">📅 22:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655912">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
صدای انفجار در بحرین و اربیل واقع در اقلیم کردستان عراق شنیده شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/akhbarefori/655912" target="_blank">📅 22:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655911">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">♦️
در طول جنگها کمک های مردمی کم می شود اما در جنگ ۴۰ روزه فقط کمک به بهزیستی ۴۰۰ درصد افزایش یافت
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
کمک های نقدی و غیرنقدی عموما در طول جنگ ها کاهش پیدا می کند در جنگ ۱۲ روزه ما هم این اتفاق افتاد چراکه مردم احساس ناامنی می کنند و نگران منابع زیستی مثل غذا و دارو هستند. اما در جنگ چهل روزه این روند معکوس شد. کمک های مردم افزایش پیدا کرد و فقط به سازمان بهزیستی هزار و ۷۰۰ میلیارد تومان کمک کردند که نسبت به مدت مشابه ۴۰۰درصد افزایش داشت. این یک قاعده گریزی بود.
🔹
همچنین ۳۰هزار نفر در قالب پزشک، روانپزشک و مددکار به ما کمک کردند. ما به این جمع بندی رسیدیم که از این فرصت در پساجنگ نیز استفاده کنیم و آن را استمرار دهیم.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/akhbarefori/655911" target="_blank">📅 22:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655910">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5706309767.mp4?token=awESIZvQBnCe2ib8-lRMZiHVL666Zp103Kez15a_V83GRoSr8Bt8DAQiczqQqAMEDigEMwz4D6R2m_rGQRSnAn8Owal0TBjm3zZFZPcss0U70GHaFczMsxvAMOgXRBdN-yBvp73XDfLYGPqk6GfGsoI3IJOvqocKtpvYC7HFD8MzB79uxeNN4silPkZ1QLsRzgFBd7xr8lhm0nNdBg6VydPLi-bGfFri7xRJqrqmuiv6dLbOts-KHUy9mtvag9TO2UgHnKNwJOqw7M889y6U2JcT2k61mAKoMfjiULrJ-53Px4VQWVzAqT2JpMQ4MDiNyNzKJ5xhcBhIIwCDbUp3wWkkyqWo0ic-pQ7nfCxEscWage_Kg1I8D8wAR2LsT-oMokCBFd0FU3-pP_Dd9zBmvG3JJUU3O0X9_vNJkWLtuzpyd07epf408dxBVkfYnUeumCrScBlF2LoPmq4jX-DNoFP8Pdi8H0qUvYuwZuSWtW-am3SHoHrcpkS-EHFcy7RBaXmZs0aPreJVCiV24oe9PNNGst4JXwFe3vbpLKMc-3lOm53LcpwFNL9SqyZfRsT40bB0s1dKaL9Awd8IxoJnxJilNYzfN0HR1gZMLoqmLurfKixYEfLEjREKwCCYg0q88bQ-AJUuRig5LbBWib4Zzpr_HBZ9m2fiYyCLEBX1KQM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5706309767.mp4?token=awESIZvQBnCe2ib8-lRMZiHVL666Zp103Kez15a_V83GRoSr8Bt8DAQiczqQqAMEDigEMwz4D6R2m_rGQRSnAn8Owal0TBjm3zZFZPcss0U70GHaFczMsxvAMOgXRBdN-yBvp73XDfLYGPqk6GfGsoI3IJOvqocKtpvYC7HFD8MzB79uxeNN4silPkZ1QLsRzgFBd7xr8lhm0nNdBg6VydPLi-bGfFri7xRJqrqmuiv6dLbOts-KHUy9mtvag9TO2UgHnKNwJOqw7M889y6U2JcT2k61mAKoMfjiULrJ-53Px4VQWVzAqT2JpMQ4MDiNyNzKJ5xhcBhIIwCDbUp3wWkkyqWo0ic-pQ7nfCxEscWage_Kg1I8D8wAR2LsT-oMokCBFd0FU3-pP_Dd9zBmvG3JJUU3O0X9_vNJkWLtuzpyd07epf408dxBVkfYnUeumCrScBlF2LoPmq4jX-DNoFP8Pdi8H0qUvYuwZuSWtW-am3SHoHrcpkS-EHFcy7RBaXmZs0aPreJVCiV24oe9PNNGst4JXwFe3vbpLKMc-3lOm53LcpwFNL9SqyZfRsT40bB0s1dKaL9Awd8IxoJnxJilNYzfN0HR1gZMLoqmLurfKixYEfLEjREKwCCYg0q88bQ-AJUuRig5LbBWib4Zzpr_HBZ9m2fiYyCLEBX1KQM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
طارمی: آمریکا باید به این اصل که ورزش از سیاست جداست عمل کند
«مهدی طارمی»در گفتگو با الجزیره:
🔹
اتفاقاتی که در حمله آمریکا برای ایران افتاده خیلی بد بود و ما فقط می‌توانیم با بازی کردن دل مردم را شاد کنیم.
🔹
ما ایرانی‌ها آدم‌های صلح طلبی هستیم و دنیا درمورد ما اشتباه می‌کند. دیگر تیم‌ها در جام جهانی باید صلح طلبی را نشان دهند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655910" target="_blank">📅 22:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655909">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
عراقچی: اگر عقلانیت حاکم باشد، جنگ دوباره آغاز نخواهد شد
🔹
ما آمادگی ادامه جنگ را داریم؛ هم از نظر توان نظامی، هم انسجام ملی و هم اراده مقابله با تجاوز.
🔹
وضعیت نظامی ما حتی بهتر از قبل از جنگ است، چون توانسته‌ایم در زمان جنگ نیز تولیدات نظامی را ادامه دهیم…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655909" target="_blank">📅 22:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655908">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نماهنگ مست نجف</div>
  <div class="tg-doc-extra">علی اکبر حائری قرار مداحی /  @gharar_madahi</div>
</div>
<a href="https://t.me/akhbarefori/655908" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">✨
مست نجف
عاشق اینه بره پیوسته نجف
نمیشه از دست گدا خسته نجف
هر چی که بخواهی رو علی تو مضیفش داره
🎙
#علی_اکبر_حائری
#عید_غدیر
💚
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
مرجع رسمی مداحی
👇🏻
👇🏻
@gharar_madahi</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655908" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655907">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af37965d7.mp4?token=h2ur-Awvle93aWtQUFiVuQI5MlBfuRjGDJfuL3Hk5u5QFMMh5yV_nUvuKX63tNwVotqiOrX7fqGljn5IS_ZTG7hqtAxxV7mPhf-cYVLe8-1kAhIo73q8l6VWayfWeLLl0kM0u02U_zWD6D5JIV2OpaeHGt7k0MPl1EJTLzkVlAyBMFxiYQffx75HCh88cm3K9wLCWMbmJR4kRBCFawp8QX4qMI3uQEO-9lizQ6DVlOTK0oV1aYAwFG4BtyKeSASfQ7Xw5bBFvqKtP2pf2PuZrcPZCGLUfbH0YzRujLcHlA18B4S0wLKquAA5VfRu1eUbCMdzDoJFEuuWGR5tmIk2Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af37965d7.mp4?token=h2ur-Awvle93aWtQUFiVuQI5MlBfuRjGDJfuL3Hk5u5QFMMh5yV_nUvuKX63tNwVotqiOrX7fqGljn5IS_ZTG7hqtAxxV7mPhf-cYVLe8-1kAhIo73q8l6VWayfWeLLl0kM0u02U_zWD6D5JIV2OpaeHGt7k0MPl1EJTLzkVlAyBMFxiYQffx75HCh88cm3K9wLCWMbmJR4kRBCFawp8QX4qMI3uQEO-9lizQ6DVlOTK0oV1aYAwFG4BtyKeSASfQ7Xw5bBFvqKtP2pf2PuZrcPZCGLUfbH0YzRujLcHlA18B4S0wLKquAA5VfRu1eUbCMdzDoJFEuuWGR5tmIk2Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و در پی اقدامات تجاوزکارانه، نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی…</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/akhbarefori/655907" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655906">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oKlo-CtfMfJLxFdGoDVY8Lvjd8L42nyTrCIrtWNqpgc_PLAEy0OpM_3tUqq89jI4T4Kn6UcPYEuLrcI0jwYWzB8qygZsyIXzNGvsGXbwOXd9h5yEI2YPEPr0u_wKuBZBMSZW7wlwBanXfMqO_rOf03dHBEv9hrzIdUF5XrPa0fpuWYGs3O54xatHaFgmb-51ZBlO5nfvcZUnmGk0-u75ps7HgChtjkazNu3dMbDkarqFO9xNonds3r-5Rp4avsLbUaoFrBY4GvHYZh8DD6yuligId-uNlozYLZSfY1Y70Vu6AJ_CwpeVQxx3LLtRoxF3-7vNJllcQ5Z9RdNW9KxGUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هند به خاطر جنگ ایران ۱۲ میلیارد دلار طلا فروخت!
🔹
بانک مرکزی هند (RBI) از پس جنگ ایران، نزدیک به ۱۲ میلیارد دلار طلا فروخته است. هند در دورهٔ جنگ و شوک نفتی، از طلا به‌ عنوان منبع اضطراری تأمین نقدینگی دلاری استفاده کرده است.
🔹
طبق ارزیابی بلومبرگ اکونومیکس، بانک مرکزی هند در طول دو هفته منتهی به ۲ می، حدود ۱۲ میلیارد دلار طلا فروخته و شاید این عدد فراتر رفته است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655906" target="_blank">📅 22:47 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655905">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">♦️
عراقچی: لبنان در این جنگی که توسط آمریکا و اسرائیل به ما تحمیل شد هزینه داده است و ما هرگز مردم لبنان را فراموش نمی‌کنیم
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/akhbarefori/655905" target="_blank">📅 22:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655904">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6LGLoeQFocOlEpJKQGOwxhO_eHm5noT3mWHPWpWlGvqsWIH1yD-5prhMJZ3AF91uUcvMVansCF5B6kZSIhg1zrKvXvj0AT0bx9B8W3qDAI3N7sgT_J5-fKGTBTrLDqPlYeDx0gBAMVEOr7HqAPBW5hHYiG6sANae7Sqd-LMRIdazCT6dIexw8hm3PkYYFvGLXiCEqCyGJM4fy1ELvO62xbF-tks7DLnY0SiPq1NboaZLQJNlYVo66ajJY_NU2xwD2l3koU7839blcRrJvp-zlciJX8zibyEehtF646c9flhjP7hIlHwzXSoe7ihbtDkCexpgVS01APO9ohxU4fF8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سند زنانه غدیر، روایتی که از دستان فاطمه‌ها گذشت
🔹
روایت غدیر از کم‌نظیرترین روایات اسلامی است؛ زیرا در سندی از این روایت، تمام راویان آن زنانی از خاندان پیامبر(ص) هستند. بیشتر آنان «فاطمه» نام دارند و هر راوی، روایت را از عمه خود نقل کرده است.
🔹
اهمیت دیگر…</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/655904" target="_blank">📅 22:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655898">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KGs9n6GTGwcGn5JvoLVSdAfHwWKriSnbk6h2CNplFlVLBoumLuwMvN84yUKV-HAjCF1AmEMhj4eU3dPYCec5zV8x_ihokv7WS04NuokXCWSHOP3Nky0p4_KAJyUnrmNYGM9lQEq7fLeT2EdWau03s14GG42F6FOlBm1rKrwH0MKrVn8GcxY38YJg7f-3iMVFy_GX4YaUFkbHYmJL8OMnHjn4RA4raXIj0YZ6rLtJ7PiVsDGLy8PRCYhCSSrLCiGF4mjj_U1SzWujCFQi3hzX3WZNpbzdodii1IjHiVDCk1l5bQ9ORARlLSLX0B6suaBWZTjkUmbclLHuPnOnT8sssQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWaYb3jCJxceXEr1ACxACf3grP0W5eoxEUfkZ5HppxqzlKNfkz_K10H40buydCsdSSnnQWSGZYd7iofr6DhUpaSWBLFDxmZwZ_Ssbe722V97pwI9g4WvSE8l9UOU8jLrUzct6WxffMBiowwz6yFR9MRdVew8MTLN674_gCkXrtC5Tk_Trti0lmuDL1Mr7u48ZpPrTde5ebFkgI1IdqCdwdpxiRNtDKE3mS6ybFJakQb0MGhg5FvSuqJ47InVD-I-iKR2woHQ8TP_4yLLWdJz96_Xa_adBH9aHq7JnHd7LZwxgRZV23-edSHeZxDOGlClHxo6Pq44j847Jrjuch7YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pwF0exKinyBr6GIbvitek_lP4zTHaVqAZXry5SvfFYW6_YY74wdn1ivRBVcp5cSpPaFQPk_vQWF6ssx3EyTaEt7X1PQgkQbhkdrp_n0pJvZLRt7-G_QN_YksG73yFxPF0pUdLBKvnDYzRQLwdDR31AiLFWAqXEE9PrMoPGTvK-MHgXKjPSO2613ig1wDj6ykUFG_E9UkSZMS1VT3EMPAhvSDzab56UKvRIV_-ULpcm4gCp4SDJrurSSY8uS0oJvtaqzYSkTniGGeS8O7VkKwXQm3cfHEyPjqdjJXPkXoGRnWR_D6iaT-EBXi6ZUXOviKU6asLrGLXygjnOhIx7CB7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XJ7cwoz60kTHSfgM_76oW71MQh0PNIPbknw8xJXhA7l-j1bG1cUaoiGxoOk-_at9mysYv8DLIVGJDXSONN_r_JgOGZNr6uPuXaWEcnQ-3HKpl2TB7RX2ird0O5ZIGHfG_OhrbmcoUXZiEhbScEYfR_QKiBTRTcNvvjQkHtfi8LYitpArFD3iuKcuQIpwMQawMSeSoiXCk-jGT0fvVaFReLuPHu1PGPQlgOAsGHdHUmlVtnZwA8GMzIDD4qVmIF5SYUBmDXhg-LiO17n3FuNF4KZtPHrty4LHxRhVIlgYG05sujiTI5Bisy8n6ReWp1GTdo_HrfcOkqpzouGQehkaGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SWaYb3jCJxceXEr1ACxACf3grP0W5eoxEUfkZ5HppxqzlKNfkz_K10H40buydCsdSSnnQWSGZYd7iofr6DhUpaSWBLFDxmZwZ_Ssbe722V97pwI9g4WvSE8l9UOU8jLrUzct6WxffMBiowwz6yFR9MRdVew8MTLN674_gCkXrtC5Tk_Trti0lmuDL1Mr7u48ZpPrTde5ebFkgI1IdqCdwdpxiRNtDKE3mS6ybFJakQb0MGhg5FvSuqJ47InVD-I-iKR2woHQ8TP_4yLLWdJz96_Xa_adBH9aHq7JnHd7LZwxgRZV23-edSHeZxDOGlClHxo6Pq44j847Jrjuch7YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nMb1B3fuzRM_lMZL3P0bSqa1WaFN5dv4HJnmC0wwhbtH17hByvTMS4lLAjPttvUj46Pc9xbD_1fpZUzb0tDVQOEtgD3Lzd-KYgNDn_8gs7oMnyCiV5d9ZAdldRandWkAPpCt9_7CIFmvRYLwsbG-dV7cTI2CuMgE1Ue8Ejf_PZeEOb9VMIUrWH0CjQq2VPoGxTzOsRVBtB2N29yiZh1ZQBsqMDi22CHNPKLmQkw8mM1wvQFeVdL3T-BIEqu9NyqqmV0MEgRKnDeQOe35qKTzL5FKuoSxzPGsZCbX95nBiz64n50M64wzhWJkjvhTFIVbfniS8Z0Q08innUXOjQ2Nuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصاویری از  رعدوبرق مهیب در گیلان
#اخبار_گیلان
در فضای مجازی
👇
@akhbaregilan</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/655898" target="_blank">📅 22:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655897">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2LESkSH4OhlRdlefTzqY9hNBk7zYBEIOuzCDebzcTSPb9b0zowWDiZe7HrI5qUXnvXlDkx-xgQp3v2wf1YIElXvXWqjcCYyX9oihi5FCjFM8g2AvCqj1NZExQ_l60r2mhT0f_ttbFd-vYOCe41lqUxj6QcFirB0d3HIZFCXuuA9oUelkNcoXIqOqtB3vpHfau1KJVZz9oKqytXUU6i862fqXMcDfXEwVHuz-1TZ7gmIBaqpvaS2prcJi54rMKTGLwH60R74cSMiX4I3lJDh8nV7hfyUPoxZI5sUJsiqzpCX-pngU5IjwTzccE4WzUNnoSdS5LB3m6CsV3qbP2VvAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
از هواپیمای غسل تعمید داده شده تا کاروان‌ موتوری عظیم | روش‌های عجیب و غریب بدرقه تیم‌ها به جام جهانی | تصاویر
🔹
با نزدیک شدن به آغاز رقابت‌های جام جهانی ۲۰۲۶ در آمریکای شمالی، تیم‌های ملی تنها به فکر تمرین و مسابقه نیستند؛ بسیاری از آنها تلاش کرده‌اند ورود خود را به این تورنمنت بزرگ به رویدادی نمایشی و به‌یادماندنی تبدیل کنند. از کاروان‌های عظیم موتورسیکلت و خودرو گرفته تا مراسم سنتی، موسیقی زنده و استقبال‌های غیرمعمول، ورود برخی تیم‌ها بیشتر به جشن شباهت داشته تا یک سفر ورزشی ساده.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3220316</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/akhbarefori/655897" target="_blank">📅 22:36 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655896">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
نیروی دریایی ارتش، مرکز فرماندهی و کنترل شرارت‌های ارتش آمریکا علیه کشورمان را هدف قرار داد
🔹
ساعاتی قبل و در پی اقدامات تجاوزکارانه، نقض مقررات تنگه هرمز و شرارت علیه شناورهای تجاری ایرانی در دریای عمان از سوی ارتش تروریستی و متجاوز آمریکا، نیروی دریایی ارتش جمهوری اسلامی ایران، به محض کشف و شناسایی، "مرکز فرماندهی و کنترل" این شرارت، مستقر در یک فروند ناوشکن آمریکایی که قصد نزدیک شدن به آب‌های جمهوری اسلامی ایران در دریای عمان را داشت،  مورد هدف قرار داد.
🔹
نیروی دریایی ارتش، با تمام توان، دشمن جنایتکار و متجاوز آمریکایی_صهیونیستی را رصد کرده و انتقام خون پاک شهدای سرافراز ناوشکن دنا را به شدیدترین وجه، خواهد گرفت و با هرگونه شرارت، در کمترین زمان ممکن برخورد خواهد کرد/فارس
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655896" target="_blank">📅 22:32 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655895">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">♦️
مستند "هتل خانه"؛ چند دقیقه با خانواده‌هایی که همه زندگی‌شان در یک چشم برهم زدن دود شد!
🔹
اینجا همه مثل یه خونواده شدن...
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655895" target="_blank">📅 22:27 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655894">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
عراقچی: بازگشت به مذاکرات بر اساس تامین حقوق مردم ایران و پایان جنگ علیه ایران، لبنان و منطقه خواهد بود  عراقچی:
🔹
آمریکا خواسته هایی داشت که برآورده نشد و در نهایت مجبور شدند درخواست مذاکره کنند.
🔹
ما توانایی ادامه جنگ را در هر مقطع زمانی داریم و این بدان…</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655894" target="_blank">📅 22:23 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655893">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cksZk8CP2Hn-7T9goqLoFn5ppVy_XceaUwdjA-XZwadLk12b1-kg7BP_qNqQYLl8aaM9kgftYtYP_0JnM9HZSDkVweLk7t2xD9UlJZRo-rR2-eNF4TLpFlSSOX6erBq9h5NQ2MMNLOVKft5Mxe8PCiHYdf-kI8J2FSiH9a0VjhMAYkEMP0XRfjEVgvnayHS5rQamKEE_sBjW2SWPQAoz9IzycT8oSov1yuVp9OsSWAVUH2WPXBJb8tH4je0AU70zb55jQd3Wj1T53craWh0KIAsDFnFuzQMTn64lg0sraSvx5JM-fxjnLzYHjWE7sXlZdxCzSZnFcVam6_NxKgU-yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💫
فروش فوق العاده
💫
دنباله ویلا تو شمالی ؟
🔥
فقط با 2 میلیارد صاحب ویلا شوید
...
فروش ویژه ویلاهای
🏖
ساحلی
🏖
و
🏕
جنگلی
🏕
برای بازدید از ویلاهای شمال روی لینک زیر کلیک نمائید.
👇
👇
👇
☑️
https://t.me/joinchat/AAAAAD7AqpYevY1QwQAGqg</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655893" target="_blank">📅 22:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655891">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
عراقچی: دو روز پیش پیامی به آمریکایی ها مبنی بر لزوم توقف تجاوزات اسرائیل به بیروت فرستادیم  عراقچی:
🔹
تماس ما با آمریکایی ها قطع نشد اما پیشرفتی در مذاکرات حاصل نشد
🔹
ما و آمریکایی ها در حال بررسی متونی هستیم که رد و بدل شده است و در حال کار بر روی فرمول…</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/akhbarefori/655891" target="_blank">📅 22:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655890">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
عراقچی: در نهایت آمریکا پس از موضع‌گیری و فشار ایران، از حمله اسرائیل به بیروت جلوگیری کرد
🔹
نیروهای مسلح ما آماده ضربه زدن به اسرائیل در صورت حمله به بیروت هستند.
🔹
در حال حاضر هیچ روشی در مذاکره وجود ندارد، اما پیام هایی با آمریکایی ها رد و بدل می شود.…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/akhbarefori/655890" target="_blank">📅 22:09 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655884">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JgdTu-J-qBAJGhzOgFqZkazyKAlJegkW3LNPeQX_wmXXIXaQVpR9jPYtkNHUGHTedADUwxKNbmfJca5kdCAx043Ge2wDJIaCPMp-DzsPypI9ikF_FFxYxQqGwVm2D8AjfrlebeQh9Www7IKYY3SZEeF20KRtZ1YRhr6NsAkDK8WKg8l8PbgCUEVCnyMsjMQdEk7CCzlzgOPiokyo70Gkk0i9pICA9Xv8cjF-PV8FeMAVdH9K6Z1vWwNKyvPPu9Ki9i1qGOCfY7MzRtAHGT1-QaL9HvPz3qUKYBjBv0cNMfpLfpseHOoe8WAUL-_YDV-hygykSs2fYGukxhy8pzE1VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e_yRQAhaQs_XNMF6W3J4wMut1XC013YopyGfM9U0BfN6jl4MbTDWDwm_I2gXcQGEzouEPl3bH6M6EWY5Ykk22YwQXBMUAAuU2tCIK2xSExUPwGfF31fz7XPHY619F_Ju4-xCzIV3Vtmg6du_Z5O06NPRVYo3RnN8tROtGgLB5wg72J_IDqUeCMKGLVNCcstTtAwue6ndic5tdXZTvX4nxZkJjdXNp7gpx2nOqSDZ1VZHUzIOxZSI2Yh_WAe9HYxbwZzAfaFayd1rZvHIvSEHDV310ftN3aUd3SAJQIhAnWSRFL5X6bV9iFcM1LOGet10U-J9sLKQdUZqli2jfI-BXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tg2B2WYsGAzcwxLB_qHNKA5jtubOE37JOvXIvgFbki9rr23XI1Nl5FeF9M6Tg1UWp7Ffp-ajBbfZ2vSbkWQ-WLr10Rv6iREI4rYyniNxFAfvjp5eEU8t8oso7s-v46YY3Pm3tMGX71HVRKRkyy96MIEGyADeJ-UVKEv4AFC0wLuWye5cDqjbNfA0gX5VVJZAW2xY64DDYxGKT9-HPN3YB431GoNRql3G-wX4elFCCtsUNWHugauBzcIeSUf7BjXRUBSLbfpl6vMUHiIJ9ulhoeyBnnBIAyew36GudypaaDgBw4WJUJjV6OXydF_PD-YK4QFaUntfpY-QFgJImSShqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HbCWv6xCsfb2JOFT3UCv507JonkAG0b6PoFEFJzkhUdRDq6ddobJMBAPDuJXD9vxA2j-iX7xeluIn3lBN5nE1RslOMMcevMppCfsKsW_nav3SoiwREPYdQc59sTJ39v6yVOmVPD6YcX6F_UZCoilID8KCNT53ecngnxkdn9zncMI6K2cRDksyFYOr26bb3jyCVuBWlsLBLaz1wZcPuIV71PwmM6pg_ORtCdmsjnhHh3cpXxw-8hwEbBfFy8xwnj-5Q9jzBXUAg_vsnn1P7e5pEqYmn27FkPSLF8gXJ6cZNGvrSDslXzEHPYQy9L4UdRBwo3gSdZ76b504IQ-jJPm_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nDShKRK1qoV-ZCkvYqggOrtMODCaEC65BdFwAt1rLnAmyZAExod50Cd02u1hKjFMnwxBIb2Hczh-vEF2Putu7dkLuBlEJscwfikRcwuO-_6S77lzYIuErTApA8pVM77HCtH2hpgUj6fo_8FgjtK9cpkpu1heaDcH8lErv1DFSJfkR5bmVCqT6711V31zZxppisDK41McPYwZwXPrWIYkbeRXg2yAKYuobc5Swual55Hsqd2cWM7rsSk3O4XyAa4at92a50WqI5oKVCPleUiU81C5PWqVHhece1bJFLcnXDcxfYAbtvQo8X988iGKnF2Bt_2DAKcUQTyRgz4jtZJaWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S6AE7-IY1VnjEbKGUFyEKCjenxiKM5HwWwsnmh-jLoa6M0xwcZOV_lNF_Xzbfy0VhdV4aOLIS4T3HYnn-bdtxQ-ZGpYL2_ZZ31v2NrR9gsW8_pbEGgscgXFo39prbs5PyxI6lrTGFj4OmRKnVBI3B0uKvbAENza7PO3UWqmWoRYEMNtTG-OayGkYkxEiYNuG-P1PIu9SGztrR7h_JtbHXKeYakOzI1rIot_SdgmSc5jPCckBGHW9r3VUcYK0SqUgTXdu9H1hGbsOaUNSxZ80zh3PK-fJ1uxkXOA0KJIo9RLCuA_FG74Dj6WE19Zr68jRXsckBsnlr0PECnm8qE_ElA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۵ فکت تاریخی ایرانی درباره پاسداشت غدیر
@Tv_Fori</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655884" target="_blank">📅 22:08 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655883">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">♦️
عراقچی: در زمان حمله نیروهای رژیم صهیونیستی حومه جنوبی بیروت، موضع قاطعی اتخاذ کردیم و نیروهای مسلح آماده پاسخگویی شدند  عراقچی:
🔹
نقض آتش بس در بیروت تجاوز است و ما به همه طرف ها اعلام کرده ایم که اگر به بیروت حمله کنند، آن را تحمل نخواهیم کرد.
🔹
من به صراحت…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655883" target="_blank">📅 22:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655881">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ipReMPbLP7wXDKqeBdvHL2p10kbQ9hRChNkP6sVLsHwuan3SIrwNPfPsHWiKahXgz8sh3ua9lZ353o0Wsp6AKNPWynwoPg0lyuZkhtZ8VY1yMyKafW_Vfwoo9YvEuapxpVn6FL4Jis-gm6MNSFokKWJUoMubkUwkgreFMj6NBNZt_4rE6j0Vo0-VBVpAla_coE3DGAznWxvI4EpK8vLDp6aUG-Wjbkqx5jHzdcyW6HNyJYYsyklgtpiU_KJymbq9IW050RciyIj6TdbPwZoQspEHvmIMEoX6wLDAYQtE7uGMew9uuoCZAWQHd_KR6oAPoutbz4iDMkn1AY95v8Acpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهمانی کیلومتری غدیر در پاکستان
امسال مهمونی کیلومتری غدیر همزمان با ایران و مهمونی غدیر تهران در ۳۰ نقطه جهان برگزار می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655881" target="_blank">📅 22:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655878">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QKj7ogQfy0V-EtHxWKQG6suuEc5e4nPXlPJJ4EGvwWeE-JvXbyg1H7ARL9lbhKBZ8vCXEYquza7fB-sNIAamPqqmxjRi9nPNEMPwzA1mYPV5wp9608BeNB2aVIvXDbCkXJ0qOAWzkURp_bmUivG5s6GaewDpvN3hadt-iNyLlhOOxt-_TVx8JESasaC5eEBDnA1r8xTW5ywJXDer6K6YCHHi_LGEEu9cBJWJGVwsVDeSS97JLitR80p-nh0x9k064NM9uy4GjAv-iCtqZ70q5AIn6s_f_TzuHmUK9sm7vMjB6GtGXr2BisC2jWBNlgaERXzNINzmwNU5Isel1nyaYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ORGSXLQoBnxf9Kh3uQeXBd8HKwuI9MkaYzPvyovkZPCccnwmvp2ODpCgqwIx-8b_lWNsLQGFhGOy6NQXllx8RsMJmafDdJQnhhO0-2hybNVrgvYQp5XR_5LtjlbmsWY-XvWRxbtzyMKFzk23WVHuIJFWJWntIYvcERTM4ReJ4T1Tepfn9sZ5nX5jym4dxB5m37WniGbpv3qYMEVjWMPMuab9KaAjDd4ks7b8qad9xTkci6HYoLTusqTMRgRQBMiSXSOJW9teGcAo-f4NsCwPQ9ZEY4idGlKcWBje4yH3axUvxvHodvH7TTCe-CgaW2YhUVxSe270cjLQ7d8o_YTLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7JLeMhz3i_3H8kIW3owC3ZEzH23u-Tf710cA5OkG6qnCBEKbmYyWGx6Yg0lFohN0fh50sZirhqA_ObH0wxwPExu5hihGre0cPK8atYySJZn5sjadDQ32L--49XmlUI2V2-M7rDf3JQUSqcUfWD6H-StC5AoGevPRF-HQKqgQzw0b861CQkKxV0i_XiFpMyWAoSABlS62PYY51n3Nf1CJRAz6JOYHfJmWJIxqzKRwVQAF4bjXghUZ1zY3mAgon_-FH6-LF5f8ovJwpwXCztuJonbBDvAg6UrHqJtZaOfJjxcRtKLRSnsRW4CZZqLw6FWrBzZiYjPf9RtelmmxtgrhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
نظر رهبر شهید انقلاب در مورد جشن کیلومتری غدیر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655878" target="_blank">📅 22:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655877">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
یک چهارم کودکان ایرانی از تحصیل بازمانده‌اند
!
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
بیش از یک میلیون کودک دبستانی در سطح کشور از تحصیل بازمانده اند یعنی معادل یک‌چهارم آنها!
🔹
وقتی کسی در فرآیند آموزش قرار نگیرد، دچار پیچ هرز شیطانی توسعه نیافتگی می شود.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655877" target="_blank">📅 21:59 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655876">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
عراقچی: امروز در مذاکراتی هستیم که برای دستیابی به یک یادداشت تفاهم با آمریکا انجام می دهیم که اولین مورد آن پایان جنگ است  عراقچی:
🔹
یا جنگ در ایران و لبنان متوقف می‌شود یا متوقف نمی شود، نه در ایران و نه در لبنان.
🔹
آنچه جنگ را در دو روز گذشته متوقف کرد،…</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655876" target="_blank">📅 21:57 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655875">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
عراقچی: در آتش‌بس، از نخست‌وزیر پاکستان خواستم که عبارت «به‌ویژه لبنان» را در هنگام توقف جنگ در همه جبهه‌ها درج کند
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655875" target="_blank">📅 21:53 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655874">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W38iqVxQWT3B_usPksVTZStX82pVOTAf5oIt6R0RgC8L2jItCTIcWPF5ATnkFIxwcCpWFlgeiKsJXG6S7WkrBTkKOlR7U2L_Ez_QWe0C8ps_VhzVeM3WkNKHkiT9irWxLfeKv8ZL_EKLSI4Ozoqf5ZYzJfLrxDWqk9gvvQB0FiZG0R_fsx8YR81dk3HKjaK6qzbN8XKPCg4S6nZDiSjGiKL1Ne3wGTZA6Cm3bp90UFmrRVmtEv0dDWqzcqdCb-NwnMEkxQhURcfUyS66ay9iBIdrkzAAgfLKke_5veW9dKBxXPe6oe2eTe6DKRxbcBkyknmUi0a3L8apbri17pbtkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
تیک‌تاک جنگ را به نفع ایران برگرداند!
🔹
بنیاد دفاع از دموکراسی آمریکا مدعی شد که تیک‌تاک جنگ روایت را به ایران داد. یک تحقیق تازه نشان می‌دهد الگوریتم این اپ، محتوای حامی تهران را ۷ درصد تقویت و محتوای حامی واشنگتن را ۱۹ درصد خفه کرده است.
🔹
شانس تصادفی بودن این سوگیری فقط یک در ۶.۵ میلیون عنوان شده است. نتیجه این عملکرد تیک‌تاک این بوده که ۶۴ درصد جوانان آمریکا با جنگ علیه ایران مخالف‌اند./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655874" target="_blank">📅 21:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655869">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگرافیک قرار</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bGiMF7RINFUS36dVmttOYCNyXtOSTNWc6XCBSyahHzDjZc1KIYj4Vfv6Jiw4c5PFr8qCPzlNgCaIwgmneho8rZlFUGuJ_sveX-1YUPhhsRAqvyCbVWqYnLJH2pZD8GYkdIZaNmOKwUwLYquuZT6ondQnY2yw2qwdSklKeS67apve3UOLVdAKufPGB7zkIR7dXafaPk_Dv6iHpuYtAQKVbjcXq59kEBz_rYmjmyO_r7-HVXMpo7rGeRRTjELHKwcQ88vFai4a52JkayHRBVknQkJf85KPAIpVXiRblYikOaDvsF2hBzQcd1ELK6DV3SQ6XMnxLcv7VOqvAZZH__QSiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/t-CmeazLozrAi-rlcilMBC2O36hb5DICiaK3UCjN_qarbCktS1WxjiZBIhKL4AuZLeS_7-1yHDUYHuGTdVcSnFWD7mHHLuP2qnVNNBRvV_Zkv-99a5fumzJQnzZvzax-Tc8Hmo4YIJwRCqYgfzs7XiJDySYja9-E7c9ZbD6khvLh-XMuJeKuW0AOKzpe_qw-D5NAfkZqEDEmM4kJ87E_p_Z9FmexIJxiZKxp96_5pXRXn6LEAPfSEVg1B8jHvZy6MLPeFKEYtLxVu9E-clvuWiWAjftzS3kr81ug0Wpl3vUDKRlxhOOqul_98MJgcowGNCSoiiU2nHJsPju_NiIrfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KK9qtZmBkqi2WqKoKsu8W22o-oWC3nSDoIo0y9u-auewoziyY6-FcWoBTdqitEvqpdBAIyrIqe-KTR7iyf4gizcxIqHhRqU0nNqMetR1J3EJ7WSuI8QlTCGdauKiJba3J4N77uU6CytnRbpqoq9_p6tG9bPvBVFmmC8OHeBnZWyzHEdapWYf3qjnKLXGEGVP_z4WdLIRjFnU-uC6LXPRUw4igtlS7y5Jigbcy5Z9cdXYT9_s48jisqzi0JiN4yazdO51NiOChqUsd5c4Ip4XG8CWDxw7BsTlGA1MSaRQrsvu6AalIqUq3lAEwzPxczHg5fgT10KSZqMoE8Aog8g11w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UUuy49q00k-Cdd5yxQ8CB0FxUQKpYjDyD1heB-GdpL0X-0zoth1-7H8jmuTzSvrGiyDEySPopf1CyssO8ZzfCUprz8TJjj4YhdJ4ScE5UXARekQeXTCeIMssdTa29uEeJ3Xg88YEIhQ0asRFhwhj-Fq6OK9iBy_VmSnarDKaBgHGnXBzXIYI2EAVdaVlGxYSh65e_gpS4EoBlOJNDOwEuFTYsvoY6nss4MdS5Y0opghD7C0UiiNXJpfsD8BRoh049Qo0tKTGPXKX3LE1gLrzhzMBKXYDZwG4oKmGNhu8sd9dgEzQ1pb22WdXkBnCCVw14LIFEjHwq0WMK7HhlD2DhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M0EFLliMIypV_9Krj8O6NnCjE5JEQmhP-BXg8sUcyA4NNN0oFtJj8p3UIEdV5OV4ublzUrOmOBhCZ3fy7kwbp2QMNSFmsjLnrKmbu9av8kI1ixBufdX63li6vd_caOjydYSRylzJqrDxjLNr9al5ilCIoVvZWan4j7qypbT-qA8UBi2j2_7jSupxk4Gt6FWQdIZyrx6QzTX1dEQR29NQImn_0CG_tNrBDdNxraY1KaI85bDbRM6aHgTskWeiU3xUy8AxOx54lHMoCl_8uv7lytyvZxQRGLJyQ8bmew9XWIudjgRMHqP1WRi9jnTkbqvnlW_VLfq0UcEnwBA4oiB6Pw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✨
علی مع الحق و الحق مع العلی
#عید_غدیر
💚
#بک_گراند
#پس_زمینه
#پروفایل
#امام_علی
@gerafic_gharar</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/akhbarefori/655869" target="_blank">📅 21:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655868">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
عراقچی: ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است  وزیر امور خارجه کشورمان:
🔹
لبنان را کشوری برادر و دوست می‌دانیم.
🔹
ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است.
🔹
ما دیدگاه‌ها و ملاحظاتی داشتیم که آن‌ها را بیان کردیم و حزب‌الله…</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/akhbarefori/655868" target="_blank">📅 21:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655867">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXKLCrWiRWTBHc9iGaHuYkJ9-r79LqatxhDA6QVgBK7s9Ean7-u0ipzD4542friwBTLW7Gh3EF0UF4iU4BW_2TNnGWLCTwesy0EE-5jMjbmZ4YkQc9acKrUioFsdtsqzeXIe4xjoGWZx-y7b6fPF6tqdvPFnANvbeF73QgTfb9NFjZlb_cP06-qs3izqLRlKC8UpDbKkl2IfAPkB4AEduFK2bKfHfYYuFzFWkMd49kFP2PW-jbC2QAG2SYTgRxhd4doRmFKiPqpJRzZtADydkbdTBbYOrYCBYIGwitWwZAlQ3FPyskAnUI7jXo99w-sr7e7LHUfjRlTD88ryyV6r0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آخرین سفر پیامبر(ص)
🔹
سال دهم هجری قمری... پیامبر اسلام(ص) همراه هزاران مسلمان برای انجام آخرین حج خود راهی مکه شدند. سفری که بعدها «حجةالوداع» نام گرفت.
🔹
مناسک حج به پایان رسید و کاروان‌های مسلمانان راه بازگشت را در پیش گرفتند. هیچ‌کس نمی‌دانست در مسیر…</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/akhbarefori/655867" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655866">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
عراقچی: ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است
وزیر امور خارجه کشورمان:
🔹
لبنان را کشوری برادر و دوست می‌دانیم.
🔹
ایران هرگز به دنبال مداخله در سیاست داخلی لبنان نبوده است.
🔹
ما دیدگاه‌ها و ملاحظاتی داشتیم که آن‌ها را بیان کردیم و حزب‌الله بخش مهمی از ساختار سیاسی لبنان است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/akhbarefori/655866" target="_blank">📅 21:48 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655865">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
۲۰ میلیون نفر در ایران خانه ندارند
حبیب قاسمی، عضو کمیسیون عمران مجلس در
#گفتگو
با خبرفوری:
🔹
سال گذشته طبق مصوبه شورای عالی مسکن میزان افزایش اجاره‌خانه‌ها ۲۵ درصد بود، طبق مکاتبات شورای عالی امنیت ملی و وزارت راه امسال هم همان افزایش ۲۵ درصدی احتمالا تمدید شود.
🔹
وام‌های ودیعه مسکن از ۶۵۰ میلیون به ۸۵۰ میلیون تومان افزایش پیدا کرد اما درخواست کمیسیون عمران یک میلیارد و دویست میلیون بود.
🔹
سالانه ۵۰۰ - ۶۰۰ هزار زوج جوان به صف وام ودیعه مسکن اضافه می‌شوند اما این میزان افزایش مسکن وجود ندارد و در حال حاضر ۲۰ میلیون نفر فاقد مسکن هستند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655865" target="_blank">📅 21:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655864">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nejLEy3DzOFrZ2o65Yz2iKQawiZY9JOdEqJIoglk-7hKVIb7dhwqkeHfqdaDG4TPhIxgFB3wirMv9SjrCpqvO3U4UzHJGFS5lFdqiqLytEMAXEt6CUK4TR0Pte-jVrhKlSeYXEXpAI2fQ8dtDh4Oq6q3OEEwbV1C5LrMapBEJE-7vnPdYTaWAfxXdPQmeQHjnQa3Ccc2hgr1xtBrjdLpiArKJgrucJczubbV6coBm6PruGB2Q1w2AnFWrMN974pS44ZK4nhGqCMRzwTjOte2A07tJO62EQ3XyXSy9mt3RrQ8I1jTQrLx589X2LOPEP0bi2dfPcs8zj1j5aeK4bhB_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجاهد شهید
‌
🔹
تصویری ویژه از رهبر معظم انقلاب در کنار امام شهید؛ انتشار برای اولین بار به مناسبت عید سعید غدیر
🔹
حضرت آیت‌الله سیدمجتبی خامنه‌ای:«قائد شهید ما، مجاهدی خستگی‌ناپذیر و چون کوه استوار و محکم، و از عمق جان، مؤمن به وعده‌های الهی بودند.» ۲۰/فروردین/۱۴۰۵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655864" target="_blank">📅 21:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655863">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd1efc5a8b.mp4?token=nsjvmmgieevmWX4EHafigy1Wc780XVAwa0CYxeXvSxbWhkQQ7KS4rlnsxXzt6_ywpzNQ8w9sN2zl7LWYVhevLCNSsg3gJ8pyoTKB6SHglCaXp_f6zApbLrJY8qMWfC1G1fmgl-taEWhIswJzJeVyy9eHGc-5js409Vg_baJTuljADQueK710jial-X6owXc2USwcBqdMyHoFRo5Lmv0xu2hBDm6P_QdyivxR8GR5THB-dl3O529rlNXqh62hXfOUIJ9h1udRip3qChgKU0qpYUsnlYAk5kxZw1nB_Vzvm82Qo9GbCKL3f_870VtKooCJ5yV5C-wJUWxFlw0lE1vilg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd1efc5a8b.mp4?token=nsjvmmgieevmWX4EHafigy1Wc780XVAwa0CYxeXvSxbWhkQQ7KS4rlnsxXzt6_ywpzNQ8w9sN2zl7LWYVhevLCNSsg3gJ8pyoTKB6SHglCaXp_f6zApbLrJY8qMWfC1G1fmgl-taEWhIswJzJeVyy9eHGc-5js409Vg_baJTuljADQueK710jial-X6owXc2USwcBqdMyHoFRo5Lmv0xu2hBDm6P_QdyivxR8GR5THB-dl3O529rlNXqh62hXfOUIJ9h1udRip3qChgKU0qpYUsnlYAk5kxZw1nB_Vzvm82Qo9GbCKL3f_870VtKooCJ5yV5C-wJUWxFlw0lE1vilg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تنش و جنجال در کنگره؛ رفتار خارج از عرف روبیو نمایندگان را به واکنش واداشت
🔹
جلسه استماع مارکو روبیو، وزیر امور خارجه دولت تروریستی آمریکا، با رفتارها و اظهارات جنجالی وی به حاشیه کشیده شد و خشم نمایندگان دموکرات را برانگیخت
🔹
یکی از نمایندگان زن دموکرات…</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/akhbarefori/655863" target="_blank">📅 21:28 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655862">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">♦️
ادعای زیاده‌خواهانه ترامپ: هیچ توجیهی برای غنی‌سازی اورانیوم ۶۰ درصدی توسط ایران وجود ندارد
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/akhbarefori/655862" target="_blank">📅 21:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655861">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
ماجرای
ناامیدی از زندگی و جداشدن روح از جسم توسط موجودی وحشتناک
🔹
00:06:00 شرایط سخت زندگی با پدرم
🔹
00:13:15 تاکید روح برادرم به سختی شب اول قبر
🔹
00:19:00 حضور موجودی وحشتناک در اتاق هم زمان با درخواست مرگم از خداوند
🔹
00:27:40  توصیف لحظه سخت جدا شدن روح از جسم
🔹
00:47:10 احساس نزدیکی به خداوند و درک عمیق از مهربانیش
🔹
00:51:20  میوه‌های دزدی شده که هنگام خوردن تبدیل به گلوله‌های آتش می‌شد
🔹
00:54:00 نشاط عمیق از اعمال دنیوی مربوط به اهل بیت و شرمندگی از قضای نماز صبح
🔹
01:09:00 تغییرات تجربه گر بعد از تجربه
🔹
قسمت ششم، (از پا فتاده)، فصل چهارم
🔹
#تجربه‌گر
: محمدعلی درودی
#زندگی_پس_از_زندگی
#فصل_چهارم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/655861" target="_blank">📅 21:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655860">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
گفت و گو تاج درباره تیم ملی فوتبال ایران
تاج:
🔹
به دنبال آن هستیم تا به کمک یک اسپانسر، برخی از افراد رسانه‌ای را راهی مکزیک کنیم
🔹
تعدادی آشپز، فیزیوتراپ و ... نیز هستند که برای آن‌ها هم با فیفا در حال مذاکره هستیم
🔹
فیفا درباره ویزای آمریکا به ما امیدواری داده که به عهده آن‌ها بگذاریم و حل می‌کنند
🔹
سعی می‌کنیم با هواپیما به لس‌آنجلس برویم، نه زمینی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655860" target="_blank">📅 21:14 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655859">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hbdxriFLDXz3y9zmpy5-YsIFQnb20Ww7E29ryW_BQ7eWfbwRxcnEwdywmzBelpVXgwOvHfCctoDhTk5KuvZmwdVuDQUa4qV2PdS-Y0nfBHxOLBojNzYbseWEAUY2jCb5pmKYZhNroel2t78y5DWrn2znyg6lBXqWO-EepndB48i-HpLhnWvox28RdaBzJMy9i7rxI3MvgVEtRa9DfypvsLIHWQ4m9muX0hhUpl0YC605NwyXTPVSl1_65Y-MQV4fHXr8cN2-_uX20Dfhad0GCm4ZVsbKTw3If207tT7UhmrQsHz5FKhwHJuYy0IUyeOUQXdnjGanTot8CtQxirVlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌱
در پناه ِ غدیر، در کنار یکدیگر هستیم
🔹
در یازدهمین جشنواره مردمی اطعام عید غدیر همراه ما باشید...
🔸
با اجرای: مژده لواسانی و امیر مهدی باقری
🔸
با کلام: حجت الاسلام برمایی
🔸
با حضور: حسین حقیقی
🔸
با نوای: کربلایی علی اکبر حائری
✨
وعده ما: ۱۴ خردادماه از ساعت ۱۹ هم‌زمان با شام عید سعید غدیر در خیابان فدائیان اسلام(بین چهارراه نخرسی و چمن)</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/655859" target="_blank">📅 21:13 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655858">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a122f61aae.mp4?token=koBbqruulOZMatWnV671CKHTOtM8RpbzkJY48sNyGd6ymZx7Cya6UVIiyeNv8wVrSzmoI_PnfrpsDS_1CljuzE-eA5JnVB5-fwophLZ1Rw3MjcI1NTzImE2jJpbQWtDe9rveZbPZMkVSCNeAITZ_ClBXXf0h07QfYE2tMWBjqBSSK2zAqz0KR77a6-R6d0x8RC1QfD1NF16oZRZS8SpLW79CbvHEYE1E9ABLaNJ-sVHc1orLjFnPi8Qti9raCQVnq-iEdWHkQ8GzbjHDso3x8dq_pnicV72OZGrR7K_cs8IgkJo864ycwVpsW39LQecF5xlavUvKMfLf3Sq5Y3KCJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a122f61aae.mp4?token=koBbqruulOZMatWnV671CKHTOtM8RpbzkJY48sNyGd6ymZx7Cya6UVIiyeNv8wVrSzmoI_PnfrpsDS_1CljuzE-eA5JnVB5-fwophLZ1Rw3MjcI1NTzImE2jJpbQWtDe9rveZbPZMkVSCNeAITZ_ClBXXf0h07QfYE2tMWBjqBSSK2zAqz0KR77a6-R6d0x8RC1QfD1NF16oZRZS8SpLW79CbvHEYE1E9ABLaNJ-sVHc1orLjFnPi8Qti9raCQVnq-iEdWHkQ8GzbjHDso3x8dq_pnicV72OZGrR7K_cs8IgkJo864ycwVpsW39LQecF5xlavUvKMfLf3Sq5Y3KCJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مارکو روبیو: خود ترامپ در جلسه بعدی ناتو در ترکیه حضور خواهد داشت
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/655858" target="_blank">📅 21:11 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655857">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S-0evk09w29943GnxzXw5RAUlxk2A-h4Q2D2jEdGjqcNGUTYZ04yItbHkpzLREhN5G-mpsULjskYqfOHJfknHuERWVHAI-BK7BmqIgpgxkqA3GAHDjp8psTExWfoBGBD3wpnvR4ILh4HD4A5FDVUaGg4ht38vLEgVsb38663n9IaFqR0eFJzdYfRiokyuop7jRCfFHgi8Cx1ZCWjNxX7_lw8cxc2LX0TLVwlyuJei8Y53Dv0cCTe6WX8j00EBPqHviVz4x73kjDHg92_K7tYwek-bOrhvoV5k63uP6g7bxTKDyQg5RNyP4PunaFw9p7OpJc8e1XRHd7th34v_0jpPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این دیپلماسی شکننده در نهایت به جنگ ختم می‌شود
🔹
روند دیپلماسی میان ایران و آمریکا زیر فشار حملات نظامی، کارشکنی اسرائیل و ...، سبب بی‌اعتمادی میان دوطرف شده است.
🔹
برخی
توافق محدود
را برای پایان فوری جنگ کافی می‌دانند، اما گروهی دیگر معتقدند بدون توافقی کامل، جنگ فقط عقب می‌افتد.
گزارش خبرفوری را اینجا بخوانید
👇
khabarfoori.com/fa/tiny/news-3219943</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655857" target="_blank">📅 21:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655856">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49592cc00b.mp4?token=UVGk5JAykr8tuJyrg4_xaDa0EuTCXbiDNPHfCNe2vGQGhX65pe1TED42fMADjawh_RRhG6rmGee9DYWwhZdxDXywChHFLAki_Uwqr7woO0EbKceIOhC2UdCnUtiqkGbIVsHdwGMdyAyuofq62ml5N-aV3GWoy1jFxVKeTerp0bTldAKQ6uFbMuAJoMTtU8SYvDXd2w-CiT5bJdJHp03pKcSvJdLhSvmhQLEF08Ex2A6FOJpQJW8JN6hE4oTthGYkyZT6k_JD98lftjZuqubaZYVwgJ5ljYiQLU5BmcsE4yMifIEd6RdN3fZO33gJfG6tBZ4M8w-MLRL6evkhSru09w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49592cc00b.mp4?token=UVGk5JAykr8tuJyrg4_xaDa0EuTCXbiDNPHfCNe2vGQGhX65pe1TED42fMADjawh_RRhG6rmGee9DYWwhZdxDXywChHFLAki_Uwqr7woO0EbKceIOhC2UdCnUtiqkGbIVsHdwGMdyAyuofq62ml5N-aV3GWoy1jFxVKeTerp0bTldAKQ6uFbMuAJoMTtU8SYvDXd2w-CiT5bJdJHp03pKcSvJdLhSvmhQLEF08Ex2A6FOJpQJW8JN6hE4oTthGYkyZT6k_JD98lftjZuqubaZYVwgJ5ljYiQLU5BmcsE4yMifIEd6RdN3fZO33gJfG6tBZ4M8w-MLRL6evkhSru09w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تقابل فعالان حقوق بشر با روبیو: دستان تو به خون ایرانی‌ها آغشته است
🔹
فعالان حقوق بشر پیش از حضور وزیر خارجه آمریکا مارکو روبیو در کنگره آمریکا، او را «جنایتکار جنگی» خطاب کردند.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655856" target="_blank">📅 21:05 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655855">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PyMj63p3dd_KpJkBrpNmbZVglImFYL26KWTBd21EILobWeNKxHN8XDgGVQxNhAKdDE74Sk60s-L68GLI9Hul31iFJhoJNnABrSAWbvfo_L_6Ml-AzYuOKIuw9uNgw4rotTcC5dSExotxFA25428-T66bg2iovkZO1tN0patKOme6clYVRS_N7KxLdf9puwwsqH_51WtzkzQEtP5ienYp5lpN9cG16Sc5jEMZ3SMRdNjiwavXj2OIr8vpgpGy_hkAYtmyaYThu1YYkedQrYsdonCxJxMhVcTSSN1mqWEjtqOff37GoHUAwfHVkbHnJ1nUY4BxN5JYc15Ifqy4_59t3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازداشت مدیر یک شرکت ایرانی حوزه فناوری در آمریکا
🔹
وزارت دادگستری آمریکا خبر داد که مدیرعامل شرکت ایران تک به اتهام تأمین تجهیزات آمریکایی برای تأسیسات هسته‌ای و نظامی ایران دستگیر شد.
🔹
جمشید قمی، ۶۳ ساله، اهل ساحل نیوپرت، به توطئه برای نقض قانون اختیارات اقتصادی اضطراری بین‌المللی متهم شده است./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/akhbarefori/655855" target="_blank">📅 21:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655854">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
روسیه تهدید به حمله اتمی کرد
معاون وزیر خارجه روسیه:
🔹
روسیه در صورت تعرض به تمامیت ارضی خود، در بدترین سناریوها می‌تواند با استفاده از ابزارهای هسته‌ای به متجاوز پاسخ دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/akhbarefori/655854" target="_blank">📅 21:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655853">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
نیروگاه اتمی بوشهر به رکورد جدید تولید برق رسید
رئیس سازمان انرژی اتمی:
🔹
همزمان با عید سعید غدیر، نیروگاه اتمی بوشهر به رکورد تولید ۸۰ میلیارد کیلووات‌ساعت برق دست یافت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/akhbarefori/655853" target="_blank">📅 21:01 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655852">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VpheZA4sz5lDGzPyb2tnNIjUlAhgZuKSgh9_ImexX5JARVozLWA3eQ5O4QlmPlwvGKqhqxlky24UbexLesuX_5f3nQmVio_q-weskZt8kyBnnAdsTdLrV3yw2eJrhdEuh52VETh-Lgt6LfZK0Aijsxgw7y39n0W72NXycfRo4IcyT-FKoyNiNsAjL24kQLAnN9VSq6LVg6wr7aPqPrt6sVqLphoaOyOoDBsOzsreFojt9RbL2tweHxYe0u6K4dz9m-bwGGwBmPuTTWXgS5EKtMlOOixun3Hc9MvOiqrQmdYKae0FUxjVGTVQGISM0ajzjsU1628ybpf6nDoIRF6vEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آغاز عرضه مستقیم محصولات کیا (خرداد 1405)
شرکت کوشا خودرو از آغاز قریب‌الوقوع مرحله جدید عرضه مستقیم محصولات خود خبر داد.
این شرکت در سال‌های اخیر با تمرکز بر ایجاد ساختاری منسجم در حوزه فروش و خدمات پس از فروش، تلاش کرده است فرآیندی شفاف، منظم و مشتری‌محور را در عرضه محصولات کیا در بازار ایران دنبال کند.
بر اساس اعلام این شرکت، با توجه به استقبال بازار و تقاضای موجود، مرحله جدید عرضه مستقیم محصولات کوشا خودرو به‌زودی آغاز خواهد شد و جزئیات مربوط به شرایط فروش از طریق مبادی رسمی اطلاع‌رسانی می‌شود.
www.kooshakhodro.com
02149970000
کوشا خودرو
فروش و خدمات پس از فروش کیا در ایران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/akhbarefori/655852" target="_blank">📅 21:00 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655851">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5c24bf4b9.mp4?token=DjtwDrEVWjxIj0IDclSE-3KfTjZm8HD9ayde1FuxAhGFmKJ3445XMphGv20Ow_1ed1Zk5X8t1aDLQ_AqNAFmLy430B2IaveeHeUzTNFBxAU601aa0YZHc6Q1ZsFanalGvX00l8se1OwtuHjAvgoJGGMVNK3eKACfXw_70wfqdKS9U_hBQiDofGDOKzyBrPrRjFitrm6YXNnsNgVqbLZNfQ9k9dxyQmAuUqmNvynvsHEKr8Q3nTDtFx6jhJ8W5mQW9GJm2qdJy6TvMj_ABp7L2g3IOpNoiKXbJx22ikjnbjdLKbaJBYzZH_XI7Xm_wT2yQRVPacfDKfV_4E5bd3fdtw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5c24bf4b9.mp4?token=DjtwDrEVWjxIj0IDclSE-3KfTjZm8HD9ayde1FuxAhGFmKJ3445XMphGv20Ow_1ed1Zk5X8t1aDLQ_AqNAFmLy430B2IaveeHeUzTNFBxAU601aa0YZHc6Q1ZsFanalGvX00l8se1OwtuHjAvgoJGGMVNK3eKACfXw_70wfqdKS9U_hBQiDofGDOKzyBrPrRjFitrm6YXNnsNgVqbLZNfQ9k9dxyQmAuUqmNvynvsHEKr8Q3nTDtFx6jhJ8W5mQW9GJm2qdJy6TvMj_ABp7L2g3IOpNoiKXbJx22ikjnbjdLKbaJBYzZH_XI7Xm_wT2yQRVPacfDKfV_4E5bd3fdtw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ادعای روبیو:  گفتگوها با ایران درباره غنی‌سازی اورانیوم و بحث ذخایر است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/akhbarefori/655851" target="_blank">📅 20:58 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655850">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبانک توسعه صادرات ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcWAFNgau6wqTGQGu9TJ7iO0vTgnPsL0dZV0F1SYpmGkj0Djfw3VLuIIflS25FrHqWRjy8r540SRWrBhIkEBdybgq949llAfs9P61FPNMduWym7JfbXVIMHD2Z1dfHzKxzOLj4FSJFXkU5WALgTF3f-qK3SeuN8oqUqCHgsVyFj3pBjib6xPrgFI3GLlOmVHQSUYeCutSwBxkBmWeoUlHvMnPLuXQuH6zF6oQ81vRlQl9Cfx2OucDXNMP1P8zcB3ckcdv_alvkuM1dsXT5o4T3m8AaaZl_TnUIkRhyIdO6gy3EzH_G-hM3199yKjcSse0GCSrV1Vgl5dvgJhJiWaFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
افزایش نسبت ضریب تامین مالی در طرح غدیر بانک توسعه صادرات ایران
🟢
بانک توسعه صادرات ایران همزمان با دهه امامت و ولایت و در آستانه عید سعید غدیر با اجرای طرح غدیر، نسبت ضریب تامین مالی انواع تسهیلات برای مشتریان خود را تا 33 درصد افزایش داد.
مشروح‌خبر
🏦
@edbi_bank
🏦
www.edbi.ir</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/655850" target="_blank">📅 20:56 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655849">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
علت ترس آمریکا از ادامه جنگ با ایران؛ سقوط دلار در راه است
🔹
واشنگتن نگران جنگ با ایران نیست، نگران چیزی بزرگتر است؛ پایان هژمونی ارزی‌اش. اینجا نقطه آغاز پایان یک امپراتوری ارزی است.
🔹
راز ترس واشنگتن از جنگ ایران در این ویدئو فاش می‌شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/akhbarefori/655849" target="_blank">📅 20:54 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655848">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
وزارت نیرو شایعات خاموشی‌های برنامه‌ریزی‌شده را تکذیب کرد
🔹
هرگونه تصمیم درباره خاموشی‌های احتمالی صرفاً از طریق مراجع رسمی اطلاع‌رسانی می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/akhbarefori/655848" target="_blank">📅 20:52 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655847">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">♦️
فیلم چرت زدن ترامپ،مارکو روبیو را رسوا کرد
🔹
مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا در جلسه استماع سنا مدعی شد: هرگز ندیده‌ام  ترامپ به خواب برود.
🔹
اندکی بعد تد لیئو، نماینده دموکرات: من به شما فیلم کوتاه نشان خواهم داد که اثبات می‌کند دقیقاً به…</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/655847" target="_blank">📅 20:50 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655846">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromهیئت قرار</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MHUdu1_r6M4d0gegNG-0yWmQA917FFTuIuH-kMLT9wflDehfIEVdG3ldtbuEl7W7yZuG9wGGK1KowiDtVsDCOwoBiXND2-qYz5Mea-TEIgSXtij_Dya3YUQRf9ixrybWcJ_GmLmGrvaVsIdl1qu0D5u88SnS-Y8zZTqUmOZj6n5HGmamhY7OIsCn6EJMJUkiXN8N8n0sCTFAxyzJi7a35pxp8XxPPt12xasHj42GEI2aaVwIWGH75AcOyYLviZAL5fRy492su4g-0LXVIkX5WqjYVjrMIp3i6LBDsKB-zV26krHBMBRcGteX7HWICU3pvrVIm4BdVvfvj658OrfjTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✨
اعمال روز عید غدیر
#عید_غدیر
💚
مداحی های جدید غدیری رو اینجا ببینید
👇🏻
👇🏻
@Heyate_gharar
@Heyate_gharar</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655846" target="_blank">📅 20:44 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655844">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
ادعای ترامپ: رابطه من با نتانیاهو عالی است و در مورد مسئله لبنان بین ما توافق وجود دارد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/akhbarefori/655844" target="_blank">📅 20:43 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655843">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fcfa0d3b0.mp4?token=R1gqWEiwKtwUmQO-bN2B3TClcvdBjiLuX4cb-F8XVrGi-RkEfIOkDMvP7AtWjAK-qH9ddGkNgfOULtA6NqaFfb88SBG5q39DPe2rIb45FI2gtscfhbiB2lhZT5wg7GihSNdmSoCF_KNgcxPmbhsSfIX09OrK-BioO-X1YUlF8nvSNAcca-vC-B9EL1G_sYnacuwXfqGseuN4H7A-68GnSZ3vlD3sOuYzk2emJaiCdPOcaJkaOBxVaBhLCLWtgzQfkZLpV_2FOEU6nC3rJP6SouIZj04TekaOQp3MVsVo9Wxmj21bu7M8s5ADwKGehKdHcS9bOqllTZRaG_dPjnuE9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fcfa0d3b0.mp4?token=R1gqWEiwKtwUmQO-bN2B3TClcvdBjiLuX4cb-F8XVrGi-RkEfIOkDMvP7AtWjAK-qH9ddGkNgfOULtA6NqaFfb88SBG5q39DPe2rIb45FI2gtscfhbiB2lhZT5wg7GihSNdmSoCF_KNgcxPmbhsSfIX09OrK-BioO-X1YUlF8nvSNAcca-vC-B9EL1G_sYnacuwXfqGseuN4H7A-68GnSZ3vlD3sOuYzk2emJaiCdPOcaJkaOBxVaBhLCLWtgzQfkZLpV_2FOEU6nC3rJP6SouIZj04TekaOQp3MVsVo9Wxmj21bu7M8s5ADwKGehKdHcS9bOqllTZRaG_dPjnuE9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغلطه نتانیاهو کودک کش برای توجیه وضعیت تنگه هرمز
🔹
نخست‌وزیر رژیم صهیونیستی در مصاحبه‌ای امروز چهارشنبه به جای پیشنهاد دادن راهی برای حل و فصل بحران تنگه هرمز در نتیجه جنگ‌افروزی علیه ایران مدعی شده که مسئله به گونه‌ای دیگر حل خواهد شد.
🔹
او در این مصاحبه…</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/akhbarefori/655843" target="_blank">📅 20:41 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655842">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4b912394c9.mp4?token=vLfikQz-PIzLAcPDUILhhJ439xlzY2tKizuP3EcobtdZt95NwMzbKTdQ-qI09M05EcQcM07DYn61K-daMaFu1YnxZX9cJ4s30dsf6sZ5zJG5nLgqW_Leka4kzwI2syhr1r0M1NAap704ZrVD4TBlynhunFGXpTdfxj6MPFssvE-p9JmcqLD8rXe1KkaqaETaYj-IqndDz5i-99PXiPBOuVTfhQN3sKrInb4-9rbua6prXoUKfxjcAWelGY34qYR4qwhM0-v7f-qf_E3cpE95leNcuB2v45985qE1IJuTUXU51WtFPh5LSVw5wy2q_WckNpF7jsBciYVq2RwxzY212Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4b912394c9.mp4?token=vLfikQz-PIzLAcPDUILhhJ439xlzY2tKizuP3EcobtdZt95NwMzbKTdQ-qI09M05EcQcM07DYn61K-daMaFu1YnxZX9cJ4s30dsf6sZ5zJG5nLgqW_Leka4kzwI2syhr1r0M1NAap704ZrVD4TBlynhunFGXpTdfxj6MPFssvE-p9JmcqLD8rXe1KkaqaETaYj-IqndDz5i-99PXiPBOuVTfhQN3sKrInb4-9rbua6prXoUKfxjcAWelGY34qYR4qwhM0-v7f-qf_E3cpE95leNcuB2v45985qE1IJuTUXU51WtFPh5LSVw5wy2q_WckNpF7jsBciYVq2RwxzY212Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مغلطه نتانیاهو کودک کش برای توجیه وضعیت تنگه هرمز
🔹
نخست‌وزیر رژیم صهیونیستی در مصاحبه‌ای امروز چهارشنبه به جای پیشنهاد دادن راهی برای حل و فصل بحران تنگه هرمز در نتیجه جنگ‌افروزی علیه ایران مدعی شده که مسئله به گونه‌ای دیگر حل خواهد شد.
🔹
او در این مصاحبه مدعی شده که کشورها در آینده به جای عبور دادن نفت خودشان از مسیر خلیج فارس راه‌هایی جایگزین پیدا خواهند کرد.
#Demon
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/akhbarefori/655842" target="_blank">📅 20:38 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655841">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kY2AhOlct7Kt32doBOQ-SOepNseZINZ-MLKP-Cq6SrLWugdE0HtfXuq-DV7zjzomXVfZ-oflOqYjXWPn9dDcuAVueb48i1lzKaH56UZakB7agYSO2jxC3SBq5ec-WWnXYiwGjD5mwtKvWRZDKxcxqdMwI8JOxtiM7RQg6973fohgTQzdPEzbnH_uI67AeM3gpeNChwm2XHi6shZTYj3GMUErXf9Q51IoWG-HisklVkAckcs-pja5KjsJqbucKvg-b8mDtFQxlEAZhWO68Q3KPGyZxE9oEtF8cBDRCsnNpSVmTxYdgL3oQ-MaJ21FvxQkP50ObgJbsbREAgebtmKYng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نامه ۵۳ نهج‌البلاغه؛ منشور عدالت و مردم‌داری
🔹
این نامه، مجموعه‌ای از توصیه‌های بنیادین در باب
تقوا، عدالت، رحمت، رعایت حق، رسیدگی به طبقات ضعیف، توجه به رضایت عمومی و پرهیز از خودکامگی
را در بر دارد.
🔹
در این متن شریف، نگاه به مردم بر پایه کرامت انسانی و مسئولیت‌پذیری استوار شده است؛
آنجا که می‌فرماید:
«مردم دو دسته‌اند؛ یا برادر دینی تو هستند، یا همانند تو در آفرینش.»
🔹
در این نگاه، اداره امور با
عدالت، میانه‌روی در حق، دقت در رسیدگی، توجه به ضعفا و حفظ حرمت مردم
معنا پیدا می‌کند.
🔹
همچنین تأکید می‌شود که
رضایت عمومی
، اصلی اساسی در پایداری و سلامت جامعه است.
🔹
نامه ۵۳ نهج‌البلاغه، صرفاً یک متن تاریخی نیست؛ بلکه معیاری روشن برای فهم نسبت میان
قدرت، مسئولیت، عدالت و حقوق مردم
است.
🔹
بازخوانی این نامه، بازخوانی اصولی است که هر جامعه برای استقرار انصاف، آرامش و اعتماد عمومی به آن نیازمند است.
وَاللَّهُ الْمُسْتَعَانُ عَلَى كُلِّ شَيْءٍ
وَ لَا قُوَّةَ إِلَّا بِاللَّهِ
#حکمت_علوی
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/akhbarefori/655841" target="_blank">📅 20:35 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655840">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xsi32tIKgcG-JdR-rM9n6_5VXMUqDhq1DA8X2ADzhXCivBLJuLZZESkNX4Fb2w9a066wzzliECrAfrLGEFXw_sD1GS6YEzgkbdHk5k5gRd2mcrgiUYYXRMBdqqO0ksUK5yDhogPF4xE5u_CyElOwMbUJaNrAI50bWz_RSIrLMtLe4u-bgVaOr372rLRTlfmnuNseCDow2jnWny95_41gfxpC5AwhtwgeBBnsCUX3g7hOf307qxlFloOwFqM27OKdguPgOpV1BDGxjPZR5hLQWSkJSqvZLI_QzPeqUFJGFWSv6kAVgMqXgYBczYvwOvM7ZJrm1rwYlUxTbhR9ycE-iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غدیر یعنی سپردنِ تمامِ نشدن‌ها به کسی که براش هیچ بن‌بستی وجود نداره
#حیدر
#VoiceOfAli
توییتر خبرفوری را دنبال کنید
👇🏻
https://x.com/Akhbare_Fori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/655840" target="_blank">📅 20:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655839">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">♦️
قالیباف: دوران تهدید بی هزینه به پایان رسیده است/ امام‌ به ما آموخت در برابر زورگویی عقب‌نشینی نکنیم
‌
رئیس مجلس در پیامی به مناسبت ۱۴ خرداد سالروز ارتحال امام راحل تاکید کرد:
🔹
امام خمینی(ره) به ملت ایران آموخت که در برابر زورگویی و سلطه‌طلبی عقب‌نشینی نکند و امروز ملت ایران با الهام از همان مکتب، در نبرد با آمریکا و رژیم صهیونیستی نشان داد که دوران تهدید بی‌هزینه ایران به پایان رسیده و هر تجاوزی با پاسخی قاطع، پشیمان‌کننده و متناسب مواجه خواهد شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/akhbarefori/655839" target="_blank">📅 20:21 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655837">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r3fCdyAE6t6v4T6Hl0XOF4w5lIjKEiaKXN-aSGJtcgyhFR6913vAIuQs4HPisp7R0uEy8AxVh9B7I1P8iGSuF_S_x9Kr1puyf2gW8nTJAHBDIc35MNnJasv_5-W2Y9yJD26o3szvYyI-7hobJx-Qtj4yqLCo12mhh-gNq7Ls3xvsYbQQ_Sht97V3q7Ev75jCOE9cPvK7M1bmSiIi8YE3Gm6gqpyh4MGNARPYyADO_eTROdls9fR38nc9HpTFo3vwZhvG7Ow_tO9jn9xVXadcqmwUm-j3tsoUe6TLb380hSjb_jp3kty3FZXP1Gmp5JccT5BcwmFeXE6pOkwAFDrRGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vr4xFVcSyNdvhHvNnZTaVPdbMDTlin7tSGBN0_rMZoCOgpGbmaYUjXOKivpZo09Csco8gn9S_S8aGAHRc_odYe1Eht-VGlq9C7iXwhhPP_zbUb1L4WUSuHYBKNVSkrx6ws62Njs__GNs6hHdynx-Jiup_THDpkDNHRHBikEvvLbA59q8Bwc5jA3TtC8zKmkWS88ljV8Plj6b3U5Zkcd5YrDC-HfxALpiD08DcPqfUPQY88SCCe_BsaL7QDPx4DvZ-m_PZR18WqOlVv2fnngX5Jduk5IR5dXs4N5lwZ08e_9gIFD4mznceo06L4Oyz9T8auC5RXVD7_I_9wDBQgwTJg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📚
نام کتاب: علی از زبان علی
🖋
نویسنده: محمد محمدیان
🔹
شاهکاری مستند که نگارش آن بالغ بر ده سال زمان برده است و زندگانی امیرالمؤمنین را از ولادت تا شهادت، تنها با تکیه بر سخنان خود ایشان روایت می‌کند؛ سفری عمیق و اول‌شخص به قلب تاریخ، عدالت و مظلومیت فاتح خیبر.
🔹
«علی از زبان علی» دعوتی است برای شنیدن علی(ع) از زبان خود او.
#فوری_کتاب
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/akhbarefori/655837" target="_blank">📅 20:19 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655836">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
ادعای گروسی: ذخایر اورانیوم غنی شده ایران همچنان در همان محل پیشین قرار دارد، اما دسترسی به آن به دلیل خسارت‌های فیزیکی دشوار است
🔹
ذخایر یاد شده «به شکل گاز در سیلندرها» نگهداری می‌شوند و رسیدگی یا جابه‌جایی آن‌ها بسیار دشوار است، اما غیر ممکن نیست
🔹
برخی کشورها برای میزبانی از این مواد اعلام آمادگی کرده‌اند‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/655836" target="_blank">📅 20:12 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655835">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iGNlB1t8yNjaEW5oxiT3dW49lCQnpJRe6fj3qt-65q50dVNnLhqjj4HURRL2s5JLNrhE3_ISpgnvUvadok9eQRWwmR96GNxgx8viX81qZ4X2k1-s-Ea29oR7gBSQhuPvhn3slZ03PGt7TbbMnqkRXdlxOtR29UtwbP3GFeUQkRi6EUuOHJzG05Hr2bUuEdAGcSqxjtv0nXiUxSQg-NQ63_89N2oMsuSF3ADJkDn-gTx2YO2Ck3oL7uD0J9qJbPps4Bu3XG68PH90SyUxFg4l4TUar5ev0aU3UG70dIVUiffm1KGrH-CbgKAZpb3tN9g_Nk6NJ4kMCdKxphpUr5FaJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خروس‌ها در سودای سومین ستاره | فرانسه آماده فتح جهان | چرا فرانسه مدعی شماره یک جام جهانی است؟
🔹
تیم ملی فوتبال فرانسه بار دیگر با نسلی پرستاره و ترکیبی از تجربه و جوانی، یکی از اصلی‌ترین مدعیان جام جهانی ۲۰۲۶ به شمار می‌رود. فرانسوی‌ها که در دو دوره اخیر جام جهانی یک قهرمانی و یک نایب‌قهرمانی به دست آورده‌اند، حالا با هدایت دیدیه دشان به دنبال ثبت افتخاری تاریخی هستند؛ حضوری در سومین فینال متوالی جام جهانی.
در خبرفوری بخوانید و ببینید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3218944</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/akhbarefori/655835" target="_blank">📅 20:10 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655834">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/914771dc29.mp4?token=mDyKlTnz1lSRHrhBlY5HuYfgX4KPL7yy4Umg-6RhIS7twTtobKoiMk-0fiXh4RYL0YCvLN8I7HR2xMn4WhSos_PmaaZ-9ihu641dDKG-LmKdqUDnORKu4oWq-SdIaURkz4O-qVNy6aZpF6U6iIAxVkj30E6xNvN3V5RDLWXF51nmFw-yM484uan96n8X-oA1EuPBk3kuz0RHxxE_2j29RT7YQBpqACiGfrebiNIt6b7u59OciDIUKgcpC8-CyKBtg9s7Ei7sC873TGqXJvtJd4z2WHcHsKJLngc3t9gTb3lHeSqcZDvoOA099ww0Lxyuj6MX5se5ogu1As2kQoiCRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/914771dc29.mp4?token=mDyKlTnz1lSRHrhBlY5HuYfgX4KPL7yy4Umg-6RhIS7twTtobKoiMk-0fiXh4RYL0YCvLN8I7HR2xMn4WhSos_PmaaZ-9ihu641dDKG-LmKdqUDnORKu4oWq-SdIaURkz4O-qVNy6aZpF6U6iIAxVkj30E6xNvN3V5RDLWXF51nmFw-yM484uan96n8X-oA1EuPBk3kuz0RHxxE_2j29RT7YQBpqACiGfrebiNIt6b7u59OciDIUKgcpC8-CyKBtg9s7Ei7sC873TGqXJvtJd4z2WHcHsKJLngc3t9gTb3lHeSqcZDvoOA099ww0Lxyuj6MX5se5ogu1As2kQoiCRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فیلم چرت زدن ترامپ،مارکو روبیو را رسوا کرد
🔹
مارکو روبیو، وزیر خارجه دولت تروریستی آمریکا در جلسه استماع سنا مدعی شد: هرگز ندیده‌ام  ترامپ به خواب برود.
🔹
اندکی بعد تد لیئو، نماینده دموکرات: من به شما فیلم کوتاه نشان خواهم داد که اثبات می‌کند دقیقاً به کنگره دروغ گفتید.
🔹
این ویدیویی است که در آن دونالد ترامپ در حالی که شما صحبت می‌کنید، واقعاً خوابیده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655834" target="_blank">📅 20:07 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655833">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YwM0W0XyIumR3G1dys5hyNrLS6a6YsEh6rg__ZKDhtBjo4AED8HBbXqC8lwsvQpgSOYCofGSIyX8RcQsknhrXqf25JkoPJKuToQH7wHi9b6T00XuqUeS6oNeRBo5D8icTTBQuEEuy8COOgKSCzsfVqakkmzGrqYt209MajgsvSpFse0Fh_475EfGROCKzgtFAeqQxjpVm7iSchKlu5dGgaFVrdhxyjvtFiqNjljfvYtZP69pMZJCGEgIjseYFtL4vYzYXg2x2fWklaYhfx8dkbdMUNLyddmMlp3j3NUerjLM_dZN7S776fJT5A3-oizfOx3gIItVTpLA9MO2bDTJSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بمب گوگل ترکید؛ شگفتانه باورنکردنی هوش مصنوعی!
🔹
گوگل از مدل جدید هوش مصنوعی خود با نام Gemini Omni رونمایی کرد، ابزاری که فراتر از یک چت‌بات عمل می‌کند. این سامانه قادر است همزمان متن، عکس، صدا و ویدیو را درک کرده و خروجی ویدیویی تولید کند.
🔹
از جمله قابلیت‌های آن می‌توان به تبدیل متن و عکس به ویدیو، درک فیزیک و نور، ویرایش ویدیو با تایپ، ترکیب رسانه‌های مختلف و حفظ پیوستگی شخصیت‌ها اشاره کرد. به بیان ساده، کاربر با یک استودیوی تمام‌عیار تولید محتوا گفتگو می‌کند./ خبرفوری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/655833" target="_blank">📅 20:06 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655832">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a97ba8ff0.mp4?token=PfY0JgP4oIUx6r7w_oWWw17VNuAQfdYLzV5ZP5i3-L0Plp1MHr_glDx2iBSVDhUqH4j200Pp7Sn_vmhyovh6y4PXunzE1WSPCWJxWVcgwH8kR0NodO3PjeZsP8T0sMzZApm2KVVhWYw1wKCWdk8B_InpNJIWJmrJfE-Um4Z6eOMh814t9Pg_Ohq-I4FcB7sp79KCmsP_TWMTx2ZsjttCFuzf4sUBwIt62o3oRHI-P6csteJXyZNKT-wvJFBrrG0kiXAfqIyhoTdcU3PQ94VtSiXYj23zi3Skj42-PzjFVuVSlAcyl30v5sQU1KHsS7pTwyiu2aSJObTjKsHaUG6V-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a97ba8ff0.mp4?token=PfY0JgP4oIUx6r7w_oWWw17VNuAQfdYLzV5ZP5i3-L0Plp1MHr_glDx2iBSVDhUqH4j200Pp7Sn_vmhyovh6y4PXunzE1WSPCWJxWVcgwH8kR0NodO3PjeZsP8T0sMzZApm2KVVhWYw1wKCWdk8B_InpNJIWJmrJfE-Um4Z6eOMh814t9Pg_Ohq-I4FcB7sp79KCmsP_TWMTx2ZsjttCFuzf4sUBwIt62o3oRHI-P6csteJXyZNKT-wvJFBrrG0kiXAfqIyhoTdcU3PQ94VtSiXYj23zi3Skj42-PzjFVuVSlAcyl30v5sQU1KHsS7pTwyiu2aSJObTjKsHaUG6V-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی علی؛ تو به ولله تمام منی
❤️
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/akhbarefori/655832" target="_blank">📅 20:02 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655831">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
پیام تبریک پزشکیان بمناسبت فرارسیدن عید سعید غدیر
‌
🔹
عید غدیر، فصل باران حقیقت بر شوره‌زار مسیر تاریخ است ،غدیر تراز جاودانه حکمرانی مبتنی بر عدالت و کرامت انسانی است.
🔹
برای عبور از تنگناها باید به صداقت علوی و عدالت غدیری بازگردیم.
🔹
این‌جانب ضمن گرامی‌داشت یاد و خاطره بنیان‌گذار فقید انقلاب و بزرگ‌داشت رهبر عظیم‌الشأن شهیدمان، این عید بزرگ و میثاق مبین را به محضر یکایک آزادگان جهان و دوست‌داران و شیعیان آن امام همام تبریک و تهنیت می‌گویم
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/akhbarefori/655831" target="_blank">📅 19:49 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655829">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NgXFF9N88t1vSTNIclPPqHaIWEfkgBiNJ8o4olwwiPiThp1VFrrd4k_JReefNy3mKB5riJrdXV3kMAEZVwPfof5e82jhaQQmUKCaawgnbVUnTlIvhD6eGRqx_0etuNJyQHgxY1BF294FUnDQz-2wT9UesHGrrw0puxNi63vz9KAcowhtxRAskyNoOc618A6N7pntfSOwrHzfrspAa3ksiyG6DH-suBu--DtyenNunG1eSv3BCdj056u4miq8gHgVv35GOj8R9pU4Kt0El2NYaUNqiNI0rmxNiyRyyxPTfLraqGaWCJYF3Daebpw9vZtDjM5NGBlH5jxnvY-UnaYZ7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
کشف و ضبط محموله‌ تجهیزات خرابکارانه از شبکه بزرگ خرابکاری، انتقال اقلام نظامی گروهک‌های تروریستی تجزیه طلب
قرارگاه حمزه سید الشهدا (ع) نیروی زمینی سپاه:
🔹
گروهک های تروریستی تجزیه طلب با هماهنگی و هدایت سرویس های جاسوسی استکبار جهانی، قصد داشتند تجهیزاتی را جهت اقدامات خرابکارانه به داخل کشور منتقل نمایند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655829" target="_blank">📅 19:45 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655828">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بهزیستی در پرونده قتل مهسا شاکی است / بسیاری از مقامات از بهزیستی فرزند می‌خواهند ولی نمی‌دهیم / دلیلی ندارد کودکی را از خانواده‌ای که به آن اُنس گرفته جدا کنیم
رئیس سازمان بهزیستی کشور در
#گفتگو
با خبرفوری:
🔹
در پرونده قتل مهسا هم پدر زیستی او و هم بهزیستی شاکی است. بخشی از این پرونده اداری است که شما دیدید من برخورد کردم و برخوردم را رسانه ای کردم و همکارانم را از سمتشان برکنار کردم. بخشی دیگر نیز قضایی است و الان همکاری کامل با قاضی پرونده داریم
🔹
بسیار پیش می آید که مقامات در سطح استاندار، وزیر، نماینده مجلس و... از من تقاضای فرزند می کنند اما تنها جایی که علیرغم همه احترامی که برایشان قائلم، به سادگی پاسخشان را نمی‌دهم، فرزندخواندگی است. به خاطر اینکه آنها هم حتما باید از نظر کارشناسی تایید شوند
🔹
بچه ای که با خانواده ای انس گرفته، نباید از خانواده گسسته شود و ما هم تا جایی که قانون اجازه می دهد، نمی گذاریم این اتفاق بیفتد ولی در برخی موارد از دست ما خارج است و کاری نمی توانیم انجام دهیم.
گفتگوی مریم محمدپور با سیدجواد حسینی را اینجا ببینید و بخوانید
👇
khabarfoori.com/fa/tiny/news-3219779</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/akhbarefori/655828" target="_blank">📅 19:39 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655825">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LZ4s_Yrq8V9WdDKKooUzKjchMuMI4cfZUO8z102YEqKyrAL8bfDA1_UKOKa_U6M6ejA8ZSikV6D-B7SNhpAgQKzFlBLvz8jYSWzvk59t_sFUMVxHWTkuDSYAYWzQgRVBL3p2--cYClhI48qSfAmLRjqBFsz8wYGw2P3PmoMXPiEZAJ_i0fnM5bITEQIZF85y8HgiB0x27A5M8ZXunA1WWqAL_xzyCOX6pUV0vKERcGTu3tTFS20kU-g4Z1EuMQyf-A3ooJW8vf_NoZqbfSl1gwACnExOEM1XczODRsth2cPGWhkqSWgA0MRkCAcaFz-DBAb10KJwcuZtJhqVm5lYoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سند زنانه غدیر، روایتی که از دستان فاطمه‌ها گذشت
🔹
روایت غدیر از کم‌نظیرترین روایات اسلامی است؛ زیرا در سندی از این روایت، تمام راویان آن زنانی از خاندان پیامبر(ص) هستند. بیشتر آنان «فاطمه» نام دارند و هر راوی، روایت را از عمه خود نقل کرده است.
🔹
اهمیت دیگر این حدیث، نقل آن در منابع معتبر اهل سنت و تأکید آن بر دو حدیث بنیادین «غدیر» و «منزلت» است که جایگاه امیرالمؤمنین(ع) را تبیین می‌کنند.
#جرعه‌ای_از_خم
#فقط_به_عشق_علی
#LiveLikeAli
#VoiceOfAli
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/akhbarefori/655825" target="_blank">📅 19:30 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655824">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
اطلاعیه شماره ۱ ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه
بسم الله الرّحمن الرّحیم
🔹
با تبریک عید سعید غدیرخم و گرامیداشت سی‌وهفتمین سالگرد رحلت جانگداز بنیان‌گذار جمهوری اسلامی ایران حضرت امام خمینی رحمةالله‌علیه، به‌اطلاع ملّت بزرگ ایران، آزادگان جهان و علاقه‌مندان به رهبر شهید انقلاب اسلامی حضرت آیت‌الله‌العظمی سیّدعلی حسینی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه می‌رساند، برنامه‌ریزی‌های لازم برای برگزاری باشکوه مراسم وداع، تشییع و تدفین امام مجاهد شهیدمان توسط دستگاه‌های مسئول و گروه‌های مردمی، در حال پیگیری است؛ لذا شایعات و برخی گمانه‌زنی‌های رسانه‌ای درباره‌ی جزئیات این رویداد فاقد اعتبار است.
🔹
برنامه‌ها، اقدامات رسانه‌ای و جزئیات این رویداد عظیم در اطلاعیه‌های بعدی ستاد بزرگداشت عروج خونین امام مجاهد شهید حضرت آیت‌الله‌العظمی خامنه‌ای‌ قدّس‌الله‌نفسه‌الزکیه اعلام خواهدشد. ان‌شاء‌الله.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/akhbarefori/655824" target="_blank">📅 19:26 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655823">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
ادعای رئیس ستاد ارتش اسرائیل: آماده‌ایم فوراً به نبرد علیه ایران بازگردیم
🔹
نیروی دریایی نقش تعیین‌کننده‌ای در هرگونه رویارویی نظامی جدید با ایران خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/akhbarefori/655823" target="_blank">📅 19:20 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655822">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
بازداشت ۱۵ شهروند بحرینی توسط حکومت دست نشانده آل خلیفه
🔹
وزارت کشور حکومت آل خلیفه در ادامه خوش رقصی برای عناصر آمریکایی صهیونیستی، ۱۵ شهروند خود را به اتهام آنچه ارتباط با ایران خوانده است، به طرز وحشیانه‌ای بازداشت کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/akhbarefori/655822" target="_blank">📅 19:17 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655821">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
گزارش تحقیقی نیویورک تایمز از جنایت آمریکا در شهر لامرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/akhbarefori/655821" target="_blank">📅 19:15 · 13 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-655820">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BLsZa8ZNEjXQNECmgfpc1yZw0XEMBStaZ1kH8h4pKh6P7a5-5MejTZNvGDz4z_h-zTGy-RpOMe3StqufenByRCWU56HXAuoIXu5YRwLqWEM76K_iYDTxuEWNiAxerVub5zWcJGrTTFW9h8jglb6A3_8W3kKkRzJuH5JFr9HISvCs__Flks1j0NKPHCG0rDdc76nA0M0audVAdXqWAsSZaouCy80APFtuOVld388uLU_FZCGGHA9HBtbXcFbTuX0roviQPCzwa9RcUY3zNajhhoiNy6Q1UjESvM3czKIbcOWfVAvoCUQxoODFiTypFg478dhMyDWZQteOBgDzm7B2bA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قاطع وزیر امور خارجه کشورمان/ هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد
🔹
نیروهای مسلح ما در حال انجام حملات دفاعی در چارچوب حق مشروع دفاع از خود علیه مکان‌هایی هستند که از آنجا به ایالات متحده اجازه داده می‌شود برای حمله به کشتی‌رانی غیرنظامی و نقض آتش‌بس استفاده کند.
🔹
هرگونه اقدام خصمانه با پاسخی فوری و قاطع مواجه خواهد شد. آنچه تحریم‌ها و جنگ نتوانستند به آن دست یابند، با جنگ بیشتر نیز به دست نخواهد آمد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/akhbarefori/655820" target="_blank">📅 19:12 · 13 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
